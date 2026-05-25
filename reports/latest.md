# Zero Day Pulse

> **Generated:** 2026-05-25 14:31 UTC &nbsp;|&nbsp; **Total:** 10 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 8 &nbsp;|&nbsp; 🟡 High: 2 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal vulnerabilities in SimpleHelp versions up to 5.5.7 allow unauthenticated remote attackers to retrieve logs, configuration files, and credentials, potentially gaining elevated access.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** DragonForce
- **Mitigation:** Immediately upgrade SimpleHelp servers to version 5.5.8 or later; if immediate patching is not possible, isolate SimpleHelp servers from the internet, block management ports, rotate stored credentials, audit logs for suspicious activity, and apply network‑level controls.
- **Vendor Advisory:** http://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is a prompt injection where an attacker injects malicious content into a Claude Code context window to trigger unintended behavior.
- **Affected Products:** Claude Code
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is a technique where an attacker injects malicious instructions into data or tools used by an LLM‑powered application (e.g., documents, web content, or third‑party connectors). The LLM may unknowingly execute or follow these instructions while completing user queries, potentially without explicit user input. IPI targets complex AI applications that integrate multiple data sources and agentic automation, manipulating the model via trusted content pipelines rather than direct user prompts.
- **Affected Products:** Google Workspace (Gemini in Workspace and Workspace apps with multiple data sources)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Google's layered defense includes content provenance and filtering, use of retrieval and tool‑use controls, strict access controls for connectors, model behavior guardrails, telemetry and monitoring, and user education. General mitigations: restrict external connectors, validate and sanitize retrieved data, apply provenance and integrity checks, implement rate limits and monitoring for anomalous agent behavior, enforce least‑privilege access, and keep models and tooling updated.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The advisory describes indirect prompt injection (IPI) where web content (malicious pages or third‑party resources) supplies instructions that influence an agentic AI (Gemini in Chrome) to disclose data, perform unsafe actions, or execute unintended behaviors. Attacks chain web‑origin content, prompts, and agentic browsing actions to manipulate the AI’s decision flow or override safety checks.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Chrome introduced layered defenses: prompt‑injection blocking, origin access restrictions, and runtime safeguards to prevent unsafe AI actions (as described in the advisory). Harden web content handling, restrict privileged context exposure, validate and sanitize external inputs, and limit agentic browsing capabilities until patches are applied.
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

- **Technical Details:** Indirect prompt injection (IPI) embeds malicious instructions in external content (webpages, emails, documents, calendar invites, HTML comments, images/URLs). When generative AI systems ingest this content, the hidden instructions can override user intent to exfiltrate data, perform unauthorized transactions, navigate to malicious sites, or corrupt output. Techniques include concealment via CSS/HTML comments, system‑tag spoofing, URL‑based exfiltration, and payment‑instruction payloads.
- **Affected Products:** Gemini (including Gemini in Google Workspace and the Gemini app); specific versions unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known.
- **Mitigation:** Google’s layered defenses include model hardening (Gemini 2.5 adversarial training), prompt‑injection content classifiers, security‑thought reinforcement, markdown sanitization, suspicious URL redaction, user‑confirmation frameworks, end‑user security mitigation notifications, and contextual user confirmations for risky actions. Operational guidance advises applying content filtering, requiring explicit confirmation for destructive actions, monitoring for IPI patterns, and conducting adversarial testing.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** State-sponsored actors target large backbone, provider‑edge (PE), and customer‑edge (CE) routers and leverage compromised devices and trusted connections to pivot; they modify router firmware/configuration to maintain persistent, long‑term access and exfiltrate data for espionage.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Harden and monitor routers and edge devices (network segmentation, restrict management access, change/rotate credentials, implement multifactor for admin access, monitor for configuration changes and anomalous routing behavior, apply vendor patches when available, use EDR/NDR and IOC detection as per CISA advisory).
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** true
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS), military unit 26165
- **Mitigation:** Implement enhanced network monitoring, segment logistics and IT networks, apply least-privilege access controls, enforce multi-factor authentication, maintain up-to-date backups, follow CISA and vendor-specific guidance in the advisory URL above
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟡 High Severity — Ghost CMS CVE-2026-26980 Exploited to Hijack 700+ Sites for ClickFix Attacks

**CVE:** `CVE-2026-26980` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-25
**Reference:** <https://thehackernews.com/2026/05/ghost-cms-cve-2026-26980-exploited-to.html>

> Threat actors are exploiting a recently disclosed critical security flaw in Ghost CMS to inject malicious JavaScript code with an aim to fuel ClickFix attacks.

According to QiAnXin XLab, the activity involves the exploitation of CVE-2026-26980 (CVSS score: 9.4), an SQL injection vulnerability in Ghost&#x27;s Content API that could allow an unauthenticated attacker to read arbitrary data from the

**Parallel AI Enrichment:**

- **Technical Details:** Blind SQL injection in Ghost Content API allows unauthenticated attackers to perform Boolean‑based/time‑based queries against the database via crafted requests, enabling full database read (including admin API keys) and injection of malicious JavaScript to deliver ClickFix attacks.
- **Affected Products:** Ghost CMS Content API v3.24.0 through v6.19.0
- **CVSS Score:** 9.4
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor‑provided security update to upgrade Ghost to a patched version. If patching cannot be performed immediately, block or limit access to Ghost Content API endpoints, deploy WAF rules to block SQL injection patterns, rotate any exposed API keys, audit sites for injected JavaScript, and take compromised sites offline until cleaned.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 10. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

**Parallel AI Enrichment:**

- **Technical Details:** A malicious DNS response can trigger multiple out-of-bounds reads, writes, and other memory‑safety issues in the baseband DNS parser, allowing potential corruption or code execution via crafted DNS responses.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** true
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Deploy vendor‑provided firmware updates; Google replaced the memory‑unsafe DNS parser with a memory‑safe Rust implementation in Pixel 10 baseband firmware to mitigate the class of memory‑safety vulnerabilities. If updates unavailable, block untrusted DNS traffic or use network‑level DNS filtering.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html

---
