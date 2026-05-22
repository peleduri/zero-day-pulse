# Zero Day Pulse 🔴

[![Zero Day Pulse](https://github.com/peleduri/zero-day-pulse/actions/workflows/zero-day-pulse.yml/badge.svg)](https://github.com/peleduri/zero-day-pulse/actions/workflows/zero-day-pulse.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)

> Automated zero-day and actively-exploited vulnerability monitor — collects signals from 13 public sources every 6 hours, enriches each finding with [Parallel AI](https://parallel.ai) deep research, and publishes a live dashboard to GitHub Pages.

**[Live Dashboard →](https://peleduri.github.io/zero-day-pulse/)** &nbsp;|&nbsp; **[Latest Report →](reports/latest.md)**

---

## What it does

Every 6 hours a GitHub Action:

1. **Collects** vulnerability signals from 13 public RSS/Atom feeds and the [CISA Known Exploited Vulnerabilities (KEV)](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) catalog
2. **Filters** for zero-day keywords, actively-exploited indicators, and CVE references — deduplicating across sources
3. **Enriches** the top findings using `parallel-cli enrich`: CVSS score, PoC availability, patch status, threat actors, and mitigations — all researched automatically
4. **Publishes** a Markdown + JSON report committed to this repo, an HTML dashboard deployed to GitHub Pages, and a comment on a pinned tracking issue

```
RSS feeds + CISA KEV
        │
        ▼ pulse/feeds.py
  Feed collector (13 sources)
        │
        ▼ pulse/filter.py
  Zero-day signal filter
  (keywords · CVE IDs · dedup)
        │
        ▼ pulse/enrich.py
  Parallel AI enrichment
  (CVSS · PoC · patch · actors)
        │
        ▼ pulse/report.py
  HTML dashboard + MD/JSON report
  → GitHub Pages + repo commit
```

---

## Example output

```
🔴 CISA KEV — CVE-2026-34926 — TrendAI Apex One Zero-Day Exploited in the Wild
   CVE: CVE-2026-34926 | Source: SecurityWeek | Published: 2026-05-22

   ✨ Parallel AI Enrichment:
   - Technical Details: Directory traversal in on-premise Apex One agent
   - CVSS Score: 9.8
   - Exploit Available: true — PoC published on GitHub
   - Patch Available: true — Apex One SP1 Patch 1 (build 13088)
   - Active Exploitation: true — confirmed by CISA KEV catalog
   - Threat Actors: APT41
   - Mitigation: Apply vendor patch immediately; restrict agent management port
```

---

## Feed sources

| Source | Type | Signal |
|---|---|---|
| [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | JSON | ⭐ Confirmed active exploitation |
| [NVD Recent CVEs](https://nvd.nist.gov) | RSS | All new CVEs |
| [CISA US-CERT Alerts](https://www.cisa.gov/uscert/ncas/alerts) | RSS | ICS / critical infrastructure |
| [Exploit-DB](https://www.exploit-db.com) | RSS | Public exploits & PoCs |
| [Packet Storm Security](https://packetstormsecurity.com) | RSS | Exploits & advisories |
| [SANS Internet Storm Center](https://isc.sans.edu) | RSS | Threat intel |
| [GitHub Security Advisories](https://github.com/advisories) | Atom | OSS ecosystem |
| [Google Project Zero](https://googleprojectzero.blogspot.com) | Atom | In-depth zero-day research |
| [The Hacker News](https://thehackernews.com) | RSS | Breaking security news |
| [Bleeping Computer](https://www.bleepingcomputer.com) | RSS | Malware & breach coverage |
| [SecurityWeek](https://www.securityweek.com) | RSS | Research & analysis |
| [Full Disclosure](https://seclists.org/fulldisclosure/) | RSS | Researcher disclosures |
| [Rapid7 Blog](https://blog.rapid7.com) | RSS | Metasploit & research |

Feed list is fully configurable in [`config/feeds.yaml`](config/feeds.yaml) — no code changes needed.

---

## Fork & run your own instance

### 1. Fork this repository

### 2. Add your Parallel AI API key

**Settings → Secrets and variables → Actions → New repository secret**

| Secret | Value |
|---|---|
| `PARALLEL_API_KEY` | Your key from [platform.parallel.ai](https://platform.parallel.ai) |

Without this secret the pipeline still runs — it just skips the AI enrichment step.

### 3. Enable GitHub Pages

**Settings → Pages → Source → GitHub Actions**

### 4. Create the tracking issue label

**Issues → Labels → New label** — name: `zero-day-pulse`, color: `#e11d48`

### 5. Trigger the first run

**Actions → Zero Day Pulse → Run workflow**

Your dashboard will be live at `https://<your-username>.github.io/zero-day-pulse/`.

---

## Run locally

```bash
git clone https://github.com/peleduri/zero-day-pulse
cd zero-day-pulse
pip install -r requirements.txt

# No API key needed — skips enrichment
python main.py --skip-enrichment --lookback-hours 48

# With Parallel AI enrichment
export PARALLEL_API_KEY=your_key_here
python main.py --lookback-hours 24 --max-enrich 10
```

Reports are written to `reports/latest.md` and `reports/latest.json`.

### CLI options

| Flag | Default | Description |
|---|---|---|
| `--lookback-hours` | `24` | How far back to collect entries |
| `--max-enrich` | `10` | Max findings to enrich with Parallel AI |
| `--output-dir` | `reports` | Output directory for reports |
| `--skip-enrichment` | off | Skip Parallel AI enrichment |

---

## Project structure

```
zero-day-pulse/
├── .github/workflows/
│   └── zero-day-pulse.yml   # Scheduled GitHub Action (every 6h)
├── config/
│   └── feeds.yaml           # Feed URLs and zero-day keywords
├── pulse/
│   ├── feeds.py             # RSS/Atom + CISA KEV collection
│   ├── filter.py            # Zero-day signal detection & dedup
│   ├── enrich.py            # Parallel AI CLI enrichment wrapper
│   └── report.py            # HTML dashboard + MD/JSON generation
├── docs/
│   └── index.html           # GitHub Pages dashboard (auto-generated)
├── reports/
│   ├── latest.md            # Latest report (Markdown)
│   └── latest.json          # Latest report (JSON)
└── main.py                  # CLI entry point
```

---

## Security

This tool fetches content from external sources and renders it publicly. The following mitigations are in place:

- **XSS**: All external content is HTML-escaped before rendering; `javascript:` and `data:` URL schemes are blocked
- **XML bomb / XXE**: Feed parsing uses [`defusedxml`](https://github.com/tiran/defusedxml)
- **Supply chain**: All GitHub Actions are pinned to immutable commit SHAs; Python dependencies are pinned with `==`
- **Shell injection**: `workflow_dispatch` inputs are passed via environment variables, never interpolated into shell commands
- **Secrets**: `PARALLEL_API_KEY` is handled exclusively via GitHub Actions secrets — never logged or committed

---

## Contributing

Pull requests are welcome. To add a new feed, edit [`config/feeds.yaml`](config/feeds.yaml) — no Python changes needed. To add new zero-day keywords, update the `zero_day_keywords` list in the same file.

Please open an issue before submitting large changes.

---

## License

[MIT](LICENSE) — free to fork, modify, and run your own instance.
