# Zero Day Pulse

> **Generated:** 2026-06-02 15:57 UTC &nbsp;|&nbsp; **Total:** 13 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated remote attackers can exploit a directory‑traversal issue in the SimpleHelp web interface to retrieve arbitrary files (e.g., logs, configuration files, credentials) from the server, which can lead to escalation and ransomware deployment.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (https://medium.com/@RosanaFS/simplehelp-cve-2024-57727-tryhackme-walkthrough-9f88c2061fb9)
- **Patch Available:** true (https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know, http://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570)
- **Active Exploitation:** true (https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a)
- **Threat Actors:** Ransomware actors (including DragonForce)
- **Mitigation:** Apply the SimpleHelp 5.5.8 patch or later. If a patch cannot be applied immediately, block access to the SimpleHelp management interface from untrusted networks, restrict it to trusted IP addresses, implement network segmentation, rotate credentials, and monitor for anomalous file access or log retrieval activity.
- **Vendor Advisory:** https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — Google fixes one actively exploited Android zero-day, 124 flaws

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-02
**Reference:** <https://www.bleepingcomputer.com/news/security/google-fixes-one-actively-exploited-android-zero-day-124-flaws/>

> Google has released the June 2026 Android security patches to address 124 vulnerabilities, including one zero-day flaw exploited in targeted attacks. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true; Vendor advisory URL unavailable.
- **Active Exploitation:** true
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection manipulates an AI system by embedding malicious instructions in data that later becomes part of the model’s prompt context, causing the model to execute unintended actions.
- **Affected Products:** Google Gemini (including Workspace integration), Anthropic Claude Code
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (http://infosecurity-magazine.com/news/researchers-10-wild-indirect)
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply input sanitization, enforce strict content filtering, limit context window size, and monitor for suspicious prompts as described in Google's layered‑defense guidance.
- **Vendor Advisory:** http://github.com/advisories/GHSA-vp62-r36r-9xqp

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) allows an attacker to inject malicious instructions into data or tools consumed by an LLM, influencing its behavior without direct user input. In the CVE‑2026‑39861 chain, a prompt‑injection step is required to trigger a sandbox escape that leads to arbitrary file write.
- **Affected Products:** Google Workspace with Gemini; Anthropic Claude Code (CVE-2026-39861)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true (http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html; https://advisories.gitlab.com/npm/@anthropic-ai/claude-code/CVE-2026-39861/)
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Apply layered defenses: sanitize and validate external content, restrict tool/data access scopes, use integrity checks, enforce deterministic tool outputs, track provenance, harden prompts and use injection‑resistant parsing, continuously monitor telemetry, and apply vendor‑provided patches and updates as described in the Google blog.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is a threat where untrusted web content causes a browser‑embedded AI agent to take unintended actions (e.g., initiating financial transactions or exfiltrating data). It can appear in malicious sites, third‑party iframe content, or user‑generated content and is mitigated by isolating the agent from untrusted content, using a User Alignment Critic model, origin gating, deterministic checks, user confirmations for sensitive actions, and continuous monitoring.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known.
- **Mitigation:** Mitigations include: a separate User Alignment Critic model that vet agent actions; Agent Origin Sets that restrict readable and writable origins; deterministic checks and mandatory user confirmations for sensitive operations (e.g., payments, medical sites); real‑time indirect‑prompt‑injection classifiers; limiting model exposure to untrusted content (iframe gating); and rapid distribution of fixes via Chrome’s auto‑update mechanism.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Improper locking/race‑condition in the Rust‑based Android Binder subsystem, potentially leading to privilege escalation or kernel crashes.
- **Affected Products:** Android platform components (C, C++, Java, Kotlin, Rust); Rust‑based Android Binder implementation; Linux kernel 6.18 and later (Android Binder driver).
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply the patches from the Android Security Bulletin (2025‑12‑01). If patching is delayed, limit exposure by applying least‑privilege, disabling/isolating affected components, and using platform mitigations such as SELinux and sandboxing.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-12-01

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) embeds malicious instructions in external content (web pages, repositories, emails, documents, calendar invites). When an LLM or agent ingests that content as context, the hidden instructions can override or contaminate system instructions, causing data exfiltration, unauthorized actions, or model hijacking. Attack vectors include poisoned web content, malicious repo README/code comments, or crafted files that are parsed by agents without instruction isolation.
- **Affected Products:** Google Gemini, Gemini in Workspace apps, Anthropic Claude Code
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — http://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true — http://securityweek.com/malicious-ai-prompt-injection-attacks-increasing-but-sophistication-still-low-google
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: input sanitization/validation, provenance and source‑trust checks, instruction scrubbing/normalized internal prompts, sandboxing agent actions, strict data access controls, user confirmation for sensitive outputs, telemetry and detection for anomalous instruction patterns.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** APT actors exploit publicly known CVEs and weak/default credentials on internet‑exposed edge devices (routers, PE/CE routers, gateways) to gain initial access (T1190), create unauthorized administrative accounts via authentication bypass (e.g., CVE-2023-20198 on Cisco IOS XE), modify ACLs, abuse Guest Shell on Cisco IOS XE/NX‑OS for persistence, use SNMP/SSH/TCL/Python scripts, and establish GRE/MPLS tunnels for data exfiltration.
- **Affected Products:** Cisco IOS/IOS XE (CVE-2023-20198, CVE-2023-20273, CVE-2018-0171), Ivanti Connect Secure/Policy (CVE-2024-21887), Palo Alto PAN-OS (CVE-2024-3400); other likely targets include Fortinet, Juniper, Nokia routers/switches, Sierra Wireless, SonicWall, Microsoft Exchange.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching known exploited CVEs; disable unused protocols/services; change default credentials and require public‑key authentication for admin roles; disable management access from untrusted networks; perform firmware/software integrity checks (hash validation) and use CISCO/NIST/NDI guidance; follow CISA mitigations and Cisco‑specific hardening (disable or monitor Guest Shell); conduct threat hunting for indicators (e.g., Snort rule for CVE-2023-20198).
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Long‑running Russian GRU espionage campaign targeting Western logistics and technology organizations. Adversaries use targeted intrusion tradecraft including spearphishing and credential compromise for initial access, exploitation of public‑facing services, deployment of web shells and custom malware, credential harvesting and lateral movement, and persistent C2 to exfiltrate data and maintain access.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** GRU 85th GTsSS (Unit 26165) — tracked as APT28 (Russian state‑sponsored)
- **Mitigation:** Apply MFA for remote access; enforce least privilege and network segmentation; patch and harden public‑facing applications; deploy/monitor EDR and logging (Azure/AWS/GCP, VPNs, remote access gateways); rotate and secure credentials; hunt for web shells and unusual outbound connections; follow CISA/FBI incident response guidance and report intrusions.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — Android Update Patches Exploited Zero-Day, 123 Other Vulnerabilities

**CVE:** `CVE-2025-48595` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-02
**Reference:** <https://www.securityweek.com/android-update-patches-exploited-zero-day-123-other-vulnerabilities/>

> Google says the Android vulnerability CVE-2025-48595 has been exploited in limited, targeted attacks. The post Android Update Patches Exploited Zero-Day, 123 Other Vulnerabilities appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true — https://source.android.com/docs/security/bulletin/2026/2026-06-01
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Install the June 2026 Android security updates from device OEMs and apply Google’s security patches as provided. General hardening: enable Play Protect, restrict app installs to Play Store only, and keep devices updated.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2026/2026-06-01

---

## 11. 🟠 Zero-Day — CISA flags two-year-old Oracle flaw as actively exploited in attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-02
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-oracle-weblogic-flaw/>

> CISA has ordered government agencies to secure their systems against a high-severity Oracle WebLogic Server vulnerability that was patched two years ago and is now actively exploited in attacks. [...]

---

## 12. 🟠 Zero-Day — Oracle WebLogic Vulnerability Exploited in the Wild

**CVE:** `CVE-2024-21182` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-02
**Reference:** <https://www.securityweek.com/oracle-weblogic-vulnerability-exploited-in-the-wild/>

> The vulnerability is CVE-2024-21182 and it can be exploited without authentication to hack affected WebLogic servers. The post Oracle WebLogic Vulnerability Exploited in the Wild appeared first on SecurityWeek .

---

## 13. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
