# Zero Day Pulse

> **Generated:** 2026-05-25 19:15 UTC &nbsp;|&nbsp; **Total:** 11 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 9 &nbsp;|&nbsp; 🟡 High: 2 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path traversal vulnerability in SimpleHelp 5.5.7 and earlier that allows unauthenticated remote attackers to retrieve logs, configuration files, and credentials, potentially leading to high‑privilege access and ransomware deployment.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true – https://medium.com/@RosanaFS/simplehelp-cve-2024-57727-tryhackme-walkthrough-9f88c2061fb9
- **Patch Available:** true – https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know
- **Active Exploitation:** true – https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a
- **Threat Actors:** DragonForce (ransomware actors)
- **Mitigation:** Upgrade SimpleHelp to version 5.5.8 or later; if immediate patching is not possible, isolate/unexpose SimpleHelp servers from the internet, restrict access to management interfaces, rotate exposed credentials, monitor logs for suspicious activity, and apply network‑level filtering.
- **Vendor Advisory:** https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — ⚡ Weekly Recap: Linux Flaws, Defender 0-Days, Router Botnets, and Supply Chain Chaos

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-25
**Reference:** <https://thehackernews.com/2026/05/weekly-recap-linux-flaws-defender-0.html>

> Monday recap. Same mess, new week.

A sketchy dev tool got people pwned, old bugs came back from the dead, and security products somehow needed protecting from themselves. A bunch of companies spent the week checking old boxes and forgotten servers they should&#x27;ve patched years ago. Good times.

Phishing crews are getting smarter too - less obvious scam junk, more targeted stuff that actually

**Parallel AI Enrichment:**

- **Technical Details:** Linux kernel CVE-2026-46333: improper privilege management allowing an unprivileged local user to execute commands as root. Microsoft Defender CVE-2026-41091: privilege escalation to SYSTEM; CVE-2026-45498: denial‑of‑service condition. ASUS router CVE-2018-5999: unauthenticated remote code execution as root via a long‑standing firmware flaw. Drupal Core CVE-2026-9082: SQL injection affecting all supported Drupal versions.
- **Affected Products:** Linux kernel (default installations of Debian, Fedora, Ubuntu), Microsoft Defender, ASUS RT-AC series routers, Drupal Core (all supported versions)
- **CVSS Score:** CVE-2026-46333 (Linux kernel): 5.5; CVE-2018-5999 (ASUS router): 9.8; CVE-2026-9082 (Drupal): 6.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (exploits observed for ASUS router CVE-2018-5999 and Drupal CVE-2026-9082)
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true (exploitation reported for ASUS router CVE-2018-5999 and Drupal CVE-2026-9082)
- **Threat Actors:** RondoDox, RedSun, UnDefend
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) — attackers seed malicious instructions in web content or hidden site code which AI agents that ingest external pages can follow, leading to actions like data exfiltration, fraud, or API key theft.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Harden data ingestion: treat external web content as untrusted, apply sanitization and instruction‑filtering, use strict context separation, prompt integrity checks, allowlisting, rate limits and monitoring; follow vendor hardening advisories (see vendor advisory URL).
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is a class of attacks where attacker‑controlled content in data sources or integrated tools injects malicious instructions that influence an LLM’s behavior when the model processes user queries. IPI can occur without direct user input by poisoning documents, web pages, or third‑party tools that the LLM accesses; the attack leverages the model’s tendency to follow instructions found in input context and tool outputs.
- **Affected Products:** Google Workspace (components using Gemini/GenAI integrations)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true - http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Recommended mitigations include layered defenses: content provenance and validation, input/output sanitization, model instruction filtering, restricting agentic automation where appropriate, limiting external data sources, robust access controls, monitoring for anomalous model behaviors, and continuous updates to detection/filters.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The primary attack class is indirect prompt injection where web content or malicious extensions can manipulate agent prompts or hijack the Gemini panel to escalate privileges, access local files, and perform unsafe actions. Google introduced layered defenses: blocking prompt injections, restricting origin access, and UX controls (work log, user approval) to mitigate automated unsafe agent actions.
- **Affected Products:** Google Chrome (agentic browsing / Gemini integration)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true - https://blog.google/security/architecting-security-for-agentic/
- **Active Exploitation:** true
- **Threat Actors:** None known.
- **Mitigation:** Apply the vendor updates/patches from Google; disable or remove untrusted extensions; restrict agentic browsing features until patched; follow Chrome security blog recommendations (layered defenses, origin restrictions, user controls).
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Near‑miss linear buffer overflow in the Rust‑based CrabbyAVIF library (pre‑release) that was rendered non‑exploitable by Scudo's guard pages, causing the overflow to crash rather than corrupt memory.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — patch: https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use Scudo hardened allocator (guard pages), improve crash reporting to detect overflows into Scudo pages, and expand unsafe‑Rust review and training (encapsulate unsafe, safety comments, deep‑dive training).
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injections embed malicious instructions in external data sources (emails, documents, calendar invites). Google hardened Gemini models (Gemini 2.5) via adversarial training and added runtime defenses — content classifiers to detect/disregard malicious instructions, prompt reinforcement to steer the model away, sanitization/redaction of external resources and suspicious URLs, and user‑confirmation flows to prevent unsafe automated actions.
- **Affected Products:** Gemini (including Gemini 2.5), Gemini in Google Workspace, Gemini app
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — https://blog.google/security/mitigating-prompt-injection-attacks/
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Layered defenses deployed by Google: prompt‑injection content classifiers; security thought reinforcement; markdown sanitization and suspicious URL redaction; user confirmation (HITL) framework; end‑user security mitigation notifications; model hardening via adversarial training.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors compromise routers and IoT devices, modify router configurations/firmware and leverage trusted connections to pivot into networks and maintain long-term persistent access.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Apply network segmentation, restrict management plane access, monitor for anomalous configuration changes, audit internet-facing routers and implement multi-factor authentication and vendor guidance.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable (advisory describes campaign activity and TTPs rather than a single CVE-level vulnerability).
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS) (also tracked under various names).
- **Mitigation:** Implement CISA/NSA recommended mitigations from the joint advisory (e.g., network segmentation, multi-factor authentication, patching of known software, monitoring/logging, restrict administrative access, review remote access configurations, hunt for indicators of compromise provided in the advisory).
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 10. 🟡 High Severity — Ghost CMS CVE-2026-26980 Exploited to Hijack 700+ Sites for ClickFix Attacks

**CVE:** `CVE-2026-26980` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-25
**Reference:** <https://thehackernews.com/2026/05/ghost-cms-cve-2026-26980-exploited-to.html>

> Threat actors are exploiting a recently disclosed critical security flaw in Ghost CMS to inject malicious JavaScript code with an aim to fuel ClickFix attacks.

According to QiAnXin XLab, the activity involves the exploitation of CVE-2026-26980 (CVSS score: 9.4), an SQL injection vulnerability in Ghost&#x27;s Content API that could allow an unauthenticated attacker to read arbitrary data from the

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is an unauthenticated blind SQL injection in Ghost CMS's Content API that allows attackers to send crafted queries and retrieve arbitrary data from the database, including admin API keys.
- **Affected Products:** Ghost CMS v3.24.0 - v6.19.0
- **CVSS Score:** 9.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply the official TryGhost patch immediately. If the patch cannot be applied, restrict public access to the Content API, block suspicious payloads, rotate exposed API and admin keys, and monitor and audit logs for unauthorized activity.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
