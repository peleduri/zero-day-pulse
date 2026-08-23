# TODOS

## Pipeline (filter / reporting)

### Persistent seen-state across runs (snapshot → diff reports)

- **Priority:** P2
- **What:** Persist reported CVE/entry IDs (e.g. a committed `seen.json`) so each 6-hourly run reports only NEW findings instead of re-snapshotting the whole lookback window.
- **Why:** Every finding currently appears in ~4 consecutive reports (6h cron × 24h window) — duplicate noise in reports and any downstream issues. Enrichment budget also re-spends on already-enriched CVEs.
- **Pros:** Reports become "what's newly hot since last run" — much higher signal for a monitoring tool.
- **Cons:** State file adds commit noise every run; the "what's currently hot" snapshot view is lost unless kept alongside; state reset/corruption edge cases need thought.
- **Context:** This is the tool's original snapshot-by-design behavior (surfaced during the 2026-07 network-vendor-feeds eng review, outside-voice finding #5). The vendor-feeds plan only fixed the infinite-replay variant (unparseable pubDates bypassing the cutoff). Start at `pulse/filter.py` dedup plus a state read/write in `main.py`. Snapshot-vs-diff is a product decision — run it through /office-hours before building.
- **Depends on / blocked by:** Nothing; cleanly separate PR. Land after the network-vendor-feeds branch to avoid conflicts in `filter.py`.

## Feeds

### Protect AI Blog feed is dead (404 on every run)

- **Priority:** P2
- **What:** `https://protectai.com/blog/rss.xml` returns 404 on every pipeline run. Either find a working replacement for AI/ML security coverage or drop the entry.
- **Why:** The feed contributes zero findings and logs a `WARNING ... failed ... 404` every 6 hours, so real feed failures are harder to spot in the log. AI/ML security coverage is silently missing.
- **Pros:** Removes recurring log noise; either restores the coverage or makes its absence explicit.
- **Cons:** If dropped without a replacement, AI/ML supply-chain coverage narrows to Checkmarx, HuggingFace and Trail of Bits.
- **Context:** Found by /qa on 2026-07-27. Probed 2026-07-27: `protectai.com/blog/rss.xml`, `/rss.xml`, `/blog/feed`, `/feed` all 404; `www.protectai.com/blog/rss.xml` returns 200 but serves HTML, not a feed. Protect AI was acquired, which likely moved the blog. Kept in `config/feeds.yaml` deliberately rather than deleted — dropping a feed is a coverage decision.
- **Depends on / blocked by:** Nothing.

### Full Disclosure feed times out intermittently

- **Priority:** P4
- **What:** `seclists.org/rss/fulldisclosure.rss` intermittently exceeds the 20s request timeout; it returned 200 when re-probed.
- **Why:** A timed-out feed silently contributes nothing for that run. Two runs 2 minutes apart differed by one finding purely because of this.
- **Pros:** A retry (or a longer per-feed timeout) would stop findings appearing and disappearing between runs.
- **Cons:** Adds retry complexity to a pipeline that currently degrades gracefully; seclists is slow, not broken.
- **Context:** Observed twice by /qa on 2026-07-27 (`Read timed out. (read timeout=20)` in `pulse/feeds.py` `fetch_feed`). Low priority: the 6-hourly cadence means a miss is picked up on the next run.
- **Depends on / blocked by:** Nothing.

## Completed

_(none yet)_
