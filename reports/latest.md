# Zero Day Pulse

> **Generated:** 2026-05-27 02:09 UTC &nbsp;|&nbsp; **Total:** 32 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 18 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated path traversal in SimpleHelp that lets remote attackers download arbitrary files by sending specially crafted HTTP requests.
- **Affected Products:** SimpleHelp Remote Monitoring and Management versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof-of-concept/weaponized exploit reported (see SecurityWeek).
- **Patch Available:** Patches released in SimpleHelp versions 5.5.8, 5.4.10, and 5.3.9
- **Active Exploitation:** Confirmed active exploitation reported by CISA (AA25-163A) and FortiGuard.
- **Threat Actors:** DragonForce ransomware group and other ransomware operators
- **Mitigation:** Upgrade to the patched SimpleHelp versions; if patching is not possible, isolate or block internet‑exposed SimpleHelp servers, conduct threat hunting, and monitor network traffic per CISA guidance.
- **Vendor Advisory:** https://simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — KnowledgeDeliver flaw exploited as a zero-day to install web shells

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://www.bleepingcomputer.com/news/security/knowledgedeliver-flaw-exploited-as-a-zero-day-to-install-web-shells/>

> Hackers exploited a critical zero-day vulnerability in a server running the KnowledgeDeliver learning management system (LMS) to deploy the Godzilla web shell. [...]

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability arises from hard‑coded identical ASP.NET machineKey values in KnowledgeDeliver’s web.config. Attackers can craft signed ViewState payloads that the server accepts and deserializes, achieving unauthenticated remote code execution and in‑memory deployment of the BLUEBEAM/Godzilla web shell.
- **Affected Products:** Digital Knowledge KnowledgeDeliver (versions released before February 24, 2026)
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept is available.
- **Patch Available:** Patch available: Vendor released fixes after Feb 24 2026 — update KnowledgeDeliver to versions released after Feb 24 2026.
- **Active Exploitation:** Yes — confirmed active exploitation in the wild, reported by Mandiant, Google Cloud Threat Intelligence, BleepingComputer, and SecurityWeek.
- **Threat Actors:** Unknown specific group; an unknown threat actor observed by Mandiant deployed the BLUEBEAM/Godzilla web shell.
- **Mitigation:** Rotate and generate unique, cryptographically strong ASP.NET machineKey values in web.config for each deployment; update KnowledgeDeliver to versions released after Feb 24 2026; restrict LMS access to trusted IP ranges; implement WAF rules to block suspicious __VIEWSTATE payloads; disable ViewState if possible; monitor for indicators such as large/malformed __VIEWSTATE, IIS deserialization errors, w3wp.exe spawning, and web‑shell artifacts.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — Hackers Exploited KnowledgeDeliver Zero-Day for Web Shell Deployment

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://www.securityweek.com/hackers-exploited-knowledgedeliver-zero-day-for-web-shell-deployment/>

> Hardcoded machineKey values in a configuration file enabled ViewState deserialization attacks leading to remote code execution. The post Hackers Exploited KnowledgeDeliver Zero-Day for Web Shell Deployment appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Hard‑coded ASP.NET machineKey values allow attackers to craft a malicious ViewState payload that bypasses validation and deserializes arbitrary objects, resulting in remote code execution.
- **Affected Products:** Digital Knowledge KnowledgeDeliver (all deployments prior to February 24, 2026)
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** No public proof-of-concept available; exploitation observed in the wild.
- **Patch Available:** Vendor released patches for Digital Knowledge KnowledgeDeliver in versions released after February 24, 2026.
- **Active Exploitation:** Confirmed active exploitation reported by Mandiant, with attackers deploying Godzilla web shells and Cobalt Strike backdoors.
- **Threat Actors:** Mandiant reported attackers deploying Godzilla web shells and Cobalt Strike; no specific APT identified.
- **Mitigation:** Update KnowledgeDeliver to versions released after February 24, 2026; audit and replace hard‑coded machineKey values with unique cryptographically strong keys; restrict access to the application; implement WAF rules to block malicious ViewState payloads; monitor for large or malformed __VIEWSTATE parameters and web‑shell indicators.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — Iranian Hackers Deploy MiniFast and MiniJunk V2 via Phishing and SEO Poisoning

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://thehackernews.com/2026/05/iranian-hackers-deploy-minifast-and.html>

> The Iranian state-sponsored threat actor known as Nimbus Manticore (aka Screening Serpens and UNC1549) has been attributed to a fresh campaign using lures impersonating organizations in the aviation and software sectors across the U.S., Europe, and the Middle East following the joint U.S.-Israeli military campaign against the country in late February 2026.

The activity, besides embracing

**Parallel AI Enrichment:**

- **Technical Details:** The actor used SEO‑poisoned search results and spear‑phishing lures impersonating aviation and software vendors to deliver installers/attachments that deploy MiniFast (an AI‑assisted backdoor) and MiniJunk V2. Delivery included malicious installers and hosting via cloud services (e.g., Microsoft Azure) and side‑loading/injection techniques to run within legitimate process contexts.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit reported.
- **Patch Available:** Patch unavailable.
- **Active Exploitation:** Confirmed active exploitation reported by The Hacker News and Check Point Research (campaigns in May 2026 using MiniFast and MiniJunk V2 via phishing and SEO poisoning).
- **Threat Actors:** Nimbus Manticore (aka Screening Serpens, UNC1549)
- **Mitigation:** Harden email defenses and user awareness; block known malicious domains and SEO-poisoned URLs; deploy/ensure EDR and up‑to‑date AV with behavioral detection; restrict execution from user download folders; apply least‑privilege and MFA for accounts; monitor for indicators of compromise reported by vendors/researchers.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an AI system processes untrusted content—such as a website, email, or document—that contains malicious instructions, allowing attackers to embed prompts that the model may execute.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept or weaponized exploit is currently available.
- **Patch Available:** No official vendor "patch" for IPI; see Google Security Blog for mitigation information.
- **Active Exploitation:** Limited malicious instances observed; no evidence of large‑scale, sophisticated active exploitation.
- **Threat Actors:** None known
- **Mitigation:** Apply layered defenses: model hardening, red‑team testing, AI Vulnerability Reward Program, content sanitization, prompt validation, and rate/timeout controls.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) involves attackers injecting malicious instructions into data or tools consumed by LLMs, influencing model behavior without direct user input. The vulnerability arises from complex AI applications that integrate multiple data sources, such as Google Workspace with Gemini, allowing crafted content or tool outputs to steer the model.
- **Affected Products:** Google Workspace features integrating Gemini (e.g., Gmail, Docs).
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept or weaponized exploit is linked in the advisory.
- **Patch Available:** No single patch available; defenses are described in the advisory.
- **Active Exploitation:** No confirmed public reports of active exploitation are mentioned in the advisory.
- **Threat Actors:** None known
- **Mitigation:** Google recommends layered defenses: deterministic defenses (user confirmation, URL sanitization, tool‑chaining policies, centralized policy engine, quick config point‑fixes), ML‑based defenses (retraining on synthetic attack variants), LLM‑based defenses (prompt engineering), and Gemini model hardening, supplemented by continuous red‑teaming and VRP engagement.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) allows malicious content on web pages or third‑party resources to manipulate the instructions or context of an AI agent in Chrome’s agentic browsing, causing the agent to perform unintended or unsafe actions.
- **Affected Products:** Google Chrome (agentic browsing / Gemini‑in‑Chrome features) — versions with agentic capabilities rolled out starting Dec 2025.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit reported.
- **Patch Available:** Apply the latest Chrome updates that include the layered security features for agentic browsing.
- **Active Exploitation:** Google observed an increase in indirect prompt injection attempts on public sites but did not report confirmed widespread active exploitation; researchers/Google flagged rising attempts.
- **Threat Actors:** None known
- **Mitigation:** Apply the latest Chrome updates; enable Chrome’s agentic‑safety features and layered defenses as described by Google; follow the guidance in the advisory.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Google reports that shifting new Android code toward Rust and focusing on memory‑safety in new code reduced memory‑safety vulnerability density substantially in 2025, with memory‑safety vulnerabilities falling below 20% of total vulnerabilities; covers changes across C/C++ and Rust adoption.
- **Affected Products:** Android platform (first-party and third-party open-source components written in C, C++, Java, Kotlin and Rust)
- **CVSS Score:** -999.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** None known
- **Patch Available:** Official vendor advisory describes adoption of Rust and platform changes; no single patch or CVE-specific fix URL provided in advisory
- **Active Exploitation:** No confirmed active exploitation reported in the advisory
- **Threat Actors:** None known
- **Mitigation:** Continue migrating new code to memory-safe languages (Rust), apply standard Android security updates, follow vendor guidance in advisory
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection embeds malicious instructions inside external data sources (web pages, documents, emails, calendar invites). When an LLM ingests that data (via browsing, document parsing, or context assembly), the hidden instructions can influence model outputs to exfiltrate secrets or perform unauthorized actions.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit known.
- **Patch Available:** No vendor patch; guidance/advisory published at the URL above.
- **Active Exploitation:** Confirmed increase in indirect prompt injection attempts in the wild per Google analysis and independent research (reports from Google, X‑Labs, Forcepoint and others).
- **Threat Actors:** None known.
- **Mitigation:** Layered defenses — input sanitization and provenance checks, restrict or disable autonomous browsing of untrusted external content, prompt allowlisting and hardening, require user confirmation before sensitive actions, least‑privilege access for models, telemetry and monitoring for anomalous model behavior.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors exploit known CVEs and misconfigurations to gain initial access to edge/backbone routers, then modify router configurations and firmware, create accounts, alter AAA/TACACS+ settings, enable packet capture (Embedded Packet Capture/PCAP), create SPAN/RSPAN/ERSPAN sessions, change ACLs, open ports, execute Tcl scripts, use SNMP and SSH for command execution, and mirror/capture traffic to collect credentials and pivot to other networks.
- **Affected Products:** Cisco IOS and IOS XE devices (including routers), broadly: backbone routers, PE and CE routers; advisory notes potential targeting of Fortinet firewalls, Juniper firewalls, Microsoft Exchange, Nokia routers/switches, Sierra Wireless devices, SonicWall (Exact versions not enumerated) — Affected products unavailable for specific versions.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No zero-day exploitation observed; actors exploit publicly known CVEs (examples cited by industry: CVE-2023-20198, CVE-2018-0171, CVE-2023-20273, CVE-2024-21887, CVE-2024-3400). No public PoC/weaponized exploit URL specified in the advisory.
- **Patch Available:** Vendors (e.g., Cisco, Ivanti, Palo Alto) have released patches for specific CVEs referenced; advisory links to vendor hardening resources but does not list a single vendor patch URL. Patch/advisory URLs: CISA advisory (above) links to Cisco resources: Cisco Software Checker and hardening guides.
- **Active Exploitation:** Yes — confirmed active exploitation in the wild of routers and infrastructure via publicly known CVEs and configuration weaknesses; advisory and allied reporting describe persistent, long-term operations and exploitation of known CVEs. Sources: CISA advisory, SecurityWeek, Canadian Centre for Cyber Security.
- **Threat Actors:** Salt Typhoon; OPERATOR PANDA; RedMike; UNC5807; GhostEmperor
- **Mitigation:** Prioritize patching known exploited CVEs; disable unused ports/protocols; use encrypted/authenticated management protocols (SSH/SFTP/HTTPS); change default credentials; require public-key authentication for admin roles; perform firmware/software integrity/hash verification; monitor logs and configurations; validate runtime image integrity; follow vendor hardening guides (Cisco IOS/IOS XE hardening); enforce network segmentation and disable unneeded services.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 11. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 12. 🟠 Zero-Day — XWiki Platform vulnerable to potential arbitrary file writing using path traversal from (subwiki) admin

**CVE:** `CVE-2026-48047` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-vgwr-23fq-pr7g>

> ### Impact
A potential path traversal vulnerability allow an attacker who manages to get a malicious WebJar extension installed on the wiki to write arbitrary files. While the consequences could be severe like overriding configuration files and setting the superadmin password, the attack first requires that the attacker already has admin access to at least a subwiki to be able to install a malicio…

---

## 13. 🟠 Zero-Day — CISA orders feds to patch actively exploited Drupal vulnerability

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-drupal-vulnerability/>

> CISA has given U.S. government agencies until Wednesday evening to secure their servers against an SQL injection vulnerability in the Drupal content management system (CMS) that it flagged as actively exploited. [...]

---

## 14. 🟠 Zero-Day — KnowledgeDeliver LMS Flaw Exploited to Deploy Godzilla and Cobalt Strike

**CVE:** `CVE-2026-5426` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://thehackernews.com/2026/05/knowledgedeliver-lms-flaw-exploited-to.html>

> A now-patched high-severity security flaw affecting Digital Knowledge KnowledgeDeliver, a Learning Management System (LMS) popular in Japan, was exploited as a zero-day to deliver the Godzilla web shell and ultimately facilitate the deployment of Cobalt Strike Beacon.

The vulnerability, tracked as CVE-2026-5426 (CVSS score: 7.5), stems from the use of hard-coded ASP.NET machine keys, leading to

---

## 15. 🟡 High Severity — @hapi/wreck leaks sensitive `Proxy-Authorization` header across cross-hostname redirects

**CVE:** `CVE-2026-44979` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-vhjm-w67q-g75c>

> ### Impact
When `@hapi/wreck` follows a 3xx redirect to a different hostname, only the `Authorization` and `Cookie` headers are stripped. The standard credential header `Proxy-Authorization` is forwarded intact to the redirect target, potentially exposing forward-proxy credentials to a host outside the original trust boundary.

Redirect following is opt-in. The redirects option defaults to false (…

---

## 16. 🟡 High Severity — LiquidJS's `{% render %}` tag silently bypasses per-render `ownPropertyOnly:true` via `Context.spawn()`

**CVE:** `CVE-2026-44646` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-9x9p-qf8f-mvjg>

> ## Summary

`Context.spawn()` in liquidjs creates a child `Context` for the `{% render %}` tag but does not propagate the parent context&#x27;s resolved `ownPropertyOnly` value. The new context re-derives `ownPropertyOnly` from `opts.ownPropertyOnly` (the instance-level option), silently discarding any `RenderOptions.ownPropertyOnly` override that was supplied to `parseAndRender()`. As a result, a…

---

## 17. 🟡 High Severity — LiquidJS's strip_html filter bypass via newline characters in HTML tags enables XSS

**CVE:** `CVE-2026-44644` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-2qv6-9wx5-cwv4>

> ## Summary

The `strip_html` filter in liquidjs is intended to remove HTML tags from a string before rendering, and is widely used as an XSS sanitizer. The implementation uses a regex whose catch-all branch (`&lt;.*?&gt;`) does not match line terminators, so any HTML tag containing a `\n` or `\r` character passes through unmodified. An attacker who can place a newline inside a tag (e.g. `&lt;img\n…

---

## 18. 🟡 High Severity — Yamcs Vulnerable to Server-Side Code Injection (RCE) via Janino Expression Engine in `JavaExprAlgorithmExecutionFactory`

**CVE:** `CVE-2026-44632` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-524g-x36v-9wm6>

> ### Summary
A Server-Side Code Injection vulnerability exists in the Yamcs algorithm evaluation engine (`org.yamcs.algorithms.JavaExprAlgorithmExecutionFactory`). The application dynamically compiles and evaluates user-controlled algorithm text without enforcing a secure sandbox. An authenticated user with the `ChangeMissionDatabase` privilege can exploit this to achieve Remote Code Execution (RCE…

---

## 19. 🟡 High Severity — Yamcs vulnerable to unauthorized user enumeration via IAM API endpoints

**CVE:** `CVE-2026-44595` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-p2rj-mrmc-9w29>

> ### Summary

The IAM API endpoints (`listUsers`, `getUser`, `listGroups`, and `getGroup`) in `yamcs-core` do not enforce the required `SystemPrivilege.ControlAccess` check. As a result, **any authenticated user** (even those with low or no privileges) can enumerate all user accounts in the system, including their usernames, superuser status, and group memberships.

This constitutes a broken access…

---

## 20. 🟡 High Severity — Kirby CMS has pre-authentication path traversal and PHP file inclusion during user lookup

**CVE:** `CVE-2026-44177` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-9hx7-c53c-v6x8>

> ### TL;DR

This vulnerability affects all Kirby sites on Kirby 5.3.0-5.4.0 and is independent from setup conditions and authentication.

**This vulnerability is of high severity for all Kirby sites**.

----

### Introduction

Path traversal is a type of attack that allows to access arbitrary filesystem paths. By using special elements such as `..` and `/` separators, attackers can escape outside o…

---

## 21. 🟡 High Severity — Kirby CMS vulnerable to cross-site scripting (XSS) from list field content in the site frontend

**CVE:** `CVE-2026-44175` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-5fhx-9q32-q257>

> ### TL;DR

This vulnerability affects all Kirby sites that use the list field or list block, when content is authored by users who may not be fully trusted. The attack requires an authenticated Panel user with update permission to any list field or list block.

**This vulnerability is of high severity for affected sites.**

Kirby sites are *not* affected if they don&#x27;t use the list field (or b…

---

## 22. 🟡 High Severity — Kirby CMS has an Arbitrary Method Call via REST API Search and Collection Query Endpoints

**CVE:** `CVE-2026-44174` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-86rh-h242-j8xp>

> ### TL;DR

This vulnerability affects all Kirby sites that might have potential attackers in the group of authenticated Panel users.

**This vulnerability is of high severity for affected sites and has a high real-world impact.**

----

### Introduction

Arbitrary method call is a type of arbitrary code execution. It is a vulnerability that allows attackers to run any commands or code of the attac…

---

## 23. 🟡 High Severity — FUXA Vulnerable to Unauthenticated Remote Code Execution via Script Test Mode Authorization Bypass

**CVE:** `CVE-2026-43947` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-rg3m-cfq7-g6h6>

> ### Summary

An unauthenticated Remote Code Execution vulnerability exists in FUXA when `secureEnabled` is set to `true`. The `POST /api/runscript` endpoint checks authorization against the stored script&#x27;s permission by ID, but when `test: true` is set in the request, it compiles and executes attacker-supplied code instead of the stored script&#x27;s code. An unauthenticated attacker who know…

---

## 24. 🟡 High Severity — FUXA Vulnerable to Pre-auth RCE via Path Manipulation & Configuration Injection

**CVE:** `CVE-2026-43945` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-p69w-mmfv-xrfj>

> **Pre-auth** RCE in FUXA via Logic Bypass

Summary

A Critical vulnerability chain exists in FUXA (v.1.3.0-2706) that allows an unauthenticated remote attacker to achieve Full Remote Code Execution (RCE) as root. The exploit succeeds even when the platform is configured in its most secure state (Secure Mode Enabled and Node-RED Secure Auth Enabled).

Details
The vulnerability is a Path Confusion f…

---

## 25. 🟡 High Severity — Yamcs Vulnerable to LDAP Injection in LdapAuthModule

**CVE:** `CVE-2026-42568` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-cqh3-jg8p-336j>

> ### Summary

An LDAP injection vulnerability exists in `org.yamcs.security.LdapAuthModule` when constructing search filters. The username parameter is inserted directly into the LDAP filter without proper RFC 4515 escaping.

### Root Cause

**File:** `yamcs-core/src/main/java/org/yamcs/security/LdapAuthModule.java:233`

The `username` parameter is inserted directly into an LDAP search filter witho…

---

## 26. 🟡 High Severity — netty-incubator-codec-ohttp's HPKEContext operations may produce empty byte[] on failures

**CVE:** `CVE-2026-41207` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-f659-372h-6x3x>

> HKDF_expand: returns non-NULL on failure. The byte[] is filled with zeros and has no way to distinguish success from failure. Since this output is used as HKDF key material for the response AEAD, a  failure silently produces an all-zero key.

When EVP_HPKE_CTX_export fails it also returns an empty byte[] array filled with zeros. This byte[] feeds directly into OHttpCrypto.createResponseAEAD(...). …

---

## 27. 🟡 High Severity — XWiki Platform's Livetable results still allow reconstructing password hashes using 768 requests

**CVE:** `CVE-2026-48048` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-rh28-mqj4-8x59>

> ### Impact
XWiki discovered that the patch for GHSA-5cf8-vrr8-8hjm was insufficient and with slightly modified parameters to the `LiveTableResults`, it is still possible to discover password hashes one bit at a time, so with 768 requests, the full password salt and hash can be retrieved of a user.

### Patches
The check for password (and email properties) has been adjusted in XWiki 18.0.0RC1, 17.1…

---

## 28. 🟡 High Severity — Typebot has Stored XSS via Rating Block Custom Icon that Bypasses isUnsafe Sandbox in Builder Preview

**CVE:** `CVE-2026-28445` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-6m7c-xfhp-p9fh>

> ## Summary
The rating block&#x27;s custom icon feature accepts arbitrary HTML/SVG via the `customIcon.svg` field and renders it using Solid&#x27;s `innerHTML` directive without any sanitization. When a malicious typebot is imported or crafted by a workspace collaborator, the payload executes in the builder&#x27;s DOM context (builder.typebot.io), bypassing the `isUnsafe` Web Worker sandbox that pr…

---

## 29. 🟡 High Severity — Reconciling the Past: Correcting Records for Unfixed Kubernetes CVEs

**CVE:** `CVE-2020-8561` | `CVE-2020-8562` | `CVE-2021-25740` | `CVE-2020-8554` &nbsp;|&nbsp; **Source:** Kubernetes Security Announcements &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://kubernetes.io/blog/2026/05/26/reconciling-unfixed-kubernetes-cves/>

> The Kubernetes project relies on transparency to empower cluster administrators and security researchers. One important way we do that is by publishing CVE records into the Common Vulnerabilities and Exposures database. As part of our ongoing effort to mature the official Kubernetes CVE Feed , we have identified some discrepancies. CVE records for a few older, unfixed issues incorrectly include a …

---

## 30. 🟡 High Severity — Weblate has a Server-Side Request Forgery issue

**CVE:** `CVE-2025-66407` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-hfpv-mc5v-p9mm>

> ### Impact
The Create Component functionality in Weblate allows authorized users to add new translation components by specifying both a version control system and a source code repository URL to pull from. However, the repository URL field is not validated or sanitized, allowing an attacker to supply arbitrary protocols, hostnames, and IP addresses, including localhost, internal network addresses,…

---

## 31. 🟡 High Severity — Microsoft Patches SharePoint RCE Flaw CVE-2026-45659 Across Server Versions

**CVE:** `CVE-2026-45659` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://thehackernews.com/2026/05/microsoft-patches-sharepoint-rce-flaw.html>

> Microsoft has rolled out updates to fix a remote code execution vulnerability impacting SharePoint that could be exploited by bad actors in attacks without requiring any specialized conditions to be met.

The vulnerability, tracked as CVE-2026-45659, carries a CVSS score of 8.8. It has been assigned an important severity.

&quot;Deserialization of untrusted data in Microsoft Office SharePoint allo…

---

## 32. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
