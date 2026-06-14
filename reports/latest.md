# Zero Day Pulse

> **Generated:** 2026-06-14 19:07 UTC &nbsp;|&nbsp; **Total:** 11 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is an unauthenticated path traversal vulnerability in SimpleHelp Remote Support/RMM that allows remote attackers to read arbitrary files on the server by supplying crafted path strings, leading to disclosure of logs, configuration files, and credentials.
- **Affected Products:** SimpleHelp Remote Support / Remote Monitoring and Management (RMM) – versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Public proof‑of‑concept exploit is available; see the OffSec analysis for details.
- **Patch Available:** SimpleHelp fixed the issue in versions released after 5.5.7; patch information is available via the vendor support portal.
- **Active Exploitation:** Confirmed active exploitation in the wild; ransomware actors are exploiting unpatched SimpleHelp instances.
- **Threat Actors:** Ransomware actors (e.g., DragonForce‑linked ransomware)
- **Mitigation:** Upgrade SimpleHelp to a version newer than 5.5.7. If upgrade is not possible, block management ports from untrusted networks, restrict access via firewall/VPN, segment the network, rotate credentials, and apply any vendor‑recommended hardening steps.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when adversarial instructions are embedded in external content (web pages, documents, search results, or retrieved context) that an LLM or agent ingests via retrieval or browsing. Attackers craft payloads that blend into benign content to bypass simple filters and rely on the model's instruction‑following behavior to execute the malicious directive. IPI can target RAG systems and agentic workflows that retrieve and incorporate external content into prompts; techniques demonstrated include poisoning web content, crafting natural‑language injection patterns, and exploiting retrieval pipelines and tool‑invocation logic.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoCs are available: http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability, https://arxiv.org/abs/2601.07072, https://www.infosecurity-magazine.com/news/researchers-10-wild-indirect/
- **Patch Available:** No vendor patch; mitigations recommended in advisory
- **Active Exploitation:** Yes, active exploitation has been reported in the wild.
- **Threat Actors:** None known
- **Mitigation:** Google recommends multiple mitigations including: (1) treat retrieved web content as untrusted, (2) use context filtering/sanitization and strict source validation, (3) apply retrieval and prompt engineering hardening (instruction‑following constraints, output filters), (4) use provenance and provenance‑aware ranking to prefer trusted sources, (5) limit agent capabilities and perform step validation and human‑in‑the‑loop for high‑risk actions.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) enables attackers to inject malicious instructions into data or tools used by an LLM, influencing the LLM’s behavior potentially without direct user input.
- **Affected Products:** Google Workspace with Gemini
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC or weaponized exploit referenced in this advisory.
- **Patch Available:** No vendor patch indicated; Google describes continuous defenses and updates rather than a discrete patch.
- **Active Exploitation:** Advisory does not report confirmed active exploitation; it references ongoing monitoring of public disclosures but no confirmed in‑the‑wild exploit.
- **Threat Actors:** None known
- **Mitigation:** Continuous, layered defenses including deterministic defenses (user confirmation, URL sanitization, tool‑chaining policies/config updates), ML‑based defenses with synthetic‑data retraining, LLM‑based prompt engineering, and Gemini model hardening.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The primary new threat is indirect prompt injection, where malicious sites craft content that causes the agentic browser AI to be manipulated via indirect prompts; Google mitigates this with layered defenses including a secondary oversight AI and origin/access restrictions.
- **Affected Products:** Chrome (agentic browsing / Gemini‑in‑Chrome features)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public exploit or PoC has been reported.
- **Patch Available:** No vendor patch is available; Google described new layered defenses (see advisory URL).
- **Active Exploitation:** No confirmed active exploitation has been reported.
- **Threat Actors:** None known
- **Mitigation:** Implement Google’s layered defenses: use the secondary AI overseer, restrict origin access for agentic features, keep Chrome updated, and follow guidance in the advisory URL.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A near‑miss linear buffer overflow in the CrabbyAVIF Rust library (unsafe Rust) was found and fixed pre‑release; Scudo hardened allocator’s guard pages rendered the overflow non‑exploitable and turned silent corruption into a noisy crash, aiding detection.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit available (vulnerability fixed pre‑release).
- **Patch Available:** Official patch available — commit: https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Use Scudo hardened allocator (guard pages) where possible; ensure crash reporting surfaces overflows into Scudo guard pages; apply the official patch (see commit link above); improve unsafe‑Rust review and training (new module in Comprehensive Rust training).
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injections embed hidden malicious instructions within external data sources (emails, documents, calendar invites, web content) that an AI system ingests; these instructions can cause the model to exfiltrate data or execute unauthorized actions. The technique leverages the model's tendency to follow natural‑language prompts without proper validation.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit/PoC unavailable
- **Patch Available:** No official patch; vendor mitigations/advice in advisory
- **Active Exploitation:** Some indirect prompt injection activity has been reported by researchers (e.g., Noma Labs' GeminiJack) and Google analyses note increased attempts, but no confirmed large‑scale in‑the‑wild exploitation is detailed in the advisory.
- **Threat Actors:** None known
- **Mitigation:** Use layered defense controls as described by Google: input sanitization, strict content handling, prompt engineering safeguards, context filtering and provenance checks, privilege separation, rate‑limiting and monitoring, and user confirmations for high‑risk actions.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors compromise routers and network devices (including backbone, provider edge, and customer edge routers), modify router software/configuration to maintain persistent, long‑term access, and leverage compromised devices and trusted connections to pivot into other networks.
- **Affected Products:** Major telecommunications backbone routers, provider edge (PE) routers, customer edge (CE) routers, and other compromised network devices
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit URLs identified.
- **Patch Available:** Vendor-specific patches vary; check vendor advisories for updates.
- **Active Exploitation:** Confirmed active exploitation in the wild; actors have maintained persistent access to government, telecom, transportation, lodging, and military infrastructure networks.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Apply vendor firmware patches and advisories; inventory and isolate affected routers; rotate/secure credentials; restrict management interfaces; enable logging/monitoring and network segmentation; apply CISA/FBI recommended hardening steps and detection signatures.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** The campaign employs phishing and credential theft to gain initial access, uses web shells or compromised credentials for lateral movement, harvests credentials for account takeover, and deploys custom GRU‑associated malware and tooling.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit / PoC unavailable (no public PoC or weaponized exploit linked in the advisory).
- **Patch Available:** Patch unavailable / No vendor patch indicated in CSA.
- **Active Exploitation:** Confirmed targeting/campaign activity reported (CSA states long‑running campaign since 2022 targeting Western logistics and technology companies).
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS), military unit 26165 (aka APT28 / Fancy Bear)
- **Mitigation:** Implement multi‑factor authentication (MFA), enforce least‑privilege access, apply vendor patches and updates, monitor for known indicators of compromise (IOCs), isolate sensitive systems, and follow incident‑response procedures.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** CVE‑2026‑45586: Elevation of privilege via a link‑following flaw (CWE‑59) in Windows Collaborative Translation Framework (CTFMON). CVE‑2026‑50507: Security feature bypass (CWE‑306) allowing BitLocker bypass with physical access. CVE‑2026‑44815: Stack‑based buffer overflow in DHCP Client Service exploitable via rogue DHCP responses. CVE‑2026‑45648: Out‑of‑bounds write in Active Directory Domain Services (NSPI RPC) leading to remote code execution. CVE‑2026‑44803 and CVE‑2026‑44812: Integer overflow in Win32K graphics component enabling remote code execution with user interaction.
- **Affected Products:** Windows 11 (OS builds 26200.8655, 26100.8655), Windows 10 (various builds), Windows Collaborative Translation Framework (CTFMON), Windows BitLocker, Windows DHCP Client Service, Windows Active Directory Domain Services, Windows Graphics/Win32K, Microsoft Defender components
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Proof‑of‑concept exploit published for the Microsoft Defender RoguePlanet zero‑day (source: The Hacker News) and for the BitLocker bypass (CVE‑2026‑50507) as noted by CrowdStrike; specific PoC URLs are not included in the sources.
- **Patch Available:** Microsoft released the cumulative update KB5094126 on June 9, 2026; details and download information are available on the Microsoft Support page.
- **Active Exploitation:** Defender zero‑day (RoguePlanet) vulnerabilities have been reported as exploited in the wild per media coverage; for other CVEs (e.g., CVE‑2026‑45586) CrowdStrike indicates no evidence of active exploitation.
- **Threat Actors:** None known
- **Mitigation:** Apply the June 9, 2026 cumulative update (KB5094126) as soon as possible; where patches are not yet available, restrict applications that can call vulnerable APIs, enforce physical security for BitLocker devices, and isolate DHCP services to prevent rogue server attacks.
- **Vendor Advisory:** https://support.microsoft.com/en-us/topic/june-9-2026-kb5094126-os-builds-26200-8655-and-26100-8655-1a9bcba6-5f53-4075-8156-fe11ac631737

---

## 10. 🟠 Zero-Day — When a Government Pulls an AI Model: What the Fable 5 and Mythos 5 Suspension Means for Security Teams

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Snyk Vulnerability Research &nbsp;|&nbsp; **Published:** 2026-06-14
**Reference:** <https://snyk.io/blog/fable-mythos-suspension-security-takeaways/>

> On June 12, 2026, a US export-control directive led Anthropic to disable Claude Fable 5 and Mythos 5 worldwide over a reported jailbreak. The reported trigger was a code-analysis capability that defenders use routinely. Here is what happened, how the security community read it, and what security teams can take from it.

**Parallel AI Enrichment:**

- **Technical Details:** Anthropic disabled access after a reported jailbreak that used the models' code‑analysis capability to bypass guardrails and enable restricted behavior; the mechanism involved prompt/model jailbreak techniques abusing code‑analysis features.
- **Affected Products:** Claude Fable 5, Claude Mythos 5
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit reported; reported trigger was a code-analysis jailbreak capability but no public exploit URL available.
- **Patch Available:** Patch not applicable; vendor (Anthropic) disabled access to models per U.S. export-control directive. Vendor advisory URL unavailable.
- **Active Exploitation:** No confirmed active exploitation in the wild reported in sources; suspension followed a government export‑control directive citing national‑security concerns.
- **Threat Actors:** None known
- **Mitigation:** For security teams: restrict use of model‑run code analysis features for unvetted/foreign users; apply least privilege, monitoring and logging of model outputs, limit sensitive tasks to vetted/trusted models and environments, isolate AI‑assisted code analysis to air‑gapped or internal‑only instances where possible, and maintain vendor communication channels for updates.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
