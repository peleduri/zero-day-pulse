# Zero Day Pulse

> **Generated:** 2026-05-24 08:16 UTC &nbsp;|&nbsp; **Total:** 9 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 8 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 9

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path traversal vulnerability in SimpleHelp Remote Monitoring and Management that permits an unauthenticated attacker to supply '../' sequences in file path parameters, enabling arbitrary file read/write and possible remote code execution.
- **Affected Products:** SimpleHelp 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know)
- **Active Exploitation:** true (https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a)
- **Threat Actors:** Ransomware actors (unspecified)
- **Mitigation:** Apply the vendor‑provided patch by upgrading SimpleHelp to a version newer than 5.5.7; keep the software updated and restrict remote access where possible.
- **Vendor Advisory:** https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) involves seeding malicious instructions in web content or comments so that AI agents that browse or ingest that content obey the injected instructions; variants include hidden webpage code, crafted comments in repositories, or payloads designed to exploit elevated agent privileges ('Comment and Control' weaponizes agent elevated access to control agent behavior).
- **Affected Products:** AI agents and tooling that browse or ingest untrusted web content (e.g., Anthropic Claude Code Security Review, Google Gemini CLI Action, GitHub Copilot Agent)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Harden agent browsing and content ingestion: treat web content as untrusted, use strict input sanitization and instruction‑parsing defenses, limit agents' elevated privileges and side‑effecting actions, apply allowlists/disallowlists, perform content provenance checks, and implement runtime guards and prompt integrity checks. Vendor guidance and detection monitoring recommended.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is a vulnerability where malicious instructions are hidden in external data (web pages, emails, documents, etc.) that an LLM processes, causing the model to follow the attacker’s instructions without direct user input. Attack surfaces include agentic automation and multi‑source data ingestion, allowing hidden commands to alter model outputs or trigger unauthorized actions.
- **Affected Products:** Gemini, Google Workspace apps (Gmail, Docs, Drive, Chat)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Google’s mitigation includes layered controls such as deterministic defenses (user confirmation, URL sanitization, tool‑chaining policies), ML‑based defenses retrained on synthetic data, markdown sanitization and suspicious URL redaction, Gemini model hardening to ignore harmful instructions, and end‑user notifications with a confirmation framework.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection in the Gemini CLI permits an attacker to inject malicious instructions that are executed by the agent, resulting in remote code execution prior to sandbox activation.
- **Affected Products:** @google/gemini-cli < 0.39.1, @google/gemini-cli < 0.40.0-preview.3, google-github-actions/run-gemini-cli < 0.1.22
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (http://thehackernews.com/2026/04/google-fixes-cvss-10-gemini-cli-ci-rce.html)
- **Patch Available:** true (http://thehackernews.com/2026/04/google-fixes-cvss-10-gemini-cli-ci-rce.html)
- **Active Exploitation:** true (http://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Apply origin isolation, layered defenses, and a trusted‑model architecture as described by Google to limit indirect prompt injection; adopt the security layers introduced for agentic browsing in Chrome.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow in the Rust CrabbyAVIF component allowed out‑of‑bounds writes. Android’s Scudo hardened allocator inserted guard pages around secondary allocations, making the overflow non‑exploitable. The patch modifies the buffer handling logic to properly enforce bounds.
- **Affected Products:** Android platform (specific versions not disclosed) – CrabbyAVIF component
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true (https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the patch at https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050 or update the device to an Android build that contains the fix. Ensure Scudo hardened allocator is enabled to provide additional protection.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) embeds malicious instructions in external content (emails, documents, calendar invites, images/URLs) so that a generative AI ingests them and follows attacker instructions; Google mitigates by model hardening (adversarial training), ML-based content classifiers, markdown sanitization/suspicious-URL redaction, security “thought-reinforcement,” and human-in-the-loop confirmations.
- **Affected Products:** Gemini (Gemini 2.5, Gemini in Google Workspace, Gemini app)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** false
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses: adversarial model training, content classifiers to detect malicious instructions, markdown sanitization and external URL redaction, contextual user confirmations (HITL), end-user mitigation notifications, and integration with threat intelligence (Safe Browsing). See vendor advisory for Help Center links and white papers.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors modify router firmware/configurations to maintain persistent, long‑term access, exfiltrate data, and pivot using compromised devices and trusted connections.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Network segmentation, continuous monitoring, applying available patches, changing default credentials, hardening management interfaces (e.g., SNMP), disabling unused services, and following vendor‑specific advisories.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Actors employed spearphishing (malicious archive or link) to gain initial access, exploited Internet‑facing services such as corporate VPNs (including SQL injection), and leveraged the WinRAR vulnerability (CVE‑2023‑38831) to execute arbitrary code from crafted archives. Post‑compromise, tools like Impacket, PsExec, and RDP were used for lateral movement and credential harvesting.
- **Affected Products:** RARLAB WinRAR (CVE-2023-38831), Roundcube Webmail (versions before 1.2.13, 1.3.x before 1.3.16, 1.4.x before 1.4.10)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** GRU unit 26165 (also known as APT28, Fancy Bear, Forest Blizzard, Blue Delta)
- **Mitigation:** Deploy network segmentation/Zero Trust, enable host firewalls and EDR, restrict and monitor VPN and remote service access, apply all relevant patches and firmware updates (including for IP cameras), harden IP cameras (disable remote access, require VPN/MFA), enable Windows attack surface reduction rules, implement application allow‑listing, and continuously monitor Windows logs and LOTL utility usage for indicators of compromise.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is a memory-safety bug in DNS parsing within modem firmware (CVE-2024-27227) that can be triggered by parsing untrusted DNS responses; Google implemented a memory-safe Rust DNS parser (hickory-proto) in the modem to eliminate this class of parsing-related memory-safety vulnerabilities.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true — http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html
- **Active Exploitation:** false — no confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Install vendor updates/Pixel system updates that include the modem mitigations; as a general mitigation, minimize exposure of modem network surfaces and apply carrier/security updates promptly.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html

---
