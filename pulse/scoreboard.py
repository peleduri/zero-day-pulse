""""Beat KEV" lead-time scoreboard (design/beat-kev-scoreboard.md).

Measures one claim: how often, and by how many days, Zero Day Pulse sees a CVE
being exploited before CISA adds it to the KEV catalog.

Two state files, both committed by the workflow:

* ``state/first_signal.json`` -- CVE -> ``{observed_at, published, source, link}``,
  written only the FIRST time a CVE gets a signal (see :func:`is_signal_entry`).
  Kept for 180 days, capped at 5000 entries, oldest ``observed_at`` pruned first.
  A signal pruned before its CVE reaches KEV is gone: that CVE's row counts as
  **missed** (KEV usually lists within weeks, so this is rare by design).
* ``state/kev_scoreboard.jsonl`` -- line 1 is a ``{"go_live": "YYYY-MM-DD"}``
  header (no ``cve`` key); every other line is one write-once row per KEV
  addition with ``dateAdded >= go_live``::

      {cve, kev_date_added, vendor, product, cve_year, observed_at, source,
       link, lead_days, bucket}

Buckets: ``earlier`` (lead_days >= 1), ``same_day_or_late`` (a signal exists,
lead_days <= 0) and ``missed`` (no signal). A zero-day reported before a CVE ID
exists can never be matched, so it counts as missed.

Nothing here may crash the pipeline: every public entry point logs and returns.
"""
import json
import logging
import os
import re
import statistics
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

from pulse.filter import _load_keywords, _matches_any
from pulse.urls import safe_url

logger = logging.getLogger(__name__)

DEFAULT_SIGNALS_PATH = "state/first_signal.json"
SIGNALS_PATH_ENV = "PULSE_SIGNALS_PATH"
DEFAULT_SCOREBOARD_PATH = "state/kev_scoreboard.jsonl"
SCOREBOARD_PATH_ENV = "PULSE_SCOREBOARD_PATH"

SIGNAL_DAYS = 180
SIGNAL_CAP = 5000
MAX_SIGNAL_CVES = 2       # a round-up citing more CVEs gives no signal at all
WARMUP_DAYS = 14
WINDOWS = (30, 90)
MIN_COUNTED = 10          # below this, a window shows "collecting data since"
TOP_LEADS = 5
TOP_LEADS_WINDOW = 90

BUCKETS = ("earlier", "same_day_or_late", "missed")

# Edge population: KEV ``vendorProject`` is matched case-insensitively, ignoring
# spaces and punctuation, as a PREFIX of these names -- so "Juniper Networks",
# "Citrix Systems", "Palo Alto Networks", "Check Point" / "CheckPoint",
# "F5 Networks", "SonicWall", "Fortinet, Inc." all count.
EDGE_VENDORS = ("Fortinet", "Ivanti", "Cisco", "Palo Alto Networks", "Citrix",
                "SonicWall", "Check Point", "F5", "Juniper")
# Prefixes actually compared (normalized); "Palo Alto" alone is enough.
_EDGE_PREFIXES = ("fortinet", "ivanti", "cisco", "paloalto", "citrix",
                  "sonicwall", "checkpoint", "f5", "juniper")

CAVEAT = "Zero-days reported before a CVE ID exists can't be matched and count as missed."

_CVE_ID_RE = re.compile(r"^CVE-(\d{4})-\d{4,}$")


def _utcnow() -> datetime:
    """The run time (``observed_at``); a function so tests can move the clock."""
    return datetime.now(timezone.utc)


# ── paths ─────────────────────────────────────────────────────────────────────

def signals_path(path: Optional[str] = None) -> str:
    """Explicit path, else ``$PULSE_SIGNALS_PATH``, else ``state/first_signal.json``."""
    return path or os.environ.get(SIGNALS_PATH_ENV) or DEFAULT_SIGNALS_PATH


def scoreboard_path(path: Optional[str] = None) -> str:
    """Explicit path, else ``$PULSE_SCOREBOARD_PATH``, else ``state/kev_scoreboard.jsonl``."""
    return path or os.environ.get(SCOREBOARD_PATH_ENV) or DEFAULT_SCOREBOARD_PATH


# ── small helpers ─────────────────────────────────────────────────────────────

def _norm_cve(c) -> Optional[str]:
    c = str(c or "").strip().upper()
    return c if _CVE_ID_RE.match(c) else None


def _parse_ts(s) -> Optional[datetime]:
    if not isinstance(s, str) or not s:
        return None
    try:
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def _parse_day(s) -> Optional[date]:
    """KEV ``dateAdded`` / header dates: ``YYYY-MM-DD`` (anything after is ignored)."""
    if not isinstance(s, str):
        return None
    try:
        return date.fromisoformat(s.strip()[:10])
    except ValueError:
        return None


def _atomic_write(p: Path, text: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_name(p.name + ".tmp")   # state/*.tmp is gitignored
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, p)


def is_edge_vendor(vendor) -> bool:
    """True if a KEV ``vendorProject`` belongs to the Edge population."""
    norm = re.sub(r"[^a-z0-9]", "", str(vendor or "").lower())
    return bool(norm) and norm.startswith(_EDGE_PREFIXES)


# ── signals ───────────────────────────────────────────────────────────────────

def is_signal_entry(entry: Dict, zd_keywords: List[str]) -> bool:
    """Entry-level part of the signal test (design decision 1).

    Uses ONLY the zero-day keyword match on the entry's own title + summary and
    the CVE count. Never ``in_kev`` / ``is_zero_day`` (``is_zero_day`` is true
    for any KEV CVE, which would make KEV its own early warning). KEV-feed
    entries (``is_kev``) never qualify.
    """
    if entry.get("is_kev"):
        return False
    cves = [c for c in (_norm_cve(x) for x in entry.get("cve_ids") or []) if c]
    if not cves or len(set(cves)) > MAX_SIGNAL_CVES:
        return False
    return _matches_any(f"{entry.get('title', '')} {entry.get('summary', '')}", zd_keywords)


def collect_signals(entries: Iterable[Dict], kev_lookup: Optional[Dict],
                    zd_keywords: Optional[List[str]] = None) -> Tuple[Dict[str, Dict], int]:
    """Qualifying signals in this run's entries: ``({cve: entry}, capped_count)``.

    Run on EVERY collected entry (after ``attach_cve_ids``/``annotate_kev``,
    before ``filter_zero_days`` dedup). Per CVE, the entry with the earliest
    ``published`` wins (missing dates lose). A CVE already in this run's KEV
    lookup gets no signal; with ``kev_lookup=None`` (catalog failed) signals are
    recorded anyway -- such a CVE can only land in same_day_or_late later.
    ``capped_count`` = keyword-matching entries dropped for citing > 2 CVEs.
    """
    if zd_keywords is None:
        zd_keywords = _load_keywords()[0]
    best: Dict[str, Tuple[Tuple, Dict]] = {}
    capped = 0
    for i, e in enumerate(entries):
        if not is_signal_entry(e, zd_keywords):
            if (not e.get("is_kev") and len(e.get("cve_ids") or []) > MAX_SIGNAL_CVES
                    and _matches_any(f"{e.get('title', '')} {e.get('summary', '')}", zd_keywords)):
                capped += 1
            continue
        pub = _parse_ts(e.get("published"))
        key = (pub is None, pub or datetime.max.replace(tzinfo=timezone.utc), i)
        for cve in {c for c in (_norm_cve(x) for x in e.get("cve_ids") or []) if c}:
            if kev_lookup is not None and cve in kev_lookup:
                continue
            if cve not in best or key < best[cve][0]:
                best[cve] = (key, e)
    return {c: v[1] for c, v in best.items()}, capped


def load_signals(path: Optional[str] = None) -> Dict[str, Dict]:
    """``first_signal.json`` as a dict; missing or corrupt -> ``{}`` (warning, never raises)."""
    p = Path(signals_path(path))
    if not p.exists():
        return {}
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("expected a JSON object")
    except Exception as e:
        logger.warning(f"[scoreboard] corrupt signal file {p} ({e}) -- treating it as empty")
        return {}
    out = {}
    for cve, raw in data.items():
        cve = _norm_cve(cve)
        if cve and isinstance(raw, dict) and _parse_ts(raw.get("observed_at")):
            out[cve] = {
                "observed_at": str(raw["observed_at"]),
                "published":   raw.get("published") if isinstance(raw.get("published"), str) else None,
                "source":      str(raw.get("source") or ""),
                "link":        safe_url(raw.get("link")) or None,
            }
    return out


def prune_signals(signals: Dict[str, Dict], now: datetime,
                  days: int = SIGNAL_DAYS, cap: int = SIGNAL_CAP) -> Dict[str, Dict]:
    """Drop signals older than ``days``, then keep the ``cap`` newest ``observed_at``.
    A pruned signal whose CVE later reaches KEV makes that row ``missed``."""
    cutoff = now - timedelta(days=days)
    kept = {c: s for c, s in signals.items()
            if (_parse_ts(s.get("observed_at")) or cutoff - timedelta(1)) >= cutoff}
    if len(kept) > cap:
        order = sorted(kept, key=lambda c: (_parse_ts(kept[c]["observed_at"]), c), reverse=True)
        kept = {c: kept[c] for c in order[:cap]}
    return kept


def update_signals(signals: Dict[str, Dict], new: Dict[str, Dict], now: datetime) -> Tuple[Dict[str, Dict], int]:
    """Add first-time signals (existing CVEs are never overwritten), then prune.
    Returns ``(signals, added_count)``."""
    out = dict(signals)
    added = 0
    for cve, e in sorted(new.items()):
        if cve in out:
            continue
        pub = _parse_ts(e.get("published"))
        out[cve] = {
            "observed_at": now.isoformat(),
            "published":   pub.isoformat() if pub else None,
            "source":      str(e.get("source") or ""),
            "link":        safe_url(e.get("link")) or None,
        }
        added += 1
    return prune_signals(out, now), added


def save_signals(signals: Dict[str, Dict], path: Optional[str] = None) -> str:
    p = Path(signals_path(path))
    _atomic_write(p, json.dumps(signals, indent=2, sort_keys=True) + "\n")
    return str(p)


# ── scoreboard file ───────────────────────────────────────────────────────────

def _valid_row(r) -> bool:
    return (isinstance(r, dict) and _norm_cve(r.get("cve")) is not None
            and _parse_day(r.get("kev_date_added")) is not None
            and r.get("bucket") in BUCKETS)


def load_scoreboard(path: Optional[str] = None) -> Tuple[Optional[date], List[Dict], bool]:
    """Read the JSONL scoreboard: ``(go_live, rows, needs_rewrite)``.

    * File missing -> ``(None, [], False)``: a genuine first run.
    * Unparseable/invalid lines are skipped with a warning; for a CVE on several
      lines the first wins. Either sets ``needs_rewrite``.
    * Header missing or unparseable but valid rows exist -> go-live is rebuilt
      from the earliest ``kev_date_added`` (never reset to today) and
      ``needs_rewrite`` is set. No header and no rows -> ``(None, [], True)``.
    """
    p = Path(scoreboard_path(path))
    if not p.exists():
        return None, [], False
    lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
    go_live: Optional[date] = None
    rows: List[Dict] = []
    seen = set()
    dirty = False
    for n, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
        except ValueError:
            obj = None
        if n == 1 and isinstance(obj, dict) and "cve" not in obj and _parse_day(obj.get("go_live")):
            go_live = _parse_day(obj["go_live"])
            continue
        if not _valid_row(obj):
            logger.warning(f"[scoreboard] {p}:{n} skipped (unparseable or not a valid row)")
            dirty = True
            continue
        cve = _norm_cve(obj["cve"])
        if cve in seen:
            logger.warning(f"[scoreboard] {p}:{n} duplicate row for {cve} skipped (first wins)")
            dirty = True
            continue
        seen.add(cve)
        rows.append({**obj, "cve": cve})
    if go_live is None:
        dirty = True
        if rows:
            go_live = min(_parse_day(r["kev_date_added"]) for r in rows)
            logger.warning(f"[scoreboard] {p}: go-live header missing -- rebuilt as {go_live} "
                           f"from the earliest row")
        else:
            logger.warning(f"[scoreboard] {p}: no header and no valid rows")
    return go_live, rows, dirty


def save_scoreboard(go_live: date, rows: List[Dict], path: Optional[str] = None) -> str:
    """Rewrite the whole file atomically: header on line 1, then rows in order."""
    p = Path(scoreboard_path(path))
    out = [json.dumps({"go_live": go_live.isoformat()})]
    out += [json.dumps(r, sort_keys=True) for r in rows]
    _atomic_write(p, "\n".join(out) + "\n")
    return str(p)


def build_rows(kev_records: Optional[List[Dict]], go_live: date, existing: Iterable[str],
               signals: Dict[str, Dict]) -> List[Dict]:
    """One new row per catalog CVE with ``dateAdded >= go_live`` that has no row yet.

    Walks the WHOLE catalog (not the lookback window) so additions missed by
    earlier runs are caught up. ``kev_records=None`` (catalog failed) -> no rows.
    """
    if kev_records is None:
        return []
    have = set(existing)
    new: List[Dict] = []
    for r in kev_records:
        if not isinstance(r, dict):
            continue
        cve = _norm_cve(r.get("cveID"))
        added = _parse_day(r.get("dateAdded"))
        if not cve or added is None or added < go_live or cve in have:
            continue
        have.add(cve)
        sig = signals.get(cve)
        observed = _parse_ts(sig.get("observed_at")) if sig else None
        if observed is not None:
            lead = (added - observed.astimezone(timezone.utc).date()).days
            bucket = "earlier" if lead >= 1 else "same_day_or_late"
        else:
            lead, bucket, sig = None, "missed", None
        new.append({
            "cve":            cve,
            "kev_date_added": added.isoformat(),
            "vendor":         str(r.get("vendorProject") or ""),
            "product":        str(r.get("product") or ""),
            "cve_year":       int(_CVE_ID_RE.match(cve).group(1)),
            "observed_at":    sig["observed_at"] if sig else None,
            "source":         sig["source"] if sig else None,
            "link":           (safe_url(sig.get("link")) or None) if sig else None,
            "lead_days":      lead,
            "bucket":         bucket,
        })
    new.sort(key=lambda x: (x["kev_date_added"], x["cve"]))
    return new


# ── numbers ───────────────────────────────────────────────────────────────────

def exclusion(row: Dict, go_live: date) -> Optional[str]:
    """``"warm_up"`` (first 14 days after go-live), ``"old_cve"`` (CVE year more
    than 1 year before the KEV ``dateAdded`` year) or ``None`` (counted)."""
    added = _parse_day(row.get("kev_date_added"))
    if added is None:
        return "warm_up"
    if added < go_live + timedelta(days=WARMUP_DAYS):
        return "warm_up"
    year = row.get("cve_year")
    if not isinstance(year, int):
        m = _CVE_ID_RE.match(str(row.get("cve") or ""))
        year = int(m.group(1)) if m else added.year
    if year < added.year - 1:
        return "old_cve"
    return None


def _num(v):
    return int(v) if float(v).is_integer() else round(float(v), 1)


def _population(rows: List[Dict]) -> Dict:
    leads = [r["lead_days"] for r in rows if r["bucket"] == "earlier"]
    counted = len(rows)
    return {
        "counted":          counted,
        "earlier":          len(leads),
        "earlier_pct":      round(100.0 * len(leads) / counted, 1) if counted else None,
        "median_lead":      _num(statistics.median(leads)) if leads else None,
        "max_lead":         max(leads) if leads else None,
        "same_day_or_late": sum(1 for r in rows if r["bucket"] == "same_day_or_late"),
        "missed":           sum(1 for r in rows if r["bucket"] == "missed"),
        "collecting":       counted < MIN_COUNTED,
    }


def _in_window(row: Dict, today: date, days: int) -> bool:
    d = _parse_day(row.get("kev_date_added"))
    return d is not None and today - timedelta(days=days) < d <= today


def compute_scoreboard(rows: List[Dict], go_live: date, today: date) -> Dict:
    """The panel / ``scoreboard.json`` numbers for windows of 30 and 90 days."""
    windows = {}
    for days in WINDOWS:
        in_win = [r for r in rows if _in_window(r, today, days)]
        reasons = [exclusion(r, go_live) for r in in_win]
        counted = [r for r, why in zip(in_win, reasons) if why is None]
        windows[str(days)] = {
            "all":      _population(counted),
            "edge":     _population([r for r in counted if is_edge_vendor(r.get("vendor"))]),
            "excluded": {"warm_up": reasons.count("warm_up"), "old_cve": reasons.count("old_cve")},
        }
    earlier = [r for r in rows if r["bucket"] == "earlier" and _in_window(r, today, TOP_LEADS_WINDOW)
               and exclusion(r, go_live) is None]
    earlier.sort(key=lambda r: (-r["lead_days"], r["kev_date_added"], r["cve"]))
    return {
        "generated_at":     datetime.now(timezone.utc).isoformat(),
        "go_live":          go_live.isoformat(),
        "warmup_days":      WARMUP_DAYS,
        "min_counted":      MIN_COUNTED,
        "edge_vendors":     list(EDGE_VENDORS),
        "caveat":           CAVEAT,
        "windows":          windows,
        "top_leads_window": TOP_LEADS_WINDOW,
        "top_leads": [{k: r.get(k) for k in ("cve", "vendor", "product", "kev_date_added",
                                            "lead_days", "source", "link")}
                      for r in earlier[:TOP_LEADS]],
        "total_rows":       len(rows),
        "rows":             rows,
    }


# ── one call per run ──────────────────────────────────────────────────────────

def run_scoreboard(entries: List[Dict], kev_records: Optional[List[Dict]],
                   kev_lookup: Optional[Dict], now: Optional[datetime] = None,
                   signals_file: Optional[str] = None,
                   scoreboard_file: Optional[str] = None) -> Optional[Dict]:
    """Update signals, then scoreboard rows, then compute the numbers.

    Call with every collected entry after ``attach_cve_ids``/``annotate_kev``
    and before ``filter_zero_days``. Returns the scoreboard dict, or ``None``
    if it could not be computed. Never raises.
    """
    now = now or _utcnow()
    run_info = {"new_signals": 0, "new_rows": 0, "capped_entries": 0}

    signals: Dict[str, Dict] = {}
    try:
        found, run_info["capped_entries"] = collect_signals(entries, kev_lookup)
        signals, run_info["new_signals"] = update_signals(load_signals(signals_file), found, now)
        p = save_signals(signals, signals_file)
        logger.info(f"[scoreboard] {run_info['new_signals']} new signal(s), {len(signals)} kept -> {p}"
                    f" ({run_info['capped_entries']} keyword entr(ies) skipped: > {MAX_SIGNAL_CVES} CVEs)")
    except Exception as e:
        logger.warning(f"[scoreboard] signal update failed: {e}")

    try:
        go_live, rows, dirty = load_scoreboard(scoreboard_file)
        if go_live is None:
            go_live = now.astimezone(timezone.utc).date()
            dirty = True
            logger.info(f"[scoreboard] new scoreboard, go-live {go_live}")
        new_rows = build_rows(kev_records, go_live, (r["cve"] for r in rows), signals)
        if kev_records is None:
            logger.warning("[scoreboard] KEV catalog unavailable -- no rows written this run")
        rows += new_rows
        run_info["new_rows"] = len(new_rows)
        if dirty or new_rows:
            save_scoreboard(go_live, rows, scoreboard_file)
        sb = compute_scoreboard(rows, go_live, now.astimezone(timezone.utc).date())
        sb["run"] = run_info
        logger.info(f"[scoreboard] {len(new_rows)} new row(s), {len(rows)} total")
        return sb
    except Exception as e:
        logger.warning(f"[scoreboard] scoreboard update failed: {e}")
        return None
