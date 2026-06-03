# Zero Day Pulse

> **Generated:** 2026-06-03 10:32 UTC &nbsp;|&nbsp; **Total:** 16 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 2 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal(s) in the SimpleHelp web interface allow unauthenticated attackers to retrieve logs, configuration files, and credentials, leading to downstream compromise.
- **Affected Products:** SimpleHelp remote support software v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Public PoC is available – OffSec blog: https://www.offsec.com/blog/cve-2024-57727/
- **Patch Available:** SimpleHelp 5.5.8 fixes released – see vendor advisory: https://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570
- **Active Exploitation:** Yes – confirmed active exploitation reported by CISA (AA25-163A).
- **Threat Actors:** Ransomware operators (e.g., DragonForce) and generic ransomware actors
- **Mitigation:** Upgrade to SimpleHelp v5.5.8. If immediate patching is impossible, restrict access to SimpleHelp management interfaces (network segmentation, firewall rules, IP allowlists), monitor for suspicious access and credential theft, and rotate exposed credentials.
- **Vendor Advisory:** https://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570

---

## 2. 🟠 Zero-Day — Google June 2026 Android Update Patches 124 Flaws, One Actively Exploited

**CVE:** `CVE-2025-48595` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-02
**Reference:** <https://thehackernews.com/2026/06/google-june-2026-android-update-patches.html>

> Google on Monday released patches for 124 security vulnerabilities impacting its Android operating system for the month of June 2026, including one high-severity flaw in the Framework component that has come under active exploitation.

Tracked as CVE-2025-48595 (CVSS score: 8.4), the security flaw has been described as a case of privilege escalation without requiring any user interaction. The

**Parallel AI Enrichment:**

- **Technical Details:** Integer overflow in the Android Framework that permits elevation of privilege (local/remote escalation) with no user interaction; enables attackers to gain elevated system privileges on affected Android versions.
- **Affected Products:** Android 14, Android 15, Android 16, Android 16-qpr2
- **CVSS Score:** 8.4
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC or weaponized exploit reported; exploit availability: not known / none public
- **Patch Available:** Official vendor patch available; security patch level 2026-06-05 or later addresses the issue.
- **Active Exploitation:** Confirmed limited, targeted active exploitation reported by Google and multiple security outlets (limited/targeted in the wild).
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2026/2026-06-01

---

## 3. 🟠 Zero-Day — Google fixes one actively exploited Android zero-day, 124 flaws

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-02
**Reference:** <https://www.bleepingcomputer.com/news/security/google-fixes-one-actively-exploited-android-zero-day-124-flaws/>

> Google has released the June 2026 Android security patches to address 124 vulnerabilities, including one zero-day flaw exploited in targeted attacks. [...]

**Parallel AI Enrichment:**

- **Technical Details:** A no‑interaction privilege escalation vulnerability (CVE‑2025‑48595) in the Android Framework affecting Android 14‑16 allows attackers to gain elevated privileges without user interaction.
- **Affected Products:** Android 14, Android 15, Android 16
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept is available; exploitation is confirmed in the wild.
- **Patch Available:** June 2026 Android security patches are available at the Android security bulletin.
- **Active Exploitation:** Active exploitation has been confirmed in targeted attacks, as reported by security news outlets.
- **Threat Actors:** None known
- **Mitigation:** Apply the June 2026 Android security patches (security patch level 2026-06-05 or later).
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2026/2026-06-01

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) — adversaries seed malicious prompt‑instruction payloads on web content scanned or browsed by AI agents, aiming to corrupt agent behavior by causing it to follow attacker‑supplied instructions (10 new IPI payloads observed in the wild).
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit reported.
- **Patch Available:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html (no vendor patch noted)
- **Active Exploitation:** Yes — security researchers observed 10 new indirect prompt injection payloads caught in the wild (sources: Google Security Blog, Infosecurity Magazine, Forcepoint).
- **Threat Actors:** None known
- **Mitigation:** Harden agent prompt handling: treat external web content as untrusted, use strict input sanitization and prompt templates that do not accept or execute external instructions; apply browsing rules to ignore instructions in fetched content; monitor for anomalous outputs.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack where malicious instructions are injected into data or tools consumed by an LLM (e.g., web content, attachments, integrated apps), causing the model or agentic automation to follow attacker‑supplied instructions without direct user input.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit unavailable
- **Patch Available:** Patch not applicable; mitigations and defense‑in‑depth guidance provided at vendor advisory URL above.
- **Active Exploitation:** Reports indicate in‑the‑wild IPI payloads were observed (research reports April 2026) but no attribution to specific threat actor groups; active exploitation has been reported in research summaries.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses including input sanitization, model‑level instruction filters, runtime tooling restrictions, provenance and source‑trust controls, continuous monitoring and telemetry, and defense‑in‑depth as described in Google’s whitepaper/blog guidance.
- **Vendor Advisory:** http://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection allows a malicious site to inject crafted prompts into the AI agent’s context, causing the agent to execute unintended commands or reveal information.
- **Affected Products:** Google Chrome (latest stable), Gemini for Chrome (preview/agentic browsing)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or exploit is currently known.
- **Patch Available:** No separate patch; security improvements are built into Chrome via updated architecture and defenses.
- **Active Exploitation:** No confirmed active exploitation in the wild has been reported.
- **Threat Actors:** None known
- **Mitigation:** Enable Chrome’s built‑in layered defenses that block prompt injection, restrict cross‑origin AI agent access, and enforce safety checks on AI‑generated actions.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow in the Rust‑based CrabbyAVIF image processing library, where input data could exceed the allocated buffer size, leading to potential memory corruption.
- **Affected Products:** Android – CrabbyAVIF library
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit available.
- **Patch Available:** https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050
- **Active Exploitation:** No active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Use of Android's Scudo hardened allocator, which places guard pages around secondary allocations, making the buffer overflow non‑exploitable.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection involves hidden malicious instructions embedded in external data sources (emails, documents, calendar invites, HTML/SVG comments, image metadata, vector‑DB chunks) that are later ingested by LLM‑enabled workflows, leading to unauthorized actions or data exfiltration.
- **Affected Products:** Gemini (Google Workspace, Gemini app)
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** PoC examples are described in third‑party research; no single public weaponized exploit URL from the vendor.
- **Patch Available:** No vendor patch; mitigations are provided via model hardening and security controls.
- **Active Exploitation:** Reporting of active tests and detections by third‑party researchers; no confirmed publicized APT campaign attribution.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: model hardening (Gemini 2.5), prompt‑injection content classifiers, markdown sanitization, suspicious URL redaction (Safe Browsing), user‑confirmation framework (Human‑In‑The‑Loop), end‑user security notifications; additionally limit AI permissions, sanitize inputs, monitor AI behavior, and conduct red‑team exercises.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors exploit publicly known CVEs in network edge devices (examples: CVE-2023-20198, CVE-2023-20273, CVE-2018-0171, CVE-2024-21887) to create admin accounts, modify router configs, enable tunnels, mirror traffic (SPAN/RSPAN/ERSPAN), abuse Guest Shell containers, modify ACLs, open ports, and install persistence tooling.
- **Affected Products:** Cisco IOS, Cisco IOS XE, Cisco NX-OS, Ivanti Connect Secure, Ivanti Policy, Palo Alto, Fortinet, Juniper, Nokia, Sierra Wireless, SonicWall
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Public exploit/tooling referenced (e.g., siet.py, map.tcl, tclproxy.tcl, wodSSHServer) and known CVE exploits; PoC URLs not provided in advisory.
- **Patch Available:** Vendor patches exist for many referenced CVEs (see Cisco, Ivanti advisories linked from CISA advisory); advisory contains vendor hardening guidance and links.
- **Active Exploitation:** Confirmed active exploitation reported in advisory and supporting industry analysis; advisory lists historically exploited CVEs and notes APT actors routinely exploit Internet-exposed devices for persistent access.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching vulnerable edge devices; follow vendor hardening guides (Cisco IOS/IOS XE hardening, Cisco Software Checker), disable/monitor Guest Shell, audit and harden SNMP, rotate and strengthen credentials, monitor logs, hunt for indicators (CISA provides JSON/XML IOC lists), follow CISA/NSA/FBI guidance.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** The campaign leverages spear‑phishing emails to harvest credentials, employs living‑off‑the‑land tools and custom web shells for persistence, escalates privileges on compromised hosts, and hijacks accounts to move laterally within logistics and technology supply‑chain networks.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponised exploit is reported.
- **Patch Available:** No universal vendor patch is available; the advisory describes tactics and mitigations instead.
- **Active Exploitation:** Yes – sustained targeting and intrusions by the Russian GRU (85th GTsSS / Unit 26165) have been reported.
- **Threat Actors:** GRU 85th GTsSS (Unit 26165), also known as APT28/Fancy Bear.
- **Mitigation:** Apply multi‑factor authentication, segment networks, deploy EDR/IDS, patch known vulnerabilities, hunt for web shells and anomalous activity, enforce least‑privilege, monitor supply‑chain accounts, and follow CISA/FBI/NCSC mitigation recommendations.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 11. 🟠 Zero-Day — Microsoft Tries to Calm Legal Threat Fears After Zero-Day Disclosure Backlash

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://www.securityweek.com/microsoft-tries-to-calm-legal-threat-fears-after-zero-day-disclosure-backlash/>

> Microsoft responds to backlash over its threats of legal action against researchers who publicly disclose zero-day vulnerabilities. The post Microsoft Tries to Calm Legal Threat Fears After Zero-Day Disclosure Backlash appeared first on SecurityWeek .

---

## 12. 🟠 Zero-Day — VS Code zero-day lets hackers steal GitHub tokens in one click

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://www.bleepingcomputer.com/news/security/vs-code-zero-day-lets-hackers-steal-github-tokens-in-one-click/>

> A security researcher has released exploit code for a Visual Studio Code (VS Code) zero-day vulnerability that allows attackers to steal GitHub authentication tokens by tricking users into clicking a link. [...]

---

## 13. 🟠 Zero-Day — CISA flags two-year-old Oracle flaw as actively exploited in attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-02
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-oracle-weblogic-flaw/>

> CISA has ordered government agencies to secure their systems against a high-severity Oracle WebLogic Server vulnerability that was patched two years ago and is now actively exploited in attacks. [...]

---

## 14. 🟠 Zero-Day — Oracle WebLogic Vulnerability Exploited in the Wild

**CVE:** `CVE-2024-21182` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-02
**Reference:** <https://www.securityweek.com/oracle-weblogic-vulnerability-exploited-in-the-wild/>

> The vulnerability is CVE-2024-21182 and it can be exploited without authentication to hack affected WebLogic servers. The post Oracle WebLogic Vulnerability Exploited in the Wild appeared first on SecurityWeek .

---

## 15. 🟡 High Severity — Critical Kirki flaw exploited to hijack WordPress admin accounts

**CVE:** `CVE-2026-8206` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-02
**Reference:** <https://www.bleepingcomputer.com/news/security/critical-kirki-flaw-exploited-to-hijack-wordpress-admin-accounts/>

> Hackers are exploiting a critical privilege escalation vulnerability (CVE-2026-8206) in the Kirki plugin for WordPress to take over any user account, including those belonging to administrators. [...]

---

## 16. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
