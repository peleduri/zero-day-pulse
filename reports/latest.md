# Zero Day Pulse

> **Generated:** 2026-06-11 10:03 UTC &nbsp;|&nbsp; **Total:** 31 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 16 &nbsp;|&nbsp; 🟡 High: 15 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a directory traversal vulnerability in SimpleHelp RMM that allows an attacker to read arbitrary sensitive files on the host by supplying crafted path strings.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof‑of‑concept described in OffSec blog (http://offsec.com/blog/cve-2024-57727)
- **Patch Available:** Patch information unavailable.
- **Active Exploitation:** Confirmed active exploitation reported by CISA in advisory AA25-163A.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — Claude Code Action: Malicious MCP Server Configuration in PRs Enables Remote Code Execution and Secret Exfiltration

**CVE:** `CVE-2026-47751` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-8q5r-mmjf-575q>

> Due to the combination of checking out PR head branches (attacker-controlled), reading `.mcp.json` from the working directory via default setting sources, and unconditionally enabling all project MCP servers via `enableAllProjectMcpServers`, it was possible for an attacker who opened a PR containing a malicious `.mcp.json` file to achieve arbitrary code execution on the GitHub Actions runner. This…

**Parallel AI Enrichment:**

- **Technical Details:** Checking out PR head branches (attacker‑controlled), reading `.mcp.json` from the working directory via default setting sources, and unconditionally enabling all project MCP servers via `enableAllProjectMcpServers` allows a malicious `.mcp.json` in a PR to execute arbitrary code on the GitHub Actions runner and potentially exfiltrate secrets.
- **Affected Products:** anthropics/claude-code-action (GitHub Action) < 1.0.74; patched in 1.0.74
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit has been reported.
- **Patch Available:** Yes — vendor patch released (see vendor advisory URL: https://github.com/advisories/GHSA-8q5r-mmjf-575q)
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Update to patched version (>= 1.0.74). As a workaround, avoid triggering the action on untrusted PRs or disable enabling of project MCP servers; do not run the action on PRs from external contributors or use repository/workflow settings to prevent PRs from running with secrets.
- **Vendor Advisory:** https://github.com/advisories/GHSA-8q5r-mmjf-575q

---

## 3. 🟠 Zero-Day — Unpatched Langflow Flaw CVE-2026-5027 Exploited for Unauthenticated RCE

**CVE:** `CVE-2026-5027` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://thehackernews.com/2026/06/unpatched-langflow-flaw-cve-2026-5027.html>

> A high-severity unpatched security flaw in Langflow, an open-source low-code platform to build artificial intelligence (AI) applications, has come under active exploitation in the wild, according to findings from VulnCheck.

The vulnerability in question is CVE-2026-5027 (CVSS score: 8.8), a case of path traversal that could allow an attacker to write files to arbitrary locations.

&quot;The &#x27…

**Parallel AI Enrichment:**

- **Technical Details:** The POST /api/v2/files endpoint fails to sanitize the filename parameter of multipart form data, allowing path‑traversal sequences (../) to write files outside the intended upload directory, which can lead to remote code execution especially when auto‑login is enabled.
- **Affected Products:** Langflow <= 1.8.4
- **CVSS Score:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** A public proof‑of‑concept is available in the GitHub repository https://github.com/EQSTLab/CVE-2026-5027.
- **Patch Available:** No official patch has been released yet.
- **Active Exploitation:** Active exploitation in the wild has been reported, referenced by VulnCheck and reported in The Hacker News article.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — New Windows Zero-Day Exploit ‘RoguePlanet’ Released

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://www.securityweek.com/new-windows-zero-day-exploit-rogueplanet-released/>

> Exploiting a race condition in Microsoft Defender, the exploit leads to local privilege escalation to SYSTEM. The post New Windows Zero-Day Exploit ‘RoguePlanet’ Released appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** A race condition in Microsoft Defender's functionality enables a local privilege escalation where an unprivileged user can abuse Defender operations to escalate to SYSTEM.
- **Affected Products:** Microsoft Defender Antivirus on Windows 10 and Windows 11 (fully patched); specific pre‑April‑2026 Defender builds previously vulnerable — precise build list unavailable.
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof‑of‑concept exploits exist (RoguePlanet/Chaotic Eclipse/Nightmare Eclipse). Example sources: https://www.securityweek.com/new-windows-zero-day-exploit-rogueplanet-released/, https://thehackernews.com/2026/06/microsoft-defender-rogueplanet-zero-day.html, http://securityaffairs.com/193436/security/chaotic-eclipse-unveils-rogueplanet-exploit-targeting-fully-patched-windows.html, https://github.com/MSNightmare/RoguePlanet
- **Patch Available:** Microsoft has published an advisory entry for CVE-2026-33825 (https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-33825). If no full patch yet, follow Microsoft guidance in that advisory.
- **Active Exploitation:** No confirmed nation‑state or widespread in‑the‑wild exploitation reported; public PoCs have been released which increase risk.
- **Threat Actors:** None known
- **Mitigation:** Apply vendor updates/patches when available; restrict local untrusted user access; use least‑privilege accounts; monitor for local privilege escalation indicators. (Specific workaround steps unavailable.)
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an attacker injects malicious prompt text into a website or hidden code. AI systems that automatically browse or crawl the page ingest the malicious prompt, leading them to generate unauthorized commands or actions. This vector does not require direct interaction with the AI model; the compromised content acts as a conduit.
- **Affected Products:** Google Gemini Enterprise
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept known
- **Patch Available:** No patch available
- **Active Exploitation:** Yes, active exploitation reported in the wild.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) enables attackers to influence LLM behavior by injecting malicious instructions into data sources or tools used by the model (e.g., documents, files, integrated apps, or external content) so the LLM executes or follows those instructions when completing user queries; this can occur without direct user input and leverages agentic/autonomous capabilities in advanced LLMs.
- **Affected Products:** Google Workspace with Gemini
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Public proof‑of‑concepts and payloads have been documented by third parties (e.g., Forcepoint and Noma Labs).
- **Patch Available:** Vendor advisory published; no specific patch listed in materials (Vendor advisory URL above). If an explicit patch is released it will be referenced in the vendor advisory.
- **Active Exploitation:** Reports indicate payloads caught in the wild and research‑disclosed zero‑click vulnerability (GeminiJack).
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: robust input sanitization, provenance‑aware retrieval, policy and instruction filtering, runtime guardrails, limiting agentic automation where appropriate, and continuous monitoring/patching; additionally, restrict data sources, apply content filtering, and enforce least‑privilege for integrated tools.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection zero‑click vulnerability in Google Gemini Enterprise/Vertex AI Search, where malicious content can inject a crafted prompt that the model processes without user interaction, leading to arbitrary command execution.
- **Affected Products:** Google Gemini Enterprise / Vertex AI Search; Chrome (agentic browsing)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept known.
- **Patch Available:** Fixed in version 1.3 – see NVD entry for details.
- **Active Exploitation:** None known
- **Threat Actors:** None known
- **Mitigation:** Update Chrome to the latest version with the new security layer and upgrade Google Gemini Enterprise to version 1.3 or later, which includes the fix for the indirect prompt injection flaw.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Android adopted Rust to replace memory‑unsafe code and reduce memory‑safety vulnerabilities; 2025 data shows memory‑safety vulnerabilities fell below 20% of total, reflecting reduced memory‑bug density across components.
- **Affected Products:** Android platform (first-party and third-party/open-source code changes across C, C++, Java, Kotlin, and Rust)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC or weaponized exploit reported
- **Patch Available:** No specific vulnerability patch; vendor blog post describing Rust adoption and memory-safety strategy: http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html
- **Active Exploitation:** None reported
- **Threat Actors:** None known
- **Mitigation:** Continue adoption of Rust and memory-safety practices, code audits, use of safer languages for new code, and backporting fixes where feasible.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection embeds hidden malicious instructions in external data (emails, documents, calendar invites). When the AI retrieves and processes this data, the instructions are executed, allowing data exfiltration or unauthorized actions.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC available.
- **Patch Available:** Patch released in version 1.3 (no separate advisory URL).
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Implement layered defenses: validate and sanitize inputs at ingestion, enforce strict retrieval sanitization, and apply execution‑time checks. Follow the hardening guidance described in the Google Security Blog.
- **Vendor Advisory:** http://blog.google/security/mitigating-prompt-injection-attacks

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors target backbone/PE/CE routers and compromised devices, modify router firmware/configuration to maintain persistent, long‑term access, and pivot via trusted connections into other networks; they leverage credential harvesting, misuse of management interfaces, and living‑off‑the‑land techniques rather than a single disclosed CVE.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept or weaponized exploit is listed in the advisory.
- **Patch Available:** Patch availability varies by vendor and product; CISA advisory links to vendor advisories and mitigation guidance—no single universal patch.
- **Active Exploitation:** Yes—CISA and allied agencies report confirmed, widespread activity and long‑term persistent access to telecommunications, government, transportation, lodging, and military infrastructure networks by PRC state‑sponsored actors.
- **Threat Actors:** Salt Typhoon; OPERATOR PANDA; RedMike; UNC5807; GhostEmperor
- **Mitigation:** Follow CISA AA25-239A mitigations: segment and isolate management interfaces; enforce multi‑factor authentication; rotate and strengthen credentials; apply vendor patches/firmware updates from vendors linked in advisory; audit router configurations and firmware integrity; monitor for anomalous routing, persistent backdoors, and unauthorized configuration changes; implement network segmentation and zero‑trust access controls.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 11. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 12. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

---

## 13. 🟠 Zero-Day — ‘GreatXML’ Zero-Day Exploit Bypasses BitLocker

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://www.securityweek.com/greatxml-zero-day-exploit-bypasses-bitlocker/>

> The PoC exploits Microsoft Defender’s offline scan to spawn a SYSTEM shell when rebooting in Recovery Mode. The post ‘GreatXML’ Zero-Day Exploit Bypasses BitLocker appeared first on SecurityWeek .

---

## 14. 🟠 Zero-Day — Microsoft Patches Exploited Exchange Server Vulnerability

**CVE:** `CVE-2026-42897` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://www.securityweek.com/microsoft-patches-exploited-exchange-server-vulnerability/>

> The company warned about zero-day attacks exploiting the Exchange Server vulnerability CVE-2026-42897 on May 14. The post Microsoft Patches Exploited Exchange Server Vulnerability appeared first on SecurityWeek .

---

## 15. 🟠 Zero-Day — China-Linked JDY Botnet Expands to 1,500+ Devices for Cyber Reconnaissance

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://thehackernews.com/2026/06/china-linked-jdy-botnet-expands-to-1500.html>

> Cybersecurity researchers have warned of a &quot;resurgence and expansion&quot; of JDY, a covert network associated with China-nexus state-sponsored threat actors.

&quot;The JDY botnet comprises over 1,500 SOHO [small office and home office] and IoT devices and operates as a centrally controlled, high-performance scanner used to discover, fingerprint, and continuously map exposed services at scal…

---

## 16. 🟠 Zero-Day — Microsoft patches Exchange Server zero-day exploited in attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-exchange-server-zero-day-exploited-in-attacks/>

> Microsoft has patched an actively exploited Exchange Server vulnerability that allows threat actors to execute arbitrary JavaScript code in cross-site scripting (XSS) attacks targeting Outlook Web Access users. [...]

---

## 17. 🟡 High Severity — nebula-mesh: Session and OIDC state cookies lack the Secure attribute

**CVE:** `CVE-2026-48058` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-rqfj-vv8r-xhqc>

> `internal/web/session.go` and `internal/web/oidc.go` set `HttpOnly` and `SameSite=Lax` on every cookie but never `Secure`. A single plaintext request to the origin (operator on a LAN, mistyped URL, HTTP→HTTPS not strictly enforced, reverse proxy misconfiguration) discloses the session.

## Affected
All released versions up to v0.3.1.

## Impact
An attacker who can observe one HTTP request to the o…

---

## 18. 🟡 High Severity — nebula-mesh: Decrypted CA private key persists in heap after signing

**CVE:** `CVE-2026-48025` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-8h84-fhqq-q58v>

> `internal/pki/resolver.go:36-64` constructs a `CAManager` with the plaintext `ed25519.PrivateKey` after unwrapping via the master key; `internal/pki/ca.go:13-16` stores it. Callers at `internal/api/enroll.go:116`, `internal/api/updates.go:297`, and `internal/api/mobile_bundle.go:40` use the manager for one `Sign()` and drop the reference on function return — but the underlying slice contents are n…

---

## 19. 🟡 High Severity — OpenTelemetry Operator for Kubernetes's ServiceMonitor bearerTokenFile reads arbitrary local file and sends contents as bearer auth

**CVE:** `CVE-2026-47701` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-cxh2-4639-vmc5>

> ## Affected

Repository: github.com/open-telemetry/opentelemetry-operator
Component: cmd/otel-allocator (TargetAllocator)
Companion: Prometheus Operator API types (CRDs)

## Summary

OpenTelemetry Operator&#x27;s TargetAllocator watches `ServiceMonitor` resources via the Prometheus Operator CR watcher and converts each selected endpoint into a Prometheus scrape configuration entry. The endpoint fi…

---

## 20. 🟡 High Severity — Ivanti, Fortinet, and SAP Release Patches for Multiple Critical Vulnerabilities

**CVE:** `CVE-2026-25089` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://thehackernews.com/2026/06/ivanti-fortinet-and-sap-release-patches.html>

> Fortinet, Ivanti, and SAP have released security updates to address multiple critical security vulnerabilities that could result in arbitrary code execution and information disclosure.

The security flaw patched by Fortinet relates to a command injection vulnerability in FortiSandbox, FortiSandbox Cloud, and FortiSandbox PaaS WEB UI. It&#x27;s tracked as CVE-2026-25089 (CVSS score: 9.1).

&quot;An

---

## 21. 🟡 High Severity — CISA Adds Cisco, Chrome, and Arista Flaws to KEV Catalog Amid Active Exploitation

**CVE:** `CVE-2026-20245` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://thehackernews.com/2026/06/cisa-adds-cisco-chrome-and-arista-flaws.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added three new vulnerabilities to its Known Exploited Vulnerabilities (KEV) catalog, following reports of active exploitation.

The list of vulnerabilities is as follows -


  CVE-2026-20245 (CVSS score: 7.8) - An improper encoding or escaping of output vulnerability in Cisco Catalyst SD-WAN Manager that could allow an

---

## 22. 🟡 High Severity — Nezha's private services (`EnableShowInService: false`) are enumerable via per-server endpoints, leaking name and timing data

**CVE:** `CVE-2026-49397` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-vrmh-5mmx-hjwx>

> # Private services (`EnableShowInService: false`) are enumerable via per-server endpoints, leaking name and timing data

**CWE**: CWE-285 (Improper Authorization) via CWE-200 (Exposure of Sensitive Information to an Unauthorized Actor) and CWE-863 (Incorrect Authorization — inconsistent gating across data-reader paths)

**CVSS v3.1**: `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N` → 5.3 (Medium)

…

---

## 23. 🟡 High Severity — Go Restful API Boilerplate: Hardcoded JWT Secret "random" Allows Token Forgery

**CVE:** `CVE-2026-48031` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-mqq6-462x-jxmm>

> ## Vulnerability: CWE-798 — Hardcoded JWT Secret + Broken Mitigation

### Affected Component
- `github.com/dhax/go-base` — Go REST API boilerplate (go-chi/jwtauth/v5, Viper, PostgreSQL/Bun)
- 1,685 stars on GitHub

### Vulnerability Locations

| File | Line | Role |
|------|------|------|
| `dev.env` | 10 | `AUTH_JWT_SECRET=random` — template default shipped to all users |
| `cmd/serve.go` | 35 | …

---

## 24. 🟡 High Severity — Papra HTTP redirect bypass can lead to SSRF via webhook delivery system

**CVE:** `CVE-2026-48051` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-5g86-85rp-f9hx>

> ### Summary

Papra&#x27;s webhook delivery system contains an SSRF protection bypass that allows any authenticated organisation member to cause the server to make HTTP requests to internal addresses — loopback, link-local, and RFC-1918 ranges. The SSRF protection validates the registered webhook URL but ignores redirect destinations. The HTTP client (`ofetch`) follows 3xx responses automatically, …

---

## 25. 🟡 High Severity — @hulumi/baseline: AccountFoundation reuse paths silently downgrade GuardDuty / Security Hub posture

**CVE:** `CVE-2026-48037` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-cj8g-prcm-mfg5>

> **Affected:** `@hulumi/baseline` `&lt; 1.4.0` — **Fixed in:** `1.4.0` — **Severity:** Medium — **CWE-693 (Protection Mechanism Failure)**

#### Summary

`AccountFoundation` can either create AWS detective services (GuardDuty for threat detection, Security Hub for compliance dashboards) or reuse pre-existing ones via opt-in flags. The reuse paths just imported the existing resources and reported su…

---

## 26. 🟡 High Severity — @hulumi/baseline: AccountFoundation audit-delivery S3 bucket could be silently weakened

**CVE:** `CVE-2026-48035` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-2mxr-p26x-mj73>

> **Affected:** `@hulumi/baseline` `&lt; 1.4.0` — **Fixed in:** `1.4.0` — **Severity:** High — **CWE-1059 (Insufficient Technical Documentation / Behavioral Inconsistency)**

#### Summary

The S3 bucket that `AccountFoundation` creates to receive CloudTrail and AWS Config audit logs is meant to be tamper-resistant — if someone with delete access can erase from it, the forensic trail is gone. There w…

---

## 27. 🟡 High Severity — @hulumi/policies has a HULUMI-H5 bypass via decoy sibling resources targeting a different bucket

**CVE:** `CVE-2026-48034` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-9vc9-4jv3-rf86>

> **Affected:** `@hulumi/policies` `&lt; 1.4.0` — **Fixed in:** `1.4.0` — **Severity:** High — **CWE-284 (Improper Access Control)**

#### Summary

HULUMI-H1 forbids raw `aws:s3:Bucket` outside of Hulumi&#x27;s `SecureBucket` component, with one exemption: a raw bucket that&#x27;s a child of a `SecureBucket` is allowed because the component is responsible for the hardening. HULUMI-H5 is the defence-…

---

## 28. 🟡 High Severity — @hulumi/policies bypasses policy packs with a forged Pulumi-URN logical name

**CVE:** `CVE-2026-48033` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-rhgj-6g2c-frmm>

> **Affected:** `@hulumi/policies` `&lt; 1.4.0` — **Fixed in:** `1.4.0` — **Severity:** High — **CWE-693 (Protection Mechanism Failure)**

#### Summary

Pulumi gives every cloud resource a structured URN that includes the resource&#x27;s type chain (`hulumi:baseline:aws:SecureBucket$aws:s3/bucketV2:BucketV2`) and the _logical name_ the developer freely chose (anything after the final `::`). Several …

---

## 29. 🟡 High Severity — @hulumi/policies bypasses IAM-role policy checks when the role trusts multiple OIDC providers

**CVE:** `CVE-2026-48032` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-g759-4pxw-6692>

> **Affected:** `@hulumi/policies` `&lt; 1.4.0` — **Fixed in:** `1.4.0` — **Severity:** High — **CWE-697 (Incorrect Comparison)**

#### Summary

AWS IAM trust policies can list more than one federated identity provider — for example, a role that accepts BOTH GitHub Actions OIDC and Google&#x27;s OIDC. The `G_OIDC_1` and `G_OIDC_2` policy rules are supposed to flag IAM roles whose GitHub-OIDC trust i…

---

## 30. 🟡 High Severity — CVE-2026-10520, CVE-2026-10523 - Multiple critical vulnerabilities affecting Ivanti Sentry

**CVE:** `CVE-2026-10520` | `CVE-2026-10523` | `CVE-2023-38035` | `CVE-2020-15505` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://www.rapid7.com/blog/post/etr-cve-2026-10520-cve-2026-10523-multiple-critical-vulnerabilities-affecting-ivanti-sentry>

> Overview On June 9, 2026, Ivanti published a security advisory for two critical vulnerabilities affecting Ivanti Sentry (formerly known as MobileIron Sentry), which per the vendor website is an “in-line gateway that manages, encrypts, and secures traffic between the mobile device and back-end enterprise systems”. The most severe issue, CVE-2026-10520 , is an OS command injection vulnerability with…

---

## 31. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
