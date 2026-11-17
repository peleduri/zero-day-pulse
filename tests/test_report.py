import unittest

from pulse.report import generate_html_report, generate_markdown_report


class ReportKevCountTests(unittest.TestCase):
    FINDINGS = [
        {"title": "old KEV via news", "cve_ids": ["CVE-2021-44228"], "in_kev": True,
         "is_zero_day": True, "epss": 0.9443, "epss_percentile": 0.9999, "link": "javascript:alert(1)"},
        {"title": "zero-day", "cve_ids": [], "is_zero_day": True},
    ]

    def test_markdown_counts_in_kev_and_shows_epss(self):
        md = generate_markdown_report(self.FINDINGS, "now")
        self.assertIn("🔴 KEV: 1", md)
        self.assertIn("🟠 Zero-Day: 1", md)
        self.assertIn("**EPSS:** 94.4%", md)
        self.assertNotIn("javascript:", md)

    def test_html_counts_in_kev(self):
        html = generate_html_report(self.FINDINGS, "now")
        self.assertIn('<span class="stat-value kev">1</span>', html)
        self.assertNotIn("javascript:", html)


if __name__ == "__main__":
    unittest.main()
