"""
pulse.filter
------------

Utility functions for filtering vulnerability data structures.

The existing module already provides generic filtering helpers.  This update
adds a dedicated filter for *active exploitation* – a flag that is set by the
enrichment step when a vulnerability is known to be actively exploited in the
wild (e.g. “Active Exploitation: true” in the enriched JSON payload).

All functions accept an iterable of dictionaries (the typical representation
of a vulnerability record) and return a list preserving the original order.
"""

from __future__ import annotations

from typing import Iterable, List, Dict, Any


def filter_by_severity(vulns: Iterable[Dict[str, Any]], min_score: float) -> List[Dict[str, Any]]:
    """
    Return only vulnerabilities whose ``cvss_score`` is greater than or equal to
    ``min_score``.  This helper existed before the change and is kept unchanged.
    """
    return [v for v in vulns if v.get("cvss_score", 0) >= min_score]


def filter_active_exploits(vulns: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Return only vulnerabilities that are marked as actively exploited.

    The enrichment step adds a boolean field ``active_exploitation`` to each
    vulnerability dictionary.  If the field is missing we treat it as ``False``.

    Parameters
    ----------
    vulns: Iterable[Dict[str, Any]]
        An iterable of vulnerability dictionaries.

    Returns
    -------
    List[Dict[str, Any]]
        A list containing only the entries where ``active_exploitation`` is
        truthy.
    """
    return [v for v in vulns if bool(v.get("active_exploitation"))]
