# Zero Day Pulse

> **Generated:** 2026-05-24 19:00 UTC &nbsp;|&nbsp; **Total:** 10 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 8 &nbsp;|&nbsp; 🟡 High: 2 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** An unauthenticated path traversal vulnerability in SimpleHelp web endpoints allows remote attackers to retrieve sensitive files (logs, configuration files, credentials) from the server, enabling further compromise.
- **Affected Products:** SimpleHelp Remote Support / RMM server versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N
- **Exploit Available:** true — https://medium.com/%40RosanaFS/simplehelp-cve-2024-57727-tryhackme-walkthrough-9f88c2061fb9
- **Patch Available:** true — https://simple-help.com/release-news
- **Active Exploitation:** true — https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a
- **Threat Actors:** Ransomware actors (including groups reported by CISA and SecurityWeek)
- **Mitigation:** Apply vendor update to SimpleHelp 5.5.8 (or later) immediately; isolate or take unpatched SimpleHelp servers offline; rotate credentials exposed to SimpleHelp; monitor for indicators of compromise per CISA advisory; restrict network access to SimpleHelp management interfaces.
- **Vendor Advisory:** https://simple-help.com/release-news

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is a class of attacks where adversaries seed malicious instructions into web content or other data sources that LLM‑powered agents consume; when the agent ingests that content during browsing or retrieval, the malicious instructions can influence the agent's behavior (e.g., cause data exfiltration, execute unintended actions, or bypass safeguards). Attack vectors include hidden site code, specially crafted payloads in public web pages, and chaining IPI with sandbox breakout or remote‑tunneling vulnerabilities to escalate impact.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Use strict content sanitization and browsing restrictions for AI agents; monitor for seeded prompt injection on public websites; apply input/output filtering and software sandboxing; restrict external web browsing by AI agents and use allowlists.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack technique where an adversary injects malicious instructions into data sources or tools that a large language model (LLM) uses during completion (for example, web content or third‑party documents available to Workspace with Gemini). Attackers can influence agentic or multi‑source LLM behavior without direct user input by embedding instructions in those sources; defenses focus on layered mitigations including input provenance, sanitization, strict tool‑usage policies, and model‑side instruction filtering.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false.
- **Patch Available:** false.
- **Active Exploitation:** false.
- **Threat Actors:** None known.
- **Mitigation:** Mitigations include layered defenses: treat external content as untrusted, provenance and source validation, content sanitization and canonicalization, model instruction filtering, restrictive tool access policies, rate‑limiting and monitoring, user confirmations for high‑risk actions, and continuous monitoring and red‑teaming to discover new payloads.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is the primary threat; it can appear in malicious sites, third‑party iframe content, or user‑generated content and can cause the agent to take unwanted actions (e.g., financial transactions or data exfiltration).
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use Chrome’s built‑in layered defenses (User Alignment Critic, Agent Origin Sets/origin gating, prompt‑injection classifier, user confirmations, Safe Browsing, on‑device scam detection); apply Chrome updates when released; follow Google guidance in the vendor advisory; restrict use of agentic browsers for sensitive tasks until organizational risk assessment is complete.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A near‑miss linear buffer overflow in the Rust CrabbyAVIF image library (CVE‑2025‑48530) was discovered and fixed pre‑release; Android’s Scudo hardened allocator turned the overflow into a noisy crash, rendering it non‑exploitable and aiding detection.
- **Affected Products:** CrabbyAVIF (Android external/rust/crabbyavif)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — patch: https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050 and advisory: https://source.android.com/docs/security/bulletin/2025-08-01
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use Scudo hardened allocator (guard pages); enforce Scudo where possible; review and limit unsafe{} usage, introduce unsafe Rust review training and tighter unsafe-code practices.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection embeds malicious instructions in external data sources (e.g., emails, documents, calendar invites) that an LLM may retrieve and execute. Google mitigates by training models with adversarial data, deploying classifiers to detect malicious instructions at retrieval/input time, sanitizing/render‑blocking external content (images, URLs), and requiring user confirmation for risky actions.
- **Affected Products:** Google Gemini (Gemini 2.5; Gemini in Google Workspace and the Gemini app)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: Gemini 2.5 model hardening (adversarial training), prompt‑injection content classifiers, security thought reinforcement, markdown sanitization with suspicious‑URL redaction, user‑confirmation (Human‑In‑The‑Loop) framework, end‑user security notifications and Help Center guidance.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state‑sponsored actors target and gain persistent access to large backbone, provider edge (PE), and customer edge (CE) routers, leveraging compromised devices and trusted connections to pivot into other networks; they often modify routers to maintain long‑term persistence and enable espionage.
- **Affected Products:** Major telecommunications backbone routers, provider edge (PE) routers, customer edge (CE) routers, and other compromised network devices (specific vendors/versions unavailable)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon; OPERATOR PANDA; RedMike; UNC5807; GhostEmperor
- **Mitigation:** Isolate and harden router management interfaces; apply vendor mitigations/patches if available; enforce multi-factor authentication for administrative access; restrict and monitor trusted connections (BGP, management VLANs); implement network segmentation and egress filtering; deploy enhanced logging and network telemetry to detect anomalous configuration changes and persistence mechanisms.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** GRU unit 26165 employed spear‑phishing with malicious attachments/links, credential‑stuffing/password‑sprays, and exploited public‑facing application vulnerabilities such as Outlook NTLM (CVE‑2023‑23397), WinRAR (CVE‑2023‑38831), and multiple Roundcube CVEs to execute arbitrary code and access email accounts. They also leveraged compromised SOHO devices and IP cameras for reconnaissance, used mailbox permission modifications for email collection, and moved laterally via Impacket/PsExec/RDP, harvesting AD credentials.
- **Affected Products:** Roundcube (versions before 1.2.13, 1.3.x before 1.3.16, 1.4.x before 1.4.10), WinRAR (CVE-2023-38831), Microsoft Outlook (CVE-2023-23397)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** APT28 / Fancy Bear / GRU unit 26165 (also tracked as Forest Blizzard, Blue Delta)
- **Mitigation:** Collect and monitor Windows logs; enable Windows attack surface reduction rules; apply software/firmware updates; audit and secure IP camera accounts; implement network segmentation; disable UPnP/P2P on devices; use VPNs for remote access; monitor for mailbox permission changes and anomalous MFA enrollment.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟡 High Severity — Ghost CMS SQL injection flaw exploited in large-scale ClickFix campaign

**CVE:** `CVE-2026-26980` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-05-24
**Reference:** <https://www.bleepingcomputer.com/news/security/ghost-cms-sql-injection-flaw-exploited-in-large-scale-clickfix-campaign/>

> A large-scale campaign is exploiting a critical SQL injection vulnerability (CVE-2026-26980) in Ghost CMS to inject malicious JavaScript code that triggers ClickFix attack flows. [...]

**Parallel AI Enrichment:**

- **Technical Details:** An unauthenticated blind SQL injection in Ghost's Content API permits attackers to inject SQL payloads that enumerate and extract database contents; the extracted data is then used to inject malicious JavaScript into served pages, enabling ClickFix redirect and credential‑harvest flows.
- **Affected Products:** Ghost CMS Content API versions v3.24.0, v3.25.0, v3.26.0, v4.0.0, v5.0.0, v6.0.0, v6.19.0
- **CVSS Score:** 9.4
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Upgrade Ghost to the patched release immediately; block or isolate vulnerable Content API endpoints, implement Web Application Firewall rules to detect and block SQLi payloads, and audit/restore any injected JavaScript on affected sites.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 10. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

**Parallel AI Enrichment:**

- **Technical Details:** A malicious DNS response can trigger a number of out-of-bounds (OOB) reads, writes, and other memory issues in the DNS parser implemented in modem firmware; this is a memory-safety parsing vulnerability (CWE-787).
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** true — vendor bulletin: https://source.android.com/security/bulletin/pixel/2024-03-01 and Google Security Blog post: http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Google mitigated the DNS parsing risk by integrating a memory‑safe Rust DNS parser into Pixel modem firmware.
- **Vendor Advisory:** https://source.android.com/security/bulletin/pixel/2024-03-01

---
