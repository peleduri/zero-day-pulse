# Zero Day Pulse 🔴

[![Zero Day Pulse](https://github.com/peleduri/zero-day-pulse/actions/workflows/zero-day-pulse.yml/badge.svg)](https://github.com/peleduri/zero-day-pulse/actions/workflows/zero-day-pulse.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)

> Automated zero-day and actively-exploited vulnerability monitor — collects signals from 20+ public sources every 6 hours, enriches each finding with [Parallel AI](https://parallel.ai) deep research, and publishes a live dashboard to GitHub Pages.

**[Live Dashboard →](https://peleduri.github.io/zero-day-pulse/)** &nbsp;|&nbsp; **[Latest Report →](reports/latest.md)**

---

## What it does

Every 6 hours a GitHub Action:

1. **Collects** vulnerability signals from 20+ public RSS/Atom feeds and the [CISA Known Exploited Vulnerabilities (KEV)](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) catalog, including [GitHub Security Advisories](https://github.com/advisories) via the REST API
2. **Filters** for zero-day keywords, actively-exploited indicators, and CVE references — deduplicating across sources. Any CVE cited by any feed is checked against the full CISA KEV catalog (`in_kev`) and scored with [FIRST EPSS](https://www.first.org/epss/), no API key needed
3. **Enriches** the top findings using `parallel-cli enrich`: CVSS score, PoC availability, patch status, threat actors, and mitigations — all researched automatically
4. **Tracks what changed** since the last run: a rolling 14-day watchlist (`state/last_run.json`) is re-checked every run, and a CVE you already saw that **entered KEV**, whose **EPSS crossed 10% or 50%**, or that is a **new My Stack hit** is listed under "Changed since last run"
5. **Keeps score against CISA KEV** ("Beat KEV"): every KEV addition since go-live is checked against the first time a zero-day article named that CVE, and the panel at the top of the report and dashboard says how often, and by how many days, Zero Day Pulse saw it first (see [Beat KEV scoreboard](#beat-kev-scoreboard))
6. **Publishes** a Markdown + JSON report committed to this repo, an HTML dashboard deployed to GitHub Pages, and updates the body of one tracking issue in place, commenting only when something changed

```
RSS feeds + CISA KEV
        │
        ▼ pulse/feeds.py
  Feed collector (20+ sources)
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

## Beat KEV scoreboard

Measures one claim: *does Zero Day Pulse see exploitation before CISA KEV lists it?*

- **Signal:** a non-KEV entry whose own title + summary matches a zero-day keyword, citing at most 2 CVEs, for a CVE not yet in KEV. The first one per CVE is stored in `state/first_signal.json` (180 days, max 5000).
- **Rows:** every run walks the whole KEV catalog; each CVE added on or after the go-live date gets one write-once row in `state/kev_scoreboard.jsonl`: **earlier** (seen ≥ 1 day before `dateAdded`), **same day/late**, or **missed**.
- **Numbers:** All and Edge (Fortinet, Ivanti, Cisco, Palo Alto Networks, Citrix, SonicWall, Check Point, F5, Juniper) over 30 and 90 days: % earlier, median/max lead, same day/late and missed. The first 14 days after go-live and old CVEs (CVE year more than 1 year before the KEV year) are excluded but counted. Windows with fewer than 10 counted additions show "collecting data since <go-live>".
- **Caveats:** zero-days reported before a CVE ID exists can't be matched and count as missed; so do signals pruned before KEV lists the CVE. Lead is in whole days (±1).
- **Raw numbers:** [`scoreboard.json`](https://peleduri.github.io/zero-day-pulse/scoreboard.json) on Pages.

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

### Vulnerability databases
| Source | Type | Signal |
|---|---|---|
| [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | JSON | ⭐ Confirmed active exploitation |
| [GitHub Security Advisories](https://github.com/advisories) | JSON API | OSS ecosystem CVEs |
| [CISA US-CERT Alerts](https://www.cisa.gov/uscert/ncas/alerts) | RSS | ICS / critical infrastructure |
| [Exploit-DB](https://www.exploit-db.com) | RSS | Public exploits & PoCs |
| [Full Disclosure](https://seclists.org/fulldisclosure/) | RSS | Researcher disclosures |

### Cloud provider security
| Source | Type | Signal |
|---|---|---|
| [AWS Security Blog](https://aws.amazon.com/blogs/security/) | RSS | AWS threat research |
| [Google Security Blog](https://security.googleblog.com) | Atom | Google threat research |

### Cloud & container security research
| Source | Type | Signal |
|---|---|---|
| [Kubernetes Security](https://kubernetes.io) | RSS | K8s CVEs & announcements |
| [Falco](https://falco.org/blog) | RSS | Cloud-native runtime security |
| [Aqua Security](https://blog.aquasec.com) | RSS | Container & Kubernetes |
| [Wiz Research](https://www.wiz.io/blog) | RSS | Cloud misconfigs & vulns |
| [Unit 42](https://unit42.paloaltonetworks.com) | RSS | Cloud threat intel |
| [CrowdStrike](https://www.crowdstrike.com/en-us/blog/) | RSS | Cloud threat intel |
| [Tenable](https://www.tenable.com/blog) | RSS | Cloud vulnerability research |
| [Snyk](https://snyk.io/blog/) | RSS | Cloud dependencies & containers |

### AI agents, coding tools & IDE extensions
| Source | Type | Signal |
|---|---|---|
| [Embrace The Red](https://embracethered.com) | RSS | ⭐ Prompt injection & agent attacks |
| [Simon Willison](https://simonwillison.net) | Atom | LLM security research |
| [Protect AI](https://protectai.com/blog) | RSS | MLSecOps research |
| [Trail of Bits](https://blog.trailofbits.com) | RSS | AI/ML security audits |
| [HuggingFace Blog](https://huggingface.co/blog) | RSS | Model & supply chain issues |
| [OpenAI Blog](https://openai.com/blog) | RSS | LLM safety & security |
| [JetBrains Security](https://blog.jetbrains.com/tag/security/) | RSS | IDE plugin vulnerabilities |
| [VS Code](https://code.visualstudio.com) | RSS | Extension & IDE security |
| [Checkmarx Research](https://checkmarx.com/blog) | RSS | AI supply chain & SAST |

### Security news
| Source | Type | Signal |
|---|---|---|
| [The Hacker News](https://thehackernews.com) | RSS | Breaking security news |
| [Bleeping Computer](https://www.bleepingcomputer.com) | RSS | Malware & breach coverage |
| [SecurityWeek](https://www.securityweek.com) | RSS | Research & analysis |
| [The Record](https://therecord.media) | RSS | Threat intelligence news |
| [SANS Internet Storm Center](https://isc.sans.edu) | RSS | Daily threat intel |
| [Rapid7](https://blog.rapid7.com) | RSS | Metasploit & research |
| [Google Project Zero](https://googleprojectzero.blogspot.com) | Atom | In-depth zero-day research |
| Palo Alto, Cisco PSIRT, Fortinet PSIRT, Ivanti, Check Point Research | RSS | Network-edge vendor advisories |

A `priority_product_keywords` watchlist (PAN-OS, FortiOS, Junos, NetScaler, BIG-IP, ...) keeps any entry that names a watched product **and** cites a CVE, ranked below high-severity findings and above everything else, without marking it high-severity.

Feed list and all keywords are fully configurable in [`config/feeds.yaml`](config/feeds.yaml) — no code changes needed.

To highlight what you actually run, list products, vendors or languages under `my_stack` in the same file (e.g. `nginx`, `eks`, `openssl`). Matching is case-insensitive and whole-word (`eks` matches "Amazon EKS", not "weeks") against the title, summary, tags, KEV vendor/product and AI-reported affected products. Matches get a **My Stack** section at the top of the dashboard and Markdown report. The repo ships with a fictional example stack; replace it with yours. With `my_stack: []` nothing stack-related is shown.

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

Run the tests (offline, HTTP mocked; pytest runs both the pytest and the `unittest` suites — CI runs this before the pipeline):

```bash
pip install -r requirements-dev.txt
python -m pytest tests/
```

### CLI options

| Flag | Default | Description |
|---|---|---|
| `--lookback-hours` | `24` | How far back to collect entries |
| `--max-enrich` | `10` | Max findings to enrich with Parallel AI |
| `--output-dir` | `reports` | Output directory for reports |
| `--skip-enrichment` | off | Skip Parallel AI enrichment |
| `--state-file` | `$PULSE_STATE_PATH` or `state/last_run.json` | Watchlist state for "what changed" (no file = baseline run, no changes) |
| `--signals-file` | `$PULSE_SIGNALS_PATH` or `state/first_signal.json` | Beat KEV first signal per CVE |
| `--scoreboard-file` | `$PULSE_SCOREBOARD_PATH` or `state/kev_scoreboard.jsonl` | Beat KEV rows (no file = go-live today) |

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
│   ├── intel.py             # CISA KEV catalog lookup + FIRST EPSS scores
│   ├── filter.py            # Zero-day signal detection, dedup & sort
│   ├── enrich.py            # Parallel AI CLI enrichment wrapper
│   ├── report.py            # HTML dashboard + MD/JSON generation
│   ├── state.py             # Watchlist state + "what changed" diff
│   ├── scoreboard.py        # Beat KEV lead-time scoreboard
│   └── urls.py              # Shared http/https-only URL check
├── tests/                   # test suite (python -m pytest tests/)
├── docs/
│   ├── index.html           # GitHub Pages dashboard (auto-generated)
│   └── scoreboard.json      # Beat KEV numbers (auto-generated)
├── reports/
│   ├── latest.md            # Latest report (Markdown)
│   ├── latest.json          # Latest report (JSON, includes `changes`)
│   └── changes.json         # This run's change list, stamped with run_id
├── state/
│   ├── last_run.json        # Rolling 14-day CVE watchlist (created by the first run)
│   ├── first_signal.json    # Beat KEV: first zero-day signal per CVE
│   └── kev_scoreboard.jsonl # Beat KEV: go-live header + one row per KEV addition
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
