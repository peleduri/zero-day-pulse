# Zero Day Pulse

> **Generated:** 2026-07-02 02:05 UTC &nbsp;|&nbsp; **Total:** 38 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 15 &nbsp;|&nbsp; 🟡 High: 23 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a CWE-22 Path Traversal vulnerability in SimpleHelp remote support software v5.5.7 and earlier. Unauthenticated remote attackers can submit crafted HTTP requests that traverse out of the intended web directory and force the server to return arbitrary files. The flaw leaks server configuration files containing sensitive secrets (e.g., licensing keys, technician account configuration) and hashed user passwords — without credentials or user interaction. Attackers chained harvested credentials with CVE-2024-57726 and CVE-2024-57728 to escalate to administrative control and pivot into downstream customer networks.
- **Affected Products:** SimpleHelp Remote Support Software v5.5.7 and all earlier releases (available on Linux, Windows, and macOS). Affected lineages include the 5.5.x branch through 5.5.7, and older v5.4.x and v5.3.x lineages.
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Public proof-of-concept exploit is available at https://github.com/imjdl/CVE-2024-57727. Horizon3.ai published a technical disclosure at https://horizon3.ai/attack-research/disclosures/critical-vulnerabilities-in-simplehelp-remote-support-software/ detailing the underlying vulnerability chain. Offensive Security (OffSec) also published a working analysis.
- **Patch Available:** Yes — official vendor patches are available. SimpleHelp released v5.5.8 on January 8, 2025 (within two days of notification); v5.4.10 and v5.3.9 patches were also issued for older branches. Subsequent maintenance releases (v5.5.9, v5.5.10, v5.5.15) included additional hardening. Patch announcement: https://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570
- **Active Exploitation:** Yes — confirmed active exploitation in the wild. Reporting sources include: (1) CISA / FBI / MS-ISAC advisory AA25-163A, 'Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider' (June 12, 2025); (2) CISA Known Exploited Vulnerabilities (KEV) Catalog — CVE-2024-57727 added February 13, 2025, remediation due March 6, 2025; (3) Sophos, 'DragonForce actors target SimpleHelp vulnerabilities to attack MSP customers' (May 27, 2025); (4) Arctic Wolf observation of a SimpleHelp exploitation campaign beginning January 22, 2025; (5) Halcyon, ThreatDown (Malwarebytes), and Health-ISAC incident write-ups. Exploitation pattern: internet-exposed/unpatched SimpleHelp servers are scanned, CVE-2024-57727 is used to harvest configuration files and credentials, actors pivot to administrative takeover, and then move laterally to downstream MSP/MSSP customers for data theft and ransomware encryption.
- **Threat Actors:** DragonForce ransomware actors. Per CISA Advisory AA25-163A (Jun 12, 2025), DragonForce exploited unpatched SimpleHelp RMM instances to compromise a utility billing software provider and conduct double-extortion attacks against downstream MSP/MSSP customers since January 2025.
- **Mitigation:** Upgrade to SimpleHelp v5.5.8 or later on the 5.5.x branch (subsequent maintenance v5.5.9 / v5.5.10 / v5.5.15 recommended). For organizations that cannot immediately apply v5.5.8, apply the v5.4.10 patch (overwrite lib/shelp-jar-with-dependencies.jar) or v5.3.9 patch (overwrite secure_utils.jar, secure_nlink.jar, secure_shelp.jar). Additional hardening from vendor and CISA: (1) change the SimpleHelp Administrator password and all Technician account passwords; (2) restrict source IPs for Technician and Administrator logins and API requests; (3) restrict firewall connections to the server; (4) regenerate API tokens; (5) configure Server Event alerts on Administrator logins, failed logins, and configuration changes; (6) audit the server's Remote Access inventory; (7) isolate or stop unpatched internet-exposed servers; (8) for systems that were encrypted: disconnect from the internet, reinstall the OS from clean media, and restore from offline backups. CISA urges maintaining offline backups, avoiding exposing RDP to the internet, conducting an RMM risk-analysis, and adopting an SBOM.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — Rancher Fleet vulnerable to cross namespace secret disclosure via unvalidated `valuesFrom` references in Helm Deployer

**CVE:** `CVE-2026-44935` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-xr65-5cpm-g36x>

> ### Impact
A vulnerability in Fleet for Rancher Manager affects multi-tenancy environments where different tenants share the same downstream clusters (e.g., different privileged or untrusted teams inside the same organization). 

On unpatched versions, tenants could bypass restrictions to access any config map or secret across all namespaces on the downstream cluster. They can create cluster-wide …

**Parallel AI Enrichment:**

- **Technical Details:** The defect is in Fleet's Helm Deployer used by Rancher Manager. In multi-tenant deployments where tenants share the same downstream cluster, Fleet failed to fully restrict resources a tenant's GitRepo/HelmOp/Bundle could reach on the downstream cluster. Two abuse paths exist: (1) A tenant places a `valuesFrom` block in `fleet.yaml` (declared inside a GitRepo) or in a HelmOp referencing a Secret or ConfigMap by name+namespace+key; the Helm deployer resolves it with cluster-wide privileges, enabling cross-namespace secret/configmap reads. (2) A tenant can create cluster-scoped HelmOp and Bundle resources on the downstream cluster without being restricted to the designated per-tenant ServiceAccount, enabling unauthorized creation of cluster-wide resources. The attacker requires an account on the upstream Rancher/Fleet control-plane that allows authoring a GitRepo or HelmOp (e.g., by pushing to a tenant-owned git repo or holding a tenant Fleet-workspace role).
- **Affected Products:** Rancher Fleet (github.com/rancher/fleet): >= 0.15.0, < 0.15.2; >= 0.14.0, < 0.14.6; >= 0.13.0, < 0.13.11; >= 0.12.0, < 0.12.15. Rancher Manager releases bundling affected Fleet versions are also indirectly affected.
- **CVSS Score:** 9.9
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Exploit Available:** No public proof-of-concept (PoC) or weaponized exploit is publicly available for CVE-2026-44935. The mechanism (valuesFrom abuse in fleet.yaml or HelmOp) is described in the advisory and security write-ups, but no working exploit code has been published for this specific CVE.
- **Patch Available:** Yes. The SUSE Rancher security team released patched Fleet versions v0.15.2, v0.14.6, v0.13.11, and v0.12.15. Advisory: https://github.com/advisories/GHSA-xr65-5cpm-g36x (source: https://github.com/rancher/fleet/security/advisories/GHSA-xr65-5cpm-g36x).
- **Active Exploitation:** No confirmed in-the-wild exploitation has been publicly reported for CVE-2026-44935. As of the advisory's latest update (Jul 1, 2026), no threat-intelligence or incident-response source (SUSE Rancher, NVD, securityonline.info, gbHackers, Lyrie.ai, Proofpoint) reports observed exploitation of this specific CVE.
- **Threat Actors:** None known. No public reporting attributes this CVE to a specific APT, ransomware operator, or named threat-actor campaign.
- **Mitigation:** 1) Upgrade Fleet to a patched release: v0.15.2, v0.14.6, v0.13.11, or v0.12.15. 2) After upgrading, use the new Fleet Policy resource (per-namespace) to (a) require GitRepos/HelmOps/Bundles to run under a designated ServiceAccount on the downstream cluster, and (b) restrict HelmOp repository/chart URLs via the anchored regex (the Policy must be created in the namespace you want to restrict and only applies to that namespace). 3) Workaround if you cannot immediately upgrade: ensure no tenants share access to the same downstream cluster, and isolate tenants to distinct downstream clusters. 4) Review cluster and Fleet deployment logs for unauthorized cross-namespace access and rotate any service accounts/credentials that may have been exposed.
- **Vendor Advisory:** https://github.com/advisories/GHSA-xr65-5cpm-g36x

---

## 3. 🟠 Zero-Day — Unpatched Argo CD Repo-Server Flaw Could Let Attackers Take Over Kubernetes Clusters

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://thehackernews.com/2026/07/unpatched-argo-cd-repo-server-flaw.html>

> Argo CD, a widely used tool for deploying software to Kubernetes, has an unpatched flaw in its repo-server component that lets an unauthenticated attacker run code, provided they can reach the component&#x27;s internal network port.

Synacktiv, which found the bug, says it can lead to a full cluster takeover. There is no fix and no CVE. The firm says it reported the flaw to Argo CD&#x27;s maintain…

**Parallel AI Enrichment:**

- **Technical Details:** Argo CD exposes an internal gRPC service from the repo-server component on TCP port 8081 (the repository.RepoServerService endpoint, e.g. /repository.RepoServerService/GenerateManifest). This gRPC interface is unauthenticated, so any actor who can reach the port can invoke GenerateManifest without credentials. Inside that handler, attacker-controlled BuildOptions / KustomizeOptions values flow untrusted data into a command-injection sink that ultimately invokes the bundled kustomize binary (and any binary it is told to use via the --helm-command option). Because kustomize is invoked server-side with attacker-controlled arguments in the context of the repo-server pod, the attacker achieves arbitrary code execution as the repo-server user and can craft a poisoned manifest entry in the Argo CD Redis cache. When selfHeal is enabled, the application controller then applies that poisoned manifest to the cluster, producing full Kubernetes cluster takeover. Synacktiv discovered the issue with a custom CodeQL model pack against argo-cd-v2.13.3. Source: https://www.synacktiv.com/en/publications/caught-in-the-octopus-trap-unauthenticated-rce-in-argo-cd-with-codeql
- **Affected Products:** Argo CD by Argoproj — demonstrated against argo-cd-v2.13.3; the vulnerability remains unpatched across the current release line as of the July 1, 2026 disclosure. No specific vulnerable version range has been published by the researchers or the vendor.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept currently released. Synacktiv developed an exploitation tool named 'argo-cdown' that automates the Redis manifest-poisoning and gRPC exploit chain, but is deliberately withholding it: 'we are temporarily delaying the release of our exploitation tool, argo-cdown. It will be made available on our GitHub at a later date so administrators can safely verify if their deployments are vulnerable.' As of the disclosure date (July 1, 2026), the Synacktiv GitHub organization does not host an argo-cdown repository. Source: https://www.synacktiv.com/en/publications/caught-in-the-octopus-trap-unauthenticated-rce-in-argo-cd-with-codeql
- **Patch Available:** No official vendor patch is available. Synacktiv responsibly disclosed the vulnerability to the Argo CD maintainers in January 2025 and continued follow-ups via GitHub and email, but 'the vulnerability remains unpatched'. The Hacker News article likewise states there is 'no fix and no CVE', and no GitHub Security Advisory has been published in the argoproj/argo-cd security-advisories page. No CVE identifier has been assigned. Sources: https://www.synacktiv.com/en/publications/caught-in-the-octopus-trap-unauthenticated-rce-in-argo-cd-with-codeql ; https://github.com/argoproj/argo-cd/security/advisories
- **Active Exploitation:** No confirmed in-the-wild exploitation has been reported. Neither the Synacktiv technical write-up nor The Hacker News coverage mention any observed attacks, APT campaigns, or ransomware operators exploiting this flaw at the time of public disclosure (July 1, 2026). Synacktiv's stated motivation for publishing was to raise awareness and give defenders a window to apply network policies before weaponization becomes likely. Sources: https://www.synacktiv.com/en/publications/caught-in-the-octopus-trap-unauthenticated-rce-in-argo-cd-with-codeql ; https://thehackernews.com/2026/07/unpatched-argo-cd-repo-server-flaw.html
- **Threat Actors:** None known.
- **Mitigation:** Because there is no official patch, the only effective control is network-level isolation. Apply strict Kubernetes NetworkPolicies so that only Argo CD's own components (application controller, API server) can reach the repo-server's gRPC port (8081) and the Argo CD Redis port. Network policies are NOT applied by default when Argo CD is installed via Helm, so admins must add them explicitly. Verify coverage with 'kubectl get networkpolicy -A'. Until an official fix lands, restrict or remove any workloads that can dial those ports from within the cluster, and consider disabling auto-sync/selfHeal on applications to limit blast radius. Sources: https://thehackernews.com/2026/07/unpatched-argo-cd-repo-server-flaw.html and https://www.synacktiv.com/en/publications/caught-in-the-octopus-trap-unauthenticated-rce-in-argo-cd-with-codeql
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — Critical Cursor Flaws Could Let Prompt Injection Escape Sandbox and Run Commands

**CVE:** `CVE-2026-50548` | `CVE-2026-50549` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://thehackernews.com/2026/07/critical-cursor-flaws-could-let-prompt.html>

> Two flaws in Cursor, an AI code editor, could let a single, ordinary-looking prompt break out of the editor&#x27;s safety sandbox and run any command on a developer&#x27;s computer. There is no click to fall for and no approval box to ignore.

Cato AI Labs found the pair and named them DuneSlide. They are tracked as CVE-2026-50548 and CVE-2026-50549, both rated 9.8 out of 10 (or 9.3

**Parallel AI Enrichment:**

- **Technical Details:** CWE-22 path traversal in the run_terminal_cmd agent tool. An attacker uses prompt injection (e.g., via untrusted MCP server content, web search results, README, or repository context) to direct Cursor's AI agent to set its working_directory parameter to a path outside the intended project workspace. Cursor's sandbox automatically grants write access to whatever directory is supplied as working_directory. The injected instructions then direct the agent to overwrite a file on that path — for example, on macOS, /Applications/Cursor.app/Contents/Resources/app/resources/helpers/cursorsandbox (the sandbox helper binary), or the user's shell startup file ~/.zshrc. After the sandbox helper is replaced, subsequent commands run with no sandbox restriction, yielding unsandboxed remote code execution on the developer's machine with no clicks, approvals, or visible warnings.
- **Affected Products:** Cursor AI code editor (all versions prior to 3.0; fixed in version 3.0)
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable. (The NVD entry and Cursor's GitHub advisory publish only a CVSS v4.0 vector: CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N. No CVSS v3 vector string is publicly available.)
- **Exploit Available:** No public proof-of-concept or weaponized exploit is publicly known at this time. OpenCVE/NVD show no EPSS data, and Strobes vulnerability intelligence explicitly states 'No known public exploits at this time'. The discoverer (Cato AI Labs) published a technical write-up but did not release a ready-to-run exploit. Not listed in CISA KEV.
- **Patch Available:** Yes. An official vendor patch has been released in Cursor version 3.0. Advisory URL: https://github.com/cursor/cursor/security/advisories/GHSA-3p48-7v9f-v5cw (companion: https://github.com/cursor/cursor/security/advisories/GHSA-3v8f-48vw-3mjx). Advisory publication date: June 5, 2026; coordinated public disclosure: July 1, 2026.
- **Active Exploitation:** None known. No source reports confirmed in-the-wild exploitation of CVE-2026-50548. The vulnerability is not listed in the CISA Known Exploited Vulnerabilities (KEV) catalog at time of disclosure.
- **Threat Actors:** None known
- **Mitigation:** Primary fix: Upgrade Cursor to version 3.0 or later, which closes this vulnerability (both DuneSlide flaws CVE-2026-50548 and CVE-2026-50549 are fixed in 3.0). Hardening advice until upgraded: Avoid letting the Cursor agent process untrusted content (unvetted MCP servers, web-search results, untrusted repo text) that could carry prompt-injection payloads; restrict permission scope of agent processes; validate/sanitize any working_directory value before it is passed to the agent's terminal command runner if prompts are generated programmatically.
- **Vendor Advisory:** https://github.com/cursor/cursor/security/advisories/GHSA-3p48-7v9f-v5cw

---

## 5. 🟠 Zero-Day — Anthropic Restores Claude Fable 5 After U.S. Lifts Jailbreak-Linked Export Controls

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://thehackernews.com/2026/07/anthropic-restores-claude-fable-5-after.html>

> Anthropic is putting Claude Fable 5 back online worldwide. On June 30, the U.S. Commerce Department lifted the export controls it had imposed on Fable and its more tightly controlled sibling Mythos 5 about two and a half weeks earlier.

Fable 5 returns to users on Wednesday, July 1, across Claude.ai, the Claude Platform, Claude Code, and Claude Cowork.

Export controls restrict who can

**Parallel AI Enrichment:**

- **Technical Details:** Prompt-based safety-guardrail jailbreak on Claude Fable 5. Innocuous-sounding rephrasing — most notably 'fix this code' or 'read this codebase and fix software flaws' in place of 'find vulnerabilities in this code' — causes Fable 5 to identify software flaws and generate example exploitation code. Researchers augmented this technique with role inversion, alternative framing, and contextual reinterpretation. Anthropic characterizes the bug as a 'narrow, non-universal jailbreak' limited to the specific vulnerability-identification behavior.
- **Affected Products:** Anthropic Claude Fable 5, Anthropic Claude Mythos 5
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — public PoC exists. Pliny the Liberator published a jailbreak demonstration on X/Twitter (https://x.com/elder_plinius/status/2064776322979676227). The 'fix this code' / 'read this codebase and fix software flaws' prompt-framing technique was widely circulated. Anthropic opened a HackerOne disclosure program on July 1, 2026 (https://hackerone.com/anthropic-cyber-jailbreak/).
- **Patch Available:** Yes — Anthropic redeployed Claude Fable 5 and restored Claude Mythos 5 access on June 30, 2026 (user access restored July 1, 2026) with the new safety classifier as the patch. Reference: https://www.anthropic.com/news/redeploying-fable-5
- **Active Exploitation:** Yes, publicly demonstrated exploitation by researchers. Pliny the Liberator showed working jailbreaks of Fable 5 on X/Twitter; Amazon researchers independently demonstrated the same 'fix this code' technique and reported it to the U.S. government (per Axios on June 13, 2026). No reports of malicious in-the-wild exploitation by criminal or state-sponsored threat actors were identified. Reporting sources: https://www.securityweek.com/anthropic-disputes-fable-5-ai-jailbreak/, https://www.axios.com/2026/06/13/anthropic-amazon-white-house, https://x.com/elder_plinius/status/2064776322979676227.
- **Threat Actors:** None known
- **Mitigation:** Anthropic deployed a new independent safety classifier targeting the reported 'fix this code' style technique; blocked requests are routed/redelegated to Claude Opus 4.8. The classifier is reported to block >99% of the originally reported technique. Anthropic also tuned the classifier conservatively, increasing false-positive flagging for benign debugging prompts. External analysts recommend cross-product adversarial red-teaming in addition to prompt-level testing.
- **Vendor Advisory:** https://www.anthropic.com/news/redeploying-fable-5

---

## 6. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an AI-specific vulnerability class in which an attacker plants hidden malicious instructions inside untrusted third-party content (web pages, emails, documents, calendar events, etc.) that an LLM-powered system later ingests. When the AI reads the 'poisoned' content it follows the attacker's instructions in preference to, or in addition to, the user's original request — enabling data exfiltration, destructive file/system actions (e.g. instructing the agent to run 'sudo rm -rf'), payment fraud, SEO/attribution hijack, DoS, and credential theft. Hiding/obfuscation techniques documented in the wild include HTML comments (<!-- … -->), CSS invisibility (display:none, font-size:1px, rgba(_, 0.01)), accessibility-attribute abuse (aria-hidden, visually-hidden), meta-tag/semantic-namespace spoofing, system-prompt tag impersonation, magic-string/internal-token spoofing, copyright-law invocation as cover, and conditional LLM targeting via prompts such as 'If you are an AI…'. Google measured a 32% relative increase in malicious IPI attempts between November 2025 and February 2026.
- **Affected Products:** Google Gemini (consumer app and Gemini in Workspace apps, including Gmail and Docs), Google Workspace with Gemini, Google Chrome agentic capabilities, and the broader agentic AI ecosystem (ChatGPT, Microsoft Copilot, GitHub Copilot, Cursor, Claude Code, AI-powered CI/CD reviewers, and AI-based ad-validation/moderation systems). Common Crawl-derived data sources are also flagged as potential attack surface.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — weaponized real-world payloads (not a single PoC, but multiple live in-the-wild samples). Forcepoint X-Labs documented 10 distinct IPI payloads caught in the wild on 22 April 2026 across domains including thelibrary-welcome[.]uk, kassoon[.]com, luminousmen[.]com, faladobairro[.]com, lawsofux[.]com, lcpdfr[.]com, and archibase[.]co — spanning data exfiltration, SEO hijack, destructive agent commands ('sudo rm -rf'), DoS, attribution spoofing, and fraud. Sources: https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads and https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/ (Palo Alto Unit 42, 3 March 2026). Educational/reusable payload collections: https://swisskyrepo.github.io/PayloadsAllTheThings/Prompt%20Injection/
- **Patch Available:** No CVE-issued patch — the post is a threat-landscape report, not a single CVE advisory. However Google has shipped continuous defensive updates across Gemini, Workspace with Gemini, and Chrome agentic features (User Alignment Critic, Agent Origin Sets, user-confirmation framework, prompt-injection classifiers). Advisory/mitigation references: https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/ and https://www.securityweek.com/google-fortifies-chrome-agentic-ai-against-indirect-prompt-injection-attacks/
- **Active Exploitation:** Confirmed active exploitation in the wild. Google observed a 32% relative increase in the malicious IPI category between November 2025 and February 2026 (figures from the article itself). Independently corroborated by Forcepoint X-Labs (10 live IPI payloads across real domains), Palo Alto Unit 42 (web-based IPI targeting ad-validation AI agents, 3 March 2026), and analyzed by Help Net Security (24 April 2026, https://www.helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild/) and SecurityWeek (27 April 2026, https://www.securityweek.com/malicious-ai-prompt-injection-attacks-increasing-but-sophistication-still-low-google/). Abuse patterns documented include pranks, SEO manipulation, data/IP/credential exfiltration to attacker-controlled endpoints, and destructive file actions against agentic AI with shell access.
- **Threat Actors:** None known. The article is a threat-intelligence/landscape report (not a vulnerability advisory for a single CVE) and does not name any specific APT groups, ransomware operators, or named attacker campaigns. Forcepoint's parallel '10 IPI Payloads' research also explicitly states no actor names were identified.
- **Mitigation:** Google's layered defense (per https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/ and https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini): (1) prompt-injection content classifiers (proprietary ML detection across formats); (2) 'security thought reinforcement' — targeted system-instruction text that reminds the model to ignore adversarial instructions; (3) markdown sanitization + suspicious-URL redaction via Google Safe Browsing to prevent URL-based exfil; (4) a user-confirmation framework requiring explicit approval for risky operations (payments, deletes, sign-ins); (5) end-user security-mitigation notifications; (6) Gemini model adversarial robustness (hardening via synthetic data from a vulnerability catalog). Chrome agentic-specific mitigations (Dec 2025): a 'User Alignment Critic' Gemini model that vets planner actions against the user's goals, expanded 'Agent Origin Sets' (tightened Site Isolation / same-origin scope), deterministic + model-based user confirmations for impactful actions, and a prompt-injection classifier running in parallel with the planner. Defensive discovery sources: human red-team, automated red-team, and the Google AI Vulnerability Reward Program. Forcepoint's general guidance: enforce a strict data-vs-instruction boundary, and analyze context for concealment mechanisms rather than pattern-matching trigger phrases alone.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html (canonical mirror: https://blog.google/security/prompt-injections-web/) — Google Security Blog post 'AI threats in the wild: The current state of prompt injections on the web', published 2026-04-23 by Thomas Brunner, Yu-Han Liu, and Moni Pande.

---

## 7. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) lets an attacker influence an LLM's (Gemini's) behavior by embedding malicious instructions into external content the model ingests as part of fulfilling a user task — emails, Google Docs/Slides, Drive files, shared links, calendar events, or third-party web pages. The trigger lives in the data, so it can execute 'without any input directly from the user.' Obfuscation techniques include HTML-comment embedding, 1-pixel / white-on-white text, CSS display:none, ARIA-hidden/visually-hidden attributes, meta tag namespace spoofing, system-prompt tag impersonation, magic-string spoofing, copyright-law invocation, and persuasion amplifiers (e.g., 'ultrathink'). Demonstrated outcomes include phishing content injection (fake password-reset pages inside Gemini summaries), output/attribution hijacking, semantic poisoning, system-prompt leakage, data destruction, API-key exfiltration, traffic/SEO hijacking, and AI denial-of-service.
- **Affected Products:** Google Workspace with Gemini (Gemini integrations in Gmail, Google Docs, Slides, Drive, Chat, and Calendar), the standalone Gemini app, and the Gemini 2.5 model family. Specific per-product version numbers are not publicly published.
- **CVSS Score:** 7.6
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — multiple public PoCs and in-the-wild observations exist:
- SafeBreach Labs (Aug 2025): hijacked Gemini Voice Assistant via WhatsApp, Slack, SMS, Signal, Instagram, Messenger (https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/)
- HiddenLayer (Sep 2024): Gemini for Workspace phishing/content manipulation via speaker notes, shared documents, and emails (https://www.hiddenlayer.com/research/new-gemini-for-workspace-vulnerability-enabling-phishing-content-manipulation)
- 0din.ai 'Phishing For Gemini' (Jul 2025): IPI hidden in white-text email instructions hijacking Gemini's Gmail summary (https://0din.ai/blog/phishing-for-gemini)
- Cyera Research Labs: command/prompt injection in Gemini CLI (https://www.cyera.com/research/cyera-research-labs-discloses-command-prompt-injection-vulnerabilities-in-gemini-cli)
- Palo Alto Unit 42: web-based IPI observed in the wild against LLM-powered AI agents (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/)
- Forcepoint X-Labs (Apr 2026): 10 verified in-the-wild IPI payloads spanning financial fraud, data destruction, API key exfiltration, and AI denial-of-service (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads)
- **Patch Available:** No single discrete patch — Google deploys continuous configuration updates, classifier retraining, system-prompt refinements, and model hardening rather than a versioned CVE fix. The SafeBreach-disclosed Gemini Voice Assistant exploit (Aug 2025) was mitigated via 'content classifier updates.' The April 2, 2026 blog functions as the ongoing vendor advisory: http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html
- **Active Exploitation:** Yes — confirmed active exploitation in the wild has been reported:
- Forcepoint X-Labs (April 22, 2026): 10 verified IPI payloads targeting AI assistants, agentic browsers, and coding assistants (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads)
- Palo Alto Unit 42 (March 2026): web-based IPI observed in the wild across multiple ad-review-product AI agents and domains (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/)
- Help Net Security (April 24, 2026): IPI 'taking hold in the wild' (https://www.helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild/)
- Google's own April 2, 2026 blog describes IPI as an 'evolving threat vector' being weaponized against Workspace with Gemini [1].
- **Threat Actors:** None known
- **Mitigation:** Google's documented defense-in-depth strategy for Workspace with Gemini (layered, continuously updated):
1. Deterministic defenses — human-in-the-loop user-confirmation framework for risky actions, URL sanitization and redaction of suspicious URLs (leveraging Google Safe Browsing), and tool-chaining policies.
2. ML-based defenses — prompt-injection content classifiers (proprietary ML models detecting malicious instructions in emails, files, and other formats) and retraining of Gemini models with synthetic adversarial data.
3. LLM-based defenses — refined system instructions ('security thought reinforcement') directing the model to prioritize the user's task over instructionsfound in untrusted data.
4. Model hardening — improving Gemini's internal capability to identify and ignore harmful instructions.
5. Markdown sanitization of retrieved/ingested content.
6. End-user security mitigation notifications — contextual warnings and 'Learn more' links when a defense is triggered.
For administrators/users: limit Gemini summarization of untrusted external content, restrict which Workspace apps may pass external data to Gemini, keep human-in-the-loop confirmations enabled for tool use, monitor for end-user mitigation notifications, and apply Google's Workspace Gemini feature updates as they ship.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 8. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) in agentic Chrome: the on-device agentic planning model consumes untrusted web content (HTML/text from malicious sites, third-party iframes, user-generated content such as reviews/social posts, embedded images, emails, and documents) when deciding what actions to take for the user. Adversaries hide instructions inside that content so the agentic planner interprets them as user/system intent, enabling goal hijacking (perform unintended actions), data exfiltration (read page-local data, drive downloads, send messages), unauthorized financial transactions, and account-takeover pivots. Related CVE-2026-0628 is a missing policy enforcement in Chrome's WebView tag chain: a low-privilege extension using the declarativeNetRequest API could tamper with traffic to gemini.google.com/app in the 'Live in Chrome' side panel, inject JavaScript into that privileged component, and inherit Gemini's camera, microphone, screenshot, and local-file-access capabilities without new consent prompts.
- **Affected Products:** Google Chrome with Gemini in Chrome and agentic browsing capabilities (Chrome 142+ line); Gemini in Workspace apps (Gmail, Docs editors, Drive, Chat); Gemini app; adjacent CVE-2026-0628 affects Google Chrome prior to 143.0.7499.192
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC is referenced in the original Google vendor advisory; however, multiple related IPI proof-of-concepts and in-the-wild payloads have been published: Noma Labs 'GeminiJack' (https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/), Unit 42 demonstration of CVE-2026-0628 (https://unit42.paloaltonetworks.com/gemini-live-in-chrome-hijacking/), Forcepoint X-Labs '10 Indirect Prompt Injection Payloads Caught in the Wild' (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads), and HiddenLayer/0din.ai Gemini-for-Workspace IPI (https://0din.ai/blog/phishing-for-gemini).
- **Patch Available:** Yes. Protections for the IPI threat class ship via Chrome's automatic-update channel, with the December 2025 advisories describing a combination of browser-side and Gemini-side architectural changes rather than a discrete build number. For the related CVE-2026-0628 Chrome-extension hijack, Google released Chrome 143.0.7499.192 in the January 2026 stable-channel update (https://chromereleases.googleblog.com/2026/01/stable-channel-update-for-desktop.html; Chromium issue https://issues.chromium.org/issues/463155954). For GeminiJack (Gemini Enterprise/Vertex AI Search), Google updated the RAG processing pipeline and fully separated Vertex AI Search from Gemini Enterprise; no CVE was assigned for that finding.
- **Active Exploitation:** Google's primary vendor advisory does not report confirmed in-the-wild exploitation, and OffSeq Threat Radar states 'no known exploits have been reported in the wild' for the adjacent CVE-2026-0628. However, multiple independent research reports confirm active exploitation of related IPI vulnerabilities against AI assistants and agentic browsers: (1) Noma Labs 'GeminiJack' zero-click exfiltration in Gemini Enterprise disclosed 2025-12-08 (https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/); (2) Forcepoint X-Labs documented 10 IPI payloads actively observed in the wild 2026-04-22 (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads); (3) Unit 42 'Web-Based Indirect Prompt Injection Observed in the Wild' 2026-03-03 (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/); (4) Help Net Security 'Indirect prompt injection is taking hold in the wild' 2026-04-24 (https://www.helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild/). No named APT or ransomware operator has been publicly tied to these campaigns.
- **Threat Actors:** None known
- **Mitigation:** Apply Google's layered defense-in-depth mitigations: (1) User Alignment Critic—an isolated Gemini-based model inspecting only action metadata, never unfiltered untrusted web content, vetoing misaligned actions. (2) Agent Origin Sets—expanded Site Isolation restricting agent actions to task-related origins. (3) User-Confirmation Framework—deterministic and model-based human-in-the-loop checks for sensitive sites (banking, payments), Google Password Manager sign-ins, and calendar/event edits. (4) Prompt-injection classifier—runs alongside the planning model to block actions whose inputs are classified as IPI. (5) Spotlight/grounding to distinguish trusted system/user instructions from untrusted page content. (6) Google Safe Browsing real-time URL scanning, on-device scam detection, and Markdown sanitization of suspicious links. (7) Continuous automated red-teaming and public-web sweeps for IPI patterns. For the adjacent CVE-2026-0628 Chrome-extension hijack, update Chrome to ≥143.0.7499.192 and minimize use of untrusted extensions. Hardening advice generally includes requiring human approval for sensitive actions, input/output validation where possible, and avoiding fully autonomous agent use on untrusted sites.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 9. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2025-48530 is a linear buffer overflow / out-of-bounds memory access (CWE-125) in CrabbyAVIF, an AVIF (AV1 Image File) parser/decoder implemented in (unsafe) Rust for the Android platform. The vulnerability is caused by incorrect bounds checks in multiple locations of the NV12-color-format decoding path, producing OOB accesses on YUV planes, the alpha plane, the Y plane, the UV planes, chroma-width and plane-size calculations, and row-byte computations. If theoretically exploitable, the chain of allocate→decoder write→copy/access could lead to remote code execution with no additional execution privileges and no user interaction. In practice, Android's Scudo hardened user-mode allocator surrounds secondary allocations with guard pages, converting silent memory corruption into a noisy crash that surfaced the bug before it shipped.
- **Affected Products:** Google Android (AOSP version 16) — CrabbyAVIF (AVIF/AV1 Image File parser/decoder component written in Rust). Affects Android versions prior to security patch level 2025-08-01.
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** No public proof-of-concept or weaponized exploit is publicly available for CVE-2025-48530. SentinelOne explicitly reports 'No public exploit code available; Known Exploited: No'. The vulnerability was caught internally by Google before being shipped, mitigating the risk of weaponization.
- **Patch Available:** Yes. Official patch is available via Android Security Bulletin—August 2025 (https://source.android.com/docs/security/bulletin/2025-08-01), which includes two AOSP fix commits in the CrabbyAVIF repository: (1) https://android.googlesource.com/platform/external/rust/crabbyavif/+/9bcc1a311114ab844b417d3cdec50dcedfd0603f and (2) https://android.googlesource.com/platform/external/rust/crabbyavif/+/42feb427a42afd9eebe6391a0d8a7b083fe82140 (commit message '[25Q2-release] crabbyavif fixes for NV12 crashes', author Vignesh Venkatasubramanian, Google, dated May 8, 2025). Tenable also references https://android.googlesource.com/platform/external/rust/crabbyavif/+/87124e11e14f2f6fed75d57f5723ddab37cd4bff.
- **Active Exploitation:** No confirmed active exploitation in the wild. Google's blog post states the vulnerability 'was a near-miss' that was avoided from shipping. The Android Security Bulletin—August 2025 does not flag it as 'Actively exploited'. SentinelOne reports 'Known Exploited: No' with EPSS probability ~0.13%. (Note: a Tenable page asserts active exploitation; this is contradicted by Google's official narrative and the Android Security Bulletin and should be treated as unverified.)
- **Threat Actors:** None known. The vulnerability was caught internally by Google before being shipped to any public release, so there has been no opportunity for threat actor exploitation. The Android Security Bulletin—August 2025 does not flag this CVE as actively exploited, and the Google Security Blog explicitly characterizes it as a 'near-miss'.
- **Mitigation:** Apply the Android Security update with security patch level 2025-08-01 or later. Google's Scudo hardened allocator already provides defense-in-depth: its guard pages around secondary allocations detect/contain the OOB write. This is precisely the mechanism by which the bug was originally surfaced and contained pre-release, demonstrating the value of memory safety infrastructure beyond Rust's compile-time guarantees.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 10. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection embeds hidden, model-bound instructions inside untrusted content ingested by an LLM (e.g., the body of an email, a document, or a calendar invite). Unlike direct prompt injection, the malicious instruction never has to be typed by the user — it arrives as 'data'. When the LLM processes that data, the hidden instruction behaves like a system-level command, causing the model to perform rogue actions on the user's behalf (exfiltrate data, modify or delete content, affect model behavior). The Google post cites CVE-2025-32711 ('EchoLeak') in Microsoft 365 Copilot as a zero-click representative example in which prompt injection caused sensitive organizational data to be leaked through rendered images.
- **Affected Products:** Google Gemini (Gemini 2.5 family of models, the Gemini consumer app, Gemini in Google Workspace, the Gemini Voice Assistant / Android Utilities agent), Gmail, Google Calendar
- **CVSS Score:** 9.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — public proofs-of-concept exist: (a) SafeBreach Labs PoC hijacking Google Gemini Voice Assistant via WhatsApp/Slack — https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/; (b) Aim Security PoC for CVE-2025-32711 ('EchoLeak') zero-click Microsoft 365 Copilot data exfiltration — https://www.aim.security/lp/aim-labs-echoleak-m365.
- **Patch Available:** Yes — for the Google GenAI products in scope, Google is rolling out model and classifier defenses in production. Concretely, the SafeBreach Gemini Voice Assistant hijack report (2025-08-17) was mitigated by Google on 2025-11-14 via content-classifier and prompt-handling updates (no Google CVE number was issued). For the related industry issue referenced as motivation, Microsoft issued a patch for CVE-2025-32711 ('EchoLeak') — MSRC advisory: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32711.
- **Active Exploitation:** Yes — confirmed in-the-wild exploitation of the broader indirect-prompt-injection class. Sources: (1) Palo Alto Unit 42, 'Web-Based Indirect Prompt Injection Observed in the Wild' (2026-03) — first observed real-world case in December 2025 against an AI product-ad-review system using 22 payload-engineering techniques — https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/; (2) HelpNetSecurity summary (2026-04) of Google telemetry — 32% relative increase in malicious IPI activity November 2025–February 2026 across 2–3 billion crawled pages/month — https://www.helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild/; (3) Google Security Blog follow-up 'AI threats in the wild: The current state of prompt injections' (2026-04) — https://blog.google/security/prompt-injections-web/. No exploitation of the specific 2025-06-13 mitigation announcement against Google's flagship Gemini/Gmail/Calendar surfaces has been publicly reported.
- **Threat Actors:** None known
- **Mitigation:** Google's layered defense strategy: (1) Model hardening — adversarial-data training of Gemini 2.5 models to resist injected instructions; (2) Prompt-injection content classifiers — proprietary ML models that scan untrusted content (emails, files, web pages) and block or strip malicious instructions before the LLM acts on them; (3) Security thought reinforcement — locked-in system-style instructions that steer the LLM to ignore adversarial content; (4) Markdown sanitization + suspicious-URL redaction — strip rendered markdown and block external image URLs (mitigating EchoLeak-style data exfiltration), combined with Google Safe Browsing; (5) Human-In-The-Loop (HITL) — require explicit user confirmation for sensitive operations (e.g., deleting a calendar event) before the agent executes them; (6) End-user notifications — surface contextual alerts and 'Learn more' links when a defense has mitigated an attempted attack, plus an in-product feedback channel for false positives/negatives.
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

## 15. 🟠 Zero-Day — Phantom Squatting Uses AI-Hallucinated Domains for Phishing and Malware

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://thehackernews.com/2026/07/phantom-squatting-uses-ai-hallucinated.html>

> Large language models keep inventing web addresses that do not exist. Attackers have started buying those made-up domains before anyone else can, then hosting phishing pages on them to catch traffic that AI tools point their way.

Palo Alto Networks&#x27; Unit 42 calls the trick phantom squatting, and its new research shows it is already happening in the wild.

The reason it matters is

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

## 37. 🟡 High Severity — Citrix Patches Six NetScaler Flaws Allowing File Read and Denial-of-Service

**CVE:** `CVE-2026-8451` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://thehackernews.com/2026/07/citrix-patches-six-netscaler-flaws.html>

> Citrix on Tuesday released security updates to address multiple flaws in NetScaler ADC (formerly Citrix ADC) and NetScaler Gateway (formerly Citrix Gateway) that could be exploited by an attacker to facilitate arbitrary file reads or trigger a denial-of-service (DoS) condition.

The vulnerabilities are listed below -


  CVE-2026-8451 (CVSS score: 8.8) - An insufficient input validation

---

## 38. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
