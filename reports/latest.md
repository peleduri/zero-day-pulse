# Zero Day Pulse

> **Generated:** 2026-07-03 19:02 UTC &nbsp;|&nbsp; **Total:** 30 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 13 &nbsp;|&nbsp; 🟡 High: 17 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated path-traversal (directory traversal) in SimpleHelp v5.5.7 and earlier allows remote attackers to read sensitive files on the server by supplying crafted path inputs to vulnerable endpoints.
- **Affected Products:** SimpleHelp remote support / RMM v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (see vendor advisory https://guides.simple-help.com/kb---security-vulnerabilities-01-2025)
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply vendor updates/patches from SimpleHelp immediately; if patching is not immediately possible, isolate/unexpose affected SimpleHelp instances, restrict network access to the application (firewall/ACLs), rotate credentials stored on compromised systems, and monitor for suspicious access—follow CISA and vendor guidance for containment and remediation.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — Critical Cursor AI Code Editor Flaws Could Lead to OS-Level Remote Code Execution

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-03
**Reference:** <https://www.securityweek.com/critical-cursor-ai-ide-flaws-could-lead-to-os-level-remote-code-execution/>

> The DuneSlide vulnerabilities enable zero-click prompt injection attacks that escape Cursor&#x27;s sandbox and execute arbitrary code on the underlying operating system. The post Critical Cursor AI Code Editor Flaws Could Lead to OS-Level Remote Code Execution appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Two zero-click prompt-injection vulnerabilities (CVE-2026-50548 and CVE-2026-50549, collectively called DuneSlide) allow the Cursor AI agent to influence runtime parameters (notably working_directory) so that the IDE sandbox can include writable paths; this enables sandbox escape and arbitrary OS-level command execution. Fixed in Cursor 3.0.
- **Affected Products:** Cursor IDE (versions prior to 3.0; fixed in Cursor 3.0)
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true — fixed in Cursor 3.0 (see vendor security page: https://cursor.com/security)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Upgrade to Cursor 3.0. If immediate upgrade is not possible, disable or isolate AI agent features and run Cursor in a restricted environment (restrict writable paths) until patched.
- **Vendor Advisory:** https://cursor.com/security

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is a two-stage semantic attack: an adversary hides natural-language instructions inside ordinary web content or data sources; an AI agent ingests that external content and, treating it as input/context, follows the hidden instructions (exfiltrating data, performing unauthorized actions, or bypassing authorizations).
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — public PoCs / real-world demonstrations reported (examples: http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability, http://miggo.io/post/weaponizing-calendar-invites-a-semantic-attack-on-google-gemini)
- **Patch Available:** false
- **Active Exploitation:** true — confirmed in-the-wild IPI payloads and demonstrations reported (examples: http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability, http://miggo.io/post/weaponizing-calendar-invites-a-semantic-attack-on-google-gemini, Forcepoint/ImmersiveLabs writeups)
- **Threat Actors:** None known
- **Mitigation:** High-level mitigations reported: continuously monitor and sweep public web content for IPI patterns; sanitize or filter external text before feeding it to AI agents; restrict and harden external data sources and integrations; enforce strict instruction-following policies and agent boundaries; apply vendor fixes for specific CVEs when available.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when an attacker injects malicious instructions into external content or tools (web pages, files, tool outputs) that an LLM or agent ingests; when the model uses those data sources to answer queries or drive agentic steps, the injected instructions can influence the model’s behavior and outputs, potentially without direct user input.
- **Affected Products:** Google Workspace (with Gemini)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply a layered defense: monitor and sweep public web content for known IPI patterns, classify/sanitize or block untrusted external inputs before they influence prompts or agents, harden model/agent behavior (limit or sandbox agentic automation/tool execution on untrusted data), and follow vendor security guidance and updates.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Insufficient policy enforcement in the WebView/tag used by Chrome allowed attacker-controlled content (indirect prompt injection / 'GeminiJack' zero-click) to influence agent instructions; this can lead to script injection into privileged/agent contexts and exposure of data.
- **Affected Products:** Google Chrome (WebView) prior to 143.0.7499.192, Google Gemini Enterprise
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — proof-of-concept repositories published (example: https://github.com/fevar54/CVE-2026-0628-POC).
- **Patch Available:** true — Google published fixes/updates (see vendor advisory: https://blog.google/security/architecting-security-for-agentic/ and news coverage of the patch).
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses described by the vendor: restrict origin/access for agentic components, enforce stricter WebView/tag policies, and block untrusted content from being interpreted as agent instructions (see vendor blog and coverage).
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable. The blog post summarizes a memory-safety prevention strategy (Rust adoption) and high-level metrics but does not describe a single vulnerability’s exploitation chain or per-vulnerability technical attack vector.
- **Affected Products:** Android platform (AOSP and ecosystem) — first-party and third-party code; languages referenced: C, C++, Java, Kotlin, Rust; no specific OS versions listed
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true — Android Security Bulletins provide vendor fixes (example: https://source.android.com/docs/security/bulletin/2025-12-01).
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Adopt memory-safe languages (Rust) for new platform code, follow Android secure-review and patching practices, and apply vendor Android Security Bulletin updates promptly.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection embeds malicious instructions in external content (emails, documents, calendar invites, web pages, image metadata, hidden DOM elements, or encoded payloads like Base64/invisible characters). When an LLM processes that content as part of a benign user request, it executes the embedded instructions alongside the legitimate task. This enables data exfiltration (e.g., via rendered markdown image URLs in zero-click attacks), unauthorized tool calls, prompt leakage, denial-of-service, or manipulation of agentic actions. Unlike direct prompt injection, the attacker never touches the user's prompt—only the data the model reads.
- **Affected Products:** Google Gemini 2.5 family (Gemini app, Gemini in Google Workspace including Gmail, Docs editors, Drive, Chat). The broader vulnerability class also affects LLM-powered assistants, RAG applications, AI agents, and email/code assistants generally.
- **CVSS Score:** CVSS score unavailable. No CVE has been assigned to indirect prompt injection as it applies to Google Gemini.
- **CVSS Vector:** CVSS vector unavailable. No CVE has been assigned to indirect prompt injection as it applies to Google Gemini.
- **Exploit Available:** true - Public PoCs and weaponized exploits exist. Sources: https://github.com/Joe-B-Security/awesome-prompt-injection, https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/
- **Patch Available:** true - Google deployed layered defenses across Gemini 2.5 models in the Gemini app and Gemini in Workspace as of June 2025. Advisory: http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html
- **Active Exploitation:** true - Confirmed active exploitation in the wild. Palo Alto Unit 42 reports real-world web-based indirect prompt injection campaigns against AI agents including ad-review evasion, phishing SEO manipulation, data-destruction attempts, denial-of-service attacks, and unauthorized transaction redirection. CrowdStrike documents additional cases including job-applicant code hidden in image metadata and LinkedIn-bio prompt tricks targeting AI recruiters. Sources: https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/, https://www.crowdstrike.com/en-us/blog/indirect-prompt-injection-attacks-hidden-ai-risks/
- **Threat Actors:** None known. Sources describe the threat using generic terms ("attackers", "malicious actors", "adversaries") without attribution to specific APT groups, ransomware operators, or named campaigns.
- **Mitigation:** Google's layered defense strategy: (1) Prompt injection content classifiers (ML models to detect/filter malicious instructions in files, emails, web content before they reach the LLM); (2) Security thought reinforcement (system-prompt instructions telling the model to ignore adversarial content); (3) Markdown sanitization and suspicious URL redaction (strips external image rendering, uses Google Safe Browsing to mask risky links); (4) User confirmation framework (human-in-the-loop approval for risky actions); (5) End-user security mitigation notifications; (6) Model resilience/hardening (adversarial fine-tuning, automated red-teaming, Spotlighting/self-reflection). For admins: restrict Gemini to trusted data sources, enforce least-privilege tool access, monitor for shadow-AI use, and train users.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored APTs (Salt Typhoon/RedMike/UNC5807/GhostEmperor/OPERATOR PANDA) target internet-exposed network edge devices — large backbone routers of telecom providers, provider edge (PE) and customer edge (CE) routers, VPN gateways, and firewalls. Initial access is achieved by exploiting known n-day vulnerabilities in Ivanti Connect Secure/Ivanti Policy Secure (CVE-2024-21887, often chained with CVE-2023-46805), Palo Alto PAN-OS GlobalProtect (CVE-2024-3400), and Cisco IOS XE (CVE-2023-20198 to create unauthorized admin accounts, chained with CVE-2023-20273; plus CVE-2018-0171 Smart Install). After exploitation, attackers modify router configurations for persistence: adding ACLs to whitelist attacker IPs, configuring GRE/IPsec tunnels and static routes for traffic mirroring, opening non-standard high ports, configuring SSH backdoors, modifying TACACS+/RADIUS server pointers to harvest credentials, and creating privileged accounts while brute-forcing or decrypting weak passwords. Evasion uses Cisco Guest Shell containerized Linux environments (which bypass traditional syslog and AAA accounting) and the 'JumbledPath' utility to obfuscate traffic sources. Collection includes harvesting BGP routes, RSVP sessions, MIB dumps, and MPLS info via TFTP. Lateral movement leverages compromised devices and trusted carrier-grade interconnections to pivot into other networks (telecoms, government, transportation, lodging, military). CISA states exploitation of zero-day vulnerabilities has NOT been observed.
- **Affected Products:** Ivanti Connect Secure (9.x, 22.x) and Ivanti Policy Secure (9.x, 22.x) — CVE-2024-21887 (command injection; often chained with CVE-2023-46805 authentication bypass); Palo Alto Networks PAN-OS GlobalProtect — CVE-2024-3400 (command injection); Cisco IOS XE — CVE-2023-20198 (Web UI auth bypass creating unauthorized local accounts) and CVE-2023-20273 (often chained with CVE-2023-20198); Cisco IOS/IOS XE Smart Install — CVE-2018-0171. Additional suspected targets referenced in the advisory: Fortinet firewalls, Juniper firewalls, Microsoft Exchange, Nokia routers and switches, Sierra Wireless devices, SonicWall firewalls.
- **CVSS Score:** CVSS score unavailable — the advisory aggregates several CVEs (CVE-2024-21887, CVE-2024-3400, CVE-2023-20198, CVE-2023-20273, CVE-2018-0171), each with their own individual base scores published by NVD/vendors.
- **CVSS Vector:** CVSS vector unavailable — AA25-239A is a joint threat-activity advisory covering multiple n-day CVEs across several vendors; no single CVSS v3 vector applies to the advisory as a whole. Individual CVE vectors exist in their respective NVD/vendor records.
- **Exploit Available:** true — Public PoCs/exploit code exist for the referenced CVEs, including https://github.com/Chocapikk/CVE-2024-21887 for the Ivanti command injection. Cisco Talos/GreyNoise confirmed exploitation of CVE-2018-0171 and CVE-2023-20198 in Salt Typhoon activity.
- **Patch Available:** true — Vendor patches are available for all CVEs referenced in the advisory. Ivanti patches for CVE-2023-46805/CVE-2024-21887: https://hub.ivanti.com/s/article/KB-CVE-2023-46805-Authentication-Bypass-CVE-2024-21887-Command-Injection-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure-Gateways. Palo Alto PAN-OS fixes for CVE-2024-3400 and Cisco IOS XE fixes for CVE-2023-20198, CVE-2023-20273, and CVE-2018-0171 have been published in the respective vendor security advisories.
- **Active Exploitation:** true — Confirmed active in-the-wild exploitation. CISA, NSA, FBI, and DC3 explicitly attribute ongoing PRC state-sponsored exploitation to telecommunications, government, transportation, lodging, and military networks. Recorded Future (Feb 2025) documented RedMike/Salt Typhoon targeting Cisco telecom networks Dec 2024–Jan 2025; Cisco Talos reported Salt Typhoon gained initial access to telecoms primarily via legitimate login credentials on Cisco devices; GreyNoise observed exploitation of CVE-2018-0171 tied to the Salt Typhoon campaign.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, and GhostEmperor (collectively PRC state-sponsored APT actors). Tracking names documented by CISA, NSA, FBI, DC3, and corroborated by Recorded Future, Cisco Talos, and NJCCIC.
- **Mitigation:** Prioritize patching the listed CVEs and upgrading unsupported devices; baseline and audit router/AAA/ACL/routing configurations for unexpected GRE tunnels, external IPs in AAA/ACLs, traffic mirroring, or unauthorized Guest Shell containers; implement management-plane isolation (out-of-band management networks or management VRFs with default-deny ACLs restricting egress); enable control-plane policing (CoPP); use SSHv2 only and disable Telnet and unencrypted HTTP; change all default admin credentials and SNMP community strings; enforce SNMPv3 with restricted writes; use strong MFA/PKI authentication and Type 8 (PBKDF2) password storage; minimize authentication attempt windows and account lockouts; monitor and disable Cisco Guest Shell where operationally unnecessary and hunt for 'guestshell enable', 'guestshell run bash', 'chvrf', and 'dohost' commands; monitor TACACS+/RADIUS server changes; verify firmware/image hashes against vendor values with signed image enforcement; deploy detection signatures (Snort, YARA, vendor NGFW AV) for the listed CVEs; hunt for the supplied IOCs and STIX bundle from the advisory JSON.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Since 2022, GRU Unit 26165 has conducted a cyber-espionage campaign against Western logistics entities and IT companies supporting aid delivery to Ukraine. TTPs include credential guessing/brute force (often via Tor), spearphishing with spoofed login pages and malware-laden attachments, and exploitation of public-facing applications: Outlook CVE-2023-23397 leaks Net-NTLMv2 hashes through malicious calendar items; WinRAR CVE-2023-38831 achieves arbitrary code execution when a user opens a benign file inside a crafted ZIP archive containing a same-named folder; Roundcube CVE-2020-12641 enables command injection via im_convert_path/im_identify_path, CVE-2020-35730 enables stored XSS via link references, and CVE-2021-44026 enables SQL injection via search/search_params. Post-exploitation uses Impacket, PsExec, RDP for lateral movement; HEADLACE, MASEPIE, OCEANMAP, STEELHOOK payloads; DLL search-order hijacking; persistence via scheduled tasks and Run keys; defense evasion via clearing Windows Event Logs; AD credential dumping with ntdsutil/vssadmin/Certipy; mailbox permission manipulation in Exchange; and exfiltration over OpenSSH. Compromised SOHO devices used as proxies; IP cameras at border crossings targeted via RTSP credential brute-forcing.
- **Affected Products:** Microsoft Outlook (all versions prior to March 2023 Patch Tuesday fixes - CVE-2023-23397), RARLAB WinRAR before 6.23 (CVE-2023-38831), Roundcube Webmail before 1.3.17 and 1.4.x before 1.4.12 (CVE-2021-44026), Roundcube Webmail before 1.2.13, 1.3.x before 1.3.16, and 1.4.x before 1.4.10 (CVE-2020-35730), Roundcube Webmail before 1.4.4 (CVE-2020-12641), SOHO routers/NAS, IP cameras, and corporate VPNs.
- **CVSS Score:** 9.8 (CVE-2023-23397 - highest severity referenced; CVE-2023-38831 = 7.8; other CVEs have individual NVD scores)
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/R:U/C:H/I:H/A:H (CVE-2023-23397, highest-severity referenced CVE)
- **Exploit Available:** true
- **Patch Available:** true - Patches available: Microsoft Outlook (March 2023 Patch Tuesday - https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23397), WinRAR 6.23 (CVE-2023-38831), Roundcube 1.4.10+ and 1.4.12+ for referenced CVEs
- **Active Exploitation:** true - CISA AA25-141A documents an ongoing, multi-year (since 2022) Russian state-sponsored cyber-espionage campaign by GRU Unit 26165 against Western logistics and IT firms involved in coordinating and delivering aid to Ukraine. The authoring agencies 'expect similar targeting and TTP use to continue.'
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS), military unit 26165. Industry-tracked aliases: APT28, Fancy Bear, Forest Blizzard (Strontium), BlueDelta, UAC-0001.
- **Mitigation:** Apply vendor patches for the referenced CVEs (Outlook March 2023 update; WinRAR 6.23 or later; Roundcube 1.3.17+/1.4.12+ or later). Harden authentication against credential abuse (MFA, lockout, anti-brute-force, block Tor/commercial VPN egress where feasible). Apply zero-trust network segmentation and restrict lateral movement (limit RDP, SMBv1, legacy protocols; disable NTLM where possible). On IP cameras and SOHO routers, disable UPnP, P2P, and Anonymous Visit features; close unused ports (FTP, web admin); enable authenticated RTSP only; enable logging and monitor. Audit remote-access activity, mailbox permission changes, and unauthorized use of personal accounts in official communications. Monitor for LOLBin abuse (ntdsutil, wevtutil, vssadmin, Certipy) and for Impacket/PsExec activity. Hunt for IOCs listed in the advisory. Restrict access to hosting and API-mocking platforms; only use approved systems for sensitive information.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

**Parallel AI Enrichment:**

- **Technical Details:** Remote code execution (RCE) in Ivanti Sentry leading to full appliance compromise — allows configuration changes, credential theft, data access, and lateral movement. Low-level exploit details (vulnerable parameter/auth requirements) are not present in the supplied corpus.
- **Affected Products:** Ivanti Sentry appliance (specific versions unavailable)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — public PoC available (e.g., http://horizon3.ai/attack-research/vulnerabilities/cve-2026-10520, http://enigma-global.com/reports/cve-2026-10520-critical-ivanti-sentry-os-command-injection-actively-exploited-mqaltqap-twhb)
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true — confirmed by Shadowserver Foundation and multiple reports
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 12. 🟠 Zero-Day — In Other News: Canadian Hacker Jailed, Open Source Zero-Days, Two Sentenced for ATM Jackpotting

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-03
**Reference:** <https://www.securityweek.com/in-other-news-canadian-hacker-jailed-open-source-zero-days-two-sentenced-for-atm-jackpotting/>

> Noteworthy stories that might have slipped under the radar: Anonymous-linked Canadian hacker jailed, researcher drops zero-days in open source projects, Venezuelans sentenced in the US over ATM jackpotting. The post In Other News: Canadian Hacker Jailed, Open Source Zero-Days, Two Sentenced for ATM Jackpotting appeared first on SecurityWeek .

---

## 13. 🟠 Zero-Day — Google, FBI Disrupt NetNut Residential Proxy Network Powered by Millions of Devices

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-03
**Reference:** <https://www.securityweek.com/google-fbi-disrupt-netnut-residential-proxy-network-powered-by-millions-of-devices/>

> NetNut rented access to millions of compromised devices, allowing cybercriminals and nation-state actors to mask their identities during attacks. The post Google, FBI Disrupt NetNut Residential Proxy Network Powered by Millions of Devices appeared first on SecurityWeek .

---

## 14. 🟡 High Severity — 9router has an Incomplete Fix: Local-Only Access Gate Bypass in 9router via Host Header SpoofING

**CVE:** `CVE-2026-49353` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-6g2f-w7g3-77vf>

> ## Summary

The fix for CVE-2026-46339 (unauthenticated RCE via unprotected MCP plugin routes) introduced a local-only access gate in `src/dashboardGuard.js` that restricts spawn-capable routes (`/api/mcp/*`, `/api/tunnel/*`, `/api/cli-tools/*`) to loopback requests. The gate determines &quot;local&quot; by inspecting the `Host` and `Origin` HTTP headers rather than the TCP source address. When 9r…

---

## 15. 🟡 High Severity — 9router's Hardcoded Default fallback JWT Secret  Allows Authentication Bypass

**CVE:** `CVE-2026-49352` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-jphh-m39h-6gwx>

> ### Summary
9router uses a publicly known hardcoded string `&quot;9router-default-secret-change-me&quot;` as the fallback of JWT secret for all Dashboard session JWTs when the `JWT_SECRET` environment variable is not set. Because this secret is committed in the public repository and unchanged across all releases, any unauthenticated remote attacker can forge a valid `auth_token` cookie and gain fu…

---

## 16. 🟡 High Severity — LaunchServer FileServerHandler has an unauthenticated path traversal issue

**CVE:** `CVE-2026-54617` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-5g75-477j-2c2f>

> ### Summary
An unauthenticated path traversal in the LaunchServer HTTP file server (`FileServerHandler`) lets any remote actor read **any file** readable by the LaunchServer process (e.g. `../../../../etc/passwd`). This is a generic arbitrary-file-read primitive, so the fix must address the traversal itself, not any specific file.

The readable files include the server&#x27;s own secrets, which tu…

---

## 17. 🟡 High Severity — Algernon vulnerable to server-side script source disclosure on Windows via NTFS filename

**CVE:** `CVE-2026-52792` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-mm6c-5j6x-hq8m>

> ### Summary

Algernon selects its file handler from `filepath.Ext()` (engine/handlers.go:134), which does not treat the NTFS-equivalent names `x.lua::$DATA`, `x.lua.`, or `x.lua ` as `.lua`. On Windows, an unauthenticated client appends one of these suffixes to any server-side script on a public path and receives its raw source instead of executed output, leaking embedded secrets such as database …

---

## 18. 🟡 High Severity — Steeltoe: OAEP setting silently selects PKCS#1 v1.5 padding

**CVE:** `CVE-2026-50268` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-4j9m-h44m-2hv8>

> ### Summary

Configuring `encrypt:rsa:algorithm=OAEP` does not enable OAEP encryption. Due to an incorrect BouncyCastle transformation string, the `OAEP` setting selects PKCS#1 v1.5, which is the same algorithm as the `DEFAULT` setting.

### Impact

Operators who configure `encrypt:rsa:algorithm=OAEP` to obtain CCA2-secure padding receive PKCS#1 v1.5 instead. Currently, `Decrypt()` is called only …

---

## 19. 🟡 High Severity — Steeltoe's static JWKS cache shared across schemes and never invalidated

**CVE:** `CVE-2026-50202` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-7fqc-p256-7pwj>

> ### Summary

The JWT signing key cache in `TokenKeyResolver` uses `kid` as the sole cache key without namespacing by authority. In applications with multiple `JwtBearer` schemes pointing to different identity providers, a key fetched for one scheme can satisfy token validation for another. Additionally, cached keys have no expiration, so rotated or revoked keys remain trusted until the application…

---

## 20. 🟡 High Severity — Steeltoe's env sanitizer misses connection strings — leaks embedded DB passwords

**CVE:** `CVE-2026-50200` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-q62h-354g-5r85>

> ### Summary

The `Sanitizer` component in the Environment actuator redacts configuration values by matching the configuration key name against a suffix list. The default list (`password`, `secret`, `key`, `token`, `.*credentials.*`, `vcap_services`) does not cover the standard .NET pattern `ConnectionStrings:&lt;name&gt;` or Steeltoe Connectors&#x27; `Steeltoe:Client:&lt;type&gt;:Default:Connectio…

---

## 21. 🟡 High Severity — SimpleSAMLphp HTTP-Artifact TLS validator confusion allows cross-IdP authentication bypass

**CVE:** `CVE-2026-49283` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-6929-8p9f-26jx>

> ## Summary

SimpleSAMLphp&#x27;s HTTP-Artifact receive path can treat an unsigned embedded SAML `Response` as cryptographically valid for the wrong IdP.

In the `HTTPArtifact::receive()` flow, the SOAP `ArtifactResponse` receives a TLS-based validator from `SOAPClient::addSSLValidator()`. The embedded SAML `Response` then receives a validator that delegates signature validation to that outer `Arti…

---

## 22. 🟡 High Severity — Linuxfabrik Monitoring Plugins: Sudoers may be able to obtain privilege escalation via /usr/bin/apt-get arguments

**CVE:** `CVE-2026-52817` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-8w6w-23mq-h8rg>

> ### Summary
In the [Debian.sudoers](https://github.com/Linuxfabrik/monitoring-plugins/blob/main/assets/sudoers/Debian.sudoers) file, `apt-get` is allowed for the nagios user. The full command including the arguments are not enforced and can therefore be choosen arbitrarily. This allows to easily get a root shell as the nagios user:

### PoC
By choosing a particular argument, you can get (as a nagi…

---

## 23. 🟡 High Severity — zebrad has persistent on-disk corruption of Sapling/Orchard subtree roots after chain fork via pop_tip

**CVE:** `CVE-2026-52733` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-2gf8-q9rr-jq3h>

> ### Am I affected

You are affected if:

1. You run `zebrad` up to and including `v4.4.1`.
2. Your node participates in a network where chain forks occur (mainnet, testnet, or any network with multiple miners).

All default configurations are affected. The corruption persists across restarts because it is written to RocksDB.

### Summary

When `pop_tip` removes the tip block during a chain fork, s…

---

## 24. 🟡 High Severity — Mautic vulnerable to Path Traversal via Campaign Import

**CVE:** `CVE-2026-9559` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-6r9h-4h75-7q4x>

> ### Summary
A path traversal vulnerability exists in the campaign import feature of Mautic 7. When extracting uploaded ZIP files during campaign imports, a flaw in the validation logic allows file paths to escape the intended temporary directories. 

### Impact
An authenticated user with campaign import privileges (`campaign:imports:create`) can write arbitrary PHP files to sensitive system direct…

---

## 25. 🟡 High Severity — Mautic has Server-Side Template Injection (SSTI) in Theme Templates

**CVE:** `CVE-2026-9558` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-9fx4-7cmj-47vg>

> ### Summary
A Server-Side Template Injection (SSTI) vulnerability exists in Mautic&#x27;s theme engine. The platform renders uploaded Twig templates without a sandbox or strict function restrictions. Authenticated users with permissions to create or upload themes can abuse this to execute arbitrary code.

### Impact
An authenticated user with theme upload and creation privileges can bypass boundar…

---

## 26. 🟡 High Severity — Mautic Focus component Vulnerable to SSRF

**CVE:** `CVE-2026-9557` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-jmv8-8j9j-rcpc>

> ### Summary
A Server-Side Request Forgery (SSRF) vulnerability exists in the Mautic Focus component (`MauticFocusBundle`). Under certain conditions, insufficiency in validating user-supplied URLs allows authenticated users to trigger outbound HTTP requests from the hosting server.

### Impact
An authenticated user with access to the Mautic panel can exploit this vulnerability to perform internal p…

---

## 27. 🟡 High Severity — zebrad has mempool transaction admission denial via single-peer inbound queue saturation

**CVE:** `CVE-2026-52732` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-4fc2-h7jh-287c>

> ### Am I affected

You are affected if:

1. You run `zebrad` up to and including `v4.4.1`.
2. Your node accepts inbound P2P connections (`network.listen_addr` is set, which is the default).
3. Your node&#x27;s mempool is active (node is synced near the chain tip).

All default configurations are affected.

### Summary

A single unauthenticated P2P peer can monopolize all 25 inbound mempool downloa…

---

## 28. 🟡 High Severity — Dragonfly Manager OAuth provider client_secret disclosure via unauthenticated GET /api/v1/oauth

**CVE:** `CVE-2026-49254` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-4q9j-6299-gxmr>

> ### Summary

The Dragonfly Manager exposes `GET /api/v1/oauth` and `GET /api/v1/oauth/:id` to unauthenticated clients. The response body deserializes the entire `manager/models.Oauth` struct, which includes the `client_secret` field. Any network-reachable attacker can read the OAuth client secrets configured for `github` or `google` providers, defeating the confidentiality guarantee of those secre…

---

## 29. 🟡 High Severity — joserfc: HS256/HS384/HS512 verify accepts empty/nil HMAC key (cross-language sibling of CVE-2026-45363)

**CVE:** `CVE-2026-49852` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-gg9x-qcx2-xmrh>

> ### Summary

`joserfc.jwt.decode` accepts attacker-forged HMAC-signed tokens when the
caller-supplied verification key is the empty string or `None`.
`HMACAlgorithm.sign` and `HMACAlgorithm.verify` in
[`src/joserfc/_rfc7518/jws_algs.py:62-70`](https://github.com/authlib/joserfc/blob/1ddca8f3c73ff47e3bc3ac06cb0c08a9535677ec/src/joserfc/_rfc7518/jws_algs.py#L62-L70) feed whatever
`OctKey.get_op_key(…

---

## 30. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
