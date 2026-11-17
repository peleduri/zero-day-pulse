"""Deterministic vulnerability intel: CISA KEV catalog lookup and FIRST EPSS scores.

Neither source needs an API key. Every failure is logged and returned as ``None``
(distinct from an empty result) so callers never mistake a partial fetch for a
complete one. Nothing here is fatal to the pipeline.
"""
import logging
import re
from typing import Dict, List, Optional, Tuple

import requests

from pulse.feeds import KEV_URL, REQUEST_HEADERS

logger = logging.getLogger(__name__)

EPSS_URL = "https://api.first.org/data/v1/epss"
EPSS_BATCH_SIZE = 100
EPSS_TIMEOUT = 30
KEV_TIMEOUT = 30

_CVE_ID_RE = re.compile(r"^CVE-\d{4}-\d{4,}$")

KevLookup = Dict[str, Dict]
EpssScores = Dict[str, Dict]


# ── CISA KEV ──────────────────────────────────────────────────────────────────

def load_kev_catalog() -> Optional[Tuple[List[Dict], KevLookup]]:
    """Download the full CISA KEV catalog once.

    Returns ``(raw_records, lookup)`` where ``lookup`` maps CVE id ->
    ``{date_added, due_date, vendor, product, ransomware}``, or ``None`` on any
    failure (network, HTTP status, or unexpected shape).
    """
    try:
        resp = requests.get(KEV_URL, headers=REQUEST_HEADERS, timeout=KEV_TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
        records = data.get("vulnerabilities") if isinstance(data, dict) else None
        if not isinstance(records, list):
            raise ValueError("response has no 'vulnerabilities' list")
    except Exception as e:
        logger.warning(f"[CISA KEV] catalog download failed: {e}")
        return None

    raw_records = [r for r in records if isinstance(r, dict)]
    lookup: KevLookup = {}
    for r in raw_records:
        cve = str(r.get("cveID", "")).strip().upper()
        if not cve:
            continue
        lookup[cve] = {
            "date_added": r.get("dateAdded", ""),
            "due_date":   r.get("dueDate", ""),
            "vendor":     r.get("vendorProject", ""),
            "product":    r.get("product", ""),
            "ransomware": str(r.get("knownRansomwareCampaignUse", "")).strip().lower() == "known",
        }
    logger.info(f"[CISA KEV] catalog loaded: {len(lookup)} CVEs")
    return raw_records, lookup


# ── FIRST EPSS ────────────────────────────────────────────────────────────────

def _parse_epss_batch(payload) -> EpssScores:
    """Validate one EPSS API response; raise ValueError on an unexpected shape."""
    if not isinstance(payload, dict) or not isinstance(payload.get("data"), list):
        raise ValueError("response has no 'data' list")
    scores: EpssScores = {}
    for row in payload["data"]:
        if not isinstance(row, dict):
            raise ValueError("non-object row in 'data'")
        cve = str(row.get("cve", "")).strip().upper()
        if not _CVE_ID_RE.match(cve):
            raise ValueError(f"invalid cve in row: {cve!r}")
        epss = float(row["epss"])
        pct = float(row["percentile"])
        if not (0.0 <= epss <= 1.0 and 0.0 <= pct <= 1.0):
            raise ValueError(f"score out of range for {cve}")
        scores[cve] = {"epss": epss, "percentile": pct, "date": str(row.get("date", ""))}
    return scores


def fetch_epss(cves) -> Optional[EpssScores]:
    """Fetch EPSS scores for ``cves`` in batches of 100.

    Returns a dict CVE -> ``{epss, percentile, date}`` (CVEs FIRST has no score
    for are simply absent), or ``None`` if ANY batch fails, so a partial result
    is never treated as complete.
    """
    unique = sorted({c.strip().upper() for c in cves if isinstance(c, str)})
    unique = [c for c in unique if _CVE_ID_RE.match(c)]
    if not unique:
        return {}

    scores: EpssScores = {}
    for i in range(0, len(unique), EPSS_BATCH_SIZE):
        batch = unique[i:i + EPSS_BATCH_SIZE]
        # IDs are regex-validated above, so they are safe to place in the query string.
        url = f"{EPSS_URL}?cve={','.join(batch)}"
        try:
            resp = requests.get(url, headers=REQUEST_HEADERS, timeout=EPSS_TIMEOUT)
            resp.raise_for_status()
            scores.update(_parse_epss_batch(resp.json()))
        except Exception as e:
            logger.warning(f"[EPSS] batch {i // EPSS_BATCH_SIZE + 1} failed, discarding all EPSS data: {e}")
            return None
    logger.info(f"[EPSS] scores for {len(scores)}/{len(unique)} CVEs")
    return scores


# ── annotation ────────────────────────────────────────────────────────────────

def annotate_kev(entries: List[Dict], kev_lookup: Optional[KevLookup]) -> List[Dict]:
    """Set ``in_kev`` and the ``kev_*`` fields on each entry (in place).

    ``in_kev`` is true if ANY of the entry's ``cve_ids`` is in the catalog. KEV
    dates, vendor/product and ransomware flag come from the KEV CVE with the
    earliest due date. With ``kev_lookup=None`` (catalog failed) ``in_kev`` is False.
    """
    for e in entries:
        hits = [kev_lookup[c] for c in (e.get("cve_ids") or []) if kev_lookup and c in kev_lookup]
        if hits:
            first = min(hits, key=lambda h: (not h.get("due_date"), h.get("due_date") or ""))
            e.update({
                "in_kev":         True,
                "kev_date_added": first.get("date_added") or None,
                "kev_due_date":   first.get("due_date") or None,
                "kev_vendor":     first.get("vendor") or None,
                "kev_product":    first.get("product") or None,
                "kev_ransomware": bool(first.get("ransomware")),
            })
        else:
            e.update({
                "in_kev":         False,
                "kev_date_added": None,
                "kev_due_date":   None,
                "kev_vendor":     None,
                "kev_product":    None,
                "kev_ransomware": False,
            })
    return entries


def annotate_epss(findings: List[Dict], epss: Optional[EpssScores]) -> List[Dict]:
    """Set ``epss`` / ``epss_percentile`` to the maximum across ``cve_ids`` (in place).

    Both fields are None when ``epss`` is None (fetch failed) or no CVE has a score.
    """
    for f in findings:
        scored = [epss[c] for c in (f.get("cve_ids") or []) if epss and c in epss]
        f["epss"] = max(s["epss"] for s in scored) if scored else None
        f["epss_percentile"] = max(s["percentile"] for s in scored) if scored else None
    return findings


def annotate(findings: List[Dict], kev_lookup: Optional[KevLookup],
             epss: Optional[EpssScores]) -> List[Dict]:
    """Apply both KEV and EPSS annotations."""
    annotate_kev(findings, kev_lookup)
    return annotate_epss(findings, epss)
