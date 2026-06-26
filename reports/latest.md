# Zero Day Pulse

> **Generated:** 2026-06-26 08:49 UTC &nbsp;|&nbsp; **Total:** 29 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 15 &nbsp;|&nbsp; 🟡 High: 14 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a directory/path traversal vulnerability that allows unauthenticated remote attackers to read arbitrary files on the server by traversing the file system.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know)
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors
- **Mitigation:** Apply the vendor patch and upgrade SimpleHelp to a version newer than 5.5.7; ensure systems are up to date and limit remote access.
- **Vendor Advisory:** http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — First-Ever Exploitation of PTC Windchill Vulnerability Discovered in the Wild

**CVE:** `CVE-2026-12569` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://www.securityweek.com/first-ever-exploitation-of-ptc-windchill-vulnerability-discovered-in-the-wild/>

> CISA has added the remote code execution flaw CVE-2026-12569 to its Known Exploited Vulnerabilities catalog. The post First-Ever Exploitation of PTC Windchill Vulnerability Discovered in the Wild appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Critical remote code execution via deserialization of untrusted data, allowing an unauthenticated attacker to execute arbitrary code on PTC Windchill and FlexPLM.
- **Affected Products:** PTC Windchill (PDMlink) and PTC FlexPLM, versions prior to 11.0 M030 (including 11.0 M030, 11.1 M020, 11.2.1, 12.0.2, 12.1.2, 13.0.2, 13.1.1, 13.1.2.8, 13.1.3.4)
- **CVSS Score:** 9.3
- **CVSS Vector:** CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:L/SI:L/SA:L/AU:Y/R:U/V:C/U:Red
- **Exploit Available:** false
- **Patch Available:** true (https://support.ptc.com/appserver/auth/it/esd/product.jsp?prodFamily=WPD)
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor‑provided patches for the affected versions (e.g., 13.1.2.8, 13.1.3.4, 13.0.2, 12.1.2, 12.0.2, 11.2.1, 11.1 M020, 11.0 M030) and follow the remediation guidance on the PTC advisory page.
- **Vendor Advisory:** https://www.ptc.com/en/about/trust-center/advisory-center/active-advisories/windchill-flexplm-rce-vulnerability?srsltid=AfmBOoqNdPLMuKneefANqjs5we48dM76E0OGt6aUODJllXcC0-R7dTZC

---

## 3. 🟠 Zero-Day — Google Details Turla's New STOCKSTAY Backdoor Used in Ukraine Espionage Attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://thehackernews.com/2026/06/google-details-turlas-new-stockstay.html>

> The Russian state-sponsored threat actor known as Turla has been attributed to a previously undocumented .NET backdoor called STOCKSTAY that has been deployed against government and military organizations in Ukraine, and entities that have an interest in Italian foreign policy.

Describing the Windows backdoor as continually developed by the hacking group, Google Threat Intelligence Group (

**Parallel AI Enrichment:**

- **Technical Details:** STOCKSTAY is a multi-component .NET backdoor written in C# using Windows Forms. It communicates via a secure WebSocket connection (websocket-sharp) and uses WM_COPYDATA IPC between components: a downloader (STOCKSTAY.MARKETMAKER) and modules STOCKBROKER (proxy tunneler), STOCKTRADER (information gathering), and STOCKMARKET (controller). The backdoor mimics legitimate programs such as stock market viewers, PDF viewers, and calculators.
- **Affected Products:** Microsoft Windows (with .NET Framework), WinRAR
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (source: https://thehackernews.com/2026/06/google-details-turlas-new-stockstay.html)
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true (source: https://thehackernews.com/2026/06/google-details-turlas-new-stockstay.html)
- **Threat Actors:** Turla
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — LangGraph Checkpoint: Unsafe JSON deserialization in checkpoint loading

**CVE:** `CVE-2026-48775` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-fjqc-hq36-qh5p>

> ## Summary

LangGraph&#x27;s `JsonPlusSerializer` can reconstruct Python objects from JSON checkpoint payloads. Under conditions where someone could modify checkpoint bytes at rest in the backing store, the deserialization path could reconstruct objects beyond what the application expects, which could in turn result in code execution at checkpoint load time.

This is a defense-in-depth issue. The …

**Parallel AI Enrichment:**

- **Technical Details:** LangGraph's JsonPlusSerializer can reconstruct Python objects from JSON checkpoint payloads; if checkpoint bytes can be modified, deserialization can reconstruct arbitrary objects leading to code execution at checkpoint load time.
- **Affected Products:** LangGraph SQLite Checkpoint (versions prior to 4.1.1)
- **CVSS Score:** 6.8
- **CVSS Vector:** CVSS:3.1/AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (https://github.com/langchain-ai/langgraph/security/advisories/GHSA-fjqc-hq36-qh5p)
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Upgrade to LangGraph version 4.1.1 or later, which fixes the issue; restrict write access to checkpoint storage and ensure integrity of checkpoint files.
- **Vendor Advisory:** https://github.com/langchain-ai/langgraph/security/advisories/GHSA-fjqc-hq36-qh5p

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is a technique where an attacker embeds malicious prompts in data processed by an LLM, causing the model to execute unintended instructions. In the GeminiJack case, a zero‑click vulnerability in Google Gemini Enterprise allowed an attacker to inject a hidden prompt via indirect means, hijacking the AI agent.
- **Affected Products:** Google Gemini Enterprise
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability)
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Implement input and output validation and sanitization, enforce human oversight, monitor for suspicious prompt patterns, and continuously update security controls for AI agents.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack where malicious instructions are embedded in secondary data sources (e.g., shared documents, emails, APIs) that the LLM processes, causing unintended behavior without direct user input.
- **Affected Products:** Google Workspace, Google Gemini (including Gemini Enterprise)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Google employs a defense‑in‑depth, layered strategy including context segmentation, input attribution, prompt sanitisation, deterministic defenses (user confirmation, URL sanitisation), ML‑based classifiers, LLM‑based prompt engineering, model hardening, continuous monitoring, synthetic data generation, and human‑in‑the‑loop review.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection occurs when malicious sites embed payloads that cause the AI agent to execute unintended instructions, leading to data leakage or arbitrary actions.
- **Affected Products:** Google Chrome (Gemini AI agentic browsing), Google Gemini Enterprise
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true (http://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads)
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** true (http://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads)
- **Threat Actors:** Threat actors unknown
- **Mitigation:** New architecture introduced by Google to mitigate indirect prompt injection risk
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Adopt Rust for new code to reduce memory safety vulnerabilities.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: hidden malicious instructions embedded in external data sources (emails, documents, web pages, calendar invites, metadata) that are ingested by AI/LLM-based systems and cause them to perform unintended or malicious actions (exfiltration, unauthorized transactions, data destruction, navigation). Attackers use concealment (CSS display:none, HTML comments, metadata, system-tag spoofing) and authoritative framing to evade human detection and weaponize agentic AI.
- **Affected Products:** Google Gemini, Google Workspace (Gemini integration)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: model hardening with adversarial training (Gemini 2.5), purpose-built ML detectors for malicious instructions, security thought reinforcement (prompt-level guards), markdown/HTML sanitization and suspicious-URL redaction, system-level safeguards and confirmation dialogs, end-user mitigation notifications, continuous monitoring and telemetry, red-teaming and BugSWAT/VRP collaboration, and adoption of secure AI frameworks (SAIF).
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Chinese state-sponsored actors exploit network-device CVEs to compromise backbone, provider edge, and customer edge routers, modify firmware for persistent access, and pivot through compromised devices to other networks.
- **Affected Products:** backbone routers, provider edge (PE) routers, customer edge (CE) routers, network edge devices
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Apply detection tips and hardening guidance from CISA, monitor for IOCs, segment and isolate router infrastructure, and implement strict access controls until patches are released.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 11. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 12. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 13. 🟠 Zero-Day — LangGraph SDK has unsafe URL path construction

**CVE:** `CVE-2026-48776` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-w39p-vh2g-g8g5>

> ## Summary

`langgraph-sdk` constructs HTTP request paths for resource operations by interpolating caller-supplied identifier values into URL templates. Without sanitization of those values, identifiers that contain characters with special meaning in URL paths could cause the resulting request to address a different resource (and potentially a different resource type) than the SDK method&#x27;s ca…

---

## 14. 🟠 Zero-Day — New macOS malware embeds fake errors to confuse AI analysis tools

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://www.bleepingcomputer.com/news/security/new-macos-malware-embeds-fake-errors-to-confuse-ai-analysis-tools/>

> A newly discovered macOS malware dubbed &quot;Gaslight&quot; is designed to confuse AI-assisted malware analysis tools by hiding prompt injection strings and fake debugging data within the executable. [...]

---

## 15. 🟠 Zero-Day — New Gaslight macOS Malware Uses Prompt Injection to Disrupt AI-Assisted Analysis

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://thehackernews.com/2026/06/new-gaslight-macos-malware-uses-prompt.html>

> A previously undocumented Rust-based macOS implant and information stealer has been found to embed a prompt injection payload designed to trick a malware analyst&#x27;s artificial intelligence (AI) tools and trick it into aborting or refusing an analysis of the artifact.

The malware has been codenamed Gaslight owing to this deceptive behavior. It&#x27;s been assessed with high confidence that the…

---

## 16. 🟡 High Severity — Lemur: ACME SSRF + creator-equality IDOR lead to AWS IAM/PKI compromise

**CVE:** `CVE-2026-55166` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-v2wp-frmc-5q3v>

> &lt;!-- obsidian --&gt;&lt;h1 data-heading=&quot;Lemur 1.9.0: any SSO-authenticated user achieves AWS IAM compromise and permanent PKI key access via ACME acme_url SSRF and creator-equality IDOR&quot;&gt;Lemur 1.9.0: any SSO-authenticated user achieves AWS IAM compromise and permanent PKI key access via ACME acme_url SSRF and creator-equality IDOR&lt;/h1&gt;
&lt;h2 data-heading=&quot;Vulnerability…

---

## 17. 🟡 High Severity —  Lemur: JWT verifier honors attacker-supplied alg, enabling ATO

**CVE:** `CVE-2026-55165` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-r9gp-7f88-9r54>

> &lt;!-- obsidian --&gt;&lt;h1 data-heading=&quot;Lemur 1.9.0: JWT verifier trusts attacker-supplied alg from token header — defense-in-depth gap; chain-dependent ATO with secret disclosure&quot;&gt;Lemur 1.9.0: JWT verifier trusts attacker-supplied alg from token header — defense-in-depth gap; chain-dependent ATO with secret disclosure&lt;/h1&gt;
&lt;h2 data-heading=&quot;Vulnerability Summary&quo…

---

## 18. 🟡 High Severity — Lemur Privilege Escalation: Non-admin role members can rewrite role membership via PUT /api/1/roles/<id>

**CVE:** `CVE-2026-55163` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-x3vf-mgxj-7785>

> ## Summary
 
The `PUT /api/1/roles/&lt;id&gt;` handler in `lemur/roles/views.py` gates only on `RoleMemberPermission(role_id).can()`, which is satisfied for any user who is already a member of the target role. The handler then passes `data[&quot;users&quot;]` and `data[&quot;name&quot;]` directly to `service.update()`, permitting any role member to rewrite that role&#x27;s membership list and name…

---

## 19. 🟡 High Severity — Lemur: Crafted CRL/OCSP URLs in uploaded certificates lead to post-authentication SSRF

**CVE:** `CVE-2026-55162` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-54vg-pfh7-jq95>

> ## Summary
 
When verifying an uploaded certificate, `lemur/certificates/verify.py` extracts the CRL Distribution Point URL and the OCSP responder URL directly from the certificate&#x27;s extensions and issues outbound requests to those URLs without scheme restriction or destination allow-listing. An authenticated user holding the operator role (required by `StrictRolePermission` on `POST /certifi…

---

## 20. 🟡 High Severity — GitHub MCP Server: Lockdown mode singleton in HTTP server causes cross-user GraphQL client confusion

**CVE:** `CVE-2026-48529` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-pjp5-fpmr-3349>

> ### Summary

When running in HTTP mode with --lockdown-mode enabled, the RepoAccessCache is implemented as a process-global singleton initialized with the first authenticated user&#x27;s GraphQL client. All subsequent requests from different users share this singleton and their lockdown-related GraphQL queries are executed using the first user&#x27;s credentials. The singleton is never updated to …

---

## 21. 🟡 High Severity — MessagePack-CSharp: DynamicUnionResolver-generated deserializers miss depth enforcement

**CVE:** `CVE-2026-48513` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-wfr3-xj75-pfwh>

> ## Summary

Runtime-generated union deserializers emitted by `DynamicUnionResolver` do not call `MessagePackSecurity.DepthStep(ref reader)` and do not decrement `reader.Depth` around recursive deserialization and skip paths.

This means union deserialization does not consistently participate in the maximum object graph depth enforcement that protects other recursive formatter paths. For unknown un…

---

## 22. 🟡 High Severity — Lemur has an authorization bypass in StrictRolePermission / AuthorityCreatorPermission

**CVE:** `CVE-2026-48508` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-qcqw-jwxc-2hqg>

> ## Summary

`StrictRolePermission` and `AuthorityCreatorPermission` in `lemur/auth/permissions.py` call `flask_principal.Permission.__init__()` with zero `Need`s when their config flags are unset. Both flags defaulted to `False` in code prior to the fix, so this was the state of any Lemur install that hadn&#x27;t explicitly opted in.

Flask-Principal&#x27;s `Permission.allows()` returns `True` whe…

---

## 23. 🟡 High Severity — amazon-braket-sdk vulnerable to Insecure Deserialization via pickle.loads()

**CVE:** `CVE-2026-9291` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-g697-2xrc-gc46>

> **Summary**
Amazon Braket SDK is an open-source Python library for interacting with the Amazon Braket quantum computing service, including managing hybrid quantum jobs and retrieving job results. An issue exists where, under certain circumstances, a remote authenticated user with S3 write access to a Braket job output bucket can achieve arbitrary code execution by exploiting insecure deserializati…

---

## 24. 🟡 High Severity — i18next-fs-backend vulnerable to prototype pollution via crafted missing-key string

**CVE:** `CVE-2026-48713` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-2933-q333-qg83>

> ### Impact

`i18next-fs-backend` ≤ 2.6.5, when used to persist missing translation keys (e.g. via `i18next-http-middleware`&#x27;s `missingKeyHandler` exposed to untrusted input), is vulnerable to prototype pollution via crafted missing-key strings.

`Backend.writeFile()` splits each queued missing-key string on the configured `keySeparator` (default `.`) before calling the internal `setPath()` wa…

---

## 25. 🟡 High Severity — i18next-http-middleware: MissingKeyHandler does not reject keys whose segments contain prototype-polluting names

**CVE:** `CVE-2026-48714` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-f49m-vf83-692w>

> ### Impact

`i18next-http-middleware` ≤ 3.9.6&#x27;s `missingKeyHandler` blocked the literal request-body keys `__proto__`, `constructor`, and `prototype` (added in 3.9.3, see GHSA-5fgg-jcpf-8jjw), but did not reject dotted variants such as `&quot;__proto__.polluted&quot;`. Downstream backends that split the missing-key string on a configured `keySeparator` (notably `i18next-fs-backend` ≤ 2.6.5) h…

---

## 26. 🟡 High Severity — OpenAM: Unauthenticated Authentication Bypass via RADIUS Spoofing

**CVE:** `CVE-2026-46560` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-386j-6m86-78f9>

> ## Summary

**Description**

An Improper Verification of Cryptographic Signature (CWE-347) issue in OpenAM&#x27;s RADIUS authentication module allows an unauthenticated network attacker to spoof an Access-Accept response and obtain an OpenAM session for any RADIUS username, without knowing the configured shared secret. This affects OpenAM Community Edition through version 16.0.6 and was patched in…

---

## 27. 🟡 High Severity — @anthropic-ai/claude-code has an Insecure Temporary File in /copy Command that Enables Response Disclosure and Symlink-Based File Write

**CVE:** `CVE-2026-46406` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-4vp2-6q8c-pvq2>

> The Claude Code `/copy` command wrote responses to a hardcoded, predictable path (`/tmp/claude/response.md`) without UID isolation, randomness, or symlink protection. The file was created world-readable (0644) in a world-traversable directory (0755), allowing any local user to read a privileged user&#x27;s Claude response, which could contain secrets or credentials. Additionally, because the path …

---

## 28. 🟡 High Severity — OpenAM has Unsafe Java Deserialization via SNS

**CVE:** `CVE-2026-45794` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-pp89-732f-3g8q>

> ## Summary

**Description**

A Deserialization of Untrusted Data (CWE-502) issue exists in OpenAM&#x27;s Push Notification SNS callback resource. The REST route that handles SNS push messages is mounted with anonymous access and, when a supplied message identifier has expired from the in-memory dispatcher, falls back to a CTS-stored predicate blob whose top-level keys are treated as Java class nam…

---

## 29. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
