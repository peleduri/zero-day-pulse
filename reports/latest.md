# Zero Day Pulse

> **Generated:** 2026-06-02 20:35 UTC &nbsp;|&nbsp; **Total:** 15 &nbsp;|&nbsp; 🔴 KEV: 2 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🔴 CISA KEV — CVE-2022-0492 — Linux Kernel Improper Authentication Vulnerability

**CVE:** `CVE-2022-0492` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-06-02
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2022-0492>

> Vendor: Linux | Product: Kernel. Linux Kernel contains an improper authentication vulnerability which could allow for privilege escalation via the cgroups v1 release_agent feature. Required action: Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable. (due 2026-06-05)

**Parallel AI Enrichment:**

- **Technical Details:** Vulnerability in cgroup_release_agent_write (kernel/cgroup/cgroup‑v1.c) allows the cgroups v1 release_agent feature to run an attacker‑controlled binary as root when notify_on_release is enabled, provided the container runs as root, AppArmor/SELinux are disabled, seccomp is off, and unprivileged user namespaces are permitted. This enables container escape and local privilege escalation.
- **Affected Products:** Linux kernel (cgroup_release_agent_write in kernel/cgroup/cgroup‑v1.c); patched in mainline 5.17‑rc3 and Ubuntu kernels 5.13.0-37.42, 5.4.0-1069.73, etc.
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (https://www.rapid7.com/db/modules/exploit/linux/local/docker_cgroup_escape)
- **Patch Available:** true (https://ubuntu.com/security/CVE-2022-0492)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Install the patched kernel (e.g., Ubuntu kernel 5.17‑rc3 or back‑ported packages). If patching is not possible, disable unprivileged user namespaces, avoid privileged containers, enable AppArmor/SELinux and seccomp filters, and use runtime detection tools such as Falco.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 2. 🔴 CISA KEV — CVE-2025-48595 — Android Framework Integer Overflow Vulnerability

**CVE:** `CVE-2025-48595` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-06-02
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2025-48595>

> Vendor: Android | Product: Framework. Android Framework contains an integer overflow vulnerability that allows for code execution that could allow for local privilege escalation. Required action: Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable. (due 2026-06-05)

**Parallel AI Enrichment:**

- **Technical Details:** An integer overflow (CWE‑190) in multiple locations of the Android Framework/Qualcomm components allows local privilege escalation without requiring any user interaction.
- **Affected Products:** Android Framework on devices receiving June 2026 security updates (affected OEM/SoC-specific Android builds)
- **CVSS Score:** 8.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — https://source.android.com/docs/security/bulletin/2026/2026-06-01
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Install the June 2026 Android security updates from device OEMs immediately; until patched, follow least‑privilege policies, avoid installing untrusted apps, and restrict app and USB debugging access.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2026/2026-06-01

---

## 3. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Multiple path traversal (directory traversal) vulnerabilities allow unauthenticated remote attackers to retrieve logs, configuration files, and credentials, potentially accessing downstream customers.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true – https://medium.com/@RosanaFS/simplehelp-cve-2024-57727-tryhackme-walkthrough-9f88c2061fb9
- **Patch Available:** true – https://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors
- **Mitigation:** Upgrade to SimpleHelp 5.5.8 or later; if a patch cannot be applied, isolate/unexpose SimpleHelp instances from the internet, restrict access via firewall or VPN, rotate credentials, and monitor for compromise.
- **Vendor Advisory:** https://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570

---

## 4. 🟠 Zero-Day — Google June 2026 Android Update Patches 124 Flaws, One Actively Exploited

**CVE:** `CVE-2025-48595` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-02
**Reference:** <https://thehackernews.com/2026/06/google-june-2026-android-update-patches.html>

> Google on Monday released patches for 124 security vulnerabilities impacting its Android operating system for the month of June 2026, including one high-severity flaw in the Framework component that has come under active exploitation.

Tracked as CVE-2025-48595 (CVSS score: 8.4), the security flaw has been described as a case of privilege escalation without requiring any user interaction. The

**Parallel AI Enrichment:**

- **Technical Details:** An integer overflow (CWE‑190) in multiple locations of the Android Framework/Qualcomm components allows local privilege escalation without requiring any user interaction.
- **Affected Products:** Android Framework on devices receiving June 2026 security updates (affected OEM/SoC-specific Android builds)
- **CVSS Score:** 8.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — https://source.android.com/docs/security/bulletin/2026/2026-06-01
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Install the June 2026 Android security updates from device OEMs immediately; until patched, follow least‑privilege policies, avoid installing untrusted apps, and restrict app and USB debugging access.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2026/2026-06-01

---

## 5. 🟠 Zero-Day — Google fixes one actively exploited Android zero-day, 124 flaws

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-02
**Reference:** <https://www.bleepingcomputer.com/news/security/google-fixes-one-actively-exploited-android-zero-day-124-flaws/>

> Google has released the June 2026 Android security patches to address 124 vulnerabilities, including one zero-day flaw exploited in targeted attacks. [...]

**Parallel AI Enrichment:**

- **Technical Details:** The actively exploited zero‑day affects display/graphics code (Qualcomm display driver/memory allocation handling) leading to memory corruption that can be leveraged for remote code execution or privilege escalation when processed by vulnerable drivers/components.
- **Affected Products:** Android devices (security patch level 2026-06-01); includes Qualcomm display drivers on multiple Qualcomm chipsets (e.g., CVE-2026-21385)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — https://source.android.com/docs/security/bulletin/2026/2026-06-01
- **Active Exploitation:** true — https://www.bleepingcomputer.com/news/security/google-fixes-one-actively-exploited-android-zero-day-124-flaws/
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Install the June 2026 Android security updates (apply security patch level 2026-06-01); if patch cannot be applied, minimize exposure by restricting untrusted apps, disable unnecessary peripherals, and follow vendor hardening guidance.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2026/2026-06-01

---

## 6. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when malicious content on public web pages (often hidden or encoded) is processed by AI agents and causes the agent to execute unintended instructions or reveal sensitive data. Attackers craft content that looks benign to humans but includes instructions targeting LLM system prompts or tool calls, leveraging chain‑of‑thought/style triggers and encoding to evade simple filters.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Follow Google guidance: harden input handling for AI agents (sanitize/whitelist ingestion sources, provenance checks, content filtering, model output constraints, multi‑layered defenses), monitor for IPI payload patterns, and apply best practices recommended in vendor blog posts.
- **Vendor Advisory:** https://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 7. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when an attacker injects malicious instructions into data or tools consumed by an LLM (including hidden website code or payloads embedded in third‑party content), causing the model or agentic automation to follow those instructions even without user input.
- **Affected Products:** Google Workspace with Gemini
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html
- **Active Exploitation:** true — see citations
- **Threat Actors:** None known
- **Mitigation:** Layered defenses and continuous mitigation by vendor: content filtering, provenance checks, tool and data source hardening, agent policy controls, and monitoring; see Google’s white paper and blog posts for implementation guidance.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 8. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection in agentic browsing — attackers can place crafted content (pages, iframes, user‑generated content) that influence the agent’s planning model to perform unwanted actions (e.g., financial transactions, data exfiltration).
- **Affected Products:** Chrome (agentic capabilities, Gemini in Chrome)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — https://blog.google/security/architecting-security-for-agentic/
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses: user confirmations for sensitive actions, origin gating (Agent Origin Sets), User Alignment Critic, real‑time prompt‑injection classifiers, deterministic checks for model‑generated URLs, continuous red‑teaming and updates via Chrome auto‑update. Follow updated VRP rules to report issues.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 9. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable
- **Affected Products:** Android platform (first‑party and third‑party/open‑source components across C, C++, Java, Kotlin, Rust) – versions unspecified
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Continue migrating new and replacement Android platform code to memory‑safe languages (Rust), perform rigorous code review, fuzzing, and security testing per Google’s guidance.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 10. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Google describes "indirect prompt injections" as hidden malicious instructions within external data sources (emails, documents, calendar invites) that aim to manipulate generative AI to exfiltrate data or perform rogue actions. Mitigations include model hardening (adversarial training), prompt‑injection content classifiers, security thought reinforcement, markdown sanitization, suspicious URL redaction, and a user‑confirmation (HITL) framework.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known.
- **Mitigation:** Use layered defenses described by Google: model hardening/adversarial training; prompt‑injection content classifiers; security thought reinforcement (injecting guidance to ignore adversarial instructions); markdown sanitization and external‑image suppression; suspicious‑URL detection/redaction (Safe Browsing); contextual user confirmation for risky actions; end‑user notifications and help‑center guidance.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 11. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

---

## 12. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 13. 🟠 Zero-Day — CISA flags two-year-old Oracle flaw as actively exploited in attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-02
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-oracle-weblogic-flaw/>

> CISA has ordered government agencies to secure their systems against a high-severity Oracle WebLogic Server vulnerability that was patched two years ago and is now actively exploited in attacks. [...]

---

## 14. 🟠 Zero-Day — Oracle WebLogic Vulnerability Exploited in the Wild

**CVE:** `CVE-2024-21182` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-02
**Reference:** <https://www.securityweek.com/oracle-weblogic-vulnerability-exploited-in-the-wild/>

> The vulnerability is CVE-2024-21182 and it can be exploited without authentication to hack affected WebLogic servers. The post Oracle WebLogic Vulnerability Exploited in the Wild appeared first on SecurityWeek .

---

## 15. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
