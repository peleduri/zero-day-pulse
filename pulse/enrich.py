import csv
import io
import json
import logging
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Dict, List

logger = logging.getLogger(__name__)

ENRICH_INTENT = """
For this security vulnerability, research and provide ALL of the following fields. Fields MUST be returned in structured JSON format where specified. Add EPSS score (0.0 to 1.0) and percentile for all CVEs that match a cve_id provided during enrichment.

- technical_details: Concise technical explanation of the vulnerability mechanism and attack vector
- affected_products: Comma-separated list of affected software/hardware products and specific versions
- cvss_score: CVSS v3.x base score (numeric, e.g. 9.8) if publicly available
- cvss_vector: CVSS v3 vector string (e.g. CVSS:3.1/AV:N/AC:L/...) if available
- exploit_available: Structured object {boolean, url?: string} indicating existence and source URL of PoC/exploit.
- patch_available: Structured object {boolean, url?: string} indicating official patch status and advisory URL.
- active_exploitation: Structured object {boolean, sources?: list[string]} confirming wild exploitation and listing cited sources.
- threat_actors: Known threat actor groups or campaigns (or 'None known').
- mitigation: Specific workaround or hardening steps if no patch is available.
- vendor_advisory: Single URL to the official vendor security advisory or bulletin, if applicable.

- technical_details: Concise technical explanation of the vulnerability mechanism and attack vector
- affected_products: Comma-separated list of affected software/hardware products and specific versions
- cvss_score: CVSS v3.x base score (numeric, e.g. 9.8) if publicly available
- cvss_vector: CVSS v3 vector string (e.g. CVSS:3.1/AV:N/AC:L/...) if available
- exploit_available: Whether a public proof-of-concept (PoC) or weaponized exploit exists — state true/false and source URL if known
- patch_available: Whether an official vendor patch has been released — state true/false and patch/advisory URL if known
- active_exploitation: Whether confirmed active exploitation in the wild has been reported — state true/false and cite sources
- threat_actors: Known threat actor groups, APT campaigns, or ransomware operators exploiting this vulnerability (or 'None known')
- mitigation: Specific workaround or mitigation steps if no patch is available, or key hardening advice
- vendor_advisory: URL to the official vendor security advisory or bulletin
"""


def _prepare_input(findings: List[Dict]) -> List[Dict]:
    return [
        {
            "vulnerability_id": (f.get("cve_ids") or [f.get("id", "UNKNOWN")])[0],
            "title": f.get("title", "")[:200],
            "description": f.get("summary", "")[:600],
            "source": f.get("source", ""),
            "published": f.get("published", ""),
            "reference_link": f.get("link", ""),
        }
        for f in findings
    ]


_INPUT_COLS = frozenset(
    ("vulnerability_id", "title", "description", "source", "published", "reference_link",
     "batch_id", "insertion_timestamp")
)


def _merge_enrichment(findings: List[Dict], enriched_rows: List[Dict]) -> List[Dict]:
    enriched_by_id = {
        row.get("vulnerability_id", ""): row
        for row in enriched_rows
        if isinstance(row, dict)
    }
    result = []
    for f in findings:
        vid = (f.get("cve_ids") or [f.get("id", "")])[0]
        enrichment = {
            k: v
            for k, v in enriched_by_id.get(vid, {}).items()
            if k not in _INPUT_COLS
        }
        result.append({**f, "enrichment": enrichment if enrichment else None})
    return result


def enrich_with_parallel(findings: List[Dict], max_items: int = 10) -> List[Dict]:
    if not findings:
        return []

    api_key = os.environ.get("PARALLEL_API_KEY", "").strip()
    if not api_key:
        logger.warning("PARALLEL_API_KEY not set — skipping Parallel AI enrichment")
        return findings

    # Locate parallel-cli in PATH only (L2: no fallback to arbitrary fs paths)
    cli = shutil.which("parallel-cli")
    if not cli:
        # Also check the scripts dir next to sys.executable — pip puts entry-points there
        candidate = Path(sys.executable).parent / "parallel-cli"
        if candidate.is_file():
            cli = str(candidate)
    if not cli:
        logger.warning("parallel-cli not found in PATH — skipping enrichment")
        return findings
    logger.info(f"parallel-cli found at {cli}")

    to_enrich = findings[:max_items]
    rest = findings[max_items:]
    items = _prepare_input(to_enrich)

    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = Path(tmpdir) / "enriched.csv"

        cmd = [
            cli, "enrich", "run",
            "--data", json.dumps(items),
            "--target", str(output_path),
            "--intent", ENRICH_INTENT,
        ]

        logger.info(f"Enriching {len(items)} findings via parallel-cli ...")
        try:
            proc = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=600,
                env={**os.environ, "PARALLEL_API_KEY": api_key},
            )
            if proc.returncode != 0:
                logger.error(
                    f"parallel-cli enrich failed (exit {proc.returncode}):\n"
                    f"{(proc.stderr or proc.stdout)[:1000]}"
                )
                return findings

            raw = output_path.read_text()
            enriched_rows = list(csv.DictReader(io.StringIO(raw)))

            enriched = _merge_enrichment(to_enrich, enriched_rows)
            logger.info(f"Enrichment complete — {len(enriched)} findings processed")
            return enriched + rest

        except subprocess.TimeoutExpired:
            logger.error("parallel-cli enrich timed out after 600s")
        except Exception as e:
            logger.error(f"Enrichment error: {e}")

    return findings
