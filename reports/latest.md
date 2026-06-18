# Zero Day Pulse

> **Generated:** 2026-06-18 14:42 UTC &nbsp;|&nbsp; **Total:** 32 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 16 &nbsp;|&nbsp; 🟡 High: 16 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a directory traversal flaw in SimpleHelp versions ≤5.5.7 that lets unauthenticated attackers read sensitive files by manipulating file paths.
- **Affected Products:** SimpleHelp remote support software version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (unspecified) leveraging CVE-2024-57727
- **Mitigation:** Upgrade SimpleHelp to a version newer than 5.5.7; apply network segmentation and restrict remote access where possible.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — PraisonAI: Server-Side Request Forgery (SSRF) in SearxNG / search_web tools via attacker-controlled searxng_url parameter

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-4pcv-mg8v-vrgf>

> ### Summary
A Server-Side Request Forgery (SSRF) vulnerability in the SearxNG / `search_web` search tools allows an attacker to make the server perform requests to arbitrary internal endpoints and read the responses back. The `searxng_url` argument is passed directly to `requests.get()` with no validation of scheme, host, or port. Because `searxng_url` is exposed to the LLM as a tool parameter and…

**Parallel AI Enrichment:**

- **Technical Details:** An SSRF in SearxNG’s search tools: the `searxng_url` argument is passed directly to `requests.get()` with no validation of scheme, host, or port, allowing an attacker to cause the server to request arbitrary internal endpoints and return the responses.
- **Affected Products:** SearxNG search tools (search_web / searxng_search)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Disable or restrict the search_web / searxng_search tools until patched; validate and restrict searxng_url inputs to allowed hosts/schemes/ports; use network egress controls and metadata server protections; treat tool parameters from untrusted content as untrusted and sanitize.
- **Vendor Advisory:** https://github.com/advisories/GHSA-4pcv-mg8v-vrgf

---

## 3. 🟠 Zero-Day — PraisonAI: Webhook signature verification skipped (fail-open) when secret unset, allowing forged inbound webhooks (WhatsApp & Linear bots)

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-x92v-rpx6-p6cw>

> The WhatsApp and Linear bot adapters verify the inbound webhook HMAC signature only
when a secret is configured. When the secret environment variable is unset — the
default on a fresh install and common in development — verification is skipped entirely
and the webhook body is parsed and dispatched as a genuine, trusted event. A remote,
unauthenticated attacker who can reach the bot&#x27;s webhook …

**Parallel AI Enrichment:**

- **Technical Details:** When the webhook secret environment variable is unset, the adapter skips HMAC signature verification and processes the request as authentic, enabling unauthenticated attackers to inject arbitrary events.
- **Affected Products:** PraisonAI WhatsApp bot adapter, PraisonAI Linear bot adapter
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Configure the WHATSAPP_APP_SECRET and Linear bot webhook secret environment variables before deployment; ensure the secret is set in production to prevent signature verification from being skipped.
- **Vendor Advisory:** https://github.com/advisories/GHSA-x92v-rpx6-p6cw

---

## 4. 🟠 Zero-Day — PraisonAI: Jobs webhook SSRF protection bypass via DNS rebinding

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

- **Technical Details:** PraisonAI's Jobs API validates `webhook_url` during request parsing and when building the Job object to block loopback/private addresses, but that validation uses DNS at parse time and is not bound to the subsequent network request. The webhook sender later calls `httpx.AsyncClient.post()` using the original hostname with no send‑time validation, IP pinning, or guarded transport. An attacker‑controlled hostname can resolve to a public IP during validation and later resolve to a loopback/private address (DNS rebinding), allowing SSRF to internal endpoints.
- **Affected Products:** PraisonAI Async Jobs API (Jobs webhook handling)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true - https://github.com/advisories/GHSA-rjvw-7vvw-549v
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply vendor patch; perform send‑time validation (re‑resolve hostname and check IPs at request time), implement IP allowlist/denylist, enforce IP pinning or use a guarded transport that prevents requests to loopback/private ranges, and restrict webhook hostnames to known safe domains. If patch unavailable, block outgoing requests to RFC1918, loopback, and link‑local addresses from the webhook sender and perform DNS resolution at send‑time.
- **Vendor Advisory:** https://github.com/advisories/GHSA-rjvw-7vvw-549v

---

## 5. 🟠 Zero-Day — PraisonAI: SpiderTools redirect-target SSRF protection bypass

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

- **Technical Details:** SpiderTools.scrape_page() validates initial URL (blocking loopback, private, link‑local, metadata, internal hostnames) but calls requests.Session.get() without disabling redirects or validating redirect Location targets. An attacker can supply a benign‑looking public URL that passes validation which then issues an HTTP redirect to a blocked internal target (e.g., 127.0.0.1 or 169.254.169.254); requests follows redirects by default and the final response body is parsed and returned, enabling SSRF and data exfiltration.
- **Affected Products:** PraisonAI SpiderTools (scrape_page)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Disable automatic redirects or validate redirect targets before following them; perform backend DNS resolution and block internal/private IP ranges; configure the HTTP client to forbid requests to loopback/link‑local/metadata IPs; apply the vendor patch/update.
- **Vendor Advisory:** https://github.com/advisories/GHSA-6h9p-93hq-q7h6

---

## 6. 🟠 Zero-Day — Docker MCP Gateway: Argument injection via OCI image label YAML

**CVE:** `CVE-2026-55887` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-r2xf-7jw5-pjg6>

> ## Summary

A maliciously crafted OCI image label can inject arbitrary arguments into the `docker run` command line constructed by the MCP Gateway. An attacker who controls an image that the victim references via `docker://`, or that the victim&#x27;s catalog pulls a snapshot from, can mount the host filesystem, run as UID 0, and execute arbitrary code on the host.
  
## Details

 The `io.docker.s…

**Parallel AI Enrichment:**

- **Technical Details:** An attacker can craft an OCI image label containing malicious YAML that populates fields like `command`, `volumes`, or `user` in the `catalog.Server` struct. Because the label is unmarshalled without validation, these fields are injected into the `docker run` command line built by the MCP Gateway, enabling arbitrary command execution on the host as root.
- **Affected Products:** Docker MCP Gateway (any version)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Do not pull or reference OCI images from untrusted sources. Implement validation of the `io.docker.server.metadata` label to reject unexpected fields. Use the `allowHosts`, `disableNetwork`, and `user` options to restrict container privileges and network exposure. Run the MCP Gateway with least‑privilege permissions and consider disabling the feature that processes arbitrary image labels until a patch is available.
- **Vendor Advisory:** https://github.com/advisories/GHSA-r2xf-7jw5-pjg6

---

## 7. 🟠 Zero-Day — Hostile states behind three-quarters of attacks on Britain's critical infrastructure, cyber chief warns

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Record by Recorded Future &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://therecord.media/britain-nation-state-cyberattacks-richard-horne-rusi>

> NCSC CEO Richard Horne warned that “kinetic targeting in any conflict tomorrow will be based on intelligence gathered today” and that nation-state adversaries were “prepositioning” throughout British critical infrastructure.

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Volt Typhoon; other threat actors: None known.
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — Microsoft Confirms RoguePlanet Defender Zero-Day, Says Patch is in Development

**CVE:** `CVE-2026-50656` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://thehackernews.com/2026/06/microsoft-confirms-rogueplanet-defender_02022423645.html>

> Microsoft has formally disclosed that it&#x27;s working to release a patch to address a Defender zero-day codenamed RoguePlanet.

The vulnerability has now been assigned the CVE identifier CVE-2026-50656 (CVSS score: 7.8), with the tech giant describing it as a privilege escalation flaw.

&quot;Microsoft is aware of an elevation of privilege in the Microsoft Malware Protection Engine in Microsoft …

**Parallel AI Enrichment:**

- **Technical Details:** A race condition in the Microsoft Malware Protection Engine allows a local unprivileged user to trigger a privilege‑escalation path that can spawn a SYSTEM shell on Windows 10 and Windows 11 systems with the June 2026 updates installed.
- **Affected Products:** Microsoft Defender (Microsoft Malware Protection Engine) on Windows 10 (June 2026 update), Windows 11 (June 2026 update)
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Enforce least‑privilege for local accounts, disable or restrict the ability of unprivileged users to mount ISO images, and monitor for unexpected process elevation or SYSTEM shells.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50656

---

## 9. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an AI system processes external content (webpages, documents, emails) that contains malicious instructions; when the AI reads this poisoned content it may silently follow the attacker's commands instead of the user's original intent.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Layered defenses and hardening: monitor and filter untrusted external content, use model/human-in-the-loop classification of suspicious content, apply least‑privilege for agent actions, continuous red‑teaming and vulnerability reward programs.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 10. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection occurs when untrusted external data or secondary tools (web content, notifications, extensions, plugins, connectors) include adversarial instructions that are consumed by an LLM or agentic automation and cause it to perform unintended actions; zero‑click variants (e.g., GeminiJack) exploit agentic browsing/automation to trigger malicious prompts without user interaction.
- **Affected Products:** Google Workspace with Gemini integrations (general multi‑source agentic LLM applications); precise versions unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Layered defenses — input provenance, strict source allowlists/deny‑lists, content sanitization and canonicalization, provenance‑aware instruction filtering, limiting agentic automation scope and capabilities, rate‑limiting and telemetry for anomalous behaviors, and rapid patching/coordination.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

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

## 17. 🟡 High Severity — Grav: Admin Backup Zip File Exposes Account Credentials and Configuration Secrets

**CVE:** `CVE-2026-55885` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-2f86-9cp8-6hcf>

> ### Summary
An authenticated administrator with backup permissions can download a ZIP archive containing the full Grav installation root, including `user/accounts/admin.yaml` with the admin&#x27;s bcrypt password hash and email, plus `user/config/` with all site configuration. The download endpoint requires only the session-static `admin-nonce` in the URL, no additional form-level CSRF token, and …

---

## 18. 🟡 High Severity — praisonaiagents: SSRF guard validates literal IPs only and never resolves DNS

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

## 19. 🟡 High Severity —  ZITADEL: Missing client_id binding in OIDC authorization code exchange and refresh token flows (RFC 6749 Section 4.1.3 violation)

**CVE:** `CVE-2026-55672` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-xqxv-4jc2-x56x>

> ### Summary

Zitadel&#x27;s OAuth2 / OIDC `CodeExchange` and `RefreshToken` implementations omit a critical validation step to ensure that the requesting client matches the client that originally initiated the authorization flow. This violates RFC 6749 Section 4.1.3, which mandates that the authorization server must ensure the authorization code was issued to the authenticated confidential client.…

---

## 20. 🟡 High Severity —  ZITADEL: Cross-Tenant User Leakage via Recycled Identifiers

**CVE:** `CVE-2026-55670` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-6x8v-2fq5-2229>

> ### Summary

A flaw in the user lifecycle enforcement allowed deleted users to retain their original organization/tenant association. Recreating a deleted user under a distinct organization can cause the new user instance to be incorrectly provisioned within the original organization if the previous ID would be used to recreate it.

### Impact

When a user is created, the system maps the generated…

---

## 21. 🟡 High Severity — Hydro: Insufficient session expiration when recreating sessions

**CVE:** `CVE-2026-55617` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-94jp-7776-qj6q>

> ### Impact

Hydro contains an insufficient session expiration vulnerability in its session recreation logic. When a session is recreated, including during logout or other session renewal flows, Hydro creates a new session token but does not delete the previous server-side session token.

As a result, an old sid cookie may remain valid even after the legitimate user logs out or the session is recre…

---

## 22. 🟡 High Severity — http-proxy-middleware: multipart/form-data field injection via unescaped CRLF in `fixRequestBody`

**CVE:** `CVE-2026-55603` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-gcq2-9pq2-cxqm>

> ## Summary
`fixRequestBody()` is the library&#x27;s documented helper for re-emitting a request body that was already consumed by a body parser. When the **outgoing** `Content-Type` is `multipart/form-data`, it rebuilds the body with `handlerFormDataBodyData()`, which interpolates each `req.body` key and value directly into the multipart wire format **without neutralizing CR/LF**:

```js
// dist/h…

---

## 23. 🟡 High Severity — piscina: Prototype Pollution Gadget → RCE via inherited options.filename

**CVE:** `CVE-2026-55388` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-x9g3-xrwr-cwfg>

> ## Summary

`piscina`&#x27;s constructor and `run()` paths read the `filename` option via plain member access:

```js
// dist/index.js line 92 (constructor)
const filename = options.filename
  ? (0, common_1.maybeFileURLToPath)(options.filename)
  : null;
this.options = { ...kDefaultOptions, ...options, filename, maxQueue: 0 };

// dist/index.js line 616 (run())
run(task, options = kDefaultRunOpti…

---

## 24. 🟡 High Severity — Gotenberg: SSRF via LibreOffice document processing

**CVE:** `CVE-2026-55229` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-2mrg-35hw-x3x9>

> **Summary**

 Server-Side Request Forgery (SSRF) vulnerability affecting the `/forms/libreoffice/convert` endpoint in Gotenberg v8.33.0 running with the default configuration.

By uploading a specially crafted DOCX document, an attacker can cause LibreOffice to automatically retrieve external resources during document conversion. As a result, outbound requests are made from the server hosting Gote…

---

## 25. 🟡 High Severity — Strimzi: Unrestricted access to all Secrets within namespace watched by the Topic operator

**CVE:** `CVE-2026-55226` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-r427-j2h7-wv3m>

> ### Impact

When only the Topic or only the User operators are deployed as part of the Entity Operator in the `Kafka` custom resource, the RBAC rights are not following the principle of least-privilege and the Entity Operator ServiceAccount still has access rights corresponding to both operators. That might allow the ServiceAccount to access `KafkaUser` custom resources and Secrets when the User o…

---

## 26. 🟡 High Severity — Strimzi: Cross-namespace privilege escalation via `Kafka.spec.entityOperator`

**CVE:** `CVE-2026-55225` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-mw9r-p8xp-wx96>

> ### Impact

Having the Topic and User operators to watch different namespaces than the one where the Kafka cluster is deployed, is a fully documented feature.

When the `watchedNamespace` field is used within the Topic or User operator (as part of the `Kafka.spec.entityOperator` field), the Cluster Operator creates a Role granting full CRUD on Secrets into the specified namespace. It also creates …

---

## 27. 🟡 High Severity —  ZITADEL: Server-Side Request Forgery (SSRF) and Denylist Bypass in Outgoing HTTP Components

**CVE:** `CVE-2026-55671` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-29jh-8cfq-rr8x>

> ### Summary

A Server-Side Request Forgery (SSRF) vulnerability was discovered in Zitadel affecting:

* **HTTP Notification Channels:** Used as an alternative to SMTP/Twilio configurations, sending payloads to user-defined URLs via HTTP POST webhooks.
* **OIDC BackChannel Logout:** Terminates sessions across different applications. When a session ends, the Zitadel server sends an HTTP POST request…

---

## 28. 🟡 High Severity — Oracle June 2026 Critical Security Patch Update Addresses 243 CVEs (CVE-2026-35273)

**CVE:** `CVE-2026-35273` &nbsp;|&nbsp; **Source:** Tenable Security Research &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://www.tenable.com/blog/oracle-june-2026-critical-security-patch-update-addresses-243-cves-cve-2026-35273>

> Oracle addresses 243 CVEs in its June 2026 Critical Security Patch Update with 245 patches, including 122 critical updates. Key Takeaways The June 2026 Critical Security Patch Update (CSPU) contains fixes for 243 unique CVEs in 245 security updates 122 issues (49.8% of all patches) were assigned a critical severity rating Oracle Fusion Middleware received the highest number of patches at 106, acco…

---

## 29. 🟡 High Severity — Avo: Missing Authorization in Avo Association Attach Endpoint Allows Unauthorized Relationship Manipulation and Privilege Escalation

**CVE:** `CVE-2026-55518` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-8fq9-273g-6mrg>

> ## Summary

A critical missing authorization flaw exists in Avo&#x27;s association attach workflow. The UI and `GET /resources/:resource/:id/:related/new` path can check `attach_&lt;association&gt;?`, but the actual write endpoint, `POST /resources/:resource/:id/:related`, does not run the same authorization check before mutating the association.

As a result, an authenticated low-privileged Avo u…

---

## 30. 🟡 High Severity — HAPI FHIR: XXE in XsltUtilities.saxonTransform via unhardened Saxon TransformerFactory

**CVE:** `CVE-2026-55471` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-2f55-g35j-5jmf>

> ### Summary

`org.hl7.fhir.utilities.XsltUtilities` exposes two parallel families of XSLT
transform helpers. The `transform(...)` overloads obtain their
`TransformerFactory` from the project&#x27;s hardened helper
`XMLUtil.newXXEProtectedTransformerFactory()` (which sets
`ACCESS_EXTERNAL_DTD=&quot;&quot;` and `ACCESS_EXTERNAL_STYLESHEET=&quot;&quot;`). The sibling
`saxonTransform(...)` overloads i…

---

## 31. 🟡 High Severity — LangChain4j: SQL injection via metadata filters in langchain4j-mariadb and langchain4j-pgvector

**CVE:** `CVE-2026-55405` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-2mfg-cc43-9pcj>

> ### Summary
The MariaDB and pgvector embedding stores build metadata-filter SQL by string-concatenating
filter **keys** (and, in MariaDB, string **values**) directly into the query without adequate
escaping. A crafted metadata key in `EmbeddingSearchRequest.filter()` can break out of its SQL
context and inject arbitrary SQL into the statements executed by the stores&#x27; search and
`removeAll(Fil…

---

## 32. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
