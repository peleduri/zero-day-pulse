# Zero Day Pulse

> **Generated:** 2026-06-13 02:07 UTC &nbsp;|&nbsp; **Total:** 34 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 20 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal vulnerability allowing unauthenticated remote attackers to read sensitive files on the server via directory/path traversal.
- **Affected Products:** SimpleHelp remote support / RMM versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors
- **Mitigation:** Update SimpleHelp to a patched version (upgrade to a release newer than 5.5.7). If immediate patching is not possible, isolate SimpleHelp servers from public access, restrict network access to trusted hosts, and monitor for indicators of compromise.
- **Vendor Advisory:** https://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — Active Exploitation of Oracle PeopleSoft Zero-Day (CVE-2026-35273)

**CVE:** `CVE-2026-35273` | `CVE-2013-3821` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://www.rapid7.com/blog/post/etr-active-exploitation-of-oracle-peoplesoft-zero-day-cve-2026-35273>

> Overview On June 10, 2026, Oracle published a security alert for CVE-2026-35273 , a critical vulnerability in the Updates Environment Management component of PeopleSoft Enterprise PeopleTools. Oracle released an out-of-band patch the same day as the advisory, underscoring the urgency of remediation. The vulnerability has a CVSSv3.1 score of 9.8 and is remotely exploitable without authentication. P…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is a server‑side request forgery (SSRF, CWE‑918) in the Updates Environment Management component that permits unauthenticated remote HTTP access, which can be chained to achieve remote code execution.
- **Affected Products:** PeopleSoft Enterprise PeopleTools (Updates Environment Management component)
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** ShinyHunters
- **Mitigation:** Apply the Oracle out‑of‑band patch immediately; restrict PeopleSoft HTTP access with network segmentation, firewalls/WAF rules, and limit exposure to trusted networks.
- **Vendor Advisory:** https://www.oracle.com/security-alerts/alert-cve-2026-35273.html

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) abuses hidden or benign‑looking web content (e.g., hidden HTML, comments, or embedded scripts) to deliver instructions that influence AI agents’ prompts. Attackers chain these injected instructions with agent workflows (e.g., web‑scraping + chain‑of‑thought prompts) to cause data exfiltration, unauthorized actions, or execution of secondary exploits. Researchers observed real‑world payloads hidden in website code used to manipulate AI assistants.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Harden agent input handling by (1) treating web content as untrusted, (2) stripping or sanitizing hidden/metadata content (comments, hidden fields, alt text), (3) enforcing strict output verification and least‑privilege for agent actions, (4) using model grounding with structured sources and retrieval‑augmented verification, and (5) applying content allowlists/denylists and prompting policies.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) / "GeminiJack" is a RAG‑context poisoning attack where attacker‑controlled content (shared Doc/Calendar/Gmail) embeds instructions that are retrieved by the RAG pipeline and treated as model instructions, causing the model to search across connected Workspace data and exfiltrate results (e.g., via an external image request).
- **Affected Products:** Google Gemini Enterprise, Vertex AI Search (VAIS), Workspace with Gemini
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true — https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Google’s layered defenses — automated and human red‑teaming, centralized vulnerability cataloging, RAG pipeline hardening, separation of VAIS from Gemini Enterprise, runtime filters and browser/agent security layers — plus organizational hardening (restrict RAG data sources, monitoring, DLP integration, vet shared content).
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: malicious webpage content or third‑party resources craft inputs that influence an agentic browser’s prompts, causing the agent to perform unintended actions or disclose information.
- **Affected Products:** Chrome (agentic browsing / Gemini integration) – specific versions unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true - http://blog.google/security/architecting-security-for-agentic
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use Chrome’s updated layered defenses for agentic browsing; follow vendor guidance to restrict origin access and avoid unsafe AI actions; keep Chrome updated to receive the announced protections.
- **Vendor Advisory:** http://blog.google/security/architecting-security-for-agentic

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** The 2025 Google Security Blog summary attributes a sustained reduction in memory‑safety vulnerabilities to moving new Android code to Rust; the mechanism is elimination of common memory‑safety classes (use‑after‑free, buffer overflows, null/dangle pointer bugs) by using Rust’s ownership/typing guarantees and safe APIs. Specific vulnerability instances and exploit mechanics are not described in the blog.
- **Affected Products:** Android platform (first-party and third-party code across C, C++, Java, Kotlin, and Rust)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Continue migration of new Android platform code to Rust, apply defensive coding and code review for existing C/C++ components, enable platform hardening and careful third‑party dependency management.
- **Vendor Advisory:** https://blog.google/security/rust-in-android-move-fast-fix-things/

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection uses hidden or external instructions embedded in untrusted data sources (webpages, emails, documents, calendar invites) that AI systems ingest during browsing, retrieval, or summarization; attackers hide instructions (e.g., via concealed webpage code or content) that cause models to disclose sensitive data or perform unauthorized actions.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Layered defense per Google: treat external inputs as untrusted; use input provenance and filtering, prompt hardening (explicit system instructions and input sanitization), access controls and least privilege for data access, output filtering and redaction, monitoring and anomaly detection; apply model and application-level defenses across the prompt lifecycle.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Backbone routers, Provider Edge (PE) routers, Customer Edge (CE) routers
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Mitigation steps unavailable.
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
- **Threat Actors:** Russian GRU (85th GTsSS, Unit 26165), also identified as APT28.
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** CVE‑2026‑45586: Elevation of privilege via abuse of the Windows Collaborative Translation Framework (CTFMON) allowing a low‑privileged user to gain higher privileges. CVE‑2026‑50507: Security feature bypass in Windows BitLocker that can subvert encryption protections. CVE‑2026‑44815: Remote code execution in the Windows DHCP Client Service through a vulnerable API that can be abused to execute arbitrary code.
- **Affected Products:** Windows Collaborative Translation Framework (CTFMON), Windows BitLocker, Windows DHCP Client Service
- **CVSS Score:** 7.8, 6.8, 9.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/)
- **Patch Available:** true (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45586, https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50507, https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-44815)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the Microsoft patches linked in the Update Guide for all three CVEs. For the DHCP Client Service vulnerability, audit and restrict applications that call the vulnerable API. For the BitLocker bypass, ensure encryption keys are stored securely and monitor for abnormal decryption attempts. For the CTFMON elevation‑of‑privilege issue, limit user permissions and disable unnecessary translation services where possible.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45586

---

## 11. 🟠 Zero-Day — Factoring "short-sleeve" RSA keys with polynomials

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Trail of Bits Blog &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://blog.trailofbits.com/2026/06/12/factoring-short-sleeve-rsa-keys-with-polynomials/>

> What happens when the bits of an RSA private key are heavily biased toward 0 instead of being randomly generated? The public key’s bits could be biased enough for us to detect these incorrectly generated keys in the wild. Together with Hanno Böck of the badkeys project, we found hundreds of unique keys that not only have this property, but can be quickly factored. We also found the bug that led to…

---

## 12. 🟠 Zero-Day — Anthropic Disputes Fable 5 AI Jailbreak

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://www.securityweek.com/anthropic-disputes-fable-5-ai-jailbreak/>

> An AI hacker claims to have achieved a prompt-based jailbreak shortly after Fable 5’s launch, but Anthropic says it’s not a real jailbreak. The post Anthropic Disputes Fable 5 AI Jailbreak appeared first on SecurityWeek .

---

## 13. 🟠 Zero-Day — CISA orders feds to patch actively exploited Ivanti flaw by Sunday

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-gives-feds-3-days-to-patch-ivanti-flaw-exploited-in-attacks/>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) ordered government agencies to patch an actively exploited Ivanti Sentry flaw within three days, as mandated by the newly issued Binding Operational Directive (BOD) 26-04. [...]

---

## 14. 🟠 Zero-Day — Google Confirms Exploitation of Oracle PeopleSoft Zero-Day by ShinyHunters

**CVE:** `CVE-2026-35273` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://www.securityweek.com/google-confirms-exploitation-of-oracle-peoplesoft-zero-day-by-shinyhunters/>

> Oracle has mitigated CVE-2026-35273, but it has not publicly confirmed the vulnerability’s in-the-wild exploitation. The post Google Confirms Exploitation of Oracle PeopleSoft Zero-Day by ShinyHunters appeared first on SecurityWeek .

---

## 15. 🟡 High Severity — File Browser has incorrect access control for public directory shares via rule path rebasing

**CVE:** `CVE-2026-54091` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-j9jx-hp4c-ghhh>

> ### Summary
File Browser&#x27;s public share handlers rebase the share owner&#x27;s filesystem root to the shared directory and then evaluate descendant paths against the owner&#x27;s global and per-user rules using the rebased relative path instead of the original path relative to the owner&#x27;s scope.

As a result, an attacker who knows a public directory share URL can access files and subdire…

---

## 16. 🟡 High Severity — File Browser has a DoS Vulnerability via Public Login API

**CVE:** `CVE-2026-54092` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-w5fm-68j4-fpc4>

> ### Summary
Unchecked passwords maximums allow for an arbitrarily large password to be passed into the login API. This spikes CPU and memory, and after testing, crashes, heavily lags any container created, and has even made my docker daemon start to send errors with status code 500 even after the container was destroyed.

### Details
When sending JSON in the body of the request to the route `api/l…

---

## 17. 🟡 High Severity — Fleet: Observer-level enrollment secret extraction via ORDER BY oracle on Apple MDM commands endpoint

**CVE:** `CVE-2026-46371` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-x4qr-qw6h-wvxq>

> ### Summary

A vulnerability in Fleet&#x27;s Apple MDM commands listing endpoint allowed authenticated users with the lowest-privilege Observer role to extract sensitive values from joined database tables — including host enrollment secrets and Apple Push Notification Service (APNS) tokens — through a cursor-based binary search oracle. The endpoint accepted a user-supplied `order_key` parameter th…

---

## 18. 🟡 High Severity — Fleet has observer-level enrollment secret extraction via ORDER BY oracle on labels host-listing endpoint

**CVE:** `CVE-2026-46370` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-vxm7-9x8v-8gm4>

> ### Summary

A vulnerability in Fleet&#x27;s labels host-listing endpoint allowed authenticated users with the lowest-privilege Observer role to extract host enrollment secrets (`node_key`, `orbit_node_key`) through a cursor-based binary search oracle. The endpoint accepted a user-supplied `order_key` parameter that was not validated against a column allowlist, permitting sort order to be driven b…

---

## 19. 🟡 High Severity — Fabric.js improper escaping in fabric.Gradient colorStops leads to XSS in SVG serialization

**CVE:** `CVE-2026-44311` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-w22m-hvvm-xmwx>

> ### Summary

A potential Cross-Site Scripting (XSS) vulnerability exists in Fabric.js due to improper escaping of user-controlled input during SVG serialization via the `toSVG()` method.

Specifically, the `color` field within the `colorStops` array of a `fabric.Gradient` object is not properly escaped when converted into SVG `&lt;stop&gt;` elements. If an application renders the generated SVG str…

---

## 20. 🟡 High Severity — Radius Controller May Delete a Container Resource via an Injected Deployment Annotation (Multi-Tenant Installs)

**CVE:** `CVE-2026-53999` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-fp5j-4fj2-4jvq>

> # Radius Controller May Delete a Container Resource via an Injected Deployment Annotation (Multi-Tenant Installs)

## Summary

A configuration-validation issue in the Radius Kubernetes controller can cause it to issue a `DELETE` for the container resource referenced by a tampered `radapp.io/status` annotation on a Deployment. It follows the &quot;Confused Deputy&quot; pattern. Real-world impact is…

---

## 21. 🟡 High Severity — TYPO3 CMS has Privilege Escalation & SQL Injection in its Form Framework

**CVE:** `CVE-2026-49741` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-jh32-v29g-68pq>

> ### Problem
Backend users with write access to the `form_definition` database table were able to directly create, update, or delete form definition records via `DataHandler`, bypassing the Form Framework&#x27;s persistence validation and permission checks. This allowed injecting arbitrary form configurations, re-enabling attack vectors originally addressed in [TYPO3-CORE-SA-2018-003](https://typo3…

---

## 22. 🟡 High Severity — TYPO3 CMS has Insecure Deserialization via Core API

**CVE:** `CVE-2026-49740` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-c78m-c52x-jgwp>

> ### Problem
TYPO3&#x27;s cache frontend (`VariableFrontend`) and persistent key-value store (`Registry`) deserialized PHP payloads without integrity validation or class restrictions. An attacker with write access to the underlying storage backend (cache store or sys_registry database table) could inject a crafted serialized payload to trigger PHP Object Injection, potentially exploiting a gadget c…

---

## 23. 🟡 High Severity — TYPO3 CMS has Broken Access Control in its File Abstraction Layer

**CVE:** `CVE-2026-49738` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-jf56-v8jc-jcc5>

> ### Problem
The path allowance check in `GeneralUtility::isAllowedAbsPath()` performed a plain string prefix comparison without requiring a directory separator boundary, causing a path like `/var/www/html-other/secret.yaml` to be incorrectly accepted as valid when the project root was `/var/www/html`. Administrator users with access to the File Abstraction Layer were able to create new file storag…

---

## 24. 🟡 High Severity — gorest InMemorySecret2FA race condition allows process crash via concurrent map access (CWE-362)

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

## 25. 🟡 High Severity — Budibase: Basic app users can exfiltrate stored REST datasource auth by rewriting datasource base URL

**CVE:** `CVE-2026-48152` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-3gp5-q4jw-3v94>

> ### Summary
Budibase stores external REST datasource credentials server-side and documents that database credentials are applied server-side and are not exposed in the UI. The REST datasource implementation redacts stored Basic/Bearer/OAuth2 auth secrets before returning datasource data to clients. However, the single-datasource `GET` and `PUT` routes are guarded by generic `TABLE READ`, not by Bu…

---

## 26. 🟡 High Severity — Budibase: Workspace-scoped builder escalates to global admin via /api/public/v1/roles/assign

**CVE:** `CVE-2026-48150` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-6xp4-cf37-ppjh>

> ## Summary

`/api/public/v1/roles/assign` is guarded by the `builderOrAdmin` middleware, which passes any user who is a builder for the app id in the `x-budibase-app-id` header. That check admits both global builders and workspace-scoped builders (`builder.apps` set but `builder.global` unset). The controller then spreads the request body into the SDK call, and the SDK grants `builder.global=true`…

---

## 27. 🟡 High Severity — Budibase: Unvalidated VectorDB Host Parameter Enables SSRF

**CVE:** `CVE-2026-48148` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-cv96-5348-p5p8>

> ### Summary

The VectorDB configuration endpoint in Budibase accepts a host parameter that undergoes no validation against internal IP ranges, reserved hostnames, or URL schemes. Any authenticated user with builder-level access can supply an arbitrary host value such as `169.254.169.254` or localhost, causing the server to initiate outbound TCP connections to internal network addresses or cloud me…

---

## 28. 🟡 High Severity — GeoServer has a Server-Side Request Forgery (SSRF) Vulnerability in its XML Entity Resolution

**CVE:** `CVE-2025-58175` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-x4r9-gmw3-hxww>

> ### Summary
A GeoServer that uses `ENTITY_RESOLUTION_ALLOWLIST` may allow attacker to perform unauthenticated Server-Side Request Forgery (SSRF).

### Details
This vulnerability requires that GeoServer is set up to use a proxy base URL and the `ENTITY_RESOLUTION_ALLOWLIST` (default since 2.25.0):

### Impact
This vulnerability allows an attacker to cause GeoServer to make requests to an unintended…

---

## 29. 🟡 High Severity — GeoServer has an arbitrary file write vulnerability in its Master Password Dump Page

**CVE:** `CVE-2025-52465` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-7qmg-grcp-qf25>

> ### Summary
A vulnerability exists that allows an authenticated administrator with access to GeoServer&#x27;s security system to pass arbitrary file names to the Master Password Dump web page and create files containing the master password in plaintext. The provided file name must be an absolute path to the target file, the target file can not already exist and all parent directories must already …

---

## 30. 🟡 High Severity — Budibase: SSRF via OAuth2 Config Validation — Missing fetchWithBlacklist Protection

**CVE:** `CVE-2026-48146` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-g6qx-g4pr-92v7>

> ### Summary

The OAuth2 token fetch function in `packages/server/src/sdk/workspace/oauth2/utils.ts` (line 59) uses raw `fetch(config.url)` with **no SSRF protection**. The safe wrapper `fetchWithBlacklist()` exists in the same codebase and is used in every other outbound HTTP call (automation steps, plugin downloads, object store), but was **not applied** to the OAuth2 token endpoint.

A user with…

---

## 31. 🟡 High Severity — Budibase: SSRF via User-Controlled queryId in Automation Execute Query Step

**CVE:** `CVE-2026-48128` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-6964-pp88-6wp9>

> ### Summary

The executeQuery automation step in Budibase accepts a queryId from automation step inputs and passes it directly to the query execution controller without additional validation. When combined with a REST datasource configured to target internal infrastructure, this creates a server-side request forgery path where automation execution causes the Budibase server to make outbound HTTP r…

---

## 32. 🟡 High Severity — NIOExtras: NIOHTTPRequestDecompressor ratio limit bypass via inflated Content-Length

**CVE:** `CVE-2026-28975` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-6ph5-fww6-vfwv>

> ### Impact

When `NIOHTTPRequestDecompressor` is configured with `.ratio(N)`, the decompression limit is enforced using the `Content-Length` header value from the incoming request rather than the actual number of compressed bytes received. Since `Content-Length` is attacker-controlled, a malicious client can supply an inflated value that causes the ratio check to always pass, effectively disabling…

---

## 33. 🟡 High Severity — LangGraph has NoSQL parameter injection in MongoDBSaver, allowing cross-tenant state access

**CVE:** `CVE-2026-48121` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-98xf-r82g-9mhx>

> ## Summary

A NoSQL injection vulnerability existed in `MongoDBSaver` where checkpoint identifier fields from `config.configurable` were used in MongoDB queries without strict type enforcement. In vulnerable versions, attacker-controlled object payloads (for example MongoDB operators like `$gt` and `$ne`) could be interpreted as query operators instead of literal identifier values.

This could byp…

---

## 34. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
