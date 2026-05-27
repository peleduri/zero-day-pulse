# Zero Day Pulse

> **Generated:** 2026-05-27 08:59 UTC &nbsp;|&nbsp; **Total:** 30 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 18 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Multiple path traversal vulnerabilities in SimpleHelp remote support software v5.5.7 and earlier enable unauthenticated remote attackers to traverse directories and access or manipulate files on the server.
- **Affected Products:** SimpleHelp Remote Support Software version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know)
- **Active Exploitation:** true
- **Threat Actors:** DragonForce ransomware group
- **Mitigation:** Apply the SimpleHelp patch (upgrade to a version newer than 5.5.7), restrict network access to the RMM service, and disable remote support features if they are not required.
- **Vendor Advisory:** http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — KnowledgeDeliver flaw exploited as a zero-day to install web shells

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://www.bleepingcomputer.com/news/security/knowledgedeliver-flaw-exploited-as-a-zero-day-to-install-web-shells/>

> Hackers exploited a critical zero-day vulnerability in a server running the KnowledgeDeliver learning management system (LMS) to deploy the Godzilla web shell. [...]

**Parallel AI Enrichment:**

- **Technical Details:** ViewState deserialization RCE due to identical hardcoded ASP.NET machineKey across deployments; attacker crafts signed __VIEWSTATE payloads to trigger unsafe deserialization and remote code execution, enabling in‑memory .NET web shell (BLUEBEAM/Godzilla) deployment and subsequent Cobalt Strike.
- **Affected Products:** KnowledgeDeliver (Digital Knowledge) installations deployed before Feb 24, 2026 using the vendor‑supplied web.config with hardcoded ASP.NET machineKey.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Rotate machineKey to unique cryptographically strong values for each instance; restrict LMS access to known IP ranges; monitor Windows Application event logs (Event ID 1316), w3wp.exe suspicious child processes, file integrity on .js/.aspx/.config, anomalous User-Agent strings; perform thorough investigation and remediation.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — Hackers Exploited KnowledgeDeliver Zero-Day for Web Shell Deployment

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://www.securityweek.com/hackers-exploited-knowledgedeliver-zero-day-for-web-shell-deployment/>

> Hardcoded machineKey values in a configuration file enabled ViewState deserialization attacks leading to remote code execution. The post Hackers Exploited KnowledgeDeliver Zero-Day for Web Shell Deployment appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** KnowledgeDeliver used a standardized web.config with hard‑coded ASP.NET machineKey (decryptionKey/validationKey). The shared machineKey allowed attackers to craft malicious __VIEWSTATE payloads, leading to ViewState deserialization and unauthenticated remote code execution. Exploitation resulted in in‑memory .NET web shells (BLUEBEAM/Godzilla) and subsequent Cobalt Strike deployment.
- **Affected Products:** Digital Knowledge KnowledgeDeliver (all deployments prior to 2026-02-24)
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — source: https://cloud.google.com/blog/topics/threat-intelligence/knowledgedeliver-viewstate-deserialization-vulnerability, https://www.securityweek.com/hackers-exploited-knowledgedeliver-zero-day-for-web-shell-deployment/
- **Patch Available:** true — Patch advisory URL unavailable.
- **Active Exploitation:** true — confirmed in the wild (Mandiant/Google Cloud blog; SecurityWeek).
- **Threat Actors:** Unknown threat actor(s) (Mandiant observed deployment of Godzilla/BLUEBEAM and subsequent Cobalt Strike Beacon activity)
- **Mitigation:** Rotate to unique, cryptographically strong machineKey per instance; restrict LMS access to trusted IPs; monitor ASP.NET event logs (Event ID 1316 / Event code 4009), watch w3wp.exe child processes, use file integrity monitoring for .js/.aspx/.config changes, and watch for anomalous User‑Agent strings. Hunt using the published IoCs.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** An attacker hides malicious prompt text in a web page (e.g., in comments, hidden HTML elements, or scripts). An AI agent that crawls or is fed the page reads the hidden text as part of its prompt, leading the model to follow the attacker’s instructions, which can result in data leakage, command execution, or influence over downstream tasks.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** 1. Restrict AI agents from directly ingesting arbitrary web pages; use curated data sources. 2. Implement robust input sanitization and filter hidden HTML/comments for suspicious prompts. 3. Apply prompt‑guardrails or sandboxing to validate model outputs before acting on them. 4. Monitor and log anomalous AI responses for early detection of injection attempts.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when an attacker embeds malicious instructions within external data or tools that an LLM consumes while fulfilling a user’s request. The model may follow those injected instructions because agentic workflows surface external content into the model’s context, allowing attackers to override or influence the system or user instructions.
- **Affected Products:** Google Workspace (features integrating Gemini and other LLM‑powered Workspace apps); Gemini in Workspace (no specific versions listed)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply Google's layered defenses — content‑source filtering and validation, model grounding and instruction scrubbing, strict tool/data access controls, monitoring and anomaly detection, user education and prompt design best practices; implement least‑privilege for agents and limit autonomous actions.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: untrusted web content (pages, iframes, UGC, ads) can craft text that manipulates an agent/planner model into taking unwanted actions (financial transactions, data exfiltration). Chrome’s mitigations focus on layered defenses: a separate User Alignment Critic that vets planned actions without direct access to untrusted content; Agent Origin Sets (read-only vs read-write origins) enforced by a gating function; runtime prompt‑injection classifiers; deterministic checks for sensitive navigations and actions; user confirmations for sensitive steps; and continuous red‑teaming and monitoring.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use Chrome’s layered defenses: ensure Chrome is updated (auto-update), enforce origin gating and user confirmations, rely on the User Alignment Critic and prompt‑injection classifiers, avoid sharing sensitive credentials to agents, and follow Google VRP guidance to report issues. For vendors: implement origin isolation, action‑vetting critics, real‑time injection detection, and user‑in‑the‑loop confirmations.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow in the CrabbyAVIF component of Android's media stack. The overflow would have allowed out‑of‑bounds writes, but Android's Scudo hardened allocator placed guard pages around secondary allocations, rendering the bug non‑exploitable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the latest Android platform updates that include the CrabbyAVIF patch; the Scudo hardened allocator already provides defense-in-depth by using guard pages to prevent exploitation.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) embeds malicious instructions in external data (emails, documents, calendar invites) that aim to manipulate LLM outputs or exfiltrate data. The attack vector relies on hidden instructions that the model may inadvertently execute, leading to data leakage or unauthorized actions.
- **Affected Products:** Gemini (Google Workspace), Gemini app
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Deploy layered defenses: apply vendor mitigations (Gemini model hardening and content classifiers), enable product‑provided security features (URL redaction, markdown sanitization, user confirmation prompts), train users to recognize suspicious content, and follow the Help Center guidance (https://support.google.com/docs/answer/16204578).
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** APT actors exploit publicly known CVEs and weak/default credentials on exposed edge/network devices to create unauthorized administrative accounts, enable web/management services, execute scripts (TCL/Python) or run containers (Guest Shell/IOx), modify ACLs, open ports, configure GRE/IPsec tunnels and SPAN/RSPAN/ERSPAN to mirror/exfiltrate traffic, and maintain persistent access for long‑term collection and lateral movement.
- **Affected Products:** Cisco IOS, Cisco IOS XE, Cisco NX‑OS (including Guest Shell/IOx), Ivanti Connect Secure, Ivanti Policy, Fortinet (firewalls), Juniper (firewalls/routers), Nokia routers/switches, Sierra Wireless devices, SonicWall firewalls, and other edge/network devices
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true — https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a
- **Patch Available:** true — https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a
- **Active Exploitation:** true — https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching of known exploited CVEs; disable unused ports/protocols and outbound management access; enforce strong/unique admin credentials and public‑key auth; monitor firmware/software integrity and validate hashes; monitor logs for on‑box PCAP/monitor‑session creation and suspicious ACL changes; follow vendor hardening guidance (Cisco IOS/XE/NX‑OS hardening guides).
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
- **Threat Actors:** GRU 85th GTsSS (Unit 26165) — tracked as APT28 (Russian state-sponsored)
- **Mitigation:** Follow CISA/CSA mitigations and hardening guidance in advisory (network segmentation, multi-factor authentication, monitoring/logging, patching, supply-chain risk management).
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 11. 🟠 Zero-Day — CISA Urges Immediate Patching of Exploited LiteSpeed cPanel Plugin Zero-Day

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://www.securityweek.com/cisa-urges-immediate-patching-of-exploited-litespeed-cpanel-plugin-zero-day/>

> Resolved last week, the vulnerability was exploited in the wild as a zero-day to execute scripts with root privileges. The post CISA Urges Immediate Patching of Exploited LiteSpeed cPanel Plugin Zero-Day appeared first on SecurityWeek .

---

## 12. 🟠 Zero-Day — XWiki Platform vulnerable to potential arbitrary file writing using path traversal from (subwiki) admin

**CVE:** `CVE-2026-48047` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-vgwr-23fq-pr7g>

> ### Impact
A potential path traversal vulnerability allow an attacker who manages to get a malicious WebJar extension installed on the wiki to write arbitrary files. While the consequences could be severe like overriding configuration files and setting the superadmin password, the attack first requires that the attacker already has admin access to at least a subwiki to be able to install a malicio…

---

## 13. 🟡 High Severity — @hapi/wreck leaks sensitive `Proxy-Authorization` header across cross-hostname redirects

**CVE:** `CVE-2026-44979` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-vhjm-w67q-g75c>

> ### Impact
When `@hapi/wreck` follows a 3xx redirect to a different hostname, only the `Authorization` and `Cookie` headers are stripped. The standard credential header `Proxy-Authorization` is forwarded intact to the redirect target, potentially exposing forward-proxy credentials to a host outside the original trust boundary.

Redirect following is opt-in. The redirects option defaults to false (…

---

## 14. 🟡 High Severity — LiquidJS's `{% render %}` tag silently bypasses per-render `ownPropertyOnly:true` via `Context.spawn()`

**CVE:** `CVE-2026-44646` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-9x9p-qf8f-mvjg>

> ## Summary

`Context.spawn()` in liquidjs creates a child `Context` for the `{% render %}` tag but does not propagate the parent context&#x27;s resolved `ownPropertyOnly` value. The new context re-derives `ownPropertyOnly` from `opts.ownPropertyOnly` (the instance-level option), silently discarding any `RenderOptions.ownPropertyOnly` override that was supplied to `parseAndRender()`. As a result, a…

---

## 15. 🟡 High Severity — LiquidJS's strip_html filter bypass via newline characters in HTML tags enables XSS

**CVE:** `CVE-2026-44644` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-2qv6-9wx5-cwv4>

> ## Summary

The `strip_html` filter in liquidjs is intended to remove HTML tags from a string before rendering, and is widely used as an XSS sanitizer. The implementation uses a regex whose catch-all branch (`&lt;.*?&gt;`) does not match line terminators, so any HTML tag containing a `\n` or `\r` character passes through unmodified. An attacker who can place a newline inside a tag (e.g. `&lt;img\n…

---

## 16. 🟡 High Severity — Yamcs Vulnerable to Server-Side Code Injection (RCE) via Janino Expression Engine in `JavaExprAlgorithmExecutionFactory`

**CVE:** `CVE-2026-44632` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-524g-x36v-9wm6>

> ### Summary
A Server-Side Code Injection vulnerability exists in the Yamcs algorithm evaluation engine (`org.yamcs.algorithms.JavaExprAlgorithmExecutionFactory`). The application dynamically compiles and evaluates user-controlled algorithm text without enforcing a secure sandbox. An authenticated user with the `ChangeMissionDatabase` privilege can exploit this to achieve Remote Code Execution (RCE…

---

## 17. 🟡 High Severity — Yamcs vulnerable to unauthorized user enumeration via IAM API endpoints

**CVE:** `CVE-2026-44595` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-p2rj-mrmc-9w29>

> ### Summary

The IAM API endpoints (`listUsers`, `getUser`, `listGroups`, and `getGroup`) in `yamcs-core` do not enforce the required `SystemPrivilege.ControlAccess` check. As a result, **any authenticated user** (even those with low or no privileges) can enumerate all user accounts in the system, including their usernames, superuser status, and group memberships.

This constitutes a broken access…

---

## 18. 🟡 High Severity — Kirby CMS has pre-authentication path traversal and PHP file inclusion during user lookup

**CVE:** `CVE-2026-44177` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-9hx7-c53c-v6x8>

> ### TL;DR

This vulnerability affects all Kirby sites on Kirby 5.3.0-5.4.0 and is independent from setup conditions and authentication.

**This vulnerability is of high severity for all Kirby sites**.

----

### Introduction

Path traversal is a type of attack that allows to access arbitrary filesystem paths. By using special elements such as `..` and `/` separators, attackers can escape outside o…

---

## 19. 🟡 High Severity — Kirby CMS vulnerable to cross-site scripting (XSS) from list field content in the site frontend

**CVE:** `CVE-2026-44175` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-5fhx-9q32-q257>

> ### TL;DR

This vulnerability affects all Kirby sites that use the list field or list block, when content is authored by users who may not be fully trusted. The attack requires an authenticated Panel user with update permission to any list field or list block.

**This vulnerability is of high severity for affected sites.**

Kirby sites are *not* affected if they don&#x27;t use the list field (or b…

---

## 20. 🟡 High Severity — Kirby CMS has an Arbitrary Method Call via REST API Search and Collection Query Endpoints

**CVE:** `CVE-2026-44174` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-86rh-h242-j8xp>

> ### TL;DR

This vulnerability affects all Kirby sites that might have potential attackers in the group of authenticated Panel users.

**This vulnerability is of high severity for affected sites and has a high real-world impact.**

----

### Introduction

Arbitrary method call is a type of arbitrary code execution. It is a vulnerability that allows attackers to run any commands or code of the attac…

---

## 21. 🟡 High Severity — FUXA Vulnerable to Unauthenticated Remote Code Execution via Script Test Mode Authorization Bypass

**CVE:** `CVE-2026-43947` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-rg3m-cfq7-g6h6>

> ### Summary

An unauthenticated Remote Code Execution vulnerability exists in FUXA when `secureEnabled` is set to `true`. The `POST /api/runscript` endpoint checks authorization against the stored script&#x27;s permission by ID, but when `test: true` is set in the request, it compiles and executes attacker-supplied code instead of the stored script&#x27;s code. An unauthenticated attacker who know…

---

## 22. 🟡 High Severity — FUXA Vulnerable to Pre-auth RCE via Path Manipulation & Configuration Injection

**CVE:** `CVE-2026-43945` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-p69w-mmfv-xrfj>

> **Pre-auth** RCE in FUXA via Logic Bypass

Summary

A Critical vulnerability chain exists in FUXA (v.1.3.0-2706) that allows an unauthenticated remote attacker to achieve Full Remote Code Execution (RCE) as root. The exploit succeeds even when the platform is configured in its most secure state (Secure Mode Enabled and Node-RED Secure Auth Enabled).

Details
The vulnerability is a Path Confusion f…

---

## 23. 🟡 High Severity — Yamcs Vulnerable to LDAP Injection in LdapAuthModule

**CVE:** `CVE-2026-42568` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-cqh3-jg8p-336j>

> ### Summary

An LDAP injection vulnerability exists in `org.yamcs.security.LdapAuthModule` when constructing search filters. The username parameter is inserted directly into the LDAP filter without proper RFC 4515 escaping.

### Root Cause

**File:** `yamcs-core/src/main/java/org/yamcs/security/LdapAuthModule.java:233`

The `username` parameter is inserted directly into an LDAP search filter witho…

---

## 24. 🟡 High Severity — netty-incubator-codec-ohttp's HPKEContext operations may produce empty byte[] on failures

**CVE:** `CVE-2026-41207` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-f659-372h-6x3x>

> HKDF_expand: returns non-NULL on failure. The byte[] is filled with zeros and has no way to distinguish success from failure. Since this output is used as HKDF key material for the response AEAD, a  failure silently produces an all-zero key.

When EVP_HPKE_CTX_export fails it also returns an empty byte[] array filled with zeros. This byte[] feeds directly into OHttpCrypto.createResponseAEAD(...). …

---

## 25. 🟡 High Severity — XWiki Platform's Livetable results still allow reconstructing password hashes using 768 requests

**CVE:** `CVE-2026-48048` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-rh28-mqj4-8x59>

> ### Impact
XWiki discovered that the patch for GHSA-5cf8-vrr8-8hjm was insufficient and with slightly modified parameters to the `LiveTableResults`, it is still possible to discover password hashes one bit at a time, so with 768 requests, the full password salt and hash can be retrieved of a user.

### Patches
The check for password (and email properties) has been adjusted in XWiki 18.0.0RC1, 17.1…

---

## 26. 🟡 High Severity — Typebot has Stored XSS via Rating Block Custom Icon that Bypasses isUnsafe Sandbox in Builder Preview

**CVE:** `CVE-2026-28445` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-6m7c-xfhp-p9fh>

> ## Summary
The rating block&#x27;s custom icon feature accepts arbitrary HTML/SVG via the `customIcon.svg` field and renders it using Solid&#x27;s `innerHTML` directive without any sanitization. When a malicious typebot is imported or crafted by a workspace collaborator, the payload executes in the builder&#x27;s DOM context (builder.typebot.io), bypassing the `isUnsafe` Web Worker sandbox that pr…

---

## 27. 🟡 High Severity — Reconciling the Past: Correcting Records for Unfixed Kubernetes CVEs

**CVE:** `CVE-2020-8561` | `CVE-2020-8562` | `CVE-2021-25740` | `CVE-2020-8554` &nbsp;|&nbsp; **Source:** Kubernetes Security Announcements &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://kubernetes.io/blog/2026/05/26/reconciling-unfixed-kubernetes-cves/>

> The Kubernetes project relies on transparency to empower cluster administrators and security researchers. One important way we do that is by publishing CVE records into the Common Vulnerabilities and Exposures database. As part of our ongoing effort to mature the official Kubernetes CVE Feed , we have identified some discrepancies. CVE records for a few older, unfixed issues incorrectly include a …

---

## 28. 🟡 High Severity — Weblate has a Server-Side Request Forgery issue

**CVE:** `CVE-2025-66407` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-hfpv-mc5v-p9mm>

> ### Impact
The Create Component functionality in Weblate allows authorized users to add new translation components by specifying both a version control system and a source code repository URL to pull from. However, the repository URL field is not validated or sanitized, allowing an attacker to supply arbitrary protocols, hostnames, and IP addresses, including localhost, internal network addresses,…

---

## 29. 🟡 High Severity — Microsoft Patches SharePoint RCE Flaw CVE-2026-45659 Across Server Versions

**CVE:** `CVE-2026-45659` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://thehackernews.com/2026/05/microsoft-patches-sharepoint-rce-flaw.html>

> Microsoft has rolled out updates to fix a remote code execution vulnerability impacting SharePoint that could be exploited by bad actors in attacks without requiring any specialized conditions to be met.

The vulnerability, tracked as CVE-2026-45659, carries a CVSS score of 8.8. It has been assigned an important severity.

&quot;Deserialization of untrusted data in Microsoft Office SharePoint allo…

---

## 30. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
