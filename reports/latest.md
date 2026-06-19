# Zero Day Pulse

> **Generated:** 2026-06-19 10:11 UTC &nbsp;|&nbsp; **Total:** 31 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 17 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE‑2024‑57727 is an unauthenticated directory‑traversal vulnerability in SimpleHelp RMM that permits remote attackers to read arbitrary files on the server by sending crafted requests containing path‑traversal sequences.
- **Affected Products:** SimpleHelp Remote Support / Remote Monitoring and Management (RMM) version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof‑of‑concept is available in the OffSec blog analysis.
- **Patch Available:** A patch is available; SimpleHelp version 5.5.8 resolves the vulnerability. See the vendor advisory for details.
- **Active Exploitation:** Confirmed active exploitation reported by CISA.
- **Threat Actors:** Ransomware actors (unspecified groups)
- **Mitigation:** Upgrade to SimpleHelp version 5.5.8 or later, isolate SimpleHelp services from the internet, restrict access with firewalls or VPN, rotate credentials and secrets, and perform threat hunting for indicators of compromise.
- **Vendor Advisory:** https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — AgenticMail: Unauthenticated inbound mail triggers bypassPermissions resume of the operator's Claude Code session (bridge-wake)

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-fq4x-789w-jg5h>

> ## Summary
Two inbound-mail handlers act on a privileged effect without verifying that the sender is the operator, while a sibling handler in the same repo does. The higher-impact one: any external email routed to the bridge inbox causes the dispatcher to resume the operator&#x27;s Claude Code session with `permissionMode: &#x27;bypassPermissions&#x27;`, embedding the attacker-controlled `from`/`s…

**Parallel AI Enrichment:**

- **Technical Details:** Two inbound‑mail handlers act on a privileged effect without verifying that the sender is the operator. Any external email routed to the bridge inbox causes the dispatcher to resume the operator's Claude Code session with `permissionMode: 'bypassPermissions'`, embedding attacker‑controlled `from`/`subject`/`preview` into the prompt, resulting in an indirect prompt injection into a fully‑privileged agent running as the operator's OAuth identity.
- **Affected Products:** AgenticMail packages (claudecode, core)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC or weaponized exploit located.
- **Patch Available:** Patch/advisory published on GitHub Security Advisories (https://github.com/advisories/GHSA-fq4x-789w-jg5h).
- **Active Exploitation:** No public reports of active exploitation in the wild.
- **Threat Actors:** None known
- **Mitigation:** Remove or restrict bridge inbox routing from untrusted mail; verify sender identity before acting on inbound mail; disable automatic resume with bypassPermissions; apply vendor‑provided patch or update to patched package versions. If no patch is available, disable the affected inbound‑mail handlers or run the agent with least privilege without permissionMode bypass.
- **Vendor Advisory:** https://github.com/advisories/GHSA-fq4x-789w-jg5h

---

## 3. 🟠 Zero-Day — Grav: Stored CSS injection via Markdown image ?style=… reaches MediaObjectTrait::style() — incomplete patch of GHSA-r7fx-8g49-7hhr

**CVE:** `CVE-2026-55890` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-pmf8-g7c8-7v54>

> ## Summary

The fix for **GHSA-r7fx-8g49-7hhr / CVE-2026-42841** (Stored XSS via Markdown media `attribute()` action) is incomplete. The maintainer patched `MediaObjectTrait::attribute()` to deny dangerous attribute names (event handlers, `style`, `xmlns`, `srcdoc`, `formaction`) but the sibling `MediaObjectTrait::style()` method is reachable through the **same Markdown excerpt-action pipeline** a…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is a stored CSS injection via the MediaObjectTrait::style() method, which writes attacker‑controlled strings directly into the <img style> attribute without sanitization, reachable through the Markdown image action pipeline.
- **Affected Products:** Grav CMS 2.0 line (all currently‑shipping versions)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept known.
- **Patch Available:** No official vendor patch fully addressing this vulnerability has been released.
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://github.com/advisories/GHSA-pmf8-g7c8-7v54

---

## 4. 🟠 Zero-Day — PraisonAI: Server-Side Request Forgery (SSRF) in SearxNG / search_web tools via attacker-controlled searxng_url parameter

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-4pcv-mg8v-vrgf>

> ### Summary
A Server-Side Request Forgery (SSRF) vulnerability in the SearxNG / `search_web` search tools allows an attacker to make the server perform requests to arbitrary internal endpoints and read the responses back. The `searxng_url` argument is passed directly to `requests.get()` with no validation of scheme, host, or port. Because `searxng_url` is exposed to the LLM as a tool parameter and…

**Parallel AI Enrichment:**

- **Technical Details:** The searxng_url parameter is passed directly into requests.get() without validation of scheme, host, or port in searxng_tools.py and web_search.py. Because searxng_url is exposed as a tool parameter to the LLM and search_web is part of default agent tools, attackers can supply an arbitrary internal URL via prompt injection; the server will fetch it and return the response, enabling internal service/API disclosure, host/port probing, and cloud metadata access.
- **Affected Products:** praisonaiagents (< 1.6.61)
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:L/A:L
- **Exploit Available:** Proof-of-concept (PoC) included in the GitHub advisory demonstrating arbitrary internal requests; URL: https://github.com/advisories/GHSA-4pcv-mg8v-vrgf
- **Patch Available:** Patched in praisonaiagents release 1.6.61 (see advisory: https://github.com/advisories/GHSA-4pcv-mg8v-vrgf)
- **Active Exploitation:** No confirmed active exploitation reported in the advisory; none known.
- **Threat Actors:** None known
- **Mitigation:** Disable or remove the default search_web/searxng_search tools in agent deployments that ingest untrusted content; restrict tool parameters so searxng_url cannot be model-controlled; configure network egress controls to block access to internal IP ranges (169.254.169.254 and RFC1918 addresses) from agents; run agents with least-privilege network policies and avoid exposing instance metadata endpoints.
- **Vendor Advisory:** Vendor advisory URL unavailable.

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

- **Technical Details:** The WhatsApp and Linear bot adapters only verify inbound webhook HMAC signatures when a secret is configured. If the secret environment variable is unset (the default on fresh installs/development), verification is skipped (fail‑open) and inbound webhook bodies are parsed and treated as genuine events. An unauthenticated attacker who can reach the webhook endpoint can inject forged platform events.
- **Affected Products:** PraisonAI (WhatsApp and Linear bot adapters)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public exploit available
- **Patch Available:** Patch unavailable
- **Active Exploitation:** No active exploitation reported
- **Threat Actors:** None known
- **Mitigation:** Configure and set the webhook secrets (environment variables) for WhatsApp and Linear bots; restrict network access to webhook endpoints (IP allowlist, VPN), add reverse‑proxy authentication, and remove public exposure in development. Monitor incoming webhook sources and rotate secrets after any suspected misuse. If a vendor patch is released, apply it promptly.
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

- **Technical Details:** The Async Jobs API validates the webhook URL during parsing, blocking direct private targets. However, when the job completes, the original hostname is sent via httpx.AsyncClient.post() without additional validation, IP pinning, or transport safeguards. An attacker can exploit DNS rebinding to have the hostname resolve to a public IP during validation and later resolve to a loopback or internal IP during the request, achieving SSRF.
- **Affected Products:** PraisonAI Async Jobs API (all versions)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** A proof‑of‑concept exploit is described in the advisory (see citation).
- **Patch Available:** No official patch has been released for this vulnerability.
- **Active Exploitation:** No confirmed active exploitation has been reported.
- **Threat Actors:** None known
- **Mitigation:** Implement validation of the webhook URL at the time of the outbound request, enforce IP pinning or restrict allowed destinations to a whitelist, and avoid relying solely on hostname validation during parsing.
- **Vendor Advisory:** https://github.com/advisories/GHSA-rjvw-7vvw-549v

---

## 7. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) — attackers hide instructions inside web content (HTML comments, hidden divs, CSS concealment, meta namespaces, accessibility-hidden text) so AI systems that retrieve and process that content treat attacker‑controlled instructions as authoritative, enabling actions like API‑key exfiltration, unauthorized transactions, data destruction, navigation to admin endpoints, or output hijacking.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof‑of‑concept payloads have been observed; see Forcepoint blog for details.
- **Patch Available:** Patch not applicable; vendor mitigations and hardening guidance provided at vendor advisory.
- **Active Exploitation:** Yes — Forcepoint X‑Labs reported 10 verified in‑the‑wild IPI payloads and Google telemetry observed a 32% rise in malicious detections between Nov 2025 and Feb 2026.
- **Threat Actors:** None known
- **Mitigation:** Harden RAG/data‑retrieval boundaries, sanitize and treat retrieved content as untrusted (do not treat user‑content as system instructions), apply content filtering/detection for concealment patterns, layered defenses (as described in Google Workspace mitigations), monitor telemetry and block IPI URLs at network/agent stage.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 8. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) injects malicious instructions into external data sources or tools that LLMs ingest (e.g., web pages, documents, comments, or connectors). Attackers weaponize hidden web content or injected data to influence model behavior without direct user input; RAG (retrieval‑augmented generation) and agentic systems are particularly susceptible.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit reported in the Google advisory; exploit availability: none reported.
- **Patch Available:** No vendor 'patch' applicable; Google published mitigations and continuous‑evaluation approach at the advisory URL above.
- **Active Exploitation:** Some indirect prompt injection payloads have been observed in the wild (Forcepoint’s April 2026 report), and zero‑click IPI variants like 'GeminiJack' were disclosed by Noma Labs; however the Google advisory does not report specific confirmed targeted exploitation campaigns against Workspace users.
- **Threat Actors:** None known
- **Mitigation:** Google’s recommended mitigations include end‑to‑end evaluation across Workspace apps (Gmail, Drive, Docs), input/output validation and sanitization, model‑level defenses, simulated attacks for continuous improvement, human oversight and controls on agentic automation, and monitoring for known IPI payload patterns.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 9. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection against the agentic browser model. Attackers embed hidden instructions in malicious web pages, third-party iframes, or user-generated content that the Gemini-in-Chrome agent ingests as part of its task context. These instructions can hijack the agent's goals (goal-hijacking), exfiltrate sensitive data (e.g., navigating to banking sites, reading emails), or attempt to bypass site-isolation boundaries when the compromised agent acts across origins. The attack can be chained with other vulnerabilities when the agent is manipulated to trigger underlying browser flaws.
- **Affected Products:** Google Chrome with Gemini in Chrome agentic capabilities (Chrome 143 stable channel and later versions with agentic features enabled)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No specific PoC URL linked in this blog post. Related class-of-attack demonstrations exist (e.g., Noma Labs' GeminiJack against Google Gemini, Brave's research against Perplexity Comet, Trail of Bits' Comet audit).
- **Patch Available:** No specific patch announced in this blog post—the post describes a new security architecture being rolled into Chrome. Chrome's auto-update capability enables rapid delivery of subsequent fixes. Related patches: Chrome stable channel update December 10, 2025 (addressing CVE-2025-14174 and others); CVE-2026-0628 (Gemini panel hijack via malicious extensions) patched in early 2026.
- **Active Exploitation:** No confirmed in-the-wild exploitation tied to a specific Chrome/Gemini CVE is documented in this blog post. The post identifies indirect prompt injection as the 'primary new threat facing all agentic browsers.' Independent research (Noma Labs' GeminiJack, Brave, Trail of Bits, Forcepoint X-Labs) confirmed prompt-injection attacks were being found and weaponized against multiple agentic AI products in 2025-2026. A directly attributable, named in-the-wild campaign against Chrome's Gemini agent specifically is not cited in this post.
- **Threat Actors:** None known
- **Mitigation:** Chrome's layered defenses include: (1) User Alignment Critic—a separate high-trust Gemini model that vets the planning model's proposed actions against the user's stated goal; (2) Spotlighting—a training/serving technique that instructs the model to prioritize user/system instructions over page content; (3) Agent Origin Sets—restricts agent actions to a Read-only origin set and a Read-writable origin set, gated by a trusted component; (4) User Confirmations—deterministic and model-based checks requiring explicit user approval before accessing sensitive sites or performing consequential actions; (5) Prompt-injection classifier—real-time scanner run in parallel with the planning model; (6) Work logs/transparency—observable record of agent steps; (7) Automated red-teaming—LLM-driven generation of malicious sandboxed sites; (8) Safe Browsing and on-device scam detection as supporting layers. End-user recommendations: keep Chrome auto-updates enabled, restrict extension interactions with the Gemini panel, and exercise caution when installing browser extensions.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic

---

## 10. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** The blog post details Android's migration from memory-unsafe C/C++ to memory-safe Rust in new and actively developed code. 2025 data shows memory-safety vulnerabilities falling below 20% of total Android vulnerabilities for the first time. Rust code shows ~0.2 memory-safety vulnerabilities per million lines of code (MLOC) vs ~1,000/MLOC in C/C++ — a ~1000× reduction. Approximately 4% of Rust code lives inside unsafe{} blocks. Rust changes show ~4× lower rollback rates and ~25% less time in code review than C++. CVE-2025-48530 (the case study CVE) was an incorrect-bounds-check bug in the Android System causing potential out-of-bounds memory accesses and remote code execution with no privileges or user interaction required; it was caught and patched internally before public release.
- **Affected Products:** Android platform (C, C++, Java, Kotlin, and Rust — first-party and third-party/open-source code). Specific components cited: Android 6.12 Linux kernel (Binder in Rust), CrabbyAVIF image library, Google Play Services (Nearby Presence), Google Messages app (MLS protocol), Chromium PNG/JSON/web-font parsers, Android firmware. CVE-2025-48530 affected Google Android 16.0 (Android System component).
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** No public proof-of-concept or weaponized exploit is documented. The blog post explicitly describes CVE-2025-48530 as a 'near-miss' that 'never made it into a public release' — it was patched internally before reaching users, so no public PoC was released for that specific issue.
- **Patch Available:** CVE-2025-48530 (the example cited in the blog post) was patched in the Android System before the vulnerable code reached any public Android release, and is documented in the Android Security Bulletin–August 2025 (security patch level 2025-08-05): https://source.android.com/docs/security/bulletin/2025-08-01 . The broader Rust-in-Android strategy is the long-term mitigation direction, not a discrete vulnerability that requires a patch.
- **Active Exploitation:** No active in-the-wild exploitation is reported. The blog post presents CVE-2025-48530 as a 'near-miss': it was identified and patched internally before reaching any public Android release, so there is no observed exploitation for that specific issue. No threat actors, APT campaigns, or ransomware operators are mentioned in connection with the strategy, components, or CVE discussed in the post.
- **Threat Actors:** None known
- **Mitigation:** Google's layered memory-safety hardening strategy: (1) write new and actively-developed code in memory-safe Rust instead of C/C++; (2) encapsulate any unsafe{} Rust behind safe abstractions and provide comprehensive internal Rust training — including a new module covering reasoning about unsafe Rust, soundness, and undefined behavior; (3) in C/C++ that cannot yet be rewritten, use the Scudo hardened allocator (which places guard pages around secondary allocations so overflows become crashes rather than exploitable memory corruption); (4) apply the Chromium 'Rule of 2' (no new code should be untrustworthy input + complex memory logic + high privilege simultaneously); (5) adhere to an industry-standard 90-day patch window. For CVE-2025-48530 specifically, the fix was applied pre-release.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

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

## 15. 🟡 High Severity — Splunk Enterprise Vulnerability Exploited in Attacks Days After Disclosure

**CVE:** `CVE-2026-20253` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://www.securityweek.com/splunk-enterprise-vulnerability-exploited-in-attacks-days-after-disclosure/>

> CISA has given federal agencies only three days to patch CVE-2026-20253, which can be exploited for unauthenticated remote code execution. The post Splunk Enterprise Vulnerability Exploited in Attacks Days After Disclosure appeared first on SecurityWeek .

---

## 16. 🟡 High Severity — Signal K Server: Server-Side Request Forgery via Remote Connection Endpoints

**CVE:** `CVE-2026-55591` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-q59x-jc9f-gfqf>

> ### Summary
signalk-server versions up to and including 2.27.0 contain a Server-Side Request Forgery (SSRF) vulnerability in three administrative endpoints used for remote Signal K server connection management. The `makeRemoteRequest()` function accepts attacker-controlled `host`, `port`, `useTLS`, and `selfsignedcert` parameters without any validation, allowing an attacker to force the server to …

---

## 17. 🟡 High Severity — gemini-mcp-tool vulnerable to OS command injection and @file exfiltration via prompt quoting (CVE-2026-0755)

**CVE:** `CVE-2026-0755` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-4h5r-5jm8-jxjm>

> Untrusted prompt input could reach the Gemini CLI @file parser, allowing read/exfiltration of arbitrary local files (@/etc/passwd, @~/.ssh/id_rsa, @../../secret). On Windows, unquoted cmd.exe metacharacters could break out into OS command injection.

Fix (1.1.6): removed the broken shell:false double-quote wrapping; added assertSafeFileReferences() to contain @file refs to the working directory; h…

---

## 18. 🟡 High Severity — OpenClaw: Internal/webchat command auth could inherit ownerAllowFrom wildcard state

**CVE:** `CVE-2026-53854` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-4hpg-mp64-x7xq>

> ### Summary

Internal/webchat command auth could inherit ownerAllowFrom wildcard state. In affected versions, a sender on an affected internal or webchat path could inherit wildcard ownerAllowFrom state across channel boundaries.

This advisory is scoped to the named feature and configuration. It does not change OpenClaw&#x27;s trusted-operator model: authenticated Gateway operators, installed plu…

---

## 19. 🟡 High Severity — F5 Patches Two Critical NGINX Open Source Flaws Enabling Remote Code Execution

**CVE:** `CVE-2026-42530` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://thehackernews.com/2026/06/f5-patches-two-critical-nginx-open.html>

> F5 has released security updates to address two critical security flaws in NGINX Open Source that could be exploited to achieve code execution on affected systems.

The vulnerabilities are listed below -


  CVE-2026-42530 (CVSS v4 score: 9.2) - A use-after-free vulnerability in the ngx_http_v3_module that could be triggered by a remote unauthenticated attacker when NGINX Open Source is

---

## 20. 🟡 High Severity — Armeria: External Control of File Name or Path in xDS SDS DataSource

**CVE:** `CVE-2026-11752` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-hgw6-8c77-v4gq>

> ## External Control of File Name or Path in xDS SDS DataSource

### Summary

`DataSourceStream` in the `:xds` module resolves control-plane-supplied `filename` and `environment_variable` fields from SDS Secret resources without any allow-list or base-directory confinement. A semi-trusted or compromised xDS control plane (or an attacker who can MITM SDS responses) can read arbitrary local files and…

---

## 21. 🟡 High Severity — Daytona: Path traversal in sandbox volume id mounts arbitrary host paths into the sandbox — cross-tenant data access and host escape

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

## 22. 🟡 High Severity — tract-nnef: integer overflow in NNEF `.dat` tensor parser yields an out-of-bounds read on model load

**CVE:** `CVE-2026-55093` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-x5mv-8wgw-29hg>

> - **Component:** `tract-nnef` (`nnef/src/tensors.rs::read_tensor`) + `tract-data` (`data/src/tensor.rs`)
- **Affected versions:** `&lt; 0.21.16`, `0.22.0`–`0.22.2`, `0.23.0`–`0.23.1` — the dense `DatLoader` path was unguarded across all three release lines; patched in 0.21.16 / 0.22.2 / 0.23.1
- **Class:** CWE-190 (integer overflow) → CWE-125 (out-of-bounds read)
- **Trigger:** loading a crafted N…

---

## 23. 🟡 High Severity — opentelemetry-collector-contrib: githubreceiver silently ignores configured required_headers authentication

**CVE:** `CVE-2026-55701` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-w5cv-pw74-4rxc>

> ## githubreceiver Silently Ignores Configured required_headers Authentication

### Summary

The githubreceiver webhook handler does not enforce the `required_headers` configuration. Headers are validated at startup (config rejects empty keys/values) but never checked on incoming requests. This follows the same pattern as [GHSA-prf6-xjxh-p698](https://github.com/open-telemetry/opentelemetry-collect…

---

## 24. 🟡 High Severity — Kirby: External Initialization of the Panel on reverse proxy setups with the `Forwarded` header

**CVE:** `CVE-2026-54003` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-whxw-24jc-cwmv>

> ### TL;DR

This vulnerability affects Kirby sites that have no configured user accounts and are running on publicly accessible servers behind a reverse proxy that sets the `Forwarded: for=...`, `X-Client-IP`, or `X-Real-IP` request header.

It was possible to install the Panel (= create the first admin user) in these setups even from remote IP addresses.

**This vulnerability is of critical severi…

---

## 25. 🟡 High Severity — Kirby: Cross-site scripting (XSS) from incomplete HTML/XML sanitization in `Dom::sanitize()`

**CVE:** `CVE-2026-54002` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-wr9h-4r83-f4v6>

> ### TL;DR

This vulnerability affects Kirby sites and plugins that use the `writer` or `list` fields or that use `$dom-&gt;sanitize()`, `Sane::sanitize()`, `Sane\Html::sanitize()`, `Sane\Svg::sanitize()`, `Sane\Xml::sanitize()`,  `Sane::sanitizeFile()` or `$file-&gt;sanitizeContents()` with untrusted input.

It was possible to inject malicious markup as children of an unknown HTML/XML tag, which w…

---

## 26. 🟡 High Severity — Kirby: Self cross-site scripting (self-XSS) in the writer field

**CVE:** `CVE-2026-49276` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-rhj6-r49h-5932>

> ### TL;DR

This vulnerability affects Kirby sites that use the writer field in any blueprint.

It was possible to include a scripting link as the target of a link (or email link). This link target would then be clickable by the user who entered it.

A successful attack commonly requires knowledge of the content structure by the attacker as well as social engineering of a user with access to the Pa…

---

## 27. 🟡 High Severity — Jupyter Server: Stored XSS in `NbconvertFileHandler` / `NbconvertPostHandler` via missing `sandbox` CSP 

**CVE:** `CVE-2026-44727` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-fcw5-x6j4-ccmp>

> The nbconvert HTTP handlers in jupyter_server render user-authored notebook HTML under the Jupyter origin without a sandbox directive in their `Content-Security-Policy`. 

Combined with `nbconvert.HTMLExporter`&#x27;s default non-sanitizing behavior, a notebook carrying an HTML payload in a display_data output triggers stored XSS with cookie access, full /api/* authority, and kernel RCE.

### Impa…

---

## 28. 🟡 High Severity — BBOT: Server-Side Request Forgery (SSRF) in docker_pull module via WWW-Authenticate realm parsing

**CVE:** `CVE-2026-12566` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-3mp7-vp6j-2mxx>

> The `docker_pull` module uses the `realm` parameter from a Docker registry&#x27;s `WWW-Authenticate` response header as the authentication endpoint without validation. An attacker in a man-in-the-middle position between bbot and a Docker registry could modify this header to redirect the authentication request to an arbitrary endpoint, potentially leaking authentication tokens.

---

## 29. 🟡 High Severity — praisonai-platform: Authorization Bypass Through User-Controlled Key

**CVE:** `CVE-2026-47415` | `CVE-2026-47418` | `CVE-2026-47419` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-2fjj-qqg8-fg7x>

> ## Summary

The issue create and update endpoints in `praisonai-platform` accept a `project_id` in the request body and persist it without validating that the project belongs to the URL workspace. A user who is a member of workspace `W_B` (and has no access to workspace `W_A`) can create issues that reference a project owned by `W_A`. Because `ProjectService.get_stats()` aggregates issues by `proj…

---

## 30. 🟡 High Severity — Grav: Admin Backup Zip File Exposes Account Credentials and Configuration Secrets

**CVE:** `CVE-2026-55885` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-2f86-9cp8-6hcf>

> ### Summary
An authenticated administrator with backup permissions can download a ZIP archive containing the full Grav installation root, including `user/accounts/admin.yaml` with the admin&#x27;s bcrypt password hash and email, plus `user/config/` with all site configuration. The download endpoint requires only the session-static `admin-nonce` in the URL, no additional form-level CSRF token, and …

---

## 31. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
