# Zero Day Pulse

> **Generated:** 2026-09-22 15:52 UTC &nbsp;|&nbsp; **Total:** 17 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 13 &nbsp;|&nbsp; 🟡 High: 4 &nbsp;|&nbsp; ✨ Enriched: 0

---

## 1. 🟠 Zero-Day — Improve Router Hygiene to Protect Against Russian State-Sponsored Targeting

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Wed, 08 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a>

> Russian Government-Sponsored Activity Targets Poorly Configured and Vulnerable Devices Across Critical Sectors Executive summary Russian Federal Security Service (FSB) Center 16 cyber actors continue to exploit poorly configured and vulnerable networking devices worldwide, opportunistically compromising multiple critical infrastructure sector networks. This joint Cybersecurity Advisory (CSA) build…

---

## 2. 🟠 Zero-Day — September 2026 Patch Tuesday: Two Exploited Zero-Days and 113 Critical Vulnerabilities Among 972 CVEs

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Sep 08, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-september-2026/>

---

## 3. 🟠 Zero-Day — @aborruso/ckan-mcp-server has SSRF via DNS-name → internal IP — incomplete fix of CVE-2026-53509

**CVE:** `CVE-2026-61612` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://github.com/advisories/GHSA-798p-78g2-v556>

> ## Summary
The SSRF guard `validateServerUrl` (added for CVE-2026-33060, extended for CVE-2026-53509) validates only the **hostname string** and never resolves DNS. Any caller-supplied `server_url` whose hostname *resolves* to an internal address passes the guard, so the server issues requests to **loopback and cloud metadata (`169.254.169.254`)**. This is a third bypass of the same guard, still p…

---

## 4. 🟠 Zero-Day — @roomi-fields/notebooklm-mcp has a path traversal in vault.batch tool that allows arbitrary file write outside intended vault directory

**CVE:** `CVE-2026-61647` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://github.com/advisories/GHSA-jjhp-8crj-mppq>

> ## Summary

The `vault_batch` MCP tool (and the equivalent `POST /batch-to-vault` HTTP endpoint) accepted a caller-supplied `vault_dir` path that was passed directly to `path.resolve()` + `fs.mkdir()` with no containment check. A caller — or a prompt-injected LLM driving the MCP — could therefore create directories and write `.md` / `.json` answer files anywhere the server process can write.

The …

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 10. 🟠 Zero-Day — Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite

**CVE:** `CVE-2025-66376` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Tue, 21 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a>

> Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite Executive summary A group of Russian state-supported cyber actors has been targeting and compromising various Western government and commercial organizations using the Zimbra Collaboration Suite (ZCS) software since at least July 2025. The Russian state-supported advanced persistent threat …

---

## 11. 🟠 Zero-Day — D-Link warns of max severity zero-day bug in DIR-822A routers

**CVE:** `CVE-2026-86296` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://www.bleepingcomputer.com/news/security/d-link-warns-of-max-severity-zero-day-bug-in-dir-822a-routers/>

> D-Link warned customers of a maximum-severity vulnerability (CVE-2026-86296) with public proof-of-concept (PoC) exploit code and no patch, affecting legacy DIR-822A dual-band Wi-Fi routers. [...]

---

## 12. 🟠 Zero-Day — New CVSS 10.0 VeloCloud Orchestrator Flaw Actively Exploited in Certificate-Based Setups

**CVE:** `CVE-2026-93952` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://thehackernews.com/2026/09/new-cvss-100-velocloud-orchestrator.html>

> Attackers are exploiting a new flaw in on-premises VeloCloud Orchestrator (VCO), the server that manages the Edge devices in a VeloCloud SD-WAN, Arista said on September 22.

The flaw, tracked as CVE-2026-93952, may allow a remote attacker with no login access to privilege internal functions and affect the VCO host. Only orchestrators set up to authenticate their Edges with certificates are

---

## 13. 🟠 Zero-Day — New Windows Defender zero-day blocks Microsoft antivirus updates

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://www.bleepingcomputer.com/news/security/new-windows-defender-zero-day-blocks-microsoft-antivirus-updates/>

> Over the weekend, security researcher Abdelhamid Naceri (also known as Nightmare Eclipse) released another Microsoft Defender zero-day exploit that blocks antivirus updates. [...]

---

## 14. 🟡 High Severity — SharePoint Flaw Initially Listed as Spoofing by Microsoft Enables Authenticated RCE

**CVE:** `CVE-2026-65660` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://thehackernews.com/2026/09/sharepoint-flaw-initially-listed-as.html>

> A SharePoint Server vulnerability that Microsoft initially classified as a spoofing flaw with a CVSS score of 6.5 actually enables authenticated remote code execution, according to full technical details published today by Viettel Cyber Security researcher Dinh Ho Anh Khoa.

The flaw, CVE-2026-65660, affects SharePoint Server 2016, 2019, and Subscription Edition. Patches have been

---

## 15. 🟡 High Severity — Zyxel and Veeam Flaws Under Active Exploitation With Command and SYSTEM Access

**CVE:** `CVE-2026-7273` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://thehackernews.com/2026/09/zyxel-and-veeam-flaws-under-active.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Monday added a now-patched security flaw impacting Zyxel GS1900 series switches to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

The vulnerability, tracked as CVE-2026-7273 (CVSS score: 8.8), is a stack-based buffer overflow vulnerability that could result in arbitrary operating

---

## 16. 🟡 High Severity — nginx ignition has TOTP Reuse During Validity Window

**CVE:** `CVE-2026-61630` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-21
**Reference:** <https://github.com/advisories/GHSA-hf33-q6cf-c66f>

> ### Summary
Any user that has enabled the OTP 2FA can have their TOTP reused during the standard 30 second validity window.

### Details
The https://github.com/pquerna/otp package [doesn&#x27;t include](https://github.com/pquerna/otp/issues/61) checking for already used TOTPs within its the validity window. This requires each application that uses the package to implement their own method of track…

---

## 17. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
