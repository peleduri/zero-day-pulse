# Zero Day Pulse

> **Generated:** 2026-06-29 02:11 UTC &nbsp;|&nbsp; **Total:** 10 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 9 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 8

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated remote attackers can perform path traversal to read arbitrary files on the server by manipulating file-path parameters.
- **Affected Products:** SimpleHelp remote support software v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Public proof-of-concept available on GitHub (imjdl/CVE-2024-57727) – includes poc.py script.
- **Patch Available:** Patch released as SimpleHelp version 5.5.8 (available from SimpleHelp download page).
- **Active Exploitation:** Confirmed exploitation by ransomware actors leveraging CVE-2024-57727 to compromise SimpleHelp RMM customers, as reported by CISA.
- **Threat Actors:** Ransomware actors
- **Mitigation:** Upgrade to SimpleHelp version 5.5.8 or later, which contains security fixes for this vulnerability.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) enables an attacker to influence an LLM’s behavior by injecting malicious instructions into the data or tools the LLM uses to complete a user’s query; these injected instructions can be embedded in external content and may affect the model even without direct user input.
- **Affected Products:** Google Workspace with Gemini
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) or weaponized exploit is known.
- **Patch Available:** No official patch has been released.
- **Active Exploitation:** No confirmed active exploitation has been reported; Google has observed an increase in malicious indirect prompt injection attempts on public web sites.
- **Threat Actors:** None known
- **Mitigation:** Layered mitigations described by Google: deterministic defenses (user confirmation, URL sanitization, tool-chaining policies and centralized policy engine/configuration), ML-based defenses (synthetic-data-driven model retraining and validation), LLM-based defenses (prompt engineering and iterative optimization), Gemini model hardening (improvements to Gemini to detect and ignore harmful embedded instructions), continuous human and automated red-teaming, and the Google AI Vulnerability Rewards Program (VRP).
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Near-miss linear buffer overflow in CrabbyAVIF (Rust unsafe code) rendered non-exploitable by Scudo hardened allocator guard pages; vulnerability tracked as CVE-2025-48530 and patched.
- **Affected Products:** Android platform (first-party and third-party components across C, C++, Java, Kotlin, and Rust); Android Linux kernel 6.12 (Rust support)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) or weaponized exploit is reported in the advisory.
- **Patch Available:** Yes — a patch was produced and tracked (see CVE-2025-48530 patch link in the advisory).
- **Active Exploitation:** No confirmed active exploitation reported in the advisory; the advisory states the vulnerability did not reach public release.
- **Threat Actors:** None known
- **Mitigation:** Use memory-safety strategies (adopt Rust for new systems code), enable and require Scudo hardened allocator where possible, and apply the referenced patch for CVE-2025-48530.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is a class of attacks where hidden malicious instructions are embedded in external data sources (emails, documents, calendar invites, dynamic URLs) that can cause generative AI agents to exfiltrate data or perform rogue actions; defenses discussed include layered defenses and suspicious URL detection (e.g., Safe Browsing) integrated into model pipelines.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof-of-concept examples have been published demonstrating data exfiltration via indirect prompt injection (e.g., Slack AI PoC writeups cited by the advisory and external posts).
- **Patch Available:** No official vendor patch indicated in the advisory; Google recommends layered defenses and detection controls (see advisory).
- **Active Exploitation:** No confirmed active exploitation campaigns reported in the cited sources; the advisory and writeups describe the technique and PoCs but do not report confirmed in-the-wild campaigns.
- **Threat Actors:** None known
- **Mitigation:** Use a layered defense strategy: filter and sanitize external data inputs, detect and block suspicious/dynamic URLs (e.g., Safe Browsing), apply content validation and least-privilege access for AI agents, and monitor for anomalous data exfiltration patterns as recommended in the Google advisory.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors target and compromise large backbone, PE and CE routers and other edge devices, leverage compromised devices and trusted connections to pivot, and modify router firmware/configuration to maintain persistent, long-term access and enable espionage operations.
- **Affected Products:** Backbone routers, provider edge (PE) routers, customer edge (CE) routers, and other network edge devices (no vendor/product versions specified)
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit URL reported in the cited sources; reports describe active compromise but do not publish exploit code.
- **Patch Available:** No official vendor patch or remediation guidance reported in the cited sources (vendor patch/advisory URL unavailable)
- **Active Exploitation:** Confirmed active exploitation reported: CISA and multiple analyst reports state PRC state-sponsored actors are actively compromising backbone/edge routers worldwide and maintaining persistent access.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Harden and monitor network-edge devices: segment networks, restrict and monitor management access to routers, apply vendor patches when available, replace or rebuild compromised routers, monitor router control plane and configurations for unauthorized changes, and deploy network-level anomaly detection and logging (as recommended by CISA and analysts).
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** The campaign uses phishing and credential theft, exploitation of Internet-facing infrastructure (corporate VPNs, public-facing application vulnerabilities and SQL injection), exploitation of specific CVEs (e.g., WinRAR CVE-2023-38831, Roundcube CVE-2020-35730 and CVE-2020-12641), and living-off-the-land binaries for persistence and lateral movement.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) or weaponized exploit is referenced in the advisory or corpus.
- **Patch Available:** Patches/patch guidance exist for the CVEs referenced (see advisory CVE list; apply vendor CVE patches).
- **Active Exploitation:** The advisory describes and attributes active and ongoing targeting/exploitation of Western logistics and technology companies by GRU unit 26165.
- **Threat Actors:** APT28 (Fancy Bear), Russian GRU Unit 26165 (85th GTsSS)
- **Mitigation:** Network segmentation and Zero Trust design, patch vulnerable software and firmware (including IP cameras and listed CVEs), disable or harden legacy protocols (NTLM, SMBv1), harden host firewalls and network appliances, restrict/monitor outbound connections (block or alert on suspicious hosting/API services), enable and monitor authentication for remote camera access (use VPNs), and implement strong identity and access controls and hunt/monitor for listed IOCs.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit available.
- **Patch Available:** No patch available.
- **Active Exploitation:** No active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 10. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-27227 is a memory-safety flaw in the DNS parser of the Pixel baseband firmware, allowing remote attackers to trigger memory corruption via crafted DNS packets, leading to possible code execution; the vulnerability is network-borne, requires no privileges, and impacts confidentiality, integrity, and availability.
- **Affected Products:** Google Pixel 10 baseband modem firmware, Google Pixel 9 baseband modem firmware
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** No public proof-of-concept or exploit is known.
- **Patch Available:** Patches are available for CVE-2024-27227.
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Implement a Rust-based DNS parser and use Android's Scudo hardened allocator to mitigate the vulnerability.
- **Vendor Advisory:** http://blog.google/security/bringing-rust-to-the-pixel-baseband

---
