import re
import unittest

from pulse.report import (_advisory_url, _epss_label, _epss_level, _poc_url,
                          generate_html_report, generate_markdown_report)


def _body(html):
    # skip the static <style> block so CSS class names don't count as rendered output
    return html.split("<body>", 1)[1]


def _f(**kw):
    base = {"title": "t", "cve_ids": ["CVE-2026-0001"], "source": "s",
            "published": "2026-11-17T00:00:00+00:00", "is_zero_day": True, "epss": None}
    base.update(kw)
    return base


class EpssBadgeTests(unittest.TestCase):
    def test_thresholds(self):
        self.assertEqual(_epss_level(_f(epss=0.5)), "red")
        self.assertEqual(_epss_level(_f(epss=0.1)), "yellow")
        self.assertEqual(_epss_level(_f(epss=0.09)), "grey")
        self.assertEqual(_epss_level(_f(epss=None)), "grey")

    def test_labels(self):
        self.assertEqual(_epss_label(_f(epss=0.61)), "EPSS 61%")
        self.assertEqual(_epss_label(_f(epss=0.001)), "EPSS <1%")
        self.assertEqual(_epss_label(_f(epss=None)), "EPSS n/a")

    def test_badge_in_html(self):
        html = generate_html_report([_f(epss=0.61), _f(epss=0.2), _f(epss=None)], "now")
        self.assertIn('<span class="badge badge-epss epss-red">EPSS 61%</span>', html)
        self.assertIn('<span class="badge badge-epss epss-yellow">EPSS 20%</span>', html)
        self.assertIn('<span class="badge badge-epss epss-grey">EPSS n/a</span>', html)


class KevBadgeTests(unittest.TestCase):
    def test_due_date_and_ransomware(self):
        html = generate_html_report([_f(in_kev=True, kev_due_date="2026-12-05", kev_ransomware=True)], "now")
        self.assertIn("KEV due 2026-12-05", html)
        self.assertIn("badge-ransom", html)
        md = generate_markdown_report([_f(in_kev=True, kev_due_date="2026-12-05", kev_ransomware=True)], "now")
        self.assertIn("**KEV:** in catalog, due 2026-12-05", md)
        self.assertIn("ransomware", md)

    def test_no_kev_badge_without_in_kev(self):
        html = _body(generate_html_report([_f()], "now"))
        self.assertNotIn("badge-kevdue", html)
        self.assertNotIn("badge-ransom", html)


class ButtonTests(unittest.TestCase):
    def test_poc_requires_true_and_safe_url(self):
        ok = _f(enrichment={"exploit_available": True, "exploit_url": "https://github.com/x/poc"})
        self.assertEqual(_poc_url(ok), "https://github.com/x/poc")
        for e in ({"exploit_available": True, "exploit_url": "javascript:alert(1)"},
                  {"exploit_available": True, "exploit_url": ""},
                  {"exploit_available": None, "exploit_url": "https://github.com/x/poc"},
                  {"exploit_available": False, "exploit_url": "https://github.com/x/poc"},
                  {"exploit_available": "true", "exploit_url": "https://github.com/x/poc"}):
            self.assertEqual(_poc_url(_f(enrichment=e)), "", e)
        self.assertEqual(_poc_url(_f(enrichment=None)), "")

    def test_poc_button_html(self):
        html = generate_html_report([_f(enrichment={"exploit_available": True,
                                                    "exploit_url": "https://github.com/x/poc"})], "now")
        self.assertIn('<a class="btn btn-poc" href="https://github.com/x/poc" target="_blank" '
                      'rel="noopener noreferrer">PoC Available</a>', html)
        html = _body(generate_html_report([_f(enrichment={"exploit_available": True,
                                                          "exploit_url": "javascript:alert(1)"})], "now"))
        self.assertNotIn("btn-poc", html)
        self.assertNotIn("javascript:", html)

    def test_advisory_hidden_for_nvd_and_unsafe(self):
        adv = lambda u: _advisory_url(_f(enrichment={"vendor_advisory": u}))
        self.assertEqual(adv("https://www.fortiguard.com/psirt/FG-IR-1"), "https://www.fortiguard.com/psirt/FG-IR-1")
        self.assertEqual(adv("https://nvd.nist.gov/vuln/detail/CVE-2026-0001"), "")
        self.assertEqual(adv("https://NVD.NIST.GOV/vuln/detail/CVE-2026-0001"), "")
        self.assertEqual(adv("https://sub.nvd.nist.gov/x"), "")
        self.assertEqual(adv("https://nvd.nist.gov.evil.example/x"), "https://nvd.nist.gov.evil.example/x")
        self.assertEqual(adv("javascript:alert(1)"), "")
        self.assertEqual(adv("data:text/html,x"), "")
        self.assertEqual(adv("http://[::1"), "")

    def test_advisory_button_html(self):
        html = generate_html_report([_f(enrichment={"vendor_advisory": "https://vendor.example/adv?a=1&b=2"})], "now")
        self.assertIn('class="btn btn-advisory" href="https://vendor.example/adv?a=1&amp;b=2"', html)
        html = _body(generate_html_report([_f(enrichment={"vendor_advisory": "https://nvd.nist.gov/x"})], "now"))
        self.assertNotIn("btn-advisory", html)


class VersionsLineTests(unittest.TestCase):
    def test_presence(self):
        both = generate_html_report([_f(enrichment={"affected_versions": "< 1.27.3",
                                                     "fixed_version": "1.27.3"})], "now")
        self.assertIn('Affected: <code>&lt; 1.27.3</code> → Fixed: <code>1.27.3</code>', both)
        only_fixed = generate_html_report([_f(enrichment={"affected_versions": "Unknown",
                                                          "fixed_version": "2.0"})], "now")
        self.assertIn('<div class="versions">Fixed: <code>2.0</code></div>', only_fixed)
        self.assertNotIn("Affected:", only_fixed)
        none = _body(generate_html_report([_f(enrichment={"affected_versions": "", "fixed_version": "N/A"}),
                                           _f()], "now"))
        self.assertNotIn('class="versions"', none)

    def test_markdown(self):
        md = generate_markdown_report([_f(enrichment={"affected_versions": "< 1.27.3",
                                                      "fixed_version": "1.27.3"})], "now")
        self.assertIn("**Affected:** &lt; 1.27.3 → **Fixed:** 1.27.3", md)


class StatsTests(unittest.TestCase):
    FINDINGS = [
        _f(in_kev=True, epss=0.9, stack_match=["nginx"]),
        _f(is_kev=True, epss=0.5),
        _f(epss=0.49, stack_match=["eks"]),
        _f(epss=None),
    ]

    def _stat(self, html, label):
        m = re.search(r'<span class="stat-value[^"]*">(\d+)</span><span class="stat-label">'
                      + re.escape(label) + "</span>", html)
        return int(m.group(1)) if m else None

    def test_counts_with_stack(self):
        html = generate_html_report(self.FINDINGS, "now", my_stack=["nginx", "eks"])
        self.assertEqual(self._stat(html, "In KEV"), 2)
        self.assertEqual(self._stat(html, "High EPSS"), 2)
        self.assertEqual(self._stat(html, "My Stack"), 2)
        self.assertEqual(self._stat(html, "Total"), 4)
        md = generate_markdown_report(self.FINDINGS, "now", my_stack=["nginx", "eks"])
        self.assertIn("📈 High EPSS: 2", md)
        self.assertIn("🎯 My Stack: 2", md)

    def test_no_stack_output_when_my_stack_empty(self):
        # stale stack_match values on findings must not leak out when my_stack is empty
        for stack in (None, []):
            html = _body(generate_html_report(self.FINDINGS, "now", my_stack=stack))
            md = generate_markdown_report(self.FINDINGS, "now", my_stack=stack)
            self.assertIsNone(self._stat(html, "My Stack"))
            self.assertEqual(self._stat(html, "High EPSS"), 2)
            for needle in ("My Stack", "badge-stack", "stack-section", "All Findings"):
                self.assertNotIn(needle, html)
            self.assertNotIn("My Stack", md)


class MyStackSectionTests(unittest.TestCase):
    FINDINGS = [  # already in the main sort order; titles name the expected stack position
        _f(title="no-match", in_kev=True, epss=0.99, stack_match=[]),
        _f(title="S4 zd-no-epss", epss=None, stack_match=["a"], published="2026-11-17"),
        _f(title="S5 not-zd-no-epss", epss=None, is_zero_day=False, stack_match=["a"], published="2026-11-18"),
        _f(title="S3 low-epss", epss=0.05, stack_match=["a"]),
        _f(title="S1 kev-low-epss", in_kev=True, epss=0.01, stack_match=["a", "b"]),
        _f(title="S2 high-epss", epss=0.8, stack_match=["b"]),
        _f(title="S6 older", epss=None, is_zero_day=False, stack_match=["a"], published="2026-11-01"),
    ]
    EXPECTED = ["S1 kev-low-epss", "S2 high-epss", "S3 low-epss", "S4 zd-no-epss",
                "S5 not-zd-no-epss", "S6 older"]

    def _order(self, text, titles):
        return sorted(titles, key=text.index)

    def test_html_section_order_and_full_list_unchanged(self):
        html = _body(generate_html_report(self.FINDINGS, "now", my_stack=["a", "b"]))
        stack_part, all_part = html.split("All Findings", 1)
        stack_part = stack_part.split("🎯 My Stack", 1)[1]
        self.assertNotIn("no-match", stack_part)
        self.assertEqual(self._order(stack_part, self.EXPECTED), self.EXPECTED)
        all_titles = [f["title"] for f in self.FINDINGS]
        self.assertEqual(self._order(all_part, all_titles), all_titles)
        self.assertIn('<span class="badge badge-stack">b</span>', html)
        self.assertIn("stack-head", html)

    def test_markdown_highlights_at_top(self):
        md = generate_markdown_report(self.FINDINGS, "now", my_stack=["a", "b"])
        self.assertIn("## 🎯 My Stack Highlights", md)
        top, full = md.split("## 1. ", 1)
        self.assertIn("My Stack Highlights", top)
        self.assertEqual(self._order(top, self.EXPECTED), self.EXPECTED)
        self.assertNotIn("no-match", top)
        self.assertIn("**My Stack:** `a`, `b`", full)

    def test_no_section_when_no_matches(self):
        findings = [_f(stack_match=[])]
        html = _body(generate_html_report(findings, "now", my_stack=["nginx"]))
        self.assertNotIn("stack-section", html)
        self.assertIn('<span class="stat-value stack">0</span>', html)
        md = generate_markdown_report(findings, "now", my_stack=["nginx"])
        self.assertNotIn("My Stack Highlights", md)


class SafetyTests(unittest.TestCase):
    EVIL = _f(title='<script>alert("x")</script>', summary="<img src=x onerror=alert(1)>",
              source="<b>src</b>", in_kev=True, kev_due_date="<i>soon</i>", stack_match=["<x>"],
              enrichment={"affected_versions": "<svg/onload=1>", "fixed_version": "\"'><a>",
                          "exploit_available": True, "exploit_url": 'https://e.example/"><script>',
                          "vendor_advisory": "https://v.example/'onmouseover='x"})

    def test_html_escapes_everything(self):
        html = generate_html_report([self.EVIL], "now", my_stack=["<x>"])
        self.assertNotIn("<script>", html)
        self.assertIn("&lt;script&gt;alert(&quot;x&quot;)&lt;/script&gt;", html)
        for raw in ("<img", "<b>src", "<i>soon", "<svg", "<x>", "'onmouseover='", '"><a>'):
            self.assertNotIn(raw, html)

    def test_markdown_escapes_title(self):
        md = generate_markdown_report([self.EVIL], "now", my_stack=["<x>"])
        self.assertNotIn("<script>", md)
        self.assertNotIn("<img", md)
        self.assertIn("&lt;script&gt;", md)

    def test_no_external_assets(self):
        html = generate_html_report([self.EVIL, _f(epss=0.7)], "now",
                                    repo_url="https://github.com/o/r", my_stack=["<x>"])
        self.assertNotRegex(html, r"(?i)<script\b")
        self.assertNotRegex(html, r"(?i)<link\b")
        self.assertNotRegex(html, r"(?i)\bsrc\s*=\s*[\"']?\s*(https?:)?//")
        self.assertNotRegex(html, r"(?i)@import|url\(")

    def test_unsafe_repo_url_not_linked(self):
        html = generate_html_report([], "now", repo_url="javascript:alert(1)")
        self.assertNotIn("javascript:", html)


if __name__ == "__main__":
    unittest.main()
