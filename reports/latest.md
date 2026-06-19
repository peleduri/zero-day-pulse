# Zero Day Pulse

> **Generated:** 2026-06-19 14:39 UTC &nbsp;|&nbsp; **Total:** 33 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 21 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal vulnerability allowing unauthenticated remote attackers to read sensitive files via directory/path traversal in SimpleHelp 5.5.7 and earlier.
- **Affected Products:** SimpleHelp Remote Support / RMM versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (unspecified)
- **Mitigation:** Immediately upgrade SimpleHelp to the patched version (post‑5.5.7), or disconnect/unexpose SimpleHelp from public networks, restrict access via firewall/VPN, and monitor for indicators of compromise per CISA guidance.
- **Vendor Advisory:** https://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — CISA: Splunk Enterprise flaw actively exploited, patch by Sunday

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-splunk-enterprise-flaw-actively-exploited-patch-by-sunday/>

> CISA has urged U.S. federal agencies to secure their systems by Sunday against a critical Splunk Enterprise vulnerability that is being exploited in attacks. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated PostgreSQL sidecar service endpoint allows arbitrary file creation/truncation, which can be chained to remote code execution via lo_export or malicious database restore.
- **Affected Products:** Splunk Enterprise 10.2.0‑10.2.3, 10.0.0‑10.0.6
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true - https://www.bleepingcomputer.com/news/security/cisa-splunk-enterprise-flaw-actively-exploited-patch-by-sunday/
- **Patch Available:** true - https://advisory.splunk.com/advisories/SVD-2026-0610
- **Active Exploitation:** true - https://www.cisa.gov/news-events/alerts/2026/06/18/cisa-adds-one-known-exploited-vulnerability-catalog
- **Threat Actors:** None known
- **Mitigation:** Apply the patches (10.2.4 or 10.0.7) immediately. If patching is not possible, disable the PostgreSQL sidecar service and restrict network access to the service to trusted IPs; implement network segmentation and monitor relevant logs.
- **Vendor Advisory:** https://advisory.splunk.com/advisories/SVD-2026-0610

---

## 3. 🟠 Zero-Day — AgenticMail: Unauthenticated inbound mail triggers bypassPermissions resume of the operator's Claude Code session (bridge-wake)

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-fq4x-789w-jg5h>

> ## Summary
Two inbound-mail handlers act on a privileged effect without verifying that the sender is the operator, while a sibling handler in the same repo does. The higher-impact one: any external email routed to the bridge inbox causes the dispatcher to resume the operator&#x27;s Claude Code session with `permissionMode: &#x27;bypassPermissions&#x27;`, embedding the attacker-controlled `from`/`s…

**Parallel AI Enrichment:**

- **Technical Details:** An external email sent to the bridge inbox triggers the dispatcher to resume the operator's Claude Code session with `permissionMode: 'bypassPermissions'`. The attacker‑controlled `from`, `subject`, and `preview` fields are inserted verbatim into the prompt, enabling an indirect prompt injection into a fully‑privileged agent running as the operator.
- **Affected Products:** AgenticMail (npm package @agenticmail/claudecode)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://github.com/advisories/GHSA-fq4x-789w-jg5h

---

## 4. 🟠 Zero-Day — Grav: Stored CSS injection via Markdown image ?style=… reaches MediaObjectTrait::style() — incomplete patch of GHSA-r7fx-8g49-7hhr

**CVE:** `CVE-2026-55890` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-pmf8-g7c8-7v54>

> ## Summary

The fix for **GHSA-r7fx-8g49-7hhr / CVE-2026-42841** (Stored XSS via Markdown media `attribute()` action) is incomplete. The maintainer patched `MediaObjectTrait::attribute()` to deny dangerous attribute names (event handlers, `style`, `xmlns`, `srcdoc`, `formaction`) but the sibling `MediaObjectTrait::style()` method is reachable through the **same Markdown excerpt-action pipeline** a…

**Parallel AI Enrichment:**

- **Technical Details:** Stored CSS injection via Markdown image: MediaObjectTrait::style() writes editor‑controlled strings directly into the rendered <img style="…"> attribute without sanitization, allowing an admin.pages user to inject arbitrary CSS (stored XSS/CSS injection).
- **Affected Products:** Grav CMS (versions up to the release prior to the incomplete GHSA fix)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true - https://github.com/advisories/GHSA-pmf8-g7c8-7v54
- **Patch Available:** true - http://advisories.gitlab.com/composer/getgrav/grav/CVE-2026-55890
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Restrict who can edit pages (remove admin.pages from untrusted users), sanitize or remove style attributes at render time, patch MediaObjectTrait::style() to reject/sanitize dangerous content, and apply the vendor patch/advisory once complete.
- **Vendor Advisory:** http://advisories.gitlab.com/composer/getgrav/grav/CVE-2026-55890

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Google describes Indirect Prompt Injection (IPI) as attackers seeding malicious instructions in web content or hidden site code that AI agents may ingest via browsing or multi-source inputs; examples include hidden comments, URL fragments, or obfuscated payloads that cause agents to follow attacker-supplied instructions instead of intended task context.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Google recommends proactive web monitoring for IPI patterns, input/output validation and sanitization, limiting external browsing for agents, human oversight, strict prompt/agent isolation, and continuous vendor patching and threat‑hunting.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) enables attackers to inject malicious instructions into secondary data sources (web content, integrated tools, or external connectors) that LLM‑based agents consume while fulfilling user queries, potentially influencing model behavior or causing data exfiltration; GeminiJack exploited an architectural interaction allowing zero‑click exfiltration via crafted inputs in integrated services.
- **Affected Products:** Google Workspace (Workspace with Gemini integrations), Google Gemini Enterprise, Vertex AI Search
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true — https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability
- **Patch Available:** true — https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Layered defenses per Google: content filtering and sanitization, provenance and trust signals, query and tool isolation, least‑privilege access for connectors, monitoring and anomaly detection, model behavior constraints and prompt hardening. Follow vendor advisory for configuration and updates.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is the primary new threat facing agentic browsers. Adversaries embed malicious natural-language instructions in untrusted web content (malicious sites, third-party iframes, user-generated content such as reviews, or hidden HTML/CSS via comments/display:none/transparent text). When an agentic AI in Chrome (powered by Gemini) ingests that content, the injected instructions can hijack the agent's planning and execution path ('goal hijacking')—e.g., initiating unintended financial transactions or exfiltrating user data.
- **Affected Products:** Google Chrome with Gemini in Chrome / agentic capabilities (no specific version range stated)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true - http://security.googleblog.com/2025/12/architecting-security-for-agentic.html (delivered via Chrome auto-updates rolling out from December 2025). A related but distinct CVE-2026-0628 was patched in Chrome 143.0.7499.192 (https://chromereleases.googleblog.com/2026/01/stable-channel-update-for-desktop.html) approximately one month later.
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Chrome's layered defense architecture (delivered via Chrome auto-updates): (1) User Alignment Critic evaluates each proposed action for task alignment before execution; (2) Agent Origin Sets restrict the agent's read/write permissions to a defined set of task-relevant origins, blocking cross-origin data leakage; (3) User Confirmations use deterministic plus model-based checks to require explicit user approval on sensitive sites (e.g., banking) or consequential actions (e.g., payments); (4) Real-time Detection runs a prompt-injection classifier in parallel with the planning model; (5) Spotlighting instructs the model to prioritize user/system messages over untrusted page content; (6) Deterministic URL Checks restrict model-generated URLs to an allow-listed set of public roots; (7) automated Red-teaming generates adversarial sandboxed sites for ongoing testing. Users should keep Chrome auto-updates enabled to receive these protections.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Near-miss linear buffer overflow in CrabbyAVIF (unsafe Rust usage) discovered and fixed pre-release; Scudo hardened allocator prevented exploitation by placing guard pages around secondary allocations and converted overflow into a noisy crash; crash reporting gap fixed.
- **Affected Products:** Android platform: CrabbyAVIF (platform/external/rust/crabbyavif)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Ensure Scudo hardened allocator enabled; patch applied to CrabbyAVIF; add unsafe‑Rust training and unsafe‑review processes; follow defense‑in‑depth (static analysis, sandboxing, runtime mitigations).
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection involves hidden malicious instructions in external data sources that become part of an LLM's prompt, enabling the attacker to cause the model to execute unwanted commands or exfiltrate data without direct user input.
- **Affected Products:** Microsoft 365 Copilot, Microsoft Copilot Studio (CVE-2026-21520), unspecified product fixed in version 1.3 (CVE-2025-54131)
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (http://arxiv.org/abs/2509.10540)
- **Patch Available:** true (http://nvd.nist.gov/vuln/detail/CVE-2025-54131)
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply layered defenses: validate and sanitize external data before it reaches the model, employ content‑filtering and prompt‑guardrails, run model calls in isolated sandboxes, and monitor for anomalous model behavior.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** State‑sponsored actors compromise large backbone, provider edge (PE), and customer edge (CE) routers, modify firmware or configuration to establish persistent footholds, and leverage trusted connections to pivot laterally across targeted networks.
- **Affected Products:** Backbone routers, Provider edge (PE) routers, Customer edge (CE) routers
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Apply the mitigations outlined in the CISA advisory: patch router firmware where updates are available, enforce strong authentication, segment networks, monitor for anomalous traffic, and disable unnecessary services.
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

## 13. 🟡 High Severity — guzzlehttp/guzzle: Dot-Only Cookie Domains Match All Hosts

**CVE:** `CVE-2026-55767` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-cwxw-98qj-8qjx>

> ### Impact

`CookieJar` incorrectly accepts cookies with a dot-only `Domain` attribute, such as `Domain=.`, `Domain=..`, `Domain=...`, and whitespace-padded variants such as `Domain= . `. In affected versions, `SetCookie::matchesDomain()` removes leading dots from the cookie domain, normalizing dot-only values to the empty string; `SetCookie::validate()` only rejected a strictly empty domain, so t…

---

## 14. 🟡 High Severity — undici vulnerable to cross-origin request routing via SOCKS5 proxy pool reuse

**CVE:** `CVE-2026-6734` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-hm92-r4w5-c3mj>

> ## Impact

When using `Socks5ProxyAgent`, undici reuses a single connection pool across different origins without verifying that the pool&#x27;s origin matches the requested origin. All requests are dispatched through the pool connected to the first origin, regardless of the intended destination.

This causes cross-origin request routing: credentials and request data intended for origin B are sent…

---

## 15. 🟡 High Severity — NL Portal Backend Libraries: Unauthenticated form resolver forwards the privileged Objecten-API token to a caller-supplied URL (SSRF)

**CVE:** `CVE-2026-55414` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-xm3x-9cfw-jhx4>

> ## Summary

The public GraphQL resolvers `getFormDefinitionByObjectenApiUrl(url)` and the deprecated `getFormDefinitionById(id)` fetch a caller-supplied URL using the **privileged Objecten-API token**. Because the `/graphql` endpoint is `permitAll()` and these resolvers do not declare a `CommonGroundAuthentication` parameter, an **unauthenticated** caller can make the backend issue an outbound req…

---

## 16. 🟡 High Severity — canto-saas-api: OAuth credentials exposed in URL query string and exception messages

**CVE:** `CVE-2026-55375` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-37pm-83g7-r22v>

> ## Summary

  In affected versions, the OAuth2 token request sends `app_id`, `app_secret`,
  `refresh_token` and `code` as URL query parameters of the POST request to
  `https://oauth.&lt;domain&gt;/oauth/api/oauth2/token`. Request URLs are commonly
  recorded in access logs, proxy logs and APM traces, so the application secret
  and refresh token can be persisted in plain text outside the applica…

---

## 17. 🟡 High Severity — Network-AI: CVE-2026-46701 fix incomplete — empty default secret still authorizes all requests

**CVE:** `CVE-2026-48814` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-r78r-rwrf-rjwp>

> ## Advisory / Disclosure

# Network-AI — CVE-2026-46701 fix is incomplete: the &quot;Empty Default Secret&quot; unauth path survives

**Target:** Jovancoding/Network-AI (npm `network-ai`), **latest v5.7.1**
**Status:** the advisory (&quot;Unauthenticated Cross-Origin MCP Tool Invocation via Empty
Default Secret&quot;) named three flaws. The fix (5.4.5) closed the **CORS** flaw
(`Access-Control-All…

---

## 18. 🟡 High Severity — Splunk Enterprise Vulnerability Exploited in Attacks Days After Disclosure

**CVE:** `CVE-2026-20253` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://www.securityweek.com/splunk-enterprise-vulnerability-exploited-in-attacks-days-after-disclosure/>

> CISA has given federal agencies only three days to patch CVE-2026-20253, which can be exploited for unauthenticated remote code execution. The post Splunk Enterprise Vulnerability Exploited in Attacks Days After Disclosure appeared first on SecurityWeek .

---

## 19. 🟡 High Severity — Signal K Server: Server-Side Request Forgery via Remote Connection Endpoints

**CVE:** `CVE-2026-55591` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-q59x-jc9f-gfqf>

> ### Summary
signalk-server versions up to and including 2.27.0 contain a Server-Side Request Forgery (SSRF) vulnerability in three administrative endpoints used for remote Signal K server connection management. The `makeRemoteRequest()` function accepts attacker-controlled `host`, `port`, `useTLS`, and `selfsignedcert` parameters without any validation, allowing an attacker to force the server to …

---

## 20. 🟡 High Severity — gemini-mcp-tool vulnerable to OS command injection and @file exfiltration via prompt quoting (CVE-2026-0755)

**CVE:** `CVE-2026-0755` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-4h5r-5jm8-jxjm>

> Untrusted prompt input could reach the Gemini CLI @file parser, allowing read/exfiltration of arbitrary local files (@/etc/passwd, @~/.ssh/id_rsa, @../../secret). On Windows, unquoted cmd.exe metacharacters could break out into OS command injection.

Fix (1.1.6): removed the broken shell:false double-quote wrapping; added assertSafeFileReferences() to contain @file refs to the working directory; h…

---

## 21. 🟡 High Severity — OpenClaw: Internal/webchat command auth could inherit ownerAllowFrom wildcard state

**CVE:** `CVE-2026-53854` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-4hpg-mp64-x7xq>

> ### Summary

Internal/webchat command auth could inherit ownerAllowFrom wildcard state. In affected versions, a sender on an affected internal or webchat path could inherit wildcard ownerAllowFrom state across channel boundaries.

This advisory is scoped to the named feature and configuration. It does not change OpenClaw&#x27;s trusted-operator model: authenticated Gateway operators, installed plu…

---

## 22. 🟡 High Severity — F5 Patches Two Critical NGINX Open Source Flaws Enabling Remote Code Execution

**CVE:** `CVE-2026-42530` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://thehackernews.com/2026/06/f5-patches-two-critical-nginx-open.html>

> F5 has released security updates to address two critical security flaws in NGINX Open Source that could be exploited to achieve code execution on affected systems.

The vulnerabilities are listed below -


  CVE-2026-42530 (CVSS v4 score: 9.2) - A use-after-free vulnerability in the ngx_http_v3_module that could be triggered by a remote unauthenticated attacker when NGINX Open Source is

---

## 23. 🟡 High Severity — Armeria: External Control of File Name or Path in xDS SDS DataSource

**CVE:** `CVE-2026-11752` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-hgw6-8c77-v4gq>

> ## External Control of File Name or Path in xDS SDS DataSource

### Summary

`DataSourceStream` in the `:xds` module resolves control-plane-supplied `filename` and `environment_variable` fields from SDS Secret resources without any allow-list or base-directory confinement. A semi-trusted or compromised xDS control plane (or an attacker who can MITM SDS responses) can read arbitrary local files and…

---

## 24. 🟡 High Severity — Daytona: Path traversal in sandbox volume id mounts arbitrary host paths into the sandbox — cross-tenant data access and host escape

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

## 25. 🟡 High Severity — tract-nnef: integer overflow in NNEF `.dat` tensor parser yields an out-of-bounds read on model load

**CVE:** `CVE-2026-55093` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-x5mv-8wgw-29hg>

> - **Component:** `tract-nnef` (`nnef/src/tensors.rs::read_tensor`) + `tract-data` (`data/src/tensor.rs`)
- **Affected versions:** `&lt; 0.21.16`, `0.22.0`–`0.22.2`, `0.23.0`–`0.23.1` — the dense `DatLoader` path was unguarded across all three release lines; patched in 0.21.16 / 0.22.2 / 0.23.1
- **Class:** CWE-190 (integer overflow) → CWE-125 (out-of-bounds read)
- **Trigger:** loading a crafted N…

---

## 26. 🟡 High Severity — opentelemetry-collector-contrib: githubreceiver silently ignores configured required_headers authentication

**CVE:** `CVE-2026-55701` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-w5cv-pw74-4rxc>

> ## githubreceiver Silently Ignores Configured required_headers Authentication

### Summary

The githubreceiver webhook handler does not enforce the `required_headers` configuration. Headers are validated at startup (config rejects empty keys/values) but never checked on incoming requests. This follows the same pattern as [GHSA-prf6-xjxh-p698](https://github.com/open-telemetry/opentelemetry-collect…

---

## 27. 🟡 High Severity — Kirby: External Initialization of the Panel on reverse proxy setups with the `Forwarded` header

**CVE:** `CVE-2026-54003` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-whxw-24jc-cwmv>

> ### TL;DR

This vulnerability affects Kirby sites that have no configured user accounts and are running on publicly accessible servers behind a reverse proxy that sets the `Forwarded: for=...`, `X-Client-IP`, or `X-Real-IP` request header.

It was possible to install the Panel (= create the first admin user) in these setups even from remote IP addresses.

**This vulnerability is of critical severi…

---

## 28. 🟡 High Severity — Kirby: Cross-site scripting (XSS) from incomplete HTML/XML sanitization in `Dom::sanitize()`

**CVE:** `CVE-2026-54002` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-wr9h-4r83-f4v6>

> ### TL;DR

This vulnerability affects Kirby sites and plugins that use the `writer` or `list` fields or that use `$dom-&gt;sanitize()`, `Sane::sanitize()`, `Sane\Html::sanitize()`, `Sane\Svg::sanitize()`, `Sane\Xml::sanitize()`,  `Sane::sanitizeFile()` or `$file-&gt;sanitizeContents()` with untrusted input.

It was possible to inject malicious markup as children of an unknown HTML/XML tag, which w…

---

## 29. 🟡 High Severity — Kirby: Self cross-site scripting (self-XSS) in the writer field

**CVE:** `CVE-2026-49276` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-rhj6-r49h-5932>

> ### TL;DR

This vulnerability affects Kirby sites that use the writer field in any blueprint.

It was possible to include a scripting link as the target of a link (or email link). This link target would then be clickable by the user who entered it.

A successful attack commonly requires knowledge of the content structure by the attacker as well as social engineering of a user with access to the Pa…

---

## 30. 🟡 High Severity — Jupyter Server: Stored XSS in `NbconvertFileHandler` / `NbconvertPostHandler` via missing `sandbox` CSP 

**CVE:** `CVE-2026-44727` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-fcw5-x6j4-ccmp>

> The nbconvert HTTP handlers in jupyter_server render user-authored notebook HTML under the Jupyter origin without a sandbox directive in their `Content-Security-Policy`. 

Combined with `nbconvert.HTMLExporter`&#x27;s default non-sanitizing behavior, a notebook carrying an HTML payload in a display_data output triggers stored XSS with cookie access, full /api/* authority, and kernel RCE.

### Impa…

---

## 31. 🟡 High Severity — BBOT: Server-Side Request Forgery (SSRF) in docker_pull module via WWW-Authenticate realm parsing

**CVE:** `CVE-2026-12566` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-3mp7-vp6j-2mxx>

> The `docker_pull` module uses the `realm` parameter from a Docker registry&#x27;s `WWW-Authenticate` response header as the authentication endpoint without validation. An attacker in a man-in-the-middle position between bbot and a Docker registry could modify this header to redirect the authentication request to an arbitrary endpoint, potentially leaking authentication tokens.

---

## 32. 🟡 High Severity — praisonai-platform: Authorization Bypass Through User-Controlled Key

**CVE:** `CVE-2026-47415` | `CVE-2026-47418` | `CVE-2026-47419` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-2fjj-qqg8-fg7x>

> ## Summary

The issue create and update endpoints in `praisonai-platform` accept a `project_id` in the request body and persist it without validating that the project belongs to the URL workspace. A user who is a member of workspace `W_B` (and has no access to workspace `W_A`) can create issues that reference a project owned by `W_A`. Because `ProjectService.get_stats()` aggregates issues by `proj…

---

## 33. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
