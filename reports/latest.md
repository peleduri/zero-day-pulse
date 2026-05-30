# Zero Day Pulse

> **Generated:** 2026-05-30 08:16 UTC &nbsp;|&nbsp; **Total:** 52 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 15 &nbsp;|&nbsp; 🟡 High: 37 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE‑2024‑57727 is a path traversal vulnerability in SimpleHelp Remote Monitoring and Management that lets an unauthenticated attacker craft HTTP requests to download arbitrary files (e.g., serverconfig.xml) from the host, enabling credential theft and further privilege escalation.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proofs of concept have been published; examples are referenced in the vendor blog and Horizon3.ai disclosures.
- **Patch Available:** Yes – patches are available in SimpleHelp versions 5.5.8 and later.
- **Active Exploitation:** Confirmed – CISA reports active exploitation by ransomware groups such as DragonForce and Medusa.
- **Threat Actors:** DragonForce, Medusa (and other ransomware operators reported by CISA)
- **Mitigation:** Isolate affected SimpleHelp servers, block internet traffic to them, upgrade immediately to SimpleHelp 5.5.8 or later, inspect configuration files for compromise, and perform threat‑hunting for suspicious executables and network traffic as advised by CISA.
- **Vendor Advisory:** http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — vm2 has a CVE-2023-37903 patch bypass: nesting:true without explicit require still allows full RCE

**CVE:** `CVE-2026-47137` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-m4wx-m65x-ghrr>

> ## Summary

The fix for GHSA-8hg8-63c5-gwmx (CVE-2023-37903) introduced a check in `nodevm.js` line 263 that blocks the combination `nesting: true` + `require: false`. However, the check uses strict equality (`options.require === false`), which is trivially bypassed by omitting the `require` option entirely.

When `require` is not specified, `options.require` is `undefined`, not `false`. The stric…

**Parallel AI Enrichment:**

- **Technical Details:** A fix for GHSA-8hg8-63c5-gwmx (CVE-2023-37903) added a guard in nodevm.js that checks options.require === false when nesting:true to prevent full require during nested VM creation. Because the check used strict equality, callers that omit the require option (options.require === undefined) bypass the guard; later destructuring sets requireOpts = false by default, resulting in the insecure combination nesting:true with require effectively false and allowing creation of nested contexts that enable escaping the sandbox and achieving remote code execution.
- **Affected Products:** vm2 npm package versions prior to 3.11.0 (notably 3.10.4 and earlier)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC available at https://semgrep.dev/blog/2026/calling-back-to-vm2-and-escaping-sandbox
- **Patch Available:** Yes — upstream vm2 released fixes (see GitHub Security Advisory and release notes).
- **Active Exploitation:** Reports of active exploitation documented in news coverage (e.g., BleepingComputer).
- **Threat Actors:** None known
- **Mitigation:** Do not run untrusted code using vulnerable vm2 versions; upgrade to fixed vm2 >= 3.11.0 (or latest patched release). If immediate upgrade impossible, block use of nesting:true with untrusted input and ensure explicit require option is provided (do not rely on options.require === false guard). Consider running sandboxed workloads in separate hardened processes/containers and apply runtime process‑level restrictions (seccomp, user namespaces).
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — Gogs Zero-Day Exposes Servers to Remote Code Execution

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://www.securityweek.com/gogs-zero-day-exposes-servers-to-remote-code-execution/>

> The critical-severity issue, assigned a CVSS score of 9.4, is an argument injection flaw that can be exploited by authenticated attackers via pull requests with malicious branch names. The post Gogs Zero-Day Exposes Servers to Remote Code Execution appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Authenticated attackers can exploit an argument injection flaw via pull requests with malicious branch names, and misuse of symbolic links in Gogs' repository file editing allows file overwrite and remote code execution.
- **Affected Products:** Gogs (any version prior to a fix)
- **CVSS Score:** 9.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Proof of Concept available at https://github.com/zAbuQasem/gogs-CVE-2025-8110
- **Patch Available:** No official patch available yet.
- **Active Exploitation:** Yes, active exploitation reported in the wild (CISA KEV entry and security reports).
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Sandbox escape via symlink creation in workspace: a sandboxed process can create symlinks pointing outside the workspace; an unsandboxed process later follows the symlink and writes outside, enabled by a prompt injection (TOCTOU/symlink‑following path traversal).
- **Affected Products:** Anthropic Claude Code < 2.1.64
- **CVSS Score:** 7.7
- **CVSS Vector:** CVSS:4.0/AV:N/AC:L/AT:P/PR:N/UI:P/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N
- **Exploit Available:** No public PoC/weaponized exploit reported.
- **Patch Available:** Patch available: Anthropic released Claude Code 2.1.64 (https://github.com/anthropics/claude-code/security/advisories/GHSA-vp62-r36r-9xqp)
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Update to Claude Code 2.1.64 or later; avoid processing untrusted content; run Claude Code in an isolated environment; monitor for suspicious symlinks and unexpected writes.
- **Vendor Advisory:** https://github.com/anthropics/claude-code/security/advisories/GHSA-vp62-r36r-9xqp

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an attack technique that injects malicious instructions into data sources or tools an LLM consumes (e.g., web content, documents, tool outputs) to influence model behavior while processing a user’s query; attacks can succeed without direct user input and exploit agentic automation and multi‑source contexts.
- **Affected Products:** Google Workspace (features including Gmail, Docs) when used with Gemini
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public proof-of-concept or weaponized exploit reported
- **Patch Available:** No single "patch" — Google reports ongoing, continuously‑deployed mitigations and provides the advisory URL above.
- **Active Exploitation:** No confirmed active exploitation in the wild reported in the vendor advisory or cited prior reports.
- **Threat Actors:** None known
- **Mitigation:** Defense-in-depth including continuous discovery (human and automated red‑teaming, VRP, OSINT), synthetic-data-driven ML retraining, deterministic defenses (URL sanitization, user confirmation, policy engine tool‑chaining controls, regex takedowns), LLM‑based defenses via prompt engineering, and Gemini model hardening; operational recommendation: enable layered controls, apply URL/tool sanitization policies, enforce user confirmations for risky tool actions, and participate in vendor guidance.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when untrusted web content (pages, iframes, UGC, ads) manipulates an agent’s planning model to perform unwanted actions such as financial transactions or data exfiltration. Chrome counters include a User Alignment Critic that vets planned actions, Agent Origin Sets limiting readable/writeable origins, a prompt‑injection classifier, deterministic checks for sensitive URLs/actions, user confirmations, and continuous red‑teaming/monitoring.
- **Affected Products:** Chrome (agentic capabilities with Gemini)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit reported.
- **Patch Available:** Chrome auto‑update delivers fixes; no discrete patch URL provided.
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Use of User Alignment Critic, origin gating (read‑only vs read‑write origins), real‑time prompt‑injection classifier, deterministic sensitive‑site checks, user confirmations for sensitive actions, and Chrome auto‑update for fixes.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Android platform (first‑party and third‑party/open‑source components across C, C++, Java, Kotlin, and Rust)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit available.
- **Patch Available:** No patch available or applicable.
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack where hidden malicious instructions are embedded within external data sources (web content, emails, documents, invites). Agentic AI or LLM‑powered features that ingest external content can unwittingly execute these instructions, leading to data exfiltration or unsafe actions.
- **Affected Products:** Affected products unavailable (general class: agentic browsers and LLM‑integrated apps such as Gemini for Chrome and Workspace apps)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC/weaponized exploit reported in prior context
- **Patch Available:** Not applicable; mitigation guidance and layered defenses provided by vendors (see vendor advisory)
- **Active Exploitation:** Reports of increasing IPI attempts on public web (sources: Google analyses, security news) but no confirmed large‑scale exploitation detailed
- **Threat Actors:** None known
- **Mitigation:** Apply layered defense: input provenance checks, origin‑restricted content access, content sanitization/whitelisting, agent‑level policy enforcement, least‑privilege data access, user confirmation for sensitive actions, monitoring/alerting for anomalous agent behavior.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors compromise backbone, provider edge, and customer edge routers, modify firmware or configuration to maintain persistent access, and use trusted connections to pivot into adjacent networks, enabling long‑term espionage.
- **Affected Products:** Backbone routers, Provider Edge (PE) routers, Customer Edge (CE) routers
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit or PoC available.
- **Patch Available:** No official patch available.
- **Active Exploitation:** Confirmed active exploitation; actors have obtained persistent access to government, telecom, transportation, lodging, and military infrastructure networks.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Apply latest firmware updates to backbone, PE, and CE routers; segment and isolate critical network segments; enforce strong authentication and access controls; monitor for anomalous router behavior; implement network‑level intrusion detection and blacklist known malicious IPs.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Actors leveraged credential‑stuffing and brute‑force, spear‑phishing, and exploited specific vulnerabilities: Outlook NTLM relay (CVE‑2023‑23397), Roundcube XSS/command execution (CVE‑2020‑12641, CVE‑2020‑35730, CVE‑2021‑44026), WinRAR arbitrary code execution (CVE‑2023‑38831), and flaws in internet‑facing VPN/SOHO devices to gain initial access and persist, then exfiltrated data via native tools and staged uploads.
- **Affected Products:** Microsoft Outlook (CVE‑2023‑23397), WinRAR (CVE‑2023‑38831), Roundcube Webmail (versions before 1.4.4, 1.2.13, 1.3.x before 1.3.16, 1.4.x before 1.4.10), Internet‑facing VPNs and SOHO devices
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof‑of‑concept exploits exist for CVE‑2023‑23397 (Outlook) and CVE‑2023‑38831 (WinRAR); weaponised exploitation has been observed in GRU‑attributed campaigns.
- **Patch Available:** Patch available from Microsoft for CVE‑2023‑23397, from RARLAB for CVE‑2023‑38831, and from Roundcube for CVE‑2020‑12641, CVE‑2020‑35730, and CVE‑2021‑44026.
- **Active Exploitation:** Yes—CISA, FBI, and NSA joint advisories report active exploitation of these CVEs by GRU‑attributed campaigns targeting logistics and technology companies.
- **Threat Actors:** GRU 85th Main Special Service Center (unit 26165), also known as APT28, Fancy Bear, Forest Blizzard, BlueDelta.
- **Mitigation:** Prioritize applying vendor patches; disable or harden NTLM and legacy authentication protocols; enforce MFA; monitor authentication logs; restrict remote access; audit and remove unnecessary mailbox permissions; inventory and secure SOHO devices; monitor PowerShell and scheduled tasks; follow vendor‑recommended hardening guidance.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟠 Zero-Day — PAN-OS GlobalProtect Authentication Bypass (CVE-2026-0257) Under Active Exploitation

**CVE:** `CVE-2026-0257` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-30
**Reference:** <https://thehackernews.com/2026/05/pan-os-globalprotect-authentication.html>

> Palo Alto Networks has warned that a recently disclosed medium-severity security flaw impacting PAN-OS and Prisma Access has come under active exploitation in the wild.

The vulnerability, tracked as CVE-2026-0257 (CVSS score: 7.8), refers to a case of authentication bypass that could be exploited by bad actors to set up VPN connections.

&quot;Authentication bypass vulnerabilities in the

---

## 12. 🟠 Zero-Day — PraisonAI: Arbitrary code execution via unguarded `spec.loader.exec_module` in `agents_generator.py` - sibling of CVE-2026-44334

**CVE:** `CVE-2026-47398` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-78r8-wwqv-r299>

> &lt;html&gt;&lt;head&gt;&lt;/head&gt;&lt;body&gt;&lt;h2&gt;Arbitrary code execution via ungated &lt;code&gt;spec.loader.exec_module&lt;/code&gt; in &lt;code&gt;agents_generator.py&lt;/code&gt; (v4.6.32 chokepoint refactor bypass)&lt;/h2&gt;
&lt;h3&gt;Summary&lt;/h3&gt;
&lt;p&gt;The v4.6.32 chokepoint refactor (which patched CVE-2026-44334 / GHSA-xcmw-grxf-wjhj) added the &lt;code&gt;PRAISONAI_ALLO…

---

## 13. 🟠 Zero-Day — ChatGPhish Vulnerability Turns ChatGPT Web Summaries Into a Phishing Surface

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://thehackernews.com/2026/05/chatgphish-vulnerability-turns-chatgpt.html>

> Cybersecurity researchers have disclosed details of a vulnerability in OpenAI ChatGPT that leverages the artificial intelligence (AI) assistant&#x27;s implicit trust in Markdown links and images to trigger prompt injections and open the door to phishing attacks.

The technique has been codenamed ChatGPhish by Permiso Security.

&quot;The chatgpt.com response renderer trusts Markdown links and Mark…

---

## 14. 🟠 Zero-Day — Axios has a Patch Bypass: Proxy-Authorization Header Injection via Prototype Pollution — Incomplete Null-Prototype Fix

**CVE:** `CVE-2026-44489` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-654m-c8p4-x5fp>

> # [Patch Bypass] Proxy-Authorization Header Injection via Prototype Pollution — Incomplete Null-Prototype Fix in Axios 1.15.2

## Summary

The `Object.create(null)` fix introduced in Axios 1.15.2 (GHSA-q8qp-cvcw-x6jj) protects the **top-level config object** from prototype pollution. However, **nested objects** created by `utils.merge()` (e.g., `config.proxy`) are still constructed as plain `{}` w…

---

## 15. 🟠 Zero-Day — Microsoft calls zero-day releases ‘never justifiable’ as researcher threatens to drop more

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Record by Recorded Future &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more>

> Each vulnerability was published with working proof-of-concept code to the Microsoft-owned code repository GitHub, making them immediately available to both attackers and security professionals.

---

## 16. 🟡 High Severity — praisonai-platform: Any workspace member can promote themselves or others to owner via PATCH /workspaces/{id}/members/{user_id}

**CVE:** `CVE-2026-47416` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-c2m8-4gcg-v22g>

> ## Summary

**Type:** Vertical privilege escalation. The `PATCH /workspaces/{workspace_id}/members/{user_id}` endpoint is gated by `require_workspace_member(workspace_id)`, which defaults to `min_role=&quot;member&quot;` and is never overridden by the route. The handler then calls `MemberService.update_role(workspace_id, user_id, body.role)` which sets the target member&#x27;s role to whatever the…

---

## 17. 🟡 High Severity — praisonai-platform: JWT signing key defaults to hardcoded "dev-secret-change-me", allowing token forgery for any user when PLATFORM_ENV is unset

**CVE:** `CVE-2026-47410` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-3qg8-5g3r-79v5>

> ## Summary

**Type:** Insecure default cryptographic key. The JWT signing secret defaults to the hardcoded literal `&quot;dev-secret-change-me&quot;` when `PLATFORM_JWT_SECRET` is unset. A safety check exists but only fires when `PLATFORM_ENV != &quot;dev&quot;`; the default value of `PLATFORM_ENV` is `&quot;dev&quot;`, so the check is silently bypassed in any deployment that does not explicitly o…

---

## 18. 🟡 High Severity — PraisonAI Platform: Missing role checks let any workspace member become owner and control workspace membership

**CVE:** `CVE-2026-47405` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-h37g-4h4p-9x97>

> ### Summary

PraisonAI Platform has a broken workspace authorization check that allows any authenticated low-privilege workspace member to escalate their own role to `owner`.

The issue is caused by privileged workspace-management routes using the shared dependency `require_workspace_member(...)` without requiring `admin` or `owner`. The dependency defaults to `min_role=&quot;member&quot;`, so rou…

---

## 19. 🟡 High Severity — PraisonAI Platform workspace-scoped routes allow cross-workspace object access by global object ID

**CVE:** `CVE-2026-47399` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-6h6v-6m7w-7vxx>

> ### Summary

PraisonAI Platform&#x27;s workspace-scoped REST routes contain a systemic object-level authorization flaw that allows an authenticated user from one workspace to access, modify, and delete objects belonging to another workspace by supplying the victim object&#x27;s global UUID.

The affected pattern appears in workspace-scoped routes such as agents, projects, issues, and comments. The…

---

## 20. 🟡 High Severity — PraisonAI Platform has a cross-workspace IDOR + member-role privilege escalation

**CVE:** `CVE-2026-47407` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-h8q5-cp56-rr65>

> ## Summary

The Platform server exposes resources under `/api/v1/workspaces/{workspace_id}/...` and protects them with a `require_workspace_member(workspace_id)` FastAPI dependency. The dependency only checks that the caller is a member of the workspace_id in the URL prefix. The route handlers then look up the inner resource (`agent_id`, `issue_id`, `project_id`, `label_id`, `comment_id`, `depende…

---

## 21. 🟡 High Severity — praisonai-platform: list_issue_activity returns activity log for any issue regardless of workspace ownership

**CVE:** `CVE-2026-47408` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-27p4-pjqv-whgj>

> ## Summary

**Type:** Insecure Direct Object Reference. The `GET /workspaces/{workspace_id}/issues/{issue_id}/activity` endpoint is gated by `require_workspace_member(workspace_id)` and dispatches to `ActivityService.list_for_issue(issue_id)`, which executes `SELECT * FROM activity WHERE issue_id = :issue_id` with no workspace constraint. A user who is a member of any workspace can read the full a…

---

## 22. 🟡 High Severity — PraisonAI has Cross-Workspace IDOR and Privilege Escalation via Platform API

**CVE:** `CVE-2026-48169` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-gv23-xrm3-8c62>

> ### Summary

The PraisonAI Platform API has two authorization failures that together break workspace isolation. The service layer for issues and projects performs global primary-key lookups without checking workspace ownership, so any authenticated user can read, modify, and delete resources in any workspace just by swapping UUIDs in their API requests. On top of that, every member management endp…

---

## 23. 🟡 High Severity — PraisonAI has an Arbitrary File Write in Python API

**CVE:** `CVE-2026-47397` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-hvhp-v2gc-268q>

> # Bug Report: Arbitrary File Write in Python API

## Summary

Hidden metadata in a webpage causes PraisonAI agents to write attacker-controlled content to arbitrary paths. `write_file` skips path validation when `workspace=None` (always `None` in production).

## Affected

PraisonAI &lt;= 4.6.37 (pip install praisonai)

## Root Cause

`code/tools/write_file.py:77-83` — path validation skipped when…

---

## 24. 🟡 High Severity — PraisonAI's unauthenticated A2A official example can reach real LLM-driven `eval()` tool execution

**CVE:** `CVE-2026-47391` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-vg22-4gmj-prxw>

> ## Summary

The first-party PraisonAI A2A server example combines three behaviors into a remotely exploitable Critical chain:

1. The example exposes an A2A server without configuring `auth_token`.
2. The same example binds the server to `0.0.0.0`.
3. The example registers a `calculate(expression)` tool implemented with Python `eval(expression)`.

An unauthenticated network client can send a JSON-…

---

## 25. 🟡 High Severity — PraisonAI vulnerable to unauthenticated arbitrary file read via MCP workflow.show, workflow.validate, deploy.validate

**CVE:** `CVE-2026-47394` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-9cr9-25q5-8prj>

> ## Summary

The fix for GHSA-9mqq-jqxf-grvw / CVE-2026-44336 is incomplete. The original advisory description named four vulnerable handlers in `mcp_server/adapters/cli_tools.py`:

&gt; &quot;registers four file-handling tools by default, `praisonai.rules.create`, `praisonai.rules.show`, `praisonai.rules.delete`, **and `praisonai.workflow.show`**. Each accepts a path or filename string from MCP `t…

---

## 26. 🟡 High Severity — PraisonAI vulnerable to sandbox escape via `print.__self__` builtins module leak in `execute_code` (subprocess mode)

**CVE:** `CVE-2026-47392` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-4mr5-g6f9-cfrh>

> ## Summary

`execute_code()` in `praisonaiagents/tools/python_tools.py` (v1.6.37, subprocess sandbox mode) can be fully bypassed using `print.__self__` to retrieve the real Python `builtins` module, from which `__import__` can be extracted via `vars()` and runtime string construction. This achieves arbitrary OS command execution on the host, completely defeating the sandbox.

This is a **novel byp…

---

## 27. 🟡 High Severity — PraisonAI CLI automatically resolves @url mentions in prompt text and can read loopback URLs into model context

**CVE:** `CVE-2026-47395` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-5cxw-77wg-jrf3>

> ### Summary

PraisonAI&#x27;s direct-prompt CLI automatically expands `@url:` mentions in raw prompt text before agent execution begins.

If a prompt contains `@url:&lt;http-or-https-url&gt;`, the CLI calls `MentionsParser.process(...)`. The `@url:` handler then performs a direct `urllib.request.urlopen()` request to the attacker-controlled URL and returns the response body. That response body is …

---

## 28. 🟡 High Severity — PraisonAI spider_tools SSRF protection bypass via alternate loopback host encodings

**CVE:** `CVE-2026-47390` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-5c6w-wwfq-7qqm>

> ### Summary

PraisonAI&#x27;s `spider_tools` URL validation can be bypassed using alternate loopback host encodings.

The affected component is:

```text
praisonaiagents/tools/spider_tools.py
````

The tool contains a URL validation function intended to block local or unsafe targets before fetching attacker-controlled URLs. However, the validation only blocks a small set of exact host strings such…

---

## 29. 🟡 High Severity — Nezha's authenticated DDNS webhook configuration allows blind SSRF from the dashboard host

**CVE:** `CVE-2026-47268` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-6x26-5727-rrm9>

> #### Summary

An authenticated Nezha dashboard user can create or update a DDNS profile with provider `webhook` and configure an arbitrary `webhook_url`, HTTP method, request body, and headers. When DDNS is triggered for a server that uses that profile, the dashboard process sends the configured request with `utils.HttpClient` without the SSRF protections used by notification webhooks.

This allow…

---

## 30. 🟡 High Severity — Admidio: CSRF in SSO client `enable` action toggles SAML/OIDC clients without token validation

**CVE:** `CVE-2026-47229` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-xg76-5qj2-2hhv>

> ## Summary

`modules/sso/clients.php` validates an `adm_csrf_token` on every state-changing branch except `enable`. The `enable` case loads the SAML or OIDC client by UUID, calls `$client-&gt;enable($enabled)`, and persists the new state with no token check. Because the action is reachable via plain GET parameters, a third-party page can trick an authenticated administrator into disabling (or sile…

---

## 31. 🟡 High Severity — BoxLite has a Timeout Bypass Vulnerability

**CVE:** `CVE-2026-47213` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-xjhv-pp2r-6f82>

> #### Summary

BoxLite is a sandbox service that allows users to create lightweight virtual machines (Boxes) and run OCI containers within them. BoxLite allows users to configure a timeout for services running inside the virtual machine. When the timeout is triggered, BoxLite sends a signal to kill the process. However, instead of using the uncatchable SIGKILL signal, BoxLite uses the catchable SIG…

---

## 32. 🟡 High Severity — Symfony: Twilio SMS Notifier allows unauthenticated webhook injection due to missing X-Twilio-Signature verification

**CVE:** `CVE-2026-47212` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-55rj-x2vc-4whq>

> ### Description

The Twilio SMS notifier bridge ships a webhook request parser used to authenticate and decode the status callbacks Twilio POSTs to an application&#x27;s webhook endpoint. Its `doParse(Request $request, #[\SensitiveParameter] string $secret)` method receives the configured webhook secret but never reads it; it decodes and returns the payload unconditionally, ignoring the `X-Twilio-…

---

## 33. 🟡 High Severity — ouroboros-ai Vulnerable to Remote Code Execution via Untrusted Project-Directory .env

**CVE:** `CVE-2026-47211` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-c4m7-2gwp-vw76>

> ### Impact
A Remote Code Execution (RCE) vulnerability was discovered in Ouroboros. If a user clones a malicious repository and runs Ouroboros commands within that directory, it can lead to arbitrary code execution and potential system takeover.

The vulnerability (CWE-426: Untrusted Search Path &amp; CWE-15: External Control of System Setting) stems from Ouroboros loading the `.env` file from the…

---

## 34. 🟡 High Severity — CC-Tweaked has an SSRF Protection Bypass with NAT64

**CVE:** `CVE-2026-47695` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-5jh9-2h63-pw4q>

> ### Summary

CC-Tweaked&#x27;s HTTP API (`http.request`, `http.websocket`) blocks requests to private network ranges to prevent server-side request forgery (SSRF). This protection can be bypassed on IPv6-capable servers using NAT64 well-known prefix addresses (`64:ff9b::/96`). An attacker who can execute Lua code can reach any internal IPv4 service that the filter is intended to block, by addressi…

---

## 35. 🟡 High Severity — Koel Vulnerable to SSRF via Podcast Episode Enclosure URLs

**CVE:** `CVE-2026-47260` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-7j2f-6h2r-6cqc>

> ## Summary

Koel validates the podcast feed URL via the `SafeUrl` rule (DNS resolution + public IP check), but the individual episode `&lt;enclosure url=&quot;...&quot;&gt;` values extracted from the RSS XML are stored directly into the database without any SSRF validation. When a user plays an episode, the server downloads the full HTTP response from the unvalidated enclosure URL via `Http::sink(…

---

## 36. 🟡 High Severity — Sparkle's AppInstaller post-stage-1 XPC listener accepts unvalidated connections, allowing spoofed appcast item data injection

**CVE:** `CVE-2026-47122` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-g3hp-f6mg-559v>

> ## Summary

AppInstaller post-stage-1 XPC listener accepts unvalidated connections, allowing spoofed appcast item data injection.

## Details

`Autoupdate/AppInstaller.m`&#x27;s `shouldAcceptNewConnection:` only enforces `SUCodeSigningVerifier validateConnection:` before stage 1 completes. After `_performedStage1Installation = YES`, new connections to the registered Mach service `&lt;bundleId&gt;-…

---

## 37. 🟡 High Severity — russh server userauth state is not reset when authentication principal changes

**CVE:** `CVE-2026-46705` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-hpv4-5h6f-wqr3>

> ### Summary
The `russh` server authentication path keeps internal userauth state across `SSH_MSG_USERAUTH_REQUEST` messages without separating that state when the request principal changes.

RFC 4252 allows the `user name` and `service name` fields to change between authentication requests. The issue is not that such changes are invalid. The issue is that russh-owned authentication state, such as …

---

## 38. 🟡 High Severity — Metasploit Wrap Up 05/29/2026

**CVE:** `CVE-2026-43284` | `CVE-2026-43500` | `CVE-2026-3055` | `CVE-2022-28368` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-05-29-2026>

> More Linux LPEs Hark the age of the Linux LPE has arrived. This week’s release follows up on recent work bringing new Linux LPEs to Metasploit users. Copy Fail seemed to have kicked off a trend of similar bugs and hot on its heels is Dirty Frag. Dirty Frag is actually two vulnerabilities in a trenchcoat, individually identified as CVE-2026-43284 and CVE-2026-43500. Each is exploitable individually…

---

## 39. 🟡 High Severity — amazon-redshift-python-driver vulnerable to Remote Code Execution via eval() Injection

**CVE:** `CVE-2026-8838` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-29h4-r29x-hchv>

> ### Summary
amazon-redshift-python-driver is the official Python connector for Amazon Redshift. In versions 2.1.13 and earlier, the driver insufficiently validates data received from the server during query result processing. A rogue server or man-in-the-middle could leverage this to execute arbitrary code on the client.

### Impact
When a client connects to a rogue server implementing the Postgre…

---

## 40. 🟡 High Severity — AgenticMail API/storage and outbound relay hardening fixes

**CVE:** `CVE-2026-47255` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-wjjv-3mj2-39hf>

> The current upstream main branch at commit 7e0206d was reviewed, and the fix-first patch set was rebased on 2026-05-18. The patches cover: validated and bound inactive-agent hour filtering; storage SQL identifier validation; metadata-backed ownership checks for raw storage SQL; blocking direct storage metadata access through raw SQL; fail-closed outbound worker secret handling; SMTP envelope/heade…

---

## 41. 🟡 High Severity — unbounded-spsc: Sender::send pointer-as-value transmute causes OOB read and fake-Arc drop under TX/RX race

**CVE:** `CVE-2026-46690` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-6m57-8r3p-pqx6>

> ## Summary

`Sender::send` in `src/lib.rs` contains an `unsafe` block in the `DISCONNECTED` arm that transmutes a **raw pointer** (`*mut Producer&lt;T&gt;`) into the bytes of a **value-level** `Consumer&lt;T&gt;`. The author&#x27;s intent, visible in the surrounding comment at lines 386-390, was a value transmute. The shipped code is one level of indirection off.

The resulting `Consumer&lt;T&gt;`…

---

## 42. 🟡 High Severity — IPAM controller service account granted unnecessary full access to Secrets

**CVE:** `CVE-2026-47190` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-49pm-43hf-6xfq>

> ### Impact

IPAM is the IP address Manager for Cluster API Provider Metal3. The IPAM controller&#x27;s ClusterRole granted full CRUD permissions (create, delete, get, list, patch, update, watch) on core/v1 Secrets. The controller never accesses Secrets during normal operation. If the controller pod were compromised (e.g. via supply chain attack or container escape), an attacker could leverage thes…

---

## 43. 🟡 High Severity — NodeVM observability builtins leak host process and HTTP request data

**CVE:** `CVE-2026-47141` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-9g8x-92q2-p28f>

> ## Summary

`NodeVM` exposes some process-wide observability builtins when they are allowed through `require.builtin`.

The following builtins are not blocked by the dangerous builtin denylist:

```text
diagnostics_channel
async_hooks
perf_hooks
```

These modules are process-wide, not sandbox-local. Sandboxed code can use them to observe host application data across the vm2 boundary.

**Note**: I…

---

## 44. 🟡 High Severity — NodeVM network builtin exclusions bypass via internal _http_client and _http_server

**CVE:** `CVE-2026-47139` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-r9pm-gxmw-wv6p>

> ## Summary

`NodeVM` supports excluding public network builtins from the wildcard builtin option. With this configuration direct access to `http`, `https`, `http2`, `net`, `dgram`, `tls`, `dns`, and `dns/promises` is blocked.

However, Node.js also exposes underscored internal HTTP builtins such as `_http_client` and `_http_server`. These are not blocked when the public modules are excluded.

Sand…

---

## 45. 🟡 High Severity — vm2 sandbox escape via JSPI-backed Promise `.finally()` species bypass

**CVE:** `CVE-2026-47210` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-6j2x-vhqr-qr7q>

> ### Summary
A sandbox escape vulnerability in `vm2` allows arbitrary code execution in the host process when untrusted code is executed with async support on runtimes exposing WebAssembly JSPI (`WebAssembly.promising` / `WebAssembly.Suspending`). In the tested configuration, a JSPI-backed Promise can reach `Promise.prototype.finally()` in a way that bypasses the expected Promise-species hardening …

---

## 46. 🟡 High Severity — vm2 is Vulnerable to Sandbox Breakout Through Promise Species

**CVE:** `CVE-2026-47208` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-76w7-j9cq-rx2j>

> ### Summary

VM2 suffers from a sandbox breakout vulnerability. This allows attackers to write code which can escape from the VM2 sandbox and execute arbitrary commands on the host system.

### Details

The `localPromise` constructor was changed to call `this.then(undefined, eater)` to ensure a rejected promise is always used. However, this is missing a call to `resetPromiseSpecies` to ensure that…

---

## 47. 🟡 High Severity — Gotenberg has an SSRF deny-list bypass in IsPublicIP via IPv6 6to4 / NAT64 / site-local prefixes

**CVE:** `CVE-2026-45741` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-86m8-88fq-xfxp>

> ### Summary

`IsPublicIP` in `pkg/gotenberg/outbound.go` incorrectly classifies IPv6 6to4 / NAT64 / deprecated site-local addresses as public IPs, allowing an unauthenticated attacker to reach internal destinations (e.g., cloud metadata services at `169.254.169.254`) via a single crafted DNS AAAA record. This is a variant of CVE-2026-44430 (modelcontextprotocol/registry).

### Details

`IsPublicIP…

---

## 48. 🟡 High Severity — axios Vulnerable to Credential Theft and Response Hijacking via Prototype Pollution Gadget in Config Merge

**CVE:** `CVE-2026-44495` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-3g43-6gmg-66jw>

> ## Summary

Axios versions before the fixed releases contain prototype-pollution gadgets in request config processing. If another vulnerability in the same JavaScript process has already polluted `Object.prototype.transformResponse`, affected Axios versions may treat that inherited value as request configuration or as an option validator.

Axios does not itself create the prototype pollution. Expl…

---

## 49. 🟡 High Severity — axios Vulnerable to Full Man-in-the-Middle via Prototype Pollution Gadget in `config.proxy`

**CVE:** `CVE-2026-44494` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-35jp-ww65-95wh>

> # Vulnerability Disclosure: Full Man-in-the-Middle via Prototype Pollution Gadget in `config.proxy`

## Summary

The Axios library is vulnerable to a Prototype Pollution &quot;Gadget&quot; attack that allows any `Object.prototype` pollution in the application&#x27;s dependency tree to be escalated into a **full Man-in-the-Middle (MITM) attack** — intercepting, reading, and modifying all HTTP traff…

---

## 50. 🟡 High Severity — Froxlor has privilege escalation in SSH key synchronization via symlinked `authorized_keys` path

**CVE:** `CVE-2026-41236` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-mq5v-pxpm-8jw2>

> ### Summary
Froxlor 2.3.6 contains a symlink-following flaw in the root-owned SSH key synchronization path used for customer FTP users. The provisioning code appends public keys to `~/.ssh/authorized_keys` under a customer-controlled home directory without verifying that the target path is not a symbolic link.

If an attacker controls a shell-enabled customer account and can modify files inside th…

---

## 51. 🟡 High Severity — GitHub CLI has an incorrect authorization header in API requests to TUF repository mirrors via `gh attestation`, `gh release verify`, and `gh release verify-asset` commands

**CVE:** `CVE-2026-48501` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-8xvp-7hj6-mcj9>

> ### Summary

GitHub CLI incorrectly includes an authorization header in API requests to TUF repository mirrors via `gh attestation`, `gh release verify`, and `gh release verify-asset` commands.

 **Affected users:**

  - Authenticated `github.com` users who previously ran `gh attestation` commands, `gh release verify`, or `gh release verify-asset`: the `github.com` token was included in requests t…

---

## 52. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
