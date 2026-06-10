# Zero Day Pulse

> **Generated:** 2026-06-10 14:49 UTC &nbsp;|&nbsp; **Total:** 32 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 19 &nbsp;|&nbsp; 🟡 High: 13 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE‑2024‑57727 is a directory traversal vulnerability that permits unauthenticated remote attackers to read sensitive files by supplying crafted file path parameters to SimpleHelp RMM components.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (unspecified)
- **Mitigation:** Upgrade SimpleHelp to a version newer than 5.5.7, apply vendor patches when released, and restrict network access to the RMM service.
- **Vendor Advisory:** https://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — New Windows Zero-Day Exploit ‘RoguePlanet’ Released

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://www.securityweek.com/new-windows-zero-day-exploit-rogueplanet-released/>

> Exploiting a race condition in Microsoft Defender, the exploit leads to local privilege escalation to SYSTEM. The post New Windows Zero-Day Exploit ‘RoguePlanet’ Released appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** RoguePlanet exploits a race condition in Microsoft Defender to achieve local privilege escalation to SYSTEM. The PoC tricks a victim into opening a .vhd(x) file on a remote SMB share, allowing redirection of a cleaned file and can bypass BitLocker via NTFS.sys.
- **Affected Products:** Microsoft Defender on Windows 10, Microsoft Defender on Windows 11
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the latest Windows and Microsoft Defender updates, restrict local file/SMB exposure, and treat the PoC as functional. Specific workaround steps are not detailed.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — Microsoft Patches Record 206 Flaws, Including Three Zero-Days and Critical RCE Bugs

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://thehackernews.com/2026/06/microsoft-patches-record-206-flaws.html>

> Microsoft on Tuesday released fixes for a record 206 security vulnerabilities impacting its software portfolio, including three flaws that have been publicly disclosed at the time of release.

Of the 206 flaws, 39 are rated Critical, and 167 are rated Important in severity. This includes 63 privilege escalation, 56 remote code execution, 30 information disclosure, 27 spoofing, 20 security

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-45657 is a use‑after‑free vulnerability in the Windows Kernel that allows an attacker to achieve remote code execution by sending crafted network traffic. CVE-2026-45585 bypasses Windows BitLocker security, enabling unauthorized access to encrypted volumes.
- **Affected Products:** Windows Kernel (all supported versions), Windows BitLocker
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (PoC YellowKey – https://thehackernews.com/2026/06/microsoft-patches-record-206-flaws.html)
- **Patch Available:** true (https://msrc.microsoft.com/update-guide/releaseNote/2026-Jun)
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Apply the Microsoft security updates released in June 2026 to all affected systems.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/releaseNote/2026-Jun

---

## 4. 🟠 Zero-Day — Microsoft Defender 'RoguePlanet' zero-day grants SYSTEM privileges

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.bleepingcomputer.com/news/microsoft/microsoft-defender-rogueplanet-zero-day-grants-system-privileges/>

> A security researcher has released a new Microsoft Defender zero-day exploit named &quot;RoguePlanet&quot; just hours after Microsoft fixed two previously disclosed flaws during June 2026 Patch Tuesday. [...]

**Parallel AI Enrichment:**

- **Technical Details:** The exploit (named RoguePlanet) targets a race condition in Microsoft Defender that allows local privilege escalation to SYSTEM by exploiting a time‑of‑check/time‑of‑use or similar race during Defender operations, leading to a SYSTEM‑level shell when successful.
- **Affected Products:** Microsoft Defender (Windows)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Disable or limit Microsoft Defender real-time components where feasible, apply principle of least privilege, and isolate untrusted code execution until vendor advisory/patch is available. Monitor vendor advisories for updates.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — Patch Tuesday - June 2026

**CVE:** `CVE-2026-33825` | `CVE-2026-45585` | `CVE-2026-45498` | `CVE-2026-41091` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.rapid7.com/blog/post/em-patch-tuesday-june-2026>

> Microsoft is publishing 200 vulnerabilities on June 2026 Patch Tuesday . Microsoft is not aware of exploitation in the wild for any of these vulnerabilities, and is aware of public disclosure for three. This is similar to last month’s Patch Tuesday, however several of last month’s vulnerabilities ended up on CISA KEV in the days following their publication. So far this month, Microsoft has provide…

**Parallel AI Enrichment:**

- **Technical Details:** Race/logic flaw in Defender file remediation and insufficient access‑control granularity allow an authorized attacker to elevate privileges to SYSTEM.
- **Affected Products:** Microsoft Defender (Windows)
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply the Microsoft patch; follow the mitigation guidance published in the Microsoft advisory. If a patch were unavailable, implement the workarounds recommended by Microsoft.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33825

---

## 6. 🟠 Zero-Day — Microsoft’s June 2026 Patch Tuesday Addresses 198 CVEs ( CVE-2026-49160, CVE-2026-50507)

**CVE:** `CVE-2026-49160` | `CVE-2026-50507` | `CVE-2025-10263` | `CVE-2026-8863` &nbsp;|&nbsp; **Source:** Tenable Security Research &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.tenable.com/blog/microsofts-june-2026-patch-tuesday-addresses-198-cves-cve-2026-49160-cve-2026-50507>

> 32 Critical 166 Important 0 Moderate 0 Low Microsoft addresses 198 CVEs in the largest Patch Tuesday release, including three zero-days. Microsoft patched 198 CVEs in its June 2026 Patch Tuesday release, with 32 rated critical and 166 rated as important. Our counts omitted 6 CVEs that were already addressed by Microsoft via servicing and do not require additional customer action to resolve as well…

**Parallel AI Enrichment:**

- **Technical Details:** Uncontrolled resource consumption in HTTP/2 handling in HTTP.sys allows an unauthenticated remote attacker to cause denial of service by sending specially crafted HTTP/2 requests that exhaust server resources (dubbed “HTTP/2 Bomb”).
- **Affected Products:** Windows HTTP.sys (HTTP/2)
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true - https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-49160
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Configure the MaxHeadersCount registry setting to limit the number of headers in HTTP/2 and HTTP/3 requests and apply the June 2026 security updates promptly.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-49160

---

## 7. 🟠 Zero-Day — Microsoft June 2026 Patch Tuesday fixes 3 zero-day, 200 flaws

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.bleepingcomputer.com/news/microsoft/microsoft-june-2026-patch-tuesday-fixes-3-zero-day-200-flaws/>

> Today is Microsoft&#x27;s June 2026 Patch Tuesday, with security updates for 200 flaws and three publicly disclosed zero-day vulnerabilities. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an adversary injects malicious instructions into external content (web pages, documents, or retrieval corpora) that an LLM‑based agent fetches during RAG or agentic workflows; the model then incorporates those instructions, leading to unauthorized behaviors (e.g., data exfiltration, bypassing safety). Notable end‑to‑end IPI exploits include "GeminiJack" (zero‑click via indirect prompt injection) and academic demonstrations using natural queries and poisoned external corpora.
- **Affected Products:** LLM-based agents and retrieval-augmented systems (no specific product versions listed)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply vendor hardening guidance: content filtering and sanitization of retrieved content, strict tool‑use and code execution policies, provenance tracking, RAG retrieval validation, prompt sanitization, model instruction boundaries, user confirmation for high‑risk actions, continuous monitoring and threat intelligence sharing.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 9. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) abuses external data sources or agentic tools consumed by an LLM to inject malicious instructions which the model may execute when fulfilling a user query; it can be zero‑click when the LLM ingests attacker‑controlled content (e.g., email, web content, files) without direct user input, causing the model or downstream agents to perform unintended actions.
- **Affected Products:** Google Workspace integrations using Gemini (e.g., Gemini Enterprise)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Google's layered defenses (content filtering, provenance signals, context sanitization, tool access controls, telemetry/monitoring, human review) and vendor hardening for Workspace + Gemini; reduce attacker‑controlled inputs, enforce least‑privilege for agent tooling, validate/sanitize external data, monitor for IPI patterns, and apply vendor guidance from the Google Security Blog.
- **Vendor Advisory:** http://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections

---

## 10. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) – attacker‑controlled web content injects instructions that an agentic browser or AI‑assisted feature may execute indirectly, e.g., via page content or comments, and can be chained with other vulnerabilities (such as CVE‑2025‑54131) to exfiltrate data or trigger actions.
- **Affected Products:** Google Chrome (agentic/Gemini features)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability
- **Patch Available:** true — http://blog.google/security/architecting-security-for-agentic.html
- **Active Exploitation:** true — https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability, https://nvd.nist.gov/vuln/detail/CVE-2025-54131
- **Threat Actors:** None known
- **Mitigation:** Apply vendor updates; enable Chrome’s latest stable release with Gemini/agentic security patches; follow Google guidance to restrict agentic features, limit origin access, and block untrusted content. Monitor for IPI payloads and sanitize/validate outputs from agentic features.
- **Vendor Advisory:** http://blog.google/security/architecting-security-for-agentic.html

---

## 11. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

---

## 12. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 13. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

---

## 14. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 15. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

---

## 16. 🟠 Zero-Day — Microsoft patches Exchange Server zero-day exploited in attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-exchange-server-zero-day-exploited-in-attacks/>

> Microsoft has patched an actively exploited Exchange Server vulnerability that allows threat actors to execute arbitrary JavaScript code in cross-site scripting (XSS) attacks targeting Outlook Web Access users. [...]

---

## 17. 🟠 Zero-Day — Microsoft patches YellowKey, GreenPlasma, MiniPlasma zero-days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-yellowkey-greenplasma-miniplasma-zero-days/>

> On Tuesday, Microsoft patched two zero-day vulnerabilities that let attackers gain SYSTEM privileges on fully patched Windows systems, and a third one that grants access to BitLocker-protected drives. [...]

---

## 18. 🟠 Zero-Day — Microsoft Defender RoguePlanet Zero-Day Grants SYSTEM Access on Updated Windows

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://thehackernews.com/2026/06/microsoft-defender-rogueplanet-zero-day.html>

> The anonymous security researcher going by the name Chaotic Eclipse (aka Nightmare-Eclipse) has released a proof-of-concept (PoC) exploit for yet another Microsoft Defender zero-day named RoguePlanet.

&quot;The exploit is a race condition, so it&#x27;s a hit or miss,&quot; the researcher, who published the exploit under a new GitHub account, &quot;MSNightmare&quot; said. &quot;I have managed to g…

---

## 19. 🟠 Zero-Day — SymfonyRuntime CVE-2024-50340 Patch Bypass: Web Requests Can Still Set APP_ENV/APP_DEBUG via parse_str/SAPI Argv Mismatch

**CVE:** `CVE-2026-47767` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://github.com/advisories/GHSA-fqc7-9xjw-jrh3>

> ### Description

CVE-2024-50340 (GHSA-x8vp-gf4q-mw5j) addressed an issue where, with `register_argc_argv=On`, a crafted query string let an unauthenticated GET change the kernel environment and debug flag by feeding `--env`/`--no-debug` through `$_SERVER[&#x27;argv&#x27;]`. The fix shipped in `symfony/runtime` 5.4.46 / 6.4.14 / 7.1.7 gated the argv read on `empty($_GET)` as a proxy for &quot;is th…

---

## 20. 🟡 High Severity — Nezha's private services (`EnableShowInService: false`) are enumerable via per-server endpoints, leaking name and timing data

**CVE:** `CVE-2026-49397` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-vrmh-5mmx-hjwx>

> # Private services (`EnableShowInService: false`) are enumerable via per-server endpoints, leaking name and timing data

**CWE**: CWE-285 (Improper Authorization) via CWE-200 (Exposure of Sensitive Information to an Unauthorized Actor) and CWE-863 (Incorrect Authorization — inconsistent gating across data-reader paths)

**CVSS v3.1**: `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N` → 5.3 (Medium)

…

---

## 21. 🟡 High Severity — Go Restful API Boilerplate: Hardcoded JWT Secret "random" Allows Token Forgery

**CVE:** `CVE-2026-48031` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-mqq6-462x-jxmm>

> ## Vulnerability: CWE-798 — Hardcoded JWT Secret + Broken Mitigation

### Affected Component
- `github.com/dhax/go-base` — Go REST API boilerplate (go-chi/jwtauth/v5, Viper, PostgreSQL/Bun)
- 1,685 stars on GitHub

### Vulnerability Locations

| File | Line | Role |
|------|------|------|
| `dev.env` | 10 | `AUTH_JWT_SECRET=random` — template default shipped to all users |
| `cmd/serve.go` | 35 | …

---

## 22. 🟡 High Severity — Papra HTTP redirect bypass can lead to SSRF via webhook delivery system

**CVE:** `CVE-2026-48051` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-5g86-85rp-f9hx>

> ### Summary

Papra&#x27;s webhook delivery system contains an SSRF protection bypass that allows any authenticated organisation member to cause the server to make HTTP requests to internal addresses — loopback, link-local, and RFC-1918 ranges. The SSRF protection validates the registered webhook URL but ignores redirect destinations. The HTTP client (`ofetch`) follows 3xx responses automatically, …

---

## 23. 🟡 High Severity — @hulumi/baseline: AccountFoundation reuse paths silently downgrade GuardDuty / Security Hub posture

**CVE:** `CVE-2026-48037` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-cj8g-prcm-mfg5>

> **Affected:** `@hulumi/baseline` `&lt; 1.4.0` — **Fixed in:** `1.4.0` — **Severity:** Medium — **CWE-693 (Protection Mechanism Failure)**

#### Summary

`AccountFoundation` can either create AWS detective services (GuardDuty for threat detection, Security Hub for compliance dashboards) or reuse pre-existing ones via opt-in flags. The reuse paths just imported the existing resources and reported su…

---

## 24. 🟡 High Severity — @hulumi/baseline: AccountFoundation audit-delivery S3 bucket could be silently weakened

**CVE:** `CVE-2026-48035` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-2mxr-p26x-mj73>

> **Affected:** `@hulumi/baseline` `&lt; 1.4.0` — **Fixed in:** `1.4.0` — **Severity:** High — **CWE-1059 (Insufficient Technical Documentation / Behavioral Inconsistency)**

#### Summary

The S3 bucket that `AccountFoundation` creates to receive CloudTrail and AWS Config audit logs is meant to be tamper-resistant — if someone with delete access can erase from it, the forensic trail is gone. There w…

---

## 25. 🟡 High Severity — @hulumi/policies has a HULUMI-H5 bypass via decoy sibling resources targeting a different bucket

**CVE:** `CVE-2026-48034` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-9vc9-4jv3-rf86>

> **Affected:** `@hulumi/policies` `&lt; 1.4.0` — **Fixed in:** `1.4.0` — **Severity:** High — **CWE-284 (Improper Access Control)**

#### Summary

HULUMI-H1 forbids raw `aws:s3:Bucket` outside of Hulumi&#x27;s `SecureBucket` component, with one exemption: a raw bucket that&#x27;s a child of a `SecureBucket` is allowed because the component is responsible for the hardening. HULUMI-H5 is the defence-…

---

## 26. 🟡 High Severity — @hulumi/policies bypasses policy packs with a forged Pulumi-URN logical name

**CVE:** `CVE-2026-48033` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-rhgj-6g2c-frmm>

> **Affected:** `@hulumi/policies` `&lt; 1.4.0` — **Fixed in:** `1.4.0` — **Severity:** High — **CWE-693 (Protection Mechanism Failure)**

#### Summary

Pulumi gives every cloud resource a structured URN that includes the resource&#x27;s type chain (`hulumi:baseline:aws:SecureBucket$aws:s3/bucketV2:BucketV2`) and the _logical name_ the developer freely chose (anything after the final `::`). Several …

---

## 27. 🟡 High Severity — @hulumi/policies bypasses IAM-role policy checks when the role trusts multiple OIDC providers

**CVE:** `CVE-2026-48032` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-g759-4pxw-6692>

> **Affected:** `@hulumi/policies` `&lt; 1.4.0` — **Fixed in:** `1.4.0` — **Severity:** High — **CWE-697 (Incorrect Comparison)**

#### Summary

AWS IAM trust policies can list more than one federated identity provider — for example, a role that accepts BOTH GitHub Actions OIDC and Google&#x27;s OIDC. The `G_OIDC_1` and `G_OIDC_2` policy rules are supposed to flag IAM roles whose GitHub-OIDC trust i…

---

## 28. 🟡 High Severity — CVE-2026-10520, CVE-2026-10523 - Multiple critical vulnerabilities affecting Ivanti Sentry

**CVE:** `CVE-2026-10520` | `CVE-2026-10523` | `CVE-2023-38035` | `CVE-2020-15505` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://www.rapid7.com/blog/post/etr-cve-2026-10520-cve-2026-10523-multiple-critical-vulnerabilities-affecting-ivanti-sentry>

> Overview On June 9, 2026, Ivanti published a security advisory for two critical vulnerabilities affecting Ivanti Sentry (formerly known as MobileIron Sentry), which per the vendor website is an “in-line gateway that manages, encrypts, and secures traffic between the mobile device and back-end enterprise systems”. The most severe issue, CVE-2026-10520 , is an OS command injection vulnerability with…

---

## 29. 🟡 High Severity — Pheditor: OS Command Injection in terminal handler via unsanitized 'dir' parameter

**CVE:** `CVE-2026-48030` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://github.com/advisories/GHSA-jvc5-6g7q-c843>

> ### Summary

An OS Command Injection vulnerability in the terminal action handler allows any authenticated user to execute arbitrary OS commands by injecting shell metacharacters into the &#x27;dir&#x27; POST parameter, completely bypassing the TERMINAL_COMMANDS whitelist and achieving full Remote Code Execution with web server privileges.

### Details

The terminal handler in pheditor.php accepts…

---

## 30. 🟡 High Severity — PhoenixStorybook: Unauthenticated remote code execution via HEEx template injection in phoenix_storybook playground

**CVE:** `CVE-2026-8467` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://github.com/advisories/GHSA-55hg-8qxv-qj4p>

> ### Summary
An unsafe HEEx template generation vulnerability allows any unauthenticated user to execute arbitrary code on the server. The phoenix_storybook playground accepts user-controlled attribute values over WebSocket and interpolates them unsanitized into a HEEx template that is subsequently compiled and evaluated with full Elixir `Kernel` access.

### Details
The vulnerability is a three-st…

---

## 31. 🟡 High Severity — Veeam Backup & Replication RCE Flaw Lets Domain Users Run Remote Code

**CVE:** `CVE-2026-44963` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://thehackernews.com/2026/06/veeam-backup-replication-rce-flaw-lets.html>

> Veeam has released security patches to address a critical flaw in its Backup &amp; Replication software that could result in remote code execution.

Tracked as CVE-2026-44963, the vulnerability carries a CVSS score of 9.4 out of a maximum of 10.0.

&quot;A vulnerability allowing remote code execution (RCE) on the Backup Server by an authenticated domain user,&quot; Veeam said in a Tuesday advisory…

---

## 32. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
