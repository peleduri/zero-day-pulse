# Zero Day Pulse

> **Generated:** 2026-07-08 13:28 UTC &nbsp;|&nbsp; **Total:** 19 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 17 &nbsp;|&nbsp; 🟡 High: 2 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CWE-22 Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal'). Unauthenticated remote attackers can issue crafted HTTP requests to the SimpleHelp web application to traverse out of the intended directory and download arbitrary files from the SimpleHelp host. Files reachable via the flaw include SimpleHelp server configuration files that contain secrets (e.g., API tokens, integration credentials) and hashed user passwords, which the attacker can then crack offline to obtain valid technician/administrator credentials and pivot into downstream managed endpoints.
- **Affected Products:** SimpleHelp Remote Support / Remote Monitoring and Management (RMM) software, versions 5.5.7 and all earlier releases (including 5.4.x branch prior to 5.4.10 and 5.3.x branch prior to 5.3.9).
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true - Public PoC: https://github.com/imjdl/CVE-2024-57727 ; also a Metasploit module (auxiliary/scanner/http/simplehelp_toolbox_path_traversal) and OffSec writeup at https://www.offsec.com/blog/cve-2024-57727/
- **Patch Available:** true - SimpleHelp released patches between January 8-13, 2025 (v5.5.8, v5.4.10, and v5.3.9). Advisory: https://guides.simple-help.com/kb---security-vulnerabilities-01-2025 ; Release News: https://simple-help.com/release-news
- **Active Exploitation:** true - Confirmed active exploitation since at least January 2025. CISA published advisory AA25-163A on June 12, 2025, documenting ransomware actors (DragonForce) leveraging unpatched SimpleHelp RMM instances to compromise a utility billing software provider and downstream customers via double-extortion ransomware. CVE-2024-57727 was added to CISA's Known Exploited Vulnerabilities (KEV) Catalog on 2025-02-13. Sources: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a ; https://www.picussecurity.com/resource/blog/ransomware-actors-exploit-cve-2024-57727-in-unpatched-simplehelp-rmm ; https://www.securityweek.com/simplehelp-vulnerability-exploited-against-utility-billing-software-users/
- **Threat Actors:** DragonForce ransomware group (confirmed by CISA in AA25-163A); broader pattern of ransomware actors exploiting SimpleHelp vulnerabilities since January 2025 to compromise utility billing software providers and downstream customers via double-extortion attacks.
- **Mitigation:** Primary remediation is to upgrade to a patched SimpleHelp release: v5.5.8 or later, v5.4.10 on the 5.4 branch, or v5.3.9 on the 5.3 branch. For SimpleHelp servers that cannot be patched immediately, CISA (AA25-163A) recommends: (1) isolate the SimpleHelp server from the public internet or stop the server process; (2) change the SimpleHelp server Administrator password and all Technician account passwords; (3) restrict source IP addresses allowed to reach Technician/Administrator logins, API requests, and firewall connections; (4) disable the built-in SimpleHelpAdmin user and use an Administrator Technician account instead; (5) disable local Technician account logins and use Active Directory / LDAP authentication; (6) create new API tokens and revoke old ones; (7) configure Server Event alerts for Administrator logins, failed logins, and configuration changes; (8) add SimpleHelp binaries to endpoint security allowlists; (9) hunt for suspicious executables with three-letter filenames (e.g., aaa.exe) created after January 2025; (10) run host and network vulnerability scans; (11) for already-encrypted systems, disconnect from the internet, wipe, and rebuild from clean backups.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — Critical Vulnerability Exposes GitHub Agentic Workflows to Prompt Injection

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://www.securityweek.com/critical-vulnerability-exposes-github-agentic-workflows-to-prompt-injection/>

> Researchers show how attackers can use a crafted public GitHub Issue to trick AI-powered workflows into exposing data from private repositories without authentication. The post Critical Vulnerability Exposes GitHub Agentic Workflows to Prompt Injection appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** An indirect (agentic) prompt-injection vulnerability (dubbed 'GitLost') in GitHub Agentic Workflows. An unauthenticated attacker posts a crafted GitHub Issue to a public repository belonging to an organization that also owns private repositories. The issue's title and body contain hidden prompt-injection instructions (Noma Labs bypassed guardrails by appending the keyword 'Additionally' followed by a plausible-looking directive). When the organization's agentic workflow is triggered by the issue event (e.g., issues.opened or issues.assigned), it embeds the attacker-controlled issue text into the prompt of an AI agent (e.g., anthropics/claude-code-action, GitHub Copilot, or similar). The agent treats that untrusted user data as trusted instructions, fetches sensitive content such as README.md files from private repositories in the same organization, and exfiltrates it by posting it as a public comment on the issue — all without any authentication. The root cause is a failure to maintain a strict trust boundary between system-level directives and untrusted event/user data.
- **Affected Products:** GitHub Agentic Workflows (Public Preview, launched February 2026) — specifically agentic workflows that (a) read public input such as GitHub Issue titles/bodies, (b) hold access to private repositories in the same organization, and (c) can post output publicly (e.g., as issue/PR comments)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** No fully patched, version-tagged fix has been publicly released. Recommended hardening: (1) Treat all user-controlled content (issue title/body, PR descriptions, commit messages, comments) as untrusted input, never as instructions. (2) Scope agent permissions to the minimum required and avoid giving agents write/post privileges they do not strictly need. (3) Restrict what any agent can post publicly. (4) Sanitize or isolate user input from the instruction context before passing it to the model. (5) Restrict the toolset available to AI agents (e.g., remove gh issue edit/comment capabilities when not required). (6) Treat AI output as untrusted code; do not execute generated output without validation. (7) Restrict the blast radius of leaked GitHub tokens via IP allow-listing. (8) Use stable identifiers (e.g., issue.number) plus constrained commands (e.g., gh issue view) instead of directly interpolating github.event.issue.title or body. (9) Validate model-derived outputs against strict allowlists or typed schemas. (10) Apply human approval gates for sensitive actions. GitHub updated the documentation that originally created the flaw following responsible disclosure.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — CISA orders feds to prioritize patching Langflow auth bypass flaw

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-prioritize-patching-langflow-auth-bypass-flaw/>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) gave federal agencies until Friday to patch an actively exploited vulnerability in the Langflow visual framework for building AI agents. [...]

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-55255 is an Insecure Direct Object Reference (IDOR) vulnerability (CWE-639) in Langflow's POST /api/v1/responses endpoint. The endpoint accepts a flow UUID in the 'model' field and looks up the target flow via the helper function get_flow_by_id_or_endpoint_name() in helpers/flow.py, which queries the database by UUID without verifying that the authenticated caller owns that flow. As a result, any authenticated user who knows (or can enumerate, via /api/v1/flows/) another user's flow UUID can cause the victim's flow to be executed under their own credentials, exposing the victim's workflow logic, conversation/transcript data, and any API keys or sensitive context held by that flow. The vulnerability requires valid Langflow authentication (PR:L) but is exploitable over the network without user interaction, and successful exploitation changes the security scope (S:C).
- **Affected Products:** Langflow prior to version 1.9.1 (i.e., all Langflow versions < 1.9.1, including the 1.8.x line). The NVD entry describes the flaw as affecting versions prior to 1.9.2; the official Langflow security advisory and vendor fix (PR #12832) ship the patch in 1.9.1.
- **CVSS Score:** 9.9
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:L
- **Exploit Available:** true — Proof-of-concept exploit included in the official Langflow advisory (GHSA-qrpv-q767-xqq2) using a curl POST to /api/v1/responses with the victim's flow_id in the 'model' field. Public write-ups describing the exploit are also published at https://www.sysdig.com/blog/understanding-langflow-cve-2026-55255-and-why-higher-cvss-vulnerabilities-arent-always-the-most-exploited and https://www.mallory.ai/vulnerabilities/019ee281-978e-7851-b012-a0645d1d53ce.
- **Patch Available:** true — https://github.com/langflow-ai/langflow/security/advisories/GHSA-qrpv-q767-xqq2 (patch shipped in Langflow 1.9.1, fix commit/PR: https://github.com/langflow-ai/langflow/pull/12832).
- **Active Exploitation:** true — Confirmed active exploitation in the wild. CISA added CVE-2026-55255 to its Known Exploited Vulnerabilities (KEV) Catalog on 2026-07-07 with a federal-agency remediation due date of 2026-07-10 (https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-55255). The Sysdig Threat Research Team observed live exploitation on 2026-06-25 from IP 45.207.216.55 enumerating /api/v1/flows/ and triggering the IDOR with a 'leak api keys' prompt (https://www.sysdig.com/blog/understanding-langflow-cve-2026-55255-and-why-higher-cvss-vulnerabilities-arent-always-the-most-exploited). CrowdSec reported 18 distinct attacking IPs exploiting the flaw between 2026-04-09 and 2026-04-21 (https://www.crowdsec.net/vulntracking-report/cve-2026-21445-langflow-authentication-bypass-exploitation).
- **Threat Actors:** None known. Sysdig Threat Research Team characterized the threat actor as opportunistic and financially motivated (a single IP 45.207.216.55 was observed enumerating flow IDs and exfiltrating API keys with the prompt 'leak api keys'). CrowdSec tracked 18 distinct attacking IPs exploiting the flaw between April 9 and April 21, 2026, but did not attribute the activity to a named threat group.
- **Mitigation:** 1) Upgrade to Langflow version 1.9.1 or later (the official fix is PR #12832, which adds user-ownership verification in get_flow_by_id_or_endpoint_name). 2) Until the patch can be applied, restrict network exposure of the Langflow instance — place it behind a VPN, identity-aware proxy, reverse proxy enforcing authentication, or tightly scoped IP allowlist so the /api/v1/responses and /api/v1/flows/ endpoints are not reachable by untrusted authenticated users. 3) Audit existing Langflow deployments and rotate any API keys, secrets, or sensitive data stored in flows that may have been exposed via prior exploitation. 4) Monitor for anomalous POST requests to /api/v1/responses where the 'model' field value does not correspond to a flow owned by the authenticated user. CISA's Known Exploited Vulnerabilities catalog set the remediation due date for federal agencies as 2026-07-10 under BOD 26-04.
- **Vendor Advisory:** https://github.com/langflow-ai/langflow/security/advisories/GHSA-qrpv-q767-xqq2

---

## 4. 🟠 Zero-Day — CISA Adds 4 Actively Exploited Adobe, Joomla, and Langflow Flaws to KEV

**CVE:** `CVE-2026-48282` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://thehackernews.com/2026/07/cisa-adds-4-actively-exploited-adobe.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added four security flaws to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

The vulnerabilities are listed below -


  CVE-2026-48282 (CVSS score: 10.0) - A path traversal vulnerability in Adobe ColdFusion that could lead to arbitrary code execution in the context of the

**Parallel AI Enrichment:**

- **Technical Details:** An improper limitation of a pathname to a restricted directory ('path traversal') vulnerability exists in Adobe ColdFusion's Remote Development Services (RDS) module, specifically in the FILEIO handler at /CFIDE/main/ide.cfm?ACTION=FILEIO. The FileWriteOperator lacks proper path canonicalization and validation, allowing unauthenticated attackers (when RDS is enabled and authentication is disabled) to send a length-prefixed RPC POST request using the WRITE operator to write arbitrary files (e.g., a malicious .cfm webshell using <cfexecute>) to absolute paths or via directory traversal sequences (../, ..\\) into the ColdFusion web root (e.g., C:\\ColdFusion2025\\cfusion\\wwwroot\\). The attacker then accesses the uploaded file directly via the web server to trigger arbitrary code execution in the context of the current user.
- **Affected Products:** Adobe ColdFusion 2025 Update 9 and earlier (versions 2025.9 and earlier), Adobe ColdFusion 2023 Update 20 and earlier (versions 2023.20 and earlier)
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Exploit Available:** true (https://labs.watchtowr.com/its-37oc-and-all-we-can-think-about-is-coldfusion-adobe-coldfusion-security-bulletin-apsb26-68-cve-bonanza/)
- **Patch Available:** true (https://helpx.adobe.com/security/products/coldfusion/apsb26-68.html)
- **Active Exploitation:** true (https://www.cisa.gov/news-events/alerts/2026/07/07/cisa-adds-one-known-exploited-vulnerability-catalog; https://www.helpnetsecurity.com/2026/07/07/adobe-coldfusion-cve-2026-48282-exploitation-detected/; https://thehackernews.com/2026/07/cisa-adds-4-actively-exploited-adobe.html)
- **Threat Actors:** None known
- **Mitigation:** Upgrade to Adobe ColdFusion 2025 Update 10 or ColdFusion 2023 Update 21 (priority rating 1). If RDS is not required, disable the Remote Development Services module to eliminate the attack surface. Hunt for indicators of compromise including unauthorized .cfm, .cfc, .cfml, or .jsp files in the ColdFusion web root and /CFIDE/ directories, HTTP POST requests to /CFIDE/main/ide.cfm?ACTION=FILEIO, and probe/temporary marker files (e.g., .probe_*.txt).
- **Vendor Advisory:** https://helpx.adobe.com/security/products/coldfusion/apsb26-68.html

---

## 5. 🟠 Zero-Day — Critical Gitea Flaw Under Active Exploitation, Researchers Warn

**CVE:** `CVE-2026-20896` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://www.securityweek.com/critical-gitea-flaw-under-active-exploitation-researchers-warn/>

> Attackers are exploiting the critical Gitea vulnerability CVE-2026-20896 to bypass authentication with a single HTTP header and access vulnerable repositories and secrets. The post Critical Gitea Flaw Under Active Exploitation, Researchers Warn appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** The official Gitea Docker image ships an app.ini configuration template that hard-codes REVERSE_PROXY_TRUSTED_PROXIES = * (a wildcard meaning every source IP is treated as a trusted reverse proxy). When an administrator enables ENABLE_REVERSE_PROXY_AUTHENTICATION, Gitea trusts the X-WEBAUTH-USER HTTP header received from any source IP and uses it to log the request in as that user without a password, token, or other authentication factor. An unauthenticated remote attacker can therefore send a single crafted request to an internet-exposed Gitea instance with header X-WEBAUTH-USER: <username> (e.g., the built-in 'admin' user) to fully impersonate that account, including gaining administrative access to repositories, code, and stored secrets.
- **Affected Products:** Gitea Open Source Git Server Docker images (gitea/gitea) versions up to and including 1.26.2 (all Docker image versions prior to 1.26.3)
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true. A working proof-of-concept (poc.py) and checker (detect.py) are publicly available. Source: https://sploitus.com/exploit?id=0FC89D13-9196-52D2-AF79-402D089DB0F4
- **Patch Available:** true. Gitea released version 1.26.3 to address the vulnerability. Advisory: https://github.com/go-gitea/gitea/security/advisories/GHSA-f75j-4cw6-rmx4
- **Active Exploitation:** true. Confirmed active exploitation/probing in the wild. Sources: SecurityWeek (https://www.securityweek.com/critical-gitea-flaw-under-active-exploitation-researchers-warn/), The Hacker News (https://thehackernews.com/2026/07/threat-actors-probe-gitea-docker-flaw.html) — probing detected 13 days after public disclosure, SecurityAffairs (https://securityaffairs.com/194902/hacking/critical-gitea-docker-bug-under-active-exploitation-exposes-repositories-and-secrets.html).
- **Threat Actors:** None known. No named APT groups, ransomware operators, or campaigns have been publicly attributed. Researchers observed probing attempts (e.g., one probe from ProtonVPN exit IP 159.26.98[.]241) but no specific threat actor has been linked to exploitation.
- **Mitigation:** 1) Upgrade the Gitea Docker image to 1.26.3 or later, which removes the wildcard default. 2) On existing deployments, edit app.ini and replace the wildcard REVERSE_PROXY_TRUSTED_PROXIES = * with an explicit allow-list of your reverse proxy's IP/CIDR (e.g., REVERSE_PROXY_TRUSTED_PROXIES = 10.0.0.0/8,172.16.0.0/12,192.168.0.0/16). 3) If reverse-proxy authentication is not required, set ENABLE_REVERSE_PROXY_AUTHENTICATION = false. 4) Ensure the Gitea instance is not directly exposed to the internet without an authenticating reverse proxy in front of it. 5) Audit logs and repositories for unauthorized access by admin or other privileged accounts.
- **Vendor Advisory:** https://github.com/go-gitea/gitea/security/advisories/GHSA-f75j-4cw6-rmx4

---

## 6. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an LLM-powered application ingests untrusted external content (web pages, emails, documents, calendar entries, etc.) that contains adversarial instructions hidden inside ordinary-looking text, HTML attributes, images, or metadata. The model treats these attacker-supplied instructions as part of its prompt context and executes them — overriding or augmenting the legitimate user's intent. Attack vectors observed by Google include instructions not to crawl a page, lures that cause an agent to stream infinite text until timeout, SEO manipulation, experimental data exfiltration from the user's environment, and commands that attempt to delete files on the user's machine. Cross-app agentic features that can read from one source and act in another (e.g., Gemini reading an email or document and acting in Workspace) amplify impact.
- **Affected Products:** Gemini; Google Workspace (Gmail, Docs, Drive, Slides, Sheets via Gemini features such as "Help me write" and chat); Chrome Enterprise; AI agents and LLM-integrated applications generally. No specific product versions are cited in the Google Security Blog post.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — Public proof-of-concept demonstrations and weaponized exploits are publicly available, including a benign HTML-based PoC targeting MongoDB Atlas (https://github.com/brennanbrown/atlas-prompt-injection-poc) and SafeBreach Labs' indirect-prompt-injection exploit against the Gemini voice assistant (https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/).
- **Patch Available:** false — Indirect Prompt Injection is a class of attack against LLM-based systems rather than a single patched bug. Google has not released a single vendor patch that eliminates the class; defenses are mitigations and hardening (layered classifiers, guardrails, instruction tuning, red-team programs, VRP) rather than a code patch.
- **Active Exploitation:** true — Google's Threat Intelligence teams report real-world IPI abuse, including a 32% relative increase in the malicious category of prompt injections between November 2025 and February 2026. Unit 42 documents web-based IPI observed in the wild, and Mandiant (M-Trends 2026) notes red teams actively use prompt-injection techniques in real engagements. A prior concrete calendar-invite-based exfiltration bypass against Google Gemini is documented by Miggo.
- **Threat Actors:** None known. The Google Security Blog post and supporting industry reporting (Unit 42, Proofpoint, CrowdStrike, Mandiant) describe categories of adversaries — hackers, scammers, SEO manipulators, and red teams — but do not attribute Indirect Prompt Injection (IPI) abuse to any named APT group, ransomware operator, or tracked campaign.
- **Mitigation:** Google-recommended defenses: harden AI models and products, run dedicated red-team pressure testing, operate the AI Vulnerability Reward Program for external researchers, deploy a layered defense strategy, and process data at global scale to identify and neutralize threats. Workspace-specific mitigations: content classifiers, security guardrails, machine-learning defenses, instruction tuning, and model refinement. Industry-recommended controls (Unit 42, CrowdStrike, Proofpoint): human-in-the-loop for any critical/sensitive action, principle of least privilege for tool/API access, input validation and sanitization, a separate "evaluator" LLM to scan inputs/outputs, strict system-prompt layering/instructional separation, least-privilege data access for the assistant, monitoring/anomaly detection on model outputs, and user training.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 7. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is a vulnerability class targeting LLM-based applications such as Workspace with Gemini. An attacker embeds malicious natural-language instructions inside untrusted content that the LLM ingests as part of fulfilling a user's request — e.g., the body of an email, a Doc, a file in Drive, a web page, or any tool/output the agent processes. Because the LLM cannot reliably distinguish trusted system/user instructions from instructions smuggled in via retrieved data, the injected text can redirect the model's behavior (summarization, tool calls, data exfiltration, transactions, etc.) even when the user never typed anything malicious. Unit 42 has observed additional obfuscation variants — base64-encoded payloads decoded at runtime, visually hidden text via zero font size / CSS suppression / transparency, and semantic jailbreak phrasing — that defeat naive content filtering. The result is unauthorized actions performed by the AI agent under the user's identity.
- **Affected Products:** Google Gemini app; Google Workspace with Gemini including Gemini in Gmail, Gemini in Docs editors, Gemini in Drive, and Gemini in Chat (all current/continuously updated Gemini versions).
- **CVSS Score:** CVSS score unavailable. No CVSS v3.x base score has been publicly assigned to this vulnerability class.
- **CVSS Vector:** CVSS vector unavailable. Indirect prompt injection is treated as a class of vulnerability affecting LLM-based systems rather than a single CVE-trackable software flaw, and Google has not assigned a CVSS v3 vector for it.
- **Exploit Available:** true. Multiple public, real-world indirect prompt injection payloads and techniques have been published and are being actively used. Forcepoint X-Labs publicly disclosed 10 verified IPI payloads observed on live websites (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads, Apr 22, 2026). Unit 42 publicly documented 22 web-based IPI techniques observed in the wild, including a weaponized instance at reviewerpress[.]com targeting AI product-ad-review systems, base64-encoded instructions decoded at runtime, visually concealed prompts (zero-sized text, CSS suppression, transparency), and 'Ignore previous instructions' / PayPal- and Stripe-hijacking payloads (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/).
- **Patch Available:** false. Google has not released a discrete patch for indirect prompt injection because it is treated as a continuous, evolving threat class rather than a single bug; instead, layered mitigations are continuously deployed across Workspace with Gemini. The vendor advisory itself is the canonical reference: http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html
- **Active Exploitation:** true. Confirmed active exploitation in the wild. Unit 42 confirmed weaponized IPI activity in real-world telemetry including the reviewerpress[.]com ad-review bypass (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/). Forcepoint X-Labs documented 10 verified IPI payloads operating against production AI agents on live websites (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads, Apr 22, 2026). Google itself reported a 32% relative increase in malicious IPI activity between November 2025 and February 2026, as cited in Help Net Security (https://www.helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild/).
- **Threat Actors:** None known. No specific APT, cybercrime, or ransomware group is publicly attributed to indirect prompt injection attacks against Workspace with Gemini. Forcepoint X-Labs notes that the shared injection templates observed across multiple domains suggest 'organized tooling' rather than isolated experimentation, but no named campaign or actor has been identified.
- **Mitigation:** No single patch is available because IPI is a continuous, evolving threat class; Google explicitly states 'IPI is not the kind of technical problem you solve and move on.' Google's recommended approach is a layered defense-in-depth strategy that combines: (1) deterministic controls — a centralized Policy Engine enforcing URL sanitization, regex-based takedowns of known-bad patterns, tool-chaining policies, and a user-confirmation framework that requires explicit approval for sensitive actions; (2) ML-based defenses — prompt-injection content classifiers trained on synthetic variants of newly discovered attacks; (3) LLM-based defenses — iteratively refined system instructions ('security thought reinforcement') that remind the model to ignore adversarial directives; (4) Gemini model hardening — improving the underlying model's internal ability to recognize and discard harmful instructions in retrieved data; (5) markdown sanitization and suspicious-URL redaction via Google Safe Browsing; (6) end-user security-mitigation notifications when Gemini blocks a suspected attack; and (7) hardening guidance for developers per OWASP LLM01 (separation of untrusted content from system prompts, semantic firewalls, input/output filtering). Administrator reference: https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 8. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: an attacker plants adversarial instructions in web content that an agentic browser ingests (malicious sites, third-party iframes, user-generated content such as reviews). The Gemini-powered agent concatenates this untrusted content with the user's trusted instructions in the same token stream, causing it to take unintended, privileged actions (e.g., initiating financial transactions, exfiltrating data). Variants include: (1) GeminiJack - RAG poisoning of Google Gemini Enterprise/Vertex AI Search via shared Google Docs, Calendar invites, and emails; the AI retrieves poisoned content and exfiltrates data through disguised HTTP requests. (2) CVE-2026-0628 - a Chrome extension using the declarativeNetRequest API injects scripts/HTML into the privileged Gemini panel. (3) Unit 42 observed Base64 encoding, dynamic execution, timed delays, CSS rendering suppression, SEO-poisoned footers, and JavaScript-based payloads.
- **Affected Products:** Google Chrome with Gemini in Chrome agentic capabilities; CVE-2026-0628 affects Google Chrome prior to 143.0.7499.192 on desktop (Windows/Mac/Linux) via WebView tag; GeminiJack affects Google Gemini Enterprise and Google Vertex AI Search.
- **CVSS Score:** CVSS score unavailable. NVD has not yet published a numeric CVSS for the related CVE-2026-0628 (Chromium severity rated 'High'); the advisory itself does not carry a CVE/CVSS.
- **CVSS Vector:** CVSS vector unavailable. No CVE has been assigned to the indirect prompt injection architectural issue in the Dec 8, 2025 Google advisory, and the related CVE-2026-0628 NVD entry shows 'N/A - assessment not yet provided'.
- **Exploit Available:** true. Public proof-of-concept code is available at https://github.com/brennanbrown/atlas-prompt-injection-poc. Noma Labs published a zero-click GeminiJack PoC for Google Gemini Enterprise/Vertex AI Search (https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability).
- **Patch Available:** true. The new agentic security architecture is being shipped by Google to Chrome. The related CVE-2026-0628 was patched in Chrome 143.0.7499.192 (January 2026 Desktop stable channel). Primary advisory: http://security.googleblog.com/2025/12/architecting-security-for-agentic.html.
- **Active Exploitation:** true. (a) Noma Labs publicly demonstrated a working zero-click GeminiJack exploit against Google Gemini Enterprise/Vertex AI Search on Dec 8-9, 2025 (https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability). (b) Unit 42 documented real-world indirect prompt injection campaigns actively observed in the wild in December 2025 (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection). (c) Unit 42 reported CVE-2026-0628 being quickly patched after discovery (https://unit42.paloaltonetworks.com/gemini-live-in-chrome-hijacking).
- **Threat Actors:** None known. No specific APT, ransomware operator, or threat actor group is named. Unit 42 has publicly documented four real-world indirect prompt injection campaign patterns observed in December 2025, but none are attributed to a named actor.
- **Mitigation:** Google's layered defenses: (1) User Alignment Critic - isolated high-trust LLM vetting every agent action; (2) Agent Origin Sets - restricts agent to relevant origins partitioned into read-only and read-writable sets; (3) mandatory user confirmations for sensitive sites and actions; (4) prompt-injection classifier running in parallel with planning model; (5) 'Spotlighting' to prioritize user/system instructions over page content; (6) automated red-teaming. Hardening: keep Chrome updated (CVE-2026-0628 fixed in Chrome 143.0.7499.192), install only trusted extensions, and treat Gemini-in-Chrome agentic actions involving authentication/payments/data movement as requiring explicit user confirmation.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 9. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2025-48530 is a linear buffer overflow / out-of-bounds read (CWE-125) in the Rust-based CrabbyAVIF AVIF image decoder included with the Android System component. In multiple locations within the decoder, incorrect bounds checks allow OOB accesses on the NV12/YUV planes (Y plane, UV planes, alpha plane) and in chroma-width calculations when parsing maliciously crafted AVIF images. It can be chained with other bugs to achieve remote code execution without additional execution privileges and without user interaction. Google's Scudo hardened allocator deterministically rendered the issue non-exploitable in practice by placing guard pages around secondary allocations, converting the silent memory corruption into a noisy crash.
- **Affected Products:** Google Android 16 (System component, platform/external/rust/crabbyavif AVIF decoder package); versions prior to security patch level 2025-08-05 (August 2025 update)
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true (https://source.android.com/security/bulletin/2025-08-01)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the August 2025 Android Security Bulletin patches immediately (security patch level 2025-08-05 or later) to all affected Android 16 devices. Where patching is delayed, limit network exposure of affected devices, implement network segmentation, enforce strict inbound firewall rules, deploy mobile device management (MDM) policies, and configure alerts for system service crashes or restarts that may indicate attempted exploitation.
- **Vendor Advisory:** https://source.android.com/security/bulletin/2025-08-01

---

## 10. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is an AI-specific attack class in which an attacker embeds hidden natural-language instructions inside external content (emails, documents, calendar invites, web pages) that a large language model later retrieves and processes. When Gemini ingests that content, the hidden instructions are concatenated into the model prompt and can cause the model to deviate from the user's intent — for example, exfiltrating user data, generating attacker-controlled phishing content, or invoking connected tools/agents without consent. This is distinct from direct prompt injection (where the attacker types malicious instructions directly into the prompt) because the attacker channel is content the user (not the attacker) chose to consume. LLM-as-agent flows introduce additional side channels such as markdown rendering and image preview that enable zero-click data exfiltration, as demonstrated by the EchoLeak (CVE-2025-32711) zero-click chain against Microsoft 365 Copilot which the Google blog cites as a motivating example.
- **Affected Products:** Gemini 2.5 models, Gemini app, Gemini in Google Workspace (Gmail, Google Docs, Google Drive, Google Chat, Google Calendar)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true — PoCs include EchoLeak (CVE-2025-32711) referenced in the blog (https://arxiv.org/html/2509.10540v1), 'Invitation Is All You Need' against Gemini for Workspace (https://sites.google.com/view/invitation-is-all-you-need/home), and SafeBreach Labs' Gemini voice-assistant exploit (https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/)
- **Patch Available:** true — http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html (mitigations deployed as model-side and product-side defenses rather than a traditional downloadable patch)
- **Active Exploitation:** false — no confirmed in-the-wild exploitation of Gemini via indirect prompt injection has been reported. Research-grade PoCs exist (EchoLeak, 'Invitation Is All You Need', SafeBreach voice-assistant exploit), but these are controlled demonstrations. For the closely related EchoLeak (CVE-2025-32711) referenced in the blog, Microsoft and Aim Security confirmed no in-the-wild exploitation before the May 2025 server-side fix.
- **Threat Actors:** None known
- **Mitigation:** Google documents a six-layer defense-in-depth strategy applied across Gemini 2.5, the Gemini app, and Gemini in Workspace: (1) Model hardening via adversarial training; (2) Prompt-injection content classifiers (XPIA-style) that scan incoming emails, files, and external content before they reach the model; (3) 'Security thought reinforcement' — system instructions steering the model to ignore adversarial instructions; (4) Markdown sanitization and suspicious-URL redaction integrated with Google Safe Browsing to neutralize EchoLeak-style payloads; (5) Human-in-the-Loop user confirmation for sensitive actions (e.g., deleting calendar events, sending messages, modifying settings); (6) End-user security mitigation notifications (banners and help-center links) when an attack is detected and blocked. Additional Workspace admin guidance is published at https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 11. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

---

## 12. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 13. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

---

## 14. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 15. 🟠 Zero-Day — CrowdStrike Uncovers New Prompt Injection Techniques

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jul 07, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-uncovers-new-prompt-injection-techniques/>

---

## 16. 🟠 Zero-Day — CISA orders feds to patch max severity ColdFusion flaw by Friday

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-max-severity-coldfusion-flaw-by-friday/>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has ordered government agencies to patch an actively exploited maximum-severity flaw in the Adobe ColdFusion commercial web app development platform by Friday. [...]

---

## 17. 🟠 Zero-Day — Chinese hackers develop LONGLEASH malware to expand ORB network

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://www.bleepingcomputer.com/news/security/chinese-hackers-develop-longleash-malware-to-expand-orb-network/>

> Chinese hackers tracked as &#x27;UAT-7810&#x27; are actively evolving their malware to expand their Operational Relay Box (ORB) network by compromising internet-facing networking devices, primarily unpatched Ruckus routers. [...]

---

## 18. 🟡 High Severity — 15-Year-Old GhostLock Flaw Enables Root and Container Escape on Most Linux Distros

**CVE:** `CVE-2026-43499` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://thehackernews.com/2026/07/15-year-old-ghostlock-flaw-enables-root.html>

> Researchers at Nebula Security have disclosed GhostLock (CVE-2026-43499), a 15-year-old Linux kernel flaw that lets any logged-in user take full root control of a machine that has not been patched.

The vulnerable code has shipped by default in essentially every mainstream distribution since 2011. The flaw needs no special permission, no unusual settings, and no network

---

## 19. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
