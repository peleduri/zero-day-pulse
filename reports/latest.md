# Zero Day Pulse

> **Generated:** 2026-06-25 08:47 UTC &nbsp;|&nbsp; **Total:** 16 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 4 &nbsp;|&nbsp; ✨ Enriched: 5

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Directory traversal vulnerability allowing attackers to read sensitive files via path traversal.
- **Affected Products:** SimpleHelp remote support software v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit has been reported.
- **Patch Available:** A patch has been released; see vendor advisory at http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability
- **Active Exploitation:** CISA reported ransomware actors exploiting unpatched SimpleHelp Remote Monitoring and Management using CVE-2024-57727.
- **Threat Actors:** Ransomware actors
- **Mitigation:** Apply the vendor patch released for SimpleHelp 5.5.7 and earlier; if patch unavailable, restrict access and monitor.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — CISA Warns Critical Lantronix EDS5000 Flaw Is Being Actively Exploited

**CVE:** `CVE-2025-67038` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-24
**Reference:** <https://thehackernews.com/2026/06/cisa-warns-critical-lantronix-eds5000.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday warned of active exploitation of a critical security flaw impacting Lantronix EDS5000 Series devices, urging Federal Civilian Executive Branch (FCEB) agencies to apply the fixes by June 26, 2026.

The vulnerability in question is CVE-2025-67038 (CVSS score: 9.8), a code injection flaw that could result in the execution

**Parallel AI Enrichment:**

- **Technical Details:** The HTTP RPC module executes a shell command to write logs on authentication failure; the username is concatenated without sanitization, allowing OS command injection with root privileges.
- **Affected Products:** Lantronix EDS5000 (2.1.0.0R3), Lantronix EDS3000PS
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or exploit known.
- **Patch Available:** No official vendor patch available.
- **Active Exploitation:** CISA has reported active exploitation in the wild.
- **Threat Actors:** None known
- **Mitigation:** Apply mitigations per CISA BOD 26-04 guidance, restrict network exposure, monitor logs, and follow vendor instructions when available.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — How much cyber risk does AI create for organizations? 457 million security issues. Here’s what you can do about it.

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Tenable Security Research &nbsp;|&nbsp; **Published:** 2026-06-24
**Reference:** <https://www.tenable.com/blog/how-much-cyber-risk-does-ai-create-for-organizations-457-million-security-issues-heres-what>

> Over a 30 day period, Tenable detected 457 million AI-related security issues among 7,000-plus organizations, an average of 62,000 exposures per organization. If we didn’t already know that shadow AI was a problem, data like this makes it clear every organization needs to visualize, map, assess, and protect with a comprehensive exposure management program. Key takeaways AI tools — approved and una…

**Parallel AI Enrichment:**

- **Technical Details:** Tenable attributes the AI-related security issues to misconfigurations, unmanaged model dependencies, exposed credentials, unapproved (shadow) AI tools, identity flaws, and excessive permissions across IT, cloud, OT, AI, IoT environments. These non-CVE findings create attack paths to critical assets and accounted for the majority of breach entry points in Tenable telemetry.
- **Affected Products:** AI tools (approved and unapproved), OpenClaw AI assistant
- **CVSS Score:** 1e-11
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public proof-of-concept or weaponized exploit reported in the Tenable blog
- **Patch Available:** No vendor patch—issues are primarily misconfigurations/unmanaged dependencies (not a patchable CVE)
- **Active Exploitation:** No confirmed active exploitation reported in the Tenable blog
- **Threat Actors:** None known
- **Mitigation:** Adopt AI-driven exposure management: continuous asset discovery (including shadow AI), map attack paths, prioritize exposures contextually, use automated/orchestrated remediation and agentic AI workflows with guardrails and human oversight, enforce approved AI tooling, and patch known CVEs for traditional software issues.
- **Vendor Advisory:** https://www.tenable.com/blog/how-much-cyber-risk-does-ai-create-for-organizations-457-million-security-issues-heres-what

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: attacker-controlled content on a webpage inserts prompts or instructions that the agentic LLM reads and follows, causing the model to execute or disclose actions/information it shouldn’t.
- **Affected Products:** Google Chrome (agentic browsing feature), Gemini AI integrated in Chrome
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) or weaponized exploit is reported in the examined sources.
- **Patch Available:** Google/Chrome announced a new security architecture for agentic browsing that mitigates indirect prompt injection risks (see vendor advisory URL).
- **Active Exploitation:** Indirect prompt injection payloads have been observed on the public web (multiple payloads detected), indicating active exploitation attempts or probes in the wild.
- **Threat Actors:** None known
- **Mitigation:** Implement input and output validation and sanitization, and apply human oversight and controls for LLM-driven features.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability involves exploitation of CVEs in network devices such as backbone, provider edge, and customer edge routers, allowing attackers to gain persistent access and pivot to other networks.
- **Affected Products:** Backbone routers, provider edge (PE) routers, customer edge (CE) routers
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit known.
- **Patch Available:** No official patch has been released; no patch or remediation guidance is currently available from the vendor.
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 11. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

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
