import unittest

from pulse.enrich import _merge_enrichment, _normalize_enrichment, _tail
from pulse.report import _safe_url


class NormalizeEnrichmentTests(unittest.TestCase):
    def test_true_with_url_moves_url_into_empty_exploit_url(self):
        out = _normalize_enrichment({"exploit_available": "true (https://github.com/x/poc)", "exploit_url": ""})
        self.assertIs(out["exploit_available"], True)
        self.assertEqual(out["exploit_url"], "https://github.com/x/poc")

    def test_existing_exploit_url_is_kept(self):
        out = _normalize_enrichment({"exploit_available": "True - https://a.example/1",
                                     "exploit_url": "https://b.example/2"})
        self.assertIs(out["exploit_available"], True)
        self.assertEqual(out["exploit_url"], "https://b.example/2")

    def test_false_and_no(self):
        for raw in ("false", "False.", "no", "No public exploit", False):
            self.assertIs(_normalize_enrichment({"exploit_available": raw})["exploit_available"], False, raw)

    def test_yes_and_bool(self):
        for raw in ("yes", "TRUE", True):
            self.assertIs(_normalize_enrichment({"exploit_available": raw})["exploit_available"], True, raw)

    def test_unclear_value_becomes_none(self):
        self.assertIsNone(_normalize_enrichment({"exploit_available": "unknown"})["exploit_available"])
        self.assertIsNone(_normalize_enrichment({"exploit_available": 3})["exploit_available"])

    def test_javascript_and_data_urls_rejected(self):
        out = _normalize_enrichment({
            "exploit_url": "javascript:alert(1)",
            "vendor_advisory": "data:text/html,<script>alert(1)</script>",
        })
        self.assertEqual(out["exploit_url"], "")
        self.assertEqual(out["vendor_advisory"], "")

    def test_javascript_url_in_exploit_available_not_moved(self):
        out = _normalize_enrichment({"exploit_available": "true (javascript:alert(1))", "exploit_url": ""})
        self.assertIs(out["exploit_available"], True)
        self.assertEqual(out["exploit_url"], "")

    def test_unsafe_exploit_url_replaced_by_url_from_text(self):
        out = _normalize_enrichment({"exploit_available": "true (https://ok.example/poc)",
                                     "exploit_url": "javascript:alert(1)"})
        self.assertEqual(out["exploit_url"], "https://ok.example/poc")

    def test_safe_urls_kept_and_other_fields_untouched(self):
        out = _normalize_enrichment({"vendor_advisory": " https://vendor.example/adv ", "cvss_score": "9.8"})
        self.assertEqual(out["vendor_advisory"], "https://vendor.example/adv")
        self.assertEqual(out["cvss_score"], "9.8")
        self.assertNotIn("exploit_available", out)

    def test_same_rule_as_report_safe_url(self):
        for url in ("https://x", "HTTP://x", "javascript:x", "data:x", "ftp://x", ""):
            self.assertEqual(_normalize_enrichment({"vendor_advisory": url})["vendor_advisory"], _safe_url(url))

    def test_merge_applies_normalization(self):
        findings = [{"cve_ids": ["CVE-2026-0001"]}, {"cve_ids": ["CVE-2026-0002"]}]
        rows = [{"vulnerability_id": "CVE-2026-0001", "title": "t", "exploit_available": "false",
                 "vendor_advisory": "javascript:alert(1)"}]
        merged = _merge_enrichment(findings, rows)
        self.assertEqual(merged[0]["enrichment"], {"exploit_available": False, "vendor_advisory": ""})
        self.assertIsNone(merged[1]["enrichment"])


class TailTests(unittest.TestCase):
    def test_tail_keeps_end(self):
        self.assertEqual(_tail("a" * 3000 + "ERROR", 10), "aaaaaERROR")
        self.assertEqual(_tail(None), "")


if __name__ == "__main__":
    unittest.main()
