# Zero Day Pulse

> **Generated:** 2026-07-08 19:06 UTC &nbsp;|&nbsp; **Total:** 29 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 16 &nbsp;|&nbsp; 🟡 High: 13 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path traversal vulnerability (CWE-22) in SimpleHelp RMM web application endpoints (including the 'toolbox' component) that allows unauthenticated remote attackers to download arbitrary files from the SimpleHelp host by sending crafted HTTP requests containing directory traversal sequences (e.g., '../../../../etc/passwd'). Sensitive files retrievable include SimpleHelp's serverconfig.xml (containing hashed admin/technician passwords), /etc/passwd, and private SSH keys. Attackers chain this flaw to extract configuration, crack or replay the hashed admin password, and gain administrative remote-access to downstream SimpleHelp-managed machines.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) v5.5.7 and earlier (including v5.4.x and v5.3.x branches)
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Yes. A public proof-of-concept is available at https://github.com/imjdl/CVE-2024-57727. A Metasploit module (auxiliary/scanner/http/simplehelp_toolbox_path_traversal) also exists.
- **Patch Available:** Yes. SimpleHelp released v5.5.8 in January 2025, plus patched builds v5.4.10 and v5.3.9 for older branches. Vendor advisory: https://guides.simple-help.com/kb---security-vulnerabilities-01-2025
- **Active Exploitation:** Yes. CISA Advisory AA25-163A (06/12/2025) confirms exploitation of CVE-2024-57727 by ransomware actors (DragonForce) targeting a utility billing software provider and downstream customers via unpatched SimpleHelp RMM. Arctic Wolf separately observed exploitation starting January 22, 2025.
- **Threat Actors:** DragonForce ransomware group
- **Mitigation:** 1) Immediately upgrade SimpleHelp servers to v5.5.8 or later; for v5.4.x deploy v5.4.10, and for v5.3.x deploy v5.3.9. 2) Verify both the SimpleHelp server and all deployed Remote Access (RAS) installations are updated. 3) Change all Administrator and Technician passwords; restrict/login allowlists to known IPs. 4) Isolate SimpleHelp servers from direct internet exposure or stop the server process until fully patched. 5) For hosts believed to be compromised: disconnect from the internet, reinstall the OS from clean media, and restore from clean offline backups. 6) Maintain daily offline backups and a robust asset inventory; disable unnecessary OS applications and network protocols on internet-facing assets; review serviceconfig.xml for unauthorized registered servers.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — Critical Vulnerability Exposes GitHub Agentic Workflows to Prompt Injection

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://www.securityweek.com/critical-vulnerability-exposes-github-agentic-workflows-to-prompt-injection/>

> Researchers show how attackers can use a crafted public GitHub Issue to trick AI-powered workflows into exposing data from private repositories without authentication. The post Critical Vulnerability Exposes GitHub Agentic Workflows to Prompt Injection appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Indirect (workflow-level) prompt injection in GitHub Agentic Workflows ('GitLost'). An unauthenticated attacker opens a public GitHub Issue on any repository in an org using Agentic Workflows. The workflow's AI agent, triggered by events like 'issues.assigned', ingests the issue body as context. Attackers smuggle instructions past guardrails using keywords like 'Additionally', causing the agent to invoke built-in tools (file readers, 'add-comment', 'gh' CLI) to read files from private repositories in the same org using the CI GITHUB_TOKEN, then publish exfiltrated content as a public comment. No authentication to private repos is required because the CI token already holds the necessary scope. Formally categorized as 'Agentic Workflow Injection (AWI)' in arXiv:2605.07135.
- **Affected Products:** GitHub Agentic Workflows (gh-aw) — public preview (launched 2026-02-13); Safe Outputs MCP Gateway introduced in v1.8.0; permission tightening in v1.12.0; specification published at v1.24.0 (2026-06-13)
- **CVSS Score:** 40.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — public PoC published by Noma Labs. Workflow run: https://github.com/sasinomalabs/poc/actions/runs/23909666039 ; Injected public issue: https://github.com/sasinomalabs/poc/issues/153
- **Patch Available:** No formal CVE/GHSA patch advisory has been issued — the feature remains in public preview. GitHub has iteratively hardened it through the Safe Outputs MCP Gateway (added in gh-aw v1.8.0; over-broad add-comment / hide-comment permissions tightened in v1.12.0; specification published as v1.24.0 on 2026-06-13). Upgrade to the latest gh-aw release and follow the Safe Outputs MCP Gateway Specification: https://github.github.com/gh-aw/specs/safe-outputs-specification/
- **Active Exploitation:** No confirmed in-the-wild exploitation has been reported. Noma Labs executed the attack only in a controlled researcher proof-of-concept (https://github.com/sasinomalabs/poc/actions/runs/23909666039). No CISA KEV entry, no mass scanning observation, and no named threat actor tied to the 'GitLost' flaw has been reported across SecurityWeek, DarkReading, DevOps.com, Hackread, SiliconANGLE, or Noma Security coverage.
- **Threat Actors:** None known
- **Mitigation:** Treat all user-generated content (issue titles, bodies, comments, PR descriptions, commit messages) as untrusted input. Restrict the workflow's GITHUB_TOKEN scope to the minimum needed for the trigger repository — do NOT grant cross-repository read. Enforce least privilege on every AI agent tool and restrict which tools can post public content. Keep a hard logical separation between untrusted user input and the agent's core system prompt. Adopt GitHub's Safe Outputs MCP Gateway, which forces agent outputs through allowlisted/filtered channels (available in gh-aw v1.8.0+, hardened in v1.12.0; spec v1.24.0 published 2026-06-13). Audit existing Agentic Workflows markdown definitions and remove unnecessary cross-repo permissions before enabling workflows on issue events.
- **Vendor Advisory:** https://github.github.com/gh-aw/specs/safe-outputs-specification/

---

## 3. 🟠 Zero-Day — CISA orders feds to prioritize patching Langflow auth bypass flaw

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-prioritize-patching-langflow-auth-bypass-flaw/>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) gave federal agencies until Friday to patch an actively exploited vulnerability in the Langflow visual framework for building AI agents. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Insecure Direct Object Reference (IDOR) / authorization-bypass-through-user-controlled-key in the get_flow_by_id_or_endpoint_name helper in src/backend/base/langflow/helpers/flow.py. When a flow is referenced by UUID (flow_id), the helper queries the database directly without checking that the authenticated caller owns the flow. The flaw is reachable via the /api/v1/responses endpoint, where an authenticated low-privileged user (holding any valid Langflow API key) can specify another tenant's flow_id as the 'model' parameter and have the victim's flow executed under their identity. This grants cross-tenant read/execution access to AI workflows, the data they process, and downstream LLM/cloud secrets configured in those flows, plus the ability to consume the victim's compute resources. Network-accessible, low-complexity, requires only valid authentication (PR:L).
- **Affected Products:** Langflow versions < 1.9.1 (langflow-ai/langflow on PyPI, Docker, and self-hosted deployments); fixed in 1.9.1, recommended upgrade to 1.9.2 or later.
- **CVSS Score:** 9.9
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:L
- **Exploit Available:** Yes - a public proof-of-concept / exploit recipe is included in the official GitHub advisory (GHSA-qrpv-q767-xqq2). It is a simple authenticated curl request to POST /api/v1/responses supplying the victim's flow_id (UUID) as the 'model' field and the attacker's x-api-key header. Reference: https://github.com/advisories/GHSA-qrpv-q767-xqq2
- **Patch Available:** Yes - official vendor patch has been released. Fixed in Langflow 1.9.1 via pull request #12832 (commit on the langflow-ai/langflow repository); the recommended upgrade target is 1.9.2 or later. Patch / advisory URL: https://github.com/advisories/GHSA-qrpv-q767-xqq2 (GitHub Security Advisory, GitHub Reviewed, Critical severity, published Jun 19, 2026).
- **Active Exploitation:** Yes - confirmed active exploitation in the wild. Sysdig Threat Research Team (TRT) first observed exploitation of CVE-2026-55255 on June 25, 2026 (03:41 UTC) from a single operator (IP 45.207.216.55), chained with prior CVE-2026-33017 RCE attempts; the same operator hijacked flows and injected 'leak api keys' prompts to harvest embedded LLM/cloud/database credentials. CISA added CVE-2026-55255 to the Known Exploited Vulnerabilities (KEV) Catalog on July 7, 2026, with a BOD 26-04 remediation deadline of July 10, 2026 for U.S. Federal Civilian Executive Branch agencies. Sources: Sysdig TRT blog (https://www.sysdig.com/blog/understanding-langflow-cve-2026-55255-and-why-higher-cvss-vulnerabilities-arent-always-the-most-exploited), Help Net Security (https://www.helpnetsecurity.com/2026/07/08/langflow-vulnerability-cve-2026-55255-exploited/), and BleepingComputer (https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-prioritize-patching-langflow-auth-bypass-flaw/).
- **Threat Actors:** None known (by named group/attribution). Public reporting describes a single opportunistic, financially motivated operator observed from IP 45.207.216.55 abusing the flaw for credential harvesting (embedded LLM provider API keys, cloud credentials, database secrets); no specific APT or ransomware group has been publicly attributed.
- **Mitigation:** Upgrade Langflow to version 1.9.2 or later (1.9.1 contains the upstream fix in PR #12832, but 1.9.2+ is the CISA/SentinelOne-recommended baseline). Hardening: place Langflow behind authentication/network ACLs, restrict API key issuance, audit cross-user flow executions, rotate any LLM provider keys, cloud credentials, and database secrets stored in or reachable from Langflow flows, and hunt for the IoCs published by Sysdig and SentinelOne (notably source IP 45.207.216.55 and unusual /api/v1/responses traffic patterns).
- **Vendor Advisory:** https://github.com/advisories/GHSA-qrpv-q767-xqq2

---

## 4. 🟠 Zero-Day — CISA Adds 4 Actively Exploited Adobe, Joomla, and Langflow Flaws to KEV

**CVE:** `CVE-2026-48282` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://thehackernews.com/2026/07/cisa-adds-4-actively-exploited-adobe.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added four security flaws to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

The vulnerabilities are listed below -


  CVE-2026-48282 (CVSS score: 10.0) - A path traversal vulnerability in Adobe ColdFusion that could lead to arbitrary code execution in the context of the

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-48282 is an Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Adobe ColdFusion's Remote Development Services (RDS) module. An unauthenticated attacker can send a specially crafted HTTP POST request to the /CFIDE/main/ide.cfm?ACTION=FILEIO endpoint using the RDS RPC protocol. Because the server fails to validate or canonicalize the target path, the attacker can traverse out of the intended directory and write arbitrary files (e.g., a malicious .cfm webshell) into the ColdFusion webroot. The attacker then requests the dropped file directly via the web server, triggering arbitrary code execution in the context of the ColdFusion service account, which can be escalated to full host compromise.
- **Affected Products:** Adobe ColdFusion 2025 Update 9 and earlier, Adobe ColdFusion 2023 Update 20 and earlier
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Exploit Available:** Yes - watchTowr published a full technical proof-of-concept on July 2, 2026, including the raw HTTP POST request payload exploiting the RDS FILEIO path traversal. Source: https://labs.watchtowr.com/its-37oc-and-all-we-can-think-about-is-coldfusion-adobe-coldfusion-security-bulletin-apsb26-68-cve-bonanza/
- **Patch Available:** Yes - Adobe released ColdFusion 2025 Update 10 and ColdFusion 2023 Update 21 on June 30, 2026 (advisory APSB26-68, Priority 1). Patch/advisory URL: https://helpx.adobe.com/security/products/coldfusion/apsb26-68.html
- **Active Exploitation:** Yes - confirmed active exploitation in the wild. CISA added CVE-2026-48282 to its Known Exploited Vulnerabilities (KEV) Catalog on July 7, 2026 (https://www.helpnetsecurity.com/2026/07/07/adobe-coldfusion-cve-2026-48282-exploitation-detected/). Threat-intelligence service KEVIntel observed exploitation attempts against its honeypot sensors on July 2, 2026 - within hours of watchTowr's public technical PoC. Resecurity has also independently tracked exploitation of this flaw in the wild.
- **Threat Actors:** None known
- **Mitigation:** 1) Upgrade to ColdFusion 2025 Update 10 or ColdFusion 2023 Update 21 (released June 30, 2026). 2) Disable Remote Development Services (RDS) unless strictly required. 3) Restrict/block external network access to management endpoints, specifically /CFIDE/administrator, /CFIDE/main/ide.cfm, and /CFIDE/main/websocket.cfm (firewall them off or allowlist admin source IPs). 4) Deploy a Web Application Firewall (WAF) rule to block RDS RPC payloads and path-traversal patterns. 5) Run ColdFusion under a least-privilege service account and limit write permissions to the webroot. 6) Hunt for unauthorized .cfm, .cfc, .cfml, or .jsp files in the webroot and /CFIDE/ directories. 7) If compromise is suspected, reset administrator passwords, database credentials, and any API keys stored on the host.
- **Vendor Advisory:** https://helpx.adobe.com/security/products/coldfusion/apsb26-68.html

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an architectural attack class against LLM-integrated applications and AI agents. An attacker plants hidden natural-language or multimodal instructions inside untrusted external content (public web pages, SEO text, emails, documents, image metadata). When the AI assistant/agent later retrieves and ingests that content as part of a user-driven task, the model can silently follow the attacker-controlled instructions instead of (or in addition to) the user's intent. Because the injected text comes from a trusted data channel rather than from the user/system prompt, classical prompt-instruction boundaries are blurred. Observed malicious outcomes include data exfiltration of user context, unauthorized tool calls/file deletion, message/email abuse from the agent, denial-of-service via infinite-stream generation, and SEO poisoning.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes. Multiple public PoCs and weaponized exploits exist. Google documents real-world payloads: data-exfiltration prompts, 'delete all files' payloads, resource-exhaustion via infinite streams, the 'tweety bird' tone-changing prank, and SEO-manipulation injections. Public PoC sources: OWASP LLM01:2025 (https://genai.owasp.org/llmrisk/llm01-prompt-injection/), OWASP prompt-injection attacks page (https://github.com/OWASP/www-community/blob/master/pages/attacks/prompt-injection.md), HiddenLayer Cursor research (https://www.hiddenlayer.com/research/how-hidden-prompt-injections-can-hijack-ai-code-assistants-like-cursor), and Trail of Bits GitHub Copilot research (https://blog.trailofbits.com/2025/08/06/prompt-injection-engineering-for-attackers-exploiting-github-copilot/).
- **Patch Available:** No traditional vendor patch has been released for the IPI class. Google treats IPI as a continuous engineering/red-team problem covered by ongoing hardening and the AI Vulnerability Reward Program rather than a single fixable bug. Reference: http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html
- **Active Exploitation:** Confirmed active in-the-wild exploitation. The Google Security Blog (Apr 23, 2026, http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html) reports a 32% increase in the 'malicious' prompt-injection category in Common Crawl data between November 2025 and February 2026. Independent confirmation: Palo Alto Networks Unit 42 'Web-Based Indirect Prompt Injection Observed in the Wild' (Mar 3, 2026, https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/), Forcepoint X-Labs '10 Indirect Prompt Injection Payloads Caught in the Wild' (Apr 22, 2026), and Help Net Security 'Indirect prompt injection is taking hold in the wild' (Apr 24, 2026, https://www.helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild/).
- **Threat Actors:** None known
- **Mitigation:** No single vendor patch exists; IPI is mitigated via defense-in-depth. Google recommends continuous model hardening, ongoing red-team/pressure-testing, and the AI Vulnerability Reward Program. Microsoft guidance (https://learn.microsoft.com/en-us/security/zero-trust/sfi/defend-indirect-prompt-injection) and OWASP (https://genai.owasp.org/llmrisk/llm01-prompt-injection/) recommend: probabilistic + deterministic mitigations layered together; human-in-the-loop confirmation for high-impact agent actions; least-privilege permissions and tool scoping on agents; sanitization and origin marking of retrieved content; system prompts that explicitly instruct the model to ignore instructions found in external data; strict input validation, output filtering, and activity monitoring; and segmenting untrusted content so it cannot reach privileged tools or memory.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) — classified as CWE-1427 'Improper Neutralization of Input Used for LLM Prompting' and OWASP LLM01:2025 — exploits an LLM's inability to distinguish developer system directives from untrusted external content. Attackers embed malicious natural-language instructions inside data sources the assistant ingests (email HTML with hidden/invisible text, shared documents, calendar invites, web pages, RAG-retrieved files). When the user issues an unrelated query, the model ingests the poisoned content and the embedded directives override the system prompt, causing unintended actions: data exfiltration via markdown-image or link callbacks to attacker-controlled URLs (leaking chat history, email, calendar); phishing-content rewriting (substituting attacker URLs into AI summaries); tool-call abuse (deleting files, sending emails, executing shell commands); and resource exhaustion (fork bombs, sudo rm -rf). Observed delivery mechanisms include CSS-hidden text (display:none, opacity:0, off-screen positioning), white-on-white text, textarea-staged tokens, SVG/CDATA encapsulation, data-* attribute cloaking, and zero-width/invisible Unicode characters. The attack requires no direct input from the victim and persists as long as the malicious content sits in the model's data sources.
- **Affected Products:** Google Gemini app (consumer Gemini); Google Workspace with Gemini — Gemini in Gmail, Gemini in Docs editors, Gemini in Drive, Gemini in Chat; Gemini Enterprise; Vertex AI Search; Gemini CLI. No specific build numbers or version ranges published in the advisory.
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — public PoCs and weaponized payloads are widely available. Key sources: (1) HiddenLayer exploit for Gemini for Workspace in Gmail/Slides/Drive (Sep 25, 2024) — https://www.hiddenlayer.com/research/new-gemini-for-workspace-vulnerability-enabling-phishing-content-manipulation ; (2) Noma 'GeminiJack' zero-click IPI exfiltrating email/calendar/document data via image-tag callbacks in Gemini Enterprise / Vertex AI Search (Dec 8, 2025) — https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/ ; (3) Forcepoint X-Labs — 10 verified IPI payloads on live websites (Apr 22, 2026) — https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads ; (4) 0din.ai 'Phishing for Gemini' invisible-character injection hijacking Gemini summaries (Jul 10, 2025) — https://0din.ai/blog/phishing-for-gemini ; (5) Cyera Research Labs — command & prompt-injection chain in Gemini CLI (Nov 17, 2025; Google issued patches via VRP) — https://www.cyera.com/research/cyera-research-labs-discloses-command-prompt-injection-vulnerabilities-in-gemini-cli ; (6) Immersive Labs — IPI-in-HTML-email PoC bypassing commercial email-security products (Jul 21, 2025) — https://www.immersivelabs.com/resources/c7-blog/weaponizing-llms-bypassing-email-security-products-via-indirect-prompt-injection.
- **Patch Available:** No traditional software 'patch' is applicable — IPI is a class-level vulnerability, not a single code defect with a fixed version. Google's standing mitigation framework is documented at https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html and operationalized in this April 2026 advisory (https://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html). Specific IPI-related bugs that HAVE been patched include the Gemini CLI command/prompt-injection chain (Cyera, Nov 17 2025) and the Gemini-Workspace IPI (HiddenLayer, Sep 25 2024), addressed via Google's Vulnerability Rewards Program.
- **Active Exploitation:** Yes — confirmed in-the-wild exploitation reported by multiple independent researchers. Palo Alto Unit 42 documented web-based indirect prompt injection (IDPI) attacks Dec 2025–Mar 2026 used to evade AI ad-review/moderation (reviewerpress[.]com), manipulate SEO for phishing/betting domains (1win affiliate network), and trigger destructive actions (sudo rm -rf, fork bombs) — https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/ (Mar 3, 2026). Forcepoint X-Labs confirmed 10 verified IPI payloads on otherwise legitimate websites on Apr 22, 2026 (financial fraud via PayPal/Stripe donation scams, data destruction, DoS, output hijacking, API-key exfiltration) — https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads. Help Net Security corroborates (Apr 24, 2026): 'Indirect prompt injection is taking hold in the wild' — https://www.helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild/. Immersive Labs published an IPI-in-HTML-email PoC bypassing commercial email-security products (Jul 21, 2025) — https://www.immersivelabs.com/resources/c7-blog/weaponizing-llms-bypassing-email-security-products-via-indirect-prompt-injection. 0din.ai 'Phishing for Gemini' demonstrated live AI-summary hijacking in Gemini (Jul 10, 2025) — https://0din.ai/blog/phishing-for-gemini.
- **Threat Actors:** None known
- **Mitigation:** Google's layered defense strategy (no single patch): (1) prompt-injection content classifiers detecting malicious instructions across ingested data formats; (2) 'security thought reinforcement' — targeted system-level security instructions added around prompt content; (3) Markdown sanitization and suspicious-URL redaction via Google Safe Browsing for external images/links; (4) user-confirmation framework requiring explicit approval before risky Gemini operations; (5) end-user contextual security-notification UI when IPI is detected and mitigated; (6) model resilience — adversarial robustness hardening of the underlying Gemini model. End-user / admin hardening: treat AI summaries as untrusted, verify suspicious AI-generated actions out-of-band, and apply least-privilege on the agentic surface (limit tools Gmail/Drive/Chat share with Gemini). Workspace admin reference: https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini ; user help: https://support.google.com/gemini?p=gemini_apps_safety.
- **Vendor Advisory:** https://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is a category-level threat to agentic browsers. An attacker plants hidden instructions inside untrusted web content (malicious sites, third-party iframes, user-generated content like reviews) that the AI agent reads while completing a user's multi-step task. Those instructions manipulate the agent's planning model, allowing the attacker to perform actions the user never requested — including goal-hijacking, initiating unwanted financial transactions (purchases, payments, messaging), and exfiltrating sensitive data. The AI side-panel acts as a new intermediary with overly broad access to the browser environment, widening the attack surface relative to a non-agentic browser. IPI effectively serves as a bypass of the traditional same-origin policy via an AI intermediary.
- **Affected Products:** Google Chrome with Gemini in Chrome agentic capabilities
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit is referenced in this blog post. The blog is a defensive architecture announcement, not a vulnerability disclosure.
- **Patch Available:** No specific patch or CVE is referenced in this blog post. The described defenses are being deployed as new integrated components of Chrome's agentic browsing experience. Google notes that fixes can be pushed rapidly to users via Chrome's auto-update mechanism. Blog URL: http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** No confirmed in-the-wild exploitation is cited in this blog post. The blog is a proactive architectural disclosure, not a response to observed exploitation. For broader context, a separate Google Threat Intelligence Group report from January 29, 2025 (https://cloud.google.com/blog/topics/threat-intelligence/adversarial-misuse-generative-ai) observed attempted but unsuccessful prompt-injection/jailbreak activity against the Gemini web app by state-backed actors attributed to Iran, China, and Russia — the report explicitly states no original/persistent prompt-attack success was observed.
- **Threat Actors:** None known
- **Mitigation:** Chrome's layered defense architecture for Gemini agentic capabilities: (1) User Alignment Critic — an isolated Gemini-based model that vets every proposed action against the user's stated goal; (2) Agent Origin Sets — extends same-origin policy via a trusted gating function restricting the agent to user-bounded Read-only and Read-writable origins, blocking cross-origin data leakage; (3) User Confirmations — deterministic pauses on sensitive flows (banking/medical sites, password manager sign-ins, purchases, payments, messaging); (4) Real-time prompt-injection classifier — on-Chrome classifier running alongside Safe Browsing and on-device AI scam detection; (5) Spotlighting — technique prioritizing user/system instructions over page content; (6) Continuous automated red-teaming — sandboxed malicious-site generators; (7) Chrome bug bounty up to $20,000. Chrome's auto-update channel enables rapid defense deployment.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2025-48530 is a linear/out-of-bounds read memory safety flaw (CWE-125) in CrabbyAVIF, the Rust-based AVIF image decoder used by Android. Incorrect bounds checks in multiple locations of the CrabbyAVIF parser/decoder cause out-of-bounds memory accesses when handling a crafted AVIF image. Android's Scudo hardened allocator surrounded the affected secondary allocations with guard pages, so the overflow manifested as a noisy crash rather than silent memory corruption. In combination with other bugs, this OOB bug could potentially be chained into remote code execution over the network.
- **Affected Products:** Google Android 16 (platform/external/rust/crabbyavif package); AOSP '16-next' branch of CrabbyAVIF
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** No public proof-of-concept or weaponized exploit is publicly known. According to Google's November 13, 2025 Security Blog post, the linear buffer overflow was caught internally before it ever shipped to a public Android release.
- **Patch Available:** Yes. Patches were merged into CrabbyAVIF in AOSP and shipped in the Android Security Bulletin August 2025 (security patch level 2025-08-01). Patch commits: https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050, https://android.googlesource.com/platform/external/rust/crabbyavif/+/9bcc1a311114ab844b417d3cdec50dcedfd0603f, and https://android.googlesource.com/platform/external/rust/crabbyavif/+/42feb427a42afd9eebe6391a0d8a7b083fe82140
- **Active Exploitation:** No confirmed active exploitation in the wild. Google's write-up notes the vulnerability was caught internally before it reached a public Android release. The vulnerability is not listed in CISA's Known Exploited Vulnerabilities (KEV) catalog, and no third-party threat-intelligence source reports observed exploitation.
- **Threat Actors:** None known
- **Mitigation:** Apply the Android 2025-08-01 security patch level (or later). The Scudo hardened allocator with guard pages neutralized this overflow. Devices already running a compatible patch level are not affected.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is a class of attack against generative AI systems in which an adversary hides malicious natural-language instructions inside external content that the LLM subsequently ingests—emails, documents, calendar invites, web pages, or other data sources the AI retrieves or summarizes on the user's behalf. When the model processes this tainted content, the embedded instructions hijack the model's reasoning, causing it to exfiltrate sensitive user data (e.g., forwarding emails/documents to an attacker), perform unauthorized actions (e.g., deleting calendar events, sending messages), or otherwise deviate from the user's intent. Unlike direct prompt injection, the attacker never touches the model's prompt directly; the payload is delivered via untrusted data the model is instructed to consume. The June 2025 blog specifically references CVE-2025-32711 ('EchoLeak') in Microsoft 365 Copilot as a real-world instance where rendered external image URLs could be used to exfiltrate conversational context.
- **Affected Products:** Google Gemini app, Gemini in Google Workspace (Gmail, Google Docs editors, Google Drive, Google Chat, Google Calendar), Gemini 2.5 models (with the layered defense strategy also applicable to Gemini 2.0). No specific build numbers or version ranges are published — the protections are described as continuously applied to the Gemini model family.
- **CVSS Score:** 9.3
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No Google-specific Gemini proof-of-concept or weaponized exploit is referenced in the blog. The post does reference CVE-2025-32711 ("EchoLeak"), a 0-click image-rendering prompt-injection exfiltration vulnerability disclosed against Microsoft 365 Copilot (June 2025, CVSS 9.3), as an example of the same class of attack—and states that EchoLeak is 'not applicable to Gemini' because Gemini's markdown sanitizer blocks external image URL rendering. Independent third-party research (e.g., https://www.miggo.io/post/weaponizing-calendar-invites-a-semantic-attack-on-google-gemini) demonstrated related prompt-injection techniques against Gemini, but no public PoC targeting a specific Gemini CVE is cited by Google in this advisory.
- **Patch Available:** No discrete vendor patch is associated with this blog post — it is general defensive guidance for the indirect-prompt-injection class of vulnerabilities affecting the Gemini product family. The mitigations are delivered as ongoing model updates (Gemini 2.5 hardening), built-in platform features (markdown sanitizer, Google Safe Browsing URL redaction), and product features (HITL confirmation, end-user alerts) rather than as a single downloadable patch. Advisory URL: https://blog.google/security/mitigating-prompt-injection-attacks/ (also published at http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html).
- **Active Exploitation:** Google references 'attacks that we've stopped' and 'ways we see bad actors trying to leverage AI,' indicating Google has observed indirect-prompt-injection attempts against Gemini-based products and that the layered defenses have mitigated them. No specific in-the-wild Gemini compromise via indirect prompt injection is reported as tied to this June 13, 2025 advisory. A real-world instance on a competing product (Microsoft 365 Copilot) was disclosed as CVE-2025-32711 / 'EchoLeak' in June 2025, and Palo Alto Unit 42 observed web-based indirect prompt injection attacks in the wild starting around December 2025 (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/).
- **Threat Actors:** None known. The June 13, 2025 Google Security Blog post does not name any specific threat actor group, APT campaign, or ransomware operator. (Note: a later February 2026 Google Threat Intelligence Group report documented state-sponsored APT groups abusing Gemini AI as a productivity tool, but that concerns adversaries using Gemini across the attack lifecycle—not exploiting Gemini via indirect prompt injection—and is out of scope for this June 2025 advisory.)
- **Mitigation:** Google's blog describes a layered defense strategy as the mitigation — there is no single patch. The layers are: (1) Adversarial-data training of the Gemini 2.5 model to make it inherently resistant to embedded malicious instructions, paired with continuous automated red-teaming and fine-tuning. (2) Prompt-injection content classifiers — ML models that scan incoming emails, documents, and other external content for likely malicious instructions before they reach the LLM. (3) Security thought reinforcement — targeted system-level instructions that remind the model to ignore adversarial commands in untrusted data. (4) Markdown sanitization and suspicious-URL redaction — Gemini strips or refuses to render external image URLs and uses Google Safe Browsing to redact unsafe links, which is what neutralizes EchoLeak-style attacks. (5) Human-in-the-loop user confirmation framework — risky actions (e.g., deleting calendar events, sending messages on the user's behalf) require explicit user approval. (6) End-user security-mitigation notifications — Gemini surfaces contextual alerts and help-center links when defenses block a suspected prompt-injection attempt. Google Workspace administrators can additionally review Google's Gemini admin controls at https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** CISA AA25-239A documents PRC state-sponsored actors conducting long-running cyber-espionage intrusions against backbone, provider-edge (PE), and customer-edge (CE) routers of major telecommunications providers, plus government, transportation, lodging, and military networks. Initial access is achieved by exploiting publicly known, previously disclosed vulnerabilities in internet-exposed network edge devices (the CVEs above). After gaining a foothold, the actors (a) modify Access Control Lists, often naming them 'access-list 20', to whitelist actor-controlled IPs; (b) abuse Cisco Guest Shell / IOx containers and enable Cisco IOS XR 'sshd_operns' on the non-standard port TCP/57722 for covert persistence; (c) replace TACACS+/RADIUS server entries with attacker-controlled IPs to harvest credentials via PCAP; (d) enable traffic mirroring (SPAN/RSPAN/ERSPAN), then encapsulate stolen traffic in GRE/mGRE/IPsec tunnels to multi-hop proxies (e.g., STOWAWAY) using non-standard ports; (e) clear local logs and disable log forwarding; (f) collect BGP, RSVP, MIB, and MPLS configuration data via TFTP; (g) enumerate subscriber records and exfiltrate over custom SFTP clients (cmd1, cmd3, new2, sft). The actors pivot through provider-to-provider and provider-to-customer trusted connections to reach additional networks. CISA notes that exploitation of zero-day vulnerabilities has NOT been observed to date — the activity is based on known, previously disclosed CVEs.
- **Affected Products:** Cisco IOS XE Software (Web UI feature, physical and virtual devices, versions prior to 17.9.4a, 17.6.6a, 17.3.8a, 16.12.10a and other fixed releases); Cisco IOS and IOS XE Smart Install (TCP/4786, CVE-2018-0171); Cisco IOS XR (sshd_operns on TCP/57722); Palo Alto Networks PAN-OS GlobalProtect (versions before 10.2.9-h1, 11.0.4-h1, 11.1.2-h3); Ivanti Connect Secure 9.x and 22.x; Ivanti Policy Secure 9.x and 22.x. Additional suspected/affected targets identified by the industry include Fortinet, Juniper, Microsoft Exchange, Nokia routers/switches, Sierra Wireless devices, SonicWall, Check Point, Forcepoint, and Trellix.
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H (vector for CVE-2024-3400, the highest-severity CVE cited in AA25-239A; the advisory additionally references CVE-2023-20198 CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, CVE-2018-0171 CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, CVE-2024-21887 CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H, CVE-2023-46805, and CVE-2023-20273).
- **Exploit Available:** Yes. Public proof-of-concept exploits exist on GitHub for the most-exploited CVEs in this campaign: CVE-2024-3400 (https://github.com/retkoussa/CVE-2024-3400) and CVE-2023-20198 (https://github.com/smokeintheshell/CVE-2023-20198). Horizon3.ai also published a technical deep-dive and PoC for the Cisco IOS XE Web UI vulnerabilities CVE-2023-20198 and CVE-2023-20273 (https://horizon3.ai/attack-research/attack-blogs/cisco-ios-xe-cve-2023-20198-deep-dive-and-poc/). Metasploit and multiple exploit kits additionally cover several of the referenced CVEs.
- **Patch Available:** Yes. Vendor patches exist for every CVE cited in AA25-239A: Cisco IOS XE fixed in releases 17.9.4a, 17.6.6a, 17.3.8a, and 16.12.10a (advisory https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxe-webui-privesc-j22SaA4z; Smart Install guidance https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180328-smi2.html and https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180409-smi.html); Palo Alto Networks PAN-OS fixed in 10.2.9-h1, 11.0.4-h1, and 11.1.2-h3 (https://security.paloaltonetworks.com/CVE-2024-3400/); Ivanti Connect Secure and Ivanti Policy Secure patched per Ivanti KB (https://hub.ivanti.com/s/article/KB-CVE-2023-46805-Authentication-Bypass-CVE-2024-21887-Command-Injection-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure-Gateways and https://www.ivanti.com/blog/security-update-for-ivanti-connect-secure-and-ivanti-policy-secure-gateways).
- **Active Exploitation:** Yes — confirmed active exploitation in the wild. CISA, NSA, and FBI jointly released AA25-239A on August 27, 2025 (web-posted September 3, 2025) documenting ongoing PRC state-sponsored compromise of telecommunications backbone, PE, and CE routers worldwide, with 'considerable success exploiting publicly known common vulnerabilities'. The activity overlaps with industry-tracked intrusions commonly referred to as Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, and GhostEmperor. CISA notes that exploitation of zero-day vulnerabilities has NOT been observed to date — all observed exploitation leverages previously disclosed CVEs.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor, APT40 (Kryptonite Panda); associated PRC entities Sichuan Juxinhe Network Technology Co. Ltd., Beijing Huanyu Tianqiong Information Technology Co. Ltd., and Sichuan Zhixin Ruijie Network Technology Co. Ltd.
- **Mitigation:** Apply patches for the six CVEs cited in the advisory (Cisco IOS XE 17.9.4a/17.6.6a/17.3.8a/16.12.10a; PAN-OS 10.2.9-h1/11.0.4-h1/11.1.2-h3; Ivanti Connect/Policy Secure KB patches). Cisco-specific hardening: disable Smart Install (no vstack) and restrict/block TCP/4786; disable the HTTP/HTTPS web UI ('no ip http server', 'no ip http secure-server'); disable outbound VTY ('transport output none'); audit and remove 'sshd_operns' on TCP/57722; use Type 8 (PBKDF2-SHA256) or Type 6 (AES) credentials instead of Type 5/7; disable Guest Shell ('guestshell disable' on IOS XE, 'guestshell destroy' on NX-OS) and IOx ('no iox'); append 'deny any any log' to all ACLs. General: segregate management traffic (SSH/HTTPS/SNMP/TACACS+/RADIUS) into an out-of-band network or dedicated management VRF; enforce SNMPv3, disable Telnet and unencrypted HTTP; apply Control-Plane Policing (CoPP) and infrastructure ACLs; baseline and audit router configs for unexpected GRE/IPsec tunnels, non-standard listening ports, external IPs in ACLs/TACACS+/RADIUS, packet capture jobs, and virtualized containers; validate firmware/image hashes against vendor values; prioritize patching from CISA's Known Exploited Vulnerabilities Catalog; upgrade unsupported devices to vendor-supported hardware.
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

## 15. 🟠 Zero-Day — Designing for the inevitable: System prompt leakage and mitigations in generative AI applications

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** AWS Security Blog &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://aws.amazon.com/blogs/security/designing-for-the-inevitable-system-prompt-leakage-and-mitigations-in-generative-ai-applications/>

> System prompts form the foundation of generative AI applications. A system prompt is a collection of instructions and operational context provided to a large language model (LLM) that shapes how the model behaves and interacts with users and tools. System prompts often contain proprietary information, including role definitions, behavioral guidelines, tool descriptions and usage instructions, […]

---

## 16. 🟠 Zero-Day — CISA orders feds to patch max severity ColdFusion flaw by Friday

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-max-severity-coldfusion-flaw-by-friday/>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has ordered government agencies to patch an actively exploited maximum-severity flaw in the Adobe ColdFusion commercial web app development platform by Friday. [...]

---

## 17. 🟡 High Severity — Ubiquiti Patches Critical UniFi Flaws Across Connect, Talk, Access, Protect, and OS

**CVE:** `CVE-2026-50746` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://thehackernews.com/2026/07/ubiquiti-patches-critical-unifi-flaws.html>

> Ubiquiti has shipped updates to address multiple critical security flaws impacting UniFi Connect, UniFi Talk, UniFi Access, UniFi Protect, and UniFi OS that could result in privilege escalation and arbitrary command execution.

The list of vulnerabilities is as follows -


  CVE-2026-50746 (CVSS score: 10.0) - An improper access control vulnerability in UniFi Connect Application that an attacker

---

## 18. 🟡 High Severity — 15-Year-Old GhostLock Flaw Enables Root and Container Escape on Most Linux Distros

**CVE:** `CVE-2026-43499` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://thehackernews.com/2026/07/15-year-old-ghostlock-flaw-enables-root.html>

> Researchers at Nebula Security have disclosed GhostLock (CVE-2026-43499), a 15-year-old Linux kernel flaw that lets any logged-in user take full root control of a machine that has not been patched.

The vulnerable code has shipped by default in essentially every mainstream distribution since 2011. The flaw needs no special permission, no unusual settings, and no network

---

## 19. 🟡 High Severity — Weblate SSRF: outbound URL guard misses some private ranges

**CVE:** `CVE-2026-50127` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-vmfc-9982-2m45>

> ### Impact

Weblate&#x27;s `VCS_RESTRICT_PRIVATE` did not properly account for some transitional IPv6 ranges, multicast addresses, or some semi-private IPv4 ranges, which allowed some addresses to bypass private range restrictions.

### Patches

* https://github.com/WeblateOrg/weblate/pull/19768

### Resources

The issue was reported by @tonghuaroot via GitHub, and the same user also provided the …

---

## 20. 🟡 High Severity — oasdiff does not enforce --allow-external-refs=false on the git-revision load path (SSRF / local file read)

**CVE:** `CVE-2026-53508` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-2jcc-mxv7-p3f9>

> ## Summary

From **v1.13.2** through **v1.18.0**, oasdiff did not enforce `--allow-external-refs=false` (library: `openapi3.Loader.IsExternalRefsAllowed = false`) when loading a spec from a **git revision** (the `rev:path` form, e.g. `main:openapi.yaml`). External `$ref`s were resolved on that load path even when external refs were explicitly disabled, so the mitigation silently did not apply ther…

---

## 21. 🟡 High Severity — Goploy: Cross-namespace IDOR and RCE via body-supplied row id in project and project_file handlers

**CVE:** `CVE-2026-53552` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-26rh-24rg-j3vv>

> ### Summary

`Project.AddFile`, `Project.EditFile`, `Project.RemoveFile`, and `Project.Edit` in `cmd/server/api/project/handler.go` accept a project or project-file row id from the JSON body and act on it without checking that the project belongs to the caller&#x27;s namespace. The corresponding `model.ProjectFile.GetData` and `model.Project.GetData` queries filter only by row id. A user holding t…

---

## 22. 🟡 High Severity — Kite has an authenticated cluster RBAC bypass in /api/v1/overview

**CVE:** `CVE-2026-53487` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-gvhc-wv3v-7pf8>

> ## Summary

Authenticated Kite users with any role can request `/api/v1/overview` for a cluster that their roles do not permit by selecting that cluster with `x-cluster-name`. The overview route is registered before `middleware.RBACMiddleware()` and `GetOverview` only checks `len(user.Roles) &gt; 0`, so it returns aggregate Kubernetes inventory and capacity data from unauthorized clusters.

The is…

---

## 23. 🟡 High Severity — ratex-parser has unbounded parser recursion that leads to stack overflow (process abort)

**CVE:** `CVE-2026-53531` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-4w5h-hx6r-28q7>

> ### Summary


RaTeX’s recursive-descent parser recurses one (or more) native stack frame per nesting level at `{`, `\left`, `\sqrt{`, `^{`, etc, with **no maximum depth limit**. A short, ~10 KB input of nested groups overflows the 8 MB main-thread stack and aborts the process. With `panic = &quot;abort&quot;` (`Cargo.toml:48`), and because a Rust stack overflow is always a fatal `SIGABRT` regardle…

---

## 24. 🟡 High Severity — @better-auth/oauth-provider's OAuth authorization-code grant allows concurrent redemption when two token requests race the find-then-delete primitive

**CVE:** `CVE-2026-53518` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-7w99-5wm4-3g79>

> ### Am I affected?

Users are affected if all of the following are true:

- Their project depends on `@better-auth/oauth-provider` at a version `&gt;= 1.6.0, &lt; 1.6.11`, or uses the embedded plugin in `better-auth &gt;= 1.4.8-beta.7, &lt; 1.6.0`, or enables the legacy `oidc-provider` or `mcp` plugins from `better-auth/plugins`.
- Their application exposes `/api/auth/oauth2/token` (or the legacy …

---

## 25. 🟡 High Severity — @better-auth/sso provider registration has server-side request forgery via unvalidated OIDC endpoints

**CVE:** `CVE-2026-53513` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-5rr4-8452-hf4v>

> ### Am I affected?

Users are affected if all of the following are true:

- Their application uses `@better-auth/sso` at a version `&gt;= 0.1.0, &lt; 1.6.11` on the stable line, or any `1.7.0-beta.x` on the pre-release line.
- The `sso()` plugin is added to their application&#x27;s `betterAuth({ plugins: [...] })` array.
- Any user with a valid Better Auth session can reach `POST /sso/register` (t…

---

## 26. 🟡 High Severity — Better Auth: OAuth refresh-token rotation forks the token family on concurrent redemption

**CVE:** `CVE-2026-53517` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-392p-2q2v-4372>

> ### Am I affected?

Users are affected if all of the following are true:

- Their project depends on `@better-auth/oauth-provider` at a version `&gt;= 1.6.0, &lt; 1.6.11`, or uses the embedded plugin in `better-auth &gt;= 1.4.8-beta.7, &lt; 1.6.0`.
- At least one OAuth client served by their application&#x27;s authorization server requests the `offline_access` scope, so refresh tokens are minted.
…

---

## 27. 🟡 High Severity — Better Auth: OAuth refresh-token replay via missing client authentication on oidc-provider and mcp plugins

**CVE:** `CVE-2026-53512` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-pw9m-5jxm-xr6h>

> ### Am I affected?

Users are affected if all of the following are true:

- Their application uses `better-auth` and has enabled at least one of: `oidcProvider()` (imported from `better-auth/plugins/oidc-provider`), or `mcp()` (imported from `better-auth/plugins/mcp`).
- Their application has at least one confidential OAuth client registered (any client with `type: &quot;web&quot; | &quot;native&q…

---

## 28. 🟡 High Severity — @aborruso/ckan-mcp-server: SSRF via base_url allows access to internal networks (Potential fix bypass of CVE-2026-33060)

**CVE:** `CVE-2026-53509` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-g84h-j7jj-x32p>

> ### Summary
A known vulnerability CVE-2026-33060 indicated tools including ckan_package_search and sparql_query that accept a base_url parameter had the risk of making HTTP requests to arbitrary endpoints without restriction. A fix was applied to filter out ip addresses. However, a method to bypass exists.

### Details
CKAN MCP Server validates caller-supplied CKAN server URLs by inspecting only t…

---

## 29. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
