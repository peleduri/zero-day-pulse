# Zero Day Pulse

> **Generated:** 2026-06-24 19:26 UTC &nbsp;|&nbsp; **Total:** 25 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 11 &nbsp;|&nbsp; 🟡 High: 14 &nbsp;|&nbsp; ✨ Enriched: 9

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a directory traversal vulnerability that allows unauthenticated remote attackers to read arbitrary files on affected SimpleHelp remote support software (v5.5.7 and earlier) by manipulating file path parameters.
- **Affected Products:** SimpleHelp remote support software v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability)
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors
- **Mitigation:** Apply the vendor patch (upgrade to a version newer than 5.5.7) and ensure systems are updated promptly.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — CISA Warns Critical Lantronix EDS5000 Flaw Is Being Actively Exploited

**CVE:** `CVE-2025-67038` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-24
**Reference:** <https://thehackernews.com/2026/06/cisa-warns-critical-lantronix-eds5000.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday warned of active exploitation of a critical security flaw impacting Lantronix EDS5000 Series devices, urging Federal Civilian Executive Branch (FCEB) agencies to apply the fixes by June 26, 2026.

The vulnerability in question is CVE-2025-67038 (CVSS score: 9.8), a code injection flaw that could result in the execution

---

## 3. 🟠 Zero-Day — How much cyber risk does AI create for organizations? 457 million security issues. Here’s what you can do about it.

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Tenable Security Research &nbsp;|&nbsp; **Published:** 2026-06-24
**Reference:** <https://www.tenable.com/blog/how-much-cyber-risk-does-ai-create-for-organizations-457-million-security-issues-heres-what>

> Over a 30 day period, Tenable detected 457 million AI-related security issues among 7,000-plus organizations, an average of 62,000 exposures per organization. If we didn’t already know that shadow AI was a problem, data like this makes it clear every organization needs to visualize, map, assess, and protect with a comprehensive exposure management program. Key takeaways AI tools — approved and una…

**Parallel AI Enrichment:**

- **Technical Details:** AI tools — approved and unapproved — are driving a massive wave of daily exposures, primarily tied to misconfigurations and unmanaged dependencies rather than standard CVEs.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Implement a comprehensive exposure management program that visualizes, maps, assesses, and protects against AI-related security exposures.
- **Vendor Advisory:** https://www.tenable.com/blog/how-much-cyber-risk-does-ai-create-for-organizations-457-million-security-issues-heres-what

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when malicious payloads are placed on publicly accessible web pages; AI agents that retrieve and process external content incorporate the payload into their prompt, causing them to execute unintended instructions. This can happen without user interaction (zero‑click), as demonstrated by the GeminiJack vulnerability in Google Gemini Enterprise, and can be chained with hidden website code to affect assistants such as GitHub Copilot.
- **Affected Products:** Google Gemini Enterprise, Microsoft Copilot Studio, MS-Agent, EmailGPT, Claude.ai, GitHub Copilot
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Monitor the public web for known IPI patterns, restrict LLMs from unrestricted web browsing, apply input sanitization and safe completion constraints, and keep AI systems updated with the latest security controls.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) enables attackers to embed malicious instructions inside data or tools consumed by an LLM, influencing model behavior even without direct user input. Google describes defenses including continuous discovery (human and automated red‑teaming, AI Vulnerability Rewards Program), synthetic data generation to expand attack variants, deterministic defenses (user confirmation, URL sanitization, tool‑chaining policies governed by a policy engine), ML‑based defenses (retraining on generated variants), LLM‑based defenses (prompt engineering), and Gemini model hardening to better identify and ignore harmful embedded commands.
- **Affected Products:** Google Workspace (Gemini)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Use continuous detection (human red‑team, automated red‑team, VRP) and centralized vulnerability cataloging; generate synthetic attack variants for ML retraining and LLM prompt‑engineering; apply deterministic controls (user confirmation, URL sanitization, tool‑chaining policies) via a policy engine; and apply Gemini model hardening to reduce susceptibility to embedded malicious instructions.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is a threat where a malicious site injects prompts that manipulate the AI model's behavior, potentially causing unintended actions. An attacker can trigger this vulnerability when chained with indirect prompt injection, as described in the security advisory.
- **Affected Products:** Google Chrome (with Gemini agentic browsing)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Deploy the new architecture announced by Google engineer Nathan Parker that mitigates indirect prompt injection risks in agentic browsing.
- **Vendor Advisory:** http://blog.google/security/architecting-security-for-agentic

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** An elevation-of-privilege vulnerability in the Android Framework (CVE-2025-48595) that can allow local attackers to gain code execution or elevated system privileges on affected devices with no user interaction required.
- **Affected Products:** Android Framework on devices running Android 14 and later
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (public reports of active exploitation exist; no public PoC URL provided in supplied corpus)
- **Patch Available:** true (Google published a June 2026 Android Security Bulletin and scheduled patch set / AOSP source patches)
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Install the June 2026 Android security update / apply the vendor patches released in the June 2026 Android Security Bulletin; apply the corresponding AOSP source patches when available.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2026/2026-06-01

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection involves embedding hidden malicious instructions in external data sources such as websites, emails, or documents that an AI system later processes, causing the model to follow the attacker’s commands instead of the user’s intended input.
- **Affected Products:** Google Gemini, Google Workspace (Docs, Gmail, Calendar)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Google recommends a layered defense strategy including input validation and sanitization, context‑aware filtering, restricting LLM access to untrusted data, continuous monitoring for suspicious patterns, and user confirmation prompts; additionally, hardening Gemini and applying security safeguards are advised.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability exploits CVEs in network-device firmware, allowing attackers to compromise backbone, provider edge, and customer edge routers, gain persistent access, and pivot to other networks.
- **Affected Products:** backbone routers, provider edge (PE) routers, customer edge (CE) routers
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Mitigation steps unavailable.
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
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th GTsSS (Unit 26165) — tracked as APT28
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 12. 🟡 High Severity — OliveTin has a Concurrent Template Parsing Race Condition which Leads to Cross-Request Command Contamination

**CVE:** `CVE-2026-48708` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-24
**Reference:** <https://github.com/advisories/GHSA-7fq5-7wr8-rjwj>

> ## Summary

OliveTin&#x27;s template engine uses a **single shared `text/template.Template` instance** (`tpl` package-level variable in `service/internal/tpl/templates.go`) across all goroutines. Every action execution calls `tpl.Parse(source)` followed by `t.Execute()` on this shared instance with no synchronization. When two or more actions execute concurrently (which is the normal case — each `…

---

## 13. 🟡 High Severity — OpenAM Pre-auth User Profile Tampering via Anonymous SOAP Authn in Liberty IDPP/Discovery Endpoints

**CVE:** `CVE-2026-45052` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-24
**Reference:** <https://github.com/advisories/GHSA-p462-xxwx-pqf4>

> ## Summary

**Description**

An Improper Authorization (CWE-285) issue in OpenAM&#x27;s Liberty Web Services SOAP receiver allows an unauthenticated remote attacker to write persistent entries into the Liberty Discovery store on any user&#x27;s LDAP entry, and into a shared root-realm Discovery branch. This impacts OpenAM Community Edition through version 16.0.6. This issue was patched in version …

---

## 14. 🟡 High Severity — OpenAM: Pre-auth RCE via Java Deserialization in WebAuthn Authenticator Storage

**CVE:** `CVE-2026-45051` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-24
**Reference:** <https://github.com/advisories/GHSA-6c99-87fr-6q7r>

> ## Summary

**Description**

A deserialization of untrusted data vulnerability (CWE-502) exists in OpenAM&#x27;s WebAuthn authentication module. Under certain conditions, this may allow an attacker to achieve arbitrary code execution in the context of the application server. This affects OpenAM Community Edition through version 16.0.6 and was patched in version 16.1.1.

This is not the default con…

---

## 15. 🟡 High Severity — Cisco Unified CM Flaw Exploited After PoC Reveals File-Write Path to Root

**CVE:** `CVE-2026-20230` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-24
**Reference:** <https://thehackernews.com/2026/06/cisco-unified-cm-flaw-exploited-after.html>

> Threat actors have begun to exploit a recently disclosed critical security flaw impacting Cisco Unified Communications Manager (Unified CM) and Unified Communications Manager Session Management Edition (Unified CM SME).

The vulnerability, tracked as CVE-2026-20230 (CVSS score: 8.6), is a case of improper input validation for specific HTTP requests that could allow an unauthenticated, remote

---

## 16. 🟡 High Severity — Snipe-IT API Vulnerable to Cross-Tenant Accessory Injection

**CVE:** `CVE-2026-54329` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-pwpj-p52h-q484>

> ### Impact
A cross-tenant data injection vulnerability was identified in the Snipe-IT Accessories API when Full Multiple Companies Support (FMCS) is enabled. A low-privileged authenticated user belonging to one company can create an accessory record under another company by supplying a foreign company_id value in the API request body.

The issue occurs because the API create path mass-assigns requ…

---

## 17. 🟡 High Severity — Snipe-IT Vulnerable to Privilege Escalation via Missing admin Permission Check in User Creation

**CVE:** `CVE-2026-55483` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-hf68-g98v-wp9g>

> ### Impact
The `store()` method in both the web and API `UsersController` only strips the superuser permission when a non-superuser creates a user. It does not strip the admin permission. This allows any authenticated user with the `users.create` permission to create a new user with full admin privileges.

The `users.create permission`  may commonly be delegated to HR staff, department leads, or s…

---

## 18. 🟡 High Severity — Snipe-IT has Multi-Tenancy Bypass via Bulk Asset Update

**CVE:** `CVE-2026-55482` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-33g4-646g-qwmm>

> ### Impact
The `BulkAssetsController::update()` method accepts `company_id` directly from user input without calling `Company::getIdForCurrentUser()`, the standard company-scoping function used by every other controller in the codebase. A non-superadmin user can move assets across company boundaries, breaking multi-tenancy isolation.

### Patches
Patched in https://github.com/grokability/snipe-it/…

---

## 19. 🟡 High Severity — Flask-Security has an Open Redirect issue

**CVE:** `CVE-2023-49438` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-w2j7-f3c6-g8cw>

> # Open Redirect in Flask-Security

## Summary

`flask_security.utils.validate_redirect_url()` can allow an attacker-controlled redirect URL when subdomain redirects are enabled.

The bypass uses a backslash inside the URL authority/host:

```text
http://evil.com\.whitelist.com
http://evil.com%5C.whitelist.com
```

Python&#x27;s `urlsplit()` parses the full authority as `evil.com\.whitelist.com` or…

---

## 20. 🟡 High Severity — Snipe-IT's TOTP is Brute-Forceable Due to Missing Rate Limiting on `POST /two-factor`

**CVE:** `CVE-2026-49870` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-mr8g-2mj4-pcq2>

> ### Impact
`POST /two-factor` had no rate limiting, lockout, or attempt counter. An attacker with valid credentials can submit unlimited TOTP guesses. The TOTP implementation accepts the current code plus one step on either side (`config/google2fa.php window=1`), so at any instant 3 of 1,000,000 codes are accepted.

After a correct guess the attacker holds a fully authenticated session. If the ins…

---

## 21. 🟡 High Severity — Snipe-IT Vulnerable to Privilege Escalation for self via API Permissions Assignment

**CVE:** `CVE-2026-48493` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-52fw-7fw2-fmv5>

> ### Impact
A user with only users.edit AND api permissions can send a PATCH to /api/v1/users/{their_own_id} and grant themselves any permission except admin and superuser — for example `assets.view`, `assets.create`, `reports.view`, import, etc.

### Patches
Patched in https://github.com/grokability/snipe-it/pull/19024

---

## 22. 🟡 High Severity — OHttpVersionChunkDraft: Missing Final-Chunk Enforcement Leads to Undetected Stream Truncation

**CVE:** `CVE-2026-48480` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-r6fj-869h-4f6q>

> The codec-ohttp implementation of draft-ietf-ohai-chunked-ohttp does not verify that a cryptographically-signed final chunk was received before the outer HTTP body terminates. An on-path adversary (the OHTTP relay itself, or any MITM on the relay↔gateway or relay↔client transport) can forward a prefix of a legitimate chunked-OHTTP message—cut at a non-final chunk boundary—and close the outer body …

---

## 23. 🟡 High Severity — jackson-databind: InetSocketAddress deserialization triggers eager DNS resolution (SSRF)

**CVE:** `CVE-2026-54514` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-hgj6-7826-r7m5>

> ## Summary
`JDKFromStringDeserializer` constructed `InetSocketAddress` with `new InetSocketAddress(host, port)`, which performs eager DNS name resolution for hostname inputs at deserialization time. An application that binds untrusted JSON into a type containing an `InetSocketAddress` field issues an attacker-chosen DNS query during `readValue`, before any application-level validation or connect l…

---

## 24. 🟡 High Severity — jackson-databind has a PolymorphicTypeValidator bypass via generic type parameters that allows arbitrary class instantiation

**CVE:** `CVE-2026-54512` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-j3rv-43j4-c7qm>

> `jackson-databind`&#x27;s `PolymorphicTypeValidator` (PTV) is the primary safety mechanism guarding polymorphic deserialization. When polymorphic typing is enabled and a type identifier contains generic parameters (i.e. the type ID string contains `&lt;`), `DatabindContext._resolveAndValidateGeneric()` validates **only the raw container class name** (the substring before `&lt;`) against the config…

---

## 25. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
