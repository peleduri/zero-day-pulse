# Zero Day Pulse

> **Generated:** 2026-06-22 16:26 UTC &nbsp;|&nbsp; **Total:** 11 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path‑traversal vulnerability in SimpleHelp Remote Monitoring and Management that lets an unauthenticated remote attacker craft a file request containing '../' sequences to traverse directories and read sensitive files.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (versions 5.5.7 and earlier)
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (unspecified)
- **Mitigation:** Apply the vendor‑released patches for SimpleHelp 5.5.7 or later; if patches cannot be applied immediately, disable remote RMM access, enforce strict network segmentation, and monitor for anomalous file accesses.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an attack vector where adversarial content on the public web or other retrieved context contains hidden or malicious instructions that are picked up by AI agents during retrieval and influence their behavior. Examples include hidden website code, crafted web content, and comment‑based payloads that cause agents to execute unintended actions or reveal sensitive data.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Input/output validation and sanitization, human oversight and controls around LLM outputs, retrieval‑filtering and whitelisting of sources, monitoring for IPI patterns, and vendor hardening of retrieval pipelines.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) — attackers seed malicious instructions into data sources or third‑party content consumed by an LLM‑enabled service (e.g., web pages, documents, integrated tools). When the LLM ingests that tainted data during query processing or agentic automation, the injected instructions can influence the model’s behavior, potentially without any direct user input.
- **Affected Products:** Google Workspace (features that integrate Gemini/GenAI and automated agents)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Harden input/output handling: validate and sanitize external data, restrict agentic automation privileges, implement human‑in‑the‑loop approval for sensitive actions, provenance/trust signals for content sources, content filtering, rate/behavior monitoring, and regular scanning of public web for known IPI patterns (per Google recommendations).
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection in agentic browsing allows a malicious web page to inject crafted content into the Gemini agent’s prompts, potentially causing the agent to execute unintended actions or leak local resources. The issue can be amplified when chained with other vulnerabilities such as CVE-2025-54131, leading to local file access or privacy breaches.
- **Affected Products:** Chrome (Gemini agentic browsing feature)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true - http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply the latest Chrome updates that include the agentic‑browsing mitigations, follow Google’s layered‑defense guidance (restrict origin access, enforce additional agent oversight), and disable agentic features when not required.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Near-miss linear buffer overflow in CrabbyAVIF (Rust) in unsafe code; Scudo hardened allocator’s guard pages rendered it non-exploitable and converted overflow into a crash; issue assigned CVE-2025-48530 and patched pre-release.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Ensure Scudo hardened allocator deployment, prioritize patches (90-day window), improved crash reporting for Scudo overflows, unsafe-Rust training and stricter unsafe code review practices; follow Android Security Bulletin guidance.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection attacks embed hidden or malicious instructions within external data sources (emails, documents, calendar invites, web pages) that AI agents ingest; when an agent processes this content without adequate provenance, grounding, or filtering, the malicious instructions can cause data exfiltration or unauthorized actions.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Layered defenses — validate and sanitize external inputs, enforce strict access controls and least privilege for model data, use provenance/metadata and content filtering, model grounding and refusal policies, context window trimming, allowlisting, rate‑limiting and human‑in‑the‑loop review for sensitive outputs.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2023-20198 exploits a privilege‑escalation flaw in Cisco IOS XE's web UI, allowing an unauthenticated attacker to obtain root privileges. CVE-2023-20273 is a similar privilege‑escalation issue. CVE-2018-0171 leverages Cisco Smart Install to execute arbitrary code on IOS/IOS XE devices. CVE-2024-21887 is a command‑injection vulnerability in Ivanti Connect Secure and Ivanti Policy Secure that permits remote command execution.
- **Affected Products:** Cisco IOS XE (Web UI feature), Cisco IOS and IOS XE (Smart Install), Ivanti Connect Secure (9.x, 22.x), Ivanti Policy Secure (9.x, 22.x)
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Disable Guest Shell if not required, enable image and configuration integrity verification, validate firmware/image hashes, prioritize patching of CVE-2023-20198, CVE-2023-20273, CVE-2024-21887, and CVE-2018-0171, and hunt for related IOCs.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** The actors leveraged exploitation of internet‑facing infrastructure, including compromised corporate VPNs, via public vulnerabilities such as the WinRAR vulnerability (CVE‑2023‑38831) and Roundcube Webmail vulnerabilities (CVE‑2020‑35730, CVE‑2020‑12641). They also used SQL injection to gain initial access, then moved laterally within victim networks.
- **Affected Products:** WinRAR (CVE-2023-38831), Roundcube Webmail (CVE-2020-35730, CVE-2020-12641)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** APT28, Fancy Bear, Forest Blizzard, Blue Delta
- **Mitigation:** Collect and monitor Windows logs; Enable attack surface reduction rules; Educate users to only use approved corporate systems; Apply network segmentation; Restrict VPN access; Patch or mitigate vulnerable services where possible.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** CVE‑2026‑47281: Improper input validation in VS Code allows privilege elevation over a network when a user opens a malicious .code-workspace file. CVE‑2026‑47284: Improper handling leads to information disclosure of sensitive data when a malicious .code-workspace file is opened. CVE‑2026‑50507: A protection‑mechanism failure in BitLocker permits bypass of device‑encryption via a physical attack, granting full access to encrypted data.
- **Affected Products:** Visual Studio Code, Windows BitLocker
- **CVSS Score:** 9.6, 6.5, 6.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H/E:U/RL:O/RC:C; CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N/E:U/RL:O/RC:C; CVSS:3.1/AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:P/RL:O/RC:C
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known, Bitskrieg, YellowKey
- **Mitigation:** Apply the official patches released on June 9 2026. For VS Code, do not open .code-workspace files from untrusted sources. For BitLocker, maintain strict physical security controls to prevent unauthorized physical access.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-47281, https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-47284, https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50507

---

## 10. 🟠 Zero-Day — What the Latest ShinyHunters Breaches Reveal About Modern Cyberattacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://www.securityweek.com/what-the-latest-shinyhunters-breaches-reveal-about-modern-cyberattacks/>

> Groups like ShinyHunters are demonstrating that attackers do not necessarily need malware or zero-day exploits to cause massive damage. The post What the Latest ShinyHunters Breaches Reveal About Modern Cyberattacks appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** The attacks exploit valid credentials, MFA fatigue, vishing, OAuth token abuse, compromised SaaS integrations, excessive permissions, misconfigured identity settings, third‑party trust exploitation, and help‑desk impersonation to access and exfiltrate data without a specific software flaw.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** ShinyHunters
- **Mitigation:** Enforce strong MFA, monitor and detect identity anomalies (impossible travel, token misuse, MFA manipulation), restrict guest‑user and OAuth permissions, reduce excessive SaaS privileges, harden help‑desk workflows, apply least‑privilege for integrations, monitor third‑party trust, and implement identity threat detection and response.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
