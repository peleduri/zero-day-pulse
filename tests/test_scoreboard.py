"""Beat KEV scoreboard (design/beat-kev-scoreboard.md, decision 10)."""
import json
import os
import tempfile
import unittest
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

from pulse import scoreboard as sbm
from pulse.filter import attach_cve_ids, filter_zero_days
from pulse.intel import annotate_kev
from pulse.report import generate_html_report, generate_markdown_report, save_reports

NOW = datetime(2026, 11, 17, 12, 0, tzinfo=timezone.utc)
GO_LIVE = date(2026, 8, 1)          # well past warm-up for November rows
ZD = ["zero-day", "exploited in the wild"]


def _entry(title, cves, summary="", published="2026-11-17T08:00:00+00:00", source="News",
           link="https://news.example/a", is_kev=False, **extra):
    e = {"title": title, "summary": summary, "cve_ids": list(cves), "published": published,
         "source": source, "link": link}
    if is_kev:
        e["is_kev"] = True
    e.update(extra)
    return e


def _rec(cve, added, vendor="Acme", product="Widget"):
    return {"cveID": cve, "dateAdded": added, "vendorProject": vendor, "product": product}


def _row(cve, added, bucket, lead=None, vendor="Acme", source="News", link="https://n.example/x"):
    return {"cve": cve, "kev_date_added": added, "vendor": vendor, "product": "P",
            "cve_year": int(cve.split("-")[1]), "observed_at": None if bucket == "missed" else "x",
            "source": None if bucket == "missed" else source,
            "link": None if bucket == "missed" else link,
            "lead_days": lead, "bucket": bucket}


class _TmpDir(unittest.TestCase):
    def setUp(self):
        self._d = tempfile.TemporaryDirectory()
        self.dir = Path(self._d.name)
        self.sig = str(self.dir / "first_signal.json")
        self.sb = str(self.dir / "kev_scoreboard.jsonl")

    def tearDown(self):
        self._d.cleanup()


# ── signal predicate ──────────────────────────────────────────────────────────

class SignalTests(unittest.TestCase):
    def test_keyword_match_on_own_text(self):
        found, _ = sbm.collect_signals([_entry("Acme zero-day exploited", ["CVE-2026-1000"])], {}, ZD)
        self.assertEqual(list(found), ["CVE-2026-1000"])
        found, _ = sbm.collect_signals([_entry("Acme patch notes", ["CVE-2026-1000"])], {}, ZD)
        self.assertEqual(found, {})

    def test_ignores_in_kev_and_is_zero_day(self):
        # flags alone (no keyword in the text) never make a signal
        e = _entry("Acme advisory", ["CVE-2026-1000"], in_kev=True, is_zero_day=True)
        self.assertEqual(sbm.collect_signals([e], {}, ZD)[0], {})
        # keyword in text: the flags don't matter either way
        e = _entry("Acme zero-day", ["CVE-2026-1000"], in_kev=False, is_zero_day=False)
        self.assertIn("CVE-2026-1000", sbm.collect_signals([e], {}, ZD)[0])

    def test_kev_feed_entry_never_signals(self):
        e = _entry("CVE-2026-1000 — zero-day", ["CVE-2026-1000"], is_kev=True, source="CISA KEV")
        self.assertEqual(sbm.collect_signals([e], None, ZD)[0], {})

    def test_cve_already_in_kev_gets_no_signal(self):
        e = _entry("Old bug exploited in the wild", ["CVE-2026-1000", "CVE-2026-2000"])
        found, _ = sbm.collect_signals([e], {"CVE-2026-1000": {}}, ZD)
        self.assertEqual(list(found), ["CVE-2026-2000"])

    def test_roundup_over_two_cves_gives_no_signal(self):
        e = _entry("Patch Tuesday: one zero-day", ["CVE-2026-1001", "CVE-2026-1002", "CVE-2026-1003"])
        found, capped = sbm.collect_signals([e], {}, ZD)
        self.assertEqual(found, {})
        self.assertEqual(capped, 1)
        two = _entry("Chain zero-day", ["CVE-2026-1001", "CVE-2026-1002"])
        self.assertEqual(sorted(sbm.collect_signals([two], {}, ZD)[0]), ["CVE-2026-1001", "CVE-2026-1002"])

    def test_failed_catalog_load_still_records(self):
        found, _ = sbm.collect_signals([_entry("zero-day", ["CVE-2026-1000"])], None, ZD)
        self.assertIn("CVE-2026-1000", found)

    def test_uses_config_keywords_by_default(self):
        found, _ = sbm.collect_signals([_entry("Actively exploited Acme bug", ["CVE-2026-1000"])], {})
        self.assertIn("CVE-2026-1000", found)

    def test_signals_taken_before_dedup_keep_earliest(self):
        early = _entry("Acme zero-day (first report)", ["CVE-2026-1000"],
                       published="2026-11-16T01:00:00+00:00", source="Early Blog",
                       link="https://early.example/1")
        late_kev = _entry("CVE-2026-1000 — Acme", ["CVE-2026-1000"], is_kev=True,
                          published="2026-11-17", source="CISA KEV")
        late = _entry("Acme zero-day roundup", ["CVE-2026-1000"],
                      published="2026-11-17T01:00:00+00:00", source="Late News")
        undated = _entry("Acme zero-day", ["CVE-2026-1000"], published="", source="Undated")
        entries = [late, undated, early, late_kev]
        # no KEV lookup hit (catalog loaded but CVE not listed yet)
        found, _ = sbm.collect_signals(entries, {}, ZD)
        self.assertEqual(found["CVE-2026-1000"]["source"], "Early Blog")
        # dedup would keep only one finding: the scoreboard must not depend on it
        with mock.patch("pulse.filter._load_keywords", return_value=(ZD, [], [])):
            kept = filter_zero_days([dict(e) for e in entries])
        self.assertEqual(len(kept), 1)
        self.assertEqual(kept[0]["source"], "CISA KEV")


class EdgeVendorTests(unittest.TestCase):
    def test_real_kev_spellings(self):
        for v in ["Juniper", "Juniper Networks", "Citrix", "Citrix Systems", "Palo Alto Networks",
                  "Check Point", "CheckPoint", "F5", "F5 Networks", "SonicWall", "SonicWALL",
                  "Fortinet", "Fortinet, Inc.", "Ivanti", "Cisco", "cisco", "  FORTINET "]:
            self.assertTrue(sbm.is_edge_vendor(v), v)

    def test_non_edge(self):
        for v in ["Microsoft", "Apple", "Google", "Pulse Secure", "Oracle", "", None,
                  "Linux", "Progress", "VMware", "Atlassian"]:
            self.assertFalse(sbm.is_edge_vendor(v), v)


# ── first_signal.json ─────────────────────────────────────────────────────────

class SignalFileTests(_TmpDir):
    def test_missing_and_corrupt(self):
        self.assertEqual(sbm.load_signals(self.sig), {})
        Path(self.sig).write_text("{nope")
        with self.assertLogs("pulse.scoreboard", "WARNING"):
            self.assertEqual(sbm.load_signals(self.sig), {})
        Path(self.sig).write_text("[1, 2]")
        with self.assertLogs("pulse.scoreboard", "WARNING"):
            self.assertEqual(sbm.load_signals(self.sig), {})

    def test_first_signal_is_never_overwritten(self):
        e1 = _entry("zero-day", ["CVE-2026-1000"], source="First")
        sig, added = sbm.update_signals({}, {"CVE-2026-1000": e1}, NOW)
        self.assertEqual(added, 1)
        later = NOW + timedelta(days=2)
        sig2, added2 = sbm.update_signals(sig, {"CVE-2026-1000": _entry("zero-day", ["CVE-2026-1000"],
                                                                        source="Second")}, later)
        self.assertEqual(added2, 0)
        self.assertEqual(sig2["CVE-2026-1000"]["source"], "First")
        self.assertEqual(sig2["CVE-2026-1000"]["observed_at"], NOW.isoformat())
        sbm.save_signals(sig2, self.sig)
        self.assertEqual(sbm.load_signals(self.sig), sig2)

    def test_link_and_published_sanitized(self):
        e = _entry("zero-day", ["CVE-2026-1000"], link="javascript:alert(1)", published="garbage")
        sig, _ = sbm.update_signals({}, {"CVE-2026-1000": e}, NOW)
        self.assertIsNone(sig["CVE-2026-1000"]["link"])
        self.assertIsNone(sig["CVE-2026-1000"]["published"])

    def test_prune_180_days(self):
        sig = {"CVE-2026-0001": {"observed_at": (NOW - timedelta(days=181)).isoformat()},
               "CVE-2026-0002": {"observed_at": (NOW - timedelta(days=179)).isoformat()},
               "CVE-2026-0003": {"observed_at": "not a date"}}
        self.assertEqual(list(sbm.prune_signals(sig, NOW)), ["CVE-2026-0002"])

    def test_prune_5000_cap_drops_oldest(self):
        sig = {f"CVE-2026-{i:05d}": {"observed_at": (NOW - timedelta(minutes=i)).isoformat()}
               for i in range(5003)}
        kept = sbm.prune_signals(sig, NOW)
        self.assertEqual(len(kept), 5000)
        for gone in ("CVE-2026-05000", "CVE-2026-05001", "CVE-2026-05002"):
            self.assertNotIn(gone, kept)
        self.assertIn("CVE-2026-00000", kept)


# ── rows, buckets, lead days ──────────────────────────────────────────────────

def _sig(observed_at, source="News", link="https://n.example/x"):
    return {"observed_at": observed_at, "published": None, "source": source, "link": link}


class RowTests(unittest.TestCase):
    def test_three_buckets(self):
        signals = {"CVE-2026-0001": _sig("2026-11-14T06:00:00+00:00"),
                   "CVE-2026-0002": _sig("2026-11-17T06:00:00+00:00"),
                   "CVE-2026-0003": _sig("2026-11-20T06:00:00+00:00")}
        recs = [_rec("CVE-2026-0001", "2026-11-17"), _rec("CVE-2026-0002", "2026-11-17"),
                _rec("CVE-2026-0003", "2026-11-17"), _rec("CVE-2026-0004", "2026-11-17")]
        rows = {r["cve"]: r for r in sbm.build_rows(recs, GO_LIVE, [], signals)}
        self.assertEqual((rows["CVE-2026-0001"]["bucket"], rows["CVE-2026-0001"]["lead_days"]), ("earlier", 3))
        self.assertEqual((rows["CVE-2026-0002"]["bucket"], rows["CVE-2026-0002"]["lead_days"]),
                         ("same_day_or_late", 0))
        self.assertEqual((rows["CVE-2026-0003"]["bucket"], rows["CVE-2026-0003"]["lead_days"]),
                         ("same_day_or_late", -3))
        m = rows["CVE-2026-0004"]
        self.assertEqual((m["bucket"], m["lead_days"], m["observed_at"], m["source"]), ("missed", None, None, None))
        self.assertEqual(set(m), {"cve", "kev_date_added", "vendor", "product", "cve_year",
                                  "observed_at", "source", "link", "lead_days", "bucket"})
        self.assertEqual(m["cve_year"], 2026)

    def test_lead_days_across_utc_date_boundary(self):
        # 23:30 at UTC-5 on the 15th is 04:30 UTC on the 16th -> 1 day before the 17th
        signals = {"CVE-2026-0001": _sig("2026-11-15T23:30:00-05:00"),
                   "CVE-2026-0002": _sig("2026-11-16T23:59:59+00:00"),
                   "CVE-2026-0003": _sig("2026-11-17T00:00:01+00:00")}
        recs = [_rec(c, "2026-11-17") for c in signals]
        rows = {r["cve"]: r for r in sbm.build_rows(recs, GO_LIVE, [], signals)}
        self.assertEqual(rows["CVE-2026-0001"]["lead_days"], 1)
        self.assertEqual(rows["CVE-2026-0001"]["bucket"], "earlier")
        self.assertEqual(rows["CVE-2026-0002"]["lead_days"], 1)
        self.assertEqual(rows["CVE-2026-0003"]["lead_days"], 0)
        self.assertEqual(rows["CVE-2026-0003"]["bucket"], "same_day_or_late")

    def test_before_go_live_and_existing_skipped(self):
        recs = [_rec("CVE-2026-0001", "2026-07-31"), _rec("CVE-2026-0002", "2026-08-01"),
                _rec("CVE-2026-0003", "2026-09-01")]
        rows = sbm.build_rows(recs, GO_LIVE, ["CVE-2026-0003"], {})
        self.assertEqual([r["cve"] for r in rows], ["CVE-2026-0002"])

    def test_failed_catalog_writes_no_rows(self):
        self.assertEqual(sbm.build_rows(None, GO_LIVE, [], {}), [])


class ScoreboardFileTests(_TmpDir):
    def _lines(self):
        return [json.loads(l) for l in Path(self.sb).read_text().splitlines()]

    def test_missing_file_is_first_run(self):
        self.assertEqual(sbm.load_scoreboard(self.sb), (None, [], False))

    def test_write_once_rows(self):
        recs = [_rec("CVE-2026-0001", "2026-11-17")]
        r1 = sbm.run_scoreboard([], recs, {"CVE-2026-0001": {}}, now=NOW,
                                signals_file=self.sig, scoreboard_file=self.sb)
        self.assertEqual(r1["run"]["new_rows"], 1)
        before = Path(self.sb).read_text()
        # A later signal for the same CVE must not rewrite its missed row
        late = _entry("zero-day", ["CVE-2026-0001"])
        r2 = sbm.run_scoreboard([late], recs, {}, now=NOW + timedelta(days=1),
                                signals_file=self.sig, scoreboard_file=self.sb)
        self.assertEqual(r2["run"]["new_rows"], 0)
        self.assertEqual(Path(self.sb).read_text(), before)
        self.assertEqual(self._lines()[1]["bucket"], "missed")

    def test_catalog_walk_catches_up_missed_runs(self):
        # Run 1: go-live; catalog fails on run 2; run 3 sees two additions from days ago
        sbm.run_scoreboard([], [], {}, now=NOW, signals_file=self.sig, scoreboard_file=self.sb)
        r = sbm.run_scoreboard([], None, None, now=NOW + timedelta(days=1),
                               signals_file=self.sig, scoreboard_file=self.sb)
        self.assertEqual(r["run"]["new_rows"], 0)
        self.assertEqual(len(self._lines()), 1)
        recs = [_rec("CVE-2026-0001", "2026-11-17"), _rec("CVE-2026-0002", "2026-11-18"),
                _rec("CVE-2026-0003", "2026-11-16")]  # before go-live
        r = sbm.run_scoreboard([], recs, {}, now=NOW + timedelta(days=5),
                               signals_file=self.sig, scoreboard_file=self.sb)
        self.assertEqual(r["run"]["new_rows"], 2)
        self.assertEqual(self._lines()[0], {"go_live": "2026-11-17"})
        self.assertEqual([l["cve"] for l in self._lines()[1:]], ["CVE-2026-0001", "CVE-2026-0002"])

    def test_corrupt_and_duplicate_lines_rewritten_once(self):
        good = _row("CVE-2026-0001", "2026-11-10", "missed")
        dup = _row("CVE-2026-0001", "2026-11-10", "earlier", lead=4)
        other = _row("CVE-2026-0002", "2026-11-11", "earlier", lead=2)
        Path(self.sb).write_text("\n".join([
            json.dumps({"go_live": "2026-08-01"}), json.dumps(good), "{broken",
            json.dumps(dup), json.dumps({"cve": "nope"}), json.dumps(other)]) + "\n")
        with self.assertLogs("pulse.scoreboard", "WARNING"):
            go_live, rows, dirty = sbm.load_scoreboard(self.sb)
        self.assertEqual(go_live, GO_LIVE)
        self.assertTrue(dirty)
        self.assertEqual([(r["cve"], r["bucket"]) for r in rows],
                         [("CVE-2026-0001", "missed"), ("CVE-2026-0002", "earlier")])
        recs = [_rec("CVE-2026-0001", "2026-11-10"), _rec("CVE-2026-0002", "2026-11-11")]
        sbm.run_scoreboard([], recs, {}, now=NOW, signals_file=self.sig, scoreboard_file=self.sb)
        lines = self._lines()
        self.assertEqual(lines[0], {"go_live": "2026-08-01"})
        self.assertEqual([l["cve"] for l in lines[1:]], ["CVE-2026-0001", "CVE-2026-0002"])
        # Second run: clean file, no rewrite, no re-added rows
        mtime_text = Path(self.sb).read_text()
        self.assertFalse(sbm.load_scoreboard(self.sb)[2])
        sbm.run_scoreboard([], recs, {}, now=NOW, signals_file=self.sig, scoreboard_file=self.sb)
        self.assertEqual(Path(self.sb).read_text(), mtime_text)

    def test_lost_header_rebuilt_from_earliest_row(self):
        rows = [_row("CVE-2026-0002", "2026-10-05", "missed"), _row("CVE-2026-0001", "2026-09-20", "missed")]
        for header in ("", "{garbage\n"):
            Path(self.sb).write_text(header + "\n".join(json.dumps(r) for r in rows) + "\n")
            with self.assertLogs("pulse.scoreboard", "WARNING"):
                go_live, got, dirty = sbm.load_scoreboard(self.sb)
            self.assertEqual(go_live, date(2026, 9, 20))   # not today
            self.assertTrue(dirty)
            self.assertEqual(len(got), 2)
            sbm.run_scoreboard([], [], {}, now=NOW, signals_file=self.sig, scoreboard_file=self.sb)
            self.assertEqual(self._lines()[0], {"go_live": "2026-09-20"})
            self.assertEqual(len(self._lines()), 3)

    def test_corrupt_signal_file_does_not_crash(self):
        Path(self.sig).write_text("\x00\x01 not json")
        Path(self.sb).write_text("total garbage\n")
        r = sbm.run_scoreboard([_entry("zero-day", ["CVE-2026-0009"])], [], {}, now=NOW,
                               signals_file=self.sig, scoreboard_file=self.sb)
        self.assertIsNotNone(r)
        self.assertIn("CVE-2026-0009", sbm.load_signals(self.sig))
        self.assertEqual(self._lines(), [{"go_live": "2026-11-17"}])

    def test_unexpected_error_never_raises(self):
        with mock.patch.object(sbm, "build_rows", side_effect=RuntimeError("boom")), \
                self.assertLogs("pulse.scoreboard", "WARNING"):
            self.assertIsNone(sbm.run_scoreboard([], [], {}, now=NOW,
                                                 signals_file=self.sig, scoreboard_file=self.sb))

    def test_paths_overridable_by_env(self):
        with mock.patch.dict(os.environ, {"PULSE_SIGNALS_PATH": self.sig,
                                          "PULSE_SCOREBOARD_PATH": self.sb}):
            self.assertEqual(sbm.signals_path(), self.sig)
            self.assertEqual(sbm.scoreboard_path(), self.sb)
        with mock.patch.dict(os.environ, {}, clear=True):
            self.assertEqual(sbm.signals_path(), "state/first_signal.json")
            self.assertEqual(sbm.scoreboard_path(), "state/kev_scoreboard.jsonl")


# ── exclusions and numbers ────────────────────────────────────────────────────

class NumbersTests(unittest.TestCase):
    def test_warm_up_and_old_cve(self):
        self.assertEqual(sbm.exclusion(_row("CVE-2026-0001", "2026-08-14", "missed"), GO_LIVE), "warm_up")
        self.assertIsNone(sbm.exclusion(_row("CVE-2026-0001", "2026-08-15", "missed"), GO_LIVE))
        self.assertIsNone(sbm.exclusion(_row("CVE-2025-0001", "2026-11-01", "missed"), GO_LIVE))
        self.assertEqual(sbm.exclusion(_row("CVE-2024-0001", "2026-11-01", "missed"), GO_LIVE), "old_cve")
        # warm-up wins over old CVE
        self.assertEqual(sbm.exclusion(_row("CVE-2019-0001", "2026-08-02", "missed"), GO_LIVE), "warm_up")

    def test_windows_populations_and_stats(self):
        today = date(2026, 11, 17)
        rows = [
            _row("CVE-2026-0001", "2026-11-16", "earlier", lead=6, vendor="Check Point"),
            _row("CVE-2026-0002", "2026-11-10", "earlier", lead=2, vendor="Ivanti"),
            _row("CVE-2026-0003", "2026-11-05", "earlier", lead=1, vendor="Microsoft"),
            _row("CVE-2026-0004", "2026-11-05", "same_day_or_late", lead=0, vendor="Juniper Networks"),
            _row("CVE-2026-0005", "2026-11-01", "missed", vendor="Apple"),
            _row("CVE-2026-0006", "2026-09-01", "earlier", lead=9, vendor="Fortinet"),  # 90d only
            _row("CVE-2021-0007", "2026-11-12", "earlier", lead=30, vendor="Cisco"),   # old CVE
        ]
        sb = sbm.compute_scoreboard(rows, GO_LIVE, today)
        w30, w90 = sb["windows"]["30"], sb["windows"]["90"]
        self.assertEqual(w30["all"], {"counted": 5, "earlier": 3, "earlier_pct": 60.0, "median_lead": 2,
                                      "max_lead": 6, "same_day_or_late": 1, "missed": 1, "collecting": True})
        self.assertEqual(w30["edge"]["counted"], 3)
        self.assertEqual(w30["edge"]["median_lead"], 4)
        self.assertEqual(w30["excluded"], {"warm_up": 0, "old_cve": 1})
        self.assertEqual(w90["all"]["counted"], 6)
        self.assertEqual(w90["all"]["median_lead"], 4)  # median of 6, 2, 1, 9
        self.assertEqual([l["cve"] for l in sb["top_leads"]],
                         ["CVE-2026-0006", "CVE-2026-0001", "CVE-2026-0002", "CVE-2026-0003"])
        self.assertEqual(sb["go_live"], "2026-08-01")

    def test_collecting_threshold_and_empty(self):
        rows = [_row(f"CVE-2026-{i:04d}", "2026-11-10", "missed") for i in range(10)]
        sb = sbm.compute_scoreboard(rows, GO_LIVE, date(2026, 11, 17))
        self.assertFalse(sb["windows"]["30"]["all"]["collecting"])
        self.assertEqual(sb["windows"]["30"]["all"]["earlier_pct"], 0.0)
        self.assertIsNone(sb["windows"]["30"]["all"]["median_lead"])
        edge = sb["windows"]["30"]["edge"]
        self.assertEqual((edge["counted"], edge["earlier_pct"], edge["collecting"]), (0, None, True))


# ── rendering ─────────────────────────────────────────────────────────────────

class RenderTests(unittest.TestCase):
    def _sb(self, n_missed=0):
        rows = [_row("CVE-2026-0001", "2026-11-16", "earlier", lead=6, vendor="<b>Check Point</b>",
                     source="Evil <script>@team", link="javascript:alert(1)"),
                _row("CVE-2026-0002", "2026-11-15", "earlier", lead=3, vendor="Ivanti",
                     source="Volexity", link="https://volexity.example/post")]
        rows += [_row(f"CVE-2026-{i + 10:04d}", "2026-11-10", "missed") for i in range(n_missed)]
        return sbm.compute_scoreboard(rows, GO_LIVE, date(2026, 11, 17))

    def test_markdown_panel_at_top_and_escaped(self):
        md = generate_markdown_report([{"title": "x", "cve_ids": [], "is_zero_day": True}], "now",
                                      changes=[{"kind": "entered_kev", "cve": "CVE-2026-9"}],
                                      scoreboard=self._sb())
        self.assertLess(md.index("🏁 Beat KEV"), md.index("Changed since last run"))
        self.assertLess(md.index("🏁 Beat KEV"), md.index("## 1."))
        self.assertIn("collecting data since 2026-08-01", md)
        self.assertIn(sbm.CAVEAT, md)
        self.assertIn("Excluded: 0 warm-up, 0 old CVEs", md)
        self.assertIn("&lt;script&gt;", md)
        self.assertNotIn("<script>", md)
        self.assertNotIn("javascript:", md)
        self.assertIn("@​team", md)
        self.assertIn("<https://volexity.example/post>", md)

    def test_both_lines_use_same_fields_once_counted(self):
        md = generate_markdown_report([], "now", scoreboard=self._sb(n_missed=10))
        self.assertIn("All: Counted 12 · Earlier 2 (17%) · Median lead 4.5d · Max lead 6d"
                      " · Same day/late 0 · Missed 10", md)
        self.assertIn("Edge devices: collecting data since 2026-08-01 — Counted 1 · Earlier 1", md)  # "<b>Check Point</b>" is not Edge

    def test_html_panel_escaped_and_first(self):
        html = generate_html_report([{"title": "x", "cve_ids": [], "is_zero_day": True}], "now",
                                    scoreboard=self._sb())
        self.assertIn("🏁 Beat KEV", html)
        self.assertLess(html.index("scoreboard-section"), html.index('class="card'))
        self.assertNotIn("<script>", html)
        self.assertNotIn("<b>Check Point", html)
        self.assertNotIn("javascript:", html)
        self.assertIn('href="https://volexity.example/post"', html)

    def test_no_scoreboard_no_panel(self):
        self.assertNotIn("Beat KEV", generate_markdown_report([], "now"))
        self.assertNotIn("Beat KEV", generate_html_report([], "now"))

    def test_save_reports_writes_scoreboard_json(self):
        with tempfile.TemporaryDirectory() as d:
            paths = save_reports([], os.path.join(d, "reports"), run_id="1", scoreboard=self._sb())
            data = json.loads(Path(d, "docs", "scoreboard.json").read_text())
            self.assertEqual(paths["scoreboard"], str(Path(d, "docs", "scoreboard.json")))
            self.assertEqual(data["go_live"], "2026-08-01")
            self.assertIn("30", data["windows"])
            paths = save_reports([], os.path.join(d, "r2"), run_id="1")
            self.assertNotIn("scoreboard", paths)


# ── end to end: two offline runs of main.py ──────────────────────────────────

CVE_X = "CVE-2026-55501"
CVE_Y = "CVE-2026-55502"
NEWS_URL = "https://news.example/feed.xml"


class _Resp:
    def __init__(self, status=200, body=b"", data=None):
        self.status_code, self.content, self._data = status, body, data

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError(f"HTTP {self.status_code}")

    def json(self):
        return self._data


def _rss(published: datetime) -> bytes:
    pub = published.strftime("%a, %d %b %Y %H:%M:%S +0000")
    return f"""<?xml version="1.0"?><rss version="2.0"><channel><title>N</title>
<item><title>Acme Gateway zero-day exploited in the wild ({CVE_X})</title>
<link>https://news.example/acme-zero-day</link><pubDate>{pub}</pubDate>
<description>Attackers are using {CVE_X} against Acme gateways.</description></item>
</channel></rss>""".encode()


class EndToEndTests(unittest.TestCase):
    def _run(self, d, catalog, now, published):
        import main as main_mod
        from pulse import feeds as pfeeds

        cfg = {"feeds": [{"name": "News Example", "url": NEWS_URL, "tags": ["news"]}],
               "cisa_kev_url": "https://kev.example/kev.json"}

        def fake_get(url, *a, **kw):
            if url == NEWS_URL:
                return _Resp(body=_rss(published))
            if url == "https://kev.example/kev.json":
                return _Resp(data={"vulnerabilities": catalog})
            if url.startswith("https://api.first.org/"):
                return _Resp(data={"data": []})
            if url.startswith("https://api.github.com/advisories"):
                return _Resp(data=[])
            return _Resp(status=404)

        args = ["--skip-enrichment", "--lookback-hours", "48", "--output-dir", str(d / "reports"),
                "--state-file", str(d / "state" / "last_run.json"),
                "--signals-file", str(d / "state" / "first_signal.json"),
                "--scoreboard-file", str(d / "state" / "kev_scoreboard.jsonl")]
        with mock.patch("requests.get", side_effect=fake_get), \
                mock.patch.object(pfeeds, "load_config", return_value=cfg), \
                mock.patch("pulse.intel.load_config", return_value=cfg), \
                mock.patch.object(pfeeds.time, "sleep"), \
                mock.patch.object(sbm, "_utcnow", return_value=now):
            self.assertEqual(main_mod.main(args), 0)

    def test_two_runs_earlier_and_missed(self):
        real_now = datetime.now(timezone.utc)
        t1 = real_now - timedelta(days=1)
        t2 = real_now
        old = {"cveID": "CVE-2021-44228", "dateAdded": "2021-12-10", "vendorProject": "Apache",
               "product": "Log4j2", "dueDate": "2021-12-24"}
        base = os.environ.get("PULSE_E2E_DIR")
        with tempfile.TemporaryDirectory(dir=base) as tmp:
            d = Path(tmp)
            # Run 1: news signals CVE-X; the catalog does not list it yet
            self._run(d, [old], t1, published=real_now - timedelta(hours=2))
            sig = json.loads((d / "state" / "first_signal.json").read_text())
            self.assertEqual(sig[CVE_X]["source"], "News Example")
            self.assertEqual(sig[CVE_X]["observed_at"], t1.isoformat())
            lines = (d / "state" / "kev_scoreboard.jsonl").read_text().splitlines()
            self.assertEqual(lines, [json.dumps({"go_live": t1.date().isoformat()})])

            # Run 2 (next day): KEV lists CVE-X and CVE-Y (no signal) today
            added = t2.date().isoformat()
            catalog = [old,
                       {"cveID": CVE_X, "dateAdded": added, "vendorProject": "Acme", "product": "Gateway",
                        "dueDate": added},
                       {"cveID": CVE_Y, "dateAdded": added, "vendorProject": "Fortinet",
                        "product": "FortiOS", "dueDate": added}]
            self._run(d, catalog, t2, published=real_now - timedelta(hours=2))
            rows = {r["cve"]: r for r in map(json.loads,
                    (d / "state" / "kev_scoreboard.jsonl").read_text().splitlines()[1:])}
            self.assertEqual(set(rows), {CVE_X, CVE_Y})
            self.assertEqual((rows[CVE_X]["bucket"], rows[CVE_X]["lead_days"]), ("earlier", 1))
            self.assertEqual(rows[CVE_X]["link"], "https://news.example/acme-zero-day")
            self.assertEqual((rows[CVE_Y]["bucket"], rows[CVE_Y]["lead_days"]), ("missed", None))

            sb = json.loads((d / "docs" / "scoreboard.json").read_text())
            self.assertEqual(sb["total_rows"], 2)
            self.assertEqual(sb["windows"]["30"]["excluded"]["warm_up"], 2)  # day 1 of go-live
            md = (d / "reports" / "latest.md").read_text()
            self.assertIn("🏁 Beat KEV", md)
            self.assertIn("Excluded: 2 warm-up, 0 old CVEs", md)
            self.assertIn("Beat KEV", (d / "docs" / "index.html").read_text())


if __name__ == "__main__":
    unittest.main()
