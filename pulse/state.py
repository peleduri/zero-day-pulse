"""Run-to-run state and the "what changed" diff (design §5).

``state/last_run.json`` is a rolling 14-day watchlist of every CVE seen recently,
tracked individually::

    {stack_terms_hash, generated_at, run_id,
     cves: {CVE: {first_seen, last_seen, in_kev, epss, stack_match, stack_terms_hash}}}

Each run re-checks the whole watchlist against the fresh KEV catalog and EPSS
scores and emits only changes:

* ``entered_kev``   — a watched CVE stored ``in_kev=false`` is now in KEV.
* ``epss_crossed``  — a watched CVE's EPSS went from below 0.1 (or 0.5) to at or
                      above it; the highest threshold crossed is reported.
* ``new_stack_hit`` — a CVE's stack match went from empty to non-empty under the
                      same ``my_stack`` terms; a first-seen CVE that matches emits.

Fetch failures (``kev_lookup``/``epss`` is ``None``) keep the stored values and
emit nothing for that source. No state file means the whole run is a baseline.
Nothing here is fatal: a corrupt state file is logged and treated as missing.
"""
import hashlib
import json
import logging
import os
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

from pulse.urls import safe_url

logger = logging.getLogger(__name__)

DEFAULT_STATE_PATH = "state/last_run.json"
STATE_PATH_ENV = "PULSE_STATE_PATH"
WATCH_DAYS = 14
WATCH_CAP = 1000
EPSS_THRESHOLDS = (0.1, 0.5)
KIND_ORDER = {"entered_kev": 0, "epss_crossed": 1, "new_stack_hit": 2}

_CVE_ID_RE = re.compile(r"^CVE-\d{4}-\d{4,}$")


def state_path(path: Optional[str] = None) -> str:
    """Explicit path, else ``$PULSE_STATE_PATH``, else ``state/last_run.json``."""
    return path or os.environ.get(STATE_PATH_ENV) or DEFAULT_STATE_PATH


def current_run_id() -> str:
    """GitHub Actions run id (``$GITHUB_RUN_ID``), or "local" outside Actions."""
    return os.environ.get("GITHUB_RUN_ID") or "local"


def stack_terms_hash(terms: Optional[Iterable[str]]) -> str:
    """Order-, case- and duplicate-insensitive hash of the ``my_stack`` terms."""
    norm = sorted({str(t).strip().lower() for t in (terms or []) if str(t).strip()})
    return hashlib.sha256(json.dumps(norm).encode("utf-8")).hexdigest()


# ── load / save ───────────────────────────────────────────────────────────────

def _num(v) -> Optional[float]:
    if isinstance(v, bool) or not isinstance(v, (int, float)):
        return None
    return float(v)


def _clean_entry(raw: Dict) -> Dict:
    sm = raw.get("stack_match")
    in_kev = raw.get("in_kev")
    return {
        "first_seen":       str(raw.get("first_seen") or ""),
        "last_seen":        str(raw.get("last_seen") or raw.get("first_seen") or ""),
        "in_kev":           in_kev if isinstance(in_kev, bool) else None,
        "epss":             _num(raw.get("epss")),
        "stack_match":      [str(t) for t in sm] if isinstance(sm, list) else [],
        "stack_terms_hash": raw.get("stack_terms_hash") if isinstance(raw.get("stack_terms_hash"), str) else None,
    }


def load_state(path: Optional[str] = None) -> Optional[Dict]:
    """Load the state file. ``None`` (baseline run) if missing or corrupt — never raises."""
    p = Path(state_path(path))
    if not p.exists():
        logger.info(f"[state] no state file at {p} — this run is a baseline")
        return None
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or not isinstance(data.get("cves"), dict):
            raise ValueError("expected an object with a 'cves' object")
    except Exception as e:
        logger.warning(f"[state] corrupt state file {p} ({e}) — treating this run as a baseline")
        return None
    cves = {}
    for cve, raw in data["cves"].items():
        cve = str(cve).strip().upper()
        if _CVE_ID_RE.match(cve) and isinstance(raw, dict):
            cves[cve] = _clean_entry(raw)
    return {
        "stack_terms_hash": data.get("stack_terms_hash") if isinstance(data.get("stack_terms_hash"), str) else None,
        "generated_at":     data.get("generated_at"),
        "run_id":           data.get("run_id"),
        "cves":             cves,
    }


def save_state(state: Dict, path: Optional[str] = None) -> str:
    """Write the state atomically (temp file + rename). Returns the path written."""
    p = Path(state_path(path))
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_name(p.name + ".tmp")
    tmp.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(tmp, p)
    logger.info(f"[state] saved {len(state.get('cves', {}))} watched CVEs → {p}")
    return str(p)


def watched_cves(state: Optional[Dict]) -> List[str]:
    return sorted((state or {}).get("cves", {}))


# ── diff ──────────────────────────────────────────────────────────────────────

def _current_by_cve(findings: List[Dict]) -> Dict[str, Dict]:
    """Per-CVE view of this run: first (highest-sorted) citing finding + union of stack matches."""
    out: Dict[str, Dict] = {}
    for f in findings:
        sm = f.get("stack_match") if isinstance(f.get("stack_match"), list) else []
        for cve in f.get("cve_ids") or []:
            cve = str(cve).strip().upper()
            if not _CVE_ID_RE.match(cve):
                continue
            cur = out.setdefault(cve, {"finding": f, "stack_match": []})
            for t in sm:
                if t not in cur["stack_match"]:
                    cur["stack_match"].append(str(t))
    return out


def _context(cur: Optional[Dict]) -> Dict:
    f = (cur or {}).get("finding") or {}
    return {"title": f.get("title") or None, "link": safe_url(f.get("link")) or None}


def _crossed(old: Optional[float], new: Optional[float]) -> Optional[float]:
    if old is None or new is None:
        return None
    hit = [t for t in EPSS_THRESHOLDS if old < t <= new]
    return max(hit) if hit else None


def _parse_ts(s: str) -> Optional[datetime]:
    try:
        dt = datetime.fromisoformat(s)
    except (TypeError, ValueError):
        return None
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def prune(cves: Dict[str, Dict], now: datetime,
          days: int = WATCH_DAYS, cap: int = WATCH_CAP) -> Dict[str, Dict]:
    """Drop CVEs not seen for ``days`` (or with unreadable dates), then keep the
    ``cap`` with the newest ``first_seen`` (oldest pruned first)."""
    cutoff = now - timedelta(days=days)
    kept = {}
    for cve, e in cves.items():
        seen = _parse_ts(e.get("last_seen") or e.get("first_seen") or "")
        if seen is not None and seen >= cutoff:
            kept[cve] = e
    if len(kept) > cap:
        order = sorted(kept, key=lambda c: (_parse_ts(kept[c]["first_seen"]) or cutoff, c), reverse=True)
        kept = {c: kept[c] for c in order[:cap]}
    return kept


def diff_state(state: Optional[Dict], findings: List[Dict], kev_lookup: Optional[Dict],
               epss: Optional[Dict], stack_terms: Optional[List[str]],
               now: Optional[datetime] = None,
               run_id: Optional[str] = None) -> Tuple[Dict, List[Dict]]:
    """Compare this run against ``state``. Returns ``(new_state, changes)``.

    ``kev_lookup`` / ``epss`` of ``None`` mean that fetch failed: stored values
    are kept and no change of that kind is emitted.
    """
    now = now or datetime.now(timezone.utc)
    now_s = now.isoformat()
    cur_hash = stack_terms_hash(stack_terms)
    baseline = state is None
    stored: Dict[str, Dict] = (state or {}).get("cves", {})
    # A my_stack edit re-baselines every stack match this run (no new_stack_hit at all).
    stack_alerts = bool(stack_terms) and not baseline and (state or {}).get("stack_terms_hash") == cur_hash
    current = _current_by_cve(findings)

    new_cves: Dict[str, Dict] = {}
    changes: List[Dict] = []
    for cve in sorted(set(stored) | set(current)):
        old = stored.get(cve)
        cur = current.get(cve)
        watched = old is not None and not baseline

        # ── KEV ──
        if kev_lookup is None:
            in_kev = old["in_kev"] if old else None
        else:
            in_kev = cve in kev_lookup
            if watched and old["in_kev"] is False and in_kev:
                k = kev_lookup[cve]
                changes.append({"kind": "entered_kev", "cve": cve, **_context(cur),
                                "kev_date_added": k.get("date_added") or None,
                                "kev_due_date": k.get("due_date") or None,
                                "kev_ransomware": bool(k.get("ransomware"))})

        # ── EPSS ── (FIRST having no score for a CVE keeps the stored value)
        old_epss = old["epss"] if old else None
        if epss is None or cve not in epss:
            new_epss = old_epss
        else:
            new_epss = _num(epss[cve].get("epss"))
            t = _crossed(old_epss, new_epss) if watched else None
            if t is not None:
                changes.append({"kind": "epss_crossed", "cve": cve, **_context(cur),
                                "threshold": t, "old_epss": old_epss, "new_epss": new_epss})

        # ── stack ── (absent CVEs keep their stored match and hash)
        if cur is None:
            sm, sm_hash = old["stack_match"], old["stack_terms_hash"]
        else:
            sm, sm_hash = cur["stack_match"], cur_hash
            if stack_alerts and sm:
                first_seen = old is None
                gained = old is not None and not old["stack_match"] and old["stack_terms_hash"] == cur_hash
                if first_seen or gained:
                    changes.append({"kind": "new_stack_hit", "cve": cve, **_context(cur),
                                    "stack_match": list(sm)})

        new_cves[cve] = {
            "first_seen":       old["first_seen"] if old and old["first_seen"] else now_s,
            "last_seen":        now_s if cur is not None else (old["last_seen"] if old else now_s),
            "in_kev":           in_kev,
            "epss":             new_epss,
            "stack_match":      list(sm),
            "stack_terms_hash": sm_hash,
        }

    changes.sort(key=lambda c: (KIND_ORDER[c["kind"]], c["cve"]))
    new_state = {
        "stack_terms_hash": cur_hash,
        "generated_at":     now_s,
        "run_id":           run_id or current_run_id(),
        "cves":             prune(new_cves, now),
    }
    if baseline:
        logger.info(f"[state] baseline run: {len(new_state['cves'])} CVEs watched, no changes emitted")
    else:
        logger.info(f"[state] {len(changes)} change(s); watching {len(new_state['cves'])} CVEs")
    return new_state, changes
