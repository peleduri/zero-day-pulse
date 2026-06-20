# Zero Day Pulse

> **Generated:** 2026-06-20 02:07 UTC &nbsp;|&nbsp; **Total:** 34 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 11 &nbsp;|&nbsp; 🟡 High: 23 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal / directory traversal vulnerability allowing unauthenticated attackers to read sensitive files on affected SimpleHelp servers via crafted requests that traverse directories.
- **Affected Products:** SimpleHelp remote support / Remote Monitoring and Management (RMM) — versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true - https://www.offsec.com/blog/cve-2024-57727/
- **Patch Available:** true - https://www.broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability
- **Active Exploitation:** true - https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a
- **Threat Actors:** Ransomware actors (unspecified)
- **Mitigation:** Apply vendor updates/patch to latest SimpleHelp; if unable, restrict network access to SimpleHelp services, implement firewall rules to block external access, and monitor logs for suspicious file access.
- **Vendor Advisory:** https://www.broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — In Other News: Apple Patches Beats Eavesdropping Flaw, DOT Closes Delta CrowdStrike Probe, AWS Continuum

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://www.securityweek.com/in-other-news-apple-patches-beats-eavesdropping-flaw-dot-closes-delta-crowdstrike-probe-aws-continuum/>

> Other noteworthy stories that might have slipped under the radar: Android TV botnet Popa linked to Israeli firm, Velvet Ant maintained decade-long stealth, unpatched GCP Config Connector flaw enables takeover. The post In Other News: Apple Patches Beats Eavesdropping Flaw, DOT Closes Delta CrowdStrike Probe, AWS Continuum appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Apple Beats Studio Buds: Unauthenticated Bluetooth/firmware flaw allows a nearby attacker to capture microphone audio from unpaired devices seeking pairing. Popa Android TV botnet: Malicious SDK embedded in apps turns devices into persistent residential proxies for traffic forwarding and scraping. Velvet Ant: Actor chains internet‑facing footholds with backdoored PAM/OpenSSH and Nginx/FastCGI proxies, deploying GS‑Netcat and SOCKS5 to steal credentials in air‑gapped networks. GCP Config Connector: Confused‑deputy authorization bypass lets any Kubernetes namespace user submit a malicious IAMPolicyMember, escalating to GCP Organization Owner.
- **Affected Products:** Beats Studio Buds (firmware prior to 1B211); Android TV boxes/streaming devices with malicious SDK; Air‑gapped network authentication components (backdoored PAM/OpenSSH, Nginx/FastCGI); Google Cloud Config Connector (Kubernetes operator)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** true for Beats Studio Buds (Apple firmware 1B211); false for Google Cloud Config Connector; patch availability unknown for Popa Android TV botnet and Velvet Ant.
- **Active Exploitation:** true for Popa Android TV botnet and Velvet Ant; unknown for Apple Beats and GCP Config Connector
- **Threat Actors:** Threat actors unknown for Apple Beats and GCP Config Connector; NetNut/Alarum Technologies linked to Popa Android TV botnet; China‑nexus actor (named Velvet Ant) linked to Velvet Ant campaign.
- **Mitigation:** Install the Apple Beats Studio Buds firmware update 1B211; remove or inspect untrusted apps/SDKs on Android TV devices and factory‑reset if needed; replace backdoored PAM/OpenSSH and Nginx/FastCGI components, rotate credentials, rebuild systems, and deploy integrity monitoring for Velvet Ant; avoid using Config Connector for organization‑level management, restrict creation of Config Connector resources, enforce strict Kubernetes RBAC, monitor IAM changes, and apply compensating controls for GCP Config Connector.
- **Vendor Advisory:** https://support.apple.com/en-us/127557

---

## 3. 🟠 Zero-Day — CISA: Splunk Enterprise flaw actively exploited, patch by Sunday

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-splunk-enterprise-flaw-actively-exploited-patch-by-sunday/>

> CISA has urged U.S. federal agencies to secure their systems by Sunday against a critical Splunk Enterprise vulnerability that is being exploited in attacks. [...]

**Parallel AI Enrichment:**

- **Technical Details:** The PostgreSQL sidecar service endpoint lacks authentication, allowing unauthenticated users to invoke /v1/postgres/recovery/backup and /v1/postgres/recovery/restore to create or truncate arbitrary files. An attacker‑controlled database dump and passfile (.pgpass) are used to execute SQL during restore, writing malicious Python scripts that achieve remote code execution.
- **Affected Products:** Splunk Enterprise 10.2.0‑10.2.3, 10.0.0‑10.0.6
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Disable the PostgreSQL sidecar service to remove the attack surface (note: disabling breaks Edge Processor, OpAmp, SPL2 pipelines).
- **Vendor Advisory:** https://advisory.splunk.com/advisories/SVD-2026-0603

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** When combined with CVE‑2026‑50083, CVE‑2026‑50084, and CVE‑2026‑50085, an otherwise‑unauthenticated attacker could execute a full takeover of affected systems via indirect prompt injection.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when malicious instructions are embedded in third‑party data sources or tools that an LLM accesses (e.g., web pages, documents, plugins). The LLM, while retrieving or using that external content to answer a user query or drive agentic workflows, can be influenced to follow the injected instructions—potentially without direct user input—leading to unauthorized actions, data exfiltration, or corrupted outputs.
- **Affected Products:** Google Workspace (products using Gemini / GenAI integrations), Gemini Enterprise (reported vulnerable in some research)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Input and output validation and sanitization; restrict or sandbox web‑browsing/third‑party data sources; apply strict content filters and provenance checks; implement human‑in‑the‑loop approval for agentic actions; monitor and block known IPI payload patterns; apply vendor recommendations from Google Workspace security blog.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The primary issue is indirect prompt injection — untrusted web content can influence agentic/browser‑integrated LLM agents by injecting or manipulating prompts or context that the agent executes; when chained with other vulnerabilities (e.g., CVE‑2025‑54131), this can lead to privilege escalation, local file access, or data exfiltration.
- **Affected Products:** Chrome (Gemini agentic browsing features)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Harden agentic browsing by applying Google’s architectural mitigations in the advisory, update Chrome to patched versions, disable/limit agentic browsing or Gemini CLI in headless/automated environments, validate and sanitize third‑party content to reduce indirect prompt injection exposure.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Near‑miss linear buffer overflow in the Rust CrabbyAVIF component (unsafe Rust/FFI area) was discovered and fixed pre‑release; Scudo hardened allocator’s guard pages rendered the overflow non‑exploitable and converted silent corruption to a crash.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050 and Android bulletin https://source.android.com/docs/security/bulletin/2025-08-01
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use Scudo hardened allocator (guard pages), improved crash reporting for overflow detection, restrictive use and review of unsafe{} blocks, and developer training on unsafe Rust (Comprehensive Rust training module).
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** OS command injection vulnerability in the MobileIron Configuration Service (MICS) web portal interface allowing remote command execution via crafted input.
- **Affected Products:** MobileIron Configuration Service (MICS) web portal interface of Ivanti Sentry
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors target large backbone, provider edge (PE) and customer edge (CE) routers, leverage compromised devices and trusted network connections to pivot, and modify router firmware or configuration to maintain persistent, long‑term access.
- **Affected Products:** Telecommunications backbone routers, provider edge (PE) routers, customer edge (CE) routers, and other network infrastructure devices
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon; OPERATOR PANDA; RedMike; UNC5807; GhostEmperor
- **Mitigation:** Harden routers (restrict management interfaces, enforce multi‑factor authentication, segment networks, apply least‑privilege), monitor for unauthorized configuration changes and anomalous traffic, inventory and isolate compromised devices, apply vendor updates where available, and follow the detailed simulation and mitigation guidance in the CISA advisory.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** GRU 85th Main Special Service Center (85th GTsSS), military unit 26165 (Russian GRU)
- **Mitigation:** Follow CISA advisory guidance and general hardening for targeted organizations (logistics, IT firms) — specific mitigation steps in vendor/CISA advisory.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 11. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

---

## 12. 🟡 High Severity — symfony/ux-icons: XSS via unsanitized SVG content in local files and Iconify on-demand responses

**CVE:** `CVE-2026-55877` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-6v8j-33hc-mv84>

> ### Description

The `ux_icon()` Twig function is marked `is_safe=[&#x27;html&#x27;]`, so Twig never escapes its output. `Icon::toHtml()` inlines the SVG source verbatim into the page. Browsers execute `&lt;script&gt;` elements and `on*` event-handler attributes found inside inline SVG, making any unsanitized icon a vector for cross-site scripting.

Two code paths were affected. In the local file …

---

## 13. 🟡 High Severity — OpenBao: Transit secrets engine crashes on key creation with `derived: true` for asymmetric key types

**CVE:** `CVE-2026-55776` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-8w8f-r2xv-4q4j>

> On OpenBao 2.5.4 and 2.5.2(and likely earlier versions also), an authenticated caller with write access to `transit/keys/*` can crash the OpenBao server by issuing a single key-creation request that combines an asymmetric `type` (`rsa-*`, `ecdsa-*`, `ed25519`)
with `derived: true`. The server returns no HTTP response and the process terminates (exit code 2). This is a remote, low-complexity denial…

---

## 14. 🟡 High Severity — OpenBao: Cross-namespace lease revocation/renewal via canonical sys/leases/{revoke,renew} — incomplete fix of CVE-2026-45808

**CVE:** `CVE-2026-55774` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-c36x-h252-g9x2>

> ### Summary

OpenBao users with access to the `sys/leases/revoke/:lease_id` endpoint in any namespace can revoke leases in any other namespace as long as the lease identifier is known to them, bypassing ACLs that should apply for cross-namespace revocations.

### Impact

OpenBao&#x27;s namespaces provide multi-tenant separation. A tenant who intentionally leaks lease identifiers can have their lea…

---

## 15. 🟡 High Severity — OpenBao: LDAPi ldaputil (wrong escape func)

**CVE:** `CVE-2026-55770` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-6mwx-4547-5vc9>

> ## 1. Description

### Component

`sdk/helper/ldaputil/client.go` — the shared LDAP utility library used by both the LDAP authentication backend and OpenLDAP secrets engine to construct LDAP search filters and bind DNs.

### Root Cause

The LDAP utility contains a **function selection error** that causes incorrect escaping of user-controlled input in LDAP filter construction. Two lines construct t…

---

## 16. 🟡 High Severity — StarCitizenWiki Extension Embed Video: Stored XSS via malformed src url with $wgEmbedVideoRequireConsent enabled

**CVE:** `CVE-2026-55692` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-5c7p-g73q-rpg5>

> ### Summary
With $wgEmbedVideoRequireConsent enabled (the default), the urls for videos are stored in a json-ified data attribute`data-mw-iframeconfig`. When given a malformed url or id, the data-mw-iframeconfig attribute can be escaped via single quotes, allowing for html/javascript injection.

### Details
The sprintf [here](https://github.com/StarCitizenWiki/mediawiki-extensions-EmbedVideo/blob/…

---

## 17. 🟡 High Severity — Langflow: BaseFileComponent-based nodes arbitrary file read with RCE exploit

**CVE:** `CVE-2026-55447` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-ccv6-r384-xp75>

> ### Summary
All components based on `BaseFileComponent` are vulnerable to the following vulnerability:
1. Docling (`DoclingInlineComponent`)
2. Docling Serve (`DoclingRemoteComponent`)
3. Read File (`FileComponent`)
4. NVIDIA Retriever Extraction (`NvidiaIngestComponent`)
5. Video File (`VideoFileComponent`)
6. Unstructured API (`UnstructuredComponent`)

For clarity, from now on I&#x27;ll only ref…

---

## 18. 🟡 High Severity — Langflow: Unauthenticated DoS through multipart form boundary file upload

**CVE:** `CVE-2026-55446` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-qwqc-p3q8-wcg9>

> ### Summary
An attacker can send a `/api/v1/files/upload/` request without any authentication token/cookies and abuse a very long multipart form boundary to make the langflow app unusable for all users for an indefinite amount of time. 

### Details
https://github.com/langflow-ai/langflow/blob/v1.0.18/src/backend/base/langflow/api/v1/files.py#L40

The file upload function will try to process the m…

---

## 19. 🟡 High Severity — Langflow: Logout button does not clear session

**CVE:** `CVE-2026-55423` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-7hw8-6q6r-4276>

> ### Summary
The logout button does not clear the session. The previous user stays logged in unless another user explicitly logs in.

### Details
Not in auto login mode. Hosted on localhost. `access_token_lf` remains present in both Local Storage and Cookies. `refresh_token_lf` remains present in Cookies.

**Root cause:** the `/logout` endpoint deleted the authentication cookies without matching th…

---

## 20. 🟡 High Severity — Mailpit: Incomplete SSRF protection in Link Check API via IPv6 transition mechanisms

**CVE:** `CVE-2026-55187` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-w4mc-hhc6-xp28>

> ## Summary

The remediation shipped in mailpit v1.29.2 for [GHSA-mpf7-p9x7-96r3](https://github.com/axllent/mailpit/security/advisories/GHSA-mpf7-p9x7-96r3) (CVE-2026-27808) is incomplete. The `tools.IsInternalIP` deny-list relies on Go&#x27;s stdlib classification helpers (`IsLoopback`, `IsPrivate`, `IsLinkLocalUnicast`, `IsLinkLocalMulticast`, `IsUnspecified`, `IsMulticast`) plus an inline CGNAT…

---

## 21. 🟡 High Severity — Traefik Kubernetes Ingress NGINX provider fails open when auth-secret resolution fails

**CVE:** `CVE-2026-54762` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-4mr2-fg2p-w63c>

> ## Summary

There is a medium severity vulnerability in Traefik&#x27;s Kubernetes Ingress NGINX provider that causes affected routes to fail open. When an Ingress explicitly enables BasicAuth or DigestAuth through the supported `nginx.ingress.kubernetes.io/auth-type` and `auth-secret` annotations, but the referenced auth Secret cannot be resolved or parsed, Traefik logs the resolution error, skips…

---

## 22. 🟡 High Severity — dbt MCP Server: Unauthenticated OAuth Context Endpoint Leaks dbt Platform Tokens

**CVE:** `CVE-2026-55837` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-jr33-mw75-7j8f>

> ## Unauthenticated OAuth Context Endpoint Leaks dbt Platform Tokens

### Summary

The local OAuth helper FastAPI server bundled with `dbt-mcp` exposes the `GET /dbt_platform_context` endpoint without any form of authentication or host-origin validation. After a user completes the OAuth login flow against dbt Cloud (cloud.getdbt.com), the endpoint returns the full `DbtPlatformContext` object — incl…

---

## 23. 🟡 High Severity — Craft CMS: Blind SSRF and Arbitrary JavaScript Injection via Host Header Poisoning in actionResourceJs

**CVE:** `CVE-2026-55791` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-c55v-343g-5xff>

> **1. Overview**

Craft CMS is vulnerable to Server-Side Request Forgery (SSRF) and Arbitrary JavaScript Injection through the `/actions/app/resource-js` endpoint. By exploiting the default permissive `trustedHosts` configuration, an attacker can poison the `Host` or `X-Forwarded-Host` header to manipulate the application’s `$baseUrl`. This bypasses the endpoint’s internal URL validation, forcing t…

---

## 24. 🟡 High Severity — @tinacms/cli: Remote Code Execution in @tinacms/cli via Forestry migration — unsanitised __TINA_INTERNAL__ marker in user-controlled YAML labels

**CVE:** `CVE-2026-54074` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-4936-9hrh-qqpw>

> ## Description

### Summary

`@tinacms/cli` contains a Remote Code Execution vulnerability in its
Forestry-to-Tina migration command. The internal helper `addVariablesToCode`
unquotes any value matching the marker `&quot;__TINA_INTERNAL__:::(.*?):::&quot;`
inside the stringified collection JSON. User-supplied `label` and `name`
fields from `.forestry/**/*.yml` are placed into that JSON without any…

---

## 25. 🟡 High Severity — Grafana Operator: Privilege escalation from namespace admin to cluster admin via GrafanaDashboard jsonnetLib fileName

**CVE:** `CVE-2026-11769` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-fcw4-wwqm-m8cf>

> We have released version 5.24.0 of the Grafana Operator. This patch includes a MODERATE severity security fix for a path traversal/privilege escalation vulnerability in the Grafana Operator.


### Summary

The Grafana Operator supports loading dashboards &amp; library panels using the jsonnet data templating language. The jsonnet expression is evaluated in the context of the operator manager pod.
…

---

## 26. 🟡 High Severity — @cyclonedx/cyclonedx-npm: Shell Injection via Unsanitized --workspace Argument

**CVE:** `CVE-2026-55849` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-v75r-vx73-82pj>

> ## Summary
A command injection vulnerability exists in `@cyclonedx/cyclonedx-npm` when the CLI is invoked with the `--workspace &lt;value&gt;` option while the environment variable `npm_execpath` is unset or empty.  
User‑supplied `--workspace` values are passed to a subshell without proper sanitization, enabling attackers to inject arbitrary OS commands.  
This issue corresponds to **CWE‑78**: Im…

---

## 27. 🟡 High Severity — Concurrent Ruby: ReadWriteLock allows wrong-thread write release and stray read-release counter corruption

**CVE:** `CVE-2026-54906` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-6wx8-w4f5-wwcr>

> ### Summary
`Concurrent::ReadWriteLock#release_write_lock` does not verify that the calling thread acquired the write lock. Any thread with access to the lock object can release an active write lock held by another thread. A second writer can then enter its critical section while the first writer is still running.

`Concurrent::ReadWriteLock#release_read_lock` also decrements the shared counter ev…

---

## 28. 🟡 High Severity — Concurrent Ruby: `ReentrantReadWriteLock` read-count overflow grants a write lock without exclusivity

**CVE:** `CVE-2026-54905` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-wv3x-4vxv-whpp>

> ### Summary
`Concurrent::ReentrantReadWriteLock` can incorrectly grant a write lock after one thread acquires the read lock 32,768 times.

The lock stores a thread&#x27;s local read and write hold counts in one integer. The low 15 bits are used for the read hold count, and bit 15 is used as `WRITE_LOCK_HELD`. After 32,768 reentrant read acquisitions, the local read count crosses into the write-loc…

---

## 29. 🟡 High Severity — CoreWCF: SPNEGO SecurityContextToken proof key wrapped without confidentiality

**CVE:** `CVE-2026-54784` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-2288-8h3r-cqgg>

> ### Impact
When the proof key recovered from the RSTR can be observed by a party that is not the legitimate client, that party can impersonate the authenticated Windows principal for the lifetime of the SCT (default ~10 hours) and decrypt or forge any subsequent WS‑SecureConversation traffic that uses keys derived from the SCT.

#### Preconditions
Using security mode TransportWithMessageCredential…

---

## 30. 🟡 High Severity — CoreWCF: SamlSerializer skips SignatureValue verification when SAML signing token is not an X.509 certificate

**CVE:** `CVE-2026-54774` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-rpj7-hr7h-w6p9>

> ### Impact
When a service is configured to validate SAML tokens using a method other than X.509 certificate signing, the final signature verification is skipped.

#### Preconditions
The service is configured to authenticate using SAML tokens and an out of band token resolver (commonly the IssuerTokenResolver of IssuedTokenServiceCredential) holds a non-X.509 SecurityToken whose key identifier the …

---

## 31. 🟡 High Severity — CoreWCF: Pre-authentication infinite-loop CPU exhaustion in CoreWCF net.tcp / net.pipe / net.uds framing handshake

**CVE:** `CVE-2026-54772` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-p86g-xrr2-pf7c>

> ### Impact
An unauthenticated remote attacker can pin one server thread‑pool worker at 100 % CPU per connection. With a few connections, the CPU usage can be exhausted.

#### Preconditions
An attacker being able to reach a service which is exposing an endpoint using one of NetTcpBinding, NetNamedPipeBinding, or UnixDomainSocketBinding.

### Patches
Fixed in CoreWCF v1.8.1 and v1.9.1

### Workaroun…

---

## 32. 🟡 High Severity — Weekly Metasploit Update: NTLM Relay Priv Esc, MCP Server Integration, Paperclip AI RCE Chain, and more

**CVE:** `CVE-2026-41679` | `CVE-2026-41459` | `CVE-2026-34413` | `CVE-2026-34415` | `CVE-2026-34414` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-19-06-2026>

> This week&#x27;s release includes five new modules, including a full unauthenticated RCE chain for Paperclip AI and a VS Code extension persistence technique. On the post-exploitation side, the new windows/local/ntlm_relay_2_self module coerces the local machine account to authenticate via OpenEncryptedFileRaw (WebDAV), relays that NTLM authentication to a Domain Controller&#x27;s LDAP service, th…

---

## 33. 🟡 High Severity — Splunk Enterprise Vulnerability Exploited in Attacks Days After Disclosure

**CVE:** `CVE-2026-20253` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://www.securityweek.com/splunk-enterprise-vulnerability-exploited-in-attacks-days-after-disclosure/>

> CISA has given federal agencies only three days to patch CVE-2026-20253, which can be exploited for unauthenticated remote code execution. The post Splunk Enterprise Vulnerability Exploited in Attacks Days After Disclosure appeared first on SecurityWeek .

---

## 34. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
