# TODOS

## Feeds

### Protect AI Blog feed is dead (404 on every run)

- **Priority:** P2
- **What:** `https://protectai.com/blog/rss.xml` returns 404 on every pipeline run. Either find a working replacement for AI/ML security coverage or drop the entry.
- **Why:** The feed contributes zero findings and logs a `WARNING ... failed ... 404` every 6 hours, so real feed failures are harder to spot in the log. AI/ML security coverage is silently missing.
- **Pros:** Removes recurring log noise; either restores the coverage or makes its absence explicit.
- **Cons:** If dropped without a replacement, AI/ML supply-chain coverage narrows to Checkmarx, HuggingFace and Trail of Bits.
- **Context:** Found by /qa on 2026-07-27. Probed 2026-07-27: `protectai.com/blog/rss.xml`, `/rss.xml`, `/blog/feed`, `/feed` all 404; `www.protectai.com/blog/rss.xml` returns 200 but serves HTML, not a feed. Protect AI was acquired, which likely moved the blog. Kept in `config/feeds.yaml` deliberately rather than deleted — dropping a feed is a coverage decision.
- **Depends on / blocked by:** Nothing.

### VS Code Release Notes adds ~49 noisy entries per run

- **Priority:** P2
- **What:** `https://code.visualstudio.com/feed.xml` contributes ~49 raw entries every run (release notes, not advisories). Almost none pass the gate, but they inflate the raw count and the log.
- **Why:** Noise in the collection step makes real feed changes harder to spot, and any release note that mentions a CVE plus a broad keyword can slip through.
- **Pros:** Cleaner raw counts and logs; fewer accidental findings.
- **Cons:** Dropping it loses the (rare) VS Code security fix that is only announced in release notes; filtering per feed adds config surface.
- **Context:** Observed in pipeline logs. Options: drop the feed, replace it with a security-only source, or add a per-feed title filter in `config/feeds.yaml`.
- **Depends on / blocked by:** Nothing.

### Rapid7 feed XML malformed (parse error)

- **Priority:** P3
- **What:** The Rapid7 Blog feed returns XML that fails to parse (parse error in `fetch_feed`), so it contributes nothing.
- **Why:** The parse failure is logged as a feed failure and silently drops Rapid7 coverage (Metasploit modules, Patch Tuesday analysis).
- **Pros:** Restores a high-signal research source.
- **Cons:** Working around malformed XML (beyond the existing namespace patch in `_patch_namespaces`) risks loosening parsing; any fix must keep `defusedxml`.
- **Context:** Observed in pipeline logs. Check whether the feed URL moved, or whether a specific undeclared entity/namespace is the cause.
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

### Persistent seen-state across runs (snapshot → diff reports)

- **Completed:** 2026-11-17 in #13 ("What changed" alerts). A rolling per-CVE watchlist in `state/last_run.json` drives `entered_kev`, `epss_crossed` and `new_stack_hit` change alerts on the tracker issue; the report itself stays a snapshot of the lookback window.
