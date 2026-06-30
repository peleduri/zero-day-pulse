# Zero Day Pulse

> **Generated:** 2026-06-30 08:57 UTC &nbsp;|&nbsp; **Total:** 16 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 13 &nbsp;|&nbsp; 🟡 High: 3 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is an unauthenticated directory/path traversal vulnerability in SimpleHelp 5.5.7 and earlier that allows an attacker to craft path traversal input to read sensitive files from the server.
- **Affected Products:** SimpleHelp remote support software (SimpleHelp RMM) version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true; http://guides.simple-help.com/kb---security-vulnerabilities-01-2025
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor-released patches (update SimpleHelp to the patched release). If immediate patching is not possible, isolate/unexpose affected SimpleHelp instances until they can be updated and monitor for suspicious access (per vendor and CISA advisory).
- **Vendor Advisory:** http://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — CISA: Windows BlueHammer flaw now exploited by ransomware gangs

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-windows-bluehammer-flaw-now-exploited-by-ransomware-gangs/>

> CISA confirmed on Monday that ransomware gangs are now exploiting a Microsoft Defender privilege escalation vulnerability, dubbed BlueHammer, that has previously been abused in zero-day attacks. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Local privilege-escalation in Microsoft Defender caused by insufficient access-control granularity and race/timing or update-process abuses (filesystem timing/path confusion and Defender update/Volume Shadow Copy replacement) that allow an unprivileged user to escalate to SYSTEM.
- **Affected Products:** Microsoft Defender on Windows 10, Windows 11
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — public PoC reported (e.g. HelpNetSecurity Apr 8, 2026: https://www.helpnetsecurity.com/2026/04/08/bluehammer-windows-zero-day-exploit-leaked/)
- **Patch Available:** false — no official Microsoft advisory/patch located in collected evidence
- **Active Exploitation:** true
- **Threat Actors:** Ransomware gangs (unnamed in public reporting)
- **Mitigation:** Reduce local privilege exposure (limit unprivileged user rights), monitor and restrict Defender update/process operations, deploy vendor patches when released, and follow CISA Known Exploited Vulnerabilities guidance.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — Oracle E-Business Suite Flaw CVE-2026-46817 Actively Exploited in the Wild

**CVE:** `CVE-2026-46817` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://thehackernews.com/2026/06/oracle-e-business-suite-flaw-cve-2026.html>

> A critical security flaw impacting Oracle E-Business Suite has come under active exploitation in the wild, according to Defused Cyber.

The vulnerability, tracked as CVE-2026-46817 (CVSS score: 9.8), refers to an improper privilege management and authentication flaw in Oracle Payments that could be abused to take over susceptible instances.

&quot;Easily exploitable vulnerability allows

**Parallel AI Enrichment:**

- **Technical Details:** An improper privilege management / authentication weakness in the Oracle Payments File Transmission component that can be reached over HTTP by an unauthenticated attacker; successful exploitation can result in takeover of Oracle Payments instances.
- **Affected Products:** Oracle E-Business Suite — Oracle Payments (File Transmission component), versions 12.2.3 through 12.2.15
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true — https://www.oracle.com/security-alerts/cspumay2026.html
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply Oracle's May 2026 Critical Security Patch Update (CSPU) that contains the fix. If immediate patching is not possible, reduce network exposure to Oracle Payments (restrict HTTP access, place behind WAF or ACLs) and monitor for indicators of compromise.
- **Vendor Advisory:** https://www.oracle.com/security-alerts/cspumay2026.html

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) embeds adversarial natural-language instructions inside untrusted external content (public web pages, documents, emails, search results) that an LLM retrieves or parses during agentic/RAG operations. Because LLMs cannot reliably distinguish trusted system prompts from untrusted data, the injected instructions can hijack the agent into performing attacker-chosen actions: (a) exfiltration of user/context data to attacker-controlled URLs, (b) destruction/local execution (e.g., embedded 'delete all files' commands), (c) resource exhaustion via infinite-text streaming to waste tokens/timeouts, and (d) SEO-style manipulation to promote specific businesses in AI summaries. Google's Threat Intelligence teams conducted a broad Common Crawl sweep and observed an uptick in detections, including a 32% relative increase in the 'malicious' category between November 2025 and February 2026.
- **Affected Products:** Google Gemini (no specific version), Gemini-powered AI agents (general), Google Workspace with Gemini (no specific version), and broadly any LLM/agentic system that ingests untrusted external content (web pages, documents, emails).
- **CVSS Score:** CVSS score unavailable. No CVE is associated with this report, so no CVSS base score is published.
- **CVSS Vector:** CVSS vector unavailable. The blog post is a threat-intelligence research report, not a CVE advisory; no CVE ID and no CVSS v3 vector is assigned.
- **Exploit Available:** true. The blog documents real-world, in-the-wild indirect prompt injection (IPI) payloads harvested from the public web, including recurring signature patterns ('ignore ... instructions', 'if you are an AI'), SEO prompt injections, resource-exhaustion infinite-text-stream payloads designed to break AI agents, and destructive instructions. Source: http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html
- **Patch Available:** false. No single vendor patch is associated with this blog; Google treats indirect prompt injection as an evolving threat class addressed via continuous defensive hardening, layered detection, and the AI Vulnerability Reward Program rather than a one-time patch. Source: http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html
- **Active Exploitation:** true. Google's Threat Intelligence team documented active exploitation 'in the wild' on the public web via a Common Crawl sweep. They observed a 32% relative increase in the malicious IPI category between November 2025 and February 2026, across payload categories including SEO manipulation, AI-agent deterrence (resource exhaustion), data exfiltration and destructive instructions. Sources: http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html and https://www.helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild/
- **Threat Actors:** None known. The Google Security Blog post does not name any specific APT groups, threat actor campaigns, or ransomware operators. Researchers observed the activity via a Common Crawl sweep of the public web and grouped findings by attack categories (e.g., SEO manipulation, resource-exhaustion 'code to deter AI agents', data-exfiltration payloads, and destructive instructions such as 'delete all files on the user's machine') rather than attributing them to known actors.
- **Mitigation:** Google recommends a layered defense strategy rather than a single patch: (1) prompt-injection content classifiers that detect/filter adversarial instructions, (2) security thought-reinforcement prompts that re-prioritize user-directed tasks, (3) markdown sanitisation and suspicious-URL redaction backed by Google Safe Browsing, (4) a user confirmation framework (human-in-the-loop) before sensitive actions such as deleting calendar events, (5) end-user mitigation notifications when a risk is detected, (6) adversarial-robustness/model-resilience built into Gemini, (7) dedicated red teams pressure-testing the systems, and (8) the AI Vulnerability Reward Program for external researcher reporting.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI): adversaries place malicious instructions into data sources or tools (web pages, dynamically constructed browser content, etc.) that LLM-based agents ingest while answering user queries. When the agent consumes those sources, the adversary instructions can influence or override the agent’s behavior (e.g., perform actions, reveal data, or follow attacker-supplied logic).
- **Affected Products:** Gemini, Google Workspace (Gmail, Docs editors, Drive, Chat)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true; in-the-wild IPI payloads documented (e.g. Forcepoint X‑Labs disclosure: https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads)
- **Patch Available:** false; vendor describes ongoing mitigations and continuous hardening rather than a single discrete patch (see vendor advisory).
- **Active Exploitation:** true; multiple security teams documented live IPI payloads and Google/press analysis noting increased malicious prompt-injection attempts.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses and continuous hardening: Google describes a layered defense for Gemini and Workspace (monitoring the public web for IPI patterns, app-level protections in Gemini and Workspace apps, and continuous model and system hardening). See the vendor advisory and Workspace admin guidance for details.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection / RAG content poisoning ("GeminiJack") and privileged-component hijacking: attackers embed malicious instructions in retrieved documents/emails/calendar items or exploit Chrome/Gemini implementation flaws so the agent executes or returns sensitive data (exfil via crafted image/HTTP requests) or a malicious extension hijacks the Gemini panel to escalate privileges and access local files/camera/screenshots.
- **Affected Products:** Google Chrome (prior to 143.0.7499.192), Google Gemini Enterprise (Gemini RAG / Workspace integrations)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — reporting indicates at least one high-severity Chrome zero-day was exploited in the wild (see Infosecurity report: https://www.infosecurity-magazine.com/news/google-chrome-security-update/). Public weaponized PoC was not found in the retrieved corpus.
- **Patch Available:** true — Google released Chrome security updates addressing related issues (see Chrome stable-channel update Dec 10/11, 2025: https://chromereleases.googleblog.com/2025/12/stable-channel-update-for-desktop_10.html).
- **Active Exploitation:** true — active exploitation was reported (see Infosecurity and Unit42 coverage).
- **Threat Actors:** None known
- **Mitigation:** Vendor mitigations: layered defenses (User Alignment Critic, spotlighting, Agent Origin Sets / origin gating, prompt-injection classifier), plus Chrome security updates/patches. Operational mitigations include promptly applying Chrome updates, restricting agent data sources, and monitoring for poisoned/shared artifacts.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Incorrect bounds checks in multiple locations of the AVIF parser/decoder (CrabbyAVIF) cause out-of-bounds accesses of YUV/alpha/chroma plane calculations; these OOB accesses can, when combined with other bugs, enable remote code execution without user interaction.
- **Affected Products:** Android System (Android 16) versions prior to the August 2025 security patch level (security patch levels 2025-08-01 / 2025-08-05); reported affected devices in secondary sources include Pixel 3a, Samsung S10, OnePlus 7
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true — https://source.android.com/docs/security/bulletin/2025-08-01
- **Active Exploitation:** false
- **Threat Actors:** Threat actors unknown
- **Mitigation:** Apply the August 2025 Android security update (security patch level 2025-08-01 / 2025-08-05 as applicable) immediately; limit network exposure of vulnerable devices until patched (firewall/segmentation); rely on Android platform mitigations such as the Scudo hardened allocator (guard pages) and improved crash reporting to detect/prevent exploitation.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack class where LLMs or AI agents ingest external content (web pages, emails, files, calendar invites) that contains hidden or crafted instructions; those instructions are interpreted inside concatenated prompts or agent workflows and can cause data exfiltration or unsafe actions unless mitigated.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — public PoCs/payloads reported (examples: Unit42 report: https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/, X‑Labs: https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads, Trail of Bits writeup: https://blog.trailofbits.com/2025/08/06/prompt-injection-engineering-for-attackers-exploiting-github-copilot/, GitHub topic: https://github.com/topics/prompt-injection).
- **Patch Available:** false — no single product patch; vendor mitigation guidance published (see https://blog.google/security/mitigating-prompt-injection-attacks/).
- **Active Exploitation:** true — observed in the wild (examples: Unit42, X‑Labs). See field_basis for citations.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: prompt-injection content classifiers, intent-aware inspection, scoped access (least privilege), input/output validation and filtering, security-thought reinforcement, and keeping LLMs out of critical loops — follow vendor guidance (Google blog) and industry advisories (OWASP/CISA/CIS) for implementation details.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated Server-Side Request Forgery (SSRF) in the WebDialer service: crafted HTTP requests can trigger file writes to the underlying OS and be leveraged for root-level compromise on affected Cisco Unified CM / Unified CM SME systems.
- **Affected Products:** Cisco Unified Communications Manager (Unified CM), Cisco Unified CM SME — WebDialer service enabled
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — public proof-of-concept reported (see https://horizon3.ai/attack-research/vulnerabilities/cve-2026-20230/)
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true — multiple reports of active exploitation (Horizon3, TheHackerNews, HelpNetSecurity, BleepingComputer)
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-ssrf-cXPnHcW

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Pre-authenticated OS command-injection in Ivanti Sentry that allows a remote, unauthenticated attacker to execute OS-level commands (root-level on the appliance), enabling full appliance compromise and potential credential/data theft and lateral movement.
- **Affected Products:** Ivanti Sentry — versions before R10.5.2, R10.6.2, and R10.7.1
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Exploit Available:** true — public PoC released (e.g., Horizon3) and PoC/exploits observed in the wild (e.g., Rapid7 reporting)
- **Patch Available:** true — Ivanti released a security advisory and patches (see vendor advisory URL above)
- **Active Exploitation:** true — multiple sources report confirmed active exploitation in the wild (see basis pointers)
- **Threat Actors:** None known
- **Mitigation:** Apply Ivanti's published updates immediately (upgrade to the patched R10.5.2 / R10.6.2 / R10.7.1 releases as applicable). If immediate patching isn't possible, isolate or block internet access to Sentry management interfaces, restrict access via firewall/VPN, and monitor logs and credentials for suspicious activity.
- **Vendor Advisory:** https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523?language=en_US

---

## 11. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 12. 🟠 Zero-Day — Nissan discloses employee data breach linked to Oracle zero-day attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-29
**Reference:** <https://www.bleepingcomputer.com/news/security/nissan-discloses-employee-data-breach-linked-to-oracle-zero-day-attacks/>

> Nissan is warning that it suffered a data breach affecting current and former employees after threat actors exploited an Oracle PeopleSoft vulnerability in data theft attacks previously linked to the ShinyHunters extortion group. [...]

---

## 13. 🟠 Zero-Day — NAIC says public data stolen in ShinyHunters' PeopleSoft breach

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-29
**Reference:** <https://www.bleepingcomputer.com/news/security/naic-says-public-data-stolen-in-shinyhunters-peoplesoft-breach/>

> The National Association of Insurance Commissioners (NAIC) says the ShinyHunters extortion group stole only publicly available data, outdated logs, and configuration files after breaching its systems by exploiting a zero-day vulnerability in an Oracle PeopleSoft server. [...]

---

## 14. 🟡 High Severity — Apple Patches 30+ iOS, macOS, Safari Flaws, Including AI-Discovered WebKit Bugs

**CVE:** `CVE-2026-43707` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://thehackernews.com/2026/06/apple-patches-30-ios-macos-safari-flaws.html>

> Apple on Monday released security updates for iOS, macOS, and the Safari web browser to address over three dozen flaws, including four vulnerabilities in WebKit that were discovered using artificial intelligence (AI) tools like Anthropic Claude and OpenAI Codex Security.

The WebKit vulnerabilities are listed below -


  CVE-2026-43707 - A memory corruption issue that could result in an

---

## 15. 🟡 High Severity — Critical SimpleHelp flaw exploited to deploy new stealer malware

**CVE:** `CVE-2026-48558` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-29
**Reference:** <https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-simplehelp-flaw-deploy-new-djinn-infostealer-taskweaver-malware/>

> Hackers are exploiting a recently disclosed critical vulnerability (CVE-2026-48558) in SimpleHelp to deploy Djinn Stealer, a previously undocumented cross-platform information stealer targeting Windows, macOS, and Linux. [...]

---

## 16. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
