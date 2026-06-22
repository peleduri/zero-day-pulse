# Zero Day Pulse

> **Generated:** 2026-06-22 11:31 UTC &nbsp;|&nbsp; **Total:** 11 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path traversal vulnerability in SimpleHelp v5.5.7 and earlier that permits unauthenticated attackers to read sensitive files on the server by supplying crafted path inputs to vulnerable endpoints.
- **Affected Products:** SimpleHelp Remote Support / RMM — versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (unspecified groups)
- **Mitigation:** Apply the vendor‑supplied patches/upgrade SimpleHelp to a patched release; if immediate patching is unavailable, restrict access to the SimpleHelp management interface with firewall rules or VPN‑only access, disable any public‑facing instances, rotate credentials/keys, audit logs, and monitor for indicators of compromise per CISA guidance.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) – adversary places malicious instructions in web content or retrieval sources which AI agents retrieve and incorporate into their prompt context, causing unintended behavior (e.g., data exfiltration, command execution). GeminiJack is a zero‑click IPI demonstrated against Google Gemini Enterprise using hidden/indirect instructions.
- **Affected Products:** Google Gemini Enterprise (GeminiJack), Microsoft Copilot Studio (ShareLeak/CVE-2026-21520), AI agents that browse web content
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Block or sanitize untrusted retrieval sources, implement strict retrieval filters, canonicalization and content whitelisting, model‑level instruction hardening (ignore externally retrieved instructions), telemetry and detection for anomalous retrievals, apply vendor guidance.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) allows an attacker to influence an LLM’s output by inserting malicious instructions into the data sources or tools the model consumes, causing the model to act on the injected payload without direct user input.
- **Affected Products:** Google Workspace (Gemini)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability)
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** GeminiJack is an indirect prompt injection vulnerability in Google Gemini Enterprise that can be combined with other steps to gain unauthorized local file access and invade user privacy. In Chrome's Gemini feature, the flaw (CVE‑2026‑0628) allows similar file‑access behavior.
- **Affected Products:** Google Chrome (including Gemini agentic capabilities), Google Gemini Enterprise
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (patched, see http://unit42.paloaltonetworks.com/gemini-live-in-chrome-hijacking)
- **Active Exploitation:** false
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow in the unsafe‑Rust CrabbyAVIF AVIF parser/decoder (CVE‑2025‑48530) could have allowed remote code execution; Scudo hardened allocator rendered it non‑exploitable and the flaw was fixed pre‑release.
- **Affected Products:** CrabbyAVIF (Android platform external/rust/crabbyavif) — affected Android platform AVIF parser; specific version range unavailable.
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — patch: https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050 ; advisory: https://source.android.com/docs/security/bulletin/2025-08-01
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Ensure Scudo hardened allocator enabled (Android default), apply official patch/advisory, improve crash reporting to detect overflows into Scudo guard pages, and follow Google’s unsafe‑Rust training and review practices.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection vulnerabilities occur when hostile instructions are embedded in external data sources (emails, documents, calendar invites, plugins, or other content) that an AI system ingests, causing the model to execute attacker-controlled instructions or exfiltrate data. The layered defense strategy includes input filtering/validation, content provenance and sanitization, sandboxing/execution controls for agent/plugins, model fine‑tuning with adversarial data, presence and intent detection, and telemetry/monitoring to detect anomalous outputs.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — https://blog.google/security/mitigating-prompt-injection-attacks/
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply layered defenses: validate and sanitize external inputs before feeding to models; enforce strict least‑privilege for agents and plugins; restrict model access to sensitive contexts; use content provenance checks and allowlists/deny‑lists; fine‑tune models on adversarial examples and instruction‑following safety training; implement monitoring, rate‑limiting, and human review for high‑risk actions. Use Google’s guidance at https://blog.google/security/mitigating-prompt-injection-attacks/ for specifics.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** State‑sponsored actors target large backbone, PE and CE routers, compromising devices or trusted connections to gain persistent, long‑term access. They modify router configuration or firmware to maintain footholds and use the compromised infrastructure for lateral movement and data exfiltration.
- **Affected Products:** Backbone routers, provider‑edge (PE) routers, customer‑edge (CE) routers and other network devices
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Isolate affected devices if compromise suspected; perform integrity checks and reinstall firmware/software from trusted images; rotate and enforce strong administrative credentials and multi‑factor authentication; limit management‑plane access with VPN/ACLs or jump hosts; apply vendor security advisories/patches when available; monitor for anomalous configuration changes; collect and analyze device logs and network telemetry; implement segmentation and out‑of‑band management.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** GRU unit 26165 conducts espionage via spearphishing (malicious attachments and links), credential guessing/brute force, exploitation of public‑facing applications (Outlook NTLM calendar exploit CVE‑2023‑23397 to harvest NTLM hashes, Roundcube and WinRAR RCEs), manipulation of Exchange mailbox permissions for mailbox collection, Active Directory reconnaissance and credential dumping (Certipy, ADExplorer, ntdsutil), lateral movement (Impacket, PsExec, RDP), exfiltration via OpenSSH/PowerShell, and targeting IP cameras via RTSP brute force to monitor shipments.
- **Affected Products:** Microsoft Outlook (NTLM/calendar) – CVE-2023-23397, Roundcube Webmail – CVE-2020-12641, CVE-2020-35730, CVE-2021-44026, WinRAR – CVE-2023-38831, other internet‑facing VPNs and SOHO devices
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** true
- **Threat Actors:** GRU 85th GTsSS (Unit 26165) — tracked as APT28 / Fancy Bear / Forest Blizzard / Blue Delta
- **Mitigation:** Apply vendor patches for cited CVEs; harden email infrastructure (disable/limit NTLM, monitor for malicious calendar invites using Microsoft‑provided detection script); patch Roundcube and WinRAR; harden and monitor VPNs and SOHO devices; audit and monitor IP camera accounts and RTSP access; increase logging/threat hunting for indicators and LOLBin abuse (ntdsutil, wevtutil, vssadmin, Certipy, ADExplorer); implement MFA and privileged access controls.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-41091 is a local privilege escalation caused by improper link resolution ('link following') before file access in Microsoft Defender/Malware Protection Engine. CVE-2026-45498 is a denial‑of‑service vulnerability in the Microsoft Defender Antimalware Platform triggered by crafted input that disrupts the service.
- **Affected Products:** Microsoft Defender (Microsoft Malware Protection Engine / Antimalware Platform)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply vendor updates immediately (install Microsoft security updates/patches and engine/definition updates). If patching is delayed, follow Microsoft/enterprise hardening guidance: restrict local access to trusted users, disable unneeded components, and ensure up‑to‑date antimalware definitions and endpoint protections.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-41091; https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45498

---

## 10. 🟠 Zero-Day — What the Latest ShinyHunters Breaches Reveal About Modern Cyberattacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://www.securityweek.com/what-the-latest-shinyhunters-breaches-reveal-about-modern-cyberattacks/>

> Groups like ShinyHunters are demonstrating that attackers do not necessarily need malware or zero-day exploits to cause massive damage. The post What the Latest ShinyHunters Breaches Reveal About Modern Cyberattacks appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Attack used cross‑site scripting (XSS) vulnerabilities in Canvas Free‑for‑Teacher accounts to escalate to administrative access and exfiltrate data; additionally, ShinyHunters employed credential theft, MFA fatigue/vishing, OAuth token abuse, misconfigured guest‑user permissions, and compromised SaaS integrations.
- **Affected Products:** Instructure Canvas (Free-for-Teacher tier)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** ShinyHunters
- **Mitigation:** Disable/retire affected Free-for-Teacher accounts; enforce least‑privilege OAuth scopes; inventory and revoke unnecessary tokens; deploy phishing‑resistant MFA (FIDO2/WebAuthn); harden identity controls and monitoring; perform web‑app security testing (pen testing, SAST/DAST); monitor for anomalous bulk data exports and privileged activity.
- **Vendor Advisory:** https://instructure.com/incident_update

---

## 11. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
