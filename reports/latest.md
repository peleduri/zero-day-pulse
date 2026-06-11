# Zero Day Pulse

> **Generated:** 2026-06-11 02:32 UTC &nbsp;|&nbsp; **Total:** 32 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 17 &nbsp;|&nbsp; 🟡 High: 15 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal vulnerability in SimpleHelp web interface allows unauthenticated remote attackers to read arbitrary files (logs, configuration, credentials) by supplying crafted path inputs to vulnerable endpoints.
- **Affected Products:** SimpleHelp Remote Support / Remote Monitoring and Management (RMM) – versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true - public PoC reported (OffSec blog)
- **Patch Available:** true - vendor released advisory/patch (Broadcom advisory)
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (likely DragonForce/known ransomware groups)
- **Mitigation:** Immediately upgrade SimpleHelp to the fixed version per vendor advisory; if a patch cannot be applied, isolate/unexpose SimpleHelp from the internet, block vulnerable endpoints, rotate credentials found in configuration files, and monitor for indicators of compromise per CISA guidance.
- **Vendor Advisory:** https://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — Claude Code Action: Malicious MCP Server Configuration in PRs Enables Remote Code Execution and Secret Exfiltration

**CVE:** `CVE-2026-47751` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-8q5r-mmjf-575q>

> Due to the combination of checking out PR head branches (attacker-controlled), reading `.mcp.json` from the working directory via default setting sources, and unconditionally enabling all project MCP servers via `enableAllProjectMcpServers`, it was possible for an attacker who opened a PR containing a malicious `.mcp.json` file to achieve arbitrary code execution on the GitHub Actions runner. This…

**Parallel AI Enrichment:**

- **Technical Details:** When the action checks out PR head branches (attacker‑controlled) and reads a malicious .mcp.json from the working directory via default setting sources while unconditionally enabling all project MCP servers through enableAllProjectMcpServers, an attacker can supply a malicious MCP server configuration in a PR to cause the action to connect to and run code from attacker‑controlled MCP servers, enabling remote code execution on the GitHub Actions runner and potential exfiltration of workflow secrets available to privileged users who trigger the action on the PR.
- **Affected Products:** Claude Code Action (GitHub Action) — configurations that check out PR head branches and use default setting sources that read .mcp.json and enableAllProjectMcpServers
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — https://github.com/advisories/GHSA-8q5r-mmjf-575q
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply vendor patch per advisory; until patched, do not run the vulnerable Claude action on untrusted PRs, disable automatic reading of .mcp.json from workdir or disable enableAllProjectMcpServers, require maintainers to merge or reproduce fixes in non‑PR environments, and restrict secrets and tokens in workflows that could be exposed.
- **Vendor Advisory:** https://github.com/advisories/GHSA-8q5r-mmjf-575q

---

## 3. 🟠 Zero-Day — Unpatched Langflow Flaw CVE-2026-5027 Exploited for Unauthenticated RCE

**CVE:** `CVE-2026-5027` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://thehackernews.com/2026/06/unpatched-langflow-flaw-cve-2026-5027.html>

> A high-severity unpatched security flaw in Langflow, an open-source low-code platform to build artificial intelligence (AI) applications, has come under active exploitation in the wild, according to findings from VulnCheck.

The vulnerability in question is CVE-2026-5027 (CVSS score: 8.8), a case of path traversal that could allow an attacker to write files to arbitrary locations.

&quot;The &#x27…

**Parallel AI Enrichment:**

- **Technical Details:** A path traversal vulnerability in the POST /api/v2/files endpoint fails to sanitize the multipart 'filename' parameter, allowing attackers to include '../' sequences to write files to arbitrary filesystem locations; because Langflow enables unauthenticated auto-login by default, an attacker can obtain a session and trigger file writes leading to remote code execution.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor patch/advisory; if a patch is unavailable, block or restrict access to Langflow instances (network‑level firewall, IP allowlists), disable unauthenticated auto‑login, restrict or remove exposure of the /api/v2/files endpoint, apply WAF rules to block path‑traversal payloads, and monitor for unexpected file writes and new sessions.
- **Vendor Advisory:** https://github.com/langflow-ai/langflow/security/advisories

---

## 4. 🟠 Zero-Day — New Windows Zero-Day Exploit ‘RoguePlanet’ Released

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://www.securityweek.com/new-windows-zero-day-exploit-rogueplanet-released/>

> Exploiting a race condition in Microsoft Defender, the exploit leads to local privilege escalation to SYSTEM. The post New Windows Zero-Day Exploit ‘RoguePlanet’ Released appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is a TOCTOU race condition and path‑confusion in Microsoft Defender’s signature/update workflow. The exploit abuses the Volume Shadow Copy Service (VSS), the Cloud Files API, opportunistic locks, and Windows update/definition mechanisms to read shadow‑copy‑backed registry hives (SAM) and obtain credential material, resulting in local privilege escalation to SYSTEM.
- **Affected Products:** Microsoft Defender Antivirus on Windows 10 and Windows 11 (pre‑patch)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Apply any available Microsoft updates immediately; enable Defender Tamper Protection; restrict local unprivileged user access; monitor for suspicious local privilege escalation activity and credential dumping. If no patch is available, consider temporarily disabling Defender’s automatic definition update features only as a last resort and in controlled environments.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — Microsoft Patches Record 206 Flaws, Including Three Zero-Days and Critical RCE Bugs

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://thehackernews.com/2026/06/microsoft-patches-record-206-flaws.html>

> Microsoft on Tuesday released fixes for a record 206 security vulnerabilities impacting its software portfolio, including three flaws that have been publicly disclosed at the time of release.

Of the 206 flaws, 39 are rated Critical, and 167 are rated Important in severity. This includes 63 privilege escalation, 56 remote code execution, 30 information disclosure, 27 spoofing, 20 security

**Parallel AI Enrichment:**

- **Technical Details:** Technical details vary by CVE; the release patched multiple classes of vulnerabilities including privilege escalation, remote code execution, information disclosure, and spoofing across multiple Microsoft products.
- **Affected Products:** Windows 10, Windows 11, Windows Server releases, Microsoft Office/Office Components, Microsoft Edge (Chromium-based), Azure services, other Microsoft components
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true - https://msrc.microsoft.com/update-guide
- **Active Exploitation:** true - https://www.zerodayinitiative.com/blog/2026/6/9/the-june-2026-security-update-review
- **Threat Actors:** None known
- **Mitigation:** Apply the official Microsoft updates from the MSRC Update Guide / Windows Update immediately. Where immediate patching is not possible, follow vendor workarounds listed per-CVE in Microsoft advisories (disable affected features, restrict access, apply configuration mitigations).
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide

---

## 6. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an attack where malicious instructions are embedded in external content (web pages, files, or retrieved documents) that an AI agent retrieves and executes, bypassing model/system safeguards. Exploits include zero‑click IPI demonstrated by Noma Labs (GeminiJack) against Google Gemini Enterprise leveraging crafted external content to cause unintended agent behavior.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Layered defensive controls — input/output filtering, retrieval sanitization, provenance tagging, strict tool/agent permissions, RAG source validation, continuous monitoring, and vendor‑provided mitigations outlined in Google's advisory.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 7. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when an attacker embeds malicious instructions into the data sources, tools, or context that a large language model consumes. The LLM then follows these injected prompts, potentially executing harmful commands or revealing data, even when the end‑user does not directly supply the malicious input.
- **Affected Products:** Google Workspace (Gemini integration)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (http://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads)
- **Patch Available:** true (http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html)
- **Active Exploitation:** true (http://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads)
- **Threat Actors:** None known
- **Mitigation:** Implement Google’s layered defense: validate and sanitize all inputs to Gemini, isolate LLM interactions in sandboxed environments, monitor for anomalous prompt patterns, restrict tool and API access to trusted services, and keep Gemini and Workspace components up‑to‑date.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 8. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection where malicious web pages craft content that manipulates an agentic browser's AI prompts, potentially causing unsafe actions. Google mitigates this with layered defenses, a supervisory second agent, origin restrictions, and prompt‑injection blocking.
- **Affected Products:** Chrome (agentic browsing / Gemini integration)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use the latest Chrome with agentic protections; restrict untrusted sites from granting agentic permissions; follow vendor guidance in the blog post.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 9. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow in the Rust‑based CrabbyAVIF library would have allowed out‑of‑bounds writes, but Android’s Scudo hardened allocator placed guard pages around secondary allocations, rendering the overflow non‑exploitable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the CrabbyAVIF patch from the AOSP repository (https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050) and ensure Scudo hardened allocator is enabled on the device.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-11-01

---

## 10. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when an LLM or agent retrieves external data (emails, documents, web pages, calendar invites, etc.) that contains hidden malicious instructions which are then interpreted as part of the model prompt, causing data exfiltration or unauthorized actions. The attack chain typically involves retrieval of attacker‑controlled content, prompt‑merging, and execution by an agent with privileged access.
- **Affected Products:** Google Gemini (agentic features), Chrome agentic/browser integrations, LangChain GmailToolkit (prior to v1.3)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply vendor patches where available (e.g., LangChain GmailToolkit >=1.3); implement layered defenses such as input provenance checks, retrieval filtering, content sanitization, multi‑agent monitoring/guardrails, least‑privilege access to secrets, telemetry and anomaly detection, and deny‑by‑default for risky actions.
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

## 13. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

---

## 14. 🟠 Zero-Day — China-Linked JDY Botnet Expands to 1,500+ Devices for Cyber Reconnaissance

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://thehackernews.com/2026/06/china-linked-jdy-botnet-expands-to-1500.html>

> Cybersecurity researchers have warned of a &quot;resurgence and expansion&quot; of JDY, a covert network associated with China-nexus state-sponsored threat actors.

&quot;The JDY botnet comprises over 1,500 SOHO [small office and home office] and IoT devices and operates as a centrally controlled, high-performance scanner used to discover, fingerprint, and continuously map exposed services at scal…

---

## 15. 🟠 Zero-Day — Microsoft patches Exchange Server zero-day exploited in attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-exchange-server-zero-day-exploited-in-attacks/>

> Microsoft has patched an actively exploited Exchange Server vulnerability that allows threat actors to execute arbitrary JavaScript code in cross-site scripting (XSS) attacks targeting Outlook Web Access users. [...]

---

## 16. 🟠 Zero-Day — Microsoft patches YellowKey, GreenPlasma, MiniPlasma zero-days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-yellowkey-greenplasma-miniplasma-zero-days/>

> On Tuesday, Microsoft patched two zero-day vulnerabilities that let attackers gain SYSTEM privileges on fully patched Windows systems, and a third one that grants access to BitLocker-protected drives. [...]

---

## 17. 🟠 Zero-Day — Microsoft Defender RoguePlanet Zero-Day Grants SYSTEM Access on Updated Windows

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://thehackernews.com/2026/06/microsoft-defender-rogueplanet-zero-day.html>

> The anonymous security researcher going by the name Chaotic Eclipse (aka Nightmare-Eclipse) has released a proof-of-concept (PoC) exploit for yet another Microsoft Defender zero-day named RoguePlanet.

&quot;The exploit is a race condition, so it&#x27;s a hit or miss,&quot; the researcher, who published the exploit under a new GitHub account &quot;MSNightmare&quot; said. &quot;I have managed to ge…

---

## 18. 🟡 High Severity — nebula-mesh: Session and OIDC state cookies lack the Secure attribute

**CVE:** `CVE-2026-48058` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-rqfj-vv8r-xhqc>

> `internal/web/session.go` and `internal/web/oidc.go` set `HttpOnly` and `SameSite=Lax` on every cookie but never `Secure`. A single plaintext request to the origin (operator on a LAN, mistyped URL, HTTP→HTTPS not strictly enforced, reverse proxy misconfiguration) discloses the session.

## Affected
All released versions up to v0.3.1.

## Impact
An attacker who can observe one HTTP request to the o…

---

## 19. 🟡 High Severity — nebula-mesh: Decrypted CA private key persists in heap after signing

**CVE:** `CVE-2026-48025` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-8h84-fhqq-q58v>

> `internal/pki/resolver.go:36-64` constructs a `CAManager` with the plaintext `ed25519.PrivateKey` after unwrapping via the master key; `internal/pki/ca.go:13-16` stores it. Callers at `internal/api/enroll.go:116`, `internal/api/updates.go:297`, and `internal/api/mobile_bundle.go:40` use the manager for one `Sign()` and drop the reference on function return — but the underlying slice contents are n…

---

## 20. 🟡 High Severity — OpenTelemetry Operator for Kubernetes's ServiceMonitor bearerTokenFile reads arbitrary local file and sends contents as bearer auth

**CVE:** `CVE-2026-47701` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-cxh2-4639-vmc5>

> ## Affected

Repository: github.com/open-telemetry/opentelemetry-operator
Component: cmd/otel-allocator (TargetAllocator)
Companion: Prometheus Operator API types (CRDs)

## Summary

OpenTelemetry Operator&#x27;s TargetAllocator watches `ServiceMonitor` resources via the Prometheus Operator CR watcher and converts each selected endpoint into a Prometheus scrape configuration entry. The endpoint fi…

---

## 21. 🟡 High Severity — Ivanti, Fortinet, and SAP Release Patches for Multiple Critical Vulnerabilities

**CVE:** `CVE-2026-25089` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://thehackernews.com/2026/06/ivanti-fortinet-and-sap-release-patches.html>

> Fortinet, Ivanti, and SAP have released security updates to address multiple critical security vulnerabilities that could result in arbitrary code execution and information disclosure.

The security flaw patched by Fortinet relates to a command injection vulnerability in FortiSandbox, FortiSandbox Cloud, and FortiSandbox PaaS WEB UI. It&#x27;s tracked as CVE-2026-25089 (CVSS score: 9.1).

&quot;An

---

## 22. 🟡 High Severity — CISA Adds Cisco, Chrome, and Arista Flaws to KEV Catalog Amid Active Exploitation

**CVE:** `CVE-2026-20245` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://thehackernews.com/2026/06/cisa-adds-cisco-chrome-and-arista-flaws.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added three new vulnerabilities to its Known Exploited Vulnerabilities (KEV) catalog, following reports of active exploitation.

The list of vulnerabilities is as follows -


  CVE-2026-20245 (CVSS score: 7.8) - An improper encoding or escaping of output vulnerability in Cisco Catalyst SD-WAN Manager that could allow an

---

## 23. 🟡 High Severity — Nezha's private services (`EnableShowInService: false`) are enumerable via per-server endpoints, leaking name and timing data

**CVE:** `CVE-2026-49397` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-vrmh-5mmx-hjwx>

> # Private services (`EnableShowInService: false`) are enumerable via per-server endpoints, leaking name and timing data

**CWE**: CWE-285 (Improper Authorization) via CWE-200 (Exposure of Sensitive Information to an Unauthorized Actor) and CWE-863 (Incorrect Authorization — inconsistent gating across data-reader paths)

**CVSS v3.1**: `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N` → 5.3 (Medium)

…

---

## 24. 🟡 High Severity — Go Restful API Boilerplate: Hardcoded JWT Secret "random" Allows Token Forgery

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

## 25. 🟡 High Severity — Papra HTTP redirect bypass can lead to SSRF via webhook delivery system

**CVE:** `CVE-2026-48051` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-5g86-85rp-f9hx>

> ### Summary

Papra&#x27;s webhook delivery system contains an SSRF protection bypass that allows any authenticated organisation member to cause the server to make HTTP requests to internal addresses — loopback, link-local, and RFC-1918 ranges. The SSRF protection validates the registered webhook URL but ignores redirect destinations. The HTTP client (`ofetch`) follows 3xx responses automatically, …

---

## 26. 🟡 High Severity — @hulumi/baseline: AccountFoundation reuse paths silently downgrade GuardDuty / Security Hub posture

**CVE:** `CVE-2026-48037` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-cj8g-prcm-mfg5>

> **Affected:** `@hulumi/baseline` `&lt; 1.4.0` — **Fixed in:** `1.4.0` — **Severity:** Medium — **CWE-693 (Protection Mechanism Failure)**

#### Summary

`AccountFoundation` can either create AWS detective services (GuardDuty for threat detection, Security Hub for compliance dashboards) or reuse pre-existing ones via opt-in flags. The reuse paths just imported the existing resources and reported su…

---

## 27. 🟡 High Severity — @hulumi/baseline: AccountFoundation audit-delivery S3 bucket could be silently weakened

**CVE:** `CVE-2026-48035` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-2mxr-p26x-mj73>

> **Affected:** `@hulumi/baseline` `&lt; 1.4.0` — **Fixed in:** `1.4.0` — **Severity:** High — **CWE-1059 (Insufficient Technical Documentation / Behavioral Inconsistency)**

#### Summary

The S3 bucket that `AccountFoundation` creates to receive CloudTrail and AWS Config audit logs is meant to be tamper-resistant — if someone with delete access can erase from it, the forensic trail is gone. There w…

---

## 28. 🟡 High Severity — @hulumi/policies has a HULUMI-H5 bypass via decoy sibling resources targeting a different bucket

**CVE:** `CVE-2026-48034` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-9vc9-4jv3-rf86>

> **Affected:** `@hulumi/policies` `&lt; 1.4.0` — **Fixed in:** `1.4.0` — **Severity:** High — **CWE-284 (Improper Access Control)**

#### Summary

HULUMI-H1 forbids raw `aws:s3:Bucket` outside of Hulumi&#x27;s `SecureBucket` component, with one exemption: a raw bucket that&#x27;s a child of a `SecureBucket` is allowed because the component is responsible for the hardening. HULUMI-H5 is the defence-…

---

## 29. 🟡 High Severity — @hulumi/policies bypasses policy packs with a forged Pulumi-URN logical name

**CVE:** `CVE-2026-48033` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-rhgj-6g2c-frmm>

> **Affected:** `@hulumi/policies` `&lt; 1.4.0` — **Fixed in:** `1.4.0` — **Severity:** High — **CWE-693 (Protection Mechanism Failure)**

#### Summary

Pulumi gives every cloud resource a structured URN that includes the resource&#x27;s type chain (`hulumi:baseline:aws:SecureBucket$aws:s3/bucketV2:BucketV2`) and the _logical name_ the developer freely chose (anything after the final `::`). Several …

---

## 30. 🟡 High Severity — @hulumi/policies bypasses IAM-role policy checks when the role trusts multiple OIDC providers

**CVE:** `CVE-2026-48032` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-g759-4pxw-6692>

> **Affected:** `@hulumi/policies` `&lt; 1.4.0` — **Fixed in:** `1.4.0` — **Severity:** High — **CWE-697 (Incorrect Comparison)**

#### Summary

AWS IAM trust policies can list more than one federated identity provider — for example, a role that accepts BOTH GitHub Actions OIDC and Google&#x27;s OIDC. The `G_OIDC_1` and `G_OIDC_2` policy rules are supposed to flag IAM roles whose GitHub-OIDC trust i…

---

## 31. 🟡 High Severity — CVE-2026-10520, CVE-2026-10523 - Multiple critical vulnerabilities affecting Ivanti Sentry

**CVE:** `CVE-2026-10520` | `CVE-2026-10523` | `CVE-2023-38035` | `CVE-2020-15505` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://www.rapid7.com/blog/post/etr-cve-2026-10520-cve-2026-10523-multiple-critical-vulnerabilities-affecting-ivanti-sentry>

> Overview On June 9, 2026, Ivanti published a security advisory for two critical vulnerabilities affecting Ivanti Sentry (formerly known as MobileIron Sentry), which per the vendor website is an “in-line gateway that manages, encrypts, and secures traffic between the mobile device and back-end enterprise systems”. The most severe issue, CVE-2026-10520 , is an OS command injection vulnerability with…

---

## 32. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
