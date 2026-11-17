import unittest
from unittest import mock

import requests

from pulse import feeds, intel
from pulse.filter import attach_cve_ids, filter_zero_days, sort_findings

KEV_RECORDS = [
    {
        "cveID": "CVE-2021-44228", "vendorProject": "Apache", "product": "Log4j2",
        "vulnerabilityName": "Apache Log4j2 RCE", "dateAdded": "2021-12-10",
        "shortDescription": "JNDI injection.", "requiredAction": "Apply updates.",
        "dueDate": "2021-12-24", "knownRansomwareCampaignUse": "Known",
    },
    {
        "cveID": "CVE-2021-45046", "vendorProject": "Apache", "product": "Log4j2",
        "vulnerabilityName": "Apache Log4j2 Deserialization", "dateAdded": "2023-05-01",
        "shortDescription": "Incomplete fix.", "requiredAction": "Apply updates.",
        "dueDate": "2023-05-22", "knownRansomwareCampaignUse": "Unknown",
    },
]


def _resp(payload=None, status=200, exc=None):
    r = mock.Mock()
    r.status_code = status
    if status >= 400:
        r.raise_for_status.side_effect = requests.HTTPError(f"{status}")
    else:
        r.raise_for_status.return_value = None
    if exc is not None:
        r.json.side_effect = exc
    else:
        r.json.return_value = payload
    return r


def _epss_payload(cves, score=0.5):
    return {"status": "OK", "data": [
        {"cve": c, "epss": str(score), "percentile": "0.9", "date": "2026-11-17"} for c in cves
    ]}


class KevCatalogTests(unittest.TestCase):
    @mock.patch("pulse.intel.requests.get")
    def test_load_success_builds_lookup(self, get):
        get.return_value = _resp({"vulnerabilities": KEV_RECORDS})
        raw, lookup = intel.load_kev_catalog()
        self.assertEqual(len(raw), 2)
        self.assertEqual(get.call_count, 1)
        self.assertEqual(lookup["CVE-2021-44228"], {
            "date_added": "2021-12-10", "due_date": "2021-12-24",
            "vendor": "Apache", "product": "Log4j2", "ransomware": True,
        })
        self.assertFalse(lookup["CVE-2021-45046"]["ransomware"])

    @mock.patch("pulse.intel.requests.get")
    def test_load_failure_returns_none(self, get):
        get.side_effect = requests.ConnectionError("blocked")
        self.assertIsNone(intel.load_kev_catalog())

    @mock.patch("pulse.intel.requests.get")
    def test_load_http_error_and_bad_shape_return_none(self, get):
        get.return_value = _resp(status=503)
        self.assertIsNone(intel.load_kev_catalog())
        get.return_value = _resp({"unexpected": []})
        self.assertIsNone(intel.load_kev_catalog())

    def test_fetch_cisa_kev_none_catalog_returns_empty(self):
        self.assertEqual(feeds.fetch_cisa_kev(24, None), [])

    def test_fetch_cisa_kev_builds_new_additions_from_raw_records(self):
        recent = dict(KEV_RECORDS[0], cveID="CVE-2026-0001", dateAdded="2999-01-01")
        entries = feeds.fetch_cisa_kev(24, KEV_RECORDS + [recent])
        self.assertEqual([e["id"] for e in entries], ["CVE-2026-0001"])
        e = entries[0]
        self.assertTrue(e["is_kev"])
        self.assertEqual(e["cve_ids"], ["CVE-2026-0001"])
        self.assertEqual(e["source"], "CISA KEV")
        self.assertIn("Required action: Apply updates.", e["summary"])


class KevGateTests(unittest.TestCase):
    def _lookup(self):
        with mock.patch("pulse.intel.requests.get",
                        return_value=_resp({"vulnerabilities": KEV_RECORDS})):
            return intel.load_kev_catalog()[1]

    @mock.patch("pulse.filter._load_keywords", return_value=(["zero-day"], ["remote code execution"]))
    def test_keywordless_rss_entry_citing_old_kev_cve_passes_gate(self, _kw):
        rss_entry = {  # shape produced by feeds._parse_rss: no cve_ids, no keyword
            "id": "https://blog.example/post", "title": "Patch roundup for this week",
            "summary": "Several teams still run builds affected by CVE-2021-44228.",
            "link": "https://blog.example/post", "published": "2026-11-17T00:00:00+00:00",
            "source": "Example Blog", "tags": [],
        }
        control = dict(rss_entry, id="other", summary="Nothing to see here.")
        entries = [rss_entry, control]
        attach_cve_ids(entries)
        intel.annotate_kev(entries, self._lookup())
        out = filter_zero_days(entries)
        self.assertEqual(len(out), 1)
        f = out[0]
        self.assertEqual(f["cve_ids"], ["CVE-2021-44228"])
        self.assertTrue(f["in_kev"])
        self.assertFalse(f.get("is_kev", False))
        self.assertTrue(f["is_zero_day"])
        self.assertEqual(f["kev_due_date"], "2021-12-24")
        self.assertTrue(f["kev_ransomware"])

    @mock.patch("pulse.filter._load_keywords", return_value=(["zero-day"], []))
    def test_kev_catalog_unavailable_leaves_in_kev_false(self, _kw):
        entries = [{"id": "x", "title": "t", "summary": "CVE-2021-44228", "published": ""}]
        attach_cve_ids(entries)
        intel.annotate_kev(entries, None)
        self.assertFalse(entries[0]["in_kev"])
        self.assertEqual(filter_zero_days(entries), [])

    def test_attach_cve_ids_keeps_structured_ids(self):
        entries = [{"title": "CVE-2020-0001", "summary": "", "cve_ids": ["CVE-2024-9999"]},
                   {"title": "see cve-2020-0002 and CVE-2020-0002", "summary": "CVE-2020-0003"}]
        attach_cve_ids(entries)
        self.assertEqual(entries[0]["cve_ids"], ["CVE-2024-9999"])
        self.assertEqual(entries[1]["cve_ids"], ["CVE-2020-0002", "CVE-2020-0003"])


class AnnotateTests(unittest.TestCase):
    LOOKUP = {
        "CVE-2021-0001": {"date_added": "2021-01-01", "due_date": "2021-03-01",
                          "vendor": "A", "product": "a", "ransomware": False},
        "CVE-2021-0002": {"date_added": "2021-02-01", "due_date": "2021-02-15",
                          "vendor": "B", "product": "b", "ransomware": True},
    }
    EPSS = {
        "CVE-2021-0001": {"epss": 0.04, "percentile": 0.70, "date": "d"},
        "CVE-2021-0003": {"epss": 0.61, "percentile": 0.98, "date": "d"},
    }

    def test_multi_cve_any_kev_earliest_due_and_max_epss(self):
        f = {"cve_ids": ["CVE-2021-0001", "CVE-2021-0002", "CVE-2021-0003"]}
        intel.annotate([f], self.LOOKUP, self.EPSS)
        self.assertTrue(f["in_kev"])
        self.assertEqual(f["kev_due_date"], "2021-02-15")  # earliest due date wins
        self.assertEqual(f["kev_vendor"], "B")
        self.assertTrue(f["kev_ransomware"])
        self.assertEqual(f["epss"], 0.61)
        self.assertEqual(f["epss_percentile"], 0.98)

    def test_no_match(self):
        f = {"cve_ids": ["CVE-2099-0001"]}
        intel.annotate([f], self.LOOKUP, self.EPSS)
        self.assertFalse(f["in_kev"])
        self.assertIsNone(f["kev_due_date"])
        self.assertIsNone(f["epss"])
        self.assertIsNone(f["epss_percentile"])

    def test_sources_unavailable(self):
        f = {"cve_ids": ["CVE-2021-0001"]}
        intel.annotate([f], None, None)
        self.assertFalse(f["in_kev"])
        self.assertIsNone(f["epss"])
        self.assertIsNone(f["epss_percentile"])


class EpssTests(unittest.TestCase):
    CVES = [f"CVE-2026-{i:05d}" for i in range(250)]

    @mock.patch("pulse.intel.requests.get")
    def test_batches_of_100(self, get):
        get.side_effect = lambda url, **kw: _resp(_epss_payload(url.split("cve=", 1)[1].split(",")))
        scores = intel.fetch_epss(self.CVES + self.CVES[:10] + ["not-a-cve"])
        self.assertEqual(get.call_count, 3)
        sizes = [len(c.args[0].split("cve=", 1)[1].split(",")) for c in get.call_args_list]
        self.assertEqual(sizes, [100, 100, 50])
        for c in get.call_args_list:
            self.assertTrue(c.args[0].startswith("https://api.first.org/data/v1/epss?cve="))
            self.assertEqual(c.kwargs["timeout"], 30)
        self.assertEqual(len(scores), 250)
        self.assertEqual(scores["CVE-2026-00007"], {"epss": 0.5, "percentile": 0.9, "date": "2026-11-17"})

    @mock.patch("pulse.intel.requests.get")
    def test_total_failure_returns_none(self, get):
        get.side_effect = requests.Timeout("timeout")
        self.assertIsNone(intel.fetch_epss(self.CVES))

    @mock.patch("pulse.intel.requests.get")
    def test_partial_failure_returns_none(self, get):
        get.side_effect = [
            _resp(_epss_payload(self.CVES[:100])),
            _resp(status=500),
            _resp(_epss_payload(self.CVES[200:])),
        ]
        self.assertIsNone(intel.fetch_epss(self.CVES))

    @mock.patch("pulse.intel.requests.get")
    def test_bad_shape_returns_none(self, get):
        for payload in ({"status": "OK"}, [], {"data": [{"cve": "CVE-2026-00001", "epss": "x", "percentile": "1"}]},
                        {"data": [{"cve": "CVE-2026-00001", "epss": "7", "percentile": "0.1"}]}):
            get.side_effect = None
            get.return_value = _resp(payload)
            self.assertIsNone(intel.fetch_epss(["CVE-2026-00001"]), payload)
        get.return_value = _resp(exc=ValueError("not json"))
        self.assertIsNone(intel.fetch_epss(["CVE-2026-00001"]))

    @mock.patch("pulse.intel.requests.get")
    def test_no_cves_makes_no_request(self, get):
        self.assertEqual(intel.fetch_epss([]), {})
        get.assert_not_called()


class SortTests(unittest.TestCase):
    def test_in_kev_sorts_first_then_existing_order(self):
        findings = [
            {"id": "zd-new", "is_zero_day": True, "published": "2026-11-17"},
            {"id": "hs", "is_high_severity": True, "published": "2026-11-18"},
            {"id": "old-kev", "in_kev": True, "is_zero_day": True, "published": "2026-11-01"},
            {"id": "kev-feed", "is_kev": True, "is_zero_day": True, "published": "2026-11-10"},
            {"id": "zd-old", "is_zero_day": True, "published": "2026-11-02"},
        ]
        order = [f["id"] for f in sort_findings(findings)]
        self.assertEqual(order, ["kev-feed", "old-kev", "zd-new", "zd-old", "hs"])


if __name__ == "__main__":
    unittest.main()
