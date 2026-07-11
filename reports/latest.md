# Zero Day Pulse

> **Generated:** 2026-07-11 01:26 UTC &nbsp;|&nbsp; **Total:** 25 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 11 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is an unauthenticated path traversal vulnerability in the SimpleHelp server's /toolbox-resource endpoint. Crafted HTTP requests containing directory-traversal sequences (e.g., '../') allow remote, unauthenticated attackers to download arbitrary files from the SimpleHelp host. Sensitive files include serverconfig.xml, which stores hashed SimpleHelpAdmin and local technician account passwords, LDAP credentials, OIDC client secrets, API keys, and TOTP seeds used for MFA. Successful exploitation enables credential theft and downstream full takeover of the SimpleHelp server and managed endpoints without requiring prior authentication.
- **Affected Products:** SimpleHelp Remote Support / RMM software versions 5.5.7 and earlier (all releases prior to and including 5.5.7)
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true — Public exploit code is available, including a Metasploit module (https://www.rapid7.com/db/modules/auxiliary/scanner/http/simplehelp_toolbox_path_traversal/) and a GitHub PoC (https://github.com/imjdl/CVE-2024-57727).
- **Patch Available:** true — Patched versions released 2025-01-08: SimpleHelp 5.5.8 (and later) for 5.5.x, 5.4.10 for 5.4.x, and 5.3.9 for 5.3.x. Advisory: https://guides.simple-help.com/kb---security-vulnerabilities-01-2025
- **Active Exploitation:** true — CISA added CVE-2024-57727 to the KEV Catalog on 2025-02-13. CISA Advisory AA25-163A (2025-06-12) documents DragonForce ransomware actors actively exploiting unpatched SimpleHelp instances since January 2025 against a utility billing software provider and its customers. Multiple vendors (Sophos, Arctic Wolf, Picus, Halcyon, Huntress) have independently observed in-the-wild exploitation.
- **Threat Actors:** DragonForce ransomware actors (per CISA Advisory AA25-163A); Sophos has also attributed exploitation to 'multiple threat actors' including potential Medusa ransomware affiliates. Arctic Wolf independently observed exploitation campaigns.
- **Mitigation:** 1) Upgrade the SimpleHelp server (and any deployed Remote Access Services) to version 5.5.8 or later; users on 5.4.x must apply the 5.4.10 patch; users on 5.3.x must apply the 5.3.9 patch. 2) If compromise is suspected or cannot be ruled out, isolate the SimpleHelp server from the network, stop the SimpleHelp service, and reinstall the OS and SimpleHelp from clean media, restoring data only from clean, offline backups. 3) Immediately rotate all credentials that were stored on the SimpleHelp host: SimpleHelpAdmin and all local technician account passwords, LDAP bind credentials, OIDC client secrets, API keys, and TOTP MFA seeds. 4) Force password resets for any downstream customers/endpoints whose credentials were stored on the server. 5) Review logs for unauthorized access (especially to /toolbox-resource), unknown outbound connections, unfamiliar executables (e.g., aaa.exe / bbb.exe-style filenames), and evidence of double-extortion ransomware activity. 6) Restrict the SimpleHelp server's network exposure—do not expose it directly to the internet; require a VPN and IP allow-listing for both technician/admin logins and the management API.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — Weekly Metasploit Update: Exploits for FlowiseAI CSV Agent and MacOS Package Kit

**CVE:** `CVE-2026-41264` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-07-11
**Reference:** <https://www.rapid7.com/blog/post/pt-weekly-metasploit-update-exploits-for-flowiseai-csv-agent-and-macos-package-kit>

> More AI, more software, more bugs! AI, it&#x27;s all you hear about nowadays and everyone&#x27;s got an opinion on it. Here at Metasploit, we care less about those opinions and more about the growing attack surface all this new software brings with it (yeehaw exploits!). Take for example the new Flowise CSV Agent Prompt Injection RCE brought to you by Takahiro Yokoyama and zdi-disclosures. Flowise…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is in the `run` method of the `CSV_Agents` class (packages/components/nodes/agents/CSVAgent/core.ts). Flowise executes an LLM-generated Python script inside a pyodide runtime to answer CSV queries, but the runtime lacks proper sandboxing. A pre-validation step (`validatePythonCodeForDataFrame`) attempts to block dangerous calls by regex-matching a blacklist of forbidden patterns (e.g., `import os`, `subprocess`, `eval`, `open`). This blacklist is incomplete and can be trivially bypassed via aliasing tricks such as `import pandas as np, os as pandas` followed by `pandas.system("...")`. After validation passes, pyodide evaluates the script on the host, yielding arbitrary OS command execution. An unauthenticated remote attacker can trigger this either by sending crafted prompts to a chatflow using the CSV Agent node, or by uploading a CSV file containing malicious text that the agent reads back and processes.
- **Affected Products:** FlowiseAI Flowise (npm packages `flowise` and `flowise-components`) versions <= 3.0.13, specifically deployments using the CSV Agent chatflow node
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true — Public PoC (poc.py) in the GitHub advisory (https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-3hjv-c53m-58jj) and Metasploit module by Takahiro Yokoyama in the Jul 11, 2026 Metasploit weekly update (https://www.rapid7.com/blog/post/pt-weekly-metasploit-update-exploits-for-flowiseai-csv-agent-and-macos-package-kit)
- **Patch Available:** true — Flowise v3.1.0 (advisory: https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-3hjv-c53m-58jj)
- **Active Exploitation:** false — No confirmed in-the-wild exploitation has been publicly reported as of the Metasploit module release (Jul 11, 2026). However, the public availability of a Metasploit exploit module and a vendor-issued PoC significantly lowers the barrier to opportunistic exploitation of internet-exposed unpatched instances.
- **Threat Actors:** None known
- **Mitigation:** Upgrade Flowise to version 3.1.0 or later (the fix moves Python execution into a properly sandboxed subprocess and tightens the disallowed-pattern checks). If patching is not immediately possible: (1) restrict network access to the Flowise HTTP/API endpoints (default port 3000); (2) remove or replace any chatflows that use the CSV Agent node; (3) place Flowise behind authentication; (4) run the Flowise process with least-privilege OS user permissions to limit the blast radius of a successful RCE.
- **Vendor Advisory:** https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-3hjv-c53m-58jj

---

## 3. 🟠 Zero-Day — mcp-atlassian: Arbitrary file read via missing path validation in confluence_upload_attachment

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-g5r6-gv6m-f5jv>

> ### Summary
`confluence_upload_attachment` passes `file_path` directly to `open(file_path, &quot;rb&quot;)` with no path validation. Any authenticated MCP client — or an AI agent manipulated via prompt injection — can read any file the server process can access and exfiltrate it to Confluence as an attachment.

### Details
Root cause: `src/mcp_atlassian/confluence/attachments.py`, `_upload_attachm…

**Parallel AI Enrichment:**

- **Technical Details:** In `src/mcp_atlassian/confluence/attachments.py`, the helper `_upload_attachment_direct()` opens `file_path` via `open(file_path, "rb")` and uploads its contents to Confluence without first calling the existing `validate_safe_path()` sanitization. Because `file_path` comes directly from the MCP `confluence_upload_attachment` tool argument, any MCP client — or an LLM agent influenced via prompt injection — can supply an arbitrary filesystem path (e.g., `/proc/self/environ`, `~/.ssh/id_ed25519`, `C:\Windows\System32\drivers\etc\hosts`) and have the server exfiltrate its contents as a Confluence attachment. The sibling `download_attachment()` routine in the same file already calls `validate_safe_path()`, confirming the upload path was simply missed. This is classified as CWE-22 (Path Traversal).
- **Affected Products:** mcp-atlassian (PyPI package), versions < 0.22.0 — the `confluence_upload_attachment` MCP tool in the sooperset/mcp-atlassian server.
- **CVSS Score:** 7.7
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known.
- **Mitigation:** Upgrade mcp-atlassian to version 0.22.0 or later. Until upgraded, restrict the MCP server's filesystem access and network exposure, run it under a least-privileged user account, disable or gate the `confluence_upload_attachment` tool, block untrusted content from being processed by LLM agents that can call MCP tools, and rotate any secrets that may have been exposed via process environment variables or filesystem access.
- **Vendor Advisory:** https://github.com/advisories/GHSA-g5r6-gv6m-f5jv

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an attack class in which adversaries embed hidden instructions inside external content (web pages, emails, documents, images, search results) that an LLM or AI agent later retrieves and processes within its context window. The model treats the injected content as legitimate instructions and follows the attacker's directives instead of the user's, enabling goal hijacking, exfiltration of user data or API keys, unauthorized tool/agent actions (e.g., file deletion, shell command execution such as 'sudo rm -rf'), SEO/referral manipulation of AI summaries, denial-of-service via infinite text streams, and forced output or attribution hijacking. Attack vectors include hidden HTML/DOM text and comments, accessibility attributes (e.g., aria-hidden, visually-hidden CSS), markdown metadata, prompt-imitating system tags, and magic-string canaries that target specific agent frameworks.
- **Affected Products:** Google Gemini (consumer and enterprise Gemini app); Gemini in Google Workspace apps (Gmail, Docs, Drive, Calendar, Chat integrations); and broadly any LLM-powered agent that ingests untrusted external content (web pages, emails, documents, search results). No specific affected versions are enumerated because indirect prompt injection is a threat class against the AI product category rather than a versioned software vulnerability; no CVE is assigned.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true. Public PoC payloads and curated payload lists: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Prompt%20Injection/README.md and https://github.com/topics/prompt-injection. Forcepoint X-Labs catalogued 10 live indirect prompt injection payloads observed on real websites: https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads.
- **Patch Available:** true. No single downloadable patch exists because indirect prompt injection is a threat class rather than a versioned software flaw. Google continuously ships mitigations across Gemini and Workspace (prompt-injection classifiers, security thought reinforcement, markdown/URL sanitization, user confirmation flows, model hardening). Advisory URL: http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html. Layered-defense write-up: https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini. Google's AI Vulnerability Rewards Program additionally incentivizes external reporting of IPI issues.
- **Active Exploitation:** true. Google Threat Intelligence observed prompt injections on the public web via Common Crawl data, with a 32% increase in the 'malicious' category between November 2025 and February 2026. Forcepoint X-Labs independently confirmed active exploitation by cataloguing 10 indirect prompt injection payloads found live on real-world websites (financial-fraud donation scams, AI-agent RCE via injected shell commands, API-key theft, attribution hijack, DoS, and SEO/referral manipulation). Sources: http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html and https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads.
- **Threat Actors:** None known. The Google Security Blog post does not attribute exploitation to any specific named threat actor, APT group, or ransomware operator. It refers generically to 'threat actors' and 'adversaries'. A Forcepoint X-Labs follow-up noted shared injection templates across domains (suggesting organized tooling) and one payload that attributed itself to 'Kirill Bobrov', but no formal threat-actor attribution has been published.
- **Mitigation:** Apply a layered defense strategy: (1) deploy prompt-injection classifiers on inbound external content; (2) reinforce the model with explicit security/system instructions prioritizing user intent over embedded instructions; (3) sanitize markdown and strip/redact suspicious URLs via Google Safe Browsing before content reaches the model; (4) require human-in-the-loop confirmation for sensitive agent actions (e.g., deleting calendar events, running shell commands, sending messages); (5) harden models against adversarial manipulation through adversarial training and red-teaming; (6) notify end users when risky inputs are detected and mitigated; and (7) apply least-privilege scoping to agent tools. Google's layered defense for Gemini in Workspace is documented at https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) exploits Gemini's ingestion of untrusted content (emails, documents, Slides speaker notes, Drive files, Calendar events, web pages, OS/messaging notifications) alongside user prompts. An attacker embeds adversarial natural-language instructions inside that untrusted content — for example, white-on-white HTML in an email body, text in Slides speaker notes, a Calendar event description, or a push notification from a messaging app. When Gemini processes the document to summarize, answer, or act, it treats the hidden instructions as authoritative and follows them, overriding the user's intent. Demonstrated impacts include: (a) injecting phishing/security-warning content into Gemini summaries to harvest credentials (HiddenLayer, 0DIN); (b) coercing Gemini into calling external tools that exfiltrate or manipulate user data — e.g., the Miggo Calendar-invite attack that bypassed authorization to create calendar entries, and the SafeBreach 'Fake Context Alignment' attack where a single user 'Yes' triggered smart-home and app-URI actions; (c) corrupting RAG memory and long-term context. The attack requires no special user input — even routine summarization triggers it.
- **Affected Products:** Google Workspace with Gemini (cloud service — no fixed version), including the Gemini app and Gemini integrations in Gmail, Google Docs editors, Drive, Chat, and Calendar. Indirect prompt injection is a class-of-vulnerability affecting LLM-augmented applications rather than a single software version.
- **CVSS Score:** CVSS score unavailable. No CVSS v3.x base score has been published for indirect prompt injection in Google Workspace with Gemini. Google treats this as a class-of-vulnerability with continuous mitigation rather than a single scored CVE.
- **CVSS Vector:** CVSS vector unavailable. No CVE has been assigned to indirect prompt injection in Google Workspace with Gemini. The issue is treated as a class-of-vulnerability affecting LLM-augmented applications rather than a single scored CVE.
- **Exploit Available:** true — Multiple public PoCs and weaponized demos exist: (1) HiddenLayer 'New Gemini for Workspace Vulnerability' (25 Sep 2024) — indirect prompt injection via emails, Slides speaker notes, Drive docs; (2) 0DIN/Marco Figueroa 'Phishing for Gemini' (10 Jul 2025) — hidden white-text email instructions hijack Gemini summaries to inject phishing banners; (3) SafeBreach/Or Yair 'Gemini Voice Assistant' exploit (17 Aug 2025) — instant-messaging notifications used to poison context; (4) Miggo/Liad Eliyahu 'Weaponizing Calendar Invites' (19 Jan 2026) — calendar-event descriptions bypass authorization; (5) PayloadsAllTheThings prompt-injection repository. Sources: https://www.hiddenlayer.com/research/new-gemini-for-workspace-vulnerability-enabling-phishing-content-manipulation, https://0din.ai/blog/phishing-for-gemini, https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/, https://www.miggo.io/post/weaponizing-calendar-invites-a-semantic-attack-on-google-gemini, https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Prompt%20Injection/README.md
- **Patch Available:** true — Google has continuously deployed mitigations for indirect prompt injection in Workspace with Gemini through server-side model updates, classifier improvements, and system-prompt changes (documented in the 02 Apr 2026 blog post and the layered-defense admin article). Because indirect prompt injection is a class-of-vulnerability, mitigation is ongoing rather than a one-time per-version patch; customers do not need to apply a per-version patch. Adjacent fixes have shipped for related Gemini products (e.g., the CVSS 10.0 Gemini CLI / GitHub-Action command-injection flaw patched by Google in May 2026). Source: https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/
- **Active Exploitation:** true — Google's own blog post 'AI threats in the wild: The current state of prompt injections on the web' (23 Apr 2026) confirms that unnamed threat actors are actively seeding indirect prompt injections on public websites to manipulate AI browsing agents (data exfiltration, SEO manipulation, resource-exhaustion). Palo Alto Unit 42 has documented real-world web-based indirect-prompt-injection campaigns (e.g., the reviewerpress[.]com SEO-poisoning campaign). Multiple independent researchers have published working weaponized exploits targeting Gemini for Workspace (HiddenLayer, 0DIN, SafeBreach, Miggo). Sources: https://blog.google/security/prompt-injections-web/, https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/
- **Threat Actors:** None known. No specific APT group, ransomware operator, or named threat-actor campaign has been publicly attributed for exploiting indirect prompt injection against Google Workspace with Gemini. However, Google documented (23 Apr 2026 blog 'AI threats in the wild') that unnamed threat actors are actively seeding indirect prompt injections on public websites to manipulate AI browsing agents (data exfiltration, SEO manipulation, resource-exhaustion). Multiple independent security researchers have published weaponized PoCs/exploits targeting Gemini for Workspace.
- **Mitigation:** Google applies a layered defense: (1) prompt-injection content classifiers at the model perimeter; (2) security-thought reinforcement in system prompts; (3) markdown sanitization and suspicious-URL redaction in model outputs; (4) a user-confirmation framework requiring explicit human approval for sensitive actions (sending email, creating events, OAuth grants); (5) end-user security-mitigation notifications when an attempted injection is blocked; (6) continuous model hardening via adversarial fine-tuning and red-team findings from the AI Vulnerability Reward Program. Admin/user hardening: enable Workspace audit logging for Gemini activity, restrict Gemini access to untrusted/spam mail, disable Gemini summarization of external-sender mail where possible, and instruct end users never to follow instructions found inside an AI-generated summary that originated from a third-party document. Google deploys mitigations server-side; no customer-side patch is required for the Workspace cloud service itself.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/ (canonical: http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html)

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is a class of attack where untrusted web content (malicious sites, third-party iframes, user-generated content) contains instructions that cause an AI agent to take unwanted actions on behalf of the user (financial transactions, data exfiltration, goal-hijacking). Because agentic browsers rely on the same Gemini model that processes untrusted web content to plan subsequent actions, the planner is inherently vulnerable to instruction-following influenced by attacker-controlled page content. Google's layered defense includes: (1) a User Alignment Critic — a second isolated Gemini model that double-checks every proposed action against the user's stated goal using only metadata (not raw page content), so it cannot be directly poisoned; (2) Agent Origin Sets that architecturally restrict the agent to read from a task-relevant set of origins and write only to a separate task-relevant set of origins, preventing cross-site data exfiltration and Site Isolation bypasses; (3) deterministic and model-based user confirmation prompts for sensitive sites (banking, healthcare) and consequential actions (payments, messages, Password Manager sign-in); (4) a real-time prompt-injection classifier that scans every page the agent sees and runs in parallel with the planner; and (5) 'spotlighting' techniques that train/condition the model to prefer user and system instructions over page content, plus automated red-teaming using synthetic malicious sites and LLM-driven attacks.
- **Affected Products:** Google Chrome with Gemini in Chrome agentic capabilities; specific affected versions unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Chrome's layered defenses are delivered automatically through Chrome's auto-update mechanism. Users should keep Chrome up to date. Defenses include: the User Alignment Critic (a separate, isolated Gemini model that vetoes misaligned actions), Agent Origin Sets that limit the agent's read/write origins to those relevant to the task, deterministic user confirmation prompts for sensitive sites (banking, healthcare) and consequential actions (payments, message sending, Password Manager sign-in), a real-time prompt-injection classifier that flags pages containing indirect prompt injection, and 'spotlighting' to bias the model toward user/system instructions over page-embedded instructions. Users and enterprises can additionally disable Gemini in Chrome and the agentic browsing features until they have evaluated the residual risk.
- **Vendor Advisory:** http://security.googleblog.com/2026/12/architecting-security-for-agentic.html

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2025-48530 is a linear (heap) buffer overflow in CrabbyAVIF, the Rust-based AVIF image decoder in Android. It is caused by incorrect bounds checks leading to out-of-bounds memory reads/writes when parsing a maliciously crafted AVIF image. The bug originates in an `unsafe` Rust code block where the compiler's memory-safety guarantees do not apply. It is the first known memory-safety vulnerability in Rust code shipped in the Android platform. The flaw could potentially lead to remote code execution when chained with other bugs, with no user interaction or extra execution privileges required. Android's Scudo hardened user-mode allocator detected the corruption and rendered the out-of-bounds write non-exploitable as a code-execution primitive.
- **Affected Products:** Android 16 (System component). The vulnerable code is in CrabbyAVIF, Google's Rust-based AVIF image parser/decoder within external/rust/crabbyavif in AOSP.
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true — Patched in the Android Security Bulletin August 2025 (2025-08-01 / 2025-08-05 patch levels). Reference patches in AOSP: https://android.googlesource.com/platform/external/rust/crabbyavif/+/9bcc1a311114ab844b417d3cdec50dcedfd0603f and https://android.googlesource.com/platform/external/rust/crabbyavif/+/42feb427a42afd9eebe6391a0d8a7b083fe82140 (bug A-419563680).
- **Active Exploitation:** false. Google has confirmed there is no evidence of active exploitation. The vulnerability was identified and patched internally before ever shipping to users, and Google stated that none of the vulnerabilities in the August 2025 update were under active exploitation.
- **Threat Actors:** None known. Google disclosed CVE-2025-48530 as a "near-miss" — the flaw was identified and patched internally before any public release shipped, and there is no evidence of exploitation by any threat actor, APT group, or ransomware operator.
- **Mitigation:** Apply the Android security update corresponding to the 2025-08-05 patch level (Android Security Bulletin August 2025) to all Android 16 devices as soon as possible. Until patches can be deployed, limit exposure of affected Android endpoints to untrusted image content and rely on Android's built-in Scudo hardened allocator (enabled by default on Android), which mitigates exploitation. Long-term, Google is strengthening developer training by adding a deep-dive module on unsafe Rust to its Comprehensive Rust curriculum to reduce similar mistakes in unsafe code blocks.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack class targeting LLM-based systems. Unlike direct prompt injection (where malicious instructions are typed directly into a prompt), IPI hides malicious instructions inside external content the LLM ingests—emails, documents, calendar invites, web pages, or images. When Gemini summarizes, retrieves over, or acts on this content, the hidden instructions are processed as if they came from the user, potentially causing data exfiltration, phishing content generation, or unauthorized actions. The blog references CVE-2025-32711 ('EchoLeak'), a zero-click image-rendering exfiltration vulnerability in Microsoft 365 Copilot, as an example of the attack class and notes that Gemini's markdown sanitizer blocks external image URLs, so the same technique does not apply to Gemini. No specific CVE has been assigned to Gemini for this attack class.
- **Affected Products:** Gemini 2.5 models, Gemini app, Gemini in Google Workspace (Gmail, Docs, and other Workspace apps). Specific build/version numbers are not published.
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true - Public PoCs and weaponized demonstrations exist for indirect prompt injection against Gemini and similar LLMs (e.g., SafeBreach Labs research on Gemini voice assistant prompt injection, Miggo research on calendar invite semantic attacks against Gemini in Workspace). Source: https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/ ; https://www.miggo.io/post/weaponizing-calendar-invites-a-semantic-attack-on-google-gemini
- **Patch Available:** true - Defenses are deployed server-side/continuously (model retraining, classifier rollout, sanitization rules). Reference: http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html
- **Active Exploitation:** true - Indirect prompt injection against LLM assistants including Gemini is actively exploited in the wild as a class. Confirmed by Google's April 2026 follow-up report documenting threat actors seeding prompt injections on public websites. Specific named APT/ransomware groups exploiting Gemini have not been publicly disclosed. Sources: https://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html ; https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/ ; https://www.miggo.io/post/weaponizing-calendar-invites-a-semantic-attack-on-google-gemini
- **Threat Actors:** None known
- **Mitigation:** Google's documented layered defenses for Gemini (continuously deployed, no user patch required): (1) Adversarial training of Gemini 2.5 models with indirect prompt injection examples from Google's AI Vulnerability Reward Program; (2) ML-based prompt injection/content classifiers that detect and ignore malicious instructions in emails and files before they reach the model; (3) Markdown/output sanitization that blocks external image URLs and unsafe rendering tokens, neutralizing EchoLeak-style exfiltration; (4) Suspicious URL detection via Google Safe Browsing to redact risky links in Gemini's responses; (5) Human-in-the-loop (HITL) confirmation prompts before Gemini takes sensitive or irreversible actions (e.g., sending mail, modifying docs); (6) End-user security notifications when Gemini detects malicious instructions in underlying content. Additional customer guidance: enable Workspace Gemini admin controls, restrict Gemini extensions/connectors to trusted data sources, and apply least-privilege access to data Gemini can reach.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored APT actors exploit publicly known CVEs in edge networking equipment (routers, VPNs, firewalls) to gain initial access. After compromise, they modify device configurations to maintain persistent, long-term access: creating or altering access-control lists (often naming them 'access-list 20'), enabling GRE/IPsec tunnels for covert connectivity, configuring traffic mirroring (SPAN/RSPAN/ERSPAN) to snoop traffic, abusing Linux container subsystems on network devices (Cisco GuestShell/IOx on IOS XE and NX-OS) for persistence and evasion of host-based detection, and pivoting via trusted provider-to-provider or provider-to-customer links. They retain router credentials for re-entry and harvest authentication material from administrative devices and mail servers to monitor defender activity.
- **Affected Products:** Ivanti Connect Secure and Ivanti Policy Secure (web-component); Palo Alto Networks PAN-OS (GlobalProtect feature); Cisco IOS, IOS XE, and NX-OS (routers/switches, including backbone and provider-edge/customer-edge routers). Suspected additional targets include Fortinet firewalls, Juniper firewalls, Microsoft Exchange, Nokia routers/switches, Sierra Wireless devices, and SonicWall firewalls. Specific vulnerable versions correspond to: CVE-2024-21887 (Ivanti), CVE-2023-46805 (Ivanti), CVE-2024-3400 (Palo Alto), CVE-2023-20273 (Cisco IOS XE), CVE-2023-20198 (Cisco IOS XE), CVE-2018-0171 (Cisco IOS/IOS XE Smart Install).
- **CVSS Score:** CVSS score unavailable - the advisory aggregates multiple CVEs, each with its own CVSS v3.1 base score (no single score applies to the advisory as a whole). Individual CVE scores include: CVE-2024-21887 (9.1), CVE-2024-3400 (10.0), CVE-2023-20198 (10.0), CVE-2023-46805 (8.2), CVE-2018-0171 (9.8), CVE-2023-20273 (7.2).
- **CVSS Vector:** CVSS vector unavailable - the advisory aggregates multiple CVEs, each with its own CVSS v3.1 vector (no single vector applies to the advisory as a whole).
- **Exploit Available:** true - Public PoCs and weaponized exploits are available for CVE-2024-21887 (https://github.com/Chocapikk/CVE-2024-21887), CVE-2018-0171 (https://www.exploit-db.com/exploits/44451), CVE-2024-3400 (Palo Alto GlobalProtect command injection), CVE-2023-46805 (Ivanti auth bypass), and CVE-2023-20198 (Cisco IOS XE Web UI auth bypass).
- **Patch Available:** true - Vendor patches exist for every CVE referenced in the advisory (Ivanti patches for CVE-2024-21887 and CVE-2023-46805; Palo Alto Networks patches for CVE-2024-3400; Cisco patches for CVE-2023-20273, CVE-2023-20198, and CVE-2018-0171). Primary advisory/patch index: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a
- **Active Exploitation:** true - CISA, NSA, FBI, and international partners (ACSC, CCCS, NCSC-NZ, NCSC-UK, NUKIB, SUPO, BND, BfV, BSI, AISE/AISI, NCO) confirm active, ongoing exploitation of the targeted edge devices by these PRC state-sponsored actors in the United States, Australia, Canada, New Zealand, the United Kingdom, and globally, primarily targeting telecommunications, government, transportation, lodging, and military infrastructure networks. [1]
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor, plus three PRC-contracted companies identified by the U.S. government: Sichuan Juxinhe Network Technology Co. Ltd., Beijing Huanyu Tianqiong Information Technology Co. Ltd., and Sichuan Zhixin Ruijie Network Technology Co. Ltd. (collectively referred to in the advisory as PRC state-sponsored APT actors).
- **Mitigation:** Prioritize patching edge devices against the six CVEs explicitly listed in the advisory (CVE-2024-21887, CVE-2023-46805, CVE-2024-3400, CVE-2023-20273, CVE-2023-20198, CVE-2018-0171); enforce phishing-resistant MFA (FIDO2/WebAuthn or PKI smart cards) on all administrative accounts; disable or restrict Cisco GuestShell (`guestshell disable`) and IOx (`no iox`); audit device configurations against known-good baselines, looking for unauthorized ACL changes, unexpected GRE/IPsec tunnels, and SPAN/RSPAN/ERSPAN sessions; require SNMPv3 with authentication and privacy on all network gear; use TACACS+/RADIUS for AAA with command authorization; restrict management-plane access with infrastructure ACLs; forward all network device logs (including container/GuestShell logs) to a central SIEM; and replace any unsupported/end-of-life network devices with vendor-supported hardware running current software.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2023-23397 is a critical Microsoft Outlook Elevation of Privilege vulnerability (CWE-20: Improper Input Validation) in the handling of the PidLidReminderFileParameter MAPI property. An attacker crafts an Outlook message/calendar item with an extended MAPI property referencing a remote UNC path (e.g., \\\\attacker-controlled\\foo.bar). When Outlook processes the reminder, it silently initiates an outbound SMB connection to the attacker's server, leaking the victim's Net-NTLMv2 hash without any user interaction (zero-click). The harvested hash can be relayed (NTLM relay) to authenticate as the victim against other services. GRU Unit 26165 leveraged this flaw since 2022 in spearphishing campaigns against Western logistics, IT, and transport-coordination entities supporting Ukraine aid, complemented by exploitation of CVE-2023-38831 (WinRAR — spoofed file extensions inside ZIP/RAR archives enabling code execution) and Roundcube Webmail vulnerabilities (CVE-2020-12641, CVE-2020-35730, CVE-2021-44026 — XSS and SQL injection) against webmail targets. Post-exploitation involved deployment of HEADLACE/MASEPIE backdoors, credential extraction tools (Certipy, ldap-dump, GPPPassword), PsExec for lateral movement, periodic Exchange Web Services (EWS) queries for email collection, and outbound C2 via residential proxies and dedicated VPS infrastructure.
- **Affected Products:** Microsoft Outlook 2013, 2016, 2019, 2021, Microsoft 365 Apps (versions prior to March 14, 2023 security updates) [CVE-2023-23397]; RARLAB WinRAR versions before 6.23 [CVE-2023-38831]; Roundcube Webmail before 1.3.17 and 1.4.x before 1.4.12 [CVE-2021-44026]; Roundcube Webmail before 1.2.13, 1.3.x before 1.3.16, and 1.4.x before 1.4.10 [CVE-2020-35730]; Roundcube Webmail [CVE-2020-12641]
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true — public PoC available, e.g., https://github.com/Trackflaw/CVE-2023-23397
- **Patch Available:** true — Microsoft security update for CVE-2023-23397 released March 14, 2023; WinRAR 6.23 for CVE-2023-38831; Roundcube patches for CVE-2021-44026, CVE-2020-35730, and CVE-2020-12641. Advisory: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a
- **Active Exploitation:** true — CISA, NSA, FBI, and partner agencies confirm Russian GRU Unit 26165 has actively exploited CVE-2023-23397 (and related CVEs) in targeted campaigns against Western logistics entities and technology companies since at least 2022, in support of Russia's military objectives related to Ukraine. Microsoft Threat Intelligence and independent researchers also observed in-the-wild exploitation of CVE-2023-23397 prior to AA25-141A publication. Sources: CISA AA25-141A (https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a), Microsoft MSRC (https://msrc.microsoft.com/update-guide/vulnerability/cve-2023-23397).
- **Threat Actors:** Russian GRU 85th Main Special Service Center (85th GTsSS), military unit 26165 — tracked as APT28, Fancy Bear, Forest Blizzard, Blue Delta, Sednit, Sofacy, STRONTIUM, Tin Woodman, and UAC-0028
- **Mitigation:** 1) Apply the Microsoft Outlook security update from March 14, 2023 to remediate CVE-2023-23397, and all subsequent monthly rollups. 2) Block outbound SMB (TCP/445) and WebDAV (TCP/80, 443) from user workstations at the network egress to prevent NTLM hash leakage via PidLidReminderFileParameter. 3) Enforce SMB signing, LDAP signing, and LDAP channel binding to defeat NTLM relay attacks. 4) Disable NTLMv1; where NTLMv2 is required, enable Extended Protection for Authentication (EPA) and NTLM relay protections. 5) Update WinRAR to version 6.23 or later (CVE-2023-38831). 6) Update Roundcube Webmail to patched versions for CVE-2020-12641, CVE-2020-35730, and CVE-2021-44026. 7) Hunt for and remediate GRU IoCs listed in the advisory (HEADLACE/MASEPIE IPv4 addresses, domains, and file hashes). 8) Audit and rotate any credentials that may have been harvested via Outlook autodiscover or NTLM relay. 9) Enforce Kerberos-only authentication where possible and require MFA on all remote-access and privileged accounts. 10) Hunt for HEADLACE/MASEPIE implants, unauthorized PsExec usage, suspicious EWS query patterns, and outbound C2 to known GRU proxy infrastructure.
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

## 13. 🟠 Zero-Day — CrowdStrike Uncovers New Prompt Injection Techniques

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jul 07, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-uncovers-new-prompt-injection-techniques/>

---

## 14. 🟠 Zero-Day — Unpatched XRING Flaw in XQUIC Lets Remote Clients Crash HTTP/3 Servers

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://thehackernews.com/2026/07/unpatched-xring-flaw-in-xquic-lets.html>

> A single wrong variable on one line in XQUIC, Alibaba&#x27;s QUIC and HTTP/3 library, lets any remote client crash the server with a short burst of completely legal traffic. There is no patch.

FoxIO researcher Sébastien Féry disclosed the flaw on July 8 and nicknamed it XRING. He says it needs no login and no malformed packets: about 260 bytes of ordinary QPACK traffic takes the server

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
