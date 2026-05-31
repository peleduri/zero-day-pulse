# Zero Day Pulse

> **Generated:** 2026-05-31 08:34 UTC &nbsp;|&nbsp; **Total:** 9 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 8 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 9

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated path traversal vulnerabilities in SimpleHelp v5.5.7 and earlier enable remote attackers to retrieve server logs, configuration files, and credentials, which can be leveraged to gain privileged access to downstream customer environments.
- **Affected Products:** SimpleHelp remote support / RMM software – versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** DragonForce and unspecified ransomware actors
- **Mitigation:** Immediately upgrade to SimpleHelp v5.5.8; restrict or block external access to SimpleHelp administration interfaces; apply network segmentation; rotate credentials and secrets; review logs and indicators of compromise per vendor guidance.
- **Vendor Advisory:** https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) seeds malicious instructions into web content or hidden site elements so AI agents that browse or ingest that content incorporate the attacker‑controlled instructions into their prompts or workflows. Attackers can hide payloads in comment tags, ASCII art, or invisible elements; when an AI agent fetches and synthesizes page content to form prompts or system instructions, the injected content can override intended instructions or cause privileged actions.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Restrict or disable automated web browsing by agents; sanitize and canonicalize fetched web content before using in prompts; apply least privilege to agent actions and separate privileged capabilities from untrusted content; use system cards, prompt templates, and input validation; monitor for anomalous agent behavior and treat web content as untrusted.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack technique that injects malicious instructions into data or tools consumed by an LLM (e.g., web pages, documents, tool outputs), causing the LLM to follow attacker instructions instead of the user's intent. It leverages multi‑source agentic workflows and can occur without direct user input.
- **Affected Products:** Google Workspace with Gemini (general — specific versions unavailable)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Defense‑in‑depth combining deterministic defenses (user confirmation, URL sanitization, tool chaining policies), ML‑based defenses retrained with synthetic attack data, LLM model hardening, automated and human red‑teaming, and policy/config updates (regex takedowns, centralized policy engine). Specific vendor guidance is in the advisory link above.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: malicious web pages, iframes, or user‑generated content embed prompts or instructions that are fed to the agentic model’s planner, causing it to execute unwanted actions such as financial transactions or credential exfiltration. Chrome mitigates this by limiting content exposure, using origin‑based gating, and running a real‑time classifier to block injected prompts.
- **Affected Products:** Google Chrome – agentic browsing / Gemini integration
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — https://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** User Alignment Critic (trusted vetting model), Agent Origin Sets (read‑only and read‑writable gating), deterministic user confirmations for sensitive actions, real‑time indirect prompt‑injection classifier, on‑device Safe Browsing/AI checks, continuous red‑team testing and VRP updates.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow in the CrabbyAVIF component of Android, mitigated by the Scudo hardened allocator which placed guard pages around secondary allocations, rendering the flaw non‑exploitable.
- **Affected Products:** CrabbyAVIF (Android)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Apply the CrabbyAVIF patch from the Android Open Source Project and ensure the Scudo hardened allocator is enabled on the device.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) hides malicious instructions in external data sources such as emails, documents, or calendar invites. When a generative AI model processes this content, the embedded instructions can cause the model to exfiltrate data, execute rogue actions, or otherwise compromise security. Google mitigates this through adversarial training of Gemini 2.5, content classifiers for various formats, markdown sanitization to block image‑based exfiltration, and Safe Browsing‑based URL redaction.
- **Affected Products:** Gemini (Google Workspace and Gemini app) – Gemini 2.5
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: adversarial training of Gemini 2.5, proprietary prompt‑content classifiers, markdown sanitizer to block external image URLs, Safe Browsing‑based suspicious URL detection and redaction, contextual user confirmation for risky actions, end‑user security notifications and Help Center guidance, adversarial testing/red‑team exercises, AI VRP engagement, industry partnerships (CoSAI), and ongoing model improvements.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors target internet‑facing network appliances, modify router firmware or configurations to gain persistent, long‑term access, and use these compromised devices to pivot deeper into victim networks.
- **Affected Products:** Cisco, Palo Alto, Ivanti, Fortinet, Juniper, Microsoft Exchange
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Apply available vendor patches, restrict internet‑facing access to routers and switches, implement strict configuration monitoring, and use network segmentation to limit lateral movement.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** GRU 85th Main Special Service Center (85th GTsSS), military unit 26165 (aka APT28)
- **Mitigation:** Apply standard hardening and detection guidance from the advisory (network segmentation, multifactor authentication, privilege restriction, endpoint detection and response, patching of known vendor products); see advisory for details.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

**Parallel AI Enrichment:**

- **Technical Details:** A malicious DNS response can trigger out‑of‑bounds reads, writes, and other memory issues in the modem DNS parser, enabling memory‑safety vulnerabilities in the baseband.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** true — https://source.android.com/security/bulletin/pixel/2024-03-01
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Install the vendor security update from the Android/Pixel security bulletin; as a long‑term hardening measure Google implemented a Rust‑based DNS parser in Pixel modem firmware (see Google Security Blog).
- **Vendor Advisory:** https://source.android.com/security/bulletin/pixel/2024-03-01

---
