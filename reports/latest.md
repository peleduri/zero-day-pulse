# Zero Day Pulse

> **Generated:** 2026-06-15 11:42 UTC &nbsp;|&nbsp; **Total:** 11 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** A directory traversal flaw in SimpleHelp v5.5.7 and earlier allows an unauthenticated remote attacker to traverse the file system and read arbitrary files, potentially leading to further compromise.
- **Affected Products:** SimpleHelp remote support software v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (unspecified)
- **Mitigation:** Upgrade SimpleHelp to version 5.5.8 or later, which includes fixes for the path‑traversal vulnerability.
- **Vendor Advisory:** https://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) abuses external content retrieved by an LLM‑based agent (e.g., web pages, retrieved documents or tool outputs) to inject malicious instructions that are incorporated into the agent’s prompt/context. Attacks target RAG pipelines and agentic workflows by poisoning retrieved snippets or crafting web content that convinces the model to ignore safety directives, exfiltrate data, or execute unauthorized actions. A zero‑click IPI (GeminiJack) demonstrated against Google Gemini Enterprise triggered unintended behavior via injected content in retrieved context.
- **Affected Products:** AI agents (retrieval‑augmented generation (RAG) systems and agentic LLM systems); Google Gemini Enterprise
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Restrict and validate retrieved content (source allowlists, content sanitization, canonicalization); apply strict prompt templates that separate external content as data only; use model grounding and provenance checks; implement retrieval filtering, content‑type whitelisting, and strict action authorization for agents; apply least‑privilege for tool/connector access and require human approval for high‑risk actions.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) injects malicious instructions into data sources or tools that LLMs consult when completing user queries. Attackers can embed payloads in documents, web content, or tool outputs that are ingested by the model or its agents, causing it to follow attacker‑controlled instructions—sometimes without any direct user interaction (zero‑click). The attack leverages agentic automation and multi‑source context fetching to manipulate model behavior.
- **Affected Products:** Google Workspace with Gemini integrations (specific product versions not published)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor‑provided mitigations and layered defenses: treat untrusted content as adversarial, enforce strict tool/data input validation and sanitization, restrict autonomous agent actions, implement content provenance controls, apply least‑privilege principles for tool access, rate‑limit requests, monitor for anomalous behavior, and keep models and systems regularly updated with hardening patches.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection — attackers supply malicious instructions embedded in web content or external data that an AI agent consumes during agentic browsing, causing the agent to perform unsafe actions or disclose sensitive data. Chrome's architecture addresses this by restricting origin access, layering defenses to detect and block prompt injections, and adding supervision agents to validate actions.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — vendor advisory: http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use Chrome's updated agentic security features described in the advisory (layered defenses to block prompt injections, origin access restrictions, and oversight agents). Follow vendor guidance and keep Chrome updated.
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
- **Threat Actors:** None known.
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injections embed hidden malicious instructions in external data sources (e.g., emails, documents, calendar invites) that aim to manipulate AI assistants to exfiltrate data or perform harmful actions. Google mitigates this via model hardening, adversarial training, security‑thought reinforcement, markdown sanitization, suspicious‑URL redaction, user‑confirmation frameworks, and end‑user security notifications.
- **Affected Products:** Gemini (Google Workspace, Gemini app)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Implement layered defenses: model hardening/adversarial training, security‑thought reinforcement, markdown sanitization (disable external image rendering), suspicious‑URL detection/redaction via Google Safe Browsing, user‑confirmation for risky actions, end‑user security notifications, and continuous red‑team testing.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** APT actors exploit publicly known CVEs and avoidable weaknesses in internet‑exposed network and edge devices (e.g., Cisco IOS/XE web UI authentication bypass CVE‑2023‑20198, Cisco Smart Install CVE‑2018‑0171, Ivanti CVE‑2024‑21887) to create unauthorized admin accounts, run Tcl/Python scripts, enable high‑port services, abuse Guest Shell, execute commands via SNMP/SSH, modify firmware/configurations for persistence, and exfiltrate traffic via GRE/MPLS tunnels.
- **Affected Products:** Cisco IOS, Cisco IOS XE, Cisco NX-OS, Ivanti Connect Secure, Ivanti Policy, Fortinet, Juniper, Nokia routers/switches, Sierra Wireless, SonicWall
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching known exploited CVEs; disable unused ports/protocols and management interfaces; restrict/disable web UI exposure; require public‑key authentication for admin accounts; change default credentials; monitor firmware/software integrity and perform hash verification; use vendor hardening guides (e.g., Cisco IOS/XE hardening); disable Guest Shell where not needed; block outbound connections from management interfaces; perform threat hunting for IOCs and configuration anomalies; follow CISA/NSA/FBI guidance.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Operation is espionage‑focused using typical GRU tradecraft: spearphishing and credential theft, network intrusion and lateral movement to access logistics and IT systems to collect sensitive information and operational data.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS), military unit 26165 (APT28/Fancy Bear)
- **Mitigation:** Implement recommended CSIRT/CISA mitigations: strengthen account hygiene and MFA, network segmentation, endpoint detection and response, monitor for IOCs, restrict external‑facing services, apply least‑privilege principles, and backup critical data.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** CVE‑2026‑45586: link‑following (CWE‑59) elevation of privilege in Windows CTFMON allowing a low‑privileged local attacker to gain SYSTEM. CVE‑2026‑50507: missing authentication (CWE‑306) in BitLocker permitting bypass with physical access. CVE‑2026‑49160: denial‑of‑service in HTTP.sys. CVE‑2026‑47291: remote code execution via kernel‑mode HTTP driver in HTTP.sys. CVE‑2026‑44815: stack‑based buffer overflow (CWE‑121) in DHCP Client Service enabling remote code execution via rogue DHCP server responses.
- **Affected Products:** Windows (Collaborative Translation Framework/CTFMON, BitLocker, HTTP.sys, DHCP Client Service, Active Directory Domain Services, Outlook, Word, Windows Media, Windows Graphics Component/Win32K, Kerberos KDC)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the June 9, 2026 Microsoft updates (KB5094126 and individual CVE patches). For unpatched exposures, restrict physical access to BitLocker‑protected devices, audit and limit applications that call DhcpGetOriginalSubnetMask, and isolate/limit exposure of services using HTTP.sys/IIS. Follow standard hardening: network segmentation, least‑privilege, full‑disk encryption with secure key management, and endpoint detection.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/releaseNote/2026-Jun

---

## 10. 🟠 Zero-Day — When a Government Pulls an AI Model: What the Fable 5 and Mythos 5 Suspension Means for Security Teams

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Snyk Vulnerability Research &nbsp;|&nbsp; **Published:** 2026-06-14
**Reference:** <https://snyk.io/blog/fable-mythos-suspension-security-takeaways/>

> On June 12, 2026, a US export-control directive led Anthropic to disable Claude Fable 5 and Mythos 5 worldwide over a reported jailbreak. The reported trigger was a code-analysis capability that defenders use routinely. Here is what happened, how the security community read it, and what security teams can take from it.

**Parallel AI Enrichment:**

- **Technical Details:** Reported issue was a model jailbreak enabling code‑analysis capability (used routinely by defenders) that triggered a US export‑control directive; specific technical mechanism unavailable.
- **Affected Products:** Claude Fable 5, Claude Mythos 5
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Disable affected models (vendor action). Use lower‑grade Claude models (e.g., Opus 4.x), restrict external/foreign access, monitor vendor advisories, and apply environment‑level controls (access controls, network segmentation, input‑output filters).
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
