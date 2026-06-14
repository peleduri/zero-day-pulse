# Zero Day Pulse

> **Generated:** 2026-06-14 13:26 UTC &nbsp;|&nbsp; **Total:** 10 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 9 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** An unauthenticated path traversal allows crafted HTTP requests (e.g., /toolbox-resource/../serverconfig.xml) to download arbitrary files such as serverconfig.xml containing hashed credentials, which can be chained with other flaws for remote code execution.
- **Affected Products:** SimpleHelp remote support/RMM software versions 5.5.7 and earlier, 5.4.x prior to 5.4.10, 5.3.x prior to 5.3.9
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true — https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2024/CVE-2024-57727.yaml
- **Patch Available:** true — https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know
- **Active Exploitation:** true
- **Threat Actors:** DragonForce and other ransomware actors
- **Mitigation:** Upgrade SimpleHelp to version 5.5.8 or later (or 5.4.10, 5.3.9). If a patch cannot be applied, isolate the SimpleHelp servers, block external access, apply vendor‑recommended mitigations, and perform threat hunting per CISA guidance.
- **Vendor Advisory:** https://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an AI system ingests web content (e.g., browsing, retrieval‑augmented‑generation, or reading external corpora) that contains adversarially‑crafted instructions or payloads which alter the model's behavior or cause data exfiltration. Attacks observed include seeding prompt‑injection content on public web pages and leveraging agents or RAG pipelines to surface those pages to the model, enabling instruction override or data leakage.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Implement Google's recommended mitigations: avoid blindly executing or surfacing untrusted web content to AI systems; enforce provenance checks, content sanitization, strict browsing policies for agents, and monitoring for prompt‑injection indicators.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) in RAG workflows: attacker plants malicious instructions in shared Workspace content (Docs/Calendar/Gmail). When Gemini Enterprise retrieves that content into model context, the model interprets the embedded instructions as legitimate, performs broader searches across accessible datasources, and exfiltrates results (e.g., via external image URL callbacks).
- **Affected Products:** Google Gemini Enterprise (RAG across Workspace data sources: Gmail, Google Calendar, Docs/Drive)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Google’s layered defenses – prompt‑injection content classifiers, markdown sanitization, suspicious URL redaction, user confirmation framework, security thought reinforcement, model resilience, and centralized policy engine. Administrators should follow Google Workspace guidance for configuring datasource access and apply the recommended policies.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection allows malicious web content to manipulate agentic AI prompts (e.g., for Gemini in Chrome). Noma Labs demonstrated a chained zero‑click exploit (GeminiJack) leveraging indirect prompt injection against Google Gemini Enterprise; NVD entry CVE‑2025‑54131 documents chaining with indirect prompt injection.
- **Affected Products:** Chrome (agentic browsing / Gemini integration)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Use Google’s layered defenses for agentic browsing – restrict origin access to agentic contexts, add a supervisory agent to validate actions, and block or sanitize untrusted content from influencing agent prompts. Apply Chrome updates when available and follow Google’s guidance in the advisory.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A near‑miss linear buffer overflow in CrabbyAVIF (unsafe Rust) was discovered and fixed before release; Android’s Scudo hardened allocator and guard pages rendered the issue non‑exploitable and converted overflow into a crash; the issue was tracked as CVE‑2025‑48530.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true (patch: https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use Scudo hardened allocator (guard pages), improve crash reporting for overflow detection, add training and stricter reviews for unsafe Rust, and encapsulate unsafe code; patch applied to CrabbyAVIF.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) embeds malicious instructions in external data sources (emails, documents, calendar invites, images/URLs) that an AI agent may ingest and follow; mitigations focus on preventing LLMs from executing adversarial instructions via training, runtime detectors, sanitization, URL redaction, and requiring explicit user confirmation.
- **Affected Products:** Gemini (Google Workspace, Gemini app), Gemini 2.5 models
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses including model hardening/adversarial training, purpose‑built ML detectors for malicious instructions, "security thought reinforcement", markdown sanitization and external URL/suspicious‑URL redaction, contextual user confirmation (human‑in‑the‑loop), end‑user mitigation notifications and Threat Intel/VRP collaboration.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Threat actors modify router configurations to create unauthorized ACLs, change TACACS+/RADIUS settings, and deploy virtualized containers on devices to achieve persistence and evade detection, enabling lateral movement across networks.
- **Affected Products:** Ivanti (CVE‑2024‑21887); Cisco IOS XE (CVE‑2023‑20273, CVE‑2023‑20198); Cisco IOS/IOS XE (CVE‑2018‑0171)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Chinese state‑sponsored actors (e.g., Salt Typhoon)
- **Mitigation:** Prioritize patching edge devices; monitor device logs and configurations for unexpected ACLs, TACACS+/RADIUS changes, and virtual container activity; disable unused ports and protocols; change default credentials; require public‑key authentication; use vendor‑recommended OS versions.
- **Vendor Advisory:** Vendor advisory URL unavailable.

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
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Russian GRU (85th GTsSS / Unit 26165), also known as APT28
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** CVE‑2026‑45586 exploits a link‑following flaw in CTFMON (CWE‑59) for local privilege escalation; CVE‑2026‑50507 bypasses BitLocker authentication (CWE‑306) allowing physical‑access credential theft; CVE‑2026‑26142 uses insecure deserialization in Nuance PowerScribe for remote code execution; CVE‑2026‑44815 triggers a stack‑based buffer overflow in the DHCP client to achieve remote code execution.
- **Affected Products:** Windows 10, Windows 11, Windows Server 2019, Windows Server 2022, Microsoft Defender, Microsoft Exchange, BitLocker, Nuance PowerScribe, DHCP client, Remote Desktop Client, Device Health Attestation, Graphics drivers, Kernel components
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/
- **Patch Available:** true — https://msrc.microsoft.com/update-guide/
- **Active Exploitation:** true — https://redlegg.com/blog/security-bulletin-multiple-microsoft-defender-vulnerabilities-exploited-in-the-wild?hs_amp=true, https://thehackernews.com/2026/06/microsoft-defender-rogueplanet-zero-day.html
- **Threat Actors:** None known
- **Mitigation:** Apply the June 2026 security updates (KB5094126) immediately. For unpatched issues, restrict access to affected services, enforce physical device protection, limit apps that can call vulnerable APIs, segment networks, and enable Microsoft Defender/E DR detections.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/

---

## 10. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

**Parallel AI Enrichment:**

- **Technical Details:** A malicious DNS response can trigger out‑of‑bounds reads, writes, and other memory issues in the modem's DNS parser; replacing the unsafe C/C++ parser with a memory‑safe Rust implementation (hickory‑proto adapted for no_std) mitigates this class of memory‑safety vulnerabilities.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Use of a memory‑safe Rust DNS parser in Pixel 10 modem firmware; general hardening and `no_std` Rust integration steps as described in the vendor post. If a patch is not yet available, update device firmware when vendor releases are provided.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html

---
