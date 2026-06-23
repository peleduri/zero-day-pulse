# Zero Day Pulse

> **Generated:** 2026-06-23 14:20 UTC &nbsp;|&nbsp; **Total:** 36 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 26 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal (directory traversal) vulnerability in SimpleHelp web interface that allows unauthenticated remote attackers to read arbitrary files on the server by sending crafted requests that traverse filesystem paths.
- **Affected Products:** SimpleHelp remote support / Remote Monitoring and Management (RMM) software, versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Public proof‑of‑concept and weaponized exploitation reported; see https://www.offsec.com/blog/cve-2024-57727/
- **Patch Available:** A patch is available; SimpleHelp released an updated version after 5.5.7. Details at https://guides.simple-help.com/kb---security-vulnerabilities-01-2025
- **Active Exploitation:** Yes — confirmed active exploitation reported by CISA advisory AA25-163A.
- **Threat Actors:** Ransomware actors
- **Mitigation:** Upgrade to the latest SimpleHelp release; if unable to patch immediately, isolate/offline SimpleHelp, restrict access via firewall to trusted IPs, rotate credentials, and monitor logs for suspicious access.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) involves embedding malicious prompt fragments in web content so that AI models that retrieve and process the content incorporate the attacker‑controlled instructions into their reasoning, potentially leading to unauthorized actions or data leakage.
- **Affected Products:** Microsoft Copilot Studio (CVE-2026-21520)
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit available.
- **Patch Available:** No official patch available.
- **Active Exploitation:** Yes, active exploitation in the wild has been reported.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) enables attackers to influence LLM behavior by injecting malicious instructions into the data or tools the LLM uses while fulfilling a user’s request; this may be possible without direct user input (e.g., via notifications, web content, or other integrated data).
- **Affected Products:** Google Workspace with Gemini integrations
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof‑of‑concept details reported by third parties exist; no single vendor‑supplied exploit repository.
- **Patch Available:** No official "patch" published; see advisory URL for mitigation details.
- **Active Exploitation:** Reports describe proof‑of‑concept zero‑click or notification‑based IPI; no confirmed widescale active exploitation attributed to specific actors.
- **Threat Actors:** None known
- **Mitigation:** See Google advisory for mitigations (input sanitation, provenance tracking, source isolation, policy‑based controls, model‑level hardening).
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is an indirect prompt injection: attackers inject malicious instructions into data sources or web content that an agentic AI treats as authoritative, causing the agent to execute unintended actions or exfiltrate data. The GeminiJack example demonstrates exploitation of trust boundaries between user‑controlled content and model instructions.
- **Affected Products:** Chrome agentic/Gemini integration, Gemini Enterprise components
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit is known.
- **Patch Available:** Google announced layered mitigations and architecture changes in the Chrome agentic/Gemini integration; no separate patch URL is provided (see blog post).
- **Active Exploitation:** No confirmed active exploitation reported; industry reporting describes the issue but no mass exploitation evidence.
- **Threat Actors:** None known
- **Mitigation:** Use Chrome’s new layered defenses for agentic browsing: restrict agent access to untrusted sites, sandbox data sources, validate and canonicalize data, and require explicit user confirmation for agent actions.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC found; exploit reported as in-the-wild (no public weaponized PoC URL found).
- **Patch Available:** Google released patches in the Android June 2026 security patch level (2026-06-05 delivery to partners) via the Android Security Bulletin.
- **Active Exploitation:** Confirmed indications of limited, targeted exploitation have been reported.
- **Threat Actors:** None known
- **Mitigation:** Apply June 2026 Android security updates; install vendor updates and avoid untrusted apps/sources.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2026/2026-06-01

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** An unauthenticated OS command injection in the Ivanti Sentry (MobileIron Configuration Service) web portal allows remote attackers to inject and execute OS‑level commands via crafted requests to the web interface, enabling full system compromise and potential backdoor installation.
- **Affected Products:** Ivanti Sentry (MobileIron Configuration Service) versions before R10.5.2, R10.6.2, and R10.7.1
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** Public proof‑of‑concept exploit available (reported June 10, 2026)
- **Patch Available:** Yes — Ivanti released updates addressing CVE-2026-10520 (see vendor advisory URL above).
- **Active Exploitation:** Yes — active exploitation confirmed by Shadowserver/Foundation and multiple incident reports; public PoC released on June 10, 2026.
- **Threat Actors:** None known
- **Mitigation:** Apply Ivanti vendor updates immediately; if patching is delayed, isolate or block access to the MICS web portal from untrusted networks, remove or restrict administrative access, implement Web Application Firewall rules to block malicious payloads, and monitor for indicators of compromise.
- **Vendor Advisory:** https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523?language=en_US

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** State‑sponsored actors compromise backbone, provider edge and customer edge routers, modify firmware or configuration to maintain long‑term access, and leverage these compromised devices to pivot into other network segments.
- **Affected Products:** Network routers (backbone routers, provider edge (PE) routers, customer edge (CE) routers)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit or PoC is known.
- **Patch Available:** No official patch is available; guidance is limited to mitigation steps.
- **Active Exploitation:** No confirmed active exploitation reported in the advisory.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Follow the mitigation guidance in CISA Alert AA25-239A which includes router configuration hardening, network segmentation, monitoring for anomalous traffic, and applying recommended detection rules.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Actors used exploitation of internet‑facing apps (including CVE-2023-38831 in WinRAR and Roundcube CVEs), spearphishing (malicious attachments/links), SQLi, living‑off‑the‑land tools (ntdsutil, vssadmin, wevtutil), Impacket/PsExec, RDP lateral movement, mailbox‑permission manipulation for sustained email collection, and exfiltration of O365 mailboxes.
- **Affected Products:** RARLAB WinRAR (CVE-2023-38831); Roundcube Webmail (CVE-2020-35730, CVE-2020-12641)
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit URLs cited in the advisory.
- **Patch Available:** Vendor patches available for referenced CVEs (see vendor/security advisories for WinRAR CVE-2023-38831 and Roundcube CVE-2020-35730/CVE-2020-12641). Specific vendor advisory URLs not provided in CSA.
- **Active Exploitation:** Yes — advisory notes exploitation of CVE-2023-38831 and other vulnerabilities by GRU unit 26165 against targets; CISA reports active targeting of logistics and technology companies.
- **Threat Actors:** Russian GRU (unit 26165) — tracked in industry as APT28 / Fancy Bear / Forest Blizzard / Blue Delta.
- **Mitigation:** Enable Windows attack surface reduction rules; collect and monitor Windows logs; enable application hardening and executable allowlisting; monitor for LOTL usage and specific IOCs; follow CISA mitigation actions in advisory.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch information unavailable.
- **Active Exploitation:** No reports of active exploitation related to this blog post; the CrowdStrike blog summarizes survey findings about cloud breaches, not a specific software vulnerability.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 10. 🟠 Zero-Day — Algerian Man Extradited to US for Running Cybercrime Marketplaces

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://www.securityweek.com/algerian-man-extradited-to-us-for-running-cybercrime-marketplaces/>

> 26-year-old Abdellah Belmili faces up to 30 years in prison for allegedly operating the marketplaces Market0Day and Spoxy. The post Algerian Man Extradited to US for Running Cybercrime Marketplaces appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** OS command injection in Ivanti Sentry allows a remote unauthenticated user to execute OS commands (remote command injection).
- **Affected Products:** Ivanti Sentry versions before R10.5.2, R10.6.2 and R10.7.1
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit found in searched sources.
- **Patch Available:** Yes — Ivanti released updates addressing the issue (see vendor advisory URL).
- **Active Exploitation:** Confirmed — added to CISA Known Exploited Vulnerabilities Catalog.
- **Threat Actors:** None known
- **Mitigation:** Apply Ivanti updates to R10.5.2, R10.6.2 or R10.7.1 or later; follow Ivanti advisory for workarounds/hardening.
- **Vendor Advisory:** https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523?language=en_US

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
