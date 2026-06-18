# Zero Day Pulse

> **Generated:** 2026-06-18 10:04 UTC &nbsp;|&nbsp; **Total:** 33 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 15 &nbsp;|&nbsp; 🟡 High: 18 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE‑2024‑57727 is a directory‑traversal flaw in SimpleHelp remote support software that lets unauthenticated attackers read sensitive files by manipulating file paths.
- **Affected Products:** SimpleHelp remote support software version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept or exploit is known.
- **Patch Available:** No official patch has been released yet.
- **Active Exploitation:** Confirmed active exploitation reported by CISA.
- **Threat Actors:** Ransomware actors (unspecified groups)
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — Hostile states behind three-quarters of attacks on Britain's critical infrastructure, cyber chief warns

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Record by Recorded Future &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://therecord.media/britain-nation-state-cyberattacks-richard-horne-rusi>

> NCSC CEO Richard Horne warned that “kinetic targeting in any conflict tomorrow will be based on intelligence gathered today” and that nation-state adversaries were “prepositioning” throughout British critical infrastructure.

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or exploit reported.
- **Patch Available:** Patch information unavailable.
- **Active Exploitation:** No confirmed active exploitation of a specific CVE reported.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable; general advice implied: strengthen digital resilience, hardening of critical infrastructure, reduce exposure to nation‑state prepositioning.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — Microsoft Confirms RoguePlanet Defender Zero-Day, Says Patch is in Development

**CVE:** `CVE-2026-50656` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://thehackernews.com/2026/06/microsoft-confirms-rogueplanet-defender_02022423645.html>

> Microsoft has formally disclosed that it&#x27;s working to release a patch to address a Defender zero-day codenamed RoguePlanet.

The vulnerability has now been assigned the CVE identifier CVE-2026-50656 (CVSS score: 7.8), with the tech giant describing it as a privilege escalation flaw.

&quot;Microsoft is aware of an elevation of privilege in the Microsoft Malware Protection Engine in Microsoft …

**Parallel AI Enrichment:**

- **Technical Details:** Race condition/elevation-of-privilege in the Microsoft Malware Protection Engine (Defender) that abuses the quarantine/scan pipeline to elevate a local unprivileged user to SYSTEM.
- **Affected Products:** Microsoft Defender / Microsoft Malware Protection Engine on Windows 10 and Windows 11
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC exists at http://github.com/MSNightmare/RoguePlanet.
- **Patch Available:** Patch not yet released; Microsoft says patch in development.
- **Active Exploitation:** Confirmed reports of active exploitation in the wild.
- **Threat Actors:** None known
- **Mitigation:** No official patch yet; general mitigations include disabling Microsoft Defender real‑time components temporarily where acceptable, applying principle of least privilege, restricting local untrusted accounts, and monitoring Defender‑related processes and quarantine operations; seek vendor advisory and apply patch when released.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — Malicious JetBrains Plugins Steal AI API Keys as Chrome Extensions Capture Chatbot Chats

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://thehackernews.com/2026/06/malicious-jetbrains-plugins-steal-ai.html>

> Cybersecurity researchers have flagged a &quot;coordinated malware campaign&quot; on the JetBrains Marketplace that has published no less than 15 malicious plugins capable of exfiltrating artificial intelligence (AI) provider keys.

&quot;Every plugin poses as an AI coding assistant built on DeepSeek and other large language models, offering chat, commit messages, code review, bug finding, and uni…

**Parallel AI Enrichment:**

- **Technical Details:** Malicious plugins harvested API keys entered into plugin settings and exfiltrated them in plaintext via HTTP to attacker C2 (IP 39.107.60[.]51). Plugins also installed a JVM‑wide X509TrustManager to weaken TLS checks and returned attacker‑supplied API keys to paying users.
- **Affected Products:** JetBrains Marketplace third‑party IDE plugins (all versions published prior to removal)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit reported
- **Patch Available:** JetBrains removed the 15 plugins from Marketplace, banned publishers, remotely disabled installed copies via a backend kill‑switch; no separate patch required.
- **Active Exploitation:** Confirmed active data theft (keys exfiltrated) reported by Aikido Security and disclosed by JetBrains; activity observed since Oct 2025 through June 10, 2026.
- **Threat Actors:** None known
- **Mitigation:** Remove the listed plugins, revoke and rotate any AI provider API keys entered into them, inspect provider usage/billing, block outbound traffic to 39.107.60[.]51, scan repos for leaked keys, and adopt least‑privilege/scoped tokens or JetBrains ACP agents.
- **Vendor Advisory:** https://blog.jetbrains.com/platform/2026/06/marketplace-ecosystem-security-update-malicious-ai-plugins/

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when untrusted web content contains adversarial instructions that influence an AI agent's prompts or context (e.g., hidden webpage text or crafted snippets in retrieved documents), causing the agent to execute attacker‑controlled directives. It affects RAG and agentic systems that incorporate external corpora and web browsing.
- **Affected Products:** AI agents, retrieval‑augmented generation (RAG) systems, and agentic systems that incorporate external web content; specific product names not listed.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof‑of‑concept indirect prompt injection payloads observed; see Forcepoint blog (https://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads).
- **Patch Available:** No official vendor patch released; mitigation guidance available at Google Security Blog (https://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html) and Google Prompt Injection Blog (https://blog.google/security/prompt-injections-web).
- **Active Exploitation:** Confirmed in‑the‑wild occurrences of indirect prompt injection payloads were reported by Google Security Blog, Google prompt injection posts, Forcepoint X‑Labs, and Noma Labs (GeminiJack).
- **Threat Actors:** None known
- **Mitigation:** Reduce trust in external content, sanitize and filter retrieved documents, enforce strict prompt templates that ignore injected instructions, use provenance and source filtering, continuously monitor for IPI patterns, and apply vendor‑provided guidance from Google blogs and Forcepoint report.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) injects malicious instructions into auxiliary data sources or tools used by an LLM (e.g., documents, web results, connectors). When the model consults those sources during query completion or when agentic automation invokes tools, the injected instructions can influence model behavior (including without user input), causing it to execute attacker‑controlled actions or reveal sensitive data.
- **Affected Products:** Google Workspace (Workspace apps integrating Gemini/GenAI)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Proof‑of‑concept / zero‑click demonstration (GeminiJack) reported by Noma Labs; see http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability
- **Patch Available:** No vendor patch released; mitigations are detailed in the advisory.
- **Active Exploitation:** No confirmed widespread active exploitation reported; niche research demonstrations reported (GeminiJack).
- **Threat Actors:** None known
- **Mitigation:** Apply Google's layered defenses: input provenance tagging, content sanitization, strict tool/data scoping, behavioral monitoring and anomaly detection, reinforcement of agent orchestration controls, least‑privilege for connected data sources, and continuous monitoring/updates.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability can be triggered when chained with indirect prompt injection; further technical specifics are not disclosed.
- **Affected Products:** Google Chrome (agentic browsing/Gemini integration) – fixed in version 1.3
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC reported.
- **Patch Available:** Fixed in version 1.3; see https://nvd.nist.gov/vuln/detail/CVE-2025-54131
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Apply architectural limits to agent data access and defenses against indirect prompt injection as described in the Google Security Blog; upgrade to Chrome version 1.3 or later when available.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is a race condition in an unsafe block of the Rust‑based android binder driver (rust_binder) within the Linux kernel, where simultaneous operations on the driver’s death_list can lead to corrupted state.
- **Affected Products:** Linux kernel (rust_binder component)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit known.
- **Patch Available:** A patch has been released in the Linux kernel update addressing the rust_binder race condition (see NVD entry).
- **Active Exploitation:** No active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Update the Linux kernel to a version that includes the rust_binder race‑condition fix.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injections embed hidden malicious instructions within external data sources (e.g., emails, documents, calendar invites). When processed by an LLM, these instructions can cause the model to exfiltrate data or perform unauthorized actions. Google’s layered defense mitigates this by hardening the model, reinforcing security‑focused prompts, sanitizing markdown, and redacting suspicious URLs.
- **Affected Products:** Gemini 2.5 models, upcoming Gemini models (Gemini in Google Workspace, Gemini app)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public exploits have been reported, including the EchoLeak CVE‑2025‑32711 and documented in‑the‑wild prompt injection payloads.
- **Patch Available:** No official patch has been released; Google uses a continuous layered security approach instead.
- **Active Exploitation:** Yes. Researchers identified 10 in‑the‑wild prompt injection payloads (April 2026) and Google reported a 32% increase in malicious indirect prompt injection detections between November 2025 and February 2026.
- **Threat Actors:** None known
- **Mitigation:** Model hardening (adversarial data training for Gemini 2.5), security thought reinforcement (targeted security instructions), markdown sanitization and suspicious URL redaction, end‑user security mitigation notifications.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors exploit known CVEs in internet‑facing network devices (e.g., CVE‑2023‑20198, CVE‑2023‑20273, CVE‑2024‑21887, CVE‑2018‑0171) to obtain initial access, then create local admin accounts, enable SSH, add authorized keys, deploy Guest Shell containers, execute Tcl scripts, and establish tunnels (GRE/mGRE/IPsec) for data exfiltration and C2. They also mirror traffic via SPAN/RSPAN/ERSPAN and use multi‑hop STOWAWAY relays.
- **Affected Products:** Cisco IOS XE (Web UI, Smart Install) – fixed in 17.9.4a, 17.6.6a, 17.3.8a, 16.12.10a; Palo Alto Networks PAN‑OS (GlobalProtect) – fixed in 10.2.9‑h1, 11.0.4‑h1, 11.1.2‑h3; Ivanti Connect Secure / Policy Secure – patches for 9.x/22.x; additional routers/firewalls/VPNs such as Fortinet, Juniper, Nokia, Sierra Wireless, SonicWall (versions listed in CISA appendix).
- **CVSS Score:** -9999.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof‑of‑concepts for the individual CVEs are known to exist, but specific URLs are not enumerated in the sources.
- **Patch Available:** Vendor patches are available for Cisco IOS XE (17.9.4a, 17.6.6a, 17.3.8a, 16.12.10a), Palo Alto Networks PAN‑OS (10.2.9‑h1, 11.0.4‑h1, 11.1.2‑h3), Ivanti Connect Secure / Policy Secure (9.x/22.x) and Cisco Smart Install mitigations.
- **Active Exploitation:** Yes – CISA reports confirmed active exploitation of the publicly disclosed CVEs by the identified threat actors.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching known exploited CVEs; disable unnecessary management interfaces (e.g., HTTP/Web UI, Smart Install), restrict management ports and ACLs, enforce strong credentials and public‑key authentication, monitor for tunneling/mirroring/unexpected ACLs, verify firmware integrity and hashes, hunt for persistence mechanisms (new local admin accounts, SSH keys, Guest Shell containers).
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 11. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 12. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

---

## 13. 🟠 Zero-Day — Introducing the Red Agent POV Series

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Wiz Research &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://www.wiz.io/blog/red-agent-pov-series>

> An inside look at how the Red Agent, our AI-Powered Attacker, uncovers complex, exploitable risks in the wild

---

## 14. 🟠 Zero-Day — The Top 10 Attack Surface Exposures in 2026

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://thehackernews.com/2026/06/the-top-10-attack-surface-exposures-in.html>

> Breaches don&#x27;t always start with a zero-day. An exposed admin panel can get brute-forced, or credentials reused from a previous attack. But when a vulnerability does drop — like MongoBleed earlier this year, which let attackers pull credentials and session tokens from server memory without authentication — anything internet-facing is immediately at risk.

With time-to-exploit now down to a

---

## 15. 🟠 Zero-Day — CISA orders feds to patch max severity Joomla plugin flaw by Friday

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-max-severity-joomla-plugin-flaw-by-friday/>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has ordered federal agencies to patch a maximum-severity flaw in the Widget Factory Joomla Content Editor (JCE) plugin that is being actively exploited in the wild. [...]

---

## 16. 🟡 High Severity — Oracle June 2026 Critical Security Patch Update Addresses 243 CVEs (CVE-2026-35273)

**CVE:** `CVE-2026-35273` &nbsp;|&nbsp; **Source:** Tenable Security Research &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://www.tenable.com/blog/oracle-june-2026-critical-security-patch-update-addresses-243-cves-cve-2026-35273>

> Oracle addresses 243 CVEs in its June 2026 Critical Security Patch Update with 245 patches, including 122 critical updates. Key Takeaways The June 2026 Critical Security Patch Update (CSPU) contains fixes for 243 unique CVEs in 245 security updates 122 issues (49.8% of all patches) were assigned a critical severity rating Oracle Fusion Middleware received the highest number of patches at 106, acco…

---

## 17. 🟡 High Severity — Avo: Missing Authorization in Avo Association Attach Endpoint Allows Unauthorized Relationship Manipulation and Privilege Escalation

**CVE:** `CVE-2026-55518` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-8fq9-273g-6mrg>

> ## Summary

A critical missing authorization flaw exists in Avo&#x27;s association attach workflow. The UI and `GET /resources/:resource/:id/:related/new` path can check `attach_&lt;association&gt;?`, but the actual write endpoint, `POST /resources/:resource/:id/:related`, does not run the same authorization check before mutating the association.

As a result, an authenticated low-privileged Avo u…

---

## 18. 🟡 High Severity — HAPI FHIR: XXE in XsltUtilities.saxonTransform via unhardened Saxon TransformerFactory

**CVE:** `CVE-2026-55471` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-2f55-g35j-5jmf>

> ### Summary

`org.hl7.fhir.utilities.XsltUtilities` exposes two parallel families of XSLT
transform helpers. The `transform(...)` overloads obtain their
`TransformerFactory` from the project&#x27;s hardened helper
`XMLUtil.newXXEProtectedTransformerFactory()` (which sets
`ACCESS_EXTERNAL_DTD=&quot;&quot;` and `ACCESS_EXTERNAL_STYLESHEET=&quot;&quot;`). The sibling
`saxonTransform(...)` overloads i…

---

## 19. 🟡 High Severity — LangChain4j: SQL injection via metadata filters in langchain4j-mariadb and langchain4j-pgvector

**CVE:** `CVE-2026-55405` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-2mfg-cc43-9pcj>

> ### Summary
The MariaDB and pgvector embedding stores build metadata-filter SQL by string-concatenating
filter **keys** (and, in MariaDB, string **values**) directly into the query without adequate
escaping. A crafted metadata key in `EmbeddingSearchRequest.filter()` can break out of its SQL
context and inject arbitrary SQL into the statements executed by the stores&#x27; search and
`removeAll(Fil…

---

## 20. 🟡 High Severity — Capsule: Incomplete fix of CVE-2026-30963: singular/plural typo leaves namespaces/finalize unprotected

**CVE:** `CVE-2026-55636` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-gwxr-7h77-7777>

> ### Summary
Capsule v0.13.2 webhook rules contain `namespace/finalize` (singular) instead of `namespaces/finalize` (plural). K8s requires plural. The finalize defense from CVE-2026-30963 fix is absent.

### Details
PUT to `/api/v1/namespaces/&lt;ns&gt;/finalize` has resource=namespaces (plural). The singular rule never matches. `matchPolicy: Equivalent` does not compensate.

### PoC
Confirmed on k…

---

## 21. 🟡 High Severity — webpack-dev-server vulnerable to HMR WebSocket interception via permissive user proxies

**CVE:** `CVE-2026-9595` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-mx8g-39q3-5c79>

> ### Impact

When a user-configured proxy on `webpack-dev-server` has a broad context (e.g. `/`) and `ws: true`, it also intercepts the dev server&#x27;s own HMR WebSocket and forwards it to the proxy target. This leaks the browser&#x27;s cookies and `Origin` header to the backend, bypasses the dev server&#x27;s Host/Origin validation, and corrupts the HMR socket (both HMR and the proxy end up writ…

---

## 22. 🟡 High Severity — Gitea: API Fork Missing CanCreateOrgRepo Check Allows Org Secret Exfiltration

**CVE:** `CVE-2026-22555` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-fhx7-m96w-mv29>

> ## Summary

The API endpoint `POST /api/v1/repos/{owner}/{repo}/forks` only checks `IsOrgMember()` when a user forks a repository into an organization, but does not check `CanCreateOrgRepo()`. The web UI fork handler correctly checks both. This allows a read-only organization member — in a team with `can_create_org_repo=false` — to create repositories in the organization namespace via the API. The…

---

## 23. 🟡 High Severity — Daytona: Cross-tenant data leak in notification WebSocket gateway via unverified organizationId join

**CVE:** `CVE-2026-54324` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-qwxf-2m7m-2m3x>

> ### Summary
A cross-tenant authorization flaw in Daytona&#x27;s notification WebSocket gateway allowed any authenticated user to subscribe to another organization&#x27;s realtime notification channel and passively receive that organization&#x27;s events.

### Impact
The notification gateway&#x27;s JWT handshake joined a client-supplied organization identifier to the corresponding notification room…

---

## 24. 🟡 High Severity — Open WebUI: SSRF Protection Bypass in Playwright Web Loader via HTTP Redirects

**CVE:** `CVE-2026-54018` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-jrfp-m64g-pcwv>

> ### Summary
The SafePlaywrightURLLoader implements a validate_url function to prevent SSRF attacks by checking the IP address of the user-provided URL. However, this validation is performed only on the initial URL.

Since Playwright automatically follows HTTP redirects (301/302) by default, an attacker can bypass the validation by providing a safe URL that redirects to a restricted internal networ…

---

## 25. 🟡 High Severity — Open WebUI: Path traversal / SSRF in terminal server proxy via encoded path traversal

**CVE:** `CVE-2026-54017` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-r2wg-2mcr-66rv>

> ### Summary

The terminal-server reverse proxy in `backend/open_webui/routers/terminals.py` does not fully confine the user-controlled `path` segment before forwarding it to an admin-configured terminal server. An authenticated user who has been granted access to a terminal server can craft `path` values containing encoded `../` traversal sequences that escape the intended path (or policy) scope o…

---

## 26. 🟡 High Severity — OpenClaw: MCP Streamable HTTP redirects could forward configured custom headers to another origin

**CVE:** `CVE-2026-53840` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-rjxq-qqhf-8hwh>

> ### Summary

OpenClaw supports remote MCP Streamable HTTP servers with operator-configured custom headers. In affected releases, those headers could be forwarded when the MCP endpoint responded with a cross-origin redirect.

This issue is limited to configured MCP Streamable HTTP servers that use custom headers. It does not expose unrelated OpenClaw credentials.

### Affected configurations

This …

---

## 27. 🟡 High Severity — Open WebUI: Redirect-Bypass SSRF in OAuth `_process_picture_url` (incomplete-fix sibling of CVE-2026-45401)

**CVE:** `CVE-2026-54008` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-226f-f24g-524w>

> ## Summary

`backend/open_webui/utils/oauth.py::_process_picture_url` (v0.9.5, lines 1435-1470) calls `validate_url(picture_url)` on the initial URL only, then invokes `aiohttp.ClientSession.get(picture_url, ...)` without `allow_redirects=False`. aiohttp&#x27;s default is `allow_redirects=True, max_redirects=10`; the function does not pass the project&#x27;s `AIOHTTP_CLIENT_ALLOW_REDIRECTS` env co…

---

## 28. 🟡 High Severity — NocoDB: Refresh Tokens Persist Through Password Recovery

**CVE:** `CVE-2026-53928` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-r989-7g3j-wjhw>

> ### Summary
A stolen refresh token survived a password-forgot flow and could be used to mint fresh
JWTs even after the user reset their password.

### Details
`passwordChange` and `passwordReset` deleted the user&#x27;s refresh tokens, but
`passwordForgot` only rotated `token_version` and revoked OAuth tokens — it did not
call `UserRefreshToken.deleteAllUserToken(user.id)`. An attacker holding a c…

---

## 29. 🟡 High Severity — vLLM: incomplete CVE-2026-22778 fix leaks PIL repr addresses via Anthropic router

**CVE:** `CVE-2026-54236` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-hgg8-fqqc-vfmw>

> # vLLM: incomplete CVE-2026-22778 fix leaks PIL repr addresses via the Anthropic API router

**Researcher:** Kai Aizen — SnailSploit (@SnailSploit), Adversarial &amp; Offensive Security Research
**Severity:** CVSS 3.1 5.3 (Medium)  `AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N`
**Target:** https://github.com/vllm-project/vllm

---

## Summary

The fix for CVE-2026-22778 / GHSA-4r2x-xpjr-7cvv (PRs #31987 an…

---

## 30. 🟡 High Severity — Traefik: Kubernetes Gateway crossProviderNamespaces bypass allows HTTPRoute outside the allowlist to expose internal Traefik services

**CVE:** `CVE-2026-54761` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-3g6v-2r68-prfc>

> ## Summary

There is a high severity vulnerability in Traefik&#x27;s Kubernetes Gateway provider affecting the `crossProviderNamespaces` allowlist. For `HTTPRoute` rules that declare multiple (WRR) backendRefs, Traefik evaluates the allowlist against the target `backendRef.namespace` instead of the route&#x27;s own namespace. As a result, an `HTTPRoute` created in a namespace that is not allow-lis…

---

## 31. 🟡 High Severity — Pi Agent: Pi loads project-local extensions without approval

**CVE:** `CVE-2026-54325` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-mqxh-6gq7-558m>

> # Pi loads project-local extensions without approval

Pi before 0.79.0 loaded project-local configuration and resources from a repository&#x27;s `.pi` directory without first asking the user to trust that repository. This included project-local extensions, which are executable TypeScript or JavaScript modules loaded into the Pi process.

An attacker who controls a repository could place Pi-specifi…

---

## 32. 🟡 High Severity — Pi Agent: Predictable temporary extension install paths allow local privilege escalation on shared Linux hosts

**CVE:** `CVE-2026-54328` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-jfgx-wxx8-mp94>

> # Predictable temporary extension install paths allow local privilege escalation on shared Linux hosts

Pi versions with temporary npm or git extension package installs used predictable paths under the operating system temporary directory. On Linux-based multi-user systems, a local attacker who can write to the shared temporary directory could prepare the expected package location before another u…

---

## 33. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
