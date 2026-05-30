# Zero Day Pulse

> **Generated:** 2026-05-30 19:00 UTC &nbsp;|&nbsp; **Total:** 37 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 27 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Multiple unauthenticated path traversal (directory traversal) vulnerabilities in SimpleHelp <=5.5.7 allow attackers to retrieve arbitrary files (logs, configuration files, credentials), enabling further compromise and account takeover.
- **Affected Products:** SimpleHelp remote support software v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** DragonForce ransomware actors
- **Mitigation:** Upgrade SimpleHelp to version 5.5.8 immediately. If patching is delayed, restrict network access to SimpleHelp (block external access, allow only trusted management networks), implement firewall rules and VPN access, rotate any credentials discovered on affected systems, monitor logs for suspicious file access, and isolate compromised hosts. Follow additional mitigation guidance from the CISA advisory.
- **Vendor Advisory:** https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) uses hidden or untrusted web content (e.g., hidden HTML, third‑party scripts, persistent memory in AI agents) to insert instructions that influence AI assistant behavior, enabling data exfiltration, fraud, or code execution when an agent incorporates that content into prompts.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Harden agent input handling—sanitize and validate web‑sourced content, restrict parsing of hidden DOM elements and scripts, apply provenance checks, disable automatic execution of untrusted content, implement rate‑limiting and monitoring for anomalous agent behavior.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is a threat where attacker‑supplied instructions are injected into data or tools consumed by an LLM (e.g., files, connectors, web content) causing the model to follow malicious instructions when completing the user query. IPI can occur without direct user input and is mitigated via layered defenses including sanitization, provenance, and model instruction controls.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses: data filtering and sanitization of external sources, provenance tracking, tool/output validation, model-level instruction filtering and policy enforcement, continuous monitoring and threat intelligence sharing.
- **Vendor Advisory:** http://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection embeds hidden or manipulated instructions in web content that are later ingested by the LLM agent, causing it to perform unwanted actions such as unauthorized transactions or data exfiltration. CVE‑2026‑0628 is a privilege‑escalation flaw in Chrome's Gemini integration that lets a malicious extension bypass user consent, read local files, capture media, and execute arbitrary commands within the browser environment.
- **Affected Products:** Google Chrome (agentic capabilities / Gemini feature)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Enable Chrome's built‑in prompt‑injection classifier, keep Chrome (including the Gemini/agentic component) up‑to‑date with the January 2026 patch, restrict third‑party extensions, and apply network‑level filtering to block malicious web content that could deliver indirect prompt injections.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Adopting Rust in Android reduces memory‑safety vulnerabilities (use‑after‑free, buffer overflows, etc.) by shifting new code to a memory‑safe language, resulting in memory‑safety bugs falling below 20% of total vulnerabilities in 2025.
- **Affected Products:** Android platform (first‑party and third‑party/open‑source components across C, C++, Java, Kotlin, and Rust) — 2025 coverage
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Continue migrating new native components to Rust, apply standard hardening (least privilege, sandboxing), keep platform updates applied; for C/C++ components use ASLR, stack canaries, bounds‑checking tools, sanitizer builds, and timely patching.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injections involve hidden malicious instructions placed in external data sources such as websites, emails, documents, or calendar invites. When an LLM processes this content, the concealed commands are executed, allowing attackers to influence the model’s behavior without a direct prompt.
- **Affected Products:** Microsoft Copilot Studio
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Adopt a layered defense strategy: sanitize and validate all inputs, verify the provenance of external data, enforce context checks before feeding data to LLMs, filter model outputs for suspicious commands, and continuously monitor interactions for anomalous behavior.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors target large backbone routers (including PE and CE routers) and leverage compromised devices and trusted connections to pivot; they modify routers to maintain persistent, long-term access to networks
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon; OPERATOR PANDA; RedMike; UNC5807; GhostEmperor
- **Mitigation:** Key mitigations per advisory: monitor and harden backbone, provider edge (PE) and customer edge (CE) routers; restrict and monitor trusted network connections; detect and remediate router modifications that enable persistence; follow CISA/National Security Agency mitigation guidance
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** The campaign exploits multiple known flaws: CVE-2023-23397 in Microsoft Outlook allows remote code execution via crafted NTLM authentication requests; CVE-2023-38831 in WinRAR enables arbitrary code execution when a malicious RAR archive is opened; and several Roundcube webmail vulnerabilities (CVE-2020-12641, CVE-2020-35730, CVE-2021-44026) permit credential theft and cross‑site scripting. Attackers chain these flaws to gain initial access and move laterally within target networks.
- **Affected Products:** Microsoft Outlook (CVE-2023-23397), WinRAR (CVE-2023-38831), Roundcube (CVE-2020-12641, CVE-2020-35730, CVE-2021-44026)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** APT28, Fancy Bear, Forest Blizzard, Blue Delta
- **Mitigation:** Segment networks, enforce MFA, apply all vendor‑released patches (e.g., Outlook, WinRAR, Roundcube), update firmware on IP cameras, disable unnecessary remote access to cameras, and ensure IP cameras are supported. Also employ strong password policies and monitor for IOCs such as Certipy, Get‑GPPPassword.py, and ldap‑dump.py.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟠 Zero-Day — PAN-OS GlobalProtect Authentication Bypass (CVE-2026-0257) Under Active Exploitation

**CVE:** `CVE-2026-0257` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-30
**Reference:** <https://thehackernews.com/2026/05/pan-os-globalprotect-authentication.html>

> Palo Alto Networks has warned that a recently disclosed medium-severity security flaw impacting PAN-OS and Prisma Access has come under active exploitation in the wild.

The vulnerability, tracked as CVE-2026-0257 (CVSS score: 7.8), refers to a case of authentication bypass that could be exploited by bad actors to set up VPN connections.

&quot;Authentication bypass vulnerabilities in the

**Parallel AI Enrichment:**

- **Technical Details:** Authentication bypass in GlobalProtect portal and gateway allowing unauthorized VPN establishment by an attacker exploiting flawed authentication handling.
- **Affected Products:** PAN‑OS (GlobalProtect portal and gateway)
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply vendor‑provided patches/updates immediately; if patching is delayed, disable GlobalProtect portal/gateway where feasible, restrict administrative access, implement compensating access controls and monitoring as listed in the advisory.
- **Vendor Advisory:** https://security.paloaltonetworks.com/CVE-2026-0257

---

## 10. 🟠 Zero-Day — PraisonAI: Arbitrary code execution via unguarded `spec.loader.exec_module` in `agents_generator.py` - sibling of CVE-2026-44334

**CVE:** `CVE-2026-47398` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-78r8-wwqv-r299>

> &lt;html&gt;&lt;head&gt;&lt;/head&gt;&lt;body&gt;&lt;h2&gt;Arbitrary code execution via ungated &lt;code&gt;spec.loader.exec_module&lt;/code&gt; in &lt;code&gt;agents_generator.py&lt;/code&gt; (v4.6.32 chokepoint refactor bypass)&lt;/h2&gt;
&lt;h3&gt;Summary&lt;/h3&gt;
&lt;p&gt;The v4.6.32 chokepoint refactor (which patched CVE-2026-44334 / GHSA-xcmw-grxf-wjhj) added the &lt;code&gt;PRAISONAI_ALLO…

**Parallel AI Enrichment:**

- **Technical Details:** Two unguarded `spec.loader.exec_module` calls in `praisonai/agents_generator.py` (functions `load_tools_from_module` and `load_tools_from_module_class`) load modules specified by `module_path` from `agents.yaml` without the `PRAISONAI_ALLOW_LOCAL_TOOLS` gate or any path validation, enabling remote code execution when an attacker controls the module path.
- **Affected Products:** PraisonAI (pip) versions >= 2.0.0, <= 4.6.39
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Set PRAISONAI_ALLOW_LOCAL_TOOLS="true" only when safe; apply strict allowlist validation of module_path; upgrade to patched version 4.6.40; disable network‑reachable recipe server defaults (avoid allow_any_github=True) and restrict writable/shared config directories.
- **Vendor Advisory:** https://github.com/advisories/GHSA-78r8-wwqv-r299

---

## 11. 🟡 High Severity — praisonai-platform: Any workspace member can promote themselves or others to owner via PATCH /workspaces/{id}/members/{user_id}

**CVE:** `CVE-2026-47416` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-c2m8-4gcg-v22g>

> ## Summary

**Type:** Vertical privilege escalation. The `PATCH /workspaces/{workspace_id}/members/{user_id}` endpoint is gated by `require_workspace_member(workspace_id)`, which defaults to `min_role=&quot;member&quot;` and is never overridden by the route. The handler then calls `MemberService.update_role(workspace_id, user_id, body.role)` which sets the target member&#x27;s role to whatever the…

---

## 12. 🟡 High Severity — praisonai-platform: JWT signing key defaults to hardcoded "dev-secret-change-me", allowing token forgery for any user when PLATFORM_ENV is unset

**CVE:** `CVE-2026-47410` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-3qg8-5g3r-79v5>

> ## Summary

**Type:** Insecure default cryptographic key. The JWT signing secret defaults to the hardcoded literal `&quot;dev-secret-change-me&quot;` when `PLATFORM_JWT_SECRET` is unset. A safety check exists but only fires when `PLATFORM_ENV != &quot;dev&quot;`; the default value of `PLATFORM_ENV` is `&quot;dev&quot;`, so the check is silently bypassed in any deployment that does not explicitly o…

---

## 13. 🟡 High Severity — PraisonAI Platform: Missing role checks let any workspace member become owner and control workspace membership

**CVE:** `CVE-2026-47405` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-h37g-4h4p-9x97>

> ### Summary

PraisonAI Platform has a broken workspace authorization check that allows any authenticated low-privilege workspace member to escalate their own role to `owner`.

The issue is caused by privileged workspace-management routes using the shared dependency `require_workspace_member(...)` without requiring `admin` or `owner`. The dependency defaults to `min_role=&quot;member&quot;`, so rou…

---

## 14. 🟡 High Severity — PraisonAI Platform workspace-scoped routes allow cross-workspace object access by global object ID

**CVE:** `CVE-2026-47399` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-6h6v-6m7w-7vxx>

> ### Summary

PraisonAI Platform&#x27;s workspace-scoped REST routes contain a systemic object-level authorization flaw that allows an authenticated user from one workspace to access, modify, and delete objects belonging to another workspace by supplying the victim object&#x27;s global UUID.

The affected pattern appears in workspace-scoped routes such as agents, projects, issues, and comments. The…

---

## 15. 🟡 High Severity — PraisonAI Platform has a cross-workspace IDOR + member-role privilege escalation

**CVE:** `CVE-2026-47407` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-h8q5-cp56-rr65>

> ## Summary

The Platform server exposes resources under `/api/v1/workspaces/{workspace_id}/...` and protects them with a `require_workspace_member(workspace_id)` FastAPI dependency. The dependency only checks that the caller is a member of the workspace_id in the URL prefix. The route handlers then look up the inner resource (`agent_id`, `issue_id`, `project_id`, `label_id`, `comment_id`, `depende…

---

## 16. 🟡 High Severity — praisonai-platform: list_issue_activity returns activity log for any issue regardless of workspace ownership

**CVE:** `CVE-2026-47408` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-27p4-pjqv-whgj>

> ## Summary

**Type:** Insecure Direct Object Reference. The `GET /workspaces/{workspace_id}/issues/{issue_id}/activity` endpoint is gated by `require_workspace_member(workspace_id)` and dispatches to `ActivityService.list_for_issue(issue_id)`, which executes `SELECT * FROM activity WHERE issue_id = :issue_id` with no workspace constraint. A user who is a member of any workspace can read the full a…

---

## 17. 🟡 High Severity — PraisonAI has Cross-Workspace IDOR and Privilege Escalation via Platform API

**CVE:** `CVE-2026-48169` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-gv23-xrm3-8c62>

> ### Summary

The PraisonAI Platform API has two authorization failures that together break workspace isolation. The service layer for issues and projects performs global primary-key lookups without checking workspace ownership, so any authenticated user can read, modify, and delete resources in any workspace just by swapping UUIDs in their API requests. On top of that, every member management endp…

---

## 18. 🟡 High Severity — PraisonAI has an Arbitrary File Write in Python API

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

## 19. 🟡 High Severity — PraisonAI's unauthenticated A2A official example can reach real LLM-driven `eval()` tool execution

**CVE:** `CVE-2026-47391` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-vg22-4gmj-prxw>

> ## Summary

The first-party PraisonAI A2A server example combines three behaviors into a remotely exploitable Critical chain:

1. The example exposes an A2A server without configuring `auth_token`.
2. The same example binds the server to `0.0.0.0`.
3. The example registers a `calculate(expression)` tool implemented with Python `eval(expression)`.

An unauthenticated network client can send a JSON-…

---

## 20. 🟡 High Severity — PraisonAI vulnerable to unauthenticated arbitrary file read via MCP workflow.show, workflow.validate, deploy.validate

**CVE:** `CVE-2026-47394` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-9cr9-25q5-8prj>

> ## Summary

The fix for GHSA-9mqq-jqxf-grvw / CVE-2026-44336 is incomplete. The original advisory description named four vulnerable handlers in `mcp_server/adapters/cli_tools.py`:

&gt; &quot;registers four file-handling tools by default, `praisonai.rules.create`, `praisonai.rules.show`, `praisonai.rules.delete`, **and `praisonai.workflow.show`**. Each accepts a path or filename string from MCP `t…

---

## 21. 🟡 High Severity — PraisonAI vulnerable to sandbox escape via `print.__self__` builtins module leak in `execute_code` (subprocess mode)

**CVE:** `CVE-2026-47392` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-4mr5-g6f9-cfrh>

> ## Summary

`execute_code()` in `praisonaiagents/tools/python_tools.py` (v1.6.37, subprocess sandbox mode) can be fully bypassed using `print.__self__` to retrieve the real Python `builtins` module, from which `__import__` can be extracted via `vars()` and runtime string construction. This achieves arbitrary OS command execution on the host, completely defeating the sandbox.

This is a **novel byp…

---

## 22. 🟡 High Severity — PraisonAI CLI automatically resolves @url mentions in prompt text and can read loopback URLs into model context

**CVE:** `CVE-2026-47395` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-5cxw-77wg-jrf3>

> ### Summary

PraisonAI&#x27;s direct-prompt CLI automatically expands `@url:` mentions in raw prompt text before agent execution begins.

If a prompt contains `@url:&lt;http-or-https-url&gt;`, the CLI calls `MentionsParser.process(...)`. The `@url:` handler then performs a direct `urllib.request.urlopen()` request to the attacker-controlled URL and returns the response body. That response body is …

---

## 23. 🟡 High Severity — PraisonAI spider_tools SSRF protection bypass via alternate loopback host encodings

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

## 24. 🟡 High Severity — Nezha's authenticated DDNS webhook configuration allows blind SSRF from the dashboard host

**CVE:** `CVE-2026-47268` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-6x26-5727-rrm9>

> #### Summary

An authenticated Nezha dashboard user can create or update a DDNS profile with provider `webhook` and configure an arbitrary `webhook_url`, HTTP method, request body, and headers. When DDNS is triggered for a server that uses that profile, the dashboard process sends the configured request with `utils.HttpClient` without the SSRF protections used by notification webhooks.

This allow…

---

## 25. 🟡 High Severity — Admidio: CSRF in SSO client `enable` action toggles SAML/OIDC clients without token validation

**CVE:** `CVE-2026-47229` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-xg76-5qj2-2hhv>

> ## Summary

`modules/sso/clients.php` validates an `adm_csrf_token` on every state-changing branch except `enable`. The `enable` case loads the SAML or OIDC client by UUID, calls `$client-&gt;enable($enabled)`, and persists the new state with no token check. Because the action is reachable via plain GET parameters, a third-party page can trick an authenticated administrator into disabling (or sile…

---

## 26. 🟡 High Severity — BoxLite has a Timeout Bypass Vulnerability

**CVE:** `CVE-2026-47213` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-xjhv-pp2r-6f82>

> #### Summary

BoxLite is a sandbox service that allows users to create lightweight virtual machines (Boxes) and run OCI containers within them. BoxLite allows users to configure a timeout for services running inside the virtual machine. When the timeout is triggered, BoxLite sends a signal to kill the process. However, instead of using the uncatchable SIGKILL signal, BoxLite uses the catchable SIG…

---

## 27. 🟡 High Severity — Symfony: Twilio SMS Notifier allows unauthenticated webhook injection due to missing X-Twilio-Signature verification

**CVE:** `CVE-2026-47212` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-55rj-x2vc-4whq>

> ### Description

The Twilio SMS notifier bridge ships a webhook request parser used to authenticate and decode the status callbacks Twilio POSTs to an application&#x27;s webhook endpoint. Its `doParse(Request $request, #[\SensitiveParameter] string $secret)` method receives the configured webhook secret but never reads it; it decodes and returns the payload unconditionally, ignoring the `X-Twilio-…

---

## 28. 🟡 High Severity — ouroboros-ai Vulnerable to Remote Code Execution via Untrusted Project-Directory .env

**CVE:** `CVE-2026-47211` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-c4m7-2gwp-vw76>

> ### Impact
A Remote Code Execution (RCE) vulnerability was discovered in Ouroboros. If a user clones a malicious repository and runs Ouroboros commands within that directory, it can lead to arbitrary code execution and potential system takeover.

The vulnerability (CWE-426: Untrusted Search Path &amp; CWE-15: External Control of System Setting) stems from Ouroboros loading the `.env` file from the…

---

## 29. 🟡 High Severity — CC-Tweaked has an SSRF Protection Bypass with NAT64

**CVE:** `CVE-2026-47695` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-5jh9-2h63-pw4q>

> ### Summary

CC-Tweaked&#x27;s HTTP API (`http.request`, `http.websocket`) blocks requests to private network ranges to prevent server-side request forgery (SSRF). This protection can be bypassed on IPv6-capable servers using NAT64 well-known prefix addresses (`64:ff9b::/96`). An attacker who can execute Lua code can reach any internal IPv4 service that the filter is intended to block, by addressi…

---

## 30. 🟡 High Severity — Koel Vulnerable to SSRF via Podcast Episode Enclosure URLs

**CVE:** `CVE-2026-47260` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-7j2f-6h2r-6cqc>

> ## Summary

Koel validates the podcast feed URL via the `SafeUrl` rule (DNS resolution + public IP check), but the individual episode `&lt;enclosure url=&quot;...&quot;&gt;` values extracted from the RSS XML are stored directly into the database without any SSRF validation. When a user plays an episode, the server downloads the full HTTP response from the unvalidated enclosure URL via `Http::sink(…

---

## 31. 🟡 High Severity — Sparkle's AppInstaller post-stage-1 XPC listener accepts unvalidated connections, allowing spoofed appcast item data injection

**CVE:** `CVE-2026-47122` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-g3hp-f6mg-559v>

> ## Summary

AppInstaller post-stage-1 XPC listener accepts unvalidated connections, allowing spoofed appcast item data injection.

## Details

`Autoupdate/AppInstaller.m`&#x27;s `shouldAcceptNewConnection:` only enforces `SUCodeSigningVerifier validateConnection:` before stage 1 completes. After `_performedStage1Installation = YES`, new connections to the registered Mach service `&lt;bundleId&gt;-…

---

## 32. 🟡 High Severity — russh server userauth state is not reset when authentication principal changes

**CVE:** `CVE-2026-46705` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-hpv4-5h6f-wqr3>

> ### Summary
The `russh` server authentication path keeps internal userauth state across `SSH_MSG_USERAUTH_REQUEST` messages without separating that state when the request principal changes.

RFC 4252 allows the `user name` and `service name` fields to change between authentication requests. The issue is not that such changes are invalid. The issue is that russh-owned authentication state, such as …

---

## 33. 🟡 High Severity — Metasploit Wrap Up 05/29/2026

**CVE:** `CVE-2026-43284` | `CVE-2026-43500` | `CVE-2026-3055` | `CVE-2022-28368` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-05-29-2026>

> More Linux LPEs Hark the age of the Linux LPE has arrived. This week’s release follows up on recent work bringing new Linux LPEs to Metasploit users. Copy Fail seemed to have kicked off a trend of similar bugs and hot on its heels is Dirty Frag. Dirty Frag is actually two vulnerabilities in a trenchcoat, individually identified as CVE-2026-43284 and CVE-2026-43500. Each is exploitable individually…

---

## 34. 🟡 High Severity — amazon-redshift-python-driver vulnerable to Remote Code Execution via eval() Injection

**CVE:** `CVE-2026-8838` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-29h4-r29x-hchv>

> ### Summary
amazon-redshift-python-driver is the official Python connector for Amazon Redshift. In versions 2.1.13 and earlier, the driver insufficiently validates data received from the server during query result processing. A rogue server or man-in-the-middle could leverage this to execute arbitrary code on the client.

### Impact
When a client connects to a rogue server implementing the Postgre…

---

## 35. 🟡 High Severity — AgenticMail API/storage and outbound relay hardening fixes

**CVE:** `CVE-2026-47255` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-wjjv-3mj2-39hf>

> The current upstream main branch at commit 7e0206d was reviewed, and the fix-first patch set was rebased on 2026-05-18. The patches cover: validated and bound inactive-agent hour filtering; storage SQL identifier validation; metadata-backed ownership checks for raw storage SQL; blocking direct storage metadata access through raw SQL; fail-closed outbound worker secret handling; SMTP envelope/heade…

---

## 36. 🟡 High Severity — unbounded-spsc: Sender::send pointer-as-value transmute causes OOB read and fake-Arc drop under TX/RX race

**CVE:** `CVE-2026-46690` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-6m57-8r3p-pqx6>

> ## Summary

`Sender::send` in `src/lib.rs` contains an `unsafe` block in the `DISCONNECTED` arm that transmutes a **raw pointer** (`*mut Producer&lt;T&gt;`) into the bytes of a **value-level** `Consumer&lt;T&gt;`. The author&#x27;s intent, visible in the surrounding comment at lines 386-390, was a value transmute. The shipped code is one level of indirection off.

The resulting `Consumer&lt;T&gt;`…

---

## 37. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
