# Zero Day Pulse

> **Generated:** 2026-05-31 02:09 UTC &nbsp;|&nbsp; **Total:** 10 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 9 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path traversal vulnerability in SimpleHelp remote support software that permits unauthenticated attackers to read arbitrary files on the server, such as logs, configuration files, and credential stores, potentially leading to full system compromise.
- **Affected Products:** SimpleHelp remote support software v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true - http://horizon3.ai/attack-research/disclosures/critical-vulnerabilities-in-simplehelp-remote-support-software
- **Patch Available:** true - http://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570
- **Active Exploitation:** true
- **Threat Actors:** DragonForce ransomware group
- **Mitigation:** Upgrade to SimpleHelp version 5.5.8 immediately. If immediate upgrade is not possible, restrict network access to the SimpleHelp service, enforce strict file‑system permissions, and monitor for anomalous file reads.
- **Vendor Advisory:** http://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when adversarial content on the web or in user‑supplied artifacts contains instructions that an AI agent or LLM‑based automation system ingests and executes, causing unauthorized actions, secret leakage, or workflow subversion. Attack chains often combine IPI with elevated agent privileges or integrations (e.g., CI/CD actions, code‑review tools, system CLIs), exemplified by the 'Comment and Control' chain in Claude Code.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Treat untrusted content as hostile; apply input sanitization and content provenance checks; enforce least‑privilege for AI agents; restrict secret exposure to web content; sandbox agent runtimes; implement explicit allowlists/denylists for actions; monitor and alert for anomalous agent behavior.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack where adversaries inject malicious instructions into data or tools the LLM accesses (e.g., documents, URLs, markdown). The LLM can be influenced to perform unintended actions or disclose data when it processes those inputs as part of fulfilling a user query.
- **Affected Products:** Google Workspace with Gemini
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Defense‑in‑depth including human and automated red‑teaming, Google AI VRP, synthetic‑data‑driven ML retraining, deterministic defenses (URL sanitization, markdown sanitization, suspicious URL redaction, user confirmation framework, tool‑chaining policies), LLM‑based defenses and prompt‑engineering, and Gemini model hardening.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) allows malicious web content to craft inputs that indirectly influence AI agents embedded in the browser, leading to unauthorized actions. Chrome mitigates this by adding layered defenses that block prompt injections, enforce origin restrictions, and prevent unsafe AI actions.
- **Affected Products:** Google Chrome (agentic/Gemini‑enabled builds; specific versions not listed in advisory)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — see vendor advisory: http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Update Chrome to the latest version with the new layered defenses; enable the prompt‑injection blocking, origin‑restriction controls, and AI‑action restrictions as recommended by Google.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Introducing Rust into Android’s codebase reduces memory‑safety bugs (e.g., buffer overflows, use‑after‑free) in C/C++ components, leading to a drop of memory‑safety related vulnerabilities to less than 20% of total findings in 2025. The improvement is attributed to Rust’s guarantees against such classes of bugs and accompanying process changes.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true - Android security updates and Google advisories (https://blog.google/security/rust-in-android-move-fast-fix-things/)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Continue migration to memory‑safe languages (Rust), improve code review processes, employ fuzz testing, and apply timely security updates as advised by Google.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injections are hidden malicious instructions embedded in external data sources (emails, documents, calendar invites, web content) that aim to manipulate generative AI systems to exfiltrate data or perform unauthorized actions. Google mitigates this via model hardening (adversarial training), prompt‑injection content classifiers, security thought reinforcement, markdown sanitization, suspicious URL redaction, user‑confirmation frameworks, and end‑user security mitigation notifications.
- **Affected Products:** Gemini app, Gemini in Google Workspace (Gmail, Docs, Drive, Chat)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply layered defenses: use model hardening/adversarial training, deploy prompt‑injection content classifiers on all untrusted inputs, enable markdown sanitization and suspicious URL redaction, require explicit user confirmations for risky actions, monitor with end‑user security mitigation notifications, and follow Google Help Center guidance (https://support.google.com/docs/answer/16204578).
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** APT actors exploit publicly known CVEs in edge/network devices (routers, PE/CE routers, VPN gateways) to gain initial access; they modify router configurations (ACLs, AAA/TACACS+), enable services/ports, deploy on‑box Linux containers, use embedded packet capture and SPAN/RSPAN/ERSPAN to collect credentials and traffic, create accounts, execute commands via SNMP/SSH, and employ GRE/IPsec tunnels for exfiltration and covert channels.
- **Affected Products:** Cisco IOS, Cisco IOS XE (various versions), Ivanti Connect Secure / Ivanti Policy (CVE‑2024‑21887, CVE‑2023‑46805), Palo Alto PAN‑OS GlobalProtect (CVE‑2024‑3400), Fortinet, Juniper, Microsoft Exchange, Nokia routers/switches, Sierra Wireless, SonicWall
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching known exploited CVEs; audit and monitor device configuration and logs for unexpected ACL entries, external AAA/TACACS+ IPs, packet capture/mirroring, virtual containers, and opened ports; verify firmware integrity and hashes; employ credential hardening (disable password auth where possible, use PKI/MFA, strong password hashing); implement change management and alerting; follow vendor hardening guides (Cisco IOS/IOS XE hardening, Cisco Software Checker) and apply vendor patches.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Unit 26165 conducts espionage using credential guessing/brute force, spearphishing, Outlook NTLM relay (CVE‑2023‑23397), Roundcube and WinRAR vulnerabilities to execute code, abuses SOHO routers and IP cameras for proxying and reconnaissance, moves laterally with Impacket/PsExec/RDP, harvests AD data, manipulates mailbox permissions, and exfiltrates data via archived ZIP files and OpenSSH.
- **Affected Products:** Microsoft Outlook (CVE-2023-23397), WinRAR (CVE-2023-38831), Roundcube Webmail (CVE-2020-12641, CVE-2020-35730, CVE-2021-44026), SOHO router/device firmware, OpenSSH (Windows builds), IP camera vendors/models
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Russian GRU Unit 26165 (tracked as APT28/Fancy Bear, Forest Blizzard, Blue Delta)
- **Mitigation:** Network segmentation; enable Windows attack surface reduction and EDR; collect and monitor Windows logs; audit and harden email and mailbox permissions; apply vendor patches for cited CVEs; disable or harden NTLM; authenticate/tune RTSP on IP cameras; restrict/examine SOHO device access; monitor for listed LOTL utilities and suspicious command lines; report incidents to CISA/FBI/DC3.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — PAN-OS GlobalProtect Authentication Bypass (CVE-2026-0257) Under Active Exploitation

**CVE:** `CVE-2026-0257` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-30
**Reference:** <https://thehackernews.com/2026/05/pan-os-globalprotect-authentication.html>

> Palo Alto Networks has warned that a recently disclosed medium-severity security flaw impacting PAN-OS and Prisma Access has come under active exploitation in the wild.

The vulnerability, tracked as CVE-2026-0257 (CVSS score: 7.8), refers to a case of authentication bypass that could be exploited by bad actors to set up VPN connections.

&quot;Authentication bypass vulnerabilities in the

**Parallel AI Enrichment:**

- **Technical Details:** An authentication bypass in GlobalProtect portal/gateway when authentication override cookies are enabled allows an unauthenticated attacker to bypass authentication and establish VPN connections to the network.
- **Affected Products:** PAN-OS GlobalProtect portal and gateway on affected PAN-OS and Prisma Access deployments
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply vendor-provided patches/updates to affected PAN-OS/Prisma Access versions; if patch cannot be applied immediately, disable authentication override cookies, restrict access to portals/gateways, and apply compensating controls.
- **Vendor Advisory:** https://security.paloaltonetworks.com/CVE-2026-0257

---

## 10. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

**Parallel AI Enrichment:**

- **Technical Details:** A malicious DNS response can trigger out‑of‑bounds reads, writes, and other memory issues in the modem DNS parser, leading to memory‑safety vulnerabilities.
- **Affected Products:** Pixel 9 modem DNS parser, Pixel 10 modem DNS parser
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Replace the memory‑unsafe DNS parser with a memory‑safe Rust‑based parser (as implemented for Pixel 10).
- **Vendor Advisory:** https://source.android.com/security/bulletin/pixel/2024-03-01

---
