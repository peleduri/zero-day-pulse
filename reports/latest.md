# Zero Day Pulse

> **Generated:** 2026-06-24 08:52 UTC &nbsp;|&nbsp; **Total:** 30 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 20 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a directory traversal vulnerability that allows unauthenticated remote attackers to read arbitrary files on the server by manipulating file path inputs.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** true (http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability)
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors
- **Mitigation:** Mitigation steps unavailable
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection occurs when attacker-controlled content is incorporated into an LLM’s retrieval or prompt context, causing the model to follow malicious instructions. Attackers can place malicious instructions in web pages, comments, hidden site code or other retrievable data; examples include GeminiJack, a zero-click IPI demonstrated against Google Gemini Enterprise.
- **Affected Products:** Google Gemini Enterprise
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Implement input and output validation and sanitization, apply human oversight and controls, and follow best practices for LLM security.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) attacks inject malicious instructions into data or tools that an LLM uses to complete a user query (possibly without direct user input). Attackers can influence agentic/automated LLM behavior via poisoned external content, URLs, or tool outputs. Google’s defenses include layered controls: discovery (human and automated red‑teaming, vulnerability cataloging), synthetic attack-data generation for model retraining, deterministic defenses (user confirmation, URL sanitization, tool‑chaining policies), ML‑based retraining, and LLM prompt/system‑instruction hardening to make Gemini ignore embedded harmful commands.
- **Affected Products:** Google Workspace with Gemini
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false (continuous mitigations and defenses described; no discrete vendor 'patch' released)
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Apply defense‑in‑depth: run human and automated red‑teaming, use centralized vulnerability cataloging and synthetic-data generation to create training/validation sets, deploy deterministic protections (user confirmation, URL sanitization, tool‑chaining policies via a policy engine), retrain ML detectors, apply LLM prompt/system‑instruction hardening, and monitor/public web disclosures for new IPI patterns.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection in Chrome's agentic browsing allows malicious sites to inject crafted content that influences the LLM prompts, potentially causing unintended actions.
- **Affected Products:** Google Chrome
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Chrome's new architecture introduces input sanitization and isolation for LLM prompts, mitigating indirect prompt injection; users should keep Chrome updated and avoid untrusted sites.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability sits in the Rust-based Android Binder driver (rust_binder) and is a race condition that can corrupt memory, leading to crashes.
- **Affected Products:** Linux kernel 6.18+ (rust_binder), Android OS (kernel)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (https://www.rescana.com/post/cve-2025-68260-critical-race-condition-in-rust-based-android-binder-subsystem-affects-linux-kernel)
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known.
- **Mitigation:** Apply the official kernel patches provided by the Linux kernel.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: hidden malicious instructions embedded in external data sources (emails, documents, calendar invites, web content) cause an LLM-based assistant to follow attacker instructions or exfiltrate data. Google mitigates by model hardening (adversarial training), purpose-built ML detectors, system-level safeguards, and 'security thought reinforcement' which surrounds prompt content with targeted security instructions to keep the model focused on user-directed tasks and ignore adversarial instructions.
- **Affected Products:** Gemini (including Gemini in Google Workspace), Gemini app
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — mitigations and model hardening have been integrated into Gemini (see advisory URL).
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: adversarial training / model hardening (Gemini 2.5), purpose-built ML detectors to flag malicious instructions, system-level blocking/filtering/redaction flows, security-thought-reinforcement to steer model behavior, end-user security notifications with help links, and ongoing red-teaming and VRP collaboration. Follow the Google advisory Help Center links for configuration and user guidance.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Chinese state-sponsored actors target network infrastructure globally, gaining persistent access to routers and other devices, and pivot through compromised connections to maintain long-term control.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

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
- **Threat Actors:** Russian GRU (85th GTsSS, Unit 26165), APT-28
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 10. 🟠 Zero-Day — Algerian Man Extradited to US for Running Cybercrime Marketplaces

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://www.securityweek.com/algerian-man-extradited-to-us-for-running-cybercrime-marketplaces/>

> 26-year-old Abdellah Belmili faces up to 30 years in prison for allegedly operating the marketplaces Market0Day and Spoxy. The post Algerian Man Extradited to US for Running Cybercrime Marketplaces appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟡 High Severity — Cisco Unified CM Flaw Exploited After PoC Reveals File-Write Path to Root

**CVE:** `CVE-2026-20230` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-24
**Reference:** <https://thehackernews.com/2026/06/cisco-unified-cm-flaw-exploited-after.html>

> Threat actors have begun to exploit a recently disclosed critical security flaw impacting Cisco Unified Communications Manager (Unified CM) and Unified Communications Manager Session Management Edition (Unified CM SME).

The vulnerability, tracked as CVE-2026-20230 (CVSS score: 8.6), is a case of improper input validation for specific HTTP requests that could allow an unauthenticated, remote

---

## 12. 🟡 High Severity — Snipe-IT API Vulnerable to Cross-Tenant Accessory Injection

**CVE:** `CVE-2026-54329` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-pwpj-p52h-q484>

> ### Impact
A cross-tenant data injection vulnerability was identified in the Snipe-IT Accessories API when Full Multiple Companies Support (FMCS) is enabled. A low-privileged authenticated user belonging to one company can create an accessory record under another company by supplying a foreign company_id value in the API request body.

The issue occurs because the API create path mass-assigns requ…

---

## 13. 🟡 High Severity — Snipe-IT Vulnerable to Privilege Escalation via Missing admin Permission Check in User Creation

**CVE:** `CVE-2026-55483` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-hf68-g98v-wp9g>

> ### Impact
The `store()` method in both the web and API `UsersController` only strips the superuser permission when a non-superuser creates a user. It does not strip the admin permission. This allows any authenticated user with the `users.create` permission to create a new user with full admin privileges.

The `users.create permission`  may commonly be delegated to HR staff, department leads, or s…

---

## 14. 🟡 High Severity — Snipe-IT has Multi-Tenancy Bypass via Bulk Asset Update

**CVE:** `CVE-2026-55482` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-33g4-646g-qwmm>

> ### Impact
The `BulkAssetsController::update()` method accepts `company_id` directly from user input without calling `Company::getIdForCurrentUser()`, the standard company-scoping function used by every other controller in the codebase. A non-superadmin user can move assets across company boundaries, breaking multi-tenancy isolation.

### Patches
Patched in https://github.com/grokability/snipe-it/…

---

## 15. 🟡 High Severity — Flask-Security has an Open Redirect issue

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

## 16. 🟡 High Severity — Snipe-IT's TOTP is Brute-Forceable Due to Missing Rate Limiting on `POST /two-factor`

**CVE:** `CVE-2026-49870` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-mr8g-2mj4-pcq2>

> ### Impact
`POST /two-factor` had no rate limiting, lockout, or attempt counter. An attacker with valid credentials can submit unlimited TOTP guesses. The TOTP implementation accepts the current code plus one step on either side (`config/google2fa.php window=1`), so at any instant 3 of 1,000,000 codes are accepted.

After a correct guess the attacker holds a fully authenticated session. If the ins…

---

## 17. 🟡 High Severity — Snipe-IT Vulnerable to Privilege Escalation for self via API Permissions Assignment

**CVE:** `CVE-2026-48493` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-52fw-7fw2-fmv5>

> ### Impact
A user with only users.edit AND api permissions can send a PATCH to /api/v1/users/{their_own_id} and grant themselves any permission except admin and superuser — for example `assets.view`, `assets.create`, `reports.view`, import, etc.

### Patches
Patched in https://github.com/grokability/snipe-it/pull/19024

---

## 18. 🟡 High Severity — OHttpVersionChunkDraft: Missing Final-Chunk Enforcement Leads to Undetected Stream Truncation

**CVE:** `CVE-2026-48480` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-r6fj-869h-4f6q>

> The codec-ohttp implementation of draft-ietf-ohai-chunked-ohttp does not verify that a cryptographically-signed final chunk was received before the outer HTTP body terminates. An on-path adversary (the OHTTP relay itself, or any MITM on the relay↔gateway or relay↔client transport) can forward a prefix of a legitimate chunked-OHTTP message—cut at a non-final chunk boundary—and close the outer body …

---

## 19. 🟡 High Severity — jackson-databind: InetSocketAddress deserialization triggers eager DNS resolution (SSRF)

**CVE:** `CVE-2026-54514` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-hgj6-7826-r7m5>

> ## Summary
`JDKFromStringDeserializer` constructed `InetSocketAddress` with `new InetSocketAddress(host, port)`, which performs eager DNS name resolution for hostname inputs at deserialization time. An application that binds untrusted JSON into a type containing an `InetSocketAddress` field issues an attacker-chosen DNS query during `readValue`, before any application-level validation or connect l…

---

## 20. 🟡 High Severity — jackson-databind has a PolymorphicTypeValidator bypass via generic type parameters that allows arbitrary class instantiation

**CVE:** `CVE-2026-54512` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-j3rv-43j4-c7qm>

> `jackson-databind`&#x27;s `PolymorphicTypeValidator` (PTV) is the primary safety mechanism guarding polymorphic deserialization. When polymorphic typing is enabled and a type identifier contains generic parameters (i.e. the type ID string contains `&lt;`), `DatabindContext._resolveAndValidateGeneric()` validates **only the raw container class name** (the substring before `&lt;`) against the config…

---

## 21. 🟡 High Severity — OctoPrint has possible file exfiltration via query parameters on upload endpoints

**CVE:** `CVE-2026-54134` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-j4h9-pm27-4rfw>

> ### Impact

OctoPrint versions up until and including 1.11.7 as well as 2.0.0rc1 and 2.0.0rc2 contain a vulnerability that allows an attacker with the `FILE_UPLOAD` permission to exfiltrate files from the host that OctoPrint has read access to, by moving them into the upload folder where they then can be downloaded from. This vulnerability was already reported as [GHSA-m9jh-jf9h-x3h2/CVE-2025-4806…

---

## 22. 🟡 High Severity — AVideo has an incomplete fix of CVE-2026-33482: sanitizeFFmpegCommand still allows a single '&' (background operator), giving OS command execution at the same execAsync sh -c sink

**CVE:** `CVE-2026-55173` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-wc3f-xc32-435f>

> ### Summary

The fix for CVE-2026-33482 (GHSA-pmj8-r2j7-xg6c) is incomplete. That advisory reported that `sanitizeFFmpegCommand()` (`plugin/API/standAlone/functions.php`) failed to strip `$(...)` command substitution, allowing OS command injection at the `execAsync()` `sh -c` sink. The fix (commit `25c8ab90`) added `$`, `(`, `)`, `{`, `}`, `\n`, `\r` to the denylist character class and a `str_repl…

---

## 23. 🟡 High Severity — Gogs's Unauthenticated Jupyter Notebook (ipynb) Sanitizer allows arbitrary data: URIs leading to XSS

**CVE:** `CVE-2026-52816` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-3w28-36p9-w929>

> ## Summary

The Jupyter Notebook (ipynb) sanitizer endpoint at `POST /-/api/sanitize_ipynb` allows arbitrary `data:` URIs without proper restrictions, potentially leading to Cross-Site Scripting (XSS). The endpoint uses `bluemonday.UGCPolicy()` with `p.AllowURLSchemes(&quot;data&quot;)` which permits all data URI schemes including `data:text/html`, enabling attackers to inject malicious HTML/JavaS…

---

## 24. 🟡 High Severity — OpenAM Authenticated Privilege Escalation via Raw Token Disclosure Session RPC

**CVE:** `CVE-2026-45048` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-vvhj-w2jq-263q>

> ## Summary

Description

An insufficient authorization (CWE-285) and information exposure (CWE-200) issue in OpenAM&#x27;s session management endpoint allows a low-privileged authenticated user to retrieve active session credentials belonging to other users, including those with higher privileges. This affects OpenAM Community Edition through version 16.0.6 and was patched in version 16.1.1.

This…

---

## 25. 🟡 High Severity — Gogs has Path Traversal in organization name that results in RCE through Git hooks

**CVE:** `CVE-2026-52813` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-c39w-43gm-34h5>

> ### Summary

Organization names containing path traversal sequences (`../`) are accepted by Gogs, and repositories under them are written to paths following these path traversals. This allows storing/retrieving data for repositories at arbitrary locations on the filesystem.
By creating nested structure of Git repositories, one can overwrite the other&#x27;s `hooks` configuration to result in Remot…

---

## 26. 🟡 High Severity — Gogs: LFS dedupe path leaks private repo content across tenants

**CVE:** `CVE-2026-52812` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-6p9m-q3jp-47h4>

> Summary

Git LFS storage is content-addressed by OID alone (`&lt;LFS-root&gt;/&lt;oid[0]&gt;/&lt;oid[1]&gt;/&lt;oid&gt;`) but per-repo authorization lives in the `lfs_object` table keyed `(repo_id, oid)`. `serveUpload` skips re-uploading when the OID file already exists on disk and inserts a new `(repo_id, oid)` row pointing at it **without verifying the request body hashes to the OID being claime…

---

## 27. 🟡 High Severity — Gogs vulnerable to RCE via git rebase --exec argument injection in pull request merge

**CVE:** `CVE-2026-52806` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-qf6p-p7ww-cwr9>

> # Gogs: RCE via `git rebase --exec` Argument Injection in PR Merge

## Summary

Gogs allows authenticated users to achieve Remote Code Execution (RCE) on the server by creating a pull request with a specially crafted branch name that injects the `--exec` flag into the `git rebase` command during the &quot;Rebase before merging&quot; merge operation.

## Severity

**Critical** - CVSS 3.1 Base Score…

---

## 28. 🟡 High Severity — Gogs has a Migration Redirect Bypass that Leads to Internal Repository Theft

**CVE:** `CVE-2026-52805` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-g2f5-gjr4-qjvm>

> # Migration URL validation bypass via HTTP redirect to blocked internal endpoints

## Summary

A Server-Side Request Forgery (SSRF) vulnerability exists in the repository migration functionality. The application validates only the initially submitted URL hostname, but `git clone --mirror` follows HTTP redirects. An authenticated user can submit a public URL that redirects to a blocked internal end…

---

## 29. 🟡 High Severity — Gogs Vulnerable to Privilege Escalation via Collaboration Access Mode Validation

**CVE:** `CVE-2026-52804` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-4565-r4x7-hg8j>

> ## Summary

A repository admin collaborator can escalate their privileges to owner-level access by exploiting an off-by-one error in the `ChangeCollaborationAccessMode` function.

## Vulnerable Code

In `internal/database/repo_collaboration.go`, line 129:

```go
func (r *Repository) ChangeCollaborationAccessMode(userID int64, mode AccessMode) error {
    // Discard invalid input
    if mode &lt;= …

---

## 30. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
