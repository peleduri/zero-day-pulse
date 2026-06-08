# Zero Day Pulse

> **Generated:** 2026-06-08 02:32 UTC &nbsp;|&nbsp; **Total:** 9 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 8 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 9

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a directory traversal vulnerability in SimpleHelp RMM versions ≤5.5.7 that allows unauthenticated remote attackers to read sensitive files, logs, configuration data, and credentials via crafted path inputs.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (https://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570)
- **Active Exploitation:** true
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Upgrade SimpleHelp to version 5.5.8 or later.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an attack vector where adversarial content is seeded in web-accessible sources (e.g., web pages, web-hosted documents) that AI agents or retrieval-augmented systems may fetch; the adversarial content contains crafted instructions or payloads that influence the model’s behavior when the agent incorporates that external content into its prompt or context. IPI leverages the model’s tendency to follow instructions present in retrieved content, enabling stealthy manipulation without directly compromising the model.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — Forcepoint disclosed 10 in-the-wild IPI payloads (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads)
- **Patch Available:** false
- **Active Exploitation:** true — multiple vendors and researchers reported in-the-wild IPI payloads (Google Security Blog; Forcepoint X‑Lab report).
- **Threat Actors:** None known
- **Mitigation:** Monitor and vet external content sources; use allowlists/deny-lists for retrieval, sanitize or canonicalize retrieved text, apply prompt-wrapping or instruction isolation (keep system instructions separate and immutable), validate outputs against policies, and limit agent web-browsing/RAG to trusted domains. (Hardening and defensive monitoring recommended.)
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack technique that injects malicious instructions into data sources or tools used by a large language model (e.g., documents, web content, connectors, or tool outputs) so the model is steered to behave in unintended ways when completing a user’s query. It can occur without direct user input and is exacerbated by agentic automation and multi‑source data integration.
- **Affected Products:** Google Workspace with Gemini, Gemini app
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** false — vendor mitigation/advisory available: http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html
- **Active Exploitation:** true — detection of IPI payloads in the wild reported (see Forcepoint Apr 22, 2026).
- **Threat Actors:** None known
- **Mitigation:** Apply layered defenses: data provenance and sanitization, strict tool/output validation, query and context filtering, prompt hardening and model-level instruction controls, monitoring and anomaly detection, access controls and least privilege for connectors; follow vendor continuous‑mitigation guidance at the advisory URL above.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Google describes the primary threat as "indirect prompt injection," where malicious web content manipulates agentic AI assistants by influencing prompts or context; Chrome added layered defenses including prompt-injection blocking, restricted origin access, and a second AI overseer to validate actions.
- **Affected Products:** Chrome (agentic browsing / Gemini for Chrome)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true - http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known.
- **Mitigation:** Use latest Chrome with the agentic/Gemini updates; Google recommends layered defenses (prompt-injection protections, origin restrictions, limiting unsafe AI actions) and architecting security for agentic features per the advisory.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Linear buffer overflow (memory safety) discovered in CrabbyAVIF (platform/external/rust/crabbyavif) in unsafe Rust; rendered non-exploitable on Android due to Scudo hardened allocator guard pages; fixed pre-release and assigned CVE-2025-48530
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true - patch and tracking: https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050 and CVE tracking in Android bulletin: https://source.android.com/docs/security/bulletin/2025-08-01
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use Scudo hardened allocator (default on Pixel and many devices); ensure Scudo enabled on devices; follow unsafe Rust review/training and apply the patch; increase crash signalting for overflows
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injections (IPI) are hidden malicious instructions embedded in external data sources (emails, documents, calendar invites, images, URLs) that influence an LLM’s behavior during prompt completion, enabling data exfiltration or unauthorized actions. Google mitigates this via model hardening (adversarial training), prompt‑injection content classifiers, security thought reinforcement, markdown sanitization, suspicious‑URL redaction, user‑confirmation frameworks, and end‑user mitigation notifications.
- **Affected Products:** Google Gemini (Gemini 2.5), Google Workspace
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses — model hardening with adversarial training, prompt‑injection classifiers, security thought reinforcement, markdown sanitization and URL redaction (Safe Browsing), user‑confirmation frameworks for risky actions, end‑user notifications, deterministic policy‑engine controls (regex takedowns, URL sanitization), and continuous red‑teaming with synthetic adversarial data.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors focus on large backbone routers and PE/CE routers, leverage compromised devices and trusted connections to pivot into other networks, and often modify routers to maintain persistent, long‑term access; specific vulnerability mechanism not detailed in advisory
- **Affected Products:** Telecommunications backbone routers, provider edge (PE) routers, customer edge (CE) routers, and compromised network devices (specific vendors/models/versions not specified in advisory)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon; OPERATOR PANDA; RedMike; UNC5807; GhostEmperor (activity partially overlaps with reporting on these groups)
- **Mitigation:** Follow CISA guidance for simulation and mitigation — harden and monitor edge and backbone routing devices, apply vendor updates where available, restrict and monitor trusted connections, limit administrative access, use strong authentication and network segmentation, and monitor for indicators of compromise as described in the CISA advisory
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

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
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU), 85th Main Special Service Center (85th GTsSS), military unit 26165
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

**Parallel AI Enrichment:**

- **Technical Details:** A malicious DNS response can trigger out‑of‑bounds reads, writes, and other memory safety violations in the baseband DNS parser, leading to potential remote code execution.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Migrate the DNS parsing component to Rust, which eliminates memory‑safety vulnerabilities; apply the updated firmware that includes these Rust‑based mitigations.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html

---
