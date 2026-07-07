# Zero Day Pulse

> **Generated:** 2026-07-07 14:06 UTC &nbsp;|&nbsp; **Total:** 46 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 34 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated path-traversal (directory traversal) in SimpleHelp ≤5.5.7 allowing an attacker to retrieve arbitrary files from the host (including server configuration and hashed passwords) via crafted HTTP requests.
- **Affected Products:** SimpleHelp remote support / RMM software v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — https://github.com/imjdl/CVE-2024-57727
- **Patch Available:** true — vendor KB / release notes: https://guides.simple-help.com/kb---security-vulnerabilities-01-2025
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply vendor-released patches/updates (upgrade to the patched versions e.g., 5.5.8 / 5.4.10 / 5.3.9) or follow vendor/CISA mitigations; discontinue use if mitigations are unavailable.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — Langroid: Neo4jChatAgent executes LLM-generated Cypher without validation (prompt-to-Cypher injection; config-conditional RCE), mirroring the SQLChatAgent bug fixed in CVE-2026-25879

**CVE:** `CVE-2026-55615` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-2pq5-3q89-j7cc>

> Neo4jChatAgent passes LLM-generated Cypher queries straight to the Neo4j driver with no validation, no statement-type allowlist, and no opt-out gate. The query text is influenceable by prompt injection (direct user input or indirect content the agent reads back via RAG), so an attacker who can influence the prompt can read or destroy all graph data and, when APOC or dbms.security procedures are en…

**Parallel AI Enrichment:**

- **Technical Details:** Neo4jChatAgent accepts LLM-generated Cypher and passes it directly to the Neo4j driver with no validation, no statement-type allowlist, and no opt-out gate. The LLM-controlled string is passed as the first positional argument to session.run / tx.run without validation, enabling attackers who can influence prompts to read, modify, or delete graph data (e.g., MATCH (n) DETACH DELETE n). When privileged procedures (APOC / dbms.*) are available to the DB role, the same injection can lead to filesystem or OS-level actions (apoc.load.*, apoc.import.*, dbms.* admin procedures), producing a config-conditional RCE.
- **Affected Products:** langroid (pip) <= 0.65.4 (patched in 0.65.5)
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true; https://github.com/advisories/GHSA-2pq5-3q89-j7cc
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Upgrade to langroid 0.65.5 (contains the fix). Ensure agents run against least-privilege Neo4j roles; keep the new allow_dangerous_operations gate (default False) in place; restrict or disable Cypher tools if not required; avoid granting APOC/dbms admin procedures to the DB role unless strictly necessary; apply the vendor patch promptly.
- **Vendor Advisory:** https://github.com/advisories/GHSA-2pq5-3q89-j7cc

---

## 3. 🟠 Zero-Day — Langroid: Sandbox Escape to Remote Code Execution via Incomplete `eval()` Mitigation in TableChatAgent

**CVE:** `CVE-2026-54769` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-q9p7-wqxg-mrhc>

> ### Advisory Details
**Title**: Sandbox Escape to Remote Code Execution via Incomplete `eval()` Mitigation in TableChatAgent

**Description**:
### Summary
Langroid is vulnerable to a critical Sandbox Escape leading to Remote Code Execution (RCE) in its `TableChatAgent` and `VectorStore` capabilities. When these agents evaluate LLM-generated tool messages with `full_eval=True`, they attempt to sand…

**Parallel AI Enrichment:**

- **Technical Details:** Langroid's TableChatAgent and VectorStore capabilities evaluate LLM-generated tool messages using Python's eval() with full_eval=True. The implementation attempts to sandbox execution by passing locals={} as an argument to eval(). However, this is an incomplete mitigation: because __builtins__ is not explicitly scrubbed from the globals dictionary mapping, Python implicitly injects all built-in functions during execution. This grants access to dangerous built-ins such as __import__('os').system(), allowing an attacker who can supply a prompt/payload to achieve unauthenticated Remote Code Execution (RCE) on the host. Secondary flaw location: langroid/vector_store/base.py uses the same flawed empty-dictionary scoping mitigation on dynamically built expressions.
- **Affected Products:** langroid (Python package) <= 0.65.1
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true (langroid 0.65.2 - https://github.com/advisories/GHSA-q9p7-wqxg-mrhc)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Upgrade to langroid version 0.65.2 (the patched version that replaces the broken eval()-based sandboxing). Additionally, do not feed untrusted user input directly into TableChatAgent or VectorStore code paths that use full_eval=True; restrict or sanitize any LLM tool-message content before it reaches pandas_eval().
- **Vendor Advisory:** https://github.com/advisories/GHSA-q9p7-wqxg-mrhc

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when an LLM or agent ingests external content (web pages, documents, emails) that contains hidden or obfuscated instructions which the model treats as authoritative. Observed techniques include CSS-hidden text, invisible/white-on-white text, selection-proof hiding, meta tag / OpenGraph / JSON-LD embedding, HTML comments, CSS comments, Unicode/zero-width obfuscation, authority-imitation (system-override delimiters), and structured-data abuse; impacts range from manipulated summaries to unauthorized navigation, command execution or data leakage when agentic privileges or authenticated sessions exist.
- **Affected Products:** Google Gemini Enterprise, Cursor (versions <1.3), ChatGPT Atlas (AI-powered browser), Perplexity Comet (AI-powered browser)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — PoC/examples: https://github.com/brennanbrown/atlas-prompt-injection-poc , https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/
- **Patch Available:** true — Partial/targeted patches: Cursor fixed in version 1.3 (see NVD CVE-2025-54131). Vendor mitigation guidance published (see Google Security Blog post linked above).
- **Active Exploitation:** true — see Google Security Blog, Unit42 (Palo Alto Networks), and Forcepoint analyses reporting in-the-wild IPI detections.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: segregate and mark untrusted external content, require human approval for high-risk actions, validate outputs via deterministic formats, implement guardrails and downstream validation, limit agent privileges (logged-out mode / restrict auto-actions), and deploy web-scale detection for obfuscated payloads. See vendor guidance and OWASP/industry recommendations.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an adversarial attack class that embeds malicious instructions inside external content (documents, emails, web pages, tool outputs, or retrieval corpora) which an LLM ingests during normal processing (summarization, RAG, or agentic tool use), causing the model to follow the hidden instructions. Academic work has demonstrated end-to-end IPI exploits against RAG and agentic systems.
- **Affected Products:** Gemini app, Gemini in Workspace apps (Gmail, Docs editors, Drive, Chat)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Layered mitigations: model hardening / adversarial robustness, prompt-injection content classifiers, security-thought reinforcement, markdown sanitization and suspicious-URL redaction, and a user-confirmation (human-in-the-loop) framework for sensitive actions; plus continuous monitoring and rapid-response improvements.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection against agentic browsing (hidden or crafted web content that influences LLM prompts) and related XSS/privilege-escalation vectors in Chrome WebView can be chained to allow local file access, data exposure, or unauthorized AI actions (zero-click variants like GeminiJack have been described).
- **Affected Products:** Google Chrome (WebView tag), Google Chrome agentic Gemini integration (Gemini in Chrome), Google Gemini Enterprise
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Exploit Available:** true — PoC/demo available: https://github.com/brennanbrown/atlas-prompt-injection-poc
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply vendor-recommended layered defenses for agentic browsing: restrict origin access, sandbox and isolate model-driven components (agentic capabilities), block or sanitize prompt-like content from untrusted pages, require explicit user interaction for sensitive actions, and deploy Chrome’s published mitigations/updates for agentic browsing (per vendor guidance).
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Out-of-bounds accesses (incorrect bounds checks) in the CrabbyAVIF AVIF parser/decoder (Y/UV/alpha plane and plane-size/row-bytes calculations) that can lead to memory corruption; when combined with other bugs this could enable remote code execution without user interaction.
- **Affected Products:** Google Android 16.0 (devices with security patch level prior to 2025-08-01 / 2025-08-05)
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true — https://source.android.com/docs/security/bulletin/2025-08-01
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the Android security updates (security patch levels 2025-08-01 or 2025-08-05 as appropriate). Until patched, reduce network exposure of vulnerable devices, enforce strict firewall/MDM controls, monitor for system service crashes, and rely on Android platform protections (Google Play Protect).
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI): adversary embeds hidden instructions inside external content (emails, documents, calendar invites, markdown/HTML, image or URL content) that an LLM ingests (e.g., during summarization or agent tool-chaining). Those embedded instructions become part of the model’s effective prompt and can cause data exfiltration or unauthorized actions (e.g., via malicious URLs, HTML payloads, or formatted markdown).
- **Affected Products:** Gemini (Gemini app and Gemini in Google Workspace — Gmail, Drive, Docs, Chat), Gemini Advanced, NotebookLM PRO
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true; PoC / writeups: https://www.immersivelabs.com/resources/c7-blog/weaponizing-llms-bypassing-email-security-products-via-indirect-prompt-injection , https://kenhuangus.substack.com/p/indirect-prompt-injection-with-cross
- **Patch Available:** true; vendor mitigations/updates described in advisory: http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html
- **Active Exploitation:** true; sources: SafeBreach Labs reporting and industry writeups reporting IPI payloads observed in the wild (see field_basis pointers)
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: model hardening (Gemini model updates), prompt-injection content classifiers, security thought reinforcement, markdown sanitization, suspicious-URL detection/redaction (Safe Browsing), user confirmation (HITL) for risky actions, end-user mitigation notifications, deterministic policy/config rules, red-teaming/VRP collaboration, and ML retraining using synthetic adversarial data (see vendor advisory for details).
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** State-linked actors compromise edge/backbone routers and remote-access appliances by exploiting known CVEs and weak configurations, modify router/device ACLs and configuration (and sometimes abuse management shells) to maintain persistent access, capture authentication traffic (RADIUS/TACACS+), and use compromised devices as vantage points for lateral movement and data collection/exfiltration.
- **Affected Products:** Cisco routers (backbone / provider-edge / customer-edge), Palo Alto PAN-OS GlobalProtect (affected PAN-OS versions per vendor advisory), Ivanti Connect Secure (9.x, 22.x), Fortinet devices (unspecified models/versions), Juniper routers (unspecified), Microsoft Exchange (unspecified)
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true — patch availability varies by vendor (examples: Ivanti KB for CVE-2024-21887: https://hub.ivanti.com/..., Palo Alto advisory for CVE-2024-3400: https://security.paloaltonetworks.com/CVE-2024-3400)
- **Active Exploitation:** false
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Harden and restrict management interfaces (disable or strictly harden GuestShell/management shells), apply vendor patches where available, rotate and protect device credentials, restrict and monitor RADIUS/TACACS+ exposure, monitor for modified ACLs and unexpected SSH/config changes, and increase logging/alerting on edge routers and remote-access appliances.
- **Vendor Advisory:** https://hub.ivanti.com/s/article/KB-CVE-2023-46805-Authentication-Bypass-CVE-2024-21887-Command-Injection-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure-Gateways, https://security.paloaltonetworks.com/CVE-2024-3400

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** GRU unit 26165 has weaponized multiple public vulnerabilities to gain initial access (exposed VPNs, WinRAR, Roundcube, etc.). Notably, CVE-2023-23397 is an Outlook elevation/NTLM-leak issue where a malicious reminder value (PidLidReminderFileParameter) causes Outlook on Windows to connect to a remote SMB server and leak the user's Net-NTLMv2 hash; the attacker can relay or offline-crack that hash to gain authentication and then perform post-exploit actions (mailbox permission manipulation, sustained email collection).
- **Affected Products:** Microsoft Outlook (CVE-2023-23397), WinRAR (CVE-2023-38831), Roundcube Webmail (CVE-2020-35730, CVE-2020-12641), exposed VPN infrastructure
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true; Microsoft and CISA reporting show weaponization and malicious samples (see Microsoft guidance and the CISA AA25-141A advisory).
- **Patch Available:** true; Microsoft released security updates for CVE-2023-23397 (see Microsoft update guidance / MSRC and CISA advisory).
- **Active Exploitation:** true
- **Threat Actors:** GRU unit 26165 (85th GTsSS), aka Fancy Bear / APT28
- **Mitigation:** Apply vendor updates for Outlook/Exchange immediately; block or restrict outbound SMB (TCP/445) from endpoints and via perimeter controls; add high-value accounts to Protected Users group or otherwise restrict NTLM usage; implement network segmentation, monitoring/alerting for suspicious mailbox/Exchange activity, and prioritize patching of listed CVEs (Outlook, WinRAR, Roundcube); follow CISA AA25-141A and Microsoft guidance for hunting and remediation.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 11. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

---

## 12. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 13. 🟡 High Severity — EGroupware has Authenticated RCE via Malicious eTemplate Upload

**CVE:** `CVE-2026-40187` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-8737-2x9g-xjj7>

> ## Summary

An authenticated administrator can achieve OS-level Remote Code Execution (RCE) by uploading a malicious eTemplate XML file (`.xet`) to the VFS `/etemplates` mount.

The `Widget::expand_name()` method passes template widget attribute values directly into a PHP `eval()` call with only double-quote escaping applied - **backtick characters are not escaped**.

In PHP, backticks inside a do…

---

## 14. 🟡 High Severity — New API: SSRF Protection Bypass via Unresolved Hostname in Notification URLs

**CVE:** `CVE-2026-33655` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-6qcr-qxgr-m7fv>

> ## Summary

The default SSRF protection configuration did not apply IP filtering to hostnames. With `ApplyIPFilterForDomain` disabled by default, URL validation checked domain allow/block rules but did not resolve a hostname and validate the resolved IP address. Authenticated users could configure notification URLs for Webhook, Bark, or Gotify notifications and point a hostname at an internal or m…

---

## 15. 🟡 High Severity — EGroupware has a Remote Code Execution Vulnerability

**CVE:** `CVE-2026-27823` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-h9qx-v5xp-ph8p>

> ## Summary
A critical vulnerability has been identified in EGroupware that may lead to Remote Code Execution (RCE).
The issue allows an authenticated attacker to execute arbitrary commands on the server. If user self-registration is enabled, the vulnerability may be exploitable without prior authentication.

The vulnerability stems from improper authorization checks combined with a file write prim…

---

## 16. 🟡 High Severity — Critical Adobe ColdFusion Vulnerability Exploited in Attacks

**CVE:** `CVE-2026-48282` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://www.securityweek.com/critical-adobe-coldfusion-vulnerability-exploited-in-attacks/>

> Hackers are exploiting a recently patched critical vulnerability (CVE-2026-48282) in Adobe ColdFusion that carries a CVSS score of 10/10. The post Critical Adobe ColdFusion Vulnerability Exploited in Attacks appeared first on SecurityWeek .

---

## 17. 🟡 High Severity — Suspected China-Aligned Hackers Exploit Roundcube Flaws Against Universities

**CVE:** `CVE-2024-42009` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://thehackernews.com/2026/07/suspected-china-aligned-hackers-exploit.html>

> A suspected China-aligned threat activity cluster has been observed exploiting Roundcube webmail software belonging to physics and engineering departments of U.S. and Canadian universities as part of a new campaign.

The activity involves the exploitation of now-patched, critical security flaws in the open-source email solution, such as CVE-2024-42009 (CVSS score: 9.3), to siphon credentials,

---

## 18. 🟡 High Severity — CERT/CC Warns of Hidden Admin Backdoor in Tenda Router Firmware

**CVE:** `CVE-2026-11405` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://thehackernews.com/2026/07/certcc-warns-of-hidden-admin-backdoor.html>

> Several versions of firmware released by Chinese network device manufacturer Tenda have been found to embed an undocumented authentication backdoor that enables administrative access to the devices&#x27; web management interfaces, the CERT Coordination Center (CERT/CC) warned Monday.

&quot;An attacker can exploit this vulnerability, tracked as CVE-2026-11405, to bypass the password verification p…

---

## 19. 🟡 High Severity — OPNsense XPATH Injection (CVE-2026-53582)

**CVE:** `CVE-2026-53582` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://seclists.org/fulldisclosure/2026/Jul/18>

> Posted by evan on Jul 06 SUMMARY: a stored XPATH injection allows any user with just ca manager/certificate manager perms to leak any secret key/any value in config.xml, thus achieving privilege escalation and potentially remote code execution. this can also likely be chained via csrf and some clever hiding. see https://github.com/opnsense/core/security/advisories/GHSA-xww7-76m6-mh2r == VULN == th…

---

## 20. 🟡 High Severity — BeyondTrust Patches Critical Auth Bypass Flaws in Remote Support and PRA

**CVE:** `CVE-2026-40138` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://thehackernews.com/2026/07/beyondtrust-patches-critical-auth.html>

> BeyondTrust has released updates to address two critical security flaws affecting Remote Support (RS) and Privileged Remote Access (PRA) products that, if successfully exploited, could allow unauthenticated attackers to take control of susceptible devices.

The vulnerabilities are listed below -


  CVE-2026-40138 (CVSS score: 9.2) - A pre-authentication vulnerability exists in the

---

## 21. 🟡 High Severity — mknod: Device nodes created mislabeled on SELinux, with broken cleanup (remove_dir on a node)

**CVE:** `CVE-2026-35361` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-r9hw-mj3w-phcq>

> uutils calls `mknod` *before* setting the SELinux context (GNU uses `setfscreatecon` first, labeling atomically). If `set_selinux_security_context` fails, cleanup uses `std::fs::remove_dir`, which cannot remove device nodes or FIFOs, leaving the mislabeled node behind.

**Impact:** on SELinux-enforcing systems the node is created with the wrong context; the command reports failure but leaves a mis…

---

## 22. 🟡 High Severity — mkfifo: permissions of an existing file are changed after FIFO creation fails

**CVE:** `CVE-2026-35341` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-pmf6-rcx4-v53v>

> When `mkfifo()` fails (e.g. target already exists), the code shows an error but is missing a `continue;`, so it falls through to `fs::set_permissions` and changes the permissions of the pre-existing file to the default FIFO mode (`0o666` &amp; umask -&gt; `0644`).

```
$ touch secret; chmod 000 secret
$ coreutils mkfifo secret fifo3 fifo4
mkfifo: cannot create fifo &#x27;secret&#x27;: File exists
…

---

## 23. 🟡 High Severity — 9routers has Exposure of Sensitive Information and Unprotected Database Import/Export, Allowing Complete Credential Theft and Database Takeover

**CVE:** `CVE-2026-55500` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-qvfm-67h2-2qfx>

> ## Summary

The `/api/settings/database` endpoint allows full database export (containing all credentials, API keys, OAuth tokens, and settings) and full database import (complete overwrite) without any authentication requirement beyond the `ALWAYS_PROTECTED` middleware check, which only validates JWT or CLI token. Combined with other vulnerabilities (e.g., default password, tunnel exposure), this…

---

## 24. 🟡 High Severity — Craft CMS: Potential authenticated Remote Code Execution via referrer redirect

**CVE:** `CVE-2026-55794` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-f74w-488g-8x5r>

> ### Requirements:

* Control panel access
* Permissions to edit an entry

### Details

Control panel users with the ability to edit entries can execute unsandboxed Twig code via the HTTP Referrer header.

The issue happens when a user is saving entries. Strings for a signed redirect URL are being compiled as a Twig template via `renderObjectTemplate()`, and while a sandboxed alternative already ex…

---

## 25. 🟡 High Severity — Linuxfabrik Monitoring Plugins have local privilege escalation using embedded command

**CVE:** `CVE-2026-55426` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-798h-hpph-m24j>

> ### Summary
When a check plugin places user provided input inside a command which is passed to `shell_exec`, an attacker can abuse this to run arbitrary commands. This is mainly dangerous for plugins which are listed in the sudoers file, because this allows an attacker controlling the nagios user to get root privileges.

### Details
An example for this is the `restic-check` plugin, where the `--re…

---

## 26. 🟡 High Severity — Suspended Coder users retain access to AI Bridge LLM proxy endpoints

**CVE:** `CVE-2026-55435` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-wqxv-w64v-5wh6>

> ### Summary

AI Bridge proxy endpoints authenticate via `Server.IsAuthorized` in `coderd/aibridgedserver`, which validates key format, expiry, secret and deleted or system users but does not check whether the account is suspended. Because suspension does not revoke existing API keys, a suspended user&#x27;s unexpired token keeps working.

&gt; **Note:** Practical impact is limited to already-issue…

---

## 27. 🟡 High Severity — Coder: Devcontainer recreate endpoint missing write authorization allows read-only roles to destroy containers

**CVE:** `CVE-2026-55433` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-jqj2-x4c5-jfxm>

> ### Summary

The devcontainer recreate endpoint relied on route middleware that checked only `ActionRead` on the workspace and, unlike the sibling delete endpoint, performed no `ActionUpdate` check before triggering the destructive rebuild.

&gt; **Note:** Exploitation requires an existing low-privilege role with access to the target workspace.

### Impact

Any authenticated principal with read-on…

---

## 28. 🟡 High Severity — Coder: User-admin role can reset owner account password

**CVE:** `CVE-2026-55077` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-29xf-69gq-m9jx>

> ### Summary

The `PUT /api/v2/users/{user}/password` endpoint authorized only `ActionUpdatePersonal` and did not prevent a `user-admin` from resetting an `owner` account&#x27;s password. It also did not require the current password when an admin reset another user&#x27;s password.

&gt; **Note:** Exploitation requires the privileged `user-admin` role so practical risk is limited to deployments tha…

---

## 29. 🟡 High Severity — Coder vulnerable to OIDC account takeover via email-based user matching and email_verified bypass

**CVE:** `CVE-2026-55075` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-9r87-mvcw-x35f>

> ### Summary

Two flaws in Coder&#x27;s OIDC login chained into account takeover: email-based user matching fell back to linking by email without checking for an existing link to a different IdP subject and the `email_verified` claim was only enforced when present as a boolean `false` so an absent or non-boolean claim was treated as verified.

### Impact

An attacker who could authenticate at the c…

---

## 30. 🟡 High Severity — Coder's OIDC email_verified type coercion bypass enables account takeover via unverified email linking

**CVE:** `CVE-2026-55076` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-75vm-6w67-gwvp>

> ### Summary

Coder&#x27;s OIDC callback checked `email_verified` with a direct Go `bool` type assertion. When an IdP returned the claim as a non-boolean (for example the string `&quot;false&quot;`) or omitted it, the assertion failed open and the email was treated as verified. Combined with an unconditional email-based account fallback, this enabled account takeover.

### Impact

An attacker who r…

---

## 31. 🟡 High Severity — OpenRemote has Cross-Realm User Information Disclosure in UserResourceImpl

**CVE:** `CVE-2026-54641` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-xqr9-4wvv-gvch>

> ### Summary

A realm admin of tenant B can read the profile, client roles, and realm roles of any user in any other realm (including the master realm) by supplying the target user&#x27;s UUID in the REST API path. Three read endpoints in UserResourceImpl check whether the caller holds the read:admin role but omit a check that the target user belongs to the caller&#x27;s own realm. The vulnerabilit…

---

## 32. 🟡 High Severity — GoFiber never set HSTS header in helmet middleware due to incorrect protocol check

**CVE:** `CVE-2026-53624` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-gv83-gqw6-9j2c>

> ### Summary

The `helmet` middleware in gofiber/fiber never sets the `Strict-Transport-Security` (HSTS) response header, even when `HSTSMaxAge` is explicitly configured, because the condition check at `helmet.go:67` uses `c.Protocol()` — which returns the HTTP protocol version string (e.g., `&quot;HTTP/1.1&quot;`, `&quot;HTTP/2.0&quot;`) — instead of `c.Scheme()` — which returns the URL scheme (`&…

---

## 33. 🟡 High Severity — Langroid: handle_message() executes user-supplied tool JSON without sender verification 

**CVE:** `CVE-2026-54771` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-gjgq-w2m6-wr5q>

> ## Summary

A Langroid application exposing a chat interface to untrusted users may allow direct tool invocation via raw JSON payloads, even when tools are registered with `use=False, handle=True`.

## Details

`enable_message(..., use=False, handle=True)` only prevents the LLM from being instructed to generate the tool. The tool dispatch path in `agent_response()` → `handle_message()` → `get_tool…

---

## 34. 🟡 High Severity — Dragonfly scheduler v1 and v2 gRPC unauthenticated SSRF via attacker-controlled PeerHost in DownloadTinyFile

**CVE:** `CVE-2026-54637` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-chwm-m7g7-685g>

> ## Summary

The Dragonfly **scheduler**&#x27;s v1 gRPC service contains an unauthenticated Server-Side Request Forgery (SSRF). When a peer reports a successful download of a TINY task, the scheduler calls `Peer.DownloadTinyFile()` and issues an HTTP `GET` to a host and port taken verbatim from the attacker-controlled `PeerHost.Ip` / `PeerHost.DownPort` fields of the gRPC request body. The HTTP cli…

---

## 35. 🟡 High Severity — Decompress: Archive extraction can create files and links outside of the target directory

**CVE:** `CVE-2026-53486` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-mp2f-45pm-3cg9>

> ### Impact

When extracting an archive to a directory, a crafted archive can read or write files outside that directory. The flaw is in the code that writes the parsed entries, so it affects every format decompress handles: tar, tar.gz, tar.bz2, and zip by default, plus any others added through the plugins option.

A link (hardlink) or symlink entry is created without checking where its target poi…

---

## 36. 🟡 High Severity — mv: symlinks expanded during cross-device move (resource exhaustion / data duplication)

**CVE:** `CVE-2026-35365` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-h444-6j9x-p8vh>

> When moving directories across filesystems, uutils `mv` dereferences symlinks inside the tree, copying their targets as real files/dirs instead of preserving the symlinks. GNU preserves symlinks by default. E.g. a `etc_link -&gt; /etc` inside the source becomes a full copy of `/etc` at the destination.

**Impact:** (1) resource exhaustion — a small tree can expand into a huge copy (time/disk DoS);…

---

## 37. 🟡 High Severity — id: groups= computed from real GID instead of effective GID

**CVE:** `CVE-2026-35370` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-47c7-qrm7-mqw7>

> The id utility in uutils coreutils miscalculates the groups= section of its output. The implementation uses a user&#x27;s real GID instead of their effective GID to compute the group list, leading to potentially divergent output compared to GNU coreutils. Because many scripts and automated processes rely on the output of id to make security-critical access-control or permission decisions, this dis…

---

## 38. 🟡 High Severity — install: TOCTOU symlink race (unlink-then-create without O_EXCL) allows arbitrary file overwrite

**CVE:** `CVE-2026-35355` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-239g-2685-54x3>

> `copy_file` in `install/src/install.rs` removes the destination then recreates it by pathname via `File::create` / `fs::copy` without `O_EXCL`/`create_new`. Between the unlink and the recreate, a local attacker with write access to the destination directory can drop in a symlink and redirect the write.

**Impact:** when `install` runs privileged into an attacker-writable directory (staging/build p…

---

## 39. 🟡 High Severity — ln: rejects non-UTF-8 source filenames in target-directory mode

**CVE:** `CVE-2026-35373` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-jcjr-rh8q-7xqf>

> In target-directory forms (`ln SOURCE... DIRECTORY`), `ln` rejects source paths with non-UTF-8 filename bytes, while GNU accepts them. Breaks GNU compatibility for byte-oriented filenames on Unix filesystems.

PoC:
```
name=$(printf &#x27;bad_\377&#x27;); mkdir dst; : &gt; &quot;$name&quot;; ln &quot;$name&quot; dst
# GNU: exit 0, creates dst/bad_\377 ; uutils: exit 1, dst empty
```

---
_Zellic p…

---

## 40. 🟡 High Severity — chmod: --preserve-root bypassed by any path that resolves to root (e.g. /../)

**CVE:** `CVE-2026-35338` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-4c7q-4928-8445>

> `Chmoder::chmod()` only compares the literal argument against `Path::new(&quot;/&quot;)`, so the `--preserve-root` guard is bypassed by any path that *resolves* to root — a symlink to `/` or simply `/../`.

```
if self.recursive &amp;&amp; self.preserve_root &amp;&amp; file == Path::new(&quot;/&quot;) {
    return Err(ChmodError::PreserveRoot(&quot;/&quot;.to_string()).into());
}
```

**PoC** — re…

---

## 41. 🟡 High Severity — 16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems

**CVE:** `CVE-2026-53359` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://thehackernews.com/2026/07/16-year-old-linux-kvm-flaw-lets-guest.html>

> A use-after-free bug in Linux&#x27;s KVM hypervisor can be triggered from a guest virtual machine to corrupt the shadow-page state of the host kernel that runs it.

Dubbed &#x27;Januscape&#x27; and tracked as CVE-2026-53359, the flaw sits in the shadow MMU code that KVM shares across both Intel and AMD. The public proof-of-concept panics the host; the researcher claims that a separate, unreleased …

---

## 42. 🟡 High Severity — flyto-core has SSRF guard bypass via IPv6 transition addresses (IPv4-mapped / 6to4 / NAT64) in validate_url_ssrf

**CVE:** `CVE-2026-55787` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-794r-5rp2-fpg8>

> ## Summary

`flyto-core`&#x27;s SSRF protection (`validate_url_ssrf` / `is_private_ip` in `src/core/utils.py`) blocks private and metadata destinations by resolving the host and testing the resulting IP for membership in a hardcoded `PRIVATE_IP_RANGES` list. That list contains only the *native* RFC 1918 / loopback / link-local / unique-local ranges. It does **not** account for IPv6 transition addr…

---

## 43. 🟡 High Severity — Cilium vulnerable to sensitive information disclosure and cluster disruption via local Envoy admin socket access

**CVE:** `CVE-2026-49445` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-3fcv-jvfp-m4q9>

> ### Impact

When Cilium L7 functionality is enabled on a cluster, the Envoy instance supporting this functionality creates a world-accessible socket on cluster nodes. A local attacker would be able to access Envoy admin endpoints. Depending on deployment configuration, this can expose sensitive information or allow disruptive administrative operations, such as:

- Exposing TLS secrets
- Disrupting…

---

## 44. 🟡 High Severity — Formie Hidden field defaults vulnerable to Server-Side Template Injection

**CVE:** `CVE-2026-52889` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-565m-g33j-jq96>

> ## Summary
Formie Hidden fields could evaluate request-derived values as Twig during front-end form rendering.

When a Hidden field used a dynamic default value such as HTTP User Agent, Referer URL, Current URL, Query Parameter, or Cookie Value, the value was copied from the incoming request and later passed to Craft’s Twig rendering layer. This allowed an unauthenticated attacker to provide Twig …

---

## 45. 🟡 High Severity — Threat Actors Probe Gitea Docker Flaw CVE-2026-20896 13 Days After Disclosure

**CVE:** `CVE-2026-20896` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://thehackernews.com/2026/07/threat-actors-probe-gitea-docker-flaw.html>

> Threat actors have been observed attempting to exploit a recently patched critical security flaw in Gitea Docker images, according to Sysdig.

The vulnerability in question is CVE-2026-20896 (CVSS score: 9.8), a vulnerability that stems from the DevOps platform trusting the &quot;X-WEBAUTH-USER&quot; header from any source IP address, effectively allowing an unauthenticated internet client to get …

---

## 46. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
