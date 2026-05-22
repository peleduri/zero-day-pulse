# Zero Day Pulse

[![Zero Day Pulse](https://github.com/peleduri/zero-day-pulse/actions/workflows/zero-day-pulse.yml/badge.svg)](https://github.com/peleduri/zero-day-pulse/actions/workflows/zero-day-pulse.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An automated, open-source monitor that collects zero-day and actively-exploited vulnerability signals from public RSS feeds and the [CISA Known Exploited Vulnerabilities (KEV)](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) catalog, then enriches each finding with deep research powered by [Parallel AI](https://parallel.ai).

**Latest public report → [`reports/latest.md`](reports/latest.md)**

---

## How it works

```
RSS feeds + CISA KEV
        │
        ▼
  Feed collector          pulse/feeds.py
        │
        ▼
  Zero-day filter         pulse/filter.py
  (keywords + CVE IDs)
        │
        ▼
  Parallel AI enrich      pulse/enrich.py
  (PoC, patch, CVSS, …)
        │
        ▼
  Markdown + JSON report  pulse/report.py
  committed to repo
```

The GitHub Action runs every 6 hours, commits the latest report to `reports/`, and appends a comment to a pinned tracking issue.

---

## Feed sources

| Source | Type | Signal |
|---|---|---|
| [NVD Recent CVEs](https://nvd.nist.gov) | RSS | All new CVEs |
| [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | JSON | Confirmed active exploitation |
| [CISA US-CERT Alerts](https://www.cisa.gov/uscert/ncas/alerts) | RSS | ICS/critical infrastructure |
| [Exploit-DB](https://www.exploit-db.com) | RSS | Public exploits & PoCs |
| [Packet Storm Security](https://packetstormsecurity.com) | RSS | Exploits & advisories |
| [SANS Internet Storm Center](https://isc.sans.edu) | RSS | Threat intel |
| [GitHub Security Advisories](https://github.com/advisories) | Atom | OSS ecosystem |
| [The Hacker News](https://thehackernews.com) | RSS | Breaking news |
| [Bleeping Computer](https://www.bleepingcomputer.com) | RSS | Malware & breaches |
| [SecurityWeek](https://www.securityweek.com) | RSS | Research & analysis |
| [Full Disclosure](https://seclists.org/fulldisclosure/) | RSS | Researcher disclosures |
| [Rapid7 Blog](https://blog.rapid7.com) | RSS | Metasploit & research |
| [Google Project Zero](https://googleprojectzero.blogspot.com) | Atom | In-depth zero-day research |

---

## Setup (fork & run)

### 1. Fork this repository

### 2. Add the Parallel AI API key secret

In your fork: **Settings → Secrets and variables → Actions → New repository secret**

| Secret name | Value |
|---|---|
| `PARALLEL_API_KEY` | Your key from [platform.parallel.ai](https://platform.parallel.ai) |

### 3. Enable GitHub Actions

Actions → *(enable if prompted)*

The workflow will run automatically every 6 hours.  
To trigger it manually: **Actions → Zero Day Pulse → Run workflow**.

---

## Run locally

```bash
pip install -r requirements.txt

# Without enrichment (no API key needed)
python main.py --skip-enrichment --lookback-hours 48

# With Parallel AI enrichment
export PARALLEL_API_KEY=your_key_here
python main.py --lookback-hours 24 --max-enrich 10
```

Reports are written to `reports/latest.md` and `reports/latest.json`.

---

## Report format

Each finding includes:

- **Severity badge** — 🔴 CISA KEV / 🟠 Zero-Day / 🟡 High Severity
- CVE IDs, source feed, published date
- Original summary from the feed
- **Parallel AI enrichment** (when `PARALLEL_API_KEY` is set):
  - Technical details of the exploit mechanism
  - Affected products & versions
  - CVSS score & vector
  - PoC / exploit availability
  - Patch status
  - Active exploitation evidence
  - Known threat actors
  - Mitigation advice
  - Vendor advisory link

---

## Options

```
python main.py --help

  --lookback-hours  Hours to look back for new vulnerabilities (default: 24)
  --max-enrich      Max findings to enrich with Parallel AI (default: 10)
  --output-dir      Directory to write reports into (default: reports)
  --skip-enrichment Skip Parallel AI enrichment
```

---

## License

MIT
