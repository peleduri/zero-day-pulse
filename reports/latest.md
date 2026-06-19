# Zero Day Pulse

> **Generated:** 2026-06-19 02:48 UTC &nbsp;|&nbsp; **Total:** 31 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 17 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal vulnerability enabling unauthenticated remote attackers to read arbitrary files (e.g., /etc/passwd, private SSH keys) on SimpleHelp servers.
- **Affected Products:** SimpleHelp remote support software versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC available; see OffSec blog with Metasploit auxiliary scanner details.
- **Patch Available:** Patch available: https://simple-help.com/kb---security-vulnerabilities-01-2025
- **Active Exploitation:** Confirmed active exploitation: CISA lists the vulnerability in its KEV catalog and cites ransomware actors exploiting unpatched SimpleHelp deployments.
- **Threat Actors:** Ransomware actors (unspecified groups) exploiting SimpleHelp
- **Mitigation:** If a patch cannot be applied immediately, isolate the SimpleHelp server instance from the internet or stop the server process, and upgrade to the latest version as soon as possible.
- **Vendor Advisory:** https://simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — AgenticMail: Unauthenticated inbound mail triggers bypassPermissions resume of the operator's Claude Code session (bridge-wake)

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-fq4x-789w-jg5h>

> ## Summary
Two inbound-mail handlers act on a privileged effect without verifying that the sender is the operator, while a sibling handler in the same repo does. The higher-impact one: any external email routed to the bridge inbox causes the dispatcher to resume the operator&#x27;s Claude Code session with `permissionMode: &#x27;bypassPermissions&#x27;`, embedding the attacker-controlled `from`/`s…

**Parallel AI Enrichment:**

- **Technical Details:** Two inbound‑mail handlers act on a privileged effect without verifying the sender is the operator. An external email routed to the bridge inbox causes the dispatcher to resume the operator's Claude Code session with permissionMode: 'bypassPermissions', embedding attacker‑controlled from/subject/preview into the resumed agent's prompt, resulting in an indirect prompt injection into a fully‑privileged agent (Bash/Write/Edit/WebFetch + the agenticmail MCP toolbelt).
- **Affected Products:** @agenticmail/agenticmail (AgenticMail)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit reported.
- **Patch Available:** Patch status not specified in the advisory.
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Harden inbound‑mail handlers to verify the sender/operator identity before resuming a session, avoid using bypassPermissions with untrusted input, restrict external email routing to trusted senders, and disable automatic bridge‑wake resume if a patch is unavailable.
- **Vendor Advisory:** https://github.com/advisories/GHSA-fq4x-789w-jg5h

---

## 3. 🟠 Zero-Day — Grav: Stored CSS injection via Markdown image ?style=… reaches MediaObjectTrait::style() — incomplete patch of GHSA-r7fx-8g49-7hhr

**CVE:** `CVE-2026-55890` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-pmf8-g7c8-7v54>

> ## Summary

The fix for **GHSA-r7fx-8g49-7hhr / CVE-2026-42841** (Stored XSS via Markdown media `attribute()` action) is incomplete. The maintainer patched `MediaObjectTrait::attribute()` to deny dangerous attribute names (event handlers, `style`, `xmlns`, `srcdoc`, `formaction`) but the sibling `MediaObjectTrait::style()` method is reachable through the **same Markdown excerpt-action pipeline** a…

**Parallel AI Enrichment:**

- **Technical Details:** A stored CSS injection vulnerability exists where Grav's Markdown image processing pipeline reaches MediaObjectTrait::style(), which writes editor‑controlled strings directly into an <img style="…"> attribute without sanitization. An authenticated user with admin.pages permission can save Markdown containing a ?style=… parameter in the image URL, leading to CSS injection or XSS depending on browser behavior.
- **Affected Products:** getgrav/grav (Grav CMS) — affected Markdown image handling via MediaObjectTrait::style(); specific vulnerable versions unavailable.
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit located.
- **Patch Available:** No official vendor patch specifically for CVE-2026-55890 was located; recommend updating Grav to newer releases when available.
- **Active Exploitation:** No reports of confirmed active exploitation located.
- **Threat Actors:** None known
- **Mitigation:** Restrict who can edit/save Markdown (limit admin.pages permission to trusted users); avoid allowing user‑supplied ?style=… parameters in image URLs and strip inline style attributes via output filtering or WAF rules; upgrade to a vendor‑provided fix when released.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — PraisonAI: Server-Side Request Forgery (SSRF) in SearxNG / search_web tools via attacker-controlled searxng_url parameter

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-4pcv-mg8v-vrgf>

> ### Summary
A Server-Side Request Forgery (SSRF) vulnerability in the SearxNG / `search_web` search tools allows an attacker to make the server perform requests to arbitrary internal endpoints and read the responses back. The `searxng_url` argument is passed directly to `requests.get()` with no validation of scheme, host, or port. Because `searxng_url` is exposed to the LLM as a tool parameter and…

**Parallel AI Enrichment:**

- **Technical Details:** Server-Side Request Forgery (CWE-918) in PraisonAI's SearxNG/search_web tools. The `searxng_url` argument is passed unvalidated directly to `requests.get()`. Because the parameter is exposed to the LLM and search_web/searxng_search is part of the default agent toolset, prompt injection in ingested content (web pages, files, prior tool output) can coerce the agent to issue requests to attacker-chosen URLs. The server fetches those URLs and returns response bodies into the agent context, enabling internal-service access, host/port enumeration, and cloud instance metadata reach (169.254.169.254) with potential IAM credential exposure.
- **Affected Products:** PraisonAI praisonaiagents Python package, versions < 1.6.61
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:L/A:L
- **Exploit Available:** No public PoC or weaponized exploit identified for GHSA-4pcv-mg8v-vrgf at this time. The attack is reproducible from the advisory description (attacker-controlled `searxng_url` passed to `requests.get()`).
- **Patch Available:** Yes. Fixed in PraisonAI `praisonaiagents` version 1.6.61. Advisory URL: https://github.com/advisories/GHSA-4pcv-mg8v-vrgf (also indexed at https://github.com/MervinPraison/PraisonAI/security/advisories/GHSA-4pcv-mg8v-vrgf).
- **Active Exploitation:** No confirmed in-the-wild exploitation specific to GHSA-4pcv-mg8v-vrgf has been publicly reported as of 2026-06-19. PraisonAI vulnerabilities overall have shown rapid post-disclosure scanning per Sysdig/SecurityWeek/Kiteworks/The Hacker News.
- **Threat Actors:** None known
- **Mitigation:** Upgrade `praisonaiagents` to version 1.6.61 or later. Defense-in-depth: allow-list valid `searxng_url` scheme/host/port (HTTPS only, block private RFC1918/link-local/loopback including 169.254.169.254); re-resolve and re-validate the host after DNS lookup to defeat DNS rebinding; disable `search_web` / `searxng_search` from the default agent toolset when not needed; apply egress network policy / firewall so the agent host cannot reach internal IP space; treat all ingested web/file/tool content as untrusted to defeat the prompt-injection trigger; avoid logging or surfacing raw arbitrary-URL response bodies into the model context.
- **Vendor Advisory:** https://github.com/advisories/GHSA-4pcv-mg8v-vrgf

---

## 5. 🟠 Zero-Day — PraisonAI: Webhook signature verification skipped (fail-open) when secret unset, allowing forged inbound webhooks (WhatsApp & Linear bots)

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-x92v-rpx6-p6cw>

> The WhatsApp and Linear bot adapters verify the inbound webhook HMAC signature only
when a secret is configured. When the secret environment variable is unset — the
default on a fresh install and common in development — verification is skipped entirely
and the webhook body is parsed and dispatched as a genuine, trusted event. A remote,
unauthenticated attacker who can reach the bot&#x27;s webhook …

**Parallel AI Enrichment:**

- **Technical Details:** The WhatsApp and Linear bot adapters verify inbound webhook HMAC signatures only when a secret is set. If the secret environment variable is unset (default on fresh installs and common in development), verification is skipped, the webhook body is parsed as trusted, and an unauthenticated attacker can inject arbitrary platform events.
- **Affected Products:** PraisonAI bots — WhatsApp bot adapter, Linear bot adapter
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC or weaponized exploit located
- **Patch Available:** https://github.com/advisories/GHSA-x92v-rpx6-p6cw
- **Active Exploitation:** No confirmed active exploitation reported
- **Threat Actors:** None known
- **Mitigation:** Ensure a webhook secret is configured in deployment (set the environment variable, e.g. WHATSAPP_APP_SECRET), restrict webhook endpoints via network controls (IP allowlists, firewall), require authentication at the reverse proxy, and validate incoming webhooks by enabling HMAC signature checking. Patch to verify signatures even when secret unset or fail‑closed.
- **Vendor Advisory:** https://github.com/advisories/GHSA-x92v-rpx6-p6cw

---

## 6. 🟠 Zero-Day — PraisonAI: Jobs webhook SSRF protection bypass via DNS rebinding

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-rjvw-7vvw-549v>

> # Jobs webhook SSRF protection bypass via DNS rebinding

## Summary

PraisonAI&#x27;s Async Jobs API validates `webhook_url` when a job request is parsed
and again when the internal `Job` object is constructed. That validation blocks
direct loopback/private targets, but it is not bound to the later network
request. When a job completes, `_send_webhook()` passes the original hostname to
`httpx.Asyn…

**Parallel AI Enrichment:**

- **Technical Details:** The Async Jobs API accepts an attacker-controlled webhook_url which is validated during request parsing (blocking direct loopback/private IPs), but the code later calls httpx.AsyncClient.post() using the original hostname with no send-time validation, IP pinning, or guarded transport. An attacker-controlled hostname can resolve to a public IP during validation and later resolve (via DNS rebinding) to loopback/private addresses at send time, enabling SSRF to internal services.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit identified in public advisories or writeups.
- **Patch Available:** No official vendor patch announced in the GitHub advisory; no vendor advisory URL provided.
- **Active Exploitation:** No confirmed public reports of active exploitation in the wild found.
- **Threat Actors:** None known
- **Mitigation:** As a workaround, perform send-time validation and IP pinning: resolve the hostname at request time and at send time, compare IP(s), and block loopback/private ranges; use a guarded transport that prevents requests to internal addresses; restrict webhook_url to allowlist domains or require outbound webhook delivery via a proxy that enforces egress rules.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 7. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when AI systems ingest attacker‑controlled content on the web (hidden HTML comments, display:none elements, spoofed system tags, metadata namespaces, accessibility‑hidden text). Attack chain: poison web content → conceal payload from humans → AI ingests content → AI follows attacker instructions → potential actions include data exfiltration, navigation, payments, command execution.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit URL reported.
- **Patch Available:** Vendor advisory URL unavailable.
- **Active Exploitation:** Confirmed active exploitation has been observed: Google reported a 32% increase in malicious IPI probes (Nov 2025–Feb 2026) and Forcepoint published ten real‑world IPI payload incidents on active sites.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses – input/output validation and sanitization, human oversight, content‑context checks, concealment detection (hidden DOM/CSS/comment detection), provenance/metadata validation; see Google blog mitigations and Google Workspace continuous approach link.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 8. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when malicious instructions are embedded in content retrieved by a RAG pipeline (e.g., Docs, Calendar, Email). The poisoned content is added to the model’s context, causing the LLM to treat the instruction as legitimate and execute it, such as exfiltrating data via crafted external URLs or images. This flow was demonstrated in the GeminiJack attack.
- **Affected Products:** Google Workspace (Gemini Enterprise / Gemini in Workspace) – affected RAG‑enabled Workspace with Gemini integrations.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Proof‑of‑concept and technical write‑up published by Noma Labs describing GeminiJack attack flow.
- **Patch Available:** No separate downloadable patch has been released; mitigations are implemented by Google as described in the advisory.
- **Active Exploitation:** Confirmed research disclosure and a reported zero‑click exploit ("GeminiJack") by Noma Labs demonstrating real‑world exfiltration.
- **Threat Actors:** None known
- **Mitigation:** Google’s layered defenses: prompt‑injection content classifiers; security thought reinforcement; markdown sanitization and suspicious URL redaction; user confirmation framework; end‑user security mitigation notifications; deterministic policy engine for rapid config fixes; ML/LLM hardening and retraining.
- **Vendor Advisory:** https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini

---

## 9. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection in Gemini Enterprise enables an attacker to inject malicious instructions that the AI agent will execute, potentially leading to unauthorized actions or data exfiltration.
- **Affected Products:** Google Chrome (latest version as of December 2025)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept or weaponized exploit has been released.
- **Patch Available:** No official patch has been released yet.
- **Active Exploitation:** No confirmed active exploitation has been reported.
- **Threat Actors:** None known
- **Mitigation:** Enable Chrome’s new security layers that block indirect prompt injection, restrict origin access for AI agents, and keep Chrome updated to the latest version.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 10. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** CWE-125 (Out-of-bounds Read) in CrabbyAVIF, Android's AVIF parser/decoder written in unsafe Rust. Incorrect bounds checking produced out-of-bounds accesses across multiple NV12 YUV processing paths—including the Y plane, UV planes, alpha plane, chroma-width calculation, plane-size calculation, and per-row byte calculations (linear buffer overflow). Exploitation requires no user interaction and no additional execution privileges, and could enable remote code execution when chained with other bugs.
- **Affected Products:** Android System (AOSP) — Android 16, security patch level prior to 2025-08-01; specifically the CrabbyAVIF AV1 Image File Format (AVIF) parser/decoder component (platform/external/rust/crabbyavif). No publicly released Android build shipped the vulnerable code.
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** No public proof-of-concept (PoC) or weaponized exploit exists for CVE-2025-48530. Although security researchers publicly analyzed the OOB access code paths (see https://x.com/xvonfers/status/1952499317702344798), no functional exploit PoC has been published. The vulnerable code never reached a public Android release, eliminating a production target.
- **Patch Available:** Yes — patched in the Android Security Bulletin—August 2025 at security patch level 2025-08-01. Patch commits: https://android.googlesource.com/platform/external/rust/crabbyavif/+/9bcc1a311114ab844b417d3cdec50dcedfd0603f and https://android.googlesource.com/platform/external/rust/crabbyavif/+/42feb427a42afd9eebe6391a0d8a7b083fe82140. Advisory: https://source.android.com/docs/security/bulletin/2025-08-01
- **Active Exploitation:** No active exploitation reported. The vulnerable code was discovered internally by Google and remediated before being included in any publicly released Android build, leaving no production attack surface. No bulletin (Android, NVD, INCIBE-CERT), cybersecurity news outlet (CyberScoop, Malwarebytes, The Hacker News), or threat-intelligence source links any exploitation or threat actor to CVE-2025-48530.
- **Threat Actors:** None known
- **Mitigation:** No end-user remediation required: the vulnerable code never shipped in a public Android build. Defense-in-depth: keep devices on Android security patch level 2025-08-05 or later. Codebase-level hardening recommended by Google: (1) Mandate the Scudo hardened allocator (guard pages turn silent corruption into crashes), (2) encapsulate `unsafe` Rust blocks inside safe abstractions with documented safety preconditions, and (3) require Comprehensive Rust training for engineers writing unsafe code.
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

## 14. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

---

## 15. 🟡 High Severity — Signal K Server: Server-Side Request Forgery via Remote Connection Endpoints

**CVE:** `CVE-2026-55591` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-q59x-jc9f-gfqf>

> ### Summary
signalk-server versions up to and including 2.27.0 contain a Server-Side Request Forgery (SSRF) vulnerability in three administrative endpoints used for remote Signal K server connection management. The `makeRemoteRequest()` function accepts attacker-controlled `host`, `port`, `useTLS`, and `selfsignedcert` parameters without any validation, allowing an attacker to force the server to …

---

## 16. 🟡 High Severity — gemini-mcp-tool vulnerable to OS command injection and @file exfiltration via prompt quoting (CVE-2026-0755)

**CVE:** `CVE-2026-0755` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-4h5r-5jm8-jxjm>

> Untrusted prompt input could reach the Gemini CLI @file parser, allowing read/exfiltration of arbitrary local files (@/etc/passwd, @~/.ssh/id_rsa, @../../secret). On Windows, unquoted cmd.exe metacharacters could break out into OS command injection.

Fix (1.1.6): removed the broken shell:false double-quote wrapping; added assertSafeFileReferences() to contain @file refs to the working directory; h…

---

## 17. 🟡 High Severity — OpenClaw: Internal/webchat command auth could inherit ownerAllowFrom wildcard state

**CVE:** `CVE-2026-53854` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-4hpg-mp64-x7xq>

> ### Summary

Internal/webchat command auth could inherit ownerAllowFrom wildcard state. In affected versions, a sender on an affected internal or webchat path could inherit wildcard ownerAllowFrom state across channel boundaries.

This advisory is scoped to the named feature and configuration. It does not change OpenClaw&#x27;s trusted-operator model: authenticated Gateway operators, installed plu…

---

## 18. 🟡 High Severity — F5 Patches Two Critical NGINX Open Source Flaws Enabling Remote Code Execution

**CVE:** `CVE-2026-42530` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://thehackernews.com/2026/06/f5-patches-two-critical-nginx-open.html>

> F5 has released security updates to address two critical security flaws in NGINX Open Source that could be exploited to achieve code execution on affected systems.

The vulnerabilities are listed below -


  CVE-2026-42530 (CVSS v4 score: 9.2) - A use-after-free vulnerability in the ngx_http_v3_module that could be triggered by a remote unauthenticated attacker when NGINX Open Source is

---

## 19. 🟡 High Severity — Armeria: External Control of File Name or Path in xDS SDS DataSource

**CVE:** `CVE-2026-11752` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-hgw6-8c77-v4gq>

> ## External Control of File Name or Path in xDS SDS DataSource

### Summary

`DataSourceStream` in the `:xds` module resolves control-plane-supplied `filename` and `environment_variable` fields from SDS Secret resources without any allow-list or base-directory confinement. A semi-trusted or compromised xDS control plane (or an attacker who can MITM SDS responses) can read arbitrary local files and…

---

## 20. 🟡 High Severity — Daytona: Path traversal in sandbox volume id mounts arbitrary host paths into the sandbox — cross-tenant data access and host escape

**CVE:** `CVE-2026-54319` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-fjv8-j4p5-cr9m>

> ## Summary
A sandbox volume reference (`volumeId`, which may also be a volume name) was forwarded to the
runner and used to build the host bind-mount source path without confinement. A reference
containing path-traversal sequences could in principle resolve the mount source outside the
intended per-volume base directory.

## Impact
Had the traversal been reachable, an authenticated user could have…

---

## 21. 🟡 High Severity — tract-nnef: integer overflow in NNEF `.dat` tensor parser yields an out-of-bounds read on model load

**CVE:** `CVE-2026-55093` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-x5mv-8wgw-29hg>

> - **Component:** `tract-nnef` (`nnef/src/tensors.rs::read_tensor`) + `tract-data` (`data/src/tensor.rs`)
- **Affected versions:** `&lt; 0.21.16`, `0.22.0`–`0.22.2`, `0.23.0`–`0.23.1` — the dense `DatLoader` path was unguarded across all three release lines; patched in 0.21.16 / 0.22.2 / 0.23.1
- **Class:** CWE-190 (integer overflow) → CWE-125 (out-of-bounds read)
- **Trigger:** loading a crafted N…

---

## 22. 🟡 High Severity — opentelemetry-collector-contrib: githubreceiver silently ignores configured required_headers authentication

**CVE:** `CVE-2026-55701` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-w5cv-pw74-4rxc>

> ## githubreceiver Silently Ignores Configured required_headers Authentication

### Summary

The githubreceiver webhook handler does not enforce the `required_headers` configuration. Headers are validated at startup (config rejects empty keys/values) but never checked on incoming requests. This follows the same pattern as [GHSA-prf6-xjxh-p698](https://github.com/open-telemetry/opentelemetry-collect…

---

## 23. 🟡 High Severity — Kirby: External Initialization of the Panel on reverse proxy setups with the `Forwarded` header

**CVE:** `CVE-2026-54003` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-whxw-24jc-cwmv>

> ### TL;DR

This vulnerability affects Kirby sites that have no configured user accounts and are running on publicly accessible servers behind a reverse proxy that sets the `Forwarded: for=...`, `X-Client-IP`, or `X-Real-IP` request header.

It was possible to install the Panel (= create the first admin user) in these setups even from remote IP addresses.

**This vulnerability is of critical severi…

---

## 24. 🟡 High Severity — Kirby: Cross-site scripting (XSS) from incomplete HTML/XML sanitization in `Dom::sanitize()`

**CVE:** `CVE-2026-54002` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-wr9h-4r83-f4v6>

> ### TL;DR

This vulnerability affects Kirby sites and plugins that use the `writer` or `list` fields or that use `$dom-&gt;sanitize()`, `Sane::sanitize()`, `Sane\Html::sanitize()`, `Sane\Svg::sanitize()`, `Sane\Xml::sanitize()`,  `Sane::sanitizeFile()` or `$file-&gt;sanitizeContents()` with untrusted input.

It was possible to inject malicious markup as children of an unknown HTML/XML tag, which w…

---

## 25. 🟡 High Severity — Kirby: Self cross-site scripting (self-XSS) in the writer field

**CVE:** `CVE-2026-49276` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-rhj6-r49h-5932>

> ### TL;DR

This vulnerability affects Kirby sites that use the writer field in any blueprint.

It was possible to include a scripting link as the target of a link (or email link). This link target would then be clickable by the user who entered it.

A successful attack commonly requires knowledge of the content structure by the attacker as well as social engineering of a user with access to the Pa…

---

## 26. 🟡 High Severity — Jupyter Server: Stored XSS in `NbconvertFileHandler` / `NbconvertPostHandler` via missing `sandbox` CSP 

**CVE:** `CVE-2026-44727` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-fcw5-x6j4-ccmp>

> The nbconvert HTTP handlers in jupyter_server render user-authored notebook HTML under the Jupyter origin without a sandbox directive in their `Content-Security-Policy`. 

Combined with `nbconvert.HTMLExporter`&#x27;s default non-sanitizing behavior, a notebook carrying an HTML payload in a display_data output triggers stored XSS with cookie access, full /api/* authority, and kernel RCE.

### Impa…

---

## 27. 🟡 High Severity — BBOT: Server-Side Request Forgery (SSRF) in docker_pull module via WWW-Authenticate realm parsing

**CVE:** `CVE-2026-12566` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-3mp7-vp6j-2mxx>

> The `docker_pull` module uses the `realm` parameter from a Docker registry&#x27;s `WWW-Authenticate` response header as the authentication endpoint without validation. An attacker in a man-in-the-middle position between bbot and a Docker registry could modify this header to redirect the authentication request to an arbitrary endpoint, potentially leaking authentication tokens.

---

## 28. 🟡 High Severity — praisonai-platform: Authorization Bypass Through User-Controlled Key

**CVE:** `CVE-2026-47415` | `CVE-2026-47418` | `CVE-2026-47419` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-2fjj-qqg8-fg7x>

> ## Summary

The issue create and update endpoints in `praisonai-platform` accept a `project_id` in the request body and persist it without validating that the project belongs to the URL workspace. A user who is a member of workspace `W_B` (and has no access to workspace `W_A`) can create issues that reference a project owned by `W_A`. Because `ProjectService.get_stats()` aggregates issues by `proj…

---

## 29. 🟡 High Severity — Grav: Admin Backup Zip File Exposes Account Credentials and Configuration Secrets

**CVE:** `CVE-2026-55885` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-2f86-9cp8-6hcf>

> ### Summary
An authenticated administrator with backup permissions can download a ZIP archive containing the full Grav installation root, including `user/accounts/admin.yaml` with the admin&#x27;s bcrypt password hash and email, plus `user/config/` with all site configuration. The download endpoint requires only the session-static `admin-nonce` in the URL, no additional form-level CSRF token, and …

---

## 30. 🟡 High Severity — Oracle June 2026 Critical Security Patch Update Addresses 243 CVEs (CVE-2026-35273)

**CVE:** `CVE-2026-35273` &nbsp;|&nbsp; **Source:** Tenable Security Research &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://www.tenable.com/blog/oracle-june-2026-critical-security-patch-update-addresses-243-cves-cve-2026-35273>

> Oracle addresses 243 CVEs in its June 2026 Critical Security Patch Update with 245 patches, including 122 critical updates. Key Takeaways The June 2026 Critical Security Patch Update (CSPU) contains fixes for 243 unique CVEs in 245 security updates 122 issues (49.8% of all patches) were assigned a critical severity rating Oracle Fusion Middleware received the highest number of patches at 106, acco…

---

## 31. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
