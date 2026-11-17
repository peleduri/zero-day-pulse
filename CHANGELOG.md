# Changelog

All notable changes to Zero Day Pulse are documented in this file.
Format: [X.Y.Z.W] - YYYY-MM-DD, newest first.

## [0.2.0.0] - 2026-11-17

First versioned release. It covers the intel layer (#11), dashboard cards and My Stack (#12), "what changed" alerts (#13), and the network-edge vendor work first proposed in July as 0.1.0.0 (#9). That 0.1.0.0 was never merged on its own; it is ported onto the current pipeline here.

### Added
- **Intel layer (#11):** the full CISA KEV catalog is downloaded once per run and every finding citing a KEV CVE is flagged `in_kev` (a zero-day signal, so old exploited CVEs pass the filter); FIRST EPSS scores for every finding; enrichment hygiene.
- **Dashboard cards and My Stack (#12):** EPSS and KEV badges (due date, ransomware), PoC/Advisory buttons, and a My Stack section for findings that match the `my_stack` config.
- **"What changed" alerts (#13):** a rolling 14-day per-CVE watchlist in `state/last_run.json`; the tracker issue gets a comment only when a CVE enters KEV, crosses an EPSS threshold, or newly matches your stack.
- **Network-edge vendor advisory feeds:** Palo Alto, Cisco PSIRT, Fortinet PSIRT, Ivanti, and Check Point Research.
- **Product watchlist** (`priority_product_keywords`, 37 terms): an entry naming a watched product (PAN-OS, Junos, FortiOS, NetScaler, BIG-IP, SonicOS, ...) and citing a CVE survives the filter, including vendors with no public feed (Juniper, Citrix, F5, SonicWall) caught via news feeds and KEV. Watchlist matches sort below high-severity and above everything else, without being marked high-severity.
- Ten exploitation-class severity keywords (authentication bypass, command injection, path traversal, buffer overflow, ...).
- pytest suites for feed parsing (`tests/test_feeds.py`) and the filter (`tests/test_filter.py`), alongside the existing `unittest` suites. `requirements-dev.txt` pins `pytest==8.4.1`; GitHub Actions runs `python -m pytest tests/` before the pipeline, so a red suite blocks report publishing.

### Changed
- `cisa_kev_url` in `config/feeds.yaml` is now actually used for the KEV download (falls back to the built-in URL).
- Sort order: KEV → zero-day → high-severity → priority product → recency.

### Fixed
- Date parsing for Palo Alto, Cisco, Google Security Blog, CISA US-CERT (named US time zones such as `EDT`), and CrowdStrike: their formats previously failed to parse, silently bypassing the lookback window. Unparseable dates now log a warning naming the feed.
- CVE ids that appear only in link URLs or past the summary truncation limit (common in Ivanti roll-ups) are extracted from the raw feed element in both RSS and Atom parsers, capped at 10 per entry so a "Patch Tuesday" round-up can't claim hundreds. A capped round-up that cites a KEV CVE is reported as a KEV finding.
- Deduplication: KEV-feed entries win even though they are collected last, and a non-zero-day multi-CVE roll-up can no longer swallow a dedicated zero-day article about one of its CVEs (zero-day articles are still deduplicated against each other).
- Dashboard cards wrap long unbroken tokens instead of widening the page on phones.
