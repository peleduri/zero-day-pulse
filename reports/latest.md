# Zero Day Pulse

> **Generated:** 2026-06-05 02:08 UTC &nbsp;|&nbsp; **Total:** 25 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 15 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal / directory traversal vulnerabilities in SimpleHelp 5.5.7 and earlier allow unauthenticated attackers to retrieve logs, configuration files, and credentials, enabling downstream access to customer environments.
- **Affected Products:** SimpleHelp Remote Support / Remote Monitoring and Management (RMM) v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (unspecified); DragonForce ransomware group
- **Mitigation:** Upgrade SimpleHelp to v5.5.8 or later immediately; if patching is not possible, isolate/unpublish SimpleHelp instances from the internet, restrict access via network controls (IP allowlists, VPN), rotate potentially exposed credentials, and review logs and downstream customer access.
- **Vendor Advisory:** http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — The June 2026 AI Executive Order: What federal agencies need to know and how Tenable can help

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Tenable Security Research &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://www.tenable.com/blog/summary-june-2026-ai-executive-order-requirements>

> On June 2, 2026, the White House signed an Executive Order directing federal agencies to harden their systems with AI-enabled cyber defenses and to stand up a new AI cybersecurity clearinghouse — most of it on a 30-day clock. Here’s what the EO requires and how Tenable can help. Key takeaways: The new AI Security Executive Order will require national security and civilian federal agencies to prior…

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
- **Vendor Advisory:** https://www.tenable.com/blog/summary-june-2026-ai-executive-order-requirements

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** IPI occurs when an AI system processes external content (e.g., websites, emails, documents) that contains hidden malicious instructions—often placed in HTML comments, invisible CSS, or metadata. These instructions override the model’s context (e.g., using phrases like "Ignore previous instructions"), causing the AI to execute attacker‑desired actions such as API calls, payment authorizations, or file deletions.
- **Affected Products:** Google Antigravity IDE (patched 2026-02-28), production AI agents that ingest untrusted web content
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Run quarterly IPI red‑team exercises, incorporate Forcepoint’s documented payload categories into test suites, and enforce strict segmentation so that crawled web content cannot authorize API calls, payments, or credential access without out‑of‑band confirmation. Google also recommends hardening models and participating in the AI Vulnerability Reward Program.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) injects malicious instructions into the data sources, tools, or context that an LLM uses to generate responses, enabling an attacker to manipulate the model’s behavior without direct user interaction.
- **Affected Products:** Google Workspace (Gemini integration)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Implement Google’s layered defense strategy: continuously monitor inputs, enforce strict data sanitization, apply policy controls for tool usage, and use runtime checks to detect anomalous LLM behavior.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Insufficient policy enforcement in the WebView tag used by Chrome’s Gemini/agentic features allows an attacker to bypass origin checks and gain local file access through indirect prompt‑injection style vectors.
- **Affected Products:** Google Chrome prior to 143.0.7499.192
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true – https://unit42.paloaltonetworks.com/gemini-live-in-chrome-hijacking/
- **Patch Available:** true – http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Update Chrome to version 143.0.7499.192 or later. Follow Google’s guidance: restrict origin access, block indirect prompt injections, use content restrictions, and disable agentic/Gemini features until the patch is applied.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

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

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injections (IPI) embed hidden malicious instructions in external data sources (emails, documents, calendar invites) to manipulate AI agents. Google mitigates IPI via adversarially trained models (Gemini 2.5), dedicated ML classifiers that detect malicious instructions, security thought reinforcement to keep LLMs task‑focused, markdown sanitization to prevent external image‑based exfiltration, suspicious‑URL redaction using Safe Browsing, and a user confirmation framework requiring explicit confirmation for risky actions.
- **Affected Products:** Gemini (Google Workspace, Gemini app) version 2.5
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Layered defenses including model hardening (Gemini 2.5), prompt‑injection content classifiers, security thought reinforcement, markdown sanitization and suspicious URL redaction, user confirmation (HITL) framework, end‑user mitigation notifications, Safe Browsing URL checks, adversarial training, red‑teaming and VRP engagement.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors compromise and modify routers and network devices to maintain persistent, long‑term access, leveraging compromised devices and trusted connections to pivot across networks; they focus on router firmware/OS modifications and abuse of management interfaces.
- **Affected Products:** Large backbone routers, provider edge (PE) routers, customer edge (CE) routers, compromised IoT and router devices
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Follow CISA/NSA mitigations: inventory and isolate affected network devices, update device firmware per vendor guidance, change default credentials, restrict management access (ACLs, VPN/MFA), monitor for indicators of compromise (IOCs), segment networks, and apply vendor‑specific hardening per advisory.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

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
- **Threat Actors:** Russian GRU 85th GTsSS (Unit 26165) — tracked as APT28 and affiliated GRU actors
- **Mitigation:** Implement network segmentation, multifactor authentication (MFA), enhanced logging and monitoring, patch management, restrict remote access, apply vendor and threat intelligence indicators of compromise (IOCs) from advisory; follow CISA/NSA guidance
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — Shopware: Stored XSS via SVG file upload — no SVG sanitization

**CVE:** `CVE-2026-48015` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-xvhc-gm7j-mhmc>

> SVG files are in the `allowed_extensions` whitelist and can be uploaded by any admin user via the media manager. There is zero SVG content sanitization anywhere in the upload pipeline. A malicious SVG with JavaScript (`onload`, `&lt;script&gt;`, `&lt;foreignObject&gt;`) executes in the context of the Shopware domain when accessed.

## The Problem

In `src/Core/Framework/Resources/config/packages/s…

**Parallel AI Enrichment:**

- **Technical Details:** Shopware's media manager permits SVG uploads via the allowed_extensions whitelist. Because SVG content is not sanitized, a crafted SVG containing onload, <script>, or <foreignObject> elements can execute arbitrary JavaScript in the context of the Shopware domain when the file is accessed.
- **Affected Products:** Shopware 6 (versions prior to 6.7.10.1)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Upgrade to Shopware version 6.7.10.1 or later, which includes a fix for the SVG XSS issue. If upgrading is not immediately possible, disable SVG uploads or remove SVG from the allowed_extensions whitelist to prevent the vulnerability.
- **Vendor Advisory:** https://github.com/advisories/GHSA-xvhc-gm7j-mhmc

---

## 11. 🟡 High Severity — AdGuard Home: DoQ-to-UDP State Reduction and Source-Port Oracle

**CVE:** `CVE-2026-47703` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-xgx4-4h9w-53pv>

> ## Summary

This report covers the client-triggered DoQ forwarding path in:

- `dnsproxy` `v0.81.2` (`adguard/dnsproxy:v0.81.2`)
- `AdGuard Home` `v0.107.74` (`adguard/adguardhome:latest`, image version label `v0.107.74`)

The issue was reproduced on `2026-04-25` with the products configured through
their documented DoQ listener and plain UDP upstream surfaces. The scope is the
internal backend UD…

---

## 12. 🟡 High Severity — Shopware: SSRF in Media External-Link Endpoint Bypasses IP Validation

**CVE:** `CVE-2026-48013` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-gq96-5pfx-f4vc>

> ## Summary

The `/api/_action/media/external-link` endpoint allows authenticated admin users to make server-side HTTP HEAD requests to arbitrary internal IP addresses. While the parallel `uploadFromURL` flow validates target IPs against private/reserved ranges via `FileUrlValidator`, the `linkURL` flow only performs a URL format check (regex for `http://` or `https://` prefix), allowing SSRF to in…

---

## 13. 🟡 High Severity — Shopware: Admin API ACL Bypass in Order State Transition Endpoints

**CVE:** `CVE-2026-48014` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-f8q6-3g5w-jjr6>

> ## Summary
This is a vertical authorization bypass in the Admin API affecting order state transition features (`/api/_action/order/{orderId}/state/{transition}` and similar transaction/delivery transition routes). The root cause is that the transition action routes do not declare required server-side ACL privileges, allowing low-privileged users to pass the authorization boundary. As a result, aut…

---

## 14. 🟡 High Severity — Shopware: Privilege escalation: non-admin user with user:create ACL can create admin accounts

**CVE:** `CVE-2026-48010` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-v39m-97p8-gqg7>

> `UserController::upsertUser()` writes user data in `SYSTEM_SCOPE` and does not filter the `admin` field. A non-admin API user with `user:create` or `user:update` ACL permission can set `admin: true` on new or existing users, escalating to full admin access.

## The Problem

In `src/Core/Framework/Api/Controller/UserController.php`, line 210-234:

```php
public function upsertUser(?string $userId, …

---

## 15. 🟡 High Severity — Shopware: Admin Account Takeover via User Recovery Hash Exposure

**CVE:** `CVE-2026-48009` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-8v9p-g828-v98f>

> ## Summary

A low-privilege admin user with `user_recovery:read` ACL can take over any admin account. The attacker triggers password recovery for the victim (unauthenticated endpoint), reads the recovery hash from the Admin API search endpoint, then uses the hash to reset the victim&#x27;s password (another unauthenticated endpoint). The recovery hash — intended to be secret and delivered only via…

---

## 16. 🟡 High Severity — Shopware: Privilege Escalation via Sync API Integration Admin Flag Bypass

**CVE:** `CVE-2026-48008` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-gv8p-48fr-4fxg>

> ## Summary

A non-admin API user with `integration:create` ACL privilege can escalate to full administrator by creating an integration with `admin: true` through the Sync API (`POST /api/_action/sync`). The regular integration endpoint (`POST /api/integration`) correctly blocks this, but the Sync API bypasses the controller-level check by writing directly through the DAL EntityWriter. The `integra…

---

## 17. 🟡 High Severity — Hono: JWT middleware accepts any Authorization scheme, not only Bearer

**CVE:** `CVE-2026-47673` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-f577-qrjj-4474>

> ### Summary

The `jwt` and `jwk` middlewares do not verify that the `Authorization` header value uses the`Bearer` scheme. Any two-part header value — regardless of the scheme name in the first position — proceeds to JWT verification. A request presenting a valid JWT under a non-`Bearer` scheme identifier (such as `Basic` or `Token`) is authenticated identically to a correctly formed `Bearer` reque…

---

## 18. 🟡 High Severity — epa4all-client: Unauthenticated REST API for Patient Record Writes

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

## 19. 🟡 High Severity — Nhost CLI local configserver allows cross-origin unauthenticated read/write access to local development configuration and secrets

**CVE:** `CVE-2026-47671` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-64cj-qvx5-m4f3>

> ### Summary

The hidden `nhost configserver` used by `nhost dev` exposes the Mimir GraphQL API with dummy authorization directives and permissive CORS. When a developer is running the local development environment, any process that can reach the developer&#x27;s localhost service, including a web page loaded from an arbitrary origin, can query the configserver for local Nhost configuration and sec…

---

## 20. 🟡 High Severity — Nuclio: Missing authorization on project write paths allows any authenticated user to modify or delete any project

**CVE:** `CVE-2026-45730` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-m8xg-8xg9-mxhm>

> This vulnerability exists in Nuclio Dashboard&#x27;s project management API, allowing any authenticated user (without membership in the target project) to bypass OPA authorization checks on write paths (`PUT /api/projects/{id}`, `DELETE /api/projects`) and modify or delete any project along with all its associated resources (functions, API gateways, etc.). CWE classification: CWE-862 (Missing Auth…

---

## 21. 🟡 High Severity — Matrix Rust SDK: Sender-binding gaps in to-device and room-key attribution

**CVE:** `CVE-2026-45056` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-wfq4-36m3-9g42>

> ### Impact

The `matrix-sdk-crypto` crate before 0.16.1 is missing a check for the sender&#x27;s user ID when decrypting an Olm-encrypted to-device message containing the `sender_device_keys` property.

This could be exploited to spoof the sender of an encrypted to-device message, but only if the attacker colludes with (or is) the homeserver operator.

### Patches

This issue is fixed in `matrix-s…

---

## 22. 🟡 High Severity — Doorkeeper Openid Connect: Dynamic Client Registration feature creates public clients with client_secret

**CVE:** `CVE-2026-44476` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-m6vc-f87m-cc2h>

> ### Impact

The `DynamicClientRegistrationController#register` action hard-codes `confidential: false` when creating applications (dynamic_client_registration_controller.rb:18-25), yet the response includes a client_secret and advertises `token_endpoint_auth_methods_supported: [&quot;client_secret_basic&quot;, &quot;client_secret_post&quot;]`.

Because Doorkeeper&#x27;s `Application.by_uid_and_sec…

---

## 23. 🟡 High Severity — Axios: Proxy-Authorization Credential Leak to Origin Server Across HTTP-to-HTTPS Redirect in Axios Node.js HTTP Adapter

**CVE:** `CVE-2026-44487` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-p92q-9vqr-4j8v>

> ## Summary

Axios’s Node.js HTTP adapter may forward a `Proxy-Authorization` header to a redirected origin during specific proxy-to-direct redirect flows.

This affects Node.js usage, where an initial HTTP request is sent through an authenticated HTTP proxy, redirects are followed, and the redirected URL is no longer proxied. Under affected redirect shapes, the final origin can receive the proxy c…

---

## 24. 🟡 High Severity — Axios: Proxy-Authorization header leaks to redirect target when proxy is re-evaluated to direct connection

**CVE:** `CVE-2026-44486` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-j5f8-grm9-p9fc>

> ### Summary

Axios’ Node.js HTTP adapter can leak proxy credentials to a redirect target in affected versions. When a request is sent through an authenticated proxy, Axios may add a `Proxy-Authorization` header. If Axios then follows a redirect and the redirected request is no longer sent through that proxy, the stale `Proxy-Authorization` header can remain on the redirected request and be sent to…

---

## 25. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
