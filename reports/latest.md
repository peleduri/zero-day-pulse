# Zero Day Pulse

> **Generated:** 2026-06-25 02:05 UTC &nbsp;|&nbsp; **Total:** 17 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 5 &nbsp;|&nbsp; ✨ Enriched: 3

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path‑traversal vulnerability that lets unauthenticated attackers send crafted HTTP requests to SimpleHelp remote support software (v5.5.7 and earlier) to read arbitrary files, including configuration files with hashed passwords.
- **Affected Products:** SimpleHelp remote support software v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Public proof‑of‑concept code is available on GitHub: https://github.com/imjdl/CVE-2024-57727
- **Patch Available:** Patch released in SimpleHelp version 5.5.8 (and later). See SimpleHelp release notes https://simple-help.com/release-news for details.
- **Active Exploitation:** Confirmed active exploitation reported by CISA and ransomware actors leveraging unpatched SimpleHelp RMM instances.
- **Threat Actors:** Ransomware actors (unspecified groups) have exploited this vulnerability in the wild.
- **Mitigation:** Apply the SimpleHelp 5.5.8 patch or later. If patch cannot be applied immediately, restrict external network access to the SimpleHelp server, enforce strong authentication, and disable unauthenticated remote file downloads.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — CISA Warns Critical Lantronix EDS5000 Flaw Is Being Actively Exploited

**CVE:** `CVE-2025-67038` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-24
**Reference:** <https://thehackernews.com/2026/06/cisa-warns-critical-lantronix-eds5000.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday warned of active exploitation of a critical security flaw impacting Lantronix EDS5000 Series devices, urging Federal Civilian Executive Branch (FCEB) agencies to apply the fixes by June 26, 2026.

The vulnerability in question is CVE-2025-67038 (CVSS score: 9.8), a code injection flaw that could result in the execution

**Parallel AI Enrichment:**

- **Technical Details:** The HTTP RPC module concatenates the username with a shell command without sanitization, allowing attackers to inject arbitrary OS commands via the username parameter, which are executed with root privileges.
- **Affected Products:** Lantronix EDS5000 (2.1.0.0R3)
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit known.
- **Patch Available:** No official patch available yet; apply mitigations per vendor instructions.
- **Active Exploitation:** CISA has warned that CVE-2025-67038 is actively exploited in the wild.
- **Threat Actors:** None known
- **Mitigation:** Apply vendor-recommended mitigations: minimize network exposure, restrict internet access, use firewalls/VPNs, and follow CISA defensive measures.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — How much cyber risk does AI create for organizations? 457 million security issues. Here’s what you can do about it.

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Tenable Security Research &nbsp;|&nbsp; **Published:** 2026-06-24
**Reference:** <https://www.tenable.com/blog/how-much-cyber-risk-does-ai-create-for-organizations-457-million-security-issues-heres-what>

> Over a 30 day period, Tenable detected 457 million AI-related security issues among 7,000-plus organizations, an average of 62,000 exposures per organization. If we didn’t already know that shadow AI was a problem, data like this makes it clear every organization needs to visualize, map, assess, and protect with a comprehensive exposure management program. Key takeaways AI tools — approved and una…

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

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI): adversary injects malicious instructions into data or tools used by an LLM (including via external content or agentic tool workflows) so the model follows those injected instructions instead of the user's intent.
- **Affected Products:** Google Workspace with Gemini
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) or weaponized exploit is referenced in the advisory or extracted blog post.
- **Patch Available:** No single 'patch' is described; Google describes continuous mitigations including configuration updates, deterministic defenses (regex takedowns, URL sanitization, user confirmation), ML/LLM model retraining and model hardening (see advisory).
- **Active Exploitation:** The advisory states Google monitors publicly disclosed IPI attacks and uses open-source intelligence feeds, but it does not report confirmed active exploitation specifically affecting Workspace with Gemini in the blog post.
- **Threat Actors:** None known
- **Mitigation:** Defense-in-depth: deterministic defenses (user confirmation, URL sanitization, tool-chaining policies, regex takedowns via a centralized Policy Engine), ML-based defenses (synthetic-data-driven retraining and validation), LLM-based defenses and prompt-engineering, and model hardening of Gemini to better detect and ignore injected instructions. Google also uses human and automated red-teaming and an AI VRP to discover and remediate IPI vectors.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

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

## 12. 🟠 Zero-Day — Mandiant reveals how Cisco SD-WAN zero-day attacks gained root access

**CVE:** `CVE-2026-20245` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-24
**Reference:** <https://www.bleepingcomputer.com/news/security/mandiant-reveals-how-cisco-sd-wan-zero-day-attacks-gained-root-access/>

> New details have been revealed on how hackers exploited a Cisco Catalyst SD-WAN vulnerability tracked as CVE-2026-20245 in zero-day attacks to create rogue root accounts on targeted devices. [...]

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

## 16. 🟡 High Severity — Cisco Unified CM Flaw Exploited After PoC Reveals File-Write Path to Root

**CVE:** `CVE-2026-20230` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-24
**Reference:** <https://thehackernews.com/2026/06/cisco-unified-cm-flaw-exploited-after.html>

> Threat actors have begun to exploit a recently disclosed critical security flaw impacting Cisco Unified Communications Manager (Unified CM) and Unified Communications Manager Session Management Edition (Unified CM SME).

The vulnerability, tracked as CVE-2026-20230 (CVSS score: 8.6), is a case of improper input validation for specific HTTP requests that could allow an unauthenticated, remote

---

## 17. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
