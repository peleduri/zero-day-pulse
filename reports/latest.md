# Zero Day Pulse

> **Generated:** 2026-06-06 19:04 UTC &nbsp;|&nbsp; **Total:** 17 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 5 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 lets attackers read sensitive files via path traversal in SimpleHelp Remote Support / RMM.
- **Affected Products:** SimpleHelp Remote Support / Remote Monitoring and Management (version 5.5.7 and earlier)
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (http://offsec.com/blog/cve-2024-57727; http://attackerkb.com/topics/G4CTOrbDx0/cve-2024-57727)
- **Patch Available:** true (http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know)
- **Active Exploitation:** true (https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a)
- **Threat Actors:** Ransomware actors
- **Mitigation:** Upgrade to SimpleHelp 5.5.8 or later; apply vendor advisory guidance; isolate or restrict unpatched SimpleHelp RMM instances until patched.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — New ChatGPT Lockdown Mode Limits Tools That Could Enable Data Exfiltration

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-06
**Reference:** <https://thehackernews.com/2026/06/new-chatgpt-lockdown-mode-limits-tools.html>

> OpenAI has begun rolling out a new Lockdown Mode to ChatGPT for eligible personal accounts to reduce the risk of data exfiltration arising from prompt injection attacks.

The feature is primarily designed for people and organizations that handle sensitive data and require stricter protection guarantees. Lockdown Mode is available to logged-in users across Free, Go, Plus, and Pro, and

**Parallel AI Enrichment:**

- **Technical Details:** Lockdown Mode deterministically disables or restricts certain ChatGPT capabilities and external integrations (web browsing, plugins/external tools, code execution/advanced tools, file uploads/transfer mechanisms) that could be abused by prompt‑injection attacks to exfiltrate data. It also adds Elevated Risk labels to warn users when a request may pose higher data‑leakage risk.
- **Affected Products:** ChatGPT (Free, Go, Plus, Pro), ChatGPT Business
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — https://openai.com/index/introducing-lockdown-mode-and-elevated-risk-labels-in-chatgpt/
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Enable Lockdown Mode for accounts handling sensitive data; disable or restrict web access, external tools/plugins, code execution/analysis tools, and file‑system or external API integrations; follow organizational policies for limiting model access and avoid submitting sensitive data to general‑purpose chat when not in Lockdown Mode.
- **Vendor Advisory:** https://openai.com/index/introducing-lockdown-mode-and-elevated-risk-labels-in-chatgpt/

---

## 3. 🟠 Zero-Day — AI Agent Uncovers 21 Zero-Days in FFmpeg; Chrome Patches Record 429 Bugs

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-06
**Reference:** <https://thehackernews.com/2026/06/ai-agent-uncovers-21-zero-days-in.html>

> Two things landed within days of each other this week. A security startup reported 21 previously unknown vulnerabilities in FFmpeg, the media library inside almost everything that touches video, all of them found by an autonomous AI agent.

The same week, Google shipped Chrome 149 with patches for 429 security bugs, the most ever in a single release.

Only the FFmpeg bugs were found by AI.

**Parallel AI Enrichment:**

- **Technical Details:** Memory‑corruption bugs (heap or stack overflows) in FFmpeg parsers, demuxers (e.g., TS demuxer, service‑description‑table) and decoders (e.g., VP9) that can be triggered by crafted media streams, potentially leading to arbitrary code execution when processing untrusted RTSP/RTP or file inputs.
- **Affected Products:** FFmpeg (versions prior to the June 2026 upstream fix)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (PoC published at https://github.com/DepthFirstDisclosures/ffmpeg-dfvuln127)
- **Patch Available:** true (upstream fixes available; see https://ffmpeg.org/security.html)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Update to the latest FFmpeg upstream build or install the vendor/distribution security update immediately. Prioritize hardening by sandboxing media processing, validating or restricting untrusted RTSP/RTP streams, and applying strict input validation for media files.
- **Vendor Advisory:** https://ffmpeg.org/security.html

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when AI systems process web content containing adversarial instructions that cause the model to follow attacker commands; Google found categories including pranks, SEO manipulation, deterrence, data exfiltration, and destructive instructions. Detection used pattern matching, LLM classification, and human validation.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses—hardening models, red‑team testing, monitoring (Common Crawl/scale scans), LLM‑based classification of suspicious content, human review, and Google’s AI Vulnerability Reward program; see Google Workspace continuous‑mitigation blog for product guidance.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) enables an attacker to insert malicious instructions into the data or tools accessed by a Large Language Model, causing the model to produce unintended behavior even when the user provides no direct input.
- **Affected Products:** Google Workspace with Gemini, Gemini app, Gemini in Workspace apps
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (source: http://securityweek.com/malicious-ai-prompt-injection-attacks-increasing-but-sophistication-still-low-google)
- **Patch Available:** true (source: http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html)
- **Active Exploitation:** true (source: http://securityweek.com/malicious-ai-prompt-injection-attacks-increasing-but-sophistication-still-low-google)
- **Threat Actors:** None known
- **Mitigation:** Multi‑layered approach includes Human Red‑Teaming, Automated Red‑Teaming, synthetic data generation to expand attack variants, deterministic defenses such as user confirmation and URL sanitization, ML‑based defenses retrained on new data, LLM‑based prompt engineering, and model hardening of Gemini to ignore harmful instructions.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: agentic browsers executing multi‑step/agent workflows can be manipulated by adversarial content on websites (e.g., crafted pages or comments) that inject prompts into the agent’s context, causing unintended actions or data leakage. The attack vector involves malicious web content returned during browsing that an agent interprets as high‑level instructions.
- **Affected Products:** Google Chrome (agentic browsing / Gemini in Chrome)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Harden agent input handling and prompt parsing; treat web content as untrusted, apply strict prompt sanitization, limit agent capabilities by default, require explicit user confirmation for sensitive actions, enable origin‑based isolation and least‑privilege policies, and follow the vendor’s recommended mitigations from the advisory.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

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
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when hidden or malicious instructions embedded in external data sources (emails, documents, calendar invites, webpages) are consumed by generative AI systems, causing them to exfiltrate data or perform unauthorized actions. The attack leverages trusted data ingestion pipelines and model prompts to inject instructions that the model may follow if not properly filtered or validated.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use a layered defense: validate and sanitize external data before ingestion; enforce strong access controls and least privilege for data access; apply provenance tracking and blocklisted content filters; implement model-level guardrails (e.g., response filters, instruction masking, verification checks); use orchestration checks that keep sensitive connectors separate; log and monitor model inputs/outputs for anomalous behavior; conduct threat modelling and red‑teaming to find IPI vectors.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Threat actors gain initial access by compromising backbone, provider edge (PE) or customer edge (CE) routers, then modify firmware or configurations to maintain long‑term persistence. Compromised routers are used as pivot points, leveraging trusted network connections to move laterally into additional systems.
- **Affected Products:** large backbone routers, provider edge (PE) routers, customer edge (CE) routers
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Implement strict network segmentation and zero‑trust controls around router infrastructure, regularly apply firmware and security updates, disable unnecessary services, monitor router logs for anomalous activity, and follow CISA’s simulation and mitigation guidance to test defenses.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Unit 26165 employed spearphishing, credential stuffing/password spraying, exploitation of internet‑facing services (including Roundcube and WinRAR vulnerabilities and Outlook NTLM calendar invite exploitation), mailbox‑permission manipulation for sustained email collection, living‑off‑the‑land tools (Impacket, PsExec, Certipy), DLL search‑order hijacking, scheduled tasks/run keys for persistence, and data exfiltration via OpenSSH and archived uploads.
- **Affected Products:** Roundcube (versions before 1.4.4, 1.2.13, 1.3.x before 1.3.16, 1.4.x before 1.4.10), WinRAR (CVE-2023-38831), Microsoft Outlook/Exchange (CVE-2023-23397)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** GRU 85th GTsSS (unit 26165) — also tracked as APT28/Fancy Bear/Forest Blizzard/Blue Delta
- **Mitigation:** Apply relevant vendor patches for referenced CVEs (Outlook NTLM CVE-2023-23397, WinRAR CVE-2023-38831, Roundcube CVEs), harden email infrastructure and disable/mitigate NTLM where possible, enforce MFA and monitor for mailbox permission changes, block/monitor suspicious outbound traffic to hosting/API‑mocking services, hunt for LOTL behaviors (Impacket, Certipy, schtasks, wevtutil, ntdsutil), and follow CISA/FBI recommended detection and hardening guidance.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 11. 🟠 Zero-Day — CISA Adds Actively Exploited SolarWinds Serv-U DoS Flaw to KEV Catalog

**CVE:** `CVE-2026-28318` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-06
**Reference:** <https://thehackernews.com/2026/06/cisa-adds-actively-exploited-solarwinds.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has added a high-severity security flaw impacting SolarWinds Serv-U  multi-protocol file server software to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

The vulnerability, tracked as CVE-2026-28318 (CVSS score: 7.5), is a denial-of-service (DoS) bug that causes the service to crash

---

## 12. 🟠 Zero-Day — Cisco Catalyst SD-WAN Manager CVE-2026-20245 Flaw Actively Exploited – No Patch Available

**CVE:** `CVE-2026-20245` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-06
**Reference:** <https://thehackernews.com/2026/06/cisco-catalyst-sd-wan-manager-cve-2026.html>

> Cisco has warned that a high-severity security flaw impacting Catalyst SD-WAN Manager has come under active exploitation.

The vulnerability, tracked as CVE-2026-20245, carries a CVSS score of 7.8 out of a maximum of 10.0. It affects the following deployment types -


  On-Prem Deployment
  Cisco SD-WAN Cloud-Pro
  Cisco SD-WAN Cloud (Cisco Managed)
  Cisco SD-WAN for Government (FedRAMP)

&quot;A

---

## 13. 🟡 High Severity — Critical Everest Forms Pro flaw exploited to take over WordPress sites

**CVE:** `CVE-2026-3300` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-06
**Reference:** <https://www.bleepingcomputer.com/news/security/critical-everest-forms-pro-flaw-exploited-to-take-over-wordpress-sites/>

> Hackers are actively exploiting a critical vulnerability (CVE-2026-3300) in the Everest Forms Pro plugin, which lets them take complete control of a WordPress website. [...]

---

## 14. 🟡 High Severity — Bugsink: Issue bulk actions can affect another project’s issue if its UUID is known

**CVE:** `CVE-2026-47716` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-g5vc-q7qc-v939>

> ### Description
Bugsink’s issue list supports bulk actions such as resolving or muting selected issues. In affected versions, the issue list view authorizes access through the project in the URL, but applies the requested bulk action to the submitted issue IDs without also requiring those issues to belong to that project.

This is a project-boundary authorization issue: a logged-in user with acces…

---

## 15. 🟡 High Severity — Bugsink: Issue event views can show an event from another project if its UUID is known

**CVE:** `CVE-2026-47715` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-vx2f-6m6h-9frf>

> ### Description

Bugsink issue event pages accept a direct event identifier from the URL and, in affected versions, look up that event without also requiring it to belong to the issue in the URL.

This is a project-boundary authorization issue: a logged-in user with access to one project can view another project’s event data through an issue they are allowed to access. However, the issue is mitiga…

---

## 16. 🟡 High Severity — Shopper: Authorization bypass and RBAC privilege escalation in team settings

**CVE:** `CVE-2026-47744` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-05
**Reference:** <https://github.com/advisories/GHSA-c3qp-2ggw-xjg7>

> ## Impact

Two distinct authorization defects in the team settings allowed any authenticated panel user to take over the RBAC system:

- `Settings/Team/Index` had no `mount()` authorization. Any authenticated user could load the page and use its public actions to create new roles and delete other users, including administrators.
- `Settings/Team/RolePermission` gated its write actions on the read-…

---

## 17. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
