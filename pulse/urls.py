"""Shared URL-safety helper used by report rendering and enrichment parsing."""
import re

_SAFE_URL_RE = re.compile(r"^https?://", re.IGNORECASE)


def safe_url(url) -> str:
    """Return ``url`` stripped if its scheme is http/https, else "".

    H1: blocks javascript:, data: and every other non-http scheme.
    """
    if not isinstance(url, str):
        return ""
    url = url.strip()
    return url if _SAFE_URL_RE.match(url) else ""
