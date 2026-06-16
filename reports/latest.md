# Zero Day Pulse

> **Generated:** 2026-06-16 20:40 UTC &nbsp;|&nbsp; **Total:** 35 &nbsp;|&nbsp; 🔴 KEV: 1 &nbsp;|&nbsp; 🟠 Zero-Day: 13 &nbsp;|&nbsp; 🟡 High: 21 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🔴 CISA KEV — CVE-2026-48907 — Widget Factory Joomla Content Editor Improper Access Control Vulnerability

**CVE:** `CVE-2026-48907` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-48907>

> Vendor: Widget Factory | Product: Joomla Content Editor . Widget Factory Joomla Content Editor contains an improper access control vulnerability which could allow for upload and execution of PHP code via the creation of new editor profiles for unauthenticated users.  Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Se…

**Parallel AI Enrichment:**

- **Technical Details:** An unauthenticated AJAX endpoint in the JCE extension allows creation of new editor profiles; attackers can enable PHP uploads and upload malicious PHP to /tmp/, leading to remote code execution.
- **Affected Products:** Joomla Content Editor (JCE) extension for Joomla versions 1.0.0‑2.9.99.4
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H/E:A/AU:Y/U:Red
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Immediately update to 2.9.99.5; if patching not possible, disable or remove the JCE extension, block vulnerable AJAX endpoints, restrict file upload handling, and follow CISA BOD 26-04 and Forensics Triage guidance as noted.
- **Vendor Advisory:** https://www.joomlacontenteditor.net/

---

## 2. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated attackers can exploit a directory traversal flaw by sending crafted HTTP requests, enabling them to navigate the file system and read arbitrary files, including configuration files and hashed passwords.
- **Affected Products:** SimpleHelp remote support software version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** DragonForce ransomware
- **Mitigation:** Isolate the SimpleHelp server from the internet or stop the server process, continuously monitor inbound/outbound traffic, and upgrade to the latest patched version as soon as possible.
- **Vendor Advisory:** https://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an AI system retrieves external content (web pages, knowledge bases, or RAG documents) that contains maliciously crafted instructions or prompts; the model then incorporates those instructions into its internal context or agentic plan, causing unintended behavior or data exfiltration.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true — https://arxiv.org/abs/2601.07072
- **Patch Available:** false
- **Active Exploitation:** true — https://blog.google/security/prompt-injections-web/
- **Threat Actors:** None known
- **Mitigation:** Harden retrieval and ingestion (filter/whitelist sources, sanitize and provenance‑tag retrieved content), apply RAG and agent request constraints, enforce output/safety checks, sandbox agent actions, and monitor for anomalous prompts and retrievals.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when an attacker injects malicious instructions into data sources or tools (documents, search results, connectors, third‑party content) that an LLM ingests while completing a user’s query, causing the model or agentic automation to follow attacker‑controlled instructions — potentially without direct user input.
- **Affected Products:** Google Workspace with Gemini integrations (Gmail, Google Drive, Slides, Workspace Gemini/Gemini Enterprise); specific versions unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true — https://noma.security/noma-labs/geminijack/
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses: restrict and sanitize external data sources, apply content filtering and normalization, enforce least‑privilege access for connectors and agents, use guardrails and model‑level instruction filtering, monitoring and anomaly detection, and vendor‑provided hardening for Workspace with Gemini as per Google guidance.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection manipulates an AI agent via crafted web content to perform unintended actions. Chrome mitigates this with a user alignment critic, origin isolation, user confirmations, and real‑time threat detection. The Gemini CLI RCE flaw trusted workspace configuration in headless CI/CD runs, allowing malicious config to execute commands before sandboxing. Cursor’s CVE‑2025‑54131 bypasses an allow‑list in auto‑run mode using backticks or $(cmd) when combined with indirect prompt injection.
- **Affected Products:** Cursor versions below 1.3, @google/gemini-cli versions below 0.39.1 and 0.40.0-preview.3, google-github-actions/run-gemini-cli versions below 0.1.22
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Update Chrome to the latest version with built‑in agentic defenses, upgrade Cursor to version 1.3 or later, and upgrade @google/gemini-cli to 0.39.1 (or 0.40.0-preview.3) and google-github-actions/run-gemini-cli to 0.1.22 or newer. Apply the layered defense measures (user alignment critic, origin isolation, user confirmations) for agentic browsing.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow in the CrabbyAVIF Rust component (near‑miss) was discovered and fixed before release; Scudo hardened allocator rendered it non‑exploitable by placing guard pages around secondary allocations and converting silent corruption into noisy crashes.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — patch committed to CrabbyAVIF repository (https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050) and tracked in the Android security bulletin (https://source.android.com/docs/security/bulletin/2025-08-01).
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use of Scudo hardened allocator (guard pages) and improved crash reporting to detect overflows; training for unsafe Rust and stricter review of unsafe{} blocks. General mitigation: prefer Rust for new code and make Scudo mandatory where possible.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection embeds malicious instructions in external data sources (emails, files, calendar invites, URLs, images) which, when processed by agentic LLMs, can cause data exfiltration or unintended actions.
- **Affected Products:** Gemini (Gemini 2.5), Google Workspace (Gmail, Docs, Calendar), Gemini app — specific versions unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** false
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses: adversarial model training and hardening; deploy prompt‑injection content classifiers; apply security thought‑reinforcement in prompt handling; sanitize markdown and redact/flag suspicious external URLs and image rendering; require contextual user confirmations for risky actions; provide end‑user notifications and help resources; continuous red‑team testing and AI VRP engagement.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** APT actors exploit publicly known CVEs in edge/network devices (not zero‑days), create unauthorized admin accounts via CVE‑2023‑20198, execute commands via SNMP/SSH/web endpoints, modify ACLs, enable traffic mirroring/tunnels, run scripts in Guest Shell (TCL/Python) to persist and collect traffic, and pivot via trusted provider links.
- **Affected Products:** Cisco IOS, Cisco IOS XE, Cisco NX‑OS, Ivanti Connect Secure, Ivanti Policy, Fortinet firewalls, Juniper firewalls, Microsoft Exchange, Nokia routers and switches, Sierra Wireless devices, SonicWall
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching known exploited CVEs; disable unused protocols (Telnet/FTP/HTTP); enforce strong credentials and public‑key authentication for admin; monitor device configs/logs for unexpected ACLs, GRE/tunnels, SPAN/RSPAN/ERSPAN, virtual containers; verify firmware integrity and compare hashes.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Unit 26165 employed malware to gain initial access, establish persistence, and exfiltrate data from targeted logistics and technology organizations.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS), military unit 26165
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** CVE‑2026‑45586 is an elevation‑of‑privilege flaw in the Windows Collaborative Translation Framework (CTFMON). CVE‑2026‑50507 is a security‑feature bypass in Windows BitLocker. CVE‑2026‑44815 is a remote code execution vulnerability in the Windows DHCP Client Service that can be triggered via the DhcpGetOriginalSubnetMask API.
- **Affected Products:** Windows Collaborative Translation Framework (CTFMON), Windows BitLocker, Windows DHCP Client Service
- **CVSS Score:** 7.8, 6.8, 9.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** For the DHCP Client Service (CVE‑2026‑44815) administrators should audit and restrict applications that call the DhcpGetOriginalSubnetMask API. For the other two vulnerabilities, applying the Microsoft patches released on Patch Tuesday mitigates the issues.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45586, https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50507, https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-44815

---

## 11. 🟠 Zero-Day — Google Vertex AI SDK Flaw Let Attackers Hijack Model Uploads via Bucket Squatting

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://thehackernews.com/2026/06/google-vertex-ai-sdk-flaw-let-attackers.html>

> A flaw in the Google Cloud Vertex AI SDK for Python let an attacker with no access to a victim&#x27;s project hijack the victim&#x27;s machine learning model upload and run code inside Google&#x27;s serving infrastructure.

Palo Alto Networks Unit 42, which found and reported the bug through Google&#x27;s bug bounty program, calls the technique &quot;Pickle in the Middle&quot; and said it saw no e…

---

## 12. 🟠 Zero-Day — LangChain: Path traversal and sandbox escape in LangChain file-search middleware and loaders

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-gr75-jv2w-4656>

> ## Summary

Several LangChain components that resolve filesystem paths or expand search patterns do not consistently confine the *resolved* path to the intended root directory. Affected behaviors include: a file-search agent middleware that validates a starting directory but not the search pattern or the resolved target of matched files, so glob patterns and symlinks can reach files outside the co…

---

## 13. 🟠 Zero-Day — Fake Microsoft Alerts Used to Deploy North Korean NarwhalRAT Malware

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://thehackernews.com/2026/06/fake-microsoft-alerts-used-to-deploy.html>

> The North Korean state-sponsored hacking group known as ScarCruft (aka APT37) has been observed using spear-phishing messages impersonating Microsoft Account security notifications to deliver malware called NarwhalRAT.

&quot;The attack email contained a message impersonating an MS account security alert,&quot; the Genians Security Center (GSC) said. &quot;It was designed to create concern over po…

---

## 14. 🟠 Zero-Day — Cisco Releases Security Updates for Actively Exploited SD-WAN Manager Flaw

**CVE:** `CVE-2026-20262` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://thehackernews.com/2026/06/cisco-releases-security-updates-for.html>

> Cisco has released security updates for a medium-severity security flaw in Catalyst SD-WAN Manager that has come under active exploitation in the wild.

The vulnerability, tracked as CVE-2026-20262, carries a CVSS score of 6.5 out of 10.0.

&quot;A vulnerability in the web UI of Cisco Catalyst SD-WAN Manager, formerly SD-WAN vManage, could allow an authenticated, remote attacker to create a file o…

---

## 15. 🟡 High Severity — LobeHub: Unauthenticated SSRF in `/webapi/proxy`

**CVE:** `CVE-2026-54157` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-xmwj-c75x-6346>

> ## Unauthenticated SSRF in /webapi/proxy allows anyone to proxy requests and inject cookies on lobehub.com

## Summary

The `/webapi/proxy` endpoint on app.lobehub.com accepts a URL in the POST body and fetches it server-side without any authentication. This is the same proxy code that was vulnerable in CVE-2024-32964, where `/api/proxy` was fixed by adding auth middleware. The `/webapi/proxy` rou…

---

## 16. 🟡 High Severity — Crawl4AI: AST Sandbox Escape via gi_frame.f_back Chain - Pre-Auth RCE in Docker API

**CVE:** `CVE-2026-53753` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-qxjp-w3pj-48m7>

> ### Summary

The `_safe_eval_expression()` function in the computed fields feature uses an AST validator that only blocks attributes starting with underscore. Python generator and frame object attributes (`gi_frame`, `f_back`, `f_builtins`) do NOT start with underscore, enabling a complete sandbox escape to achieve arbitrary code execution.

The attack requires no authentication (JWT disabled by d…

---

## 17. 🟡 High Severity — Deno: Permission Bypass via Unicode Normalization Mismatch on macOS (APFS)

**CVE:** `CVE-2026-49401` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-8xpq-cjcf-3wh9>

> ## Summary

Deno&#x27;s permission system enforces filesystem and execution restrictions by
comparing the requested path against the path supplied to `--deny-read`,
`--deny-write`, `--deny-run`, or `--deny-ffi`. On macOS, that comparison was
done at the raw-byte level while the APFS filesystem treats different Unicode
spellings of the same name as the same file.

That means a program could reach a…

---

## 18. 🟡 High Severity — Deno: BYONM module resolution allows `package.json` main path traversal to bypass `--allow-read` restrictions

**CVE:** `CVE-2026-49406` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-968w-xfqw-vp9q>

> ## Summary

When Deno was run in BYONM mode (`nodeModulesDir: &quot;manual&quot;`), the module resolver did not validate that a package&#x27;s resolved entrypoint stayed within its `node_modules/&lt;pkg&gt;/` directory. A malicious `package.json` whose `main` field contained `..` segments was able to resolve to an arbitrary path on disk, and the resolver then read that file without consulting the …

---

## 19. 🟡 High Severity — n8n: Merge Node SQL Mode Prototype Pollution

**CVE:** `CVE-2026-54311` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-9c38-2mcm-q7f7>

> ## Impact
An authenticated user with permission to create or modify workflows could pollute the sandbox used by the Merge node&#x27;s SQL Query mode. Because the sandbox context was cached and reused across all workflow executions on the instance, prototype mutations introduced by one user&#x27;s workflow persist into subsequent Merge SQL executions belonging to other users or projects. This allow…

---

## 20. 🟡 High Severity — Langflow: Unauthenticated RCE in Shareable Playgrounds

**CVE:** `CVE-2026-48519` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-v5ff-9q35-q26f>

> ### Summary
The &quot;Shareable Playground&quot; (or &quot;Public Flows&quot; in code) contains a critical RCE vulnerability.
Simply sharing a flow exposes the deployment to RCE risk by authenticated users.

Tested on commit 2d67402b1dbaefcbce85a244d4a6cd5e4bda1cfe

### Details
Shareable Playground feature works by enabling the execution of workflows by unauthenticated users, by accessing a link.
…

---

## 21. 🟡 High Severity — Astro: XSS via Unescaped Attribute Names in Spread Props

**CVE:** `CVE-2026-54298` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-jrpj-wcv7-9fh9>

> ## Summary

The `spreadAttributes` function in Astro&#x27;s server-side rendering pipeline iterates over object keys and passes them directly to `addAttribute`, which interpolates the key into the HTML output without escaping. When a developer uses the spread syntax `{...props}` on an HTML element and the object keys come from an untrusted source (API, CMS, URL parameters), an attacker can inject …

---

## 22. 🟡 High Severity — Astro: Host header SSRF in prerendered error page fetch

**CVE:** `CVE-2026-54299` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-2pvr-wf23-7pc7>

> ## Summary

Astro SSR apps with prerendered error pages (`/404` or `/500` using `export const prerender = true`) fetch those pages over HTTP at runtime when an error occurs. The URL for this fetch is derived from `request.url`, which in turn gets its origin from the incoming `Host` header. When the `Host` header is not validated against `allowedDomains`, an attacker can point the fetch at an arbit…

---

## 23. 🟡 High Severity — hono: Body Limit Middleware can be bypassed on AWS Lambda by understating `Content-Length`

**CVE:** `CVE-2026-54288` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-rv63-4mwf-qqc2>

> ### Summary

The Body Limit Middleware trusts the request&#x27;s `Content-Length` header to decide whether a body is within the limit. On AWS Lambda (API Gateway v1/v2, ALB, VPC Lattice, and Lambda@Edge) the body is delivered fully buffered and the adapter builds the request with the client-declared `Content-Length`, which need not match the actual payload. A client can declare a tiny `Content-Len…

---

## 24. 🟡 High Severity — hono: Lambda@Edge adapter keeps only the last value of a repeated request header, dropping the rest

**CVE:** `CVE-2026-54289` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-wgpf-jwqj-8h8p>

> ### Summary

On AWS Lambda@Edge, CloudFront delivers a request header that appears more than once as several separate entries. The adapter writes each value with `Headers.set` instead of `Headers.append`, so every value overwrites the previous one and only the last reaches the application. Repeated request headers such as `X-Forwarded-For`, `Forwarded`, and `Via` are silently truncated to a single…

---

## 25. 🟡 High Severity — hono: Path traversal in `serve-static` on Windows via encoded backslash (`%5C`)

**CVE:** `CVE-2026-54286` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-wwfh-h76j-fc44>

> ### Summary

On Windows hosts, an encoded backslash (`%5C`) in the request path decodes to `\`, which the Windows path resolver treats as a separator. `serve-static` then resolves a single URL segment such as `admin\secret.txt` into a nested file under the root and serves it, letting an attacker read static files meant to be protected behind prefix-mounted middleware. Directory escape (`..`) remai…

---

## 26. 🟡 High Severity — hono: AWS Lambda adapter merges multiple `Set-Cookie` headers into one value, dropping cookies on ALB single-header and Lattice

**CVE:** `CVE-2026-54287` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-j6c9-x7qj-28xf>

> ### Summary

On AWS Lambda, the ALB single-header response and the VPC Lattice v2 response join multiple `Set-Cookie` headers into one comma-separated value. Because commas also appear inside cookie attributes (for example `Expires` dates), clients cannot split the value back into individual cookies and silently drop or misparse them.

### Details

Per RFC 6265, each cookie must be its own `Set-Co…

---

## 27. 🟡 High Severity — Attackers Exploit Three Fortinet FortiSandbox Flaws, One Patched Last Week

**CVE:** `CVE-2026-39813` | `CVE-2026-39808` | `CVE-2026-25089` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://thehackernews.com/2026/06/attackers-exploit-three-fortinet.html>

> Bad actors are exploiting multiple security vulnerabilities in Fortinet FortiSandbox, according to threat intelligence firm Defused Cyber.

In a post shared on X, the company said it has observed exploitation of CVE-2026-39813, CVE-2026-39808, and CVE-2026-25089 over the past 24 hours.

CVE-2026-39813 (CVSS score: 9.1) refers to a path traversal vulnerability in FortiSandbox JRPC API that could

---

## 28. 🟡 High Severity — SEC Consult SA-20260610-0 :: Local Privilege Escalation in Slate Digital Connect (macOS)

**CVE:** `CVE-2026-24066` | `CVE-2026-24067` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://seclists.org/fulldisclosure/2026/Jun/7>

> Posted by SEC Consult Vulnerability Lab via Fulldisclosure on Jun 15 SEC Consult Vulnerability Lab Security Advisory &lt; 20260610-0 &gt; ======================================================================= title: Local Privilege Escalation product: Slate Digital Connect (macOS) vulnerable version: 1.37.0 fixed version: - CVE number: CVE-2026-24066, CVE-2026-24067 impact: high homepage:...

---

## 29. 🟡 High Severity — SEC Consult SA-20260609-0 :: Multiple Local Privilege Escalation Vulnerabilities in Waves Audio - Waves Central

**CVE:** `CVE-2026-24064` | `CVE-2026-24065` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://seclists.org/fulldisclosure/2026/Jun/6>

> Posted by SEC Consult Vulnerability Lab via Fulldisclosure on Jun 15 SEC Consult Vulnerability Lab Security Advisory &lt; 20260609-0 &gt; ======================================================================= title: Multiple Local Privilege Escalation Vulnerabilities product: Waves Audio - Waves Central vulnerable version: v13.0.8 - v16.6.0 fixed version: v16.6.2 CVE number: CVE-2026-24064, CVE-2…

---

## 30. 🟡 High Severity — CISA Flags LiteSpeed cPanel Plugin Flaw Exploited for Root Privilege Escalation

**CVE:** `CVE-2026-54420` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://thehackernews.com/2026/06/cisa-flags-litespeed-cpanel-plugin-flaw.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has added a security flaw impacting LiteSpeed cPanel Plugin to its Known Exploited Vulnerabilities (KEV) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the fixes by June 18, 2026.

The vulnerability in question is CVE-2026-54420 (CVSS score: 8.5), which has been described as a case of privilege

---

## 31. 🟡 High Severity — aws-cdk-lib: OS Command Injection in NodejsFunction Bundling

**CVE:** `CVE-2026-11417` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-999r-qq7v-r334>

> ### Summary
AWS CDK (`aws-cdk-lib`) is an open-source framework for defining cloud infrastructure in code and provisioning it through AWS CloudFormation. OS command injection in the `NodejsFunction` local bundling pipeline in `aws-cdk-lib` before 2.245.0 (2.246.0 on Windows) might allow a threat actor who controls the value of one or more bundling properties (`externalModules`, `define`, `loader`,…

---

## 32. 🟡 High Severity — Netty: QUIC stateless reset token material exposed through header-visible connection IDs

**CVE:** `CVE-2026-50009` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-cq4q-cv5g-r8q5>

> ### Summary
Netty QUIC exposes the stateless reset token on the network path when using the default HMAC-based connection-ID and stateless-reset-token generators. The reset token for the server&#x27;s current source connection ID can be derived from bytes that appear as the connection ID in QUIC headers after a source-CID rotation. An on-path attacker observing the headers can use the token to per…

---

## 33. 🟡 High Severity — Netty HTTP/3 QPACK Blocked Streams Memory Exhaustion

**CVE:** `CVE-2026-48748` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-4grm-h2qv-h6w6>

> ### Summary
A memory exhaustion vulnerability in the Netty HTTP/3 codec allows the creation of an infinite number of blocked streams, which can cause OOM error.

### Details
The vulnerability exists in `io.netty.handler.codec.http3.QpackDecoder#shouldWaitForDynamicTableUpdates`:

If a client sends a header referencing a table entry that the server hasn&#x27;t received yet, the server must pause th…

---

## 34. 🟡 High Severity — Starlette: Unvalidated request path concatenated into authority poisons request.url.hostname

**CVE:** `CVE-2026-54282` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-jp82-jpqv-5vv3>

> ### Summary

In affected versions, the HTTP request path is not validated before being used to reconstruct `request.url`. Because `request.url` is rebuilt by concatenating `{scheme}://{host}{path}` and re-parsing the result, a path that does not begin with `/` (for example `@google.com`) moves the authority boundary during re-parsing, so `request.url.hostname` and `request.url.netloc` become attac…

---

## 35. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
