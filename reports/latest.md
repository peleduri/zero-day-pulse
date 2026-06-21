# Zero Day Pulse

> **Generated:** 2026-06-21 09:34 UTC &nbsp;|&nbsp; **Total:** 14 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 9 &nbsp;|&nbsp; 🟡 High: 5 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is an unauthenticated path-traversal vulnerability in SimpleHelp's '/toolbox-resource' endpoint. Crafted HTTP requests using traversal sequences (e.g., '../../../../../../etc/passwd') allow remote, unauthenticated attackers to download arbitrary files from the SimpleHelp host. Sensitive files obtainable include serverconfig.xml (which contains hashed administrator credentials, LDAP credentials, OIDC client tokens, and TOTP seeds), /etc/passwd, and SSH keys such as /root/.ssh/id_rsa, enabling lateral movement and further compromise. CVE-2024-57727 is part of a January 2025 cluster with two related flaws: CVE-2024-57726 (missing authorization on admin API functions, CVSS 9.9) and CVE-2024-57728 (authenticated arbitrary-file-write / zip-slip, CVSS 7.2) — these were reportedly chained in observed attacks.
- **Affected Products:** SimpleHelp Remote Support / Remote Monitoring and Management (RMM) software, versions 5.5.7 and earlier (patched in 5.5.8; 5.5.15 or later recommended as a hardened release).
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true — A public Metasploit auxiliary module is available at https://www.rapid7.com/db/modules/auxiliary/scanner/http/simplehelp_toolbox_path_traversal/ (disclosed January 12, 2025; authored by horizon3ai / imjdl / jheysel-r7).
- **Patch Available:** true — Patched in SimpleHelp 5.5.8 (released January 2025, within two days of report). Vendor advisory: https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know (later hardened releases such as 5.5.15 are recommended).
- **Active Exploitation:** true — Confirmed by CISA Advisory AA25-163A (published June 12, 2025): DragonForce ransomware actors exploited an unpatched, internet-exposed SimpleHelp RMM instance at a utility billing software provider to move laterally to downstream utility customers, deploying ransomware via suspicious three-letter-name executables since at least January 2025. CVE-2024-57727 was the initial-access vehicle.
- **Threat Actors:** DragonForce ransomware actors. Per CISA Advisory AA25-163A, DragonForce has exploited unpatched SimpleHelp RMM instances (leveraging CVE-2024-57727) since January 2025 to compromise a utility billing software provider and downstream utility customers, deploying ransomware.
- **Mitigation:** 1) Immediately upgrade SimpleHelp servers to version 5.5.8 or later (5.5.15 recommended as a hardened release). 2) If unable to patch immediately, isolate the SimpleHelp server from the internet or stop the server process. 3) Apply the SimpleHelp server.xml hardening (the post-patch fix scrubs credentials from serverconfig.xml). 4) Verify and update all deployed Remote Access Services / technicians. 5) Hunt on SimpleHelp hosts and downstream customer endpoints for suspicious executables with three-alphabetic-letter filenames (e.g., aaa.exe, bbb.exe) created after January 2025. 6) Disconnect and reimage any compromised systems using clean installation media and restore data from clean, offline backups. 7) Conduct third-party RMM risk analysis and require vendors to disclose their security controls. 8) Do not expose RMM/RDP services directly to the internet without compensating controls; add SimpleHelp binaries to endpoint security allowlists.
- **Vendor Advisory:** https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) – attackers seed malicious instructions/payloads into public web content or hidden site code that AI agents consume (via browsing, RAG, or multi‑source ingestion). When agents incorporate that content into prompts or system context, the injected instructions can override or influence the agent, causing data exfiltration, unauthorized actions, or corrupted outputs.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Harden ingestion and retrieval: validate and sanitize external content, implement strict input/output filtering, source reputation controls, prompt integrity checks, human-in-the-loop for risky actions, reduce agent privilege, use content allowlists, and monitoring/telemetry for IPI indicators. Follow vendor guidance in the Google Security Blog advisory.
- **Vendor Advisory:** https://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an attack technique where an adversary embeds malicious instructions inside untrusted external data sources (web pages, emails, shared documents, calendar invitations, Drive files) that an LLM (here, Gemini) processes as context when serving a user query or executing an agentic workflow. Because Gemini and similar LLMs cannot reliably distinguish data from instructions once content enters their prompt/prompt-context, the hidden instructions can hijack the model's behavior. Demonstrated impacts against Workspace/Gemini include: (1) causing the model to scan Workspace content for sensitive terms (email correspondence, financial data, contracts, calendar details), and (2) exfiltrating matched content to attacker-controlled destinations through injected URLs that the LLM safely resolves. The technique can be zero-click (e.g., GeminiJack — victim only needs to receive a malicious email/calendar invite/shared doc).
- **Affected Products:** Google Workspace with Gemini (Gmail, Docs editors, Drive, Chat), the Gemini app, Google Gemini Enterprise, and Vertex AI Search. No specific model or platform version numbers were publicly disclosed by Google.
- **CVSS Score:** CVSS score unavailable. No CVSS v3.x base score has been publicly disclosed for indirect prompt injection in Google Workspace/Gemini.
- **CVSS Vector:** CVSS vector unavailable. No CVSS v3 vector string has been publicly assigned or disclosed for indirect prompt injection in Google Workspace with Gemini.
- **Exploit Available:** true — Two categories of public exploits/PoCs exist: (1) Noma Labs published a proof-of-concept for 'GeminiJack,' a zero-click IPI vulnerability in Google Gemini Enterprise / Vertex AI Search (https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/, December 8, 2025); and (2) Forcepoint X-Labs documented 10 verified IPI payloads recovered from live public websites (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads, April 22, 2026).
- **Patch Available:** true (partial/continuous) — For the specific GeminiJack vulnerability (IPI in Gemini Enterprise/Vertex AI Search), Google deployed updates to the RAG processing pipeline and fully separated Vertex AI Search from Gemini Enterprise (confirmed by Noma Labs and Infosecurity Magazine, December 2025; https://www.infosecurity-magazine.com/news/google-fixes-gemini-enterprise-flaw/). For broader Workspace IPI, Google treats mitigation as a continuous process rather than a single patch and ships ongoing model and policy updates via the vendor advisory at https://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html.
- **Active Exploitation:** true — Confirmed in-the-wild exploitation: (1) Forcepoint X-Labs reported 10 verified indirect prompt injection payloads on live public websites spanning financial fraud, data destruction, API-key exfiltration, AI denial-of-service, traffic/SEO manipulation, and output hijacking (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads, April 22, 2026); (2) Help Net Security (April 24, 2026) reported a 32% relative increase in malicious IPI activity between November 2025 and February 2026; (3) Google has stated that IPI is an 'evolving threat vector' and 'anticipating top priority' for the security community.
- **Threat Actors:** None known. No specific APT groups, ransomware operators, or named threat actor campaigns have been publicly attributed to IPI exploits against Google Workspace with Gemini. Forcepoint noted shared payload templates suggesting 'organized tooling,' and one Lyrie analysis referenced a handle 'Kirill Bobrov' appearing in attribution-hijacking payloads, but no formal threat actor attribution has been published.
- **Mitigation:** Google describes a continuous, multi-layered, defense-in-depth strategy rather than a single fix, including: (1) IPI content classifiers on Gemini inputs; (2) 'security thought reinforcement' — prompt-level instructions hardening the model against injected directives; (3) markdown sanitization and suspicious URL redaction of model outputs/inputs; (4) a user confirmation framework requiring explicit user approval for sensitive or irreversible actions; (5) end-user security mitigation notifications when IPI attempts are detected; (6) continuous model resilience training via synthetic attack variants generated by Google's 'Simula' framework; (7) centralized Policy Engine enforcing tool chaining, URL sanitization, and human-in-the-loop gating; (8) discovery feedback loops via human/automated red-teaming and the AI Vulnerability Rewards Program (VRP).
- **Vendor Advisory:** https://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection against agentic browsing: malicious sites embed crafted prompts that influence the AI agent to execute unsafe actions or leak local data. The attack chain can be combined with other flaws (e.g., CVE‑2026‑0628) to achieve local file access and privacy invasion.
- **Affected Products:** Google Chrome (Gemini / agentic browsing components)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply the latest Chrome updates that contain the patch; enable Chrome’s layered defenses that restrict origin access, block prompt injections, and enforce supervisory AI oversight; follow the security guidance in the vendor advisory.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** An integer overflow allows arbitrary code execution, resulting in local escalation of privilege on Android devices.
- **Affected Products:** Android 14, Android 15, Android 16, Android 16 QPR2
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (https://www.helpnetsecurity.com/2026/06/02/android-vulnerability-exploited-cve-2025-48595/)
- **Patch Available:** true (https://source.android.com/docs/security/bulletin/2026/2026-06-01)
- **Active Exploitation:** true (https://www.helpnetsecurity.com/2026/06/02/android-vulnerability-exploited-cve-2025-48595/)
- **Threat Actors:** None known
- **Mitigation:** Install the June 2026 Android security update (patch) provided in the official bulletin.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2026/2026-06-01

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is an OS command injection in the MobileIron Configuration Service (MICS) web portal interface of Ivanti Sentry, allowing an attacker to execute arbitrary operating‑system commands via crafted input.
- **Affected Products:** Ivanti Sentry (MobileIron Configuration Service) web portal
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (http://enigma-global.com/reports/cve-2026-10520-critical-ivanti-sentry-os-command-injection-actively-exploited-mqaltqap-twhb)
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** APT actors exploit publicly known CVEs and other avoidable weaknesses (T1190) in internet‑exposed edge and backbone routers, provider/customer edge devices, and management interfaces to gain initial access, then establish persistence via web UI, Tcl/Python scripts, and Guest Shell, perform lateral movement using SPAN/RSPAN/ERSPAN, and exfiltrate data. They create unauthorized admin accounts (e.g., via CVE‑2023‑20198), execute commands via SNMP/SSH, and use tooling such as siet.py, map.tcl, tclproxy.tcl.
- **Affected Products:** Cisco IOS/IOS XE (CVE-2023-20198, CVE-2023-20273, CVE-2018-0171), Ivanti Connect Secure/Policy (CVE-2024-21887), Fortinet, Juniper, Microsoft Exchange, Nokia routers/switches, Sierra Wireless, SonicWall
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon; OPERATOR PANDA; RedMike; UNC5807; GhostEmperor
- **Mitigation:** Prioritize patching of known exploited CVEs on edge/backbone devices; disable or unexpose management interfaces where possible; hunt for exploitation artifacts (e.g., double‑encoded WSMA paths, unauthorized admin accounts, Proxy‑Uri‑Source header); monitor for SNMP/SSH/Guest Shell activity and unusual high‑port HTTP servers; follow NSA/CISA/FBI guidance and MITRE D3FEND countermeasures as outlined in the advisory.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** The GRU unit 26165 weaponized CVE-2023-23397 to harvest NTLM hashes via Outlook, used Roundcube vulnerabilities (CVE-2020-12641, CVE-2020-35730) to run arbitrary shell commands, and exploited WinRAR CVE-2023-38831 to execute code from malicious archives. These exploits were combined with credential‑guessing, spear‑phishing, and VPN compromise to gain initial access to targeted logistics and technology firms.
- **Affected Products:** WinRAR (vulnerable to CVE-2023-38831), Roundcube (vulnerable to CVE-2020-12641, CVE-2020-35730), Outlook (vulnerable to CVE-2023-23397)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Russian GRU unit 26165 (85th GTsSS)
- **Mitigation:** Audit accounts, configure comprehensive logging, monitor for suspicious activity, apply general hardening measures, and implement IP camera mitigation guidance as outlined in the advisory.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Install the released updates via Windows Update or Microsoft Update Catalog.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide

---

## 10. 🟡 High Severity — SEC Consult SA-20260618-0 :: Hardcoded Root Cloud Credentials in Application Binaries in Silver Leaf Technologies - Worksnaps.net Worksnaps

**CVE:** `CVE-2025-10560` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-06-21
**Reference:** <https://seclists.org/fulldisclosure/2026/Jun/21>

> Posted by SEC Consult Vulnerability Lab via Fulldisclosure on Jun 20 SEC Consult Vulnerability Lab Security Advisory &lt; 20260618-0 &gt; ======================================================================= title: Hardcoded Root Cloud Credentials in Application Binaries product: Silver Leaf Technologies - Worksnaps.net Worksnaps vulnerable version: &lt; 1.6.20260201 fixed version: 1.6.20260201 …

**Parallel AI Enrichment:**

- **Technical Details:** Application binaries contained hardcoded cloud credentials (AWS access keys, S3 bucket names); credentials allowed enumeration and access to S3 buckets and AWS resources (e.g., aws s3api list-buckets, aws ec2 describe-instances) and showed account/root ARN.
- **Affected Products:** Worksnaps client <1.6.20260201 (Windows client versions 1.6.20250304, 1.6.20251206)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Install patched client 1.6.20260201 (vendor also implemented server‑side fixes); no workaround available.
- **Vendor Advisory:** https://sec-consult.com/vulnerability-lab/

---

## 11. 🟡 High Severity — SEC Consult SA-20260617-0 :: Multiple Critical Vulnerabilities in Sprecher Automation SPRECON-E-C/-E-P/-E-T3

**CVE:** `CVE-2022-4333` | `CVE-2022-4332` | `CVE-2025-41741` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-06-21
**Reference:** <https://seclists.org/fulldisclosure/2026/Jun/19>

> Posted by SEC Consult Vulnerability Lab via Fulldisclosure on Jun 20 SEC Consult Vulnerability Lab Security Advisory &lt; 20260617-0 &gt; ======================================================================= title: Multiple Critical Vulnerabilities product: Sprecher Automation SPRECON-E-C/-E-P/-E-T3 vulnerable version: See vulnerable versions below fixed version: See solution section below CVE n…

---

## 12. 🟡 High Severity — CVE-2025-68624: Cross-Tenant Authentication Bypass by Spoofing in N-able Mail Assure

**CVE:** `CVE-2025-68624` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-06-21
**Reference:** <https://seclists.org/fulldisclosure/2026/Jun/10>

> Posted by Alessandro Bertoldi BCS via Fulldisclosure on Jun 20 CVE-2025-68624: Cross-Tenant Authentication Bypass by Spoofing in N-able Mail Assure CVE ID: CVE-2025-68624 Status: DISPUTED CWE: CWE-290 (Authentication Bypass by Spoofing) Affected Product: N-able Mail Assure (formerly SolarWinds MSP Mail Assure) Affected Service: N-able Mail Assure cloud-based multi-tenant SMTP relay infrastructure …

---

## 13. 🟡 High Severity — Hackers Exploit Gravity SMTP WordPress Plugin Bug to Expose API Keys

**CVE:** `CVE-2026-4020` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-20
**Reference:** <https://thehackernews.com/2026/06/hackers-exploit-gravity-smtp-wordpress.html>

> Threat actors are exploiting a recently patched security flaw impacting Gravity SMTP, a WordPress plugin that&#x27;s installed on about 100,000 sites.

The vulnerability, tracked as CVE-2026-4020 (CVSS score: 5.3), is a medium-severity information disclosure flaw that can allow unauthenticated attackers to extract sensitive data, such as configuration data, API keys, secrets, and OAuth tokens

---

## 14. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
