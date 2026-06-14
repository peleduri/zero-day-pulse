# Zero Day Pulse

> **Generated:** 2026-06-14 09:01 UTC &nbsp;|&nbsp; **Total:** 12 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 2 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is a directory traversal allowing unauthenticated remote attackers to read arbitrary files (e.g., logs, configuration files, credentials) on SimpleHelp versions 5.5.7 and earlier.
- **Affected Products:** SimpleHelp Remote Support Software version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (unspecified groups) have been reported exploiting this vulnerability.
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when adversarial content in external corpora (web pages, search results, retrieved documents) contains instructions that, when ingested by LLMs or agentic systems (including RAG pipelines and browser‑enabled agents), override or influence model behavior to perform unauthorized actions. Attacks use poisoned documents, crafted payloads, or deceptive formatting to inject prompts into the retrieval pipeline, leading to data exfiltration, execution of malicious instructions, or bypassing of safeguards.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Hardening and mitigations recommended: restrict browsing to trusted sources, sanitize retrieved content before feeding to models, use retrieval filters, add instruction poisoning detection and allowlisting, and deploy RAG/agent safety checks (vendor blog recommends proactive monitoring).
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) enables adversaries to embed malicious instructions into external data sources or tools consumed by LLM‑based services (e.g., documents, search results, connectors). When the LLM processes user queries that incorporate that tainted data, the injected instructions can influence model behavior, potentially exfiltrating data or performing unauthorized actions. GeminiJack is a zero‑click IPI that exploits service integrations to trigger model behavior without direct user input.
- **Affected Products:** Google Workspace with Gemini integrations (Workspace with Gemini, Gemini Enterprise, Vertex AI Search)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply layered defenses per Google’s guidance: input sanitization and content filtering, contextual integrity checks, tool and connector hardening, strict access controls and least privilege, logging and monitoring, rate limiting, and model‑level instruction filtering. Follow the Google Workspace advisory recommendations.
- **Vendor Advisory:** http://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection targeting Chrome’s agentic (Gemini) browsing can supply malicious content or instructions from a web origin that an agent then interprets as trusted input, causing the agent to perform unsafe actions (exfiltrate API keys/credentials, follow attacker‑controlled instructions, or access restricted origins). Attacks chain web‑origin content into agent prompts (zero‑click variants reported) to hijack agentic flows.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** true — http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Chrome implemented layered defenses: restrict origin access for agent actions, add prompt‑injection filters/sanitization, limit agent capabilities by default, require explicit user consent for sensitive actions, and harden cross‑origin fetch/access controls. Users should update Chrome to the latest stable release and disable agentic features if not needed.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A race condition in the Rust‑implemented Android Binder driver (rust_binder) can corrupt memory, resulting in crash‑class behavior and potential privilege escalation.
- **Affected Products:** Android operating system (Rust‑based Binder driver)
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

- **Technical Details:** Indirect prompt injection (IPI) involves embedding hidden malicious instructions in external data sources (emails, documents, calendar invites) that are later incorporated into AI prompts, causing the model to execute unintended actions like data exfiltration or command execution.
- **Affected Products:** Google Gemini app, Google Gemini in Workspace apps
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply layered input sanitization, use provenance signals to verify data origin, harden the model against malicious prompts, and enforce workspace‑level controls as described in Google’s advisory.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** APT actors gain initial access by exploiting publicly known CVEs and weak/default credentials on Internet‑exposed edge/network devices (routers, provider‑edge/customer‑edge). They then modify device configurations (ACLs, add accounts, enable services/ports), abuse Guest Shell/IOx containers, run scripts (TCL, Python), enable traffic mirroring (SPAN/RSPAN/ERSPAN) and create tunnels to exfiltrate data.
- **Affected Products:** Cisco IOS, Cisco IOS XE (including Guest Shell/IOx), Ivanti Connect Secure, Ivanti Policy, Fortinet firewalls, Juniper firewalls, Microsoft Exchange, Nokia routers/switches, Sierra Wireless devices, SonicWall
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** true — https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching Internet‑exposed network devices (address CVEs listed in Appendix B); monitor and verify firmware/software integrity (hash checks); audit configurations and logs for unexpected ACLs, AAA changes, opened ports, packet mirroring, virtual containers; disable unused ports/protocols and outbound management connections; enforce strong credentials and public‑key authentication; follow vendor hardening guides (e.g., Cisco IOS/XE hardening) and integrity tools.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Exploitation of Outlook NTLM authentication (CVE-2023-23397) allows credential theft via crafted emails. Roundcube vulnerabilities (CVE-2020-12641, CVE-2020-35730, CVE-2021-44026) provide remote code execution through malicious web payloads. WinRAR (CVE-2023-38831) enables arbitrary code execution when a crafted archive is opened.
- **Affected Products:** Microsoft Outlook (CVE-2023-23397), Roundcube (CVE-2020-12641, CVE-2020-35730, CVE-2021-44026), WinRAR (CVE-2023-38831)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Russian GRU (unit 26165), also identified as APT28
- **Mitigation:** Deploy endpoint detection and response (EDR) solutions, collect and monitor Windows event logs, enable Windows attack surface reduction rules, change default credentials, disable weak protocols (e.g., NTLM), audit and secure IP cameras, and monitor VPN and proxy services.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-45586 is an elevation‑of‑privilege flaw in the Windows Collaborative Translation Framework. CVE-2026-50507 is a security‑feature‑bypass issue in BitLocker. CVE-2026-44815, CVE-2026-45648, and the Outlook/Word issues are stack‑based buffer overflows that allow unauthenticated or domain‑authenticated remote code execution.
- **Affected Products:** Windows Collaborative Translation Framework, Windows BitLocker, DHCP Client Service, Windows Active Directory Domain Services, Microsoft Outlook, Microsoft Word
- **CVSS Score:** 7.8, 6.8, 9.8, 8.8, 8.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/)
- **Patch Available:** true (https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Audit and restrict applications that call the vulnerable APIs (e.g., DHCP client API); apply defensive configuration and limit privileged access where possible.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45586

---

## 10. 🟠 Zero-Day — US Gov asks Anthropic to ban 'foreign national' access to Fable, Mythos

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-13
**Reference:** <https://www.bleepingcomputer.com/news/security/us-gov-asks-anthropic-to-ban-foreign-national-access-to-fable-mythos/>

> The US government has ordered Anthropic to block all foreign nationals from accessing Fable 5 and Mythos 5, forcing the company to suspend both models worldwide. Anthropic is complying but disputes the basis, calling the cited jailbreak narrow and the capability widely available elsewhere. [...]

**Parallel AI Enrichment:**

- **Technical Details:** The incident involves a narrow jailbreak capability referenced by the U.S. government as the basis for an export‑control directive; Anthropic disputes the claim and says the capability is widely available elsewhere, with no public CVE, PoC, or detailed technical disclosure.
- **Affected Products:** Claude Fable 5, Claude Mythos 5
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Anthropic disabled Claude Fable 5 and Claude Mythos 5 for all customers; users should follow the vendor guidance and use lower‑capability models or alternative providers until the directive is resolved.
- **Vendor Advisory:** https://www.anthropic.com/news/claude-fable-5-mythos-5

---

## 11. 🟡 High Severity — Critical Splunk Enterprise Flaw Lets Attackers Run Code Without Authentication

**CVE:** `CVE-2026-20253` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-13
**Reference:** <https://thehackernews.com/2026/06/critical-splunk-enterprise-flaw-lets.html>

> Splunk has released security updates to address a critical security flaw in Splunk Enterprise that could be exploited to conduct unauthenticated file operations and even remote code execution.

The vulnerability, tracked as CVE-2026-20253, is rated 9.8 on the CVSS scoring system.

&quot;In Splunk Enterprise versions below 10.2.4 and 10.0.7, an unauthenticated user could create or truncate arbitrar…

---

## 12. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
