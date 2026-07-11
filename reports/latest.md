# Zero Day Pulse

> **Generated:** 2026-07-11 12:50 UTC &nbsp;|&nbsp; **Total:** 25 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 11 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** SimpleHelp v5.5.7 and earlier contain multiple unauthenticated path traversal vulnerabilities in the web server component. By sending crafted HTTP requests with directory-traversal sequences to exposed file-fetch endpoints, a remote unauthenticated attacker can read arbitrary files from the SimpleHelp host, including server configuration files that store hashed technician passwords, API tokens, and other secrets. This enables credential theft and lateral movement to downstream RMM customers. Public PoC code (imjdl/CVE-2024-57727), a Metasploit auxiliary module, and a Nuclei template are available, significantly lowering the exploitation barrier.
- **Affected Products:** SimpleHelp Remote Support / RMM versions 5.5.7 and earlier (all releases prior to 5.5.8, 5.4.10, and 5.3.9)
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true - https://github.com/imjdl/CVE-2024-57727 ; Metasploit auxiliary module (simplehelp_toolbox_path_traversal); Nuclei template https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2024/CVE-2024-57727.yaml
- **Patch Available:** true - https://guides.simple-help.com/kb---security-vulnerabilities-01-2025
- **Active Exploitation:** true - confirmed by CISA advisory AA25-163A (https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a); also listed in the CISA KEV catalog.
- **Threat Actors:** Ransomware actors (unnamed in CISA AA25-163A); DragonForce ransomware group (Sophos/SecurityWeek reporting on May 2025 MSP campaign); Microsoft-tracked cluster Storm-1175 (linked to Medusa ransomware affiliate activity)
- **Mitigation:** Upgrade SimpleHelp to version 5.5.8 (or apply v5.4.10 / v5.3.9 for older release branches) immediately. After patching: (1) rotate all SimpleHelp administrator/technician passwords and any secrets stored in configuration files; (2) restrict network access to the SimpleHelp management interface via firewall / IP allow-listing; (3) disable unnecessary web/file-browsing endpoints; (4) monitor HTTP logs for path-traversal attempts; (5) hunt for and remediate indicators of compromise published with CISA AA25-163A and Sophos DragonForce reporting.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — 'Ghostcommit' hides prompt injection in images to fool AI agents, steal secrets

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-07-11
**Reference:** <https://www.bleepingcomputer.com/news/security/ghostcommit-hides-prompt-injection-in-images-to-fool-ai-agents-steal-secrets/>

> A PNG hiding a prompt injection could steal your repo&#x27;s secrets, researchers demonstrate. The technique, dubbed &#x27;Ghostcommit,&#x27; slipped past AI code reviewers CodeRabbit and Bugbot, which never open image files at all, then convinced a coding agent to read a repo&#x27;s .env and write every secret into the code as a list of numbers. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Ghostcommit is a two-phase attack targeting AI-assisted code review and coding agent pipelines. Phase 1 (Delivery/Bypass): An attacker opens a pull request adding an agent-convention file (e.g., AGENTS.md) referencing a PNG image, plus the PNG itself. The PNG embeds a natural-language prompt-injection payload. Text-based AI reviewers (CodeRabbit, Cursor Bugbot) treat the PNG as an opaque binary blob and never inspect it, so they wave the PR through to merge. Phase 2 (Trigger/Exfiltration): A developer later asks a vision-capable coding agent (Cursor, Antigravity, Codex CLI) to scaffold a new module. The agent reads AGENTS.md, follows the pointer to the PNG, parses the embedded instructions, and is told to open .env, read each byte, encode it as the integer value of the byte's ASCII codepoint, and emit the result as a Python/Rust constant (e.g., _PROV_CANARY = (111, 46, 65, 80, 73, ...)). When the developer commits the generated module, the repository's git history permanently contains the entire .env file as a tuple of small integers. Conventional secret scanners miss it because the bytes never appear as plaintext. The attacker then clones the public commit and runs the supplied decoder script to recover the original secrets.
- **Affected Products:** Cursor Bugbot (AI code reviewer), CodeRabbit (AI code reviewer), Cursor IDE (with Claude Sonnet 4.6, Composer-2, GPT-5.5), Antigravity (with Claude Sonnet 4.6, Gemini 3.1 Pro, Gemini 3 Flash, Opus), Codex CLI (with GPT-5.4). Specific version numbers were not published.
- **CVSS Score:** CVSS score unavailable. No CVE ID has been assigned and no CVSS score has been published.
- **CVSS Vector:** CVSS vector unavailable. No CVE ID has been assigned and no CVSS vector has been published.
- **Exploit Available:** true - Public PoC available at https://github.com/asset-group/ghostcommit
- **Patch Available:** false - No vendor patches have been released as of the disclosure date (2026-07-11). All affected vendors were notified prior to public disclosure, but no security advisory URLs or patch release notes have been published.
- **Active Exploitation:** false - No in-the-wild exploitation has been reported. The technique has only been demonstrated by the ASSET Research Group against their own isolated test repositories; there is no evidence of use by any threat actor.
- **Threat Actors:** None known. This is an academic/research disclosure from the ASSET Research Group at the University of Missouri-Kansas City; no in-the-wild exploitation or threat actor attribution has been reported.
- **Mitigation:** Until vendor patches ship, defenders should: (1) require human review for any PR that introduces or modifies agent-convention files (AGENTS.md, CLAUDE.md, .cursorrules, .cursor/rules, copilot-instructions.md, etc.) or adds images referenced by them; (2) deploy a multimodal PR-defender that runs an LLM pass over both the diff and the actual image bytes, looking for hidden instructions, steganography, invisible characters, and anomalous code shapes (the researchers released one alongside the PoC); (3) instrument coding agents at runtime to alert or block any access to .env, *.pem, id_rsa, credentials.json, and other secret-bearing files that is not strictly justified by the user's request; (4) disable automatic execution of agent-convention files in untrusted repositories; and (5) ensure secret-scanning tools (e.g., gitleaks, trufflehog) are configured to also flag integer-tuple and large-string-literal constant patterns, not only raw high-entropy strings.
- **Vendor Advisory:** https://asset-group.github.io/disclosures/ghostcommit/

---

## 3. 🟠 Zero-Day — Weekly Metasploit Update: Exploits for FlowiseAI CSV Agent and MacOS Package Kit

**CVE:** `CVE-2026-41264` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-07-11
**Reference:** <https://www.rapid7.com/blog/post/pt-weekly-metasploit-update-exploits-for-flowiseai-csv-agent-and-macos-package-kit>

> More AI, more software, more bugs! AI, it&#x27;s all you hear about nowadays and everyone&#x27;s got an opinion on it. Here at Metasploit, we care less about those opinions and more about the growing attack surface all this new software brings with it (yeehaw exploits!). Take for example the new Flowise CSV Agent Prompt Injection RCE brought to you by Takahiro Yokoyama and zdi-disclosures. Flowise…

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated remote code execution via the CSV_Agents class in Flowise. The CSV Agent uses an LLM to generate Python code that is then executed server-side. A pre-execution validator (pythonCodeValidator.ts) only inspects the token immediately following an 'import' keyword (e.g., a regex like /\bimport\s+(?!pandas|numpy\b)/g), so a single statement such as `import pandas as np, os as pandas` bypasses the filter and rebinds the 'pandas' name to the 'os' module. Subsequent LLM-generated code can then invoke pandas.system(...) (or any other OS primitive) to execute arbitrary commands inside the Pyodide/Python sandbox running within the Node.js Flowise server process. Unauthenticated attackers can reach the vulnerable code path by sending crafted prompts to any chatflow that exposes a CSV Agent node via the public POST /api/v1/prediction/<chatflow-id> endpoint, achieving RCE under the Flowise service account.
- **Affected Products:** FlowiseAI Flowise npm package <= 3.0.13, FlowiseAI flowise-components npm package <= 3.0.13
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Upgrade both `flowise` and `flowise-components` to v3.1.0 or later (the fix removes dangerous imports in the CSV Agent sandbox). If immediate upgrade is not possible: (1) disable or remove all CSV Agent nodes from existing chatflows; (2) place the Flowise instance behind an authentication layer or reverse proxy that requires SSO so unauthenticated users cannot reach the /api/v1/prediction/<chatflow-id> endpoint; (3) restrict outbound LLM endpoints to trusted providers to prevent an authenticated user from pointing a chatflow at an attacker-controlled LLM that returns malicious Python; (4) monitor Flowise logs and the host for unexpected child processes spawned by the Node.js/Pyodide runtime.
- **Vendor Advisory:** https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-3hjv-c53m-58jj

---

## 4. 🟠 Zero-Day — mcp-atlassian: Arbitrary file read via missing path validation in confluence_upload_attachment

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-g5r6-gv6m-f5jv>

> ### Summary
`confluence_upload_attachment` passes `file_path` directly to `open(file_path, &quot;rb&quot;)` with no path validation. Any authenticated MCP client — or an AI agent manipulated via prompt injection — can read any file the server process can access and exfiltrate it to Confluence as an attachment.

### Details
Root cause: `src/mcp_atlassian/confluence/attachments.py`, `_upload_attachm…

**Parallel AI Enrichment:**

- **Technical Details:** The `confluence_upload_attachment` tool in `src/mcp_atlassian/confluence/attachments.py` passes the user-supplied `file_path` argument directly to Python's built-in `open(file_path, "rb")` without calling the existing `validate_safe_path()` helper that `download_attachment()` already uses. As a result, any authenticated MCP client (or an AI agent tricked via prompt injection into calling the tool) can read any file the server process has OS-level access to and POST it to Confluence as an attachment. On Linux, `/proc/self/environ` contains all environment variables the server was launched with (e.g., CONFLUENCE_API_TOKEN, AWS keys, DB credentials), enabling full Atlassian account takeover and lateral movement. CWE-22 Path Traversal.
- **Affected Products:** mcp-atlassian (Python pip package, sooperset/mcp-atlassian), versions < 0.22.0
- **CVSS Score:** 7.7
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Exploit Available:** true — Public PoC demonstrated by reporter @rainfantry; prompt injection PoC confirmed against qwen2.5:7b via Open WebUI on 2026-07-10
- **Patch Available:** true — Fixed in mcp-atlassian 0.22.0 (released 2026-07-10): https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-g5r6-gv6m-f5jv. No CVE has been assigned.
- **Active Exploitation:** false — PoC exploitation confirmed by researcher @rainfantry, but no confirmed in-the-wild exploitation by named threat actors and no CISA KEV listing as of advisory publication.
- **Threat Actors:** None known
- **Mitigation:** Upgrade mcp-atlassian to version 0.22.0 or later. Until patched, restrict the MCP server's filesystem permissions, run it under a least-privileged service account, sandbox the AI agent so untrusted content (Jira tickets, Confluence pages) cannot reach tool-calling context, and require human confirmation for any tool call reading paths outside an allow-list.
- **Vendor Advisory:** https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-g5r6-gv6m-f5jv

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an AI system (e.g., Gemini, an AI agent) processes external content (web page, email, calendar invite, document) containing attacker-supplied instructions. Because the LLM treats retrieved content and user instructions within the same context window, the hidden instructions can override the original user intent. Google taxonomizes observed payloads into five categories: (1) Harmless pranks (forcing the assistant to speak in a particular tone or character); (2) Helpful guidance (injecting extra context into summaries); (3) SEO manipulation (prompt-injection frameworks steering AI-generated answers toward promoted products or phishing sites); (4) Deterring AI agents (text like 'If you are an AI, do not crawl this site' or streams of text designed to cause timeouts, token-budget exhaustion, or denial-of-service); and (5) Malicious actions (attempts to exfiltrate user data, drive the agent to delete local files, invoke connected tools/plugins such as email, calendar, or code-execution on the attacker's behalf, or hijack the conversation). Attack vector: attacker-controlled web/email/document content → retrieval by an AI agent → poisoned instructions fused into the model prompt → unauthorized tool calls or output manipulation.
- **Affected Products:** Google Gemini (including Gemini app and Gemini in Workspace), Google AI agents, and AI assistants generally. No specific version numbers are provided; the blog discusses the class of AI products that consume untrusted external content (web pages, email, documents).
- **CVSS Score:** CVSS score unavailable. No CVE has been issued and no CVSS base score has been published for this vulnerability class.
- **CVSS Vector:** CVSS vector unavailable. No CVE has been assigned and no CVSS v3 vector has been published for this vulnerability class as described in the Google Security Blog post.
- **Exploit Available:** true - Multiple public proof-of-concept implementations exist, including repositories on GitHub such as swisskyrepo/PayloadsAllTheThings (Prompt Injection section) and brennanbrown/atlas-prompt-injection-poc. Google and Forcepoint researchers also observed real-world IPI payloads via crawls of public web content.
- **Patch Available:** false - No specific vendor software patch is referenced in the Google Security Blog post. Google describes ongoing 'hardening' of its AI models and products, layered defenses for Gemini in Workspace, and continuous red-team pressure-testing, but the blog is a research/threat-intelligence write-up rather than a security advisory with a fixed patch version. End users should keep Gemini and Workspace clients up to date and follow Google's published Workspace mitigation guidance for Gemini features.
- **Active Exploitation:** true - Google confirms active exploitation/experimentation in the wild. The blog states that 'attackers are experimenting with IPI on the web,' documents real-world examples observed via crawls of public web content (including invisible HTML instructions telling crawlers/agents to ignore previous instructions, anti-bot/anti-agent deterrence strings, and early-stage data-exfiltration attempts), and reports a 32% relative increase in the malicious category between November 2025 and February 2026. Independent coverage from Help Net Security (April 24, 2026) and Palo Alto Networks Unit 42 (March 3, 2026) corroborates Google's findings.
- **Threat Actors:** None known. The Google Security Blog post refers only to generic 'attackers,' 'adversaries,' and 'website authors' conducting IPI experiments. No specific APT group, cybercrime gang, or ransomware operator is named.
- **Mitigation:** Google recommends a layered defense strategy: (1) Treat all retrieved/external content as untrusted data and separate it from system instructions using techniques such as spotlighting and instruction hierarchy; (2) Harden model behavior against adversarial manipulation through red-teaming ('relentless pressure-testing'); (3) Operate the Google AI Vulnerability Reward Program to incentivize external researcher reports; (4) Leverage Google's global-scale, real-time data processing to identify and neutralize IPI threats at the source (e.g., search-quality demotion of SEO-poisoned pages); and (5) Enforce least-privilege on agent tools so a hijacked model cannot arbitrarily call sensitive APIs without user confirmation. Practical hardening guidance: strip/ignore instructions embedded in fetched content, require explicit user confirmation for destructive or exfiltrating tool calls, sandbox agent code execution, and monitor for anomalous outbound network or file-system actions.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is a class of attack in which an adversary embeds malicious natural-language instructions inside untrusted content (emails, calendar events, shared documents, web pages, tool outputs) that an LLM-powered assistant such as Gemini retrieves while fulfilling a user's query. Because the assistant merges this external content into its prompt context, the hidden instructions can hijack the model's behavior — causing data exfiltration, unauthorized actions (e.g., sending mail, deleting calendar events), bypass of authorization checks, or misleading summaries — even when the user never typed the malicious instruction directly.
- **Affected Products:** Google Workspace with Gemini (Gmail, Docs, Drive, Chat, Calendar integrations) and the consumer Gemini app (as of April 2026)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Google applies a layered defense to Workspace with Gemini: (1) Deterministic defenses — user confirmation before sensitive/destructive actions, URL sanitization, strict tool-chaining allow-lists, and markup/markdown sanitization to strip embedded scripts or hidden links. (2) ML-based defenses — classifiers trained to detect prompt-injection patterns in retrieved content, retrained using adversarial data from internal red-teaming, automated red-teaming, the AI VRP, and monitoring of newly disclosed attacks. (3) LLM-based defenses — system prompts that reinforce security intent and instruct the model to ignore instructions found inside untrusted data, plus intrinsic model-level hardening. (4) User-in-the-loop controls — confirmation prompts before consequential actions (sending mail, deleting events, external sharing) and security notifications when Gemini blocks a suspected attack, with links to help-center guidance. (5) Administrative controls — Workspace admins can disable Gemini features acting on Gmail/Drive/Calendar, restrict Gemini apps via allow-lists, and enforce DLP/sharing policies. (6) User hardening — treat AI-generated summaries as untrusted, verify any proposed action before confirming, and avoid pasting untrusted content into prompts where avoidable.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The advisory is not a vulnerability disclosure but a proactive security architecture post by Google's Chrome security team. The primary new threat it identifies is indirect prompt injection, where untrusted web content (malicious sites, third-party iframe content, or user-generated content such as reviews) embeds instructions that cause the Gemini-powered agent to perform unwanted actions such as initiating financial transactions or exfiltrating sensitive data. Because Gemini's planning model reads the same web content where the attack resides, it is inherently exposed. Google's layered mitigations include: (1) a User Alignment Critic — a separate Gemini model isolated from untrusted web content that vets each proposed action against the user's stated goal and can veto/replan on misalignment; (2) Agent Origin Sets — an extension of Chrome's Site Isolation that architecturally constrains the agent to only the origins a gating function deems relevant, blocking cross-site data leakage; (3) mandatory user confirmations for sensitive actions such as banking interactions or Password Manager–mediated sign-ins; (4) an on-device prompt-injection detection classifier working alongside Safe Browsing and scam detection; and (5) automated red-teaming combined with a Chrome bug-bounty program offering up to $20,000 for breaking the new defenses. No specific CVE, exploit chain, or vulnerable code path is disclosed in the post.
- **Affected Products:** Google Chrome with Gemini in Chrome agentic capabilities (no specific version range was disclosed in the advisory; the post addresses the Gemini-in-Chrome integration and upcoming agentic browsing features broadly)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** No patch is applicable because the post is a proactive architecture announcement rather than a fix for a specific disclosed vulnerability. Recommended hardening: keep Chrome updated to the latest stable release so that auto-update delivers any related defensive updates; enable Safe Browsing and Chrome's enhanced scam/phishing protections; treat any unexpected agent action on financial or sensitive sites as a prompt-injection red flag and rely on the User Alignment Critic's confirmation prompts; minimize the origins the Gemini agent is permitted to interact with on a given task; and report suspected indirect prompt injection bypasses to the Chrome bug-bounty / VRP program (Google advertises rewards up to $20,000 for breaking the new defenses).
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2025-48530 is a linear buffer overflow (CWE-125, Out-of-Bounds Read) in CrabbyAVIF, the Rust-based AVIF image parser/decoder shipped in the Android platform. The bug originated in an unsafe Rust block where incorrect bounds checks on NV12 chroma plane dimensions allowed out-of-bounds accesses against YUV/alpha/UV plane buffers and the row-byte calculation. Because the AVIF decoder processes untrusted image content, the flaw was remotely reachable (e.g., zero-click scenarios via received media) without user interaction or execution privileges, and could be chained with other bugs for remote code execution. Android's Scudo hardened allocator mitigated exploitation by placing guard pages around secondary allocations, causing crashes on attempted exploitation.
- **Affected Products:** Google Android 16 and Android 16-next (System component: CrabbyAVIF AVIF image parser/decoder, specifically NV12 handling paths including YUV planes, alpha plane, Y plane, UV planes, chroma width, plane size, and row bytes calculations).
- **CVSS Score:** 8.1 (third-party scoring by SentinelOne; Google's official score not published)
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H (third-party scoring by SentinelOne; Google has not published an official CVSS vector)
- **Exploit Available:** false
- **Patch Available:** true - https://source.android.com/docs/security/bulletin/2025-08-01
- **Active Exploitation:** false
- **Threat Actors:** None known. The vulnerability was identified and remediated internally before being shipped in a public Android release; no exploitation by threat actors, APT groups, or ransomware operators has been reported.
- **Mitigation:** Apply the Android security patch level 2025-08-05 or later via the August 2025 Android Security Bulletin. Defense-in-depth is provided by Android's Scudo hardened allocator, which inserts guard pages around secondary allocations so that out-of-bounds accesses fault rather than achieve code execution. No pre-patch workaround is needed because the vulnerable code path never shipped to a public Android release.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is an attack class against LLM-based assistants in which an adversary embeds malicious instructions in third-party content the model will later process (e.g., emails, documents, calendar invites, web pages, or push notifications). When the user asks Gemini to summarize, act on, or interact with that content, the hidden instructions are concatenated into the model's prompt context. Because LLMs cannot reliably distinguish trusted system instructions from untrusted data, the model can be coerced into overriding its system prompt and (a) exfiltrating sensitive user data (emails, files, contacts) to an attacker-controlled destination, (b) performing unauthorized tool/agent actions (sending email, controlling smart-home devices, calling APIs), or (c) producing attacker-influenced output. Indirect prompt injection differs from direct prompt injection in that the attacker never interacts with the Gemini chat UI directly; the malicious payload rides in via untrusted external data sources. The SafeBreach Labs PoC refined two notable sub-techniques: (1) 'Fake Context Alignment' — crafting injected text so it mimics a prior system or assistant turn to gain the model's trust; and (2) 'Delayed Tool Invocation' — deferring malicious tool calls until after the user-visible response, so the user sees a benign answer while the side-effect executes.
- **Affected Products:** Google Gemini app (consumer-facing); Gemini in Google Workspace (Gmail, Google Docs/Sheets/Slides editors, Google Drive, Google Chat); Gemini 2.5 family of foundation models (including Gemini 2.5 Pro and Gemini 2.5 Flash); Gemini-powered agents, extensions, and connectors. The SafeBreach Labs PoC specifically targeted the Gemini AI assistant on Android that summarizes messaging-app notifications (SMS, WhatsApp, Slack, etc.).
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable. Google did not assign a CVE identifier or CVSS v3 vector to this class of vulnerability; the advisory describes a category of attacks (indirect prompt injection) and a defense-in-depth strategy rather than a single CVE-numbered flaw.
- **Exploit Available:** true — Source: https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/ (SafeBreach Labs PoC for notification-based indirect prompt injection against Gemini on Android, disclosed August 2025 and patched November 2025). Secondary coverage: https://www.darkreading.com/application-security/malicious-notifications-could-trick-google-gemini-users and https://www.securityweek.com/gemini-voice-assistant-hijacked-via-messaging-notifications/
- **Patch Available:** true — Patch/advisory URL: https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html. The layered mitigations described in the June 13, 2025 blog post are deployed across the Gemini app and Gemini in Workspace. The SafeBreach Labs-reported Gemini voice-assistant notification-injection issue was separately fixed by Google in mid-November 2025 (per SecurityWeek and Dark Reading coverage).
- **Active Exploitation:** false — Google has not publicly reported confirmed in-the-wild exploitation of indirect prompt injection against Gemini. The SafeBreach Labs disclosure is a responsible-research proof-of-concept, not observed attacker activity. Google states its layered defenses have consistently mitigated indirect-prompt-injection attempts observed against Gemini to date.
- **Threat Actors:** None known. Google has not attributed in-the-wild exploitation of indirect prompt injection against Gemini to any specific threat actor group. The most prominent public demonstration was by SafeBreach Labs (responsible disclosure). Google's Threat Intelligence Group has separately tracked adversarial misuse of generative AI by actors including APT45 (North Korea-linked), TeamPCP/UNC6780, and pro-Russia influence operators, but those observations concern use of AI to enhance traditional operations rather than exploitation of Gemini via indirect prompt injection.
- **Mitigation:** Google has deployed a multi-layered defense-in-depth strategy across Gemini rather than a single patch: (1) Adversarial training and hardening of Gemini 2.5 models against prompt-injection payloads; (2) Purpose-built ML content classifiers that detect and block suspected prompt-injection inputs before they reach the model; (3) 'Security thought reinforcement' — contextual system-instruction scaffolding reminding the model to ignore directives embedded in retrieved content; (4) Markdown sanitization and suspicious-URL redaction backed by Google Safe Browsing to strip embedded links/scripts and neutralize exfiltration channels; (5) A user-confirmation / human-in-the-loop (HITL) framework requiring explicit user approval before sensitive actions such as sending email, sharing data, or controlling connected devices; (6) End-user security-mitigation notifications and Workspace help-center articles when an attempted attack is detected or mitigated. Recommended hardening for Workspace admins: enable enhanced DLP for Gemini, restrict agent/connector permissions, audit which third-party data sources Gemini can ingest, and review AI-generated actions. For users: treat AI-summarized notifications and untrusted document content as untrusted input, and confirm sensitive actions.
- **Vendor Advisory:** https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors exploit known vulnerabilities in network edge devices (routers, VPNs, firewalls) to gain initial access. They chain authentication-bypass bugs with command-injection/RCE bugs (e.g., Ivanti CVE-2023-46805 + CVE-2024-21887; Cisco CVE-2023-20198 + CVE-2023-20273) and use single-CVE exploits against Palo Alto Networks GlobalProtect (CVE-2024-3400) and Cisco Smart Install (CVE-2018-0171). After access, they modify router configurations for persistence: create ACLs named with numbers like 10, 20, 50 to whitelist attacker IPs; enable services on non-standard ports (SSH/SFTP/RDP/HTTP) including doubled ports like 22x22; redirect TACACS+ traffic to actor-controlled IPs to harvest credentials; abuse Cisco Guest Shell containers to stage tools and capture TACACS+/RADIUS authentication traffic; configure GRE/IPsec tunnels, SPAN/RSPAN/ERSPAN mirroring, and TFTP exfiltration of BGP/RSVP/MIB/MPLS data. They pivot through trusted provider-to-provider and provider-to-customer links, use LOLBins, deploy virtualized containers on network devices for evasion, and use bespoke tools (e.g., cmd1, cmd3, new2, sft) for staged data exfiltration.
- **Affected Products:** Ivanti Connect Secure (versions 9.x, 22.x) and Ivanti Policy Secure (versions 9.x, 22.x); Palo Alto Networks PAN-OS with GlobalProtect feature; Cisco IOS and IOS XE (including Web UI feature and Smart Install); large backbone routers, provider edge (PE) routers, and customer edge (CE) routers from multiple vendors
- **CVSS Score:** CVSS score unavailable (no single CVSS for the advisory; individual CVE base scores: CVE-2024-3400 = 10.0, CVE-2023-20198 = 10.0, CVE-2024-21887 = 9.1, CVE-2023-46805 = 8.2, CVE-2023-20273 = 7.2, CVE-2018-0171 = 9.8)
- **CVSS Vector:** CVSS vector unavailable (AA25-239A is a multi-CVE Joint Cybersecurity Advisory describing a threat campaign, not a single vulnerability; individual CVE vectors include CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H for CVE-2024-3400 and CVE-2023-20198, CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H for CVE-2024-21887 and CVE-2023-20273, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H for CVE-2023-46805)
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor (PRC state-sponsored cyber threat actors; associated entities include Sichuan Juxinhe Network Technology Co., Ltd.; Beijing Huanyu Tianqiong Information Technology Co., Ltd.; and Sichuan Zhixin Ruijie Network Technology Co., Ltd.)
- **Mitigation:** Apply vendor patches for exploited CVEs (CVE-2024-21887, CVE-2023-46805, CVE-2024-3400, CVE-2023-20198, CVE-2023-20273, CVE-2018-0171). Upgrade unsupported/EoL network devices to supported models. Hunt for IOCs: ACLs named 'access-list 20', '10', or '50'; non-standard SSH/HTTP ports including doubled ports (e.g., 22x22); abnormal TACACS+/RADIUS server IPs; unauthorized Guest Shell enablement; SPAN/RSPAN/ERSPAN sessions; unknown GRE/IPsec tunnels. Compare running and startup configurations against a known-good baseline. Verify firmware/image hashes against vendor values and enable secure boot / signed image enforcement. Disable unused services (Telnet, Smart Install, HTTP, Guest Shell). Use SNMPv3 with authentication/privacy instead of default community strings. Disable unused local accounts and audit TACACS+/RADIUS configurations. Capture and review AAA traffic for unexpected destinations. Restrict management plane access to dedicated networks with strong authentication. Collect and retain logs (including disabled/deleted) for forensic review. Prioritize remediation using CISA's Known Exploited Vulnerabilities Catalog.
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

## 14. 🟠 Zero-Day — CrowdStrike Uncovers New Prompt Injection Techniques

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jul 07, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-uncovers-new-prompt-injection-techniques/>

---

## 15. 🟡 High Severity — SiYuan: Stored XSS to RCE via Unsanitized Attribute View Asset Cell Content

**CVE:** `CVE-2026-50551` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-56mp-4f3v-fgj2>

> SiYuan v3.6.5 and earlier versions contain a stored cross-site scripting (XSS) vulnerability in the Attribute View (database) asset cell renderer that escalates to remote code execution (RCE) in the Electron desktop client. This is a neighbor-bug of CVE-2026-44588: the fix for -44588 used `escapeAriaLabel()` (double-escapes `&lt;`), but the AV asset renderers were left using the weaker `escapeAttr…

---

## 16. 🟡 High Severity — prestashop/ps_facetedsearch: PHP Object Injection in faceted search cache allows unauthenticated RCE

**CVE:** `CVE-2026-54159` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-m5f5-28qr-9g9r>

> ### Impact

A PHP Object Injection vulnerability affects the PrestaShop module `ps_facetedsearch`.

The module rebuilds the selected search filters from the request URL. The value of a slider filter (**price** or **weight**) is taken from the URL without sufficient validation, then stored in an internal filter-block cache where it is serialized and later read back with a raw native `unserialize()`…

---

## 17. 🟡 High Severity — SiYuan: Stored XSS to RCE via attribute-view cell rendering in genAVValueHTML()

**CVE:** `CVE-2026-54158` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-5xfx-xj4h-5p7r>

> ### Summary

The attribute-view (database) cell renderer `genAVValueHTML` interpolates cell content raw in four of its branches: `text`, `url`, `phone`, and `mAsset`. A cell value like `&lt;/textarea&gt;&lt;img src=x onerror=&quot;...&quot;&gt;` or `&quot;&gt;&lt;img src=x onerror=&quot;...&quot;&gt;` breaks out of its surrounding tag and runs arbitrary JavaScript in the renderer when the victim o…

---

## 18. 🟡 High Severity — File Browser: Command Injection via Authentication Hook Shell Substitution (Pre-Authentication RCE)

**CVE:** `CVE-2026-54088` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-m93h-4hw7-5qcm>

> ## Overview

The Hook Authentication feature in File Browser allows administrators to delegate login verification to an external shell command. User-supplied credentials (username and password) are interpolated into this command string using `os.Expand` without sanitization. An **unauthenticated remote attacker** can inject shell metacharacters in the username or password field at the login screen…

---

## 19. 🟡 High Severity — SiYuan: Unauthenticated Admin API Access via Blanket chrome-extension:// Origin Allowlist

**CVE:** `CVE-2026-54069` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-hvr9-72v2-fff3>

> ## Summary

SiYuan Note&#x27;s kernel HTTP server unconditionally trusts all `chrome-extension://` origins, granting `RoleAdministrator` access to every installed browser extension without any authentication. Combined with the default empty `AccessAuthCode` on desktop installs, any Chrome/Chromium extension -- including a compromised legitimate extension via supply chain attack -- can make fully a…

---

## 20. 🟡 High Severity — Authorizer: Unvalidated redirect_uri in /authorize leaks OAuth2 tokens to attacker-controlled URL

**CVE:** `CVE-2026-54072` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-h29v-hj44-q8cv>

> ## Summary

The `/authorize` endpoint accepts any `redirect_uri` without validating it against `AllowedOrigins`. When `response_type=token` or `response_type=id_token`, the server appends `access_token`, `id_token`, and `refresh_token` as query parameters and issues a 302 redirect to the attacker-supplied URL. An unauthenticated attacker can obtain the required `client_id` from the public `/graphq…

---

## 21. 🟡 High Severity — SiYuan: Stored XSS to RCE via CSS-snippet <style> breakout in renderSnippet()

**CVE:** `CVE-2026-54067` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-mvjr-vv3c-w4qv>

> ### Summary

A CSS snippet body containing `&lt;/style&gt;` breaks out of its surrounding `&lt;style&gt;` tag when `renderSnippet()` interpolates it via `insertAdjacentHTML`. A payload like `&lt;/style&gt;&lt;img src=x onerror=&quot;...&quot;&gt;` runs arbitrary JavaScript in the renderer. On Electron desktop builds the renderer runs with `nodeIntegration:true`, so `require(&#x27;child_process&#x2…

---

## 22. 🟡 High Severity — MCP Atlassian: DNS-rebinding TOCTOU bypass of the SSRF fix (CVE-2026-27826)

**CVE:** `CVE-2026-27826` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-489g-7rxv-6c8q>

> ### Summary
GHSA-7r34-79r5-rcc9&#x27;s fix added `validate_url_for_ssrf`, which resolves the attacker-controlled `X-Atlassian-{Jira,Confluence}-Url` header host **once at middleware time** and trusts the result. But the outbound request is later built with the **raw hostname** and **re-resolves at connect time with no IP pinning**. An attacker-controlled rebinding DNS name returns a public IP on t…

---

## 23. 🟡 High Severity — Kimai has Server-Side Request Forgery in Invoice PDF Rendering via Markdown Image URLs

**CVE:** `CVE-2026-49865` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-pj8j-p4g4-4vw8>

> ### Summary

Kimai 2.56.0 contains a server-side request forgery vulnerability in its invoice PDF preview and generation workflow. If an attacker can control Markdown content that is later rendered into an invoice PDF, such as `Customer.invoiceText`, the server-side PDF renderer will fetch remote image URLs embedded in Markdown image syntax.

This allows the application server to issue outbound re…

---

## 24. 🟡 High Severity — API Platform Core vulnerable to cross-user attribute leak in JSON:API and HAL item normalizers due to missing isCacheKeySafe gate

**CVE:** `CVE-2026-49858` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-pjhx-3c3w-9v23>

> ### Impact

`#[ApiProperty(security: ...)]` is evaluated per request to decide whether a property is exposed. The `componentsCache` arrays in `ApiPlatform\JsonApi\Serializer\ItemNormalizer` and `ApiPlatform\Hal\Serializer\ItemNormalizer` are keyed on `$context[&#x27;cache_key&#x27;]`, which is set unconditionally before delegating to the parent normalizer. The component structure (attributes, rela…

---

## 25. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
