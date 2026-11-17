#!/usr/bin/env python3
import argparse
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s — %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger("zero-day-pulse")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Zero Day Pulse — public security vulnerability monitor"
    )
    parser.add_argument(
        "--lookback-hours", type=int, default=24,
        help="Collect entries published within this many hours (default: 24)",
    )
    parser.add_argument(
        "--max-enrich", type=int, default=10,
        help="Maximum findings to enrich with Parallel AI (default: 10)",
    )
    parser.add_argument(
        "--output-dir", default="reports",
        help="Directory to write reports into (default: reports)",
    )
    parser.add_argument(
        "--skip-enrichment", action="store_true",
        help="Skip Parallel AI enrichment (useful for testing without an API key)",
    )
    args = parser.parse_args()

    # Lazy imports so errors surface clearly
    from pulse.feeds  import collect_all_feeds
    from pulse.intel  import load_kev_catalog, fetch_epss, annotate_kev, annotate_epss
    from pulse.filter import attach_cve_ids, filter_zero_days, sort_findings
    from pulse.enrich import enrich_with_parallel
    from pulse.report import save_reports

    logger.info(f"Starting Zero Day Pulse  lookback={args.lookback_hours}h  max_enrich={args.max_enrich}")

    # One KEV catalog download per run: feeds "new KEV additions" + the CVE lookup.
    kev_catalog = load_kev_catalog()
    kev_records, kev_lookup = kev_catalog if kev_catalog is not None else (None, None)

    entries = collect_all_feeds(lookback_hours=args.lookback_hours, kev_records=kev_records)
    if not entries:
        logger.error("No entries collected — check network connectivity")
        return 1

    # Pre-gate: CVE ids for every entry, then KEV lookup so old KEV CVEs pass the gate.
    attach_cve_ids(entries)
    annotate_kev(entries, kev_lookup)

    findings = filter_zero_days(entries)
    logger.info(f"Findings after filter: {len(findings)}")

    epss = fetch_epss(c for f in findings for c in f.get("cve_ids") or [])
    annotate_epss(findings, epss)
    findings = sort_findings(findings)

    if not args.skip_enrichment and findings:
        findings = enrich_with_parallel(findings, max_items=args.max_enrich)

    paths = save_reports(findings, args.output_dir)

    kev = sum(1 for f in findings if f.get("in_kev") or f.get("is_kev"))
    zd  = sum(1 for f in findings if f.get("is_zero_day") and not (f.get("in_kev") or f.get("is_kev")))
    en  = sum(1 for f in findings if f.get("enrichment"))

    print(f"\nZero Day Pulse complete")
    print(f"  Total findings : {len(findings)}")
    print(f"  CISA KEV       : {kev}")
    print(f"  Zero-days      : {zd}")
    print(f"  Enriched       : {en}")
    print(f"  JSON report    : {paths['json']}")
    print(f"  Markdown report: {paths['markdown']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
