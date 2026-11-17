import json
import os
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

from pulse import state as pstate
from pulse.report import (generate_changes_markdown, generate_html_report,
                          generate_markdown_report, save_reports)
from pulse.state import diff_state, load_state, prune, save_state, stack_terms_hash

NOW = datetime(2026, 11, 17, 12, 0, tzinfo=timezone.utc)
STACK = ["nginx", "linux"]
H = stack_terms_hash(STACK)


def _entry(in_kev=False, epss=None, stack_match=None, h=H, first_seen=None, last_seen=None):
    fs = first_seen or (NOW - timedelta(days=1)).isoformat()
    return {"first_seen": fs, "last_seen": last_seen or fs, "in_kev": in_kev, "epss": epss,
            "stack_match": stack_match or [], "stack_terms_hash": h}


def _state(cves, h=H):
    return {"stack_terms_hash": h, "generated_at": "x", "run_id": "1", "cves": cves}


def _finding(cve, title="t", stack_match=None, link="https://example.com/a"):
    return {"title": title, "link": link, "cve_ids": [cve], "stack_match": stack_match or []}


def _kev(*cves):
    return {c: {"date_added": "2026-11-16", "due_date": "2026-12-07", "ransomware": False} for c in cves}


def _epss(**scores):
    return {k.replace("_", "-"): {"epss": v, "percentile": 0.9, "date": "d"} for k, v in scores.items()}


def kinds(changes):
    return [(c["kind"], c["cve"]) for c in changes]


class BaselineTests(unittest.TestCase):
    def test_no_state_is_baseline(self):
        f = [_finding("CVE-2026-0001", stack_match=["nginx"])]
        new, changes = diff_state(None, f, _kev("CVE-2026-0001"), _epss(CVE_2026_0001=0.9), STACK, now=NOW)
        self.assertEqual(changes, [])
        e = new["cves"]["CVE-2026-0001"]
        self.assertEqual((e["in_kev"], e["epss"], e["stack_match"], e["stack_terms_hash"]),
                         (True, 0.9, ["nginx"], H))
        self.assertEqual(new["stack_terms_hash"], H)

    def test_missing_and_corrupt_state_file(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "last_run.json")
            self.assertIsNone(load_state(p))
            Path(p).write_text("{not json")
            with self.assertLogs("pulse.state", "WARNING"):
                self.assertIsNone(load_state(p))
            Path(p).write_text('["a list"]')
            with self.assertLogs("pulse.state", "WARNING"):
                self.assertIsNone(load_state(p))

    def test_round_trip_and_env_path(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "sub", "last_run.json")
            st = _state({"CVE-2026-0001": _entry(in_kev=True, epss=0.2)})
            with mock.patch.dict(os.environ, {"PULSE_STATE_PATH": p}):
                save_state(st)
                loaded = load_state()
            self.assertEqual(loaded["cves"]["CVE-2026-0001"]["epss"], 0.2)
            self.assertTrue(loaded["cves"]["CVE-2026-0001"]["in_kev"])


class KevTests(unittest.TestCase):
    def test_entered_kev_for_watched_cve(self):
        st = _state({"CVE-2026-0001": _entry(in_kev=False)})
        _, changes = diff_state(st, [_finding("CVE-2026-0001", title="Bug")], _kev("CVE-2026-0001"), {}, STACK, now=NOW)
        self.assertEqual(kinds(changes), [("entered_kev", "CVE-2026-0001")])
        self.assertEqual(changes[0]["kev_due_date"], "2026-12-07")
        self.assertEqual(changes[0]["title"], "Bug")

    def test_entered_kev_for_watched_cve_absent_this_run(self):
        st = _state({"CVE-2026-0001": _entry(in_kev=False)})
        _, changes = diff_state(st, [], _kev("CVE-2026-0001"), {}, STACK, now=NOW)
        self.assertEqual(kinds(changes), [("entered_kev", "CVE-2026-0001")])
        self.assertIsNone(changes[0]["title"])

    def test_first_seen_kev_cve_no_change(self):
        _, changes = diff_state(_state({}), [_finding("CVE-2026-0002")], _kev("CVE-2026-0002"), {}, STACK, now=NOW)
        self.assertEqual(changes, [])

    def test_kev_none_keeps_stored_and_emits_nothing(self):
        st = _state({"CVE-2026-0001": _entry(in_kev=False), "CVE-2026-0003": _entry(in_kev=True)})
        new, changes = diff_state(st, [_finding("CVE-2026-0001")], None, {}, STACK, now=NOW)
        self.assertEqual(changes, [])
        self.assertIs(new["cves"]["CVE-2026-0001"]["in_kev"], False)
        self.assertIs(new["cves"]["CVE-2026-0003"]["in_kev"], True)

    def test_unknown_kev_status_is_baseline(self):
        # first seen while the catalog was down → stored None → no alert later
        new, _ = diff_state(_state({}), [_finding("CVE-2026-0004")], None, {}, STACK, now=NOW)
        self.assertIsNone(new["cves"]["CVE-2026-0004"]["in_kev"])
        _, changes = diff_state(new, [], _kev("CVE-2026-0004"), {}, STACK, now=NOW)
        self.assertEqual(changes, [])


class EpssTests(unittest.TestCase):
    def _run(self, old, new, watched=True):
        st = _state({"CVE-2026-0001": _entry(epss=old)} if watched else {})
        return diff_state(st, [_finding("CVE-2026-0001")], {}, _epss(CVE_2026_0001=new), STACK, now=NOW)

    def test_cross_low_threshold(self):
        _, changes = self._run(0.08, 0.12)
        self.assertEqual(kinds(changes), [("epss_crossed", "CVE-2026-0001")])
        self.assertEqual((changes[0]["threshold"], changes[0]["old_epss"], changes[0]["new_epss"]), (0.1, 0.08, 0.12))

    def test_cross_high_threshold(self):
        _, changes = self._run(0.3, 0.61)
        self.assertEqual(changes[0]["threshold"], 0.5)

    def test_both_thresholds_reports_highest(self):
        _, changes = self._run(0.04, 0.61)
        self.assertEqual(len(changes), 1)
        self.assertEqual(changes[0]["threshold"], 0.5)

    def test_no_cross(self):
        self.assertEqual(self._run(0.12, 0.4)[1], [])
        self.assertEqual(self._run(0.6, 0.3)[1], [])

    def test_null_stored_is_baseline(self):
        new, changes = self._run(None, 0.7)
        self.assertEqual(changes, [])
        self.assertEqual(new["cves"]["CVE-2026-0001"]["epss"], 0.7)

    def test_first_seen_high_epss_no_change(self):
        self.assertEqual(self._run(None, 0.9, watched=False)[1], [])

    def test_epss_none_keeps_stored_and_emits_nothing(self):
        st = _state({"CVE-2026-0001": _entry(epss=0.05)})
        new, changes = diff_state(st, [_finding("CVE-2026-0001")], {}, None, STACK, now=NOW)
        self.assertEqual(changes, [])
        self.assertEqual(new["cves"]["CVE-2026-0001"]["epss"], 0.05)

    def test_unscored_cve_keeps_stored(self):
        st = _state({"CVE-2026-0001": _entry(epss=0.05)})
        new, _ = diff_state(st, [], {}, {}, STACK, now=NOW)
        self.assertEqual(new["cves"]["CVE-2026-0001"]["epss"], 0.05)


class StackTests(unittest.TestCase):
    def test_first_seen_match_emits(self):
        f = [_finding("CVE-2026-0005", stack_match=["nginx"])]
        _, changes = diff_state(_state({}), f, {}, {}, STACK, now=NOW)
        self.assertEqual(kinds(changes), [("new_stack_hit", "CVE-2026-0005")])
        self.assertEqual(changes[0]["stack_match"], ["nginx"])

    def test_watched_cve_gains_match_same_hash(self):
        st = _state({"CVE-2026-0005": _entry(stack_match=[])})
        f = [_finding("CVE-2026-0005", stack_match=["linux"])]
        _, changes = diff_state(st, f, {}, {}, STACK, now=NOW)
        self.assertEqual(kinds(changes), [("new_stack_hit", "CVE-2026-0005")])

    def test_already_matching_no_change(self):
        st = _state({"CVE-2026-0005": _entry(stack_match=["nginx"])})
        f = [_finding("CVE-2026-0005", stack_match=["nginx", "linux"])]
        self.assertEqual(diff_state(st, f, {}, {}, STACK, now=NOW)[1], [])

    def test_my_stack_edit_rebaselines(self):
        old_h = stack_terms_hash(["nginx"])
        st = _state({"CVE-2026-0005": _entry(stack_match=[], h=old_h)}, h=old_h)
        f = [_finding("CVE-2026-0005", stack_match=["linux"]),
             _finding("CVE-2026-0006", stack_match=["linux"])]  # first-seen too
        new, changes = diff_state(st, f, {}, {}, STACK, now=NOW)
        self.assertEqual(changes, [])
        self.assertEqual(new["stack_terms_hash"], H)
        self.assertEqual(new["cves"]["CVE-2026-0005"]["stack_terms_hash"], H)
        self.assertEqual(new["cves"]["CVE-2026-0005"]["stack_match"], ["linux"])

    def test_absent_cve_keeps_match_and_reappearing_with_old_hash_does_not_emit(self):
        old_h = stack_terms_hash(["nginx"])
        st = _state({"CVE-2026-0007": _entry(stack_match=[], h=old_h),
                     "CVE-2026-0008": _entry(stack_match=["nginx"], h=old_h)}, h=old_h)
        # run 1: stack edited, both CVEs absent → stored values and hashes kept
        new, changes = diff_state(st, [], {}, {}, STACK, now=NOW)
        self.assertEqual(changes, [])
        self.assertEqual(new["cves"]["CVE-2026-0008"]["stack_match"], ["nginx"])
        self.assertEqual(new["cves"]["CVE-2026-0007"]["stack_terms_hash"], old_h)
        # run 2: same terms as run 1, CVE-0007 reappears matching → silent re-baseline
        new2, changes2 = diff_state(new, [_finding("CVE-2026-0007", stack_match=["linux"])],
                                    {}, {}, STACK, now=NOW + timedelta(hours=6))
        self.assertEqual(changes2, [])
        self.assertEqual(new2["cves"]["CVE-2026-0007"]["stack_terms_hash"], H)

    def test_empty_stack_never_emits(self):
        _, changes = diff_state(_state({}, h=stack_terms_hash([])),
                                [_finding("CVE-2026-0005", stack_match=["x"])], {}, {}, [], now=NOW)
        self.assertEqual(changes, [])

    def test_stack_match_union_across_findings(self):
        f = [_finding("CVE-2026-0009", stack_match=["nginx"]),
             _finding("CVE-2026-0009", stack_match=["linux"])]
        new, _ = diff_state(None, f, {}, {}, STACK, now=NOW)
        self.assertEqual(new["cves"]["CVE-2026-0009"]["stack_match"], ["nginx", "linux"])

    def test_hash_is_order_and_case_insensitive(self):
        self.assertEqual(stack_terms_hash(["Nginx", "linux"]), stack_terms_hash(["linux", "nginx", "NGINX"]))


class PruneTests(unittest.TestCase):
    def test_14_day_window(self):
        old = (NOW - timedelta(days=15)).isoformat()
        st = _state({"CVE-2026-0001": _entry(first_seen=old, last_seen=old),
                     "CVE-2026-0002": _entry()})
        new, _ = diff_state(st, [], {}, {}, STACK, now=NOW)
        self.assertEqual(sorted(new["cves"]), ["CVE-2026-0002"])

    def test_seen_again_refreshes_window(self):
        old = (NOW - timedelta(days=15)).isoformat()
        st = _state({"CVE-2026-0001": _entry(first_seen=old, last_seen=old)})
        new, _ = diff_state(st, [_finding("CVE-2026-0001")], {}, {}, STACK, now=NOW)
        self.assertEqual(new["cves"]["CVE-2026-0001"]["first_seen"], old)

    def test_cap_prunes_oldest_first_seen(self):
        cves = {f"CVE-2026-{i:05d}": _entry(first_seen=(NOW - timedelta(minutes=i)).isoformat())
                for i in range(1, 1006)}
        kept = prune(cves, NOW)
        self.assertEqual(len(kept), pstate.WATCH_CAP)
        self.assertIn("CVE-2026-00001", kept)
        self.assertNotIn("CVE-2026-01005", kept)

    def test_prune_after_diff(self):
        # a full watchlist still yields changes for an entry the cap later drops
        cves = {f"CVE-2026-{i:05d}": _entry(first_seen=(NOW - timedelta(minutes=i)).isoformat())
                for i in range(1, 1001)}
        cves["CVE-2026-01000"]["in_kev"] = False
        new_f = [_finding(f"CVE-2026-9{i:04d}") for i in range(5)]
        new, changes = diff_state(_state(cves), new_f, _kev("CVE-2026-01000"), {}, STACK, now=NOW)
        self.assertEqual(kinds(changes), [("entered_kev", "CVE-2026-01000")])
        self.assertNotIn("CVE-2026-01000", new["cves"])
        self.assertEqual(len(new["cves"]), 1000)


class OutputTests(unittest.TestCase):
    CHANGES = [
        {"kind": "entered_kev", "cve": "CVE-2026-0001", "title": "<script>x</script> @octocat",
         "link": "javascript:alert(1)", "kev_due_date": "2026-12-05"},
        {"kind": "epss_crossed", "cve": "CVE-2026-0002", "title": "B", "link": "https://e.com/b",
         "threshold": 0.5, "old_epss": 0.04, "new_epss": 0.61},
        {"kind": "new_stack_hit", "cve": "CVE-2026-0003", "title": None, "link": None,
         "stack_match": ["<nginx>"]},
    ]

    def test_section_omitted_when_empty(self):
        md = generate_markdown_report([], "now", None, [])
        html = generate_html_report([], "now", changes=[])
        self.assertNotIn("Changed since last run", md)
        self.assertNotIn("Changed since last run", html)
        self.assertEqual(generate_changes_markdown([]), "")

    def test_section_rendered_escaped_and_on_top(self):
        f = [{"title": "nginx bug", "cve_ids": ["CVE-2026-0003"], "stack_match": ["nginx"], "is_zero_day": True}]
        md = generate_markdown_report(f, "now", ["nginx"], self.CHANGES)
        html = generate_html_report(f, "now", my_stack=["nginx"], changes=self.CHANGES)
        for out in (md, html):
            self.assertIn("Changed since last run", out)
            self.assertNotIn("<script>", out)
            self.assertNotIn("javascript:", out)
            self.assertNotIn("<nginx>", out)
            self.assertIn("4% → 61%", out)
            self.assertIn("due 2026-12-05", out)
        self.assertNotIn("@octocat", md)   # mention neutralised on GitHub-rendered Markdown
        self.assertLess(md.index("Changed since last run"), md.index("My Stack Highlights"))
        self.assertLess(html.index("Changed since last run"), html.index("🎯 My Stack <span"))
        self.assertIn('href="https://e.com/b"', html)
        comment = generate_changes_markdown(self.CHANGES)
        self.assertEqual(comment.count("\n- "), 3)
        self.assertNotIn("@octocat", comment)

    def test_changes_json_carries_run_id_from_env(self):
        with tempfile.TemporaryDirectory() as d, \
                mock.patch.dict(os.environ, {"GITHUB_RUN_ID": "987654321"}):
            paths = save_reports([], os.path.join(d, "reports"), changes=self.CHANGES[1:2])
            data = json.loads(Path(paths["changes"]).read_text())
            latest = json.loads(Path(d, "reports", "latest.json").read_text())
            self.assertTrue(Path(d, "reports", "changes.md").read_text().startswith("## ⚡"))
        self.assertEqual(data["run_id"], "987654321")
        self.assertEqual(data["changes"][0]["cve"], "CVE-2026-0002")
        self.assertEqual(latest["changes"], data["changes"])

    def test_run_id_falls_back_to_local(self):
        env = {k: v for k, v in os.environ.items() if k != "GITHUB_RUN_ID"}
        with mock.patch.dict(os.environ, env, clear=True):
            self.assertEqual(pstate.current_run_id(), "local")


if __name__ == "__main__":
    unittest.main()
