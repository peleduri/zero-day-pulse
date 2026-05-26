# Zero Day Pulse

> **Generated:** 2026-05-26 01:59 UTC &nbsp;|&nbsp; **Total:** 12 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 2 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE‑2024‑57727 is a path traversal vulnerability in SimpleHelp v5.5.7 and earlier that allows unauthenticated remote attackers to traverse filesystem paths and retrieve sensitive files (logs, configuration, credentials).
- **Affected Products:** SimpleHelp remote support/RMM v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** DragonForce and other ransomware groups
- **Mitigation:** Upgrade immediately to SimpleHelp v5.5.8 or later; if unable to patch, restrict network access to the SimpleHelp management interface, isolate affected hosts, rotate exposed credentials, audit logs for suspicious access, and apply network‑level controls (firewall, IP allowlists).
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — ⚡ Weekly Recap: Linux Flaws, Defender 0-Days, Router Botnets, and Supply Chain Chaos

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-25
**Reference:** <https://thehackernews.com/2026/05/weekly-recap-linux-flaws-defender-0.html>

> Monday recap. Same mess, new week.

A sketchy dev tool got people pwned, old bugs came back from the dead, and security products somehow needed protecting from themselves. A bunch of companies spent the week checking old boxes and forgotten servers they should&#x27;ve patched years ago. Good times.

Phishing crews are getting smarter too - less obvious scam junk, more targeted stuff that actually

**Parallel AI Enrichment:**

- **Technical Details:** Linux kernel CVE‑2026‑46333: improper privilege management allowing an unprivileged local user to read files and execute commands as root. Microsoft Defender CVE‑2026‑41091: privilege escalation to SYSTEM. CVE‑2026‑45498: denial‑of‑service affecting Defender. Drupal Core CVE‑2026‑9082: SQL injection enabling data access/exfiltration. Cisco Secure Workload CVE‑2026‑20223: insufficient validation/authentication on REST API allowing crafted requests to read data and change configuration across tenants. YellowKey CVE‑2026‑45585: BitLocker bypass permitting physical‑access attackers to decrypt device storage. Four‑Faith router CVE‑2024‑9643: authentication bypass enabling configuration changes and botnet enrollment.
- **Affected Products:** Linux kernel (Debian, Fedora, Ubuntu default installations), Microsoft Defender, Drupal Core (all supported versions), Cisco Secure Workload, Windows 11 26H1/24H2/25H2 (x64) and Windows Server 2025, Four‑Faith F3x36 industrial cellular routers
- **CVSS Score:** CVE-2026-46333:5.5, CVE-2026-9082:6.5, CVE-2026-20223:10.0, CVE-2026-45585:6.8, CVE-2024-9643:9.8; other scores unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (DirtyDecrypt PoC linked in article); other vulnerabilities exploit status unknown.
- **Patch Available:** true (Cisco Secure Workload); true (Drupal Core); false (YellowKey – mitigations only); other patch statuses unknown.
- **Active Exploitation:** true (Microsoft Defender); true (Drupal Core); true (Four‑Faith router); other vulnerabilities status unknown.
- **Threat Actors:** Chaotic Eclipse (linked to Defender vulnerabilities); others unknown.
- **Mitigation:** Apply Cisco Secure Workload updates immediately; apply Drupal Core security updates; follow Microsoft’s YellowKey mitigations; restrict physical access to devices; isolate and block Four‑Faith routers, monitor network traffic; no specific mitigation provided for Linux kernel, Defender, or other unpatched items.
- **Vendor Advisory:** Vendor advisory URL unavailable for most entries; Cisco Secure Workload advisory available at https://thehackernews.com/2026/05/weekly-recap-linux-flaws-defender-0.html

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) leverages malicious or crafted content on web pages (including hidden or injected payloads) that, when browsed by an AI agent or tool, injects instructions into the agent's prompt context. Attackers host payloads (visible or hidden in page code) that aim to exfiltrate data, perform actions (API key theft, data destruction, fraud), or escalate to remote code execution when combined with vulnerable agent frameworks or sandbox escapes.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** - Validate and sanitize untrusted web content before feeding to agents; restrict agent browsing to allowlist sites; implement prompt integrity checks and input/output sandboxing; rotate and restrict credentials/API keys; apply least privilege for agent actions; monitor agent activity and alerts for anomalous commands.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an adversarial technique where attackers inject malicious instructions into external data sources or tools that an LLM consumes during a user request, causing the model to follow those instructions. The attack surface includes multi‑source AI applications, web content, and agentic tool chains.
- **Affected Products:** Google Workspace with Gemini (specific versions unavailable)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Continuous multi‑layered defenses including deterministic defenses (URL sanitization, user confirmation, tool‑chaining policies), ML/LLM‑based defenses retrained with synthetic attack data, model hardening of Gemini, policy engine for rapid configuration fixes, collaboration with Google AI VRP, red‑team testing and automated red‑team exercises.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is the primary threat: untrusted web content (pages, iframes, user‑generated content, ads) may craft inputs that influence an agentic model’s planner to perform unwanted actions (financial transactions, data exfiltration). Chrome’s mitigations limit model exposure to only relevant origins, run a separate high‑trust Alignment Critic that sees only action metadata to approve/reject actions, perform deterministic checks on model‑generated URLs, and apply runtime classifiers to detect prompt‑injection attempts before actions are taken.
- **Affected Products:** Google Chrome (agentic capabilities, Gemini in Chrome); specific versions unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses described by Chrome: User Alignment Critic to vet actions, Agent Origin Sets (read‑only and read‑write origin gating), deterministic user confirmations for sensitive actions (payments, signin), real‑time indirect‑prompt‑injection classifier, site isolation and gating of which page content is sent to the model, continuous red‑teaming and auto‑update to deploy fixes.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A near‑miss linear buffer overflow was discovered in the Rust CrabbyAVIF library (pre‑release). The overflow was rendered non‑exploitable on Android devices using the Scudo hardened allocator because guard pages around secondary allocations converted the overflow into a noisy crash; the issue was fixed before public release and tracked as CVE-2025-48530.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use Scudo hardened allocator (guard‑page protections), ensure crash‑reporting surfaces overflows into Scudo guard pages, apply the published patch, and follow unsafe‑Rust review and training best practices.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injections (IPI) are attacker‑controlled instructions embedded in external data sources (emails, documents, calendar invites, web content) that, when consumed by generative AI systems, can cause the model to leak data or perform unauthorized actions.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — advisory: http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses — validate and sanitize external inputs, apply content provenance and trust signals, constrain model outputs with strict instruction‑following policies, implement data exfiltration detection and least‑privilege data access, and apply application‑layer filters and allowlists/denylists. Follow vendor advisory for detailed controls.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors compromise routers and IoT devices, modify router configuration/firmware to maintain persistent, long‑term access, and pivot from compromised/trusted connections into other networks for espionage.
- **Affected Products:** Backbone routers (major telecommunications providers), provider edge (PE) routers, customer edge (CE) routers, compromised IoT devices and other networked devices
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Isolate and segment network management; apply vendor updates where available; change default credentials; disable unnecessary management interfaces; implement strong authentication (e.g., multifactor/SSH keys); monitor for anomalous router configuration changes and unusual outbound connections; use intrusion detection and log aggregation; enforce least privilege on trusted connections.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

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
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS), also known as APT28
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — [SECURITY ADVISORY] CVE-2026-34474 - ZTE H298A/H108N Unauthenticated Admin Credential Exposure

**CVE:** `CVE-2026-34474` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://seclists.org/fulldisclosure/2026/May/20>

> Posted by m.nageh on May 25 -----BEGIN SECURITY ADVISORY----- Advisory ID: MONX-2026-003 CVE ID: CVE-2026-34474 Title: ZTE ZXHN H298A / H108N - Unauthenticated Admin Password &amp; WLAN Credential Exposure Affected: ZTE ZXHN H298A 1.1, ZTE ZXHN H108N 2.6 (EOL; no patch planned) Date: 2026-05-20 Author: Mina Nageh Salalma (Monx Research) Contact: minanageh379 () gmail com Public URL:...

**Parallel AI Enrichment:**

- **Technical Details:** A crafted unauthenticated HTTP request to an legacy/diagnostic path (ETHCheat) on affected ZTE ZXHN web interfaces returns sensitive fields including the administrator password and WLAN pre‑shared key (PSK), enabling credential exposure and remote access.
- **Affected Products:** ZTE ZXHN H298A 1.1, ZTE ZXHN H108N 2.6
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true – https://gist.github.com/minanagehsalalma/7a8516b9b00d0008f2f25750320560c9
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Restrict access to device web interface (WAN block, firewall, IP access controls), change default credentials, disable remote management, and apply firmware updates where available; isolate or replace EOL devices.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟡 High Severity — Ghost CMS CVE-2026-26980 Exploited to Hijack 700+ Sites for ClickFix Attacks

**CVE:** `CVE-2026-26980` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-25
**Reference:** <https://thehackernews.com/2026/05/ghost-cms-cve-2026-26980-exploited-to.html>

> Threat actors are exploiting a recently disclosed critical security flaw in Ghost CMS to inject malicious JavaScript code with an aim to fuel ClickFix attacks.

According to QiAnXin XLab, the activity involves the exploitation of CVE-2026-26980 (CVSS score: 9.4), an SQL injection vulnerability in Ghost&#x27;s Content API that could allow an unauthenticated attacker to read arbitrary data from the

---

## 12. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
