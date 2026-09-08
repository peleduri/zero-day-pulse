import yaml
import pytest

import pulse.filter as pf

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


# ── Survival gate: regressions ───────────────────────────────────────────────

def test_kev_entry_survives(fixture_config):
    out = pf.filter_zero_days([entry("Some vuln", cve_ids=["CVE-2026-99990"], is_kev=True)])
    assert len(out) == 1
    assert out[0]["is_zero_day"] is True


def test_zero_day_keyword_survives_without_cve(fixture_config):
    out = pf.filter_zero_days([entry("zero-day in gadget")])
    assert len(out) == 1
    assert out[0]["cve_ids"] == []


def test_cve_plus_severity_keyword_survives(fixture_config):
    out = pf.filter_zero_days([entry("critical bug CVE-2026-11111")])
    assert len(out) == 1
    assert out[0]["is_high_severity"] is True


# ── Survival gate: new priority-product path ─────────────────────────────────

def test_cve_plus_product_keyword_survives_not_high_severity(fixture_config):
    out = pf.filter_zero_days([entry("pan-os bug CVE-2026-22222")])
    assert len(out) == 1
    assert out[0]["is_priority_product"] is True
    assert out[0]["is_high_severity"] is False  # ordering feature, not a severity claim


def test_product_keyword_without_cve_drops(fixture_config):
    assert pf.filter_zero_days([entry("pan-os quirky behavior")]) == []


def test_cve_without_any_keyword_drops(fixture_config):
    assert pf.filter_zero_days([entry("minor bug CVE-2026-88888")]) == []


def test_synthetic_gate_against_real_config():
    # The design doc's hard gate, against the REAL config/feeds.yaml.
    out = pf.filter_zero_days(
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
    out = pf.filter_zero_days([entry("Authentication bypass CVE-2026-91111 in appliance")])
    assert len(out) == 1 and out[0]["is_high_severity"] is True

    # New priority keyword beyond pan-os ("fortios") + CVE → kept as product watch.
    out = pf.filter_zero_days([entry("FortiOS update CVE-2026-92222")])
    assert len(out) == 1
    assert out[0]["is_priority_product"] is True and out[0]["is_high_severity"] is False


def test_missing_priority_product_section_defaults_empty(tmp_path, monkeypatch):
    cfg = {k: v for k, v in FIXTURE_CFG.items() if k != "priority_product_keywords"}
    cfg_path = tmp_path / "feeds.yaml"
    cfg_path.write_text(yaml.safe_dump(cfg))
    monkeypatch.setattr(pf, "CONFIG_PATH", cfg_path)
    # pp entry now drops; severity path still works — config stays backward compatible
    assert pf.filter_zero_days([entry("pan-os bug CVE-2026-22222")]) == []
    assert len(pf.filter_zero_days([entry("critical bug CVE-2026-11111")])) == 1


def test_fallback_extraction_when_cve_ids_not_preattached(fixture_config):
    out = pf.filter_zero_days([entry("critical breach CVE-2026-77777", cve_ids=None)])
    assert len(out) == 1
    assert out[0]["cve_ids"] == ["CVE-2026-77777"]


# ── Sort order ───────────────────────────────────────────────────────────────

def test_sort_order_kev_zd_hs_pp(fixture_config):
    e_pp = entry("pan-os bug CVE-2026-00004")
    e_hs = entry("critical bug CVE-2026-00003")
    e_zd = entry("zero-day found CVE-2026-00002")
    e_kev = entry("Known exploited", cve_ids=["CVE-2026-00001"], is_kev=True)
    out = pf.filter_zero_days([e_pp, e_hs, e_zd, e_kev])
    titles = [e["title"] for e in out]
    assert titles == [
        "Known exploited",
        "zero-day found CVE-2026-00002",
        "critical bug CVE-2026-00003",
        "pan-os bug CVE-2026-00004",
    ]


# ── Deduplication ────────────────────────────────────────────────────────────

def test_kev_preferred_over_earlier_non_kev_duplicate(fixture_config):
    # KEV arrives LAST in collection order (fetch_cisa_kev is appended after feeds);
    # the KEV-first pass must still make it win the CVE dedup.
    article = entry("critical flaw CVE-2026-33333")
    kev = entry("KEV: exploited flaw", cve_ids=["CVE-2026-33333"], is_kev=True)
    out = pf.filter_zero_days([article, kev])
    assert len(out) == 1
    assert out[0].get("is_kev") is True


def test_zero_day_entry_not_suppressed_by_earlier_rollup(fixture_config):
    rollup = entry(
        "Monthly critical update",
        summary="Fixes CVE-2026-44444, CVE-2026-55555, CVE-2026-66666.",
    )
    zd_article = entry("zero-day exploited: CVE-2026-44444")
    out = pf.filter_zero_days([rollup, zd_article])
    titles = {e["title"] for e in out}
    assert "zero-day exploited: CVE-2026-44444" in titles  # not swallowed by the roll-up
    assert len(out) == 2


def test_plain_duplicate_still_deduplicated(fixture_config):
    # Regression: two non-zd, non-KEV entries about the same CVE → one survives.
    first = entry("critical bug CVE-2026-12121", eid="a")
    second = entry("critical issue CVE-2026-12121 again", eid="b")
    out = pf.filter_zero_days([first, second])
    assert len(out) == 1
