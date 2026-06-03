# Zero Day Pulse

> **Generated:** 2026-06-03 02:36 UTC &nbsp;|&nbsp; **Total:** 14 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 2 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal (directory traversal) vulnerability allowing unauthenticated remote attackers to read sensitive files such as logs, configuration files, and credentials from SimpleHelp servers (affects v5.5.7 and earlier).
- **Affected Products:** SimpleHelp remote support software v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true - http://tenable.com/cve/CVE-2024-57727
- **Patch Available:** true - https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (e.g., DragonForce-associated ransomware actors)
- **Mitigation:** Upgrade SimpleHelp to 5.5.8 or later; if immediate patching not possible, isolate/unexpose SimpleHelp management interfaces from public networks, block access to admin ports, apply network segmentation, and monitor for suspicious activity and credential theft.
- **Vendor Advisory:** https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — Google June 2026 Android Update Patches 124 Flaws, One Actively Exploited

**CVE:** `CVE-2025-48595` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-02
**Reference:** <https://thehackernews.com/2026/06/google-june-2026-android-update-patches.html>

> Google on Monday released patches for 124 security vulnerabilities impacting its Android operating system for the month of June 2026, including one high-severity flaw in the Framework component that has come under active exploitation.

Tracked as CVE-2025-48595 (CVSS score: 8.4), the security flaw has been described as a case of privilege escalation without requiring any user interaction. The

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2025-48595 enables code execution via an integer overflow, resulting in local privilege escalation on Android without requiring any user interaction.
- **Affected Products:** Android operating system (June 2026 security patch), Framework component
- **CVSS Score:** 8.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply the June 2026 Android security patch (available via the official Android security bulletin) to remediate CVE-2025-48595.
- **Vendor Advisory:** http://source.android.com/docs/security/bulletin/2026/2026-06-01

---

## 3. 🟠 Zero-Day — Google fixes one actively exploited Android zero-day, 124 flaws

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-02
**Reference:** <https://www.bleepingcomputer.com/news/security/google-fixes-one-actively-exploited-android-zero-day-124-flaws/>

> Google has released the June 2026 Android security patches to address 124 vulnerabilities, including one zero-day flaw exploited in targeted attacks. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Local attackers can exploit the actively abused high‑severity Android Framework vulnerability (CVE-2025-48595) to obtain code execution and escalate privileges on devices running Android 14 or later.
- **Affected Products:** Android 14, Android 15, Android 16, Android 16 QPR2
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (https://source.android.com/docs/security/bulletin/2026/2026-06-01)
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply the June 2026 Android security patches (security patch level 2026‑06‑05 or later) to all affected devices.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2026/2026-06-01

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when AI systems process external content (websites, emails, documents) containing malicious instructions which the AI may follow. Google scanned Common Crawl using pattern‑matching, LLM‑based classification (Gemini), and human validation; observed categories include harmless pranks, helpful guidance, SEO manipulation, deterring AI agents, and malicious attempts (data exfiltration, destruction). Many observed attacks were low‑sophistication experiments on public web pages.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses — harden AI models and products (e.g., Google’s red‑team testing, defenses in Gemini), pattern‑based filtering combined with LLM classification and human review, limit agent autonomy and external content handling, resource/time limits to avoid streaming/infinite‑text traps, and participation in vulnerability disclosure programs (e.g., Google AI Vulnerability Reward Program).
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) injects malicious instructions into data or tool inputs (e.g., web pages, calendar event descriptions) that are later ingested by an LLM. The model then follows the attacker‑supplied instruction, leading to actions like credential theft, API key exfiltration, or unauthorized financial transactions.
- **Affected Products:** Google Workspace, Gemini, Google Calendar
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Deploy a layered defense: conduct regular human and automated red‑team exercises, continuously monitor for IPI indicators, retrain ML‑based detectors, harden prompts and model configurations, and iteratively update defenses as new vectors are discovered.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an evolving threat vector where malicious content on web pages or other inputs manipulates agentic AI prompts to cause unsafe or unauthorized actions. It can appear in malicious sites and via indirect payloads that influence AI agents’ behavior.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Restrict origin access, block prompt injections, add layered defenses and watch‑over agents; follow vendor guidance in Chrome security blog post.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Android (unspecified versions)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection embeds hidden malicious instructions in external data sources (emails, documents, calendar invites, web content, or retrieval results). When a generative AI ingests such external content as context or retrieval‑augmented input, the hidden instructions can influence the model’s outputs or prompt‑following behavior to exfiltrate data, perform unauthorized actions, or override safety constraints. Attack mechanisms include contaminated retrieval results, hidden HTML/metadata payloads, or attacker‑controlled content returned by integrated web/document sources. The attack leverages models' tendency to follow instructions present in contextual inputs and imperfect input sanitization or provenance checks.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Layered defenses including input provenance and origin tracking, stricter retrieval filters and sanitization of external content, instruction‑scoped parsing (separating user instructions from untrusted content), output filtering and red‑team testing, model fine‑tuning to resist following arbitrary embedded instructions, strict access controls for data egress, user warnings and consent, and monitoring/alerting for anomalous model behavior.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors exploit publicly known CVEs and weak credentials to gain initial access to edge/backbone routers, modify router configurations for lateral movement, enable on‑box PCAP or SPAN/ERSPAN, create tunnels, alter AAA (TACACS+/RADIUS) to capture credentials, create privileged accounts, execute commands via SNMP/SSH/HTTP, and run virtual containers on devices for persistence and evasion.
- **Affected Products:** large backbone routers, provider‑edge (PE) routers, customer‑edge (CE) routers, Cisco IOS/XE, Ivanti Connect Secure/Policy, Palo Alto Networks, Fortinet, Juniper, Nokia, Sierra Wireless, SonicWall
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching of the listed CVEs, monitor and audit router configurations, enforce SNMPv3, disable unused protocols, change default credentials, require public‑key authentication, verify firmware hashes, monitor PCAP/tunnel activity, and follow the threat‑hunting guidance provided in the advisory.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Russian GRU 85th GTsSS (Unit 26165) / APT28.
- **Mitigation:** Implement network segmentation, multifactor authentication, patch management, monitor for indicators of compromise (see CISA advisory AA25-141A for IOCs), restrict remote access, and apply principle of least privilege.
- **Vendor Advisory:** Vendor advisory URL unavailable.

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

## 13. 🟡 High Severity — Critical Kirki flaw exploited to hijack WordPress admin accounts

**CVE:** `CVE-2026-8206` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-02
**Reference:** <https://www.bleepingcomputer.com/news/security/critical-kirki-flaw-exploited-to-hijack-wordpress-admin-accounts/>

> Hackers are exploiting a critical privilege escalation vulnerability (CVE-2026-8206) in the Kirki plugin for WordPress to take over any user account, including those belonging to administrators. [...]

---

## 14. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
