import json
import logging
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Dict, List

from pulse.urls import safe_url

logger = logging.getLogger(__name__)

ENRICH_INTENT = """
For this security vulnerability, research and return EXACTLY these fields, one value per field:
- technical_details: Concise technical explanation of the vulnerability mechanism and attack vector
- affected_products: Comma-separated list of affected software/hardware products
- affected_versions: Affected version range(s) only (e.g. "< 1.27.3"), or empty if unknown
- fixed_version: First fixed version(s) only (e.g. "1.27.3"), or empty if no fix is known
- cvss_score: CVSS v3.x base score as a number (e.g. 9.8) if publicly available
- cvss_vector: CVSS v3 vector string (e.g. CVSS:3.1/AV:N/AC:L/...) if available
- exploit_available: exactly true or false (no other text): whether a public proof-of-concept or weaponized exploit exists
- exploit_url: URL of the public exploit/PoC (http or https only), or empty if none
- patch_available: Whether an official vendor patch has been released — true/false
- active_exploitation: Whether confirmed active exploitation in the wild has been reported — true/false and cite sources
- threat_actors: Known threat actor groups, APT campaigns, or ransomware operators exploiting this vulnerability (or 'None known')
- mitigation: Specific workaround or mitigation steps if no patch is available, or key hardening advice
- vendor_advisory: URL (http or https only) of the official vendor security advisory or bulletin — not NVD
Do not return EPSS scores.
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


_SOURCE_COLUMNS = [
    {"name": "vulnerability_id", "description": "CVE ID (or source ID when no CVE is known)"},
    {"name": "title",            "description": "Headline of the report or advisory"},
    {"name": "description",      "description": "Short summary of the report or advisory"},
    {"name": "source",           "description": "Name of the feed the finding came from"},
    {"name": "published",        "description": "Publication date"},
    {"name": "reference_link",   "description": "URL of the original report"},
]

_INPUT_COLS = frozenset(
    ("vulnerability_id", "title", "description", "source", "published", "reference_link",
     "batch_id", "insertion_timestamp")
)


_URL_IN_TEXT_RE = re.compile(r"https?://[^\s<>\"'()\[\],]+", re.IGNORECASE)
_URL_FIELDS = ("exploit_url", "vendor_advisory")
_TRUE_WORDS = ("true", "yes")
_FALSE_WORDS = ("false", "no", "none")
LOG_TAIL_CHARS = 2000


def _coerce_bool(value):
    """Map an AI-returned value to True/False, or None when it is not a clear yes/no."""
    if isinstance(value, bool):
        return value
    if not isinstance(value, str):
        return None
    word = re.split(r"[^a-z]", value.strip().lower(), maxsplit=1)[0]
    if word in _TRUE_WORDS:
        return True
    if word in _FALSE_WORDS:
        return False
    return None


def _normalize_enrichment(enrichment: Dict) -> Dict:
    """Defensive parsing of one enrichment row.

    - ``exploit_available`` becomes True/False/None. A value like
      "true (https://x)" becomes True and its URL moves into ``exploit_url``
      when that field is empty.
    - Every URL field passes through ``safe_url`` (http/https only), so
      ``javascript:`` / ``data:`` values become "".
    """
    out = dict(enrichment)
    raw = out.get("exploit_available")
    if "exploit_available" in out:
        out["exploit_available"] = _coerce_bool(raw)
        if isinstance(raw, str) and not safe_url(out.get("exploit_url") or ""):
            m = _URL_IN_TEXT_RE.search(raw)
            if m:
                out["exploit_url"] = m.group(0)
    for key in _URL_FIELDS:
        if key in out:
            out[key] = safe_url(out.get(key) or "")
    return out


def _tail(text: str | None, n: int = LOG_TAIL_CHARS) -> str:
    text = text or ""
    return text[-n:]


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
        result.append({**f, "enrichment": _normalize_enrichment(enrichment) if enrichment else None})
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
        # Pass the rows via a JSON file (--source-type json) rather than one huge
        # --data argv string; only the small column list goes on the command line.
        input_path = Path(tmpdir) / "input.json"
        output_path = Path(tmpdir) / "enriched.json"
        input_path.write_text(json.dumps(items))

        cmd = [
            cli, "enrich", "run",
            "--source-type", "json",
            "--source", str(input_path),
            "--source-columns", json.dumps(_SOURCE_COLUMNS),
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
                # The CLI logs INFO lines to stderr and prints its error message to
                # stdout, so log the END of both streams.
                logger.error(
                    f"parallel-cli enrich failed (exit {proc.returncode})\n"
                    f"--- stderr (last {LOG_TAIL_CHARS} chars) ---\n{_tail(proc.stderr)}\n"
                    f"--- stdout (last {LOG_TAIL_CHARS} chars) ---\n{_tail(proc.stdout)}"
                )
                return findings

            enriched_rows = json.loads(output_path.read_text())
            if not isinstance(enriched_rows, list):
                raise ValueError("enrichment output is not a JSON array")

            enriched = _merge_enrichment(to_enrich, enriched_rows)
            logger.info(f"Enrichment complete — {len(enriched)} findings processed")
            return enriched + rest

        except subprocess.TimeoutExpired:
            logger.error("parallel-cli enrich timed out after 600s")
        except Exception as e:
            logger.error(f"Enrichment error: {e}")

    return findings
