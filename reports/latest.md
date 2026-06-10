# Zero Day Pulse

> **Generated:** 2026-06-10 09:39 UTC &nbsp;|&nbsp; **Total:** 21 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 17 &nbsp;|&nbsp; 🟡 High: 4 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE‑2024‑57727 is a directory‑traversal vulnerability in SimpleHelp RMM that allows unauthenticated remote attackers to read arbitrary files on the system, enabling retrieval of logs, configuration data, and credentials.
- **Affected Products:** SimpleHelp remote support software version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (generic)
- **Mitigation:** Apply the vendor‑released patch (upgrade SimpleHelp to a version newer than 5.5.7). If immediate patching is not possible, limit network exposure of the SimpleHelp service and enforce strict access controls.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — Microsoft Defender 'RoguePlanet' zero-day grants SYSTEM privileges

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.bleepingcomputer.com/news/microsoft/microsoft-defender-rogueplanet-zero-day-grants-system-privileges/>

> A security researcher has released a new Microsoft Defender zero-day exploit named &quot;RoguePlanet&quot; just hours after Microsoft fixed two previously disclosed flaws during June 2026 Patch Tuesday. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Public PoC exploits a race condition in Microsoft Defender leading to arbitrary code execution and escalation to SYSTEM privileges; exact vulnerable component and exploit steps unavailable in vendor advisory.
- **Affected Products:** Microsoft Defender for Endpoint/Windows Defender components on supported Windows versions (specific versions unavailable)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — https://thehackernews.com/2026/06/microsoft-defender-rogueplanet-zero-day.html
- **Patch Available:** false — no official vendor patch reported; Microsoft June 2026 Patch Tuesday fixed other issues but not RoguePlanet.
- **Active Exploitation:** true — https://thehackernews.com/2026/06/microsoft-defender-rogueplanet-zero-day.html, https://www.bleepingcomputer.com/news/microsoft/microsoft-defender-rogueplanet-zero-day-grants-system-privileges/
- **Threat Actors:** None known
- **Mitigation:** Disable or restrict Microsoft Defender real‑time components where feasible, enforce least‑privilege, apply network‑level protections, and monitor for suspicious high‑privilege process creation. (Specific vendor mitigations unavailable.)
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — Patch Tuesday - June 2026

**CVE:** `CVE-2026-33825` | `CVE-2026-45585` | `CVE-2026-45498` | `CVE-2026-41091` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.rapid7.com/blog/post/em-patch-tuesday-june-2026>

> Microsoft is publishing 200 vulnerabilities on June 2026 Patch Tuesday . Microsoft is not aware of exploitation in the wild for any of these vulnerabilities, and is aware of public disclosure for three. This is similar to last month’s Patch Tuesday, however several of last month’s vulnerabilities ended up on CISA KEV in the days following their publication. So far this month, Microsoft has provide…

**Parallel AI Enrichment:**

- **Technical Details:** Insufficient granularity of access control in Microsoft Defender allows an authorized attacker to elevate privileges locally via a race condition in the file remediation logic.
- **Affected Products:** Microsoft Defender (Windows Defender) on supported Windows platforms
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-33825
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor patch; restrict local user privileges and enforce least‑privilege policies; if the patch is delayed, limit access to Defender components and monitor for suspicious local privilege escalation attempts.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-33825

---

## 4. 🟠 Zero-Day — Microsoft’s June 2026 Patch Tuesday Addresses 198 CVEs ( CVE-2026-49160, CVE-2026-50507)

**CVE:** `CVE-2026-49160` | `CVE-2026-50507` | `CVE-2025-10263` | `CVE-2026-8863` &nbsp;|&nbsp; **Source:** Tenable Security Research &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.tenable.com/blog/microsofts-june-2026-patch-tuesday-addresses-198-cves-cve-2026-49160-cve-2026-50507>

> 32 Critical 166 Important 0 Moderate 0 Low Microsoft addresses 198 CVEs in the largest Patch Tuesday release, including three zero-days. Microsoft patched 198 CVEs in its June 2026 Patch Tuesday release, with 32 rated critical and 166 rated as important. Our counts omitted 6 CVEs that were already addressed by Microsoft via servicing and do not require additional customer action to resolve as well…

**Parallel AI Enrichment:**

- **Technical Details:** Resource exhaustion in HTTP/2 allows an unauthenticated remote attacker to trigger uncontrolled resource consumption leading to denial-of-service by exhausting server resources ("HTTP/2 Bomb").
- **Affected Products:** HTTP.sys (Windows HTTP/2 implementation)
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Exploit Available:** false
- **Patch Available:** true — https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-49160
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply Microsoft updates; if patch unavailable, mitigate by disabling HTTP/2 or limiting HTTP/2 connections via IIS/HTTP.sys configuration.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-49160

---

## 5. 🟠 Zero-Day — Microsoft June 2026 Patch Tuesday fixes 3 zero-day, 200 flaws

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.bleepingcomputer.com/news/microsoft/microsoft-june-2026-patch-tuesday-fixes-3-zero-day-200-flaws/>

> Today is Microsoft&#x27;s June 2026 Patch Tuesday, with security updates for 200 flaws and three publicly disclosed zero-day vulnerabilities. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (source: https://www.bleepingcomputer.com/news/microsoft/microsoft-june-2026-patch-tuesday-fixes-3-zero-day-200-flaws/)
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 6. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when malicious instructions are embedded in external web content or retrieval corpora and then incorporated into an LLM’s prompt (e.g., via RAG or browsing agents), causing the model to follow attacker‑supplied instructions. End‑to‑end IPI exploits have been demonstrated against RAG and agentic systems under realistic queries.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Hardening guidance per vendor: sanitize or filter retrieved content, use strict source allowlists, prompt integrity checks, retrieval provenance, model output validation, and apply vendor updates. See Google advisory for specific mitigations.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 7. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) tricks LLM‑powered Workspace/Gemini by inserting malicious instructions into secondary data sources (emails, documents, calendar invites, comments) or tool outputs that the model consumes while fulfilling a user’s request. Attackers can chain IPI with other vulnerabilities (e.g., zero‑click GeminiJack) to exfiltrate data or alter agent behavior without user interaction. CVE‑2025‑54131 references an attack chain involving IPI; GeminiJack uses crafted content to trigger unintended model behavior and data leakage.
- **Affected Products:** Google Workspace (Gemini in Workspace / Gemini Enterprise), Gemini CLI prior to version 1.3
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Multi‑layered mitigations recommended by vendor: continuous monitoring for known IPI patterns, content provenance and integrity checks, sanitization and strict parsing of external content, policy‑based tool and data source access controls, least‑privilege for agentic actions, keep Gemini CLI and Workspace components updated (apply vendor patches), defensive detection of payload patterns, and privilege/network isolation for automated agents.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 8. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The primary risk is indirect prompt injection: malicious webpage content can craft inputs that influence an AI agent embedded in the browser to perform unsafe actions or disclose sensitive data. Google describes layered defenses (prompt sanitization/restrictions, origin access restrictions, and an oversight agent) to limit these attacks.
- **Affected Products:** Google Chrome (agentic browsing / Gemini integration)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply vendor updates; enable Chrome’s agentic‑browsing protections; follow vendor guidance (restrict origin access, sanitize or ignore untrusted page‑provided prompts, require user confirmation for sensitive actions, and use oversight/approval flows).
- **Vendor Advisory:** http://blog.google/security/architecting-security-for-agentic

---

## 9. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** The blog provides a high‑level overview of Android’s memory‑safety program and reports that after adopting Rust, memory‑safety vulnerabilities fell below 20% of total; it does not describe a specific vulnerability or attack vector.
- **Affected Products:** Android platform (first‑party and third‑party/open‑source code changes across C, C++, Java, Kotlin, Rust)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Continue adopting Rust and memory‑safety practices in Android code; follow Android security bulletins and vendor guidance.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 10. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection involves embedding hidden malicious instructions in external data sources such as emails, documents, or calendar invites. When the AI processes this data, the hidden instructions are executed, allowing the attacker to exfiltrate data or trigger rogue actions without direct user input.
- **Affected Products:** Google Gemini app version <1.3
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Implement Google's layered defense strategy: validate and sanitize all external inputs, enforce strict context handling policies, apply runtime monitoring for anomalous AI behavior, and keep the Gemini app updated to the latest patched version.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 11. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

---

## 12. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 13. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

---

## 14. 🟠 Zero-Day — No Patch Planned for Exploited Arista EOS Vulnerability

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://www.securityweek.com/no-patch-planned-for-exploited-arista-eos-vulnerability/>

> Organizations are advised to apply vendor-supplied mitigations or discontinue the vulnerable devices. The post No Patch Planned for Exploited Arista EOS Vulnerability appeared first on SecurityWeek .

---

## 15. 🟠 Zero-Day — Microsoft Defender RoguePlanet Zero-Day Grants SYSTEM Access on Updated Windows

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://thehackernews.com/2026/06/microsoft-defender-rogueplanet-zero-day.html>

> The anonymous security researcher going by the name Chaotic Eclipse (aka Nightmare-Eclipse) has released a proof-of-concept (PoC) exploit for yet another Microsoft Defender zero-day named RoguePlanet.

&quot;The exploit is a race condition, so it&#x27;s a hit or miss,&quot; the researcher, who published the exploit under a new GitHub account, &quot;MSNightmare&quot; said. &quot;I have managed to g…

---

## 16. 🟠 Zero-Day — SymfonyRuntime CVE-2024-50340 Patch Bypass: Web Requests Can Still Set APP_ENV/APP_DEBUG via parse_str/SAPI Argv Mismatch

**CVE:** `CVE-2026-47767` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://github.com/advisories/GHSA-fqc7-9xjw-jrh3>

> ### Description

CVE-2024-50340 (GHSA-x8vp-gf4q-mw5j) addressed an issue where, with `register_argc_argv=On`, a crafted query string let an unauthenticated GET change the kernel environment and debug flag by feeding `--env`/`--no-debug` through `$_SERVER[&#x27;argv&#x27;]`. The fix shipped in `symfony/runtime` 5.4.46 / 6.4.14 / 7.1.7 gated the argv read on `empty($_GET)` as a proxy for &quot;is th…

---

## 17. 🟠 Zero-Day — Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now

**CVE:** `CVE-2026-11645` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://thehackernews.com/2026/06/chrome-v8-zero-day-cve-2026-11645.html>

> Google has released security updates to address 74 vulnerabilities, including one that has come under active exploitation in the wild.

The high-severity vulnerability, tracked as CVE-2026-11645 (CVSS score: 8.8), has been described as an out-of-bounds memory access in V8, Chrome&#x27;s JavaScript and WebAssembly engine.

&quot;Out-of-bounds read and write in V8 in Google Chrome prior to 149.0.782…

---

## 18. 🟡 High Severity — Pheditor: OS Command Injection in terminal handler via unsanitized 'dir' parameter

**CVE:** `CVE-2026-48030` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://github.com/advisories/GHSA-jvc5-6g7q-c843>

> ### Summary

An OS Command Injection vulnerability in the terminal action handler allows any authenticated user to execute arbitrary OS commands by injecting shell metacharacters into the &#x27;dir&#x27; POST parameter, completely bypassing the TERMINAL_COMMANDS whitelist and achieving full Remote Code Execution with web server privileges.

### Details

The terminal handler in pheditor.php accepts…

---

## 19. 🟡 High Severity — PhoenixStorybook: Unauthenticated remote code execution via HEEx template injection in phoenix_storybook playground

**CVE:** `CVE-2026-8467` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://github.com/advisories/GHSA-55hg-8qxv-qj4p>

> ### Summary
An unsafe HEEx template generation vulnerability allows any unauthenticated user to execute arbitrary code on the server. The phoenix_storybook playground accepts user-controlled attribute values over WebSocket and interpolates them unsanitized into a HEEx template that is subsequently compiled and evaluated with full Elixir `Kernel` access.

### Details
The vulnerability is a three-st…

---

## 20. 🟡 High Severity — Veeam Backup & Replication RCE Flaw Lets Domain Users Run Remote Code

**CVE:** `CVE-2026-44963` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://thehackernews.com/2026/06/veeam-backup-replication-rce-flaw-lets.html>

> Veeam has released security patches to address a critical flaw in its Backup &amp; Replication software that could result in remote code execution.

Tracked as CVE-2026-44963, the vulnerability carries a CVSS score of 9.4 out of a maximum of 10.0.

&quot;A vulnerability allowing remote code execution (RCE) on the Backup Server by an authenticated domain user,&quot; Veeam said in a Tuesday advisory…

---

## 21. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
