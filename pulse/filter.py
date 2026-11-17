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


def load_my_stack() -> List[str]:
    """``my_stack`` terms from config (empty list when absent, empty or malformed)."""
    with open(CONFIG_PATH) as f:
        cfg = yaml.safe_load(f) or {}
    terms = cfg.get("my_stack") or []
    if not isinstance(terms, list):
        logger.warning("config my_stack is not a list; ignoring it")
        return []
    return [str(t).strip() for t in terms if t is not None and str(t).strip()]


def _term_pattern(term: str) -> "re.Pattern":
    # Word-boundary match that also works for terms with non-word edge chars
    # ("c++", ".net"): \b would fail there, so use (?<!\w) / (?!\w) lookarounds.
    return re.compile(r"(?<!\w)" + re.escape(term) + r"(?!\w)", re.IGNORECASE)


def _stack_text(finding: Dict) -> str:
    parts = [finding.get("title"), finding.get("summary"),
             finding.get("kev_vendor"), finding.get("kev_product")]
    tags = finding.get("tags")
    if isinstance(tags, (list, tuple)):
        parts.extend(tags)
    enrichment = finding.get("enrichment")
    if isinstance(enrichment, dict):
        products = enrichment.get("affected_products")
        if isinstance(products, (list, tuple)):
            parts.extend(products)
        else:
            parts.append(products)
    # newline separator so a term can't match across two fields
    return "\n".join(str(p) for p in parts if p)


def stack_match(finding: Dict, terms: List[str]) -> List[str]:
    """Return the ``terms`` found in ``finding`` (config order, de-duplicated, case-insensitive)."""
    if not terms:
        return []
    text = _stack_text(finding)
    matched: List[str] = []
    seen: set[str] = set()
    for term in terms:
        key = term.lower()
        if not term or key in seen:
            continue
        if _term_pattern(term).search(text):
            matched.append(term)
            seen.add(key)
    return matched


def annotate_stack(findings: List[Dict], terms: List[str]) -> List[Dict]:
    """Set ``stack_match`` on every finding (in place); [] when nothing matches."""
    for f in findings:
        f["stack_match"] = stack_match(f, terms)
    return findings


def extract_cve_ids(text: str) -> List[str]:
    return list(dict.fromkeys(m.upper() for m in CVE_RE.findall(text)))


def attach_cve_ids(entries: List[Dict]) -> List[Dict]:
    """Pre-gate step: give EVERY raw entry (RSS/Atom included) its ``cve_ids``.

    Entries that already carry ids from a structured source (KEV, GHSA) keep
    them; all others get the CVEs cited in their title + summary.
    """
    for entry in entries:
        if not entry.get("cve_ids"):
            text = f"{entry.get('title', '')} {entry.get('summary', '')}"
            entry["cve_ids"] = extract_cve_ids(text)
    return entries


def _matches_any(text: str, keywords: List[str]) -> bool:
    lower = text.lower()
    return any(kw.lower() in lower for kw in keywords)


def _score_entry(entry: Dict, zd_keywords: List[str], hs_keywords: List[str]) -> tuple[bool, bool]:
    text = f"{entry.get('title', '')} {entry.get('summary', '')}"
    # in_kev (any cited CVE is anywhere in the KEV catalog) counts as a zero-day signal
    is_zd = bool(entry.get("is_kev") or entry.get("in_kev") or _matches_any(text, zd_keywords))
    is_hs = _matches_any(text, hs_keywords)
    return is_zd, is_hs


def _is_kev(entry: Dict) -> bool:
    return bool(entry.get("in_kev") or entry.get("is_kev"))


def filter_zero_days(entries: List[Dict]) -> List[Dict]:
    """Gate + dedup. Expects ``attach_cve_ids`` and KEV annotation to have run. No sort."""
    zd_keywords, hs_keywords = _load_keywords()
    filtered: List[Dict] = []
    seen_cves: set[str] = set()
    seen_ids: set[str] = set()

    for entry in entries:
        cve_ids = entry.get("cve_ids") or []

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

    logger.info(f"Filtered to {len(filtered)} actionable findings ({sum(1 for e in filtered if _is_kev(e))} KEV)")
    return filtered


def sort_findings(findings: List[Dict]) -> List[Dict]:
    """Sort: KEV (catalog or feed) → zero-day → high-severity, then recency descending."""
    return sorted(
        findings,
        key=lambda e: (
            _is_kev(e),
            e.get("is_zero_day", False),
            e.get("is_high_severity", False),
            e.get("published") or "",
        ),
        reverse=True,
    )
