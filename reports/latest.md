# Zero Day Pulse

> **Generated:** 2026-06-11 20:09 UTC &nbsp;|&nbsp; **Total:** 23 &nbsp;|&nbsp; 🔴 KEV: 1 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 10 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🔴 CISA KEV — CVE-2026-10520 — Ivanti Sentry OS Command Injection Vulnerability

**CVE:** `CVE-2026-10520` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-10520>

> Vendor: Ivanti | Product: Sentry. Ivanti Sentry (formerly known as MobileIron Sentry) contains an OS command injection vulnerability which could allow a remote unauthenticated user to achieve root-level remote code execution. This vulnerability can be successfully exploited in cases where the Sentry appliance is in an unmanaged state with its endpoints externally reachable. The use of mTLS with EP…

**Parallel AI Enrichment:**

- **Technical Details:** An OS command injection flaw in Ivanti Sentry allows a remote unauthenticated user to inject and execute arbitrary operating‑system commands, potentially gaining root privileges on the appliance.
- **Affected Products:** Ivanti Sentry before R10.5.2, R10.6.2, R10.7.1
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523?language=en_US)
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Apply the Ivanti Sentry updates released in the advisory and configure mTLS or restricted HTTPS access as recommended.
- **Vendor Advisory:** https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523?language=en_US

---

## 2. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path traversal vulnerability in the SimpleHelp web interface that allows unauthenticated attackers to read sensitive files on affected installations, leading to credential exposure and downstream compromise.
- **Affected Products:** SimpleHelp remote support/RMM software — versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (unspecified groups)
- **Mitigation:** Upgrade to patched SimpleHelp version; restrict/limit access to SimpleHelp management interfaces (network segmentation, firewall rules, IP allowlisting), monitor logs for abnormal access, apply least privilege, and perform incident response if compromise suspected
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 3. 🟠 Zero-Day — Oracle mitigates PeopleSoft zero-day exploited in data theft attacks

**CVE:** `CVE-2026-35273` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://www.bleepingcomputer.com/news/security/oracle-mitigates-peoplesoft-zero-day-exploited-in-data-theft-attacks/>

> Oracle is warning about a critical PeopleSoft Suite zero-day vulnerability tracked as CVE-2026-35273 that allows unauthenticated remote code execution, with the flaw actively exploited in ShinyHunter data theft attacks. [...]

**Parallel AI Enrichment:**

- **Technical Details:** An unauthenticated attacker with network access via HTTP can exploit a flaw in PeopleSoft Enterprise PeopleTools (Updates Environment Management) to achieve remote code execution and takeover of the PeopleSoft system.
- **Affected Products:** PeopleSoft Enterprise PeopleTools 8.61, 8.62
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** ShinyHunters
- **Mitigation:** Follow the Oracle Security Alert guidance: isolate PeopleSoft administrative interfaces, restrict network access to PeopleSoft HTTP endpoints, apply Oracle's provided fixes/patches, and monitor for indicators of compromise.
- **Vendor Advisory:** https://www.oracle.com/security-alerts/alert-cve-2026-35273.html

---

## 4. 🟠 Zero-Day — Criminal AI-as-a-Service in 2026: How the Underground Market Is Operationalizing Cybercrime

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://www.rapid7.com/blog/post/tr-criminal-ai-underground-market-operationalizing-cybercrime-2026>

> Introduction The underground market for criminally oriented generative AI has moved beyond the early hype surrounding &#x27;malicious chatbots.&#x27; The gradual integration of AI as a productivity layer within cybercrime operations has become the dominant story, indicating that while the potential for fully autonomous AI hacking systems is possible, attackers are not embracing them as expected. I…

**Parallel AI Enrichment:**

- **Technical Details:** The blog explains the mechanism as adversaries integrating generative AI to accelerate routine phases of attacks—automating phishing lure drafting, reconnaissance and profiling of targets, triaging and debugging malware/tooling, and improving social‑engineering content—thereby increasing scale and reducing required operator skill. This is an operational/abuse‑of‑capability issue rather than a software vulnerability.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Mitigations include: strengthen phishing defenses (multi‑factor authentication, email filtering, user training, phishing‑resistant MFA), implement robust identity and access management, monitor for scaled automation indicators (high‑volume, low‑effort content, rapid reconnaissance activity), apply least‑privilege and extensive logging, use anomaly detection on account and network behavior, and engage threat intelligence to track AI‑assisted tooling. Detection and monitoring controls are emphasized over a vendor patch.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when adversarial content is hosted in external corpora or web pages that LLM systems retrieve (via RAG or browsing) and that content contains malicious instructions which the model incorporates into its output or agent behavior. This includes natural-language prompts and payloads seeded on webpages or corpora that are later retrieved during model query processing.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Harden retrieval and agent workflows: validate and sanitize retrieved content; apply provenance, allow‑listing/block‑listing, instruction‑scrubbing, response filters and model grounding; restrict autonomous actions for agents; monitor for anomalous outputs; apply vendor advisories when available. Specific mitigations include not executing untrusted retrieved instructions, implementing strict instruction parsing and canonicalization, and using safety classifiers.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) allows an attacker to embed malicious instructions in data or web content that a large language model (LLM) consumes, influencing its output without any direct user input. Noma Labs demonstrated a zero‑click IPI exploit (GeminiJack) against Google Gemini Enterprise, showing that the attacker can affect LLM behavior solely through crafted content.
- **Affected Products:** Google Workspace with Gemini integrations
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability
- **Patch Available:** true — http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply vendor guidance: layered defenses including content filtering, provenance and trust signals, sanitization of external data, restricting agentic automation, least‑privilege access to tools, telemetry and anomaly detection.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** A zero‑click vulnerability (GeminiJack) that can be triggered via chained indirect prompt injection against Google Gemini Enterprise/agentic browsing in Chrome; indirect prompt injection allows malicious web content to influence agent prompts and actions, enabling unauthorized actions without user interaction.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Chrome layered defenses including restricting origin access, blocking prompt injections, and adding an overseer AI agent (per Google's architecting security post); follow vendor advice and update Chrome to receive these defenses.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Linear buffer overflow in CrabbyAVIF (unsafe Rust near‑miss) that was fixed pre‑release; Scudo hardened allocator rendered it non‑exploitable and turned the overflow into a crash.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Scudo hardened allocator provides protection via guard pages; improved crash reporting to detect overflows; training and unsafe‑Rust review practices to reduce recurrence.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection embeds hidden or crafted instructions in external content (emails, documents, calendar invites, web pages) that an AI agent ingests and treats as part of its prompt/context, leading to data exfiltration or unintended actions unless filtered or policy‑checked.
- **Affected Products:** Google Gemini Enterprise, Gemini in Workspace apps (Gemini for Chrome/agentic browsers), Vertex AI Search
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Deploy layered defenses: content provenance and origin restrictions, input sanitization and transformation, policy and instruction filtering, secondary supervisory agents/monitoring, restrict agent capabilities and origin access, robust evaluation and threat modeling, user confirmation for sensitive actions.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state‑sponsored actors target large backbone routers and provider/customer edge routers, leverage compromised devices and trusted connections to pivot, and modify routers to maintain persistent, long‑term access.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Implement network segmentation, monitor for unauthorized configuration changes on routers, restrict management access, apply vendor‑recommended hardening, and follow CISA/NSA guidance to counter compromise of networks worldwide.
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

## 14. 🟡 High Severity — Kolibri has Unauthenticated Server-Side Request Forgery (SSRF) in RemoteFacilityUserViewset

**CVE:** `CVE-2026-48053` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-4mj9-pf4r-cqrc>

> ## Summary

Several Kolibri API endpoints accept an unvalidated `baseurl` parameter and fetch attacker-controlled URLs from the Kolibri server, reflecting the response body back to the caller. The original report identified two endpoints on the `RemoteFacilityUser*` viewsets; remediation review found two further reflection points on the same pattern. The GET endpoint was unauthenticated.

## Affec…

---

## 15. 🟡 High Severity — Arc: Unauthenticated access to Go debug pprof endpoints leaks runtime state and enables CPU-burn DoS

**CVE:** `CVE-2026-48050` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-j93g-rp6m-j32m>

> ### Summary

Arc registers Go&#x27;s `net/http/pprof` handlers at `/debug/pprof/*` via `app.Use(pprof.New())` in `internal/api/server.go`, and `/debug/pprof` is added to `PublicPrefixes` in `cmd/arc/main.go`. The auth middleware short-circuits before the token check on prefix match, so the endpoints are reachable without any authentication.

### Impact

Any network-reachable caller (no token requi…

---

## 16. 🟡 High Severity — @hapi/inert has a static-file confinement bypass via sibling-prefix path

**CVE:** `CVE-2026-48049` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-rcvq-m9j9-6f4g>

> ### Impact
`@hapi/inert` serves static files from a directory configured with `path` (in the `directory` / `file` handlers) or `relativeTo` (for `h.file()`), with confinement enforced by the `confine` option (default `true`). Before the patch, the confinement check compared the resolved absolute path against the confine directory using a raw string-prefix test, so a sibling directory whose absolut…

---

## 17. 🟡 High Severity — python-zeroconf: Unbounded TC-deferred queue allows LAN-local memory exhaustion via spoofed-source flood

**CVE:** `CVE-2026-48045` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-9663-mqmp-p9mm>

> ### Impact

`AsyncListener.handle_query_or_defer` retained every truncated (TC-bit) incoming query in `self._deferred[addr]` and armed a per-addr timer in `self._timers[addr]` that flushed the reassembled query within ~500 ms (RFC 6762 §18.5). Neither the per-addr list nor the number of distinct `addr` keys was capped, and the dedup check (`for incoming in reversed(deferred): if incoming.data == m…

---

## 18. 🟡 High Severity — Meta Ads MCP: Unauthenticated HTTP MCP Tool Execution Leaks Operator Meta Access Token

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

## 19. 🟡 High Severity — @hapi/wreck: Sensitive credential headers leak across cross-port and cross-scheme redirects

**CVE:** `CVE-2026-48022` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-x426-x7cc-3fpc>

> ### Impact
Wreck strips credential headers (Authorization, Cookie, Proxy-Authorization) before following a cross-origin redirect, but the origin check compares hostnames only and ignores scheme and port. As a result, credentials are forwarded intact across same-host port changes and HTTPS-to-HTTP downgrades, allowing a co-tenant on an adjacent port or a network-position attacker capable of forging…

---

## 20. 🟡 High Severity — Netty's Lack of Lifecycle Cleanup Leads to Pooled ByteBuf Leak in RedisArrayAggregator

**CVE:** `CVE-2026-48006` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-6jv9-x5w9-2ccm>

> ### Impact
The RedisArrayAggregator handler permanently leaks pooled direct-memory buffers when a Redis pipeline connection closes before a RESP array aggregate completes. The handler retains child messages in per-handler state (`depths` field) but defines no `channelInactive`, `handlerRemoved`, or `exceptionCaught` method to release them when the pipeline tears down. Because the leaked buffers ar…

---

## 21. 🟡 High Severity — PDM: Project-Controlled `.pdm-plugins` Content Executes Before CLI Parsing

**CVE:** `CVE-2026-47781` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-qq6c-99pv-prvf>

> ## Summary

PDM automatically loads project-local plugin paths from `.pdm-plugins` during `Core` initialization. Because this path is added via `site.addsitedir()`, attacker-controlled `.pth` files inside the project plugin directory are processed and can execute Python code before normal CLI handling begins.

This allows arbitrary code execution with the privileges of the user running `pdm` from …

---

## 22. 🟡 High Severity — free5GC UDR has improper `ueId` validation in EE subscription handlers that allows arbitrary identifier persistence

**CVE:** `CVE-2026-47780` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-6gxq-gpr8-xgjp>

> ### Summary
The free5GC UDR accepts arbitrary non-3GPP ueId values in the EE subscription creation and query flows because the regular expression used for validation ends with the catch-all alternative |.+. This causes the validation logic to accept any non-empty string rather than restricting input to expected SUPI/GPSI-style formats. In a tested deployment, a crafted value such as ARBITRARY_STRI…

---

## 23. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
