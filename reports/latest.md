# Zero Day Pulse

> **Generated:** 2026-06-05 19:30 UTC &nbsp;|&nbsp; **Total:** 27 &nbsp;|&nbsp; 🔴 KEV: 1 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 12 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🔴 CISA KEV — CVE-2026-28318 — SolarWinds Serv-U Uncontrolled Resource Consumption Vulnerability

**CVE:** `CVE-2026-28318` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-28318>

> Vendor: SolarWinds | Product: Serv-U. SolarWinds Serv-U contains an uncontrolled resource consumption vulnerability that allows specially crafted POST requests using the Content-Encoding: deflate header to crash the Serv-U service without authentication. Required action: Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the pr…

**Parallel AI Enrichment:**

- **Technical Details:** SolarWinds Serv‑U contains an uncontrolled resource consumption vulnerability where specially crafted POST requests using the Content‑Encoding: deflate header can crash the Serv‑U service without authentication.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply mitigations per vendor instructions in the SolarWinds advisory, follow applicable BOD 22-01 guidance for cloud services, or discontinue use if mitigations are unavailable.
- **Vendor Advisory:** https://www.solarwinds.com/trust-center/security-advisories/CVE-2026-28318

---

## 2. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a directory traversal vulnerability in the SimpleHelp web interface that permits unauthenticated remote attackers to read arbitrary files on the server by supplying crafted path input to vulnerable endpoints.
- **Affected Products:** SimpleHelp Remote Monitoring and Management versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors
- **Mitigation:** Upgrade SimpleHelp to version 5.5.8 or later. If immediate upgrade is not possible, restrict access to SimpleHelp management interfaces to trusted IPs, block Internet access to the service, employ network segmentation and monitoring, and apply least‑privilege access controls.
- **Vendor Advisory:** https://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 3. 🟠 Zero-Day — MCP Server Kubernetes: kubectl-generic flag injection enables Kubernetes bearer token exfiltration

**CVE:** `CVE-2026-47250` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-6mx4-4h42-r8vh>

> ### Summary
The `kubectl_generic` tool in `mcp-server-kubernetes` passes user-supplied flags directly to kubectl without any allowlist, enabling a **privilege escalation attack** within Kubernetes environments. An attacker who already has limited cluster or codebase access, for example, a developer with pod-deployment permissions but not cluster-admin credentials, can plant a single structured JSO…

**Parallel AI Enrichment:**

- **Technical Details:** The kubectl_generic tool in mcp-server-kubernetes passes user-supplied flags directly to kubectl without any allowlist, enabling a privilege escalation attack. An attacker with limited access can plant a structured JSON line in application logs; when an operator with a privileged kubeconfig uses the MCP server to read those logs and an AI agent follows the injected instruction, kubectl_generic can be coerced to execute kubectl commands that exfiltrate the Kubernetes bearer token.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Remove or disable the kubectl_generic command; do not allow privileged kubeconfigs to be used with untrusted MCP servers or agents; sanitize and do not auto-execute user-supplied flags; implement an allowlist for kubectl flags and require manual review of logs containing structured input.
- **Vendor Advisory:** https://github.com/advisories/GHSA-6mx4-4h42-r8vh

---

## 4. 🟠 Zero-Day — What 2026 DBIR Confirms: Attacks Are Living in the Browser

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://www.bleepingcomputer.com/news/security/what-2026-dbir-confirms-attacks-are-living-in-the-browser/>

> Phishing, shadow AI, malicious extensions, and credential theft increasingly happen inside the browser. Keep Aware explains what the 2026 Verizon DBIR reveals about browser-layer security gaps and modern attacks. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Implement browser‑layer visibility, enforce governance of AI use within browsers, control and monitor high‑risk extensions, and deploy detection for credential theft occurring inside browsers.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — Cisco warns of unpatched SD-WAN zero-day exploited in attacks

**CVE:** `CVE-2026-20245` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://www.bleepingcomputer.com/news/security/new-cisco-sd-wan-flaw-exploited-in-zero-day-attacks-to-gain-root/>

> On Thursday, Cisco warned of a high-severity, unpatched zero-day in the Cisco Catalyst SD-WAN Manager (tracked as CVE-2026-20245) actively exploited in attacks enabling root privilege escalation. [...]

**Parallel AI Enrichment:**

- **Technical Details:** A CLI vulnerability in Cisco Catalyst SD‑WAN Manager that allows an authenticated, local attacker to execute arbitrary commands as root via the management CLI.
- **Affected Products:** Cisco Catalyst SD‑WAN Manager (formerly SD‑WAN vManage)
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Restrict local/SSH access to the management interface, follow CISA/agency guidance to inventory SD‑WAN systems, apply available compensating controls, and monitor for indicators of compromise.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 6. 🟠 Zero-Day — The June 2026 AI Executive Order: What federal agencies need to know and how Tenable can help

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Tenable Security Research &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://www.tenable.com/blog/summary-june-2026-ai-executive-order-requirements>

> On June 2, 2026, the White House signed an Executive Order directing federal agencies to harden their systems with AI-enabled cyber defenses and to stand up a new AI cybersecurity clearinghouse — most of it on a 30-day clock. Here’s what the EO requires and how Tenable can help. Key takeaways: The new AI Security Executive Order will require national security and civilian federal agencies to prior…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Agencies should harden systems with AI-enabled cyber defenses and inventory AI assets; Tenable One AI Exposure can help agencies discover and inventory AI tools and libraries and apply AI usage policies across the environment to help prioritize vulnerabilities and automate remediation workflows.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 7. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when AI agents ingest attacker‑controlled content (web pages, documents, files) that contain malicious instructions. The attacker poisons the content—often hidden via CSS, HTML comments, metadata, or special tags—so the model treats the embedded instructions as authoritative, leading to actions such as data exfiltration, command execution, financial transactions, or content suppression. Observed techniques include CSS concealment, HTML comment injection, system‑prompt tag spoofing, magic‑string impersonation, meta‑namespace injection, accessibility‑attribute abuse, and TOCTOU sandbox‑escape chains (e.g., the Antigravity IDE chain).
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Implement layered defenses: restrict AI agents from accessing untrusted external content; enforce strict parsing that separates data from instructions; sanitize or strip hidden/high‑risk HTML elements (CSS, comments, metadata) before ingestion; conduct quarterly IPI red‑team exercises using Forcepoint’s payload taxonomy; apply vendor patches (e.g., the Antigravity IDE patch).
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 8. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) hides malicious instructions in data sources (web pages, docs, emails, calendar invites, metadata, hidden HTML/CSS, or images). When the LLM ingests that data during a request, the embedded instructions are treated as part of the prompt, allowing data exfiltration, command execution, or content manipulation. Noma Labs demonstrated a zero‑click attack (GeminiJack) where a shared document with hidden instructions caused Gemini Enterprise/Vertex AI Search to exfiltrate Gmail, Calendar, and Docs content via an invisible image request. Forcepoint cataloged live payloads using CSS display:none, tiny fonts, metadata abuse, and magic‑string spoofing to poison AI inputs.
- **Affected Products:** Google Gemini Enterprise (Gemini in Workspace), Vertex AI Search (prior deployments)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true — https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/
- **Patch Available:** true — http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html
- **Active Exploitation:** true — http://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads, http://hackread.com/hackers-hidden-site-instruction-attack-ai-assistants
- **Threat Actors:** None known
- **Mitigation:** Use Google’s layered defenses – prompt‑injection content classifiers, markdown/URL sanitization, suspicious URL redaction, security thought‑reinforcement, user‑confirmation framework, end‑user mitigation notifications, model hardening, and ML‑based defenses; additionally block IPI URLs at network gateways (e.g., Forcepoint protections).
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 9. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) – attacker‑controlled web content crafts inputs that influence agentic browser prompts or agent instructions, causing the agent to perform unsafe actions or disclose sensitive data. Google’s design adds a supervising agent and layered restrictions to limit origin access and unsafe actions.
- **Affected Products:** Chrome (agentic browsing / Gemini integration)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** true — http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Use Chrome’s new layered defenses (restrict origin access, block indirect prompt injections), avoid visiting untrusted sites, and disable agentic/assistant features until mitigations are fully deployed.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 10. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow in the CrabbyAVIF Rust crate's unsafe code path was discovered and fixed pre‑release; Android's Scudo hardened allocator used guard pages to turn the overflow into a crash, rendering it non‑exploitable. Tracked as CVE‑2025‑48530.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — patch: https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the official patch above; use Scudo hardened allocator (already default on many Android devices); follow unsafe Rust review practices and training as described in Google’s guidance.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 11. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 12. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

---

## 13. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 14. 🟠 Zero-Day — In Other News: Anthropic Maps AI Threats, Unpatched Comodo Flaw, Palantir Chief Eyed for CISA

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://www.securityweek.com/in-other-news-anthropic-maps-ai-threats-unpatched-comodo-flaw-palantir-chief-eyed-for-cisa/>

> Other noteworthy stories that might have slipped under the radar: Ultrahuman data leak, The Gentlemen ransomware analysis, Hola Browser bundles miner. The post In Other News: Anthropic Maps AI Threats, Unpatched Comodo Flaw, Palantir Chief Eyed for CISA appeared first on SecurityWeek .

---

## 15. 🟠 Zero-Day — Shopware: Stored XSS via SVG file upload — no SVG sanitization

**CVE:** `CVE-2026-48015` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-xvhc-gm7j-mhmc>

> SVG files are in the `allowed_extensions` whitelist and can be uploaded by any admin user via the media manager. There is zero SVG content sanitization anywhere in the upload pipeline. A malicious SVG with JavaScript (`onload`, `&lt;script&gt;`, `&lt;foreignObject&gt;`) executes in the context of the Shopware domain when accessed.

## The Problem

In `src/Core/Framework/Resources/config/packages/s…

---

## 16. 🟡 High Severity — DbGate: Remote Code Execution via functionName injection in loadReader endpoint

**CVE:** `CVE-2026-48017` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-hv83-ggc4-v385>

> ### Summary

The `POST /runners/load-reader` endpoint in DbGate accepts a `functionName` parameter that is directly interpolated into a JavaScript code template without any sanitization or validation. An authenticated user (with basic access, no special permissions required) can inject arbitrary JavaScript code that executes on the server with full process privileges, bypassing the `require=null` …

---

## 17. 🟡 High Severity — Sync-in Server: SSRF protection bypass via IPv4-mapped IPv6 addresses in regExpPrivateIP

**CVE:** `CVE-2026-47684` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-q4x5-8cj6-52wg>

> Summary:
The private IP blocklist regex used in the URL download feature does not match IPv4-mapped IPv6 addresses (e.g. ::ffff:127.0.0.1), allowing SSRF protection to be bypassed on dual-stack systems.

Affected components

backend/src/applications/files/services/files-manager.service.ts – downloadFromUrl() checks regExpPrivateIP against request.socket.remoteAddress.
backend/src/applications/file…

---

## 18. 🟡 High Severity — Source controller: Improper path handling allows traversal

**CVE:** `CVE-2026-47680` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-jjrm-hr5f-673x>

> ### Impact

An actor with the ability to influence the contents of a bucket referenced by a `Bucket` resource can cause source-controller to write fetched object data to paths outside the per-reconciliation working directory.

The corruption surface is bounded by source-controller&#x27;s own and downstream Flux controllers&#x27; digest verification: source-controller verifies stored artifact diges…

---

## 19. 🟡 High Severity — Authenticated Remote Code Execution via loadReader functionName code injection in DbGate

**CVE:** `CVE-2026-47670` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-wm5r-5qp3-5vxf>

> ### Summary

DbGate is vulnerable to authenticated Remote Code Execution (RCE). Any user with valid DbGate credentials can execute arbitrary OS commands as root by exploiting an unsanitized `functionName` parameter in the `/runners/load-reader` endpoint. The `require = null` mitigation is trivially bypassed via dynamic `import()`.


&lt;br/&gt;

### Details

**Code injection via `functionName` in …

---

## 20. 🟡 High Severity — DbGate: Unauthenticated Remote Code Execution via JSON Script Runner

**CVE:** `CVE-2026-47668` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-8v3q-9vmx-36vc>

> ### Summary
DbGate&#x27;s JSON script runner (`POST /runners/start`) allows remote code execution via code injection in the `functionName` parameter of JSON script `assign` commands. The `functionName` value is interpolated directly into dynamically generated JavaScript source code via string concatenation. The generated code is then executed in a forked Node.js child process.

### Details
#### St…

---

## 21. 🟡 High Severity — NocoDB: Cross-Workspace Integration Use in Connection Test

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

## 22. 🟡 High Severity — Omni: Reader-level users can retrieve imported cluster CA keys via ResourceService

**CVE:** `CVE-2026-45726` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-wv8c-6mx2-xf4j>

> ## Summary

Omni supports importing standalone Talos clusters.

During this process, an ImportedClusterSecrets resource is created, which contains the full CA secrets bundle for the cluster being imported.

If these secrets are not rotated by the importing actor, an authenticated Omni user with Reader access can read this resource and gain full access to the Talos, Kubernetes and etcd APIs of the …

---

## 23. 🟡 High Severity — Hackers Exploit Critical Everest Forms Pro WordPress Plugin Flaw to Take Over Sites

**CVE:** `CVE-2026-3300` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://thehackernews.com/2026/06/hackers-exploit-critical-everest-forms.html>

> Threat actors are actively exploiting a critical security flaw in Everest Forms Pro, a WordPress plugin with about 4,000 active installations, to execute arbitrary code, leading to a complete site compromise.

The vulnerability in question is CVE-2026-3300 (CVSS score: 9.8), a remote code execution bug impacting all versions of the plugin up to, and including, 1.9.12. A patch for the flaw was

---

## 24. 🟡 High Severity — AdGuard Home: DoQ-to-UDP State Reduction and Source-Port Oracle

**CVE:** `CVE-2026-47703` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-xgx4-4h9w-53pv>

> ## Summary

This report covers the client-triggered DoQ forwarding path in:

- `dnsproxy` `v0.81.2` (`adguard/dnsproxy:v0.81.2`)
- `AdGuard Home` `v0.107.74` (`adguard/adguardhome:latest`, image version label `v0.107.74`)

The issue was reproduced on `2026-04-25` with the products configured through
their documented DoQ listener and plain UDP upstream surfaces. The scope is the
internal backend UD…

---

## 25. 🟡 High Severity — Shopware: SSRF in Media External-Link Endpoint Bypasses IP Validation

**CVE:** `CVE-2026-48013` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-gq96-5pfx-f4vc>

> ## Summary

The `/api/_action/media/external-link` endpoint allows authenticated admin users to make server-side HTTP HEAD requests to arbitrary internal IP addresses. While the parallel `uploadFromURL` flow validates target IPs against private/reserved ranges via `FileUrlValidator`, the `linkURL` flow only performs a URL format check (regex for `http://` or `https://` prefix), allowing SSRF to in…

---

## 26. 🟡 High Severity — Shopware: Admin API ACL Bypass in Order State Transition Endpoints

**CVE:** `CVE-2026-48014` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-f8q6-3g5w-jjr6>

> ## Summary
This is a vertical authorization bypass in the Admin API affecting order state transition features (`/api/_action/order/{orderId}/state/{transition}` and similar transaction/delivery transition routes). The root cause is that the transition action routes do not declare required server-side ACL privileges, allowing low-privileged users to pass the authorization boundary. As a result, aut…

---

## 27. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
