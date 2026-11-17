import yaml
import pytest

import pulse.filter as pf
from pulse import intel

PUBLISHED = "2026-07-25T00:00:00+00:00"

FIXTURE_CFG = {
    "zero_day_keywords": ["zero-day"],
    "high_severity_keywords": ["critical"],
    "priority_product_keywords": ["pan-os"],
}


@pytest.fixture
def fixture_config(tmp_path, monkeypatch):
    cfg_path = tmp_path / "feeds.yaml"
    cfg_path.write_text(yaml.safe_dump(FIXTURE_CFG))
    monkeypatch.setattr(pf, "CONFIG_PATH", cfg_path)
    return cfg_path


def entry(title, summary="", cve_ids=None, is_kev=False, eid=None):
    e = {
        "id": eid or title,
        "title": title,
        "summary": summary,
        "published": PUBLISHED,
        "source": "TestFeed",
        "tags": ["test"],
    }
    if cve_ids is not None:
        e["cve_ids"] = cve_ids
    if is_kev:
        e["is_kev"] = True
    return e


def run(entries, kev_lookup=None):
    """The current pre-gate pipeline: attach_cve_ids → annotate_kev → filter_zero_days."""
    pf.attach_cve_ids(entries)
    intel.annotate_kev(entries, kev_lookup)
    return pf.filter_zero_days(entries)


# ── Survival gate: regressions ───────────────────────────────────────────────

def test_kev_entry_survives(fixture_config):
    out = run([entry("Some vuln", cve_ids=["CVE-2026-99990"], is_kev=True)])
    assert len(out) == 1
    assert out[0]["is_zero_day"] is True


def test_zero_day_keyword_survives_without_cve(fixture_config):
    out = run([entry("zero-day in gadget")])
    assert len(out) == 1
    assert out[0]["cve_ids"] == []


def test_cve_plus_severity_keyword_survives(fixture_config):
    out = run([entry("critical bug CVE-2026-11111")])
    assert len(out) == 1
    assert out[0]["is_high_severity"] is True


# ── Survival gate: new priority-product path ─────────────────────────────────

def test_cve_plus_product_keyword_survives_not_high_severity(fixture_config):
    out = run([entry("pan-os bug CVE-2026-22222")])
    assert len(out) == 1
    assert out[0]["is_priority_product"] is True
    assert out[0]["is_high_severity"] is False  # ordering feature, not a severity claim


def test_product_keyword_without_cve_drops(fixture_config):
    assert run([entry("pan-os quirky behavior")]) == []


def test_cve_without_any_keyword_drops(fixture_config):
    assert run([entry("minor bug CVE-2026-88888")]) == []


def test_synthetic_gate_against_real_config():
    # The design doc's hard gate, against the REAL config/feeds.yaml.
    out = run(
        [entry("CVE-2026-99999 PAN-OS: Multiple Cross-Site Scripting")]
    )
    assert len(out) == 1
    assert out[0]["is_priority_product"] is True
    assert out[0]["is_high_severity"] is False


def test_real_config_new_vendor_feeds_and_keywords():
    # The feeds.yaml change itself: the 5 vendor feeds exist and the new
    # severity/priority keywords actually gate entries through the real config.
    with open(pf.CONFIG_PATH) as f:
        cfg = yaml.safe_load(f)
    feed_names = {feed["name"] for feed in cfg["feeds"]}
    for expected in (
        "Palo Alto Security Advisories",
        "Cisco Security Advisories (PSIRT)",
        "Fortinet PSIRT Advisories",
        "Ivanti Security Advisories",
        "Check Point Research",
    ):
        assert expected in feed_names, f"missing feed: {expected}"

    # New high-severity keyword ("authentication bypass") + CVE → kept as high-severity.
    out = run([entry("Authentication bypass CVE-2026-91111 in appliance")])
    assert len(out) == 1 and out[0]["is_high_severity"] is True

    # New priority keyword beyond pan-os ("fortios") + CVE → kept as product watch.
    out = run([entry("FortiOS update CVE-2026-92222")])
    assert len(out) == 1
    assert out[0]["is_priority_product"] is True and out[0]["is_high_severity"] is False


def test_missing_priority_product_section_defaults_empty(tmp_path, monkeypatch):
    cfg = {k: v for k, v in FIXTURE_CFG.items() if k != "priority_product_keywords"}
    cfg_path = tmp_path / "feeds.yaml"
    cfg_path.write_text(yaml.safe_dump(cfg))
    monkeypatch.setattr(pf, "CONFIG_PATH", cfg_path)
    # pp entry now drops; severity path still works — config stays backward compatible
    assert run([entry("pan-os bug CVE-2026-22222")]) == []
    assert len(run([entry("critical bug CVE-2026-11111")])) == 1


def test_fallback_extraction_when_cve_ids_not_preattached(fixture_config):
    # The title/summary fallback now lives in the pre-gate attach_cve_ids step.
    out = run([entry("critical breach CVE-2026-77777", cve_ids=None)])
    assert len(out) == 1
    assert out[0]["cve_ids"] == ["CVE-2026-77777"]


# ── Sort order ───────────────────────────────────────────────────────────────

def test_sort_order_kev_zd_hs_pp(fixture_config):
    e_pp = entry("pan-os bug CVE-2026-00004")
    e_hs = entry("critical bug CVE-2026-00003")
    e_zd = entry("zero-day found CVE-2026-00002")
    e_kev = entry("Known exploited", cve_ids=["CVE-2026-00001"], is_kev=True)
    out = pf.sort_findings(run([e_pp, e_hs, e_zd, e_kev]))  # filter no longer sorts
    titles = [e["title"] for e in out]
    assert titles == [
        "Known exploited",
        "zero-day found CVE-2026-00002",
        "critical bug CVE-2026-00003",
        "pan-os bug CVE-2026-00004",
    ]


# ── Deduplication ────────────────────────────────────────────────────────────

def test_kev_preferred_over_earlier_non_kev_duplicate(fixture_config):
    # KEV-feed entries arrive LAST in collection order (fetch_cisa_kev is appended after feeds);
    # the KEV-first pass must still make it win the CVE dedup.
    article = entry("critical flaw CVE-2026-33333")
    kev = entry("KEV: exploited flaw", cve_ids=["CVE-2026-33333"], is_kev=True)
    out = run([article, kev])
    assert len(out) == 1
    assert out[0].get("is_kev") is True


def test_zero_day_entry_not_suppressed_by_earlier_rollup(fixture_config):
    rollup = entry(
        "Monthly critical update",
        summary="Fixes CVE-2026-44444, CVE-2026-55555, CVE-2026-66666.",
    )
    zd_article = entry("zero-day exploited: CVE-2026-44444")
    out = run([rollup, zd_article])
    titles = {e["title"] for e in out}
    assert "zero-day exploited: CVE-2026-44444" in titles  # not swallowed by the roll-up
    assert len(out) == 2


def test_plain_duplicate_still_deduplicated(fixture_config):
    # Regression: two non-zd, non-KEV entries about the same CVE → one survives.
    first = entry("critical bug CVE-2026-12121", eid="a")
    second = entry("critical issue CVE-2026-12121 again", eid="b")
    out = run([first, second])
    assert len(out) == 1


def test_filter_does_not_sort(fixture_config):
    # Sorting is a separate step (sort_findings) that runs after EPSS annotation.
    e_hs = entry("critical bug CVE-2026-00003")
    e_zd = entry("zero-day found CVE-2026-00002")
    assert [e["title"] for e in run([e_hs, e_zd])] == [e_hs["title"], e_zd["title"]]


def test_priority_product_ranks_below_high_severity_above_plain(fixture_config):
    findings = [
        {"id": "plain", "published": "2026-07-26"},
        {"id": "pp", "is_priority_product": True, "published": "2026-07-01"},
        {"id": "hs", "is_high_severity": True, "published": "2026-07-02"},
        {"id": "hs-pp", "is_high_severity": True, "is_priority_product": True, "published": "2026-07-01"},
        {"id": "in-kev", "in_kev": True, "published": "2026-07-01"},
    ]
    assert [f["id"] for f in pf.sort_findings(findings)] == ["in-kev", "hs-pp", "hs", "pp", "plain"]


# ── Interaction with in_kev (any cited CVE is in the KEV catalog) ────────────

KEV_LOOKUP = {
    "CVE-2026-40003": {"date_added": "2026-07-01", "due_date": "2026-07-22",
                       "vendor": "Ivanti", "product": "Connect Secure", "ransomware": False},
    "CVE-2026-40011": {"date_added": "2026-07-01", "due_date": "2026-07-22",
                       "vendor": "Ivanti", "product": "Connect Secure", "ransomware": False},
}


def _rss_roundup(n):
    import defusedxml.ElementTree as ET
    from datetime import datetime, timezone
    from pulse.feeds import _parse_rss

    links = " ".join(f'&lt;a href="https://ex.com/CVE-2026-{40000 + i}"&gt;x&lt;/a&gt;' for i in range(n))
    xml = (f'<rss version="2.0"><channel><title>t</title><item><title>Monthly round-up</title>'
           f"<description>{links}</description></item></channel></rss>")
    return _parse_rss(ET.fromstring(xml), "TestFeed", ["test"], datetime(2000, 1, 1, tzinfo=timezone.utc))


def test_capped_roundup_citing_kev_cve_becomes_zero_day(fixture_config):
    # Keyword-less round-up; raw-element extraction keeps its first 10 CVEs, one
    # of which (CVE-2026-40003) is in KEV. With in_kev = "any cited CVE is in
    # KEV" the round-up is kept as a KEV/zero-day finding. Accepted: it IS about
    # an exploited CVE.
    out = run(_rss_roundup(60), KEV_LOOKUP)
    assert len(out) == 1
    f = out[0]
    assert len(f["cve_ids"]) == 10
    assert f["in_kev"] is True and f["is_zero_day"] is True
    assert f["is_high_severity"] is False


def test_kev_cve_beyond_the_cap_does_not_flag_roundup(fixture_config):
    # CVE-2026-40011 is the 12th id — cut by MAX_CVE_IDS_PER_ENTRY, so it can't
    # make the round-up in_kev; with no other signal the round-up drops.
    lookup = {"CVE-2026-40011": KEV_LOOKUP["CVE-2026-40011"]}
    assert run(_rss_roundup(12), lookup) == []


def test_kev_feed_entry_wins_over_in_kev_article(fixture_config):
    # An article citing a KEV CVE is in_kev (zero-day) but not is_kev; the
    # KEV-feed entry is processed first and is the one that claims the CVE.
    article = entry("Patch notes", summary="Fixes CVE-2026-40003.", eid="article")
    kev = entry("KEV: CVE-2026-40003", cve_ids=["CVE-2026-40003"], is_kev=True, eid="kev")
    out = run([article, kev], KEV_LOOKUP)
    # The article is zero-day (via in_kev) but its only CVE was already claimed
    # by a zero-day/KEV entry, so it is a duplicate.
    assert [f["id"] for f in out] == ["kev"]


def test_duplicate_zero_day_articles_still_deduplicated(fixture_config):
    # The roll-up exemption must not turn off dedup between zero-day articles:
    # the same exploited CVE covered by several news sites is one finding.
    a = entry("zero-day exploited: CVE-2026-44444", eid="a")
    b = entry("Another zero-day write-up on CVE-2026-44444", eid="b")
    out = run([a, b])
    assert [f["id"] for f in out] == ["a"]


def test_in_kev_articles_about_same_kev_cve_deduplicated(fixture_config):
    a = entry("Patch notes", summary="Fixes CVE-2026-40003.", eid="a")
    b = entry("More patch notes", summary="See CVE-2026-40003.", eid="b")
    out = run([a, b], KEV_LOOKUP)
    assert [f["id"] for f in out] == ["a"]


def test_zero_day_with_one_new_cve_survives_claimed_ones(fixture_config):
    a = entry("zero-day exploited: CVE-2026-44444", eid="a")
    b = entry("zero-day chain CVE-2026-44444 and CVE-2026-45555", eid="b")
    assert [f["id"] for f in run([a, b])] == ["a", "b"]
