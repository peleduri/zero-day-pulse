# Zero Day Pulse

> **Generated:** 2026-06-24 14:05 UTC &nbsp;|&nbsp; **Total:** 30 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 20 &nbsp;|&nbsp; ✨ Enriched: 7

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal allowing unauthenticated attackers to read arbitrary files on the server via crafted HTTP requests.
- **Affected Products:** SimpleHelp remote support software version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept or weaponized exploit known.
- **Patch Available:** Patch released and applied within two days of reporting, per SimpleHelp advisory.
- **Active Exploitation:** Ransomware actors have exploited the vulnerability to compromise a utility billing software provider, as reported by CISA.
- **Threat Actors:** Ransomware actors
- **Mitigation:** Apply the vendor patch or upgrade SimpleHelp to a version newer than 5.5.7.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — How much cyber risk does AI create for organizations? 457 million security issues. Here’s what you can do about it.

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Tenable Security Research &nbsp;|&nbsp; **Published:** 2026-06-24
**Reference:** <https://www.tenable.com/blog/how-much-cyber-risk-does-ai-create-for-organizations-457-million-security-issues-heres-what>

> Over a 30 day period, Tenable detected 457 million AI-related security issues among 7,000-plus organizations, an average of 62,000 exposures per organization. If we didn’t already know that shadow AI was a problem, data like this makes it clear every organization needs to visualize, map, assess, and protect with a comprehensive exposure management program. Key takeaways AI tools — approved and una…

**Parallel AI Enrichment:**

- **Technical Details:** AI-related security issues arise from misconfigurations, unmanaged dependencies, shadow AI tools, and LLM misconfigurations rather than standard CVEs.
- **Affected Products:** AI tools (approved and unapproved), OpenClaw (agentic AI personal assistant), LLMs, AI workloads, cloud workloads.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit available.
- **Patch Available:** No official patch available.
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known.
- **Mitigation:** Implement a comprehensive exposure management program: visualize, map, assess, and protect AI tools; deploy automated, agentic workflows to contain and remediate exposures at machine speed.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is a technique where an attacker injects malicious instructions into data or tools consumed by an LLM, allowing the attacker to influence model behavior — potentially without any direct user input — in complex multi‑source AI applications such as Google Workspace with Gemini.
- **Affected Products:** Google Workspace (including Gemini integration)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept (PoC) or weaponized exploit reported in the provided sources.
- **Patch Available:** No official patch available; mitigation steps are described in the advisory.
- **Active Exploitation:** Confirmed active exploitation reported in the wild; sources: Forcepoint X‑Labs ("10 Indirect Prompt Injection Payloads Caught in the Wild") and SecurityWeek reporting on Google's analysis.
- **Threat Actors:** None known.
- **Mitigation:** Follow Googles continuous mitigation guidance: monitor the public web for IPI patterns, sanitize or restrict access to untrusted data sources, apply hardening and access controls for LLM tool integrations, and follow the advisory's recommended detection and response practices.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is when malicious or untrusted web content influences prompts or context provided to an LLM-based agent, causing it to perform unintended actions (e.g., navigation, form submission, data exfiltration). Chrome’s defenses limit model exposure to untrusted origins, vet planned actions via a separate Alignment Critic, and require confirmations for sensitive operations.
- **Affected Products:** Google Chrome (Agentic Browsing / Gemini AI feature)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public indirect prompt-injection payloads/PoC examples have been observed in the wild (reported Apr 22–24, 2026); sources report payload collections but not necessarily a single packaged weaponized exploit.
- **Patch Available:** Chrome implements mitigations as part of a new agentic security architecture (delivered through Chrome updates). See the Google Security Blog advisory for details.
- **Active Exploitation:** No confirmed reports of active exploitation of Chrome agentic capabilities in the cited vendor advisory; however, independent reporting observed indirect prompt-injection payloads in the wild (Forcepoint/related reporting, Apr 2026).
- **Threat Actors:** None known
- **Mitigation:** Use the latest Chrome release (which includes the new agentic security architecture: User Alignment Critic, Agent Origin Sets / origin gating, user confirmations, and real-time threat detection). Restrict use of agentic browsing on untrusted sites and require user confirmation for sensitive actions.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2025-48595: a high-severity elevation-of-privilege vulnerability in the Android Framework that allows local attackers to gain code execution and escalate privileges on Android 14+ devices.
- **Affected Products:** Android 14 (and later) devices
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) or weaponized exploit is referenced in the provided sources.
- **Patch Available:** A patch set is scheduled in the June 2026 Android Security Bulletin (security patch level 2026-06-05).
- **Active Exploitation:** Confirmed active exploitation in the wild; reported by Google in the June 2026 Android Security Bulletin and corroborated by security reporting/CISA listings.
- **Threat Actors:** None known
- **Mitigation:** Install the June 2026 Android Security Bulletin updates (security patch level 2026-06-05) as they become available; keep devices updated to the latest Android security patch level.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection involves hidden malicious instructions embedded in external data sources (e.g., emails, documents, calendar invites) that, when processed by an LLM, can cause exfiltration of data or execution of rogue actions.
- **Affected Products:** Google Gemini (Gemini 2.5 models), Google Workspace (Gemini integration), Google Gemini app
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept exploit is available.
- **Patch Available:** No official patch; mitigation provided via layered security controls and model hardening.
- **Active Exploitation:** No confirmed active exploitation in the wild has been reported.
- **Threat Actors:** None known
- **Mitigation:** Layered security approach including prompt injection content classifiers, security thought reinforcement, markdown sanitization and suspicious URL redaction, user confirmation framework, and end‑user security mitigation notifications.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** State-sponsored actors target large backbone, PE and CE routers and other network-edge devices, modify router software/configuration to maintain persistent, long-term access, and pivot through compromised devices and trusted connections into other networks.
- **Affected Products:** Backbone routers, provider edge (PE) routers, customer edge (CE) routers, network edge devices
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploitation of network-device CVEs has been observed in the wild; however, no public proof-of-concept (PoC) or vendor-supplied weaponized exploit URL is reported in the consulted sources.
- **Patch Available:** No official vendor patch or remediation guidance was reported in the reviewed sources.
- **Active Exploitation:** Yes — the advisory and multiple analyses report exploitation of network-device CVEs in the wild (see cited sources).
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** CISA’s advisory and accompanying STIX/IOCs include mitigation recommendations and detection/response guidance; operators are advised to apply CISA’s detection guidance, review supplied IOCs, monitor for indicators on edge/backbone routers, isolate and remediate compromised devices, and restrict administrative access to network-edge devices.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 10. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

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
