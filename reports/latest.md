# Zero Day Pulse

> **Generated:** 2026-06-25 14:01 UTC &nbsp;|&nbsp; **Total:** 16 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 4 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path‑traversal (directory traversal) flaw that lets unauthenticated attackers read arbitrary files on the server.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) software v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** true (http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know)
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors
- **Mitigation:** Apply the vendor‑released patch (upgrade SimpleHelp to a version newer than 5.5.7) and restrict network access to the RMM service.
- **Vendor Advisory:** http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — CISA Warns Critical Lantronix EDS5000 Flaw Is Being Actively Exploited

**CVE:** `CVE-2025-67038` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-24
**Reference:** <https://thehackernews.com/2026/06/cisa-warns-critical-lantronix-eds5000.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday warned of active exploitation of a critical security flaw impacting Lantronix EDS5000 Series devices, urging Federal Civilian Executive Branch (FCEB) agencies to apply the fixes by June 26, 2026.

The vulnerability in question is CVE-2025-67038 (CVSS score: 9.8), a code injection flaw that could result in the execution

**Parallel AI Enrichment:**

- **Technical Details:** The HTTP RPC module concatenates the username directly into a shell command for logging without sanitization, allowing OS command injection with root privileges.
- **Affected Products:** Lantronix EDS5000 (2.1.0.0R3), Lantronix EDS3000PS
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (http://cvefeed.io/vuln/detail/CVE-2025-67038)
- **Patch Available:** true (https://ltrxdev.atlassian.net/wiki/spaces/LTRXTS/pages/2538438657/Latest+Firmware+for+the+EDS5000+series+EDS5008+EDS5016+EDS5032)
- **Active Exploitation:** true (source: https://bleepingcomputer.com/news/security/cisa-warns-of-max-severity-ubiquiti-flaws-exploited-in-attacks)
- **Threat Actors:** None known
- **Mitigation:** Upgrade to EDS5000 version 2.2.0.0R1 (see vendor advisory).
- **Vendor Advisory:** https://ltrxdev.atlassian.net/wiki/spaces/LTRXTS/pages/2538438657/Latest+Firmware+for+the+EDS5000+series+EDS5008+EDS5016+EDS5032

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection via malicious content on web pages that AI agents ingest, causing the model to follow attacker‑supplied instructions, potentially leading to command execution or data exfiltration.
- **Affected Products:** Google Gemini Enterprise
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Input and output validation and sanitization, human oversight and controls in LLMs.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is a technique where an attacker injects malicious instructions into data or tools used by an LLM, influencing its behavior without direct user input. A zero‑click vulnerability (GeminiJack) demonstrated this in Google Gemini Enterprise.
- **Affected Products:** Google Workspace, Google Gemini Enterprise
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true (source: http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability)
- **Patch Available:** false
- **Active Exploitation:** true (sources: http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability, http://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads)
- **Threat Actors:** None known
- **Mitigation:** Google Workspace employs continuous monitoring for known IPI patterns, input/output validation, sanitization, and human oversight. Implementing strict content sanitization and limiting LLM access to external data reduces risk.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** An indirect prompt-injection (zero-click) vulnerability (GeminiJack) allows an attacker to embed malicious prompts into the AI model's input via web content or chained injections, causing agentic browsing or Gemini Enterprise to perform unintended actions without user interaction.
- **Affected Products:** Google Chrome (agentic browsing), Google Gemini Enterprise
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Google announced a new agentic-architecture with layered defenses (prompt-injection blocking, origin access restrictions, monitoring and policy enforcement) to mitigate indirect prompt injection; apply vendor recommendations and updates when available.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** We adopted Rust for its security and are seeing a 1000x reduction in memory safety vulnerability density compared to Android's C and C++ code.
- **Affected Products:** Android system services and libraries
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Adopt Rust for Android system services and libraries to improve memory safety.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection involves hidden malicious instructions embedded in external data sources (e.g., emails, documents, calendar invites) that cause AI agents to perform unauthorized actions. Unlike direct prompt injection, the malicious content is concealed in external sources and only executed when the AI processes that data.
- **Affected Products:** Google Workspace, Gemini
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Layered defense strategy (input validation, sanitization, monitoring, prompt content classifiers, security thought reinforcement, markdown sanitization, suspicious URL redaction, end‑user security notifications).
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors exploit network edge devices such as backbone routers, provider edge (PE) routers, and customer edge (CE) routers, modifying firmware or configuration to maintain persistent, long‑term access and leveraging compromised devices to pivot within networks.
- **Affected Products:** backbone routers, provider edge (PE) routers, customer edge (CE) routers
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Apply detection tips and STIX IOCs from the advisory, monitor router configurations, segment networks, disable unused services, and apply vendor updates when available.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

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
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Russian GRU's 85th GTsSS (Unit 26165), also known as APT28
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

**Parallel AI Enrichment:**

- **Technical Details:** OS Command Injection vulnerability in Ivanti Sentry before R10.5.2, R10.6.2 and R10.7.1 allows a remote unauthenticated user to achieve root‑level remote code execution.
- **Affected Products:** Ivanti Sentry 10.5.1, 10.6.1, 10.7.0 and prior
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Exploit Available:** true (public PoC available, e.g., https://horizon3.ai/attack-research/vulnerabilities/cve-2026-10520)
- **Patch Available:** true (official patch available at https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523?language=en_US)
- **Active Exploitation:** true (active exploitation confirmed by Shadowserver as of June 10, 2026)
- **Threat Actors:** None known
- **Mitigation:** Upgrade to fixed versions (10.5.2, 10.6.2, 10.7.1) via Ivanti download portal; restrict management port (8443) from internet exposure; apply network segmentation and mTLS as recommended.
- **Vendor Advisory:** https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523?language=en_US

---

## 11. 🟠 Zero-Day — New Gaslight macOS Malware Uses Prompt Injection to Disrupt AI-Assisted Analysis

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://thehackernews.com/2026/06/new-gaslight-macos-malware-uses-prompt.html>

> A previously undocumented Rust-based macOS implant and information stealer has been found to embed a prompt injection payload designed to trick a malware analyst&#x27;s artificial intelligence (AI) tools and trick it into aborting or refusing an analysis of the artifact.

The malware has been codenamed Gaslight owing to this deceptive behavior. It&#x27;s been assessed with high confidence that the…

---

## 12. 🟠 Zero-Day — Cisco Catalyst SD-WAN Zero-Day CVE-2026-20245 Exploited to Gain Root Access

**CVE:** `CVE-2026-20245` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://thehackernews.com/2026/06/cisco-catalyst-sd-wan-zero-day-cve-2026.html>

> An unknown threat actor exploited a recently disclosed high-severity security flaw impacting Cisco Catalyst SD-WAN as a zero-day at least two months before it was publicly disclosed, according to new findings from Google-owned Mandiant.

The vulnerability, tracked as CVE-2026-20245 (CVSS score: 7.8), allows an authenticated, local attacker to execute arbitrary commands with elevated privileges

---

## 13. 🟡 High Severity — OliveTin has a Concurrent Template Parsing Race Condition which Leads to Cross-Request Command Contamination

**CVE:** `CVE-2026-48708` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-24
**Reference:** <https://github.com/advisories/GHSA-7fq5-7wr8-rjwj>

> ## Summary

OliveTin&#x27;s template engine uses a **single shared `text/template.Template` instance** (`tpl` package-level variable in `service/internal/tpl/templates.go`) across all goroutines. Every action execution calls `tpl.Parse(source)` followed by `t.Execute()` on this shared instance with no synchronization. When two or more actions execute concurrently (which is the normal case — each `…

---

## 14. 🟡 High Severity — OpenAM Pre-auth User Profile Tampering via Anonymous SOAP Authn in Liberty IDPP/Discovery Endpoints

**CVE:** `CVE-2026-45052` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-24
**Reference:** <https://github.com/advisories/GHSA-p462-xxwx-pqf4>

> ## Summary

**Description**

An Improper Authorization (CWE-285) issue in OpenAM&#x27;s Liberty Web Services SOAP receiver allows an unauthenticated remote attacker to write persistent entries into the Liberty Discovery store on any user&#x27;s LDAP entry, and into a shared root-realm Discovery branch. This impacts OpenAM Community Edition through version 16.0.6. This issue was patched in version …

---

## 15. 🟡 High Severity — OpenAM: Pre-auth RCE via Java Deserialization in WebAuthn Authenticator Storage

**CVE:** `CVE-2026-45051` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-24
**Reference:** <https://github.com/advisories/GHSA-6c99-87fr-6q7r>

> ## Summary

**Description**

A deserialization of untrusted data vulnerability (CWE-502) exists in OpenAM&#x27;s WebAuthn authentication module. Under certain conditions, this may allow an attacker to achieve arbitrary code execution in the context of the application server. This affects OpenAM Community Edition through version 16.0.6 and was patched in version 16.1.1.

This is not the default con…

---

## 16. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
