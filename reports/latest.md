# Zero Day Pulse

> **Generated:** 2026-06-28 08:40 UTC &nbsp;|&nbsp; **Total:** 10 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 9 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 6

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Directory traversal vulnerability allowing attackers to read sensitive files via path traversal, enabling unauthenticated remote attackers to access files
- **Affected Products:** SimpleHelp remote support software v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit steps unavailable.
- **Patch Available:** Patch released within two days of reporting; see vendor advisory
- **Active Exploitation:** Confirmed exploitation reported by CISA, leveraging CVE-2024-57727
- **Threat Actors:** Ransomware actors
- **Mitigation:** Apply the vendor patch or upgrade to a version newer than 5.5.7
- **Vendor Advisory:** http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI / IDPI) occurs when attacker-controlled content (web pages or user-controlled documents/emails) is retrieved into a model’s context (RAG or agent workflows) and contains hidden or obfuscated instructions; the LLM ingests those instructions and may follow them, enabling data exfiltration, bypasses (e.g., ad-review), or other malicious actions. Techniques include dynamic runtime assembly (Base64/DOM injection, canvas/OCR hiding), instruction obfuscation, and delivery via shared documents or calendar invites.
- **Affected Products:** Google Gemini Enterprise (RAG integrations for Google Workspace: Gmail, Google Calendar, Google Docs) — impacted RAG/data-source integrations
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public, documented in-the-wild examples and demonstration payloads have been reported (Unit42’s observed IDPI ad-review bypass and Noma’s GeminiJack writeup), but no single vendor-published weaponized PoC repository or CVE exploit package is listed in the cited sources.
- **Patch Available:** No single vendor 'patch' or CVE-style bulletin was published; Google describes continuous defenses, layered mitigations and its AI Vulnerability Rewards Program (VRP) instead (see vendor blog posts).
- **Active Exploitation:** Yes — Google reports experimentation and an uptick in IPI detections on the public web, and third-party telemetry (Palo Alto Unit42) documents observed real-world IDPI activity including a December 2025 ad-review bypass example.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: harden RAG ingestion and retrieval boundaries, continuous automated and human red‑teaming, integrate VRP findings, detect/flag anomalous prompt payloads at web-scale, use content-disallow/whitelists for high-privilege queries, apply static+dynamic analysis of fetched content, and follow community guidance (e.g., OWASP LLM Prompt Injection cheat sheet).
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: hidden/malicious instructions embedded in external data sources (web content, emails, documents, calendar invites) that can cause a generative AI or agent to reveal sensitive data or perform unauthorized actions.
- **Affected Products:** Generative AI systems and AI-powered browsers/agents (vendor-agnostic); Google notes mitigation integrated in Gemini 2.5
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof-of-concept code exists (benign PoCs demonstrating indirect prompt injection in AI browsers); no widely reported weaponized exploit in the cited corpus.
- **Patch Available:** No traditional "patch" reported; Google describes product-level mitigations integrated into Gemini 2.5 and a layered defense (see advisory).
- **Active Exploitation:** Yes — industry and vendor reporting indicates indirect prompt-injection activity observed in the wild (Google web sweep and Unit42 analysis).
- **Threat Actors:** None known
- **Mitigation:** Layered defenses across the prompt lifecycle: input sanitization and validation, limiting model access to sensitive sources, product-level guardrails (as rolled into Gemini 2.5), and monitoring for known indirect injection patterns.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors gain initial access by exploiting widely known/public CVEs in internet-facing edge devices (T1190) rather than observed zero-days; techniques include WSMA endpoint authentication bypass (example: CVE-2023-20198 on Cisco IOS XE with double-encoded paths), use of Guest Shell to run scripts and native tooling for post-exploitation, creation/modification of accounts and ACLs for persistence, SNMP abuse, establishing GRE/IPsec tunnels for covert exfiltration and routing changes, and collection of configuration and BGP/MPLS state to map and pivot.
- **Affected Products:** Cisco IOS / IOS XE (including Guest Shell/IOx), Cisco NX‑OS, Palo Alto Networks PAN‑OS (GlobalProtect configurations), Ivanti Connect Secure / Ivanti Policy, Fortinet (potential), Juniper (potential), Nokia routers and switches (potential), Sierra Wireless (potential), SonicWall (potential), Microsoft Exchange (potential)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public exploit tooling and scripts have been observed/ referenced (examples: publicly available siet.py and other exploit/tooling referenced by CISA and analysis partners); PoCs/tooling exist for several of the cited CVEs (CVE-dependent).
- **Patch Available:** Vendor patches are available for many of the CVEs cited in CISA AA25-239A (organizations are advised to apply vendor-supplied updates for affected products); status is CVE/vendor-dependent and organizations should follow vendor CVE advisories referenced from CISA.
- **Active Exploitation:** Confirmed — CISA and allied agencies report these PRC‑linked APT actors have exploited publicly known CVEs in the wild against network edge devices; corroborated by vendor-agnostic analysis and national cyber centres.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching of the high-risk CVEs CISA lists; disable unused ports/protocols and unencrypted management protocols; change default credentials and require public‑key authentication for admin roles where feasible; monitor firmware/software integrity (compare hashes to vendor known-good), perform configuration integrity checks and monitor for unauthorized changes, restrict SNMP and management access, and perform threat hunting on CLI activity, ACL and route changes.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** GRU unit 26165 conducts cyber-espionage against logistics and technology companies using initial access via exploitation of internet-facing infrastructure (corporate VPNs and public-facing application vulnerabilities including WinRAR CVE-2023-38831 and Roundcube CVEs), spearphishing, credential theft, and living-off-the-land binaries; activity is mapped to MITRE ATT&CK tactics (Initial Access, Execution, Persistence, Privilege Escalation, Credential Access, Lateral Movement, Collection, C2).
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) or weaponized exploit URLs are provided in the advisory.
- **Patch Available:** Patches or vendor updates exist for the referenced CVEs (e.g., WinRAR CVE-2023-38831 and Roundcube CVE-2020-35730 / CVE-2020-12641); consult vendor advisory pages for each product for the specific patch URLs.
- **Active Exploitation:** Advisory describes active targeting and a campaign but does not state a confirmed single-instance active exploitation of a disclosed CVE in the wild; the campaign is ongoing espionage activity described by CISA.
- **Threat Actors:** Russian GRU (Unit 26165 / 85th GTsSS), tracked in industry as APT28 / Fancy Bear and related aliases.
- **Mitigation:** Apply vendor patches for referenced CVEs, implement network segmentation and Zero Trust principles, disable unnecessary remote access to IP cameras, restrict/allowlist access via firewalls, monitor and hunt for the listed IOCs and LOTL usage, and follow the detailed mitigation actions in the CISA advisory.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 10. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

**Parallel AI Enrichment:**

- **Technical Details:** A malicious DNS response can trigger a number of out-of-bounds reads, writes, and other memory issues.
- **Affected Products:** Google Android 13, Google Pixel (custom firmware versions prior to 20240305)
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** No public proof-of-concept or exploit is known.
- **Patch Available:** Patch available via Android security bulletin: https://source.android.com/security/bulletin/pixel/2024-03-01
- **Active Exploitation:** No confirmed active exploitation in the wild has been reported.
- **Threat Actors:** None known
- **Mitigation:** Google hardens the cellular baseband modem and integrates a memory-safe Rust DNS parser into the firmware.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html

---
