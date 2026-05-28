# Zero Day Pulse

> **Generated:** 2026-05-28 01:52 UTC &nbsp;|&nbsp; **Total:** 25 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 13 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Multiple path traversal vulnerabilities (including CVE‑2024‑57727) in SimpleHelp v5.5.7 and earlier enable unauthenticated remote attackers to retrieve logs, configuration files, and credentials and may allow remote code execution.
- **Affected Products:** SimpleHelp Remote Monitoring and Management, versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — http://medium.com/%40RosanaFS/simplehelp-cve-2024-57727-tryhackme-walkthrough-9f88c2061fb9
- **Patch Available:** true — http://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570
- **Active Exploitation:** true — http://cisa.gov/news-events/cybersecurity-advisories/aa25-163a
- **Threat Actors:** Ransomware actors
- **Mitigation:** Upgrade to SimpleHelp 5.5.8; if immediate patching is not possible, isolate/unexpose SimpleHelp instances, block management ports, rotate credentials, apply network segmentation, and enable EDR detections as described in the advisory.
- **Vendor Advisory:** http://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570

---

## 2. 🟠 Zero-Day — Inside the customer environment: Where threat actors, vulnerabilities, and exposed assets intersect

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Tenable Security Research &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://www.tenable.com/blog/vulnerability-prioritization-attacker-mapping-severity-exploitation-risk>

> Tenable Research has developed a graph-based model linking 600+ threat groups to real-world customer exposures. It reveals which vulnerabilities sit at the intersection of severity, active exploitation, and organizational risk. Key takeaways The &quot;patch everything&quot; strategy is dead: Vulnerability prioritization based on exploitation risk offers a path forward. A directed graph model linki…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability occurs when NGINX Open Source is configured to proxy HTTP/2 traffic by setting proxy_http_version to 2 and also uses proxy_set_body, causing malformed handling of the proxied request body.
- **Affected Products:** NGINX Open Source (when proxy_http_version is set to 2 and proxy_set_body is used)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — CISA gives feds 4 days to patch actively exploited cPanel plugin flaw

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-gives-feds-4-days-to-patch-actively-exploited-cpanel-plugin-flaw/>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has given U.S. federal agencies four days to secure their servers against a critical vulnerability in the LiteSpeed cPanel user-end plugin, which is actively being exploited in attacks. [...]

**Parallel AI Enrichment:**

- **Technical Details:** An attacker leveraging the lsws.redisAble function can execute arbitrary scripts with root privileges, enabling full system compromise.
- **Affected Products:** LiteSpeed User-End cPanel Plugin versions 2.3 through 2.4.4
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (https://securityweek.com/cisa-urges-immediate-patching-of-exploited-litespeed-cpanel-plugin-zero-day)
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Update the LiteSpeed User-End cPanel Plugin to version 2.4.5 or newer.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Attackers embed hidden or obfuscated instructions in web content (e.g., tiny/transparent text, HTML comments, metadata, CSS display:none). When AI agents crawl or retrieve this content, they treat the hidden text as legitimate instructions, leading to hijacking, data exfiltration, or tool misuse. Chaining with insufficient input sanitization or retrieval‑augmented generation can further enable code execution.
- **Affected Products:** Google Gemini, Google Workspace, GitHub Copilot, Anthropic Claude Code, Microsoft Copilot Studio (ShareLeak), Salesforce Agentforce
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Sanitize and validate all external content before ingestion, enforce least‑privilege tool access, separate instruction and data streams, apply robust RAG retrieval sanitization, and monitor AI agent outputs for anomalous behavior.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) enables attackers to influence LLM behavior by injecting malicious instructions into data or tools the LLM consumes (e.g., email/calendar content, URLs, linked documents). Attack surface includes agentic automation and multi‑source data ingestion in Workspace with Gemini; attack mechanisms include embedded instructions in content, malicious URLs, and tool‑chaining abuses.
- **Affected Products:** Google Workspace (Gemini‑integrated apps such as Gmail, Docs)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Layered defenses — deterministic controls (user confirmation, URL sanitization, tool‑chaining policies governed by a centralized Policy Engine), ML‑based defenses retrained on synthetic attack variants, LLM‑based prompt‑engineering defenses, human and automated red‑teaming, Google AI VRP, synthetic‑data augmentation (Simula) and model hardening for Gemini. Immediate mitigations include URL sanitization, user confirmations, tool access policies, and regex/config point fixes.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection—malicious or untrusted web content (including iframes, user‑generated content, ads) can embed instructions that manipulate the agent’s planner model to perform unwanted actions (financial transactions, data exfiltration, credential leakage).
- **Affected Products:** Chrome (agentic/Gemini browsing features, preview)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use Chrome’s built‑in layered defenses (User Alignment Critic, origin gating, prompt‑injection classifier, user confirmations); administrators should restrict agentic‑browser use in sensitive environments, tune origin isolation, monitor agent logs, and follow Google VRP guidance.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Near‑miss linear buffer overflow in CrabbyAVIF’s unsafe Rust code; Scudo allocator’s guard pages caused the overflow to crash rather than be exploitable, and a patch was applied before release.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use the Scudo hardened allocator (Android’s default) and apply rigorous code review and training for unsafe Rust code.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack where hidden or external content (web pages, email, documents, calendar invites, etc.) contains malicious instructions that are consumed by a generative AI system (e.g., an LLM‑based agent or assistant). The malicious content aims to override or manipulate the assistant's prompt, causing data exfiltration or rogue actions. Attackers may seed payloads on websites or other data sources hoping an AI agent will ingest them during browsing or document parsing.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Implement layered defenses as recommended by Google: input‑sanitization and source‑trust policies, content provenance and integrity checks, prompt design and instruction hygiene, strict context window limits for browsing/parsing agents, principle of least privilege for data access, detection/monitoring for anomalous model outputs, and annotating or blocking untrusted external content. For agents that browse the web, restrict browsing to vetted domains and validate scraped content; for file/document ingestion, use metadata provenance and scanning for instruction‑like payloads.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors compromise routers and IoT devices, modify router firmware/configuration to maintain persistent, long‑term access, and leverage trusted connections to pivot into target networks.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Follow CISA mitigations: inventory external‑facing devices, apply vendor firmware updates where available, disable unused services, rotate credentials and keys, enable network segmentation and monitoring, implement strict access controls and multifactor authentication, monitor for indicators of compromise.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Campaign-level targeting of Western logistics, transportation, and technology firms (including coordination/transport/delivery of foreign assistance to Ukraine) by Russian GRU actors since 2022 using espionage tradecraft (phishing, credential compromise, network intrusions, supply-chain/third-party targeting) to gather intelligence and disrupt operations.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true — confirmed sustained targeting and operations since 2022 reported by CISA and allied agencies.
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th GTsSS (Unit 26165) — tracked as APT28 and other industry names.
- **Mitigation:** Standard mitigations from the joint CSA: implement multi-factor authentication, network segmentation, monitoring and logging, patching and asset inventory, supply-chain risk management, and employee phishing awareness training. (If vendor‑specific mitigations exist, vendor advisory URL unavailable.)
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟠 Zero-Day — Langroid has Prompt to SQL Injection, Leading to RCE

**CVE:** `CVE-2026-25879` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-mxfr-6hcw-j9rq>

> # Security Vulnerability Report: Prompt to SQL Injection leading to RCE in latest Langroid

## Affected Scope
langroid &lt; 0.63.0

## Vulnerability Description

SQLChatAgent executes SQL produced by an LLM, which is influenceable by prompt injection. When configured with a database role that has privileges enabling code execution or filesystem access (e.g., PostgreSQL pg_execute_server_program, M…

---

## 12. 🟠 Zero-Day — LA Metro Cyberattack Linked to Iranian State-Sponsored Hackers

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://www.securityweek.com/la-metro-cyberattack-linked-to-iranian-state-sponsored-hackers/>

> The attack was claimed by a hacktivist group, but evidence showed it used infrastructure linked to Iranian government threat actors. The post LA Metro Cyberattack Linked to Iranian State-Sponsored Hackers appeared first on SecurityWeek .

---

## 13. 🟡 High Severity — FUXA's Unauthenticated Project Data Disclosure Exposes Server-Side Scripts and Device Configurations

**CVE:** `CVE-2026-47717` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-q3w6-q3hc-c5x6>

> ### Summary

The GET /api/project endpoint exposes sensitive project configuration data to guest-context requests even when secureEnabled is enabled.

### Details

File: `server/api/projects/index.js`

```javascript
prjApp.get(&quot;/api/project&quot;, secureFnc, function(req, res) {
    const permission = checkGroupsFnc(req);
    runtime.project.getProject(req.userId, permission).then(result =&gt…

---

## 14. 🟡 High Severity — Yamcs Vulnerable to Authenticated Remote Code Execution (RCE) via Jython Algorithm Code Injection

**CVE:** `CVE-2026-46621` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-2g95-6x5q-xjwj>

> ### Summary
A Server-Side Code Injection vulnerability exists in the Yamcs script evaluation engine for Python algorithms. The application dynamically compiles and evaluates user-controlled algorithm text using Jython (via the JSR-223 ScriptEngine API) without enforcing a secure sandbox. An authenticated user with the `ChangeMissionDatabase` privilege can exploit this by overriding the algorithm l…

---

## 15. 🟡 High Severity — Yamcs Vulnerable to Remote Code Execution via Mission Database algorithm override

**CVE:** `CVE-2026-46562` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-vmwp-vh32-rj75>

> # Remote Code Execution via Mission Database algorithm override

## Summary

The Nashorn `ScriptEngine` used to evaluate user-supplied algorithm text in `MdbOverrideApi.updateAlgorithm` is constructed without a `ClassFilter`, allowing a user with the `ChangeMissionDatabase` privilege to execute arbitrary Java code on the Yamcs server. In Yamcs&#x27;s default configuration (no `security.yaml`), the…

---

## 16. 🟡 High Severity — Pimcore has a CustomReports Share Bypass

**CVE:** `CVE-2026-45704` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-jwcc-gv4m-93x6>

> ### Summary

`CustomReports` uses inconsistent authorization between the report listing endpoint and the report detail endpoint.

- The listing flow filters reports based on report-sharing rules
- The detail flow only checks generic `reports` or `reports_config` permissions

As a result, a low-privileged backend user who was not granted access to a report can still read that report directly by nam…

---

## 17. 🟡 High Severity — AsyncSSH `AuthorizedKeysFile %u` path traversal allows attacker-selected authorized keys to authenticate a traversal username

**CVE:** `CVE-2026-45309` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-g794-3fmp-753h>

> ## Summary
AsyncSSH 2.22.0 expands the OpenSSH-compatible `AuthorizedKeysFile` `%u` token with the raw SSH username during pre-authentication server config reload. A server configured with a documented per-user key pattern such as `AuthorizedKeysFile authorized_keys/%u` can be made to read an authorized-keys file outside the intended directory when the SSH username contains path traversal segments…

---

## 18. 🟡 High Severity — Symfony hardened the parser when handling untrusted input

**CVE:** `CVE-2026-45133` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-c2p3-7m5p-cv8x>

> ### Description

`Symfony\Component\Yaml\Parser` is the entry point for parsing YAML strings into PHP values via `Yaml::parse()`. When the parser is exposed to attacker-controlled input, deeply nested mappings or sequences cause both the block-level (`Parser::parseBlock()`) and inline (`Inline::parseSequence()` / `Inline::parseMapping()`) parsers to recurse without a depth limit. A crafted documen…

---

## 19. 🟡 High Severity — Automad has Broken Access Control: Unauthenticated exposure of administrator bcrypt password hashes and TOTP secrets via public API endpoint

**CVE:** `CVE-2026-45332` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-xm76-r88j-vm3g>

> ### Summary

 A Broken Access Control vulnerability allows an unauthenticated attacker to retrieve the bcrypt password hash of every administrator account with a single POST request. The `/_api/user-collection/create-first-user` setup endpoint remains publicly accessible once initial configuration is complete and returns full serialized user data in the JSON response body.  

### Details

Affected…

---

## 20. 🟡 High Severity — Symfony has Unauthenticated PHP Object Deserialization in MonologBridge server:log Listener

**CVE:** `CVE-2026-45077` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-m7v2-7gxm-vc2v>

> ### Description

`Symfony\Bridge\Monolog\Command\ServerLogCommand` (the `server:log` console command) is a development-time helper that opens a TCP listener and displays log records pushed to it by the application&#x27;s logging pipeline. Two unsafe defaults combine into a remotely reachable PHP object-deserialization sink:

1. The listener binds to `0.0.0.0:9911` by default; it accepts connection…

---

## 21. 🟡 High Severity — Symfony has Email Header / SMTP Command Injection via CRLF in Symfony\Component\Mime\Address

**CVE:** `CVE-2026-45067` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-qpmx-3rfj-7rhv>

> ### Description

`Symfony\Component\Mime\Address` is the value-object every Symfony Mailer address (to/cc/bcc/from/reply-to) flows through; its constructor is documented as validating the address and throwing on invalid input, so developers treat it as a security boundary.

The constructor accepts email addresses whose local-part (the part before `@`) is an RFC-5322 *quoted string* containing raw …

---

## 22. 🟡 High Severity — LiquidJS is Vulnerable to Remote Code Execution

**CVE:** `CVE-2026-45618` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-gf2q-c269-pqgc>

> ### Summary
It is possible to execute arbitrary code with crafted templates


### Details

&lt;details&gt;
&lt;summary&gt;
 `1|valueOf` -&gt; `this` when evaluating the filter


&lt;/summary&gt;

```liquid
{%assign r=1|valueOf%}
{{r|inspect}}
```

```json
{&quot;context&quot;:{&quot;scopes&quot;:[{&quot;r&quot;:&quot;[Circular]&quot;}],&quot;registers&quot;:{},&quot;breakCalled&quot;:false,&quot;c…

---

## 23. 🟡 High Severity — Kirby CMS vulnerable to cross-site scripting (XSS) from links in KirbyTags and image blocks in the site frontend

**CVE:** `CVE-2026-45368` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-qvjf-922g-pj44>

> ### TL;DR

This vulnerability affects all Kirby sites that allow the use of the `(link: …)` KirbyTag, the `link:` parameter of the `(image: …)` KirbyTag, the built-in `image` block with a link or the HTML importer for blocks, when content is authored by users who may not be fully trusted. The attack requires an authenticated Panel user with update permission to any `textarea` or `blocks` field, or…

---

## 24. 🟡 High Severity — Pimcore has Unsafe PHP Deserialization in Multiple Locations Without allowed_classes Restriction

**CVE:** `CVE-2026-45162` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-36fc-7wjg-mfvj>

> # GM-374

## Summary
Multiple locations in Pimcore v11 call PHP&#x27;s `unserialize()` on data from database columns and filesystem files without the `allowed_classes` restriction, enabling object injection if an attacker can control the serialized data source.

## Affected Component
- **Package:** `pimcore/pimcore` and `pimcore/admin-ui-classic-bundle`
- **Files:**
  - `lib/Tool/Authentication.ph…

---

## 25. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
