# Zero Day Pulse

> **Generated:** 2026-06-23 02:01 UTC &nbsp;|&nbsp; **Total:** 11 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal vulnerability in SimpleHelp 5.5.7 and earlier allows unauthenticated attackers to craft requests that traverse directories and read arbitrary files on the server, exposing sensitive configuration and credential files.
- **Affected Products:** SimpleHelp Remote Support / RMM – version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Public proof‑of‑concept and technical write‑up are available at https://www.offsec.com/blog/cve-2024-57727/
- **Patch Available:** Vendor patches are available via the SimpleHelp security advisory (https://guides.simple-help.com/kb---security-vulnerabilities-01-2025) and Broadcom protection bulletin (https://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability).
- **Active Exploitation:** Confirmed active exploitation reported by CISA (AA25‑163A) indicating ransomware actors are using CVE‑2024‑57727 against unpatched SimpleHelp instances.
- **Threat Actors:** Ransomware actors (unspecified groups)
- **Mitigation:** Isolate or take affected SimpleHelp instances offline, apply the vendor’s patch/upgrade to a version newer than 5.5.7, restrict network exposure with firewalls or allow‑lists, and rotate any credentials or keys that may have been exposed.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when web content or other external data sources include embedded instructions or adversarial payloads that are read by an AI agent or LLM‑based workflow and cause the model to follow attacker‑supplied instructions (e.g., hidden HTML, crafted webpage text, or tool outputs). Attack chains can include seeding payloads on public pages, hidden/injected code, or chaining IPI with other vulnerabilities to exfiltrate data or execute commands.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit unavailable
- **Patch Available:** Patch unavailable
- **Active Exploitation:** Yes – Google reports multiple IPI payloads observed on the public web and increased detections, and Forcepoint disclosed 10 in‑the‑wild payloads.
- **Threat Actors:** None known
- **Mitigation:** Key mitigations per Google and community guidance: input/output validation and sanitization, avoid automatic execution of untrusted web content, implement human oversight and confirmation for high‑risk actions, restrict models' access to arbitrary web content, use strict parsing and whitelisting for external data, and monitor for known IPI patterns. Forcepoint/Google recommend sweeps of web content and defensive detection for IPI payload signatures.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when malicious instructions are embedded within data sources or tools the LLM consumes (e.g., documents, web pages, emails) and the model follows those instructions during completion—potentially even without direct user input. Attackers can influence agentic automation by injecting prompts into integrated data or tooling.
- **Affected Products:** Google Workspace (Gemini integrations and agentic features)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC or weaponized exploit disclosed in vendor advisory; none known.
- **Patch Available:** No vendor patch; this is a threat‑mitigation guidance blog rather than a patchable software vulnerability.
- **Active Exploitation:** No confirmed active exploitation reported in the advisory; Google reported monitoring public web and increased attempts but did not confirm active exploitation in enterprise customers.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses and hardening recommended by Google including input/output validation and sanitization, restricting agentic automation, limiting external untrusted sources, monitoring for IPI patterns, human oversight and controls, and continuous web sweeps for known IPI patterns.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is an indirect prompt injection issue where malicious web content can inject prompts that influence the behavior of agentic browsing or Gemini services. When combined with a secondary flaw (CVE‑2025‑54131), an attacker can trigger arbitrary actions. GeminiJack specifically exploits this injection path in Google Gemini Enterprise / Vertex AI Search.
- **Affected Products:** Google Gemini Enterprise / Vertex AI Search (versions prior to 1.3)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept or weaponised exploit is known.
- **Patch Available:** Patch available in version 1.3 of Google Gemini Enterprise / Vertex AI Search; see advisory at https://blog.google/security/architecting-security-for-agentic/
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Apply the update to version 1.3 of Google Gemini Enterprise / Vertex AI Search. Additionally, keep Chrome and any agentic browsing features up‑to‑date and follow Google’s security recommendations.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is an elevation‑of‑privilege flaw in the Android Framework (CVE‑2025‑48595). Google’s Rust adoption aims to reduce memory‑safety bugs, but detailed technical exploit vectors for this CVE are not publicly described.
- **Affected Products:** Android Framework components across Android platform (affected by CVE-2025-48595)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC found in referenced advisories; weaponized exploit not publicly disclosed.
- **Patch Available:** https://source.android.com/docs/security/bulletin/2026/2026-06-01
- **Active Exploitation:** Confirmed limited/targeted active exploitation reported by Google/Android Security Bulletin for CVE-2025-48595 (June 2026 bulletin).
- **Threat Actors:** None known
- **Mitigation:** Apply the June 2026 Android security updates from device vendors immediately. If an update is unavailable, restrict installation of untrusted apps, enable Google Play Protect, avoid sideloading, and limit device privileges.
- **Vendor Advisory:** https://blog.google/security/rust-in-android-move-fast-fix-things/

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injections are hidden malicious instructions embedded in external data sources (emails, documents, calendar invites) that aim to manipulate the LLM to exfiltrate data or execute rogue actions.
- **Affected Products:** Gemini 2.5; Gemini in Google Workspace; Gemini app
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit is referenced.
- **Patch Available:** No vendor patch is provided; mitigation details are described in the same blog post.
- **Active Exploitation:** No confirmed active exploitation in the wild has been reported.
- **Threat Actors:** None known
- **Mitigation:** Model hardening (Gemini 2.5), adversarial‑training detectors, security thought reinforcement, markdown sanitization, suspicious URL redaction via Google Safe Browsing, confirmation dialogs for sensitive actions, and end‑user security notifications with help‑center links.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors target large backbone routers and PE/CE routers, modify routers for persistent long‑term access, leverage compromised devices and trusted connections to pivot into other networks and expand access for espionage.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unavailable.
- **Patch Available:** No single vendor patch is provided in the advisory; vendors may publish product-specific fixes — see vendor advisories. (No universal patch URL available.)
- **Active Exploitation:** Yes — CISA reports confirmed activity targeting networks worldwide and specifically calls out compromise of telecommunications backbone and PE/CE routers.
- **Threat Actors:** Salt Typhoon; OPERATOR PANDA; RedMike; UNC5807; GhostEmperor
- **Mitigation:** CISA recommends hardening and monitoring of backbone, provider edge (PE) and customer edge (CE) routers; restricting administrative access; rotating credentials and keys; network segmentation; logging and telemetry collection; threat hunting for persistent router modifications and lateral pivoting; apply vendor patches where available; apply vendor‑specific mitigations.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** The campaign uses spearphishing for credential harvesting, exploits public CVEs (WinRAR CVE-2023-38831, Outlook CVE-2023-23397, Roundcube CVEs) to gain initial foothold, abuses SOHO devices for proxying, leverages tools like Impacket, Certipy, ADExplorer for lateral movement and data exfiltration, manipulates mailbox permissions for email collection, and deletes logs via utilities such as wevtutil.
- **Affected Products:** WinRAR (CVE-2023-38831), Microsoft Outlook (CVE-2023-23397), Roundcube Webmail (CVE-2020-12641, CVE-2020-35730, CVE-2021-44026), various SOHO device firmware
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoCs exist for CVE-2023-38831 and CVE-2023-23397, but no direct exploit URLs are cited.
- **Patch Available:** Patch information is provided per‑CVE (e.g., Microsoft guidance, WinRAR updates) rather than a single advisory patch URL.
- **Active Exploitation:** Yes – the advisory documents confirmed active exploitation in the wild by GRU unit 26165.
- **Threat Actors:** GRU unit 26165 (APT28 / Fancy Bear / Forest Blizzard / Blue Delta)
- **Mitigation:** Network segmentation; restrict remote access; enable authenticated RTSP for cameras; audit and monitor authentication activity; apply vendor patches for referenced CVEs; harden email infrastructure; disable legacy protocols; monitor use of native utilities (ntdsutil, wevtutil, vssadmin, schtasks); follow CISA/NSA/FBI reporting guidance.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

**Parallel AI Enrichment:**

- **Technical Details:** Authentication bypass in Check Point Remote Access VPN IKEv1 implementation allowing unauthenticated remote attackers to bypass password-based authentication.
- **Affected Products:** Check Point Remote Access VPN (IKEv1)
- **CVSS Score:** 9.3
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or exploit is known.
- **Patch Available:** Hotfixes and mitigation guidance are available via the Check Point advisory page.
- **Active Exploitation:** Confirmed active exploitation in the wild, reported by vendor and security reports.
- **Threat Actors:** Qilin ransomware affiliate; other targeted attackers
- **Mitigation:** Apply the vendor hotfix/patch and follow the mitigation/workarounds detailed in the Check Point advisory.
- **Vendor Advisory:** https://support.checkpoint.com/results/sk/sk185033

---

## 10. 🟠 Zero-Day — What the Latest ShinyHunters Breaches Reveal About Modern Cyberattacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://www.securityweek.com/what-the-latest-shinyhunters-breaches-reveal-about-modern-cyberattacks/>

> Groups like ShinyHunters are demonstrating that attackers do not necessarily need malware or zero-day exploits to cause massive damage. The post What the Latest ShinyHunters Breaches Reveal About Modern Cyberattacks appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Not a software vulnerability — campaign leverages credential stuffing, scraping, and data aggregation to exfiltrate and publish stolen data; no CVE/CVSS applies.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** None known (no public PoC; attacks rely on data theft, credential stuffing, scraping rather than exploit code).
- **Patch Available:** Patch not applicable / unavailable (this is a data‑breach/exfiltration campaign, not a single software vulnerability).
- **Active Exploitation:** Confirmed — multiple breaches and data dumps by ShinyHunters as described in the article.
- **Threat Actors:** ShinyHunters (and similar data‑broker groups)
- **Mitigation:** Hardening and operational mitigations: enforce MFA, rotate/segregate credentials, monitor for credential stuffing and leaked data, tighten access controls and logging, apply least privilege, and notify affected users.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
