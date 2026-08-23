import logging
from datetime import datetime, timezone

import defusedxml.ElementTree as ET

from pulse.feeds import (
    MAX_CVE_IDS_PER_ENTRY,
    SUMMARY_MAX_LEN,
    _parse_date,
    _parse_rss,
    _parse_atom,
)

# Cutoff far in the past so no test entry is date-filtered unless we want it to be.
OLD_CUTOFF = datetime(2000, 1, 1, tzinfo=timezone.utc)

ATOM_NS = "http://www.w3.org/2005/Atom"


def parse_rss_items(items_xml: str):
    xml = f'<rss version="2.0"><channel><title>t</title>{items_xml}</channel></rss>'
    return _parse_rss(ET.fromstring(xml), "TestFeed", ["test"], OLD_CUTOFF)


def parse_atom_entries(entries_xml: str):
    xml = f'<feed xmlns="{ATOM_NS}"><title>t</title>{entries_xml}</feed>'
    return _parse_atom(ET.fromstring(xml), "TestFeed", ["test"], OLD_CUTOFF)


# ── _parse_date ──────────────────────────────────────────────────────────────

def test_existing_date_formats_still_parse():
    # Regression: the 5 formats that predate the vendor-feed change.
    samples = [
        "Fri, 25 Jul 2026 10:00:00 +0000",
        "Fri, 25 Jul 2026 10:00:00 GMT",
        "2026-07-25T10:00:00+0000",
        "2026-07-25T10:00:00Z",
        "2026-07-25",
    ]
    for raw in samples:
        assert _parse_date(raw) is not None, f"regressed: {raw!r}"


def test_palo_alto_fractional_iso_parses():
    dt = _parse_date("2026-07-08T20:30:00.000Z")
    assert dt is not None
    assert dt.tzinfo is not None


def test_blogger_fractional_with_offset_parses():
    # Google Security Blog (Blogger Atom); found by the unparseable-date warning
    # on the first live verification run — this feed had always bypassed the cutoff.
    dt = _parse_date("2026-04-23T17:38:00.001-04:00")
    assert dt is not None
    assert dt.tzinfo is not None


def test_cisa_uscert_named_timezone_parses():
    # CISA US-CERT Alerts; found by the unparseable-date warning on live verification.
    dt = _parse_date("Wed, 08 Jul 2026 14:43:49 EDT")
    assert dt is not None
    assert dt.utcoffset().total_seconds() == 0  # normalized to UTC


def test_crowdstrike_month_name_format_parses():
    # CrowdStrike Blog; found by the unparseable-date warning on live verification.
    dt = _parse_date("Jun 30, 2026 00:00:00-0500")
    assert dt is not None


def test_cisco_space_fractional_parses():
    dt = _parse_date("2026-07-21 16:01:27.0")
    assert dt is not None
    assert dt.tzinfo == timezone.utc  # no-tz dates are stamped UTC


def test_all_tz_abbreviations_normalize():
    # Every mapping in _TZ_ABBREVIATIONS is data that can silently be wrong —
    # sweep all of them, checking the resulting UTC offset, not just EDT.
    expected_offsets = {
        "UT": 0, "EDT": -4, "EST": -5, "CDT": -5, "CST": -6,
        "MDT": -6, "MST": -7, "PDT": -7, "PST": -8,
    }
    for abbr, hours in expected_offsets.items():
        dt = _parse_date(f"Wed, 08 Jul 2026 14:43:49 {abbr}")
        assert dt is not None, f"failed to parse {abbr}"
        # _parse_date converts to UTC; recover the original offset from the hour shift
        assert dt.hour == (14 - hours) % 24, f"wrong offset applied for {abbr}"


def test_garbage_date_returns_none():
    assert _parse_date("not a date at all") is None
    assert _parse_date(None) is None


# ── RSS parsing: unparseable-date warning ────────────────────────────────────

def test_unparseable_pubdate_logs_warning_and_keeps_entry(caplog):
    items = "<item><title>Odd feed</title><pubDate>weird-date-2026</pubDate></item>"
    with caplog.at_level(logging.WARNING, logger="pulse.feeds"):
        entries = parse_rss_items(items)
    assert len(entries) == 1  # entry bypasses the cutoff rather than being lost
    assert any("unparseable" in rec.message for rec in caplog.records)


def test_unparseable_atom_date_logs_warning_and_keeps_entry(caplog):
    # Same guarantee as the RSS variant, but for the separate _parse_atom branch.
    entries_xml = (
        "<entry><title>Odd atom feed</title><id>tag:odd</id>"
        "<published>weird-date-2026</published></entry>"
    )
    with caplog.at_level(logging.WARNING, logger="pulse.feeds"):
        entries = parse_atom_entries(entries_xml)
    assert len(entries) == 1
    assert any("unparseable" in rec.message for rec in caplog.records)


# ── RSS parsing: CVE extraction from raw element ─────────────────────────────

def test_rss_cve_only_in_href_is_captured():
    # The Ivanti case: CVE id lives only inside a link URL, which strip_html removes.
    items = (
        "<item><title>Security update</title>"
        "<description>&lt;a href=\"https://ex.com/CVE-2026-12345\"&gt;advisory&lt;/a&gt;</description>"
        "</item>"
    )
    entries = parse_rss_items(items)
    assert entries[0]["cve_ids"] == ["CVE-2026-12345"]
    assert "CVE-2026-12345" not in entries[0]["summary"]  # proves strip_html removed it


def test_rss_cve_beyond_truncation_is_captured():
    filler = "x" * (SUMMARY_MAX_LEN + 500)
    items = f"<item><title>Long post</title><description>{filler} CVE-2026-22222</description></item>"
    entries = parse_rss_items(items)
    assert "CVE-2026-22222" in entries[0]["cve_ids"]
    assert len(entries[0]["summary"]) <= SUMMARY_MAX_LEN  # truncation behavior unchanged


def test_rss_plain_text_cve_still_found():
    # Regression: the pre-change happy path.
    items = "<item><title>Advisory</title><description>Details about CVE-2026-33333 here.</description></item>"
    entries = parse_rss_items(items)
    assert entries[0]["cve_ids"] == ["CVE-2026-33333"]


def test_rss_mixed_title_and_description_cves_are_unioned():
    items = (
        "<item><title>Fix for CVE-2026-44444</title>"
        "<description>Also addresses CVE-2026-55555.</description></item>"
    )
    entries = parse_rss_items(items)
    assert set(entries[0]["cve_ids"]) == {"CVE-2026-44444", "CVE-2026-55555"}


def test_rss_lowercase_cve_in_href_is_uppercased():
    # Vendor hrefs commonly use lowercase ids; seen_cves dedup in filter.py
    # depends on extract_cve_ids returning canonical uppercase.
    items = (
        "<item><title>Update</title>"
        "<description>&lt;a href=\"https://ex.com/cve-2026-12345\"&gt;x&lt;/a&gt;</description></item>"
    )
    entries = parse_rss_items(items)
    assert entries[0]["cve_ids"] == ["CVE-2026-12345"]


def test_rss_same_cve_in_title_and_body_returned_once():
    items = "<item><title>Fix for CVE-2026-12345</title><description>Details on CVE-2026-12345.</description></item>"
    entries = parse_rss_items(items)
    assert entries[0]["cve_ids"] == ["CVE-2026-12345"]


def test_rss_roundup_post_cve_ids_are_capped():
    # Regression: ISSUE-001 — a link-heavy round-up ("Patch Tuesday") claimed 575
    # CVE ids from raw-element extraction. Dedup then treated all of them as
    # covered (dropping later advisories about those CVEs) and the dashboard
    # rendered the whole wall.
    # Found by /qa on 2026-07-27
    # Report: reports of run at scratchpad/qa/build2 — Rapid7 "Patch Tuesday - July 2026"
    links = " ".join(
        f'&lt;a href="https://ex.com/CVE-2026-{40000 + i}"&gt;x&lt;/a&gt;' for i in range(60)
    )
    items = f"<item><title>Patch Tuesday round-up</title><description>{links}</description></item>"
    entries = parse_rss_items(items)
    assert len(entries[0]["cve_ids"]) == MAX_CVE_IDS_PER_ENTRY
    # The first ids encountered are the ones kept, in order.
    assert entries[0]["cve_ids"][0] == "CVE-2026-40000"


def test_atom_roundup_post_cve_ids_are_capped():
    links = "".join(
        f'<link href="https://ex.com/CVE-2026-{50000 + i}" rel="related"/>' for i in range(40)
    )
    entries_xml = f"<entry><title>Monthly round-up</title><id>tag:r</id>{links}</entry>"
    entries = parse_atom_entries(entries_xml)
    assert len(entries[0]["cve_ids"]) == MAX_CVE_IDS_PER_ENTRY


def test_normal_advisory_cve_ids_untouched_by_cap():
    # An ordinary advisory names a handful of CVEs — the cap must not clip it.
    items = (
        "<item><title>Vendor advisory CVE-2026-11111</title>"
        "<description>Also fixes CVE-2026-22222 and CVE-2026-33333.</description></item>"
    )
    entries = parse_rss_items(items)
    assert entries[0]["cve_ids"] == ["CVE-2026-11111", "CVE-2026-22222", "CVE-2026-33333"]


def test_rss_entry_older_than_cutoff_is_dropped(caplog):
    # The cutoff-drop branch sits right next to the new warning code — cover both:
    # old-but-parseable entries are excluded, and NO unparseable warning fires.
    cutoff = datetime(2026, 1, 1, tzinfo=timezone.utc)
    xml = (
        '<rss version="2.0"><channel><title>t</title>'
        "<item><title>old</title><pubDate>Wed, 01 Jan 2020 00:00:00 +0000</pubDate></item>"
        "<item><title>new</title><pubDate>Wed, 08 Jul 2026 00:00:00 +0000</pubDate></item>"
        "</channel></rss>"
    )
    with caplog.at_level(logging.WARNING, logger="pulse.feeds"):
        entries = _parse_rss(ET.fromstring(xml), "TestFeed", ["test"], cutoff)
    assert [e["title"] for e in entries] == ["new"]
    assert not any("unparseable" in r.message for r in caplog.records)


def test_atom_entry_older_than_cutoff_is_dropped(caplog):
    cutoff = datetime(2026, 1, 1, tzinfo=timezone.utc)
    xml = (
        f'<feed xmlns="{ATOM_NS}"><title>t</title>'
        "<entry><title>old</title><id>tag:o</id><published>2020-01-01T00:00:00Z</published></entry>"
        "<entry><title>new</title><id>tag:n</id><published>2026-07-08T00:00:00Z</published></entry>"
        "</feed>"
    )
    with caplog.at_level(logging.WARNING, logger="pulse.feeds"):
        entries = _parse_atom(ET.fromstring(xml), "TestFeed", ["test"], cutoff)
    assert [e["title"] for e in entries] == ["new"]
    assert not any("unparseable" in r.message for r in caplog.records)


def test_rss_no_cve_attaches_empty_list():
    items = "<item><title>No identifiers here</title><description>General news.</description></item>"
    entries = parse_rss_items(items)
    assert entries[0]["cve_ids"] == []


# ── Atom parsing: CVE extraction from raw element ────────────────────────────

def test_atom_cve_in_nested_xhtml_content_is_captured():
    # Real nested markup (NOT CDATA): the href is an XML attribute that .text never sees.
    entries_xml = (
        f'<entry><title>Patch</title><id>tag:1</id>'
        f'<content type="xhtml"><div xmlns="http://www.w3.org/1999/xhtml">'
        f'Patch <a href="https://ex.com/CVE-2026-66666">here</a></div></content>'
        f'</entry>'
    )
    entries = parse_atom_entries(entries_xml)
    assert "CVE-2026-66666" in entries[0]["cve_ids"]


def test_atom_plain_text_cve_still_found():
    entries_xml = "<entry><title>CVE-2026-77770 fixed</title><id>tag:2</id></entry>"
    entries = parse_atom_entries(entries_xml)
    assert entries[0]["cve_ids"] == ["CVE-2026-77770"]
