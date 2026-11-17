import html as _html_mod
import json
import logging
import textwrap
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urlsplit

from pulse.urls import safe_url

logger = logging.getLogger(__name__)


def _is_kev(f: Dict) -> bool:
    # in_kev: any cited CVE is in the KEV catalog; is_kev: came from the KEV feed
    return bool(f.get("in_kev") or f.get("is_kev"))


def _severity_badge(f: Dict) -> str:
    if _is_kev(f):
        return "🔴 CISA KEV"
    if f.get("is_zero_day"):
        return "🟠 Zero-Day"
    if f.get("is_high_severity"):
        return "🟡 High Severity"
    return "⚪ Info"


# ── shared card data (used by both Markdown and HTML) ────────────────────────

_PLACEHOLDERS = ("", "N/A", "Unknown", "None", "null")
EPSS_HIGH = 0.5
EPSS_MEDIUM = 0.1


def _has_value(val) -> bool:
    return bool(val) and str(val).strip() not in _PLACEHOLDERS


def _text(val) -> str:
    if isinstance(val, (list, tuple)):
        val = ", ".join(str(v) for v in val if _has_value(v))
    return str(val).strip() if _has_value(val) else ""


def _epss(f: Dict) -> Optional[float]:
    v = f.get("epss")
    return float(v) if isinstance(v, (int, float)) and not isinstance(v, bool) else None


def _epss_level(f: Dict) -> str:
    """red >= 0.5, yellow >= 0.1, grey otherwise or when missing."""
    v = _epss(f)
    if v is None:
        return "grey"
    if v >= EPSS_HIGH:
        return "red"
    if v >= EPSS_MEDIUM:
        return "yellow"
    return "grey"


def _epss_pct(v: float) -> str:
    return "<1%" if 0 < v < 0.005 else f"{v:.0%}"


def _epss_label(f: Dict) -> str:
    v = _epss(f)
    return "EPSS n/a" if v is None else f"EPSS {_epss_pct(v)}"


def _is_high_epss(f: Dict) -> bool:
    v = _epss(f)
    return v is not None and v >= EPSS_HIGH


def _enrichment(f: Dict) -> Dict:
    e = f.get("enrichment")
    return e if isinstance(e, dict) else {}


def _poc_url(f: Dict) -> str:
    """PoC link only when the AI said exactly True AND the URL is http(s)."""
    e = _enrichment(f)
    if e.get("exploit_available") is not True:
        return ""
    return _safe_url(e.get("exploit_url"))


def _is_nvd(url: str) -> bool:
    host = (urlsplit(url).hostname or "").lower().rstrip(".")
    return host == "nvd.nist.gov" or host.endswith(".nvd.nist.gov")


def _advisory_url(f: Dict) -> str:
    """Vendor advisory link: http(s) only, and never NVD (#3: vendor page, not NVD)."""
    url = _safe_url(_enrichment(f).get("vendor_advisory"))
    try:
        return "" if not url or _is_nvd(url) else url
    except ValueError:  # malformed netloc (e.g. bad IPv6 literal)
        return ""


def _versions(f: Dict) -> tuple[str, str]:
    e = _enrichment(f)
    return _text(e.get("affected_versions")), _text(e.get("fixed_version"))


def _stack_terms(f: Dict, stack_on: bool) -> List[str]:
    if not stack_on:
        return []
    terms = f.get("stack_match")
    return [str(t) for t in terms] if isinstance(terms, list) else []


def _stack_sorted(findings: List[Dict]) -> List[Dict]:
    """My Stack order: KEV → EPSS desc (None last) → zero-day → recency."""
    hits = [f for f in findings if f.get("stack_match")]
    hits.sort(key=lambda f: f.get("published") or "", reverse=True)  # recency (stable base)
    hits.sort(key=lambda f: (
        not _is_kev(f),
        _epss(f) is None,
        -(_epss(f) or 0.0),
        not f.get("is_zero_day"),
    ))
    return hits


def _md_url(url) -> str:
    # safe_url, plus nothing that could break out of a <...> autolink
    url = _safe_url(url)
    return "" if any(c in url for c in "<> \t\n") else url


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


def _card_lines_md(f: Dict, stack_on: bool) -> List[str]:
    """KEV due, stack terms, affected→fixed and PoC/Advisory links as Markdown lines."""
    out: List[str] = []
    if f.get("in_kev"):
        kev = "**KEV:** in catalog"
        if f.get("kev_due_date"):
            kev += f", due {_html_mod.escape(str(f['kev_due_date']))}"
        if f.get("kev_ransomware"):
            kev += " · ☠️ known ransomware use"
        out.append(kev)
    terms = _stack_terms(f, stack_on)
    if terms:
        out.append("**My Stack:** " + ", ".join(f"`{_html_mod.escape(t)}`" for t in terms))
    affected, fixed = _versions(f)
    if affected or fixed:
        parts = []
        if affected:
            parts.append(f"**Affected:** {_html_mod.escape(affected)}")
        if fixed:
            parts.append(f"**Fixed:** {_html_mod.escape(fixed)}")
        out.append(" → ".join(parts))
    links = []
    poc = _md_url(_poc_url(f))
    if poc:
        links.append(f"**PoC:** <{poc}>")
    adv = _md_url(_advisory_url(f))
    if adv:
        links.append(f"**Advisory:** <{adv}>")
    if links:
        out.append(" &nbsp;|&nbsp; ".join(links))
    return out


def _stack_highlights_md(findings: List[Dict]) -> List[str]:
    hits = _stack_sorted(findings)
    if not hits:
        return []
    lines = ["## 🎯 My Stack Highlights", ""]
    for f in hits:
        cves = ", ".join(f"`{c}`" for c in f.get("cve_ids") or []) or "_No CVE_"
        terms = ", ".join(f"`{_html_mod.escape(t)}`" for t in _stack_terms(f, True))
        title = _html_mod.escape(str(f.get("title", "Untitled")))
        lines.append(f"- {_severity_badge(f)} — {title} — {cves} — {_epss_label(f)} — {terms}")
    return lines + ["", "---", ""]


# ── "Changed since last run" (shared by Markdown, HTML and the tracker comment) ──

def _no_mention(text: str) -> str:
    # zero-width space after "@" so external text can never @-mention anyone on GitHub
    return text.replace("@", "@\u200b")


def _fmt_epss(v) -> str:
    return _epss_pct(float(v)) if isinstance(v, (int, float)) and not isinstance(v, bool) else "n/a"


def _change_text(c: Dict) -> tuple[str, str]:
    """(icon, plain-text description) for one change; NOT escaped."""
    kind = c.get("kind")
    cve = str(c.get("cve") or "")
    if kind == "entered_kev":
        due = f" (due {c['kev_due_date']})" if c.get("kev_due_date") else ""
        ransom = " · known ransomware use" if c.get("kev_ransomware") else ""
        return "🔴", f"{cve} entered KEV{due}{ransom}"
    if kind == "epss_crossed":
        return "📈", (f"{cve} EPSS {_fmt_epss(c.get('old_epss'))} → {_fmt_epss(c.get('new_epss'))}"
                      f" (crossed {_fmt_epss(c.get('threshold'))})")
    if kind == "new_stack_hit":
        terms = ", ".join(str(t) for t in c.get("stack_match") or [])
        return "🎯", f"New My Stack hit: {cve} [{terms}]"
    return "•", f"{cve} {kind}"


def _changes_md(changes: Optional[List[Dict]]) -> List[str]:
    """Markdown "Changed since last run" section; [] when there are no changes."""
    if not changes:
        return []
    lines = [f"## ⚡ Changed since last run ({len(changes)})", ""]
    for c in changes:
        icon, text = _change_text(c)
        line = f"- {icon} {_html_mod.escape(_no_mention(text))}"
        title = _text(c.get("title"))
        if title:
            line += f" — {_html_mod.escape(_no_mention(title))}"
        link = _md_url(c.get("link"))
        if link:
            line += f" <{link}>"
        lines.append(line)
    return lines + ["", "---", ""]


def generate_changes_markdown(changes: Optional[List[Dict]]) -> str:
    """Concise change list for the tracker-issue comment ("" when empty)."""
    return "\n".join(_changes_md(changes))


def generate_markdown_report(findings: List[Dict], timestamp: str,
                             my_stack: Optional[List[str]] = None,
                             changes: Optional[List[Dict]] = None) -> str:
    stack_on = bool(my_stack)
    kev_n = sum(1 for f in findings if _is_kev(f))
    zd_n  = sum(1 for f in findings if f.get("is_zero_day") and not _is_kev(f))
    hs_n  = sum(1 for f in findings if f.get("is_high_severity") and not f.get("is_zero_day"))
    en_n  = sum(1 for f in findings if f.get("enrichment"))
    he_n  = sum(1 for f in findings if _is_high_epss(f))
    stack_stat = ""
    if stack_on:
        stack_stat = f"🎯 My Stack: {sum(1 for f in findings if f.get('stack_match'))} &nbsp;|&nbsp; "

    lines = [
        "# Zero Day Pulse",
        "",
        f"> **Generated:** {timestamp} &nbsp;|&nbsp; "
        f"**Total:** {len(findings)} &nbsp;|&nbsp; "
        f"🔴 KEV: {kev_n} &nbsp;|&nbsp; "
        f"📈 High EPSS: {he_n} &nbsp;|&nbsp; "
        f"🟠 Zero-Day: {zd_n} &nbsp;|&nbsp; "
        f"🟡 High: {hs_n} &nbsp;|&nbsp; "
        f"{stack_stat}"
        f"✨ Enriched: {en_n}",
        "",
        "---",
        "",
    ]
    lines += _changes_md(changes)

    if not findings:
        lines += ["_No actionable findings in this period._", ""]
        return "\n".join(lines)

    if stack_on:
        lines += _stack_highlights_md(findings)

    for i, f in enumerate(findings, 1):
        badge   = _severity_badge(f)
        title   = _html_mod.escape(str(f.get("title", "Untitled")))
        cves    = f.get("cve_ids", [])
        cve_str = " | ".join(f"`{c}`" for c in cves) if cves else "_No CVE_"
        source  = _html_mod.escape(str(f.get("source", "Unknown")))
        pub     = (f.get("published") or "")[:10] or "unknown date"
        link    = _md_url(f.get("link", ""))
        # H2: strip any residual HTML so markdown renderers can't execute it
        summary = _html_mod.escape(f.get("summary", ""))

        lines += [f"## {i}. {badge} — {title}", ""]
        lines += [f"**CVE:** {cve_str} &nbsp;|&nbsp; **Source:** {source} &nbsp;|&nbsp; **Published:** {pub}"]
        if isinstance(f.get("epss"), (int, float)):
            lines += [f"**EPSS:** {f['epss']:.1%} (percentile {f.get('epss_percentile') or 0:.0%})"]
        for extra in _card_lines_md(f, stack_on):
            lines += [extra]
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
    if _is_kev(f):            return "kev"
    if f.get("is_zero_day"):  return "zeroday"
    if f.get("is_high_severity"): return "high"
    return "info"


def _esc(text: str) -> str:
    # L1: use stdlib so both " and ' are escaped
    return _html_mod.escape(str(text), quote=True)


# H1: block javascript: and other non-http schemes (shared with enrich.py)
_safe_url = safe_url


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


def _card_badges_html(f: Dict, badge_html: str, stack_on: bool) -> str:
    level = _epss_level(f)
    parts = [badge_html,
             f'<span class="badge badge-epss epss-{level}">{_esc(_epss_label(f))}</span>']
    if f.get("in_kev"):
        due = f.get("kev_due_date")
        kev = f"KEV due {due}" if due else "In KEV"
        parts.append(f'<span class="badge badge-kevdue">{_esc(kev)}</span>')
        if f.get("kev_ransomware"):
            parts.append('<span class="badge badge-ransom">☠ Ransomware</span>')
    for term in _stack_terms(f, stack_on):
        parts.append(f'<span class="badge badge-stack">{_esc(term)}</span>')
    return "".join(parts)


def _card_extras_html(f: Dict) -> str:
    affected, fixed = _versions(f)
    out = []
    if affected or fixed:
        sides = []
        if affected:
            sides.append(f'Affected: <code>{_esc(affected)}</code>')
        if fixed:
            sides.append(f'Fixed: <code>{_esc(fixed)}</code>')
        out.append('<div class="versions">' + " → ".join(sides) + "</div>")
    buttons = []
    poc = _poc_url(f)
    if poc:
        buttons.append(f'<a class="btn btn-poc" href="{_esc(poc)}" target="_blank" '
                       f'rel="noopener noreferrer">PoC Available</a>')
    adv = _advisory_url(f)
    if adv:
        buttons.append(f'<a class="btn btn-advisory" href="{_esc(adv)}" target="_blank" '
                       f'rel="noopener noreferrer">Advisory</a>')
    if buttons:
        out.append('<div class="actions">' + "".join(buttons) + "</div>")
    return "".join(out)


def _changes_html(changes: Optional[List[Dict]]) -> str:
    """Dashboard "Changed since last run" section; "" when there are no changes."""
    if not changes:
        return ""
    items = []
    for c in changes:
        icon, text = _change_text(c)
        item = f'<span class="change-icon">{icon}</span> {_esc(text)}'
        title = _text(c.get("title"))
        link = _safe_url(c.get("link"))
        if title and link:
            item += (f' — <a href="{_esc(link)}" target="_blank" rel="noopener noreferrer">'
                     f'{_esc(title)}</a>')
        elif title:
            item += f" — {_esc(title)}"
        items.append(f'<li class="change change-{_esc(c.get("kind", ""))}">{item}</li>')
    return ('<section class="section changes-section">'
            f'<h2 class="section-head changes-head">⚡ Changed since last run '
            f'<span class="section-count">{len(changes)}</span></h2>'
            '<ul class="changes">' + "".join(items) + '</ul></section>\n')


def _finding_card(f: Dict, stack_on: bool = False) -> str:
    bkey = _badge_key(f)
    badge_html, card_cls = _HTML_BADGE[bkey]
    title  = _esc(f.get("title", "Untitled"))
    link   = f.get("link", "")
    cves   = f.get("cve_ids", [])
    source = _esc(f.get("source", ""))
    pub    = _esc((f.get("published") or "")[:10] or "—")
    summary = _esc((f.get("summary") or "")[:400])

    safe_link  = _safe_url(link)
    title_html = (f'<a href="{_esc(safe_link)}" target="_blank" rel="noopener noreferrer">{title}</a>'
                  if safe_link else title)
    cve_html = " ".join(f'<code class="cve">{_esc(c)}</code>' for c in cves) if cves else '<span class="no-cve">No CVE</span>'

    return textwrap.dedent(f"""\
        <article class="card {card_cls}">
          <div class="card-top">
            <div class="badges">{_card_badges_html(f, badge_html, stack_on)}</div>
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
          {_card_extras_html(f)}
          {_enrichment_html(f.get("enrichment"))}
        </article>
    """)


def generate_html_report(findings: List[Dict], timestamp: str, repo_url: str = "",
                         my_stack: Optional[List[str]] = None,
                         changes: Optional[List[Dict]] = None) -> str:
    stack_on = bool(my_stack)
    kev_n = sum(1 for f in findings if _is_kev(f))
    zd_n  = sum(1 for f in findings if f.get("is_zero_day") and not _is_kev(f))
    en_n  = sum(1 for f in findings if f.get("enrichment"))
    he_n  = sum(1 for f in findings if _is_high_epss(f))
    total = len(findings)

    cards_html = "\n".join(_finding_card(f, stack_on) for f in findings) if findings else (
        '<div class="empty">No actionable findings in this period.</div>'
    )

    stack_stat = ""
    if stack_on:
        stack_hits = _stack_sorted(findings)
        stack_stat = (f'<div class="stat"><span class="stat-value stack">{len(stack_hits)}</span>'
                      f'<span class="stat-label">My Stack</span></div>')
        if stack_hits:
            cards_html = (
                '<section class="section stack-section">'
                f'<h2 class="section-head stack-head">🎯 My Stack <span class="section-count">{len(stack_hits)}</span></h2>'
                + "\n".join(_finding_card(f, stack_on) for f in stack_hits)
                + '</section>\n<section class="section">'
                f'<h2 class="section-head">All Findings <span class="section-count">{total}</span></h2>'
                + cards_html + '</section>'
            )

    cards_html = _changes_html(changes) + cards_html

    safe_repo = _safe_url(repo_url)
    source_link = (f'<a href="{_esc(safe_repo)}" target="_blank" rel="noopener noreferrer">GitHub</a>'
                   if safe_repo else "GitHub")

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
              --amber: #e3b341; --amber-dim: rgba(227,179,65,.15);
              --grey: #6e7681;
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
            .stat-value.epss    {{ color: var(--red); }}
            .stat-value.stack   {{ color: var(--amber); }}
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
              /* Feed titles and summaries carry unbreakable tokens (long dotted
                 identifiers, bare URLs) that otherwise push the page wider than a
                 phone viewport and make the whole dashboard scroll sideways. */
              overflow-wrap: anywhere;
            }}
            .card-kev     {{ border-left-color: var(--red);    background: linear-gradient(90deg, var(--red-dim) 0%, var(--surface) 60%); }}
            .card-zeroday {{ border-left-color: var(--orange); background: linear-gradient(90deg, var(--orange-dim) 0%, var(--surface) 60%); }}
            .card-high    {{ border-left-color: var(--yellow); background: linear-gradient(90deg, var(--yellow-dim) 0%, var(--surface) 60%); }}

            .card-top {{ display: flex; flex-direction: column; gap: .4rem; margin-bottom: .5rem; }}
            .badges {{ display: flex; flex-wrap: wrap; gap: .35rem; }}
            .badge {{ font-size: .68rem; font-weight: 700; padding: .2rem .5rem;
                      border-radius: 4px; white-space: nowrap; flex-shrink: 0; margin-top: .15rem; }}
            .badge-kev     {{ background: var(--red);    color: #fff; }}
            .badge-zeroday {{ background: var(--orange); color: #fff; }}
            .badge-high    {{ background: var(--yellow); color: #fff; }}
            .badge-info    {{ background: var(--border); color: var(--muted); }}
            .epss-red      {{ background: var(--red);    color: #fff; }}
            .epss-yellow   {{ background: var(--yellow); color: #fff; }}
            .epss-grey     {{ background: var(--grey);   color: #fff; }}
            .badge-kevdue  {{ background: var(--red-dim); color: var(--red); border: 1px solid var(--red); }}
            .badge-ransom  {{ background: #8e1519; color: #fff; }}
            .badge-stack   {{ background: var(--amber-dim); color: var(--amber); border: 1px solid var(--amber); }}

            /* ── versions + action buttons ── */
            .versions {{ font-size: .8rem; color: var(--muted); margin-bottom: .5rem; }}
            .versions code {{ color: var(--text); }}
            .actions {{ display: flex; gap: .5rem; flex-wrap: wrap; margin-bottom: .25rem; }}
            .btn {{ font-size: .75rem; font-weight: 600; padding: .3rem .7rem;
                    border-radius: 6px; color: #fff; }}
            .btn:hover {{ text-decoration: none; filter: brightness(1.15); }}
            .btn-poc      {{ background: var(--red); }}
            .btn-advisory {{ background: #1f6feb; }}

            /* ── sections ── */
            .section {{ display: flex; flex-direction: column; gap: .875rem; }}
            .section-head {{ font-size: .8rem; text-transform: uppercase; letter-spacing: .06em;
                             color: var(--muted); padding-bottom: .35rem; border-bottom: 1px solid var(--border); }}
            .stack-head {{ color: var(--amber); border-bottom-color: var(--amber); }}
            .section-count {{ font-weight: 400; color: var(--muted); }}
            .changes-head {{ color: var(--blue); border-bottom-color: var(--blue); }}
            .changes {{ list-style: none; display: flex; flex-direction: column; gap: .4rem;
                        background: var(--surface); border: 1px solid var(--border);
                        border-radius: 8px; padding: .9rem 1.25rem; font-size: .88rem; }}
            .change-icon {{ display: inline-block; width: 1.4em; }}

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
              <div class="stat"><span class="stat-value kev">{kev_n}</span><span class="stat-label">In KEV</span></div>
              <div class="stat"><span class="stat-value epss">{he_n}</span><span class="stat-label">High EPSS</span></div>
              <div class="stat"><span class="stat-value zeroday">{zd_n}</span><span class="stat-label">Zero-Days</span></div>
              {stack_stat}
              <div class="stat"><span class="stat-value">{total}</span><span class="stat-label">Total</span></div>
              <div class="stat"><span class="stat-value enriched">{en_n}</span><span class="stat-label">Enriched</span></div>
            </div>
            <div class="generated">Updated {_esc(timestamp)}</div>
          </header>
          <main>
            {cards_html}
          </main>
          <footer>
            Powered by {source_link} · <a href="https://parallel.ai" target="_blank" rel="noopener noreferrer">Parallel AI</a>
            · refreshes every 30 min
          </footer>
        </body>
        </html>
    """)


# ── persistence ───────────────────────────────────────────────────────────────

def save_reports(findings: List[Dict], output_dir: str,
                 repo_url: str = "https://github.com/peleduri/zero-day-pulse",
                 my_stack: Optional[List[str]] = None,
                 changes: Optional[List[Dict]] = None,
                 run_id: Optional[str] = None) -> Dict[str, str]:
    from pulse.state import current_run_id

    changes = list(changes or [])
    run_id = str(run_id or current_run_id())
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    ts       = datetime.now(timezone.utc)
    stamp    = ts.strftime("%Y%m%d_%H%M%S")
    human_ts = ts.strftime("%Y-%m-%d %H:%M UTC")

    payload = {
        "generated": ts.isoformat(),
        "total":     len(findings),
        "kev":       sum(1 for f in findings if _is_kev(f)),
        "zero_day":  sum(1 for f in findings if f.get("is_zero_day") and not _is_kev(f)),
        "enriched":  sum(1 for f in findings if f.get("enrichment")),
        "high_epss": sum(1 for f in findings if _is_high_epss(f)),
    }
    if my_stack:
        payload["my_stack"] = sum(1 for f in findings if f.get("stack_match"))
    payload["run_id"] = run_id
    payload["changes"] = changes
    payload["findings"] = findings

    json_path = out / f"pulse_{stamp}.json"
    md_path   = out / f"pulse_{stamp}.md"
    json_path.write_text(json.dumps(payload, indent=2, default=str))
    md_path.write_text(generate_markdown_report(findings, human_ts, my_stack, changes))

    (out / "latest.json").write_text(json_path.read_text())
    (out / "latest.md").write_text(md_path.read_text())

    # "What changed" for this run, stamped with run_id so the workflow never re-posts a stale file
    changes_path = out / "changes.json"
    changes_path.write_text(json.dumps(
        {"run_id": run_id, "generated_at": ts.isoformat(), "changes": changes}, indent=2, default=str))
    (out / "changes.md").write_text(generate_changes_markdown(changes))

    # HTML dashboard → docs/index.html (served by GitHub Pages)
    docs = Path(output_dir).parent / "docs"
    docs.mkdir(exist_ok=True)
    html = generate_html_report(findings, human_ts, repo_url, my_stack, changes)
    (docs / "index.html").write_text(html)
    (docs / "latest.json").write_text(json_path.read_text())

    logger.info(f"Reports saved → {json_path}, {md_path}, {docs / 'index.html'}")
    return {"json": str(json_path), "markdown": str(md_path), "html": str(docs / "index.html"),
            "changes": str(changes_path)}
