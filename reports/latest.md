# Zero Day Pulse

> **Generated:** 2026-06-30 02:06 UTC &nbsp;|&nbsp; **Total:** 16 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 4 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** A path traversal / directory traversal vulnerability (CVE-2024-57727) in SimpleHelp RMM that allows unauthenticated remote attackers to read sensitive files via crafted path traversal requests.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) / remote support software — versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) or publicly released weaponized exploit identified in the provided sources; however, CISA and other sources report active exploitation in the wild.
- **Patch Available:** Yes — vendor released patches and published guidance (see vendor advisory: http://guides.simple-help.com/kb---security-vulnerabilities-01-2025).
- **Active Exploitation:** Yes — CISA reports ransomware actors likely leveraged CVE-2024-57727 against unpatched SimpleHelp RMM to access downstream customers and to compromise a utility billing software provider.
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor patch/upgrade per the SimpleHelp advisory; restrict or firewall SimpleHelp management/RMM interfaces from direct internet access, isolate affected instances, and review logs and downstream customer access as recommended in the vendor guidance and CISA advisory.
- **Vendor Advisory:** http://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when attacker-controlled content in external sources (web pages, documents, comments, or dynamically constructed browser content) is ingested as context by LLMs or agentic systems (RAG/agents). Because the model treats that content as part of its prompt, carefully crafted instructions in the external content can cause the model/agent to follow attacker directives (data exfiltration, unauthorized actions, or execution). Dynamic runtime construction of prompts and lack of provenance/trust checks make RAG and agentic flows particularly vulnerable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes. Public research and disclosed exploits/PoCs exist (e.g., Noma Labs’ GeminiJack zero-click disclosure and academic end-to-end IPI demonstrations).
- **Patch Available:** No single vendor patch — Google published guidance/advisory instead: http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html
- **Active Exploitation:** Yes. Google and industry researchers found IPI payloads on public web content and multiple groups published PoCs/demonstrations (vendor blog, industry reports, and research disclosures).
- **Threat Actors:** None known
- **Mitigation:** Harden RAG/agent pipelines and external data handling: continuous monitoring of external content, restrict or throttle agent access to arbitrary web sources, apply provenance and source whitelisting, sanitize/filter third-party content before inclusion in prompts, implement application-level instruction guards and confirmation for risky actions, and monitor telemetry for anomalous agent behavior.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an attack class where an adversary injects malicious instructions into data or tools consumed by an LLM (for example external corpora used by RAG or outputs from agentic tools), causing the LLM to follow those instructions and alter behavior even without direct user input. Research has demonstrated end-to-end IPI exploits against RAG and agentic systems.
- **Affected Products:** Google Workspace (with Gemini), other LLM-based agentic systems and Retrieval-Augmented Generation (RAG) pipelines that ingest external corpora or tool outputs
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — academic/technical proof-of-concept end-to-end IPI exploits have been published (research/arXiv) and security researchers/vendors have reported IPI payloads observed on the public web.
- **Patch Available:** No discrete vendor "patch" for a single CVE is announced in the advisory; Google describes continuous hardening and improved defenses rather than a single released patch or CVE fix (see vendor advisory).
- **Active Exploitation:** Google and other researchers have observed IPI attempts and payloads on public websites and reported an increase in malicious attempts; vendors/research groups have documented payloads caught in the wild.
- **Threat Actors:** None known
- **Mitigation:** No single patch; recommended mitigations described by the vendor are continuous, layered defenses: improve LLM resistance to IPI, monitor and sweep external web content for known IPI patterns, and deploy application-level defenses when launching AI capabilities. (No discrete patch URL was provided.)
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The advisory describes the attack class 'indirect prompt injection' where untrusted page content (malicious sites, third-party iframes, user-generated content) can embed instructions that influence the planning LLM to take unwanted actions (e.g., financial transactions or data exfiltration). Chrome’s mitigations include a gating function/origin-sets to limit which origins the agent can read or act on, a separate User Alignment Critic model to vet actions, spotlighting to prefer user/system instructions, and a prompt-injection classifier and other runtime checks.
- **Affected Products:** Google Chrome (agentic / Gemini features) — specific versions not specified
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit is reported in this vendor advisory. (Separate, later Gemini-related CVEs were reported in 2026, but they are distinct incidents.)
- **Patch Available:** No single CVE patch is described in this advisory; Google states architectural mitigations have been implemented in Chrome and that fixes/updates will be delivered via Chrome’s auto-update mechanism (see vendor advisory).
- **Active Exploitation:** The vendor advisory does not report confirmed active exploitation tied to this architectural advisory. (Note: separate Gemini-related CVEs were reported and patched later in 2026; those are distinct incidents.)
- **Threat Actors:** None known
- **Mitigation:** Architectural and operational mitigations described by the vendor: User Alignment Critic (a separate vetting model), origin-isolation/origin-gating (read-only vs read-writable origin sets), user confirmations and a work log for agent actions, a prompt-injection classifier that runs in parallel to the planning model, continuous red‑teaming and monitoring, and Chrome auto-update to deliver fixes.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable — the post gives high-level memory-safety rationale and aggregate vulnerability trend data rather than vulnerability-specific technical or exploit details.
- **Affected Products:** Android platform (first‑party and third‑party/open-source code across languages including C and C++); specific product SKUs or version numbers not specified.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit is described or linked in the blog post.
- **Patch Available:** Patch information unavailable — the blog post is a high-level summary and does not list or link per-vulnerability patches or advisories.
- **Active Exploitation:** No confirmed active exploitation in the wild is reported in the blog post.
- **Threat Actors:** None known
- **Mitigation:** High-level mitigations described: adopt memory-safe languages (Rust) and focus on vulnerability-prevention and rapid fixes across the Android platform; no per-vulnerability workaround steps are provided.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) hides adversarial instructions inside external data (web pages, documents, metadata, emails) that agentic or web‑consuming AI treats as instructions rather than data; if an AI agent executes those instructions it can exfiltrate data or perform actions (examples include embedded payment flows, meta-tag namespace injections, and persuasion keywords).
- **Affected Products:** Gemini app; Gemini in Google Workspace (Gmail, Docs, Drive, Chat), Cursor (versions below 1.3 per NVD/CVE-2025-54131)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public payload examples and technical write-ups exist (Forcepoint published 10 observed IPI payloads; Google and third-party writeups describe payloads). No single packaged weaponized exploit was referenced in the collected sources.
- **Patch Available:** Partial: NVD lists CVE-2025-54131 (Cursor code editor) as fixed in Cursor version 1.3 (see NVD entry). Google describes layered / model-level mitigations for Gemini (see Google Security Blog and Workspace Help).
- **Active Exploitation:** Yes — multiple researcher teams (Google and Forcepoint/X‑Labs) reported finding indirect prompt injection (IPI) payloads on public websites and analyzed concrete payloads and behaviors (see Forcepoint and Help Net Security coverage).
- **Threat Actors:** None known
- **Mitigation:** Google’s layered mitigations for Gemini include model hardening (adversarial training), prompt-injection content classifiers, security thought reinforcement (contextual safety instructions), markdown sanitization and suspicious-URL redaction, a user confirmation (HITL) framework for risky actions, and end‑user security mitigation notifications.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors target large backbone routers and network-edge devices (provider edge and customer edge routers), compromise devices and trusted interconnections, and commonly modify router configurations to maintain persistent, long-term access and pivot into other networks.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) or weaponized exploit was reported in the cited sources; summaries state "no known exploits in the wild at this time."
- **Patch Available:** No official vendor patch or remediation guidance was available at publication; CISA provided mitigations instead (no vendor patch URL available).
- **Active Exploitation:** CISA reports active targeting and compromise of networks worldwide by PRC state-sponsored actors (confirmed activity); however, for the specific CVE/issue set cited, no public weaponized exploit/PoC was reported in the referenced summaries.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Follow CISA advisory detection and hardening guidance: create alerts/alarms for unusual router behavior and commands, monitor and validate router configuration integrity, restrict and harden management-plane access, remove unauthorized accounts or configuration changes, segment networks and restrict trusted interconnections, and apply vendor patches/updates when/if published.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) or weaponized exploit is reported in the cited advisory and supporting documents.
- **Patch Available:** No vendor patch identified (advisory describes a nation-state targeting campaign rather than a discrete software vulnerability). See official advisory URL.
- **Active Exploitation:** Yes — the advisory and corroborating sources report active targeting: Russian GRU operations targeting Western logistics entities and technology companies (reported since 2022).
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th GTsSS (Unit 26165) — tracked as APT28
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

**Parallel AI Enrichment:**

- **Technical Details:** A vulnerability in Ivanti Sentry OS that enables remote code execution / full control of the appliance when exploited, permitting configuration alteration, credential theft, data access, and lateral movement into enterprise networks.
- **Affected Products:** Ivanti Sentry appliance (Ivanti Sentry OS) — specific affected versions unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof-of-concept (PoC) was released (reported June 10, 2026) and is reported to be used in attacks (sources: Enigma Global, Horizon3, Purple-Ops).
- **Patch Available:** Patch/advisory information unavailable.
- **Active Exploitation:** Confirmed active exploitation in the wild — Enigma Global reports Shadowserver confirmed active exploitation as of June 10, 2026; Horizon3 and Purple-Ops corroborate PoC-driven attacks.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 10. 🟠 Zero-Day — Nissan discloses employee data breach linked to Oracle zero-day attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-29
**Reference:** <https://www.bleepingcomputer.com/news/security/nissan-discloses-employee-data-breach-linked-to-oracle-zero-day-attacks/>

> Nissan is warning that it suffered a data breach affecting current and former employees after threat actors exploited an Oracle PeopleSoft vulnerability in data theft attacks previously linked to the ShinyHunters extortion group. [...]

**Parallel AI Enrichment:**

- **Technical Details:** An unauthenticated authentication-bypass / remote-code-execution vulnerability in Oracle PeopleSoft PeopleTools (Updates Environment Management component) that allows an attacker with HTTP network access to achieve RCE; attackers have used it to deploy tooling (e.g., MeshCentral) and exfiltrate data, reportedly via a gadget-chain of known and zero-day issues.
- **Affected Products:** Oracle PeopleSoft PeopleTools (Updates Environment Management component)
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Active exploitation is confirmed in the wild; no public PoC or weaponized exploit URL was identified in the collected sources.
- **Patch Available:** Oracle published an out-of-band Security Alert for CVE-2026-35273 (see vendor advisory URL above) — follow the Oracle advisory for patches/mitigations.
- **Active Exploitation:** Yes — multiple vendors and news outlets report in-the-wild exploitation (attributed to ShinyHunters) to steal data and deploy remote tooling.
- **Threat Actors:** ShinyHunters
- **Mitigation:** Follow Oracle's out-of-band Security Alert (apply vendor updates/mitigations), isolate or restrict network access to PeopleSoft Update Environment Management interfaces, monitor for indicators (e.g., MeshCentral deployments), and perform incident response on affected systems.
- **Vendor Advisory:** https://www.oracle.com/security-alerts/alert-cve-2026-35273.html

---

## 11. 🟠 Zero-Day — NAIC says public data stolen in ShinyHunters' PeopleSoft breach

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-29
**Reference:** <https://www.bleepingcomputer.com/news/security/naic-says-public-data-stolen-in-shinyhunters-peoplesoft-breach/>

> The National Association of Insurance Commissioners (NAIC) says the ShinyHunters extortion group stole only publicly available data, outdated logs, and configuration files after breaching its systems by exploiting a zero-day vulnerability in an Oracle PeopleSoft server. [...]

---

## 12. 🟠 Zero-Day — Microsoft Removes 119 Edge Extensions That Hid Malware in Images and Fonts

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-29
**Reference:** <https://thehackernews.com/2026/06/microsoft-removes-119-edge-extensions.html>

> Microsoft has shut down a long-running malicious extension operation on the Edge Add-ons store that hid its payloads inside ordinary image and font files, then woke up days after install to steal credentials and run ad fraud.

The company calls it StegoAd, a mash-up of steganography and adware, and ties 119 extensions to a single threat actor it says has been active since at least 2021.

---

## 13. 🟡 High Severity — Critical SimpleHelp flaw exploited to deploy new stealer malware

**CVE:** `CVE-2026-48558` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-29
**Reference:** <https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-simplehelp-flaw-deploy-new-djinn-infostealer-taskweaver-malware/>

> Hackers are exploiting a recently disclosed critical vulnerability (CVE-2026-48558) in SimpleHelp to deploy Djinn Stealer, a previously undocumented cross-platform information stealer targeting Windows, macOS, and Linux. [...]

---

## 14. 🟡 High Severity — Hackers now exploit critical Oracle E-Business flaw in attacks

**CVE:** `CVE-2026-46817` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-29
**Reference:** <https://www.bleepingcomputer.com/news/security/new-oracle-e-business-suite-flaw-now-exploited-in-attacks/>

> Attackers have begun exploiting a critical vulnerability (CVE-2026-46817) in the Oracle E-Business Suite (EBS) financial application, according to threat intelligence company Defused. [...]

---

## 15. 🟡 High Severity — Public PoC Released for Critical libssh2 CVE-2026-55200 Client-Side SSH Flaw

**CVE:** `CVE-2026-55200` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-29
**Reference:** <https://thehackernews.com/2026/06/public-poc-released-for-critical.html>

> A public proof-of-concept is now out for CVE-2026-55200, a critical flaw in libssh2 that lets a malicious or compromised SSH server trigger memory corruption on a connecting client, with possible code execution. No credentials, no user interaction. The bug affects every release up to and including 1.11.1 and carries a CVSS 4.0 score of 9.2.

libssh2 is a client-side SSH library, not a server.

---

## 16. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
