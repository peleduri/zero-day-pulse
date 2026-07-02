# Zero Day Pulse

> **Generated:** 2026-07-02 13:28 UTC &nbsp;|&nbsp; **Total:** 37 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 23 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is an unauthenticated path traversal (CWE-22) in the SimpleHelp remote support/RMM software's /toolbox-resource HTTP endpoint. By sending crafted requests with directory-traversal sequences (e.g., '../../../../../'), a remote unauthenticated attacker can download arbitrary files from the host. Commonly targeted sensitive files include SimpleHelp's serverconfig.xml (containing hashed technician/user passwords, API keys, and TOTP seeds), Linux system files (/etc/passwd, /root/.ssh/id_rsa), and Windows credential stores (C:\Windows\System32\config\SAM). Exploitation requires no authentication and no user interaction.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) versions 5.5.7 and all earlier releases (including 5.5.x, 5.4.10, and 5.3.9 lines).
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true — Public exploit code exists. Rapid7 Metasploit auxiliary scanner module published 2025-02-25 (https://www.rapid7.com/db/modules/auxiliary/scanner/http/simplehelp_toolbox_path_traversal/). Technical analysis and exploitation details also published by OffSec (https://www.offsec.com/blog/cve-2024-57727/, April 2025).
- **Patch Available:** true — Vendor (SimpleHelp) released v5.5.8 plus dedicated patches for the v5.4.10 and v5.3.9 supported lines. Vendor advisory: https://guides.simple-help.com/kb---security-vulnerabilities-01-2025 ; downloads: https://simple-help.com/downloads.
- **Active Exploitation:** true — Confirmed by CISA in Advisory AA25-163A (published 2025-06-12) attributing exploitation since at least January 2025. CVE-2024-57727 was added to CISA's Known Exploited Vulnerabilities (KEV) Catalog on 2025-02-13. The documented incident pattern: ransomware actors (DragonForce) exploited the path traversal against an unpatched SimpleHelp RMM instance at a utility billing software provider, then used harvested credentials and remote management access for lateral movement and ransomware deployment (double-extortion) against downstream customers.
- **Threat Actors:** DragonForce ransomware actors (per CISA Advisory AA25-163A, published June 12, 2025). CISA notes a broader pattern of unnamed ransomware actors exploiting the vulnerability since January 2025, including a compromise of a utility billing software provider that cascaded to downstream customers.
- **Mitigation:** Primary remediation: upgrade SimpleHelp to v5.5.8 or later (https://simple-help.com/downloads). For legacy lines, dedicated patches were issued for v5.4.10 and v5.3.9. Immediate compensating controls if upgrade is not possible: (1) isolate any internet-exposed SimpleHelp server or stop the SimpleHelp process; (2) hunt the host for suspicious three-letter executables (e.g., aaa.exe, bbb.exe) created after January 2025 — a CISA IOC tied to DragonForce hands-on-keyboard activity; (3) rotate all technician and administrator passwords and any secrets/API keys stored in serverconfig.xml, and replace potentially compromised SSH keys; (4) perform host and network scanning for indicators of compromise. Proactive controls per CISA: maintain an accurate asset inventory, keep clean offline backups, do not expose RDP to the internet, conduct RMM-specific risk analysis, and use Software Bills of Materials (SBOMs) for procurement.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — CISA: Microsoft SharePoint RCE flaw now actively exploited

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-microsoft-sharepoint-rce-flaw-now-actively-exploited/>

> CISA warned on Wednesday that attackers have begun exploiting a high-severity Microsoft SharePoint remote code execution vulnerability patched in May. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Deserialization of untrusted data (CWE-502) in Microsoft Office SharePoint. An authenticated attacker holding only low-privilege Site Member permissions submits crafted serialized .NET data to a SharePoint endpoint. SharePoint reconstructs the .NET objects from the serialized payload without enforcing a strict type allow-list, allowing the attacker to use a known gadget chain that triggers arbitrary remote code execution on the server. The attack is network-based, low complexity, and requires no user interaction (UI:N).
- **Affected Products:** Microsoft SharePoint Server Subscription Edition (builds prior to 16.0.19725.20280), Microsoft SharePoint Server 2019 (builds prior to 16.0.10417.20128), Microsoft SharePoint Enterprise Server 2016 (builds prior to 16.0.5552.1002)
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true — A weaponized in-the-wild exploit is being actively used against internet-exposed SharePoint servers, though no public PoC code has been published. Microsoft flagged the flaw as easy to exploit with repeatable success. Sources: https://thehackernews.com/2026/07/sharepoint-rce-cve-2026-45659-added-to.html, https://www.bleepingcomputer.com/news/security/cisa-microsoft-sharepoint-rce-flaw-now-actively-exploited/
- **Patch Available:** true — https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45659 (patch released May 2026; CISA federal remediation deadline was July 4, 2026)
- **Active Exploitation:** true — CISA added CVE-2026-45659 to the Known Exploited Vulnerabilities (KEV) Catalog on 2026-07-01 with 'Active' exploitation status, requiring U.S. federal agencies to remediate by 2026-07-04. Confirmed by CISA, BleepingComputer, The Hacker News, and helpnetsecurity.
- **Threat Actors:** Storm-2603 — a threat actor known for deploying Warlock ransomware, attributed by Microsoft to exploiting CVE-2026-45659. Storm-2603 is described as China-based and financially motivated, with links to Warlock ransomware operations and potential connections to Chinese state-sponsored APT groups such as APT27 (Linen Typhoon) and APT31 (Violet Typhoon).
- **Mitigation:** Primary: Install the Microsoft May 2026 security updates for the affected SharePoint versions. Additional hardening: restrict administrative endpoints to trusted internal networks; audit and remove excessive user permissions; enforce AMSI integration in SharePoint and enable full AMSI scanning mode; deploy a Web Application Firewall (WAF) to inspect serialized payload signatures; rotate machine keys and service account credentials after patching; restrict or disable non-essential web services and custom handlers.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45659

---

## 3. 🟠 Zero-Day — Rancher Fleet vulnerable to cross namespace secret disclosure via unvalidated `valuesFrom` references in Helm Deployer

**CVE:** `CVE-2026-44935` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-xr65-5cpm-g36x>

> ### Impact
A vulnerability in Fleet for Rancher Manager affects multi-tenancy environments where different tenants share the same downstream clusters (e.g., different privileged or untrusted teams inside the same organization). 

On unpatched versions, tenants could bypass restrictions to access any config map or secret across all namespaces on the downstream cluster. They can create cluster-wide …

**Parallel AI Enrichment:**

- **Technical Details:** In multi-tenancy environments where multiple tenants share the same downstream Kubernetes cluster, Fleet's Helm deployer fails to consistently enforce tenant boundaries and ServiceAccount impersonation. Two attack paths exist: (1) An attacker adds a `valuesFrom` entry to `fleet.yaml` (via GitRepo or HelmOp) that references a ConfigMap or Secret by name in any namespace; the fleet-agent reads these using its cluster-admin credentials rather than the tenant's intended ServiceAccount, enabling exfiltration of any Secret/ConfigMap on the downstream cluster when name, namespace, and key are guessable. (2) HelmOp and Bundle resources are not restricted to a specific ServiceAccount for the fleet-agent, allowing tenants to deploy resources that act cluster-wide, bypassing intended RBAC boundaries. Combined, this results in full multi-tenant isolation break, cross-namespace secret/ConfigMap disclosure, and unauthorized cluster-wide resource creation by any tenant with git-push or GitRepo-create rights.
- **Affected Products:** Rancher Fleet: 0.12.0–0.12.14, 0.13.0–0.13.10, 0.14.0–0.14.5, and 0.15.0–0.15.1 (i.e., >=0.12.0 <0.12.15; >=0.13.0 <0.13.11; >=0.14.0 <0.14.6; >=0.15.0 <0.15.2)
- **CVSS Score:** 9.9
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true (Rancher Fleet v0.15.2, v0.14.6, v0.13.11, v0.12.15 — Advisory: https://github.com/advisories/GHSA-xr65-5cpm-g36x)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Upgrade to a patched Rancher Fleet release: 0.15.2, 0.14.6, 0.13.11, or 0.12.15. After upgrading, use the new `Policy` custom resource to enforce specific ServiceAccounts for GitRepo, HelmOp, and Bundle resources, and restrict HelmOp repository/chart URLs with regular expressions. As a temporary workaround (if upgrade is not yet possible), ensure no two tenants share the same downstream cluster so the cross-tenant boundary cannot be crossed. Additionally, review cluster and Fleet logs for indicators of unauthorized cross-namespace access, and rotate any service accounts, secrets, or credentials that may have been exposed.
- **Vendor Advisory:** https://github.com/advisories/GHSA-xr65-5cpm-g36x

---

## 4. 🟠 Zero-Day — Unpatched Argo CD Repo-Server Flaw Could Let Attackers Take Over Kubernetes Clusters

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://thehackernews.com/2026/07/unpatched-argo-cd-repo-server-flaw.html>

> Argo CD, a widely used tool for deploying software to Kubernetes, has an unpatched flaw in its repo-server component that lets an unauthenticated attacker run code, provided they can reach the component&#x27;s internal network port.

Synacktiv, which found the bug, says it can lead to a full cluster takeover. There is no fix and no CVE. The firm says it reported the flaw to Argo CD&#x27;s maintain…

**Parallel AI Enrichment:**

- **Technical Details:** The Argo CD repo-server component exposes an unauthenticated gRPC endpoint (repository.RepoServerService/GenerateManifest) on its internal TCP port 8081. An attacker with network reachability to that port can submit a malicious KustomizeOptions struct that abuses the kustomize build command's --enable-helm / --helm-command flags, causing the repo-server to execute an arbitrary shell script hosted in a Git repository controlled by the attacker. Successful code execution on the repo-server enables theft of the REDIS_PASSWORD environment variable and poisoning of Argo CD's Redis-backed manifest cache. This cache poisoning can then force deployment of attacker-controlled manifests across applications, culminating in full Kubernetes cluster takeover.
- **Affected Products:** Argo CD (repo-server component); demonstrated on v2.13.3. Full list of affected versions not publicly published.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false. The Synacktiv-developed 'argo-cdown' tool exists but is being deliberately withheld from public release to allow defenders time to apply mitigations.
- **Patch Available:** false. No official vendor patch has been released; the Argoproj maintainers were notified in January 2025 but, as of disclosure on 2026-07-01, no fix has been published.
- **Active Exploitation:** false. No confirmed in-the-wild exploitation has been reported at the time of disclosure. Synacktiv demonstrated the attack in a controlled environment against Argo CD v2.13.3, but has not observed real-world exploitation and is withholding the PoC.
- **Threat Actors:** None known.
- **Mitigation:** Apply strict Kubernetes NetworkPolicies to restrict access to the Argo CD repo-server gRPC port (TCP 8081 by default) and the Redis service (argocd-redis:6379) to only trusted Argo CD components. Important caveat: Argo CD's official Helm chart sets networkPolicy.create to false by default — Helm users must explicitly set networkPolicy.create: true. Verify policies are in place with 'kubectl get networkpolicy -A'. Additional hardening: monitor repo-server and Redis activity logs for unauthorized commands or anomalous manifest cache changes; track the Argoproj project for an upcoming patch.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — Critical Cursor Flaws Could Let Prompt Injection Escape Sandbox and Run Commands

**CVE:** `CVE-2026-50548` | `CVE-2026-50549` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://thehackernews.com/2026/07/critical-cursor-flaws-could-let-prompt.html>

> Two flaws in Cursor, an AI code editor, could let a single, ordinary-looking prompt break out of the editor&#x27;s safety sandbox and run any command on a developer&#x27;s computer. There is no click to fall for and no approval box to ignore.

Cato AI Labs found the pair and named them DuneSlide. They are tracked as CVE-2026-50548 and CVE-2026-50549, both rated 9.8 out of 10 (or 9.3

**Parallel AI Enrichment:**

- **Technical Details:** Two zero-click, prompt-injection-driven sandbox escape flaws in Cursor's agent-mode terminal: (1) CVE-2026-50548 — the run_terminal_cmd tool's working_directory parameter can be set to any path by the LLM agent, and the sandbox then grants write access to that external path; (2) CVE-2026-50549 — path canonicalization fails on symlinks pointing outside the workspace, causing a fallback to the original path and allowing writes through the symlink. Attack chain: a single innocuous user prompt ingests poisoned content (MCP server response / web search result) → prompt injection steers agent to leverage one of the two primitives → agent overwrites the cursorsandbox helper binary (e.g., /Applications/Cursor.app/Contents/Resources/app/resources/helpers/cursorsandbox) → subsequent commands in the same prompt execute un-sandboxed → arbitrary command execution on the developer's host with full user privileges.
- **Affected Products:** Cursor (by Anysphere) — all versions prior to 3.0 (Cursor 2.x and earlier)
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true — Cursor 3.0 (released April 2, 2026) — https://github.com/cursor/cursor/security/advisories/GHSA-3p48-7v9f-v5cw
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Primary fix: Update to Cursor 3.0 (released April 2, 2026), which patches both CVE-2026-50548 and CVE-2026-50549. Hardening for users on affected versions: treat any content the Cursor agent may ingest (web search results, MCP server responses, fetched documents, third-party skills) as untrusted input; enable agent sandboxing; restrict which MCP servers and skills the agent can interact with; minimize use of auto-approve terminal-command flows; do not paste untrusted content into agent-mode prompts.
- **Vendor Advisory:** https://github.com/cursor/cursor/security/advisories/GHSA-3p48-7v9f-v5cw

---

## 6. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an AI system processes untrusted content (website, email, document) containing malicious instructions; the AI silently follows the attacker's commands instead of the user's original intent. Observed obfuscation techniques: HTML comments, CSS invisibility (display:none, 1px fonts, transparent colors), accessibility-attribute abuse (aria-hidden, visually-hidden), conditional 'If you are an AI…' targeting, spoofed system-prompt/magic-string tokens, custom metadata namespaces (e.g., ai:action). Observed payload goals: API-key exfiltration, persona hijacking, content suppression/DoS, agent-tool path traversal, traffic/SEO hijacking, terminal-command injection, donation/financial fraud, system prompt leakage.
- **Affected Products:** Google Gemini, AI agents/assistants/chatbots, agentic AI systems with browser/shell access, LLM-powered coding assistants, AI crawlers/indexers, Anthropic Claude, ChatGPT, Microsoft Copilot (no specific version ranges applicable—this is an attack class affecting the category of AI/LLM products)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true - 10 in-the-wild IPI payloads documented by Forcepoint X-Labs at https://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads; Google's Common Crawl scan found weaponized IPI in 2-3 billion page snapshots
- **Patch Available:** false - No single patch exists for the IPI attack class; Google describes ongoing/continuous model and product hardening rather than a discrete patch release. (Separately tracked IPI-related CVEs such as CVE-2025-54131 and the Google Antigravity IDE flaw (patched 28 Feb 2026) have individual patches.)
- **Active Exploitation:** true - Google Threat Intelligence observed a 32% relative increase in malicious IPI detections from November 2025 to February 2026 across Common Crawl snapshots of 2-3 billion pages. Forcepoint X-Labs independently documented 10 distinct passive in-the-wild IPI payloads. Confirmed by SecurityWeek and Infosecurity Magazine reporting.
- **Threat Actors:** None known
- **Mitigation:** (1) Ongoing hardening of AI models and products; (2) Dedicated red teams performing relentless adversarial pressure-testing of Gemini and other assistants; (3) Participation in the Google AI Vulnerability Reward Program; (4) Real-time global-scale data processing to detect and neutralize IPI before it reaches users; (5) Layered defense across products (Google's published strategy linked from the post: 'Mitigating prompt injection attacks with a layered defense strategy', 'Advancing Gemini's security safeguards', and 'Lessons from Defending Gemini Against Indirect Prompt Injections'); (6) Defenders more generally: enforce a strict data/instruction boundary in agent design, sanitize/inspect untrusted content flowing into the model context, allow-list agent tool calls, perform obfuscation-aware input parsing, and block known IPI-bearing URLs/domains.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 7. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is a prompt-injection variant in which an attacker plants malicious natural-language instructions inside untrusted external content that a Gemini-backed Workspace feature later consumes as part of completing the user's query. Typical vectors include instructions hidden in inbound emails (consumed by Gemini in Gmail summarization), documents in Drive/Docs (consumed by Gemini summarization or AI-assisted editing), shared files, calendar invites, or third-party web pages accessed by an AI agent. Because Gemini treats instructions found in retrieved content as part of the prompt, those hidden instructions can cause the model to ignore the user's intent, exfiltrate data it has access to, take unintended agentic actions (e.g., drafting/sending messages, calling tools), or alter outputs — all without the user supplying any malicious text themselves. IPI becomes especially impactful with agentic automation, where the model executes tool calls on behalf of the user. OWASP classifies this as LLM01:2025 Prompt Injection.
- **Affected Products:** Google Workspace with Gemini — specifically the Gemini app and Gemini integrations inside Gmail, Google Docs (and other Docs editors), Google Drive, and Google Chat. IPI is a vulnerability class affecting all current versions of these Gemini-backed Workspace surfaces; no version-specific bound applies because the issue is at the model/integration design level.
- **CVSS Score:** CVSS score unavailable. No CVSS v3.x base score has been assigned to this advisory because it documents a class-level design mitigation rather than a single, fixed vulnerability. (Note: an unrelated Gemini CLI RCE disclosed separately has been scored CVSS 10.0, but that is a distinct issue from the IPI mitigation blog post.)
- **CVSS Vector:** CVSS vector unavailable. Indirect prompt injection is a vulnerability class rather than a specific CVE-registered issue, so no single CVSS v3 vector string has been published for the IPI mitigation effort described in this advisory. Related common-weakness enumeration: CWE-1426 'Improper Validation of Generative AI Output' (https://cwe.mitre.org/data/definitions/1426.html).
- **Exploit Available:** true. Public demonstrations and PoCs include: SafeBreach Labs — 'Gemini's Secret Affair: Exploiting Gemini Voice Assistant Through Instant Messaging Apps' (https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/, Jun 3 2026); Tracebit — 'Code Execution Through Deception: Gemini AI CLI Hijack' (https://tracebit.com/blog/code-exec-deception-gemini-ai-cli-hijack, Jul 28 2025); Cyera Research Labs — command and prompt injection disclosures in Gemini CLI (https://www.cyera.com/research/cyera-research-labs-discloses-command-prompt-injection-vulnerabilities-in-gemini-cli, Nov 17 2025); Noma Labs — 'GeminiJack' against Gemini Enterprise (https://noma.security/noma-labs/geminijack/); Forcepoint X-Labs — 10 IPI payloads harvested from active sites (http://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads, Apr 22 2026); payloads catalogued in PayloadAllTheThings (https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Prompt%20Injection/README.md).
- **Patch Available:** true. Google states it is continuously deploying model hardening, ML-based detection, and system-level mitigations across the Gemini app and Gemini in Workspace; the same vendor advisory URL (http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html) documents the evolving defense program that constitutes the 'patch' for this class. There is no single discrete patch — mitigation is iterative and ongoing.
- **Active Exploitation:** true. Multiple sources confirm IPI being observed in the wild against Gemini-class/LLM-agent deployments rather than only in lab/research settings: Palo Alto Unit 42 — 'Fooling AI Agents: Web-Based Indirect Prompt Injection Observed in the Wild' (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/, Mar 3 2026) — reports detections of in-the-wild IDPI attacks against AI agents that review/validate advertisements; Forcepoint X-Labs — '10 Indirect Prompt Injection Payloads Caught in the Wild' (http://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads, Apr 22 2026) — including a documented case of unauthorized financial transaction / payment-platform exploitation; SecurityWeek reports that Google observed malicious IPI attempts on the public web increasing (http://securityweek.com/malicious-ai-prompt-injection-attacks-increasing-but-sophistication-still-low-google); and Help Net Security reported 'Indirect prompt injection is taking hold in the wild' (http://helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild).
- **Threat Actors:** None known. No APT group, nation-state actor, or ransomware operator has been publicly attributed to indirect prompt injection (IPI) exploitation. All publicly documented Gemini/Workspace IPI demonstrations come from commercial security research labs (SafeBreach, Tracebit, Cyera Research Labs, Noma Labs 'GeminiJack', Forcepoint X-Labs) and academic researchers, not from named adversary groups.
- **Mitigation:** Google's layered defense, as described in the advisory: (1) model-level hardening in Gemini (explicitly cited: Gemini 2.5 hardening for IPI resistance), (2) purpose-built machine-learning classifiers that scan untrusted content for malicious prompt-injection instructions, (3) system- and application-level safeguards integrated into the Workspace and Gemini products. Complementary hardening guidance from related industry sources: strict input sanitization and marking of untrusted data, output validation/action allow-listing, separating retrieved content from system instructions via 'spotlighting'/metadata marking, and retaining human-in-the-loop review and confirmation for any agentic/side-effect action. Workspace administrator guidance is published at https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 8. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection against agentic browser capabilities in Chrome/Gemini. Adversary-controlled web content (malicious sites, third-party iframes, user-generated content such as reviews, hidden HTML/CSS in emails, calendar invites, or shared documents) carries instructions that the agent's on-page planning model ingests alongside the user's task. The agent then acts on injected instructions — initiating payments, exfiltrating data from other open tabs/origins, deleting calendar events, or navigating to attacker-chosen URLs. The model cannot reliably distinguish attacker content from legitimate user intent. A concrete adjacent vulnerability is CVE-2026-0628: a malicious Chrome extension abuses the declarativeNetRequest API to inject JavaScript into https://gemini.google.com/app as it loads inside the high-privilege Gemini browser panel, giving the injected script access to local files, camera/microphone, and screenshots.
- **Affected Products:** Gemini in Chrome with agentic capabilities (preview, rolled to Google AI Pro / Google AI Ultra subscribers in the U.S.) — Chromium-based Google Chrome builds with bundled Gemini integration. Closely related: CVE-2026-0628 (insufficient policy enforcement in WebView tag) affects Google Chrome prior to 143.0.7499.192 on desktop platforms.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true. Multiple public PoCs exist: 0din.ai 'Phishing For Gemini' (Jul 10, 2025) — https://0din.ai/blog/phishing-for-gemini ; Noma Labs 'GeminiJack' zero-click PoC (Dec 8, 2025) — https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/ ; SafeBreach Labs voice-assistant IPI (Jun 3, 2026) — https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/ ; Immersive Labs email-HTML IPI — https://immersivelabs.com/resources/c7-blog/weaponizing-llms-bypassing-email-security-products-via-indirect-prompt-injection ; Unit 42 CVE-2026-0628 extension hijack — https://unit42.paloaltonetworks.com/gemini-live-in-chrome-hijacking/
- **Patch Available:** true. The advisory at https://security.googleblog.com/2025/12/architecting-security-for-agentic.html describes layered defenses being deployed into Gemini in Chrome. For the closely related concrete vulnerability CVE-2026-0628, Google Chrome 143.0.7499.192 ships the fix. Google Workspace's layered-defense guidance page at https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini documents operational mitigations.
- **Active Exploitation:** true (for the indirect prompt injection threat class). Google Security Blog (Apr 23, 2026) reports a broad sweep of the public web found live indirect prompt injection patterns; Forcepoint X-Labs (Apr 22, 2026) documented '10 Indirect Prompt Injection Payloads Caught in the Wild'; Palo Alto Unit 42 (Mar 3, 2026) describes real-world web-based indirect prompt injection attacks; HelpNetSecurity (Apr 24, 2026) reports the technique 'taking hold in the wild.' For the closely related concrete CVE-2026-0628, no known exploits were reported in the wild at issuance.
- **Threat Actors:** None known. The official advisory does not attribute the indirect prompt injection threat against agentic Chrome/Gemini to any specific threat actor group. Separately, Google Threat Intelligence Group has reported PRC-attributed group HEX has misused Gemini for reconnaissance and task distillation, but not for indirect prompt injection campaigns.
- **Mitigation:** Per Google's Dec 8, 2025 advisory, Chrome/Gemini ship with a layered defense: (1) User Alignment Critic — a separate model that evaluates each proposed agent action for alignment with the user's goal before execution; (2) Agent Origin Sets — partitioning origins the agent can read from (read-only) versus write to (read-writable) to prevent cross-origin leakage; (3) deterministic and model-driven User Confirmations (human-in-the-loop) for impactful actions such as payments, messaging, sign-ins, and visits to sensitive sites (banking/healthcare); (4) a real-time prompt-injection classifier that scores pages in parallel with the planner and blocks misaligned actions; (5) automated red-teaming that generates malicious sandboxed sites to test and harden the system. Google Workspace additionally layers markdown/URL sanitization (Safe Browsing redaction), security thought reinforcement in system prompts, end-user mitigation notifications, and a user confirmation framework for admins to enforce HITL on sensitive operations. User guidance: review mitigation alerts and complete any prompted confirmations before agent actions are taken.
- **Vendor Advisory:** https://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 9. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** An out-of-bounds read (CWE-125) vulnerability in the Android System component's AVIF image parser/decoder. Incorrect bounds checks in the YUV/alpha/Y plane handling, plane-size computation, chroma-width calculation, and row-bytes logic allow out-of-bounds memory accesses when specially crafted AVIF content is processed. Triggerable remotely without user interaction or authentication, and can escalate to remote code execution when chained with other vulnerabilities.
- **Affected Products:** Google Android 16.0 (Android System component, AVIF image parser/decoder), versions prior to security patch level 2025-08-05
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true - https://source.android.com/security/bulletin/2025-08-01
- **Active Exploitation:** false
- **Threat Actors:** None known.
- **Mitigation:** Apply the August 2025 Android Security Bulletin (security patch level 2025-08-05 or later) to all Android 16.0 devices. Additional measures: enforce MDM/MDM-equivalent controls for patch deployment verification; segment network exposure of vulnerable devices; enforce strict inbound firewall rules; monitor system logs for abnormal memory-access patterns, segmentation faults, or unexpected crashes in Android system services; for AVIF/image-processing workloads, gate untrusted image ingestion via intermediary sanitization until patches are deployed.
- **Vendor Advisory:** https://source.android.com/security/bulletin/2025-08-01

---

## 10. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is an attack on generative-AI systems in which an adversary places hidden adversarial instructions inside external data that an AI will later read and act on (emails, documents, calendar invites, web pages, code repositories, images). Unlike direct prompt injection, the user is the victim, not the attacker. When the LLM ingests the tainted content, it can be coerced into exfiltrating data (e.g. via markdown image URLs or tool/API calls), modifying summaries, sending attacker-controlled messages, deleting files, or executing other rogue actions. Documented examples include hijacked Gemini summaries, AI Studio image-markdown exfiltration, and the zero-click EchoLeak exfil from Microsoft 365 Copilot.
- **Affected Products:** Google Gemini app; Google Gemini in Workspace apps (Gmail, Google Docs, Google Drive, Google Chat); Gemini 2.5 model family. No specific build versions are listed—the defense is deployed continuously across Gemini.
- **CVSS Score:** CVSS score unavailable. The IPI vulnerability class described has no formal CVSS base score. CVE-2025-32711 (EchoLeak), referenced by Google as a real-world example, is scored 9.3, but it is a separate vulnerability in Microsoft 365 Copilot.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — Multiple public PoCs exist: (1) HiddenLayer 'New Gemini for Workspace Vulnerability' (https://www.hiddenlayer.com/research/new-gemini-for-workspace-vulnerability-enabling-phishing-content-manipulation) with payloads against Gemini in Gmail, Slides, Drive; (2) EmbraceTheRed AI Studio data exfiltration (https://embracethered.com/blog/posts/2024/google-aistudio-mass-data-exfil/); (3) Forcepoint X-Labs 10 wild IPI payloads (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads); (4) EchoLeak (CVE-2025-32711) academic zero-click PoC referenced in the Google post.
- **Patch Available:** false — The post is a continuously-evolving defense strategy, not a single patchable CVE. Google subsequently extended the strategy with 'Google Workspace's continuous approach to mitigating indirect prompt injections' (https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/) but no discrete patch exists for this advisory.
- **Active Exploitation:** true — Confirmed active exploitation in the wild for the broader IPI attack class: (a) Google observed a ~32% rise in malicious IPI attempts against Gemini/Workspace between Nov 2025 and Feb 2026 (https://www.securityweek.com/malicious-ai-prompt-injection-attacks-increasing-but-sophistication-still-low-google/); (b) Palo Alto Unit 42 documented a real-world IPI bypass of an AI ad-review system (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/); (c) Forcepoint collected 10 distinct wild IPI payloads including payment-rerouting and destructive payloads (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads); (d) EchoLeak (CVE-2025-32711) is the first publicly documented zero-click IPI exploit (https://nvd.nist.gov/vuln/detail/cve-2025-32711). Note: The primary Google blog does not cite a specific in-the-wild Gemini incident; exploitation evidence comes from subsequent Google and third-party research covering the same IPI class.
- **Threat Actors:** None known. No specific APT or threat-actor group has been attributed to indirect prompt injection exploitation of Google Gemini. Google's GTIG 'AI Threat Tracker' names APT45, APT27, UNC2814, and TeamPCP/UNC6780, but only as actors leveraging Gemini for vulnerability research—they are not exploiting Gemini via IPI.
- **Mitigation:** Google's layered defense strategy for Gemini consists of five layers: (1) Prompt-injection content classifiers—ML classifiers that scan external content (emails, files) for malicious instructions; (2) Security thought reinforcement—targeted system-prompt instructions reminding the LLM to prefer the user task and ignore adversarial content; (3) Markdown sanitization and suspicious-URL redaction—strip external image URLs and other markdown that could exfiltrate data, cross-check URLs against Google Safe Browsing; (4) Human-in-the-loop user confirmation—require explicit user confirmation for sensitive actions (e.g. deleting a calendar event, sending mail); (5) End-user security mitigation notifications—surface contextual alerts and 'Learn more' link when defenses catch an attack. Underpinning all layers is Gemini 2.5 model hardening via adversarial training. A follow-up Workspace post (2026-04-02) adds a centralized Policy Engine for deterministic 'point fixes' plus continuous ML retraining and prompt-level LLM guardrails.
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

## 15. 🟡 High Severity — SharePoint RCE CVE-2026-45659 Added to CISA KEV After Active Exploitation

**CVE:** `CVE-2026-45659` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://thehackernews.com/2026/07/sharepoint-rce-cve-2026-45659-added-to.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Wednesday added a high-severity flaw impacting Microsoft SharePoint Server to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

The vulnerability, tracked as CVE-2026-45659 (CVSS score: 8.8), is a case of remote code execution arising from the deserialization of untrusted data. The issue

---

## 16. 🟡 High Severity — Apify Model Context Protocol (MCP) server: Actor MCP path authority injection leaks Apify token

**CVE:** `CVE-2026-50143` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-6gr2-qh89-hxwm>

> ## Actor MCP path authority injection leaks Apify token

### Summary

`@apify/actors-mcp-server` version `0.10.7` builds Actor standby URLs by directly concatenating a trusted base URL with an attacker-controlled `webServerMcpPath` value taken from an Actor definition returned by the Apify API. An attacker who publishes a malicious Actor with a crafted `webServerMcpPath` (e.g., `@attacker.example/…

---

## 17. 🟡 High Severity — goshs: Share-link ?token=… redemption races past download limit

**CVE:** `CVE-2026-50139` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-j48m-h7xq-2xpj>

> # Share-link `?token=…` redemption races past download limit

**Ecosystem:** Go
**Package:** `goshs.de/goshs/v2` (`github.com/patrickhener/goshs`)
**Affected:** `&lt;= v2.0.9` (every release that shipped the share-link feature)

## Summary

`ShareHandler` reads the share token&#x27;s `DownloadLimit` under `RLock`, releases the lock, serves the file, then re-acquires the lock to increment the count…

---

## 18. 🟡 High Severity — goshs: WebDAV listener ignores --read-only, --upload-only, and --no-delete mode flags

**CVE:** `CVE-2026-50138` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-3whc-qvhv-xqjp>

> # WebDAV listener ignores `--read-only`, `--upload-only`, and `--no-delete` mode flags

**Ecosystem:** Go
**Package:** `goshs.de/goshs/v2` (`github.com/patrickhener/goshs`)
**Affected:** `&lt;= v2.0.9` (every release that ships the WebDAV handler)

## Summary

When `goshs` is launched with WebDAV enabled (`-w`), the mode-restriction flags `--read-only`, `--upload-only`, and `--no-delete` are enfor…

---

## 19. 🟡 High Severity — `oras-go` tar extraction: Hardlink entry with relative Linkname escapes extract dir via process CWD resolution

**CVE:** `CVE-2026-50163` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-fxhp-mv3v-67qp>

> ### Root cause

The tar-extraction helper `ensureLinkPath` at [`content/file/utils.go:262-275`](https://github.com/oras-project/oras-go/blob/main/content/file/utils.go#L262-L275) validates that a hardlink&#x27;s target resolves inside the extract base, but then returns the original unresolved `target` string back to the caller:

```go
func ensureLinkPath(baseAbs, baseRel, link, target string) (str…

---

## 20. 🟡 High Severity — oras-go blob upload vulnerable to credential forwarding via unvalidated Location header

**CVE:** `CVE-2026-50151` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-jxpm-75mh-9fp7>

> ## Summary

oras-go follows a registry-controlled `Location` header during the monolithic blob upload flow and reuses the `Authorization` header from the initial `POST` request for the subsequent `PUT` request. If a malicious registry returns a cross-host `Location`, oras-go can send the caller&#x27;s credentials to an attacker-controlled endpoint.

## Affected Versions

tested: v2.6.0 (commit 032…

---

## 21. 🟡 High Severity — Keycloak has privilege escalation via improper scope mapping enforcement

**CVE:** `CVE-2026-9795` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-32h4-44jj-c5vx>

> ### Description
A flaw was found in Keycloak&#x27;s Fine-Grained Admin Permissions (FGAPv2) feature. An administrator with limited client management permissions can exploit this vulnerability to assign any realm role, including highly privileged roles, to a client&#x27;s scope mapping. This bypasses intended security controls, allowing the injected role to be projected into a user&#x27;s authentic…

---

## 22. 🟡 High Severity — oras-go: Malicious registry can hijack Bearer token realm to exfiltrate credentials and refresh tokens

**CVE:** `CVE-2026-48978` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-xf85-363p-868w>

> ## Summary

oras-go&#x27;s `auth.Client` follows the `realm` URL from a registry&#x27;s `WWW-Authenticate: Bearer` challenge without validating its scheme or host. The `realm` field is server-controlled by design in the OCI/distribution spec — registries legitimately point token requests at a separate auth endpoint (e.g. Docker Hub&#x27;s `registry-1.docker.io` -&gt; `auth.docker.io`), so cross-ho…

---

## 23. 🟡 High Severity — Rancher has Privilege Escalation from Project Owner to Host

**CVE:** `CVE-2026-41052` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-vx8h-4prv-g744>

> ### Impact

A vulnerability has been identified in Rancher Manager that allows users assigned the Project Owner role to modify Pod Security Admission (PSA) labels on namespaces within their projects. Under the default role configuration, an attacker with the following access pattern can exploit this issue:
1. **Cluster Access:** The user is granted Cluster Member access.
2. **Project Ownership:** …

---

## 24. 🟡 High Severity — Mailpit: Sibling-endpoint memory-exhaustion DoS via unbounded JSON body on /api/v1/messages, /api/v1/tags, and /api/v1/message/{id}/release (incomplete fix of GHSA-fpxj-m5q8-fphw)

**CVE:** `CVE-2026-48824` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-28pq-6qxg-wg5r>

> ### Summary

The fix for GHSA-fpxj-m5q8-fphw (CVE-2026-45710, &quot;Mailpit: Set a default 50MB p/m limit to prevent DoS via unlimited SMTP DATA and /api/v1/send body sizes&quot;) wrapped only `POST /api/v1/send` with `http.MaxBytesReader`. The four other Mailpit JSON-body API endpoints  `PUT /api/v1/messages` (SetReadStatus), `DELETE /api/v1/messages` (DeleteMessages), `PUT /api/v1/tags` (SetMess…

---

## 25. 🟡 High Severity — Rancher Fleet has SSRF in Bundle Reader via Unvalidated Helm Repository URL in fleet.yaml

**CVE:** `CVE-2026-44936` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-hx4v-cxpf-vh8m>

> ### Impact
A vulnerability has been identified in Fleet when the `helmRepoURLRegex` field isn&#x27;t set on a `GitRepo` resource. Fleet&#x27;s bundle reader forwards Helm authentication credentials (`BasicAuth`) to any URL specified in the `helm.repo` field of a `fleet.yaml` file.

An attacker with git push access to a Fleet-monitored repository can exploit this behavior by specifying a malicious …

---

## 26. 🟡 High Severity — Rancher vulnerable to command injection through unsanitized YAML parameter

**CVE:** `CVE-2026-44939` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-mhc6-2gfq-xx62>

> ### Impact
A critical command injection vulnerability has been identified in the Rancher Manager cluster import endpoint  `/v3/import/{token}_{clusterId}.yaml` through unsanitized YAML parameters. This endpoint accepts an `authImage` query parameter that is rendered without sanitization into a generated Kubernetes manifest template. By including URL-encoded newlines in the parameter value, an atta…

---

## 27. 🟡 High Severity — Rancher Fleet has Unauthenticated Webhook: Regex Injection via Unsanitized Repository URL Components

**CVE:** `CVE-2026-44937` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-jmf4-m7j9-g72r>

> ### Impact
A vulnerability has been identified in Fleet when the webhook endpoint is configured without a secret; an attacker can forge webhook requests. The attacker doesn&#x27;t need to know the specific repository or path configured in the GitRepo resource to make Fleet process these requests.

An attacker can exploit this vulnerability to cause the following impacts:
1. Trigger continuous repo…

---

## 28. 🟡 High Severity — Fleet has PSS Bypass through addLabelsFromOptions in Fleet Agent

**CVE:** `CVE-2026-44938` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-864g-863m-vcvq>

> ### Impact
A vulnerability has been identified in Fleet&#x27;s agent-side deployer, which did not filter security-sensitive keys from `namespaceLabels` in `fleet.yaml` (or `BundleDeployment.spec.options.namespaceLabels`) when applying them to the target namespace. 

An attacker with `git push` access to a Fleet-monitored repository could overwrite Pod Security Standards (PSS) enforcement labels on…

---

## 29. 🟡 High Severity — CrateDB's Blob HTTP handler bypasses authorization

**CVE:** `CVE-2026-49989` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-2xv8-gjwh-fv8p>

> **Component:** `io.crate.protocols.http.HttpBlobHandler`
**Affected:** verified against CrateDB 6.2.7 (latest at time of report; the bug has existed since the blob HTTP handler was introduced)
**Impact:** any authenticated user can read or delete any blob whose SHA-1 digest they know, and can plant new blobs unconditionally, in any blob table, regardless of `GRANT`s.

---

## Summary

CrateDB has …

---

## 30. 🟡 High Severity — repomix: attach_packed_output can bypass file-read secret scanning for supported local files

**CVE:** `CVE-2026-49988` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-hwpp-h97w-2h3j>

> # `attach_packed_output` can register arbitrary `.json/.txt/.md/.xml` files and bypass the MCP file-read safety check

## Summary

Repomix&#x27;s MCP server exposes a normal `file_system_read_file` tool that reads absolute paths only after running the project&#x27;s secret check. However, the `attach_packed_output` plus `read_repomix_output` flow can read arbitrary local `.json`, `.txt`, `.md`, or…

---

## 31. 🟡 High Severity — Twig: Sandbox filter, tag and function allow-list bypass when sandbox state changes between renders for a cached `Template`

**CVE:** `CVE-2026-49981` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-529h-vh3j-85hq>

> ### Description

The per-template filter, tag and function allow-list check is compiled into the `checkSecurity()` method of each `Template` subclass and was invoked once from the constructor, gated by `SandboxExtension::isSandboxed($source)`. `Template` instances are then cached on the `Environment` in `$loadedTemplates`, so the verdict computed at construction time was sticky for the rest of the…

---

## 32. 🟡 High Severity — Cortex has Untrusted Project Bootstrap Code Execution via `CLAUDE_PROJECT_DIR`

**CVE:** `CVE-2026-49986` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-gvpp-v77h-5w8g>

> ## Untrusted Project Bootstrap Code Execution via `CLAUDE_PROJECT_DIR`

### Summary

The Cortex MCP server (`neuro-cortex-memory`) treats the `CLAUDE_PROJECT_DIR` environment variable — automatically set by Claude Code to the currently open project directory — as a trusted Cortex developer checkout. When the `open_visualization` tool is invoked, `_find_dev_source()` resolves the user&#x27;s active…

---

## 33. 🟡 High Severity — auth-fetch-mcp has SSRF Protection Bypass via IPv4-mapped IPv6 Loopback

**CVE:** `CVE-2026-49857` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-pvrj-8cg3-j5f8>

> ## SSRF Protection Bypass via IPv4-mapped IPv6 Loopback

### Summary

`auth-fetch-mcp` v3.0.1 implements SSRF protection in `assertSafeUrl()` (`src/security.ts`) to block requests to private and loopback addresses. However, the `isPrivateV6()` function fails to detect IPv4-mapped IPv6 loopback addresses in their hex-normalized form. When an attacker supplies a URL such as `http://[::ffff:127.0.0.1…

---

## 34. 🟡 High Severity — @jshookmcp/jshook: ICMP probe and traceroute skip local-network SSRF authorization

**CVE:** `CVE-2026-49856` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-c5r6-m4mr-8q5j>

> ## Summary

The network domain has a central SSRF authorization policy that blocks private, loopback, link-local, and reserved targets unless an explicit authorization object allows private network access. The policy is enforced by raw HTTP/TCP/TLS RTT tools, but the ICMP probe and traceroute tools resolve the target and invoke the native ICMP/traceroute sink directly.

An MCP client with access t…

---

## 35. 🟡 High Severity — Open Babel has out-of-bounds write in Gaussian translationVectors[]

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

## 36. 🟡 High Severity — Progress Kemp LoadMaster Pre-Auth RCE Flaw Faces Active Exploitation Attempts

**CVE:** `CVE-2026-8037` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://thehackernews.com/2026/07/latest-progress-kemp-loadmaster-pre.html>

> A recently disclosed critical security flaw impacting Progress Kemp LoadMaster is seeing active exploitation attempts, according to an advisory from eSentire&#x27;s Threat Response Unit (TRU).

The Canadian cybersecurity company said it identified exploitation attempts targeting CVE-2026-8037 (CVSS score: 9.6), an operating system (OS) command injection flaw that could be exploited to achieve

---

## 37. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
