# Zero Day Pulse

> **Generated:** 2026-06-01 02:31 UTC &nbsp;|&nbsp; **Total:** 9 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 8 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 9

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal (directory traversal) vulnerabilities in the SimpleHelp web interface allow unauthenticated remote attackers to retrieve arbitrary files, such as logs, configuration files, and credentials, by requesting crafted paths that escape the intended directory.
- **Affected Products:** SimpleHelp remote support software v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true - https://www.offsec.com/blog/cve-2024-57727/
- **Patch Available:** true - http://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors
- **Mitigation:** Upgrade to SimpleHelp 5.5.8 or later; if immediate patching is not possible, restrict access to SimpleHelp instances via network segmentation, firewall rules, and disabling public access; rotate credentials, review logs, and apply least‑privilege and monitoring controls.
- **Vendor Advisory:** http://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) involves placing malicious prompt fragments in user‑controlled data (e.g., web pages, documents) that are later fed to an AI model, causing the model to execute the injected instructions as if they were legitimate. This can manipulate the AI’s behavior, leak information, or trigger actions such as remote code execution in integrated agent frameworks.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Implement strict input validation and sanitization for any data fed to LLMs, apply instruction‑level filtering to block malicious prompts, isolate AI model calls in sandboxed environments, and monitor model outputs for anomalous behavior. Deploy layered defenses as described by Google’s new safeguards.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) targets LLM‑based applications that combine multiple data sources and tools by injecting malicious instructions into the data or tools the LLM consumes during query completion, potentially influencing model behavior without direct user input.
- **Affected Products:** Google Workspace with Gemini (general; specific versions unavailable)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Layered defenses including data-source vetting, input/output filtering, sanitization of external content, privilege separation for tools/agents, monitoring and anomaly detection, and continuous updates to model/tooling per Google’s continuous approach.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The primary new threat facing all agentic browsers is indirect prompt injection (IPI). Malicious or user‑generated web content can influence an agent to take unwanted actions (e.g., financial transactions or data exfiltration). Chrome mitigates this with a User Alignment Critic, Agent Origin Sets, deterministic URL checks, a real‑time IPI detection classifier, user confirmations for sensitive actions, and continuous red‑teaming.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true — Patch/advisory URL: https://blog.google/security/architecting-security-for-agentic/
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Deploy layered defenses: User Alignment Critic, origin gating (read‑only vs read‑write sets), deterministic URL checks, a prompt‑injection classifier, user confirmations for sensitive actions, Safe Browsing integration, continuous red‑teaming, and updated VRP guidance. If a formal patch is needed, Chrome auto‑update delivers fixes.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** The report attributes reductions in memory‑safety vulnerabilities (use‑after‑free, buffer overflows, etc.) by adopting Rust in Android components; the underlying mechanism is prevention of memory‑safety bugs via Rust’s ownership/borrow checker rather than runtime patches.
- **Affected Products:** Android platform (first‑party and third‑party/open‑source components across C, C++, Java, Kotlin, Rust)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — https://source.android.com/docs/security/bulletin/2025-11-01, https://source.android.com/docs/security/bulletin/2025-12-01
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply official Android Security Bulletin updates; prefer memory‑safe languages (Rust) for new code; follow Google hardening guidance in the blog post.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) embeds hidden malicious instructions within external data sources (emails, documents, calendar invites) that can influence AI agents; Google describes a layered defense across the prompt lifecycle including training with adversarial data, input sanitation, agent‑side policies, and runtime controls to detect and block IPI.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply layered defenses — sanitize and validate external content, use model and system‑level adversarial training, enforce least‑privilege data access for agents, implement runtime filtering and policy enforcement, monitor for anomalous agent behaviors; follow vendor guidance: http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors compromise large backbone, provider‑edge (PE) and customer‑edge (CE) routers, use compromised devices and trusted connections to pivot into other networks, and modify routers to maintain persistent, long‑term access.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon (also tracked as OPERATOR PANDA, RedMike, UNC5807, GhostEmperor)
- **Mitigation:** Follow CISA/NSA/FBI mitigation guidance in AA25-239A — harden routers, update device credentials, monitor for unauthorized configuration changes, segment networks, apply vendor patches where available, restrict management plane access, and use network monitoring and EDR.
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
- **Threat Actors:** Russian GRU 85th GTsSS (Unit 26165) / APT28
- **Mitigation:** Follow CSA recommended mitigations — harden external‑facing services, enforce MFA, apply network segmentation, monitor for indicators of compromise, block known malicious infrastructure, and follow incident response guidance from CISA/FBI/NSA.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

**Parallel AI Enrichment:**

- **Technical Details:** A malicious DNS response can trigger out‑of‑bounds reads, writes, and other memory issues when parsed by a memory‑unsafe DNS parser (CVE‑2024‑27227). Implementing a memory‑safe Rust DNS parser eliminates these memory‑safety errors.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true — http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Replace memory‑unsafe DNS parser with Rust implementation to reduce memory‑safety vulnerabilities; general hardening of baseband firmware and memory‑safety mitigations.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html

---
