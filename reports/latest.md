# Zero Day Pulse

> **Generated:** 2026-06-06 08:24 UTC &nbsp;|&nbsp; **Total:** 26 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 13 &nbsp;|&nbsp; 🟡 High: 13 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal vulnerability that allows an attacker to read arbitrary files (logs, configuration files, credentials) from SimpleHelp installations via crafted requests to the web interface.
- **Affected Products:** SimpleHelp remote support / RMM software – versions 5.5.7 and earlier (including 5.5.x prior to 5.5.8, 5.4.x prior to 5.4.10, 5.3.x prior to 5.3.9).
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC exists; see OffSec blog for details.
- **Patch Available:** Yes — SimpleHelp released version 5.5.8 that fixes the vulnerability. Advisory/Download URL: https://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570
- **Active Exploitation:** Confirmed — CISA reports ransomware actors leveraged unpatched SimpleHelp (including CVE‑2024‑57727) to compromise downstream customers.
- **Threat Actors:** Ransomware actors (unspecified groups)
- **Mitigation:** Apply vendor patch/update to SimpleHelp 5.5.8 or later; if immediate patching not possible, restrict access to the SimpleHelp administrative interface (IP allow‑listing, network segmentation, deny internet exposure), block or filter malicious request patterns at the perimeter, rotate any exposed credentials, review logs for suspicious access, and conduct incident response if compromise is suspected.
- **Vendor Advisory:** https://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — AI Agent Uncovers 21 Zero-Days in FFmpeg; Chrome Patches Record 429 Bugs

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-06
**Reference:** <https://thehackernews.com/2026/06/ai-agent-uncovers-21-zero-days-in.html>

> Two things landed within days of each other this week. A security startup reported 21 previously unknown vulnerabilities in FFmpeg, the media library inside almost everything that touches video, all of them found by an autonomous AI agent.

The same week, Google shipped Chrome 149 with patches for 429 security bugs, the most ever in a single release.

Only the FFmpeg bugs were found by AI.

**Parallel AI Enrichment:**

- **Technical Details:** An integer overflow occurs when processing CENC subsample data in FFmpeg, causing an out‑of‑bounds write that can allow an attacker to execute arbitrary code (RCE).
- **Affected Products:** FFmpeg versions prior to 8.1
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof‑of‑concept exploits are available for several of the FFmpeg CVEs (e.g., CVE-2026-40962). See the CVE pages for details.
- **Patch Available:** An official patch is available; upgrading to FFmpeg version 8.1 or later resolves the vulnerabilities. See the CVE advisory for details.
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Upgrade FFmpeg to version 8.1 or later. If immediate upgrade is not possible, disable CENC subsample processing or restrict media inputs that use the vulnerable codec.
- **Vendor Advisory:** https://cvefeed.io/vuln/detail/CVE-2026-40962

---

## 3. 🟠 Zero-Day — MCP Server Kubernetes: kubectl-generic flag injection enables Kubernetes bearer token exfiltration

**CVE:** `CVE-2026-47250` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-6mx4-4h42-r8vh>

> ### Summary
The `kubectl_generic` tool in `mcp-server-kubernetes` passes user-supplied flags directly to kubectl without any allowlist, enabling a **privilege escalation attack** within Kubernetes environments. An attacker who already has limited cluster or codebase access, for example, a developer with pod-deployment permissions but not cluster-admin credentials, can plant a single structured JSO…

**Parallel AI Enrichment:**

- **Technical Details:** The `kubectl_generic` tool in `mcp-server-kubernetes` passes user‑supplied flags directly to `kubectl` without any allowlist, allowing an attacker with limited cluster access to inject structured JSON into application logs; when a privileged operator reads those logs, the injected flags cause `kubectl` to execute with attacker‑controlled arguments, leading to bearer token exfiltration.
- **Affected Products:** mcp-server-kubernetes (npm package) – kubectl_generic tool; specific versions unavailable
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit is known.
- **Patch Available:** No official patch has been released yet; mitigation guidance is provided in the vendor advisory.
- **Active Exploitation:** No confirmed active exploitation has been reported.
- **Threat Actors:** None known
- **Mitigation:** Avoid using `mcp-server-kubernetes` until patched; do not use `kubectl_generic` with privileged kubeconfigs; restrict operator access to privileged kubeconfigs; sanitize or disallow reading untrusted logs into privileged contexts; implement allow‑listing of kubectl flags and validate inputs.
- **Vendor Advisory:** https://github.com/advisories/GHSA-6mx4-4h42-r8vh

---

## 4. 🟠 Zero-Day — What 2026 DBIR Confirms: Attacks Are Living in the Browser

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://www.bleepingcomputer.com/news/security/what-2026-dbir-confirms-attacks-are-living-in-the-browser/>

> Phishing, shadow AI, malicious extensions, and credential theft increasingly happen inside the browser. Keep Aware explains what the 2026 Verizon DBIR reveals about browser-layer security gaps and modern attacks. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit information unavailable.
- **Patch Available:** Patch information unavailable.
- **Active Exploitation:** Active, widespread browser‑based credential theft observed by Keep Aware and reported in the Verizon 2026 DBIR.
- **Threat Actors:** None known
- **Mitigation:** Restrict/monitor extensions, implement allow‑list policies by extension ID, block risky AI extensions, deploy in‑browser DLP and credential‑protection tools, and provide user training on malicious‑extension and phishing risks.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when AI systems process web/email/document content that contains malicious instructions; Google's scan of Common Crawl found examples including data‑exfiltration and destructive instructions but mostly low‑sophistication experiments and pranks.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit reported; exploit_available: None known.
- **Patch Available:** Patch unavailable; mitigation guidance provided in the Google blog.
- **Active Exploitation:** Google observed a small number of malicious prompt injections and a 32% relative increase in detections between Nov 2025 and Feb 2026; no confirmed large‑scale exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses — pattern matching, LLM‑based classification, human validation; refer to Google’s Workspace continuous‑mitigation guidance and layered defense strategy.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is a class of attacks where an adversary injects malicious instructions into data sources or tools that a complex AI application consults while fulfilling a user query. Because the LLM can incorporate external content (documents, web pages, tool outputs) into its context or agentic planning, injected instructions in those sources can influence model behavior without direct user input. Attack flow typically: (1) attacker plants malicious payload in a data source or accessible tool output, (2) the AI agent retrieves that content while answering a user query or executing tasks, (3) the model follows the injected instructions, producing unwanted or harmful actions or outputs.
- **Affected Products:** Google Workspace (Gemini in Workspace and Workspace apps using multi‑source data); other LLM‑based multi‑data‑source agentic systems (specific versions unavailable)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public proof‑of‑concept or weaponized exploit reported
- **Patch Available:** No official patch; mitigation measures are described in the vendor advisory.
- **Active Exploitation:** Reports of increased indirect prompt injection attempts in the wild and observed payloads, but no confirmed, widely‑weaponized exploit tied to a specific CVE.
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses: content provenance and validation, input/output sanitization, strict tool access controls and scopes for agents, rate‑limiting and anomaly detection on tool outputs, prompt and instruction filtering on ingested data, user confirmation for high‑risk actions, and continuous monitoring and updates to detection rules.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability stems from insufficient policy enforcement in Chrome's <webview> tag. A malicious extension can use the declarativeNetRequest API to modify requests to gemini.google.com/app, inject JavaScript into the privileged Gemini WebView context, and thereby gain elevated permissions such as camera, microphone, file system access, screenshot capture, and arbitrary code execution.
- **Affected Products:** Google Chrome versions prior to 143.0.7499.192 (Desktop Stable), 143.0.7499.192 (Android), and 142.0.7444.265 (Extended Stable desktop).
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** A public PoC exploit is available and indexed via VulnCheck’s XDB, referencing a GitHub repository.
- **Patch Available:** Yes. Patch released in Chrome 143.0.7499.192+ for Linux, 143.0.7499.193+ for Windows/macOS, 143.0.7499.192 for Android, and 142.0.7444.265+ for Extended Stable desktop.
- **Active Exploitation:** No confirmed active exploitation in the wild has been reported.
- **Threat Actors:** None known
- **Mitigation:** Update Chrome to the patched versions, audit and allow‑list extensions, enable Chrome Enhanced Protection, avoid running browsers with local administrator accounts, consider browser isolation, and temporarily disable Gemini if not needed.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit details unavailable
- **Patch Available:** Patch availability varies by specific vulnerabilities; Google’s blog post (Rust in Android: move fast and fix things) summarizes platform‑wide progress but does not list per‑vulnerability advisories or patch URLs. For specific fixes, consult Android Security Bulletins and individual CVE advisories.
- **Active Exploitation:** Active exploitation reports unavailable
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) hides malicious instructions inside external content (emails, documents, calendar invites, images, URLs) that an LLM will read later; attackers aim to get the assistant to exfiltrate data or perform actions. Google’s layered defenses combine model hardening (Gemini 2.5 adversarial training), ML detectors for malicious instructions, markdown sanitization/suspicious‑URL redaction, security‑thought reinforcement, user confirmation/HITL, and system‑level safeguards.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit reported
- **Patch Available:** Google has deployed mitigations in Gemini (model hardening, detection, sanitization, URL redaction, user confirmation). See vendor advisory: http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html
- **Active Exploitation:** No confirmed active exploitation reported in the vendor advisory; Google has conducted monitoring but does not report a named active campaign.
- **Threat Actors:** None known
- **Mitigation:** Use layered controls: model hardening/adversarial training, ML‑based instruction detection, input sanitization (markdown/image URL blocking), suspicious‑URL redaction (Safe Browsing), security‑thought reinforcement, explicit user confirmation for risky actions, end‑user mitigation notifications, red‑team testing, and apply vendor guidance in Google’s Help Center (https://support.google.com/docs/answer/16204578).
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors compromise routers by injecting malicious code, configuring GRE tunnels to exfiltrate data, and leveraging trusted connections to pivot within networks, achieving persistent access.
- **Affected Products:** Backbone routers, provider edge (PE) routers, customer edge (CE) routers, IoT devices
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit or proof‑of‑concept is known.
- **Patch Available:** No official patch has been released.
- **Active Exploitation:** Yes, active exploitation has been reported.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Simulate the attack to test defenses, segment networks, enforce strong authentication on routers, apply available firmware updates, and monitor for unauthorized GRE tunnels or unusual traffic.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 11. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 12. 🟠 Zero-Day — Cisco Catalyst SD-WAN Manager CVE-2026-20245 Flaw Actively Exploited – No Patch Available

**CVE:** `CVE-2026-20245` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-06
**Reference:** <https://thehackernews.com/2026/06/cisco-catalyst-sd-wan-manager-cve-2026.html>

> Cisco has warned that a high-severity security flaw impacting Catalyst SD-WAN Manager has come under active exploitation.

The vulnerability, tracked as CVE-2026-20245, carries a CVSS score of 7.8 out of a maximum of 10.0. It affects the following deployment types -


  On-Prem Deployment
  Cisco SD-WAN Cloud-Pro
  Cisco SD-WAN Cloud (Cisco Managed)
  Cisco SD-WAN for Government (FedRAMP)

&quot;A

---

## 13. 🟠 Zero-Day — In Other News: Anthropic Maps AI Threats, Unpatched Comodo Flaw, Palantir Chief Eyed for CISA

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://www.securityweek.com/in-other-news-anthropic-maps-ai-threats-unpatched-comodo-flaw-palantir-chief-eyed-for-cisa/>

> Other noteworthy stories that might have slipped under the radar: Ultrahuman data leak, The Gentlemen ransomware analysis, Hola Browser bundles miner. The post In Other News: Anthropic Maps AI Threats, Unpatched Comodo Flaw, Palantir Chief Eyed for CISA appeared first on SecurityWeek .

---

## 14. 🟡 High Severity — Bugsink: Issue bulk actions can affect another project’s issue if its UUID is known

**CVE:** `CVE-2026-47716` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-g5vc-q7qc-v939>

> ### Description
Bugsink’s issue list supports bulk actions such as resolving or muting selected issues. In affected versions, the issue list view authorizes access through the project in the URL, but applies the requested bulk action to the submitted issue IDs without also requiring those issues to belong to that project.

This is a project-boundary authorization issue: a logged-in user with acces…

---

## 15. 🟡 High Severity — Bugsink: Issue event views can show an event from another project if its UUID is known

**CVE:** `CVE-2026-47715` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-vx2f-6m6h-9frf>

> ### Description

Bugsink issue event pages accept a direct event identifier from the URL and, in affected versions, look up that event without also requiring it to belong to the issue in the URL.

This is a project-boundary authorization issue: a logged-in user with access to one project can view another project’s event data through an issue they are allowed to access. However, the issue is mitiga…

---

## 16. 🟡 High Severity — Shopper: Authorization bypass and RBAC privilege escalation in team settings

**CVE:** `CVE-2026-47744` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-c3qp-2ggw-xjg7>

> ## Impact

Two distinct authorization defects in the team settings allowed any authenticated panel user to take over the RBAC system:

- `Settings/Team/Index` had no `mount()` authorization. Any authenticated user could load the page and use its public actions to create new roles and delete other users, including administrators.
- `Settings/Team/RolePermission` gated its write actions on the read-…

---

## 17. 🟡 High Severity — Weekly Metasploit Update: Apache ActiveMQ RCE, Gogs Rebase RCE, and Windows Kernel Pointer Enum

**CVE:** `CVE-2026-34197` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-05-06-2026>

> When Open Source is a bit too Open Several fun modules landed this week, including an Apache RCE, Windows Kernel pointer collection, and Gogs RCE via naming. Leading off is Gogs&#x27; RCE that allows an attacker to execute commands by naming their branch --exec and requesting a rebase. Another useful post module by CharlesQuinnDev enumerates the Kernel pointers leaked via the popular NtQuerySystem…

---

## 18. 🟡 High Severity — DbGate: Remote Code Execution via functionName injection in loadReader endpoint

**CVE:** `CVE-2026-48017` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-hv83-ggc4-v385>

> ### Summary

The `POST /runners/load-reader` endpoint in DbGate accepts a `functionName` parameter that is directly interpolated into a JavaScript code template without any sanitization or validation. An authenticated user (with basic access, no special permissions required) can inject arbitrary JavaScript code that executes on the server with full process privileges, bypassing the `require=null` …

---

## 19. 🟡 High Severity — Sync-in Server: SSRF protection bypass via IPv4-mapped IPv6 addresses in regExpPrivateIP

**CVE:** `CVE-2026-47684` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-q4x5-8cj6-52wg>

> Summary:
The private IP blocklist regex used in the URL download feature does not match IPv4-mapped IPv6 addresses (e.g. ::ffff:127.0.0.1), allowing SSRF protection to be bypassed on dual-stack systems.

Affected components

backend/src/applications/files/services/files-manager.service.ts – downloadFromUrl() checks regExpPrivateIP against request.socket.remoteAddress.
backend/src/applications/file…

---

## 20. 🟡 High Severity — Source controller: Improper path handling allows traversal

**CVE:** `CVE-2026-47680` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-jjrm-hr5f-673x>

> ### Impact

An actor with the ability to influence the contents of a bucket referenced by a `Bucket` resource can cause source-controller to write fetched object data to paths outside the per-reconciliation working directory.

The corruption surface is bounded by source-controller&#x27;s own and downstream Flux controllers&#x27; digest verification: source-controller verifies stored artifact diges…

---

## 21. 🟡 High Severity — Authenticated Remote Code Execution via loadReader functionName code injection in DbGate

**CVE:** `CVE-2026-47670` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-wm5r-5qp3-5vxf>

> ### Summary

DbGate is vulnerable to authenticated Remote Code Execution (RCE). Any user with valid DbGate credentials can execute arbitrary OS commands as root by exploiting an unsanitized `functionName` parameter in the `/runners/load-reader` endpoint. The `require = null` mitigation is trivially bypassed via dynamic `import()`.


&lt;br/&gt;

### Details

**Code injection via `functionName` in …

---

## 22. 🟡 High Severity — DbGate: Unauthenticated Remote Code Execution via JSON Script Runner

**CVE:** `CVE-2026-47668` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-8v3q-9vmx-36vc>

> ### Summary
DbGate&#x27;s JSON script runner (`POST /runners/start`) allows remote code execution via code injection in the `functionName` parameter of JSON script `assign` commands. The `functionName` value is interpolated directly into dynamically generated JavaScript source code via string concatenation. The generated code is then executed in a forked Node.js child process.

### Details
#### St…

---

## 23. 🟡 High Severity — NocoDB: Cross-Workspace Integration Use in Connection Test

**CVE:** `CVE-2026-47381` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-96fh-m4r8-6v9v>

> ### Summary
A user in one workspace could exercise another workspace&#x27;s integration through the
`testConnection` endpoint by supplying its ID, because the integration was fetched in
a bypass scope and the caller&#x27;s permission check matched any base in any workspace.

### Details
The connection-test endpoint fetched the integration in `RootScopes.BYPASS` scope and
checked only that the inte…

---

## 24. 🟡 High Severity — Omni: Reader-level users can retrieve imported cluster CA keys via ResourceService

**CVE:** `CVE-2026-45726` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-wv8c-6mx2-xf4j>

> ## Summary

Omni supports importing standalone Talos clusters.

During this process, an ImportedClusterSecrets resource is created, which contains the full CA secrets bundle for the cluster being imported.

If these secrets are not rotated by the importing actor, an authenticated Omni user with Reader access can read this resource and gain full access to the Talos, Kubernetes and etcd APIs of the …

---

## 25. 🟡 High Severity — Hackers Exploit Critical Everest Forms Pro WordPress Plugin Flaw to Take Over Sites

**CVE:** `CVE-2026-3300` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://thehackernews.com/2026/06/hackers-exploit-critical-everest-forms.html>

> Threat actors are actively exploiting a critical security flaw in Everest Forms Pro, a WordPress plugin with about 4,000 active installations, to execute arbitrary code, leading to a complete site compromise.

The vulnerability in question is CVE-2026-3300 (CVSS score: 9.8), a remote code execution bug impacting all versions of the plugin up to, and including, 1.9.12. A patch for the flaw was

---

## 26. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
