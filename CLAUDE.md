# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project does

Zero Day Pulse is an automated vulnerability monitor that runs every 6 hours via GitHub Actions. It fetches 34 RSS/Atom/JSON feeds (including network-edge vendor PSIRTs), GitHub Security Advisories, and the CISA KEV catalog, filters for zero-day signals, optionally enriches findings via the Parallel AI CLI, and publishes a Markdown report, JSON output, and an HTML dashboard to GitHub Pages.

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

## Testing

```bash
pip install -r requirements-dev.txt
pytest tests/
```

`tests/` holds offline unit tests (no network) for the two modules with real logic: `pulse/feeds.py` (date-format parsing, CVE extraction from raw feed XML) and `pulse/filter.py` (survival gate, sort order, deduplication). CI runs the suite before the pipeline, so a failing test blocks report publishing.

Expectations when changing the pipeline:
- New date format? Add a `_parse_date` test with a real sample from that feed. Unparseable dates bypass the lookback cutoff, so this class of bug is silent — the warning in `_parse_date_logged` exists to surface it.
- New keyword class or gate change? Cover both the survive and drop paths, and assert severity flags aren't inflated.
- Fixing a bug? Add the regression test in the same commit.

There is no Makefile or build step.

## Architecture

The pipeline is linear: **collect → filter → enrich → report**.

| Module | Role |
|--------|------|
| `pulse/feeds.py` | Fetches RSS/Atom/JSON feeds and CISA KEV; uses `defusedxml` to prevent XXE; strips HTML from descriptions |
| `pulse/filter.py` | Keyword matching against `config/feeds.yaml`, CVE-ID extraction via regex, deduplication (KEV entries preferred), sort by KEV → zero-day → severity → recency |
| `pulse/enrich.py` | Shells out to `parallel-cli enrich`; merges results back into findings; graceful fallback if key/CLI absent |
| `pulse/report.py` | Writes timestamped + `latest.*` Markdown/JSON; generates `docs/index.html` dark-mode dashboard |
| `main.py` | CLI entry point; lazy imports for clear error surfacing |

## Configuration

All feed URLs and keywords live in `config/feeds.yaml` — no code changes needed to add feeds or tune signal detection. Sections:
- `feeds`: list of URLs with tags
- `zero_day_keywords`: high-confidence signals (28 terms)
- `high_severity_keywords`: broader triage keywords (72 terms)
- `priority_product_keywords`: watched products (37 terms — PAN-OS, Junos, FortiOS, NetScaler, BIG-IP, ...). An entry naming one of these AND carrying a CVE survives the filter and ranks above generic matches, but is NOT marked high-severity. Use product names only; broad substrings (`vpn`, `firewall`, bare vendor names) would flood the report.
- `cisa_kev_url`: CISA Known Exploited Vulnerabilities JSON endpoint

Survival gate (`pulse/filter.py`): an entry is kept if it is a KEV entry, OR matches a zero-day keyword, OR has a CVE id AND matches either a severity or a priority-product keyword. Sort order: KEV → zero-day → high-severity → priority-product → recency.

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
