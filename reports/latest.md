# Zero Day Pulse

> **Generated:** 2026-05-28 09:43 UTC &nbsp;|&nbsp; **Total:** 24 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 11 &nbsp;|&nbsp; 🟡 High: 13 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path traversal vulnerability in SimpleHelp RMM (v5.5.7 and earlier) that enables unauthenticated remote attackers to retrieve logs, configuration files, and credentials and potentially log in with elevated privileges, allowing access to downstream customer environments.
- **Affected Products:** SimpleHelp Remote Support/Software versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** DragonForce
- **Mitigation:** Immediately upgrade SimpleHelp to v5.5.8 or later; if immediate patching not possible, isolate/segregate RMM servers from sensitive networks, restrict network access to management interfaces (firewall/ACLs to trusted IPs), rotate credentials/passwords and secrets stored in SimpleHelp, audit logs for indicators of compromise, and monitor outbound traffic for suspicious activity.
- **Vendor Advisory:** http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — Inside the customer environment: Where threat actors, vulnerabilities, and exposed assets intersect

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

- **Technical Details:** Incorrect privilege assignment in the LiteSpeed User-End cPanel Plugin (lsws.redisAble function) allows an authenticated cPanel user to execute arbitrary scripts as root, enabling privilege escalation to root.
- **Affected Products:** LiteSpeed User-End cPanel Plugin versions 2.3 through 2.4.4 (i.e., before 2.4.5)
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Remove or upgrade the plugin; apply vendor updates. cPanel auto-removed the LiteSpeed plugin during nightly updates (May 19, 2026) as a mitigation; vendors recommend upgrading to fixed plugin version 2.4.7 / WHM plugin v5.3.1 per advisory summaries.
- **Vendor Advisory:** https://support.cpanel.net/hc/en-us/articles/40599423437079-Security-LiteSpeed-plugin-automatically-removed-during-nightly-update-May-19-2026

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when adversarial content on the web (or other untrusted content) is ingested into an AI agent's context and contains malicious instructions or payloads that override or manipulate the agent's intended prompts, causing it to reveal secrets, perform unauthorized actions, or misuse APIs. Attack vectors observed include crafted web content and payloads embedded in otherwise legitimate pages that are likely to be read by agents during browsing or content retrieval.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Hardening recommendations include restricting or sanitizing external content before including it in agent context, validating and canonicalizing sources, using content allowlists, employing model grounding/verifiable sources, prompting-level defenses (explicit instruction locking, context separation), and monitoring for anomalous agent behavior.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) enables attackers to influence LLM behavior by injecting malicious instructions into data or tools the LLM consumes (e.g., documents, URLs, tool outputs). In multi-source AI apps like Workspace with Gemini, injected instructions can be executed by the model during query completion without direct user input, exploiting agentic automation and tool chaining.
- **Affected Products:** Google Workspace (Gemini-enabled): Gmail, Docs, and other Workspace apps
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Layered defenses including human and automated red‑teaming, Google AI VRP, synthetic‑attack data generation, deterministic defenses (user confirmation, URL sanitization, tool‑chaining policies via a centralized Policy Engine), ML‑based defenses retrained on synthetic attack variants, LLM‑based defenses and Gemini model hardening to detect and ignore harmful embedded instructions. Ongoing monitoring, vulnerability cataloging, and simulation testing across Workspace apps (e.g., Gmail, Docs) are recommended.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The primary threat is indirect prompt injection, where malicious sites or third‑party content manipulate the prompts supplied to the agentic browser assistant, allowing attackers to influence AI actions. Chrome’s layered defenses monitor for such injections, restrict origin access, and block unsafe AI actions.
- **Affected Products:** Chrome (agentic browsing / Gemini integration)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — http://pymnts.com/google/2025/google-adds-security-layers-to-safeguard-agentic-browsing-with-chrome
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Use Chrome's new layered defenses for agentic browsing (prompt injection protections, origin access restrictions, unsafe‑AI‑action prevention); keep Chrome updated.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A near‑miss linear buffer overflow was identified in CrabbyAVIF (external/rust/crabbyavif) in unsafe Rust; Scudo hardened allocator’s guard pages rendered the overflow non‑exploitable and the issue was fixed pre‑release.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — patch: https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use Scudo hardened allocator (guard pages); improved crash reporting to detect overflows into Scudo guard pages; increased unsafe‑Rust review and training; encapsulate unsafe code and follow safety‑comment practices.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when hidden malicious instructions are embedded within external data sources (emails, documents, calendar invites, or other ingested data) that an AI system reads and incorporates into its prompt context; these hidden instructions can cause the model to exfiltrate sensitive data or perform unauthorized actions. Defenses are layered and include input sanitization/labeling, source provenance/trust signals, model behavior constraints, context filtering, and workspace-level safeguards.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Implement layered defenses: (1) restrict and validate external data sources before ingestion; (2) sanitize and remove instructions from user-provided content (e.g., strip or neutralize imperative directives); (3) add provenance and trust metadata and enforce policies to prefer trusted sources; (4) apply context/windowing and prompt engineering to limit sensitive data exposure; (5) enforce model output constraints and red‑team/test for IPI payloads; (6) deploy vendor recommendations/advisories (see vendor advisory URL).
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC‑linked actors compromise large backbone, PE, and CE routers and IoT devices, modify router firmware/configuration to maintain persistent, long‑term access, create tunnels (e.g., GRE) and pivot from trusted connections into other networks to exfiltrate data and support espionage.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unavailable.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon (and associated industry aliases OPERATOR PANDA, RedMike, UNC5807, GhostEmperor)
- **Mitigation:** Inventory and isolate affected routers/IoT; apply vendor firmware/patches where available; rotate credentials and keys; restrict management plane access (ACLs, network segmentation, disable unused services); monitor for config/firmware changes, anomalous GRE tunnels, unusual egress; follow CISA/NSA mitigation guidance.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Adversaries exploited internet‑facing services (VPNs, SQL injection) and specific software flaws: WinRAR code‑execution (CVE‑2023‑38831), Outlook NTLM relay via malicious calendar invites (CVE‑2023‑23397) to harvest NTLM hashes, and Roundcube command injection (CVE‑2020‑12641, CVE‑2020‑35730, CVE‑2021‑44026) to execute shell commands and access mail.
- **Affected Products:** WinRAR (CVE-2023-38831), Roundcube Webmail (CVE-2020-12641; CVE-2020-35730; CVE-2021-44026), Outlook (CVE-2023-23397)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true - https://aka.ms/CVE-2023-23397ScriptDoc
- **Patch Available:** true - https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a
- **Active Exploitation:** true
- **Threat Actors:** GRU unit 26165 (tracked as APT28 / Fancy Bear / Forest Blizzard / Blue Delta)
- **Mitigation:** Employ network segmentation and Zero Trust principles, block or monitor hosting/API mocking services, apply all vendor patches and firmware updates (including IP cameras), disable unnecessary remote access, enforce MFA, monitor for known tools and behaviors, and use the Microsoft script (https://aka.ms/CVE-2023-23397ScriptDoc) to detect malicious Outlook calendar invites.
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

## 12. 🟡 High Severity — FUXA's Unauthenticated Project Data Disclosure Exposes Server-Side Scripts and Device Configurations

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

## 13. 🟡 High Severity — Yamcs Vulnerable to Authenticated Remote Code Execution (RCE) via Jython Algorithm Code Injection

**CVE:** `CVE-2026-46621` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-2g95-6x5q-xjwj>

> ### Summary
A Server-Side Code Injection vulnerability exists in the Yamcs script evaluation engine for Python algorithms. The application dynamically compiles and evaluates user-controlled algorithm text using Jython (via the JSR-223 ScriptEngine API) without enforcing a secure sandbox. An authenticated user with the `ChangeMissionDatabase` privilege can exploit this by overriding the algorithm l…

---

## 14. 🟡 High Severity — Yamcs Vulnerable to Remote Code Execution via Mission Database algorithm override

**CVE:** `CVE-2026-46562` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-vmwp-vh32-rj75>

> # Remote Code Execution via Mission Database algorithm override

## Summary

The Nashorn `ScriptEngine` used to evaluate user-supplied algorithm text in `MdbOverrideApi.updateAlgorithm` is constructed without a `ClassFilter`, allowing a user with the `ChangeMissionDatabase` privilege to execute arbitrary Java code on the Yamcs server. In Yamcs&#x27;s default configuration (no `security.yaml`), the…

---

## 15. 🟡 High Severity — Pimcore has a CustomReports Share Bypass

**CVE:** `CVE-2026-45704` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-jwcc-gv4m-93x6>

> ### Summary

`CustomReports` uses inconsistent authorization between the report listing endpoint and the report detail endpoint.

- The listing flow filters reports based on report-sharing rules
- The detail flow only checks generic `reports` or `reports_config` permissions

As a result, a low-privileged backend user who was not granted access to a report can still read that report directly by nam…

---

## 16. 🟡 High Severity — AsyncSSH `AuthorizedKeysFile %u` path traversal allows attacker-selected authorized keys to authenticate a traversal username

**CVE:** `CVE-2026-45309` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-g794-3fmp-753h>

> ## Summary
AsyncSSH 2.22.0 expands the OpenSSH-compatible `AuthorizedKeysFile` `%u` token with the raw SSH username during pre-authentication server config reload. A server configured with a documented per-user key pattern such as `AuthorizedKeysFile authorized_keys/%u` can be made to read an authorized-keys file outside the intended directory when the SSH username contains path traversal segments…

---

## 17. 🟡 High Severity — Symfony hardened the parser when handling untrusted input

**CVE:** `CVE-2026-45133` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-c2p3-7m5p-cv8x>

> ### Description

`Symfony\Component\Yaml\Parser` is the entry point for parsing YAML strings into PHP values via `Yaml::parse()`. When the parser is exposed to attacker-controlled input, deeply nested mappings or sequences cause both the block-level (`Parser::parseBlock()`) and inline (`Inline::parseSequence()` / `Inline::parseMapping()`) parsers to recurse without a depth limit. A crafted documen…

---

## 18. 🟡 High Severity — Automad has Broken Access Control: Unauthenticated exposure of administrator bcrypt password hashes and TOTP secrets via public API endpoint

**CVE:** `CVE-2026-45332` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-xm76-r88j-vm3g>

> ### Summary

 A Broken Access Control vulnerability allows an unauthenticated attacker to retrieve the bcrypt password hash of every administrator account with a single POST request. The `/_api/user-collection/create-first-user` setup endpoint remains publicly accessible once initial configuration is complete and returns full serialized user data in the JSON response body.  

### Details

Affected…

---

## 19. 🟡 High Severity — Symfony has Unauthenticated PHP Object Deserialization in MonologBridge server:log Listener

**CVE:** `CVE-2026-45077` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-m7v2-7gxm-vc2v>

> ### Description

`Symfony\Bridge\Monolog\Command\ServerLogCommand` (the `server:log` console command) is a development-time helper that opens a TCP listener and displays log records pushed to it by the application&#x27;s logging pipeline. Two unsafe defaults combine into a remotely reachable PHP object-deserialization sink:

1. The listener binds to `0.0.0.0:9911` by default; it accepts connection…

---

## 20. 🟡 High Severity — Symfony has Email Header / SMTP Command Injection via CRLF in Symfony\Component\Mime\Address

**CVE:** `CVE-2026-45067` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-qpmx-3rfj-7rhv>

> ### Description

`Symfony\Component\Mime\Address` is the value-object every Symfony Mailer address (to/cc/bcc/from/reply-to) flows through; its constructor is documented as validating the address and throwing on invalid input, so developers treat it as a security boundary.

The constructor accepts email addresses whose local-part (the part before `@`) is an RFC-5322 *quoted string* containing raw …

---

## 21. 🟡 High Severity — LiquidJS is Vulnerable to Remote Code Execution

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

## 22. 🟡 High Severity — Kirby CMS vulnerable to cross-site scripting (XSS) from links in KirbyTags and image blocks in the site frontend

**CVE:** `CVE-2026-45368` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-qvjf-922g-pj44>

> ### TL;DR

This vulnerability affects all Kirby sites that allow the use of the `(link: …)` KirbyTag, the `link:` parameter of the `(image: …)` KirbyTag, the built-in `image` block with a link or the HTML importer for blocks, when content is authored by users who may not be fully trusted. The attack requires an authenticated Panel user with update permission to any `textarea` or `blocks` field, or…

---

## 23. 🟡 High Severity — Pimcore has Unsafe PHP Deserialization in Multiple Locations Without allowed_classes Restriction

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

## 24. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
