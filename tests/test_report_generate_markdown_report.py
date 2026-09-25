import pytest
from pulse.report import generate_markdown_report


@pytest.fixture
def mixed_vulns():
    return [
        {
            "cve": "CVE-2024-57727",
            "title": "SimpleHelp path traversal",
            "cvss_score": 7.5,
            "source": "CISA",
            "active_exploitation": True,
        },
        {
            "cve": "CVE-2023-11111",
            "title": "Sample low‑risk issue",
            "cvss_score": 3.2,
            "source": "NVD",
            "active_exploitation": False,
        },
    ]


def test_generate_markdown_report_contains_active_section(mixed_vulns):
    md = generate_markdown_report(mixed_vulns)

    # The active section header must be present
    assert "## 🟢 Actively Exploited Vulnerabilities" in md

    # The active CVE should appear under that section
    assert "- **CVE-2024-57727**" in md

    # The non‑active CVE must NOT appear in the active section
    # (it will appear later in the full list)
    active_section = md.split("## 🟢 Actively Exploited Vulnerabilities")[1]
    assert "CVE-2023-11111" not in active_section
