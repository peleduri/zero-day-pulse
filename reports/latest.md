# Zero Day Pulse

> **Generated:** 2026-07-12 01:27 UTC &nbsp;|&nbsp; **Total:** 13 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Multiple unauthenticated path-traversal vulnerabilities in SimpleHelp v5.5.7 and earlier allow attackers to craft HTTP requests to download arbitrary files from the host (including server configuration files containing secrets and hashed user passwords).
- **Affected Products:** SimpleHelp remote support / RMM software v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true - see https://simple-help.com/kb---security-vulnerabilities-01-2025
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Upgrade immediately to the latest SimpleHelp version per the vendor advisory; if upgrade is not immediately possible, isolate the SimpleHelp server from the Internet or stop the server process; apply vendor mitigations or discontinue use per CISA guidance.
- **Vendor Advisory:** https://simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — 'Ghostcommit' hides prompt injection in images to fool AI agents, steal secrets

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-07-11
**Reference:** <https://www.bleepingcomputer.com/news/security/ghostcommit-hides-prompt-injection-in-images-to-fool-ai-agents-steal-secrets/>

> A PNG hiding a prompt injection could steal your repo&#x27;s secrets, researchers demonstrate. The technique, dubbed &#x27;Ghostcommit,&#x27; slipped past AI code reviewers CodeRabbit and Bugbot, which never open image files at all, then convinced a coding agent to read a repo&#x27;s .env and write every secret into the code as a list of numbers. [...]

**Parallel AI Enrichment:**

- **Technical Details:** A researcher-disclosed proof-of-concept ("Ghostcommit") hides prompt-injection text inside a PNG image committed to a repository. Automated AI code-reviewing/commit agents that process repository contents can be tricked by the hidden prompt to access repository secrets (e.g., a .env file) and output those secrets into code, because the hidden prompt coerces the agent's behaviour. The attack is a supply-chain/commit-level prompt-injection demonstrated by researchers rather than a vendor-patched CVE at time of reporting.
- **Affected Products:** CodeRabbit, Bugbot; specific versions unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (PoC reported — https://www.bleepingcomputer.com/news/security/ghostcommit-hides-prompt-injection-in-images-to-fool-ai-agents-steal-secrets/)
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Mitigations (if no vendor patch is available): restrict AI/code-review agent file access and deny access to secrets (e.g., .env); configure agents not to auto-open or process arbitrary image/binary files; require human review for changes affecting secrets or CI/CD automation; run agents with least privilege and avoid granting repository write or secret-read rights to automation; scan repositories for unexpected binary/steganographic content; rotate/compartmentalize secrets and monitor for unusual commits/edits.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) — attackers embed covert or explicit instructions inside web pages or other external content that an AI agent will ingest when browsing or processing that content; if the agent follows those instructions it can exfiltrate data, perform unauthorized actions, or bypass intended authorization controls.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — PoC/demo: https://github.com/brennanbrown/atlas-prompt-injection-poc ; weaponizable payloads documented by Forcepoint X‑Labs: https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses: restrict/limit browsing scope for AI agents, sanitize or ignore untrusted external content, enforce provenance and policy checks, apply least-privilege for data access, and require human review for sensitive actions (see vendor guidance for Workspace/Gemini and OWASP LLM guidance).
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack where adversaries hide malicious instructions inside external data sources (emails, web pages, documents, files, etc.) that an LLM ingests; those hidden instructions become part of the model’s effective prompt and can cause the model to perform unintended actions or disclose sensitive information (examples: chatbot hijack, compromised summarizer, data exfiltration).
- **Affected Products:** Gemini, Gemini in Workspace (Gmail, Docs editors, Drive, Chat)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Google describes a layered defense: model hardening/adversarial robustness, prompt-injection content classifiers, security thought reinforcement, markdown sanitization, suspicious-URL redaction, a user confirmation (human-in-the-loop) framework for sensitive actions, end-user mitigation notifications, plus monitoring and rapid response.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The issue is an indirect prompt-injection class vulnerability in agentic browsing: hidden or crafted web content can influence the LLM/agent prompt or inject content/scripts into privileged contexts. Research disclosures (GeminiJack) describe a zero-click indirect prompt injection against Gemini integration in Chrome/Gemini Enterprise that enabled script injection into privileged pages and could expose local files/privacy to the agentic context.
- **Affected Products:** Google Chrome (agentic browsing / Gemini integration), Google Gemini Enterprise
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true - public PoC(s) reported (e.g., GitHub PoC for CVE-2026-0628: http://github.com/fevar54/CVE-2026-0628-POC) and public researcher disclosure (Noma Labs GeminiJack).
- **Patch Available:** true - Google published vendor mitigations/advisory describing layered defenses and Chrome mitigations (see: http://security.googleblog.com/2025/12/architecting-security-for-agentic.html).
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use Chrome's layered defenses described by Google: block and ignore untrusted/hidden page content that could perform indirect prompt injection, restrict origin access for agentic contexts, isolate agentic/LLM execution from privileged pages, and apply the latest Chrome updates and configuration changes described in the vendor advisory: http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Incorrect bounds checks in an AVIF parser/decoder (CrabbyAVIF) can produce out-of-bounds accesses / a linear buffer overflow when handling image planes, which in some contexts could enable remote code execution (RCE) when combined with other bugs.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection embeds malicious instructions inside external content (emails, documents, web pages, search results, calendar invites, etc.) that are then ingested by generative models or agentic systems; when followed by the model these instructions can cause data exfiltration, execution of unwanted actions, or corrupted outputs. Defenses focus on sanitizing inputs, classifying suspicious content, enforcing trust boundaries, and human review.
- **Affected Products:** Gemini, Gmail (Gemini in Workspace), Google Docs (Gemini in Workspace), Google Drive (Gemini in Workspace), Google Chat (Gemini in Workspace)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (representative public PoC/demos: https://www.tenable.com/security/research/tra-2025-23, https://0din.ai/blog/phishing-for-gemini, https://blog.google/security/prompt-injections-web/)
- **Patch Available:** false
- **Active Exploitation:** true (see: https://blog.google/security/prompt-injections-web/, https://www.helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild/)
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: prompt-injection content classifiers, security-thought reinforcement, markdown sanitization and suspicious-content handling, provenance/source attribution and trust boundaries, input sanitization, human-in-the-loop review, and runtime policy/enforcement (as described by Google and OWASP guidance).
- **Vendor Advisory:** https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** State-sponsored actors target large backbone, provider-edge (PE) and customer-edge (CE) routers and other network-edge devices, compromise devices and trusted connections, modify router configurations (examples include ACLs named "access-list 20"), and abuse management features (e.g., GuestShell) to establish persistent, long-term access for lateral movement and data exfiltration.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 4.3
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Upgrade unsupported devices to vendor-supported models; harden and restrict management interfaces; restrict, monitor, and review trusted interconnections; apply strict hardening to features such as GuestShell (or disable if unnecessary); verify ACLs/configuration changes and inventory of network-edge devices; monitor for persistence indicators and unusual egress/exfiltration activity.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** GRU unit 26165 weaponized a Microsoft Outlook NTLM vulnerability (CVE-2023-23397) to collect NTLM hashes as part of credential-harvesting/initial-access activity; the campaign used additional infrastructure and scripts consistent with broader GRU TTPs.
- **Affected Products:** Microsoft Outlook (CVE-2023-23397)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — weaponized exploit used by GRU unit 26165 in the campaign (no public PoC URL present in provided corpus)
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU), unit 26165 (85th Main Special Service Center / 85th GTsSS)
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

**Parallel AI Enrichment:**

- **Technical Details:** OS command-injection flaw in Ivanti Sentry that allows a remote unauthenticated attacker to execute arbitrary operating-system commands (root-level), enabling full appliance compromise, configuration changes, credential theft, data access and potential lateral movement into enterprise networks.
- **Affected Products:** Ivanti Sentry (Sentry gateway / appliance) — specific version ranges per vendor advisory
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — public proof-of-concept released (e.g., Horizon3 advisory: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-10520) and PoC/weaponized code observed in attacks.
- **Patch Available:** true — vendor advisory/patch published (see Ivanti advisory URL above).
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor patch immediately to internet-exposed Sentry appliances; if patching cannot be immediate, isolate/remove affected appliances from public networks, restrict management interfaces, network-segment Sentry devices, and monitor for indicators of compromise and unexpected administrative changes.
- **Vendor Advisory:** https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523

---

## 11. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 12. 🟠 Zero-Day — CrowdStrike Uncovers New Prompt Injection Techniques

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jul 07, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-uncovers-new-prompt-injection-techniques/>

---

## 13. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
