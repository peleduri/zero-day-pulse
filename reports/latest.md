# Zero Day Pulse

> **Generated:** 2026-05-26 14:37 UTC &nbsp;|&nbsp; **Total:** 15 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 13 &nbsp;|&nbsp; 🟡 High: 2 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path traversal vulnerability in SimpleHelp (v5.5.7 and earlier) enabling unauthenticated attackers to retrieve logs, configuration files, credentials and potentially gain access to downstream systems.
- **Affected Products:** SimpleHelp remote support software v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true (https://medium.com/@RosanaFS/simplehelp-cve-2024-57727-tryhackme-walkthrough-9f88c2061fb9)
- **Patch Available:** true (http://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570)
- **Active Exploitation:** true (https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a)
- **Threat Actors:** Ransomware actors (e.g., DragonForce)
- **Mitigation:** Apply vendor patch to v5.5.8 immediately; if unable, isolate SimpleHelp RMM from internet, restrict access to management interfaces, apply network segmentation, rotate exposed credentials, enable logging and monitoring, and follow CISA incident response guidance.
- **Vendor Advisory:** http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — Hackers Exploited KnowledgeDeliver Zero-Day for Web Shell Deployment

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://www.securityweek.com/hackers-exploited-knowledgedeliver-zero-day-for-web-shell-deployment/>

> Hardcoded machineKey values in a configuration file enabled ViewState deserialization attacks leading to remote code execution. The post Hackers Exploited KnowledgeDeliver Zero-Day for Web Shell Deployment appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Hard‑coded ASP.NET machineKey values enable attackers who obtain the key to create malicious __VIEWSTATE payloads that bypass validation, causing deserialization and unauthenticated remote code execution; the breach culminates in deployment of in‑memory BLUEBEAM (Godzilla) web shells.
- **Affected Products:** Digital Knowledge KnowledgeDeliver (installations deployed before Feb 24, 2026)
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Unknown specific group; Mandiant reports an "unknown threat actor"
- **Mitigation:** Immediately rotate machineKey to unique cryptographically strong values per instance; restrict external access (IP allowlist); monitor Event ID 1316 and ViewState integrity failures, and hunt for suspicious w3wp.exe child processes and related IOCs.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — Iranian Hackers Deploy MiniFast and MiniJunk V2 via Phishing and SEO Poisoning

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://thehackernews.com/2026/05/iranian-hackers-deploy-minifast-and.html>

> The Iranian state-sponsored threat actor known as Nimbus Manticore (aka Screening Serpens and UNC1549) has been attributed to a fresh campaign using lures impersonating organizations in the aviation and software sectors across the U.S., Europe, and the Middle East following the joint U.S.-Israeli military campaign against the country in late February 2026.

The activity, besides embracing

**Parallel AI Enrichment:**

- **Technical Details:** Campaigns use SEO poisoning and spear/phishing lures to deliver MiniFast (AI‑assisted) and MiniJunk V2 implants. Delivery vectors include malicious links and attachments; implants perform espionage (recon, credential harvesting, persistence) and likely leverage cloud services (reported abuse of Microsoft Azure) for hosting C2 and payloads.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Nimbus Manticore (aka Screening Serpens, UNC1549)
- **Mitigation:** Increase email security and phishing awareness; block known malicious domains and SEO‑poisoned landing pages; implement URL filtering and web proxying; enable EDR/anti‑malware with YARA/signature and behavior detections; disable/limit macros and script execution; apply least‑privilege and multi‑factor authentication; isolate and investigate suspected hosts.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when adversarial content hosted on public web pages or other untrusted sources contains instructions or payloads that an LLM‑powered agent ingests as part of its context, causing it to execute unintended actions (data exfiltration, API key theft, command execution via agent frameworks). Attack vectors include crafted web pages, embedded comments, README files, or other content that agents fetch when following web browsing or tool‑use capabilities.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads
- **Patch Available:** false — https://microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks
- **Active Exploitation:** true — Sources: https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads, http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html
- **Threat Actors:** None known
- **Mitigation:** Implement input provenance controls, remote content filtering, strict instruction parsing, principle of least privilege for agents, sanitize and ignore untrusted web-origin instructions, use model grounding and instruction allowlists/denylists, robust content security policies.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) exploits the ability of large language models to consume data from multiple sources. By inserting crafted malicious instructions into those sources or associated tools, an attacker can steer the model’s output or actions even when the user does not directly provide malicious input.
- **Affected Products:** Google Workspace (Gemini), Gemini CLI
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Apply the latest Google Workspace and Gemini CLI patches, enable Google’s continuous mitigation controls, monitor logs for anomalous prompt activity, and restrict the use of automated agents that can ingest untrusted data.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Chrome's agentic features face "indirect prompt injection": malicious instructions embedded in web content (pages, iframes, UGC) can influence an agent to perform unwanted actions (e.g., transactions, exfiltration). Google describes layered defenses: origin gating, a User Alignment Critic classifier, planner/gating function separation, explicit user confirmations for sensitive actions, Safe Browsing and on‑device scam detection, and work‑logs for transparency.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false.
- **Patch Available:** true; https://blog.google/security/architecting-security-for-agentic/
- **Active Exploitation:** false.
- **Threat Actors:** None known.
- **Mitigation:** Use Google’s layered defenses and hardening: enable the latest Chrome updates with agentic protections; rely on origin gating and user confirmations; monitor Safe Browsing and on‑device protections; follow Google guidance in the vendor advisory; consider blocking agentic browsers in high‑risk environments per Gartner/NCSC guidance.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Google reports that adopting Rust in Android reduced memory‑safety vulnerability density (2025 data shows memory safety vulnerabilities fell below 20% of total vulnerabilities), reflecting a prevention‑first strategy focused on new code; Rust prevents classes of memory‑safety bugs common in C/C++.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Use memory‑safe languages (Rust) for new code, prioritize vulnerability prevention in code changes, continue auditing C/C++ components and apply defensive coding and sanitizers.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack where hidden or external instructions (e.g., in emails, documents, calendar invites, or web content) are crafted to manipulate generative AI systems that ingest external data, causing them to disclose sensitive information or perform unauthorized actions. The mechanism relies on models browsing or ingesting untrusted external content which contains adversarial instructions that the model treats as part of its prompt.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply a layered defense strategy including input provenance and validation (treat external data as untrusted), content filtering and sanitization, model instruction hardening (instruction‑following constraints and refusal policies), strict data access controls and least‑privilege for model actions, rate‑limiting and monitoring for anomalous queries, and use of browser/browsing isolation when allowing models to access web content.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors modify routers to maintain persistent, long‑term access and leverage compromised devices and trusted connections to pivot into other networks.
- **Affected Products:** Backbone routers, Provider Edge (PE) routers, Customer Edge (CE) routers
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Follow CISA’s mitigation guidance: simulate the threat scenarios, apply router hardening best practices, enforce network segmentation, and regularly update firmware.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** true
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS), military unit 26165 (aka APT28)
- **Mitigation:** Follow advisory hardening and detection recommendations (network segmentation, multifactor authentication, patching where applicable, enhanced monitoring/logging, restrict remote access, incident response planning). See vendor advisory for full mitigations.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 11. 🟠 Zero-Day — CISA orders feds to patch actively exploited Drupal vulnerability

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-drupal-vulnerability/>

> CISA has given U.S. government agencies until Wednesday evening to secure their servers against an SQL injection vulnerability in the Drupal content management system (CMS) that it flagged as actively exploited. [...]

---

## 12. 🟠 Zero-Day — KnowledgeDeliver LMS Flaw Exploited to Deploy Godzilla and Cobalt Strike

**CVE:** `CVE-2026-5426` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://thehackernews.com/2026/05/knowledgedeliver-lms-flaw-exploited-to.html>

> A now-patched high-severity security flaw affecting Digital Knowledge KnowledgeDeliver, a Learning Management System (LMS) popular in Japan, was exploited as a zero-day to deliver the Godzilla web shell and ultimately facilitate the deployment of Cobalt Strike Beacon.

The vulnerability, tracked as CVE-2026-5426 (CVSS score: 7.5), stems from the use of hard-coded ASP.NET machine keys, leading to

---

## 13. 🟠 Zero-Day — [SECURITY ADVISORY] CVE-2026-34474 - ZTE H298A/H108N Unauthenticated Admin Credential Exposure

**CVE:** `CVE-2026-34474` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://seclists.org/fulldisclosure/2026/May/20>

> Posted by m.nageh on May 25 -----BEGIN SECURITY ADVISORY----- Advisory ID: MONX-2026-003 CVE ID: CVE-2026-34474 Title: ZTE ZXHN H298A / H108N - Unauthenticated Admin Password &amp; WLAN Credential Exposure Affected: ZTE ZXHN H298A 1.1, ZTE ZXHN H108N 2.6 (EOL; no patch planned) Date: 2026-05-20 Author: Mina Nageh Salalma (Monx Research) Contact: minanageh379 () gmail com Public URL:...

---

## 14. 🟡 High Severity — Microsoft Patches SharePoint RCE Flaw CVE-2026-45659 Across Server Versions

**CVE:** `CVE-2026-45659` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://thehackernews.com/2026/05/microsoft-patches-sharepoint-rce-flaw.html>

> Microsoft has rolled out updates to fix a remote code execution vulnerability impacting SharePoint that could be exploited by bad actors in attacks without requiring any specialized conditions to be met.

The vulnerability, tracked as CVE-2026-45659, carries a CVSS score of 8.8. It has been assigned an important severity.

&quot;Deserialization of untrusted data in Microsoft Office SharePoint allo…

---

## 15. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
