import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

logger = logging.getLogger(__name__)


def _severity_badge(f: Dict) -> str:
    if f.get("is_kev"):
        return "🔴 CISA KEV"
    if f.get("is_zero_day"):
        return "🟠 Zero-Day"
    if f.get("is_high_severity"):
        return "🟡 High Severity"
    return "⚪ Info"


def _render_enrichment(enrichment: Dict | None) -> str:
    if not enrichment:
        return ""

    field_labels = [
        ("technical_details",  "Technical Details"),
        ("affected_products",  "Affected Products"),
        ("cvss_score",         "CVSS Score"),
        ("cvss_vector",        "CVSS Vector"),
        ("exploit_available",  "Exploit Available"),
        ("patch_available",    "Patch Available"),
        ("active_exploitation","Active Exploitation"),
        ("threat_actors",      "Threat Actors"),
        ("mitigation",         "Mitigation"),
        ("vendor_advisory",    "Vendor Advisory"),
    ]

    lines = ["", "**Parallel AI Enrichment:**", ""]
    for key, label in field_labels:
        val = enrichment.get(key)
        if val and str(val).strip() not in ("", "N/A", "Unknown", "None", "null"):
            if isinstance(val, list):
                val = ", ".join(str(v) for v in val)
            lines.append(f"- **{label}:** {val}")

    return "\n".join(lines) if len(lines) > 3 else ""


def generate_markdown_report(findings: List[Dict], timestamp: str) -> str:
    kev_n = sum(1 for f in findings if f.get("is_kev"))
    zd_n  = sum(1 for f in findings if f.get("is_zero_day") and not f.get("is_kev"))
    hs_n  = sum(1 for f in findings if f.get("is_high_severity") and not f.get("is_zero_day"))
    en_n  = sum(1 for f in findings if f.get("enrichment"))

    lines = [
        "# Zero Day Pulse",
        "",
        f"> **Generated:** {timestamp} &nbsp;|&nbsp; "
        f"**Total:** {len(findings)} &nbsp;|&nbsp; "
        f"🔴 KEV: {kev_n} &nbsp;|&nbsp; "
        f"🟠 Zero-Day: {zd_n} &nbsp;|&nbsp; "
        f"🟡 High: {hs_n} &nbsp;|&nbsp; "
        f"✨ Enriched: {en_n}",
        "",
        "---",
        "",
    ]

    if not findings:
        lines += ["_No actionable findings in this period._", ""]
        return "\n".join(lines)

    for i, f in enumerate(findings, 1):
        badge   = _severity_badge(f)
        title   = f.get("title", "Untitled")
        cves    = f.get("cve_ids", [])
        cve_str = " | ".join(f"`{c}`" for c in cves) if cves else "_No CVE_"
        source  = f.get("source", "Unknown")
        pub     = (f.get("published") or "")[:10] or "unknown date"
        link    = f.get("link", "")
        summary = f.get("summary", "")

        lines += [f"## {i}. {badge} — {title}", ""]
        lines += [f"**CVE:** {cve_str} &nbsp;|&nbsp; **Source:** {source} &nbsp;|&nbsp; **Published:** {pub}"]

        if link:
            lines += [f"**Reference:** <{link}>"]

        if summary:
            excerpt = summary[:400] + ("…" if len(summary) > 400 else "")
            lines += ["", f"> {excerpt}"]

        enrichment_md = _render_enrichment(f.get("enrichment"))
        if enrichment_md:
            lines.append(enrichment_md)

        lines += ["", "---", ""]

    return "\n".join(lines)


def save_reports(findings: List[Dict], output_dir: str) -> Dict[str, str]:
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    ts = datetime.now(timezone.utc)
    stamp = ts.strftime("%Y%m%d_%H%M%S")
    human_ts = ts.strftime("%Y-%m-%d %H:%M UTC")

    payload = {
        "generated": ts.isoformat(),
        "total": len(findings),
        "kev": sum(1 for f in findings if f.get("is_kev")),
        "zero_day": sum(1 for f in findings if f.get("is_zero_day") and not f.get("is_kev")),
        "enriched": sum(1 for f in findings if f.get("enrichment")),
        "findings": findings,
    }

    json_path = out / f"pulse_{stamp}.json"
    md_path   = out / f"pulse_{stamp}.md"
    json_path.write_text(json.dumps(payload, indent=2, default=str))
    md_path.write_text(generate_markdown_report(findings, human_ts))

    # Overwrite latest/* for easy public linking
    (out / "latest.json").write_text(json_path.read_text())
    (out / "latest.md").write_text(md_path.read_text())

    logger.info(f"Reports saved → {json_path}, {md_path}")
    return {"json": str(json_path), "markdown": str(md_path)}
