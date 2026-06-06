# Zero Day Pulse

> **Generated:** 2026-06-06 01:59 UTC &nbsp;|&nbsp; **Total:** 25 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 13 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is a directory/path traversal flaw that lets unauthenticated attackers read arbitrary files on the SimpleHelp server.
- **Affected Products:** SimpleHelp remote support software version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof‑of‑concept discussion is available at https://www.offsec.com/blog/cve-2024-57727/
- **Patch Available:** Patch is available in SimpleHelp version 5.5.8; download at https://simple-help.com/downloads
- **Active Exploitation:** Confirmed active exploitation in the wild by ransomware actors exploiting unpatched SimpleHelp instances.
- **Threat Actors:** Ransomware actors (unspecified) as reported by CISA
- **Mitigation:** Change administrator and technician passwords, restrict IP addresses, isolate the SimpleHelp server, and upgrade to SimpleHelp v5.5.8 (or apply patches for 5.4.10 and 5.3.9).
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — MCP Server Kubernetes: kubectl-generic flag injection enables Kubernetes bearer token exfiltration

**CVE:** `CVE-2026-47250` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-6mx4-4h42-r8vh>

> ### Summary
The `kubectl_generic` tool in `mcp-server-kubernetes` passes user-supplied flags directly to kubectl without any allowlist, enabling a **privilege escalation attack** within Kubernetes environments. An attacker who already has limited cluster or codebase access, for example, a developer with pod-deployment permissions but not cluster-admin credentials, can plant a single structured JSO…

**Parallel AI Enrichment:**

- **Technical Details:** The kubectl_generic tool in mcp-server-kubernetes passes user‑supplied flags directly to kubectl without any allowlist; an attacker can inject a crafted JSON line into logs that causes a privileged operator or AI agent to run kubectl with attacker‑controlled flags, enabling Kubernetes bearer token exfiltration.
- **Affected Products:** mcp-server-kubernetes (npm package) – specific versions not listed
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit reported
- **Patch Available:** Vendor advisory posted; patch details not provided in the advisory.
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Do not use unvalidated user‑supplied flags; upgrade to a patched version if released; restrict operator access and avoid using privileged kubeconfigs when viewing untrusted logs; sanitize or filter log content before passing to kubectl_generic.
- **Vendor Advisory:** https://github.com/advisories/GHSA-6mx4-4h42-r8vh

---

## 3. 🟠 Zero-Day — What 2026 DBIR Confirms: Attacks Are Living in the Browser

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://www.bleepingcomputer.com/news/security/what-2026-dbir-confirms-attacks-are-living-in-the-browser/>

> Phishing, shadow AI, malicious extensions, and credential theft increasingly happen inside the browser. Keep Aware explains what the 2026 Verizon DBIR reveals about browser-layer security gaps and modern attacks. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Attackers are shifting initial access and data‑exfiltration vectors into the browser: credential theft via phishing or page/script interception, malicious or high‑risk extensions that can read/modify page content and exfiltrate data, ClickFix social‑engineering that executes code from the browser onto the host, and Shadow AI where users paste sensitive data into personal AI services outside corporate DLP visibility.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability information unavailable
- **Patch Available:** Patch information unavailable.
- **Active Exploitation:** Active in‑the‑wild browser‑based credential theft, malicious extensions, ClickFix social engineering, and Shadow AI usage were observed by Keep Aware and reflected in the Verizon 2026 DBIR.
- **Threat Actors:** None known
- **Mitigation:** Implement browser‑layer visibility and controls (browser telemetry/monitoring), restrict/allowlist extensions with stronger controls, block or monitor uploads to personal AI services, deploy in‑browser phishing detection and credential‑protection measures, enforce MFA and short‑lived credentials, use corporate‑managed AI tooling, and user training on ClickFix/social‑engineering.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — Cisco warns of unpatched SD-WAN zero-day exploited in attacks

**CVE:** `CVE-2026-20245` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://www.bleepingcomputer.com/news/security/new-cisco-sd-wan-flaw-exploited-in-zero-day-attacks-to-gain-root/>

> On Thursday, Cisco warned of a high-severity, unpatched zero-day in the Cisco Catalyst SD-WAN Manager (tracked as CVE-2026-20245) actively exploited in attacks enabling root privilege escalation. [...]

**Parallel AI Enrichment:**

- **Technical Details:** CLI input validation flaw in the Cisco Catalyst SD‑WAN Manager allows an authenticated, local attacker to upload a crafted file and execute arbitrary commands as root via the CLI.
- **Affected Products:** Cisco Catalyst SD‑WAN Manager (formerly SD‑WAN vManage)
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Active exploitation reported; no public PoC or weaponized exploit URL confirmed.
- **Patch Available:** No vendor patch available as of 2026-06-05; Cisco advisory shows vulnerability disclosure but no fixed release listed.
- **Active Exploitation:** Confirmed active exploitation reported by multiple sources (Cisco advisory, NVD, Bleeping Computer, SecurityWeek).
- **Threat Actors:** None known
- **Mitigation:** Restrict local authenticated access to SD‑WAN Manager (vManage), apply least privilege for accounts, monitor for suspicious file uploads and command execution, and follow Cisco/CISA guidance to inventory and assess for compromise.
- **Vendor Advisory:** https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-privesc-4uxFrdzx

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) involves seeding malicious prompt payloads into web‑hosted content or other data sources which are then ingested by AI agents or LLMs during browsing or retrieval‑augmented workflows; payloads attempt to override or subvert model instructions to perform fraud, data exfiltration, API key theft, code manipulation or destructive actions. Prior research describes 10 verified IPI payloads spanning financial fraud, data destruction, API key theft and AI abuse.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public in‑the‑wild indirect prompt injection (IPI) payloads disclosed by Forcepoint X‑Labs; PoCs observed on live websites.
- **Patch Available:** Vendor advisory URL unavailable. (No vendor patch referenced in prior research.)
- **Active Exploitation:** Yes — confirmed in‑the‑wild IPI payloads observed on live websites, reported by Forcepoint X‑Labs and summarized in Google’s Threat Intelligence blog.
- **Threat Actors:** None known
- **Mitigation:** Mitigations recommended include: (1) Treat untrusted web content and retrieved documents as adversarial input — implement strict input filtering and sanitization; (2) Use immutable, policy‑enforced system prompts and context separation (don’t allow external content to override system instructions); (3) Apply retrieval provenance and content integrity checks before feeding into LLMs; (4) Limit models’ direct access to sensitive APIs/credentials and use scoped, monitored service accounts; (5) Monitor and alert on anomalous model outputs and risky actions; (6) Conduct regular sweeps of public‑facing content for known IPI patterns.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack by which adversaries inject malicious instructions into data or tools consumed by an LLM (e.g., web content, documents, or tool outputs) so the model follows those instructions instead of the user’s intent; attacks can be delivered indirectly via multiple data sources used by agentic or multi‑source AI applications.
- **Affected Products:** Google Workspace with Gemini (Gmail, Docs, other Workspace apps)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit referenced in the vendor post.
- **Patch Available:** No specific "patch" — Google describes continuous defenses and model hardening; no vendor patch URL.
- **Active Exploitation:** Google reports monitoring public web IPI attempts and an increase in observed malicious attempts; however, no confirmed widespread weaponized exploit in production has been cited.
- **Threat Actors:** None known
- **Mitigation:** Deterministic defenses (user confirmation, URL sanitization, tool‑chaining policies via a centralized Policy Engine), ML‑based defenses retrained with synthetic attack data, Gemini model hardening, extensive red‑team testing (human & automated), Google AI VRP, synthetic data generation and end‑to‑end simulation/testing.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is indirect prompt injection: attacker‑controlled web content can influence or manipulate prompts sent to agentic AI capabilities in Chrome, allowing malicious sites to affect AI behaviour.
- **Affected Products:** Google Chrome (agentic/Gemini-enabled browsing)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit reported.
- **Patch Available:** Google announced layered defenses for agentic browsing in Chrome; no separate patch URL beyond the vendor advisory.
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Use the vendor‑provided layered defenses built into Chrome; keep Chrome updated; follow Chrome hardening guidance, restrict untrusted content access, and limit agentic actions.
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
- **Exploit Available:** Exploit information unavailable.
- **Patch Available:** Patch information unavailable.
- **Active Exploitation:** Active exploitation information unavailable.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an AI system processes external content (webpages, emails, documents, calendar invites) that contains hidden malicious instructions, causing the model to follow those instructions unintentionally.
- **Affected Products:** Gemini (including Gemini in Google Workspace), Gemini 2.5
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept or weaponized exploit published.
- **Patch Available:** No separate patch published; Google describes built‑in and service‑side defenses and ongoing model hardening.
- **Active Exploitation:** Google observed experiments on the public web and a 32% increase in detections (Nov 2025–Feb 2026) with low sophistication; no confirmed widespread weaponized exploits reported.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: prompt injection content classifiers; security thought reinforcement; markdown sanitization and suspicious URL redaction; user confirmation/HITL framework; end‑user mitigation notifications; adversarial training and model hardening (Gemini 2.5).
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors implant malicious code or firmware on routers, create unauthorized GRE tunnels for exfiltration, modify routing tables and ACLs, and leverage compromised devices and trusted connections to pivot and maintain persistent, long‑term access to target networks.
- **Affected Products:** Large backbone routers, provider‑edge (PE) routers, and customer‑edge (CE) routers from multiple telecom‑grade vendors.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proofs‑of‑concept may exist for individual CVEs, but no single publicly released exploit covering the overall activity is referenced.
- **Patch Available:** Vendor patches exist for some exploited vulnerabilities; specific patch URLs vary by vendor.
- **Active Exploitation:** Confirmed active exploitation in the wild by PRC‑linked actors (Salt Typhoon/RedMike, OPERATOR PANDA, UNC5807, GhostEmperor) has been reported.
- **Threat Actors:** Salt Typhoon (RedMike), OPERATOR PANDA, UNC5807, GhostEmperor
- **Mitigation:** Restrict administrative access, rotate credentials and keys, apply vendor patches, validate device integrity (firmware/boot configs), monitor for GRE tunnels and abnormal configurations, segment and limit management‑plane access, and use vendor‑supported integrity checks and logging.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 12. 🟠 Zero-Day — In Other News: Anthropic Maps AI Threats, Unpatched Comodo Flaw, Palantir Chief Eyed for CISA

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://www.securityweek.com/in-other-news-anthropic-maps-ai-threats-unpatched-comodo-flaw-palantir-chief-eyed-for-cisa/>

> Other noteworthy stories that might have slipped under the radar: Ultrahuman data leak, The Gentlemen ransomware analysis, Hola Browser bundles miner. The post In Other News: Anthropic Maps AI Threats, Unpatched Comodo Flaw, Palantir Chief Eyed for CISA appeared first on SecurityWeek .

---

## 13. 🟡 High Severity — Bugsink: Issue bulk actions can affect another project’s issue if its UUID is known

**CVE:** `CVE-2026-47716` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-g5vc-q7qc-v939>

> ### Description
Bugsink’s issue list supports bulk actions such as resolving or muting selected issues. In affected versions, the issue list view authorizes access through the project in the URL, but applies the requested bulk action to the submitted issue IDs without also requiring those issues to belong to that project.

This is a project-boundary authorization issue: a logged-in user with acces…

---

## 14. 🟡 High Severity — Bugsink: Issue event views can show an event from another project if its UUID is known

**CVE:** `CVE-2026-47715` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-vx2f-6m6h-9frf>

> ### Description

Bugsink issue event pages accept a direct event identifier from the URL and, in affected versions, look up that event without also requiring it to belong to the issue in the URL.

This is a project-boundary authorization issue: a logged-in user with access to one project can view another project’s event data through an issue they are allowed to access. However, the issue is mitiga…

---

## 15. 🟡 High Severity — Shopper: Authorization bypass and RBAC privilege escalation in team settings

**CVE:** `CVE-2026-47744` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-c3qp-2ggw-xjg7>

> ## Impact

Two distinct authorization defects in the team settings allowed any authenticated panel user to take over the RBAC system:

- `Settings/Team/Index` had no `mount()` authorization. Any authenticated user could load the page and use its public actions to create new roles and delete other users, including administrators.
- `Settings/Team/RolePermission` gated its write actions on the read-…

---

## 16. 🟡 High Severity — Weekly Metasploit Update: Apache ActiveMQ RCE, Gogs Rebase RCE, and Windows Kernel Pointer Enum

**CVE:** `CVE-2026-34197` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-05-06-2026>

> When Open Source is a bit too Open Several fun modules landed this week, including an Apache RCE, Windows Kernel pointer collection, and Gogs RCE via naming. Leading off is Gogs&#x27; RCE that allows an attacker to execute commands by naming their branch --exec and requesting a rebase. Another useful post module by CharlesQuinnDev enumerates the Kernel pointers leaked via the popular NtQuerySystem…

---

## 17. 🟡 High Severity — DbGate: Remote Code Execution via functionName injection in loadReader endpoint

**CVE:** `CVE-2026-48017` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-hv83-ggc4-v385>

> ### Summary

The `POST /runners/load-reader` endpoint in DbGate accepts a `functionName` parameter that is directly interpolated into a JavaScript code template without any sanitization or validation. An authenticated user (with basic access, no special permissions required) can inject arbitrary JavaScript code that executes on the server with full process privileges, bypassing the `require=null` …

---

## 18. 🟡 High Severity — Sync-in Server: SSRF protection bypass via IPv4-mapped IPv6 addresses in regExpPrivateIP

**CVE:** `CVE-2026-47684` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-q4x5-8cj6-52wg>

> Summary:
The private IP blocklist regex used in the URL download feature does not match IPv4-mapped IPv6 addresses (e.g. ::ffff:127.0.0.1), allowing SSRF protection to be bypassed on dual-stack systems.

Affected components

backend/src/applications/files/services/files-manager.service.ts – downloadFromUrl() checks regExpPrivateIP against request.socket.remoteAddress.
backend/src/applications/file…

---

## 19. 🟡 High Severity — Source controller: Improper path handling allows traversal

**CVE:** `CVE-2026-47680` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-jjrm-hr5f-673x>

> ### Impact

An actor with the ability to influence the contents of a bucket referenced by a `Bucket` resource can cause source-controller to write fetched object data to paths outside the per-reconciliation working directory.

The corruption surface is bounded by source-controller&#x27;s own and downstream Flux controllers&#x27; digest verification: source-controller verifies stored artifact diges…

---

## 20. 🟡 High Severity — Authenticated Remote Code Execution via loadReader functionName code injection in DbGate

**CVE:** `CVE-2026-47670` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-wm5r-5qp3-5vxf>

> ### Summary

DbGate is vulnerable to authenticated Remote Code Execution (RCE). Any user with valid DbGate credentials can execute arbitrary OS commands as root by exploiting an unsanitized `functionName` parameter in the `/runners/load-reader` endpoint. The `require = null` mitigation is trivially bypassed via dynamic `import()`.


&lt;br/&gt;

### Details

**Code injection via `functionName` in …

---

## 21. 🟡 High Severity — DbGate: Unauthenticated Remote Code Execution via JSON Script Runner

**CVE:** `CVE-2026-47668` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-8v3q-9vmx-36vc>

> ### Summary
DbGate&#x27;s JSON script runner (`POST /runners/start`) allows remote code execution via code injection in the `functionName` parameter of JSON script `assign` commands. The `functionName` value is interpolated directly into dynamically generated JavaScript source code via string concatenation. The generated code is then executed in a forked Node.js child process.

### Details
#### St…

---

## 22. 🟡 High Severity — NocoDB: Cross-Workspace Integration Use in Connection Test

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

## 23. 🟡 High Severity — Omni: Reader-level users can retrieve imported cluster CA keys via ResourceService

**CVE:** `CVE-2026-45726` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-wv8c-6mx2-xf4j>

> ## Summary

Omni supports importing standalone Talos clusters.

During this process, an ImportedClusterSecrets resource is created, which contains the full CA secrets bundle for the cluster being imported.

If these secrets are not rotated by the importing actor, an authenticated Omni user with Reader access can read this resource and gain full access to the Talos, Kubernetes and etcd APIs of the …

---

## 24. 🟡 High Severity — Hackers Exploit Critical Everest Forms Pro WordPress Plugin Flaw to Take Over Sites

**CVE:** `CVE-2026-3300` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://thehackernews.com/2026/06/hackers-exploit-critical-everest-forms.html>

> Threat actors are actively exploiting a critical security flaw in Everest Forms Pro, a WordPress plugin with about 4,000 active installations, to execute arbitrary code, leading to a complete site compromise.

The vulnerability in question is CVE-2026-3300 (CVSS score: 9.8), a remote code execution bug impacting all versions of the plugin up to, and including, 1.9.12. A patch for the flaw was

---

## 25. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
