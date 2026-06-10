# Zero Day Pulse

> **Generated:** 2026-06-10 02:08 UTC &nbsp;|&nbsp; **Total:** 23 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 18 &nbsp;|&nbsp; 🟡 High: 5 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is a directory traversal flaw that enables unauthenticated remote attackers to read sensitive files on the affected system via crafted file paths.
- **Affected Products:** SimpleHelp remote support software v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — Patch Tuesday - June 2026

**CVE:** `CVE-2026-33825` | `CVE-2026-45585` | `CVE-2026-45498` | `CVE-2026-41091` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.rapid7.com/blog/post/em-patch-tuesday-june-2026>

> Microsoft is publishing 200 vulnerabilities on June 2026 Patch Tuesday . Microsoft is not aware of exploitation in the wild for any of these vulnerabilities, and is aware of public disclosure for three. This is similar to last month’s Patch Tuesday, however several of last month’s vulnerabilities ended up on CISA KEV in the days following their publication. So far this month, Microsoft has provide…

**Parallel AI Enrichment:**

- **Technical Details:** Local elevation of privilege due to insufficient granularity of access control in Microsoft Defender. Exploit chains Defender update workflow, Volume Shadow Copy, Cloud Files API, opportunistic locks and symbolic links to access SAM and escalate to NT AUTHORITY\SYSTEM.
- **Affected Products:** Microsoft Defender (Defender Antimalware Platform — version 4.18.26050.3011)
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply Microsoft security update for CVE-2026-33825; restrict local logon rights; use application control to block execution from writable directories; monitor Defender service activity for anomalies.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33825

---

## 3. 🟠 Zero-Day — Microsoft’s June 2026 Patch Tuesday Addresses 198 CVEs ( CVE-2026-49160, CVE-2026-50507)

**CVE:** `CVE-2026-49160` | `CVE-2026-50507` | `CVE-2025-10263` | `CVE-2026-8863` &nbsp;|&nbsp; **Source:** Tenable Security Research &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.tenable.com/blog/microsofts-june-2026-patch-tuesday-addresses-198-cves-cve-2026-49160-cve-2026-50507>

> 32 Critical 166 Important 0 Moderate 0 Low Microsoft addresses 198 CVEs in the largest Patch Tuesday release, including three zero-days. Microsoft patched 198 CVEs in its June 2026 Patch Tuesday release, with 32 rated critical and 166 rated as important. Our counts omitted 6 CVEs that were already addressed by Microsoft via servicing and do not require additional customer action to resolve as well…

**Parallel AI Enrichment:**

- **Technical Details:** Denial-of-service vulnerability in HTTP.sys allowing specially crafted requests to crash or hang the HTTP server/stack, leading to service disruption
- **Affected Products:** Microsoft Windows HTTP.sys (Windows HTTP stack; affects systems using HTTP.sys)
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-49160
- **Active Exploitation:** true — https://krebsonsecurity.com/2026/06/a-record-breaking-patch-tuesday-for-june-2026/; https://www.tenable.com/blog/microsofts-june-2026-patch-tuesday-addresses-198-cves-cve-2026-49160-cve-2026-50507
- **Threat Actors:** None known
- **Mitigation:** Apply vendor patch immediately; if patching delayed, mitigate by restricting inbound HTTP(S) traffic (block unwanted sources at network edge), deploy WAF rules to drop malicious requests, and monitor HTTP.sys/service restarts
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-49160

---

## 4. 🟠 Zero-Day — Microsoft June 2026 Patch Tuesday fixes 3 zero-day, 200 flaws

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.bleepingcomputer.com/news/microsoft/microsoft-june-2026-patch-tuesday-fixes-3-zero-day-200-flaws/>

> Today is Microsoft&#x27;s June 2026 Patch Tuesday, with security updates for 200 flaws and three publicly disclosed zero-day vulnerabilities. [...]

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-45586 – improper link resolution before file access in Windows CTFMON (\"link following\") lets a locally authenticated attacker elevate to SYSTEM. CVE-2026-49160 – uncontrolled resource consumption in HTTP/2 header compression/flow‑control enables a remote denial‑of‑service (the \"HTTP/2 Bomb\"). CVE-2026-50507 – BitLocker protection can be bypassed by placing specially crafted files on USB/EFI and booting into WinRE, triggering a shell (YellowKey) that grants access to encrypted drives on TPM‑only configurations.
- **Affected Products:** Windows Collaborative Translation Framework (CTFMON) on supported Windows versions, Windows HTTP.sys (HTTP/2) on Windows clients and servers handling HTTP/2/HTTP/3, Windows BitLocker on affected Windows 11 and Windows Server 2022/2025 systems using TPM-only BitLocker
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply Microsoft patches immediately. For HTTP/2 Bomb use Microsoft’s MaxHeadersCount registry setting (see KB5102602). For BitLocker, enable TPM+PIN rather than TPM‑only until patched. No additional workaround for CTFMON beyond patching.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-45586, https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-49160, http://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-50507

---

## 5. 🟠 Zero-Day — CISA gives feds 3 days to patch Check Point VPN bug exploited as zero-day

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-check-point-flaw-exploited-by-ransomware-gangs/>

> CISA has ordered U.S. government agencies to secure their Check Point Remote Access VPN and Mobile Access deployments against a critical vulnerability exploited in zero-day attacks by Qilin ransomware affiliates. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Authentication-bypass logic-flow weakness in Remote Access and Mobile Access certificate validation when using deprecated IKEv1 key exchange; allows unauthenticated remote attackers to bypass user authentication and establish a remote access VPN connection without a valid user password.
- **Affected Products:** Check Point Mobile Access / SSL VPN, Remote Access VPN, Spark Firewalls – versions: R82.10 Jumbo Hotfix Take 19 or below; R82 Jumbo Hotfix Take 103 or below; R81.20 Jumbo Hotfix Take 141 or below; R81.10 (EOS); R81 (EOS); R80.40 (EOS); Spark: R80.20.X (EOS), R81.10.X, R82.00.X
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Qilin ransomware (Qilin RaaS affiliate) – one confirmed post-compromise case; broader actor infrastructure observed (Qilin affiliate)
- **Mitigation:** If unable to patch, remove support for legacy remote access clients; configure Remote Access VPN Authentication to IKEv2 only; set Machine Certificate Authentication to mandatory; enable IPS and download signatures; follow SmartConsole log hunts and IOCs provided by Check Point.
- **Vendor Advisory:** https://support.checkpoint.com/results/sk/sk185033

---

## 6. 🟠 Zero-Day — LiteLLM Flaw CVE-2026-42271 Exploited in the Wild, Chains to Unauthenticated RCE

**CVE:** `CVE-2026-42271` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://thehackernews.com/2026/06/litellm-flaw-cve-2026-42271-exploited.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Monday added a high-severity flaw impacting BerriAI LiteLLM to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

The vulnerability, tracked as CVE-2026-42271 (CVSS score: 8.7), is a command injection vulnerability that could allow any authenticated user to run arbitrary commands on the

**Parallel AI Enrichment:**

- **Technical Details:** Two MCP preview endpoints (POST /mcp-rest/test/connection and POST /mcp-rest/test/tools/list) accepted stdio configs (command, args, env) and spawned the supplied command as a subprocess on the proxy host; the endpoints required only a valid proxy API key and lacked role checks, allowing any authenticated user to execute arbitrary commands. When chained with CVE-2026-48710 (Starlette BadHost host‑header bypass), the attack can become unauthenticated remote code execution.
- **Affected Products:** LiteLLM (BerriAI) versions >= 1.74.2 and < 1.83.7
- **CVSS Score:** 8.7
- **CVSS Vector:** CVSS:4.0/AV:N/AC:L/AT:P/PR:L/UI:N/VC:H/VI:H/VA:H/SC:H/SI:N/SA:N
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Upgrade to LiteLLM v1.83.7 and Starlette ≥ 1.0.1. If patching is not possible, block the two POST /mcp‑rest/test endpoints at the perimeter, restrict network access to the proxy, rotate stored credentials, and monitor logs for host‑header anomalies and unexpected subprocess execution.
- **Vendor Advisory:** https://github.com/BerriAI/litellm/security/advisories/GHSA-v4p8-mg3p-g94g

---

## 7. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when untrusted external content retrieved by a system (e.g., web pages, scraped corpora, or retrieved documents in RAG) contains instructions crafted to influence a downstream LLM or agent. Attackers seed malicious prompts in external content; when the system retrieves that content and includes it in prompts or agent observations, the model follows the injected instructions, enabling data exfiltration, chain‑of‑command override, or other undesired behaviors. GeminiJack is a zero‑click instance where injected content caused Google Gemini Enterprise to act on malicious instructions without user interaction.
- **Affected Products:** Google Gemini Enterprise
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true – https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Blocklist or filter retrieval sources; validate and sanitize retrieved content before including in prompts; apply prompt compartmentalization and instruction‑hiding techniques; use strict provenance/trust scoring for retrieved documents; limit model capabilities for automatically‑executed actions; apply rate‑limiting and anomaly detection on agent actions. Follow vendor guidance in the Google Security Blog advisory.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 8. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack where adversarial instructions are injected into data sources or tools (emails, documents, web content, calendar invites, connectors) that an LLM‑powered system ingests while fulfilling a user’s request; these injected instructions can influence the model’s behavior (including exfiltration or action execution) without direct user input. GeminiJack was a zero‑click IPI chain targeting Gemini Enterprise via crafted email/invite/document content.
- **Affected Products:** Google Workspace (Workspace apps using Gemini / Gemini Enterprise integrations)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply Google Workspace mitigations and layered defenses: content sanitization and filtering, strict context/trust boundaries, provenance and source validation, least‑privilege agent permissions, rate limits and monitoring, disable or harden automation/agentic actions for untrusted inputs, apply vendor configuration guidance in blog advisory.
- **Vendor Advisory:** http://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections

---

## 9. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when untrusted web content manipulates an agentic model's prompts via intermediary content or UI flows, enabling zero‑click command execution; Noma Labs demonstrated an IPI that caused Gemini Enterprise to execute injected instructions without user interaction.
- **Affected Products:** Chrome (agentic browsing / Gemini integration), Google Gemini Enterprise
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Google recommended architectural guardrails for agentic browsing (sandboxing agentic actions, strict input/output validation, provenance tracking, user transparency and control), and rolled out new Chrome security layers for agentic features. Users should keep Chrome updated and disable agentic/AI features until patched.
- **Vendor Advisory:** http://blog.google/security/architecting-security-for-agentic

---

## 10. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow (bounds‑checking error) was discovered in CrabbyAVIF (an AVIF parser/decoder implemented in unsafe Rust) that could have led to remote code execution; the flaw was caught before a public release and tracked as CVE‑2025‑48530.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true (https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor patch linked above; audit and minimize unsafe Rust usage, add bounds checks, improve fuzzing and code review for unsafe blocks; ensure up-to-date Android security patch level.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 11. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 12. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

---

## 13. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 14. 🟠 Zero-Day — Microsoft Defender 'RoguePlanet' zero-day grants SYSTEM privileges

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.bleepingcomputer.com/news/microsoft/microsoft-defender-rogueplanet-zero-day-grants-system-privileges/>

> [...]

---

## 15. 🟠 Zero-Day — SymfonyRuntime CVE-2024-50340 Patch Bypass: Web Requests Can Still Set APP_ENV/APP_DEBUG via parse_str/SAPI Argv Mismatch

**CVE:** `CVE-2026-47767` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://github.com/advisories/GHSA-fqc7-9xjw-jrh3>

> ### Description

CVE-2024-50340 (GHSA-x8vp-gf4q-mw5j) addressed an issue where, with `register_argc_argv=On`, a crafted query string let an unauthenticated GET change the kernel environment and debug flag by feeding `--env`/`--no-debug` through `$_SERVER[&#x27;argv&#x27;]`. The fix shipped in `symfony/runtime` 5.4.46 / 6.4.14 / 7.1.7 gated the argv read on `empty($_GET)` as a proxy for &quot;is th…

---

## 16. 🟠 Zero-Day — Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now

**CVE:** `CVE-2026-11645` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://thehackernews.com/2026/06/chrome-v8-zero-day-cve-2026-11645.html>

> Google has released security updates to address 74 vulnerabilities, including one that has come under active exploitation in the wild.

The high-severity vulnerability, tracked as CVE-2026-11645 (CVSS score: 8.8), has been described as an out-of-bounds memory access in V8, Chrome&#x27;s JavaScript and WebAssembly engine.

&quot;Out-of-bounds read and write in V8 in Google Chrome prior to 149.0.782…

---

## 17. 🟠 Zero-Day — Check Point VPN Zero-Day Exploited in Qilin Ransomware Attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.securityweek.com/check-point-vpn-zero-day-exploited-in-qilin-ransomware-attacks/>

> The authentication bypass vulnerability allows attackers to establish VPN connections without a valid password. The post Check Point VPN Zero-Day Exploited in Qilin Ransomware Attacks appeared first on SecurityWeek .

---

## 18. 🟠 Zero-Day — Google patches new Chrome zero-day flaw exploited in the wild

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.bleepingcomputer.com/news/security/google-patches-fifth-chrome-zero-day-bug-exploited-in-attacks-this-year/>

> Google has released emergency updates to patch another Chrome zero-day vulnerability that has been exploited in the wild, the fifth such flaw patched since the start of the year. [...]

---

## 19. 🟡 High Severity — Pheditor: OS Command Injection in terminal handler via unsanitized 'dir' parameter

**CVE:** `CVE-2026-48030` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://github.com/advisories/GHSA-jvc5-6g7q-c843>

> ### Summary

An OS Command Injection vulnerability in the terminal action handler allows any authenticated user to execute arbitrary OS commands by injecting shell metacharacters into the &#x27;dir&#x27; POST parameter, completely bypassing the TERMINAL_COMMANDS whitelist and achieving full Remote Code Execution with web server privileges.

### Details

The terminal handler in pheditor.php accepts…

---

## 20. 🟡 High Severity — PhoenixStorybook: Unauthenticated remote code execution via HEEx template injection in phoenix_storybook playground

**CVE:** `CVE-2026-8467` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://github.com/advisories/GHSA-55hg-8qxv-qj4p>

> ### Summary
An unsafe HEEx template generation vulnerability allows any unauthenticated user to execute arbitrary code on the server. The phoenix_storybook playground accepts user-controlled attribute values over WebSocket and interpolates them unsanitized into a HEEx template that is subsequently compiled and evaluated with full Elixir `Kernel` access.

### Details
The vulnerability is a three-st…

---

## 21. 🟡 High Severity — Veeam Backup & Replication RCE Flaw Lets Domain Users Run Remote Code

**CVE:** `CVE-2026-44963` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://thehackernews.com/2026/06/veeam-backup-replication-rce-flaw-lets.html>

> Veeam has released security patches to address a critical flaw in its Backup &amp; Replication software that could result in remote code execution.

Tracked as CVE-2026-44963, the vulnerability carries a CVSS score of 9.4 out of a maximum of 10.0.

&quot;A vulnerability allowing remote code execution (RCE) on the Backup Server by an authenticated domain user,&quot; Veeam said in a Tuesday advisory…

---

## 22. 🟡 High Severity — SEC Consult SA-20260608-0 :: Privilege Escalation via Binary Planting in Genetec-provided RabbitMQ in multiple Genetec products

**CVE:** `CVE-2026-25112` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://seclists.org/fulldisclosure/2026/Jun/2>

> Posted by SEC Consult Vulnerability Lab via Fulldisclosure on Jun 08 SEC Consult Vulnerability Lab Security Advisory &lt; 20260608-0 &gt; ======================================================================= title: Privilege Escalation via Binary Planting product: Genetec-provided RabbitMQ in multiple Genetec products vulnerable version: Multiple products, see below. fixed version: Multiple prod…

---

## 23. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
