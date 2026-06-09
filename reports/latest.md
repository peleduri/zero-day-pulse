# Zero Day Pulse

> **Generated:** 2026-06-09 08:58 UTC &nbsp;|&nbsp; **Total:** 33 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 19 &nbsp;|&nbsp; 🟡 High: 14 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE‑2024‑57727 is a directory‑traversal vulnerability in SimpleHelp Remote Support versions ≤5.5.7 that permits unauthenticated remote attackers to read arbitrary files via crafted file paths, enabling retrieval of logs, configuration files, and credentials.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit or PoC known.
- **Patch Available:** SimpleHelp 5.5.8 patch is available on the vendor download page.
- **Active Exploitation:** Yes, ransomware actors have actively exploited CVE‑2024‑57727 in the wild.
- **Threat Actors:** Ransomware actors (unspecified)
- **Mitigation:** Upgrade to SimpleHelp version 5.5.8 or later. If immediate upgrade is not possible, restrict remote access to the RMM service and apply network segmentation.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — CISA gives feds 3 days to patch Check Point VPN bug exploited as zero-day

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-check-point-flaw-exploited-by-ransomware-gangs/>

> CISA has ordered U.S. government agencies to secure their Check Point Remote Access VPN and Mobile Access deployments against a critical vulnerability exploited in zero-day attacks by Qilin ransomware affiliates. [...]

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-50751 is an authentication bypass vulnerability in Check Point Remote Access VPN that allows an unauthenticated attacker to bypass the normal login process and gain access to the VPN service.
- **Affected Products:** Check Point Remote Access VPN, Check Point Mobile Access
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploitation observed in the wild by Qilin ransomware affiliates; no public PoC or exploit code URL is known.
- **Patch Available:** Patch is available through Check Point's security advisory (URL unavailable).
- **Active Exploitation:** Confirmed active exploitation in the wild by Qilin ransomware affiliates, as reported by multiple sources.
- **Threat Actors:** Qilin ransomware affiliates
- **Mitigation:** Apply the Check Point security patch once released, enforce multi‑factor authentication, restrict VPN access to trusted IP ranges, and follow CISA guidance to secure Remote Access VPN and Mobile Access deployments.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — LiteLLM Flaw CVE-2026-42271 Exploited in the Wild, Chains to Unauthenticated RCE

**CVE:** `CVE-2026-42271` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://thehackernews.com/2026/06/litellm-flaw-cve-2026-42271-exploited.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Monday added a high-severity flaw impacting BerriAI LiteLLM to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

The vulnerability, tracked as CVE-2026-42271 (CVSS score: 8.7), is a command injection vulnerability that could allow any authenticated user to run arbitrary commands on the

**Parallel AI Enrichment:**

- **Technical Details:** Command injection vulnerability allowing an authenticated user to execute arbitrary commands on the host via LiteLLM’s request handling.
- **Affected Products:** LiteLLM (BerriAI LiteLLM) versions 1.74.2 through before 1.83.7
- **CVSS Score:** 8.7
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof-of-concept / exploit reports exist in media; specific PoC URL unavailable.
- **Patch Available:** Patch available in LiteLLM versions >= 1.83.7 (upgrade to 1.83.7 or later). Patch/advisory URL unavailable.
- **Active Exploitation:** Confirmed reports of active exploitation in the wild (media reports).
- **Threat Actors:** None known
- **Mitigation:** Upgrade LiteLLM to 1.83.7 or later; restrict access to the LiteLLM instance, enforce strong authentication, apply network segmentation, and monitor for suspicious commands.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — PHPSpreadsheet has a patch bypass for CVE-2026-34084 

**CVE:** `CVE-2026-45034` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-87m4-826x-3crx>

> ## Summary

CVE-2026-34084 was patched by the helper `File::prohibitWrappers`. The helper calls `parse_url($filename, PHP_URL_SCHEME)` and then checks `is_string($scheme) &amp;&amp; strlen($scheme) &gt; 1` to reject stream wrappers such as `phar://`, `php://`, `data://` or `expect://`. The check is not equivalent to &quot;does the path contain a wrapper&quot;. When the input has the form `phar:///…

**Parallel AI Enrichment:**

- **Technical Details:** A bypass exists in PHPSpreadsheet's File::prohibitWrappers helper; it calls parse_url($filename, PHP_URL_SCHEME) and checks is_string($scheme) && strlen($scheme) > 1 to reject stream wrappers. When an input uses a scheme with three or more slashes after the scheme (e.g., phar:///path/file.phar/inner), parse_url returns boolean false, skipping the is_string branch and allowing the wrapper to bypass the check.
- **Affected Products:** PHPSpreadsheet (specific affected versions: unspecified)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Public PoC availability unknown
- **Patch Available:** Yes — vendor advisory at https://github.com/advisories/GHSA-87m4-826x-3crx
- **Active Exploitation:** None known
- **Threat Actors:** None known
- **Mitigation:** Validate wrapper usage differently (do not rely solely on parse_url scheme result); normalize inputs and explicitly detect wrapper prefixes; apply vendor patch when available.
- **Vendor Advisory:** https://github.com/advisories/GHSA-87m4-826x-3crx

---

## 5. 🟠 Zero-Day — Critical Check Point VPN Zero-Day Exploited in the Wild (CVE-2026-50751)

**CVE:** `CVE-2026-50751` | `CVE-2026-50752` | `CVE-2024-24919` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://www.rapid7.com/blog/post/etr-critical-check-point-vpn-zero-day-exploited-in-the-wild-cve-2026-50751>

> Overview On June 8, 2026, Check Point published a security advisory for CVE-2026-50751 , a critical authentication bypass vulnerability affecting Check Point Remote Access VPN, Mobile Access, and Spark Firewall products. The vulnerability affects deployments configured to use the deprecated IKEv1 key exchange protocol where gateways accept legacy Remote Access clients and do not require a machine …

**Parallel AI Enrichment:**

- **Technical Details:** Improper authentication (CWE‑287) caused by a logic flow weakness in the IKEv1 implementation, permitting remote access clients to bypass credential checks when the gateway accepts legacy IKEv1 connections without requiring a machine certificate.
- **Affected Products:** Check Point Remote Access VPN, Check Point Mobile Access, Check Point Spark Firewall (deployments using deprecated IKEv1)
- **CVSS Score:** 9.3
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept or exploit is currently known.
- **Patch Available:** Patch released via vendor hotfix; see vendor advisory.
- **Active Exploitation:** Confirmed active exploitation reported by Check Point Research and Rapid7.
- **Threat Actors:** None known
- **Mitigation:** Apply the Check Point hotfix referenced in the advisory, disable IKEv1 usage, and require machine certificates for VPN connections. Until a patch is applied, restrict VPN access to clients using supported IKEv2.
- **Vendor Advisory:** http://blog.checkpoint.com/security/check-point-releases-important-hotfix-for-vulnerabilities-in-deprecated-ikev1-vpn-protocol

---

## 6. 🟠 Zero-Day — Gogs patches critical zero-day enabling remote code execution

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://www.bleepingcomputer.com/news/security/gogs-patches-critical-zero-day-enabling-remote-code-execution/>

> Gogs has patched a critical security zero-day flaw that can allow attackers to compromise Internet-facing instances and access any repositories (including private ones). [...]

**Parallel AI Enrichment:**

- **Technical Details:** The flaw is a path‑traversal via symlinks that bypasses a prior RCE fix, enabling attackers to overwrite arbitrary files outside the repository and achieve remote code execution.
- **Affected Products:** Gogs (self‑hosted Git service)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Proof of Concept available at http://github.com/zAbuQasem/gogs-CVE-2025-8110
- **Patch Available:** A patch is available; see https://www.bleepingcomputer.com/news/security/gogs-patches-critical-zero-day-enabling-remote-code-execution/
- **Active Exploitation:** Confirmed active exploitation; see Wiz Research, SecurityWeek, The Hacker News, and Bleeping Computer reports.
- **Threat Actors:** None known
- **Mitigation:** Apply the latest Gogs patch referenced in the Bleeping Computer article and upgrade to the patched version.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 7. 🟠 Zero-Day — Check Point links VPN zero-day attacks to Qilin ransomware gang

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://www.bleepingcomputer.com/news/security/check-point-links-vpn-zero-day-attacks-to-qilin-ransomware-gang/>

> Israeli cybersecurity company Check Point has released security updates to patch a critical flaw affecting Remote Access VPN and Mobile Access deployments, which was exploited in zero-day attacks. [...]

**Parallel AI Enrichment:**

- **Technical Details:** A logic flow/improper authentication weakness in certificate validation during the deprecated IKEv1 key exchange in Remote Access and Mobile Access components allows an unauthenticated remote attacker to bypass user authentication and establish a VPN session without a valid password. A related issue (CVE‑2026‑50752) affects certificate validation for site‑to‑site VPNs, enabling potential MITM attacks.
- **Affected Products:** Check Point Remote Access VPN, Mobile Access (SSL VPN), Spark Firewall, Quantum Security Gateway; versions: R80.20.X, R80.40, R81, R81.10, R81.20 Jumbo Hotfix Take 141 or below, R82 Jumbo Hotfix Take 103 or below, R82.10 Jumbo Hotfix Take 19 or below, Spark Firewall R80.20.X, R81.10.X, R82.00.X
- **CVSS Score:** 9.3
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC reported; exploitation has been observed in the wild but no public exploit is available.
- **Patch Available:** Patch available: Yes – Check Point released emergency hotfixes for CVE‑2026‑50751 and CVE‑2026‑50752 (see https://support.checkpoint.com/results/sk/sk185033).
- **Active Exploitation:** Yes – Check Point observed active exploitation beginning May 7 2026, with multiple reports confirming exploitation in the wild and linkage to the Qilin ransomware operation.
- **Threat Actors:** Qilin ransomware
- **Mitigation:** Remove support for legacy Remote Access client; configure Remote Access VPN authentication to IKEv2 only; require machine certificate authentication; enable IPS and download the latest signatures.
- **Vendor Advisory:** https://support.checkpoint.com/results/sk/sk185033

---

## 8. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when adversarial content placed in external corpora (web pages, documents, or retrieval sources) is retrieved by an LLM system (RAG or agentic browsing) and causes the model to follow malicious instructions — e.g., sandbox escape or data exfiltration demonstrated in end‑to‑end IPI exploits and the GeminiJack zero‑click vulnerability.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoCs reported in research (arXiv paper, Noma Labs writeup, Forcepoint report).
- **Patch Available:** Vendor advisory URL unavailable.
- **Active Exploitation:** Confirmed active exploitation reported in research and vendor blog posts; examples include the GeminiJack zero‑click exploit and other IPI payloads observed in the wild.
- **Threat Actors:** None known
- **Mitigation:** Follow vendor guidance: avoid trusting untrusted web content, harden retrieval/grounding pipelines, apply input sanitization, source‑filtering and provenance tracking.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 9. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) exploits the fact that large language models process data and tool outputs as part of a prompt. By embedding malicious instructions into those inputs, an attacker can steer the model’s response or actions, potentially without any explicit user query. The GeminiJack case demonstrates a zero‑click scenario where the injection occurs within Gemini Enterprise’s internal data handling.
- **Affected Products:** Google Workspace (Gemini app), Gemini Enterprise
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Proof‑of‑concept disclosed by Noma Labs (http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability).
- **Patch Available:** No official patch currently available; mitigation is provided via Google’s layered defense strategy.
- **Active Exploitation:** Yes. Reports of IPI payloads in the wild (Forcepoint) and a zero‑click exploit (GeminiJack) disclosed by Noma Labs show active exploitation.
- **Threat Actors:** None known
- **Mitigation:** Implement Google’s layered defense approach: validate and sanitize all data inputs to Gemini, isolate Gemini execution environments, monitor for anomalous tool usage, and enforce strict permission controls for integrations within Google Workspace.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 10. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection allows malicious sites or content to inject instructions into the context of agentic AI browsers, enabling data exfiltration or triggering further vulnerabilities when chained.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Public PoC available at http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability and referenced in the NVD CVE entry.
- **Patch Available:** No official patch available; Google provides layered defenses and mitigations described in the advisory.
- **Active Exploitation:** Confirmed active exploitation reported by Noma Labs (GeminiJack) and referenced in the NVD CVE entry.
- **Threat Actors:** None known
- **Mitigation:** Disable or restrict agentic browsing features; apply layered defenses including prompt‑injection filtering, origin‑access restrictions, and limiting unsafe AI actions as described by Google.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 11. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

---

## 12. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 13. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

---

## 14. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 15. 🟠 Zero-Day — Google patches new Chrome zero-day flaw exploited in the wild

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.bleepingcomputer.com/news/security/google-patches-fifth-chrome-zero-day-bug-exploited-in-attacks-this-year/>

> Google has released emergency updates to patch another Chrome zero-day vulnerability that has been exploited in the wild, the fifth such flaw patched since the start of the year. [...]

---

## 16. 🟠 Zero-Day — Google Patches 5th Chrome Zero-Day Exploited in 2026

**CVE:** `CVE-2026-11645` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.securityweek.com/google-patches-5th-chrome-zero-day-exploited-in-2026/>

> The vulnerability is tracked as CVE-2026-11645 and it was reported in late April by an anonymous researcher. The post Google Patches 5th Chrome Zero-Day Exploited in 2026 appeared first on SecurityWeek .

---

## 17. 🟠 Zero-Day — Dulwich has unbounded memory allocation in receive-pack from crafted thin packs

**CVE:** `CVE-2026-47734` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-xrvj-v92f-53gj>

> ## Impact

An uncontrolled-resource-consumption (memory exhaustion) denial-of-service vulnerability (CWE-400 / CWE-789).

A client with push access could push a tiny crafted thin pack (~174 bytes)  whose delta header declares a huge   dest_size. When dulwich ingested it via  add_thin_pack / apply_delta, it would  allocate hundreds of MB of memory based on that attacker-controlled size, with no rel…

---

## 18. 🟠 Zero-Day — ⚡ Weekly Recap: Instagram Account Hacks, Android Zero-Day, GitHub Worm and More

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://thehackernews.com/2026/06/weekly-recap-instagram-account-hacks.html>

> Monday again. The weekend was meant to be quiet. It wasn&#x27;t. Last week had poisoned packages, a broken AI helper, and a worm tearing through repos. The ugly part: basic tricks still worked.

A chatbot got fooled. A bot token got leaked inside the malware. The same old mistakes showed up again. And while everyone chased the loud stuff, quieter attackers sat in inboxes for months, reading mail a…

---

## 19. 🟠 Zero-Day — Everest Forms Vulnerability Exploited to Hack WordPress Sites

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://www.securityweek.com/everest-forms-vulnerability-exploited-to-hack-wordpress-sites/>

> The flaw allows attackers to execute arbitrary code remotely and has been exploited in the wild for two months. The post Everest Forms Vulnerability Exploited to Hack WordPress Sites appeared first on SecurityWeek .

---

## 20. 🟡 High Severity — SEC Consult SA-20260608-0 :: Privilege Escalation via Binary Planting in Genetec-provided RabbitMQ in multiple Genetec products

**CVE:** `CVE-2026-25112` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://seclists.org/fulldisclosure/2026/Jun/2>

> Posted by SEC Consult Vulnerability Lab via Fulldisclosure on Jun 08 SEC Consult Vulnerability Lab Security Advisory &lt; 20260608-0 &gt; ======================================================================= title: Privilege Escalation via Binary Planting product: Genetec-provided RabbitMQ in multiple Genetec products vulnerable version: Multiple products, see below. fixed version: Multiple prod…

---

## 21. 🟡 High Severity — Arc has an authenticated arbitrary local-file read via DuckDB I/O functions that bypasses RBAC table-level checks

**CVE:** `CVE-2026-47735` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-p2j4-c4g6-rpf5>

> ### Summary

Arc&#x27;s user-SQL validator (`internal/api/query.go:ValidateSQLRequest`) blocked only `read_parquet(` and `arc_partition_agg(` via regex denylist. The broader DuckDB I/O function family — `read_csv_auto`, `read_csv`, `read_json`, `read_json_auto`, `read_text`, `read_blob`, `glob`, `parquet_metadata`, `parquet_schema`, `read_xlsx`, etc. — was not blocked. RBAC table-reference extract…

---

## 22. 🟡 High Severity — nebula-mesh: GET /api/v1/audit-log discloses all entries to any operator

**CVE:** `CVE-2026-47726` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-qm33-p5p9-f8vg>

> `internal/api/audit.go:12` — `handleGetAuditLog` does no admin check. The route is bearer-auth gated only; any operator API key returns the full audit log via `store.ListAuditEntries` (up to limit=1000). This includes cross-tenant actor names, host/CA/operator IDs, action timestamps, and masked-IP entries from rate-limit refusals — enough surface for a tenant to enumerate the server&#x27;s activit…

---

## 23. 🟡 High Severity — nebula-mesh's web UI lacks CSRF tokens on /ui/* mutating endpoints

**CVE:** `CVE-2026-47725` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-273q-qgh5-wrj6>

> Every `/ui/*` POST / PUT / PATCH / DELETE route processes the request as soon as the session cookie validates. `SameSite=Lax` on the session cookie prevents most cross-site form submits but does not protect:

- top-level form-submit navigations from third-party pages (some browsers still send Lax cookies on top-level POSTs)
- same-registrable-domain attackers (sibling-subdomain XSS, subdomain take…

---

## 24. 🟡 High Severity — nebula-mesh: API endpoints lack ownership checks, enabling cross-operator privilege escalation

**CVE:** `CVE-2026-47724` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-598g-h2vc-h5vg>

> The `/api/v1/*` route surface trusts the bearer token alone for authorisation on most endpoints. The codebase itself admits this at `internal/api/hosts.go:384`: *&quot;API trusts the bearer token for authorisation; per-CA ownership is enforced only in the Web layer.&quot;*

The Web UI gates state-changing routes through `loadAccessibleCA` (`internal/web/cas.go`); CA-management endpoints in `intern…

---

## 25. 🟡 High Severity — nebula-mesh: Web UI and API responses lack security headers (CSP, X-Frame-Options, HSTS, etc.)

**CVE:** `CVE-2026-47723` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-w7w5-5gcp-38rw>

> None of the response paths in `internal/web/` or `internal/api/` set the standard browser-security headers. `grep` for `Content-Security-Policy`, `X-Frame-Options`, `Strict-Transport-Security`, `X-Content-Type-Options`, `Referrer-Policy` returns zero matches across the codebase.

## Impact
The admin UI signs CA certificates, mints API keys (returned inline once per page), displays TOTP QR codes, a…

---

## 26. 🟡 High Severity — nebula-mesh: Host advanced overrides allow YAML injection into agent config.yml

**CVE:** `CVE-2026-47722` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-7hp6-g3pq-3pc3>

> `internal/configgen/generator.go:86,108,119` interpolates the operator-supplied `ListenHost` and `TunDevice` fields raw into a `text/template` that produces the agent&#x27;s `config.yml`. `internal/web/advanced.go:20-35` accepts both with only `strings.TrimSpace` — no character or shape validation.

## Exploit
An operator (or attacker with any operator key, given the cross-tenant CRUD advisory) se…

---

## 27. 🟡 High Severity — FUXA: Unauthenticated SSRF via Socket.IO DEVICE_WEBAPI_REQUEST and DEVICE_PROPERTY with response reading

**CVE:** `CVE-2026-47719` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-w86f-rf9w-h3x6>

> ## Summary

An unauthenticated attacker (Alice) connects to FUXA&#x27;s Socket.IO endpoint and emits a `device-webapi-request` event whose `property.address` field names an arbitrary URL. FUXA&#x27;s `DEVICE_WEBAPI_REQUEST` handler at `server/runtime/index.js:296` calls `axios.get(address)` server-side and broadcasts the full response body back on the same event via `io.emit`. The companion handle…

---

## 28. 🟡 High Severity — Netty: Unix-socket fd receive leaks descriptors when peer sends two at once

**CVE:** `CVE-2026-45536` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-w573-9ffj-6ff9>

> netty_unix_socket_recvFd sets msg_control to `char control[CMSG_SPACE(sizeof(int))]` (line 940) — 24 bytes on 64-bit Linux. A peer-sent SCM_RIGHTS cmsg carrying two ints has cmsg_len = CMSG_LEN(8) = 24, which fits exactly with no MSG_CTRUNC, so the kernel installs both fds in the receiving process. The subsequent check `cmsg-&gt;cmsg_len == CMSG_LEN(sizeof(int))` (line 972, expected 20) fails, the…

---

## 29. 🟡 High Severity — Netty: HAProxy SSL TLV parsing leaks retained slice on invalid TLV length

**CVE:** `CVE-2026-44893` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-cc37-9q2j-3hfv>

> When decoding a PP2_TYPE_SSL TLV, HAProxyMessage.readNextTLV() first calls `header.retainedSlice(header.readerIndex(), length)` and only then reads the 1-byte client field and 4-byte verify field. If the attacker sets the TLV length below 5, the subsequent readByte/readInt throws IndexOutOfBoundsException. HAProxyMessageDecoder only catches HAProxyProtocolException around this call, so the IOOBE p…

---

## 30. 🟡 High Severity — Netty has Unbounded Direct Memory Consumption in its RedisDecoder

**CVE:** `CVE-2026-44890` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-6ghj-frrj-jjj3>

> ### Summary
An attacker can cause DoS by sending crafted Redis payloads across multiple connections without `\r\n`. This exhausts the server&#x27;s direct memory pool (OutOfDirectMemoryError), preventing legitimate connections from being processed.

### Details
io.netty.handler.codec.redis.RedisDecoder decodes the length of bulk strings and array headers using the `decodeLength` method. This metho…

---

## 31. 🟡 High Severity — Critical Check Point VPN Flaw Exploited to Bypass Passwords in IKEv1 Setups

**CVE:** `CVE-2026-50751` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://thehackernews.com/2026/06/critical-check-point-vpn-flaw-exploited.html>

> Check Point has warned of active exploitation of a critical vulnerability impacting Remote Access VPN and Mobile Access deployments that are configured to use the deprecated IKEv1 key exchange protocol.

The vulnerability, tracked as CVE-2026-50751 (CVSS score: 9.3), is a case of a logic flow weakness in certificate validation that allows an unauthenticated remote attacker to bypass user

---

## 32. 🟡 High Severity — GeoNode contains a server-side request forgery vulnerability in the service registration endpoint

**CVE:** `CVE-2026-39922` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-hw9r-6m78-w6h3>

> GeoNode versions 4.4.5 and 5.0.2 (and prior within their respective releases) contain a server-side request forgery vulnerability in the service registration endpoint that allows authenticated attackers to trigger outbound network requests to arbitrary URLs by submitting a crafted service URL during form validation. Attackers can probe internal network targets including loopback addresses, RFC1918…

---

## 33. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
