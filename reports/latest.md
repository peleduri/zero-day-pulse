# Zero Day Pulse

> **Generated:** 2026-06-11 15:32 UTC &nbsp;|&nbsp; **Total:** 24 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 10 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** A path traversal vulnerability in SimpleHelp (versions ≤5.5.7) lets unauthenticated attackers read arbitrary files on the server by supplying crafted file‑path parameters, enabling disclosure of sensitive data and further compromise.
- **Affected Products:** SimpleHelp remote support / RMM software, version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (unattributed)
- **Mitigation:** Upgrade SimpleHelp to the patched version supplied by the vendor. If immediate patching is not possible, restrict network access to the management interface (IP allowlists, firewalls), disable Internet exposure, segment the network, and rotate any discovered credentials.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — Criminal AI-as-a-Service in 2026: How the Underground Market Is Operationalizing Cybercrime

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://www.rapid7.com/blog/post/tr-criminal-ai-underground-market-operationalizing-cybercrime-2026>

> Introduction The underground market for criminally oriented generative AI has moved beyond the early hype surrounding &#x27;malicious chatbots.&#x27; The gradual integration of AI as a productivity layer within cybercrime operations has become the dominant story, indicating that while the potential for fully autonomous AI hacking systems is possible, attackers are not embracing them as expected. I…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — Claude Code Action: Malicious MCP Server Configuration in PRs Enables Remote Code Execution and Secret Exfiltration

**CVE:** `CVE-2026-47751` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-8q5r-mmjf-575q>

> Due to the combination of checking out PR head branches (attacker-controlled), reading `.mcp.json` from the working directory via default setting sources, and unconditionally enabling all project MCP servers via `enableAllProjectMcpServers`, it was possible for an attacker who opened a PR containing a malicious `.mcp.json` file to achieve arbitrary code execution on the GitHub Actions runner. This…

**Parallel AI Enrichment:**

- **Technical Details:** The Claude Code Action checks out PR head branches, reads a `.mcp.json` configuration file from the repository, and unconditionally enables all project MCP servers via `enableAllProjectMcpServers`. An attacker can submit a PR containing a malicious `.mcp.json`, causing arbitrary code execution on the GitHub Actions runner and allowing exfiltration of workflow secrets such as API keys and tokens.
- **Affected Products:** Claude Code Action (GitHub Action)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://github.com/advisories/GHSA-8q5r-mmjf-575q

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is a technique where an attacker embeds malicious prompt content into data that an AI system later consumes, causing the model to follow the attacker’s instructions or leak information. In the GeminiJack example, the payload was delivered without user interaction (zero‑click) inside a Google Gemini Enterprise request, demonstrating a direct exploitation path.
- **Affected Products:** Google Gemini Enterprise
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Implement continuous monitoring of AI inputs, apply strict input validation and sanitization, employ prompt‑guard mechanisms, and enforce strong authentication for AI‑driven services.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when attackers inject malicious instructions into external data sources or tools that a multi‑source LLM/agent ingests during query processing; the model then follows those injected instructions, potentially without user input — e.g., the GeminiJack zero‑click attack used content delivered into an agented workflow that caused unwanted behavior.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Use Google's layered defense recommendations: continuous content filtering and sanitization, provenance checks, stronger input validation and policies for data ingestion, tool access restrictions, and continual model/harness hardening as described in the Google advisory.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) — malicious web content crafts inputs that influence agentic AI instructions or LLM prompts processed by Gemini in Chrome, causing the agent to perform unsafe actions or disclose sensitive data.
- **Affected Products:** Google Chrome (agentic/Gemini-enabled builds)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Chrome layered defenses (origin‑restrictions, second ‘watcher’ agent, input sanitization, policy controls); follow vendor guidance and update Chrome. Use restrictive policies and avoid untrusted sites for agentic actions.
- **Vendor Advisory:** http://blog.google/security/architecting-security-for-agentic

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow in the CrabbyAVIF Rust crate (unsafe Rust path) was identified pre‑release. Android’s Scudo hardened allocator and guard pages rendered the issue non‑exploitable and turned silent corruption into a noisy crash; the bug was assigned CVE‑2025‑48530 for tracking.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use Scudo hardened allocator (guard pages) and improved crash reporting; prioritize unsafe‑Rust code review, add unsafe‑specific training, encapsulate unsafe code, and apply layered defenses such as static analysis, runtime mitigations, and sandboxing.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection embeds malicious instructions in external data sources (emails, documents, calendar invites, or hidden website code) that are later consumed by AI systems; when the AI incorporates or executes user‑provided external content, these hidden instructions can cause data exfiltration or unintended actions by altering the assistant's behavior via injected directives.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Apply layered defenses — validate and sanitize external inputs, treat external content as untrusted (do not automatically execute instructions found there), enforce least privilege for model access to sensitive data, use provenance and integrity checks, implement content classification and filtering for potentially malicious directives, require explicit user confirmation before executing high‑risk actions, monitor and log model decisions, and deploy model‑level guardrails or classifier‑based prompt‑safety checks.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC‑linked actors target large backbone routers, provider edge (PE) and customer edge (CE) routers, modify routers to maintain persistent, long‑term access, and leverage compromised devices and trusted connections to pivot into other networks for espionage.
- **Affected Products:** Telecommunications backbone routers, provider edge (PE) routers, customer edge (CE) routers, compromised routers and IoT devices
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon (aka PRC state-sponsored actors), OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Apply CISA recommendations: monitor and harden router and edge device configurations, restrict management access, rotate credentials, deploy network segmentation, apply vendor mitigations and monitoring for indicators of compromise, and follow vendor‑specific advisories.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** The advisory describes a long-running Russian state-sponsored cyber espionage campaign since 2022 by the GRU 85th GTsSS (Unit 26165) targeting Western logistics, transportation, and technology companies involved in coordination, transport, and delivery of assistance to Ukraine; tactics include network intrusion and espionage tradecraft (detailed TTPs and specific vulnerability mechanisms unavailable).
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** true
- **Threat Actors:** GRU 85th Main Special Service Center (85th GTsSS), Unit 26165 — also tracked as APT28/Fancy Bear/Strontium (Russian GRU)
- **Mitigation:** Apply CISA and partner mitigations and hardening guidance from the advisory (network monitoring, patching, credential protection, MFA, incident response readiness). See the advisory URL above for full recommendations.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 11. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

---

## 12. 🟠 Zero-Day — Oracle Addresses PeopleSoft Vulnerability Amid Reports of Zero-Day Attacks

**CVE:** `CVE-2026-35273` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://www.securityweek.com/oracle-addresses-peoplesoft-vulnerability-amid-reports-of-zero-day-attacks/>

> Oracle has released mitigations for CVE-2026-35273, but it has not said whether it’s a zero-day exploited in ShinyHunters attacks. The post Oracle Addresses PeopleSoft Vulnerability Amid Reports of Zero-Day Attacks appeared first on SecurityWeek .

---

## 13. 🟠 Zero-Day — ‘GreatXML’ Zero-Day Exploit Bypasses BitLocker

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://www.securityweek.com/greatxml-zero-day-exploit-bypasses-bitlocker/>

> The PoC exploits Microsoft Defender’s offline scan to spawn a SYSTEM shell when rebooting in Recovery Mode. The post ‘GreatXML’ Zero-Day Exploit Bypasses BitLocker appeared first on SecurityWeek .

---

## 14. 🟠 Zero-Day — China-Linked JDY Botnet Expands to 1,500+ Devices for Cyber Reconnaissance

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://thehackernews.com/2026/06/china-linked-jdy-botnet-expands-to-1500.html>

> Cybersecurity researchers have warned of a &quot;resurgence and expansion&quot; of JDY, a covert network associated with China-nexus state-sponsored threat actors.

&quot;The JDY botnet comprises over 1,500 SOHO [small office and home office] and IoT devices and operates as a centrally controlled, high-performance scanner used to discover, fingerprint, and continuously map exposed services at scal…

---

## 15. 🟡 High Severity — python-zeroconf: Unbounded TC-deferred queue allows LAN-local memory exhaustion via spoofed-source flood

**CVE:** `CVE-2026-48045` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-9663-mqmp-p9mm>

> ### Impact

`AsyncListener.handle_query_or_defer` retained every truncated (TC-bit) incoming query in `self._deferred[addr]` and armed a per-addr timer in `self._timers[addr]` that flushed the reassembled query within ~500 ms (RFC 6762 §18.5). Neither the per-addr list nor the number of distinct `addr` keys was capped, and the dedup check (`for incoming in reversed(deferred): if incoming.data == m…

---

## 16. 🟡 High Severity — Meta Ads MCP: Unauthenticated HTTP MCP Tool Execution Leaks Operator Meta Access Token

**CVE:** `CVE-2026-48039` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-9gw6-46qc-99vr>

> # Unauthenticated HTTP MCP Tool Execution Leaks Operator Meta Access Token

| Field            | Value |
| ---------------- | ----- |
| Repository       | pipeboard-co/meta-ads-mcp |
| Affected version | ≤ 1.0.101 (commit 496c988 ~ 7d14226); Versions 1.0.102–1.0.105 lack git tags, so patch status is unconfirmed. |
| Vulnerability    | CWE-287 — Improper Authentication |
| Severity         | Critic…

---

## 17. 🟡 High Severity — @hapi/wreck: Sensitive credential headers leak across cross-port and cross-scheme redirects

**CVE:** `CVE-2026-48022` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-x426-x7cc-3fpc>

> ### Impact
Wreck strips credential headers (Authorization, Cookie, Proxy-Authorization) before following a cross-origin redirect, but the origin check compares hostnames only and ignores scheme and port. As a result, credentials are forwarded intact across same-host port changes and HTTPS-to-HTTP downgrades, allowing a co-tenant on an adjacent port or a network-position attacker capable of forging…

---

## 18. 🟡 High Severity — Netty's Lack of Lifecycle Cleanup Leads to Pooled ByteBuf Leak in RedisArrayAggregator

**CVE:** `CVE-2026-48006` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-6jv9-x5w9-2ccm>

> ### Impact
The RedisArrayAggregator handler permanently leaks pooled direct-memory buffers when a Redis pipeline connection closes before a RESP array aggregate completes. The handler retains child messages in per-handler state (`depths` field) but defines no `channelInactive`, `handlerRemoved`, or `exceptionCaught` method to release them when the pipeline tears down. Because the leaked buffers ar…

---

## 19. 🟡 High Severity — PDM: Project-Controlled `.pdm-plugins` Content Executes Before CLI Parsing

**CVE:** `CVE-2026-47781` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-qq6c-99pv-prvf>

> ## Summary

PDM automatically loads project-local plugin paths from `.pdm-plugins` during `Core` initialization. Because this path is added via `site.addsitedir()`, attacker-controlled `.pth` files inside the project plugin directory are processed and can execute Python code before normal CLI handling begins.

This allows arbitrary code execution with the privileges of the user running `pdm` from …

---

## 20. 🟡 High Severity — free5GC UDR has improper `ueId` validation in EE subscription handlers that allows arbitrary identifier persistence

**CVE:** `CVE-2026-47780` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-6gxq-gpr8-xgjp>

> ### Summary
The free5GC UDR accepts arbitrary non-3GPP ueId values in the EE subscription creation and query flows because the regular expression used for validation ends with the catch-all alternative |.+. This causes the validation logic to accept any non-empty string rather than restricting input to expected SUPI/GPSI-style formats. In a tested deployment, a crafted value such as ARBITRARY_STRI…

---

## 21. 🟡 High Severity — nebula-mesh: Session and OIDC state cookies lack the Secure attribute

**CVE:** `CVE-2026-48058` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-rqfj-vv8r-xhqc>

> `internal/web/session.go` and `internal/web/oidc.go` set `HttpOnly` and `SameSite=Lax` on every cookie but never `Secure`. A single plaintext request to the origin (operator on a LAN, mistyped URL, HTTP→HTTPS not strictly enforced, reverse proxy misconfiguration) discloses the session.

## Affected
All released versions up to v0.3.1.

## Impact
An attacker who can observe one HTTP request to the o…

---

## 22. 🟡 High Severity — nebula-mesh: Decrypted CA private key persists in heap after signing

**CVE:** `CVE-2026-48025` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-8h84-fhqq-q58v>

> `internal/pki/resolver.go:36-64` constructs a `CAManager` with the plaintext `ed25519.PrivateKey` after unwrapping via the master key; `internal/pki/ca.go:13-16` stores it. Callers at `internal/api/enroll.go:116`, `internal/api/updates.go:297`, and `internal/api/mobile_bundle.go:40` use the manager for one `Sign()` and drop the reference on function return — but the underlying slice contents are n…

---

## 23. 🟡 High Severity — OpenTelemetry Operator for Kubernetes's ServiceMonitor bearerTokenFile reads arbitrary local file and sends contents as bearer auth

**CVE:** `CVE-2026-47701` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-cxh2-4639-vmc5>

> ## Affected

Repository: github.com/open-telemetry/opentelemetry-operator
Component: cmd/otel-allocator (TargetAllocator)
Companion: Prometheus Operator API types (CRDs)

## Summary

OpenTelemetry Operator&#x27;s TargetAllocator watches `ServiceMonitor` resources via the Prometheus Operator CR watcher and converts each selected endpoint into a Prometheus scrape configuration entry. The endpoint fi…

---

## 24. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
