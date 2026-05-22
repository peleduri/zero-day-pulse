import re
import logging
import yaml
from pathlib import Path
from typing import Dict, List

logger = logging.getLogger(__name__)

CONFIG_PATH = Path(__file__).parent.parent / "config" / "feeds.yaml"
CVE_RE = re.compile(r"CVE-\d{4}-\d{4,}", re.IGNORECASE)


def _load_keywords() -> tuple[List[str], List[str]]:
    with open(CONFIG_PATH) as f:
        cfg = yaml.safe_load(f)
    return cfg.get("zero_day_keywords", []), cfg.get("high_severity_keywords", [])


def extract_cve_ids(text: str) -> List[str]:
    return list(dict.fromkeys(m.upper() for m in CVE_RE.findall(text)))


def _matches_any(text: str, keywords: List[str]) -> bool:
    lower = text.lower()
    return any(kw.lower() in lower for kw in keywords)


def _score_entry(entry: Dict, zd_keywords: List[str], hs_keywords: List[str]) -> tuple[bool, bool]:
    text = f"{entry.get('title', '')} {entry.get('summary', '')}"
    is_zd = entry.get("is_kev", False) or _matches_any(text, zd_keywords)
    is_hs = _matches_any(text, hs_keywords)
    return is_zd, is_hs


def filter_zero_days(entries: List[Dict]) -> List[Dict]:
    zd_keywords, hs_keywords = _load_keywords()
    filtered: List[Dict] = []
    seen_cves: set[str] = set()
    seen_ids: set[str] = set()

    for entry in entries:
        text = f"{entry.get('title', '')} {entry.get('summary', '')}"
        cve_ids = entry.get("cve_ids") or extract_cve_ids(text)
        entry["cve_ids"] = cve_ids

        is_zd, is_hs = _score_entry(entry, zd_keywords, hs_keywords)
        entry["is_zero_day"] = is_zd
        entry["is_high_severity"] = is_hs

        # Require at least zero-day signal OR (high severity + CVE reference)
        if not is_zd and not (is_hs and cve_ids):
            continue

        # Deduplicate: prefer CISA KEV entries; skip duplicates from other sources
        primary_key = cve_ids[0] if cve_ids else entry.get("id", "")
        if cve_ids:
            new_cves = [c for c in cve_ids if c not in seen_cves]
            if not new_cves and not entry.get("is_kev"):
                continue
            seen_cves.update(cve_ids)
        else:
            if primary_key in seen_ids:
                continue
            seen_ids.add(primary_key)

        filtered.append(entry)

    # Sort: CISA KEV → zero-day → high-severity, then by recency descending
    filtered.sort(
        key=lambda e: (
            e.get("is_kev", False),
            e.get("is_zero_day", False),
            e.get("is_high_severity", False),
            e.get("published") or "",
        ),
        reverse=True,
    )

    logger.info(f"Filtered to {len(filtered)} actionable findings ({sum(e.get('is_kev') for e in filtered)} KEV)")
    return filtered
