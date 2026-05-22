import html
import logging
import re
import time
from datetime import datetime, timezone, timedelta
from html.parser import HTMLParser
from typing import Dict, List
from xml.etree import ElementTree as ET
import defusedxml.ElementTree as _safe_ET  # M4: blocks XML bomb / XXE

# Common RSS/Atom namespace prefixes that some publishers omit from the root element.
_MISSING_NS_MAP: Dict[bytes, bytes] = {
    b"content":  b"http://purl.org/rss/1.0/modules/content/",
    b"dc":       b"http://purl.org/dc/elements/1.1/",
    b"media":    b"http://search.yahoo.com/mrss/",
    b"georss":   b"http://www.georss.org/georss",
    b"slash":    b"http://purl.org/rss/1.0/modules/slash/",
    b"sy":       b"http://purl.org/rss/1.0/modules/syndication/",
}


def _patch_namespaces(raw: bytes) -> bytes:
    """Inject missing xmlns declarations into the root element to prevent parse failures."""
    to_inject = []
    for prefix, ns_uri in _MISSING_NS_MAP.items():
        decl = b"xmlns:" + prefix
        if (prefix + b":") in raw and decl not in raw:
            to_inject.append(decl + b'="' + ns_uri + b'"')
    if not to_inject:
        return raw
    injection = b" " + b" ".join(to_inject)
    return re.sub(rb"(<(?![?!])[^>]+?)(\/?>)", lambda m: m.group(1) + injection + m.group(2), raw, count=1)

import requests
import yaml
from pathlib import Path


class _HTMLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self._parts: List[str] = []

    def handle_data(self, data: str) -> None:
        self._parts.append(data)

    def get_text(self) -> str:
        return " ".join(" ".join(self._parts).split())


def strip_html(text: str) -> str:
    if "<" not in text:
        return text.strip()
    s = _HTMLStripper()
    s.feed(html.unescape(text))
    return s.get_text()

logger = logging.getLogger(__name__)

CONFIG_PATH = Path(__file__).parent.parent / "config" / "feeds.yaml"
REQUEST_HEADERS = {"User-Agent": "zero-day-pulse/1.0 (github.com/peleduri/zero-day-pulse)"}
REQUEST_TIMEOUT = 20

# XML namespace shortcuts
NS = {
    "atom":    "http://www.w3.org/2005/Atom",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "dc":      "http://purl.org/dc/elements/1.1/",
}

DATE_FORMATS = [
    "%a, %d %b %Y %H:%M:%S %z",
    "%a, %d %b %Y %H:%M:%S %Z",
    "%Y-%m-%dT%H:%M:%S%z",
    "%Y-%m-%dT%H:%M:%SZ",
    "%Y-%m-%d",
]


def _parse_date(raw: str | None) -> datetime | None:
    if not raw:
        return None
    raw = raw.strip()
    # Normalise "GMT" → "+0000"
    raw = re.sub(r"\bGMT\b", "+0000", raw)
    for fmt in DATE_FORMATS:
        try:
            dt = datetime.strptime(raw, fmt)
            return dt.astimezone(timezone.utc) if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def _text(el: ET.Element | None, *tags: str, ns: Dict | None = None) -> str:
    """Return stripped text from the first matching child tag."""
    if el is None:
        return ""
    for tag in tags:
        child = el.find(tag, ns or {})
        if child is not None and child.text:
            return html.unescape(child.text.strip())
    return ""


def _attr(el: ET.Element | None, tag: str, attr: str, ns: Dict | None = None) -> str:
    if el is None:
        return ""
    child = el.find(tag, ns or {})
    if child is not None:
        return child.get(attr, "")
    return ""


def _parse_rss(root: ET.Element, name: str, tags: List[str], cutoff: datetime) -> List[Dict]:
    entries = []
    for item in root.findall(".//item"):
        pub_raw = _text(item, "pubDate", "dc:date", ns=NS)
        published = _parse_date(pub_raw)
        if published and published < cutoff:
            continue

        link = _text(item, "link", "guid")
        summary = strip_html(_text(item, "description", "content:encoded", ns=NS) or "")

        entries.append({
            "id":        link or _text(item, "guid"),
            "title":     _text(item, "title"),
            "summary":   summary[:2000],
            "link":      link,
            "published": published.isoformat() if published else pub_raw,
            "source":    name,
            "tags":      tags,
        })
    return entries


def _parse_atom(root: ET.Element, name: str, tags: List[str], cutoff: datetime) -> List[Dict]:
    a = "http://www.w3.org/2005/Atom"
    entries = []
    for entry in root.findall(f"{{{a}}}entry"):
        pub_raw = (
            _text(entry, f"{{{a}}}published")
            or _text(entry, f"{{{a}}}updated")
        )
        published = _parse_date(pub_raw)
        if published and published < cutoff:
            continue

        # Prefer 'alternate' link, fall back to first <link>
        link = ""
        for lel in entry.findall(f"{{{a}}}link"):
            if lel.get("rel", "alternate") == "alternate":
                link = lel.get("href", "")
                break
        if not link:
            lel = entry.find(f"{{{a}}}link")
            link = lel.get("href", "") if lel is not None else ""

        summary_el = entry.find(f"{{{a}}}summary") or entry.find(f"{{{a}}}content")
        summary = strip_html((summary_el.text or "") if summary_el is not None else "")

        entries.append({
            "id":        _text(entry, f"{{{a}}}id") or link,
            "title":     _text(entry, f"{{{a}}}title"),
            "summary":   summary[:2000],
            "link":      link,
            "published": published.isoformat() if published else pub_raw,
            "source":    name,
            "tags":      tags,
        })
    return entries


def fetch_feed(name: str, url: str, tags: List[str], lookback_hours: int, extra_headers: Dict | None = None) -> List[Dict]:
    cutoff = datetime.now(timezone.utc) - timedelta(hours=lookback_hours)
    try:
        headers = {**REQUEST_HEADERS, **(extra_headers or {})}
        resp = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        root = _safe_ET.fromstring(_patch_namespaces(resp.content))

        # Detect Atom vs RSS
        tag = root.tag.lower()
        if "feed" in tag or root.tag == "{http://www.w3.org/2005/Atom}feed":
            entries = _parse_atom(root, name, tags, cutoff)
        else:
            entries = _parse_rss(root, name, tags, cutoff)

        logger.info(f"[{name}] {len(entries)} entries (cutoff {lookback_hours}h)")
        return entries
    except Exception as e:
        logger.warning(f"[{name}] failed ({url}): {e}")
        return []


def fetch_cisa_kev(lookback_hours: int) -> List[Dict]:
    cutoff = datetime.now(timezone.utc) - timedelta(hours=lookback_hours)
    url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    entries = []
    try:
        resp = requests.get(url, headers=REQUEST_HEADERS, timeout=30)
        resp.raise_for_status()
        data = resp.json()

        for v in data.get("vulnerabilities", []):
            date_added = v.get("dateAdded", "")
            added_dt = _parse_date(date_added)
            if added_dt and added_dt < cutoff:
                continue

            cve_id = v.get("cveID", "")
            entries.append({
                "id":      cve_id,
                "title":   f"{cve_id} — {v.get('vulnerabilityName', '')}",
                "summary": (
                    f"Vendor: {v.get('vendorProject','')} | Product: {v.get('product','')}. "
                    f"{v.get('shortDescription','')} "
                    f"Required action: {v.get('requiredAction','')} (due {v.get('dueDate','TBD')})"
                ).strip(),
                "link":      f"https://nvd.nist.gov/vuln/detail/{cve_id}",
                "published": date_added,
                "source":    "CISA KEV",
                "tags":      ["cisa", "kev", "actively-exploited"],
                "cve_ids":   [cve_id] if cve_id else [],
                "is_kev":    True,
            })

        logger.info(f"[CISA KEV] {len(entries)} entries (cutoff {lookback_hours}h)")
    except Exception as e:
        logger.warning(f"[CISA KEV] failed: {e}")
    return entries


def fetch_github_advisories(lookback_hours: int) -> List[Dict]:
    """Fetch GitHub Security Advisories via the REST API (Atom endpoint returns 406)."""
    cutoff = datetime.now(timezone.utc) - timedelta(hours=lookback_hours)
    url = "https://api.github.com/advisories"
    entries = []
    try:
        params = {"per_page": 100, "sort": "published", "direction": "desc"}
        headers = {**REQUEST_HEADERS, "Accept": "application/vnd.github+json"}
        resp = requests.get(url, headers=headers, params=params, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        for adv in resp.json():
            published_raw = adv.get("published_at", "")
            published = _parse_date(published_raw)
            if published and published < cutoff:
                break  # sorted newest-first, so we can stop early
            cve_id = adv.get("cve_id") or ""
            ghsa_id = adv.get("ghsa_id", "")
            entries.append({
                "id":        cve_id or ghsa_id,
                "title":     adv.get("summary", ghsa_id),
                "summary":   (adv.get("description") or "")[:2000],
                "link":      adv.get("html_url", f"https://github.com/advisories/{ghsa_id}"),
                "published": published_raw,
                "source":    "GitHub Security Advisories",
                "tags":      ["github", "advisories", "oss"],
                "cve_ids":   [cve_id] if cve_id else [],
            })
        logger.info(f"[GitHub Advisories] {len(entries)} entries (cutoff {lookback_hours}h)")
    except Exception as e:
        logger.warning(f"[GitHub Advisories] failed: {e}")
    return entries


def load_config() -> Dict:
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def collect_all_feeds(lookback_hours: int = 24) -> List[Dict]:
    config = load_config()
    all_entries: List[Dict] = []

    for feed_cfg in config.get("feeds", []):
        entries = fetch_feed(
            feed_cfg["name"],
            feed_cfg["url"],
            feed_cfg.get("tags", []),
            lookback_hours,
            extra_headers=feed_cfg.get("headers"),
        )
        all_entries.extend(entries)
        time.sleep(0.3)

    all_entries.extend(fetch_cisa_kev(lookback_hours))
    all_entries.extend(fetch_github_advisories(lookback_hours))
    logger.info(f"Total raw entries: {len(all_entries)}")
    return all_entries
