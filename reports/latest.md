# Zero Day Pulse

> **Generated:** 2026-06-12 19:53 UTC &nbsp;|&nbsp; **Total:** 35 &nbsp;|&nbsp; 🔴 KEV: 1 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 20 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🔴 CISA KEV — CVE-2026-35273 — Oracle PeopleSoft Enterprise PeopleTools Missing Authentication for Critical Function Vulnerability

**CVE:** `CVE-2026-35273` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-35273>

> Vendor: Oracle | Product:  PeopleSoft Enterprise PeopleTools. Oracle PeopleSoft Enterprise PeopleTools contains a missing authentication for critical function vulnerability which could allow an unauthenticated attacker to obtain takeover of PeopleSoft Enterprise PeopleTools. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Priorit…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is a server‑side request forgery (CWE‑918) in the Updates Environment Management component, allowing unauthenticated remote attackers to trigger arbitrary HTTP requests and potentially achieve remote code execution.
- **Affected Products:** PeopleSoft Enterprise PeopleTools (versions 8.61, 8.62)
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** ShinyHunters
- **Mitigation:** Apply Oracle’s out‑of‑band patch immediately; if the patch cannot be applied, restrict network access to PeopleSoft HTTP interfaces, deploy WAF rules, and disable or limit access to the Updates Environment Management component.
- **Vendor Advisory:** https://www.oracle.com/security-alerts/alert-cve-2026-35273.html

---

## 2. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal (directory traversal) vulnerability allowing attackers to read sensitive files by specifying crafted path sequences; impacts SimpleHelp RMM web interface leading to disclosure of files accessible to the service.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true — https://offsec.com/blog/cve-2024-57727
- **Patch Available:** true — http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability
- **Active Exploitation:** true — https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a
- **Threat Actors:** Ransomware actors (unspecified groups)
- **Mitigation:** Update SimpleHelp to fixed version (apply vendor patch). If patch cannot be applied, isolate/unexpose SimpleHelp RMM from untrusted networks, restrict access via firewall/ACLs, rotate credentials and secrets stored on affected hosts, and monitor for suspicious access/logs. Follow CISA advisory recommendations.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 3. 🟠 Zero-Day — Active Exploitation of Oracle PeopleSoft Zero-Day (CVE-2026-35273)

**CVE:** `CVE-2026-35273` | `CVE-2013-3821` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://www.rapid7.com/blog/post/etr-active-exploitation-of-oracle-peoplesoft-zero-day-cve-2026-35273>

> Overview On June 10, 2026, Oracle published a security alert for CVE-2026-35273 , a critical vulnerability in the Updates Environment Management component of PeopleSoft Enterprise PeopleTools. Oracle released an out-of-band patch the same day as the advisory, underscoring the urgency of remediation. The vulnerability has a CVSSv3.1 score of 9.8 and is remotely exploitable without authentication. P…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is a server‑side request forgery (CWE‑918) in the Updates Environment Management component, allowing unauthenticated remote attackers to trigger arbitrary HTTP requests and potentially achieve remote code execution.
- **Affected Products:** PeopleSoft Enterprise PeopleTools (versions 8.61, 8.62)
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** ShinyHunters
- **Mitigation:** Apply Oracle’s out‑of‑band patch immediately; if the patch cannot be applied, restrict network access to PeopleSoft HTTP interfaces, deploy WAF rules, and disable or limit access to the Updates Environment Management component.
- **Vendor Advisory:** https://www.oracle.com/security-alerts/alert-cve-2026-35273.html

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when AI systems process external content (webpages, emails, documents) that contains malicious instructions; when retrieved by models or RAG/agent systems, the model may follow those instructions. Google observed categories such as benign guidance, SEO manipulation, resource‑wasting, low‑sophistication exfiltration, and destructive instructions. Chaining IPI with other flaws (e.g., the Cursor code‑editor allowlist bypass, CVE‑2025‑54131) can enable command execution.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known.
- **Mitigation:** Layered defenses — filter and coarse‑to‑fine detection for IPI, RAG tool hardening, retrieval hygiene, limit autonomous agent web access, model‑level instruction controls, continuous monitoring, and participation in vulnerability reward programs.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when malicious instructions are embedded in data sources (emails, documents, calendar invites) that complex AI systems (like Gemini in Workspace) ingest during query processing or agentic actions; these instructions can steer model behavior or cause data exfiltration without user interaction (zero‑click). The GeminiJack case used crafted Workspace artifacts to inject instructions that influenced Gemini Enterprise and could leak corporate data.
- **Affected Products:** Google Workspace with Gemini integration, Gemini Enterprise
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Implement continuous, layered defenses: input sanitization, content provenance filters, model instruction‑robustness training, strict isolation of tools/data sources, enforce permission and data‑access controls for agentic actions, and deploy telemetry with anomaly detection. Follow the vendor advisory for detailed configuration guidance.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (content poisoning) in RAG pipelines: an attacker embeds hidden instructions in a shared Google Doc, Calendar event, or Gmail message. When the retrieval component of Gemini Enterprise or Vertex AI Search pulls the poisoned content, the instruction is treated as legitimate by the model, causing it to execute actions such as cross‑datasource searches and exfiltration via external image URLs. The vulnerability can be chained with CVE‑2025‑54131 (Cursor auto‑run allowlist bypass) to achieve command execution.
- **Affected Products:** Google Gemini Enterprise (agentic browsing / RAG integrations), Vertex AI Search, Chrome agentic browsing features
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true - http://blog.google/security/architecting-security-for-agentic.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Google deployed architectural mitigations (layered defenses, restricted origin access, separation of Vertex AI Search from Gemini Enterprise, second‑agent oversight in Chrome). Recommended hardening: restrict AI access scopes, treat user‑contributed content as untrusted (sanitize/rewrite retrieved content), disable automatic execution/auto‑run allowlists, monitor outbound requests from AI outputs, enforce strong RAG boundary checks and retrieval filtering.
- **Vendor Advisory:** http://blog.google/security/architecting-security-for-agentic.html

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A near‑miss linear buffer overflow in the CrabbyAVIF Rust library (unsafe Rust code path) was identified and fixed pre‑release; Scudo hardened allocator prevented exploitation by placing guard pages around secondary allocations and converting silent corruption into a crash.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050 and https://source.android.com/docs/security/bulletin/2025-08-01
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use Scudo hardened allocator; apply the published patch; improve unsafe Rust review and training (encapsulate unsafe, safety comments, follow best practices).
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** An indirect prompt injection (zero‑click) where malicious instructions hidden in external data are processed by Google Gemini Enterprise, allowing an attacker to trigger arbitrary actions when the prompts are evaluated.
- **Affected Products:** Google Gemini Enterprise (versions prior to 1.3)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (source: http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability)
- **Patch Available:** true (source: http://nvd.nist.gov/vuln/detail/CVE-2025-54131)
- **Active Exploitation:** true (source: http://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads)
- **Threat Actors:** None known
- **Mitigation:** Implement a layered security approach: validate and sanitize external data sources, enforce strict prompt‑execution controls, monitor for anomalous prompt behavior, and apply continuous threat analysis throughout the AI pipeline.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors compromise routers by exploiting known software vulnerabilities or misconfigurations, then modify firmware or configuration to maintain long‑term persistence and use the compromised devices to pivot within target networks.
- **Affected Products:** Backbone routers, Provider Edge (PE) routers, Customer Edge (CE) routers (e.g., Cisco telecom routers)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Apply all available firmware and software updates to routers, disable unnecessary services, enforce strong authentication, segment network zones, and monitor for anomalous routing changes.
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
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS), military unit 26165 (aka APT28).
- **Mitigation:** Refer to the joint CISA/FBI advisory for recommended mitigations and hardening guidance (vendor-specific mitigations not provided).
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

---

## 12. 🟠 Zero-Day — Factoring "short-sleeve" RSA keys with polynomials

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Trail of Bits Blog &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://blog.trailofbits.com/2026/06/12/factoring-short-sleeve-rsa-keys-with-polynomials/>

> What happens when the bits of an RSA private key are heavily biased toward 0 instead of being randomly generated? The public key’s bits could be biased enough for us to detect these incorrectly generated keys in the wild. Together with Hanno Böck of the badkeys project, we found hundreds of unique keys that not only have this property, but can be quickly factored. We also found the bug that led to…

---

## 13. 🟠 Zero-Day — Anthropic Disputes Fable 5 AI Jailbreak

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://www.securityweek.com/anthropic-disputes-fable-5-ai-jailbreak/>

> An AI hacker claims to have achieved a prompt-based jailbreak shortly after Fable 5’s launch, but Anthropic says it’s not a real jailbreak. The post Anthropic Disputes Fable 5 AI Jailbreak appeared first on SecurityWeek .

---

## 14. 🟠 Zero-Day — CISA orders feds to patch actively exploited Ivanti flaw by Sunday

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-gives-feds-3-days-to-patch-ivanti-flaw-exploited-in-attacks/>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) ordered government agencies to patch an actively exploited Ivanti Sentry flaw within three days, as mandated by the newly issued Binding Operational Directive (BOD) 26-04. [...]

---

## 15. 🟠 Zero-Day — ShinyHunters Exploits Oracle PeopleSoft Zero-Day (CVE-2026-35273) to Breach Universities

**CVE:** `CVE-2026-35273` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://thehackernews.com/2026/06/shinyhunters-exploits-oracle-peoplesoft.html>

> The ShinyHunters extortion crew exploited an unpatched flaw in Oracle PeopleSoft to break into enterprise systems, steal data, and demand payment to keep it private. The campaign hit universities hardest.

Google&#x27;s Mandiant attributes it to the group it tracks as UNC6240, and dates the activity between May 27 and June 9. Oracle did not publish its advisory until June 10, so the bug was a

---

## 16. 🟡 High Severity — TYPO3 CMS has Privilege Escalation & SQL Injection in its Form Framework

**CVE:** `CVE-2026-49741` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-jh32-v29g-68pq>

> ### Problem
Backend users with write access to the `form_definition` database table were able to directly create, update, or delete form definition records via `DataHandler`, bypassing the Form Framework&#x27;s persistence validation and permission checks. This allowed injecting arbitrary form configurations, re-enabling attack vectors originally addressed in [TYPO3-CORE-SA-2018-003](https://typo3…

---

## 17. 🟡 High Severity — TYPO3 CMS has Insecure Deserialization via Core API

**CVE:** `CVE-2026-49740` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-c78m-c52x-jgwp>

> ### Problem
TYPO3&#x27;s cache frontend (`VariableFrontend`) and persistent key-value store (`Registry`) deserialized PHP payloads without integrity validation or class restrictions. An attacker with write access to the underlying storage backend (cache store or sys_registry database table) could inject a crafted serialized payload to trigger PHP Object Injection, potentially exploiting a gadget c…

---

## 18. 🟡 High Severity — TYPO3 CMS has Broken Access Control in its File Abstraction Layer

**CVE:** `CVE-2026-49738` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-jf56-v8jc-jcc5>

> ### Problem
The path allowance check in `GeneralUtility::isAllowedAbsPath()` performed a plain string prefix comparison without requiring a directory separator boundary, causing a path like `/var/www/html-other/secret.yaml` to be incorrectly accepted as valid when the project root was `/var/www/html`. Administrator users with access to the File Abstraction Layer were able to create new file storag…

---

## 19. 🟡 High Severity — gorest InMemorySecret2FA race condition allows process crash via concurrent map access (CWE-362)

**CVE:** `CVE-2026-48154` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-cpwg-x64r-rgwg>

> ## Vulnerability: CWE-362 — Concurrent Map Access Race Condition in InMemorySecret2FA

**CWE:** CWE-362 (Concurrent Execution using Shared Resource with Improper Synchronization)

### Affected Component
- `github.com/pilinux/gorest` — Go REST API boilerplate
- InMemorySecret2FA — in-memory 2FA secret store

### Vulnerability Locations

| File | Line | Role |
|------|------|------|
| `database/mode…

---

## 20. 🟡 High Severity — Budibase: Basic app users can exfiltrate stored REST datasource auth by rewriting datasource base URL

**CVE:** `CVE-2026-48152` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-3gp5-q4jw-3v94>

> ### Summary
Budibase stores external REST datasource credentials server-side and documents that database credentials are applied server-side and are not exposed in the UI. The REST datasource implementation redacts stored Basic/Bearer/OAuth2 auth secrets before returning datasource data to clients. However, the single-datasource `GET` and `PUT` routes are guarded by generic `TABLE READ`, not by Bu…

---

## 21. 🟡 High Severity — Budibase: Workspace-scoped builder escalates to global admin via /api/public/v1/roles/assign

**CVE:** `CVE-2026-48150` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-6xp4-cf37-ppjh>

> ## Summary

`/api/public/v1/roles/assign` is guarded by the `builderOrAdmin` middleware, which passes any user who is a builder for the app id in the `x-budibase-app-id` header. That check admits both global builders and workspace-scoped builders (`builder.apps` set but `builder.global` unset). The controller then spreads the request body into the SDK call, and the SDK grants `builder.global=true`…

---

## 22. 🟡 High Severity — Budibase: Unvalidated VectorDB Host Parameter Enables SSRF

**CVE:** `CVE-2026-48148` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-cv96-5348-p5p8>

> ### Summary

The VectorDB configuration endpoint in Budibase accepts a host parameter that undergoes no validation against internal IP ranges, reserved hostnames, or URL schemes. Any authenticated user with builder-level access can supply an arbitrary host value such as `169.254.169.254` or localhost, causing the server to initiate outbound TCP connections to internal network addresses or cloud me…

---

## 23. 🟡 High Severity — GeoServer has a Server-Side Request Forgery (SSRF) Vulnerability in its XML Entity Resolution

**CVE:** `CVE-2025-58175` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-x4r9-gmw3-hxww>

> ### Summary
A GeoServer that uses `ENTITY_RESOLUTION_ALLOWLIST` may allow attacker to perform unauthenticated Server-Side Request Forgery (SSRF).

### Details
This vulnerability requires that GeoServer is set up to use a proxy base URL and the `ENTITY_RESOLUTION_ALLOWLIST` (default since 2.25.0):

### Impact
This vulnerability allows an attacker to cause GeoServer to make requests to an unintended…

---

## 24. 🟡 High Severity — GeoServer has an arbitrary file write vulnerability in its Master Password Dump Page

**CVE:** `CVE-2025-52465` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-7qmg-grcp-qf25>

> ### Summary
A vulnerability exists that allows an authenticated administrator with access to GeoServer&#x27;s security system to pass arbitrary file names to the Master Password Dump web page and create files containing the master password in plaintext. The provided file name must be an absolute path to the target file, the target file can not already exist and all parent directories must already …

---

## 25. 🟡 High Severity — Budibase: SSRF via OAuth2 Config Validation — Missing fetchWithBlacklist Protection

**CVE:** `CVE-2026-48146` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-g6qx-g4pr-92v7>

> ### Summary

The OAuth2 token fetch function in `packages/server/src/sdk/workspace/oauth2/utils.ts` (line 59) uses raw `fetch(config.url)` with **no SSRF protection**. The safe wrapper `fetchWithBlacklist()` exists in the same codebase and is used in every other outbound HTTP call (automation steps, plugin downloads, object store), but was **not applied** to the OAuth2 token endpoint.

A user with…

---

## 26. 🟡 High Severity — Budibase: SSRF via User-Controlled queryId in Automation Execute Query Step

**CVE:** `CVE-2026-48128` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-6964-pp88-6wp9>

> ### Summary

The executeQuery automation step in Budibase accepts a queryId from automation step inputs and passes it directly to the query execution controller without additional validation. When combined with a REST datasource configured to target internal infrastructure, this creates a server-side request forgery path where automation execution causes the Budibase server to make outbound HTTP r…

---

## 27. 🟡 High Severity — NIOExtras: NIOHTTPRequestDecompressor ratio limit bypass via inflated Content-Length

**CVE:** `CVE-2026-28975` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-6ph5-fww6-vfwv>

> ### Impact

When `NIOHTTPRequestDecompressor` is configured with `.ratio(N)`, the decompression limit is enforced using the `Content-Length` header value from the incoming request rather than the actual number of compressed bytes received. Since `Content-Length` is attacker-controlled, a malicious client can supply an inflated value that causes the ratio check to always pass, effectively disabling…

---

## 28. 🟡 High Severity — LangGraph has NoSQL parameter injection in MongoDBSaver, allowing cross-tenant state access

**CVE:** `CVE-2026-48121` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-98xf-r82g-9mhx>

> ## Summary

A NoSQL injection vulnerability existed in `MongoDBSaver` where checkpoint identifier fields from `config.configurable` were used in MongoDB queries without strict type enforcement. In vulnerable versions, attacker-controlled object payloads (for example MongoDB operators like `$gt` and `$ne`) could be interpreted as query operators instead of literal identifier values.

This could byp…

---

## 29. 🟡 High Severity — GeoServer DB2 DataStore Extension has a JNDI Vulnerability via Store Connection

**CVE:** `CVE-2025-27511` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-g628-r368-6vh7>

> ## Summary

Administrator can perform JNDI attack through specially crafted DB2 jdbc url leading to Remote Code Execution (RCE).

## Impact

If GeoServer has DB2 extension installed, this vulnerability can lead to executing arbitrary code.

## Details

Authenticated users can access Vector Data Sources page to creating a new data store through db2 jdbc connection, performing JNDI attack due to unr…

---

## 30. 🟡 High Severity — Russh SSH message fields were decoded through allocation-first parsers before field-specific bounds

**CVE:** `CVE-2026-48110` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-4r3c-5hpg-58qr>

> # SSH message fields were decoded through allocation-first parsers before field-specific bounds

### Summary

Several `russh` client and server message handlers decoded attacker-controlled SSH strings, name-lists, and byte fields into owned allocations before applying field-specific bounds. A remote SSH peer could send oversized, high-fanout, or malformed length-prefixed fields and make the librar…

---

## 31. 🟡 High Severity — AWS Advanced Go Wrapper has Privilege Escalation in Aurora PostgreSQL instance

**CVE:** `CVE-2026-11401` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-r236-5pc3-3qcp>

> Aurora PostgreSQL is a fully managed relational database engine that&#x27;s compatible with PostgreSQL.

An issue in Aurora PostgreSQL using the AWS Go Wrapper waa identified, see CVE-2026-11401.


Impact
An issue in AWS Wrappers for Amazon Aurora PostgreSQL may allow for privilege escalation to rds_superuser role. A low privilege authenticated user can create a crafted function that could be exec…

---

## 32. 🟡 High Severity — Russh: SSH identification parsing accepted non-canonical client banners and did not bound pre-banner input

**CVE:** `CVE-2026-48108` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-76r6-x97p-67vr>

> ### Summary

`russh` did not enforce the SSH identification-string rules as deliberately as OpenSSH. In particular, the server-side identification reader used the same permissive path as the client, allowing pre-banner lines from clients, and the reader did not enforce a bounded number of pre-banner lines.

For a library server built on `russh`, this could allow a remote peer to hold connection se…

---

## 33. 🟡 High Severity — WsgiDAV encoded dot segments can escape filesystem share roots

**CVE:** `CVE-2026-48099` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-wxq4-cc2q-338q>

> ### Impact
WsgiDAV 4.3.3 can allow a WebDAV request path containing an encoded parent-directory segment to escape the configured filesystem share root in a specific path layout.

### Patches
The issue is fixed with version 4.3.4.

### Preconditions

The practical impact depends on the deployment.

The deployment uses a filesystem-backed WsgiDAV share.

The attacker can send WebDAV requests accepte…

---

## 34. 🟡 High Severity — Netty HAProxy: Unbalanced Reference Count in Nested PP2_TYPE_SSL TLV Parsing Leads to Memory Exhaustion

**CVE:** `CVE-2026-48059` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-h2qv-fj59-j46j>

> ### Impact
The HAProxy PROXY protocol v2 codec in netty leaks native or heap memory on every connection when a client sends a syntactically valid header containing nested `PP2_TYPE_SSL` TLVs (type-length-value records) at depth two or greater. The leak occurs on the successful parse path — no exception is thrown, the message fires downstream, the decoder removes itself, and the application release…

---

## 35. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
