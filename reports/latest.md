# Zero Day Pulse

> **Generated:** 2026-05-23 12:57 UTC &nbsp;|&nbsp; **Total:** 18 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 11 &nbsp;|&nbsp; 🟡 High: 7 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path traversal vulnerability in the SimpleHelp web application that allows unauthenticated remote attackers to craft HTTP requests to traverse directories and download arbitrary files (e.g., configuration files, hashed passwords, SSH keys) from the host, enabling credential theft and further compromise.
- **Affected Products:** SimpleHelp (remote support / RMM) versions up to and including 5.5.7
- **CVSS Score:** 9.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N
- **Exploit Available:** true - public PoC and Metasploit auxiliary module documented (source: https://www.offsec.com/blog/cve-2024-57727/)
- **Patch Available:** true - vendor patch released (see vendor advisory URL)
- **Active Exploitation:** true - confirmed active exploitation reported by CISA (see advisory).
- **Threat Actors:** DragonForce (ransomware operators); other generic ransomware actors referenced by CISA
- **Mitigation:** Isolate or stop vulnerable SimpleHelp instances; restrict access to the SimpleHelp web interface (network‑level controls, firewalling, limit to trusted networks); apply vendor patches/upgrades immediately; disable file‑browsing functionality where possible; perform threat hunting and monitor for suspicious inbound/outbound traffic per CISA guidance.
- **Vendor Advisory:** https://simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — Drupal Core SQL Injection Bug Actively Exploited, Added to CISA KEV

**CVE:** `CVE-2026-9082` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://thehackernews.com/2026/05/drupal-core-sql-injection-bug-actively.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has added a recently patched critical security flaw impacting Drupal Core to its Known Exploited Vulnerabilities (KEV) catalog, based on evidence of active exploitation.

The vulnerability in question is CVE-2026-9082 (CVSS score: 6.5), an SQL injection vulnerability affecting all supported versions of Drupal Core.

&quot;Drupal Core

**Parallel AI Enrichment:**

- **Technical Details:** An SQL injection flaw in Drupal Core's database abstraction API allows unauthenticated attackers to craft requests that inject SQL when Drupal is using PostgreSQL, enabling limited data disclosure and integrity impact via crafted queries.
- **Affected Products:** Drupal Core (all supported versions) – sites using PostgreSQL backends
- **CVSS Score:** 6.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply the Drupal vendor patch/update immediately (per PSA 2026‑004). If immediate patching is not possible: restrict external access to affected endpoints, disable or block PostgreSQL‑based database connections from untrusted networks, implement WAF rules to detect/block exploit patterns, and review logs for suspicious queries.
- **Vendor Advisory:** https://www.drupal.org/psa-2026-004

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) attacks involve adversarial instructions embedded in web content (including hidden website code) that are processed by AI agents and can override or manipulate model behavior; attackers may seed web pages with malicious payloads to influence assistants during browsing or content ingestion.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Harden AI agents by treating external web content as untrusted, implement input sanitization, provenance checks, restrictive parsing, and policy‑based prompt filtering; follow vendor guidance in the Google blog post.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) allows attackers to embed malicious instructions into data sources, documents, or third‑party integrations that LLM‑powered applications retrieve during query processing, thereby influencing model behavior without the user directly providing the malicious input.
- **Affected Products:** Google Workspace (Gemini-integrated features)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Layered defense: input sanitization and filtering, provenance and content source validation, context‑aware retrieval controls, model output validation, rate‑limiting/tooling restrictions, continuous monitoring and adversarial testing.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The primary new threat facing all agentic browsers is indirect prompt injection, where malicious sites inject content that manipulates the AI agent's prompts, potentially causing undesired actions.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known.
- **Mitigation:** Use Chrome’s agent transparency and control features, restrict agent actions to user‑approved capabilities, validate content provenance, and apply general hardening as described in the Google post.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A race condition in the Rust‑based Android Binder implementation (rust_binder) causes unsafe removal from a death_list/doubly‑linked list, tied to concurrency and unsafe code patterns in that module.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known.
- **Mitigation:** Update to upstream patched kernel and apply Android Security Bulletins; if immediate patching unavailable, apply kernel hardening and restrict access to binder interfaces.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) embeds malicious instructions in external data sources (emails, documents, calendar invites, web content). When an AI system ingests or summarizes these sources, hidden instructions can cause data exfiltration or unsafe actions. Google’s defenses combine model‑level robustness (adversarial training, Gemini 2.5 hardening), ML classifiers to detect malicious instructions, prompt wrapping (“security thought reinforcement”) to keep models focused on user intent, sanitization/redaction of external content (images/URLs), and explicit user confirmations for risky actions.
- **Affected Products:** Gemini (Gemini 2.5 model hardening), Gemini in Google Workspace, Gemini app
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** true — https://blog.google/security/mitigating-prompt-injection-attacks/
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Layered defenses — model hardening (Gemini 2.5), prompt‑injection content classifiers, security thought reinforcement, markdown sanitization & suspicious URL redaction, user confirmation (HITL), end‑user mitigation notifications, Safe Browsing integration, adversarial training, red‑teaming, AI VRP collaboration
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** APT actors exploit publicly known CVEs and weak/reused credentials to gain footholds on edge routers and network devices. They use Guest Shell to run Python (e.g., siet.py) and TCL scripts (e.g., map.tcl, TCLproxy.tcl), modify ACLs, enable services/ports, create unauthorized accounts, and establish persistent GRE/mGRE/IPsec tunnels or SPAN/RSPAN/ERSPAN sessions to mirror traffic for collection and exfiltration.
- **Affected Products:** Cisco IOS/IOS XE (including Guest Shell/IOx and NX‑OS), Ivanti Connect Secure/Policy (CVE‑2024‑21887), Palo Alto PAN‑OS GlobalProtect (CVE‑2024‑3400), Fortinet, Juniper, Nokia routers/switches, Sierra Wireless, SonicWall
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true - https://media.defense.gov/2025/Aug/22/2003786665/-1/-1/0/CSA_COUNTERING_CHINA_STATE_ACTORS_COMPROMISE_OF_NETWORKS.PDF
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching known exploited CVEs, disable unused ports and protocols, enforce strong credentials and public‑key authentication, limit management‑plane access, monitor logs and configuration for unexpected ACLs, ports, containers, or packet‑mirror settings, verify firmware/software integrity with hash checks, apply vendor hardening guidance (e.g., Cisco IOS/IOS XE hardening, Cisco Software Checker), perform threat hunting and coordinate with authorities.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Actors used spearphishing with malicious attachments and links leveraging the WinRAR CVE‑2023‑38831, exploited internet‑facing infrastructure (VPNs, SQLi), manipulated mailbox permissions in Exchange/Office365 for sustained email collection, moved laterally with Impacket/PsExec/RDP, harvested AD credentials (Get‑GPPPassword.py, ldap‑dump.py), archived data and exfiltrated it via an OpenSSH binary.
- **Affected Products:** WinRAR (CVE-2023-38831), Microsoft Outlook (CVE-2023-23397), Roundcube Webmail (CVE-2020-35730, CVE-2020-12641)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** GRU 85th Main Special Service Center (85th GTsSS), military unit 26165 — tracked as APT28 / Fancy Bear / Forest Blizzard / Blue Delta
- **Mitigation:** Increase monitoring and threat hunting; deploy EDR; collect and monitor Windows logs; enable Windows attack surface reduction rules and hardening; audit and secure IP camera accounts; review remote access authentication; rotate credentials, enforce MFA, restrict privileged account usage, remediate referenced CVEs by applying vendor patches.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — LiteSpeed cPanel Plugin CVE-2026-48172 Exploited to Run Scripts as Root

**CVE:** `CVE-2026-48172` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://thehackernews.com/2026/05/litespeed-cpanel-plugin-cve-2026-48172.html>

> A maximum-severity security vulnerability impacting LiteSpeed User-End cPanel Plugin has come under active exploitation in the wild.

The flaw, tracked as CVE-2026-48172 (CVSS score: 10.0), relates to an instance of incorrect privilege assignment that an attacker could abuse to run arbitrary scripts with elevated permissions.

&quot;Any cPanel user (including an attacker or a compromised account) …

**Parallel AI Enrichment:**

- **Technical Details:** An incorrect privilege assignment in the lsws.redisAble function allows any cPanel user to execute arbitrary scripts with root privileges, which can be detected via cpanel_jsonapi_func=redisAble calls in logs.
- **Affected Products:** LiteSpeed User-End cPanel Plugin versions 2.3 through 2.4.4
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Upgrade to the patched plugin versions; if unable, uninstall the user-end plugin using /usr/local/lsws/admin/misc/lscmctl cpanelplugin --uninstall and monitor logs for cpanel_jsonapi_func=redisAble calls.
- **Vendor Advisory:** https://blog.litespeedtech.com/2026/05/21/security-update-for-litespeed-cpanel-plugin/

---

## 11. 🟠 Zero-Day — Trend Micro warns of Apex One zero-day exploited in the wild

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-05-22
**Reference:** <https://www.bleepingcomputer.com/news/security/trend-micro-warns-of-apex-one-zero-day-exploited-in-attacks/>

> Japanese cybersecurity software company Trend Micro has addressed an Apex One zero-day vulnerability exploited in attacks targeting Windows systems. [...]

---

## 12. 🟡 High Severity — Nezha Monitoring: Nezha WebSocket server stream discloses cross-tenant server telemetry to authenticated members

**CVE:** `CVE-2026-47124` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://github.com/advisories/GHSA-hvv7-hfrh-7gxj>

> ### Summary

Any authenticated non-admin member can connect to the server-status WebSocket and receive telemetry for all servers, including servers owned by other users. The normal server list API filters objects by `HasPermission`, but the WebSocket stream treats the presence of any authenticated user as authorization for the full unfiltered server list.

### Details

The server WebSocket route i…

---

## 13. 🟡 High Severity — Nezha Monitoring: RoleMember can run shell on every server (cross-tenant RCE) via POST /api/v1/cron

**CVE:** `CVE-2026-46716` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://github.com/advisories/GHSA-99gv-2m7h-3hh9>

> ## Summary

`nezha`&#x27;s dashboard supports two user roles: `RoleAdmin` (Role==0) and `RoleMember` (Role==1). The cron routes `POST /api/v1/cron` and `PATCH /api/v1/cron/:id` are wired through `commonHandler` (any authenticated user) rather than `adminHandler`, and the per-server permission check on cron creation has a vacuous-true bypass.

A `RoleMember` user can create a scheduled cron task wi…

---

## 14. 🟡 High Severity — Arcane: Missing admin authorization on global variables endpoint

**CVE:** `CVE-2026-47125` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://github.com/advisories/GHSA-jpjh-jm2p-39hh>

> ## Summary

The `PUT /api/environments/{id}/templates/variables` endpoint, which writes the system-wide `.env.global` file used for variable substitution in every project&#x27;s compose file, is missing an admin authorization check. Any authenticated non-admin user can call this endpoint with their bearer token or API key and overwrite the global environment variables that are merged into every pr…

---

## 15. 🟡 High Severity — Parse Server: Pre-authentication denial of service via client version header regex backtracking

**CVE:** `CVE-2026-47138` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://github.com/advisories/GHSA-38m6-82c8-4xfm>

> ### Impact

An unauthenticated attacker who knows a publicly-known Parse Application ID can submit a single HTTP request whose client SDK version field contains adversarial input that triggers polynomial backtracking in a request-header parser. The parsing runs before session authentication and before rate limiting on every `/parse/*` request, so the request consumes seconds to minutes of synchron…

---

## 16. 🟡 High Severity — Nezha Monitoring: RoleMember can fire other users' cron tasks via AlertRule.FailTriggerTasks (no ownership check)

**CVE:** `CVE-2026-47120` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://github.com/advisories/GHSA-rxf6-wjh4-jfj6>

> ## Summary

`createAlertRule` and `createService` (and their `update*` siblings) accept `FailTriggerTasks []uint64` and `RecoverTriggerTasks []uint64` — IDs of cron tasks to fire when the alert/service trips. The validation function only validates the alert&#x27;s `Rules.Ignore` server map; it never checks that the cron task IDs in `FailTriggerTasks` / `RecoverTriggerTasks` belong to the caller.

…

---

## 17. 🟡 High Severity — Nezha Monitoring: RoleMember-reachable SSRF with full response-body reflection via POST /api/v1/notification

**CVE:** `CVE-2026-46717` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://github.com/advisories/GHSA-w4g9-mxgg-j532>

> ## Summary

nezha&#x27;s dashboard supports two user roles: `RoleAdmin` (Role==0) and `RoleMember` (Role==1). The notification routes `POST /api/v1/notification` and `PATCH /api/v1/notification/:id` are wired through `commonHandler` rather than `adminHandler` — so a `RoleMember` user can call them. These handlers synchronously `Send()` an HTTP request to a user-controlled URL and reflect the *enti…

---

## 18. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
