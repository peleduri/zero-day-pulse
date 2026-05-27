# Zero Day Pulse

> **Generated:** 2026-05-27 19:59 UTC &nbsp;|&nbsp; **Total:** 33 &nbsp;|&nbsp; 🔴 KEV: 3 &nbsp;|&nbsp; 🟠 Zero-Day: 13 &nbsp;|&nbsp; 🟡 High: 17 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🔴 CISA KEV — CVE-2026-48027 — Nx Console Embedded Malicious Code Vulnerability

**CVE:** `CVE-2026-48027` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-48027>

> Vendor: Nx | Product: Nx Console. Nx Console contains an embedded malicious code vulnerability that allowed a malicious version of Nx Console to be published. The compromised extension fetched an obfuscated payload that could harvested credentials from multiple sources on disk and in memory. Required action: Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud …

**Parallel AI Enrichment:**

- **Technical Details:** A malicious version of the Nx Console VS Code extension was published; when installed it retrieved an obfuscated payload that harvested credentials from multiple sources on disk and in memory.
- **Affected Products:** Nx Console v18.95.0
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **Vendor Advisory:** https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w

---

## 2. 🔴 CISA KEV — CVE-2026-45321 — TanStack Unspecified Vulnerability

**CVE:** `CVE-2026-45321` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-45321>

> Vendor: TanStack | Product: TanStack. TanStack contains an unspecified vulnerability that allowed malicious versions of the product to be published to the npm registry to publish credential-stealing malware under a trusted identity. Required action: Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations a…

**Parallel AI Enrichment:**

- **Technical Details:** An attacker abused a pull_request_target "Pwn Request" misconfiguration to trigger a GitHub Actions workflow, poisoned the Actions cache across the fork↔base trust boundary, and extracted the OIDC token from the runner process memory. This enabled the attacker to publish malicious versions of @tanstack/* packages that included an obfuscated router_init.js payload which harvested credentials, exfiltrated them, and self‑propagated to other packages.
- **Affected Products:** @tanstack/react-router 1.169.5, 1.169.8; @tanstack/vue-router 1.169.5, 1.169.8; @tanstack/solid-router 1.169.5, 1.169.8; @tanstack/router-core 1.169.5, 1.169.8; plus other @tanstack/* packages (total 42 packages)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** TeamPCP (aliases: DeadCatx3, PCPcat, ShellForce, CipherForce)
- **Mitigation:** Inspect downloads/tarballs without executing scripts (npm pack / unpack and grep for router_init.js / payload hash), treat exposed hosts as compromised, contain persistence (stop/remove gh-token-monitor and editor persistence), rotate all accessible credentials/secrets, block C2 domains (e.g., *.getsession.org, api.masscan.cloud, git-tanstack.com) at DNS/egress, purge GitHub Actions caches, avoid pull_request_target workflows that run untrusted code, pin actions to SHAs, add release‑age cooldowns, and follow vendor remediation guidance.
- **Vendor Advisory:** https://tanstack.com/blog/npm-supply-chain-compromise-postmortem

---

## 3. 🔴 CISA KEV — CVE-2026-8398 — Daemon Tools Lite Embedded Malicious Code Vulnerability

**CVE:** `CVE-2026-8398` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-8398>

> Vendor: Daemon | Product: Daemon Tools Lite. Daemon Tools contains an unspecified vulnerability that has a high impact on confidentiality, integrity, and availability. Required action: Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable. (due 2026-05-30)

**Parallel AI Enrichment:**

- **Technical Details:** Supply‑chain attack trojanized official DAEMON Tools Lite installer packages, embedding malicious code into installers distributed to users; impact to confidentiality, integrity, and availability due to embedded malware in legitimate installer.
- **Affected Products:** DAEMON Tools Lite versions 12.5.0.2421 through 12.5.0.2434
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Immediately remove affected installer versions; uninstall DAEMON Tools Lite if installed from those versions; follow vendor instructions if/when released; apply BOD 22-01 guidance for cloud services or discontinue use if mitigations unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** A path traversal vulnerability in SimpleHelp 5.5.7 and earlier permits unauthenticated remote attackers to retrieve logs, configuration files, and credentials by manipulating file paths.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (source: http://medium.com/%40RosanaFS/simplehelp-cve-2024-57727-tryhackme-walkthrough-9f88c2061fb9)
- **Patch Available:** true (patch URL: http://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570)
- **Active Exploitation:** true
- **Threat Actors:** DragonForce ransomware group
- **Mitigation:** Upgrade SimpleHelp to version 5.5.8 or later, which includes fixes for CVE‑2024‑57727 and related vulnerabilities.
- **Vendor Advisory:** http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

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
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 6. 🟠 Zero-Day — CISA gives feds 4 days to patch actively exploited cPanel plugin flaw

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-gives-feds-4-days-to-patch-actively-exploited-cpanel-plugin-flaw/>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has given U.S. federal agencies four days to secure their servers against a critical vulnerability in the LiteSpeed cPanel user-end plugin, which is actively being exploited in attacks. [...]

**Parallel AI Enrichment:**

- **Technical Details:** The lsws.redisAble function in the LiteSpeed User-End cPanel plugin can be invoked by any cPanel user to execute arbitrary scripts as root, enabling privilege escalation to full system compromise.
- **Affected Products:** LiteSpeed User-End cPanel Plugin versions < 2.4.5 (e.g., 2.3, 2.3.1, 2.4, 2.4.4)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Upgrade the LiteSpeed User-End cPanel plugin to version 2.4.7 (or later) which includes the fix for CVE-2026-48172.
- **Vendor Advisory:** http://cibersafety.com/en/LiteSpeed-%E2%80%8B%E2%80%8BcPanel-privilege-escalation

---

## 7. 🟠 Zero-Day — KnowledgeDeliver flaw exploited as a zero-day to install web shells

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://www.bleepingcomputer.com/news/security/knowledgedeliver-flaw-exploited-as-a-zero-day-to-install-web-shells/>

> Hackers exploited a critical zero-day vulnerability in a server running the KnowledgeDeliver learning management system (LMS) to deploy the Godzilla web shell. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Hard‑coded ASP.NET/IIS machineKey values in the default web.config allow ViewState deserialization attacks, enabling attackers to inject and execute the Godzilla (Bluebeam) .NET web shell.
- **Affected Products:** KnowledgeDeliver Learning Management System (installations prior to 2026‑02‑24)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) involves an attacker placing malicious payloads in web content or other inputs that are later consumed by an AI system. When the AI model reads the content, the embedded instructions influence the model's output, allowing the attacker to steer the model to perform unintended actions or disclose sensitive information.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Implement strict validation and sanitization of any external content fed to AI models, restrict model access to trusted data sources, employ prompt‑hardening techniques, and monitor model responses for unexpected behavior. Deploy AI‑specific security controls such as usage limits and anomaly detection.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 9. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack where adversaries inject malicious instructions into data sources or tools that an LLM accesses while fulfilling a user query; the model may follow those injected instructions even without direct user input, influencing behavior of agentic workflows in Workspace with Gemini.
- **Affected Products:** Google Workspace (services integrating Gemini and multi‑source agentic features)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: content filtering of external inputs, robust source provenance checks, tooling isolation, policy‑driven instruction parsing, continuous monitoring and model‑level hardening as described in Google's white paper/DeepMind research. Follow specific vendor guidance in the advisory.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 10. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection—malicious or adversarial content in webpages, iframes, or user‑generated content can influence an agent’s planner model to perform unwanted actions (financial transactions, data exfiltration). Chrome mitigates this by isolating planning outputs with a User Alignment Critic, gating origins, running a prompt‑injection classifier in parallel, applying deterministic URL checks, and requiring user confirmations for sensitive actions.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Use Chrome’s layered defenses: a User Alignment Critic that vets actions with a separate high‑trust model, origin‑isolation (Agent Origin Sets) to limit readable/writable origins, a runtime prompt‑injection classifier that scans pages in parallel with planning, deterministic checks on model‑generated URLs, user confirmations for sensitive actions, transparency/work logs, and an updated Vulnerability Rewards Program for reporting.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 11. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

---

## 12. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 13. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

---

## 14. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 15. 🟠 Zero-Day — Langroid has Prompt to SQL Injection, Leading to RCE

**CVE:** `CVE-2026-25879` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-mxfr-6hcw-j9rq>

> # Security Vulnerability Report: Prompt to SQL Injection leading to RCE in latest Langroid

## Affected Scope
langroid &lt; 0.63.0

## Vulnerability Description

SQLChatAgent executes SQL produced by an LLM, which is influenceable by prompt injection. When configured with a database role that has privileges enabling code execution or filesystem access (e.g., PostgreSQL pg_execute_server_program, M…

---

## 16. 🟠 Zero-Day — LA Metro Cyberattack Linked to Iranian State-Sponsored Hackers

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://www.securityweek.com/la-metro-cyberattack-linked-to-iranian-state-sponsored-hackers/>

> The attack was claimed by a hacktivist group, but evidence showed it used infrastructure linked to Iranian government threat actors. The post LA Metro Cyberattack Linked to Iranian State-Sponsored Hackers appeared first on SecurityWeek .

---

## 17. 🟡 High Severity — LiquidJS is Vulnerable to Remote Code Execution

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

## 18. 🟡 High Severity — Kirby CMS vulnerable to cross-site scripting (XSS) from links in KirbyTags and image blocks in the site frontend

**CVE:** `CVE-2026-45368` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-qvjf-922g-pj44>

> ### TL;DR

This vulnerability affects all Kirby sites that allow the use of the `(link: …)` KirbyTag, the `link:` parameter of the `(image: …)` KirbyTag, the built-in `image` block with a link or the HTML importer for blocks, when content is authored by users who may not be fully trusted. The attack requires an authenticated Panel user with update permission to any `textarea` or `blocks` field, or…

---

## 19. 🟡 High Severity — Pimcore has Unsafe PHP Deserialization in Multiple Locations Without allowed_classes Restriction

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

## 20. 🟡 High Severity — @hapi/wreck leaks sensitive `Proxy-Authorization` header across cross-hostname redirects

**CVE:** `CVE-2026-44979` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-vhjm-w67q-g75c>

> ### Impact
When `@hapi/wreck` follows a 3xx redirect to a different hostname, only the `Authorization` and `Cookie` headers are stripped. The standard credential header `Proxy-Authorization` is forwarded intact to the redirect target, potentially exposing forward-proxy credentials to a host outside the original trust boundary.

Redirect following is opt-in. The redirects option defaults to false (…

---

## 21. 🟡 High Severity — LiquidJS's `{% render %}` tag silently bypasses per-render `ownPropertyOnly:true` via `Context.spawn()`

**CVE:** `CVE-2026-44646` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-9x9p-qf8f-mvjg>

> ## Summary

`Context.spawn()` in liquidjs creates a child `Context` for the `{% render %}` tag but does not propagate the parent context&#x27;s resolved `ownPropertyOnly` value. The new context re-derives `ownPropertyOnly` from `opts.ownPropertyOnly` (the instance-level option), silently discarding any `RenderOptions.ownPropertyOnly` override that was supplied to `parseAndRender()`. As a result, a…

---

## 22. 🟡 High Severity — LiquidJS's strip_html filter bypass via newline characters in HTML tags enables XSS

**CVE:** `CVE-2026-44644` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-2qv6-9wx5-cwv4>

> ## Summary

The `strip_html` filter in liquidjs is intended to remove HTML tags from a string before rendering, and is widely used as an XSS sanitizer. The implementation uses a regex whose catch-all branch (`&lt;.*?&gt;`) does not match line terminators, so any HTML tag containing a `\n` or `\r` character passes through unmodified. An attacker who can place a newline inside a tag (e.g. `&lt;img\n…

---

## 23. 🟡 High Severity — Yamcs Vulnerable to Server-Side Code Injection (RCE) via Janino Expression Engine in `JavaExprAlgorithmExecutionFactory`

**CVE:** `CVE-2026-44632` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-524g-x36v-9wm6>

> ### Summary
A Server-Side Code Injection vulnerability exists in the Yamcs algorithm evaluation engine (`org.yamcs.algorithms.JavaExprAlgorithmExecutionFactory`). The application dynamically compiles and evaluates user-controlled algorithm text without enforcing a secure sandbox. An authenticated user with the `ChangeMissionDatabase` privilege can exploit this to achieve Remote Code Execution (RCE…

---

## 24. 🟡 High Severity — Yamcs vulnerable to unauthorized user enumeration via IAM API endpoints

**CVE:** `CVE-2026-44595` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-p2rj-mrmc-9w29>

> ### Summary

The IAM API endpoints (`listUsers`, `getUser`, `listGroups`, and `getGroup`) in `yamcs-core` do not enforce the required `SystemPrivilege.ControlAccess` check. As a result, **any authenticated user** (even those with low or no privileges) can enumerate all user accounts in the system, including their usernames, superuser status, and group memberships.

This constitutes a broken access…

---

## 25. 🟡 High Severity — Kirby CMS has pre-authentication path traversal and PHP file inclusion during user lookup

**CVE:** `CVE-2026-44177` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-9hx7-c53c-v6x8>

> ### TL;DR

This vulnerability affects all Kirby sites on Kirby 5.3.0-5.4.0 and is independent from setup conditions and authentication.

**This vulnerability is of high severity for all Kirby sites**.

----

### Introduction

Path traversal is a type of attack that allows to access arbitrary filesystem paths. By using special elements such as `..` and `/` separators, attackers can escape outside o…

---

## 26. 🟡 High Severity — Kirby CMS vulnerable to cross-site scripting (XSS) from list field content in the site frontend

**CVE:** `CVE-2026-44175` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-5fhx-9q32-q257>

> ### TL;DR

This vulnerability affects all Kirby sites that use the list field or list block, when content is authored by users who may not be fully trusted. The attack requires an authenticated Panel user with update permission to any list field or list block.

**This vulnerability is of high severity for affected sites.**

Kirby sites are *not* affected if they don&#x27;t use the list field (or b…

---

## 27. 🟡 High Severity — Kirby CMS has an Arbitrary Method Call via REST API Search and Collection Query Endpoints

**CVE:** `CVE-2026-44174` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-86rh-h242-j8xp>

> ### TL;DR

This vulnerability affects all Kirby sites that might have potential attackers in the group of authenticated Panel users.

**This vulnerability is of high severity for affected sites and has a high real-world impact.**

----

### Introduction

Arbitrary method call is a type of arbitrary code execution. It is a vulnerability that allows attackers to run any commands or code of the attac…

---

## 28. 🟡 High Severity — FUXA Vulnerable to Unauthenticated Remote Code Execution via Script Test Mode Authorization Bypass

**CVE:** `CVE-2026-43947` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-rg3m-cfq7-g6h6>

> ### Summary

An unauthenticated Remote Code Execution vulnerability exists in FUXA when `secureEnabled` is set to `true`. The `POST /api/runscript` endpoint checks authorization against the stored script&#x27;s permission by ID, but when `test: true` is set in the request, it compiles and executes attacker-supplied code instead of the stored script&#x27;s code. An unauthenticated attacker who know…

---

## 29. 🟡 High Severity — FUXA Vulnerable to Pre-auth RCE via Path Manipulation & Configuration Injection

**CVE:** `CVE-2026-43945` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-p69w-mmfv-xrfj>

> **Pre-auth** RCE in FUXA via Logic Bypass

Summary

A Critical vulnerability chain exists in FUXA (v.1.3.0-2706) that allows an unauthenticated remote attacker to achieve Full Remote Code Execution (RCE) as root. The exploit succeeds even when the platform is configured in its most secure state (Secure Mode Enabled and Node-RED Secure Auth Enabled).

Details
The vulnerability is a Path Confusion f…

---

## 30. 🟡 High Severity — Yamcs Vulnerable to LDAP Injection in LdapAuthModule

**CVE:** `CVE-2026-42568` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-cqh3-jg8p-336j>

> ### Summary

An LDAP injection vulnerability exists in `org.yamcs.security.LdapAuthModule` when constructing search filters. The username parameter is inserted directly into the LDAP filter without proper RFC 4515 escaping.

### Root Cause

**File:** `yamcs-core/src/main/java/org/yamcs/security/LdapAuthModule.java:233`

The `username` parameter is inserted directly into an LDAP search filter witho…

---

## 31. 🟡 High Severity — netty-incubator-codec-ohttp's HPKEContext operations may produce empty byte[] on failures

**CVE:** `CVE-2026-41207` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-f659-372h-6x3x>

> HKDF_expand: returns non-NULL on failure. The byte[] is filled with zeros and has no way to distinguish success from failure. Since this output is used as HKDF key material for the response AEAD, a  failure silently produces an all-zero key.

When EVP_HPKE_CTX_export fails it also returns an empty byte[] array filled with zeros. This byte[] feeds directly into OHttpCrypto.createResponseAEAD(...). …

---

## 32. 🟡 High Severity — XWiki Platform's Livetable results still allow reconstructing password hashes using 768 requests

**CVE:** `CVE-2026-48048` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-rh28-mqj4-8x59>

> ### Impact
XWiki discovered that the patch for GHSA-5cf8-vrr8-8hjm was insufficient and with slightly modified parameters to the `LiveTableResults`, it is still possible to discover password hashes one bit at a time, so with 768 requests, the full password salt and hash can be retrieved of a user.

### Patches
The check for password (and email properties) has been adjusted in XWiki 18.0.0RC1, 17.1…

---

## 33. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
