# Zero Day Pulse

> **Generated:** 2026-06-08 10:15 UTC &nbsp;|&nbsp; **Total:** 10 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 9 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a directory traversal vulnerability in SimpleHelp remote support software that permits unauthenticated remote attackers to read arbitrary files (e.g., logs, configuration files, credentials) via crafted path strings, enabling reconnaissance and credential theft.
- **Affected Products:** SimpleHelp remote support/remote monitoring and management, versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Ransomware operators (e.g., DragonForce)
- **Mitigation:** Apply the vendor patch/update; if immediate patching is not possible, restrict access to SimpleHelp management interfaces with network ACLs or firewalls, isolate or uninstall vulnerable instances, rotate credentials, review logs for indicators of compromise, and follow CISA guidance.
- **Vendor Advisory:** https://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an attack where adversaries seed external content (web pages, documents, or other retrieval corpora) with instructions or payloads that are later retrieved by AI systems (RAG or agentic) and unintentionally executed as part of the system prompt, causing the model to reveal secrets, execute unauthorized actions, or subvert policy. Examples include HTML/text payloads crafted to override system instructions or to exfiltrate data when included in model inputs.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Harden retrieval and browsing layers: sanitize and filter external content, apply strict provenance/trust scoring, use content policies and model‑level instruction isolation (e.g., separate user/system instructions from retrieved text), restrict model actions, employ heuristic and ML‑based detectors for injection patterns, and monitor for anomalous outputs.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an attacker seeds malicious instructions into data sources or web content that an LLM or AI agent ingests while fulfilling a user query; agentic automation or browsing components can pick up these injected instructions (even without direct user input), causing the model to execute unintended actions or reveal data.
- **Affected Products:** Google Workspace (features integrating Gemini / Gemini in Workspace), Gemini Enterprise
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true — http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability
- **Patch Available:** true — http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html
- **Active Exploitation:** true — http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: content hygiene and filtering for data sources, restricting agentic/browsing capabilities, input/output sanitization, provenance checks, adversarial testing and continuous monitoring, applying vendor updates and configuration guidance from Google.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: malicious or hidden web content provides prompts or sub-tasks that influence the agentic AI in the browser (e.g., hidden DOM elements, cross‑origin content, or attacker‑controlled pages) to alter agent behavior or execute unsafe actions.
- **Affected Products:** Google Chrome (agentic/Gemini integration)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true (http://blog.google/security/architecting-security-for-agentic)
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Use the latest Chrome with agentic security updates; follow Google guidance: restrict agent origin access, enable layered defenses against prompt injection, avoid visiting untrusted sites when using agentic features, and apply organizational policy controls for AI actions.
- **Vendor Advisory:** http://blog.google/security/architecting-security-for-agentic

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Adopting Rust for new Android components eliminates classes of memory‑safety bugs (e.g., use‑after‑free, buffer overflows) by using Rust's ownership/borrow checking and safer memory defaults, resulting in a dramatic reduction of memory‑safety vulnerability density.
- **Affected Products:** Android platform (first‑party and third‑party/open‑source code changes across C, C++, Java, Kotlin, and Rust)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Continue adopting Rust for new Android components, apply Android security updates and patches from Google, and follow standard hardening best practices; no additional workarounds are specified.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection embeds hidden malicious instructions in external data sources (emails, documents, calendar invites, or external image/URL content) that downstream generative AI (e.g., Gemini) may process and act on; attacks can aim to exfiltrate data or execute rogue actions.
- **Affected Products:** Gemini (Gemini in Google Workspace, Gemini app)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Implement layered defenses: adversarial training/model hardening, prompt‑injection content classifiers, security thought reinforcement, markdown sanitization and suspicious‑URL redaction, contextual user confirmation for risky actions, end‑user security notifications; see https://support.google.com/docs/answer/16204578 for guidance.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors target large backbone, provider edge (PE), and customer edge (CE) routers and other network devices; they compromise routers and IoT devices, modify router firmware/configuration to maintain persistent, long-term access, and pivot via trusted connections into other networks.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon; OPERATOR PANDA; RedMike; UNC5807; GhostEmperor
- **Mitigation:** Apply vendor patches and mitigations per CISA advisory; harden network-device configurations, isolate management interfaces, rotate credentials, monitor for signs of unauthorized modifications, apply network segmentation and detection rules.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** The campaign employs spear‑phishing emails, exploitation of internet‑facing services, credential harvesting, custom malware, and other espionage techniques to infiltrate logistics and technology environments and access supply‑chain data.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS), military unit 26165 (APT28)
- **Mitigation:** Implement multi‑factor authentication, enforce least‑privilege access, patch and update internet‑facing systems, monitor logs and network traffic for indicators of compromise, deploy endpoint detection and response (EDR), segment networks, apply denylist/allowlist hardening, and follow the advisory’s IOC and hunting guidance.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟠 Zero-Day — SolarWinds Serv-U Vulnerability Exploited in the Wild

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://www.securityweek.com/solarwinds-patches-exploited-serv-u-vulnerability/>

> Unauthenticated attackers can exploit the flaw via specially crafted POST requests that crash the Serv-U service. The post SolarWinds Serv-U Vulnerability Exploited in the Wild appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated specially crafted POST requests using a Content‑Encoding (e.g., 'deflate') header cause uncontrolled resource consumption and crash the Serv‑U service, resulting in a denial‑of‑service condition.
- **Affected Products:** SolarWinds Serv‑U (Managed File Transfer / Secure FTP) – versions prior to 15.5.4 Hotfix 1
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Immediately upgrade to Serv‑U 15.5.4 Hotfix 1. If patching cannot be applied right away, block or rate‑limit POST requests (especially those with Content‑Encoding: deflate), restrict public access to Serv‑U servers (use VPN or WAF), and monitor for crash events.
- **Vendor Advisory:** https://documentation.solarwinds.com/en/success_center/servu/content/release_notes/servu_15-4-2_release_notes.htm

---

## 10. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-27227 is referenced as an example of DNS parsing vulnerabilities caused by parsing untrusted DNS data in memory‑unsafe code; implementing a memory‑safe Rust DNS parser mitigates that class of vulnerabilities. Further technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Use of memory-safe DNS parser (Rust) in Pixel modem to reduce attack surface; general hardening and firmware updates recommended. Specific mitigation steps unavailable.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html

---
