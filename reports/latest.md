# Zero Day Pulse

> **Generated:** 2026-06-07 02:14 UTC &nbsp;|&nbsp; **Total:** 14 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 2 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal vulnerability enabling unauthenticated remote attackers to read arbitrary files such as logs, configuration files, and credentials.
- **Affected Products:** SimpleHelp Remote Support/RMM version 5.5.7 and earlier
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know)
- **Active Exploitation:** true (https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a)
- **Threat Actors:** Ransomware actors
- **Mitigation:** Apply the vendor's patch or upgrade to a version newer than 5.5.7, and restrict network access to the SimpleHelp RMM service.
- **Vendor Advisory:** https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — New ChatGPT Lockdown Mode Limits Tools That Could Enable Data Exfiltration

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-06
**Reference:** <https://thehackernews.com/2026/06/new-chatgpt-lockdown-mode-limits-tools.html>

> OpenAI has begun rolling out a new Lockdown Mode to ChatGPT for eligible personal accounts to reduce the risk of data exfiltration arising from prompt injection attacks.

The feature is primarily designed for people and organizations that handle sensitive data and require stricter protection guarantees. Lockdown Mode is available to logged-in users across Free, Go, Plus, and Pro, and

**Parallel AI Enrichment:**

- **Technical Details:** Lockdown Mode limits ChatGPT's ability to access external tools, web browsing, plugins, API calls, and file uploads/downloads, thereby reducing the attack surface for prompt‑injection based data exfiltration.
- **Affected Products:** ChatGPT (web and apps) – Lockdown Mode applies to Free, Go, Plus, and Pro accounts (specific version numbers unavailable)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — https://help.openai.com/articles/20001061
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Enable Lockdown Mode for accounts handling sensitive data, disable third‑party plugins and web access, and avoid sharing secrets in prompts. Follow the OpenAI guidance at https://help.openai.com/articles/20001061.
- **Vendor Advisory:** https://help.openai.com/articles/20001061

---

## 3. 🟠 Zero-Day — AI Agent Uncovers 21 Zero-Days in FFmpeg; Chrome Patches Record 429 Bugs

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-06
**Reference:** <https://thehackernews.com/2026/06/ai-agent-uncovers-21-zero-days-in.html>

> Two things landed within days of each other this week. A security startup reported 21 previously unknown vulnerabilities in FFmpeg, the media library inside almost everything that touches video, all of them found by an autonomous AI agent.

The same week, Google shipped Chrome 149 with patches for 429 security bugs, the most ever in a single release.

Only the FFmpeg bugs were found by AI.

**Parallel AI Enrichment:**

- **Technical Details:** Most of the 21 reported issues are heap or stack overflows in FFmpeg components such as the TS demuxer, VP9 decoder, service‑description‑table parser, and other media parsers, triggered by specially crafted video streams.
- **Affected Products:** FFmpeg (all versions affected by CVE-2026-39210 through CVE-2026-39218 and related fixed issues)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true — https://github.com/DepthFirstDisclosures/ffmpeg-dfvuln127
- **Patch Available:** true — https://www.ffmpeg.org/security.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Update FFmpeg to the latest patched release or apply your distribution's security updates; block untrusted video sources such as RTSP and AV1-over‑RTP until the patches are deployed.
- **Vendor Advisory:** https://www.ffmpeg.org/security.html

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when AI systems process external content (webpages, emails, documents) containing malicious instructions; attackers embed prompts that cause the model to execute unintended actions such as data exfiltration, content manipulation, or command execution. Google scanned public web data using pattern matching, LLM‑based classification, and human validation to find injected prompts. Noma Labs identified a zero‑click IPI (GeminiJack) that exploits Google Gemini Enterprise without user interaction.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses — input validation and filtering, retrieval/result sanitization, least‑privilege for agent capabilities, model hardening and red‑team testing, monitoring/telemetry to detect anomalous agent behavior; follow vendor guidance (Google’s Workspace mitigation post and AI Vulnerability Reward Program) and apply threat intelligence feeds.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) involves inserting malicious instructions into data sources or tools used by an LLM (e.g., webpages, code comments, third‑party data) so the model follows attacker‑supplied instructions during query completion. Chaining IPI with vulnerable tools such as Gemini CLI can lead to command execution or data exfiltration.
- **Affected Products:** Google Workspace (Workspace apps integrating Gemini and other GenAI tools), Gemini CLI (versions prior to 1.3)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Google's layered defenses include input sanitization, content provenance/trust signals, strict tool access policies, runtime prompt filtering, limiting agentic automation privileges, and upgrading Gemini CLI to version 1.3 or later.
- **Vendor Advisory:** http://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: attacker‑controlled web content causes the agent to incorporate malicious text into prompts used by Gemini, enabling malicious instructions or data exfiltration via agentic browsing.
- **Affected Products:** Chrome (agentic/Gemini-enabled builds)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Disable agentic features (auto‑browse/Gemini in Chrome), keep Chrome updated, and follow the guidance in Google’s "Lessons from Defending Gemini Against Indirect Prompt Injections" and related Chrome security posts.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable
- **Affected Products:** Android platform – first‑party and third‑party (open source) code changes across C, C++, Java, Kotlin, and Rust
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Adopt memory‑safe languages such as Rust and harden new code; no specific per‑vulnerability workarounds are provided.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is a class of attacks where hidden or external instructions (in emails, documents, web content, calendar invites, etc.) are crafted to manipulate generative‑AI agents to disclose data or perform unauthorized actions. Attackers embed prompts in external sources consumed by AI pipelines or agents (including web retrieval, plugins, or document ingestion) causing models to follow malicious instructions via dynamic content or multi‑step agent workflows.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Layered defenses — restrict model access to sensitive data (least privilege), sanitize and filter external inputs, treat external content as untrusted, provenance and integrity checks for retrieved data, sandbox agent actions, human review for high‑risk tasks, robust logging and alerting, adversarial testing.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors target and compromise core networking equipment (backbone, PE, CE routers), modify router configuration and firmware to maintain persistent, long‑term access, and leverage trusted connections and compromised devices to pivot deeper into networks
- **Affected Products:** Backbone routers of major telecommunications providers, provider edge (PE) routers, customer edge (CE) routers, and compromised networking devices (specific vendor/product versions not listed in advisory)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Isolate and segment compromised routers; rotate and secure credentials; restrict and monitor management interfaces; apply vendor updates when available; employ network monitoring for anomalous routing and persistent access indicators; follow CISA guidance for simulation and mitigation
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Actors exploit public vulnerabilities such as CVE-2023-38831 in WinRAR and CVE-2020-35730/12641 in Roundcube Webmail to gain initial access. They then use tools like Impacket and PsExec for lateral movement, RDP for remote execution, and dump Active Directory NTDS.dit to steal credentials. Mailbox permission manipulation is employed to sustain email collection and exfiltration.
- **Affected Products:** WinRAR (CVE-2023-38831), Roundcube Webmail (CVE-2020-35730, CVE-2020-12641); additional SOHO device models not specified
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** GRU unit 26165 (APT28, Fancy Bear, Forest Blizzard, BlueDelta)
- **Mitigation:** Employ network segmentation; consider Zero Trust; ensure host firewalls and network security appliances are configured; utilize EDR; apply security patches and firmware updates to all IP cameras; disable remote access if unnecessary; block/alert on NTLM/SMB to external infrastructure; monitor logs; harden Windows features; apply firmware patches to IP cameras.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 11. 🟠 Zero-Day — CISA Adds Actively Exploited SolarWinds Serv-U DoS Flaw to KEV Catalog

**CVE:** `CVE-2026-28318` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-06
**Reference:** <https://thehackernews.com/2026/06/cisa-adds-actively-exploited-solarwinds.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has added a high-severity security flaw impacting SolarWinds Serv-U  multi-protocol file server software to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

The vulnerability, tracked as CVE-2026-28318 (CVSS score: 7.5), is a denial-of-service (DoS) bug that causes the service to crash

---

## 12. 🟠 Zero-Day — Cisco Catalyst SD-WAN Manager CVE-2026-20245 Flaw Actively Exploited – No Patch Available

**CVE:** `CVE-2026-20245` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-06
**Reference:** <https://thehackernews.com/2026/06/cisco-catalyst-sd-wan-manager-cve-2026.html>

> Cisco has warned that a high-severity security flaw impacting Catalyst SD-WAN Manager has come under active exploitation.

The vulnerability, tracked as CVE-2026-20245, carries a CVSS score of 7.8 out of a maximum of 10.0. It affects the following deployment types -


  On-Prem Deployment
  Cisco SD-WAN Cloud-Pro
  Cisco SD-WAN Cloud (Cisco Managed)
  Cisco SD-WAN for Government (FedRAMP)

&quot;A

---

## 13. 🟡 High Severity — Critical Everest Forms Pro flaw exploited to take over WordPress sites

**CVE:** `CVE-2026-3300` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-06
**Reference:** <https://www.bleepingcomputer.com/news/security/critical-everest-forms-pro-flaw-exploited-to-take-over-wordpress-sites/>

> Hackers are actively exploiting a critical vulnerability (CVE-2026-3300) in the Everest Forms Pro plugin, which lets them take complete control of a WordPress website. [...]

---

## 14. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
