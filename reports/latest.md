# Zero Day Pulse

> **Generated:** 2026-07-01 02:13 UTC &nbsp;|&nbsp; **Total:** 34 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 15 &nbsp;|&nbsp; 🟡 High: 19 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CWE-22 (Path Traversal) in the SimpleHelp web application's HTTP request handling. Certain endpoints (notably the Toolbox / file-serving components) fail to properly sanitize user-supplied file-path input, allowing an unauthenticated remote attacker to inject directory-traversal sequences (e.g., '../') in crafted HTTP requests and download arbitrary files from the underlying SimpleHelp host. Sensitive files exposed include serverconfig.xml (containing hashed user passwords and service-account secrets), /etc/passwd, and private SSH keys. Attackers identify a vulnerable SimpleHelp instance reachable via HTTP, send a crafted request to trigger path traversal, harvest credentials, then chain with CVE-2024-57726 (low-priv → server-admin privilege escalation via API key abuse) and CVE-2024-57728 (zip-slip file upload) to push ransomware payload and use the legitimate RMM functionality to fan the ransomware out across managed endpoints. No authentication is required for the initial exploitation step.
- **Affected Products:** SimpleHelp Remote Support / Remote Monitoring and Management (RMM) software, version 5.5.7 and all earlier releases.
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true — Public PoC at https://github.com/imjdl/CVE-2024-57727 and Metasploit module auxiliary/scanner/http/simplehelp_toolbox_path_traversal. YouTube technical walkthroughs also publicly demonstrate exploitation.
- **Patch Available:** true — SimpleHelp v5.5.8, released Jan 10, 2025, fixes CVE-2024-57727 (along with CVE-2024-57726 and CVE-2024-57728). Vendor advisory / KB: https://guides.simple-help.com/kb---security-vulnerabilities-01-2025. NVD reference: https://nvd.nist.gov/vuln/detail/cve-2024-57727.
- **Active Exploitation:** true — Confirmed by CISA Advisory AA25-163A 'Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider' published Jun 12, 2025, which states ransomware actors have been exploiting unpatched SimpleHelp (including via CVE-2024-57727) against MSPs and their downstream customers since January 2025, and that DragonForce actors leveraged this vulnerability chain to achieve double-extortion compromises. Additional confirmation: RH-ISAC May 29, 2025 on DragonForce leveraging the same SimpleHelp vulnerability chain against MSP customers.
- **Threat Actors:** DragonForce ransomware operators. Per CISA Advisory AA25-163A (Jun 12, 2025) and RH-ISAC reporting (May 29, 2025), DragonForce actors have chained CVE-2024-57727 with CVE-2024-57726 (privilege escalation, CVSS 9.9) and CVE-2024-57728 (arbitrary file upload / zip slip, CVSS 7.2) to escalate from unauthenticated file read → server admin → ransomware deployment across MSP and downstream customer endpoints, including a utility billing software provider compromised via unpatched SimpleHelp RMM.
- **Mitigation:** 1) Upgrade SimpleHelp to v5.5.8 or later immediately (patch released within two days of vendor disclosure in January 2025). 2) Until patched, do not expose SimpleHelp instances directly to the internet; place them behind a VPN / restrict management UI to known IPs, as the vulnerability is unauthenticated and trivially reachable. 3) Audit SimpleHelp hosts (especially serverconfig.xml exposure, unfamiliar technicians / API keys, and recent zip/file uploads) for indicators of prior exploitation — CISA AA25-163A includes detection guidance and IOCs. 4) Hunt for post-exploitation activity (DragonForce artifacts, RMM-driven lateral ransomware deployment, double-extortion patterns) and review MSP / downstream-customer environments for signs of compromise. 5) Apply CISA's AA25-163A mitigations: network segmentation, MFA on admin accounts, monitoring of outbound traffic from the RMM host, credential rotation for any secrets that lived in serverconfig.xml.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — CISA: Windows BlueHammer flaw now exploited by ransomware gangs

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-windows-bluehammer-flaw-now-exploited-by-ransomware-gangs/>

> CISA confirmed on Monday that ransomware gangs are now exploiting a Microsoft Defender privilege escalation vulnerability, dubbed BlueHammer, that has previously been abused in zero-day attacks. [...]

**Parallel AI Enrichment:**

- **Technical Details:** BlueHammer is a Local Privilege Escalation (LPE) in the Microsoft Defender Antimalware Platform classified as CWE-1220 (Insufficient Granularity of Access Control). The root cause is a TOCTOU (time-of-check to time-of-use) race condition in Windows Defender's file-remediation/signature-update engine. The exploit chains five components: (1) the Defender signature-update workflow, which creates a Volume Shadow Copy (VSS) snapshot containing accessible SAM, SYSTEM, and SECURITY registry hives; (2) the Volume Shadow Copy Service (VSS); (3) the Windows Cloud Files API (CfRegisterSyncRoot/CfConnectSyncRoot) with a fake .lock file and CfCallbackFetchPlaceholders callback that freezes Defender at the right moment; (4) batch opportunistic locks (oplocks) on RstrtMgr.dll and a bait EICAR test file; and (5) symbolic links/junction points used to redirect a path so Defender's SYSTEM-level operation is swapped into the attacker-controlled directory inside the VSS snapshot. The race forces Defender (running as SYSTEM) to open the SAM hive from the still-mounted shadow copy, read the SYSTEM hive boot key, decrypt SAM encryption material, and recover local NTLM password hashes — yielding full LPE to NT AUTHORITY\SYSTEM and the ability to spawn a SYSTEM-privileged shell. Vector: AV:L (local), AC:L (low complexity), PR:L (low privileges), UI:N (no interaction), S:U (unmodified), C:H/I:H/A:H (high C/I/A impact).
- **Affected Products:** Microsoft Defender Antimalware Platform versions prior to 4.18.26050.3011 (last vulnerable build: 4.18.26020.6), running on Windows 10 (all supported editions), Windows 11 (all supported editions), Windows Server 2016, Windows Server 2019, Windows Server 2022, and Windows Server 2025.
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true — A fully functional public PoC for BlueHammer (CVE-2026-33825) was released on approximately 2026-04-07/08 by security researcher 'Chaotic Eclipse'. Sources: https://www.cyderes.com/howler-cell/windows-zero-day-bluehammer , https://www.cynet.com/blog/bluehammer-redsun-undefended-chaotic-eclipse-adds-unexpected-risk-to-the-april-threat-landscape/
- **Patch Available:** true — Microsoft fixed CVE-2026-33825 in Microsoft Defender Antimalware Platform update 4.18.26050.3011, released as part of the April 2026 Patch Tuesday on 2026-04-14. Patch/advisory URL: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33825 (NVD: https://nvd.nist.gov/vuln/detail/CVE-2026-33825).
- **Active Exploitation:** true — CISA added CVE-2026-33825 to its Known Exploited Vulnerabilities (KEV) catalog on 2026-04-22 based on evidence of active exploitation. On 2026-06-29/30, CISA confirmed that multiple ransomware gangs are now exploiting the flaw in the wild. CISA issued a two-week patch deadline to U.S. federal agencies. Sources: https://www.cisa.gov/news-events/alerts/2026/04/22/cisa-adds-one-known-exploited-vulnerability-catalog , https://www.bleepingcomputer.com/news/security/cisa-windows-bluehammer-flaw-now-exploited-by-ransomware-gangs/ , https://www.securityweek.com/bluehammer-vulnerability-exploited-in-ransomware-attacks/
- **Threat Actors:** Chaotic Eclipse (also known as Nightmare Eclipse) is the security researcher/group that published the public BlueHammer PoC. CISA confirmed on 2026-06-29/30 that multiple ransomware gangs are exploiting CVE-2026-33825 in the wild, but no specific ransomware family or operator has been publicly attributed as of 2026-07-01.
- **Mitigation:** (1) Apply the official patch by updating the Microsoft Defender Antimalware Platform to version 4.18.26050.3011 or later via Windows Update / Microsoft Update / Microsoft Endpoint Configuration Manager (released April 2026 Patch Tuesday on 2026-04-14). (2) U.S. federal agencies must remediate per CISA's Known Exploited Vulnerabilities (KEV) catalog / BOD 22-01 timeline (CISA imposed a two-week patch deadline). (3) Harden against local LPE abuse: minimize the number of local user accounts with non-essential privileges, restrict local administrator rights, enable LSA Protection / Credential Guard where available, monitor for abnormal MsMpEng.exe child processes, and ensure EDR/Defender-for-Endpoint behavior-monitoring rules detect Volume-Shadow-Copy reads of the SAM hive.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33825

---

## 3. 🟠 Zero-Day — Oracle E-Business Suite Flaw CVE-2026-46817 Actively Exploited in the Wild

**CVE:** `CVE-2026-46817` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://thehackernews.com/2026/06/oracle-e-business-suite-flaw-cve-2026.html>

> A critical security flaw impacting Oracle E-Business Suite has come under active exploitation in the wild, according to Defused Cyber.

The vulnerability, tracked as CVE-2026-46817 (CVSS score: 9.8), refers to an improper privilege management and authentication flaw in Oracle Payments that could be abused to take over susceptible instances.

&quot;Easily exploitable vulnerability allows

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-46817 is an improper privilege management and authentication flaw (CWE-269 Improper Privilege Management, CWE-287 Improper Authentication, and CWE-306 Missing Authentication for Critical Function) in the File Transmission sub-component of Oracle Payments in Oracle E-Business Suite. The vulnerability is network-reachable over HTTP, requires no authentication, no user interaction, and has low attack complexity. An unauthenticated remote attacker can send specially crafted requests (observed in the wild as unauthenticated POST requests containing XML payloads targeting the /OA_HTML/ibytransmit endpoint, including attempts to read local files) to completely take over the Oracle Payments component and, by extension, the affected Oracle E-Business Suite instance. The vulnerability impacts Confidentiality, Integrity, and Availability (CIA: H/H/H).
- **Affected Products:** Oracle E-Business Suite versions 12.2.3 through 12.2.15, specifically the Oracle Payments component (File Transmission sub-component).
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false. Despite confirmed in-the-wild exploitation, no public proof-of-concept (PoC) or weaponized exploit code is publicly available per multiple authoritative sources (NVD, GitHub Advisory Database, The Hacker News, BleepingComputer, Help Net Security).
- **Patch Available:** true. Oracle shipped the fix in the May 2026 Critical Security Patch Update (CPU), released May 28, 2026. Advisory URL: https://www.oracle.com/security-alerts/cspumay2026verbose.html (top-level: https://www.oracle.com/security-alerts/cspumay2026.html).
- **Active Exploitation:** true. Confirmed active exploitation in the wild has been reported. Defused Cyber observed exploitation on Oracle E-Business Suite honeypots over June 27-28, 2026. Exploitation has been corroborated by The Hacker News, BleepingComputer, SecurityAffairs, Help Net Security, and the UK NHS Digital cyber alert CC-4803 (issued June 30, 2026).
- **Threat Actors:** None known. No specific APT, ransomware family, or named threat actor has been attributed. An unnamed actor was observed by Defused Cyber exploiting the vulnerability on Oracle E-Business honeypots over the weekend of June 27-28, 2026, but the operator was not identified.
- **Mitigation:** 1) Apply the Oracle May 2026 Critical Security Patch Update (CPU) immediately to all Oracle E-Business Suite instances on supported versions 12.2.3–12.2.15; this is the primary mitigation. 2) Until and after patching, restrict Oracle E-Business Suite web interfaces (HTTP/HTTPS front-end, including Oracle Payments endpoints) to internal/trusted networks only – remove any direct public internet exposure. 3) Place Oracle EBS behind a VPN, an allowlisted reverse proxy, or a WAF; restrict administrative access to jump hosts on trusted segments. 4) Baseline and monitor normal access patterns to Oracle EBS HTTP endpoints (especially /OA_HTML/ibytransmit) and alert on anomalous unauthenticated POST requests, XML payloads, or attempts to read local files. 5) For any Oracle EBS instance that was internet-facing and unpatched past May 28, 2026, treat it as potentially compromised: perform a full forensic review, rotate all credentials/keys stored on the host, rotate credentials and integrations tied to payment workflows, validate the integrity of the Oracle EBS application server, and review outbound connections, scheduled jobs, and File Transfer configurations associated with Oracle Payments.
- **Vendor Advisory:** https://www.oracle.com/security-alerts/cspumay2026verbose.html

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an AI system processes attacker-supplied content (a web page, email, document, image, or other untrusted input) that contains hidden malicious instructions. The AI agent ingests both the user's legitimate instruction and the attacker-controlled data in the same context window; the malicious instructions then override or subvert the user's intent, leading to data exfiltration, system-prompt disclosure, content destruction, or unwanted tool/agent actions. Google's analysis of 2-3 billion Common Crawl pages observed payloads delivered via standard HTML, invisible text (white-on-white, zero-font-size spans, hidden DIVs, HTML comments, metadata, JavaScript-rendered content), and SEO-style page seeding. Payloads fell into five behavioural categories: (1) Harmless pranks, (2) Helpful guidance, (3) Search-engine-optimization spam, (4) Deterring AI agents, and (5) Malicious (data exfiltration and destruction).
- **Affected Products:** Gemini, Workspace with Gemini (Google products explicitly cited in the blog). The class of attack applies broadly to agentic AI / LLM-integrated web-browsing systems; complementary reporting identifies IPI weaponization against ChatGPT, GitHub Copilot, Cursor, Claude Code, Microsoft Copilot Studio, and the LiteLLM / Trivy / Checkmarx / BerriAI AI supply chain. No specific product versions are listed because the blog addresses a class of attack rather than a single CVE-numbered vulnerability.
- **CVSS Score:** CVSS score unavailable. The blog post reports on a category of attacks (Indirect Prompt Injection) on AI systems rather than a single patched CVE-numbered vulnerability, so no CVSS base score is published.
- **CVSS Vector:** CVSS vector unavailable. The blog post describes a class of attack (Indirect Prompt Injection) rather than a single CVE-numbered vulnerability, so no CVSS v3 vector is assigned.
- **Exploit Available:** true. Weaponized IPI payloads confirmed on live web infrastructure: Forcepoint X-Labs identified 10 verified payloads (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads); Palo Alto Unit 42 catalogued 22 distinct IPI techniques observed in the wild (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/); and the Google blog references 'known exfiltration prompts published by security researchers in 2025'.
- **Patch Available:** false. No single vendor patch applies because there is no CVE for this class of attack — IPI is a property of LLM/agent design itself. Google states it is investing in 'hardening our AI models and products' continuously (see https://blog.google/security/prompt-injections-web/ and the May 2026 follow-up at http://security.googleblog.com/2026/05/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections.html). Related product-specific CVE fixes exist (e.g., MS Copilot Studio CVE-2026-21520, CVSS 7.5), but they are distinct from this blog's class-of-attack subject.
- **Active Exploitation:** true. Confirmed in-the-wild: (a) Google observed a 32% relative increase in the malicious IPI category between November 2025 and February 2026 (https://blog.google/security/prompt-injections-web/); (b) Forcepoint X-Labs verified 10 weaponised IPI payloads on live websites spanning financial fraud and data destruction (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads); (c) Palo Alto Unit 42 observed 22 distinct IPI techniques weaponized in real telemetry (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/); (d) GTIG's AI Threat Tracker (May 2026) attributes IPI activity to APT27, APT45, UNC2814, and TeamPCP/UNC6780 (https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access). Google concludes: 'we expect both the scale and sophistication of attempted IPI attacks to grow in the near future.'
- **Threat Actors:** The Google Security Blog post itself does not name specific threat actors; it refers only generically to 'threat actors' and 'individual website authors' seeding prompt injections on public websites. Related Google Threat Intelligence Group (GTIG) reporting (May 2026) attributes broader IPI/AI-abuse activity to APT27 (China), APT45 (DPRK), UNC2814, TeamPCP/UNC6780 (cybercrime cluster), and 'Operation Overload'; Palo Alto Unit 42 also attributes on-the-web IPI campaigns to the 'Screening Serpens' group.
- **Mitigation:** Defense-in-depth is required because IPI is a class of attack with no single patch. Recommended layers include: (1) AI-model hardening and adversarial training against prompt-injection payloads; (2) 'instruction hierarchy' / 'spotlighting' so trusted user instructions outrank data-channel instructions; (3) screening, sanitization, and grounding of retrieved web/document content before it is added to the prompt; (4) dedicated AI red teams and Google's AI Vulnerability Reward Program for external researchers; (5) network-layer controls such as Forcepoint Real Time Analytics and CASB-style blocks of known IPI URLs/domains; (6) Google's Secure AI Framework (SAIF) and product-level controls in Workspace with Gemini; (7) VirusTotal Code Insight / API-aggregator signal logic to detect malicious AI tooling. Google explicitly states: do not rely on any single layer; use defense-in-depth.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an attacker plants hostile instructions inside data the LLM ingests (emails, documents, calendar events, web pages, PDFs, images, code comments) rather than in the user's prompt; the agentic Gemini treats those instructions as trusted commands because it cannot reliably distinguish system/developer messages from attacker-controlled content. Typical Workspace vectors are Gmail/Docs/Drive bodies, Calendar event descriptions, Meet transcripts, and web pages fetched for summarization. Concealment techniques documented in the wild include HTML comments, CSS invisibility (display:none, font-size:1px), aria-hidden/visually-hidden attributes, off-screen positioning, white-on-white text, zero-width Unicode, and Base64- or SVG-encapsulated payloads decoded at runtime. Observed attack outcomes include summarizer hijack, unauthorized email/tool actions, calendar-entry manipulation, sensitive-data exfiltration to attacker-controlled URLs, filesystem destruction (sudo rm -rf), financial-fraud redirection, system-prompt leakage, and multi-turn data exfiltration chains.
- **Affected Products:** Google Workspace with Gemini (Gmail, Google Docs, Google Drive, Google Meet, Calendar); Gemini 2.5 family of models; standalone Gemini app; Gemini API; Vertex AI (Gemini-backed function calling); Gemini Code Assist. No specific patched version numbers are published because Google treats indirect prompt injection (IPI) as a continuously-hardened threat class rather than a single-version bug.
- **CVSS Score:** CVSS score unavailable. Google treats IPI as an evolving class of adversarial technique rather than a single CVE-style software defect, so no CVSS v3.x base score has been published for the Google Workspace with Gemini IPI disclosure of Apr 2, 2026. (For context, the related 'EchoLeak' / CVE-2025-32711 score of 9.3 applies to Microsoft 365 Copilot, not Google Workspace.)
- **CVSS Vector:** CVSS vector unavailable. Google's GenAI Security Team frames Indirect Prompt Injection (IPI) as an evolving class of adversarial technique rather than a single CVE-style software defect, so no CVSS v3 vector has been published for the Google Workspace with Gemini disclosure of Apr 2, 2026. (The related 'EchoLeak' bug, CVE-2025-32711 / CVSS 9.3, applies to Microsoft 365 Copilot, not Google Workspace.)
- **Exploit Available:** true - Multiple independent PoCs and live in-the-wild payloads exist. Forcepoint X-Labs published 10 verified in-the-wild IPI payloads on Apr 22, 2026 (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads); Palo Alto Unit 42 captured web-based IPI attacks on Mar 3, 2026 (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/); 0din.ai documented a Calendar-Inject IPI PoC abusing Gemini via hidden prompts in calendar invites (https://0din.ai/blog/phishing-for-gemini); HiddenLayer documented a Gemini-for-Workspace phishing/content-manipulation PoC (https://www.hiddenlayer.com/research/new-gemini-for-workspace-vulnerability-enabling-phishing-content-manipulation).
- **Patch Available:** false - There is no single version-cutover patch for IPI. Google's own statement is that 'IPI is not the kind of technical problem you solve and move on'; the vendor delivers continuous hardening (config updates, prompt-engineering changes, ML retraining, model updates) instead of a discrete patched release. The advisory itself (https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/) serves as the standing guidance.
- **Active Exploitation:** true - Google documents active IPI patterns on the public web in the Apr 2, 2026 advisory itself. Independent in-the-wild confirmations: Forcepoint X-Labs documented 10 live IPI payloads on Apr 22, 2026 (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads); Palo Alto Unit 42 captured web-based IPI attacks on Mar 3, 2026 (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/); Google's GTIG Feb 2026 report documents Iranian (APT42), Chinese (APT31, APT41, UNC795, UNC5356) and North Korean APT activity leveraging Gemini (https://cloud.google.com/blog/topics/threat-intelligence/distillation-experimentation-integration-ai-adversarial-use); SecurityWeek reports a measurable increase in malicious IPI attempts.
- **Threat Actors:** APT31, APT41, APT42, APT43, UNC795, and UNC5356 (named in Google Threat Intelligence Group's Feb 2026 'GTIG AI Threat Tracker' report on adversarial misuse of Gemini); information-operation groups DRAGONBRIDGE, KRYMSKYBRIDGE, and Doppelganger; criminal actors using jailbroken LLMs such as FraudGPT and WormGPT for BEC and social-engineering operations.
- **Mitigation:** Google describes a layered continuously-updated defense rather than a single patch. Components: (1) Deterministic defenses — centralized Policy Engine enforcing URL sanitization, user-confirmation prompts for sensitive actions, tool-chaining policies, and regex takedowns of known IPI patterns; (2) ML-based defenses — Gemini classifier models retrained on synthetic and real-world IPI samples, including markdown sanitization and suspicious-URL redaction using Google Safe Browsing; (3) LLM-based defenses — refined system instructions telling the model to ignore instructions embedded in data; (4) Gemini model hardening — improving the model's intrinsic ability to identify and ignore harmful in-data instructions; (5) continuous red-teaming (human and automated) plus the Google AI Vulnerability Reward Program; (6) end-user mitigation notifications in Workspace. Administrator guidance is documented at https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini and the deeper strategy at https://blog.google/security/mitigating-prompt-injection-attacks/.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: attacker-controlled content embedded in malicious web pages, third-party iframes, or user-generated content (e.g., user reviews) contains instructions that the agentic Gemini in Chrome interprets alongside legitimate user instructions. This can cause the agent to take unwanted actions such as initiating financial transactions, exfiltrating sensitive data, or being steered away from the user's intended goal.
- **Affected Products:** Google Chrome with Gemini-in-Chrome agentic capabilities (Chrome 154)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Google's announced layered defensive architecture includes: (1) User Alignment Critic — an isolated secondary LLM that evaluates agent's proposed actions and can veto unsafe ones; (2) Agent Origin Sets — restricts the agent to specific read-only and read+write origins; (3) Explicit user confirmations for sensitive sites (banking, healthcare), password manager sign-ins, and payment/messaging actions; (4) Real-time prompt-injection classifier — a dedicated model running in parallel to block actions based on injected content; (5) Spotlighting — instructs the model to prioritize user/system instructions over page content; (6) Deterministic URL checks — restrict model-generated navigation targets to known public URLs; (7) Integration with Safe Browsing, on-device scam detection, and internal red-teaming.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow (out-of-bounds read/write, CWE-125/787) caused by incorrect bounds checks in the Rust-based CrabbyAVIF AVIF parser/decoder in Android. The bug lives in unsafe blocks performing manual bounds calculations — including YUV/alpha plane sizing and chroma-width / plane-size / row-bytes calculations on the NV12 path — even though the surrounding code is written in safe Rust. A specially crafted AVIF image could trigger out-of-bounds memory accesses that, when chained with other bugs, could enable remote code execution with no user interaction and no privileges required.
- **Affected Products:** Google Android (Android System component in AOSP 16) — CrabbyAVIF AVIF parser/decoder (external/rust/crabbyavif). Addressed by Android security patch level 2025-08-05 (and 2025-08-01).
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false. No public proof-of-concept or weaponized exploit has been published; the linear buffer overflow was identified and mitigated internally before being shipped to AOSP.
- **Patch Available:** true. Patches shipped in the Android Security Bulletin – August 2025: https://source.android.com/docs/security/bulletin/2025-08-01. Upstream CrabbyAVIF commits: https://android.googlesource.com/platform/external/rust/crabbyavif/+/9bcc1a311114ab844b417d3cdec50dcedfd0603f and https://android.googlesource.com/platform/external/rust/crabbyavif/+/42feb427a42afd9eebe6391a0d8a7b083fe82140.
- **Active Exploitation:** false. No in-the-wild exploitation has been reported; the issue was identified and remediated internally prior to public AOSP release and was disclosed by Google on Nov 13, 2025 primarily as a case study on Rust memory-safety effectiveness in Android.
- **Threat Actors:** None known. The CrabbyAVIF issue (CVE-2025-48530) is described by Google as an internal 'near-miss' caught before public release; no state-sponsored, criminal, or ransomware group exploitation has been reported.
- **Mitigation:** Apply the Android security patch level 2025-08-05 (or any subsequent level) on all Android devices. Defense-in-depth: rely on the Scudo allocator hardening that caught the issue before public release; avoid parsing untrusted AVIF content from untrusted sources. Upstream CrabbyAVIF fixes: https://android.googlesource.com/platform/external/rust/crabbyavif/+/9bcc1a311114ab844b417d3cdec50dcedfd0603f and https://android.googlesource.com/platform/external/rust/crabbyavif/+/42feb427a42afd9eebe6391a0d8a7b083fe82140.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is an attack in which adversaries embed malicious instructions within external content (emails, documents, calendar invites, web pages) that an LLM later ingests. Unlike direct prompt injection (where an attacker types malicious commands into the prompt), indirect injection rides on data the model retrieves or is supplied. When the model obeys the embedded instructions, it can be coerced into rogue actions such as exfiltrating user data, performing unauthorized tool operations, or generating attacker-controlled outputs. The post cites the industry-wide 'EchoLeak' 0-click data-exfiltration pattern (CVE-2025-32711) as a real-world illustration — though Google notes EchoLeak is a Microsoft 365 Copilot issue, not a Gemini one. Google characterises the threat as emerging and growing as agents gain more tools and external-data access.
- **Affected Products:** Gemini app, Gemini in Google Workspace, Gemini 2.5 models. No specific version numbers are identified in the advisory. (The post also references CVE-2025-32711 'EchoLeak' as an illustrative example — applicable to Microsoft 365 Copilot, NOT Gemini.)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true. Public PoCs/weaponized exploits exist for the broader prompt-injection class (e.g., EchoLeak/CVE-2025-32711 for Microsoft 365 Copilot - https://nvd.nist.gov/vuln/detail/cve-2025-32711; Gemini CLI injection flaws disclosed by Cyera - https://www.cyera.com/research/cyera-research-labs-discloses-command-prompt-injection-vulnerabilities-in-gemini-cli). The Google blog itself does not identify a specific PoC for the layered-defense scenario against Gemini.
- **Patch Available:** true — Google states the layered defenses (model hardening, ML classifiers, security thought reinforcement, markdown/URL sanitization, HITL confirmation, end-user notifications) are deployed/being continuously rolled out across Gemini products. There is no discrete vendor patch advisory for prompt injection as a class; the relevant Google resource is the advisory itself: http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html. (Separate specific Gemini CLI flaws disclosed by Cyera in Nov 2025 were addressed through separate updates.)
- **Active Exploitation:** true. Indirect prompt injection against AI agents has been confirmed in the wild by multiple parties: (a) Palo Alto Unit 42 (Mar 2026) — documented web-based indirect prompt injection attacks against LLM agents - https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/; (b) Google Threat Intelligence Group (May 2026) — continued maturation of adversaries leveraging AI for vulnerability exploitation and initial access - https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access; (c) Aim Security (Jun 2025) / CVE-2025-32711 'EchoLeak' — confirmed 0-click prompt-injection against Microsoft 365 Copilot - https://nvd.nist.gov/vuln/detail/cve-2025-32711; (d) Cyera Research Labs (Nov 2025) — disclosed command/prompt injection flaws in Google Gemini CLI - https://www.cyera.com/research/cyera-research-labs-discloses-command-prompt-injection-vulnerabilities-in-gemini-cli. Specific in-the-wild campaign attribution for Gemini-in-Workspace indirect prompt injection is not provided in the advisory.
- **Threat Actors:** None known for this advisory specifically. The post references generic 'adversaries' exploiting indirect prompt injection. Broader Google Threat Intelligence Group reporting (Feb/May 2026) notes nation-state and financially motivated actors leveraging AI for vulnerability exploitation and initial access, but does not attribute a specific group to this advisory.
- **Mitigation:** Google describes a layered defense strategy applied across the prompt lifecycle: (1) Model hardening — adversarial training data integrated into Gemini 2.5 model training to make the model itself more resistant; (2) Prompt-injection content classifiers — proprietary ML models that scan inbound content (emails, files) and flag/drop suspected malicious instructions before they reach the LLM; (3) Security thought reinforcement — targeted system-level instructions surrounding the user prompt that explicitly remind the LLM to perform the user's actual task and ignore adversarial instructions; (4) Markdown & URL sanitization — processing of model output to identify external image references, plus suspicious-URL detection backed by Google Safe Browsing, with redaction of unsafe links; (5) Human-in-the-Loop (HITL) user confirmation — requires explicit user confirmation before sensitive actions (e.g., deleting a calendar event); (6) End-user security mitigation notifications — providing contextual information and dedicated help-center articles when a defense neutralises an attempted attack. Practical customer/developer guidance: avoid giving agents unrestricted tool/data access, prefer well-scoped tool designs, layer untrusted-content filtering, require user confirmation for high-impact actions, and follow OWASP LLM01:2025 mitigations.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Long-running PRC state-sponsored espionage campaign targeting telecom backbone, provider-edge, and customer-edge routers. Initial access exploits known n-day CVEs: (1) CVE-2023-20198 (Cisco IOS XE Web UI auth bypass, CVSS 10.0) creates privilege-15 local user, then CVE-2023-20273 (Cisco IOS XE post-auth command injection, CVSS 7.2) executes commands as root; (2) CVE-2018-0171 (Smart Install, CVSS 9.8) provides unauth RCE on enabled devices; (3) CVE-2024-3400 (Palo Alto GlobalProtect, CVSS 10.0) creates arbitrary files escalating to unauth OS command injection; (4) Ivanti Connect/Policy Secure hit via CVE-2023-46805 auth bypass chained with CVE-2024-21887 (CVSS 9.1) command injection. Post-exploitation abuses Cisco IOS XE/NX-OS GuestShell container to run Linux utilities (including custom 'JumbledPath' traffic-obfuscation tool through non-public infrastructure). Persistence: enabling sshd_operns on TCP/57722, creating local accounts (e.g., 'cisco'), granting passwordless sudo, enabling SPAN/RSPAN/ERSPAN, adding GRE/IPsec tunnels and static routes, modifying ACLs (notably 'access-list 20') to whitelist actor IPs, and altering TACACS+/RADIUS pointers for credential capture. No zero-days observed — all CVEs in Appendix B were previously disclosed.
- **Affected Products:** Cisco IOS and IOS XE Software with Smart Install enabled (CVE-2018-0171); Cisco IOS XE Software Web UI feature (CVE-2023-20198, CVE-2023-20273); Palo Alto Networks PAN-OS 10.2, 11.0, and 11.1 with GlobalProtect feature enabled (CVE-2024-3400); Ivanti Connect Secure 9.x and 22.x, and Ivanti Policy Secure 9.x and 22.x (CVE-2024-21887 chained with CVE-2023-46805); Cisco IOS XE and NX-OS devices running the GuestShell containerized Linux environment used as a post-exploitation persistence channel.
- **CVSS Score:** 10.0 (CVE-2023-20198, the highest-impact Appendix-B CVE — Cisco IOS XE Web UI remote unauthenticated privilege management). Other scores: CVE-2024-3400 = 10.0, CVE-2018-0171 = 9.8, CVE-2024-21887 = 9.1, CVE-2023-20273 = 7.2.
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H (CVE-2023-20198, highest impact). Other CVE vectors: CVE-2018-0171 — CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H; CVE-2023-20273 — CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H; CVE-2024-21887 — CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H; CVE-2024-3400 — CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H.
- **Exploit Available:** true — Public PoCs and weaponized exploits exist for all CVEs. CVE-2024-21887 PoC: https://packetstormsecurity.com/files/176668/Ivanti-Connect-Secure-Unauthenticated-Remote-Code-Execution.html; CVE-2024-3400: https://unit42.paloaltonetworks.com/cve-2024-3400/ and https://www.volexity.com/blog/2024/04/12/zero-day-exploitation-of-unauthenticated-remote-code-execution-vulnerability-in-globalprotect-cve-2024-3400/; CVE-2023-20198/CVE-2023-20273: https://horizon3.ai/attack-research/attack-blogs/cisco-ios-xe-cve-2023-20198-theory-crafting/; CVE-2018-0171 long-publicly weaponized.
- **Patch Available:** true — Patches released for all exploited CVEs. Cisco cisco-sa-20180328-smi2 (CVE-2018-0171); Cisco cisco-sa-iosxe-webui-privesc-j22SaA4z (CVE-2023-20198 / CVE-2023-20273); Palo Alto Networks https://security.paloaltonetworks.com/CVE-2024-3400; Ivanti https://hub.ivanti.com/s/article/KB-CVE-2023-46805-Authentication-Bypass-CVE-2024-21887-Command-Injection-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure-Gateways.
- **Active Exploitation:** true — CISA AA25-239A explicitly attributes ongoing in-the-wild exploitation of all five Appendix-B CVEs to PRC state-sponsored actors as of the September 3, 2025 publication. Cisco confirmed exploitation of CVE-2023-20198/20273 in October 2023; Palo Alto Networks and Volexity documented active exploitation of CVE-2024-3400 as a zero-day in April 2024; Singapore CSA Alert AL-2025-083 confirms continued exploitation of CVE-2018-0171 against telecom-provider edge devices (August 21, 2025). Salt Typhoon-linked activity exploiting Cisco IOS XE via GuestShell observed through 2025. No exploitation of zero-day vulnerabilities has been observed.
- **Threat Actors:** PRC state-sponsored APT groups named in CISA AA25-239A Appendix A: Salt Typhoon (also tracked as FamousSparrow/ESET, Earth Estries/Trend Micro, UNC2286, and overalapping with GhostEmperor/Kaspersky), OPERATOR PANDA, RedMike, UNC5807, and GhostEmperor. Supplementary referenced actors include APT40 (Kryptonite Panda) and Volt Typhoon.
- **Mitigation:** (1) Patch the five listed CVEs as highest priority: CVE-2024-21887 (Ivanti), CVE-2024-3400 (Palo Alto GlobalProtect), CVE-2023-20198, CVE-2023-20273, and CVE-2018-0171. (2) Disable Cisco Smart Install and the Guest Shell container where not operationally required (verify with 'show guestshell' on NX-OS and 'show app-hosting detail' on IOS XE). (3) Enforce encrypted management: SNMPv3 with authentication/privacy, no default community strings, disable Telnet and unencrypted HTTP on edge devices. (4) Audit baseline running configurations against authorized baselines; validate ACLs, remote-access configs, routing tables, and TACACS+/RADIUS server addresses for unauthorized additions. (5) Hunt for known IOCs from Appendix C — modified ACLs (e.g., 'access-list 20' additions of 167.88.173[.]252, 193.239.86[.]132, 45.61.165[.]157), new GRE/IPsec tunnels terminating on foreign infrastructure, enabled sshd_operns on TCP/57722, SPAN/RSPAN/ERSPAN sessions, new local accounts, and outbound traffic to known APT infrastructure. (6) Validate firmware and image hashes against vendor-provided values; enable signed-image enforcement. (7) Centralize AAA logging, enable syslog + off-box telemetry, enforce robust change-management with periodic configuration audits. (8) Replace unsupported end-of-life network devices.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Unit 26165 conducts a multi-stage campaign against Western logistics, transport, and IT firms supporting aid to Ukraine. Initial access via spearphishing (malicious attachments, spoofed login pages, PowerShell via clipboard), credential brute-forcing/password spraying through rotating IPs/TLS-encrypted channels, and exploitation of public vulnerabilities in internet-facing infrastructure (corporate VPNs, Roundcube webmail, Microsoft Outlook via CVE-2023-23397, WinRAR via CVE-2023-38831). Persistence via scheduled tasks, Run keys, and malicious shortcuts in startup folders; lateral movement using Impacket, PsExec, RDP, and EWS mailbox queries; exfiltration via .zip archives and OpenSSH binaries; MFA/CAPTCHA bypass via stolen cookies. Mailbox credential harvesting and Microsoft Exchange mailbox permission modification. ICS reconnaissance (railway management), trust-relationship exploitation for pivot to secondary targets, and living-off-the-land using ntdsutil, wevtutil, vssadmin, PSExec. Custom malware: HEADLACE, MASEPIE, OCEANMAP, STEELHOOK; METASPLOIT use documented. Internet-connected IP cameras at border crossings compromised via RTSP DESCRIBE requests using default/brute-forced credentials.
- **Affected Products:** Microsoft Outlook (CVE-2023-23397), RARLAB WinRAR before 6.23 (CVE-2023-38831), Roundcube Webmail before 1.4.12 / 1.3.17 (CVE-2021-44026), Roundcube Webmail before 1.4.10 / 1.3.16 / 1.2.13 (CVE-2020-35730), Roundcube Webmail (CVE-2020-12641), Internet-exposed corporate VPNs and SOHO devices, Internet-connected IP cameras/DVRs at border crossings.
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H (for CVE-2023-23397, the highest-severity exploited CVE in this campaign). Note: AA25-141A covers multiple CVEs of varying severity (Outlook 9.8, WinRAR 7.8, Roundcube lower).
- **Exploit Available:** true — Public PoCs and weaponized exploits exist for CVE-2023-23397, CVE-2023-38831, and the Roundcube CVEs referenced in this campaign.
- **Patch Available:** true — Patches exist for all CVEs referenced in the advisory: CVE-2023-23397 (Microsoft March 2023 Patch Tuesday), CVE-2023-38831 (WinRAR 6.23), CVE-2021-44026 / CVE-2020-35730 / CVE-2020-12641 (Roundcube Webmail patches in versions 1.3.17+, 1.4.10+/1.4.12+).
- **Active Exploitation:** true — Confirmed active exploitation in the wild by Unit 26165 / APT28 since 2022, targeting Western logistics entities and technology companies supporting aid to Ukraine. The campaign involves credential spraying, spearphishing, exploitation of multiple CVEs, and long-term espionage/data theft.
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS), military unit 26165. Industry-tracked aliases: APT28, Fancy Bear, Forest Blizzard, BlueDelta, UAC-0001.
- **Mitigation:** 1. Patch all internet-facing systems (Outlook, WinRAR ≥6.23, Roundcube ≥1.4.12, VPNs, firmware). 2. Adopt Zero Trust principles; segment networks. 3. Enable phishing-resistant MFA; avoid storing passwords in GPP; enforce account throttling/lockouts. 4. Deploy EDR with priority on mail servers and domain controllers. 5. Enable Windows ASR rules to block executable content from email and execution from globally writeable directories; restrict PowerShell/JavaScript/batch. 6. Block/alert on NTLM/SMB to external infrastructure. 7. For IP cameras: patch firmware, replace unsupported devices, disable UPnP/P2P/Anonymous Visit, use allowlisted firewalls, require authenticated RTSP. 8. Restrict personal accounts in official communications; restrict file-hosting/API-mocking platforms. 9. Audit logs for anomalous requests, mailbox-permission changes, credential-spray patterns.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 11. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 12. 🟠 Zero-Day — New BioShocking attack manipulates AI browser into data theft

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://www.bleepingcomputer.com/news/security/new-bioshocking-attack-manipulates-ai-browser-into-data-theft/>

> A new prompt injection attack dubbed &quot;BioShocking&quot; could trick AI-powered browsers into treating real-world risky actions as part of a fictional scenario, causing them to ignore any safety guardrails. [...]

---

## 13. 🟠 Zero-Day — oban_web missing authorization check on `save-job` event handler

**CVE:** `CVE-2026-48592` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-389x-rgxr-8m33>

> ### Summary

`oban_web` 2.12.0 through the current unpatched release exposes a `save-job` LiveView event handler that performs no authorization check, allowing any authenticated user (including those with `:read_only` access) to overwrite a queued job&#x27;s `worker` field with any other `Oban.Worker` module present in the application. On the job&#x27;s next execution attempt, Oban dispatches `per…

---

## 14. 🟠 Zero-Day — Fake Perplexity extension on Chrome Web Store tracked searches

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://www.bleepingcomputer.com/news/security/fake-perplexity-extension-on-chrome-web-store-tracked-searches/>

> A malicious extension in the Chrome Web Store is masquerading as the Perplexity AI answer engine, intercepting search traffic and collecting browsing information. [...]

---

## 15. 🟠 Zero-Day — BlueHammer Vulnerability Exploited in Ransomware Attacks

**CVE:** `CVE-2026-33825` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://www.securityweek.com/bluehammer-vulnerability-exploited-in-ransomware-attacks/>

> The Microsoft Defender vulnerability CVE-2026-33825 was exploited in the wild as a zero-day before patches were released. The post BlueHammer Vulnerability Exploited in Ransomware Attacks appeared first on SecurityWeek .

---

## 16. 🟡 High Severity — Twig: Sandbox `__toString()` policy bypass via `Traversable` in `join` and `replace` filters

**CVE:** `CVE-2026-48807` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-8x9c-rmqh-456c>

> ### Description

This is a residual bypass of CVE-2026-47732 / GHSA-pr2w-4gpj-cpq4 left after the initial fix for unguarded `__toString()` calls. It covers two related coercion points that were not caught by the original patch.

**`Traversable` in `join` and `replace` filters.** `SandboxExtension::ensureToStringAllowed()` recurses into PHP arrays so that a `Stringable` object hidden inside an arra…

---

## 17. 🟡 High Severity — Fulcio has OIDC Discovery Redirect Following Allows SSRF and JWKS Substitution for Meta-Issuer Paths, with Kubernetes Service-Account Token Leakage

**CVE:** `CVE-2026-49478` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-f5mr-q85p-6hh6>

> ## Impact

Three security vulnerabilities were identified in the OIDC Discovery client:

1. **Blind Server-Side Request Forgery (SSRF) via Cross-Host Redirects**:
   Fulcio uses an HTTP client to fetch OIDC discovery metadata (`/.well-known/openid-configuration`). Prior to this fix, if a configured issuer returned an HTTP redirect to a different host, the client followed it by default. This allowe…

---

## 18. 🟡 High Severity — CefSharp.Common: `FolderSchemeHandlerFactory` path boundary check can expose files outside the configured root folder

**CVE:** `CVE-2026-48796` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-85jm-cwp2-mvpv>

> ### Summary

`FolderSchemeHandlerFactory` was intended to restrict served files to a configured `rootFolder`, but its path validation used a raw string prefix check. A request could escape to a sibling directory whose full path starts with the root folder path, allowing files outside the configured root to be served.

### Details

In affected versions, `FolderSchemeHandlerFactory` canonicalized `r…

---

## 19. 🟡 High Severity — @adonisjs/bodyparser has an incomplete fix for CVE-2026-25754

**CVE:** `CVE-2026-48795` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-qcm7-3vpr-hj5h>

> ### Summary

The fix for [GHSA-f5x2-vj4h-vg4c](https://github.com/adonisjs/core/security/advisories/GHSA-f5x2-vj4h-vg4c) / CVE-2026-25754 introduced in commit [`40e1c71`](https://github.com/adonisjs/bodyparser/commit/40e1c71f958cffb74f6b91bed6630dca979062ed) is incomplete and can be bypassed through nested prototype pollution payloads.

The original patch replaced the internal `FormFields` storage…

---

## 20. 🟡 High Severity — Probo has an open redirect bypass via path normalization

**CVE:** `CVE-2026-49820` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-x7qq-m748-8p2c>

> ### Impact
Probo&#x27;s `saferedirect` package validates redirect URLs used across authentication flows (OIDC, SAML, session transfer, OAuth connectors, and trust-center magic links). The validator only inspected the second character of relative paths, so a URL like `/../\evil.com` passed validation because the second character is `.`. Go&#x27;s `http.Redirect` normalizes this path to `/\evil.com`…

---

## 21. 🟡 High Severity — Fission builder pods auto-mount the fission-builder ServiceAccount token in the user-supplied builder container

**CVE:** `CVE-2026-50565` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-8wcj-mfrc-jx5q>

> ### Summary

Fission builder pods were created with `ServiceAccountName: fission-builder` and no `AutomountServiceAccountToken: false`, so the kubelet auto-mounted the service-account token into every container in the pod — including the
user-supplied builder image.

### Details

The user controls the builder container image, command, and podspec through `Environment.spec.builder.image` / `.contai…

---

## 22. 🟡 High Severity — Fission Environment CRD podspec passthrough enables hostPID/hostNetwork/privileged pods, node escape

**CVE:** `CVE-2026-50564` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-gx55-f84r-v3r7>

> ### Summary

Fission&#x27;s `Environment` CRD exposes `spec.runtime.podSpec` and `spec.builder.podSpec`, which are merged into the Kubernetes pod specs for runtime and builder pods. The merge logic propagated `hostNetwork`, `hostPID`, `hostIPC`, container
 `privileged`, and `serviceAccountName` from the user-supplied podspec with no filtering, and `Environment.Validate` performed no security-relev…

---

## 23. 🟡 High Severity — Fission Container Executor Function PodSpec Injection Leading to Node Escape

**CVE:** `CVE-2026-50563` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-v455-mv2v-5g92>

> ### Summary

Fission&#x27;s Container Executor path lets a tenant supply `Function.spec.podspec` directly; the executor merges it into the executor-built podspec and creates a Deployment whose pods run the user&#x27;s container image.

### Details

Two flaws compounded:

1. `pkg/apis/core/v1/validation.go::FunctionSpec.Validate` only checked that `spec.PodSpec != nil` when `executorType: container…

---

## 24. 🟡 High Severity — Fission Environment CRD PodSpec Injection Leading to Node Escape and Cluster Takeover

**CVE:** `CVE-2026-50545` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-wmgg-3p4h-48x7>

> ### Summary

A stronger framing of the same root cause as GHSA-gx55-f84r-v3r7: the `Environment.spec.runtime.podSpec` / `spec.builder.podSpec` passthrough lacked validation, and `MergePodSpec` propagated dangerous fields into the generated pods.

### Details

Three independent flaws compounded:

1. **Validate gap.** `pkg/apis/core/v1/validation.go::Environment.Validate` checked only container nami…

---

## 25. 🟡 High Severity — Fission: Cross-namespace Environment reference via unvalidated EnvironmentRef in Function admission webhook

**CVE:** `CVE-2026-49824` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-cvw6-gfvv-953q>

> ### Summary

The Fission Function admission webhook (`pkg/webhook/function.go`) validated that `spec.secrets[].namespace` and `spec.configmaps[].namespace` equalled the function&#x27;s own namespace but performed no equivalent check on
`spec.environment.namespace`.

### Details

An attacker with permission to create Functions in their own namespace could set `spec.environment.namespace` to any oth…

---

## 26. 🟡 High Severity — Fission: Cross-namespace Package read via unvalidated PackageRef in Function admission webhook

**CVE:** `CVE-2026-49823` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-3r8v-2xmj-5c39>

> ### Summary

A Fission Function spec carries three reference types — Secret, ConfigMap, and Package. The first two were namespace-validated by the admission webhook; `PackageRef.Namespace` was not.

### Details

A tenant with `functions.fission.io/create` in their own namespace could set `spec.package.packageref.namespace` to any other namespace. When the function is invoked, the fetcher sidecar r…

---

## 27. 🟡 High Severity — Fission: Cross-namespace event leakage via KubernetesWatchTrigger allows persistent tenant surveillance

**CVE:** `CVE-2026-49822` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-gc3j-79f2-7vvw>

> ### Summary

A low-privilege developer who could create a `KubernetesWatchTrigger` (KWT) in their own namespace was able to establish a persistent surveillance channel over any other namespace.

### Details

Two independent flaws compounded:

1. `pkg/kubewatcher/kubewatcher.go::createKubernetesWatch` used `w.Spec.Namespace` (user-controlled) directly as the Watch target without checking it against…

---

## 28. 🟡 High Severity — Fission: Cross-namespace Environment reference in Package allows build-time command execution and SA token exfiltration

**CVE:** `CVE-2026-49821` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-vjhc-cf4p-72q4>

> ### Summary

Fission&#x27;s `buildermgr` controller processed `Package` CRDs without verifying that `Package.spec.environment.namespace` matched `Package.metadata.namespace`.

### Details

An attacker with `packages.fission.io/create` in their own namespace could set `spec.environment.namespace` to any other tenant&#x27;s namespace. The controller then used its high-privilege service account to fe…

---

## 29. 🟡 High Severity — RabbitMQ has predictable credential obfuscation seed value used in Shovel and Federation plugins

**CVE:** `CVE-2022-31008` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-v9gv-xp36-jgj8>

> ### Impact

Shovel and Federation plugins perform URI obfuscation in their worker (link) state. The encryption key used to encrypt
the URI was seeded with a predictable secret.

This means that in case of certain exceptions related to Shovel and Federation plugins,
reasonably easily deobfuscatable data could appear in the node log.

Patched versions correctly use a cluster-wide secret for that pur…

---

## 30. 🟡 High Severity — Microsoft.OpenAPI: Circular schema references may terminate OpenAPI parsing

**CVE:** `CVE-2026-49451` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-v5pm-xwqc-g5wc>

> ### Impact

A small OpenAPI document containing a circular schema reference can cause process termination through stack overflow in Microsoft.OpenApi. The issue affects OpenAPI document parsing through public OpenAPI.NET reader APIs and has been confirmed across both JSON and YAML reader paths.

## Affected versions

- `&gt;= 2.0.0-preview11, &lt;= 2.7.4`
- `&gt;= 3.0.0, &lt;= 3.5.3`

### Patches
…

---

## 31. 🟡 High Severity — Langflow RCE Exploited to Deploy Monero Miner on Exposed AI App Endpoints

**CVE:** `CVE-2026-33017` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://thehackernews.com/2026/06/langflow-rce-exploited-to-deploy-monero.html>

> Threat actors are continuing to exploit a critical Langflow vulnerability as part of fresh attacks designed to deliver a Monero cryptocurrency miner.

The activity has been found to weaponize CVE-2026-33017 (CVSS score: 9.3), an unauthenticated remote code execution (RCE) vulnerability in Langflow, indicating threat actors are scanning and targeting exposed artificial intelligence (AI)

---

## 32. 🟡 High Severity — Attackers Exploit SimpleHelp CVE-2026-48558 to Deploy TaskWeaver and Djinn Stealer

**CVE:** `CVE-2026-48558` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://thehackernews.com/2026/06/attackers-exploit-simplehelp-cve-2026.html>

> An unknown threat actor has been observed exploiting a recently disclosed maximum-severity security flaw in SimpleHelp to deliver two previously unreported malware families, TaskWeaver and Djinn Stealer.

The intrusion involves the exploitation of CVE-2026-48558 (CVSS score: 10.0), a critical authentication bypass vulnerability impacting the OpenID Connect (OIDC) flow that an unauthenticated

---

## 33. 🟡 High Severity — Progress Kemp LoadMaster Flaw Could Let Attackers Run Root Commands Pre-Auth

**CVE:** `CVE-2026-8037` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://thehackernews.com/2026/06/progress-kemp-loadmaster-flaw-could-let.html>

> A critical vulnerability in Progress Kemp LoadMaster can let an unauthenticated attacker execute arbitrary commands as root on the appliance by sending a crafted request to its API.

The flaw, tracked as CVE-2026-8037, carries a CVSS score of 9.8 according to ZDI. A patch is available. If you run LoadMaster with the API enabled, update now.

Progress published its advisory on June

---

## 34. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
