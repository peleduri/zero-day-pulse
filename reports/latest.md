# Zero Day Pulse

> **Generated:** 2026-06-13 08:46 UTC &nbsp;|&nbsp; **Total:** 31 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 11 &nbsp;|&nbsp; 🟡 High: 20 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** An unauthenticated remote attacker can exploit a path traversal flaw in SimpleHelp 5.5.7 and earlier to read or write arbitrary files, leading to potential code execution.
- **Affected Products:** SimpleHelp Remote Monitoring and Management version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (https://medium.com/@unKnOwn37/simplehelp-cve-2024-57727-tryhackme-3bea119c1c1e)
- **Patch Available:** true (http://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570)
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Upgrade to SimpleHelp version 5.5.8 or later.
- **Vendor Advisory:** https://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — Active Exploitation of Oracle PeopleSoft Zero-Day (CVE-2026-35273)

**CVE:** `CVE-2026-35273` | `CVE-2013-3821` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://www.rapid7.com/blog/post/etr-active-exploitation-of-oracle-peoplesoft-zero-day-cve-2026-35273>

> Overview On June 10, 2026, Oracle published a security alert for CVE-2026-35273 , a critical vulnerability in the Updates Environment Management component of PeopleSoft Enterprise PeopleTools. Oracle released an out-of-band patch the same day as the advisory, underscoring the urgency of remediation. The vulnerability has a CVSSv3.1 score of 9.8 and is remotely exploitable without authentication. P…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is a server‑side request forgery (CWE‑918) where a missing authentication check in the Updates Environment Management function allows unauthenticated HTTP requests to trigger arbitrary code execution on the server.
- **Affected Products:** PeopleSoft Enterprise PeopleTools (Updates Environment Management component)
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** ShinyHunters
- **Mitigation:** Apply the Oracle out‑of‑band patch immediately. If the patch cannot be applied, restrict HTTP access to the PeopleSoft Updates Environment Management interface, block inbound traffic to the management ports, deploy Web Application Firewall rules to block SSRF patterns, and monitor server logs for suspicious requests.
- **Vendor Advisory:** https://www.oracle.com/security-alerts/alert-cve-2026-35273.html

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when AI systems consume external content (websites, documents, email) that contains malicious instructions; attackers seed poisoned text (e.g., "if you are an AI…") so agents silently follow attacker commands instead of user intent. Google’s study scanned Common Crawl, used Gemini for classification, and human validation to identify categories (pranks, SEO, deterrence, data exfiltration, destructive commands).
- **Affected Products:** Google Workspace (with Gemini integrations), Gemini (agentic AI systems)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false.
- **Patch Available:** false.
- **Active Exploitation:** true.
- **Threat Actors:** None known.
- **Mitigation:** Layered defenses and hardening: content filtering and pattern detection, LLM‑based intent classification, human review for high‑risk cases, model hardening/red teams, secure agent design (restricting external execution), monitoring telemetry at scale, and participation in AI Vulnerability Reward Program.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** An attacker injects malicious instructions into shared Google Docs, Calendar events, or Gmail messages. Gemini ingests the poisoned content and executes the injected prompt, creating a covert channel that can leak Gmail, Calendar, and Docs data without direct user interaction.
- **Affected Products:** Google Workspace (Gmail, Google Docs, Google Calendar) – all versions
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (source: http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability)
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Deploy prompt‑injection content classifiers, enable markdown sanitization and suspicious URL redaction, enforce user‑confirmation frameworks for AI‑generated actions, and monitor for security mitigation notifications. Participate in the Google AI Vulnerability Rewards Program to report novel attacks.
- **Vendor Advisory:** https://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: malicious webpage content can inject instructions that an agentic browser (or its embedded AI agents) may execute when autonomously browsing or summarizing pages; Google’s mitigation layers restrict origin access, block prompt‑injection signals, and add a secondary ’watcher’ agent to validate actions.
- **Affected Products:** Chrome (agentic/Gemini-enabled builds)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use Chrome’s updated agentic security features (layered defenses described in advisory): restrict origin access, block prompt‑injection vectors, require user transparency and control, and employ the secondary monitoring agent; follow Google’s advisory for configuration and hardening.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow in CrabbyAVIF (an AVIF parser/decoder in unsafe Rust) could have led to remote code execution; Scudo mitigated exploitability and the flaw was fixed pre-release.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use of Scudo allocator rendered the flaw non-exploitable in practice; defense-in-depth (memory-safe languages, hardened allocators) advised.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) embeds malicious instructions within external data sources (emails, documents, calendar invites, web content) that AI systems ingest; the model or agent may prioritize or execute those hidden instructions, causing data exfiltration or unintended actions via prompt‑parsing and instruction‑following behaviors.
- **Affected Products:** AI systems that ingest external data (generative AI models, agents, plugins); OpenClaw (all versions prior to April 23, 2026 patches)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known.
- **Mitigation:** Apply layered defenses: validate and sanitize external inputs; enforce provenance/metadata checks; least‑privilege data access for agents/plugins; instruction‑scoping and guardrails in prompts; runtime filtering and detection of IPI payloads; continuous monitoring and threat intelligence updates.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors exploit publicly known CVEs and weak configurations to gain initial access to edge routers, then maintain persistence by modifying ACLs, opening ports, creating privileged accounts, and executing scripts (e.g., Tcl) on Cisco IOS devices.
- **Affected Products:** Cisco IOS, Cisco IOS XE, Cisco NX-OS, Ivanti Connect Secure, Ivanti Policy (specific CVEs: CVE-2024-21887, CVE-2023-20273, CVE-2023-20198, CVE-2018-0171)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching edge devices; disable unused ports and protocols; disable Cisco Smart Install and Guest Shell where not required; enforce strong credentials and multi‑factor authentication; monitor device logs and configurations for unexpected changes; perform firmware integrity checks; follow vendor hardening guides.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** The advisory describes a long-running cyber espionage campaign by Russian GRU (Unit 26165) targeting Western logistics entities and technology companies, including those coordinating transport and delivery of assistance to Ukraine; it documents targeting since 2022 but does not list a specific single‑vulnerability technical exploit.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** true
- **Threat Actors:** GRU 85th GTsSS (Unit 26165), tracked as APT28 (also referenced as Russian GRU)
- **Mitigation:** Follow CISA/FBI recommended mitigations in the advisory (e.g., enhanced monitoring, network segmentation, multifactor authentication, prompt patching and credential hygiene) — specific steps: implement MFA, isolate critical logistics systems, increase logging and EDR coverage, apply vendor security updates, review remote access configurations, and conduct threat hunting and incident response readiness.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** CVE‑2026‑45586 – link‑following flaw (CWE‑59) in CTFMON enabling local privilege escalation to SYSTEM; CVE‑2026‑50507 – missing authentication (CWE‑306) allowing physical‑access BitLocker bypass; CVE‑2026‑44815 – stack‑based buffer overflow (CWE‑121) in DHCP Client Service that can be triggered by a rogue DHCP server for remote code execution; CVE‑2026‑45648 – stack‑based buffer overflow in AD DS NSPI RPC interface causing out‑of‑bounds write and RCE; Outlook/Word vulnerabilities – type confusion, use‑after‑free, and heap‑based buffer overflow enabling RCE via malicious preview pane content.
- **Affected Products:** Microsoft Windows (CTFMON/Collaborative Translation Framework), Windows BitLocker, Windows DHCP Client Service, Windows Active Directory Domain Services, Microsoft Outlook, Microsoft Word, Windows Media, Windows Graphics Component (Win32K‑GRFX), Windows Kerberos KDC, other Windows and Office product families
- **CVSS Score:** CVE‑2026‑45586 — 7.8; CVE‑2026‑50507 — 6.8; CVE‑2026‑44815 — 9.8; CVE‑2026‑45648 — 8.8; CVE‑2026‑45456/45458/47635 — 8.4; CVE‑2026‑48574 — 7.8; CVE‑2026‑44803/44812 — 7.8; CVE‑2026‑47288 — 7.1
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the Microsoft patches released in June 2026; for unpatched issues, restrict applications that call vulnerable APIs (e.g., DhcpGetOriginalSubnetMask), employ network segmentation, enforce strict configuration baselines, and use CrowdStrike Falcon Exposure Management for discovery and prioritization.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/

---

## 11. 🟠 Zero-Day — Factoring "short-sleeve" RSA keys with polynomials

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Trail of Bits Blog &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://blog.trailofbits.com/2026/06/12/factoring-short-sleeve-rsa-keys-with-polynomials/>

> What happens when the bits of an RSA private key are heavily biased toward 0 instead of being randomly generated? The public key’s bits could be biased enough for us to detect these incorrectly generated keys in the wild. Together with Hanno Böck of the badkeys project, we found hundreds of unique keys that not only have this property, but can be quickly factored. We also found the bug that led to…

---

## 12. 🟡 High Severity — File Browser has incorrect access control for public directory shares via rule path rebasing

**CVE:** `CVE-2026-54091` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-j9jx-hp4c-ghhh>

> ### Summary
File Browser&#x27;s public share handlers rebase the share owner&#x27;s filesystem root to the shared directory and then evaluate descendant paths against the owner&#x27;s global and per-user rules using the rebased relative path instead of the original path relative to the owner&#x27;s scope.

As a result, an attacker who knows a public directory share URL can access files and subdire…

---

## 13. 🟡 High Severity — File Browser has a DoS Vulnerability via Public Login API

**CVE:** `CVE-2026-54092` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-w5fm-68j4-fpc4>

> ### Summary
Unchecked passwords maximums allow for an arbitrarily large password to be passed into the login API. This spikes CPU and memory, and after testing, crashes, heavily lags any container created, and has even made my docker daemon start to send errors with status code 500 even after the container was destroyed.

### Details
When sending JSON in the body of the request to the route `api/l…

---

## 14. 🟡 High Severity — Fleet: Observer-level enrollment secret extraction via ORDER BY oracle on Apple MDM commands endpoint

**CVE:** `CVE-2026-46371` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-x4qr-qw6h-wvxq>

> ### Summary

A vulnerability in Fleet&#x27;s Apple MDM commands listing endpoint allowed authenticated users with the lowest-privilege Observer role to extract sensitive values from joined database tables — including host enrollment secrets and Apple Push Notification Service (APNS) tokens — through a cursor-based binary search oracle. The endpoint accepted a user-supplied `order_key` parameter th…

---

## 15. 🟡 High Severity — Fleet has observer-level enrollment secret extraction via ORDER BY oracle on labels host-listing endpoint

**CVE:** `CVE-2026-46370` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-vxm7-9x8v-8gm4>

> ### Summary

A vulnerability in Fleet&#x27;s labels host-listing endpoint allowed authenticated users with the lowest-privilege Observer role to extract host enrollment secrets (`node_key`, `orbit_node_key`) through a cursor-based binary search oracle. The endpoint accepted a user-supplied `order_key` parameter that was not validated against a column allowlist, permitting sort order to be driven b…

---

## 16. 🟡 High Severity — Fabric.js improper escaping in fabric.Gradient colorStops leads to XSS in SVG serialization

**CVE:** `CVE-2026-44311` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-w22m-hvvm-xmwx>

> ### Summary

A potential Cross-Site Scripting (XSS) vulnerability exists in Fabric.js due to improper escaping of user-controlled input during SVG serialization via the `toSVG()` method.

Specifically, the `color` field within the `colorStops` array of a `fabric.Gradient` object is not properly escaped when converted into SVG `&lt;stop&gt;` elements. If an application renders the generated SVG str…

---

## 17. 🟡 High Severity — Radius Controller May Delete a Container Resource via an Injected Deployment Annotation (Multi-Tenant Installs)

**CVE:** `CVE-2026-53999` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-fp5j-4fj2-4jvq>

> # Radius Controller May Delete a Container Resource via an Injected Deployment Annotation (Multi-Tenant Installs)

## Summary

A configuration-validation issue in the Radius Kubernetes controller can cause it to issue a `DELETE` for the container resource referenced by a tampered `radapp.io/status` annotation on a Deployment. It follows the &quot;Confused Deputy&quot; pattern. Real-world impact is…

---

## 18. 🟡 High Severity — TYPO3 CMS has Privilege Escalation & SQL Injection in its Form Framework

**CVE:** `CVE-2026-49741` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-jh32-v29g-68pq>

> ### Problem
Backend users with write access to the `form_definition` database table were able to directly create, update, or delete form definition records via `DataHandler`, bypassing the Form Framework&#x27;s persistence validation and permission checks. This allowed injecting arbitrary form configurations, re-enabling attack vectors originally addressed in [TYPO3-CORE-SA-2018-003](https://typo3…

---

## 19. 🟡 High Severity — TYPO3 CMS has Insecure Deserialization via Core API

**CVE:** `CVE-2026-49740` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-c78m-c52x-jgwp>

> ### Problem
TYPO3&#x27;s cache frontend (`VariableFrontend`) and persistent key-value store (`Registry`) deserialized PHP payloads without integrity validation or class restrictions. An attacker with write access to the underlying storage backend (cache store or sys_registry database table) could inject a crafted serialized payload to trigger PHP Object Injection, potentially exploiting a gadget c…

---

## 20. 🟡 High Severity — TYPO3 CMS has Broken Access Control in its File Abstraction Layer

**CVE:** `CVE-2026-49738` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-jf56-v8jc-jcc5>

> ### Problem
The path allowance check in `GeneralUtility::isAllowedAbsPath()` performed a plain string prefix comparison without requiring a directory separator boundary, causing a path like `/var/www/html-other/secret.yaml` to be incorrectly accepted as valid when the project root was `/var/www/html`. Administrator users with access to the File Abstraction Layer were able to create new file storag…

---

## 21. 🟡 High Severity — gorest InMemorySecret2FA race condition allows process crash via concurrent map access (CWE-362)

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

## 22. 🟡 High Severity — Budibase: Basic app users can exfiltrate stored REST datasource auth by rewriting datasource base URL

**CVE:** `CVE-2026-48152` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-3gp5-q4jw-3v94>

> ### Summary
Budibase stores external REST datasource credentials server-side and documents that database credentials are applied server-side and are not exposed in the UI. The REST datasource implementation redacts stored Basic/Bearer/OAuth2 auth secrets before returning datasource data to clients. However, the single-datasource `GET` and `PUT` routes are guarded by generic `TABLE READ`, not by Bu…

---

## 23. 🟡 High Severity — Budibase: Workspace-scoped builder escalates to global admin via /api/public/v1/roles/assign

**CVE:** `CVE-2026-48150` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-6xp4-cf37-ppjh>

> ## Summary

`/api/public/v1/roles/assign` is guarded by the `builderOrAdmin` middleware, which passes any user who is a builder for the app id in the `x-budibase-app-id` header. That check admits both global builders and workspace-scoped builders (`builder.apps` set but `builder.global` unset). The controller then spreads the request body into the SDK call, and the SDK grants `builder.global=true`…

---

## 24. 🟡 High Severity — Budibase: Unvalidated VectorDB Host Parameter Enables SSRF

**CVE:** `CVE-2026-48148` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-cv96-5348-p5p8>

> ### Summary

The VectorDB configuration endpoint in Budibase accepts a host parameter that undergoes no validation against internal IP ranges, reserved hostnames, or URL schemes. Any authenticated user with builder-level access can supply an arbitrary host value such as `169.254.169.254` or localhost, causing the server to initiate outbound TCP connections to internal network addresses or cloud me…

---

## 25. 🟡 High Severity — GeoServer has a Server-Side Request Forgery (SSRF) Vulnerability in its XML Entity Resolution

**CVE:** `CVE-2025-58175` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-x4r9-gmw3-hxww>

> ### Summary
A GeoServer that uses `ENTITY_RESOLUTION_ALLOWLIST` may allow attacker to perform unauthenticated Server-Side Request Forgery (SSRF).

### Details
This vulnerability requires that GeoServer is set up to use a proxy base URL and the `ENTITY_RESOLUTION_ALLOWLIST` (default since 2.25.0):

### Impact
This vulnerability allows an attacker to cause GeoServer to make requests to an unintended…

---

## 26. 🟡 High Severity — GeoServer has an arbitrary file write vulnerability in its Master Password Dump Page

**CVE:** `CVE-2025-52465` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-7qmg-grcp-qf25>

> ### Summary
A vulnerability exists that allows an authenticated administrator with access to GeoServer&#x27;s security system to pass arbitrary file names to the Master Password Dump web page and create files containing the master password in plaintext. The provided file name must be an absolute path to the target file, the target file can not already exist and all parent directories must already …

---

## 27. 🟡 High Severity — Budibase: SSRF via OAuth2 Config Validation — Missing fetchWithBlacklist Protection

**CVE:** `CVE-2026-48146` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-g6qx-g4pr-92v7>

> ### Summary

The OAuth2 token fetch function in `packages/server/src/sdk/workspace/oauth2/utils.ts` (line 59) uses raw `fetch(config.url)` with **no SSRF protection**. The safe wrapper `fetchWithBlacklist()` exists in the same codebase and is used in every other outbound HTTP call (automation steps, plugin downloads, object store), but was **not applied** to the OAuth2 token endpoint.

A user with…

---

## 28. 🟡 High Severity — Budibase: SSRF via User-Controlled queryId in Automation Execute Query Step

**CVE:** `CVE-2026-48128` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-6964-pp88-6wp9>

> ### Summary

The executeQuery automation step in Budibase accepts a queryId from automation step inputs and passes it directly to the query execution controller without additional validation. When combined with a REST datasource configured to target internal infrastructure, this creates a server-side request forgery path where automation execution causes the Budibase server to make outbound HTTP r…

---

## 29. 🟡 High Severity — NIOExtras: NIOHTTPRequestDecompressor ratio limit bypass via inflated Content-Length

**CVE:** `CVE-2026-28975` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-6ph5-fww6-vfwv>

> ### Impact

When `NIOHTTPRequestDecompressor` is configured with `.ratio(N)`, the decompression limit is enforced using the `Content-Length` header value from the incoming request rather than the actual number of compressed bytes received. Since `Content-Length` is attacker-controlled, a malicious client can supply an inflated value that causes the ratio check to always pass, effectively disabling…

---

## 30. 🟡 High Severity — LangGraph has NoSQL parameter injection in MongoDBSaver, allowing cross-tenant state access

**CVE:** `CVE-2026-48121` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-98xf-r82g-9mhx>

> ## Summary

A NoSQL injection vulnerability existed in `MongoDBSaver` where checkpoint identifier fields from `config.configurable` were used in MongoDB queries without strict type enforcement. In vulnerable versions, attacker-controlled object payloads (for example MongoDB operators like `$gt` and `$ne`) could be interpreted as query operators instead of literal identifier values.

This could byp…

---

## 31. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
