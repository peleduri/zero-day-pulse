# Zero Day Pulse

> **Generated:** 2026-06-14 02:29 UTC &nbsp;|&nbsp; **Total:** 12 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 2 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Directory/path traversal vulnerability allowing access to files outside intended directories (CVE‑2024‑57727 affects SimpleHelp 5.5.7 and earlier).
- **Affected Products:** SimpleHelp Remote Monitoring and Management versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true - https://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570
- **Active Exploitation:** true - https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a
- **Threat Actors:** Ransomware actors (unspecified groups)
- **Mitigation:** Upgrade to SimpleHelp 5.5.8 or later; if immediate patching is not possible, isolate/unexpose SimpleHelp servers from the internet, restrict access, apply network‑level controls, and monitor for suspicious activity.
- **Vendor Advisory:** https://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) abuses the retrieval step in Retrieval‑Augmented Generation (RAG) pipelines: attacker‑controlled data is embedded, retrieved, and concatenated with the LLM prompt, allowing a crafted trigger fragment to steer the model into executing unintended commands or leaking data.
- **Affected Products:** Google Gemini (AI model), Google Bard, other Google AI services using RAG pipelines
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability)
- **Patch Available:** true (https://blog.google/security/prompt-injections-web/)
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply vendor‑provided updates that isolate user‑generated content from prompt instructions, enforce strict validation of retrieved fragments, and monitor for anomalous retrieval patterns. Until patches are applied, restrict external data sources used by RAG pipelines and enable defensive monitoring.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) exploits the model's use of external data sources/tools by embedding adversarial instructions inside those inputs (e.g., crafted email bodies, invites, or documents). In the GeminiJack case, hidden/malicious instructions in shared Workspace artifacts could influence Gemini Enterprise processing without user interaction (zero‑click) to exfiltrate data or change model behavior.
- **Affected Products:** Google Gemini Enterprise integrated in Google Workspace (shared documents, emails, invites, and multi‑source data workflows)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true - http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability
- **Patch Available:** true - https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Google described a layered defense strategy and continuous mitigations for indirect prompt injections in Workspace/Gemini (hardening data ingestion, provenance checks, filtering untrusted content, sandboxing agentic actions, telemetry and monitoring). Noma Labs and other reports recommend disabling or restricting automatic agentic features, applying vendor patches/updates, and restricting shared‑file processing until mitigations are applied.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The primary new threat is indirect prompt injection: malicious site content can influence an agentic browser's AI by providing instructions or content that are incorporated into agent prompts, leading the agent to take unsafe actions.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply Google’s described mitigations: use the vendor‑provided architecture and layered defenses (secondary oversight agent for Gemini, origin access restrictions, capability restriction policies), avoid allowing agentic browsing on untrusted sites, and follow least‑privilege principles for AI capabilities.
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
- **Mitigation:** Adopt memory‑safe languages and practices (Google reports adopting Rust and prioritizing memory‑safety fixes; continuing to convert/new‑code in Rust reduced memory‑safety vulnerabilities below 20% in 2025).
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack where hidden or embedded instructions in external data sources (emails, documents, calendar invites, web content) influence generative AI prompts or responses to cause data exfiltration or unauthorized actions. Attacks exploit the model’s reliance on user‑provided context and external content ingestion, or downstream tool invocation, to inject malicious directives that the model may follow.
- **Affected Products:** Gemini, Google Workspace apps integrating Gemini
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Layered defense strategy including model hardening/safety‑by‑design, purpose‑built ML detectors/classifiers for malicious input, content provenance and provenance‑aware handling, system‑level safeguards and sandboxing for tool execution, strict scoping of model capabilities, and UX‑level confirmations and rate limits. Follow vendor guidance in the Google security blog post.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors target backbone, provider edge (PE), and customer edge (CE) routers and other network devices, often modifying routers and leveraging compromised devices and trusted connections to maintain persistent, long-term access and pivot within networks.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** The advisory describes a long‑running cyber espionage campaign using credential harvesting, spearphishing, exploitation of internet‑facing services, and deployment of custom malware and legitimate tools for reconnaissance and lateral movement against Western logistics and technology companies; specific vulnerability mechanism details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Russian GRU 85th GTsSS (Unit 26165) — tracked as APT28 and related GRU actors.
- **Mitigation:** Apply multi-factor authentication, patch internet-facing services, monitor for provided IOCs, implement network segmentation, restrict administrative privileges, and follow CISA/NSA guidance in the advisory.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Windows 10 (KB5094126), Windows 11 (KB5094126), Microsoft Defender / Microsoft Malware Protection Engine, Exchange Server
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply Microsoft June 2026 security updates (install KB5094126 and associated patches); follow guidance in the Microsoft Security Update Guide. Additionally, harden or limit exposure of Exchange Server and keep Microsoft Defender/Malware Protection Engine up to date.
- **Vendor Advisory:** https://support.microsoft.com/en-us/topic/june-9-2026-kb5094126-os-builds-26200-8655-and-26100-8655-1a9bcba6-5f53-4075-8156-fe11ac631737

---

## 10. 🟠 Zero-Day — US Gov asks Anthropic to ban 'foreign national' access to Fable, Mythos

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-13
**Reference:** <https://www.bleepingcomputer.com/news/security/us-gov-asks-anthropic-to-ban-foreign-national-access-to-fable-mythos/>

> The US government has ordered Anthropic to block all foreign nationals from accessing Fable 5 and Mythos 5, forcing the company to suspend both models worldwide. Anthropic is complying but disputes the basis, calling the cited jailbreak narrow and the capability widely available elsewhere. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Reported issue is a model jailbreak/narrow capability enabling misuse of advanced model outputs; US export‑control directive cited national‑security concerns and ordered suspension of foreign‑national access, prompting Anthropic to disable the models.
- **Affected Products:** Claude Fable 5, Claude Mythos 5
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Anthropic disabled access to the models globally; restrict access to model outputs, monitor for jailbreak prompts, use vetted/trusted‑access programs when available.
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
