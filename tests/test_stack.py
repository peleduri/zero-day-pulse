import unittest
from unittest import mock

from pulse import filter as pfilter
from pulse.filter import annotate_stack, stack_match


class StackMatchTests(unittest.TestCase):
    def test_word_boundary_eks(self):
        self.assertEqual(stack_match({"title": "Amazon EKS privilege escalation"}, ["eks"]), ["eks"])
        self.assertEqual(stack_match({"title": "Patched within weeks"}, ["eks"]), [])

    def test_case_insensitive_keeps_config_spelling(self):
        self.assertEqual(stack_match({"summary": "NGINX ingress bug"}, ["Nginx"]), ["Nginx"])

    def test_config_order_and_dedup(self):
        f = {"title": "linux kernel and nginx", "summary": "Linux again"}
        self.assertEqual(stack_match(f, ["nginx", "linux", "LINUX", "nginx", "absent"]),
                         ["nginx", "linux"])

    def test_kev_vendor_product_tags_and_affected_products(self):
        self.assertEqual(stack_match({"title": "x", "kev_vendor": "Fortinet"}, ["fortinet"]), ["fortinet"])
        self.assertEqual(stack_match({"title": "x", "kev_product": "FortiOS"}, ["fortios"]), ["fortios"])
        self.assertEqual(stack_match({"title": "x", "tags": ["kubernetes", "k8s"]}, ["k8s"]), ["k8s"])
        self.assertEqual(
            stack_match({"title": "x", "enrichment": {"affected_products": "OpenSSL 3.x, curl"}}, ["curl"]),
            ["curl"])
        self.assertEqual(
            stack_match({"title": "x", "enrichment": {"affected_products": ["Redis"]}}, ["redis"]),
            ["redis"])
        self.assertEqual(stack_match({"title": "x", "enrichment": None}, ["redis"]), [])

    def test_special_char_terms(self):
        self.assertEqual(stack_match({"title": "Bug in C++ runtime"}, ["c++"]), ["c++"])
        self.assertEqual(stack_match({"title": "Bug in c++17 parser"}, ["c++"]), [])
        self.assertEqual(stack_match({"title": "Microsoft .NET Framework RCE"}, [".net"]), [".net"])
        self.assertEqual(stack_match({"title": "visit example.network"}, [".net"]), [])
        self.assertEqual(stack_match({"title": "Node.js flaw"}, ["node.js"]), ["node.js"])
        self.assertEqual(stack_match({"title": "Nodexjs"}, ["node.js"]), [])  # dot is literal

    def test_empty_terms(self):
        self.assertEqual(stack_match({"title": "nginx"}, []), [])
        findings = [{"title": "nginx"}]
        annotate_stack(findings, [])
        self.assertEqual(findings[0]["stack_match"], [])

    def test_load_my_stack(self):
        cases = [({"my_stack": ["nginx", " eks ", "", None, 5]}, ["nginx", "eks", "5"]),
                 ({"my_stack": []}, []), ({}, []), ({"my_stack": None}, []),
                 ({"my_stack": "nginx"}, [])]
        for cfg, expected in cases:
            with mock.patch("pulse.filter.yaml.safe_load", return_value=cfg):
                self.assertEqual(pfilter.load_my_stack(), expected, cfg)

    def test_shipped_config_my_stack_is_empty(self):
        self.assertEqual(pfilter.load_my_stack(), [])


if __name__ == "__main__":
    unittest.main()
