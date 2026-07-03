# Zero Day Pulse

> **Generated:** 2026-07-03 08:47 UTC &nbsp;|&nbsp; **Total:** 35 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 21 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CWE-22 path traversal in the SimpleHelp web application (notably the toolbox component) that fails to sanitize path parameters. Unauthenticated remote attackers can submit crafted HTTP requests using directory-traversal sequences to read arbitrary files on the SimpleHelp host, including serverconfig.xml (which contains API tokens, hashed technician/user passwords, and other secrets), /etc/passwd, and private SSH keys (e.g., /root/.ssh/id_rsa).
- **Affected Products:** SimpleHelp (Remote Support / RMM) version 5.5.7 and all earlier releases; SimpleHelp 5.4.x branch (fixed in v5.4.10); SimpleHelp 5.3.x branch (fixed in v5.3.9)
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true - Public PoC at https://github.com/imjdl/CVE-2024-57727; Metasploit module auxiliary/scanner/http/simplehelp_toolbox_path_traversal (Rapid7)
- **Patch Available:** true - SimpleHelp v5.5.8 (Jan 10, 2025), with backported patches v5.4.10 and v5.3.9. Advisory: https://guides.simple-help.com/kb---security-vulnerabilities-01-2025
- **Active Exploitation:** true - CISA Advisory AA25-163A (Jun 12, 2025) confirms in-the-wild ransomware exploitation since January 2025. Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a
- **Threat Actors:** DragonForce ransomware actors (per CISA Advisory AA25-163A and Sophos reporting)
- **Mitigation:** 1. Upgrade SimpleHelp to v5.5.8 (or apply v5.4.10 / v5.3.9 for the older release branches). 2. Apply the vendor hardening checklist: change all SimpleHelp Administrator and Technician passwords; restrict allowed IP ranges for technician/administrator/API logins; disable the SimpleHelpAdmin account in favor of named accounts; disable local-credential logins in favor of Active Directory/LDAP; rotate API tokens; restrict firewall ingress to the SimpleHelp server. 3. CISA-recommended compensating controls: isolate SimpleHelp servers from the public internet (or stop the service if not in use), maintain offline backups, avoid exposing RDP, perform an RMM risk analysis, and adopt an SBOM. 4. For systems confirmed compromised: disconnect from the network, re-image from clean media, and restore data from known-good backups.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — Critical Cursor AI Code Editor Flaws Could Lead to OS-Level Remote Code Execution

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-03
**Reference:** <https://www.securityweek.com/critical-cursor-ai-ide-flaws-could-lead-to-os-level-remote-code-execution/>

> The DuneSlide vulnerabilities enable zero-click prompt injection attacks that escape Cursor&#x27;s sandbox and execute arbitrary code on the underlying operating system. The post Critical Cursor AI Code Editor Flaws Could Lead to OS-Level Remote Code Execution appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-50548 and CVE-2026-50549 are zero-click remote code execution vulnerabilities in Cursor IDE's AI agent sandbox, triggered through prompt injection in content the agent ingests (e.g., MCP tool responses, web-search results). They require only a benign user prompt — no clicks or command confirmation. CVE-2026-50548: Cursor's terminal sandbox grants write access to a command's working directory. A prompt-injection payload manipulates the agent-controllable working_directory parameter of run_terminal_cmd to register an attacker-supplied path as allowed, then writes through that path to overwrite the cursorsandbox helper binary (macOS path: /Applications/Cursor.app/Contents/Resources/app/resources/helpers/cursorsandbox). Subsequent commands execute unsandboxed under the user's OS privileges. CVE-2026-50549: Cursor canonicalizes target paths before writes. When canonicalization fails, Cursor falls back to the original in-project path without approval. A malicious agent creates an in-workspace symlink pointing outside the workspace and forces canonicalization to fail, so writes through the symlink overwrite cursorsandbox, achieving unsandboxed OS-level command execution.
- **Affected Products:** Cursor IDE, all versions prior to 3.0 (i.e., every Cursor 2.x release and earlier). Fixed in Cursor 3.0 (released April 2, 2026).
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable. No CVSS v3.x vector has been published; only a CVSS 4.0 vector is available (CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N).
- **Exploit Available:** false. A detailed technical write-up exists at https://www.catonetworks.com/blog/duneslide-two-critical-rce-vulnerabilities/ but it is a research analysis, not a runnable exploit. No public weaponized PoC or exploit kit has been indexed for CVE-2026-50548 or CVE-2026-50549.
- **Patch Available:** true. Cursor version 3.0 (released April 2, 2026) fixes CVE-2026-50548 and CVE-2026-50549. https://cursor.com/blog/cursor-3 ; https://cursor.com/changelog/3-0 ; vendor advisories: https://github.com/cursor/cursor/security/advisories/GHSA-3p48-7v9f-v5cw and https://github.com/cursor/cursor/security/advisories/GHSA-3v8f-48vw-3mjx
- **Active Exploitation:** false. Multiple authoritative sources (The Hacker News, Mallory, SecurityWeek) report there is currently no evidence of exploitation in the wild. The vulnerabilities were patched in Cursor 3.0 on April 2, 2026, before public disclosure on July 1, 2026.
- **Threat Actors:** None known. No APT group, ransomware operator, or other threat actor has been publicly attributed to exploiting the DuneSlide vulnerabilities (CVE-2026-50548 and CVE-2026-50549).
- **Mitigation:** Upgrade Cursor IDE to version 3.0 or later (released April 2, 2026), which fixes both DuneSlide vulnerabilities. No vendor-published pre-patch workaround is available. Until upgraded, apply these hardening measures: avoid pasting untrusted content into contexts where the Cursor agent may ingest it (e.g., MCP tool outputs, web-search results); review and restrict which terminal commands and tools the agent is allowed to invoke; restrict or disable Cursor's terminal-sandbox settings if feasible; treat all MCP and web sources the agent reads as potential prompt-injection vectors; and monitor for suspicious writes to the Cursor installation directory (e.g., /Applications/Cursor.app/Contents/Resources/app/resources/helpers/cursorsandbox on macOS).
- **Vendor Advisory:** https://github.com/cursor/cursor/security/advisories/GHSA-3p48-7v9f-v5cw; companion advisory: https://github.com/cursor/cursor/security/advisories/GHSA-3v8f-48vw-3mjx

---

## 3. 🟠 Zero-Day — CISA: Microsoft SharePoint RCE flaw now actively exploited

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-microsoft-sharepoint-rce-flaw-now-actively-exploited/>

> CISA warned on Wednesday that attackers have begun exploiting a high-severity Microsoft SharePoint remote code execution vulnerability patched in May. [...]

**Parallel AI Enrichment:**

- **Technical Details:** CWE-502 (Deserialization of Untrusted Data) in Microsoft Office SharePoint Server. SharePoint reconstructs .NET objects from attacker-supplied serialized data without enforcing a strict gadget/type allow-list. An attacker who holds an authenticated SharePoint account with only 'Site Member' privileges can submit a crafted HTTP request containing a malicious serialized .NET object (delivered via the LosFormatter.Deserialize path inside Microsoft.SharePoint.Library). When the SharePoint worker process deserializes it, the embedded gadget chain instantiates arbitrary types and triggers a command-execution primitive inside the SharePoint server process (w3wp.exe), yielding full remote code execution on the underlying host.
- **Affected Products:** Microsoft SharePoint Server Subscription Edition (build 16.0.19725.20280), Microsoft SharePoint Server 2019 (build 16.0.10417.20128), Microsoft SharePoint Enterprise Server 2016 (build 16.0.5552.1002). SharePoint Online (Microsoft 365) is not affected.
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true — Public PoC code is available at https://github.com/mistbarbarianspot/CVE-2026-45659-SharePoint-RCE (Python script exploiting unsafe LosFormatter.Deserialize in Microsoft.SharePoint.Library to achieve authenticated RCE against SharePoint Server 2019/Subscription Edition).
- **Patch Available:** true — Microsoft released security updates in the May 2026 Patch Tuesday (May 12, 2026). Patches are available for SharePoint Server Subscription Edition, SharePoint Server 2019, and SharePoint Enterprise Server 2016. Official vendor advisory URL: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45659.
- **Active Exploitation:** true — CISA added CVE-2026-45659 to the Known Exploited Vulnerabilities (KEV) catalog on July 1, 2026, with a federal-civilian remediation deadline of July 4, 2026. Confirmed by BleepingComputer, The Hacker News, NVD entry (CISA Date Added 07/01/2026), and Shadowserver tracking of over 10,000 internet-exposed SharePoint servers.
- **Threat Actors:** None known. Cisco Talos, BleepingComputer, The Hacker News, the CISA KEV notification, and Microsoft's May 2026 advisory do not publicly attribute the active exploitation to any specific APT group or ransomware operator.
- **Mitigation:** Apply the Microsoft May 2026 Patch Tuesday updates immediately to all on-premises SharePoint Server Subscription Edition, SharePoint Server 2019, and SharePoint Enterprise Server 2016 instances. Additional hardening: take internet-exposed SharePoint front-ends off the public internet or place them behind VPN/WAF; restrict who can obtain a valid SharePoint account (especially Site Member); reduce attack surface by disabling unneeded SharePoint services and features; increase detection/monitoring for unusual ASP.NET worker processes, suspicious uploads to SharePoint endpoints, and unexpected child processes spawned by w3wp.exe.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45659

---

## 4. 🟠 Zero-Day — CISA Warns of Actively Exploited Microsoft SharePoint Vulnerability

**CVE:** `CVE-2026-45659` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://www.securityweek.com/cisa-warns-of-actively-exploited-microsoft-sharepoint-vulnerability/>

> CISA says threat actors are exploiting a recently patched SharePoint remote code execution vulnerability (CVE-2026-45659). The post CISA Warns of Actively Exploited Microsoft SharePoint Vulnerability appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-45659 is a deserialization-of-untrusted-data vulnerability (CWE-502) in Microsoft SharePoint Server. SharePoint fails to safely validate/handle attacker-controlled serialized .NET objects, so an authenticated attacker who holds only low-privilege Site Member permissions on a SharePoint site can submit a crafted payload that, when deserialized by the server, leads to remote code execution in the context of the SharePoint server. The attack is network-borne, requires low privileges (PR:L), requires no user interaction (UI:N), and yields high impact to confidentiality, integrity and availability.
- **Affected Products:** Microsoft SharePoint Server Subscription Edition, Microsoft SharePoint Server 2019, Microsoft SharePoint Enterprise Server 2016
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true — Microsoft released an out-of-band security update in May 2026. Advisory: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45659
- **Active Exploitation:** true — CISA added CVE-2026-45659 to the Known Exploited Vulnerabilities (KEV) Catalog on 2026-07-01 with a remediation due date of 2026-07-04 for U.S. federal agencies, citing evidence of active exploitation. Sources: CISA KEV (https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-45659), SecurityWeek (https://www.securityweek.com/cisa-warns-of-actively-exploited-microsoft-sharepoint-vulnerability/), The Hacker News (https://thehackernews.com/2026/07/sharepoint-rce-cve-2026-45659-added-to.html). Additional context: Tenable reports an EPSS score of 0.00503 and the vulnerability vendor-assessment of 'Exploitation Less Likely' at the time of the original May 2026 patch, prior to the subsequent CISA KEV addition confirming real-world exploitation.
- **Threat Actors:** None known specifically for CVE-2026-45659. CISA's KEV catalog does not attribute the exploitation to any particular threat actor. However, The Hacker News reports that one set of related SharePoint attacks has been attributed to Storm-2603 (a threat group known for deploying Warlock ransomware) — but that reporting ties Storm-2603 to the separate CVE-2025-11371 being exploited in the same campaign rather than specifically attributing it to CVE-2026-45659.
- **Mitigation:** Apply the Microsoft May 2026 out-of-band security update immediately. Fixed build numbers: SharePoint Server Subscription Edition 16.0.19725.20280, SharePoint Server 2019 16.0.10417.20128, SharePoint Enterprise Server 2016 16.0.5552.1002. Hardening advice: review and minimize SharePoint Site Member/Visitor accounts, audit SharePoint IIS logs and the SharePoint Unified Logging System (ULS) for anomalous ViewState/SerializedObject activity, and isolate SharePoint behind network segmentation until patched. Per CISA, U.S. federal civilian agencies were required to remediate by 2026-07-04.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45659

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is a vulnerability class against LLM-driven AI agents. An attacker plants adversarial instructions in content that the agent later ingests (webpage, email body, document, MCP/RAG source, image alt-text, HTML metadata). The agent treats untrusted content as authoritative instruction, overriding the user's intent. Observed techniques include visual hiding (CSS display:none, opacity:0, white-on-white camouflage, hidden metadata), obfuscation/runtime assembly (CDATA wrapping, data-* cloaking, Base64 payloads, homoglyphs, zero-width characters, payload splitting), and outcome primitives: resource exhaustion/DoS via infinite-text streams, data exfiltration (system prompts, user data, app tokens), system destruction (file deletion), SEO manipulation (AI search/summarizer pipeline abuse), and RCE/sandbox escape chains (CVE-2026-39861: IPI in a repo processed by Claude Code chains with a symlink-flavored sandbox escape to execute host code). GeminiJack demonstrated that a single poisoned inbound document can trigger zero-click data exfiltration from Gemini Enterprise.
- **Affected Products:** Google Gemini (consumer app), Gemini in Google Workspace (Gmail, Docs, Drive, Chat), and broadly any LLM-based AI agent that ingests untrusted external content (web pages, emails, documents, MCP/RAG sources). Related: Anthropic Claude Code versions prior to v2.1.64 (CVE-2026-39861).
- **CVSS Score:** CVSS score unavailable for the class-level IPI advisory. For related CVE-2026-39861 (Anthropic Claude Code), NVD-assigned CVSS v4.0 base score = 7.7.
- **CVSS Vector:** CVSS vector unavailable for the class-level IPI advisory. For related CVE-2026-39861 (Anthropic Claude Code), NVD-assigned CVSS v4.0 vector: CVSS:4.0/AV:N/AC:L/AT:P/PR:N/UI:P/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N.
- **Exploit Available:** true. Public PoCs and documented in-the-wild abuse include Palo Alto Unit 42's reviewerpress[.]com SEO scam and betting-platform phishing (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/), Noma Labs' GeminiJack zero-click (https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability), Google blog's Common Crawl samples (http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html), and the CVE-2026-39861 symlink-sandbox-escape chain (https://news.ycombinator.com/item?id=48057842).
- **Patch Available:** false for the IPI class itself (no single patch eliminating it; ongoing layered mitigations). However, specific CVEs caused by IPI have been patched: CVE-2026-39861 (Anthropic Claude Code RCE via IPI) is fixed in Claude Code v2.1.64+ and auto-applied to standard users (https://nvd.nist.gov/vuln/detail/CVE-2026-39861); GeminiJack is reported as mitigated by Google (https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability).
- **Active Exploitation:** true. Confirmed active in-the-wild exploitation from multiple independent sources: Google Threat Intelligence observed a 32% relative increase in 'malicious' prompt injections in Common Crawl data (Nov 2025–Feb 2026), including file-deletion, infinite-stream resource-exhaustion, and automated-SEO injections (http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html). Palo Alto Unit 42 independently documented in-the-wild web-based IPI across advertising, SEO phishing, system destruction, DoS, and sensitive/system-prompt leakage (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/). The Hacker News (2026-05-29) reported LLM-driven attackers exploited CVE-2026-39987 on 2026-05-10 to steal credentials and exfiltrate a PostgreSQL database (https://thehackernews.com/2026/05/attackers-use-llm-agent-for-post.html). Noma Labs demonstrated zero-click GeminiJack against Gemini Enterprise (https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability).
- **Threat Actors:** None known. Google and Unit 42 describe observed activity generically as originating from unnamed 'threat actors' and 'adversaries'. No specific APT group, ransomware operator, or campaign has been publicly attributed. Independent researcher Noma Labs disclosed the 'GeminiJack' zero-click variant against Gemini Enterprise.
- **Mitigation:** Google's documented layered defense for Gemini (apply all layers, not one in isolation): (1) Prompt-injection content classifiers — ML models flagging suspicious structure/keywords/patterns in untrusted inputs; (2) Security thought reinforcement — system-instruction hardening that biases the model toward user intent; (3) Markdown sanitization — strip rendering of harmful URLs/code plus Google Safe Browsing URL redaction; (4) User confirmation framework — HITL for sensitive agent actions (file delete, send, transaction); (5) End-user security notifications — contextual alerts when prompt-injection is neutralized; (6) Model resilience — adversarial training; (7) Continuous red-teaming plus the public Google AI Vulnerability Reward Program. Complementary practitioner guidance (defense-in-depth): strip/inspect HTML before ingestion, separate untrusted text from instructions ('spotlighting'/instruction hierarchy), constrain tool calls, sandbox agent code execution (patch sandbox escapes — see Claude Code ≥v2.1.64 fix for CVE-2026-39861). NVD guidance: users on standard Claude Code auto-update received the fix.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when an attacker embeds malicious natural-language instructions inside content (Google Docs, Gmail messages, Calendar invites, Slides speaker notes, Drive files, or third-party web pages) that an LLM like Gemini later consumes. When the user asks Gemini to act on that content, the injected instructions attempt to override the legitimate user prompt and cause the model to perform attacker-chosen actions — querying additional data sources, changing output, or rendering attacker-controlled resources (e.g., <img> tags that exfiltrate corporate data through normal browser HTTP requests, as demonstrated in the GeminiJack zero-click PoC). The fundamental trust-boundary problem is that LLMs cannot reliably distinguish adversarial data-text from legitimate instructions, and this worsens with agentic automation.
- **Affected Products:** Workspace with Gemini (umbrella), Gemini app, Gemini in Gmail, Gemini in Google Docs, Gemini in Google Drive, Gemini in Google Calendar, Gemini in Google Slides, Gemini 2.5 model generations, Gemini Enterprise, Vertex AI Search
- **CVSS Score:** CVSS score unavailable. No CVSS base score has been publicly assigned to the IPI threat category described in the cited Google blog post.
- **CVSS Vector:** CVSS vector unavailable. IPI is a threat category, not a single CVE-tracked vulnerability, and no CVSS v3 vector has been published for the threat vector described in the cited Google advisory.
- **Exploit Available:** true. Public PoCs and weaponized payloads are available, including GeminiJack (Noma Labs: https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/), 10 in-the-wild IPI payloads (Forcepoint X-Labs: https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads), calendar-invite exploit (Miggo: https://www.miggo.io/post/weaponizing-calendar-invites-a-semantic-attack-on-google-gemini), and Gemini for Workspace phishing PoC (HiddenLayer: https://www.hiddenlayer.com/research/new-gemini-for-workspace-vulnerability-enabling-phishing-content-manipulation).
- **Patch Available:** true (continuous). Google has shipped Gemini 2.5 hardening, the GeminiJack-specific remediation (separating RAG from Gemini Enterprise), and calendar-invite mitigation. Because IPI is a category-level threat, Google treats mitigation as ongoing rolling updates rather than a single versioned patch. Advisory: http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html
- **Active Exploitation:** true. Forcepoint X-Labs verified 10 distinct in-the-wild IPI payloads on live websites (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads) targeting AI agents, spanning financial fraud, data destruction, exfiltration, content suppression, and output hijacking. Google's own web-sweep (https://blog.google/security/prompt-injections-web) identified IPI patterns being actively used. Noma Labs, Miggo, and HiddenLayer demonstrated working exploit chains against Gemini/Workspace.
- **Threat Actors:** None known. No specific APT group, ransomware operator, or named threat actor has been identified as exploiting indirect prompt injection against Workspace with Gemini. Independent researchers have documented in-the-wild IPI payloads without APT attribution.
- **Mitigation:** Apply Google's layered defense-in-depth strategy: (1) Deterministic defenses — URL sanitization, Safe Browsing-based suspicious URL redaction, markdown sanitization, regex takedowns, and mandatory Human-in-the-Loop user confirmation before sensitive actions; (2) ML-based defenses — model retraining with adversarial/synthetic IPI data, prompt-injection content classifiers, and continuous Automated Red Teaming (ART); (3) LLM-based defenses — refined system instructions, security-thought reinforcement, and hardening models' ability to ignore adversarial text; (4) Operational signals — end-user security-mitigation notifications and contextual help-center alerts. Gemini 2.5 models have been substantially hardened. Admin guidance is published at https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: an attacker plants instructions in untrusted web content (malicious sites, third-party content in iframes, or user-generated content such as reviews and comments). When Gemini in Chrome retrieves that page to summarize, plan, or act on the user's behalf, the injected instructions are interpreted by the model as legitimate commands, enabling goal hijacking, unauthorized financial transactions, and exfiltration of sensitive data (mail, files, credentials). This represents a fundamentally new threat surface created by agentic AI browsing.
- **Affected Products:** Google Chrome with Gemini in Chrome (and previewed Gemini agentic capabilities); specific Chrome version numbers for shipped defenses not stated in the advisory.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — Advisory: https://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Google's five-layer defense architecture: (1) User Alignment Critic that evaluates whether a planned model action aligns with the user's stated intent versus untrusted content; (2) Agent Origin Sets (origin-isolation) that restrict which origins Gemini can act on; (3) User confirmation / User Acknowledgement for Sensitive Actions before Gemini performs high-risk actions; (4) Real-Time Threat Detection via a prompt-injection classifier running while the page is being processed; (5) Automated red-team testing plus incident response. Further integration with Safe Browsing, spotlighting (marking untrusted web content so the model can distinguish it from user instructions), and on-device scam detection.
- **Vendor Advisory:** https://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow / out-of-bounds write in Rust `unsafe {}` blocks within the CrabbyAVIF AVIF image decoder (AOSP). Incorrect bounds checks in multiple locations along the NV12 decoding path (YUV planes, alpha plane, Y plane, UV planes, chroma-width, plane-size, and row-bytes calculations) allow out-of-bounds memory access when processing a crafted AVIF image. This is chainable into zero-click remote code execution on Android 16 with no additional privileges and no user interaction.
- **Affected Products:** Google Android 16 (Updated AOSP build 16), CrabbyAVIF (AOSP platform/external/rust/crabbyavif) versions prior to 2025-08-05 security patch level
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true - https://source.android.com/docs/security/bulletin/2025-08-01
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the Android 2025-08-05 (or later) security patch level to obtain the CrabbyAVIF fix. Defense-in-depth mitigations include: (1) the Scudo hardened allocator with guard pages around secondary allocations, which renders the OOB access non-exploitable; (2) avoid rendering or processing untrusted AVIF images on devices below the 2025-08-05 SPL.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is an attack class against generative-AI assistants that consume external, attacker-controllable data. Unlike direct prompt injection (typed by the user), the attacker hides malicious natural-language instructions inside external content that the LLM will later read — emails, documents, calendar invites, web pages, image alt-text, hidden HTML, single-pixel/near-transparent text, metadata, or Base64/emoji payloads. When the LLM ingests that content as part of retrieval-augmented generation or tool-calling, the hidden directives hijack the model's instruction-following and cause it to: (a) exfiltrate user or enterprise data through tool calls (e.g., email/calendar/MCP-style functions), (b) take destructive/sensitive actions, or (c) subvert the system prompt. Variants include multimodal injections (instructions inside images), payload splitting across sources, instruction hierarchies that out-prioritize the system prompt, and 'Fake Context Alignment' patterns that cause delayed/unauthorized tool invocations.
- **Affected Products:** Gemini 2.5 (Flash), Gemini app, Gemini in Google Workspace (Workspace with Gemini features), Google Gemini Voice Assistant on Android, and other Google Workspace AI features that consume external content (email, documents, calendar invites). The technique broadly affects any agentic LLM that ingests untrusted external data.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable. No CVE is associated with the Google research blog post itself; the blog is a defensive publication, not a CVE advisory.
- **Exploit Available:** true — multiple public PoCs and in-the-wild payloads. Sources: Forcepoint X-Labs '10 Indirect Prompt Injection Payloads Caught in the Wild' (Apr 22, 2026, https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads); SafeBreach Labs Gemini Voice Assistant indirect prompt injection exploit (reported Aug 17, 2025; mitigated Nov 14, 2025; https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/); research artifacts in arXiv:2505.14534 'Lessons from Defending Gemini Against Indirect Prompt Injections' (https://arxiv.org/html/2505.14534v1); external reference CVE-2025-32711 (EchoLeak) targeting Microsoft 365 Copilot.
- **Patch Available:** true — defenses have already been rolled into Gemini 2.5 via adversarial training of the base model and deployment of proprietary ML content classifiers for the Gemini app and Gemini in Workspace. Reference: Google's advisory 'Mitigating prompt injection attacks with a layered defense strategy' (http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html) and the companion DeepMind post 'Advancing Gemini's security safeguards' (https://deepmind.google/blog/advancing-geminis-security-safeguards/). The SafeBreach Gemini Voice Assistant finding was mitigated server-side by Google on Nov 14, 2025.
- **Active Exploitation:** true — confirmed active exploitation in the wild. Google observed a ~32% relative increase in malicious indirect-prompt-injection activity between November 2025 and February 2026. Forcepoint X-Labs identified 10 distinct in-the-wild IPI payloads on real websites carrying out API-key theft, data destruction (sudo rm -rf), financial-fraud PayPal/Stripe injections, SEO/traffic hijacking, and AI-behavior suppression (April 2026). SafeBreach Labs publicly disclosed a reproducible indirect-prompt-injection exploit chain against Google Gemini Voice Assistant (reported Aug 17, 2025; mitigated Nov 14, 2025). APT actors (APT42, APT41, APT43, etc.) are documented users of Gemini and prompt-injection/jailbreak techniques against LLMs per the GTIG AI Threat Tracker (Feb 12, 2026).
- **Threat Actors:** State-aligned APTs reported by Google Threat Intelligence Group (Feb 2026): APT42 (Iran), APT41 (PRC), DRAGONBRIDGE (PRC), APT43 (DPRK), plus tracked clusters Temp.HEX, APT31, UNC6418, UNC795, UNC2970, and financially motivated UNC5356. Russian-aligned influence operations KRYMSKYBRIDGE and Doppelganger have also been observed abusing Gemini. Underground cybercriminal services FraudGPT and WormGPT weaponize prompt injection/jailbreaks. No single APT has been formally attributed to in-the-wild indirect prompt injection payloads against Google products specifically, but Iran-, PRC-, and DPRK-nexus actors are documented users of these techniques against LLMs generally.
- **Mitigation:** Google's published six-layer defense strategy (effective in Gemini 2.5): (1) Model hardening via adversarial training and Automated Red Teaming (ART); (2) Prompt-injection content classifiers that scan inbound emails/files and filter suspicious instructions; (3) Security thought-reinforcement in the system prompt to steer the LLM to ignore adversarial requests; (4) Markdown/HTML sanitization and Google Safe Browsing-based redaction of suspicious external URLs and non-rendered image URLs; (5) Human-in-the-Loop (HITL) explicit user confirmation for sensitive actions (e.g., deleting calendar events); (6) End-user security notifications with 'Learn more' links when an attack is mitigated. Additional OWASP-recommended controls: constrain model behavior with strict system-prompt scopes, validate outputs deterministically, enforce least-privilege for tool/API calls (call tokens from code, not the model), segregate untrusted content, and conduct continuous adversarial testing.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** The campaign targets internet-facing network and edge devices (predominantly backbone, provider-edge, and customer-edge routers, plus VPNs and remote-access gateways) by exploiting publicly known CVEs that operators failed to patch. Once inside, the actors pivot via trusted provider-to-provider and provider-to-customer interconnections. They modify router configurations to maintain persistent, long-term access, including: enabling SPAN/RSPAN/ERSPAN traffic mirroring to capture sensitive data (notably RADIUS and TACACS+ authentication traffic); configuring GRE/IPsec tunnels and static routes; modifying Access Control Lists — frequently named 'access-list 20', '10', or '50' — to allow actor-controlled IP space; modifying external IPs in TACACS+/RADIUS server configurations to redirect authentication to actor-controlled infrastructure; deploying virtualized containers on network devices (e.g., Cisco IOS XE/NX-OS Guest Shell); executing commands via SNMP; and using native tools such as siet.py, map.tcl, tclproxy.tcl, and wodSSHServer. The advisory states that exploitation of zero-day vulnerabilities has not been observed to date; the threat relies on known, unpatched CVEs.
- **Affected Products:** Cisco IOS and IOS XE (Smart Install feature, and IOS XE Web Management UI) — exploited via CVE-2018-0171, CVE-2023-20198 (chained), and CVE-2023-20273 (chained), affecting versions including IOS XE 16 and earlier; Ivanti Connect Secure (9.x, 22.x) and Ivanti Policy Secure (9.x, 22.x) — exploited via CVE-2023-46805 chained with CVE-2024-21887; Palo Alto Networks PAN-OS GlobalProtect feature (PAN-OS 10.2, 11.0, 11.1) — exploited via CVE-2024-3400. Additional suspected/scope targets per the advisory include: Fortinet firewalls, Juniper firewalls, Microsoft Exchange, Nokia routers and switches, Sierra Wireless devices, and SonicWall firewalls. Device classes: large backbone routers of major telecommunications providers, plus provider edge (PE) and customer edge (CE) routers.
- **CVSS Score:** CVSS score unavailable. The advisory covers multiple CVEs, each with its own base score (e.g., CVE-2023-20198 10.0, CVE-2024-3400 10.0, CVE-2024-21887 9.1) — but no single aggregate score is published for the advisory.
- **CVSS Vector:** CVSS vector unavailable. AA25-239A is a multi-CVE threat-activity advisory, not a single vulnerability; each referenced CVE (CVE-2023-20198, CVE-2023-20273, CVE-2024-21887, CVE-2023-46805, CVE-2024-3400, CVE-2018-0171) has its own CVSS v3 vector. The advisory itself does not publish a single CVSS vector.
- **Exploit Available:** true — Per Recorded Future's Insikt Group, RedMike (Salt Typhoon) actively exploited unpatched internet-facing Cisco IOS XE devices via CVE-2023-20198/CVE-2023-20273 between December 2024 and January 2025 against telecom providers. Public exploit code and scanning/exploit tooling for these CVEs is widely documented (e.g., Cisco and CISA KEV references). Source: https://www.recordedfuture.com/research/redmike-salt-typhoon-exploits-vulnerable-devices ; https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a
- **Patch Available:** true — Vendor patches exist for every CVE referenced in the advisory: Cisco CVE-2023-20198 (Oct 2023) and CVE-2023-20273; Cisco CVE-2018-0171 (Mar 2018, with continued exploitation noted through 2025); Ivanti CVE-2023-46805/CVE-2024-21887 (Jan 2024); Palo Alto Networks CVE-2024-3400 (Apr 2024). CISA urges organizations to prioritize applying these patches via the KEV Catalog. Sources: https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180328-smi2.html ; https://hub.ivanti.com/s/article/KB-CVE-2023-46805-Authentication-Bypass-CVE-2024-21887-Command-Injection-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure-Gateways ; https://security.paloaltonetworks.com/CVE-2024-3400 ; https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a
- **Active Exploitation:** true — Confirmed active exploitation. CISA AA25-239A documents ongoing PRC activity targeting networks globally across telecommunications, government, transportation, lodging, and military infrastructure, active since at least 2021. Recorded Future's Insikt Group documented RedMike (Salt Typhoon) actively exploiting Cisco IOS XE devices at telecom providers in December 2024–January 2025 and continuing. The advisory and the iC3/FBI IC3 PDF note that the actors use compromised backbone routers as vantage points for credential harvesting (RADIUS/TACACS+). Sources: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a ; https://www.recordedfuture.com/research/redmike-salt-typhoon-exploits-vulnerable-devices ; https://www.ic3.gov/CSA/2025/250827.pdf
- **Threat Actors:** PRC state-sponsored APT groups collectively tracked as Salt Typhoon (also tracked by Recorded Future as RedMike), OPERATOR PANDA, UNC5807, and GhostEmperor. The advisory also links the ecosystem to purported PRC private-sector contractors: Sichuan Juxinhe Network Technology Co. Ltd., Beijing Huanyu Tianqiong Information Technology Co., Ltd., and Sichuan Zhixin Ruijie Network Technology Co., Ltd.
- **Mitigation:** 1) Prioritize patching the referenced CVEs via CISA's Known Exploited Vulnerabilities (KEV) Catalog and follow vendor hardening guides. 2) Pull running configurations from network devices and compare against the latest authorized/golden versions to detect unauthorized ACL changes, SPAN/RSPAN/ERSPAN mirroring, unexpected GRE/IPsec tunnels, unexpected virtual containers (e.g., Guest Shell), and unexpected external IPs in TACACS+/RADIUS server definitions. 3) Audit remote-access configurations for proper ACL and transport-protocol application. 4) Monitor for and alert on unusual router configuration changes, especially in PE/CE routers and backbone devices. 5) Implement a robust change-management process with periodic auditing of device configurations. 6) Use vendor detection signatures (Cisco FirePower/Snort, Palo Alto NGFW, Fortinet AV/IPS, Check Point NGX, Forcepoint NGFW, Trellix) to detect associated IoCs and TTPs.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 11. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 12. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

---

## 13. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 14. 🟠 Zero-Day — Google, FBI Disrupt NetNut Residential Proxy Network Powered by Millions of Devices

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-03
**Reference:** <https://www.securityweek.com/google-fbi-disrupt-netnut-residential-proxy-network-powered-by-millions-of-devices/>

> NetNut rented access to millions of compromised devices, allowing cybercriminals and nation-state actors to mask their identities during attacks. The post Google, FBI Disrupt NetNut Residential Proxy Network Powered by Millions of Devices appeared first on SecurityWeek .

---

## 15. 🟡 High Severity — 9router has an Incomplete Fix: Local-Only Access Gate Bypass in 9router via Host Header SpoofING

**CVE:** `CVE-2026-49353` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-6g2f-w7g3-77vf>

> ## Summary

The fix for CVE-2026-46339 (unauthenticated RCE via unprotected MCP plugin routes) introduced a local-only access gate in `src/dashboardGuard.js` that restricts spawn-capable routes (`/api/mcp/*`, `/api/tunnel/*`, `/api/cli-tools/*`) to loopback requests. The gate determines &quot;local&quot; by inspecting the `Host` and `Origin` HTTP headers rather than the TCP source address. When 9r…

---

## 16. 🟡 High Severity — 9router's Hardcoded Default fallback JWT Secret  Allows Authentication Bypass

**CVE:** `CVE-2026-49352` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-jphh-m39h-6gwx>

> ### Summary
9router uses a publicly known hardcoded string `&quot;9router-default-secret-change-me&quot;` as the fallback of JWT secret for all Dashboard session JWTs when the `JWT_SECRET` environment variable is not set. Because this secret is committed in the public repository and unchanged across all releases, any unauthenticated remote attacker can forge a valid `auth_token` cookie and gain fu…

---

## 17. 🟡 High Severity — LaunchServer FileServerHandler has an unauthenticated path traversal issue

**CVE:** `CVE-2026-54617` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-5g75-477j-2c2f>

> ### Summary
An unauthenticated path traversal in the LaunchServer HTTP file server (`FileServerHandler`) lets any remote actor read **any file** readable by the LaunchServer process (e.g. `../../../../etc/passwd`). This is a generic arbitrary-file-read primitive, so the fix must address the traversal itself, not any specific file.

The readable files include the server&#x27;s own secrets, which tu…

---

## 18. 🟡 High Severity — Algernon vulnerable to server-side script source disclosure on Windows via NTFS filename

**CVE:** `CVE-2026-52792` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-mm6c-5j6x-hq8m>

> ### Summary

Algernon selects its file handler from `filepath.Ext()` (engine/handlers.go:134), which does not treat the NTFS-equivalent names `x.lua::$DATA`, `x.lua.`, or `x.lua ` as `.lua`. On Windows, an unauthenticated client appends one of these suffixes to any server-side script on a public path and receives its raw source instead of executed output, leaking embedded secrets such as database …

---

## 19. 🟡 High Severity — Steeltoe: OAEP setting silently selects PKCS#1 v1.5 padding

**CVE:** `CVE-2026-50268` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-4j9m-h44m-2hv8>

> ### Summary

Configuring `encrypt:rsa:algorithm=OAEP` does not enable OAEP encryption. Due to an incorrect BouncyCastle transformation string, the `OAEP` setting selects PKCS#1 v1.5, which is the same algorithm as the `DEFAULT` setting.

### Impact

Operators who configure `encrypt:rsa:algorithm=OAEP` to obtain CCA2-secure padding receive PKCS#1 v1.5 instead. Currently, `Decrypt()` is called only …

---

## 20. 🟡 High Severity — Steeltoe's static JWKS cache shared across schemes and never invalidated

**CVE:** `CVE-2026-50202` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-7fqc-p256-7pwj>

> ### Summary

The JWT signing key cache in `TokenKeyResolver` uses `kid` as the sole cache key without namespacing by authority. In applications with multiple `JwtBearer` schemes pointing to different identity providers, a key fetched for one scheme can satisfy token validation for another. Additionally, cached keys have no expiration, so rotated or revoked keys remain trusted until the application…

---

## 21. 🟡 High Severity — Steeltoe's env sanitizer misses connection strings — leaks embedded DB passwords

**CVE:** `CVE-2026-50200` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-q62h-354g-5r85>

> ### Summary

The `Sanitizer` component in the Environment actuator redacts configuration values by matching the configuration key name against a suffix list. The default list (`password`, `secret`, `key`, `token`, `.*credentials.*`, `vcap_services`) does not cover the standard .NET pattern `ConnectionStrings:&lt;name&gt;` or Steeltoe Connectors&#x27; `Steeltoe:Client:&lt;type&gt;:Default:Connectio…

---

## 22. 🟡 High Severity — SimpleSAMLphp HTTP-Artifact TLS validator confusion allows cross-IdP authentication bypass

**CVE:** `CVE-2026-49283` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-6929-8p9f-26jx>

> ## Summary

SimpleSAMLphp&#x27;s HTTP-Artifact receive path can treat an unsigned embedded SAML `Response` as cryptographically valid for the wrong IdP.

In the `HTTPArtifact::receive()` flow, the SOAP `ArtifactResponse` receives a TLS-based validator from `SOAPClient::addSSLValidator()`. The embedded SAML `Response` then receives a validator that delegates signature validation to that outer `Arti…

---

## 23. 🟡 High Severity — Linuxfabrik Monitoring Plugins: Sudoers may be able to obtain privilege escalation via /usr/bin/apt-get arguments

**CVE:** `CVE-2026-52817` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-8w6w-23mq-h8rg>

> ### Summary
In the [Debian.sudoers](https://github.com/Linuxfabrik/monitoring-plugins/blob/main/assets/sudoers/Debian.sudoers) file, `apt-get` is allowed for the nagios user. The full command including the arguments are not enforced and can therefore be choosen arbitrarily. This allows to easily get a root shell as the nagios user:

### PoC
By choosing a particular argument, you can get (as a nagi…

---

## 24. 🟡 High Severity — zebrad has persistent on-disk corruption of Sapling/Orchard subtree roots after chain fork via pop_tip

**CVE:** `CVE-2026-52733` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-2gf8-q9rr-jq3h>

> ### Am I affected

You are affected if:

1. You run `zebrad` up to and including `v4.4.1`.
2. Your node participates in a network where chain forks occur (mainnet, testnet, or any network with multiple miners).

All default configurations are affected. The corruption persists across restarts because it is written to RocksDB.

### Summary

When `pop_tip` removes the tip block during a chain fork, s…

---

## 25. 🟡 High Severity — Mautic vulnerable to Path Traversal via Campaign Import

**CVE:** `CVE-2026-9559` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-6r9h-4h75-7q4x>

> ### Summary
A path traversal vulnerability exists in the campaign import feature of Mautic 7. When extracting uploaded ZIP files during campaign imports, a flaw in the validation logic allows file paths to escape the intended temporary directories. 

### Impact
An authenticated user with campaign import privileges (`campaign:imports:create`) can write arbitrary PHP files to sensitive system direct…

---

## 26. 🟡 High Severity — Mautic has Server-Side Template Injection (SSTI) in Theme Templates

**CVE:** `CVE-2026-9558` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-9fx4-7cmj-47vg>

> ### Summary
A Server-Side Template Injection (SSTI) vulnerability exists in Mautic&#x27;s theme engine. The platform renders uploaded Twig templates without a sandbox or strict function restrictions. Authenticated users with permissions to create or upload themes can abuse this to execute arbitrary code.

### Impact
An authenticated user with theme upload and creation privileges can bypass boundar…

---

## 27. 🟡 High Severity — Mautic Focus component Vulnerable to SSRF

**CVE:** `CVE-2026-9557` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-jmv8-8j9j-rcpc>

> ### Summary
A Server-Side Request Forgery (SSRF) vulnerability exists in the Mautic Focus component (`MauticFocusBundle`). Under certain conditions, insufficiency in validating user-supplied URLs allows authenticated users to trigger outbound HTTP requests from the hosting server.

### Impact
An authenticated user with access to the Mautic panel can exploit this vulnerability to perform internal p…

---

## 28. 🟡 High Severity — zebrad has mempool transaction admission denial via single-peer inbound queue saturation

**CVE:** `CVE-2026-52732` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-4fc2-h7jh-287c>

> ### Am I affected

You are affected if:

1. You run `zebrad` up to and including `v4.4.1`.
2. Your node accepts inbound P2P connections (`network.listen_addr` is set, which is the default).
3. Your node&#x27;s mempool is active (node is synced near the chain tip).

All default configurations are affected.

### Summary

A single unauthenticated P2P peer can monopolize all 25 inbound mempool downloa…

---

## 29. 🟡 High Severity — Dragonfly Manager OAuth provider client_secret disclosure via unauthenticated GET /api/v1/oauth

**CVE:** `CVE-2026-49254` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-4q9j-6299-gxmr>

> ### Summary

The Dragonfly Manager exposes `GET /api/v1/oauth` and `GET /api/v1/oauth/:id` to unauthenticated clients. The response body deserializes the entire `manager/models.Oauth` struct, which includes the `client_secret` field. Any network-reachable attacker can read the OAuth client secrets configured for `github` or `google` providers, defeating the confidentiality guarantee of those secre…

---

## 30. 🟡 High Severity — joserfc: HS256/HS384/HS512 verify accepts empty/nil HMAC key (cross-language sibling of CVE-2026-45363)

**CVE:** `CVE-2026-49852` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-gg9x-qcx2-xmrh>

> ### Summary

`joserfc.jwt.decode` accepts attacker-forged HMAC-signed tokens when the
caller-supplied verification key is the empty string or `None`.
`HMACAlgorithm.sign` and `HMACAlgorithm.verify` in
[`src/joserfc/_rfc7518/jws_algs.py:62-70`](https://github.com/authlib/joserfc/blob/1ddca8f3c73ff47e3bc3ac06cb0c08a9535677ec/src/joserfc/_rfc7518/jws_algs.py#L62-L70) feed whatever
`OctKey.get_op_key(…

---

## 31. 🟡 High Severity — Craft CMS: Authorization bypass in `entries/move-to-section` via missing target-section save check

**CVE:** `CVE-2026-50280` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-43cq-c2gq-pfpw>

> ### Summary

The `EntriesController::actionMoveToSection()` endpoint checks only whether the current user can view the destination section, but it does not require permission to save entries into that section. A low-privileged authenticated control-panel user who can move an entry out of its current section can therefore move that entry into a different section where they have read access but no w…

---

## 32. 🟡 High Severity — Ransomware Groups Turn to Citrix Bleed 2, BYOVD, and Supply Chain Credentials

**CVE:** `CVE-2025-5777` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://thehackernews.com/2026/07/ransomware-groups-turn-to-citrix-bleed.html>

> Threat actors associated with the Anubis ransomware operation have been observed exploiting the Citrix Bleed 2 (CVE-2025-5777) vulnerability to obtain initial access.

&quot;Although tactics differ between affiliates, common patterns emerged in tradecraft through use of legitimate Remote Management and Monitoring (RMM) tooling, credential access, and hands-on-keyboard procedures used for lateral

---

## 33. 🟡 High Severity — Langroid: Path traversal in the file tools allows read/write outside configured current directory

**CVE:** `CVE-2026-50181` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-fg23-3346-88f5>

> ### Summary

Langroid&#x27;s `ReadFileTool` and `WriteFileTool` appear to treat `curr_dir` as the intended working-directory boundary for file operations. However, the tools only change the process working directory to `curr_dir` and then operate on the user-supplied `file_path` without resolving and enforcing that the final path remains inside `curr_dir`.

As a result, a tool caller can supply pa…

---

## 34. 🟡 High Severity — Kerberos Hub private key (X-Kerberos-Hub-PrivateKey) leaked to cross-host redirect target due to redirect-following HTTP client without CheckRedirect

**CVE:** `CVE-2026-50192` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-h5gx-45rj-2h5j>

> ### Summary

The Kerberos Hub upload path sends the agent&#x27;s Hub credentials in the custom `X-Kerberos-Hub-PrivateKey` and `X-Kerberos-Hub-PublicKey` request headers to the operator-configured Hub URL (`config.HubURI`). The HTTP client used (`&amp;http.Client{}` in `UploadKerberosHub`) is constructed without a `CheckRedirect` policy, so it follows HTTP redirects automatically. Go&#x27;s `net/h…

---

## 35. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
