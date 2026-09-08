import re
import logging
import yaml
from pathlib import Path
from typing import Dict, List

logger = logging.getLogger(__name__)

CONFIG_PATH = Path(__file__).parent.parent / "config" / "feeds.yaml"
CVE_RE = re.compile(r"CVE-\d{4}-\d{4,}", re.IGNORECASE)


def _load_keywords() -> tuple[List[str], List[str], List[str]]:
    with open(CONFIG_PATH) as f:
        cfg = yaml.safe_load(f)
    # Lowercased once here so _matches_any doesn't re-lower every keyword per entry.
    return (
        [kw.lower() for kw in cfg.get("zero_day_keywords", [])],
        [kw.lower() for kw in cfg.get("high_severity_keywords", [])],
        [kw.lower() for kw in cfg.get("priority_product_keywords", [])],
    )


def extract_cve_ids(text: str) -> List[str]:
    return list(dict.fromkeys(m.upper() for m in CVE_RE.findall(text)))


def _matches_any(text: str, keywords: List[str]) -> bool:
    lower = text.lower()
    return any(kw in lower for kw in keywords)  # keywords pre-lowercased in _load_keywords


def _score_entry(
    entry: Dict, text: str, zd_keywords: List[str], hs_keywords: List[str], pp_keywords: List[str]
) -> tuple[bool, bool, bool]:
    is_zd = entry.get("is_kev", False) or _matches_any(text, zd_keywords)
    is_hs = _matches_any(text, hs_keywords)
    is_pp = _matches_any(text, pp_keywords)
    return is_zd, is_hs, is_pp


def filter_zero_days(entries: List[Dict]) -> List[Dict]:
    zd_keywords, hs_keywords, pp_keywords = _load_keywords()
    filtered: List[Dict] = []
    seen_cves: set[str] = set()
    seen_ids: set[str] = set()

    # KEV entries are appended LAST during collection; process them first so the
    # CVE dedup below actually prefers them (stable sort keeps feed order otherwise).
    entries = sorted(entries, key=lambda e: not e.get("is_kev", False))

    for entry in entries:
        text = f"{entry.get('title', '')} {entry.get('summary', '')}"
        cve_ids = entry.get("cve_ids") or extract_cve_ids(text)
        entry["cve_ids"] = cve_ids

        is_zd, is_hs, is_pp = _score_entry(entry, text, zd_keywords, hs_keywords, pp_keywords)
        entry["is_zero_day"] = is_zd
        entry["is_high_severity"] = is_hs
        entry["is_priority_product"] = is_pp

        # Survival gate:
        #
        #   entry ──► is_kev? ───────────────────────────yes──► KEEP (zero-day)
        #              │ no
        #              ▼
        #             zero-day keyword in title/summary? yes──► KEEP (zero-day)
        #              │ no
        #              ▼
        #             has CVE id? ───────────────────────no───► DROP
        #              │ yes
        #              ▼
        #             severity keyword? (is_hs) ─────────yes──► KEEP (high-severity)
        #              │ no
        #              ▼
        #             priority-product keyword? (is_pp) ─yes──► KEEP (product watch,
        #              │ no                                     NOT high-severity)
        #              ▼
        #             DROP
        if not is_zd and not ((is_hs or is_pp) and cve_ids):
            continue

        # Deduplicate by CVE. KEV entries win ties (processed first, see sort above).
        # Zero-day-flagged entries are kept even when their CVEs were already claimed:
        # a multi-CVE roll-up must not swallow an "exploited in the wild" article
        # about one of its CVEs.
        primary_key = cve_ids[0] if cve_ids else entry.get("id", "")
        if cve_ids:
            new_cves = [c for c in cve_ids if c not in seen_cves]
            if not new_cves and not entry.get("is_kev") and not is_zd:
                continue
            seen_cves.update(cve_ids)
        else:
            if primary_key in seen_ids:
                continue
            seen_ids.add(primary_key)

        filtered.append(entry)

    # Sort: CISA KEV → zero-day → high-severity → priority-product, then recency.
    # is_priority_product is ordering only — it never claims severity.
    filtered.sort(
        key=lambda e: (
            e.get("is_kev", False),
            e.get("is_zero_day", False),
            e.get("is_high_severity", False),
            e.get("is_priority_product", False),
            e.get("published") or "",
        ),
        reverse=True,
    )

    logger.info(f"Filtered to {len(filtered)} actionable findings ({sum(1 for e in filtered if e.get('is_kev'))} KEV)")
    return filtered
