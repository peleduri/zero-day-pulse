# Zero Day Pulse

> **Generated:** 2026-07-01 19:31 UTC &nbsp;|&nbsp; **Total:** 24 &nbsp;|&nbsp; 🔴 KEV: 1 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 9 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🔴 CISA KEV — CVE-2026-45659 — Microsoft SharePoint Server Deserialization of Untrusted Data Vulnerability

**CVE:** `CVE-2026-45659` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-45659>

> Vendor: Microsoft | Product: SharePoint Server. Microsoft SharePoint Server contains a deserialization of untrusted data vulnerability which allows an authorized attacker to execute code over a network. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA…

**Parallel AI Enrichment:**

- **Technical Details:** A deserialization of untrusted data vulnerability in Microsoft SharePoint Server (server-side deserialization in file-processing / web-rendering components) allows an authenticated attacker who can submit crafted serialized input to achieve remote code execution on affected servers.
- **Affected Products:** Microsoft SharePoint Server Subscription Edition, SharePoint Server 2019, SharePoint Enterprise Server 2016
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof-of-concept(s) and exploit reports have been published (community PoC coverage and vulnerability trackers report exploits/PoCs are available).
- **Patch Available:** Microsoft has published security updates for affected SharePoint Server versions; see the MSRC advisory: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45659
- **Active Exploitation:** No confirmed reports of active exploitation in the wild were found in the collected sources.
- **Threat Actors:** None known
- **Mitigation:** Apply Microsoft’s security updates for the affected SharePoint Server versions (see MSRC advisory). If immediate patching is not possible, follow vendor hardening guidance: restrict access to SharePoint servers, enforce least privilege, isolate affected on‑prem systems, and monitor for indicators of compromise until updates can be applied.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45659

---

## 2. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CWE-22 Path Traversal. Unauthenticated path traversal in SimpleHelp RMM v5.5.7 and earlier web endpoints allows downloading arbitrary files from the SimpleHelp host by crafting HTTP requests with manipulated path components. The flaw enables extraction of serverconfig.xml containing hashed admin/technician credentials, LDAP credentials, OIDC client tokens, and TOTP seeds. Attackers chain CVE-2024-57727 with CVE-2024-57726 (admin privilege escalation) and CVE-2024-57728 (arbitrary file upload for SYSTEM/root code execution), then use the SimpleHelp technician push mechanism to deploy malware to downstream MSP/RMM customers.
- **Affected Products:** SimpleHelp Remote Support / Remote Monitoring and Management (RMM) software, versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Yes — public PoC and weaponized exploits available. Python exploit at https://github.com/imjdl/CVE-2024-57727 and Metasploit auxiliary module at https://www.rapid7.com/db/modules/auxiliary/scanner/http/simplehelp_toolbox_path_traversal/
- **Patch Available:** Yes — SimpleHelp v5.5.8 released January 10, 2025 (full installer upgrade). Backported patched library artifacts for v5.4.10 and v5.3.9 branches available in https://guides.simple-help.com/kb---security-vulnerabilities-01-2025 with SHA1-verified digests. Companion vendor advisory: https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know
- **Active Exploitation:** Confirmed active exploitation since January 2025. Primary sources: (1) CISA Advisory AA25-163A (June 12, 2025) — DragonForce ransomware actors chained CVE-2024-57727 with related CVEs against an unpatched utility billing MSP, compromising downstream customers; (2) Sophos MDR blog (May 27, 2025) — first-hand IR confirming DragonForce; (3) Halcyon blog (June 24, 2025) — continued exploitation of unpatched v5.5.7 and earlier; (4) Microsoft Threat Intelligence (April 6, 2026) — attributes broader campaign to Storm-1175. Corroborating evidence from Picus Security, AttackIQ, NYS ITS (2025-012), and AHA/Health-ISAC (Jan 29, 2025). CVE also listed in CISA KEV tracking.
- **Threat Actors:** DragonForce ransomware operators (primary, named in CISA AA25-163A and Sophos MDR incident response); Storm-1175 (Microsoft attribution for broader SimpleHelp RMM initial access campaign, linked to Medusa ransomware operations)
- **Mitigation:** Primary fix: upgrade SimpleHelp server to v5.5.8 or later. For environments that cannot immediately upgrade, apply the backported patched library artifacts with SHA1 verification per the SimpleHelp KB at https://guides.simple-help.com/kb---security-vulnerabilities-01-2025. Hardening: (a) rotate the SimpleHelp Administrator password and any Technician passwords not backed by third-party SSO; (b) restrict source IP ranges for Technician/Administrator logins; (c) isolate or stop internet-exposed SimpleHelp servers until patched; (d) threat-hunt for suspicious executables with three-alphabetic-letter filenames (e.g., aaa.exe) in JWrapper-Remote Access directories; (e) perform host/network vulnerability scans and monitor SimpleHelp traffic; (f) do not expose RDP or other remote services directly to the internet; (g) maintain offline clean backups and a current asset inventory; (h) review SBOMs and conduct RMM risk analysis for downstream providers.
- **Vendor Advisory:** https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 3. 🟠 Zero-Day — Critical Cursor Flaws Could Let Prompt Injection Escape Sandbox and Run Commands

**CVE:** `CVE-2026-50548` | `CVE-2026-50549` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://thehackernews.com/2026/07/critical-cursor-flaws-could-let-prompt.html>

> Two flaws in Cursor, an AI code editor, could let a single, ordinary-looking prompt break out of the editor&#x27;s safety sandbox and run any command on a developer&#x27;s computer. There is no click to fall for and no approval box to ignore.

Cato AI Labs found the pair and named them DuneSlide. They are tracked as CVE-2026-50548 and CVE-2026-50549, both rated 9.8 out of 10 (or 9.3

**Parallel AI Enrichment:**

- **Technical Details:** Two sandbox-escape flaws in Cursor's agent command execution. CVE-2026-50548 abuses the run_terminal_cmd tool's working_directory parameter — when path canonicalization fails, Cursor falls back to the original path, allowing an attacker to point working_directory at a sensitive location (e.g., Cursor's helper directory or ~/.zshrc) and add it to the sandbox write allow-list. CVE-2026-50549 abuses the symlink safety check — when path canonicalization fails, Cursor writes through the symlink to an arbitrary location without approval. An in-workspace prompt injection causes the agent to create a malicious symlink and set working_directory outside the workspace, overwriting the cursorsandbox helper binary so subsequent commands run unsandboxed with the developer's privileges. Attack vector is zero-click indirect prompt injection via MCP servers or web search results; no user interaction required.
- **Affected Products:** Cursor (Desktop AI code editor) — all versions prior to 3.0 (Cursor 2.x). Fixed in Cursor 3.0.
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Proof-of-concept technical write-up published by Cato Networks (https://www.catonetworks.com/blog/duneslide-two-critical-rce-vulnerabilities/) describing the full exploitation chain. No public weaponized exploit kits, Metasploit modules, or in-the-wild exploit samples have been identified.
- **Patch Available:** Yes — patched in Cursor 3.0, released April 2, 2026. Official advisories: https://github.com/cursor/cursor/security/advisories/GHSA-3p48-7v9f-v5cw and https://github.com/cursor/cursor/security/advisories/GHSA-3v8f-48vw-3mjx.
- **Active Exploitation:** No confirmed active exploitation in the wild as of July 1, 2026. Both CVEs were responsibly disclosed by Cato AI Labs researcher Maor Dokhanian on June 5, 2026, with CVE assignments on June 25, 2026. No threat actor or ransomware campaign has been publicly tied to CVE-2026-50548 or CVE-2026-50549. Source: https://thehackernews.com/2026/07/critical-cursor-flaws-could-let-prompt.html
- **Threat Actors:** None known
- **Mitigation:** Upgrade to Cursor 3.0 or later (released April 2, 2026) — the patch for both flaws. Interim hardening if upgrade is delayed: (1) treat MCP servers and web-search/connector inputs as untrusted, (2) disconnect or audit untrusted third-party MCP integrations, (3) only ingest prompts from trusted sources, (4) run Cursor from a least-privileged user account to limit sandbox-escape blast radius.
- **Vendor Advisory:** https://github.com/cursor/cursor/security/advisories/GHSA-3p48-7v9f-v5cw

---

## 4. 🟠 Zero-Day — Anthropic Restores Claude Fable 5 After U.S. Lifts Jailbreak-Linked Export Controls

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://thehackernews.com/2026/07/anthropic-restores-claude-fable-5-after.html>

> Anthropic is putting Claude Fable 5 back online worldwide. On June 30, the U.S. Commerce Department lifted the export controls it had imposed on Fable and its more tightly controlled sibling Mythos 5 about two and a half weeks earlier.

Fable 5 returns to users on Wednesday, July 1, across Claude.ai, the Claude Platform, Claude Code, and Claude Cowork.

Export controls restrict who can

**Parallel AI Enrichment:**

- **Technical Details:** Agentic Claude Code eagerly/parsing project files and repository contents allowed attacker-controlled project files or repositories to trigger remote code execution and to exfiltrate API tokens/credentials when the agent processed those files. Disclosed CVEs associated with these issues include CVE-2025-59536 and CVE-2026-21852.
- **Affected Products:** Anthropic Claude Code, Claude Fable 5, Claude Mythos 5, Claude.ai, Claude Platform, Claude Cowork
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof-of-concept demonstrations and writeups are publicly available (research disclosures and social posts describing repo-based PoCs and exploit mechanics). Example sources include Check Point Research disclosures and public PoC posts.
- **Patch Available:** Anthropic published vendor updates and redeployed Fable 5 with updated cybersecurity safeguards (see vendor advisory above).
- **Active Exploitation:** No authoritative confirmation of widespread active exploitation by named threat actors in the wild; public PoCs and community demonstrations have been posted but no confirmed large-scale campaigns reported in the collected authoritative sources.
- **Threat Actors:** None known
- **Mitigation:** Follow the vendor advisory and apply vendor updates/patches; avoid letting agentic coding assistants automatically process untrusted repositories or project files; rotate and restrict scope of any exposed API keys; use vendor-provided security plugins (e.g., Claude Code security plugin) and configuration hardening per Anthropic guidance.
- **Vendor Advisory:** https://www.anthropic.com/news/redeploying-fable-5

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI): an attacker plants malicious instructions inside content (web pages, emails, documents, repo comments) that an AI agent subsequently reads as part of its task. Because the LLM cannot reliably distinguish 'data' from 'instructions,' it executes the attacker's commands instead of (or in addition to) the user's prompt. Common obfuscation patterns: HTML comments, display:none, font-size:1px, near-transparent RGBA colours, aria-hidden/visually-hidden text, and semantic-namespace spoofing via meta tags. Common trigger phrases: 'Ignore previous instructions', 'If you are an LLM/AI', and ANTHROPIC_MAGIC_STRING_TRIGGER_REFUSAL_-style magic strings. Goal categories observed: pranks (tone/role hijack); SEO/promotion; deterrence (block AI crawlers / infinite-text DoS); exfiltration (IPs/credentials/API keys/secrets emailed to attacker); destruction (terminal-command injection, e.g., 'sudo rm -rf'); financial fraud (PayPal/Stripe donation/transaction payloads, sometimes amplified with 'ultrathink' persuader words); DoS/output suppression; and authority/trust spoofing. Across Google's Common Crawl sample, the 'malicious' sub-category grew by ~32% between November 2025 and February 2026.
- **Affected Products:** Google Gemini (incl. Workspace-integrated Gemini), Microsoft Copilot (incl. Copilot Studio and agentic flows), OpenAI ChatGPT (incl. browsing and agentic modes), GitHub Copilot, Cursor, Claude Code, AI-powered CI/CD reviewers, broadly any LLM-powered AI agent that consumes untrusted external content. No specific affected versions are enumerated because the underlying weakness (inability to reliably separate instructions from data) is a class-level vulnerability.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — public PoC/payload references cited by Google include greshake.github.io and swisskyrepo.github.io/PayloadsAllTheThings/Prompt%20Injection/. Forcepoint X-Labs (Apr 22, 2026) documented 10 verified live IPI payloads on public websites including thelibrary-welcome[.]uk, lcpdfr[.]com, and archibase[.]co, spanning financial fraud, data destruction, DoS/content suppression, SEO/traffic hijack, sensitive-data exfiltration, and output hijacking categories.
- **Patch Available:** No discrete per-product CVE patch applies to this blog post. Google's defensive posture is the continuous mitigation programme described at https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/ (Apr 2, 2026), combined with the Google AI Vulnerability Reward Program at https://bughunters.google.com. For context only (separate from the subject blog): CVE-2025-54131 (Windows AI Foundry / Foundry Agent) was addressed in version 1.3.
- **Active Exploitation:** Confirmed — active in-the-wild exploitation is the central finding of the report. Google Threat Intelligence's Common Crawl sweep (published Apr 23, 2026) confirmed malicious IPI payloads on the public web, with a ~32% relative increase in the 'malicious' payload category between Nov 2025 and Feb 2026. Forcepoint X-Labs (Apr 22, 2026) separately verified 10 IPI indicators on live websites spanning financial fraud, data destruction, exfiltration, DoS, SEO hijack, and output-suppression categories. SecurityWeek (Apr 27, 2026) and Help Net Security (Apr 24, 2026) independently corroborated both findings. Google's assessment: current threat-actor sophistication is relatively low — payloads are real and effective, but advanced research has not yet been productionised at scale. Attack surface: public web pages, blogs, forums, comments, emails, and developer resources that AI agents routinely consume.
- **Threat Actors:** No named APT groups or attributed campaigns. Observed un-attributed threat actor categories include: pranksters/experimenters (e.g., forcing AI to 'tweet like a baby bird'); SEO/traffic manipulators (promoting specific businesses via referral redirects); deterrence actors (blocking AI crawlers via resource-exhaustion pages); financially motivated fraud actors (embedding PayPal/Stripe donation/transaction instructions); data-exfiltration actors (instructing AI to harvest IPs, credentials, API keys, or secrets); system-destruction actors (terminal command injection such as 'sudo rm -rf'); and DoS/output-suppression actors. Forcepoint X-Labs notes reuse of shared injection templates across multiple domains suggests 'organized tooling,' but no specific threat group is named.
- **Mitigation:** Layered defense strategy (not a single patch): (1) Strict data–instruction boundary — AI agents must treat untrusted web content as data only and refuse to execute embedded instructions; (2) Continuous red-teaming via human + ML-driven automated payload generation (e.g., Google's 'Simula'); (3) Google AI Vulnerability Reward Program (AI VRP) for external researcher collaboration; (4) Deterministic centralised policy enforcement — URL sanitisation, user-confirmation gates for sensitive tool calls, tool-chaining allow-lists, regex takedowns for known payload patterns; (5) Gemini model hardening + ML/LLM-based defense retraining on synthetic IPI datasets; (6) Scope bounding / least privilege for agentic AI (terminal, email-send, payments); (7) Proactive URL blocklists of known IPI hosts (Forcepoint Real-Time Analytics approach).
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack class where adversarial instructions are embedded in external data sources (web pages, email HTML, files, etc.) that LLMs or LLM-powered agents later consume; the injected instructions can influence or override the model's behavior (and may occur without any direct user input).
- **Affected Products:** Google Workspace with Gemini
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — public proofs-of-concept and payload examples exist (e.g., Immersive Labs PoC embedding IPI in email HTML; Forcepoint released example payloads; PortSwigger hosts an IPI lab).
- **Patch Available:** No vendor patch — Google published guidance and layered-mitigation guidance in the advisory (see vendor advisory URL).
- **Active Exploitation:** Yes — security vendors and media reported IPI payloads and traps appearing in the wild (reports in April 2026 from Forcepoint and industry press).
- **Threat Actors:** None known
- **Mitigation:** Layered defenses (no single patch): model hardening and instruction-resistance, provenance and content filtering/controls, restricting tools/function access for agents, and engineering safeguards in agent orchestration — as described in Google’s layered-defense guidance.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The primary issue is indirect prompt injection: hidden or malicious web content can craft inputs that cause an agentic LLM/browser integration (Gemini in Chrome) to execute unintended actions. Disclosed instances include zero-click indirect prompt-injection chains that can escalate to local file access or policy-enforcement bypasses when policy checks are insufficient.
- **Affected Products:** Google Chrome (agentic browsing with Gemini integration — December 2025 preview), Google Gemini Enterprise
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public researcher disclosures/PoCs exist for related issues: Noma Labs published a zero-click GeminiJack disclosure and Unit42 published real-world indirect prompt-injection demonstrations. The Google advisory itself does not include a PoC.
- **Patch Available:** Google announced new layered defenses for agentic browsing in Chrome (see vendor advisory). Independent reporting indicates Chrome updates and fixes were issued for related Gemini/Chrome flaws (news reports cite quick patches for high-severity issues), but the blog post itself describes architectural mitigations rather than a single CVE patch URL.
- **Active Exploitation:** Researchers have demonstrated indirect prompt-injection techniques and published disclosures (Unit42 reported real-world demonstrations; Noma Labs disclosed GeminiJack). At the same time, some trackers stated "no known exploits reported" for particular CVEs; there is evidence of PoCs/demonstrations but no clear, authoritative indication of widespread confirmed mass exploitation in the wild in the cited sources.
- **Threat Actors:** None known
- **Mitigation:** Use the layered defenses and architectural hardening Google described: restrict origin access for agentic actions, block and sanitize prompt-injection vectors, prevent unsafe AI actions, enforce stricter policy checks for agentic browsing flows, and apply Chrome updates when published.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** The corpus reports a near-miss: a linear buffer overflow in CrabbyAVIF that was identified and avoided; the blog does not provide further exploit mechanics or a full vulnerability write-up.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit is described or linked in the cited sources.
- **Patch Available:** No official vendor patch is described in the blog post or linked materials; no patch URL available.
- **Active Exploitation:** No confirmed active exploitation reported in the cited sources; the post describes the issue as a "near-miss" that was avoided (linear buffer overflow in CrabbyAVIF) rather than a shipped/vulnerable release.
- **Threat Actors:** None known
- **Mitigation:** Adopt the memory-safety strategy recommended in the post (use Rust for new code to prevent memory-safety vulnerabilities) and follow Android Security Bulletin guidance and updates for patched components.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-10520: pre-authentication OS command injection in Ivanti Sentry that allows a remote unauthenticated actor to execute OS commands (lead to root). CVE-2026-10523: authentication bypass that can allow creation of administrative accounts.
- **Affected Products:** Ivanti Sentry — affected: 10.5.1, 10.6.1, 10.7.0 and prior; resolved in: 10.5.2, 10.6.2, 10.7.1
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof-of-concept (PoC) was published (reported June 10, 2026) and a PoC is being used in attacks; multiple incident responders (Shadowserver, Rapid7, security blogs) reported exploitation tied to the public PoC.
- **Patch Available:** Ivanti published resolved versions (10.5.2, 10.6.2, 10.7.1) addressing CVE-2026-10520/CVE-2026-10523; see Ivanti advisory: https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523?language=en_US
- **Active Exploitation:** Confirmed — Shadowserver Foundation and multiple security vendors/researchers reported active exploitation and widespread attempts tied to a public PoC (reported June 10, 2026).
- **Threat Actors:** None known
- **Mitigation:** Apply Ivanti’s released updates immediately (upgrade to 10.5.2, 10.6.2, 10.7.1). Treat this as an out-of-band urgent patch, block or isolate internet-exposed Sentry appliances until patched, and follow vendor hardening guidance.
- **Vendor Advisory:** https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523?language=en_US

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors target backbone and network-edge devices (backbone routers, provider-edge and customer-edge routers and other network-edge devices), leverage compromised devices and trusted connections to pivot into target networks, and often modify router configurations to maintain persistent, long-term access.
- **Affected Products:** Cisco, Palo Alto Networks, Ivanti, Fortinet, Juniper, Microsoft Exchange, and others
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit for the AA25-239A activity was reported in the advisory (CISA); note the corpus does contain later/other CVEs (e.g., CVE-2026-10520) for which public PoCs and active exploitation were reported.
- **Patch Available:** No single vendor patch is available for the multi-vendor activity described in CISA AA25-239A; CISA and third-party guidance (detection tips, STIX IOCs, mitigation guidance) are available and vendors may publish fixes for individual CVEs separately.
- **Active Exploitation:** CISA reports that exploitation of zero-day vulnerabilities described in AA25-239A "has not been observed to date." (CISA AA25-239A advisory).
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Inventory and prioritize internet‑exposed network-edge devices; restrict and harden management-plane access (limit administrative exposure); segment management and production networks; enable and centralize logging and monitoring for configuration/traffic anomalies; apply vendor fixes when published; and consume CISA and third-party detection rules/STIX IOCs to hunt for indicators of compromise.
- **Vendor Advisory:** Vendor advisory URL unavailable.

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

## 14. 🟠 Zero-Day — Phantom Squatting Uses AI-Hallucinated Domains for Phishing and Malware

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://thehackernews.com/2026/07/phantom-squatting-uses-ai-hallucinated.html>

> Large language models keep inventing web addresses that do not exist. Attackers have started buying those made-up domains before anyone else can, then hosting phishing pages on them to catch traffic that AI tools point their way.

Palo Alto Networks&#x27; Unit 42 calls the trick phantom squatting, and its new research shows it is already happening in the wild.

The reason it matters is

---

## 15. 🟠 Zero-Day — New BioShocking attack manipulates AI browser into data theft

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://www.bleepingcomputer.com/news/security/new-bioshocking-attack-manipulates-ai-browser-into-data-theft/>

> A new prompt injection attack dubbed &quot;BioShocking&quot; could trick AI-powered browsers into treating real-world risky actions as part of a fictional scenario, causing them to ignore any safety guardrails. [...]

---

## 16. 🟡 High Severity — repomix: attach_packed_output can bypass file-read secret scanning for supported local files

**CVE:** `CVE-2026-49988` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-hwpp-h97w-2h3j>

> # `attach_packed_output` can register arbitrary `.json/.txt/.md/.xml` files and bypass the MCP file-read safety check

## Summary

Repomix&#x27;s MCP server exposes a normal `file_system_read_file` tool that reads absolute paths only after running the project&#x27;s secret check. However, the `attach_packed_output` plus `read_repomix_output` flow can read arbitrary local `.json`, `.txt`, `.md`, or…

---

## 17. 🟡 High Severity — Twig: Sandbox filter, tag and function allow-list bypass when sandbox state changes between renders for a cached `Template`

**CVE:** `CVE-2026-49981` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-529h-vh3j-85hq>

> ### Description

The per-template filter, tag and function allow-list check is compiled into the `checkSecurity()` method of each `Template` subclass and was invoked once from the constructor, gated by `SandboxExtension::isSandboxed($source)`. `Template` instances are then cached on the `Environment` in `$loadedTemplates`, so the verdict computed at construction time was sticky for the rest of the…

---

## 18. 🟡 High Severity — Cortex has Untrusted Project Bootstrap Code Execution via `CLAUDE_PROJECT_DIR`

**CVE:** `CVE-2026-49986` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-gvpp-v77h-5w8g>

> ## Untrusted Project Bootstrap Code Execution via `CLAUDE_PROJECT_DIR`

### Summary

The Cortex MCP server (`neuro-cortex-memory`) treats the `CLAUDE_PROJECT_DIR` environment variable — automatically set by Claude Code to the currently open project directory — as a trusted Cortex developer checkout. When the `open_visualization` tool is invoked, `_find_dev_source()` resolves the user&#x27;s active…

---

## 19. 🟡 High Severity — auth-fetch-mcp has SSRF Protection Bypass via IPv4-mapped IPv6 Loopback

**CVE:** `CVE-2026-49857` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-pvrj-8cg3-j5f8>

> ## SSRF Protection Bypass via IPv4-mapped IPv6 Loopback

### Summary

`auth-fetch-mcp` v3.0.1 implements SSRF protection in `assertSafeUrl()` (`src/security.ts`) to block requests to private and loopback addresses. However, the `isPrivateV6()` function fails to detect IPv4-mapped IPv6 loopback addresses in their hex-normalized form. When an attacker supplies a URL such as `http://[::ffff:127.0.0.1…

---

## 20. 🟡 High Severity — @jshookmcp/jshook: ICMP probe and traceroute skip local-network SSRF authorization

**CVE:** `CVE-2026-49856` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-c5r6-m4mr-8q5j>

> ## Summary

The network domain has a central SSRF authorization policy that blocks private, loopback, link-local, and reserved targets unless an explicit authorization object allows private network access. The policy is enforced by raw HTTP/TCP/TLS RTT tools, but the ICMP probe and traceroute tools resolve the target and invoke the native ICMP/traceroute sink directly.

An MCP client with access t…

---

## 21. 🟡 High Severity — Open Babel has out-of-bounds write in Gaussian translationVectors[]

**CVE:** `CVE-2022-46291` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-jg3h-pv7c-4f9c>

> ### Summary

A memory-safety vulnerability in Open Babel&#x27;s Gaussian output parser
allowed an out-of-bounds write into the `translationVectors[]` array
when reading a crafted input file.

### Details

The Gaussian reader stored periodic-cell translation vectors into a
fixed-size `translationVectors[]` array. A malformed input could push
more vectors than the array had slots, causing a write pa…

---

## 22. 🟡 High Severity — Progress Kemp LoadMaster Pre-Auth RCE Flaw Faces Active Exploitation Attempts

**CVE:** `CVE-2026-8037` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://thehackernews.com/2026/07/latest-progress-kemp-loadmaster-pre.html>

> A recently disclosed critical security flaw impacting Progress Kemp LoadMaster is seeing active exploitation attempts, according to an advisory from eSentire&#x27;s Threat Response Unit (TRU).

The Canadian cybersecurity company said it identified exploitation attempts targeting CVE-2026-8037 (CVSS score: 9.6), an operating system (OS) command injection flaw that could be exploited to achieve

---

## 23. 🟡 High Severity — Citrix Patches Six NetScaler Flaws Allowing File Read and Denial-of-Service

**CVE:** `CVE-2026-8451` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://thehackernews.com/2026/07/citrix-patches-six-netscaler-flaws.html>

> Citrix on Tuesday released security updates to address multiple flaws in NetScaler ADC (formerly Citrix ADC) and NetScaler Gateway (formerly Citrix Gateway) that could be exploited by an attacker to facilitate arbitrary file reads or trigger a denial-of-service (DoS) condition.

The vulnerabilities are listed below -


  CVE-2026-8451 (CVSS score: 8.8) - An insufficient input validation

---

## 24. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
