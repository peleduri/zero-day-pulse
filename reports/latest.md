# Zero Day Pulse

> **Generated:** 2026-05-23 18:55 UTC &nbsp;|&nbsp; **Total:** 17 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 7 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** SimpleHelp remote support software (v5.5.7 and earlier) is vulnerable to path‑traversal (CWE‑22). An attacker can send a specially crafted HTTP request to retrieve arbitrary files from the server without authentication.
- **Affected Products:** SimpleHelp Remote Monitoring and Management, versions 5.5.7 and earlier
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC available at https://github.com/imjdl/CVE-2024-57727
- **Patch Available:** Patch available: SimpleHelp version 5.5.8 fixes the CVE‑2024‑57727 issue. Download from the vendor KB page.
- **Active Exploitation:** Confirmed active exploitation: CISA lists CVE‑2024‑57727 in its KEV catalog and reports ransomware actors (DragonForce) leveraging unpatched SimpleHelp instances.
- **Threat Actors:** DragonForce ransomware group
- **Mitigation:** Apply SimpleHelp version 5.5.8 immediately. Until patched, isolate SimpleHelp servers, restrict inbound/outbound network traffic, and conduct threat‑hunting for signs of compromise as recommended by CISA.
- **Vendor Advisory:** https://simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — Drupal Core SQL Injection Bug Actively Exploited, Added to CISA KEV

**CVE:** `CVE-2026-9082` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://thehackernews.com/2026/05/drupal-core-sql-injection-bug-actively.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has added a recently patched critical security flaw impacting Drupal Core to its Known Exploited Vulnerabilities (KEV) catalog, based on evidence of active exploitation.

The vulnerability in question is CVE-2026-9082 (CVSS score: 6.5), an SQL injection vulnerability affecting all supported versions of Drupal Core.

&quot;Drupal Core

**Parallel AI Enrichment:**

- **Technical Details:** SQL injection in Drupal Core database abstraction API allowing specially crafted requests to cause arbitrary SQL injection on sites using PostgreSQL, leading to data disclosure and potential privilege escalation or RCE.
- **Affected Products:** Drupal core versions >=8.9.0 <10.4.10, >=10.5.0 <10.5.10, >=10.6.0 <10.6.9, >=11.0.0 <11.1.10, >=11.2.0 <11.2.12, >=11.3.0 <11.3.10
- **CVSS Score:** 6.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N
- **Exploit Available:** Public exploit/PoC observed in the wild as probe/attack attempts; Imperva reported >15,000 attack attempts across ~6,000 sites. No confirmed publicly‑published full weaponized PoC URL.
- **Patch Available:** Yes — Drupal released patched versions (11.3.10, 11.2.12, 11.1.10, 10.6.9, 10.5.10, 10.4.10) and manual patches for older branches (9.5 and 8.9). See vendor advisory.
- **Active Exploitation:** Yes — CISA added CVE‑2026‑9082 to the KEV catalog based on evidence of active exploitation; Drupal acknowledged exploit attempts; Imperva reported widespread probing activity.
- **Threat Actors:** None known
- **Mitigation:** Immediately apply vendor updates or manual patches; if using PostgreSQL, prioritize updates. Review Twig/Symfony dependency updates and restrict who can update Twig templates; monitor logs and block probing IPs; isolate vulnerable sites until patched.
- **Vendor Advisory:** https://www.drupal.org/sa-core-2026-004

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) – adversaries seed malicious instructions in public web content (hidden page text, comments, repository files, etc.) that AI agents which browse or ingest that content may execute, leading to secret leakage, policy bypasses, or undesired actions.
- **Affected Products:** AI agents/systems that ingest untrusted web content (general class) — specific products/versions not listed
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC or weaponized exploit detailed in the advisory; exploit availability not reported
- **Patch Available:** No vendor patch for ‘IPI’ as it is an attack class rather than a single product vulnerability; vendor advisory URL provided above.
- **Active Exploitation:** Google Threat Intelligence observed real‑world IPI attempts on public web pages during their sweep; active exploitation reported as observed attempts.
- **Threat Actors:** None known
- **Mitigation:** Harden agents: restrict browsing of untrusted web content; apply content sanitization and canonicalization; implement instruction‑following constraints and provenance checks; use allowlists and denylisting for sources; rate‑limit and monitor; apply output filtering and secret redaction.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an attacker injects malicious instructions into data or tools that an LLM ingests (web content, documents, connectors, or tool outputs), causing the model or agentic workflows to perform unintended actions or reveal sensitive data without direct user input.
- **Affected Products:** Gemini (in Workspace) and Google Workspace apps that integrate Gemini
- **CVSS Score:** -9999.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit known.
- **Patch Available:** Patch not applicable; mitigation guidance provided in vendor advisory: https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/
- **Active Exploitation:** Reports indicate growing occurrence of IPI probes and opportunistic payloads in the wild but no confirmed large‑scale successful exploitation campaigns tied to named threat actor groups.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses including input/source provenance and trust checks, content sanitization and quarantine, tool and connector hardening, strict access controls and least privilege, human review for high‑risk actions, continuous monitoring and anomaly detection, and model‑level instruction filtering and guardrails.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The primary new threat is "indirect prompt injection," where web content can influence an agentic browser's internal prompts or agent instructions via indirect channels (e.g., content that is not a direct instruction but is interpreted by agents), enabling malicious sites to cause unsafe agent actions or data exfiltration. Google described layered defenses including prompt‑sourcing restrictions, origin access controls, and an additional supervisory agent to validate actions.
- **Affected Products:** Chrome (agentic/Gemini-enabled browsing features)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit has been reported.
- **Patch Available:** Google described new layered defenses and design changes for agentic browsing in Chrome, which are being shipped as Chrome updates and built‑in mitigations in Gemini for Chrome. See advisory for details.
- **Active Exploitation:** No confirmed active exploitation in the wild reported.
- **Threat Actors:** None known
- **Mitigation:** Use the latest Chrome updates that include the new defenses; operators should restrict agent capabilities, apply origin‑based restrictions, validate and sanitize inputs to agents, and monitor agent actions. End users should keep Chrome up to date and avoid untrusted sites when using agentic features.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow in the CrabbyAVIF library would have overwritten adjacent memory, but Android’s Scudo hardened allocator placed guard pages around secondary allocations, making the overflow non‑exploitable.
- **Affected Products:** Android platform (CrabbyAVIF component) – all versions receiving the patch.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit is available.
- **Patch Available:** https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050
- **Active Exploitation:** No active exploitation has been reported.
- **Threat Actors:** None known
- **Mitigation:** Use Android’s Scudo hardened allocator, which places guard pages around secondary allocations to prevent exploitation of buffer overflows.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection occurs when untrusted external content (e.g., emails, documents, calendar invites, or SharePoint form fields) contains crafted instructions that are ingested into an LLM’s context and interpreted as trusted system or role directives, allowing the model to execute unintended actions such as data exfiltration. The ShareLeak attack on Copilot Studio injected a payload via a SharePoint comment that concatenated with the agent’s system prompt, overriding it and causing the agent to query data sources and email the results.
- **Affected Products:** Google Gemini (Gemini app and Gemini in Workspace), Microsoft Copilot Studio
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** No public proof‑of‑concept or weaponized exploit is publicly available.
- **Patch Available:** Microsoft service‑side update (Jan 15, 2026) for Copilot Studio; Google mitigations are built into Gemini service – no separate patch required.
- **Active Exploitation:** No confirmed widespread active exploitation has been reported.
- **Threat Actors:** None known
- **Mitigation:** Google: layered defenses including prompt‑injection content classifiers, security thought reinforcement, markdown sanitization, suspicious URL redaction, user‑confirmation framework, and end‑user security notifications. Microsoft: restrict Copilot Studio access, audit environments, rotate secrets, enforce least‑privilege runtime controls, and apply service‑side remediation.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/ https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-21520

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Exploitation of publicly known CVEs in router operating systems (e.g., CVE‑2023‑20198, CVE‑2018‑0171) allows initial access; attackers then modify router configurations, employ virtualized containers on devices, and create GRE/IPsec tunnels or static routes to pivot and exfiltrate data.
- **Affected Products:** Cisco IOS, Cisco IOS XE, Cisco NX‑OS, Ivanti Connect Secure, Ivanti Policy Secure, other network appliances
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public tooling and PoCs (e.g., siet.py, map.tcl, tclproxy.tcl) are referenced in the advisory and CVE records.
- **Patch Available:** Vendors (e.g., Cisco, Ivanti) have published patches for the listed CVEs; organisations should apply vendor‑recommended updates.
- **Active Exploitation:** Confirmed active exploitation reported by authoring agencies; actors have exploited publicly known CVEs since at least 2021.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching; disable unused ports/protocols; change default administrative credentials; require public‑key authentication; use vendor‑recommended OS versions; monitor configurations; harden credentials and services.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** The actors exploit publicly disclosed vulnerabilities such as WinRAR's CVE-2023-38831, Outlook's NTLM flaw (CVE-2023-23397), and Roundcube flaws (CVE-2020-35730, CVE-2020-12641) through methods including exploitation of internet‑facing services, SQL injection, credential guessing, and spear‑phishing. These techniques provide initial access to corporate VPNs, mail servers, and IP cameras, enabling deeper network penetration.
- **Affected Products:** WinRAR (CVE-2023-38831), Microsoft Outlook (CVE-2023-23397), Roundcube (CVE-2020-35730, CVE-2020-12641)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit known.
- **Patch Available:** Patch information is provided via the advisory; no separate patch URL is given.
- **Active Exploitation:** Active exploitation reported in the wild.
- **Threat Actors:** APT28, Fancy Bear, Forest Blizzard, Blue Delta
- **Mitigation:** Apply security patches and firmware updates to all devices; ensure devices are supported; disable remote access if unnecessary; enable authenticated RTSP for IP cameras; utilize endpoint detection and response (EDR); implement network segmentation; enable logging and monitoring; collect and monitor Windows logs; enable attack surface reduction rules; audit IP camera accounts.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — LiteSpeed cPanel Plugin CVE-2026-48172 Exploited to Run Scripts as Root

**CVE:** `CVE-2026-48172` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://thehackernews.com/2026/05/litespeed-cpanel-plugin-cve-2026-48172.html>

> A maximum-severity security vulnerability impacting LiteSpeed User-End cPanel Plugin has come under active exploitation in the wild.

The flaw, tracked as CVE-2026-48172 (CVSS score: 10.0), relates to an instance of incorrect privilege assignment that an attacker could abuse to run arbitrary scripts with elevated permissions.

&quot;Any cPanel user (including an attacker or a compromised account) …

**Parallel AI Enrichment:**

- **Technical Details:** Incorrect privilege assignment in the LiteSpeed User-End cPanel Plugin’s lsws.redisAble handling allows any cPanel user (including unauthenticated/compromised accounts) to invoke functionality that runs arbitrary scripts with elevated (root) permissions; the vulnerability stems from mishandling of Redis enable/disable features and improper authorization checks on the endpoint.
- **Affected Products:** LiteSpeed User‑End cPanel Plugin versions 2.3 through 2.4.4 (fixed in 2.4.5)
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H
- **Exploit Available:** No public PoC or exploit URL confirmed in the sources reviewed.
- **Patch Available:** LiteSpeed released a patched plugin version 2.4.5 (updates to User-End cPanel Plugin) – upgrade to 2.4.5 or later. (Patch/advisory: https://www.litespeedtech.com/products/litespeed-web-server/control-panel-support/release-log)
- **Active Exploitation:** Confirmed active exploitation in the wild reported in multiple sources (LiteSpeed advisory and security reporting).
- **Threat Actors:** None known
- **Mitigation:** If patch cannot be applied immediately, block or audit suspicious requests invoking the lsws.redisAble/cpanel_jsonapi_func=redisAble endpoint; detect compromise with: grep -rE "cpanel_jsonapi_func=redisAble" /var/cpanel/logs /usr/local/cpanel/logs/ 2>/dev/null and investigate IPs; restrict cPanel user access, isolate affected hosts, and remove/rotate compromised credentials.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟡 High Severity — Nezha Monitoring: Nezha WebSocket server stream discloses cross-tenant server telemetry to authenticated members

**CVE:** `CVE-2026-47124` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://github.com/advisories/GHSA-hvv7-hfrh-7gxj>

> ### Summary

Any authenticated non-admin member can connect to the server-status WebSocket and receive telemetry for all servers, including servers owned by other users. The normal server list API filters objects by `HasPermission`, but the WebSocket stream treats the presence of any authenticated user as authorization for the full unfiltered server list.

### Details

The server WebSocket route i…

---

## 12. 🟡 High Severity — Nezha Monitoring: RoleMember can run shell on every server (cross-tenant RCE) via POST /api/v1/cron

**CVE:** `CVE-2026-46716` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://github.com/advisories/GHSA-99gv-2m7h-3hh9>

> ## Summary

`nezha`&#x27;s dashboard supports two user roles: `RoleAdmin` (Role==0) and `RoleMember` (Role==1). The cron routes `POST /api/v1/cron` and `PATCH /api/v1/cron/:id` are wired through `commonHandler` (any authenticated user) rather than `adminHandler`, and the per-server permission check on cron creation has a vacuous-true bypass.

A `RoleMember` user can create a scheduled cron task wi…

---

## 13. 🟡 High Severity — Arcane: Missing admin authorization on global variables endpoint

**CVE:** `CVE-2026-47125` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://github.com/advisories/GHSA-jpjh-jm2p-39hh>

> ## Summary

The `PUT /api/environments/{id}/templates/variables` endpoint, which writes the system-wide `.env.global` file used for variable substitution in every project&#x27;s compose file, is missing an admin authorization check. Any authenticated non-admin user can call this endpoint with their bearer token or API key and overwrite the global environment variables that are merged into every pr…

---

## 14. 🟡 High Severity — Parse Server: Pre-authentication denial of service via client version header regex backtracking

**CVE:** `CVE-2026-47138` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://github.com/advisories/GHSA-38m6-82c8-4xfm>

> ### Impact

An unauthenticated attacker who knows a publicly-known Parse Application ID can submit a single HTTP request whose client SDK version field contains adversarial input that triggers polynomial backtracking in a request-header parser. The parsing runs before session authentication and before rate limiting on every `/parse/*` request, so the request consumes seconds to minutes of synchron…

---

## 15. 🟡 High Severity — Nezha Monitoring: RoleMember can fire other users' cron tasks via AlertRule.FailTriggerTasks (no ownership check)

**CVE:** `CVE-2026-47120` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://github.com/advisories/GHSA-rxf6-wjh4-jfj6>

> ## Summary

`createAlertRule` and `createService` (and their `update*` siblings) accept `FailTriggerTasks []uint64` and `RecoverTriggerTasks []uint64` — IDs of cron tasks to fire when the alert/service trips. The validation function only validates the alert&#x27;s `Rules.Ignore` server map; it never checks that the cron task IDs in `FailTriggerTasks` / `RecoverTriggerTasks` belong to the caller.

…

---

## 16. 🟡 High Severity — Nezha Monitoring: RoleMember-reachable SSRF with full response-body reflection via POST /api/v1/notification

**CVE:** `CVE-2026-46717` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://github.com/advisories/GHSA-w4g9-mxgg-j532>

> ## Summary

nezha&#x27;s dashboard supports two user roles: `RoleAdmin` (Role==0) and `RoleMember` (Role==1). The notification routes `POST /api/v1/notification` and `PATCH /api/v1/notification/:id` are wired through `commonHandler` rather than `adminHandler` — so a `RoleMember` user can call them. These handlers synchronously `Send()` an HTTP request to a user-controlled URL and reflect the *enti…

---

## 17. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
