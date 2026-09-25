"""
pulse.report
------------

Functions that turn enriched vulnerability data into human‑readable reports.
The original repository generated a markdown summary of the latest findings.
This patch adds a dedicated *Active Exploitation* section so that readers can
quickly spot zero‑days that are already being used in the wild.
"""

from __future__ import annotations

from typing import List, Dict, Any
from datetime import datetime

from .filter import filter_active_exploits


def _format_vuln_entry(vuln: Dict[str, Any]) -> str:
    """
    Helper that formats a single vulnerability as a markdown list item.
    """
    cve = vuln.get("cve", "N/A")
    title = vuln.get("title", "Untitled")
    cvss = vuln.get("cvss_score", "—")
    source = vuln.get("source", "unknown")
    return f"- **{cve}** – {title} (CVSS: {cvss}) – *{source}*"


def generate_markdown_report(vulns: List[Dict[str, Any]]) -> str:
    """
    Produce a full markdown report for the supplied vulnerability list.

    The report contains three sections:
    1. Overview (total count, timestamp)
    2. Active Exploitation (only entries where ``active_exploitation`` is true)
    3. All Findings (the complete list)

    Parameters
    ----------
    vulns: List[Dict[str, Any]]
        Enriched vulnerability records.

    Returns
    -------
    str
        The markdown document.
    """
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    total = len(vulns)

    # Section 1 – Overview
    md = [
        "# Zero Day Pulse – Daily Report",
        "",
        f"*Generated:* {now}",
        f"*Total Findings:* {total}",
        "",
        "---",
        "",
    ]

    # Section 2 – Active Exploitation
    active = filter_active_exploits(vulns)
    md.append("## 🟢 Actively Exploited Vulnerabilities")
    md.append("")
    if active:
        md.extend([_format_vuln_entry(v) for v in active])
    else:
        md.append("_No actively exploited vulnerabilities detected today._")
    md.append("")
    md.append("---")
    md.append("")

    # Section 3 – Full List
    md.append("## 📋 All Findings")
    md.append("")
    md.extend([_format_vuln_entry(v) for v in vulns])
    md.append("")

    return "\n".join(md)
