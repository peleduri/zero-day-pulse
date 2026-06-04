# Zero Day Pulse

> **Generated:** 2026-06-04 19:55 UTC &nbsp;|&nbsp; **Total:** 35 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 9 &nbsp;|&nbsp; 🟡 High: 26 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Multiple path traversal vulnerabilities in SimpleHelp 5.5.7 and earlier enable unauthenticated remote attackers to retrieve logs, configuration files, and credentials via crafted file path inputs.
- **Affected Products:** SimpleHelp Remote Support Software version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Upgrade to SimpleHelp version 5.5.8 or later, which includes patches for CVE-2024-57727 and related issues.
- **Vendor Advisory:** http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when adversarial content on the web (e.g., pages, metadata, or other documents) supplies malicious instructions that AI agents incorporate into their prompt context during browsing or retrieval, causing the agent to follow adversary-supplied instructions or leak sensitive data. Attack vectors include poisoned web pages, crafted search results, and manipulated third‑party content fetched by agents.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply strict browsing/source whitelisting for agents, avoid auto-executing web content, implement prompt provenance/trust checks, input/output sanitization, use model-level instruction filtering and operator review for high-risk tasks.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when an attacker injects malicious instructions into external data sources or tools that an LLM‑powered system consumes during query processing, causing the model or agentic automation to follow the injected instructions even without direct user input. Attack vectors include data, third‑party tools, or web content that the system ingests; mitigations rely on layered defenses and limiting trust in external inputs.
- **Affected Products:** Google Workspace (features integrating Gemini / GenAI agents)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Multi‑layered defenses described by Google: input provenance and filtering, model instruction‑safety layers, signals‑based detection, continuous monitoring, developer/operator hardening and careful design of tool/data access.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Insufficient policy enforcement in the <webview> tag allowed a malicious extension that a user installs to inject scripts/HTML into a privileged browser UI (Gemini Live side panel), enabling code execution in the panel context and potential abuse of panel-level capabilities (local file access, screenshots, camera/mic, phishing via trusted UI).
- **Affected Products:** Google Chrome prior to 143.0.7499.192 (desktop, Linux, Android); Extended Stable prior to 142.0.7444.265
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply vendor patch (update Chrome to 143.0.7499.192+ or fixed Extended Stable build); enforce extension allowlisting and reduce extension permissions; disable/hide Gemini if not needed; monitor for PoC and remove untrusted extensions.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** The blog provides high‑level technical context about reducing memory‑safety vulnerabilities by adopting Rust in Android and shifting new‑code focus to memory‑safe languages; it does not describe a single vulnerability mechanism or exploit vector.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Use memory‑safe languages (Rust, Java/Kotlin), apply Android Security Bulletin fixes, follow Android memory‑safety guidance (hardening and testing).
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injections hide malicious commands in external content (emails, docs, calendar invites) that are later fed to generative AI models, causing the model to execute unintended actions like data exfiltration or rogue commands.
- **Affected Products:** Google Gemini 2.5, Google Workspace
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Deploy prompt‑injection content classifiers; enable markdown sanitization and suspicious URL redaction; implement user confirmation prompts for risky actions; provide end‑user mitigation notifications; train models with adversarial data to improve resilience.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors target large backbone routers, provider edge (PE) and customer edge (CE) routers, modify router firmware/configuration to maintain persistent, long‑term access, and pivot via compromised devices and trusted connections.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon (also reported as OPERATOR PANDA, RedMike, UNC5807, GhostEmperor)
- **Mitigation:** Follow CISA advisory mitigations — inventory and segment critical network devices, restrict management interfaces, apply vendor patches where available, rotate credentials, monitor for anomalous router config changes and command execution, implement least‑privilege and multi‑factor authentication, and apply network detection and response monitoring.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** true
- **Threat Actors:** GRU 85th Main Special Service Center (85th GTsSS), military unit 26165 (APT28)
- **Mitigation:** Implement hardening measures recommended by CISA/FBI/NCA: network segmentation, enable multi‑factor authentication, enforce credential hygiene, increase monitoring of privileged accounts, and develop incident‑response playbooks.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟠 Zero-Day — Shopware: Stored XSS via SVG file upload — no SVG sanitization

**CVE:** `CVE-2026-48015` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-xvhc-gm7j-mhmc>

> SVG files are in the `allowed_extensions` whitelist and can be uploaded by any admin user via the media manager. There is zero SVG content sanitization anywhere in the upload pipeline. A malicious SVG with JavaScript (`onload`, `&lt;script&gt;`, `&lt;foreignObject&gt;`) executes in the context of the Shopware domain when accessed.

## The Problem

In `src/Core/Framework/Resources/config/packages/s…

**Parallel AI Enrichment:**

- **Technical Details:** SVG files are whitelisted in allowed_extensions; admin users can upload SVGs via the media manager with no SVG content sanitization. Malicious SVGs (onload, <script>, <foreignObject>) can execute JavaScript in the Shopware domain when accessed, resulting in stored XSS.
- **Affected Products:** Shopware (unspecified 6.x versions)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — https://github.com/advisories/GHSA-xvhc-gm7j-mhmc
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Disable SVG uploads (remove "svg" from allowed_extensions), restrict who can upload media to trusted admins, serve uploaded SVGs from a different domain or via Content-Disposition/Content-Type forcing download, implement SVG sanitization (e.g., remove scripts, on* attributes, foreignObject) before serving.
- **Vendor Advisory:** https://github.com/advisories/GHSA-xvhc-gm7j-mhmc

---

## 10. 🟡 High Severity — AdGuard Home: DoQ-to-UDP State Reduction and Source-Port Oracle

**CVE:** `CVE-2026-47703` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-xgx4-4h9w-53pv>

> ## Summary

This report covers the client-triggered DoQ forwarding path in:

- `dnsproxy` `v0.81.2` (`adguard/dnsproxy:v0.81.2`)
- `AdGuard Home` `v0.107.74` (`adguard/adguardhome:latest`, image version label `v0.107.74`)

The issue was reproduced on `2026-04-25` with the products configured through
their documented DoQ listener and plain UDP upstream surfaces. The scope is the
internal backend UD…

**Parallel AI Enrichment:**

- **Technical Details:** DoQ-to-UDP forwarding does not preserve the original DNS request ID, enabling a source‑port oracle that can be exploited to reduce entropy and guess DNS transaction identifiers.
- **Affected Products:** AdGuard Home v0.107.74, dnsproxy v0.81.2
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (https://github.com/adguardteam/adguardhome/releases)
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Update AdGuard Home to the latest version (v0.107.74 or later) which includes the fix for GHSA‑xgx4‑4h9w‑53pv.
- **Vendor Advisory:** https://github.com/AdguardTeam/AdGuardHome/security/advisories/GHSA-xgx4-4h9w-53pv

---

## 11. 🟡 High Severity — Shopware: SSRF in Media External-Link Endpoint Bypasses IP Validation

**CVE:** `CVE-2026-48013` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-gq96-5pfx-f4vc>

> ## Summary

The `/api/_action/media/external-link` endpoint allows authenticated admin users to make server-side HTTP HEAD requests to arbitrary internal IP addresses. While the parallel `uploadFromURL` flow validates target IPs against private/reserved ranges via `FileUrlValidator`, the `linkURL` flow only performs a URL format check (regex for `http://` or `https://` prefix), allowing SSRF to in…

---

## 12. 🟡 High Severity — Shopware: Admin API ACL Bypass in Order State Transition Endpoints

**CVE:** `CVE-2026-48014` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-f8q6-3g5w-jjr6>

> ## Summary
This is a vertical authorization bypass in the Admin API affecting order state transition features (`/api/_action/order/{orderId}/state/{transition}` and similar transaction/delivery transition routes). The root cause is that the transition action routes do not declare required server-side ACL privileges, allowing low-privileged users to pass the authorization boundary. As a result, aut…

---

## 13. 🟡 High Severity — Shopware: Privilege escalation: non-admin user with user:create ACL can create admin accounts

**CVE:** `CVE-2026-48010` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-v39m-97p8-gqg7>

> `UserController::upsertUser()` writes user data in `SYSTEM_SCOPE` and does not filter the `admin` field. A non-admin API user with `user:create` or `user:update` ACL permission can set `admin: true` on new or existing users, escalating to full admin access.

## The Problem

In `src/Core/Framework/Api/Controller/UserController.php`, line 210-234:

```php
public function upsertUser(?string $userId, …

---

## 14. 🟡 High Severity — Shopware: Admin Account Takeover via User Recovery Hash Exposure

**CVE:** `CVE-2026-48009` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-8v9p-g828-v98f>

> ## Summary

A low-privilege admin user with `user_recovery:read` ACL can take over any admin account. The attacker triggers password recovery for the victim (unauthenticated endpoint), reads the recovery hash from the Admin API search endpoint, then uses the hash to reset the victim&#x27;s password (another unauthenticated endpoint). The recovery hash — intended to be secret and delivered only via…

---

## 15. 🟡 High Severity — Shopware: Privilege Escalation via Sync API Integration Admin Flag Bypass

**CVE:** `CVE-2026-48008` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-gv8p-48fr-4fxg>

> ## Summary

A non-admin API user with `integration:create` ACL privilege can escalate to full administrator by creating an integration with `admin: true` through the Sync API (`POST /api/_action/sync`). The regular integration endpoint (`POST /api/integration`) correctly blocks this, but the Sync API bypasses the controller-level check by writing directly through the DAL EntityWriter. The `integra…

---

## 16. 🟡 High Severity — Hono: JWT middleware accepts any Authorization scheme, not only Bearer

**CVE:** `CVE-2026-47673` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-f577-qrjj-4474>

> ### Summary

The `jwt` and `jwk` middlewares do not verify that the `Authorization` header value uses the`Bearer` scheme. Any two-part header value — regardless of the scheme name in the first position — proceeds to JWT verification. A request presenting a valid JWT under a non-`Bearer` scheme identifier (such as `Basic` or `Token`) is authenticated identically to a correctly formed `Bearer` reque…

---

## 17. 🟡 High Severity — epa4all-client: Unauthenticated REST API for Patient Record Writes

**CVE:** `CVE-2026-47672` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-c82x-f4xr-qv33>

> ### Impact
Any network-reachable caller can write arbitrary documents to any patient&#x27;s electronic
health record accessible by the institution&#x27;s SMC-B card. In a misconfigured deployment
(e.g., following the production Docker example in the README), this is exploitable from
the local network without credentials.

### Patches
- [#43](https://github.com/oviva-ag/epa4all-client/pull/43)

###…

---

## 18. 🟡 High Severity — Nhost CLI local configserver allows cross-origin unauthenticated read/write access to local development configuration and secrets

**CVE:** `CVE-2026-47671` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-64cj-qvx5-m4f3>

> ### Summary

The hidden `nhost configserver` used by `nhost dev` exposes the Mimir GraphQL API with dummy authorization directives and permissive CORS. When a developer is running the local development environment, any process that can reach the developer&#x27;s localhost service, including a web page loaded from an arbitrary origin, can query the configserver for local Nhost configuration and sec…

---

## 19. 🟡 High Severity — Nuclio: Missing authorization on project write paths allows any authenticated user to modify or delete any project

**CVE:** `CVE-2026-45730` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-m8xg-8xg9-mxhm>

> This vulnerability exists in Nuclio Dashboard&#x27;s project management API, allowing any authenticated user (without membership in the target project) to bypass OPA authorization checks on write paths (`PUT /api/projects/{id}`, `DELETE /api/projects`) and modify or delete any project along with all its associated resources (functions, API gateways, etc.). CWE classification: CWE-862 (Missing Auth…

---

## 20. 🟡 High Severity — Matrix Rust SDK: Sender-binding gaps in to-device and room-key attribution

**CVE:** `CVE-2026-45056` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-wfq4-36m3-9g42>

> ### Impact

The `matrix-sdk-crypto` crate before 0.16.1 is missing a check for the sender&#x27;s user ID when decrypting an Olm-encrypted to-device message containing the `sender_device_keys` property.

This could be exploited to spoof the sender of an encrypted to-device message, but only if the attacker colludes with (or is) the homeserver operator.

### Patches

This issue is fixed in `matrix-s…

---

## 21. 🟡 High Severity — Doorkeeper Openid Connect: Dynamic Client Registration feature creates public clients with client_secret

**CVE:** `CVE-2026-44476` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-m6vc-f87m-cc2h>

> ### Impact

The `DynamicClientRegistrationController#register` action hard-codes `confidential: false` when creating applications (dynamic_client_registration_controller.rb:18-25), yet the response includes a client_secret and advertises `token_endpoint_auth_methods_supported: [&quot;client_secret_basic&quot;, &quot;client_secret_post&quot;]`.

Because Doorkeeper&#x27;s `Application.by_uid_and_sec…

---

## 22. 🟡 High Severity — Axios: Proxy-Authorization Credential Leak to Origin Server Across HTTP-to-HTTPS Redirect in Axios Node.js HTTP Adapter

**CVE:** `CVE-2026-44487` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-p92q-9vqr-4j8v>

> ## Summary

Axios’s Node.js HTTP adapter may forward a `Proxy-Authorization` header to a redirected origin during specific proxy-to-direct redirect flows.

This affects Node.js usage, where an initial HTTP request is sent through an authenticated HTTP proxy, redirects are followed, and the redirected URL is no longer proxied. Under affected redirect shapes, the final origin can receive the proxy c…

---

## 23. 🟡 High Severity — Axios: Proxy-Authorization header leaks to redirect target when proxy is re-evaluated to direct connection

**CVE:** `CVE-2026-44486` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-j5f8-grm9-p9fc>

> ### Summary

Axios’ Node.js HTTP adapter can leak proxy credentials to a redirect target in affected versions. When a request is sent through an authenticated proxy, Axios may add a `Proxy-Authorization` header. If Axios then follows a redirect and the redirected request is no longer sent through that proxy, the stale `Proxy-Authorization` header can remain on the redirected request and be sent to…

---

## 24. 🟡 High Severity — browserstack-runner vulnerable to Remote Code Execution via vm sandbox escape in _log HTTP handler

**CVE:** `CVE-2026-49143` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-6vr3-7wcx-v5g5>

> ### Summary

The HTTP handler `/_log` in `lib/server.js` (lines 491–515) of browserstack-runner passes unauthenticated user-supplied data to `vm.runInNewContext()` combined with `eval()`, enabling a sandbox escape and arbitrary code execution on the host system.

### Details

When `browserstack-runner` starts, it creates an HTTP server on port 8888 (configurable) that listens on all network interf…

---

## 25. 🟡 High Severity — Jupyter Enterprise Gateway: Kubernetes Manifest Injection in Jinja2 Template Rendering

**CVE:** `CVE-2026-44182` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-cfw7-6c5v-2wjq>

> ### Summary

The environment variables used during the rendering of the Kubernetes manifest allow YAML injection, enabling attackers to overwrite existing keys like `securityContext` and inject multi-document YAML to create additional unintended Kubernetes resources.

### Details

The server interpolates untrusted environment variables (e.g., `KERNEL_XXX`) into Kubernetes manifests without YAML-aw…

---

## 26. 🟡 High Severity — Jupyter Enterprise Gateway: Jinja2 Template Server Side Template Injection resulting in Remote Code Execution

**CVE:** `CVE-2026-44181` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-f49j-v924-fx9w>

> ### Summary

The environment variables (`KERNEL_XXX`) used during the rendering of the Kubernetes manifest are vulnerable to Server Side Template Injection (SSTI).
By including Jinja2 template expressions it is possible to execution Python code and OS Commands in the Enterprise Gateway service.
The code can use or steal the Kubernetes service account token, which can steal Kubernetes secrets and b…

---

## 27. 🟡 High Severity — Jupyter Enterprise Gateway: ContainerProcessProxy._enforce_prohibited_ids Bypass

**CVE:** `CVE-2026-44180` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-chq7-94j8-cj28>

> ### Summary

Jupyter Enterprise Gateway has a prohibited UID and GID feature that by default prevents launching kernels with UID or GID 0 (root).
This can be bypassed. It is possible to launch kernels with a prohibited UID and/or GID by using a specially crafted `KERNEL_UID` or `KERNEL_GID` value.

The feature is described in the documentation: 

https://github.com/jupyter-server/enterprise_gatewa…

---

## 28. 🟡 High Severity — Docling Core: Unsafe remote filename resolution

**CVE:** `CVE-2026-44023` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-jmmv-h3mp-59v8>

> ### Impact
In versions `&gt;= 1.5.0, &lt; 2.74.1`, `docling-core` did not sufficiently restrict remote request destinations and could resolve a server-provided `Content-Disposition` to a local path in an unsafe manner.

In applications that accept untrusted URLs, this could allow SSRF attacks targeting local files outside the user-defined cache directory.

### Patches
Patched in `docling-core` `2.…

---

## 29. 🟡 High Severity — Docling: Unsafe URI and Path Handling in HTML Backend

**CVE:** `CVE-2026-47214` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-q29v-xc37-wh5m>

> ### Impact
The HTML backend did not perform sufficient validation during resource handling:
- Accepted `file://` URIs enabling local file system access when `enable_local_fetch=True`
- Path resolution allowed traversal outside intended directories via `../` sequences and absolute paths
- Did not block internal network resources under `enable_remote_fetch=True`
- HTTP redirects were not validated, …

---

## 30. 🟡 High Severity — Docling: Unsafe XML Entity Expansion in USPTO Patent Backend

**CVE:** `CVE-2026-44020` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-m88r-rg27-5xfg>

> ### Impact
The USPTO patent XML parser used the standard `xml.sax.parseString()` without protection against XML External Entity (XXE) attacks. An attacker could craft malicious USPTO patent XML files with external entity references that could:
- Read arbitrary files from the server filesystem
- Perform Server-Side Request Forgery (SSRF) attacks
- Cause denial of service through entity expansion (B…

---

## 31. 🟡 High Severity — Docling: Unsafe Archive Extraction and XML Parsing in METS-GBS Backend

**CVE:** `CVE-2026-44018` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-r3xg-rg9j-67fv>

> ### Impact
The METS-GBS backend&#x27;s XML parsing and the input document format detection lacked security controls, enabling:
- XML External Entity (XXE) attacks to read local files or cause denial of service
- Decompression bombs (zip bombs) to exhaust memory and disk space
- Unbounded archive extraction consuming system resources

An attacker could craft malicious METS-GBS archives that, when p…

---

## 32. 🟡 High Severity — Docling: Unsafe Playwright-based HTML Rendering

**CVE:** `CVE-2026-44016` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-pj2v-ggqh-cmq2>

> ### Impact
In versions `&gt;= 2.82.0, &lt; 2.91.0`, if the HTML backend was explicitly configured for rendering (rendering option by default deactivated), then the Playwright-based rendering feature could allow JavaScript execution and unrestricted network access when processing untrusted HTML documents. An attacker could craft malicious HTML that executes arbitrary JavaScript in the rendering con…

---

## 33. 🟡 High Severity — backpack/crud is vulnerable to Cross-Site Scripting (XSS)

**CVE:** `CVE-2022-31114` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-m8xx-3x29-84h8>

> ### Impact

It’s a “*moderate*” vulnerability… but being an admin panel, take this seriously. It’s difficult… but an attacker could conduct a targeted phishing campaign, in order to **trick your users or admins to click a malicious link, which under very specific circumstances could give them information... or even admin access**. It’s *unlikely*, but that’s not good enough in admin panels - It sh…

---

## 34. 🟡 High Severity — Docling: Unsafe Zip Extraction in EasyOCR Model Download

**CVE:** `CVE-2026-44017` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-cjqg-rq2h-2fvj>

> ### Impact
In versions `&lt; 2.91.0`, The EasyOCR model download functionality extracted ZIP archives without validating member paths, enabling Zip Slip attacks. If an attacker could compromise the model download source (via supply chain attack, DNS spoofing, or MITM), they could write arbitrary files to any location writable by the process, potentially achieving:
- Remote code execution by overwr…

---

## 35. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
