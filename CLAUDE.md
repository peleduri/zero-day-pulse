# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project does

Zero Day Pulse is an automated vulnerability monitor that runs every 6 hours via GitHub Actions. It fetches 34 RSS/Atom feeds (including network-edge vendor PSIRTs), GitHub Security Advisories and the CISA KEV catalog, filters for zero-day signals, optionally enriches findings via the Parallel AI CLI, and publishes a Markdown report, JSON output, and an HTML dashboard to GitHub Pages.

## Running locally

```bash
pip install -r requirements.txt

# No API key needed — skips enrichment
python main.py --skip-enrichment --lookback-hours 48

# With enrichment
export PARALLEL_API_KEY=<key>
python main.py --lookback-hours 24 --max-enrich 10
```

All CLI flags: `--lookback-hours` (default 24), `--max-enrich` (default 10), `--output-dir` (default `reports`), `--skip-enrichment`, `--state-file` (default `$PULSE_STATE_PATH` or `state/last_run.json`; point it at a temp path for local experiments so you don't touch the committed watchlist).

## Testing

Tests are offline (HTTP is mocked, no network or API key needed). `tests/test_feeds.py` and `tests/test_filter.py` are pytest-style; the rest are stdlib `unittest`. pytest runs both, and CI runs it before the pipeline, so a failing test blocks report publishing:

```bash
pip install -r requirements-dev.txt
python -m pytest tests/        # everything
python -m unittest -v          # unittest-style tests only
```

Expectations when changing the pipeline:
- New date format? Add a `_parse_date` test with a real sample from that feed. Unparseable dates bypass the lookback cutoff, so this class of bug is silent — the warning in `_parse_date_logged` exists to surface it.
- New keyword class or gate change? Cover both the survive and drop paths, and assert severity flags aren't inflated.
- Fixing a bug? Add the regression test in the same commit.

There is no Makefile or build step.

## Architecture

The pipeline is linear: **KEV catalog + state load → collect → CVE ids + KEV lookup → filter → EPSS (findings + watchlist, one call) → sort → enrich → stack match → state diff → report → state save**.

| Module | Role |
|--------|------|
| `pulse/feeds.py` | Fetches RSS/Atom/JSON feeds and builds new-KEV entries from the catalog records; uses `defusedxml` to prevent XXE; strips HTML from descriptions; RSS/Atom `cve_ids` come from the serialized raw element (hrefs, text past the `SUMMARY_MAX_LEN` cut), capped at `MAX_CVE_IDS_PER_ENTRY` (10); unparseable dates log a warning (`_parse_date_logged`) |
| `pulse/intel.py` | Downloads the CISA KEV catalog once per run from `cisa_kev_url` (fallback `KEV_URL`) (lookup for every CVE, `in_kev`) and FIRST EPSS scores (batches of 100); failures return `None`, never fatal |
| `pulse/filter.py` | CVE-ID extraction for every entry (pre-gate; keeps ids a parser/structured source already set), keyword matching against `config/feeds.yaml`, `in_kev` counts as a zero-day signal, gate + deduplication (see below), separate sort by KEV (`in_kev or is_kev`) → zero-day → severity → priority product → recency; `stack_match` (whole-word, case-insensitive match of `my_stack` terms) |
| `pulse/enrich.py` | Shells out to `parallel-cli enrich` (input via temp JSON file); normalizes results (`_normalize_enrichment`); logs the stderr/stdout tail on failure; graceful fallback if key/CLI absent |
| `pulse/state.py` | Rolling 14-day CVE watchlist in `state/last_run.json` (cap 1000, oldest `first_seen` pruned after the diff). Per-CVE diff emits `entered_kev`, `epss_crossed` (0.1 / 0.5) and `new_stack_hit`; first-seen CVEs only emit stack hits; KEV/EPSS fetch failure keeps stored values and emits nothing; a `my_stack` edit (per-CVE `stack_terms_hash`) re-baselines silently; missing/corrupt state = baseline run |
| `pulse/urls.py` | `safe_url` (http/https only), shared by report rendering and enrichment parsing |
| `pulse/report.py` | Writes timestamped + `latest.*` Markdown/JSON; generates `docs/index.html` dark-mode dashboard (EPSS/KEV badges, PoC/Advisory buttons, My Stack section) |
| `main.py` | CLI entry point; lazy imports for clear error surfacing |

## Configuration

All feed URLs and keywords live in `config/feeds.yaml` — no code changes needed to add feeds or tune signal detection. Sections:
- `feeds`: list of URLs with tags
- `zero_day_keywords`: high-confidence signals (28 terms)
- `high_severity_keywords`: broader triage keywords (72 terms)
- `priority_product_keywords`: watched products (37 terms — PAN-OS, Junos, FortiOS, NetScaler, BIG-IP, ...). An entry naming one of these AND carrying a CVE survives the filter and ranks above generic matches, but is NOT marked high-severity. Use product names only; broad substrings (`vpn`, `firewall`, bare vendor names) would flood the report. A missing section means none
- `my_stack`: products/vendors/languages you run (ships with a fictional example stack — replace it); when non-empty, matching findings get a My Stack section, badges and stat. Empty means no stack-related output
- `cisa_kev_url`: CISA Known Exploited Vulnerabilities JSON endpoint (read by `intel.load_kev_catalog`; falls back to `KEV_URL`)

Survival gate (`filter_zero_days`): an entry is kept if it is zero-day (`is_kev` KEV-feed entry, OR `in_kev`, OR a zero-day keyword), OR it has a CVE id AND matches a severity or a priority-product keyword. Dedup by CVE: KEV-feed entries are processed first and never dropped; a non-zero-day entry is dropped when all its CVEs were already claimed; a zero-day entry is dropped only when all its CVEs were already claimed by a zero-day/KEV entry (a non-zero-day roll-up can't swallow it). Note: a capped round-up citing one KEV CVE becomes `in_kev`/zero-day. Sort (`sort_findings`, after EPSS): KEV → zero-day → high-severity → priority-product → recency.

## Output artifacts

| Path | Description |
|------|-------------|
| `reports/latest.md` | Latest Markdown report (committed) |
| `reports/latest.json` | Latest findings JSON (committed) |
| `reports/pulse_<timestamp>.*` | Timestamped archives (gitignored) |
| `docs/index.html` | GitHub Pages dashboard (auto-generated, committed) |
| `docs/latest.json` | JSON copy served by Pages |
| `reports/changes.json` | `{run_id, generated_at, changes}` for this run (committed; `run_id` = `$GITHUB_RUN_ID` or `local`) |
| `reports/changes.md` | Change list rendered for the tracker comment (gitignored) |
| `state/last_run.json` | Watchlist state (committed by the workflow; never commit a locally generated one) |

## GitHub Actions

Workflow: `.github/workflows/zero-day-pulse.yml`  
Schedule: `0 */6 * * *`  
Required secret: `PARALLEL_API_KEY` (enrichment is skipped if absent, not fatal)  
Permissions: `contents: write`, `issues: write`, `pages: write`, `id-token: write`  
Concurrency: group `zero-day-pulse`, `cancel-in-progress: false` (runs never race on `state/`)  
Tracker issue: the open `zero-day-pulse`-labelled issue titled exactly `🚨 Zero Day Pulse — Active Vulnerability Tracker` gets its **body** replaced with `latest.md`; a **comment** (change list only, no mentions) is posted only when the run and commit/push steps succeeded, `changes.json`'s `run_id` equals this run, and `changes` is non-empty  
All action refs are pinned to immutable commit SHAs — keep them pinned when updating.

## Security invariants to maintain

- Use `defusedxml` (never `xml.etree`) for any XML parsing.
- HTML-escape all external content before rendering; block `javascript:` and `data:` URL schemes.
- Pass secrets via environment variables only — never interpolate into shell strings.
- Pin all new Python dependencies with `==` versions.
- Pin any new GitHub Actions refs to immutable commit SHAs.
