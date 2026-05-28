# Zero Day Pulse

> **Generated:** 2026-05-28 15:04 UTC &nbsp;|&nbsp; **Total:** 27 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 13 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Multiple path traversal vulnerabilities in SimpleHelp 5.5.7 and earlier allow unauthenticated remote attackers to retrieve logs, configuration files, credentials, and potentially log in with elevated privileges, enabling compromise of downstream customers.
- **Affected Products:** SimpleHelp Remote Support / Remote Monitoring and Management (RMM) versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true - https://medium.com/@RosanaFS/simplehelp-cve-2024-57727-tryhackme-walkthrough-9f88c2061fb9
- **Patch Available:** true - http://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors / DragonForce
- **Mitigation:** Apply vendor patch/update to 5.5.8 or later immediately; isolate/unplug unpatched SimpleHelp servers from internet-facing access; audit logs and credentials; rotate exposed credentials; follow CISA advisory incident response guidance.
- **Vendor Advisory:** http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — New Gogs zero-day flaw lets hackers get remote code execution

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://www.bleepingcomputer.com/news/security/new-gogs-zero-day-flaw-lets-hackers-get-remote-code-execution/>

> An unpatched zero-day vulnerability in the Gogs self-hosted Git service can allow attackers to gain remote code execution (RCE) on Internet-facing instances. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Symlink bypass of the PutContents API allows authenticated users with repo creation/modify rights to commit a symlink pointing outside the repository and then use the API to overwrite arbitrary files (e.g., .git/config), resulting in remote code execution.
- **Affected Products:** Gogs <= 0.13.3 (fixed in v0.13.4)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — https://wiz.io/blog/wiz-research-gogs-cve-2025-8110-rce-exploit
- **Patch Available:** true — https://github.com/gogs/gogs/releases/tag/v0.13.4
- **Active Exploitation:** true — https://wiz.io/blog/wiz-research-gogs-cve-2025-8110-rce-exploit
- **Threat Actors:** None known
- **Mitigation:** Upgrade to v0.13.4 or later; if upgrade is not possible, disable open‑registration, restrict internet exposure (VPN/allow‑list), monitor for suspicious repositories and PutContents activity, and apply IoC detections provided by Wiz.
- **Vendor Advisory:** https://github.com/gogs/gogs/security/advisories

---

## 3. 🟠 Zero-Day — Critical FortiClient EMS Vulnerability Exploited in Fresh Attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://www.securityweek.com/critical-forticlient-ems-vulnerability-exploited-in-fresh-attacks/>

> Fortinet rolled out hotfixes for the security defect in April, warning that it had been exploited in the wild as a zero-day and urging immediate patching. The post Critical FortiClient EMS Vulnerability Exploited in Fresh Attacks appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Improper Access Control (CWE‑284) – a pre‑authentication API access bypass in FortiClient EMS that permits unauthenticated attackers to execute unauthorized code or commands via specially crafted requests.
- **Affected Products:** FortiClient EMS 7.4.5, FortiClient EMS 7.4.6
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true - http://fortiguard.fortinet.com/psirt/FG-IR-26-099
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Install the emergency hotfix for FortiClient EMS 7.4.5 and 7.4.6, or upgrade to FortiClient EMS 7.4.7 when released; follow the vendor's hotfix installation instructions.
- **Vendor Advisory:** http://fortiguard.fortinet.com/psirt/FG-IR-26-099

---

## 4. 🟠 Zero-Day — Download pumping: New npm deception technique for supply chain attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Tenable Security Research &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://www.tenable.com/blog/how-cyberattackers-inflate-malicious-package-npm-download-counts>

> Learn how attackers exploit automated bot traffic as part of software supply chain attacks to artificially inflate download counters and mask malicious payloads as legitimate. Key takeaways Volume doesn’t equal trust. Packages with numerous versions and high download counts might seem legitimate, but attackers can easily manipulate those metrics. Attackers exploit automated infrastructure. By init…

**Parallel AI Enrichment:**

- **Technical Details:** Attackers first flood the npm registry with numerous benign versions of a package, causing automated tools and mirrors to download them and artificially inflate the package's download count. Once the package appears popular and trustworthy, later versions embed malicious code that is then delivered to downstream users who trust the high download metrics.
- **Affected Products:** @antv npm packages (multiple versions)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Shai‑Hulud (also known as Mini‑Shai‑Hulud / TeamPCP)
- **Mitigation:** 1. Maintain an up‑to‑date inventory of all npm packages used in your environment. 2. Monitor package download trends for sudden spikes that are not correlated with legitimate usage. 3. Enforce strict package signing and provenance verification (e.g., Sigstore) before accepting new versions. 4. Limit automatic fetching of packages from mirrors and configure CI pipelines to use vetted, signed sources only.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — Inside the customer environment: Where threat actors, vulnerabilities, and exposed assets intersect

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Tenable Security Research &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://www.tenable.com/blog/vulnerability-prioritization-attacker-mapping-severity-exploitation-risk>

> Tenable Research has developed a graph-based model linking 600+ threat groups to real-world customer exposures. It reveals which vulnerabilities sit at the intersection of severity, active exploitation, and organizational risk. Key takeaways The &quot;patch everything&quot; strategy is dead: Vulnerability prioritization based on exploitation risk offers a path forward. A directed graph model linki…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, Black Basta (and other groups referenced in the Tenable model).
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 6. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when attacker‑controlled web content or third‑party data contains hidden instructions that an AI agent ingests, causing the agent to execute attacker‑specified behaviors despite system instructions. The attacker places payloads in web pages or documents the agent fetches, and the concatenated prompt lets those instructions influence or override legitimate commands.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses and hardening for AI agents (input filtering, content provenance, sandboxing, model instruction isolation). See Google layered‑defense guidance and Forcepoint payload analysis.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 7. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when malicious instructions are embedded in data sources (web pages, emails, documents) that an LLM ingests; these embedded instructions can influence the model’s behavior or agentic tool use without direct user input. Google’s blog details discovery (human & automated red‑teaming, public web sweeps), synthetic‑data generation, deterministic/ML/LLM defenses, and model hardening for Gemini.
- **Affected Products:** Google Workspace (Gmail, Docs, other Workspace apps) with Gemini integration
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Deterministic defenses (user confirmation, URL sanitization, tool chaining policies, centralized policy engine and config "point fixes"), ML‑based defenses (synthetic‑data retraining), LLM‑based defenses (prompt engineering), Gemini model hardening; ongoing monitoring and VRP engagement.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections

---

## 8. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: malicious or third‑party content (web pages, embedded resources, comments) can supply crafted instructions that agentic browsing components (Gemini in Chrome or agent runtimes) may treat as high‑level directives, enabling influence over agent actions or data exfiltration.
- **Affected Products:** Chrome (agentic browsing / Gemini in Chrome)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Enable Chrome’s updated agentic protections (shipped with Gemini in Chrome); apply origin restrictions, restrict agent access to local resources, require explicit user authorization for sensitive actions, and keep Chrome/Gemini up to date.
- **Vendor Advisory:** https://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 9. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** The documented Rust-related issue (CVE-2025-68260) is a race condition in rust_binder where an unsafe remove operation can run concurrently with list manipulation (Node::release moving items to a local list while other threads may remove items), leading to memory corruption/crashes due to prev/next pointer corruption.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true — https://source.android.com/docs/security/bulletin/2025-11-01
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Apply the 2025-11-01 Android security updates (or later) and associated AOSP/kernel patches; update devices to the latest security patch level and vendor‑supplied updates. Follow Android platform mitigations (enable latest platform protections, Google Play Protect) while patches are applied.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-11-01

---

## 10. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) embeds malicious instructions in external data sources such as emails, documents, calendar invites, or hidden web code. When an AI assistant processes this data, it follows the hidden instructions, potentially exfiltrating data or performing unauthorized actions.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — vendor guidance/advisory URL: http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html
- **Active Exploitation:** true — sources: Forcepoint (10 Indirect Prompt Injection Payloads Caught in the Wild), SecurityWeek analysis
- **Threat Actors:** None known
- **Mitigation:** Use layered defense: input provenance and parsing, content sanitization, model instruction filtering, limiting high‑risk data in prompts, applying role‑based access controls, user confirmation for sensitive actions, and monitoring/telemetry.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 11. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

---

## 12. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 13. 🟠 Zero-Day — Microsoft Slams Public Zero-Day Disclosures Amid GitHub Researcher Account Removal

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://thehackernews.com/2026/05/microsoft-slams-public-zero-day.html>

> Microsoft has come out strongly in favor of Coordinated Vulnerability Disclosure (CVD), urging the research community to share their findings and give affected vendors an opportunity to better understand the impact and address them before they are publicly disclosed.

The development comes after a researcher named Chaotic Eclipse (aka Nightmare-Eclipse) disclosed details of multiple zero-day

---

## 14. 🟠 Zero-Day — Langroid has Prompt to SQL Injection, Leading to RCE

**CVE:** `CVE-2026-25879` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-mxfr-6hcw-j9rq>

> # Security Vulnerability Report: Prompt to SQL Injection leading to RCE in latest Langroid

## Affected Scope
langroid &lt; 0.63.0

## Vulnerability Description

SQLChatAgent executes SQL produced by an LLM, which is influenceable by prompt injection. When configured with a database role that has privileges enabling code execution or filesystem access (e.g., PostgreSQL pg_execute_server_program, M…

---

## 15. 🟡 High Severity — FUXA's Unauthenticated Project Data Disclosure Exposes Server-Side Scripts and Device Configurations

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

## 16. 🟡 High Severity — Yamcs Vulnerable to Authenticated Remote Code Execution (RCE) via Jython Algorithm Code Injection

**CVE:** `CVE-2026-46621` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-2g95-6x5q-xjwj>

> ### Summary
A Server-Side Code Injection vulnerability exists in the Yamcs script evaluation engine for Python algorithms. The application dynamically compiles and evaluates user-controlled algorithm text using Jython (via the JSR-223 ScriptEngine API) without enforcing a secure sandbox. An authenticated user with the `ChangeMissionDatabase` privilege can exploit this by overriding the algorithm l…

---

## 17. 🟡 High Severity — Yamcs Vulnerable to Remote Code Execution via Mission Database algorithm override

**CVE:** `CVE-2026-46562` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-vmwp-vh32-rj75>

> # Remote Code Execution via Mission Database algorithm override

## Summary

The Nashorn `ScriptEngine` used to evaluate user-supplied algorithm text in `MdbOverrideApi.updateAlgorithm` is constructed without a `ClassFilter`, allowing a user with the `ChangeMissionDatabase` privilege to execute arbitrary Java code on the Yamcs server. In Yamcs&#x27;s default configuration (no `security.yaml`), the…

---

## 18. 🟡 High Severity — Pimcore has a CustomReports Share Bypass

**CVE:** `CVE-2026-45704` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-jwcc-gv4m-93x6>

> ### Summary

`CustomReports` uses inconsistent authorization between the report listing endpoint and the report detail endpoint.

- The listing flow filters reports based on report-sharing rules
- The detail flow only checks generic `reports` or `reports_config` permissions

As a result, a low-privileged backend user who was not granted access to a report can still read that report directly by nam…

---

## 19. 🟡 High Severity — AsyncSSH `AuthorizedKeysFile %u` path traversal allows attacker-selected authorized keys to authenticate a traversal username

**CVE:** `CVE-2026-45309` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-g794-3fmp-753h>

> ## Summary
AsyncSSH 2.22.0 expands the OpenSSH-compatible `AuthorizedKeysFile` `%u` token with the raw SSH username during pre-authentication server config reload. A server configured with a documented per-user key pattern such as `AuthorizedKeysFile authorized_keys/%u` can be made to read an authorized-keys file outside the intended directory when the SSH username contains path traversal segments…

---

## 20. 🟡 High Severity — Symfony hardened the parser when handling untrusted input

**CVE:** `CVE-2026-45133` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-c2p3-7m5p-cv8x>

> ### Description

`Symfony\Component\Yaml\Parser` is the entry point for parsing YAML strings into PHP values via `Yaml::parse()`. When the parser is exposed to attacker-controlled input, deeply nested mappings or sequences cause both the block-level (`Parser::parseBlock()`) and inline (`Inline::parseSequence()` / `Inline::parseMapping()`) parsers to recurse without a depth limit. A crafted documen…

---

## 21. 🟡 High Severity — Automad has Broken Access Control: Unauthenticated exposure of administrator bcrypt password hashes and TOTP secrets via public API endpoint

**CVE:** `CVE-2026-45332` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-xm76-r88j-vm3g>

> ### Summary

 A Broken Access Control vulnerability allows an unauthenticated attacker to retrieve the bcrypt password hash of every administrator account with a single POST request. The `/_api/user-collection/create-first-user` setup endpoint remains publicly accessible once initial configuration is complete and returns full serialized user data in the JSON response body.  

### Details

Affected…

---

## 22. 🟡 High Severity — Symfony has Unauthenticated PHP Object Deserialization in MonologBridge server:log Listener

**CVE:** `CVE-2026-45077` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-m7v2-7gxm-vc2v>

> ### Description

`Symfony\Bridge\Monolog\Command\ServerLogCommand` (the `server:log` console command) is a development-time helper that opens a TCP listener and displays log records pushed to it by the application&#x27;s logging pipeline. Two unsafe defaults combine into a remotely reachable PHP object-deserialization sink:

1. The listener binds to `0.0.0.0:9911` by default; it accepts connection…

---

## 23. 🟡 High Severity — Symfony has Email Header / SMTP Command Injection via CRLF in Symfony\Component\Mime\Address

**CVE:** `CVE-2026-45067` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-qpmx-3rfj-7rhv>

> ### Description

`Symfony\Component\Mime\Address` is the value-object every Symfony Mailer address (to/cc/bcc/from/reply-to) flows through; its constructor is documented as validating the address and throwing on invalid input, so developers treat it as a security boundary.

The constructor accepts email addresses whose local-part (the part before `@`) is an RFC-5322 *quoted string* containing raw …

---

## 24. 🟡 High Severity — LiquidJS is Vulnerable to Remote Code Execution

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

## 25. 🟡 High Severity — Kirby CMS vulnerable to cross-site scripting (XSS) from links in KirbyTags and image blocks in the site frontend

**CVE:** `CVE-2026-45368` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-qvjf-922g-pj44>

> ### TL;DR

This vulnerability affects all Kirby sites that allow the use of the `(link: …)` KirbyTag, the `link:` parameter of the `(image: …)` KirbyTag, the built-in `image` block with a link or the HTML importer for blocks, when content is authored by users who may not be fully trusted. The attack requires an authenticated Panel user with update permission to any `textarea` or `blocks` field, or…

---

## 26. 🟡 High Severity — Pimcore has Unsafe PHP Deserialization in Multiple Locations Without allowed_classes Restriction

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

## 27. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
