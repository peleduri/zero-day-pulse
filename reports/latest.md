# Zero Day Pulse

> **Generated:** 2026-05-25 02:09 UTC &nbsp;|&nbsp; **Total:** 10 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 8 &nbsp;|&nbsp; 🟡 High: 2 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path traversal vulnerability in SimpleHelp Remote Monitoring and Management that enables attackers to retrieve logs, configuration files, and credentials from the target system.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true; https://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570
- **Active Exploitation:** true
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Update SimpleHelp RMM to version 5.5.8 or later. If immediate patching is not possible, restrict external network access to the SimpleHelp service and monitor for suspicious file access.
- **Vendor Advisory:** https://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (ShareLeak) allows untrusted external content to influence AI‑agent prompts or shared contexts, leading to unintended command execution or data exfiltration.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor patch; implement input validation, content filtering, and use least‑privilege service accounts.
- **Vendor Advisory:** https://nvd.nist.gov/vuln/detail/CVE-2026-21520

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack technique where malicious instructions are injected into data sources or tools that a complex AI application (e.g., Workspace with Gemini) consumes while answering user queries. These instructions are embedded in external content (web pages, documents, APIs) and can influence model behavior, enabling actions such as data exfiltration, command execution, or API key theft.
- **Affected Products:** Google Workspace (Gemini in Workspace and related GenAI integrations); other LLM‑powered multi‑source agent platforms
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Google's layered defenses include continuous detection of IPI patterns, sanitizing and validating external content, limiting autonomous tool invocation, applying contextual policy enforcement, and telemetry/alerting to detect anomalous agent behavior. Vendors also recommend hardening data‑source trust boundaries, content filtering, and reducing overuse of autonomous tool invocation.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: web content (visible or hidden) contains crafted text/URLs/inputs that are interpreted by an agentic browser’s LLM or agent planner as instructions, causing unintended actions or data exfiltration. Attack vectors include malicious page content, URLs, query parameters, hidden iframes, form fields, and third‑party scripts that influence agent prompts or chain instructions across navigations.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Implement Chrome’s agentic mitigations: site-level permission controls for agent actions, action confirmations for sensitive operations, content sanitization and input validation, heuristics to detect and ignore prompt-like content (alignment critic), restrict navigations and automated form submissions, network-level and extension hardening, and user-awareness warnings.
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
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection attacks embed malicious instructions in external data sources (emails, documents, calendar invites, images/URLs). Google’s mitigations combine model‑level robustness (adversarial training), content classifiers that detect malicious instructions, prompt‑level “security thought reinforcement” to keep LLMs focused on user tasks, sanitization/redaction of external resources, suspicious‑URL detection, and human‑in‑the‑loop confirmations to prevent unauthorized actions.
- **Affected Products:** Gemini (Gemini in Google Workspace, Gemini app)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Layered defenses including Gemini 2.5 model hardening (adversarial training), purpose-built ML content classifiers, security thought reinforcement, markdown sanitization and external image/URL redaction (suspicious URL detection via Google Safe Browsing), user confirmation (HITL) for risky actions, end‑user security notifications and Help Center guidance.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors modify routers (unauthorized commands, firmware/configuration changes) to maintain persistent, long‑term access and then pivot via trusted connections to lateral networks, targeting backbone, provider edge (PE) and customer edge (CE) routers as well as compromised SOHO/IoT devices.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon; OPERATOR PANDA; RedMike; UNC5807; GhostEmperor
- **Mitigation:** Inventory and isolate compromised devices, restrict management‑plane access, implement strong authentication and logging, apply vendor hardening recommendations, rotate credentials, monitor for anomalous configuration changes and traffic, block malicious C2 communications, and harden network segmentation.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

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
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS), military unit 26165 (aka APT28/Fancy Bear)
- **Mitigation:** Follow CISA advisory recommended mitigations (general hardening, network segmentation, multifactor authentication, logging and monitoring).
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟡 High Severity — Ghost CMS SQL injection flaw exploited in large-scale ClickFix campaign

**CVE:** `CVE-2026-26980` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-05-24
**Reference:** <https://www.bleepingcomputer.com/news/security/ghost-cms-sql-injection-flaw-exploited-in-large-scale-clickfix-campaign/>

> A large-scale campaign is exploiting a critical SQL injection vulnerability (CVE-2026-26980) in Ghost CMS to inject malicious JavaScript code that triggers ClickFix attack flows. [...]

**Parallel AI Enrichment:**

- **Technical Details:** An unauthenticated blind SQL injection in the Ghost CMS Content API allows attackers to craft queries that read arbitrary data from the database; the injected payload can then deliver malicious JavaScript (ClickFix) to victims.
- **Affected Products:** Ghost CMS Content API versions v3.24.0-6.19.0
- **CVSS Score:** 9.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true: https://www.bleepingcomputer.com/news/security/ghost-cms-sql-injection-flaw-exploited-in-large-scale-clickfix-campaign/
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** XLab (Qianxin)
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://github.com/advisories/GHSA-w52v-v783-gw97

---

## 10. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

**Parallel AI Enrichment:**

- **Technical Details:** A malicious DNS response can trigger out‑of‑bounds reads, writes, and other memory corruption in the Pixel baseband's DNS processing code.
- **Affected Products:** Google Pixel 9, Google Pixel 10
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Update Pixel devices to the latest baseband firmware released in the Google Security Blog post; the update incorporates a Rust‑based memory‑safe DNS implementation.
- **Vendor Advisory:** https://blog.google/security/bringing-rust-to-the-pixel-baseband/

---
