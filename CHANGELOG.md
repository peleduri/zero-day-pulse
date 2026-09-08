# Changelog

All notable changes to Zero Day Pulse are documented in this file.
Format: [X.Y.Z.W] - YYYY-MM-DD, newest first.

## [0.1.0.0] - 2026-07-26

### Added
- Network-edge vendor advisory coverage: Palo Alto, Cisco PSIRT, Fortinet PSIRT, Ivanti, and Check Point Research feeds — the most actively-exploited device category now reports straight from vendor PSIRTs instead of waiting for news coverage or CISA KEV.
- Product watchlist (`priority_product_keywords`, ~35 terms): any advisory naming a watched product (PAN-OS, Junos, FortiOS, NetScaler, BIG-IP, SonicOS, ...) with a CVE now appears in reports — including vendors with no public feed (Juniper, Citrix, F5, SonicWall), caught via news feeds and KEV. Watchlist matches are ranked above generic findings without inflating their severity badge.
- Ten exploitation-class severity keywords (authentication bypass, command injection, path traversal, buffer overflow, ...) improving signal detection across all feeds.
- First test suite: 35 offline tests covering date parsing, CVE extraction, the filter gate, sorting, and deduplication — wired into the GitHub Actions run so a red suite blocks report publishing.

### Fixed
- Date parsing for Palo Alto, Cisco, Google Security Blog, CISA US-CERT, and CrowdStrike feeds: their timestamp formats previously failed to parse, silently bypassing the lookback window so stale entries reappeared in every report. Unparseable dates now also log a warning naming the feed, so future vendor format drift is visible immediately.
- CVE IDs hidden inside link URLs or beyond the summary truncation limit (common in Ivanti roll-up posts) are now extracted from the raw feed XML in both RSS and Atom parsers.
- CISA KEV entries now win deduplication against earlier articles about the same CVE, and multi-CVE roll-up posts can no longer swallow dedicated zero-day articles.
