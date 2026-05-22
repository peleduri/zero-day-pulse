import html as _html_mod
import json
import logging
import re
import textwrap
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


def _render_enrichment_md(enrichment: Dict | None) -> str:
    if not enrichment:
        return ""
    field_labels = [
        ("technical_details",   "Technical Details"),
        ("affected_products",   "Affected Products"),
        ("cvss_score",          "CVSS Score"),
        ("cvss_vector",         "CVSS Vector"),
        ("exploit_available",   "Exploit Available"),
        ("patch_available",     "Patch Available"),
        ("active_exploitation", "Active Exploitation"),
        ("threat_actors",       "Threat Actors"),
        ("mitigation",          "Mitigation"),
        ("vendor_advisory",     "Vendor Advisory"),
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
        link    = _safe_url(f.get("link", ""))
        # H2: strip any residual HTML so markdown renderers can't execute it
        summary = _html_mod.escape(f.get("summary", ""))

        lines += [f"## {i}. {badge} — {title}", ""]
        lines += [f"**CVE:** {cve_str} &nbsp;|&nbsp; **Source:** {source} &nbsp;|&nbsp; **Published:** {pub}"]
        if link:
            lines += [f"**Reference:** <{link}>"]
        if summary:
            excerpt = summary[:400] + ("…" if len(summary) > 400 else "")
            lines += ["", f"> {excerpt}"]
        enrichment_md = _render_enrichment_md(f.get("enrichment"))
        if enrichment_md:
            lines.append(enrichment_md)
        lines += ["", "---", ""]

    return "\n".join(lines)


# ── HTML report ───────────────────────────────────────────────────────────────

_HTML_BADGE = {
    "kev":      ('<span class="badge badge-kev">🔴 CISA KEV</span>', "card-kev"),
    "zeroday":  ('<span class="badge badge-zeroday">🟠 Zero-Day</span>', "card-zeroday"),
    "high":     ('<span class="badge badge-high">🟡 High</span>', "card-high"),
    "info":     ('<span class="badge badge-info">⚪ Info</span>', "card-info"),
}

def _badge_key(f: Dict) -> str:
    if f.get("is_kev"):       return "kev"
    if f.get("is_zero_day"):  return "zeroday"
    if f.get("is_high_severity"): return "high"
    return "info"


def _esc(text: str) -> str:
    # L1: use stdlib so both " and ' are escaped
    return _html_mod.escape(str(text), quote=True)


_SAFE_URL_RE = re.compile(r'^https?://', re.IGNORECASE)

def _safe_url(url: str) -> str:
    # H1: block javascript: and other non-http schemes
    return url if _SAFE_URL_RE.match(url) else ""


def _enrichment_html(enrichment: Dict | None) -> str:
    if not enrichment:
        return ""
    field_labels = [
        ("technical_details",   "Technical Details"),
        ("affected_products",   "Affected Products"),
        ("cvss_score",          "CVSS Score"),
        ("cvss_vector",         "CVSS Vector"),
        ("exploit_available",   "Exploit Available"),
        ("patch_available",     "Patch Available"),
        ("active_exploitation", "Active Exploitation"),
        ("threat_actors",       "Threat Actors"),
        ("mitigation",          "Mitigation"),
        ("vendor_advisory",     "Vendor Advisory"),
    ]
    rows = []
    for key, label in field_labels:
        val = enrichment.get(key)
        if val and str(val).strip() not in ("", "N/A", "Unknown", "None", "null"):
            if isinstance(val, list):
                val = ", ".join(str(v) for v in val)
            rows.append(
                f'<div class="enrich-row">'
                f'<span class="enrich-label">{_esc(label)}</span>'
                f'<span class="enrich-value">{_esc(str(val))}</span>'
                f'</div>'
            )
    if not rows:
        return ""
    return (
        '<div class="enrichment">'
        '<div class="enrich-header">✨ Parallel AI Enrichment</div>'
        + "".join(rows) +
        '</div>'
    )


def _finding_card(f: Dict) -> str:
    bkey = _badge_key(f)
    badge_html, card_cls = _HTML_BADGE[bkey]
    title  = _esc(f.get("title", "Untitled"))
    link   = f.get("link", "")
    cves   = f.get("cve_ids", [])
    source = _esc(f.get("source", ""))
    pub    = _esc((f.get("published") or "")[:10] or "—")
    summary = _esc((f.get("summary") or "")[:400])

    safe_link  = _safe_url(link)
    title_html = (f'<a href="{_esc(safe_link)}" target="_blank" rel="noopener">{title}</a>'
                  if safe_link else title)
    cve_html = " ".join(f'<code class="cve">{_esc(c)}</code>' for c in cves) if cves else '<span class="no-cve">No CVE</span>'

    return textwrap.dedent(f"""\
        <article class="card {card_cls}">
          <div class="card-top">
            {badge_html}
            <h2 class="card-title">{title_html}</h2>
          </div>
          <div class="card-meta">
            {cve_html}
            <span class="meta-sep">·</span>
            <span>{source}</span>
            <span class="meta-sep">·</span>
            <span>{pub}</span>
          </div>
          {"<p class='summary'>" + summary + ("…" if len(f.get("summary","")) > 400 else "") + "</p>" if summary else ""}
          {_enrichment_html(f.get("enrichment"))}
        </article>
    """)


def generate_html_report(findings: List[Dict], timestamp: str, repo_url: str = "") -> str:
    kev_n = sum(1 for f in findings if f.get("is_kev"))
    zd_n  = sum(1 for f in findings if f.get("is_zero_day") and not f.get("is_kev"))
    en_n  = sum(1 for f in findings if f.get("enrichment"))
    total = len(findings)

    cards_html = "\n".join(_finding_card(f) for f in findings) if findings else (
        '<div class="empty">No actionable findings in this period.</div>'
    )

    source_link = f'<a href="{repo_url}" target="_blank" rel="noopener">GitHub</a>' if repo_url else "GitHub"

    return textwrap.dedent(f"""\
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <meta http-equiv="refresh" content="1800">
          <title>Zero Day Pulse</title>
          <style>
            :root {{
              --bg: #0d1117; --surface: #161b22; --surface2: #1c2128;
              --border: #30363d; --text: #e6edf3; --muted: #8b949e;
              --red: #f85149; --red-dim: rgba(248,81,73,.15);
              --orange: #f0883e; --orange-dim: rgba(240,136,62,.15);
              --yellow: #d29922; --yellow-dim: rgba(210,153,34,.15);
              --blue: #58a6ff; --blue-dim: rgba(88,166,255,.15);
              --green: #3fb950;
            }}
            *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
            body {{ background: var(--bg); color: var(--text);
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
                    font-size: 15px; line-height: 1.6; }}
            a {{ color: var(--blue); text-decoration: none; }}
            a:hover {{ text-decoration: underline; }}
            code {{ font-family: 'SFMono-Regular', Consolas, monospace; font-size: .85em; }}

            /* ── header ── */
            header {{
              border-bottom: 1px solid var(--border);
              padding: 1.25rem 2rem;
              display: flex; align-items: center; gap: 2rem; flex-wrap: wrap;
            }}
            .brand {{ display: flex; align-items: center; gap: .6rem; }}
            .pulse-dot {{
              width: 12px; height: 12px; border-radius: 50%;
              background: var(--red);
              box-shadow: 0 0 0 0 var(--red);
              animation: pulse 2s infinite;
            }}
            @keyframes pulse {{
              0%   {{ box-shadow: 0 0 0 0 rgba(248,81,73,.7); }}
              70%  {{ box-shadow: 0 0 0 8px rgba(248,81,73,0); }}
              100% {{ box-shadow: 0 0 0 0 rgba(248,81,73,0); }}
            }}
            .brand h1 {{ font-size: 1.25rem; font-weight: 700; letter-spacing: -.5px; }}
            .stats {{ display: flex; gap: 1.5rem; flex-wrap: wrap; }}
            .stat {{ display: flex; flex-direction: column; align-items: center; min-width: 48px; }}
            .stat-value {{ font-size: 1.5rem; font-weight: 700; line-height: 1; }}
            .stat-value.kev     {{ color: var(--red); }}
            .stat-value.zeroday {{ color: var(--orange); }}
            .stat-value.enriched {{ color: var(--green); }}
            .stat-label {{ font-size: .65rem; text-transform: uppercase;
                           letter-spacing: .05em; color: var(--muted); margin-top: .15rem; }}
            .generated {{ margin-left: auto; font-size: .8rem; color: var(--muted); }}

            /* ── main ── */
            main {{ max-width: 860px; margin: 0 auto; padding: 1.5rem 1.5rem 3rem; display: flex; flex-direction: column; gap: .875rem; }}

            /* ── cards ── */
            .card {{
              background: var(--surface); border: 1px solid var(--border);
              border-radius: 8px; padding: 1.1rem 1.25rem;
              border-left: 3px solid var(--border);
            }}
            .card-kev     {{ border-left-color: var(--red);    background: linear-gradient(90deg, var(--red-dim) 0%, var(--surface) 60%); }}
            .card-zeroday {{ border-left-color: var(--orange); background: linear-gradient(90deg, var(--orange-dim) 0%, var(--surface) 60%); }}
            .card-high    {{ border-left-color: var(--yellow); background: linear-gradient(90deg, var(--yellow-dim) 0%, var(--surface) 60%); }}

            .card-top {{ display: flex; align-items: flex-start; gap: .6rem; margin-bottom: .5rem; }}
            .badge {{ font-size: .68rem; font-weight: 700; padding: .2rem .5rem;
                      border-radius: 4px; white-space: nowrap; flex-shrink: 0; margin-top: .15rem; }}
            .badge-kev     {{ background: var(--red);    color: #fff; }}
            .badge-zeroday {{ background: var(--orange); color: #fff; }}
            .badge-high    {{ background: var(--yellow); color: #fff; }}
            .badge-info    {{ background: var(--border); color: var(--muted); }}

            .card-title {{ font-size: .95rem; font-weight: 600; line-height: 1.4; }}
            .card-meta  {{ font-size: .78rem; color: var(--muted); margin-bottom: .6rem;
                           display: flex; align-items: center; gap: .35rem; flex-wrap: wrap; }}
            .cve {{ background: var(--blue-dim); color: var(--blue);
                    border: 1px solid rgba(88,166,255,.25); border-radius: 4px;
                    padding: .05rem .35rem; }}
            .no-cve {{ color: var(--muted); font-style: italic; font-size: .78rem; }}
            .meta-sep {{ color: var(--border); }}
            .summary {{ font-size: .85rem; color: var(--muted); margin-bottom: .5rem; }}

            /* ── enrichment ── */
            .enrichment {{
              margin-top: .75rem; padding-top: .75rem;
              border-top: 1px solid var(--border);
            }}
            .enrich-header {{ font-size: .7rem; text-transform: uppercase;
                               letter-spacing: .06em; color: var(--green);
                               font-weight: 600; margin-bottom: .5rem; }}
            .enrich-row {{ display: flex; gap: .5rem; font-size: .82rem;
                           padding: .2rem 0; border-bottom: 1px solid var(--surface2); }}
            .enrich-row:last-child {{ border-bottom: none; }}
            .enrich-label {{ color: var(--muted); flex-shrink: 0; width: 160px; }}
            .enrich-value {{ color: var(--text); }}

            /* ── misc ── */
            .empty {{ text-align: center; color: var(--muted); padding: 3rem; font-size: .9rem; }}
            footer {{ text-align: center; color: var(--muted); font-size: .78rem; padding: 1.5rem; border-top: 1px solid var(--border); }}
          </style>
        </head>
        <body>
          <header>
            <div class="brand">
              <span class="pulse-dot"></span>
              <h1>Zero Day Pulse</h1>
            </div>
            <div class="stats">
              <div class="stat"><span class="stat-value kev">{kev_n}</span><span class="stat-label">CISA KEV</span></div>
              <div class="stat"><span class="stat-value zeroday">{zd_n}</span><span class="stat-label">Zero-Days</span></div>
              <div class="stat"><span class="stat-value">{total}</span><span class="stat-label">Total</span></div>
              <div class="stat"><span class="stat-value enriched">{en_n}</span><span class="stat-label">Enriched</span></div>
            </div>
            <div class="generated">Updated {_esc(timestamp)}</div>
          </header>
          <main>
            {cards_html}
          </main>
          <footer>
            Powered by {source_link} · <a href="https://parallel.ai" target="_blank" rel="noopener">Parallel AI</a>
            · refreshes every 30 min
          </footer>
        </body>
        </html>
    """)


# ── persistence ───────────────────────────────────────────────────────────────

def save_reports(findings: List[Dict], output_dir: str,
                 repo_url: str = "https://github.com/peleduri/zero-day-pulse") -> Dict[str, str]:
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    ts       = datetime.now(timezone.utc)
    stamp    = ts.strftime("%Y%m%d_%H%M%S")
    human_ts = ts.strftime("%Y-%m-%d %H:%M UTC")

    payload = {
        "generated": ts.isoformat(),
        "total":     len(findings),
        "kev":       sum(1 for f in findings if f.get("is_kev")),
        "zero_day":  sum(1 for f in findings if f.get("is_zero_day") and not f.get("is_kev")),
        "enriched":  sum(1 for f in findings if f.get("enrichment")),
        "findings":  findings,
    }

    json_path = out / f"pulse_{stamp}.json"
    md_path   = out / f"pulse_{stamp}.md"
    json_path.write_text(json.dumps(payload, indent=2, default=str))
    md_path.write_text(generate_markdown_report(findings, human_ts))

    (out / "latest.json").write_text(json_path.read_text())
    (out / "latest.md").write_text(md_path.read_text())

    # HTML dashboard → docs/index.html (served by GitHub Pages)
    docs = Path(output_dir).parent / "docs"
    docs.mkdir(exist_ok=True)
    html = generate_html_report(findings, human_ts, repo_url)
    (docs / "index.html").write_text(html)
    (docs / "latest.json").write_text(json_path.read_text())

    logger.info(f"Reports saved → {json_path}, {md_path}, {docs / 'index.html'}")
    return {"json": str(json_path), "markdown": str(md_path), "html": str(docs / "index.html")}
