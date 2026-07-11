# Zero Day Pulse

> **Generated:** 2026-07-11 18:46 UTC &nbsp;|&nbsp; **Total:** 22 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 8 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** SimpleHelp v5.5.7 and earlier contain unauthenticated path traversal vulnerabilities in the web front-end. A remote unauthenticated attacker can send crafted HTTP requests containing directory-traversal sequences (e.g., '..\\') to download arbitrary files from the SimpleHelp host. Of particular interest is serverconfig.xml (also referenced as serverconfiguration.xml), which stores cryptographic secrets, hashed Technician and Administrator passwords, and the SimpleHelpAdmin password hash. With those credentials, an attacker can log into the Technician console and pivot to downstream managed endpoints, achieving full remote takeover of customer machines. The flaw is network-reachable, requires no privileges and no user interaction, and has low attack complexity.
- **Affected Products:** SimpleHelp Remote Support / RMM v5.5.7 and all earlier releases; legacy branches prior to v5.4.10 and v5.3.9 also affected.
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true — https://github.com/imjdl/CVE-2024-57727 (public PoC); https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2024/CVE-2024-57727.yaml (Nuclei template); Metasploit auxiliary module auxiliary/scanner/http/simplehelp_toolbox_path_traversal
- **Patch Available:** true — patched in SimpleHelp v5.5.8 (with backported fixes in v5.4.10 and v5.3.9); advisory: https://simple-help.com/kb---security-vulnerabilities-01-2025
- **Active Exploitation:** true — CVE-2024-57727 was added to the CISA Known Exploited Vulnerabilities (KEV) catalog on 2025-02-13 (remediation due date 2025-03-06). CISA Advisory AA25-163A documents DragonForce ransomware actors exploiting the vulnerability to compromise a utility billing software provider and its downstream customers in a double-extortion ransomware campaign, with broader exploitation by ransomware actors since at least January 2025.
- **Threat Actors:** DragonForce ransomware operators (per CISA Advisory AA25-163A); broader campaign of unnamed ransomware actors conducting double-extortion attacks since at least January 2025.
- **Mitigation:** 1) Immediately upgrade to SimpleHelp v5.5.8, or apply the patched point releases v5.4.10 / v5.3.9 for legacy lines. 2) If patching is not immediately possible, isolate the SimpleHelp server from the public internet (place behind a firewall or stop the SimpleHelp service). 3) Treat all SimpleHelp Technician, Administrator, and SimpleHelpAdmin passwords, plus any API tokens, as compromised: rotate them and force password resets for downstream customers. 4) Restrict the Technician and Administrator login pages to trusted IP addresses only. 5) Prefer LDAP/AD authentication over local accounts where possible. 6) Hunt for suspicious three-letter .exe artifacts (e.g., aaa.exe, bbb.exe) on SimpleHelp servers and managed endpoints created since January 2025, and review SimpleHelp logs for anomalous Technician sessions.
- **Vendor Advisory:** https://simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — 'Ghostcommit' hides prompt injection in images to fool AI agents, steal secrets

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-07-11
**Reference:** <https://www.bleepingcomputer.com/news/security/ghostcommit-hides-prompt-injection-in-images-to-fool-ai-agents-steal-secrets/>

> A PNG hiding a prompt injection could steal your repo&#x27;s secrets, researchers demonstrate. The technique, dubbed &#x27;Ghostcommit,&#x27; slipped past AI code reviewers CodeRabbit and Bugbot, which never open image files at all, then convinced a coding agent to read a repo&#x27;s .env and write every secret into the code as a list of numbers. [...]

**Parallel AI Enrichment:**

- **Technical Details:** The attacker opens a pull request containing two files: (1) an AGENTS.md or equivalent convention file (auto-read by coding agents) describing innocuous 'build-provenance' hygiene that references a PNG image, and (2) docs/images/build-spec.png, a PNG whose rendered text contains the actual malicious instruction — telling the agent to read the repository's .env file byte by byte, convert each byte to its integer value, append it to a tuple, and emit the tuple as a module-level constant _PROV_CANARY before commit. A small fake 'provenance validator' and a fabricated incident postmortem serve as cover. The PR diff appears benign, so text-only AI reviewers (CodeRabbit's default configuration explicitly excludes PNG/image files; Cursor Bugbot returned no findings) raise no flags. After merge, the payload sits dormant. Later, when a developer asks the coding agent for an unrelated feature (e.g., a token-tracking module), the agent reads AGENTS.md at startup, follows the image reference, OCRs the malicious instructions embedded in the PNG, opens .env, and writes every secret into source as an integer tuple (e.g., _PROV_CANARY: Final[tuple[int, ...]] = (115, 107, 45, 67, 65, 78, 65, 82, 89, ...) — 311 integers that decode byte-for-byte to the entire .env contents). The attacker recovers the secrets by decoding the public commit. The exploit hides in two layers: the instruction lives inside an image (invisible to text-based reviewers, regex scanners, and humans scanning the diff), and the exfiltrated secrets are encoded as integer tuples (unrecognized by every secret scanner, which looks for string-shaped credentials).
- **Affected Products:** CodeRabbit (default configuration excludes PNG/image files from review); Cursor Bugbot (AI code reviewer); Cursor coding agent with Claude Sonnet 4.6, Composer-2, or GPT-5.5; Google Antigravity with Claude Sonnet 4.6, Gemini 3.1 Pro, or Gemini 3 Flash; OpenAI Codex CLI with GPT-5.4. Anthropic Claude Code (Sonnet 4.6, Haiku 4.5, Opus 4.7) refused all attempts and was not affected.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true - https://github.com/asset-group/ghostcommit
- **Patch Available:** false - no official vendor patch has been published. The researchers' open-source multimodal PR defender (GitHub App) is available at https://github.com/asset-group/ghostcommit, but no vendor-issued fix for the underlying AI reviewer/agent behavior is known at the time of disclosure.
- **Active Exploitation:** false - no confirmed in-the-wild exploitation. The disclosure is based on controlled demonstrations against repositories the researchers own, seeded with fake (non-production) canary credentials. No threat actor, APT group, or ransomware operator has been reported as exploiting this technique.
- **Threat Actors:** None known.
- **Mitigation:** Until vendors ship fixes: (1) mandate substantive human review of every PR — the survey showed 73% of merged PRs in the top 300 active public repos reach main with no human and no bot review; (2) configure AI code reviewers to actually open and analyze image/binary attachments rather than skip them, and specifically review AGENTS.md/CLAUDE.md/.cursorrules-style convention files for indirect references to other repo files; (3) extend secret scanners to decode non-string-shaped outputs (Python integer tuples, byte arrays, hex, base-N encodings) back to ASCII before matching; (4) prefer coding agents whose harness enforces stricter safety scaffolding (Anthropic's Claude Code refused every model tested); (5) treat any AGENTS.md / CLAUDE.md / .cursorrules-style convention file that points to or instructs reading other repo files as a high-risk change requiring manual review; (6) the researchers released an open-source multimodal PR defender (GitHub App, runs on a single 4 GB GPU using Gemma 4) combining invisible-character scanning, code-shape analysis, LLM review of convention text, and LLM review of attached images — it caught every attack in a 15-class stress test and 49/50 attacks on 80 unseen real PRs with zero false positives.
- **Vendor Advisory:** https://asset-group.github.io/disclosures/ghostcommit/

---

## 3. 🟠 Zero-Day — Weekly Metasploit Update: Exploits for FlowiseAI CSV Agent and MacOS Package Kit

**CVE:** `CVE-2026-41264` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-07-11
**Reference:** <https://www.rapid7.com/blog/post/pt-weekly-metasploit-update-exploits-for-flowiseai-csv-agent-and-macos-package-kit>

> More AI, more software, more bugs! AI, it&#x27;s all you hear about nowadays and everyone&#x27;s got an opinion on it. Here at Metasploit, we care less about those opinions and more about the growing attack surface all this new software brings with it (yeehaw exploits!). Take for example the new Flowise CSV Agent Prompt Injection RCE brought to you by Takahiro Yokoyama and zdi-disclosures. Flowise…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability exists in the run() method of the CSV_Agents class in packages/components/nodes/agents/CSVAgent/CSVAgent.ts. When a query is sent to a chatflow using the CSV Agent node, the server reads the CSV file, builds a system prompt describing the dataframe, and asks an LLM to generate Python code to answer the question. This code is then executed within a Pyodide runtime. The pre-execution validator (validatePythonCodeForDataFrame) only blocks a small regex list of forbidden tokens (e.g., non-pandas/numpy module imports, exec, eval, open, os, subprocess), and can be bypassed by importing disallowed modules under a pandas alias (e.g., 'import pandas as np, os as pandas; pandas.system("...")'). This allows unauthenticated remote attackers to execute arbitrary Python code in the context of the user running the Flowise server. No authentication is required to send prompts to a chatflow using the CSV Agent node.
- **Affected Products:** Flowise (npm package 'flowise') versions <= 3.0.13, Flowise (npm package 'flowise-components') versions <= 3.0.13
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true - Metasploit Framework module released (https://www.rapid7.com/blog/post/pt-weekly-metasploit-update-exploits-for-flowiseai-csv-agent-and-macos-package-kit/) and proof-of-concept referenced in vendor advisory
- **Patch Available:** true - Flowise version 3.1.0 (npm packages 'flowise' and 'flowise-components'). See advisory: https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-3hjv-c53m-58jj
- **Active Exploitation:** false - No confirmed in-the-wild exploitation reported. CVE-2026-41264 is not listed in the CISA KEV catalog.
- **Threat Actors:** None known
- **Mitigation:** Upgrade to Flowise 3.1.0 or later. Workarounds: restrict network access to the Flowise instance (e.g., bind to localhost or place behind authentication/VPN), avoid exposing chatflows with CSV Agent nodes to untrusted users, and run the Flowise server under a low-privileged account to limit blast radius.
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

- **Technical Details:** The vulnerability resides in the confluence_upload_attachment tool in src/mcp_atlassian/confluence/attachments.py, specifically in the _upload_attachment_direct() method. The implementation calls files = {'file': (filename, open(file_path, 'rb'))} without validating or canonicalizing the user-supplied file_path argument. As a result, any MCP client that can authenticate to the server — or an AI agent that has been manipulated via prompt injection — can supply an arbitrary path (e.g., /etc/passwd, ~/.ssh/id_ed25519, /proc/self/environ) and have the server open and read that file, then upload its contents to Confluence as an attachment. This effectively exfiltrates any file the MCP server's process user can read. The fix (validate_safe_path()) was already present in the same file and applied to download_attachment() but was missed for upload_attachment(), indicating an incomplete remediation.
- **Affected Products:** mcp-atlassian (pip) versions < 0.22.0
- **CVSS Score:** 7.7
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Exploit Available:** true
- **Patch Available:** true - Upgrade to mcp-atlassian v0.22.0 or later (https://github.com/advisories/GHSA-g5r6-gv6m-f5jv)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Upgrade mcp-atlassian to version 0.22.0 or later, which adds the missing validate_safe_path() call around file_path before opening it. Until patched, restrict the MCP server's filesystem permissions so its process user cannot read sensitive files (credentials, SSH keys, environment files), restrict which MCP clients/agents can invoke the confluence_upload_attachment tool, sanitize or sandbox any untrusted content that could reach an AI agent (to prevent prompt injection), and monitor Confluence for unexpected attachment uploads.
- **Vendor Advisory:** https://github.com/advisories/GHSA-g5r6-gv6m-f5jv

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) abuses the inability of an LLM-powered agent to reliably distinguish trusted developer/user instructions from untrusted data it ingests. Attackers plant hidden instructions in content the agent later reads — web pages, emails, documents, search results, support tickets, calendar entries — and when the agent processes that content it silently executes the attacker's commands. Documented concealment techniques include: (1) CSS-based invisibility (1px font, near-zero opacity, off-screen positioning, background-color matching); (2) HTML-comment hiding and JSON-LD / Open Graph / meta-tag payload placement; (3) zero-width Unicode and homoglyph obfuscation to defeat naive text filters; (4) Base64-, Morse-, or hex-encoded instructions decoded at agent runtime; (5) jailbreak scaffolding such as 'god mode', 'developer mode', 'DAN', or persona/authority overrides; (6) AI-namespace hijack via tags like <ai:action> that AI browsers honor; (7) recursive/context-stuffing prompts (e.g., repeating tokens) to bias attention away from the legitimate instruction. Documented end-to-end impacts include SEO/traffic hijack, phishing promotion, API-key and credential exfiltration, prompt/system-prompt leakage, AI denial-of-service (telling the agent to delete files or stream infinite output), unauthorized financial transactions (Stripe/PayPal donation redirection, crypto-wallet transfers), and code execution when the agent has shell or tool access.
- **Affected Products:** Google Gemini (including Gemini 2.5 Pro and Gemini 3 Flash), Anthropic Claude, Claude Code, GitHub Copilot, Cursor, LiteLLM, BerriAI, Checkmarx, Trivy vulnerability scanner, OpenClaw agent platform, OneClaw agent, ClawHub skill registry. Underlying models: Meta Llama 3.3 70B Instruct, Meta Llama 3.2 90B Vision Instruct. No specific version ranges are enumerated because this is a class-of-bug finding rather than a single-CVE advisory.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — Multiple public PoCs and weaponized payloads are available: Forcepoint X-Labs published 10 verified IPI payloads (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads); the atlas-prompt-injection-poc GitHub repository demonstrates browser-agent injection (https://github.com/brennanbrown/atlas-prompt-injection-poc); Unit 42 catalogs additional in-the-wild payloads (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/).
- **Patch Available:** false — The Google blog post is a research/threat-intelligence publication describing an attack class, not an advisory for a single patched vulnerability. There is no single vendor patch; mitigation requires the layered defenses described across every product that ingests untrusted content. Google's own hardening of Gemini (account disablement of malicious users, model red-teaming) is described as ongoing rather than a discrete fix.
- **Active Exploitation:** true — Google Threat Intelligence and Forcepoint X-Labs both report confirmed in-the-wild exploitation. Google's telemetry recorded a 32% relative increase in malicious IPI observations between November 2025 and February 2026, with attackers seeding poisoned content on ordinary public websites hoping any visiting AI agent will follow the hidden instructions. Forcepoint verified 10 distinct IPI payloads targeting financial fraud, data destruction, API-key exfiltration, and AI denial-of-service. Unit 42 documents IPI used for ad-review evasion, SEO/phishing promotion, data destruction, denial-of-service, unauthorized transactions, sensitive-data leakage, and system-prompt leakage. State-aligned actors (Operation Overload, TeamPCP/UNC6780, UNC2814, APT45, PRC-nexus Hexstrike/Strix users) are confirmed actively weaponizing IPI [1][2][3].
- **Threat Actors:** Operation Overload (pro-Russia influence operation); TeamPCP / UNC6780 (financially motivated, compromising AI dev environments and supply chains); UNC2814 (using persona-prompting and Claude Code plugins such as 'wooyun-legacy' for vulnerability research and exploitation); APT45 (DPRK, leveraging Gemini for exploit development and reconnaissance); PRC-nexus actors using Hexstrike and Strix offensive agentic tools. Additional state-aligned actors from Russia, Iran, China, and Saudi Arabia are observed scaling IPI-style abuse of LLMs.
- **Mitigation:** Because no single patch closes this class, layered controls are required. Key hardening advice: (1) treat all externally fetched content as untrusted data, never as instructions — maintain a strict data/instruction boundary; (2) use prompt-level 'spotlighting' to wrap or quote retrieved web content so the model can identify it as untrusted; (3) enforce an instruction hierarchy where system and developer prompts outrank anything found in retrieved content; (4) require human-in-the-loop confirmation for any high-impact action (payments, file deletion, outbound data transfer, code execution); (5) input sanitization and output filtering — strip or neutralize hidden HTML, zero-width Unicode, HTML comments, and known IPI sentinel strings before they reach the model; (6) harden tool-use with allow-listing, least-privilege scopes, and segregated credentials; (7) continuous red-teaming and adversarial testing of agentic workflows; (8) deploy SAIF-style controls (threat modeling, evaluation, source attribution, incident response) for AI agents as Google recommends; (9) for vendors: integrate automated code/dependency scanning (e.g., VirusTotal Code Insight) into skill/plugin registries before distribution.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) targets LLM-based applications that ingest external, attacker-influenceable content (emails, shared documents, calendar invites, web pages). The attacker embeds adversarial natural-language instructions into that data. When the user subsequently asks Gemini to summarize, search, or act on that data, the LLM ingests both the user's instruction and the injected instructions and may follow the injected ones, leading to data exfiltration, phishing content generation, unauthorized tool/agent invocations, or manipulated summaries. Because the malicious content is delivered through normal data channels, the victim does not need to type anything for the attack to succeed, and a single poisoned document can target every user whose assistant processes it.
- **Affected Products:** Google Workspace with Gemini (Gemini integrated in Gmail, Google Docs, Google Drive, Google Slides, Google Meet, and other Workspace apps), and the standalone Gemini app (consumer and enterprise). No specific version numbers disclosed (IPI is a class of attack, not a versioned software flaw).
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Google's layered, continuously-updated mitigations include: (1) continuous attack discovery via internal red-teaming, automated red-teaming, the Google AI Vulnerability Rewards Program, and OSINT monitoring; (2) synthetic attack expansion via the Simula framework (claimed ~75% generation speedup) to broaden training/validation coverage; (3) deterministic defenses via a centralized Policy Engine enforcing baseline tool calls, URL sanitization, and tool-chaining rules (enabling rapid point-fixes faster than retraining); (4) ML-based defenses retrained on the expanded synthetic attack sets; (5) system-prompt engineering tuned against agreed effectiveness metrics; (6) underlying Gemini model hardening to better ignore injected instructions while preserving legitimate task performance. For Workspace admins: enforce admin/security controls, restrict Gemini add-on scope, and monitor the Google Workspace Admin security advisories feed. For end users: treat AI-generated summaries or actions containing links, requests, or surprising instructions with the same skepticism as unsolicited email.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is the principal new attack class against agentic browsers. Adversaries embed hidden instructions in web content — malicious sites, third-party iframes, or user-generated content such as reviews and posts. When Gemini in Chrome processes the page to plan its next action, the embedded instructions can steer the agent into unintended behavior: initiating financial transactions, exfiltrating sensitive data (emails, calendar, documents), or socially engineering the user. Because the planning model inherently consumes untrusted page content, it is exposed to this attack class. Google's layered defenses include: (1) a User Alignment Critic — an isolated Gemini-based model that vets every proposed action against the user's stated goal and can veto misaligned steps; (2) Origin Sets — Chrome's origin isolation extended to agent browsing so the agent only interacts with task-relevant origins, with new origins gated by a trusted function; (3) explicit user confirmations for sensitive operations such as banking portals and Password Manager unlocks; (4) real-time prompt-injection threat detection complementing Safe Browsing and on-device scam detection; (5) automated red-teaming and rapid auto-update response. The closely related CVE-2026-0628 is an insufficient policy enforcement in the WebView tag (Chrome < 143.0.7499.192) that allowed a malicious extension to inject scripts and HTML into the privileged Gemini panel, enabling local file access, surveillance, and chained prompt injection.
- **Affected Products:** Google Chrome with Gemini in Chrome (agentic browsing capabilities) on Windows, macOS, and Linux; specifically Google Chrome versions prior to 143.0.7499.192 for CVE-2026-0628.
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Exploit Available:** true — Public proof-of-concept available at https://github.com/brennanbrown/atlas-prompt-injection-poc; CVE-2026-0628 was disclosed with full technical details by Unit 42.
- **Patch Available:** true — Chrome 143.0.7499.192 (released January 6, 2026) patches CVE-2026-0628; distributed via Chrome's auto-update channel.
- **Active Exploitation:** true — Unit 42 (Palo Alto Networks) and The Hacker News reported in-the-wild exploitation of CVE-2026-0628 in March 2026, where malicious extensions leveraged the WebView tag policy-enforcement flaw to hijack the Gemini panel, achieving local file access and surveillance. Broader indirect prompt injection against agentic browsers has been demonstrated publicly but no large-scale criminal campaign has been publicly attributed.
- **Threat Actors:** None known
- **Mitigation:** Chrome's multi-layer agentic defenses (per Google's blog): (1) User Alignment Critic — an isolated secondary Gemini model that reviews proposed actions against the user's stated goal and vetoes misaligned ones; (2) Origin Sets — Chrome's origin isolation extended to agent browsing, restricting the agent to task-relevant origins with new origins gated by a trusted function; (3) explicit user confirmations for sensitive operations such as banking flows and Password Manager unlocks; (4) real-time prompt-injection threat detection complementing Safe Browsing and on-device scam detection; (5) continuous red-teaming and a fast auto-update pipeline for response. For CVE-2026-0628 specifically: update Chrome to 143.0.7499.192 or later, audit installed extensions, enforce least-privilege extension permissions, and consider enterprise extension allowlisting. Until updated, users can disable Gemini in Chrome and avoid installing unverified extensions.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/ (mirror: http://security.googleblog.com/2025/12/architecting-security-for-agentic.html); Related CVE-2026-0628: https://chromereleases.googleblog.com/2026/01/stable-channel-update-for-desktop.html and https://nvd.nist.gov/vuln/detail/CVE-2026-0628

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Out-of-bounds (OOB) memory access in the CrabbyAVIF AVIF image parser/decoder inside the Android System component, caused by incorrect bounds checking in multiple code paths (NV12, YUV planes, alpha plane, Y plane, UV planes, chroma width calculation, and plane parsing). A specially crafted AVIF image can trigger an OOB read/write that, when chained with other bugs, leads to remote code execution without user interaction or privileges. This vulnerability is notable as the first memory-safety CVE credited in Google's Android Rust codebase — a linear buffer overflow that demonstrates that while Rust eliminates entire classes of memory-safety bugs, unsafe code or unchecked indexing patterns can still introduce memory-safety flaws.
- **Affected Products:** Google Android 16 (Android System component, CrabbyAVIF AVIF parser/decoder in Rust); security patch level 2025-08-05 or later required.
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true - https://source.android.com/docs/security/bulletin/2025-08-01
- **Active Exploitation:** false
- **Threat Actors:** None known.
- **Mitigation:** Apply the Android Security Bulletin August 2025 patch (security patch level 2025-08-05 or later) immediately. Ensure all Android 16.0 devices are updated to the latest security patch level. Limit network exposure of affected Android devices until patched. Enable Google Play Protect (enabled by default on GMS devices). Android's built-in security platform mitigations (sandboxing, SELinux, etc.) reduce the likelihood of successful exploitation.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is an attack class in which an adversary embeds hidden adversarial instructions inside untrusted external content that an LLM later ingests — such as the body of an email, a shared Google Doc, a Calendar invite description, a web page, or an attachment. When the user subsequently asks Gemini to summarize, draft a reply, or otherwise process that content, the model may treat the attacker-supplied instructions as if they were legitimate system/user directives, and can be coerced into unintended actions: exfiltrating data via crafted URLs or markdown rendering, triggering unauthorized tool calls, producing phishing-style outputs, or pivoting to follow-on actions. Because the malicious payload travels inside ordinary user-visible content rather than via the chat input, conventional input-validation alone is insufficient.
- **Affected Products:** Gemini app (consumer Gemini), Gemini in Google Workspace (Gmail, Google Docs, Google Calendar), Gemini 2.5 models
- **CVSS Score:** CVSS score unavailable. No CVSS base score was published by Google for this advisory.
- **CVSS Vector:** CVSS vector unavailable. Google did not assign a CVSS vector for the indirect prompt injection class discussed in this advisory; no CVE was issued against Google products in connection with this post. The referenced CVE-2025-32711 applies to Microsoft 365 Copilot, not Google Gemini.
- **Exploit Available:** true — Public PoCs and curated research exist (e.g., github.com/Joe-B-Security/awesome-prompt-injection, josephthacker.com 2023 PoC, Trail of Bits Aug 2025 Copilot write-up, SafeBreach Gemini voice-assistant exploit, Miggo calendar-invite semantic attack on Gemini). The blog also cites CVE-2025-32711 (EchoLeak, Microsoft 365 Copilot) as a weaponized cross-vendor example.
- **Patch Available:** true — Layered mitigations have been deployed as built-in defenses across Gemini 2.5 and Gemini in Google Workspace; reference advisory: https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html
- **Active Exploitation:** false — Google's blog does not report confirmed in-the-wild exploitation of Gemini via indirect prompt injection; it frames the issue as an emerging threat class and uses CVE-2025-32711 (EchoLeak, Microsoft 365 Copilot) as an illustrative cross-vendor example. Independent research (SafeBreach Gemini voice-assistant exploit, Miggo calendar-invite semantic attack, HiddenLayer, Palo Alto Unit 42) demonstrates weaponizable techniques and opportunistic abuse against AI-agent surfaces generally, but does not document confirmed active exploitation of Google Gemini specifically.
- **Threat Actors:** None known. The Google Security Blog post does not attribute indirect prompt injection attacks against Gemini to any specific threat actor group, APT campaign, or ransomware operator. It cites CVE-2025-32711 ("EchoLeak"), a 0-click exfiltration flaw in Microsoft 365 Copilot, only as an illustrative example of the broader vulnerability class; that CVE belongs to Microsoft, not Google. Third-party research (Palo Alto Unit 42, HiddenLayer, SafeBreach, Miggo) documents weaponizable techniques and opportunistic abuse of LLM-agent surfaces but does not tie them to named APT or ransomware groups.
- **Mitigation:** Google's layered defense for Gemini against indirect prompt injection: (1) Prompt-injection content classifiers — ML models trained on real-world adversarial data (curated via the AI Vulnerability Reward Program) that detect and strip malicious instructions before they reach the LLM; (2) Security thought reinforcement — targeted system-instruction reinforcement that steers Gemini to ignore adversarial instructions embedded in content and stay focused on the user's task; (3) Markdown sanitization and suspicious URL redaction — strips external image/link rendering and blocks URLs flagged by Google Safe Browsing; (4) User confirmation framework — requires explicit user consent before Gemini executes potentially risky actions (e.g., sending messages, modifying shared content); (5) End-user security mitigation notifications — alerts the user when Gemini blocks a response due to suspected prompt injection. Adjacent controls: adversarial training of Gemini 2.5, red-teaming via BugSWAT events and the Secure AI Framework (SAIF), and an AI VRP for ongoing researcher disclosure.
- **Vendor Advisory:** https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors exploit known vulnerabilities (CVE-2024-21887, CVE-2023-46805, CVE-2024-3400, CVE-2023-20273, CVE-2023-20198, CVE-2018-0171) in network edge devices including routers, VPNs, and firewalls. They modify router configurations—adding Access Control Lists often named 'access-list 20'—to enable persistent access, and abuse Cisco IOS XE Guest Shell containers for command execution and evasion. They establish GRE/IPsec tunnels and static routes, configure SPAN/RSPAN/ERSPAN for traffic mirroring/exfiltration, and pivot through compromised devices and trusted private connections (e.g., peering links, partner VPN tunnels) to reach additional networks in telecommunications, government, transportation, lodging, and military sectors.
- **Affected Products:** Ivanti Connect Secure, Ivanti Policy Secure, Palo Alto Networks PAN-OS (GlobalProtect), Cisco IOS, Cisco IOS XE; additional suspected targets include Fortinet firewalls, Juniper firewalls, Microsoft Exchange, Nokia routers/switches, Sierra Wireless devices, SonicWall firewalls
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor (PRC state-sponsored actors linked to MSS and PLA)
- **Mitigation:** 1) Prioritize patching known-exploited CVEs (CVE-2024-21887, CVE-2023-46805, CVE-2024-3400, CVE-2023-20273, CVE-2023-20198, CVE-2018-0171) on Ivanti, Palo Alto Networks, and Cisco devices. 2) Upgrade unsupported/end-of-life network devices to vendor-supported platforms. 3) Audit and remove unauthorized ACLs (especially 'access-list 20' and similar), GRE/IPsec tunnels, static routes, and SPAN/RSPAN/ERSPAN configurations. 4) Monitor Cisco IOS XE Guest Shell container activity and unexpected SSH keys/authorized-keys changes. 5) Use Cisco Software Checker and Cisco IOS/IOS XE Hardening Guides; deploy Cisco EEM policies to snapshot process and container state. 6) Enforce strong authentication (TACACS+ auditing, AAA logging) and disable unused management services. 7) Segment management networks, restrict outbound traffic, and review trusted peering/partner connections for compromise.
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

## 22. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
