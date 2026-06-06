# Zero Day Pulse

> **Generated:** 2026-06-06 13:06 UTC &nbsp;|&nbsp; **Total:** 26 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 12 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a directory traversal (path traversal) vulnerability in SimpleHelp remote support software that lets unauthenticated attackers read sensitive files by supplying malicious file paths.
- **Affected Products:** SimpleHelp remote support software (version 5.5.7 and earlier)
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know)
- **Active Exploitation:** true (http://cisa.gov/news-events/cybersecurity-advisories/aa25-163a)
- **Threat Actors:** Ransomware actors (unspecified)
- **Mitigation:** Upgrade SimpleHelp to a version newer than 5.5.7 (or apply the vendor‑provided patch) and ensure all remote agents are updated.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — AI Agent Uncovers 21 Zero-Days in FFmpeg; Chrome Patches Record 429 Bugs

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-06
**Reference:** <https://thehackernews.com/2026/06/ai-agent-uncovers-21-zero-days-in.html>

> Two things landed within days of each other this week. A security startup reported 21 previously unknown vulnerabilities in FFmpeg, the media library inside almost everything that touches video, all of them found by an autonomous AI agent.

The same week, Google shipped Chrome 149 with patches for 429 security bugs, the most ever in a single release.

Only the FFmpeg bugs were found by AI.

**Parallel AI Enrichment:**

- **Technical Details:** The 21 FFmpeg vulnerabilities consist of heap and stack buffer overflows, integer overflows, and out‑of‑bounds reads/writes in various codec and demuxer components. Exploitable examples include a heap buffer overflow in the RTP AV1 depacketizer (DFVULN‑127) that can overwrite an AVBuffer.free function pointer to achieve remote code execution, and integer overflow in libswscale/utils.c that leads to undersized allocations and subsequent memory corruption.
- **Affected Products:** libavformat/mpegts.c, libswscale/utils.c, fftools/ffmpeg_opt.c, libavformat/yuv4mpegenc.c, libavformat/mpegtsenc.c, libavcodec/mpegvideo_enc.c, libavformat/img2enc.c, libavcodec/vp9.c, libavformat/dashdec.c, rtpdec_av1.c, graph.c, rtpdec_jpeg.c, ffmpeg_demux.c
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** 1. Update FFmpeg to the latest upstream build or apply distribution security updates as soon as they are released. 2. Prioritize systems that ingest untrusted RTSP or AV1‑over‑RTP streams, since those are highlighted as high‑risk vectors. 3. Ensure that any embedded copies of FFmpeg in applications, containers, or appliances are also patched, not only the system‑level package.
- **Vendor Advisory:** https://ffmpeg.org/security.html

---

## 3. 🟠 Zero-Day — MCP Server Kubernetes: kubectl-generic flag injection enables Kubernetes bearer token exfiltration

**CVE:** `CVE-2026-47250` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-6mx4-4h42-r8vh>

> ### Summary
The `kubectl_generic` tool in `mcp-server-kubernetes` passes user-supplied flags directly to kubectl without any allowlist, enabling a **privilege escalation attack** within Kubernetes environments. An attacker who already has limited cluster or codebase access, for example, a developer with pod-deployment permissions but not cluster-admin credentials, can plant a single structured JSO…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability stems from passing user-supplied flags directly to kubectl without an allowlist in the kubectl_generic tool. This permits injection of kubectl flags or commands via crafted log output; when an operator using a privileged kubeconfig invokes log‑reading functionality, those flags are forwarded to kubectl, enabling extraction of bearer tokens or escalation to cluster‑admin actions.
- **Affected Products:** mcp-server-kubernetes — kubectl_generic
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true — https://github.com/advisories/GHSA-6mx4-4h42-r8vh
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor‑released updates per the advisory. If patching is not yet possible, restrict usage of the MCP server to least‑privileged kubeconfigs, avoid letting privileged operators use untrusted logs directly, implement input allowlisting/validation for kubectl flags, restrict who can deploy or write application logs, and rotate any exposed tokens and credentials.
- **Vendor Advisory:** https://github.com/advisories/GHSA-6mx4-4h42-r8vh

---

## 4. 🟠 Zero-Day — What 2026 DBIR Confirms: Attacks Are Living in the Browser

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://www.bleepingcomputer.com/news/security/what-2026-dbir-confirms-attacks-are-living-in-the-browser/>

> Phishing, shadow AI, malicious extensions, and credential theft increasingly happen inside the browser. Keep Aware explains what the 2026 Verizon DBIR reveals about browser-layer security gaps and modern attacks. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Browser‑based attacks exploit extensions that can read/modify page content and exfiltrate data, and social‑engineering techniques such as ClickFix that start in the browser and then compromise the endpoint with info‑stealers and remote‑access tools.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Deploy browser‑layer visibility and controls, govern and block high‑risk/unauthorized extensions, enforce MFA and strong credential hygiene, apply DLP and sanctioned AI controls, provide user training, and monitor browser session artifacts.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when AI systems process content (websites, email, documents) that contains malicious instructions; attackers embed payloads in public web pages that, if followed by an AI agent, could cause data exfiltration, destruction, or other malicious outcomes. Google analyzed Common Crawl snapshots, classified candidates with Gemini, and performed human validation; observed categories included pranks, helpful guidance, SEO manipulation, deterring AI agents, and malicious attempts.
- **Affected Products:** Google Gemini (and Gemini‑powered products), Google Workspace (and AI agents that browse the public web)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses — pattern matching filters, LLM‑based classification of candidate content, human validation for high‑confidence cases; harden models and products (red‑team testing), invest in detection at scale, share intelligence, and participate in vulnerability reward programs. See Google’s Workspace mitigations blog for product‑specific controls.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack technique that injects malicious instructions into data or tools used by an LLM‑powered application (e.g., Workspace with Gemini), allowing the attacker to influence the model’s behavior even without direct user input.
- **Affected Products:** Google Workspace with Gemini
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Google’s continuous, layered defense strategy: defense‑in‑depth for Gemini and Workspace apps (input validation, contextual filtering, tooling restrictions, monitoring, and updates). Use least privilege for tool access and restrict agentic automation; apply Google’s recommended mitigations in the advisory.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection occurs when a malicious or third‑party web page supplies hidden instructions that are injected into the agentic AI’s prompt, steering its decisions in a way that benefits the attacker. This attack vector leverages the AI’s ability to interpret page content as part of its reasoning process.
- **Affected Products:** Chrome (agentic browsing / Gemini integration)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true - http://blog.google/security/architecting-security-for-agentic
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Enable Chrome's updated agentic security features/updates; apply the layered defenses announced by Google, including a supervisory AI, origin access restrictions, and safe action constraints.
- **Vendor Advisory:** http://blog.google/security/architecting-security-for-agentic

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A near‑miss linear buffer overflow in the Rust crate CrabbyAVIF (CVE‑2025‑48530) was discovered and fixed pre‑release; Android’s Scudo hardened allocator uses guard pages around secondary allocations, turning the overflow into a noisy crash and rendering the issue non‑exploitable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — https://source.android.com/docs/security/bulletin/2025/2025-08-01
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Ensure devices run builds that include the vendor patch; enable Android’s Scudo hardened allocator where possible; keep Android updated following the security bulletin; employ sandboxing and other runtime mitigations.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025/2025-08-01

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) embeds malicious instructions in external data sources (emails, documents, calendar invites) which LLM‑powered assistants may ingest; attackers aim to cause data exfiltration or rogue actions by shaping input the assistant reads.
- **Affected Products:** Gemini (Gemini app, Gemini in Google Workspace), Gemini 2.5
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses — adversarial training/model hardening, prompt‑injection content classifiers, markdown sanitization and suspicious‑URL redaction, user confirmation framework, and end‑user security mitigation notifications. Follow Google guidance and help‑center recommendations.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors target large backbone routers and provider edge/customer edge routers, modify routers to maintain persistent long‑term access, and pivot via compromised devices and trusted connections into other networks.
- **Affected Products:** backbone routers, provider edge (PE) routers, customer edge (CE) routers, other compromised networking devices
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon; OPERATOR PANDA; RedMike; UNC5807; GhostEmperor
- **Mitigation:** Hardening and mitigation guidance per advisory (segmentation of management networks, restrict administrative access, monitor router configurations and firmware integrity, apply vendor patches and recommendations, implement least‑privilege access and logging/monitoring)
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 11. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 12. 🟠 Zero-Day — CISA Adds Actively Exploited SolarWinds Serv-U DoS Flaw to KEV Catalog

**CVE:** `CVE-2026-28318` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-06
**Reference:** <https://thehackernews.com/2026/06/cisa-adds-actively-exploited-solarwinds.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has added a high-severity security flaw impacting SolarWinds Serv-U  multi-protocol file server software to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

The vulnerability, tracked as CVE-2026-28318 (CVSS score: 7.5), is a denial-of-service (DoS) bug that causes the service to crash

---

## 13. 🟠 Zero-Day — Cisco Catalyst SD-WAN Manager CVE-2026-20245 Flaw Actively Exploited – No Patch Available

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

## 14. 🟠 Zero-Day — In Other News: Anthropic Maps AI Threats, Unpatched Comodo Flaw, Palantir Chief Eyed for CISA

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://www.securityweek.com/in-other-news-anthropic-maps-ai-threats-unpatched-comodo-flaw-palantir-chief-eyed-for-cisa/>

> Other noteworthy stories that might have slipped under the radar: Ultrahuman data leak, The Gentlemen ransomware analysis, Hola Browser bundles miner. The post In Other News: Anthropic Maps AI Threats, Unpatched Comodo Flaw, Palantir Chief Eyed for CISA appeared first on SecurityWeek .

---

## 15. 🟡 High Severity — Bugsink: Issue bulk actions can affect another project’s issue if its UUID is known

**CVE:** `CVE-2026-47716` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-g5vc-q7qc-v939>

> ### Description
Bugsink’s issue list supports bulk actions such as resolving or muting selected issues. In affected versions, the issue list view authorizes access through the project in the URL, but applies the requested bulk action to the submitted issue IDs without also requiring those issues to belong to that project.

This is a project-boundary authorization issue: a logged-in user with acces…

---

## 16. 🟡 High Severity — Bugsink: Issue event views can show an event from another project if its UUID is known

**CVE:** `CVE-2026-47715` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-vx2f-6m6h-9frf>

> ### Description

Bugsink issue event pages accept a direct event identifier from the URL and, in affected versions, look up that event without also requiring it to belong to the issue in the URL.

This is a project-boundary authorization issue: a logged-in user with access to one project can view another project’s event data through an issue they are allowed to access. However, the issue is mitiga…

---

## 17. 🟡 High Severity — Shopper: Authorization bypass and RBAC privilege escalation in team settings

**CVE:** `CVE-2026-47744` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-c3qp-2ggw-xjg7>

> ## Impact

Two distinct authorization defects in the team settings allowed any authenticated panel user to take over the RBAC system:

- `Settings/Team/Index` had no `mount()` authorization. Any authenticated user could load the page and use its public actions to create new roles and delete other users, including administrators.
- `Settings/Team/RolePermission` gated its write actions on the read-…

---

## 18. 🟡 High Severity — Weekly Metasploit Update: Apache ActiveMQ RCE, Gogs Rebase RCE, and Windows Kernel Pointer Enum

**CVE:** `CVE-2026-34197` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-05-06-2026>

> When Open Source is a bit too Open Several fun modules landed this week, including an Apache RCE, Windows Kernel pointer collection, and Gogs RCE via naming. Leading off is Gogs&#x27; RCE that allows an attacker to execute commands by naming their branch --exec and requesting a rebase. Another useful post module by CharlesQuinnDev enumerates the Kernel pointers leaked via the popular NtQuerySystem…

---

## 19. 🟡 High Severity — DbGate: Remote Code Execution via functionName injection in loadReader endpoint

**CVE:** `CVE-2026-48017` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-hv83-ggc4-v385>

> ### Summary

The `POST /runners/load-reader` endpoint in DbGate accepts a `functionName` parameter that is directly interpolated into a JavaScript code template without any sanitization or validation. An authenticated user (with basic access, no special permissions required) can inject arbitrary JavaScript code that executes on the server with full process privileges, bypassing the `require=null` …

---

## 20. 🟡 High Severity — Sync-in Server: SSRF protection bypass via IPv4-mapped IPv6 addresses in regExpPrivateIP

**CVE:** `CVE-2026-47684` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-q4x5-8cj6-52wg>

> Summary:
The private IP blocklist regex used in the URL download feature does not match IPv4-mapped IPv6 addresses (e.g. ::ffff:127.0.0.1), allowing SSRF protection to be bypassed on dual-stack systems.

Affected components

backend/src/applications/files/services/files-manager.service.ts – downloadFromUrl() checks regExpPrivateIP against request.socket.remoteAddress.
backend/src/applications/file…

---

## 21. 🟡 High Severity — Source controller: Improper path handling allows traversal

**CVE:** `CVE-2026-47680` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-jjrm-hr5f-673x>

> ### Impact

An actor with the ability to influence the contents of a bucket referenced by a `Bucket` resource can cause source-controller to write fetched object data to paths outside the per-reconciliation working directory.

The corruption surface is bounded by source-controller&#x27;s own and downstream Flux controllers&#x27; digest verification: source-controller verifies stored artifact diges…

---

## 22. 🟡 High Severity — Authenticated Remote Code Execution via loadReader functionName code injection in DbGate

**CVE:** `CVE-2026-47670` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-wm5r-5qp3-5vxf>

> ### Summary

DbGate is vulnerable to authenticated Remote Code Execution (RCE). Any user with valid DbGate credentials can execute arbitrary OS commands as root by exploiting an unsanitized `functionName` parameter in the `/runners/load-reader` endpoint. The `require = null` mitigation is trivially bypassed via dynamic `import()`.


&lt;br/&gt;

### Details

**Code injection via `functionName` in …

---

## 23. 🟡 High Severity — DbGate: Unauthenticated Remote Code Execution via JSON Script Runner

**CVE:** `CVE-2026-47668` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-8v3q-9vmx-36vc>

> ### Summary
DbGate&#x27;s JSON script runner (`POST /runners/start`) allows remote code execution via code injection in the `functionName` parameter of JSON script `assign` commands. The `functionName` value is interpolated directly into dynamically generated JavaScript source code via string concatenation. The generated code is then executed in a forked Node.js child process.

### Details
#### St…

---

## 24. 🟡 High Severity — NocoDB: Cross-Workspace Integration Use in Connection Test

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

## 25. 🟡 High Severity — Omni: Reader-level users can retrieve imported cluster CA keys via ResourceService

**CVE:** `CVE-2026-45726` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-wv8c-6mx2-xf4j>

> ## Summary

Omni supports importing standalone Talos clusters.

During this process, an ImportedClusterSecrets resource is created, which contains the full CA secrets bundle for the cluster being imported.

If these secrets are not rotated by the importing actor, an authenticated Omni user with Reader access can read this resource and gain full access to the Talos, Kubernetes and etcd APIs of the …

---

## 26. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
