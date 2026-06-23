# Zero Day Pulse

> **Generated:** 2026-06-23 08:56 UTC &nbsp;|&nbsp; **Total:** 36 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 26 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Unauthorized attackers can exploit a directory traversal flaw to read arbitrary files on SimpleHelp servers without authentication.
- **Affected Products:** SimpleHelp remote support / RMM versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (unspecified groups)
- **Mitigation:** Upgrade SimpleHelp to a patched version immediately; if patching is delayed, block inbound access to SimpleHelp servers, require VPN or firewall restrictions, rotate credentials, review logs for indicators of compromise, and follow CISA incident response guidance.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) in Google Gemini Enterprise allows an attacker to embed malicious prompts that alter the model's output. The GeminiJack zero‑click vulnerability shows this can be achieved without user interaction, directly injecting a crafted payload into the model's processing pipeline.
- **Affected Products:** Google Gemini Enterprise
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability)
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true (https://blog.google/security/prompt-injections-web/)
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attacker technique that injects malicious instructions into data sources or tools consumed by a large language model (LLM) during completion, causing the LLM or agentic automations to follow attacker‑supplied commands (potentially without any direct user input). Vectors include poisoned web content, document content, email, or other integrated data/tools that LLMs query; impacts arise when LLMs run tool calls or use external data without strict input validation or provenance checks.
- **Affected Products:** Google Workspace with Gemini (Gemini Enterprise integrations)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Input and output validation and sanitization; restrict LLM access to untrusted external data and tools; enforce human‑in‑the‑loop review for sensitive actions; use allowlists and provenance/metadata checks; continuous monitoring and sweeps for known IPI patterns; adopt vendor guidance from the Google Security Blog advisory.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The flaw allows an attacker to inject malicious prompts into the Gemini AI agent via a web page, which can then be chained with indirect prompt injection to achieve actions like local file read or privacy‑invasive behavior.
- **Affected Products:** Google Chrome (versions prior to the patch for CVE-2026-0628), Google Gemini Enterprise (versions prior to 1.3)
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Update Chrome to the latest version which includes a new security layer that sanitizes prompts and isolates the Gemini AI agent, thereby mitigating indirect prompt injection.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A near-miss linear buffer overflow in CrabbyAVIF (unsafe Rust) (assigned CVE-2025-48530); Scudo guard pages turned overflow into a noisy crash and made it non-exploitable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — patch: https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050 and advisory: https://source.android.com/docs/security/bulletin/2025-08-01
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Scudo hardened allocator (guard pages) rendered the overflow non-exploitable; increased crash reporting, unsafe-code review and training; make Scudo mandatory on partners.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection attacks are hidden malicious instructions embedded in external data sources (emails, documents, calendar invites) that aim to manipulate generative AI systems to exfiltrate data or perform unintended actions.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses—sanitize and validate external data sources, enforce provenance and access controls, apply output filters and rate limits, and deploy product‑level mitigations as described by Google (see vendor advisory).
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state‑sponsored actors modify large backbone, provider edge (PE) and customer edge (CE) routers, leveraging compromised devices and trusted connections to pivot within networks, thereby achieving persistent, long‑term access and enabling lateral movement.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Network segmentation, monitoring for lateral movement, hardening router configurations, replacing or re‑imaging compromised devices, applying vendor fixes when available, restricting management interfaces, enforcing MFA for administrative access, and updating firmware per vendor advisories.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** State-sponsored cyber espionage campaign targeting Western logistics and technology companies (including entities coordinating transport/delivery of assistance to Ukraine) using intrusions since 2022 for intelligence collection and operational disruption; tactics reported include targeting logistics and IT supply‑chain/access vectors (detailed technical IOC‑level data not provided here).
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** GRU (85th GTsSS / Unit 26165); tracked names include APT-28 (and related GRU designations).
- **Mitigation:** Implement multifactor authentication, network segmentation, least privilege, rapid patching/updating of enterprise systems, enhanced monitoring and logging, phishing‑resistant controls, and follow CISA/FBI joint advisory guidance (AA25-141A) for indicators and response steps.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

**Parallel AI Enrichment:**

- **Technical Details:** An OS command injection (link‑following/improper input handling in the MobileIron Configuration Service web portal) allows an unauthenticated remote attacker to execute arbitrary OS commands as root, leading to full remote code execution and takeover of the appliance.
- **Affected Products:** Ivanti Sentry (formerly MobileIron Sentry) — versions before R10.5.2, R10.6.2, and R10.7.1
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — https://horizon3.ai/attack-research/vulnerabilities/cve-2026-10520
- **Patch Available:** true — https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523?language=en_US
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor patch immediately; isolate or block network access to vulnerable Sentry appliances, restrict management interfaces to trusted networks, monitor for suspicious activity, rotate credentials, and follow temporary mitigation steps outlined in the advisory.
- **Vendor Advisory:** https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523?language=en_US

---

## 10. 🟠 Zero-Day — What the Latest ShinyHunters Breaches Reveal About Modern Cyberattacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://www.securityweek.com/what-the-latest-shinyhunters-breaches-reveal-about-modern-cyberattacks/>

> Groups like ShinyHunters are demonstrating that attackers do not necessarily need malware or zero-day exploits to cause massive damage. The post What the Latest ShinyHunters Breaches Reveal About Modern Cyberattacks appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Attacks rely on credential‑stuffing, account takeover, data scraping/exfiltration and exploitation of misconfigurations or exposed datasets rather than malware or zero‑day exploits; attackers aggregate and sell leaked databases.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** ShinyHunters
- **Mitigation:** Enforce MFA, rotate compromised credentials, implement rate‑limiting and bot protections, monitor for credential‑stuffing, secure misconfigured endpoints, encrypt sensitive data at rest and in transit, perform regular audits and logging.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟡 High Severity — Gogs has the ability to import local repositories via Mirror Settings

**CVE:** `CVE-2026-52801` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-wv27-2vqp-j7g5>

> ### Summary
The Gogs Mirror Settings functionality provide an alternative way from the well protected New Migration functionality for any authenticated users to import local repositories. This issue stems from a lack of validation of SaveAddress function.

### Details
Here is the function implementation of the secure New Migration functionality.
&lt;img width=&quot;1200&quot; height=&quot;755&quot…

---

## 12. 🟡 High Severity — @actual-app/web has CSV Formula Injection in Transaction Export via Imported Payee/Notes Fields

**CVE:** `CVE-2026-50179` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-xqjm-27pc-rvwm>

> ## Summary

`exportToCSV` and `exportQueryToCSV` in `packages/loot-core/src/server/transactions/export/export-to-csv.ts` pass user-controlled `Payee`, `Notes`, `Account`, and `Category` strings to `csv-stringify` with no `cast` callback and no formula-prefix neutralization. Strings that begin with `=`, `+`, `-`, `@`, tab, or carriage return survive verbatim into the exported CSV. When the victim (…

---

## 13. 🟡 High Severity — @budibase/backend-core has potential SSRF DNS rebinding bypass in outbound fetch validation

**CVE:** `CVE-2026-54353` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-gfq7-5x4g-3xhf>

> Summary

Authenticated users with automation permissions can bypass Budibase&#x27;s SSRF blacklist through DNS rebinding.

The outbound fetch flow validates a hostname against the blacklist before the request is sent, but the actual socket connection later performs a separate DNS lookup through node-fetch. Since the validated IPs are never pinned to the connection, an attacker-controlled hostname …

---

## 14. 🟡 High Severity — Budibase has arbitrary file read by workspace-builder via PWA-zip symlink upload

**CVE:** `CVE-2026-54352` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-w7mq-r738-x278>

> ## Summary

`POST /api/pwa/process-zip` at `packages/server/src/api/routes/static.ts:24` accepts a builder-uploaded `.zip`, extracts it with `extract-zip@2.0.1` into a temp directory, then for each entry listed in `icons.json` validates the icon path, opens it, and streams the bytes into MinIO. The resulting object is served back via `GET /api/assets/{appId}/pwa/{uuid}.png`.

`extract-zip@2.0.1` p…

---

## 15. 🟡 High Severity — Budibase: POST /api/attachments/:datasourceId/url is unauthenticated and lets anonymous callers mint S3 PUT pre-signed URLs using stored datasource IAM credentials

**CVE:** `CVE-2026-50137` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-35c4-rvc8-frhm>

> ## Summary

The Budibase server route `POST /api/attachments/:datasourceId/url` ([`packages/server/src/api/routes/static.ts`](https://github.com/Budibase/budibase/blob/56d2a984/packages/server/src/api/routes/static.ts)) is registered with **only** the `recaptcha` middleware. There is no `authorized(...)` middleware in the chain. The controller (`packages/server/src/api/controllers/static/index.ts:…

---

## 16. 🟡 High Severity — Budibase: Unauthenticated S3 signed upload URL generation allows arbitrary writes with stored datasource credentials

**CVE:** `CVE-2026-50136` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-jj36-r9w3-3pfh>

> The application server exposes an unauthenticated endpoint that generates S3 `PutObject` presigned URLs using credentials stored in a workspace datasource. The route is protected only by the recaptcha middleware and does not require authentication, table permission, datasource permission, or builder access. A public caller who knows a workspace ID and S3 datasource ID can request a signed upload U…

---

## 17. 🟡 High Severity — scimPatch vulnerable to prototype pollution via unfiltered keys in patch

**CVE:** `CVE-2026-48170` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-9m6g-wc8r-q59c>

> ## Summary

`scim-patch` performs prototype pollution when applying a SCIM PATCH operation whose `value` object contains a key like `&quot;__proto__.someProp&quot;`. After one such patch,
`Object.prototype.someProp` is set process-wide, affecting every plain object in the Node process.

Any service that calls `scimPatch()` on attacker-controlled JSON (i.e. any SCIM endpoint accepting `PATCH` from …

---

## 18. 🟡 High Severity — Budibase: SSRF via OAuth2 token endpoint URL reaches internal hosts and cloud metadata

**CVE:** `CVE-2026-48153` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-4q6h-8p4v-67vq>

> ## Summary

`fetchToken` in the OAuth2 SDK makes a POST to a builder-supplied URL with plain node-fetch, skipping the `blacklist.isBlacklisted` check that every other outbound fetch path in the codebase uses. The Joi schema for the OAuth2 URL has no scheme or host restriction. Alice, a builder, points an OAuth2 config at `http://169.254.169.254/...` or `http://127.0.0.1:5984/`; the server connects…

---

## 19. 🟡 High Severity — Gogs has SSRF in webhook deliveries

**CVE:** `CVE-2026-47267` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-c4v7-xg93-qf8g>

> ### Summary
The fix for  CVE-2022-1285 prevents adding webooks or running webhooks with URLs with a hostname that resolves in localCIDRs. However, webhooks still follow redirects allowing to access hostname inside localCIDRs.

This was already communicated in the initial report but it looks like there was a bit of a miscommunication.

### Details

By creating a webook pointing to any URL that will…

---

## 20. 🟡 High Severity — @actual-app/sync-server's missing authorization on GET /secret/:name allows non-admin OpenID users to enumerate admin-configured bank-sync secrets

**CVE:** `CVE-2026-46700` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-3f62-qv96-4p78>

> ## Summary

In `@actual-app/sync-server`, the `GET /secret/:name` endpoint (`app-secrets.js:53`) checks only that the caller has a valid session — it does not verify the caller is an admin. The sibling `POST /secret/` handler does enforce an admin check in OpenID mode, exposing an authorization asymmetry. Any authenticated non-admin (BASIC) user in OpenID multi-user deployments can probe the secre…

---

## 21. 🟡 High Severity — Glances: XML-RPC Server Missing Host Header Validation Enables DNS Rebinding Attack

**CVE:** `CVE-2026-46611` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-w856-8p3r-p338>

> ### Summary

The Glances XML-RPC server (`glances -s`, implemented in `glances/server.py`) does not validate the HTTP `Host` header, leaving it vulnerable to DNS rebinding attacks.  CVE-2026-32632 (patched in 4.5.2) added `TrustedHostMiddleware` to the REST/WebUI server; the MCP server has had equivalent protection since 4.5.1. The XML-RPC server received neither fix and has no `allowed-hosts` con…

---

## 22. 🟡 High Severity — OpenDJ Pre-Auth RCE via Java Deserialization in JMX RMI

**CVE:** `CVE-2026-46495` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-43x2-g84q-fmqx>

> ## Summary

**Description**

A Deserialization of Untrusted Data (CWE-502) issue in OpenDJ&#x27;s JMX RMI connector allows an unauthenticated remote attacker to deserialize arbitrary Java objects on the server. The vulnerability exists because the platform reads and processes attacker-controlled bytes prior to authentication. This affects OpenDJ Community Edition through 5.1.0. This has been patch…

---

## 23. 🟡 High Severity — OpenAM SAML2 Cluster Cookie-Hash-Redirect Path has Pre-authentication Reflected XSS via `FSUtils.postToTarget`

**CVE:** `CVE-2026-44793` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-fhrq-3gmx-p879>

> ## Summary

Certain federation endpoints do not consistently apply output encoding when rendering user-supplied parameters into HTML responses. Under a non-default configuration used in some clustered deployments, this inconsistency can result in reflected XSS in the OpenAM origin without authentication.

---

## 24. 🟡 High Severity — Inspektor Gadget: Unprivileged container can crash USDT note parser via crafted ELF (no shipped gadget affected)

**CVE:** `CVE-2026-44778` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-7cfq-5mhv-jrp9>

> ## Summary

A malicious container can crash or destabilize the privileged Inspektor Gadget process when a **gadget using USDT probes** is deployed. The vulnerability is in the USDT note parser (`pkg/uprobetracer/usdt.go`) which is invoked when a gadget with a `SEC(&quot;usdt/...&quot;)` section attaches to a target binary. An unprivileged process can place a crafted ELF binary at the expected libr…

---

## 25. 🟡 High Severity — Paymenter has Blind Unauthenticated SSRF on the Paypal gateway module

**CVE:** `CVE-2026-44583` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-7wwh-xcc3-9fcg>

> ### Summary
The PayPal webhook endpoint `/extensions/paypal/webhook` processes the `PAYPAL-CERT-URL` HTTP header without validation, allowing attackers to control server-side HTTP request destinations.

### Technical details:

The `/extensions/paypal/webhook` endpoint processes incoming webhook requests and trusts the value of the `PAYPAL-CERT-URL` HTTP header without validation.

This value is pa…

---

## 26. 🟡 High Severity — OpenAM has pre-auth Reflected XSS in OAuth2 / OIDC response_mode=form_post via state parameter (FormPostResponse.ftl)

**CVE:** `CVE-2026-44203` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-fq9h-c788-fx73>

> ### Summary

The OAuth 2.0 / OpenID Connect authorization endpoint does not sufficiently sanitize certain user-supplied parameters before incorporating them into the HTML response generated for the `form_post` response mode. This may allow an attacker to inject content into the rendered page in the context of the OpenAM origin.

---

## 27. 🟡 High Severity — OpenAM Authenticated Server-Side Request Forgery (SSRF) via `/sessionservice`

**CVE:** `CVE-2026-44202` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-c556-q2mh-477v>

> OpenAM (Open Identity Platform) is an open-source Identity and Access Management (IAM) platform derived from ForgeRock OpenAM, providing SSO, OAuth2, SAML, and OpenID Connect capabilities. It is widely deployed in enterprise environments as a central authentication gateway.

The `/sessionservice` endpoint, used for internal session management operations, does not sufficiently restrict the URLs tha…

---

## 28. 🟡 High Severity — xwiki-pro-macros has remote code execution from page title and content via excerpt-include macro

**CVE:** `CVE-2026-44179` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-w56x-9778-rppx>

> ### Summary
The excerpt-include macro does not properly escape the title of the included page and executes the content of the excerpt with the macro&#x27;s rights. Therefore, it is vulnerable to XWiki syntax injection via the included page&#x27;s title and content, allowing remote code execution for any user who can edit a page.

### Details
The title of the included page isn&#x27;t escaped in [Ex…

---

## 29. 🟡 High Severity — OpenAM has LDAP Injection via `_queryId` Parameter

**CVE:** `CVE-2026-41573` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-2vg8-q4c2-5cw3>

> OpenAM (Open Identity Platform) is an open-source IAM platform providing SSO, OAuth2, SAML, and OpenID Connect capabilities. The CREST REST API layer exposes user query endpoints under `/json/{realm}/users`. In `IdentityResourceV1.queryCollection()`, the HTTP query parameter `_queryId` is passed to a `CrestQuery` object with `escapeQueryId` **explicitly set to `false`**, bypassing the escape prote…

---

## 30. 🟡 High Severity — AVideo has an Authorize.Net Webhook Signature Bypass that Enables Wallet Balance Inflation via Forged Payment Data

**CVE:** `CVE-2026-33731` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-95jh-7r58-xmxw>

> ## Summary

The Authorize.Net webhook handler at `plugin/AuthorizeNet/webhook.php` contains a signature verification bypass that allows an attacker to forge webhook requests with arbitrary payment amounts and target user IDs. By supplying a valid transaction ID from a small legitimate purchase, the attacker bypasses signature validation and credits arbitrary wallet balances to any user account via…

---

## 31. 🟡 High Severity — ComfyUI-Manager has an Unprotected Alternate Channel (CWE-420)

**CVE:** `CVE-2025-67303` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-95pq-hr8p-f5g7>

> ### Impact

An **Unprotected Alternate Channel (CWE-420)** vulnerability was discovered in ComfyUI-Manager versions prior to 3.38.

#### Vulnerability Details

In affected versions, ComfyUI-Manager stored its configuration in the `user/default/ComfyUI-Manager/` directory, which was accessible via ComfyUI&#x27;s web APIs without proper access control. This unprotected alternate channel allowed remo…

---

## 32. 🟡 High Severity — AVideo Vulnerable to Unauthenticated .env File Exposure via Official Docker Compose Configuration

**CVE:** `CVE-2026-33692` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-wf69-r4mx-43rr>

> ## Vulnerability Details

**CWE**: CWE-538 - Insertion of Sensitive Information into Externally-Accessible File or Directory

The official `docker-compose.yml` (line 61) mounts the entire project root directory as the Apache document root:

```yaml
volumes:
  - &quot;./:/var/www/html/AVideo&quot;
```

This causes the `.env` file — which contains database credentials, admin passwords, and infrastru…

---

## 33. 🟡 High Severity — AVideo's Privilege Escalation via Unguarded Permission Parameters in signUp API Allows Self-Granting Upload/Stream/Meet Permissions

**CVE:** `CVE-2026-33684` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-8j8m-p79x-g4jm>

> ## Summary

The `set_api_signUp` method in the API plugin accepts `emailVerified`, `canUpload`, `canStream`, and `canCreateMeet` parameters from user-supplied input and applies them to newly created accounts without verifying that the request was authenticated with a valid APISecret. Any anonymous user who can solve a CAPTCHA can self-grant elevated permissions during account registration.

## Det…

---

## 34. 🟡 High Severity — OpenCTI has Semi-Blind SSRF via Unvalidated External URL in Data Ingestion Feature

**CVE:** `CVE-2026-21887` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-ffm6-vvph-g5f5>

> ### Summary
The OpenCTI platform’s data ingestion feature accepts user-supplied URLs without validation and uses the Axios HTTP client with its default configuration (allowAbsoluteUrls: true). This allows attackers to craft requests to arbitrary endpoints, including internal services, because Axios will accept and process absolute URLs.

This results in a semi-blind SSRF, as responses may not be f…

---

## 35. 🟡 High Severity — Paymenter vulnerable to Remote Code Execution via public file uploads

**CVE:** `CVE-2025-58048` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-5pm9-r2m8-rcmj>

> ### Impact

The ticket attachments functionality in Paymenter allows a malicious authenticated user to upload arbitrary files.

With the ability to execute arbitrary code, this vulnerability can be exploited in numerous ways, including but not limited to:
- Extracting sensitive data from the database (e.g. customer information).
- Reading credentials from .env or other configuration files.
- Runni…

---

## 36. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
