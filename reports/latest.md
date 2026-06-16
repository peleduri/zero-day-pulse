# Zero Day Pulse

> **Generated:** 2026-06-16 16:21 UTC &nbsp;|&nbsp; **Total:** 38 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 26 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a directory traversal vulnerability in SimpleHelp RMM that enables unauthenticated attackers to read arbitrary files by manipulating file paths.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or exploit publicly available.
- **Patch Available:** Patch released; see SimpleHelp blog for details.
- **Active Exploitation:** Confirmed active exploitation reported by ransomware actors leveraging unpatched SimpleHelp RMM.
- **Threat Actors:** Ransomware actors (unspecified)
- **Mitigation:** Apply the vendor-supplied patch (upgrade SimpleHelp to a version newer than 5.5.7) and restrict RMM access to trusted networks.
- **Vendor Advisory:** https://www.broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an attack where adversarial content in external corpora retrieved by LLM systems (e.g., via retrieval‑augmented generation or agentic systems) contains malicious instructions that influence model behavior. Researchers demonstrated end‑to‑end IPI exploits under natural queries and realistic external corpora, including zero‑click payloads such as GeminiJack.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoCs are available at http://arxiv.org/abs/2601.07072, http://arxiv.org/pdf/2601.07072, http://infosecurity-magazine.com/news/researchers-10-wild-indirect, and http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability.
- **Patch Available:** Patch unavailable.
- **Active Exploitation:** Confirmed active exploitation reported: GeminiJack zero‑click IPI against Google Gemini Enterprise (noma.security) and end‑to‑end IPI exploits demonstrated in the wild (arXiv). Additional web‑sweep findings are described in the Google Security Blog and Infosecurity Magazine articles.
- **Threat Actors:** None known
- **Mitigation:** Vendor monitoring and web sweeps for IPI patterns, hardening retrieval pipelines, content filtering/validation of retrieved documents, privileged prompt separation, and applying vendor advisories where available.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Attackers plant malicious instructions in shared Workspace artifacts (Docs, Calendar, Gmail). RAG retrieves this poisoned content into Gemini’s context, causing the model to execute the hidden instructions and exfiltrate data (e.g., via an external image request).
- **Affected Products:** Google Gemini Enterprise, Vertex AI Search (VAIS)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC details published by Noma Labs; no widely weaponized exploit reported.
- **Patch Available:** Google deployed updates and architectural changes separating Vertex AI Search from Gemini Enterprise. See advisory and Noma Labs report.
- **Active Exploitation:** No confirmed wide‑scale active exploitation reported; only a demonstration PoC by Noma Labs.
- **Threat Actors:** None known
- **Mitigation:** Deterministic defenses (user confirmation, URL sanitization, tool‑chaining policies), ML‑ and LLM‑based defense retraining, synthetic‑data augmentation, separation of VAIS from Gemini Enterprise, and configuration of datasource access.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection allows a malicious site to craft content that is fed as a prompt to the agentic AI, potentially causing unintended actions or data exfiltration.
- **Affected Products:** Chrome (agentic/Gemini for Chrome features)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit or PoC is known.
- **Patch Available:** Patch is delivered via Chrome updates; see the vendor advisory for details.
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Deploy Chrome’s latest version which includes a second AI watchdog, origin access restrictions, and built‑in prompt‑injection blocking. Follow Google’s guidance on configuring these defenses.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** The post explains that moving new code to memory‑safe Rust reduces memory‑safety vulnerability density, achieving a >1000× reduction and bringing memory‑safety vulnerabilities to under 20% of total vulnerabilities in 2025 across C, C++, Java, Kotlin, and Rust components.
- **Affected Products:** AOSP/Android platform (first‑party and third‑party open‑source components across C, C++, Java, Kotlin, and Rust)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** None known; no public PoC or weaponized exploit referenced in the blog post or related advisories.
- **Patch Available:** Not applicable to the blog's topic (engineering/process update). For Android security fixes refer to the Android security bulletins and AOSP patches: https://source.android.com/docs/security/bulletin/2026/2026-06-01
- **Active Exploitation:** None reported in the blog post; prior advisories about Android zero‑days (e.g., CVE-2025-48595) are separate and reported as actively exploited in June 2026 (see Android security bulletin).
- **Threat Actors:** None known
- **Mitigation:** Continue migrating new components to Rust, prioritize memory‑safe languages for new code, and apply vendor security patch levels (2026-06-05 or later) for platform vulnerabilities.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2026/2026-06-01

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection involves hidden malicious instructions embedded in external data sources (emails, documents, calendar invites) that may instruct AI to exfiltrate data or perform rogue actions. Google's mitigations include model adversarial training, content classifiers that detect and filter malicious instructions, a security‑reinforcing reasoning step, sanitization/redaction of external resources (images/URLs), and requiring explicit user confirmation for risky actions.
- **Affected Products:** Gemini (Gemini app and Gemini in Google Workspace), Gemini 2.5
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit unavailable.
- **Patch Available:** Vendor describes defenses, mitigations, and model hardening rather than a discrete patch; official vendor advisory URL above.
- **Active Exploitation:** No active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses — prompt injection content classifiers; security thought reinforcement; markdown sanitization and suspicious URL redaction; user confirmation framework; end‑user security mitigation notifications; adversarial training and model hardening (Gemini 2.5); use of Google Safe Browsing for suspicious URLs; manual and automated red‑teaming; AI VRP collaboration.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** APT actors exploit known CVEs in internet‑exposed edge/network devices (e.g., CVE‑2023‑20198 auth bypass, CVE‑2023‑20273 post‑auth command injection, CVE‑2018‑0171 Smart Install RCE, CVE‑2024‑21887 Ivanti) to create persistent access, modify router configs, enable tunnels (GRE/MPLS), run scripts/containers (Guest Shell), mirror traffic (SPAN/RSPAN/ERSPAN), create privileged accounts, and exfiltrate data.
- **Affected Products:** Cisco IOS, Cisco IOS XE, Cisco NX‑OS, Ivanti Connect Secure/Policy, Fortinet firewalls, Juniper firewalls, Microsoft Exchange, Nokia routers/switches, Sierra Wireless devices, SonicWall
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public exploit/tooling referenced (e.g., siet.py, map.tcl, tclproxy.tcl, wodSSHServer) and example Snort detection for CVE-2023-20198; PoC/weaponized exploits have been observed in industry reporting.
- **Patch Available:** No single vendor patch; vendors listed with vendor‑specific advisories (e.g., Cisco mitigations/patches for CVE-2023-20198/CVE-2023-20273, Ivanti advisories for CVE-2024-21887). See vendor resources (Cisco Software Checker, vendor hardening guides) in CISA advisory.
- **Active Exploitation:** Yes—CISA reports these APT actors are actively exploiting known CVEs and have compromised telecommunications, government, transportation, lodging, and military infrastructure globally; multiple CVEs are listed as historically exploited.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching known exploited CVEs; disable unused ports/protocols; enforce strong credential and key‑based authentication; disable Guest Shell if not required; monitor firmware/software integrity (hash checks); monitor logs, network mirroring, and management interfaces; follow vendor hardening guides; isolate/segment management networks; disable outbound connections from management interfaces.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable (advisory describes campaign targeting logistics and IT companies but does not define a single CVE‑level vulnerability mechanism).
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit referenced in advisory; exploit availability unknown.
- **Patch Available:** Patch unavailable (no vendor patch referenced in advisory).
- **Active Exploitation:** Confirmed targeting and active campaign against Western logistics entities and technology companies since 2022; sources: CISA AA25-141A, FBI CSA, Australian advisory, DoD PDF.
- **Threat Actors:** GRU 85th Main Special Service Center (85th GTsSS), military unit 26165 (tracked as APT28 and related GRU actors).
- **Mitigation:** General mitigations and hardening recommended by the advisory (network segmentation, multifactor authentication, monitoring for indicators of compromise, patching systems).
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-45586: Elevation of privilege via link‑following (CWE‑59) in Windows Collaborative Translation Framework, allowing a low‑privileged local attacker to gain higher rights without user interaction. CVE-2026-50507: Security feature bypass in Windows BitLocker with public proof‑of‑concept code. CVE-2026-44815: Remote code execution in the Windows DHCP Client Service; a rogue DHCP server can send crafted responses that trigger code execution when DhcpGetOriginalSubnetMask is called. CVE-2026-45648: Out‑of‑bounds write in Windows Active Directory Domain Services via crafted inputs to the NSPI RPC interface, leading to memory corruption and RCE. CVE-2026-45456, CVE-2026-45458, CVE-2026-47635: Critical RCE vulnerabilities in Microsoft Outlook and Word where malicious content rendered in the Preview Pane leads to code execution.
- **Affected Products:** Windows Collaborative Translation Framework (CTFMON), Windows BitLocker, Windows DHCP Client Service, Windows Active Directory Domain Services, Microsoft Outlook, Microsoft Word
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** A proof‑of‑concept exploit is publicly available for the BitLocker vulnerability (CVE-2026-50507); no public exploits are reported for the other vulnerabilities.
- **Patch Available:** Patches are available via Microsoft’s June 2026 Patch Tuesday release; specific advisory URLs are not provided in the source.
- **Active Exploitation:** No confirmed active exploitation in the wild has been reported for any of the listed vulnerabilities.
- **Threat Actors:** None known
- **Mitigation:** Apply the Microsoft patches released on June 2026. For the DHCP Client Service (CVE-2026-44815), audit and, where possible, restrict applications that call the DhcpGetOriginalSubnetMask API as a pre‑patch mitigation.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 10. 🟠 Zero-Day — LangChain: Path traversal and sandbox escape in LangChain file-search middleware and loaders

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-gr75-jv2w-4656>

> ## Summary

Several LangChain components that resolve filesystem paths or expand search patterns do not consistently confine the *resolved* path to the intended root directory. Affected behaviors include: a file-search agent middleware that validates a starting directory but not the search pattern or the resolved target of matched files, so glob patterns and symlinks can reach files outside the co…

**Parallel AI Enrichment:**

- **Technical Details:** Components that resolve filesystem paths or expand search patterns (file‑search middleware, configuration loaders, and path‑prefix checks) do not canonicalize symlinks or enforce path‑segment boundaries, permitting glob patterns or symlink traversal to reach files outside the configured root directory (path traversal / link‑following).
- **Affected Products:** langchain <= 1.3.8, langchain-anthropic <= 1.4.5
- **CVSS Score:** 5.1
- **CVSS Vector:** CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** No public PoC; no evidence of in‑the‑wild exploitation.
- **Patch Available:** Yes — patched in langchain v1.3.9 and langchain-anthropic v1.4.6.
- **Active Exploitation:** No evidence of active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Upgrade to patched versions (langchain v1.3.9 / langchain-anthropic v1.4.6). If a patch cannot be applied, confine filesystem‑backed agents to dedicated directories, sandbox/containerize them, validate and canonicalize untrusted path inputs, avoid enabling dangerous loading for untrusted configuration, and enforce path‑segment boundaries when using prefix checks.
- **Vendor Advisory:** https://github.com/langchain-ai/langchain/security/advisories/GHSA-gr75-jv2w-4656

---

## 11. 🟠 Zero-Day — Fake Microsoft Alerts Used to Deploy North Korean NarwhalRAT Malware

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://thehackernews.com/2026/06/fake-microsoft-alerts-used-to-deploy.html>

> The North Korean state-sponsored hacking group known as ScarCruft (aka APT37) has been observed using spear-phishing messages impersonating Microsoft Account security notifications to deliver malware called NarwhalRAT.

&quot;The attack email contained a message impersonating an MS account security alert,&quot; the Genians Security Center (GSC) said. &quot;It was designed to create concern over po…

---

## 12. 🟠 Zero-Day — Cisco Releases Security Updates for Actively Exploited SD-WAN Manager Flaw

**CVE:** `CVE-2026-20262` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://thehackernews.com/2026/06/cisco-releases-security-updates-for.html>

> Cisco has released security updates for a medium-severity security flaw in Catalyst SD-WAN Manager that has come under active exploitation in the wild.

The vulnerability, tracked as CVE-2026-20262, carries a CVSS score of 6.5 out of 10.0.

&quot;A vulnerability in the web UI of Cisco Catalyst SD-WAN Manager, formerly SD-WAN vManage, could allow an authenticated, remote attacker to create a file o…

---

## 13. 🟡 High Severity — Astro: XSS via Unescaped Attribute Names in Spread Props

**CVE:** `CVE-2026-54298` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-jrpj-wcv7-9fh9>

> ## Summary

The `spreadAttributes` function in Astro&#x27;s server-side rendering pipeline iterates over object keys and passes them directly to `addAttribute`, which interpolates the key into the HTML output without escaping. When a developer uses the spread syntax `{...props}` on an HTML element and the object keys come from an untrusted source (API, CMS, URL parameters), an attacker can inject …

---

## 14. 🟡 High Severity — Astro: Host header SSRF in prerendered error page fetch

**CVE:** `CVE-2026-54299` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-2pvr-wf23-7pc7>

> ## Summary

Astro SSR apps with prerendered error pages (`/404` or `/500` using `export const prerender = true`) fetch those pages over HTTP at runtime when an error occurs. The URL for this fetch is derived from `request.url`, which in turn gets its origin from the incoming `Host` header. When the `Host` header is not validated against `allowedDomains`, an attacker can point the fetch at an arbit…

---

## 15. 🟡 High Severity — hono: Body Limit Middleware can be bypassed on AWS Lambda by understating `Content-Length`

**CVE:** `CVE-2026-54288` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-rv63-4mwf-qqc2>

> ### Summary

The Body Limit Middleware trusts the request&#x27;s `Content-Length` header to decide whether a body is within the limit. On AWS Lambda (API Gateway v1/v2, ALB, VPC Lattice, and Lambda@Edge) the body is delivered fully buffered and the adapter builds the request with the client-declared `Content-Length`, which need not match the actual payload. A client can declare a tiny `Content-Len…

---

## 16. 🟡 High Severity — hono: Lambda@Edge adapter keeps only the last value of a repeated request header, dropping the rest

**CVE:** `CVE-2026-54289` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-wgpf-jwqj-8h8p>

> ### Summary

On AWS Lambda@Edge, CloudFront delivers a request header that appears more than once as several separate entries. The adapter writes each value with `Headers.set` instead of `Headers.append`, so every value overwrites the previous one and only the last reaches the application. Repeated request headers such as `X-Forwarded-For`, `Forwarded`, and `Via` are silently truncated to a single…

---

## 17. 🟡 High Severity — hono: Path traversal in `serve-static` on Windows via encoded backslash (`%5C`)

**CVE:** `CVE-2026-54286` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-wwfh-h76j-fc44>

> ### Summary

On Windows hosts, an encoded backslash (`%5C`) in the request path decodes to `\`, which the Windows path resolver treats as a separator. `serve-static` then resolves a single URL segment such as `admin\secret.txt` into a nested file under the root and serves it, letting an attacker read static files meant to be protected behind prefix-mounted middleware. Directory escape (`..`) remai…

---

## 18. 🟡 High Severity — hono: AWS Lambda adapter merges multiple `Set-Cookie` headers into one value, dropping cookies on ALB single-header and Lattice

**CVE:** `CVE-2026-54287` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-j6c9-x7qj-28xf>

> ### Summary

On AWS Lambda, the ALB single-header response and the VPC Lattice v2 response join multiple `Set-Cookie` headers into one comma-separated value. Because commas also appear inside cookie attributes (for example `Expires` dates), clients cannot split the value back into individual cookies and silently drop or misparse them.

### Details

Per RFC 6265, each cookie must be its own `Set-Co…

---

## 19. 🟡 High Severity — Attackers Exploit Three Fortinet FortiSandbox Flaws, One Patched Last Week

**CVE:** `CVE-2026-39813` | `CVE-2026-39808` | `CVE-2026-25089` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://thehackernews.com/2026/06/attackers-exploit-three-fortinet.html>

> Bad actors are exploiting multiple security vulnerabilities in Fortinet FortiSandbox, according to threat intelligence firm Defused Cyber.

In a post shared on X, the company said it has observed exploitation of CVE-2026-39813, CVE-2026-39808, and CVE-2026-25089 over the past 24 hours.

CVE-2026-39813 (CVSS score: 9.1) refers to a path traversal vulnerability in FortiSandbox JRPC API that could

---

## 20. 🟡 High Severity — SEC Consult SA-20260610-0 :: Local Privilege Escalation in Slate Digital Connect (macOS)

**CVE:** `CVE-2026-24066` | `CVE-2026-24067` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://seclists.org/fulldisclosure/2026/Jun/7>

> Posted by SEC Consult Vulnerability Lab via Fulldisclosure on Jun 15 SEC Consult Vulnerability Lab Security Advisory &lt; 20260610-0 &gt; ======================================================================= title: Local Privilege Escalation product: Slate Digital Connect (macOS) vulnerable version: 1.37.0 fixed version: - CVE number: CVE-2026-24066, CVE-2026-24067 impact: high homepage:...

---

## 21. 🟡 High Severity — SEC Consult SA-20260609-0 :: Multiple Local Privilege Escalation Vulnerabilities in Waves Audio - Waves Central

**CVE:** `CVE-2026-24064` | `CVE-2026-24065` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://seclists.org/fulldisclosure/2026/Jun/6>

> Posted by SEC Consult Vulnerability Lab via Fulldisclosure on Jun 15 SEC Consult Vulnerability Lab Security Advisory &lt; 20260609-0 &gt; ======================================================================= title: Multiple Local Privilege Escalation Vulnerabilities product: Waves Audio - Waves Central vulnerable version: v13.0.8 - v16.6.0 fixed version: v16.6.2 CVE number: CVE-2026-24064, CVE-2…

---

## 22. 🟡 High Severity — CISA Flags LiteSpeed cPanel Plugin Flaw Exploited for Root Privilege Escalation

**CVE:** `CVE-2026-54420` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://thehackernews.com/2026/06/cisa-flags-litespeed-cpanel-plugin-flaw.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has added a security flaw impacting LiteSpeed cPanel Plugin to its Known Exploited Vulnerabilities (KEV) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the fixes by June 18, 2026.

The vulnerability in question is CVE-2026-54420 (CVSS score: 8.5), which has been described as a case of privilege

---

## 23. 🟡 High Severity — aws-cdk-lib: OS Command Injection in NodejsFunction Bundling

**CVE:** `CVE-2026-11417` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-999r-qq7v-r334>

> ### Summary
AWS CDK (`aws-cdk-lib`) is an open-source framework for defining cloud infrastructure in code and provisioning it through AWS CloudFormation. OS command injection in the `NodejsFunction` local bundling pipeline in `aws-cdk-lib` before 2.245.0 (2.246.0 on Windows) might allow a threat actor who controls the value of one or more bundling properties (`externalModules`, `define`, `loader`,…

---

## 24. 🟡 High Severity — Netty: QUIC stateless reset token material exposed through header-visible connection IDs

**CVE:** `CVE-2026-50009` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-cq4q-cv5g-r8q5>

> ### Summary
Netty QUIC exposes the stateless reset token on the network path when using the default HMAC-based connection-ID and stateless-reset-token generators. The reset token for the server&#x27;s current source connection ID can be derived from bytes that appear as the connection ID in QUIC headers after a source-CID rotation. An on-path attacker observing the headers can use the token to per…

---

## 25. 🟡 High Severity — Netty HTTP/3 QPACK Blocked Streams Memory Exhaustion

**CVE:** `CVE-2026-48748` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-4grm-h2qv-h6w6>

> ### Summary
A memory exhaustion vulnerability in the Netty HTTP/3 codec allows the creation of an infinite number of blocked streams, which can cause OOM error.

### Details
The vulnerability exists in `io.netty.handler.codec.http3.QpackDecoder#shouldWaitForDynamicTableUpdates`:

If a client sends a header referencing a table entry that the server hasn&#x27;t received yet, the server must pause th…

---

## 26. 🟡 High Severity — Starlette: Unvalidated request path concatenated into authority poisons request.url.hostname

**CVE:** `CVE-2026-54282` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-jp82-jpqv-5vv3>

> ### Summary

In affected versions, the HTTP request path is not validated before being used to reconstruct `request.url`. Because `request.url` is rebuilt by concatenating `{scheme}://{host}{path}` and re-parsing the result, a path that does not begin with `/` (for example `@google.com`) moves the authority boundary during re-parsing, so `request.url.hostname` and `request.url.netloc` become attac…

---

## 27. 🟡 High Severity — python-multipart: Semicolon treated as querystring field separator enables parameter smuggling

**CVE:** `CVE-2026-53538` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-6jv3-5f52-599m>

> ### Summary

`QuerystringParser` treated `;` as a field separator in `application/x-www-form-urlencoded` bodies, in addition to `&amp;`. The [WHATWG URL standard](https://url.spec.whatwg.org/#urlencoded-parsing), modern browsers, and Python&#x27;s `urllib.parse` (since the CVE-2021-23336 fix) treat only `&amp;` as a separator. This creates a parser differential: the same bytes are tokenized into d…

---

## 28. 🟡 High Severity — Tornado: Authorization header forwarded across cross-origin redirects in SimpleAsyncHTTPClient

**CVE:** `CVE-2026-49853` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-3x9g-8vmp-wqvf>

> ## Summary

When SimpleAsyncHTTPClient follows a 3xx redirect, it shallow-copies the original HTTPRequest, rewrites the URL, decrements max_redirects, and removes only the Host header. It does not clear Authorization, auth_username, auth_password, or auth_mode when the redirect target changes origin.

As a result, credentials intended for one origin can be forwarded to a different origin when foll…

---

## 29. 🟡 High Severity — Starlette: SSRF and NTLM credential theft via UNC paths in StaticFiles on Windows

**CVE:** `CVE-2026-48818` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-wqp7-x3pw-xc5r>

> ### Summary

When serving static files on Windows, `StaticFiles` resolves the requested path with [`os.path.realpath`](https://docs.python.org/3/library/os.path.html#os.path.realpath). If a UNC path (such as `\\attacker.com\share`) reaches the resolver, `realpath` causes the process to open a connection to the remote host over SMB (port 445). This is a server-side request forgery (SSRF) that leaks…

---

## 30. 🟡 High Severity — PyJWKClient: missing scheme allowlist enables CVE-2024-21643-class SSRF + token forgery via file://, ftp://, data: schemes

**CVE:** `CVE-2026-48522` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-993g-76c3-p5m4>

> &gt; [!NOTE]
&gt; The library does not directly return non-HTTP(S) URI contents to the attacker; the chained &quot;plant a JWKS to forge tokens&quot; scenario described in the original report requires additional application-layer flaws (attacker write access to a filesystem path, untrusted jku derivation) that this fix does not address. Severity is scored for the scheme-acceptance bug in isolation…

---

## 31. 🟡 High Severity — PyJWT: Public-key JWK accepted as HMAC secret enables forged HS256 tokens when mixed families are allowed

**CVE:** `CVE-2026-48526` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-xgmm-8j9v-c9wx>

> &gt; [!NOTE]
&gt; Exploitation requires a verifier configured with both symmetric and asymmetric algorithms in `algorithms=[…]` and a raw-JSON JWK as the `key=` argument, both contrary to documented usage, hence the High attack-complexity rating.

### Summary
When the verifier is decoding JSON Web Tokens, while supporting both asymmetric and HMAC algorithms, the library does not validate use of JS…

---

## 32. 🟡 High Severity — Symfony: Mailomat Mailer Webhook Parser Reads the HMAC Algorithm from the Request: Signature Algorithm Downgrade

**CVE:** `CVE-2026-48747` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-rrj9-5q2j-4gvr>

> ### Description

`Symfony\Component\Mailer\Bridge\Mailomat\Webhook\MailomatRequestParser::validateSignature()` parses the `X-MOM-Webhook-Signature` request header as `algo=signature` and passes the wire-supplied `$algo` directly to `hash_hmac()` when verifying the request against the configured webhook secret. The request therefore selects the HMAC primitive used to authenticate it.

PHP&#x27;s `h…

---

## 33. 🟡 High Severity — Symfony: IpUtils::PRIVATE_SUBNETS Omits IPv6 Transition Forms (6to4, NAT64, Teredo, IPv4-compatible): SSRF Bypass in NoPrivateNetworkHttpClient

**CVE:** `CVE-2026-48736` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-38cx-cq6f-5755>

> ### Description

`Symfony\Component\HttpClient\NoPrivateNetworkHttpClient` is documented as a decorator that blocks requests to private networks by default. The list of blocked subnets (`Symfony\Component\HttpFoundation\IpUtils::PRIVATE_SUBNETS` on 6.4+, a private constant in `NoPrivateNetworkHttpClient` on 5.4) enumerates RFC1918, loopback, link-local and IPv4-mapped IPv6 (`::ffff:0:0/96`) prefix…

---

## 34. 🟡 High Severity — @angular/service-worker: Sensitive Header Leakage on Cross-Origin Redirects in Angular Service Worker

**CVE:** `CVE-2026-54264` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-qxh6-94w6-9r5p>

> An information disclosure vulnerability exists in the `@angular/service-worker` package of the Angular framework. When the Service Worker fetches assets, it preserves metadata (such as headers) from the original request. However, on cross-origin redirects, the Service Worker fails to strip sensitive headers, violating the Fetch redirect algorithm. 

This allows a remote attacker to obtain sensitiv…

---

## 35. 🟡 High Severity — Angular: Template and Attribute Namespace Sanitization Bypass (XSS)

**CVE:** `CVE-2026-50557` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-f3m7-gqxr-g87x>

> An issue in the `@angular/compiler` and `@angular/core` packages allows bypassing element and attribute sanitization/validation through specific namespace workarounds.

Specifically, namespaced script elements (e.g., `&lt;svg:script&gt;` or `&lt;:svg:script&gt;`) were not properly identified as script elements by the Angular template preparser, allowing them to pass through template compilation wi…

---

## 36. 🟡 High Severity — node-tar applies PAX size override to intermediary GNU long-name/long-link headers, causing tar parser interpretation differential (file smuggling)

**CVE:** `CVE-2026-53655` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-vmf3-w455-68vh>

> ### Summary

`tar` (node-tar) applies a PAX extended header&#x27;s `size=` record (and other PAX
overrides) to the **next header entry of any type**, including intermediary
metadata headers such as a GNU long-name (`L`) or long-link (`K`) entry. Per
POSIX pax, a PAX extended header (`x`) describes the *next file entry*, not the
intermediary extension headers that may sit between the `x` header and…

---

## 37. 🟡 High Severity — @angular/service-worker: Request Credential & Cache Policy Stripping

**CVE:** `CVE-2026-50184` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-95qp-cmmw-mgqv>

> An issue in the `@angular/service-worker` package compromises the integrity of request-policy enforcement during request reconstruction. When the Angular Service Worker intercepts network requests for matched assets, it reconstructs a new `Request` object using an internal helper function.

During this reconstruction process, the helper function strips explicit client-defined safety parameters: th…

---

## 38. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
