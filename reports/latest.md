# Zero Day Pulse

> **Generated:** 2026-06-30 13:56 UTC &nbsp;|&nbsp; **Total:** 17 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 13 &nbsp;|&nbsp; 🟡 High: 4 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal (directory traversal) vulnerability that allows unauthenticated attackers to craft requests which read sensitive files from the SimpleHelp RMM server (CVE-2024-57727).
- **Affected Products:** SimpleHelp remote support / Remote Monitoring and Management (RMM) software v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — public technical writeups and analyses describe exploitation of the path-traversal; combined with CISA reporting of in-the-wild ransomware activity, this indicates weaponized exploitation has been used. (No single public PoC URL is present in the provided corpus.)
- **Patch Available:** Yes — SimpleHelp reported the vulnerabilities in versions 5.5.7 and earlier were patched within two days of being reported; see vendor advisory at http://guides.simple-help.com/kb---security-vulnerabilities-01-2025
- **Active Exploitation:** Confirmed — CISA reports ransomware actors exploited unpatched SimpleHelp RMM (CVE-2024-57727) to compromise a utility billing software provider and noted likely exploitation of unpatched instances (CISA advisory).
- **Threat Actors:** Ransomware actors (unspecified)
- **Mitigation:** Apply the vendor-supplied patches/updates (update SimpleHelp off versions 5.5.7 and earlier to a fixed release) and limit network exposure of management interfaces; follow vendor KB guidance at the provided advisory.
- **Vendor Advisory:** http://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — CISA: Windows BlueHammer flaw now exploited by ransomware gangs

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-windows-bluehammer-flaw-now-exploited-by-ransomware-gangs/>

> CISA confirmed on Monday that ransomware gangs are now exploiting a Microsoft Defender privilege escalation vulnerability, dubbed BlueHammer, that has previously been abused in zero-day attacks. [...]

**Parallel AI Enrichment:**

- **Technical Details:** BlueHammer abuses the Windows Defender update process (including Volume Shadow Copy / update logic) using race/timing and filesystem/path confusion to escalate local privileges to SYSTEM (local privilege escalation).
- **Affected Products:** Microsoft Defender (Windows Defender) on Windows (specific Windows versions not specified in the supplied sources).
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — a public proof-of-concept was published in April 2026 and weaponized exploits/PoCs were observed in the wild (sources report PoC publication and Huntress-observed weaponization).
- **Patch Available:** No official vendor patch reported in the supplied sources; reporting describes BlueHammer/related RedSun as an unpatched zero-day as of the referenced coverage.
- **Active Exploitation:** Confirmed — multiple reports and CISA action indicate active exploitation in the wild (reports of weaponized use and CISA adding BlueHammer to Known Exploited Vulnerabilities).
- **Threat Actors:** Ransomware gangs (unnamed — reporters/CISA say ransomware operators are exploiting the flaw but do not name specific groups).
- **Mitigation:** No vendor patch or specific vendor workaround is present in the supplied sources. CISA has ordered agencies to patch promptly; recommended mitigation in the corpus is to apply vendor updates when available and follow CISA guidance. (No detailed temporary workaround is provided in the supplied documents.)
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — Oracle E-Business Suite Flaw CVE-2026-46817 Actively Exploited in the Wild

**CVE:** `CVE-2026-46817` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://thehackernews.com/2026/06/oracle-e-business-suite-flaw-cve-2026.html>

> A critical security flaw impacting Oracle E-Business Suite has come under active exploitation in the wild, according to Defused Cyber.

The vulnerability, tracked as CVE-2026-46817 (CVSS score: 9.8), refers to an improper privilege management and authentication flaw in Oracle Payments that could be abused to take over susceptible instances.

&quot;Easily exploitable vulnerability allows

**Parallel AI Enrichment:**

- **Technical Details:** An improper privilege management / missing or improper authentication flaw in the Oracle Payments component of Oracle E-Business Suite that allows an unauthenticated attacker with network (HTTP) access to compromise and potentially take over Oracle Payments.
- **Affected Products:** Oracle E-Business Suite — Oracle Payments component: versions 12.2.3 through 12.2.15
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) or public exploit code is known; reporting states "no public PoC" while also reporting observed exploitation on Oracle E-Business honeypots.
- **Patch Available:** Yes — Oracle shipped patches as part of its May 2026 Critical Security Patch Update (CSPU): https://www.oracle.com/security-alerts/cspumay2026verbose.html
- **Active Exploitation:** Yes — active exploitation has been reported: Defused Cyber reported observing an actor exploiting the vulnerability on Oracle E-Business honeypots (this observation is reported in multiple news summaries).
- **Threat Actors:** None known
- **Mitigation:** Apply Oracle's May 2026 Critical Security Patch Update (CSPU) patches for Oracle E-Business Suite (Oracle Payments). The supplied corpus does not include a vendor-published temporary workaround; if patching is delayed, standard mitigations to consider include restricting HTTP/network access to Payments interfaces, applying a WAF, and monitoring for anomalous activity (these additional mitigations are general best-practices and are not detailed in the cited vendor/media segments).
- **Vendor Advisory:** https://www.oracle.com/security-alerts/cspumay2026verbose.html

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an attack class where adversaries place or seed malicious prompts in external content (web pages, external corpora, or runtime-generated browser content) that AI agents, retrieval-augmented generation (RAG) systems, or agentic/browsing models retrieve and incorporate, causing the model to follow attacker-controlled instructions. Researchers have demonstrated end-to-end IPI exploits against RAG and agentic systems and reported a zero-click example (GeminiJack) that used an indirect prompt injection inside Google Gemini Enterprise.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof-of-concept / research demonstrations exist (academic/arXiv end-to-end IPI exploit writeups and the Noma Labs GeminiJack disclosure describing a zero-click IPI-based vulnerability).
- **Patch Available:** No single vendor patch is described; vendor advisory and mitigation guidance published at http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html
- **Active Exploitation:** No confirmed, attributed widespread active exploitation in the wild is reported in the cited materials; the vendor and researchers describe practical PoCs and real-world demonstrations but do not attribute active campaigns to named threat actor groups.
- **Threat Actors:** None known
- **Mitigation:** Apply content-source restrictions and hardening: limit or whitelist browsing/external sources; sanitize or canonicalize retrieved external content before inclusion in prompts/RAG context; apply model-level guardrails and prompt-sanitization/validation layers; continuous monitoring and threat-hunting for injected content. (Vendor guidance and ongoing mitigation work rather than a single product patch.)
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an attack technique in which adversarial instructions are embedded inside external content (web pages, documents, or other corpora) that a generative AI system later ingests (via browsing, retrieval-augmented generation, or tool outputs). When that content is included in the model's prompt/context, the injected instructions can influence model behavior (including data exfiltration or unauthorized actions) without explicit user-supplied malicious input.
- **Affected Products:** Google Gemini (Gemini app / Gemini in Workspace), Google Gemini Enterprise / Vertex AI Search, any Generative AI system that ingests external web content or RAG/agentic tool outputs
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof-of-concept / exploit demonstrations exist (examples: Noma Labs 'GeminiJack' disclosure and writeup; academic IPI exploit papers; industry catalogs of IPI payloads). Example sources: https://noma.security/blog/geminijack/, https://arxiv.org/html/2403.14720v1, https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads
- **Patch Available:** No single vendor 'patch' for the IPI technique; Google published mitigation guidance and layered defenses in its advisory (see vendor_advisory). For the Noma Labs 'GeminiJack' disclosure there is a public researcher writeup, but I did not find an authoritative vendor patch advisory or CVE/patched notice in the searched sources.
- **Active Exploitation:** Yes — multiple industry reports and telemetry indicate IPI payloads and attempts are being observed on the public web (industry writeups/catalogs report payloads found in the wild), though attribution to named APTs or ransomware groups is not provided.
- **Threat Actors:** None known
- **Mitigation:** Use a layered defense: model hardening (resilience improvements), purpose-built ML detectors for malicious instructions, system-level safeguards around tool use and browsing, input/output validation and sanitization, limit ingestion of untrusted external content, enforce human oversight for sensitive actions, and apply RAG/tool access controls. See vendor guidance for details.
- **Vendor Advisory:** https://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Class: indirect prompt injection — untrusted web content (pages, iframes, user-generated content) can influence an agentic planner model to perform unintended actions (e.g., financial transactions or data exfiltration). Mitigations constrain which origins/content the planner can see, vet planned actions via an isolated Alignment Critic, and force deterministic checks and user confirmations before impactful actions.
- **Affected Products:** Google Chrome (Gemini / agentic browsing capability)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit reported in the vendor advisory; none found in the collected guidance.
- **Patch Available:** No single CVE-style patch reported; vendor released architectural/feature mitigations in Chrome (see advisory URL).
- **Active Exploitation:** No confirmed active exploitation reported in the vendor advisory or in the collected guidance as of the advisory's publication.
- **Threat Actors:** None known
- **Mitigation:** User Alignment Critic (action vetting), origin-isolation / origin sets (read-only vs read-write origins), gating/approval for new origins and model-generated URLs, user confirmations and work-log transparency for sensitive actions, a prompt-injection classifier plus Safe Browsing integration, continuous red-teaming and monitoring, and VRP rule updates for agentic issues.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Out-of-bounds accesses caused by an incorrect bounds check in the Rust CrabbyAVIF image library, resulting in a linear buffer overflow. Could enable remote code execution in combination with other bugs; no additional privileges required and no user interaction needed.
- **Affected Products:** Android System component (AOSP 16)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC referenced by the vendor advisory or NVD entry.
- **Patch Available:** Yes. Addressed in the Android Security Bulletin—August 2025 (security patch levels 2025-08-05 or later) with AOSP fixes for CVE-2025-48530; see the bulletin and linked AOSP changes.
- **Active Exploitation:** No confirmed active exploitation; Google states the vulnerability never made it into a public release.
- **Threat Actors:** None known
- **Mitigation:** Enable and mandate Android’s Scudo hardened allocator; Scudo’s guard pages rendered the issue non-exploitable and aided detection. Apply the CrabbyAVIF patch referenced by Google.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI): attackers embed hidden or covert instructions inside external content (web pages, emails, documents, calendar invites) that are consumed by AI agents; when an agent processes poisoned content it can follow attacker-supplied instructions (e.g., exfiltrate data or perform unauthorized actions) instead of the user’s intent. Attacks often defer commands or use the AI’s text-processing role to create staged exfiltration or action sequences.
- **Affected Products:** Gemini (app) and Gemini in Workspace integrations — Gmail, Docs editors, Drive, Chat; affected products (specific versions) unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — public proof-of-concept demonstrations and weaponized IPI payloads have been reported (examples: Forcepoint, Help Net Security, Tenable research, independent write-ups). See vendor and industry reports for examples.
- **Patch Available:** No single downloadable "patch." Google published a layered-defense advisory and has implemented product-level mitigations for Gemini and Gemini-in-Workspace (see vendor advisory URLs).
- **Active Exploitation:** Yes — multiple industry reports and research posts document IPI payloads and proof-of-concept demonstrations in the wild; product-specific indirect-prompt-injection CVEs have also been published (e.g., EchoLeak-related disclosures).
- **Threat Actors:** None known
- **Mitigation:** Apply a layered defense: treat external content as untrusted, perform content filtering/classification and provenance checks, enforce instruction precedence and policy, gate or restrict sensitive function calls and capabilities, and apply product-level/server-side hardening as described in Google’s layered-defense guidance.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/ ; https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** At least one high-profile CVE referenced (CVE-2026-20230) is a server-side request forgery (SSRF) in Cisco Unified CM WebDialer that allows unauthenticated crafted HTTP requests to enable file writes to the underlying OS and can lead to root-level compromise. The broader campaign targets backbone/PE/CE routing devices and leverages compromised network devices and trusted connections to pivot, modify routers for persistent access, and conduct espionage.
- **Affected Products:** Cisco Unified Communications Manager (WebDialer), Palo Alto Networks products, Ivanti Connect Secure / Policy Secure, Fortinet (FortiGate), Juniper network devices, Microsoft Exchange (and other network device / remote-access products) (see CISA Appendix B per-CVE list)
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof-of-concept (PoC) reported for at least one CVE discussed in the advisory (CVE-2026-20230); PoC publication and exploit code availability reported by security researchers (see Horizon3.ai reporting).
- **Patch Available:** Yes — vendor advisory published for at least CVE-2026-20230 (Cisco published advisory referenced as cisco-sa-cucm-ssrf-cXPnHcW on June 3, 2026). Patch/advisory status for other CVEs varies by vendor; see CISA Appendix B and vendor bulletins.
- **Active Exploitation:** Active exploitation has been reported for specific CVEs referenced in the advisory — notably CVE-2026-20230 — with security researchers reporting exploitation activity in June 2026 and the CVE entered into government tracking (CISA/NVD). The original AA25-239A advisory (Aug 2025) noted no observed zero-day exploitation at publication time, but subsequent CVE disclosures changed that status for some vulnerabilities.
- **Threat Actors:** People’s Republic of China (PRC) state-sponsored actors — named groups referenced in analyses include Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Follow CISA AA25-239A and vendor advisories: apply vendor-supplied security updates immediately, disable or restrict access to vulnerable services (e.g., WebDialer/management interfaces), restrict management-plane access to trusted networks, apply least-privilege and network segmentation, and monitor for IOCs described in CISA/vendor advisories.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** GRU Unit 26165 conducted cyber-espionage against logistics and technology firms using spearphishing and exploitation of known vulnerabilities (examples: CVE-2023-23397, CVE-2023-38831, Roundcube CVEs), credential theft and webshells/backdoors for persistence, and C2 to exfiltrate data. The advisory includes IOCs/STIX for detection.
- **Affected Products:** Microsoft Outlook (CVE-2023-23397), WinRAR (CVE-2023-38831), Roundcube webmail (Roundcube CVEs)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** AA25-141A does not publish public proof-of-concept (PoC) or weaponized exploit code; third-party vendors published defensive emulation templates and recommended applying vendor CVE patches (no PoC links are cited in the advisory/coverage collected).
- **Patch Available:** Yes — the advisory and responder community recommend applying vendor patches for the referenced CVEs (examples cited: CVE-2023-23397 for Outlook, CVE-2023-38831 for WinRAR, and Roundcube CVEs). The AA25-141A advisory itself does not include vendor patch URLs.
- **Active Exploitation:** Yes — the joint CISA/FBI advisory describes a long-running campaign actively targeting Western logistics and technology entities (reported since 2022).
- **Threat Actors:** Russian GRU 85th GTsSS (Unit 26165) — tracked in industry reporting as APT-28
- **Mitigation:** Prioritize and apply vendor patches for referenced CVEs, enable and enforce MFA, monitor and hunt using the provided IOCs/STIX, harden remote access, segment networks, and follow the detection and containment guidance in the AA25-141A advisory.
- **Vendor Advisory:** Vendor advisory URL unavailable.

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

## 14. 🟡 High Severity — Attackers Exploit SimpleHelp CVE-2026-48558 to Deploy TaskWeaver and Djinn Stealer

**CVE:** `CVE-2026-48558` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://thehackernews.com/2026/06/attackers-exploit-simplehelp-cve-2026.html>

> An unknown threat actor has been observed exploiting a recently disclosed maximum-severity security flaw in SimpleHelp to deliver two previously unreported malware families, TaskWeaver and Djinn Stealer.

The intrusion involves the exploitation of CVE-2026-48558 (CVSS score: 10.0), a critical authentication bypass vulnerability impacting the OpenID Connect (OIDC) flow that an unauthenticated

---

## 15. 🟡 High Severity — Progress Kemp LoadMaster Flaw Could Let Attackers Run Root Commands Pre-Auth

**CVE:** `CVE-2026-8037` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://thehackernews.com/2026/06/progress-kemp-loadmaster-flaw-could-let.html>

> A critical vulnerability in Progress Kemp LoadMaster can let an unauthenticated attacker execute arbitrary commands as root on the appliance by sending a crafted request to its API.

The flaw, tracked as CVE-2026-8037, carries a CVSS score of 9.8 according to ZDI. A patch is available. If you run LoadMaster with the API enabled, update now.

Progress published its advisory on June

---

## 16. 🟡 High Severity — Apple Patches 30+ iOS, macOS, Safari Flaws, Including AI-Discovered WebKit Bugs

**CVE:** `CVE-2026-43707` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-29
**Reference:** <https://thehackernews.com/2026/06/apple-patches-30-ios-macos-safari-flaws.html>

> Apple on Monday released security updates for iOS, macOS, and the Safari web browser to address over three dozen flaws, including four vulnerabilities in WebKit that were discovered using artificial intelligence (AI) tools like Anthropic Claude and OpenAI Codex Security.

The WebKit vulnerabilities are listed below -


  CVE-2026-43707 - A memory corruption issue that could result in an

---

## 17. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
