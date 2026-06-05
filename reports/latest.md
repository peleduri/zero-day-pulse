# Zero Day Pulse

> **Generated:** 2026-06-05 14:22 UTC &nbsp;|&nbsp; **Total:** 27 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 13 &nbsp;|&nbsp; 🟡 High: 14 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE‑2024‑57727 is a path traversal vulnerability that lets an unauthenticated attacker retrieve arbitrary files (e.g., serverconfig.xml) via crafted HTTP requests, and can be combined with privilege‑escalation and file‑upload flaws to achieve full server compromise.
- **Affected Products:** SimpleHelp Remote Support / RMM — versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Public technical disclosure and PoC‑style descriptions are available via Horizon3.ai (see source link).
- **Patch Available:** Yes — patches released in SimpleHelp versions 5.5.8 through 5.5.15. Advisory URL: https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know
- **Active Exploitation:** Confirmed – CISA added CVE‑2024‑57727 to the KEV catalog and reports ransomware actors leveraging it; multiple industry write‑ups corroborate active exploitation.
- **Threat Actors:** DragonForce, Medusa (and other ransomware groups reported)
- **Mitigation:** Isolate or stop vulnerable SimpleHelp servers, upgrade immediately, hunt for compromise indicators, block/monitor SimpleHelp network traffic, do not expose remote services to the Internet, and follow vendor guidance.
- **Vendor Advisory:** https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — What 2026 DBIR Confirms: Attacks Are Living in the Browser

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://www.bleepingcomputer.com/news/security/what-2026-dbir-confirms-attacks-are-living-in-the-browser/>

> Phishing, shadow AI, malicious extensions, and credential theft increasingly happen inside the browser. Keep Aware explains what the 2026 Verizon DBIR reveals about browser-layer security gaps and modern attacks. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Attacks operate at the browser layer via malicious or compromised browser extensions and AI plugins that collect/exfiltrate browsing context and credentials, phishing pages and credential harvesting, in‑browser command execution (ClickFix‑style) and exploitation of vulnerable browser‑facing components.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No specific public PoC or weaponized exploit for a single named vulnerability cited; exploit information unavailable.
- **Patch Available:** No specific vendor patch known; patch information unavailable.
- **Active Exploitation:** DBIR and reporting confirm active browser‑layer attacks (malicious extensions, phishing pages, credential theft, 'ClickFix' style attacks and shadow AI plugins) are occurring in the wild.
- **Threat Actors:** None known
- **Mitigation:** Apply CIS/DBIR recommendations: enforce browser extension control/whitelisting, require MFA, use DNS/web filtering, deploy browser isolation or zero‑trust browser controls, inventory and remove unauthorized AI/browser extensions, continuous vulnerability management and timely patching, endpoint anti‑malware and privilege management.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — Cisco warns of unpatched SD-WAN zero-day exploited in attacks

**CVE:** `CVE-2026-20245` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://www.bleepingcomputer.com/news/security/new-cisco-sd-wan-flaw-exploited-in-zero-day-attacks-to-gain-root/>

> On Thursday, Cisco warned of a high-severity, unpatched zero-day in the Cisco Catalyst SD-WAN Manager (tracked as CVE-2026-20245) actively exploited in attacks enabling root privilege escalation. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Insufficient validation of user-supplied input in the CLI of Cisco Catalyst SD-WAN Manager allows an authenticated, local attacker to upload a crafted file and execute arbitrary commands as root.
- **Affected Products:** Cisco Catalyst SD-WAN Manager (formerly SD-WAN vManage) – affected CLI component
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public exploit/PoC reports: news sources report active exploitation; no confirmed public PoC URL found in sources.
- **Patch Available:** Patch unavailable. Cisco states no fix currently; monitoring and mitigation guidance provided in advisory.
- **Active Exploitation:** Confirmed active exploitation reported by Cisco and multiple security news outlets (Cisco advisory, Bleeping Computer, Help Net Security).
- **Threat Actors:** None known
- **Mitigation:** Follow Cisco advisory mitigations and hardening guidance (restrict access to management interfaces, apply recommended configuration/workarounds in advisory).
- **Vendor Advisory:** https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-privesc-4uxFrdzx

---

## 4. 🟠 Zero-Day — The June 2026 AI Executive Order: What federal agencies need to know and how Tenable can help

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Tenable Security Research &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://www.tenable.com/blog/summary-june-2026-ai-executive-order-requirements>

> On June 2, 2026, the White House signed an Executive Order directing federal agencies to harden their systems with AI-enabled cyber defenses and to stand up a new AI cybersecurity clearinghouse — most of it on a 30-day clock. Here’s what the EO requires and how Tenable can help. Key takeaways: The new AI Security Executive Order will require national security and civilian federal agencies to prior…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit not applicable / Exploit information unavailable.
- **Patch Available:** Patch not applicable / Patch information unavailable.
- **Active Exploitation:** None reported / active exploitation information unavailable.
- **Threat Actors:** None known
- **Mitigation:** General mitigation and hardening guidance available in the blog (use exposure management, continuous detection, VPR prioritization, Tenable Hexa AI automation, Tenable One AI Exposure for inventory and policy enforcement).
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when adversarial content seeded on web pages is consumed by AI agents or browsing-enabled LLMs, causing the agent to follow malicious instructions or leak secrets (examples observed include financial fraud, data destruction, and API key theft via crafted web content and payloads delivered through webpages and RAG sources).
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit or PoC known.
- **Patch Available:** No vendor patch available.
- **Active Exploitation:** Confirmed active exploitation in the wild.
- **Threat Actors:** None known
- **Mitigation:** Hardening and mitigations include multi‑layered defenses: input sanitization and filtering, provenance/trust signals, browsing content validation, denylist/allowlist policies, RAG pipeline hardening, model‑level guardrails, and monitoring for anomalous agent behavior.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when adversarial instructions are embedded in external data, documents, web content, or tooling that a large language model consumes. These malicious instructions can modify the model's output even though the user did not provide direct input, leveraging the model's reliance on external sources and agentic automation.
- **Affected Products:** Google Workspace (features integrating Gemini and agentic automation)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit reported.
- **Patch Available:** Vendor does not list a single "patch"; mitigation is provided via a continuous layered strategy.
- **Active Exploitation:** Reports of in‑the‑wild indirect prompt injection payloads (Forcepoint) but no confirmed mass exploitation tied to a named threat actor.
- **Threat Actors:** None known
- **Mitigation:** Implement continuous, layered defenses: verify content provenance and trust signals, vet documents and tools before ingestion, sanitize/filter external content, restrict privileges of agentic tools, use secondary model checks for validation, enforce strict access controls, and maintain robust logging, monitoring and rapid response processes.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection—malicious or adversarial web content (including third‑party iframes or user‑generated content) can influence an agentic planner model to take unintended actions (e.g., financial transactions or data exfiltration). Chrome's mitigations include a separate User Alignment Critic that vets planned actions using only metadata, Agent Origin Sets to restrict readable and writable origins, deterministic checks for model‑generated URLs, prompt‑injection classifiers, user confirmations for sensitive steps, and continuous red‑teaming and monitoring.
- **Affected Products:** Chrome (agentic/Gemini-enabled features)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit reported
- **Patch Available:** No single patch; mitigations and features implemented in Chrome as described in the advisory; Chrome auto‑update used to deliver fixes. Vendor advisory provided.
- **Active Exploitation:** No confirmed active exploitation reported in the advisory or prior trusted research.
- **Threat Actors:** None known
- **Mitigation:** Use Chrome's layered defenses—user confirmations for sensitive actions, origin‑gating (Agent Origin Sets) limiting read vs read‑write origins, User Alignment Critic to veto misaligned actions, real‑time prompt‑injection detection, and keep Chrome auto‑updates enabled.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC or weaponized exploit mentioned in the blog post.
- **Patch Available:** Official patches are distributed via Android Security Bulletins and platform updates; specific patch URLs are not provided in the blog post.
- **Active Exploitation:** No confirmed active exploitation reported in the blog post.
- **Threat Actors:** None known
- **Mitigation:** Continue to apply Android security updates promptly; use app sandboxing and least‑privilege configurations.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) involves malicious instructions embedded in external data sources (emails, documents, calendar invites, web content) that cause AI systems to treat the content as instructions, leading to data leakage or unauthorized actions.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit known
- **Patch Available:** No vendor patch; mitigation guidance provided in advisory: http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html
- **Active Exploitation:** Reports of increased indirect prompt injection attempts in the wild have been observed by multiple vendors but no confirmed widescale active exploitation of a specific CVE.
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses per vendor advisory: treat external content as untrusted, apply input sanitization and canonicalization, enforce least privilege for model outputs and data access, add explicit instruction‑guard rails, add multi‑layer detection and telemetry, and keep models/clients updated. See vendor advisory for details.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors gain initial access by exploiting publicly known CVEs (e.g., CVE‑2023‑20198) using the Web Services Management Agent endpoints to bypass authentication and create unauthorized admin accounts. Persistence is achieved by modifying ACLs to allow attacker‑controlled IPs, opening standard/non‑standard ports (SSH, SFTP, RDP, FTP, HTTP/HTTPS), and enabling HTTP/HTTPS servers on Cisco devices. After compromise, they execute commands via SNMP, SSH, web UI, and TCL scripts, and use SPAN/RSPAN/ERSPAN to capture in‑transit traffic for collection of subscriber data, configurations, and credentials.
- **Affected Products:** Cisco IOS / IOS XE (CVE-2018-0171, CVE-2023-20198, CVE-2023-20273); Ivanti (CVE-2024-21887, CVE-2023-46805); Palo Alto Networks (CVE-2024-3400); also potentially Fortinet firewalls, Juniper firewalls, Microsoft Exchange, Nokia routers & switches, Sierra Wireless devices, SonicWall firewalls.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept URLs are provided; however, publicly available tools such as siet.py, map.tcl, tclproxy.tcl, and wodSSHServer are referenced as being used by the actors.
- **Patch Available:** Vendor patches are available from the affected vendors (e.g., Cisco, Ivanti, Palo Alto Networks). Specific patch URLs are not provided in the advisory.
- **Active Exploitation:** Confirmed active exploitation in the wild has been reported; the actors have successfully exploited publicly known CVEs to gain persistent access to government, telecom, transportation, lodging, and military infrastructure networks globally.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Disable all unused ports and protocols; change default administrative credentials; require public‑key authentication; use encrypted management protocols (SSH, SFTP, HTTPS); deploy vendor‑recommended OS versions and apply all security updates; follow Cisco hardening guides; monitor device logs; audit non‑root accounts; review ACL changes and traffic mirroring configurations.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 11. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 12. 🟠 Zero-Day — In Other News: Anthropic Maps AI Threats, Unpatched Comodo Flaw, Palantir Chief Eyed for CISA

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://www.securityweek.com/in-other-news-anthropic-maps-ai-threats-unpatched-comodo-flaw-palantir-chief-eyed-for-cisa/>

> Other noteworthy stories that might have slipped under the radar: Ultrahuman data leak, The Gentlemen ransomware analysis, Hola Browser bundles miner. The post In Other News: Anthropic Maps AI Threats, Unpatched Comodo Flaw, Palantir Chief Eyed for CISA appeared first on SecurityWeek .

---

## 13. 🟠 Zero-Day — Shopware: Stored XSS via SVG file upload — no SVG sanitization

**CVE:** `CVE-2026-48015` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-xvhc-gm7j-mhmc>

> SVG files are in the `allowed_extensions` whitelist and can be uploaded by any admin user via the media manager. There is zero SVG content sanitization anywhere in the upload pipeline. A malicious SVG with JavaScript (`onload`, `&lt;script&gt;`, `&lt;foreignObject&gt;`) executes in the context of the Shopware domain when accessed.

## The Problem

In `src/Core/Framework/Resources/config/packages/s…

---

## 14. 🟡 High Severity — Hackers Exploit Critical Everest Forms Pro WordPress Plugin Flaw to Take Over Sites

**CVE:** `CVE-2026-3300` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://thehackernews.com/2026/06/hackers-exploit-critical-everest-forms.html>

> Threat actors are actively exploiting a critical security flaw in Everest Forms Pro, a WordPress plugin with about 4,000 active installations, to execute arbitrary code, leading to a complete site compromise.

The vulnerability in question is CVE-2026-3300 (CVSS score: 9.8), a remote code execution bug impacting all versions of the plugin up to, and including, 1.9.12. A patch for the flaw was

---

## 15. 🟡 High Severity — AdGuard Home: DoQ-to-UDP State Reduction and Source-Port Oracle

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

## 16. 🟡 High Severity — Shopware: SSRF in Media External-Link Endpoint Bypasses IP Validation

**CVE:** `CVE-2026-48013` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-gq96-5pfx-f4vc>

> ## Summary

The `/api/_action/media/external-link` endpoint allows authenticated admin users to make server-side HTTP HEAD requests to arbitrary internal IP addresses. While the parallel `uploadFromURL` flow validates target IPs against private/reserved ranges via `FileUrlValidator`, the `linkURL` flow only performs a URL format check (regex for `http://` or `https://` prefix), allowing SSRF to in…

---

## 17. 🟡 High Severity — Shopware: Admin API ACL Bypass in Order State Transition Endpoints

**CVE:** `CVE-2026-48014` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-f8q6-3g5w-jjr6>

> ## Summary
This is a vertical authorization bypass in the Admin API affecting order state transition features (`/api/_action/order/{orderId}/state/{transition}` and similar transaction/delivery transition routes). The root cause is that the transition action routes do not declare required server-side ACL privileges, allowing low-privileged users to pass the authorization boundary. As a result, aut…

---

## 18. 🟡 High Severity — Shopware: Privilege escalation: non-admin user with user:create ACL can create admin accounts

**CVE:** `CVE-2026-48010` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-v39m-97p8-gqg7>

> `UserController::upsertUser()` writes user data in `SYSTEM_SCOPE` and does not filter the `admin` field. A non-admin API user with `user:create` or `user:update` ACL permission can set `admin: true` on new or existing users, escalating to full admin access.

## The Problem

In `src/Core/Framework/Api/Controller/UserController.php`, line 210-234:

```php
public function upsertUser(?string $userId, …

---

## 19. 🟡 High Severity — Shopware: Admin Account Takeover via User Recovery Hash Exposure

**CVE:** `CVE-2026-48009` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-8v9p-g828-v98f>

> ## Summary

A low-privilege admin user with `user_recovery:read` ACL can take over any admin account. The attacker triggers password recovery for the victim (unauthenticated endpoint), reads the recovery hash from the Admin API search endpoint, then uses the hash to reset the victim&#x27;s password (another unauthenticated endpoint). The recovery hash — intended to be secret and delivered only via…

---

## 20. 🟡 High Severity — Shopware: Privilege Escalation via Sync API Integration Admin Flag Bypass

**CVE:** `CVE-2026-48008` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-gv8p-48fr-4fxg>

> ## Summary

A non-admin API user with `integration:create` ACL privilege can escalate to full administrator by creating an integration with `admin: true` through the Sync API (`POST /api/_action/sync`). The regular integration endpoint (`POST /api/integration`) correctly blocks this, but the Sync API bypasses the controller-level check by writing directly through the DAL EntityWriter. The `integra…

---

## 21. 🟡 High Severity — Hono: JWT middleware accepts any Authorization scheme, not only Bearer

**CVE:** `CVE-2026-47673` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-f577-qrjj-4474>

> ### Summary

The `jwt` and `jwk` middlewares do not verify that the `Authorization` header value uses the`Bearer` scheme. Any two-part header value — regardless of the scheme name in the first position — proceeds to JWT verification. A request presenting a valid JWT under a non-`Bearer` scheme identifier (such as `Basic` or `Token`) is authenticated identically to a correctly formed `Bearer` reque…

---

## 22. 🟡 High Severity — epa4all-client: Unauthenticated REST API for Patient Record Writes

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

## 23. 🟡 High Severity — Nhost CLI local configserver allows cross-origin unauthenticated read/write access to local development configuration and secrets

**CVE:** `CVE-2026-47671` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-64cj-qvx5-m4f3>

> ### Summary

The hidden `nhost configserver` used by `nhost dev` exposes the Mimir GraphQL API with dummy authorization directives and permissive CORS. When a developer is running the local development environment, any process that can reach the developer&#x27;s localhost service, including a web page loaded from an arbitrary origin, can query the configserver for local Nhost configuration and sec…

---

## 24. 🟡 High Severity — Nuclio: Missing authorization on project write paths allows any authenticated user to modify or delete any project

**CVE:** `CVE-2026-45730` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-m8xg-8xg9-mxhm>

> This vulnerability exists in Nuclio Dashboard&#x27;s project management API, allowing any authenticated user (without membership in the target project) to bypass OPA authorization checks on write paths (`PUT /api/projects/{id}`, `DELETE /api/projects`) and modify or delete any project along with all its associated resources (functions, API gateways, etc.). CWE classification: CWE-862 (Missing Auth…

---

## 25. 🟡 High Severity — Matrix Rust SDK: Sender-binding gaps in to-device and room-key attribution

**CVE:** `CVE-2026-45056` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-wfq4-36m3-9g42>

> ### Impact

The `matrix-sdk-crypto` crate before 0.16.1 is missing a check for the sender&#x27;s user ID when decrypting an Olm-encrypted to-device message containing the `sender_device_keys` property.

This could be exploited to spoof the sender of an encrypted to-device message, but only if the attacker colludes with (or is) the homeserver operator.

### Patches

This issue is fixed in `matrix-s…

---

## 26. 🟡 High Severity — Doorkeeper Openid Connect: Dynamic Client Registration feature creates public clients with client_secret

**CVE:** `CVE-2026-44476` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-m6vc-f87m-cc2h>

> ### Impact

The `DynamicClientRegistrationController#register` action hard-codes `confidential: false` when creating applications (dynamic_client_registration_controller.rb:18-25), yet the response includes a client_secret and advertises `token_endpoint_auth_methods_supported: [&quot;client_secret_basic&quot;, &quot;client_secret_post&quot;]`.

Because Doorkeeper&#x27;s `Application.by_uid_and_sec…

---

## 27. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
