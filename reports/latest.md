# Zero Day Pulse

> **Generated:** 2026-05-25 09:47 UTC &nbsp;|&nbsp; **Total:** 10 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 8 &nbsp;|&nbsp; 🟡 High: 2 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** An unauthenticated attacker can exploit a path traversal vulnerability in SimpleHelp Remote Monitoring and Management (versions ≤5.5.7) to read arbitrary files on the server, including logs, configuration files, and credentials.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) versions 5.5.7 and earlier
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2024/CVE-2024-57727.yaml)
- **Patch Available:** true (https://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570)
- **Active Exploitation:** true (https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a)
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Upgrade to SimpleHelp 5.5.8 or later; restrict network exposure of the RMM interface; apply firewall rules and credential rotation.
- **Vendor Advisory:** https://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) involves placing malicious prompt text in website content (e.g., hidden HTML, scripts) that is later read and processed by AI agents that browse or scrape the page, leading the AI to execute attacker‑controlled commands.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack technique where an adversary injects malicious instructions into data or tools consumed by an LLM‑powered application (e.g., web content, attachments, integrated tools) to influence the model's behavior when processing a user's query; this can occur without direct user input and leverages model‑context ingestion and agentic automation to escalate impact.
- **Affected Products:** Google Workspace with Gemini integrations
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Layered defenses described by Google: content filtering and classification, provenance and source controls, model behavior constraints, least‑privilege and scope‑limited tool access, monitoring and detection for IPI patterns, and continuous updates to detectors and training; implement workspace hardening, limit agentic capabilities, validate external data before use, and monitor for anomalous outputs.
- **Vendor Advisory:** http://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection in agentic browsing occurs when malicious page content, third‑party iframes, or user‑generated content influence the agent’s planner to execute unintended actions such as initiating financial transactions or exfiltrating data. Chrome mitigates this with a User Alignment Critic (a separate vetting model), Agent Origin Sets for read‑only/write gating, deterministic checks for model‑generated URLs, prompt‑injection classifiers, user confirmations for sensitive actions, and continuous red‑teaming and monitoring.
- **Affected Products:** Chrome (agentic/Gemini integration in Chrome)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — https://blog.google/security/architecting-security-for-agentic/
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use Chrome’s layered defenses (User Alignment Critic, origin gating/Agent Origin Sets, prompt‑injection detection, user confirmations for sensitive actions), keep Chrome auto‑updated, and follow Google’s VRP guidance to report issues.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injections embed hidden malicious instructions in external data sources (emails, documents, calendar invites) that LLMs may follow; Google mitigates via model hardening (adversarial training), prompt‑injection classifiers, security thought reinforcement, markdown sanitization, suspicious‑URL redaction, user‑confirmation framework, and end‑user notifications.
- **Affected Products:** Gemini (Google Workspace, Gemini app)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — https://blog.google/security/mitigating-prompt-injection-attacks/
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Use Google’s built‑in layered defenses (prompt‑injection classifiers, security thought reinforcement, markdown sanitization and URL redaction, user‑confirmation framework, end‑user notifications) and follow Google Help Center guidance for additional hardening steps.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** The actors modify router configurations to enable lateral movement and use virtualized containers on network devices to evade detection, leveraging publicly known CVEs such as CVE‑2023‑20198 and CVE‑2018‑0171 to gain unauthorized access.
- **Affected Products:** Cisco IOS XE, Cisco IOS, Ivanti Connect Secure, Ivanti Policy
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Disable outbound connections from management interfaces; Disable all unused ports and protocols; Change all default administrative credentials; Require public‑key authentication for administrative roles.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** The advisory describes a sustained GRU cyber‑espionage campaign (since 2022) targeting logistics and technology organizations, using intrusions, credential theft, lateral movement, and targeting of IT/OT systems supporting logistics and delivery chains.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th GTsSS, military unit 26165 (also tracked as APT28 and related GRU personas).
- **Mitigation:** Follow the joint CSA recommendations: implement network segmentation, multi‑factor authentication, enhanced logging and monitoring, timely credential and access reviews, apply vendor patches where available, restrict administrative access, and follow incident response procedures.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟡 High Severity — Ghost CMS SQL injection flaw exploited in large-scale ClickFix campaign

**CVE:** `CVE-2026-26980` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-05-24
**Reference:** <https://www.bleepingcomputer.com/news/security/ghost-cms-sql-injection-flaw-exploited-in-large-scale-clickfix-campaign/>

> A large-scale campaign is exploiting a critical SQL injection vulnerability (CVE-2026-26980) in Ghost CMS to inject malicious JavaScript code that triggers ClickFix attack flows. [...]

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is an unauthenticated blind SQL injection in Ghost CMS Content API (versions 3.24.0‑6.19.0) that allows attackers to inject malicious SQL payloads, read arbitrary data from the database, and obtain sensitive information such as admin API keys.
- **Affected Products:** Ghost CMS versions 3.24.0 through 6.19.0
- **CVSS Score:** 9.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (https://github.com/vognik/CVE-2026-26980)
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 10. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

**Parallel AI Enrichment:**

- **Technical Details:** A malicious DNS response can trigger out‑of‑bounds reads, writes, and other memory issues in the modem firmware's DNS parser. The issue is mitigated by implementing the DNS parser in Rust, eliminating memory‑unsafe code paths.
- **Affected Products:** Google Pixel 9, Google Pixel 10 (modem firmware)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Install the Google Pixel security update (2024‑03‑05 patch level or later). Ensure devices receive regular OTA updates that incorporate the Rust DNS parser mitigation.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/pixel/2024-03-01

---
