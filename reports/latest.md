# Zero Day Pulse

> **Generated:** 2026-05-27 14:52 UTC &nbsp;|&nbsp; **Total:** 29 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 17 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated remote attackers can exploit a path traversal vulnerability in SimpleHelp RMM 5.5.7 and earlier to retrieve logs, configuration files, and credentials, enabling further compromise.
- **Affected Products:** SimpleHelp Remote Monitoring and Management 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (https://medium.com/@RosanaFS/simplehelp-cve-2024-57727-tryhackme-walkthrough-9f88c2061fb9)
- **Patch Available:** true (http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know)
- **Active Exploitation:** true (https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a)
- **Threat Actors:** Dragonforce ransomware group
- **Mitigation:** Upgrade to SimpleHelp 5.5.8 and apply network restrictions (block public access, use IP allowlists, VPN, MFA) and rotate credentials.
- **Vendor Advisory:** http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — CISA gives feds 4 days to patch actively exploited cPanel plugin flaw

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-gives-feds-4-days-to-patch-actively-exploited-cpanel-plugin-flaw/>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has given U.S. federal agencies four days to secure their servers against a critical vulnerability in the LiteSpeed cPanel user-end plugin, which is actively being exploited in attacks. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Incorrect privilege assignment in the LiteSpeed cPanel user‑end plugin allows remote unauthenticated attackers to execute arbitrary scripts as root via privilege escalation.
- **Affected Products:** LiteSpeed User-End cPanel Plugin before 2.4.5
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Immediately update the plugin to version 2.4.5 or later; if patch unavailable, restrict access to cPanel, apply network‑level controls, and monitor for suspicious privilege‑escalation indicators.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — KnowledgeDeliver flaw exploited as a zero-day to install web shells

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://www.bleepingcomputer.com/news/security/knowledgedeliver-flaw-exploited-as-a-zero-day-to-install-web-shells/>

> Hackers exploited a critical zero-day vulnerability in a server running the KnowledgeDeliver learning management system (LMS) to deploy the Godzilla web shell. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Hard‑coded ASP.NET/IIS machineKey in the default web.config enables attackers to craft malicious ViewState payloads that are decrypted and processed by the server, resulting in remote code execution and deployment of the Godzilla web shell.
- **Affected Products:** KnowledgeDeliver LMS (versions prior to 2026-02-24)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (source: https://www.bleepingcomputer.com/news/security/knowledgedeliver-flaw-exploited-as-a-zero-day-to-install-web-shells/)
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is a technique where an attacker injects malicious content into prompts that are later used by an AI model, causing the model to produce unintended or harmful output. The blog notes that IPI is a top priority for the security community as a primary attack vector against AI agents.
- **Affected Products:** Microsoft Copilot Studio
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) enables attackers to influence LLM behavior by injecting malicious instructions into data or tools the LLM consumes, potentially without any direct user input. The attacks exploit multiple data sources and agentic automation to embed adversarial instructions that the LLM may follow when completing queries.
- **Affected Products:** Google Workspace with Gemini
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** false
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Continuous layered defenses including human and automated red‑teaming, Google AI VRP, vulnerability cataloging, synthetic data generation (Simula) to create attack variants, deterministic defenses (user confirmation, URL sanitization, tool‑chaining policies governed by a Policy Engine), ML‑based defenses retrained on synthetic attack data, LLM‑based defenses via prompt engineering, and Gemini model hardening to detect and ignore harmful embedded commands.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Primary risk is indirect prompt injection delivered via web content or malicious extensions that can influence agentic browsing or hijack the Gemini panel, enabling privilege escalation, local file access, or unsafe AI actions. Chrome’s mitigations add layered defenses (origin restrictions, prompt‑injection protections, secondary AI guardrails) to limit agentic actions.
- **Affected Products:** Google Chrome (builds including Gemini/agentic browsing features; December 2025+ releases)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Update Chrome to the latest patched version, remove or restrict untrusted extensions, disable agentic/Gemini features until patches are applied, and follow Google’s guidance in the vendor advisory.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

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

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: hidden malicious instructions embedded in external data sources (emails, documents, calendar invites) trick generative AI into exfiltrating data or executing actions. Google mitigations combine model hardening, ML classifiers to detect malicious instructions, sanitization of external content/URLs, reinforcement of safe reasoning, and HITL confirmations to block or filter malicious inputs.
- **Affected Products:** Gemini (Gemini in Google Workspace and the Gemini app); specific versions unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — https://blog.google/security/mitigating-prompt-injection-attacks/
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Layered defenses including Gemini 2.5 model hardening, prompt‑injection content classifiers, security thought reinforcement, markdown sanitization and suspicious URL redaction, user confirmation (HITL) framework, end‑user security mitigation notifications, adversarial training and red‑team testing.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC-linked actors compromise backbone, provider edge (PE) and customer edge (CE) routers and IoT devices; they modify routers to maintain persistent access and use compromised devices and trusted connections to pivot into other networks.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon (OPERATOR PANDA), RedMike, UNC5807, GhostEmperor
- **Mitigation:** Follow CISA mitigations: inventory network devices, implement monitoring for unauthorized configuration changes, restrict management plane access, apply vendor patches and configuration best practices, disable unused services, and segregate networks.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Russian GRU campaign uses spearphishing, credential harvesting, and network intrusion tools to gain access to Western logistics and technology organizations, then conducts reconnaissance, lateral movement, and data collection to support intelligence collection and disruption of logistics related to support for Ukraine.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** GRU 85th Main Special Service Center (85th GTsSS), military unit 26165 (Russian GRU).
- **Mitigation:** Implement multi-factor authentication; enforce least privilege and network segmentation; apply all vendor security updates; enable logging and monitor for anomalous access and C2 indicators; block known malicious IPs/domains; use EDR/IDS and hunt for IOCs listed in advisory.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟠 Zero-Day — LA Metro Cyberattack Linked to Iranian State-Sponsored Hackers

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://www.securityweek.com/la-metro-cyberattack-linked-to-iranian-state-sponsored-hackers/>

> The attack was claimed by a hacktivist group, but evidence showed it used infrastructure linked to Iranian government threat actors. The post LA Metro Cyberattack Linked to Iranian State-Sponsored Hackers appeared first on SecurityWeek .

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

## 29. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
