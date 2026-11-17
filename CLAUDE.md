# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project does

Zero Day Pulse is an automated vulnerability monitor that runs every 6 hours via GitHub Actions. It fetches 30+ RSS/Atom/JSON feeds and the CISA KEV catalog, filters for zero-day signals, optionally enriches findings via the Parallel AI CLI, and publishes a Markdown report, JSON output, and an HTML dashboard to GitHub Pages.

## Running locally

```bash
pip install -r requirements.txt

# No API key needed — skips enrichment
python main.py --skip-enrichment --lookback-hours 48

# With enrichment
export PARALLEL_API_KEY=<key>
python main.py --lookback-hours 24 --max-enrich 10
```

All CLI flags: `--lookback-hours` (default 24), `--max-enrich` (default 10), `--output-dir` (default `reports`), `--skip-enrichment`.

Tests use stdlib `unittest` (HTTP is mocked, no network or API key needed):

```bash
python -m unittest -v
```

There is no Makefile or build step.

## Architecture

The pipeline is linear: **KEV catalog + collect → CVE ids + KEV lookup → filter → EPSS → sort → enrich → report**.

| Module | Role |
|--------|------|
| `pulse/feeds.py` | Fetches RSS/Atom/JSON feeds and builds new-KEV entries from the catalog records; uses `defusedxml` to prevent XXE; strips HTML from descriptions |
| `pulse/intel.py` | Downloads the CISA KEV catalog once per run (lookup for every CVE, `in_kev`) and FIRST EPSS scores (batches of 100); failures return `None`, never fatal |
| `pulse/filter.py` | CVE-ID extraction for every entry (pre-gate), keyword matching against `config/feeds.yaml`, `in_kev` counts as a zero-day signal, deduplication (KEV-feed entries preferred), separate sort by KEV (`in_kev or is_kev`) → zero-day → severity → recency |
| `pulse/enrich.py` | Shells out to `parallel-cli enrich` (input via temp JSON file); normalizes results (`_normalize_enrichment`); logs the stderr/stdout tail on failure; graceful fallback if key/CLI absent |
| `pulse/urls.py` | `safe_url` (http/https only), shared by report rendering and enrichment parsing |
| `pulse/report.py` | Writes timestamped + `latest.*` Markdown/JSON; generates `docs/index.html` dark-mode dashboard |
| `main.py` | CLI entry point; lazy imports for clear error surfacing |

## Configuration

All feed URLs and keywords live in `config/feeds.yaml` — no code changes needed to add feeds or tune signal detection. Sections:
- `feeds`: list of URLs with tags
- `zero_day_keywords`: high-confidence signals (23 terms)
- `high_severity_keywords`: broader triage keywords (65 terms)
- `cisa_kev_url`: CISA Known Exploited Vulnerabilities JSON endpoint

## Output artifacts

| Path | Description |
|------|-------------|
| `reports/latest.md` | Latest Markdown report (committed) |
| `reports/latest.json` | Latest findings JSON (committed) |
| `reports/pulse_<timestamp>.*` | Timestamped archives (gitignored) |
| `docs/index.html` | GitHub Pages dashboard (auto-generated, committed) |
| `docs/latest.json` | JSON copy served by Pages |

## GitHub Actions

Workflow: `.github/workflows/zero-day-pulse.yml`  
Schedule: `0 */6 * * *`  
Required secret: `PARALLEL_API_KEY` (enrichment is skipped if absent, not fatal)  
Permissions: `contents: write`, `issues: write`, `pages: write`, `id-token: write`  
All action refs are pinned to immutable commit SHAs — keep them pinned when updating.

## Security invariants to maintain

- Use `defusedxml` (never `xml.etree`) for any XML parsing.
- HTML-escape all external content before rendering; block `javascript:` and `data:` URL schemes.
- Pass secrets via environment variables only — never interpolate into shell strings.
- Pin all new Python dependencies with `==` versions.
- Pin any new GitHub Actions refs to immutable commit SHAs.
