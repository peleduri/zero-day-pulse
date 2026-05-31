# Zero Day Pulse

> **Generated:** 2026-05-31 13:10 UTC &nbsp;|&nbsp; **Total:** 9 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 8 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 9

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal vulnerabilities in SimpleHelp 5.5.7 and earlier allow unauthenticated remote attackers to read arbitrary files (e.g., logs, configuration files, credentials), enabling downstream compromise and ransomware intrusion.
- **Affected Products:** SimpleHelp Remote Support / RMM — versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true - https://medium.com/@RosanaFS/simplehelp-cve-2024-57727-tryhackme-walkthrough-9f88c2061fb9
- **Patch Available:** true - http://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570
- **Active Exploitation:** true - https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a
- **Threat Actors:** Ransomware actors; DragonForce ransomware
- **Mitigation:** Apply vendor patch (upgrade to SimpleHelp 5.5.8 or later); isolate/unexpose SimpleHelp from the public internet; implement network segmentation and rotate credentials for potentially compromised accounts; review logs and follow incident‑response guidance.
- **Vendor Advisory:** http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) abuses AI agents that elevate trust/context. An attacker seeds malicious content (e.g., in pull‑requests or web pages) so that when the agent ingests that content into an elevated Claude Code context window, it triggers the "Comment and Control" chain, leading to sandboxed code execution or secret leakage.
- **Affected Products:** Anthropic Claude Code (Claude Code Security Review GitHub Action)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Harden AI agent inputs: do not ingest untrusted web content into elevated‑context windows; apply input filtering and sanitization; restrict elevated capabilities for agents that browse public content; implement strict provenance/origin controls; use sandboxing for code execution; and apply the vendor‑released patch or updated GitHub Action.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack technique that injects malicious instructions into data sources or tools used by LLMs (e.g., documents, webpages, tool outputs, or CI artifacts) so the model executes attacker‑controlled instructions while completing user queries, potentially without direct user input. Specific incidents include injection via GitHub comments and misused Gemini CLI configurations leading to RCE in CI contexts.
- **Affected Products:** Google Workspace with Gemini (general); Gemini CLI (vulnerable versions reported in news – specific versions not listed)
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known.
- **Mitigation:** Defense‑in‑depth approaches: deterministic defenses (user confirmation, URL sanitization, tool‑chaining policies, centralized policy engine and config‑based "point fixes"), ML‑based defenses (synthetic‑data‑driven model retraining), LLM‑based defenses (prompt engineering and model hardening), proactive red‑teaming, AI VRP engagement, and monitoring of public disclosures.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: malicious webpages or third‑party content can inject instructions that an agentic browser (Gemini‑powered agents) may treat as part of its system/user prompt, leading to credential theft or unsafe actions.
- **Affected Products:** Chrome (agentic/Gemini integration)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply Chrome’s updated agentic‑security features (layered defenses described in the vendor advisory), restrict agent browsing permissions, enable user confirmation for sensitive actions, avoid exposing secrets to agent contexts, and keep Chrome updated to the version that includes these mitigations.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Near-miss linear buffer overflow in CrabbyAVIF (unsafe Rust/Ffi-related code); Scudo hardened allocator rendered it non-exploitable via guard pages and converted overflow into a crash; patch committed at https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true (patch: https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050 ; tracked as CVE-2025-48530 in Android security bulletin: https://source.android.com/docs/security/bulletin/2025-08-01)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use Scudo hardened allocator (default on Pixel and many devices); ensure crash reporting highlights Scudo guard-page overflows; apply the CrabbyAVIF patch; follow unsafe Rust review and training recommendations from Google (Comprehensive Rust training updates).
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** IPI hides malicious commands in external data sources (e.g., emails, documents) that, when processed by an LLM, can cause data exfiltration or command execution. Mitigations include model‑level adversarial training, content classifiers, markdown sanitization, suspicious‑URL redaction, user confirmation (HITL), and security notifications. In Cursor, a bypass of the allow‑list allowed arbitrary command execution when chained with IPI, fixed in v1.3.
- **Affected Products:** Google Gemini 2.5, Cursor < 1.3
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Implement prompt‑injection content classifiers, enforce security thought reinforcement, apply markdown sanitization and suspicious‑URL redaction, require user confirmation for high‑risk actions (Human‑In‑The‑Loop), and provide end‑user security mitigation notifications.
- **Vendor Advisory:** https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors exploit publicly known router CVEs to gain initial access, then modify configurations, create virtual containers, insert malicious ACLs, enable unused services, and abuse Guest Shell or script execution to achieve long‑term persistence and lateral movement.
- **Affected Products:** Cisco IOS XE (CVE-2023-20273, CVE-2023-20198, CVE-2018-0171), Ivanti (CVE-2024-21887), Palo Alto PAN‑OS (CVE-2024-3400)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching the listed CVEs; monitor firmware and software integrity; review device logs and configurations for unexpected ACLs, TACACS+/RADIUS external IPs, and unauthorized containers; disable unused ports and protocols; enforce credential hardening and change‑management procedures; follow vendor‑specific hardening guides (e.g., Cisco Guest Shell guidance).
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Outlook NTLM vulnerability allows credential theft via NTLM relay; Roundcube flaws include server‑side request forgery and arbitrary code execution in the webmail interface; WinRAR vulnerability permits execution of malicious code when a crafted archive is opened.
- **Affected Products:** WinRAR, Roundcube, Microsoft Outlook
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) unit 26165 (85th Main Special Service Center)
- **Mitigation:** Collect and monitor Windows logs; Enable attack surface reduction rules; Apply security patches and firmware updates to affected software (WinRAR, Roundcube, Outlook); Disable remote access for IP cameras; Use firewall allowlists; Use VPNs for remote access.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

**Parallel AI Enrichment:**

- **Technical Details:** A malicious DNS response can trigger out-of-bounds reads, writes, and other memory issues in the DNS parser, resulting in memory‑safety vulnerabilities (CVE‑2024‑27227).
- **Affected Products:** Pixel 9 modem firmware, Pixel 10 modem firmware
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Update to the vendor‑provided baseband firmware with the Rust‑based DNS parser/hardening as described in the Google advisory; use network filtering of untrusted DNS responses where possible.
- **Vendor Advisory:** https://blog.google/security/bringing-rust-to-the-pixel-baseband/

---
