# Zero Day Pulse

> **Generated:** 2026-06-07 08:44 UTC &nbsp;|&nbsp; **Total:** 11 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 9 &nbsp;|&nbsp; 🟡 High: 2 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path traversal vulnerability in SimpleHelp Remote Support Software that enables unauthenticated remote attackers to read sensitive files by traversing directories.
- **Affected Products:** SimpleHelp Remote Support Software version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true - https://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors
- **Mitigation:** Update SimpleHelp to version 5.5.8 or later, which contains the security fixes for CVE-2024-57727.
- **Vendor Advisory:** https://www.broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — New ChatGPT Lockdown Mode Limits Tools That Could Enable Data Exfiltration

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-06
**Reference:** <https://thehackernews.com/2026/06/new-chatgpt-lockdown-mode-limits-tools.html>

> OpenAI has begun rolling out a new Lockdown Mode to ChatGPT for eligible personal accounts to reduce the risk of data exfiltration arising from prompt injection attacks.

The feature is primarily designed for people and organizations that handle sensitive data and require stricter protection guarantees. Lockdown Mode is available to logged-in users across Free, Go, Plus, and Pro, and

**Parallel AI Enrichment:**

- **Technical Details:** Lockdown Mode deterministically disables or restricts capabilities that can connect to external services or the web (e.g., browsing, plugins, external tool access) to reduce the attack surface for prompt injection and data exfiltration.
- **Affected Products:** ChatGPT (Free, Go, Plus, Pro) and ChatGPT Business (self‑serve)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** false
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Enable Lockdown Mode in ChatGPT settings (Settings → Safety and security → Advanced security → Lockdown mode). Use Lockdown Mode when handling sensitive data and follow OpenAI guidance on elevated risk labeling and minimizing external integrations.
- **Vendor Advisory:** https://help.openai.com/articles/20001061

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) leverages attacker‑controlled content in external corpora or third‑party sources that are retrieved by RAG or agent components; injected instructions cause downstream models to behave as if given malicious prompts, enabling data exfiltration, credential theft, or command execution in agentic contexts, including zero‑click vectors such as GeminiJack.
- **Affected Products:** Google Gemini Enterprise (GeminiJack zero‑click IPI), agentic AI frameworks and RAG pipelines (e.g., Google Workspace integrations, Anthropic Claude Code, GitHub Copilot Agent)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply vendor multi‑layered safeguards: content sanitization, provenance and authenticity checks, model instruction filtering, hardened RAG retrieval controls, least‑privilege for agent actions, monitoring/telemetry for anomalous behavior, regular updates to summarization and instruction‑following components, agent sandboxing, and restricting external content sources.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) allows an attacker to embed malicious instructions into the data or auxiliary tools used by a large language model, causing the model to execute those instructions and alter its response without any direct user query.
- **Affected Products:** Google Workspace (Gemini integration)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Google employs a continuous, layered defense strategy for Gemini in Workspace—monitoring inputs, sanitizing data, and applying runtime protections to detect and block indirect prompt injection attempts.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is a web‑based attack where malicious page content or third‑party sites provide inputs that manipulate an AI agent’s prompts or behavior; Google’s advisory describes layered defenses to mitigate these attacks in agentic browsing.
- **Affected Products:** Chrome (agentic browsing / Gemini features)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** false
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Deploy Chrome’s new layered defenses (as described by Google): indirect prompt injection mitigations including a monitoring "watcher" agent, origin access restrictions, blocking prompt injections and unsafe AI actions; follow Chrome updates and apply new Chrome releases when available.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true: https://source.android.com/docs/security/bulletin/2026/2026-06-01
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Update devices to the latest Android security patch level (2026-06-05 or later) and enable platform protections such as Google Play Protect; use devices with Scudo allocator where available.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2026/2026-06-01

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection embeds malicious instructions into external data (emails, documents, calendar invites, web content) that are later ingested by an LLM pipeline; when processed, the model may follow the hidden instructions (exfiltration, unauthorized actions) unless defenses (prompt hygiene, contextual provenance, instruction‑whitelisting, output filters) prevent interpretation/execution. Chaining this with CVE‑2025‑54131 can trigger a vulnerable code path, which is fixed in version 1.3.
- **Affected Products:** Google Gemini app, Gemini in Workspace apps (versions prior to Gemini 1.3)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Implement Google's layered defenses: input‑source filtering and provenance checks, strict output redaction and policy‑enforcement layers, model sandboxing/least‑privilege access to sensitive data, telemetry and alerting for anomalous system prompts, and regular model and client updates; apply vendor patch (Gemini 1.3) where available.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors compromise large backbone routers and provider/customer edge routers, leveraging compromised devices and trusted connections to pivot into other networks, and they modify routers to maintain persistent, long‑term access.
- **Affected Products:** Telecommunications backbone routers, provider edge (PE) routers, customer edge (CE) routers, and other compromised network devices
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon (OPERATOR PANDA), RedMike, UNC5805, GhostEmperor, and other PRC state-sponsored actors
- **Mitigation:** Follow CISA AA25-239A mitigation guidance: network segmentation, hardening routers, monitoring for indicators of compromise, removing unauthorized modifications, applying vendor patches when available, limiting administrative access, using multifactor authentication, enabling logging and telemetry, and coordinating incident response.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** true
- **Threat Actors:** GRU 85th GTsSS (Unit 26165) / APT28 (Russian state-sponsored)
- **Mitigation:** Implement network segmentation, multifactor authentication, patch management, monitoring for known TTPs (spearphishing, credential theft), block known malicious IPs/domains, apply CISA/NSA/Cybersecurity advisory recommended mitigations.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟡 High Severity — Critical Everest Forms Pro flaw exploited to take over WordPress sites

**CVE:** `CVE-2026-3300` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-06
**Reference:** <https://www.bleepingcomputer.com/news/security/critical-everest-forms-pro-flaw-exploited-to-take-over-wordpress-sites/>

> Hackers are actively exploiting a critical vulnerability (CVE-2026-3300) in the Everest Forms Pro plugin, which lets them take complete control of a WordPress website. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated remote code execution via insecure handling in Everest Forms Pro allowing arbitrary PHP code injection/execution, leading to full site takeover.
- **Affected Products:** Everest Forms Pro (all versions up to 1.9.12)
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — https://www.wordfence.com/blog/2026/06/attackers-actively-exploiting-critical-vulnerability-in-everest-forms-pro-plugin/
- **Patch Available:** true — vendor patch released but URL unavailable.
- **Active Exploitation:** true — https://www.bleepingcomputer.com/news/security/critical-everest-forms-pro-flaw-exploited-to-take-over-wordpress-sites/; https://www.wordfence.com/blog/2026/06/attackers-actively-exploiting-critical-vulnerability-in-everest-forms-pro-plugin/
- **Threat Actors:** None known
- **Mitigation:** Immediately update Everest Forms Pro to the patched version; if a patch is unavailable, disable or uninstall the plugin, block access to vulnerable plugin files, review logs for webshells, rotate credentials, and restore from clean backups.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
