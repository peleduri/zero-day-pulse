# Zero Day Pulse

> **Generated:** 2026-06-18 20:08 UTC &nbsp;|&nbsp; **Total:** 35 &nbsp;|&nbsp; 🔴 KEV: 1 &nbsp;|&nbsp; 🟠 Zero-Day: 15 &nbsp;|&nbsp; 🟡 High: 19 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🔴 CISA KEV — CVE-2026-20253 — Splunk Enterprise Missing Authentication for Critical Function Vulnerability

**CVE:** `CVE-2026-20253` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-20253>

> Vendor: Splunk | Product: Enterprise. Splunk Enterprise contains a missing authentication for critical function vulnerability which could allow an unauthenticated user to create or truncate arbitrary files through a PostgreSQL sidecar service endpoint. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates …

**Parallel AI Enrichment:**

- **Technical Details:** The PostgreSQL sidecar service endpoint in vulnerable Splunk Enterprise versions lacks authentication controls, allowing any network‑reachable unauthenticated user to invoke file‑operation APIs and create or truncate arbitrary files on the host.
- **Affected Products:** Splunk Enterprise 10.2.0‑10.2.3 (fixed in 10.2.4), 10.0.0‑10.0.6 (fixed in 10.0.7); Splunk Enterprise 10.4.0 not affected; versions 9.4 and earlier not affected.
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Upgrade to Splunk Enterprise 10.4.0, 10.2.4, or 10.0.7 (or later). If upgrading is not feasible, disable the PostgreSQL sidecar service by adding "[postgres]\ndisabled = true" to $SPLUNK_HOME/etc/system/local/server.conf and restart Splunk, noting that this may impact Edge Processor, OpAmp, or SPL2 data pipelines.
- **Vendor Advisory:** https://advisory.splunk.com/advisories/SVD-2026-0603

---

## 2. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Multiple unauthenticated path traversal vulnerabilities in SimpleHelp <=5.5.7 allow remote attackers to read arbitrary files on the server via crafted requests, exposing sensitive files (e.g., credentials/config) and enabling follow‑on attacks.
- **Affected Products:** SimpleHelp remote support / RMM software versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true - https://www.offsec.com/blog/cve-2024-57727
- **Patch Available:** true - https://www.tenable.com/cve/CVE-2024-57727
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (unspecified groups)
- **Mitigation:** Apply the vendor patch/update; if immediate patching is not possible, isolate/unexpose SimpleHelp RMM from the public network, block external access, restrict usage to VPN or management network, rotate credentials and secrets, review logs for indicators of compromise, and follow CISA incident response recommendations.
- **Vendor Advisory:** https://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 3. 🟠 Zero-Day — AgenticMail: Unauthenticated inbound mail triggers bypassPermissions resume of the operator's Claude Code session (bridge-wake)

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-fq4x-789w-jg5h>

> ## Summary
Two inbound-mail handlers act on a privileged effect without verifying that the sender is the operator, while a sibling handler in the same repo does. The higher-impact one: any external email routed to the bridge inbox causes the dispatcher to resume the operator&#x27;s Claude Code session with `permissionMode: &#x27;bypassPermissions&#x27;`, embedding the attacker-controlled `from`/`s…

**Parallel AI Enrichment:**

- **Technical Details:** Two inbound‑mail handlers act on a privileged effect without verifying that the sender is the operator. The higher‑impact handler resumes the operator's Claude Code session with `permissionMode: 'bypassPermissions'` for any external email routed to the bridge inbox, embedding attacker‑controlled `from`, `subject`, and `preview` verbatim into the resumed agent's prompt, resulting in an indirect prompt injection into a fully‑privileged agent (Bash/Write/Edit/WebFetch + agenticmail MCP toolbelt) running as the operator's OAuth identity.
- **Affected Products:** AgenticMail (bridge component)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Disable public/external bridging to operator inboxes; ensure inbound handlers verify sender/operator identity before performing privileged resume actions; upgrade to a fixed release when a vendor advisory/patch is published; restrict Claude Code sessions' auto‑resume and avoid permissionMode bypass; apply least‑privilege for the agent toolbelt.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — Grav: Stored CSS injection via Markdown image ?style=… reaches MediaObjectTrait::style() — incomplete patch of GHSA-r7fx-8g49-7hhr

**CVE:** `CVE-2026-55890` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-pmf8-g7c8-7v54>

> ## Summary

The fix for **GHSA-r7fx-8g49-7hhr / CVE-2026-42841** (Stored XSS via Markdown media `attribute()` action) is incomplete. The maintainer patched `MediaObjectTrait::attribute()` to deny dangerous attribute names (event handlers, `style`, `xmlns`, `srcdoc`, `formaction`) but the sibling `MediaObjectTrait::style()` method is reachable through the **same Markdown excerpt-action pipeline** a…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — PraisonAI: Server-Side Request Forgery (SSRF) in SearxNG / search_web tools via attacker-controlled searxng_url parameter

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-4pcv-mg8v-vrgf>

> ### Summary
A Server-Side Request Forgery (SSRF) vulnerability in the SearxNG / `search_web` search tools allows an attacker to make the server perform requests to arbitrary internal endpoints and read the responses back. The `searxng_url` argument is passed directly to `requests.get()` with no validation of scheme, host, or port. Because `searxng_url` is exposed to the LLM as a tool parameter and…

**Parallel AI Enrichment:**

- **Technical Details:** The `searxng_url` parameter is passed directly to `requests.get()` with no validation of scheme, host, or port, allowing an attacker who can supply `searxng_url` (e.g., via prompt injection into an LLM agent that exposes the search_web/searxng_search tool) to cause the server to perform arbitrary HTTP(S) requests to internal endpoints and return responses to the attacker.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Disable or remove the search_web/searxng_search tools from agent toolsets; validate and whitelist allowed searxng_url schemes/hosts/ports; implement strict URL validation and require operator‑controlled configuration (don’t accept user‑supplied searxng_url); restrict network egress from the agent/process to only needed destinations; run the tool in an isolated environment with no access to internal services.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 6. 🟠 Zero-Day — PraisonAI: Webhook signature verification skipped (fail-open) when secret unset, allowing forged inbound webhooks (WhatsApp & Linear bots)

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-x92v-rpx6-p6cw>

> The WhatsApp and Linear bot adapters verify the inbound webhook HMAC signature only
when a secret is configured. When the secret environment variable is unset — the
default on a fresh install and common in development — verification is skipped entirely
and the webhook body is parsed and dispatched as a genuine, trusted event. A remote,
unauthenticated attacker who can reach the bot&#x27;s webhook …

**Parallel AI Enrichment:**

- **Technical Details:** When the secret environment variable is unset, the WhatsApp and Linear bot adapters skip HMAC verification of inbound webhooks, treating the request body as trusted and enabling an unauthenticated attacker to inject arbitrary events.
- **Affected Products:** PraisalAI WhatsApp bot (src/praisonai/praisonai/bots/whatsapp.py), PraisonAI Linear bot (signature verification logic)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Configure the appropriate webhook secret environment variables (e.g., WHATSAPP_APP_SECRET and the equivalent for Linear) in all deployments; restrict network access to webhook endpoints via firewall or IP allowlist; enable authentication/ingress validation; and upgrade to the patched version provided in the advisory.
- **Vendor Advisory:** https://github.com/advisories/GHSA-x92v-rpx6-p6cw

---

## 7. 🟠 Zero-Day — PraisonAI: Jobs webhook SSRF protection bypass via DNS rebinding

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

- **Technical Details:** The Jobs API validates `webhook_url` at parse/Job construction time and blocks loopback/private targets, but validation is not enforced at send time: `_send_webhook()` calls `httpx.AsyncClient.post()` with the original hostname without send‑time validation, IP pinning, or guarded transport. An attacker‑controlled hostname can resolve to a public IP during validation and later resolve to loopback/private (DNS rebinding), enabling SSRF to internal services.
- **Affected Products:** PraisonAI (versions prior to 4.6.34)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Upgrade to the vendor‑fixed release; as a workaround, enforce send‑time validation, IP pinning, resolve hostnames to IP and validate against allowed CIDRs, restrict AllowedHosts/Allowed CIDRs, or block DNS‑rebindable hostnames. Follow PraisonAI security guidance and apply network egress restrictions.
- **Vendor Advisory:** https://github.com/advisories/GHSA-rjvw-7vvw-549v

---

## 8. 🟠 Zero-Day — PraisonAI: SpiderTools redirect-target SSRF protection bypass

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-6h9p-93hq-q7h6>

> # SpiderTools redirect-target SSRF protection bypass

## Summary

`SpiderTools.scrape_page()` validates the initial URL and rejects direct
loopback, private, link-local, metadata, and internal hostnames. It then calls
`requests.Session.get()` without disabling automatic redirects or validating
redirect `Location` targets.

Requests follows redirects by default for GET requests. A safe-looking publ…

**Parallel AI Enrichment:**

- **Technical Details:** SpiderTools.scrape_page() first validates the supplied URL, rejecting obvious internal addresses. It then uses requests.Session.get() without disabling automatic redirects or checking the Location header of redirects. Consequently, an attacker can provide a benign external URL that redirects to a blocked internal endpoint (e.g., 127.0.0.1 or 169.254.169.254), causing the library to fetch and process the internal resource, resulting in a server‑side request forgery.
- **Affected Products:** PraisonAI SpiderTools
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://github.com/advisories/GHSA-6h9p-93hq-q7h6

---

## 9. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) allows an attacker to inject malicious instructions into the prompt of an AI model via crafted user‑controlled data. The attack can be chained with other techniques (e.g., zero‑click exploits) to achieve execution or data leakage without direct user interaction.
- **Affected Products:** Google Gemini Enterprise (version unspecified)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (see https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/)
- **Patch Available:** true (see http://nvd.nist.gov/vuln/detail/CVE-2025-54131)
- **Active Exploitation:** true (see https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/ and http://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads)
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 10. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when attacker‑controlled content in external data sources (e.g., shared Workspace files) contains hidden instructions that the LLM interprets as task directives. GeminiJack is a zero‑click IPI where malicious instructions embedded in Workspace content cause Gemini Enterprise to follow attacker commands and potentially exfiltrate data without any user input.
- **Affected Products:** Google Gemini Enterprise (Workspace integrations)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true - http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability
- **Patch Available:** true - http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html
- **Active Exploitation:** true - http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability
- **Threat Actors:** None known
- **Mitigation:** Apply Google’s layered defenses and hardening for IPI as documented in the Google Security Blog: content filtering, provenance signals, tool/data access restrictions, iterative monitoring and updates; use Workspace admin controls to limit external/shared content, disable risky agentic automation, and employ content sanitization and allow‑listing.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 11. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

---

## 12. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

---

## 13. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 14. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

---

## 15. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 16. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

---

## 17. 🟡 High Severity — F5 Patches Two Critical NGINX Open Source Flaws Enabling Remote Code Execution

**CVE:** `CVE-2026-42530` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://thehackernews.com/2026/06/f5-patches-two-critical-nginx-open.html>

> F5 has released security updates to address two critical security flaws in NGINX Open Source that could be exploited to achieve code execution on affected systems.

The vulnerabilities are listed below -


  CVE-2026-42530 (CVSS v4 score: 9.2) - A use-after-free vulnerability in the ngx_http_v3_module that could be triggered by a remote unauthenticated attacker when NGINX Open Source is

---

## 18. 🟡 High Severity — Armeria: External Control of File Name or Path in xDS SDS DataSource

**CVE:** `CVE-2026-11752` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-hgw6-8c77-v4gq>

> ## External Control of File Name or Path in xDS SDS DataSource

### Summary

`DataSourceStream` in the `:xds` module resolves control-plane-supplied `filename` and `environment_variable` fields from SDS Secret resources without any allow-list or base-directory confinement. A semi-trusted or compromised xDS control plane (or an attacker who can MITM SDS responses) can read arbitrary local files and…

---

## 19. 🟡 High Severity — Daytona: Path traversal in sandbox volume id mounts arbitrary host paths into the sandbox — cross-tenant data access and host escape

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

## 20. 🟡 High Severity — tract-nnef: integer overflow in NNEF `.dat` tensor parser yields an out-of-bounds read on model load

**CVE:** `CVE-2026-55093` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-x5mv-8wgw-29hg>

> - **Component:** `tract-nnef` (`nnef/src/tensors.rs::read_tensor`) + `tract-data` (`data/src/tensor.rs`)
- **Affected versions:** `&lt; 0.21.16`, `0.22.0`–`0.22.2`, `0.23.0`–`0.23.1` — the dense `DatLoader` path was unguarded across all three release lines; patched in 0.21.16 / 0.22.2 / 0.23.1
- **Class:** CWE-190 (integer overflow) → CWE-125 (out-of-bounds read)
- **Trigger:** loading a crafted N…

---

## 21. 🟡 High Severity — opentelemetry-collector-contrib: githubreceiver silently ignores configured required_headers authentication

**CVE:** `CVE-2026-55701` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-w5cv-pw74-4rxc>

> ## githubreceiver Silently Ignores Configured required_headers Authentication

### Summary

The githubreceiver webhook handler does not enforce the `required_headers` configuration. Headers are validated at startup (config rejects empty keys/values) but never checked on incoming requests. This follows the same pattern as [GHSA-prf6-xjxh-p698](https://github.com/open-telemetry/opentelemetry-collect…

---

## 22. 🟡 High Severity — Kirby: External Initialization of the Panel on reverse proxy setups with the `Forwarded` header

**CVE:** `CVE-2026-54003` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-whxw-24jc-cwmv>

> ### TL;DR

This vulnerability affects Kirby sites that have no configured user accounts and are running on publicly accessible servers behind a reverse proxy that sets the `Forwarded: for=...`, `X-Client-IP`, or `X-Real-IP` request header.

It was possible to install the Panel (= create the first admin user) in these setups even from remote IP addresses.

**This vulnerability is of critical severi…

---

## 23. 🟡 High Severity — Kirby: Cross-site scripting (XSS) from incomplete HTML/XML sanitization in `Dom::sanitize()`

**CVE:** `CVE-2026-54002` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-wr9h-4r83-f4v6>

> ### TL;DR

This vulnerability affects Kirby sites and plugins that use the `writer` or `list` fields or that use `$dom-&gt;sanitize()`, `Sane::sanitize()`, `Sane\Html::sanitize()`, `Sane\Svg::sanitize()`, `Sane\Xml::sanitize()`,  `Sane::sanitizeFile()` or `$file-&gt;sanitizeContents()` with untrusted input.

It was possible to inject malicious markup as children of an unknown HTML/XML tag, which w…

---

## 24. 🟡 High Severity — Kirby: Self cross-site scripting (self-XSS) in the writer field

**CVE:** `CVE-2026-49276` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-rhj6-r49h-5932>

> ### TL;DR

This vulnerability affects Kirby sites that use the writer field in any blueprint.

It was possible to include a scripting link as the target of a link (or email link). This link target would then be clickable by the user who entered it.

A successful attack commonly requires knowledge of the content structure by the attacker as well as social engineering of a user with access to the Pa…

---

## 25. 🟡 High Severity — Jupyter Server: Stored XSS in `NbconvertFileHandler` / `NbconvertPostHandler` via missing `sandbox` CSP 

**CVE:** `CVE-2026-44727` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-fcw5-x6j4-ccmp>

> The nbconvert HTTP handlers in jupyter_server render user-authored notebook HTML under the Jupyter origin without a sandbox directive in their `Content-Security-Policy`. 

Combined with `nbconvert.HTMLExporter`&#x27;s default non-sanitizing behavior, a notebook carrying an HTML payload in a display_data output triggers stored XSS with cookie access, full /api/* authority, and kernel RCE.

### Impa…

---

## 26. 🟡 High Severity — BBOT: Server-Side Request Forgery (SSRF) in docker_pull module via WWW-Authenticate realm parsing

**CVE:** `CVE-2026-12566` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-3mp7-vp6j-2mxx>

> The `docker_pull` module uses the `realm` parameter from a Docker registry&#x27;s `WWW-Authenticate` response header as the authentication endpoint without validation. An attacker in a man-in-the-middle position between bbot and a Docker registry could modify this header to redirect the authentication request to an arbitrary endpoint, potentially leaking authentication tokens.

---

## 27. 🟡 High Severity — praisonai-platform: Authorization Bypass Through User-Controlled Key

**CVE:** `CVE-2026-47415` | `CVE-2026-47418` | `CVE-2026-47419` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-2fjj-qqg8-fg7x>

> ## Summary

The issue create and update endpoints in `praisonai-platform` accept a `project_id` in the request body and persist it without validating that the project belongs to the URL workspace. A user who is a member of workspace `W_B` (and has no access to workspace `W_A`) can create issues that reference a project owned by `W_A`. Because `ProjectService.get_stats()` aggregates issues by `proj…

---

## 28. 🟡 High Severity — Grav: Admin Backup Zip File Exposes Account Credentials and Configuration Secrets

**CVE:** `CVE-2026-55885` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-2f86-9cp8-6hcf>

> ### Summary
An authenticated administrator with backup permissions can download a ZIP archive containing the full Grav installation root, including `user/accounts/admin.yaml` with the admin&#x27;s bcrypt password hash and email, plus `user/config/` with all site configuration. The download endpoint requires only the session-static `admin-nonce` in the URL, no additional form-level CSRF token, and …

---

## 29. 🟡 High Severity — praisonaiagents: SSRF guard validates literal IPs only and never resolves DNS

**CVE:** `CVE-2026-47390` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-vxgj-xg5c-p4h7>

> # praisonaiagents: SSRF guard validates literal IPs only and never resolves DNS

**Researcher:** Kai Aizen — SnailSploit (@SnailSploit), Adversarial &amp; Offensive Security Research
**Target:** https://github.com/MervinPraison/PraisonAI
**Weakness:** CWE-918 Server-Side Request Forgery (SSRF).

---

## Summary

The SSRF guard shared by PraisonAI&#x27;s web tools (`SpiderTools._validate_url` → `_h…

---

## 30. 🟡 High Severity —  ZITADEL: Missing client_id binding in OIDC authorization code exchange and refresh token flows (RFC 6749 Section 4.1.3 violation)

**CVE:** `CVE-2026-55672` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-xqxv-4jc2-x56x>

> ### Summary

Zitadel&#x27;s OAuth2 / OIDC `CodeExchange` and `RefreshToken` implementations omit a critical validation step to ensure that the requesting client matches the client that originally initiated the authorization flow. This violates RFC 6749 Section 4.1.3, which mandates that the authorization server must ensure the authorization code was issued to the authenticated confidential client.…

---

## 31. 🟡 High Severity —  ZITADEL: Cross-Tenant User Leakage via Recycled Identifiers

**CVE:** `CVE-2026-55670` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-6x8v-2fq5-2229>

> ### Summary

A flaw in the user lifecycle enforcement allowed deleted users to retain their original organization/tenant association. Recreating a deleted user under a distinct organization can cause the new user instance to be incorrectly provisioned within the original organization if the previous ID would be used to recreate it.

### Impact

When a user is created, the system maps the generated…

---

## 32. 🟡 High Severity — Hydro: Insufficient session expiration when recreating sessions

**CVE:** `CVE-2026-55617` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-94jp-7776-qj6q>

> ### Impact

Hydro contains an insufficient session expiration vulnerability in its session recreation logic. When a session is recreated, including during logout or other session renewal flows, Hydro creates a new session token but does not delete the previous server-side session token.

As a result, an old sid cookie may remain valid even after the legitimate user logs out or the session is recre…

---

## 33. 🟡 High Severity — http-proxy-middleware: multipart/form-data field injection via unescaped CRLF in `fixRequestBody`

**CVE:** `CVE-2026-55603` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-gcq2-9pq2-cxqm>

> ## Summary
`fixRequestBody()` is the library&#x27;s documented helper for re-emitting a request body that was already consumed by a body parser. When the **outgoing** `Content-Type` is `multipart/form-data`, it rebuilds the body with `handlerFormDataBodyData()`, which interpolates each `req.body` key and value directly into the multipart wire format **without neutralizing CR/LF**:

```js
// dist/h…

---

## 34. 🟡 High Severity — Oracle June 2026 Critical Security Patch Update Addresses 243 CVEs (CVE-2026-35273)

**CVE:** `CVE-2026-35273` &nbsp;|&nbsp; **Source:** Tenable Security Research &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://www.tenable.com/blog/oracle-june-2026-critical-security-patch-update-addresses-243-cves-cve-2026-35273>

> Oracle addresses 243 CVEs in its June 2026 Critical Security Patch Update with 245 patches, including 122 critical updates. Key Takeaways The June 2026 Critical Security Patch Update (CSPU) contains fixes for 243 unique CVEs in 245 security updates 122 issues (49.8% of all patches) were assigned a critical severity rating Oracle Fusion Middleware received the highest number of patches at 106, acco…

---

## 35. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
