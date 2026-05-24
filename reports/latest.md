# Zero Day Pulse

> **Generated:** 2026-05-24 12:57 UTC &nbsp;|&nbsp; **Total:** 9 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 8 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 9

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated remote attackers can exploit a path traversal flaw in SimpleHelp RMM (versions ≤5.5.7) to access arbitrary files on the server, enabling information disclosure and credential theft.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:N
- **Exploit Available:** true (https://medium.com/@RosanaFS/simplehelp-cve-2024-57727-tryhackme-walkthrough-9f88c2061fb9)
- **Patch Available:** true (https://threatprotect.qualys.com/2025/02/07/simplehelp-remote-monitoring-and-management-multiple-vulnerabilities-cve-2024-57726-cve-2024-57727-cve-2024-57728/)
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Update SimpleHelp to the latest patched version; restrict RMM access to trusted networks; enforce strong authentication and monitor for unusual activity.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when adversarial content embedded in web pages/documents supplies instructions that an AI agent consumes and follows (e.g., hidden or context‑promoting payloads that override user intent). Attack vector: web or document content ingested by agents leads to execution of malicious instructions (data exfiltration, fraud, API‑key theft, destructive commands).
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Monitor and remove known IPI payloads from web content, use allowlisting and content provenance/validation, separate and sanitize external content before feeding to agents, apply prompt hardening (explicit instructions, reject or ignore embedded commands), implement model input filtering and telemetry/monitoring to detect behavioral deviations.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) enables an attacker to influence a large language model’s behavior by inserting malicious instructions into the data sources, APIs, or auxiliary tools the model uses to answer a user query, thereby achieving unauthorized actions without the user explicitly providing the malicious prompt.
- **Affected Products:** Google Workspace (all tiers), Gemini app within Workspace
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Implement continuous monitoring for indirect prompt injection patterns, enforce strict validation of data and tool outputs used by LLMs, apply prompt sanitization and input‑filtering, and adopt Google’s layered defense guidelines for Gemini‑enabled Workspace features.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is the primary threat; malicious web content or third‑party resources can influence agentic AI agents by injecting prompts or crafted content. Chrome's mitigations include layered defenses to block prompt injections, restrict origin access for agentic browsing, and add supervising AI agents/controls to prevent unsafe actions.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true — http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Update Chrome to the release containing these defenses, disable or restrict agentic browsing features where possible, follow vendor guidance to limit third‑party content and origin access, and apply general hardening (content security policies, input validation, least privilege for automation).
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection embeds malicious instructions in external data sources (emails, documents, calendar invites, images/URLs) to manipulate LLM behavior or exfiltrate data. Google mitigations include adversarial training for Gemini, ML classifiers to detect malicious instructions, sanitizing external content (images/URLs), and requiring user confirmations for risky actions.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known.
- **Mitigation:** Use layered defenses: model hardening (Gemini 2.5 adversarial training), prompt‑injection content classifiers, security‑thought reinforcement, markdown sanitization and suspicious URL redaction, user confirmation (HITL) framework, end‑user security mitigation notifications; follow Google Help Center guidance (https://support.google.com/docs/answer/16204578).
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state‑sponsored actors target large backbone routers, provider edge (PE) and customer edge (CE) routers, and leverage compromised devices/trusted connections to pivot. Actors often modify routers to maintain persistent, long‑term access, and use covert networks of compromised SOHO/IoT devices to mask activity and enable lateral movement.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Hunt for connections from IP addresses likely part of covert compromised‑device networks (e.g., SOHO routers, IoT devices); implement network segmentation, monitor for anomalous router configuration changes, apply vendor router hardening best practices, restrict management interfaces, enforce strong authentication, and follow CISA guidance AA26‑113A and AA24‑038A for defending against covert networks.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Unit 26165 employed spear‑phishing attachments, exploited WinRAR ZIP handling (CVE‑2023‑38831) and Outlook NTLM credential leakage (CVE‑2023‑23397), performed SQL injection on public‑facing applications, compromised corporate VPNs, manipulated Exchange/Office365 mailbox permissions for sustained email collection, leveraged tools such as Certipy and ADExplorer for Active Directory data exfiltration, used a dropped OpenSSH binary for data transfer, and targeted IP‑camera firmware for additional access.
- **Affected Products:** WinRAR (CVE-2023-38831), Microsoft Outlook (CVE-2023-23397), Roundcube Webmail (CVE-2020-35730, CVE-2020-12641)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** GRU 85th Main Special Service Center (85th GTsSS), military unit 26165 — tracked as APT28 / Fancy Bear / Forest Blizzard / Blue Delta
- **Mitigation:** Apply vendor patches and updates for all listed CVEs; enable endpoint detection and response (EDR) on all systems, especially mail servers and domain controllers; enforce Windows attack surface reduction rules; monitor Windows event logs and authentication activity; audit and secure IP‑camera accounts (enable authenticated RTSP where possible); collect and hunt for IOCs; enforce multi‑factor authentication and review mailbox permissions; restrict or monitor the use of legitimate utilities such as ntdsutil, wevtutil, vssadmin, ADExplorer, OpenSSH, and schtasks.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

**Parallel AI Enrichment:**

- **Technical Details:** A malicious DNS response can trigger out‑of‑bounds reads, writes, and other memory‑safety issues in the modem DNS parser implementation (C/C++), enabling remote code execution via crafted DNS responses. Rewriting the DNS parser in Rust eliminates this class of memory‑safety bugs.
- **Affected Products:** Google Pixel devices
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor Android/Pixel security bulletin updates (patch); as an architectural mitigation, replace/rewrite the DNS parser with a memory‑safe implementation (Google’s Rust hickory‑proto integration). If the patch cannot be applied, limit exposure by restricting DNS from untrusted networks and using secure carrier DNS configurations when possible.
- **Vendor Advisory:** https://source.android.com/security/bulletin/pixel/2024-03-01

---
