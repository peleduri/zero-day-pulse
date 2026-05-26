# Zero Day Pulse

> **Generated:** 2026-05-26 09:34 UTC &nbsp;|&nbsp; **Total:** 15 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 13 &nbsp;|&nbsp; 🟡 High: 2 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal vulnerability allowing unauthenticated remote attackers to retrieve arbitrary files (e.g., logs, configuration files, credentials) from the SimpleHelp server.
- **Affected Products:** SimpleHelp version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (https://medium.com/@RosanaFS/simplehelp-cve-2024-57727-tryhackme-walkthrough-9f88c2061fb9)
- **Patch Available:** true (http://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570)
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Upgrade SimpleHelp to version 5.5.8 or later; restrict network access to the RMM service until patched.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 2. 🟠 Zero-Day — Iranian Hackers Deploy MiniFast and MiniJunk V2 via Phishing and SEO Poisoning

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://thehackernews.com/2026/05/iranian-hackers-deploy-minifast-and.html>

> The Iranian state-sponsored threat actor known as Nimbus Manticore (aka Screening Serpens and UNC1549) has been attributed to a fresh campaign using lures impersonating organizations in the aviation and software sectors across the U.S., Europe, and the Middle East following the joint U.S.-Israeli military campaign against the country in late February 2026.

The activity, besides embracing

**Parallel AI Enrichment:**

- **Technical Details:** Campaign uses SEO poisoning and phishing lures impersonating aviation and software organizations to deliver MiniFast (AI‑assisted) and MiniJunk V2 malware. Distribution is via malicious search results, phishing emails with links/attachments, and cloud‑hosted installers/C2 on platforms like Azure. Payloads focus on espionage, data collection, and persistence.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Nimbus Manticore (aka Screening Serpens, UNC1549)
- **Mitigation:** Block known malicious domains/URLs, implement phishing‑resistant MFA, apply email filtering and URL rewriting/ATP, endpoint detection and response with YARA/signature for MiniFast/MiniJunk, restrict execution of unsigned installers, network egress filtering to known C2, user training, and monitor for indicators of compromise from published reports.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — ⚡ Weekly Recap: Linux Flaws, Defender 0-Days, Router Botnets, and Supply Chain Chaos

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-25
**Reference:** <https://thehackernews.com/2026/05/weekly-recap-linux-flaws-defender-0.html>

> Monday recap. Same mess, new week.

A sketchy dev tool got people pwned, old bugs came back from the dead, and security products somehow needed protecting from themselves. A bunch of companies spent the week checking old boxes and forgotten servers they should&#x27;ve patched years ago. Good times.

Phishing crews are getting smarter too - less obvious scam junk, more targeted stuff that actually

**Parallel AI Enrichment:**

- **Technical Details:** Two local privilege escalation vulnerabilities (CVE-2026-43284 and CVE-2026-43500) allow an unprivileged local user to gain root by abusing kernel networking and memory‑fragment handling in the xfrm/ESP (esp4, esp6) and rxrpc subsystems, leading to corrupted state and privilege escalation.
- **Affected Products:** Linux kernel xfrm/ESP fragmentation handling (esp4, esp6) and rxrpc subsystems; kernel versions prior to May 2026 patches
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true (http://darkreading.com/vulnerabilities-threats/dirty-frag-exploit-blow-up-enterprise-linux-distros, https://nsfocusglobal.com/linux-kernel-privilege-escalation-vulnerability-dirty-frag-alert/)
- **Patch Available:** true (http://canonical.com/blog/dirty-frag-linux-vulnerability-fixes-available, http://ubuntu.com/blog/dirty-frag-linux-vulnerability-fixes-available)
- **Active Exploitation:** true (http://darkreading.com/vulnerabilities-threats/dirty-frag-exploit-blow-up-enterprise-linux-distros, http://socprime.com/active-threats/dirty-frag-linux-vulnerability-analysis)
- **Threat Actors:** None known
- **Mitigation:** Apply the kernel patches released by the distributions immediately. If patching cannot be done promptly, limit untrusted local access, remove unnecessary setuid binaries, enforce container/VM isolation, and consider disabling the affected xfrm/ESP and rxrpc subsystems.
- **Vendor Advisory:** http://canonical.com/blog/dirty-frag-linux-vulnerability-fixes-available

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) tricks agents by placing maliciously crafted prompts or instructions in external web content (e.g., comments, README, web pages) that agents retrieve and execute, causing them to follow attacker‑supplied instructions or expose sensitive data. The "Comment and Control" chain weaponized agent elevated access and ability to process untrusted user content.
- **Affected Products:** Anthropic Claude Code (Claude Code Security Review), agent runtimes that ingest web content
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (source: https://sentinelone.com/vulnerability-database/cve-2026-39861)
- **Patch Available:** true (source: https://truefoundry.com/blog/claude-code-prompt-injection)
- **Active Exploitation:** true (sources: https://blog.google/security/prompt-injections-web/, https://sentinelone.com/vulnerability-database/cve-2026-39861)
- **Threat Actors:** None known
- **Mitigation:** Harden AI agent ingestion and isolation, treat web content as untrusted, sanitize/whitelist sources, limit agent elevated access, enforce runtime policy controls and provenance checks.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack technique where adversaries inject malicious instructions into data sources or tools consumed by an LLM (e.g., web content, documents, or integrated tool outputs) so the model follows these instructions during user query processing. IPI can occur without direct user input and exploits agentic automation and multi‑source retrieval behaviors in complex LLM‑enabled applications.
- **Affected Products:** Google Workspace products using Gemini integrations (Workspace with Gemini and Gemini-in-Workspace integrations)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Google recommends a layered defense including content filtering, source trust and provenance checks, model response validation, restricting agentic tool actions, principle‑of‑least‑privilege for tool/data access, user‑visible provenance indicators, continuous monitoring and telemetry, and rapid patching/response processes.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The primary new threat facing all agentic browsers is indirect prompt injection. Malicious instructions embedded in web content, iframes, or user‑generated content can cause the agent to take unwanted actions such as financial transactions or data exfiltration. Chrome mitigates this with a user‑alignment critic, origin‑set gating, a real‑time prompt‑injection classifier, and user confirmations for sensitive actions.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — https://blog.google/security/architecting-security-for-agentic/
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Use the latest Chrome updates (auto‑update delivers fixes). Enable agentic features only when needed and monitor work logs; rely on Chrome’s origin isolation, user confirmations, and Safe Browsing. For researchers, follow the updated Vulnerability Rewards Program guidelines and report issues to Google.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2025-68260 is a critical race condition in the Rust implementation of the Android Binder subsystem inside the Linux kernel, allowing potentially unsafe concurrent access that could be exploited to achieve memory‑corruption or privilege escalation.
- **Affected Products:** Android operating system (Rust‑based Binder subsystem), Linux kernel (Rust implementation)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-12-01

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack vector where hidden or malicious instructions embedded in external content (emails, documents, calendar invites, websites, third‑party data) manipulate generative AI models to exfiltrate data or perform unauthorized actions. The attack relies on the model processing untrusted content that contains covert commands.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Use a layered defense — validate content provenance, apply input sanitization and output filtering, restrict model access to sensitive data, implement telemetry/monitoring for anomalous model behavior, use allowlists/denylists for external sources, and apply continuous updates to detection rules.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state‑sponsored actors compromise large backbone routers (telecom PE/CE), modify router firmware or configuration to maintain persistent, long‑term access, leverage compromised devices and trusted connections to pivot into other networks, and use these footholds for espionage and lateral movement.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon (UNC4841/Volt Typhoon), OPERATOR PANDA, RedMike, UNC5807, GhostEmperor, and other PRC state‑sponsored actors
- **Mitigation:** Prioritize discovery and isolation of compromised infrastructure (especially routers), apply vendor‑recommended mitigations and firmware updates where available, rotate credentials and keys, segment networks and restrict privileged access, monitor for indicators of compromise and unusual routing/telemetry, implement robust logging and multi‑factor authentication, and follow CISA’s specific response playbooks.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS), military unit 26165 (aka APT28)
- **Mitigation:** Apply standard hardening: implement multi-factor authentication, network segmentation, endpoint detection and response, monitor for anomalous access, patch and inventory systems, restrict privileged access, and follow CISA/NSA joint advisory detection and mitigation guidance.
- **Vendor Advisory:** Vendor advisory URL unavailable.

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

## 14. 🟡 High Severity — Ghost CMS CVE-2026-26980 Exploited to Hijack 700+ Sites for ClickFix Attacks

**CVE:** `CVE-2026-26980` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-25
**Reference:** <https://thehackernews.com/2026/05/ghost-cms-cve-2026-26980-exploited-to.html>

> Threat actors are exploiting a recently disclosed critical security flaw in Ghost CMS to inject malicious JavaScript code with an aim to fuel ClickFix attacks.

According to QiAnXin XLab, the activity involves the exploitation of CVE-2026-26980 (CVSS score: 9.4), an SQL injection vulnerability in Ghost&#x27;s Content API that could allow an unauthenticated attacker to read arbitrary data from the

---

## 15. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
