# Zero Day Pulse

> **Generated:** 2026-06-15 02:34 UTC &nbsp;|&nbsp; **Total:** 11 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path traversal vulnerability in SimpleHelp RMM that enables unauthenticated remote attackers to read sensitive files such as logs, configuration files, and credentials.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability)
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors
- **Mitigation:** Apply the official SimpleHelp patch and upgrade to a version newer than 5.5.7.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an AI agent retrieves external content (webpages, emails, invites, documents) containing attacker‑controlled instructions that the agent treats as part of its prompt/context and then follows, enabling actions or data exfiltration. GeminiJack was a zero‑click IPI‑style exploit against Google Gemini Enterprise where crafted external content induced the model to exfiltrate corporate data.
- **Affected Products:** Google Gemini Enterprise (GeminiJack zero‑click IPI); other AI agents and RAG/agentic systems (general vector)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply vendor patches/updates; restrict or sanitize retrieved external content (strip/ignore instructional text in retrievals); use robust retrieval filtering and provenance checks; apply allowlist/blocklist and content classification before feeding to the model; agent-level policy enforcement and output filtering; least‑privilege access for agents and telemetry/monitoring of agent queries for anomalous behavior.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) embeds malicious instructions within external data sources or tools (e.g., web content, documents, connectors) that complex LLM‑based systems like Workspace with Gemini ingest during query handling; these instructions can influence model behavior, potentially without any explicit user input (zero‑click) as demonstrated by GeminiJack.
- **Affected Products:** Google Workspace with Gemini integrations
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability
- **Patch Available:** true — http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Layered defenses — content filtering, sanitization of external sources, limiting model access to untrusted connectors, robust prompt engineering, monitoring and anomaly detection, vendor‑provided continuous mitigations in Workspace (see vendor advisory).
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The primary mechanism is indirect prompt injection where malicious site content influences the AI agent’s prompt/decision pipeline, allowing unauthorized actions or data extraction when chained with other flaws such as a zero‑click vulnerability (GeminiJack).
- **Affected Products:** Google Chrome (agentic browsing features), Google Gemini Enterprise, Google Vertex AI Search
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/
- **Patch Available:** true — http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply the latest Google Chrome and Gemini updates, configure the browser to restrict agentic browsing origins, enable layered defenses and runtime checks that validate AI‑generated actions, and disable agentic browsing features for untrusted sites.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Near‑miss linear buffer overflow in the CrabbyAVIF Rust library (CVE‑2025‑48530). The overflow would have corrupted memory, but Android’s Scudo allocator placed guard pages that caused a crash, rendering the issue non‑exploitable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use Android’s Scudo hardened allocator (guard pages) and tightened crash reporting; expand unsafe‑Rust review practices and developer training.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) embeds malicious instructions inside external data sources (emails, documents, calendar invites, web content) that are retrieved by AI agents; when retrieved into the agent’s context, these instructions can overwrite expected prompts or chain‑of‑thought, leading to data exfiltration or unauthorized actions. Attack success relies on retrieval into the model context and absence of robust filtering/provenance controls.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses — input validation/sanitization, strict retrieval filtering, provenance checks, prompt sanitization, least‑privilege access for agents, human‑in‑the‑loop for sensitive actions, monitoring and anomaly detection, regular model and retrieval source audits.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors target and modify routers to maintain persistent, long-term access, leveraging compromised devices and trusted connections to pivot across networks and target backbone, PE, and CE routers.
- **Affected Products:** Major telecommunications backbone routers, provider edge (PE) routers, customer edge (CE) routers, compromised routers and IoT devices
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Network segmentation; isolate and inventory routers and network devices; apply network monitoring/logging; rotate credentials and keys; disable unused management interfaces; implement multi-factor authentication; restrict administrative access to management interfaces; update device firmware per vendor advisories; apply recommended mitigations in CISA advisory
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** The campaign leverages spearphishing emails to obtain credentials and deliver malware, then exploits known CVEs in WinRAR (CVE-2023-38831), Microsoft Outlook (CVE-2023-23397), and Roundcube Webmail (CVE-2020-12641, CVE-2020-35730). Additional tactics include credential stuffing, exploitation of vulnerable SOHO devices for proxying, and use of legitimate binaries (e.g., OpenSSH, PowerShell) for persistence and data exfiltration.
- **Affected Products:** WinRAR (CVE-2023-38831), Microsoft Outlook (CVE-2023-23397), Roundcube Webmail (CVE-2020-12641, CVE-2020-35730), multiple SOHO device models (brands/models not exhaustively listed)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** GRU Unit 26165 (tracked as APT28/Fancy Bear, Forest Blizzard, Blue Delta)
- **Mitigation:** Apply vendor patches and firmware updates to all affected software and devices; replace end‑of‑life SOHO hardware; enable authentication for remote services (e.g., RTSP on cameras); deploy and prioritize endpoint detection and response (EDR); enable Windows attack surface reduction rules; monitor and collect Windows logs; audit accounts and enforce least‑privilege; implement threat‑hunting and detection rules (YARA/IDS) based on provided IOCs; restrict execution of files from email attachments and links; rotate and harden credentials; monitor remote authentication activity.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-45586: Local privilege escalation via a vulnerability in the Windows subsystem; CVE-2026-50507: BitLocker protection mechanism failure allowing physical‑access bypass; CVE-2026-49160: Uncontrolled resource consumption in Windows HTTP/2 implementation leading to denial‑of‑service.
- **Affected Products:** Windows (privilege escalation) – CVE-2026-45586; Windows BitLocker – CVE-2026-50507; Windows HTTP/2 implementation – CVE-2026-49160
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true – https://msrc.microsoft.com/update-guide
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Apply the Microsoft June 2026 security updates; restrict physical access to devices to mitigate BitLocker bypass; rate‑limit or filter HTTP/2 traffic; employ standard endpoint protection and network‑based mitigations until patches are applied.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide

---

## 10. 🟠 Zero-Day — When a Government Pulls an AI Model: What the Fable 5 and Mythos 5 Suspension Means for Security Teams

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Snyk Vulnerability Research &nbsp;|&nbsp; **Published:** 2026-06-14
**Reference:** <https://snyk.io/blog/fable-mythos-suspension-security-takeaways/>

> On June 12, 2026, a US export-control directive led Anthropic to disable Claude Fable 5 and Mythos 5 worldwide over a reported jailbreak. The reported trigger was a code-analysis capability that defenders use routinely. Here is what happened, how the security community read it, and what security teams can take from it.

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability was a prompt/code‑analysis jailbreak that let an attacker craft inputs causing the model to reveal or analyze code in ways that could expose software vulnerabilities, effectively bypassing built‑in safety controls.
- **Affected Products:** Claude Fable 5, Claude Mythos 5
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Disable access to the impacted models; restrict model usage to vetted partners and trusted‑access programs; employ network and output filtering, strict access controls, and defensive prompt handling; continuously monitor vendor advisories for fixes.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
