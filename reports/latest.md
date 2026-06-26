# Zero Day Pulse

> **Generated:** 2026-06-26 13:59 UTC &nbsp;|&nbsp; **Total:** 29 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 15 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal vulnerability allowing unauthenticated attackers to read arbitrary files on the SimpleHelp host via crafted HTTP requests.
- **Affected Products:** SimpleHelp remote support software v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true (https://github.com/imjdl/CVE-2024-57727)
- **Patch Available:** true (https://www.broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability)
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors
- **Mitigation:** Apply the vendor patch released for SimpleHelp v5.5.7 and earlier, or upgrade to a newer version; if patch unavailable, restrict network access to the RMM service and block external HTTP requests.
- **Vendor Advisory:** https://www.broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — First-Ever Exploitation of PTC Windchill Vulnerability Discovered in the Wild

**CVE:** `CVE-2026-12569` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://www.securityweek.com/first-ever-exploitation-of-ptc-windchill-vulnerability-discovered-in-the-wild/>

> CISA has added the remote code execution flaw CVE-2026-12569 to its Known Exploited Vulnerabilities catalog. The post First-Ever Exploitation of PTC Windchill Vulnerability Discovered in the Wild appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Deserialization of untrusted data leads to remote code execution.
- **Affected Products:** PTC Windchill PDMLink 11.0 M030, 11.1 M020, 11.2.1.0, 12.0.2.0, 12.1.2.0, 13.0.2.0, 13.1.0.0, 13.1.1.0, 13.1.2.0, 13.1.3.0; PTC FlexPLM 11.0 M030, 11.1 M020, 11.2.1.0, 12.0.0.0, 12.0.2.0, 12.0.3.0, 12.1.2.0, 12.1.3.0, 13.0.2.0, 13.0.3.0
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true: https://www.ptc.com/en/about/trust-center/advisory-center/active-advisories/windchill-flexplm-critical-vulnerability
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply vendor-provided mitigation steps: protect publicly accessible systems, apply Apache/IIS configuration updates, and follow the workaround steps outlined in the advisory.
- **Vendor Advisory:** https://www.ptc.com/en/about/trust-center/advisory-center/active-advisories/windchill-flexplm-critical-vulnerability

---

## 3. 🟠 Zero-Day — Google Details Turla's New STOCKSTAY Backdoor Used in Ukraine Espionage Attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://thehackernews.com/2026/06/google-details-turlas-new-stockstay.html>

> The Russian state-sponsored threat actor known as Turla has been attributed to a previously undocumented .NET backdoor called STOCKSTAY that has been deployed against government and military organizations in Ukraine, and entities that have an interest in Italian foreign policy.

Describing the Windows backdoor as continually developed by the hacking group, Google Threat Intelligence Group (

**Parallel AI Enrichment:**

- **Technical Details:** STOCKSTAY is a multi-component .NET backdoor (Windows Forms) attributed to Turla. Components include STOCKSTAY.STOCKBROKER (proxy-aware tunneler), STOCKSTAY.STOCKTRADER (main backdoor), STOCKSTAY.STOCKMARKET (orchestrator/controller) and MARKETMAKER (downloader). It uses an encrypted on-disk configuration and communicates with C2 over a secure WebSocket channel (websocket-sharp library); supports commands for file download/exfiltration, screen capture, registry and process manipulation, and system info harvesting. Delivery vectors observed: spear-phishing with malicious RDP files, RAR archives exploiting CVE-2025-8088, MSI installers, and HTA-based downloaders. Defenders should hunt for WebSocket beacons and the named components, and remediate delivery-vector vulnerabilities.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Turla (aka SUMMIT / Secret Blizzard / VENOMOUS BEAR / UAC-0194)
- **Mitigation:** Patch WinRAR (remediate CVE-2025-8088) where applicable; hunt for WebSocket C2 (look for connections to *.onrender[.]com and presence of websocket-sharp.dll); deploy GTIG IOCs/YARA rules and the GTI collection; block/inspect MSI, RAR, HTA, and malicious RDP file attachments at email gateway; enforce DMARC/SPF; monitor for STOCKSTAY components (STOCKBROKER, STOCKTRADER, STOCKMARKET, MARKETMAKER) and unusual autorun entries.
- **Vendor Advisory:** https://cloud.google.com/blog/topics/threat-intelligence/stockstay-turla-intelligence-gathering

---

## 4. 🟠 Zero-Day — LangGraph Checkpoint: Unsafe JSON deserialization in checkpoint loading

**CVE:** `CVE-2026-48775` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-fjqc-hq36-qh5p>

> ## Summary

LangGraph&#x27;s `JsonPlusSerializer` can reconstruct Python objects from JSON checkpoint payloads. Under conditions where someone could modify checkpoint bytes at rest in the backing store, the deserialization path could reconstruct objects beyond what the application expects, which could in turn result in code execution at checkpoint load time.

This is a defense-in-depth issue. The …

**Parallel AI Enrichment:**

- **Technical Details:** LangGraph's JsonPlusSerializer can reconstruct Python objects from JSON checkpoint payloads. If an attacker can modify checkpoint bytes at rest in the backing store, deserialization may instantiate unexpected objects, potentially enabling code execution during checkpoint load (unsafe/insecure deserialization).
- **Affected Products:** langgraph-checkpoint (LangGraph SQLite Checkpoint) versions < 4.1.1
- **CVSS Score:** 6.8
- **CVSS Vector:** CVSS:3.1/AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true (fixed in langgraph-checkpoint v4.1.1) https://github.com/langchain-ai/langgraph/security/advisories/GHSA-fjqc-hq36-qh5p
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Upgrade to langgraph-checkpoint v4.1.1 or later; restrict and monitor write access to checkpoint storage (treat checkpoint-store compromise as a serious incident); implement integrity checks or encryption for checkpoint blobs and avoid deserializing untrusted data.
- **Vendor Advisory:** https://github.com/langchain-ai/langgraph/security/advisories/GHSA-fjqc-hq36-qh5p

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection occurs when an AI system processes external content (e.g., websites, emails, documents) that contains malicious instructions, causing the model to execute those instructions as part of its response.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Monitor for known indirect prompt injection patterns on the public web and block malicious content.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is a technique where an attacker influences an LLM by injecting malicious instructions into the data, tools, or external corpora used by the model, potentially without direct user input.
- **Affected Products:** Google Workspace (including Gemini)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (source: http://arxiv.org/pdf/2601.07072)
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true (sources: http://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads, http://arxiv.org/pdf/2601.07072)
- **Threat Actors:** None known
- **Mitigation:** Google employs a layered security approach including input/output validation, sanitization, human oversight, continuous monitoring, and builds Workspace with Gemini to be a secure and trustworthy platform.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Class: indirect prompt injection affecting agentic browsing / Gemini. Public researchers (Noma Labs) reported a zero-click 'GeminiJack' indirect prompt injection in Gemini Enterprise; Unit42 reported a high-severity Chrome issue (CVE-2026-0628) that allowed local file access/privacy invasion and was patched. The attack vector is malicious content (or chained vulnerabilities) causing the agent to accept or execute attacker-controlled prompt inputs, enabling data access or unsafe actions unless blocked by layered defenses.
- **Affected Products:** Google Chrome (agentic browsing / Gemini integration — Chrome builds that include Gemini agentic features)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (Google released mitigations/patches; see vendor advisory and reporting)
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Google implemented layered defenses for agentic browsing (restricting origin access, limiting unsafe AI actions, and an additional watch/guard layer for Gemini); follow vendor guidance and apply Chrome updates.
- **Vendor Advisory:** http://blog.google/security/architecting-security-for-agentic

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
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection attacks embed hidden malicious instructions in external data sources such as emails, documents, or calendar invites that cause AI systems to perform unintended actions. Google mitigates this by adversarial model training, content classifiers, security thought reinforcement, markdown sanitization, URL redaction, user confirmation, and end‑user security notifications.
- **Affected Products:** Google Gemini (Gemini 2.5), Google Workspace (Gmail, Docs, Calendar), Gemini app
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Layered defense: model hardening with adversarial training, prompt injection content classifiers, security thought reinforcement, markdown sanitization, suspicious URL redaction, user‑confirmation framework for risky actions, and end‑user security notifications. These measures are built into Gemini and Google Workspace services.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Exploitation of network edge devices such as backbone, provider, and customer routers using CVEs to gain persistent access, often leveraging compromised devices and trusted connections to pivot within networks.
- **Affected Products:** Backbone routers, provider edge (PE) routers, customer edge (CE) routers, network edge devices
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Apply patches when available, implement network segmentation, monitor router activity, enforce strong authentication, limit management access, and follow vendor detection guidance.
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

## 15. 🟡 High Severity — New DirtyClone Linux Kernel Flaw Lets Local Users Gain Root via Cloned Packets

**CVE:** `CVE-2026-43503` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://thehackernews.com/2026/06/new-dirtyclone-linux-kernel-flaw-lets.html>

> DirtyClone is a new Linux kernel privilege escalation in the DirtyFrag family. JFrog Security Research published a working exploit walkthrough for the flaw on June 25, the first public demonstration for this variant.

Tracked as CVE-2026-43503 (CVSS 8.8), it lets a local user corrupt file-backed memory through a cloned network packet and gain root. The patch landed in

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
