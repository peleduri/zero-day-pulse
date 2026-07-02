# Zero Day Pulse

> **Generated:** 2026-07-02 08:42 UTC &nbsp;|&nbsp; **Total:** 36 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 13 &nbsp;|&nbsp; 🟡 High: 23 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is an unauthenticated path-traversal vulnerability (CWE-22) in the WebDownloadServer servlet of SimpleHelp's /toolbox-resource/ HTTP endpoint. The respondToolboxResource method in WebDownloadServer.class does not sufficiently sanitize path components, allowing an attacker to use ../ sequences (e.g., GET /toolbox-resource/<validItem>/../secmsg/../../configuration/serverconfig.xml or ../../../../../../etc/passwd) to read arbitrary files on the SimpleHelp host with the privileges of the SimpleHelp server process. Sensitive files reachable include configuration/serverconfig.xml (containing the SimpleHelpAdmin hashed password, LDAP credentials, OAuth/OIDC client secrets, API keys, and TOTP seeds) and serverkeys.dat, plus arbitrary OS files such as /etc/passwd and /root/.ssh/id_rsa. Because no authentication is required, the bug is network-exploitable at low attack complexity. When chained with CVE-2024-57728 (authenticated arbitrary file upload), it yields pre-auth remote code execution.
- **Affected Products:** SimpleHelp Remote Support (RMM) software — versions 5.5.7 and earlier (including the 5.4.x branch prior to 5.4.10, and the 5.3.x branch prior to 5.3.9). Fixed in 5.5.8, 5.4.10, and 5.3.9 respectively.
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true — Public PoC and weaponized exploit exist. Sources: (1) Rapid7 Metasploit module (https://github.com/rapid7/metasploit-framework/blob/master/modules/auxiliary/scanner/http/simplehelp_toolbox_path_traversal.rb); (2) Horizon3.ai disclosure (https://www.horizon3.ai/attack-research/disclosures/critical-vulnerabilities-in-simplehelp-remote-support-software/); (3) OffSec write-up with sample request (https://www.offsec.com/blog/cve-2024-57727).
- **Patch Available:** true — Patch was released by SimpleHelp between January 8–13, 2025. Vendor advisory: https://simple-help.com/kb---security-vulnerabilities-01-2025 ; supporting blog: https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know
- **Active Exploitation:** true — Confirmed active, in-the-wild exploitation. CISA Advisory AA25-163A (June 12, 2025) documents DragonForce ransomware actors exploiting unpatched SimpleHelp instances to compromise a U.S. utility billing software provider and its downstream customers in double-extortion attacks since January 2025 (https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a). Independent corroboration: Sophos MDR report on DragonForce targeting SimpleHelp at an MSP (May 27, 2025); Arctic Wolf observed in-the-wild SimpleHelp initial-access campaign from January 22, 2025; Halcyon report on continued DragonForce exploitation (June 24, 2025).
- **Threat Actors:** DragonForce — a ransomware-as-a-service (RaaS) operation. CISA's AA25-163A advisory (June 12, 2025) attributes double-extortion compromises of a U.S. utility billing software provider and its downstream customers to DragonForce actors leveraging unpatched SimpleHelp RMM (and likely CVE-2024-57727). Independently corroborated by Sophos MDR, Arctic Wolf (initial-access campaign from January 22, 2025), and Halcyon (June 24, 2025 report).
- **Mitigation:** 1. Upgrade SimpleHelp server immediately to v5.5.8 (or current latest release); for 5.4.x branches upgrade to 5.4.10, and for 5.3.x branches upgrade to 5.3.9. 2. If unable to patch immediately, isolate the SimpleHelp server from the internet or stop the server process. 3. Determine SimpleHelp version by issuing an HTTP GET to /allversions (e.g., https://<host>/allversions) and inspect <SimpleHelp>/configuration/serverconfig.xml. 4. Threat-hunt for suspicious executables with three-alphabetic-character filenames (e.g., aaa.exe, bbb.exe) created since January 2025; perform full host and network vulnerability scans. 5. For embedded/bundled instances within third-party software (e.g., utility billing), third-party vendors must also identify the server version, isolate it, upgrade, and notify downstream customers. 6. Encrypted/ransomware-impacted systems should be disconnected, wiped from clean installation media, and restored from known-good offline backups. 7. Maintain offline backups, asset inventory, and avoid exposing remote services (RDP, RMM) directly to the internet with compensating controls.
- **Vendor Advisory:** https://simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — Rancher Fleet vulnerable to cross namespace secret disclosure via unvalidated `valuesFrom` references in Helm Deployer

**CVE:** `CVE-2026-44935` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-xr65-5cpm-g36x>

> ### Impact
A vulnerability in Fleet for Rancher Manager affects multi-tenancy environments where different tenants share the same downstream clusters (e.g., different privileged or untrusted teams inside the same organization). 

On unpatched versions, tenants could bypass restrictions to access any config map or secret across all namespaces on the downstream cluster. They can create cluster-wide …

**Parallel AI Enrichment:**

- **Technical Details:** In Rancher Fleet's Helm Deployer, the `valuesFrom` field in `fleet.yaml` (delivered through a `GitRepo` resource) and the `HelmOp` resource are not validated against the calling tenant's authorization. A tenant can therefore (1) read arbitrary ConfigMaps and Secrets from ANY namespace on a downstream cluster — bypassing the namespace/ServiceAccount restrictions intended to enforce multi-tenant isolation — if they know or can guess the resource name, namespace, and key; and (2) create cluster-wide `HelmOp` or `Bundle` resources via the Fleet agent without being restricted to a specific ServiceAccount. The root cause is missing authorization checks (CWE-863: Incorrect Authorization) on cross-namespace Helm value references in the Helm Deployer, ignoring ServiceAccount impersonation that should bound a tenant to their own namespace.
- **Affected Products:** Rancher Fleet: versions >=0.12.0 and <0.12.15, >=0.13.0 and <0.13.11, >=0.14.0 and <0.14.6, >=0.15.0 and <0.15.2; SUSE Rancher Manager: all versions prior to v2.14.2 that bundle the affected Fleet versions
- **CVSS Score:** 9.9
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true — Patched Rancher Fleet versions are v0.12.15, v0.13.11, v0.14.6, and v0.15.2. The vendor advisory confirms these releases: https://github.com/advisories/GHSA-xr65-5cpm-g36x (referenced from SUSE Rancher Manager v2.14.2 release notes at https://documentation.suse.com/cloudnative/rancher-manager/v2.14/en/release-notes/v2.14.2.html).
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Upgrade Rancher Fleet to a patched version: v0.12.15, v0.13.11, v0.14.6, or v0.15.2. For Docker-installed or downstream Rancher deployments, upgrade to SUSE Rancher Manager v2.14.2 (or any later release) which bundles the patched Fleet. As a short-term hardening step, ensure no two tenants share the same downstream cluster (i.e., provide separate downstream clusters per tenant). Review downstream-cluster logs and audit history for cross-namespace `valuesFrom` references and rotate any service accounts / credentials that could have been exposed.
- **Vendor Advisory:** https://github.com/advisories/GHSA-xr65-5cpm-g36x

---

## 3. 🟠 Zero-Day — Unpatched Argo CD Repo-Server Flaw Could Let Attackers Take Over Kubernetes Clusters

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://thehackernews.com/2026/07/unpatched-argo-cd-repo-server-flaw.html>

> Argo CD, a widely used tool for deploying software to Kubernetes, has an unpatched flaw in its repo-server component that lets an unauthenticated attacker run code, provided they can reach the component&#x27;s internal network port.

Synacktiv, which found the bug, says it can lead to a full cluster takeover. There is no fix and no CVE. The firm says it reported the flaw to Argo CD&#x27;s maintain…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability exists in Argo CD's `repo-server` gRPC service on internal port 8081. The `/repository.RepoServerService/GenerateManifest` endpoint accepts a `ManifestRequest` containing `KustomizeOptions`, which is forwarded unsanitized as flags to the `kustomize` binary via `os/exec`. By using `--enable-helm` with `--helm-command ./exfil.sh` (where the script resides in an attacker-controlled Git repository Argo CD has cloned), the unauthenticated caller achieves arbitrary code execution on the repo-server host. From the initial RCE, the attacker reads the `REDIS_PASSWORD` env var, connects to the unauthenticated internal Redis manifest cache, poisons cached deployment data so the next automatic sync deploys an attacker-supplied workload, resulting in full Kubernetes cluster takeover. Synacktiv verified the attack end-to-end against v2.13.3.
- **Affected Products:** Argo CD repo-server (demoed against v2.13.3); full affected version range not publicly disclosed by Synacktiv. The vulnerable code is in `GenerateManifest` in `kustomize.go`, meaning any version exposing that gRPC surface with kustomize-with-helm integration is presumed at risk.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** No vendor patch available. Compensating controls: (1) Apply Kubernetes NetworkPolicies restricting traffic to the argocd-repo-server gRPC port 8081 and the Redis port so only Argo CD components can reach them. (2) Enable network policies in the Helm chart by setting `networkPolicy.create=true` in values.yaml. (3) Verify with `kubectl get networkpolicy -A`. (4) Defense-in-depth: ensure untrusted workloads cannot run in the cluster, restrict which repositories are registered as Argo CD sources, and protect Redis from any non-Argo-CD component.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — Critical Cursor Flaws Could Let Prompt Injection Escape Sandbox and Run Commands

**CVE:** `CVE-2026-50548` | `CVE-2026-50549` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://thehackernews.com/2026/07/critical-cursor-flaws-could-let-prompt.html>

> Two flaws in Cursor, an AI code editor, could let a single, ordinary-looking prompt break out of the editor&#x27;s safety sandbox and run any command on a developer&#x27;s computer. There is no click to fall for and no approval box to ignore.

Cato AI Labs found the pair and named them DuneSlide. They are tracked as CVE-2026-50548 and CVE-2026-50549, both rated 9.8 out of 10 (or 9.3

**Parallel AI Enrichment:**

- **Technical Details:** Cursor's AI agent runs terminal commands inside a sandbox scoped to the project working directory. CVE-2026-50548 abuses the agent-controllable 'working_directory' parameter of run_terminal_cmd: the sandbox blindly grants write access to whatever path the agent specifies, letting a prompt-injected agent write outside the workspace. CVE-2026-50549 abuses Cursor's path canonicalization: if canonicalization of a target path fails (e.g., target unreadable or non-existent), Cursor falls back to the original symlink path and writes through it without approval, so an in-workspace symlink pointing outside the workspace can be used to write anywhere. Both can be chained to overwrite the Cursor-installed cursorsandbox helper, after which subsequent agent commands execute fully unsandboxed under the developer's user privileges. Delivery is zero-click: instructions are planted in content the agent reads (web search results, MCP servers, poisoned repository content), so the developer only needs to issue a normal-looking prompt.
- **Affected Products:** Cursor (desktop AI code editor) versions prior to 3.0 (i.e., Cursor 2.x and earlier)
- **CVSS Score:** 9.3
- **CVSS Vector:** CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N
- **Exploit Available:** false
- **Patch Available:** true (upgrade to Cursor 3.0; advisory URLs: https://github.com/cursor/cursor/security/advisories/GHSA-3p48-7v9f-v5cw and https://github.com/cursor/cursor/security/advisories/GHSA-3v8f-48vw-3mjx)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Upgrade to Cursor 3.0 or later. Until upgrading, restrict which Model Context Protocol (MCP) servers and web sources the agent can reach, treat all external content ingested by the agent (web results, MCP server output, repository contents) as untrusted input, and avoid running agent commands that target the Cursor install directory (e.g., /Applications/Cursor.app on macOS).
- **Vendor Advisory:** https://github.com/cursor/cursor/security/advisories/GHSA-3p48-7v9f-v5cw ; https://github.com/cursor/cursor/security/advisories/GHSA-3v8f-48vw-3mjx

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an AI system ingests external content (web pages, emails, documents, calendar invites, search snippets, or data retrieved via RAG/plugin/tool calls) containing hidden adversarial instructions that override the user's original intent. When the model reads the poisoned content, it may silently follow attacker commands (data exfiltration, tool misuse, content suppression, malicious actions). Google's GTIG observed on-page IPI attempts in five categories: harmless pranks, helpful guidance, SEO manipulation, deterring AI agents, and outright malicious payloads (including exfiltration and destruction-class instructions like 'sudo rm -rf'). A 32% relative increase in the malicious category was observed between November 2025 and February 2026, indicating the threat is maturing.
- **Affected Products:** Google Gemini (including Gemini 2.5 models), Google Workspace with Gemini (Gemini in Gmail, Docs, Calendar, Drive), AI assistants/AI agents that browse and summarize external content, GitHub Copilot, Cursor, Claude Code, coding/CI assistants, AI-powered ad-review and search pipelines, Chrome's Gemini in Chrome side panel (CVE-2026-0628, separately patched), Google Gemini Enterprise / Vertex AI Search. Specific version numbers are not enumerated in the blog post.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true - https://bughunters.google.com/blog/task-injection-exploiting-agency-of-autonomous-ai-agents, https://swisskyrepo.github.io/PayloadsAllTheThings/Prompt%20Injection/, https://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads, https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/
- **Patch Available:** false - No single-CVE patch is associated with this research blog. However, mitigations include continuous Gemini 2.5 model hardening (in production), prompt-injection content classifiers (rolling out), and Google's continuous Workspace mitigation program. Related: https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html , https://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html
- **Active Exploitation:** true - Confirmed by Google GTIG (32% increase in malicious IPI category Nov 2025-Feb 2026), Forcepoint X-Labs (10 verified in-the-wild IPI payloads on public web infrastructure), Unit 42 (first observed AI-based ad-review bypass), and Noma Labs' GeminiJack disclosure. Sources: https://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html , https://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads , https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/ , https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability
- **Threat Actors:** None known
- **Mitigation:** Google's published layered defense strategy: (1) Model hardening via adversarial-data training for Gemini 2.5 models; (2) Prompt-injection content classifiers — proprietary ML detectors that scan emails/files for malicious instructions; (3) Security thought reinforcement — system-level instructions steering the model to ignore adversarial commands; (4) Markdown sanitization and suspicious URL redaction — defeats zero-click image-rendering exfiltration; (5) Human-in-the-Loop (HITL) / user confirmation framework for risky tool actions; (6) End-user security notifications when defenses block an attack; (7) Workspace-aware mitigations including red-teaming + AI VRP, synthetic-data generation (Simula), and a stack of deterministic/ML/LLM-based defenders with iterative Gemini model hardening.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is a semantic attack on LLM-based assistants in which the adversary plants malicious natural-language instructions inside data sources the model retrieves as context (web pages, Gmail messages, Google Calendar event descriptions, shared Google Docs/Slides/Sheets, code comments, RAG documents). When the user asks Workspace-with-Gemini to summarize, search, or act on that content, the model conflates adversary-controlled text with the legitimate system/user prompt and follows the injected instructions instead. Demonstrated impact includes: (a) zero-click exfiltration of Gmail mail, Calendar meetings and Docs via an injected prompt asking the LLM to embed Workspace content inside an <img src=ATTACKER/image.svg?x=> tag (Noma Labs 'GeminiJack'); (b) bypassing Gemini's privacy controls so summaries of private meetings are written into an attacker-visible Calendar event via the Calendar.create tool (Miggo 'Weaponizing Calendar Invites'); (c) web-page-borne IPI that hides payloads via display:none, off-screen positioning, near-transparent text, HTML comments, meta tags or 'ULTRATHINK' persuasion strings to coerce AI browsers/agents into executing commands, exfiltrating API keys, manipulating payments, or wiping data (Forcepoint X-Labs). IPI works without any malicious input directly from the victim and is increasingly relevant as Gemini gains tool-calling and agentic capabilities.
- **Affected Products:** Google Workspace with Gemini (Gmail, Google Calendar, Google Docs integration); Google Gemini Enterprise (Datastore/RAG) - affected by Noma Labs 'GeminiJack' prior to Google's fix in late 2025; Google Vertex AI Search - same GeminiJack disclosure. Specific version numbers are not published in the Google blog.
- **CVSS Score:** CVSS score unavailable. The NVD entry for the related CVE-2025-54131 (Cursor) lists metrics as 'N/A'; no CVSS base score has been published for Workspace-with-Gemini IPI scenarios.
- **CVSS Vector:** CVSS vector unavailable. Indirect prompt injection is a semantic, class-of-attack problem; Google has not published a CVSS v3 vector. The closest related CVE (CVE-2025-54131) is for the Cursor IDE - unrelated to Gemini Workspace.
- **Exploit Available:** true - https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads (10 in-the-wild IPI payloads, Apr 22, 2026); https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/ (GeminiJack sample payload that exfiltrates Workspace data via img src); https://www.miggo.io/post/weaponizing-calendar-invites-a-semantic-attack-on-google-gemini (calendar-invite IPI PoC, Jan 19, 2026); https://sites.google.com/view/invitation-is-all-you-need/home (SafeBreach 'Invitation Is All You Need').
- **Patch Available:** true - http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html. Google's continuous mitigation program has shipped layered defenses (user confirmation, URL sanitization, tool-chaining policies, regex takedowns, retrained ML classifiers, refined system prompts, model hardening) for Workspace with Gemini. In addition, Google fixed the specific Gemini Enterprise / Vertex AI Search issue disclosed by Noma Labs ('GeminiJack') in late 2025.
- **Active Exploitation:** true. Exploitation has been confirmed in the wild and via security research: (1) Forcepoint X-Labs documented 10 distinct indirect prompt injection payloads observed live on real websites across diverse verticals (API-key theft, brand-poisoning, traffic hijacking, data destruction via 'sudo rm -rf', AI-crawler donation scams); (2) Help Net Security reports that IPI is 'taking hold in the wild' with shared injection templates across multiple domains; (3) Noma Labs demonstrated a working zero-click exploit (GeminiJack) against production Gemini Enterprise and Vertex AI Search in 2025, fixed by Google in late 2025; (4) Miggo demonstrated practical exfiltration of private Calendar summaries via a single crafted Calendar invite. The Google Security Blog itself characterizes IPI as 'an evolving threat vector' that 'cannot be solved and moved on from,' corroborating its ongoing operational relevance.
- **Threat Actors:** None known. The Google/Mandiant GTIG 'AI Threat Tracker' (Feb 12, 2026) names APT31, APT41, APT42, UNC795, UNC6418, Temp.HEX, and HONESTCUE, but only as actors who used Gemini as a productivity/tradecraft tool (intelligence-gathering queries, code-generation, malware development), not as having exploited indirect prompt injection as an attack vector against Workspace-with-Gemini users.
- **Mitigation:** Google's continuous mitigation program for Workspace with Gemini layers: (1) Deterministic defenses - user confirmation prompts before sensitive tool actions, URL/link sanitization in retrieved content, and strict tool-chaining policies that constrain which tools can be invoked from which sources; (2) regex takedowns of known IPI payload patterns; (3) ML-based defenses retrained on synthetic IPI data; (4) LLM-level defenses using prompt engineering with refined system instructions to keep the model's task and the retrieved context separate; (5) model-level 'hardening' to improve Gemini's intrinsic ability to detect and ignore harmful instructions in retrieved data. For researcher-reported instances in Gemini Enterprise / Vertex AI Search, Google shipped a dedicated fix in late 2025. General hardening advice for defenders: enforce human-in-the-loop confirmation for any action that crosses a trust boundary (sending mail, creating calendar events, deleting files, executing shell commands), strip/quote untrusted content before it reaches the LLM, isolate tool credentials per source, monitor LLM outputs for data-leak patterns (e.g., embedded URLs, image tags, base64 blobs) and deploy URL-reputation scanning on any URL the model requests.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IDPI) - malicious instructions embedded in web content (malicious sites, third-party iframe content, or user-generated content such as reviews) are ingested by the Gemini-in-Chrome agent and treated as legitimate instructions, causing it to take unwanted actions such as initiating financial transactions or exfiltrating sensitive data. Attack techniques include CSS/HTML hiding (font-size:0, opacity:0, display:none, aria-hidden, visually-hidden classes), hidden white-text instructions, payload splitting across a document (e.g., a resume), multimodal injection (text hidden in images), adversarial-suffix strings, multilingual/obfuscated/Base64 payloads, RAG poisoning of documents an agent later retrieves, and 'memory poisoning' when the agent compresses information across origins. OWASP catalogs the class as LLM01:2025 Prompt Injection.
- **Affected Products:** Google Chrome with 'Gemini in Chrome' agentic capabilities on macOS, Windows, and selective ChromeOS devices; related agentic browsers also affected by the same class: ChatGPT Atlas, Claude for Chrome, Perplexity Comet. Specific Chrome version numbers are not stated in the source blog post.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true - PoC at https://github.com/brennanbrown/atlas-prompt-injection-poc; real-world payloads documented by Unit 42 (reviewerpress[.]com) and Forcepoint X-Labs (10 in-the-wild IPI payloads); UW June 2026 lab PoC against Chrome with Gemini.
- **Patch Available:** true - delivered via Chrome's auto-update mechanism (http://security.googleblog.com/2025/12/architecting-security-for-agentic.html). Not a standalone CVE patch.
- **Active Exploitation:** true for indirect prompt injection broadly; not separately confirmed for Chrome-with-Gemini in production. Unit 42 (Mar 2026) confirmed a real-world IDPI instance in December 2025; Forcepoint X-Labs (Apr 2026) found 10 IPI payloads deployed on live websites; Noma Labs disclosed GeminiJack zero-click attack (Dec 2025); UW study (Jun 2026) reproduced attack conditions against Chrome with Gemini in a lab setting, but no production in-the-wild targeting of Chrome-with-Gemini users is publicly documented.
- **Threat Actors:** None known
- **Mitigation:** Google's six layered defenses for Chrome agentic browsing (shipped via auto-update, not just recommendations): (1) User Alignment Critic - a second, isolated Gemini model that vets each proposed agent action against the user's stated goal before execution; (2) Agent Origin Sets - extends Site Isolation/same-origin policy so the agent can only access data from task-related origins; (3) User Confirmations - deterministic + model-based confirmation prompts before visiting sensitive sites (banking, healthcare), signing in via Google Password Manager, or completing purchases; (4) Spotlighting - techniques that bias the model to prefer system/user instructions over page content; (5) Real-time Prompt-Injection Classifier - runs in parallel with planning model and blocks adversarial actions; (6) URL/Origin Restrictions for Model-Generated URLs - deterministic allow-list to known public URLs. Plus Chrome's Safe Browsing and on-device scam detection. User hardening: avoid pasting untrusted web content into agent tasks; keep Chrome auto-updated.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Linear buffer overflow (CWE-125 OOB access) in CrabbyAVIF, Android's Rust-based AVIF image decoder, caused by incorrect bounds checks in multiple locations of `unsafe` Rust code. In theory, could lead to remote code execution with no privileges and no user interaction. In practice, Google's Scudo hardened allocator (deployed on Pixel and most modern Android devices) used guard pages around secondary allocations to transform the overflow into a deterministic crash rather than exploitable memory corruption. Google describes it as a 'near-miss' — the first Rust-based memory safety vulnerability in Android, caught before the affected code shipped to public releases.
- **Affected Products:** Google Android (CrabbyAVIF Rust-based AVIF decoder at platform/external/rust/crabbyavif); Android Security Patch Level 2025-08-05
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true (https://source.android.com/docs/security/bulletin/2025-08-01; Android Security Patch Level 2025-08-05)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply Android Security Patch Level 2025-08-05 or later. The official fix is in the August 2025 Android Security Bulletin. Defensive layers that reduced real-world exploitability: Scudo hardened allocator with guard pages (default on Pixel and most modern Android devices). Recommended hardening: continue migrating memory-unsafe code to safe Rust where possible; audit `unsafe` Rust code paths that handle untrusted image parsing; require the Comprehensive Rust training module on reasoning about unsafe Rust; keep CrabbyAVIF (`platform/external/rust/crabbyavif`) up to date with the latest AOSP commits.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is a class of attack against LLM-driven assistants in which an adversary embeds adversarial natural-language instructions inside external content (emails, document bodies, shared Drive files, Calendar invites, web pages, or notifications) that the assistant later ingests. When the user asks Gemini to summarize, search, or act on that content, the model concatenates the external content with the system prompt and may execute the embedded instructions alongside or in place of the legitimate user task. Documented payload goals include calendar-meeting exfiltration (Miggo, 2026-01), unauthorized financial transactions, API-key/OAuth-token theft via injected tool calls, voice-channel 'Fake Context Alignment' against Gemini Live on Android (SafeBreach, 2025-08), output hijacking, and remote code execution/data destruction. Bypass primitives observed include foreign-language payload smuggling, muted hyperlink embedding, markdown/reference-style link abuse, and auto-fetched images from CSP-permitted domains.
- **Affected Products:** Gemini app; Gemini in Google Workspace (Gmail, Docs, Drive, Chat); Gemini 2.5 models. Specific downstream exploit surfaces included Gemini Voice/Gemini Live on Android (SafeBreach disclosure 2025-08-17) and Gemini's Calendar integration (Miggo Security disclosure 2026-01-19). The companion EchoLeak vulnerability (CVE-2025-32711) affects Microsoft 365 Copilot and is explicitly noted as not applicable to Gemini.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true. Multiple public PoCs and weaponized payloads exist: SafeBreach 'Fake Context Alignment' exploit against Gemini Voice (https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/); Miggo Security calendar-invite exfiltration PoC against Gemini (https://thehackernews.com/2026/01/google-gemini-prompt-injection-flaw.html); 0din.ai 'Phishing for Gemini' research (https://0din.ai/blog/phishing-for-gemini); Forcepoint X-Labs 10 live IPI payloads across financial-fraud, API-key exfiltration, output hijacking, and data-destruction (https://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads).
- **Patch Available:** true. Google's IPI mitigations are continuously deployed inside Gemini and Gemini in Workspace (this is the patch for the class). Subsequent specific Gemintern PoCs were addressed: Miggo Security's Gemini calendar-invite exfiltration flaw was patched following responsible disclosure (disclosure 2026-01-19); SafeBreach's Gemini Voice/Gemini Live findings were confirmed mitigated by Google on 2025-11-14 via content-classifier updates. Reference: http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html and https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini.
- **Active Exploitation:** true. Forcepoint X-Labs documented 10 IPI payloads weaponized across at least 10 live production websites on 2026-04-22, including financial-fraud, API-key exfiltration, output hijacking, and data-destruction payloads (https://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads). Help Net Security reported a 32% rise in malicious IPI between November 2025 and February 2026, describing 'shared injection templates across multiple domains' as 'organized tooling rather than isolated experimentation' (https://helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild). Google's blog (2025-06-13) characterizes IPI as 'a top priority for the security community' and anticipates it becoming a primary attack vector for AI agents (https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html). No public source yet attributes exploitation to a named APT or ransomware group.
- **Threat Actors:** None known. No specific APT groups, cybercrime syndicates, or ransomware operators have been publicly attributed to exploiting indirect prompt injection against Gemini. Forcepoint X-Labs reported 10 weaponized IPI payloads across the open web in April 2026 originating from 'multiple actors' using 'shared injection templates,' but did not name any specific group. Help Net Security reported a 32% rise in malicious IPI between November 2025 and February 2026 described as 'organized tooling rather than isolated experimentation,' without naming actors.
- **Mitigation:** Google's layered defense (continuously deployed, no customer patch required): prompt-injection content classifiers, security thought reinforcement (system-level instruction steering), markdown sanitization and suspicious-URL redaction via Google Safe Browsing, user confirmation framework (human-in-the-loop HITL) for risky actions, end-user security notifications when defenses fire, adversarial training in Gemini 2.5, and continuous red-team/BugSWAT exercises under the Secure AI Framework (SAIF). Customer-side hardening: enable Workspace admin policies enforcing HITL confirmations; restrict Gemini's tool authority (e.g., disable Calendar auto-write); apply allowlisting for Gemini agents; enforce DLP and Safe Browsing on outbound links; provide security-awareness training so users recognize IPI-likely content (unexpected instructions in emails/docs/invites).
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors exploit public CVEs on internet-exposed network edge devices (Cisco IOS XE Web UI, Ivanti Connect/Policy Secure, Palo Alto GlobalProtect) for initial access, then pivot through compromised devices and trusted interconnections. Post-compromise, they modify device configurations to maintain persistence and gather intelligence: they alter ACLs (notably 'access-list 20') to permit attacker IPs, enable SPAN/RSPAN/ERSPAN traffic mirroring, stand up GRE/IPsec/mGRE tunnels for exfiltration, abuse Cisco Guest Shell with Python scripts (e.g., siet.py) to evade syslog, modify TACACS+/RADIUS pointers, harvest credentials via Embedded Packet Capture and brute-forcing/decrypting Cisco Type 5/7 passwords, capture BGP/RSVP/MIB/MPLS via TFTP, and create privileged (privilege-15) local accounts. Custom backdoors include SparrowDoor and ShadowPad; webshells include DotNetNuke variants. Operational toolset includes schtasks, attrib, reg save, net group/user/use, ipconfig, netstat, nltest, certutil, PAExec, SSH from non-standard high ports, and SNMP SET requests for router reconfiguration.
- **Affected Products:** Cisco IOS XE Software Web UI (versions prior to 16.12.10a / 17.3.8a / 17.6.6a / 17.9.4a — affected by CVE-2023-20198 and CVE-2023-20273); Ivanti Connect Secure 9.x and 22.x and Ivanti Policy Secure 9.x and 22.x (CVE-2024-21887, often chained with CVE-2023-46805); Palo Alto Networks PAN-OS versions 10.2, 11.0 and 11.1 with GlobalProtect enabled (CVE-2024-3400 — fixed in 10.2.9-h1, 11.0.4-h1, 11.1.2-h3). Suspected additional targeting of Fortinet, Juniper, Microsoft Exchange, Nokia, Sierra Wireless, and SonicWall devices.
- **CVSS Score:** CVE-2024-21887 = 9.1 (Critical); CVE-2024-3400 = 10.0 (Critical, CVSS v3.1); CVE-2023-20198 = 10.0 (Critical); CVE-2023-20273 = 7.2 (High). Overall advisory impact is Critical.
- **CVSS Vector:** CVE-2024-21887 (Ivanti): CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H; CVE-2024-3400 (PAN-OS GlobalProtect): CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H; CVE-2023-20198 (Cisco IOS XE Web UI): CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H; CVE-2023-20273 (Cisco IOS XE Web UI): CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true (public PoCs: https://github.com/smokeintheshell/CVE-2023-20198 and https://github.com/retkoussa/CVE-2024-3400)
- **Patch Available:** true (Cisco IOS XE 16.12.10a / 17.3.8a / 17.6.6a / 17.9.4a; Palo Alto PAN-OS 10.2.9-h1 / 11.0.4-h1 / 11.1.2-h3; Ivanti Connect/Policy Secure 22.7R2.5)
- **Active Exploitation:** true (confirmed in the wild — activity ongoing since ~2021; sources: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a, https://leargassecurity.com/2025/08/28/cisa-aa25-239a-countering-chinese-state-sponsored-actors-compromising-network-devices-worldwide, https://www.picussecurity.com/resource/blog/cisa-alert-aa25-239a-analysis-simulation-and-mitigation-of-chinese-apts)
- **Threat Actors:** PRC state-sponsored APT actors tracked as Salt Typhoon (Microsoft), OPERATOR PANDA, RedMike, UNC5807, GhostEmperor (Kaspersky), Earth Estries (Trend Micro), FamousSparrow (ESET), and UNC2286 (Mandiant). Named PRC entities include Sichuan Juxinhe Network Technology Co. Ltd., Beijing Huanyu Tianqiong Information Technology Co., Ltd., and Sichuan Zhixin Ruijie Network Technology Co., Ltd.
- **Mitigation:** Prioritize patching of CVE-2024-21887 (Ivanti Connect/Policy Secure, 22.7R2.5), CVE-2023-20198 / CVE-2023-20273 (Cisco IOS XE 16.12.10a / 17.3.8a / 17.6.6a / 17.9.4a), and CVE-2024-3400 (PAN-OS 10.2.9-h1 / 11.0.4-h1 / 11.1.2-h3 and later). Disable unused services such as Cisco IOS XE Web UI and Cisco Smart Install on edge devices. Segregate management-plane services (SSH, HTTPS, SNMP, TACACS+, RADIUS) into dedicated out-of-band networks or VRFs. Enable Control-Plane Policing (CoPP) and infrastructure ACLs (iACLs) to restrict management access (e.g., block TCP/4786). Regularly audit device configurations for: unexpected GRE/IPsec tunnels, unexpected remote IPs in TACACS+/RADIUS configs, unexpected entries in ACLs (especially named like 'access-list 20'), SPAN/ERSPAN/RSPAN mirroring settings, and unexpected virtual containers/Guest Shell instances. Apply vendor threat-prevention signatures on perimeter gear. Disable HTTP/HTTPS servers on Cisco IOS XE devices impacted by CVE-2023-20198.
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

## 14. 🟡 High Severity — SharePoint RCE CVE-2026-45659 Added to CISA KEV After Active Exploitation

**CVE:** `CVE-2026-45659` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://thehackernews.com/2026/07/sharepoint-rce-cve-2026-45659-added-to.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Wednesday added a high-severity flaw impacting Microsoft SharePoint Server to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

The vulnerability, tracked as CVE-2026-45659 (CVSS score: 8.8), is a case of remote code execution arising from the deserialization of untrusted data. The issue

---

## 15. 🟡 High Severity — Apify Model Context Protocol (MCP) server: Actor MCP path authority injection leaks Apify token

**CVE:** `CVE-2026-50143` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-6gr2-qh89-hxwm>

> ## Actor MCP path authority injection leaks Apify token

### Summary

`@apify/actors-mcp-server` version `0.10.7` builds Actor standby URLs by directly concatenating a trusted base URL with an attacker-controlled `webServerMcpPath` value taken from an Actor definition returned by the Apify API. An attacker who publishes a malicious Actor with a crafted `webServerMcpPath` (e.g., `@attacker.example/…

---

## 16. 🟡 High Severity — goshs: Share-link ?token=… redemption races past download limit

**CVE:** `CVE-2026-50139` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-j48m-h7xq-2xpj>

> # Share-link `?token=…` redemption races past download limit

**Ecosystem:** Go
**Package:** `goshs.de/goshs/v2` (`github.com/patrickhener/goshs`)
**Affected:** `&lt;= v2.0.9` (every release that shipped the share-link feature)

## Summary

`ShareHandler` reads the share token&#x27;s `DownloadLimit` under `RLock`, releases the lock, serves the file, then re-acquires the lock to increment the count…

---

## 17. 🟡 High Severity — goshs: WebDAV listener ignores --read-only, --upload-only, and --no-delete mode flags

**CVE:** `CVE-2026-50138` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-3whc-qvhv-xqjp>

> # WebDAV listener ignores `--read-only`, `--upload-only`, and `--no-delete` mode flags

**Ecosystem:** Go
**Package:** `goshs.de/goshs/v2` (`github.com/patrickhener/goshs`)
**Affected:** `&lt;= v2.0.9` (every release that ships the WebDAV handler)

## Summary

When `goshs` is launched with WebDAV enabled (`-w`), the mode-restriction flags `--read-only`, `--upload-only`, and `--no-delete` are enfor…

---

## 18. 🟡 High Severity — `oras-go` tar extraction: Hardlink entry with relative Linkname escapes extract dir via process CWD resolution

**CVE:** `CVE-2026-50163` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-fxhp-mv3v-67qp>

> ### Root cause

The tar-extraction helper `ensureLinkPath` at [`content/file/utils.go:262-275`](https://github.com/oras-project/oras-go/blob/main/content/file/utils.go#L262-L275) validates that a hardlink&#x27;s target resolves inside the extract base, but then returns the original unresolved `target` string back to the caller:

```go
func ensureLinkPath(baseAbs, baseRel, link, target string) (str…

---

## 19. 🟡 High Severity — oras-go blob upload vulnerable to credential forwarding via unvalidated Location header

**CVE:** `CVE-2026-50151` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-jxpm-75mh-9fp7>

> ## Summary

oras-go follows a registry-controlled `Location` header during the monolithic blob upload flow and reuses the `Authorization` header from the initial `POST` request for the subsequent `PUT` request. If a malicious registry returns a cross-host `Location`, oras-go can send the caller&#x27;s credentials to an attacker-controlled endpoint.

## Affected Versions

tested: v2.6.0 (commit 032…

---

## 20. 🟡 High Severity — Keycloak has privilege escalation via improper scope mapping enforcement

**CVE:** `CVE-2026-9795` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-32h4-44jj-c5vx>

> ### Description
A flaw was found in Keycloak&#x27;s Fine-Grained Admin Permissions (FGAPv2) feature. An administrator with limited client management permissions can exploit this vulnerability to assign any realm role, including highly privileged roles, to a client&#x27;s scope mapping. This bypasses intended security controls, allowing the injected role to be projected into a user&#x27;s authentic…

---

## 21. 🟡 High Severity — oras-go: Malicious registry can hijack Bearer token realm to exfiltrate credentials and refresh tokens

**CVE:** `CVE-2026-48978` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-xf85-363p-868w>

> ## Summary

oras-go&#x27;s `auth.Client` follows the `realm` URL from a registry&#x27;s `WWW-Authenticate: Bearer` challenge without validating its scheme or host. The `realm` field is server-controlled by design in the OCI/distribution spec — registries legitimately point token requests at a separate auth endpoint (e.g. Docker Hub&#x27;s `registry-1.docker.io` -&gt; `auth.docker.io`), so cross-ho…

---

## 22. 🟡 High Severity — Rancher has Privilege Escalation from Project Owner to Host

**CVE:** `CVE-2026-41052` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-vx8h-4prv-g744>

> ### Impact

A vulnerability has been identified in Rancher Manager that allows users assigned the Project Owner role to modify Pod Security Admission (PSA) labels on namespaces within their projects. Under the default role configuration, an attacker with the following access pattern can exploit this issue:
1. **Cluster Access:** The user is granted Cluster Member access.
2. **Project Ownership:** …

---

## 23. 🟡 High Severity — Mailpit: Sibling-endpoint memory-exhaustion DoS via unbounded JSON body on /api/v1/messages, /api/v1/tags, and /api/v1/message/{id}/release (incomplete fix of GHSA-fpxj-m5q8-fphw)

**CVE:** `CVE-2026-48824` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-28pq-6qxg-wg5r>

> ### Summary

The fix for GHSA-fpxj-m5q8-fphw (CVE-2026-45710, &quot;Mailpit: Set a default 50MB p/m limit to prevent DoS via unlimited SMTP DATA and /api/v1/send body sizes&quot;) wrapped only `POST /api/v1/send` with `http.MaxBytesReader`. The four other Mailpit JSON-body API endpoints  `PUT /api/v1/messages` (SetReadStatus), `DELETE /api/v1/messages` (DeleteMessages), `PUT /api/v1/tags` (SetMess…

---

## 24. 🟡 High Severity — Rancher Fleet has SSRF in Bundle Reader via Unvalidated Helm Repository URL in fleet.yaml

**CVE:** `CVE-2026-44936` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-hx4v-cxpf-vh8m>

> ### Impact
A vulnerability has been identified in Fleet when the `helmRepoURLRegex` field isn&#x27;t set on a `GitRepo` resource. Fleet&#x27;s bundle reader forwards Helm authentication credentials (`BasicAuth`) to any URL specified in the `helm.repo` field of a `fleet.yaml` file.

An attacker with git push access to a Fleet-monitored repository can exploit this behavior by specifying a malicious …

---

## 25. 🟡 High Severity — Rancher vulnerable to command injection through unsanitized YAML parameter

**CVE:** `CVE-2026-44939` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-mhc6-2gfq-xx62>

> ### Impact
A critical command injection vulnerability has been identified in the Rancher Manager cluster import endpoint  `/v3/import/{token}_{clusterId}.yaml` through unsanitized YAML parameters. This endpoint accepts an `authImage` query parameter that is rendered without sanitization into a generated Kubernetes manifest template. By including URL-encoded newlines in the parameter value, an atta…

---

## 26. 🟡 High Severity — Rancher Fleet has Unauthenticated Webhook: Regex Injection via Unsanitized Repository URL Components

**CVE:** `CVE-2026-44937` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-jmf4-m7j9-g72r>

> ### Impact
A vulnerability has been identified in Fleet when the webhook endpoint is configured without a secret; an attacker can forge webhook requests. The attacker doesn&#x27;t need to know the specific repository or path configured in the GitRepo resource to make Fleet process these requests.

An attacker can exploit this vulnerability to cause the following impacts:
1. Trigger continuous repo…

---

## 27. 🟡 High Severity — Fleet has PSS Bypass through addLabelsFromOptions in Fleet Agent

**CVE:** `CVE-2026-44938` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-864g-863m-vcvq>

> ### Impact
A vulnerability has been identified in Fleet&#x27;s agent-side deployer, which did not filter security-sensitive keys from `namespaceLabels` in `fleet.yaml` (or `BundleDeployment.spec.options.namespaceLabels`) when applying them to the target namespace. 

An attacker with `git push` access to a Fleet-monitored repository could overwrite Pod Security Standards (PSS) enforcement labels on…

---

## 28. 🟡 High Severity — CrateDB's Blob HTTP handler bypasses authorization

**CVE:** `CVE-2026-49989` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-2xv8-gjwh-fv8p>

> **Component:** `io.crate.protocols.http.HttpBlobHandler`
**Affected:** verified against CrateDB 6.2.7 (latest at time of report; the bug has existed since the blob HTTP handler was introduced)
**Impact:** any authenticated user can read or delete any blob whose SHA-1 digest they know, and can plant new blobs unconditionally, in any blob table, regardless of `GRANT`s.

---

## Summary

CrateDB has …

---

## 29. 🟡 High Severity — repomix: attach_packed_output can bypass file-read secret scanning for supported local files

**CVE:** `CVE-2026-49988` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-hwpp-h97w-2h3j>

> # `attach_packed_output` can register arbitrary `.json/.txt/.md/.xml` files and bypass the MCP file-read safety check

## Summary

Repomix&#x27;s MCP server exposes a normal `file_system_read_file` tool that reads absolute paths only after running the project&#x27;s secret check. However, the `attach_packed_output` plus `read_repomix_output` flow can read arbitrary local `.json`, `.txt`, `.md`, or…

---

## 30. 🟡 High Severity — Twig: Sandbox filter, tag and function allow-list bypass when sandbox state changes between renders for a cached `Template`

**CVE:** `CVE-2026-49981` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-529h-vh3j-85hq>

> ### Description

The per-template filter, tag and function allow-list check is compiled into the `checkSecurity()` method of each `Template` subclass and was invoked once from the constructor, gated by `SandboxExtension::isSandboxed($source)`. `Template` instances are then cached on the `Environment` in `$loadedTemplates`, so the verdict computed at construction time was sticky for the rest of the…

---

## 31. 🟡 High Severity — Cortex has Untrusted Project Bootstrap Code Execution via `CLAUDE_PROJECT_DIR`

**CVE:** `CVE-2026-49986` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-gvpp-v77h-5w8g>

> ## Untrusted Project Bootstrap Code Execution via `CLAUDE_PROJECT_DIR`

### Summary

The Cortex MCP server (`neuro-cortex-memory`) treats the `CLAUDE_PROJECT_DIR` environment variable — automatically set by Claude Code to the currently open project directory — as a trusted Cortex developer checkout. When the `open_visualization` tool is invoked, `_find_dev_source()` resolves the user&#x27;s active…

---

## 32. 🟡 High Severity — auth-fetch-mcp has SSRF Protection Bypass via IPv4-mapped IPv6 Loopback

**CVE:** `CVE-2026-49857` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-pvrj-8cg3-j5f8>

> ## SSRF Protection Bypass via IPv4-mapped IPv6 Loopback

### Summary

`auth-fetch-mcp` v3.0.1 implements SSRF protection in `assertSafeUrl()` (`src/security.ts`) to block requests to private and loopback addresses. However, the `isPrivateV6()` function fails to detect IPv4-mapped IPv6 loopback addresses in their hex-normalized form. When an attacker supplies a URL such as `http://[::ffff:127.0.0.1…

---

## 33. 🟡 High Severity — @jshookmcp/jshook: ICMP probe and traceroute skip local-network SSRF authorization

**CVE:** `CVE-2026-49856` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-c5r6-m4mr-8q5j>

> ## Summary

The network domain has a central SSRF authorization policy that blocks private, loopback, link-local, and reserved targets unless an explicit authorization object allows private network access. The policy is enforced by raw HTTP/TCP/TLS RTT tools, but the ICMP probe and traceroute tools resolve the target and invoke the native ICMP/traceroute sink directly.

An MCP client with access t…

---

## 34. 🟡 High Severity — Open Babel has out-of-bounds write in Gaussian translationVectors[]

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

## 35. 🟡 High Severity — Progress Kemp LoadMaster Pre-Auth RCE Flaw Faces Active Exploitation Attempts

**CVE:** `CVE-2026-8037` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://thehackernews.com/2026/07/latest-progress-kemp-loadmaster-pre.html>

> A recently disclosed critical security flaw impacting Progress Kemp LoadMaster is seeing active exploitation attempts, according to an advisory from eSentire&#x27;s Threat Response Unit (TRU).

The Canadian cybersecurity company said it identified exploitation attempts targeting CVE-2026-8037 (CVSS score: 9.6), an operating system (OS) command injection flaw that could be exploited to achieve

---

## 36. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
