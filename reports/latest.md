# Zero Day Pulse

> **Generated:** 2026-06-10 20:09 UTC &nbsp;|&nbsp; **Total:** 37 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 20 &nbsp;|&nbsp; 🟡 High: 17 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal vulnerabilities allow unauthenticated attackers to read sensitive files (logs, configuration files, credentials) via directory traversal in SimpleHelp RMM web endpoints.
- **Affected Products:** SimpleHelp remote support / RMM versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof‑of‑concept available (e.g., OffSec blog https://www.offsec.com/blog/cve-2024-57727/)
- **Patch Available:** SimpleHelp 5.5.8 released – patch URL https://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570
- **Active Exploitation:** Confirmed – CISA advisory AA25-163A and SecurityWeek report document ransomware actors exploiting the vulnerability.
- **Threat Actors:** DragonForce ransomware and other ransomware actors referenced in CISA advisory AA25-163A
- **Mitigation:** Upgrade to SimpleHelp 5.5.8 or later; if patching is not immediately possible, isolate/unexpose SimpleHelp from the internet, apply network‑level access controls, and rotate credentials discovered in affected instances.
- **Vendor Advisory:** https://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570

---

## 2. 🟠 Zero-Day — Claude Code Action: Malicious MCP Server Configuration in PRs Enables Remote Code Execution and Secret Exfiltration

**CVE:** `CVE-2026-47751` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-8q5r-mmjf-575q>

> Due to the combination of checking out PR head branches (attacker-controlled), reading `.mcp.json` from the working directory via default setting sources, and unconditionally enabling all project MCP servers via `enableAllProjectMcpServers`, it was possible for an attacker who opened a PR containing a malicious `.mcp.json` file to achieve arbitrary code execution on the GitHub Actions runner. This…

**Parallel AI Enrichment:**

- **Technical Details:** Attackers could submit a PR containing a malicious .mcp.json. Because the action checked out PR head branches (attacker-controlled), read .mcp.json from the working directory via default setting sources, and unconditionally enabled all project MCP servers via enableAllProjectMcpServers, an attacker-controlled MCP server configuration could be executed, leading to remote code execution on the GitHub Actions runner and exfiltration of workflow secrets when a privileged user triggered the Claude action on the PR.
- **Affected Products:** Claude Code Action (GitHub Action)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC reported in advisory
- **Patch Available:** Official patch/advisory available from GitHub Security Advisories at https://github.com/advisories/GHSA-8q5r-mmjf-575q
- **Active Exploitation:** No confirmed active exploitation reported in advisory
- **Threat Actors:** None known
- **Mitigation:** Disable automatic enabling of project MCP servers (avoid enableAllProjectMcpServers), do not read .mcp.json from untrusted working directories, avoid running CLAUDE actions on untrusted PRs or from untrusted contributors; treat PR head branches as untrusted.
- **Vendor Advisory:** https://github.com/advisories/GHSA-8q5r-mmjf-575q

---

## 3. 🟠 Zero-Day — Unpatched Langflow Flaw CVE-2026-5027 Exploited for Unauthenticated RCE

**CVE:** `CVE-2026-5027` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://thehackernews.com/2026/06/unpatched-langflow-flaw-cve-2026-5027.html>

> A high-severity unpatched security flaw in Langflow, an open-source low-code platform to build artificial intelligence (AI) applications, has come under active exploitation in the wild, according to findings from VulnCheck.

The vulnerability in question is CVE-2026-5027 (CVSS score: 8.8), a case of path traversal that could allow an attacker to write files to arbitrary locations.

&quot;The &#x27…

**Parallel AI Enrichment:**

- **Technical Details:** A path‑traversal vulnerability in the multipart upload 'filename' parameter of POST /api/v2/files allows an attacker to include '../' sequences to write files to arbitrary filesystem locations; combined with Langflow's default unauthenticated auto‑login, a single unauthenticated request can obtain a session and lead to remote code execution by writing malicious files.
- **Affected Products:** Langflow (POST /api/v2/files endpoint)
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** Public PoC reports exist (example PoC page: https://yh.do/cve-2026-5027-langflow-path-traversal-rce/). Activity observed weaponizing the bug to write test files; Censys data shows ~7,000 exposed instances.
- **Patch Available:** Official vendor patch/advisory URL unavailable.
- **Active Exploitation:** Confirmed active exploitation reported by VulnCheck and The Hacker News; observed activity writes test files and scans exposed instances (Censys).
- **Threat Actors:** None known
- **Mitigation:** Until a patch is available, restrict network exposure (block/limit access to Langflow instances), disable unauthenticated/auto‑login, run behind authentication/zero‑trust, remove public‑facing instances, monitor for unexpected files, and apply host‑level protections (WAF, file‑system write restrictions, containerization).
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — New Windows Zero-Day Exploit ‘RoguePlanet’ Released

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://www.securityweek.com/new-windows-zero-day-exploit-rogueplanet-released/>

> Exploiting a race condition in Microsoft Defender, the exploit leads to local privilege escalation to SYSTEM. The post New Windows Zero-Day Exploit ‘RoguePlanet’ Released appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** A TOCTOU race condition in Microsoft Defender’s signature/update workflow (interacting with VSS, Cloud Files API, opportunistic locks) allows a local unprivileged user to read shadow‑copy‑backed registry hives and dump credential material, leading to SYSTEM escalation.
- **Affected Products:** Microsoft Defender on Windows 10, Windows 11
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof‑of‑concept for RoguePlanet is available (see SecurityWeek and The Hacker News articles).
- **Patch Available:** Microsoft released Patch Tuesday updates on 2026-06-10 addressing multiple Defender issues; specific RoguePlanet advisory/patch URL: https://learn.microsoft.com/en-us/security/community/ (Vendor patch reference: Microsoft June 2026 Patch Tuesday — see https://www.microsoft.com/security/blog and https://www.catalog.update.microsoft.com)
- **Active Exploitation:** Public PoC and researcher‑released exploit have been reported; no confirmed widespread active campaigns.
- **Threat Actors:** None known
- **Mitigation:** Apply the June 2026 Microsoft patches immediately; if a specific patch is unavailable, temporarily disable Microsoft Defender real‑time protection, enforce least‑privilege for local accounts, enable EDR, and block unprivileged users from installing updates.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — Microsoft Patches Record 206 Flaws, Including Three Zero-Days and Critical RCE Bugs

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://thehackernews.com/2026/06/microsoft-patches-record-206-flaws.html>

> Microsoft on Tuesday released fixes for a record 206 security vulnerabilities impacting its software portfolio, including three flaws that have been publicly disclosed at the time of release.

Of the 206 flaws, 39 are rated Critical, and 167 are rated Important in severity. This includes 63 privilege escalation, 56 remote code execution, 30 information disclosure, 27 spoofing, 20 security

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-45657: Windows Kernel use‑after‑free in TCP/IP processing, exploitable via specially crafted network traffic for system‑level code execution. CVE-2026-47291: Integer overflow in HTTP.sys enabling remote code execution via malicious HTTP requests. CVE-2026-44815: Stack buffer overflow in Windows DHCP Client allowing unauthenticated remote code execution. CVE-2026-45585: BitLocker feature bypass permitting access to encrypted data with physical access.
- **Affected Products:** Microsoft Windows (Kernel/Win32k, HTTP.sys, DHCP Client, BitLocker, Collaborative Translation Framework/CTFMON), Microsoft Defender, Microsoft Edge/Chromium, UEFI Secure Boot and other Microsoft platform components
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoCs reported: YellowKey PoC for CVE-2026-45585 (by Chaotic Eclipse); suspected "GreenPlasma" PoC for CVE-2026-45586; PoC for a Microsoft Defender zero‑day named "RoguePlanet". URLs are referenced in the Hacker News coverage.
- **Patch Available:** Patches released on June 10, 2026. Official advisory: https://msrc.microsoft.com/update-guide/releaseNote/2026-Jun
- **Active Exploitation:** Publicly disclosed zero‑days (CVE-2026-50507, CVE-2026-49160, CVE-2026-45586) with PoCs are mentioned, but no confirmed active exploitation by specific actors is reported.
- **Threat Actors:** None known
- **Mitigation:** Apply the June 2026 security updates immediately. For the HTTP/2 and HTTP/3 header DoS issue, set the "MaxHeadersCount" registry key to limit header numbers. For BitLocker bypasses, restrict physical access and ensure firmware/OS updates are applied. General hardening: prioritize patching systems exposing network services (DHCP, HTTP/HTTPS/IIS) and limit external exposure.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/releaseNote/2026-Jun

---

## 6. 🟠 Zero-Day — Microsoft Defender 'RoguePlanet' zero-day grants SYSTEM privileges

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.bleepingcomputer.com/news/microsoft/microsoft-defender-rogueplanet-zero-day-grants-system-privileges/>

> A security researcher has released a new Microsoft Defender zero-day exploit named &quot;RoguePlanet&quot; just hours after Microsoft fixed two previously disclosed flaws during June 2026 Patch Tuesday. [...]

**Parallel AI Enrichment:**

- **Technical Details:** A race‑condition in Microsoft Defender allows a malicious archive/ISO to be mounted, causing the scanner to race and grant a SYSTEM‑level shell to the attacker.
- **Affected Products:** Microsoft Defender, Microsoft Malware Protection Engine
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC "RoguePlanet" is available at https://github.com/MSNightmare/RoguePlanet
- **Patch Available:** Microsoft published updates in June 2026 addressing CVE-2026-41091. See https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-41091
- **Active Exploitation:** Active exploitation of CVE‑2026‑41091 has been reported by Microsoft and multiple security news outlets.
- **Threat Actors:** None known
- **Mitigation:** Disable real‑time scanning or set Microsoft Defender exclusions for untrusted user‑controllable mounts, and apply the vendor updates as soon as they are available.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-41091

---

## 7. 🟠 Zero-Day — Patch Tuesday - June 2026

**CVE:** `CVE-2026-33825` | `CVE-2026-45585` | `CVE-2026-45498` | `CVE-2026-41091` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.rapid7.com/blog/post/em-patch-tuesday-june-2026>

> Microsoft is publishing 200 vulnerabilities on June 2026 Patch Tuesday . Microsoft is not aware of exploitation in the wild for any of these vulnerabilities, and is aware of public disclosure for three. This is similar to last month’s Patch Tuesday, however several of last month’s vulnerabilities ended up on CISA KEV in the days following their publication. So far this month, Microsoft has provide…

**Parallel AI Enrichment:**

- **Technical Details:** Local elevation of privilege caused by an insufficient access‑control/TOCTOU race condition in Microsoft Defender's threat remediation engine, allowing an authorized user/process to gain elevated privileges.
- **Affected Products:** Microsoft Defender (Windows Defender)
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N
- **Exploit Available:** Proof‑of‑concept analysis is available (see Picus Security blog). No widely published weaponized exploit was found.
- **Patch Available:** Microsoft published a patch in April 2026 (see vendor advisory link).
- **Active Exploitation:** No confirmed active exploitation in the wild has been reported.
- **Threat Actors:** None known
- **Mitigation:** Disable or restrict Microsoft Defender components and apply the vendor‑provided mitigation steps outlined in the advisory.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33825

---

## 8. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** IPI works by poisoning or embedding malicious instructions within external documents or corpora that an AI agent retrieves during normal operation; when the agent incorporates that retrieved content into its prompt, the injected instructions override or manipulate the agent's behavior (e.g., data exfiltration, command execution in agentic systems).
- **Affected Products:** AI agents, retrieval‑augmented generation (RAG) systems, agentic LLM systems
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof‑of‑concepts are available in research papers (e.g., arXiv) and Forcepoint disclosures; no formal weaponized exploit URL is published.
- **Patch Available:** Patch unavailable
- **Active Exploitation:** Confirmed in‑the‑wild IPI payloads reported by Google’s advisory and Forcepoint research.
- **Threat Actors:** None known
- **Mitigation:** Apply strict input sanitization for retrieved external content, implement retrieval‑source allowlisting, use provenance/trust checks, limit model exposures to untrusted web content, and apply instruction‑sanitization and context‑window controls.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 9. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) injects malicious instructions into data sources or tools (emails, documents, third‑party connectors, web content, tool outputs) consumed by an LLM‑enabled application. When the LLM or agent chains incorporate those sources into prompt construction or tool calls, the injected instructions can influence model behavior (including “zero‑click” cases where user input isn’t required). Examples include crafted payloads embedded in documents or external tool responses that the model interprets as instructions.
- **Affected Products:** Google Workspace (including Workspace apps integrated with Gemini / Gemini Enterprise); specific versions: not applicable (cloud service)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Public PoC reported by Noma Labs (GeminiJack zero‑click vulnerability) – http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability. Additional IPI payload examples documented by Forcepoint X‑Labs – http://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads
- **Patch Available:** No single patch; mitigation described in vendor advisory: http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html
- **Active Exploitation:** Confirmed research disclosures and PoC demonstration (Noma Labs GeminiJack zero‑click vulnerability); no reported broad active exploitation by threat actors.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses and continuous mitigation as described by Google: input sanitation/validation of external sources, strict tool output handling, provenance and source‑trust signals, query‑time instruction filtering, least‑privilege for agent actions, monitoring/telemetry for anomalous model decisions, and rapid response/update cycles. Encourage hardening connectors and restricting auto‑execution of agentic workflows until provenance checks pass.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 10. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection allows crafted web content (e.g., malicious iframes or user‑generated pages) to inject instructions that steer the agentic model to take unwanted actions such as navigation, transactions, or data exfiltration. Chrome mitigates this with a separate User Alignment Critic model, origin‑set gating that limits data exposure, deterministic URL checks, a real‑time prompt‑injection classifier, and user confirmations for sensitive actions.
- **Affected Products:** Google Chrome (agentic browsing feature), Cursor < 1.3
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC is available for Chrome agentic capabilities; no weaponized exploit URL is provided.
- **Patch Available:** Chrome mitigation measures are described in the vendor blog; Cursor is fixed in version 1.3 (see GitHub advisory https://github.com/cursor/cursor/security/advisories/GHSA-534m-3w6r-8pqr).
- **Active Exploitation:** No confirmed public reports of active exploitation of Chrome’s agentic browsing feature. A related research finding (GeminiJack) exists but is not reported as widespread active exploitation.
- **Threat Actors:** None known
- **Mitigation:** Update Cursor to version 1.3 or later. For Chrome, keep the browser up‑to‑date and enable the built‑in mitigations: origin gating, the User Alignment Critic, prompt‑injection classifier, and user confirmations for sensitive actions. Follow Google’s security guidance and report issues via the Vulnerability Rewards Program.
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

## 15. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

---

## 16. 🟠 Zero-Day — China-Linked JDY Botnet Expands to 1,500+ Devices for Cyber Reconnaissance

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://thehackernews.com/2026/06/china-linked-jdy-botnet-expands-to-1500.html>

> Cybersecurity researchers have warned of a &quot;resurgence and expansion&quot; of JDY, a covert network associated with China-nexus state-sponsored threat actors.

&quot;The JDY botnet comprises over 1,500 SOHO [small office and home office] and IoT devices and operates as a centrally controlled, high-performance scanner used to discover, fingerprint, and continuously map exposed services at scal…

---

## 17. 🟠 Zero-Day — Microsoft patches Exchange Server zero-day exploited in attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-exchange-server-zero-day-exploited-in-attacks/>

> Microsoft has patched an actively exploited Exchange Server vulnerability that allows threat actors to execute arbitrary JavaScript code in cross-site scripting (XSS) attacks targeting Outlook Web Access users. [...]

---

## 18. 🟠 Zero-Day — Microsoft patches YellowKey, GreenPlasma, MiniPlasma zero-days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-yellowkey-greenplasma-miniplasma-zero-days/>

> On Tuesday, Microsoft patched two zero-day vulnerabilities that let attackers gain SYSTEM privileges on fully patched Windows systems, and a third one that grants access to BitLocker-protected drives. [...]

---

## 19. 🟠 Zero-Day — Microsoft Defender RoguePlanet Zero-Day Grants SYSTEM Access on Updated Windows

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://thehackernews.com/2026/06/microsoft-defender-rogueplanet-zero-day.html>

> The anonymous security researcher going by the name Chaotic Eclipse (aka Nightmare-Eclipse) has released a proof-of-concept (PoC) exploit for yet another Microsoft Defender zero-day named RoguePlanet.

&quot;The exploit is a race condition, so it&#x27;s a hit or miss,&quot; the researcher, who published the exploit under a new GitHub account &quot;MSNightmare&quot; said. &quot;I have managed to ge…

---

## 20. 🟠 Zero-Day — SymfonyRuntime CVE-2024-50340 Patch Bypass: Web Requests Can Still Set APP_ENV/APP_DEBUG via parse_str/SAPI Argv Mismatch

**CVE:** `CVE-2026-47767` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://github.com/advisories/GHSA-fqc7-9xjw-jrh3>

> ### Description

CVE-2024-50340 (GHSA-x8vp-gf4q-mw5j) addressed an issue where, with `register_argc_argv=On`, a crafted query string let an unauthenticated GET change the kernel environment and debug flag by feeding `--env`/`--no-debug` through `$_SERVER[&#x27;argv&#x27;]`. The fix shipped in `symfony/runtime` 5.4.46 / 6.4.14 / 7.1.7 gated the argv read on `empty($_GET)` as a proxy for &quot;is th…

---

## 21. 🟡 High Severity — nebula-mesh: Session and OIDC state cookies lack the Secure attribute

**CVE:** `CVE-2026-48058` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-rqfj-vv8r-xhqc>

> `internal/web/session.go` and `internal/web/oidc.go` set `HttpOnly` and `SameSite=Lax` on every cookie but never `Secure`. A single plaintext request to the origin (operator on a LAN, mistyped URL, HTTP→HTTPS not strictly enforced, reverse proxy misconfiguration) discloses the session.

## Affected
All released versions up to v0.3.1.

## Impact
An attacker who can observe one HTTP request to the o…

---

## 22. 🟡 High Severity — nebula-mesh: Decrypted CA private key persists in heap after signing

**CVE:** `CVE-2026-48025` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-8h84-fhqq-q58v>

> `internal/pki/resolver.go:36-64` constructs a `CAManager` with the plaintext `ed25519.PrivateKey` after unwrapping via the master key; `internal/pki/ca.go:13-16` stores it. Callers at `internal/api/enroll.go:116`, `internal/api/updates.go:297`, and `internal/api/mobile_bundle.go:40` use the manager for one `Sign()` and drop the reference on function return — but the underlying slice contents are n…

---

## 23. 🟡 High Severity — OpenTelemetry Operator for Kubernetes's ServiceMonitor bearerTokenFile reads arbitrary local file and sends contents as bearer auth

**CVE:** `CVE-2026-47701` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-cxh2-4639-vmc5>

> ## Affected

Repository: github.com/open-telemetry/opentelemetry-operator
Component: cmd/otel-allocator (TargetAllocator)
Companion: Prometheus Operator API types (CRDs)

## Summary

OpenTelemetry Operator&#x27;s TargetAllocator watches `ServiceMonitor` resources via the Prometheus Operator CR watcher and converts each selected endpoint into a Prometheus scrape configuration entry. The endpoint fi…

---

## 24. 🟡 High Severity — Ivanti, Fortinet, and SAP Release Patches for Multiple Critical Vulnerabilities

**CVE:** `CVE-2026-25089` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://thehackernews.com/2026/06/ivanti-fortinet-and-sap-release-patches.html>

> Fortinet, Ivanti, and SAP have released security updates to address multiple critical security vulnerabilities that could result in arbitrary code execution and information disclosure.

The security flaw patched by Fortinet relates to a command injection vulnerability in FortiSandbox, FortiSandbox Cloud, and FortiSandbox PaaS WEB UI. It&#x27;s tracked as CVE-2026-25089 (CVSS score: 9.1).

&quot;An

---

## 25. 🟡 High Severity — CISA Adds Cisco, Chrome, and Arista Flaws to KEV Catalog Amid Active Exploitation

**CVE:** `CVE-2026-20245` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://thehackernews.com/2026/06/cisa-adds-cisco-chrome-and-arista-flaws.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added three new vulnerabilities to its Known Exploited Vulnerabilities (KEV) catalog, following reports of active exploitation.

The list of vulnerabilities is as follows -


  CVE-2026-20245 (CVSS score: 7.8) - An improper encoding or escaping of output vulnerability in Cisco Catalyst SD-WAN Manager that could allow an

---

## 26. 🟡 High Severity — Nezha's private services (`EnableShowInService: false`) are enumerable via per-server endpoints, leaking name and timing data

**CVE:** `CVE-2026-49397` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-vrmh-5mmx-hjwx>

> # Private services (`EnableShowInService: false`) are enumerable via per-server endpoints, leaking name and timing data

**CWE**: CWE-285 (Improper Authorization) via CWE-200 (Exposure of Sensitive Information to an Unauthorized Actor) and CWE-863 (Incorrect Authorization — inconsistent gating across data-reader paths)

**CVSS v3.1**: `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N` → 5.3 (Medium)

…

---

## 27. 🟡 High Severity — Go Restful API Boilerplate: Hardcoded JWT Secret "random" Allows Token Forgery

**CVE:** `CVE-2026-48031` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-mqq6-462x-jxmm>

> ## Vulnerability: CWE-798 — Hardcoded JWT Secret + Broken Mitigation

### Affected Component
- `github.com/dhax/go-base` — Go REST API boilerplate (go-chi/jwtauth/v5, Viper, PostgreSQL/Bun)
- 1,685 stars on GitHub

### Vulnerability Locations

| File | Line | Role |
|------|------|------|
| `dev.env` | 10 | `AUTH_JWT_SECRET=random` — template default shipped to all users |
| `cmd/serve.go` | 35 | …

---

## 28. 🟡 High Severity — Papra HTTP redirect bypass can lead to SSRF via webhook delivery system

**CVE:** `CVE-2026-48051` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-5g86-85rp-f9hx>

> ### Summary

Papra&#x27;s webhook delivery system contains an SSRF protection bypass that allows any authenticated organisation member to cause the server to make HTTP requests to internal addresses — loopback, link-local, and RFC-1918 ranges. The SSRF protection validates the registered webhook URL but ignores redirect destinations. The HTTP client (`ofetch`) follows 3xx responses automatically, …

---

## 29. 🟡 High Severity — @hulumi/baseline: AccountFoundation reuse paths silently downgrade GuardDuty / Security Hub posture

**CVE:** `CVE-2026-48037` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-cj8g-prcm-mfg5>

> **Affected:** `@hulumi/baseline` `&lt; 1.4.0` — **Fixed in:** `1.4.0` — **Severity:** Medium — **CWE-693 (Protection Mechanism Failure)**

#### Summary

`AccountFoundation` can either create AWS detective services (GuardDuty for threat detection, Security Hub for compliance dashboards) or reuse pre-existing ones via opt-in flags. The reuse paths just imported the existing resources and reported su…

---

## 30. 🟡 High Severity — @hulumi/baseline: AccountFoundation audit-delivery S3 bucket could be silently weakened

**CVE:** `CVE-2026-48035` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-2mxr-p26x-mj73>

> **Affected:** `@hulumi/baseline` `&lt; 1.4.0` — **Fixed in:** `1.4.0` — **Severity:** High — **CWE-1059 (Insufficient Technical Documentation / Behavioral Inconsistency)**

#### Summary

The S3 bucket that `AccountFoundation` creates to receive CloudTrail and AWS Config audit logs is meant to be tamper-resistant — if someone with delete access can erase from it, the forensic trail is gone. There w…

---

## 31. 🟡 High Severity — @hulumi/policies has a HULUMI-H5 bypass via decoy sibling resources targeting a different bucket

**CVE:** `CVE-2026-48034` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-9vc9-4jv3-rf86>

> **Affected:** `@hulumi/policies` `&lt; 1.4.0` — **Fixed in:** `1.4.0` — **Severity:** High — **CWE-284 (Improper Access Control)**

#### Summary

HULUMI-H1 forbids raw `aws:s3:Bucket` outside of Hulumi&#x27;s `SecureBucket` component, with one exemption: a raw bucket that&#x27;s a child of a `SecureBucket` is allowed because the component is responsible for the hardening. HULUMI-H5 is the defence-…

---

## 32. 🟡 High Severity — @hulumi/policies bypasses policy packs with a forged Pulumi-URN logical name

**CVE:** `CVE-2026-48033` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-rhgj-6g2c-frmm>

> **Affected:** `@hulumi/policies` `&lt; 1.4.0` — **Fixed in:** `1.4.0` — **Severity:** High — **CWE-693 (Protection Mechanism Failure)**

#### Summary

Pulumi gives every cloud resource a structured URN that includes the resource&#x27;s type chain (`hulumi:baseline:aws:SecureBucket$aws:s3/bucketV2:BucketV2`) and the _logical name_ the developer freely chose (anything after the final `::`). Several …

---

## 33. 🟡 High Severity — @hulumi/policies bypasses IAM-role policy checks when the role trusts multiple OIDC providers

**CVE:** `CVE-2026-48032` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://github.com/advisories/GHSA-g759-4pxw-6692>

> **Affected:** `@hulumi/policies` `&lt; 1.4.0` — **Fixed in:** `1.4.0` — **Severity:** High — **CWE-697 (Incorrect Comparison)**

#### Summary

AWS IAM trust policies can list more than one federated identity provider — for example, a role that accepts BOTH GitHub Actions OIDC and Google&#x27;s OIDC. The `G_OIDC_1` and `G_OIDC_2` policy rules are supposed to flag IAM roles whose GitHub-OIDC trust i…

---

## 34. 🟡 High Severity — CVE-2026-10520, CVE-2026-10523 - Multiple critical vulnerabilities affecting Ivanti Sentry

**CVE:** `CVE-2026-10520` | `CVE-2026-10523` | `CVE-2023-38035` | `CVE-2020-15505` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-10
**Reference:** <https://www.rapid7.com/blog/post/etr-cve-2026-10520-cve-2026-10523-multiple-critical-vulnerabilities-affecting-ivanti-sentry>

> Overview On June 9, 2026, Ivanti published a security advisory for two critical vulnerabilities affecting Ivanti Sentry (formerly known as MobileIron Sentry), which per the vendor website is an “in-line gateway that manages, encrypts, and secures traffic between the mobile device and back-end enterprise systems”. The most severe issue, CVE-2026-10520 , is an OS command injection vulnerability with…

---

## 35. 🟡 High Severity — Pheditor: OS Command Injection in terminal handler via unsanitized 'dir' parameter

**CVE:** `CVE-2026-48030` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://github.com/advisories/GHSA-jvc5-6g7q-c843>

> ### Summary

An OS Command Injection vulnerability in the terminal action handler allows any authenticated user to execute arbitrary OS commands by injecting shell metacharacters into the &#x27;dir&#x27; POST parameter, completely bypassing the TERMINAL_COMMANDS whitelist and achieving full Remote Code Execution with web server privileges.

### Details

The terminal handler in pheditor.php accepts…

---

## 36. 🟡 High Severity — PhoenixStorybook: Unauthenticated remote code execution via HEEx template injection in phoenix_storybook playground

**CVE:** `CVE-2026-8467` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://github.com/advisories/GHSA-55hg-8qxv-qj4p>

> ### Summary
An unsafe HEEx template generation vulnerability allows any unauthenticated user to execute arbitrary code on the server. The phoenix_storybook playground accepts user-controlled attribute values over WebSocket and interpolates them unsanitized into a HEEx template that is subsequently compiled and evaluated with full Elixir `Kernel` access.

### Details
The vulnerability is a three-st…

---

## 37. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
