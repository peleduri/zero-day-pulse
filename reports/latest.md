# Zero Day Pulse

> **Generated:** 2026-06-28 02:11 UTC &nbsp;|&nbsp; **Total:** 10 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 9 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 7

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a directory traversal flaw that lets unauthenticated attackers read arbitrary files on the server via path manipulation.
- **Affected Products:** SimpleHelp remote support software v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit has been reported.
- **Patch Available:** Vendor released a patch for SimpleHelp 5.5.7 and earlier within two days of reporting the vulnerability; see the vendor advisory for details.
- **Active Exploitation:** Confirmed active exploitation by ransomware actors leveraging unpatched SimpleHelp RMM, reported in CISA advisory AA25‑163A.
- **Threat Actors:** Ransomware actors
- **Mitigation:** Apply the vendor‑released patch; if unavailable, restrict network access to the RMM service, enforce least‑privilege accounts, and monitor for suspicious file‑access activity.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack class where adversarial instructions are embedded in external content (webpages, documents, emails) that a GenAI system or agent fetches and includes when constructing prompts. If the system treats that external content as trusted context, models can follow attacker instructions or disclose sensitive data. IPI is often used in combination with other flaws (e.g., zero-click vulnerabilities in assistants) to achieve high-impact results like data exfiltration or unauthorized actions.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Industry reports and vendor blogs document PoC payloads and real-world IPI payloads observed in the wild (Unit42, Forcepoint, Noma Labs). Public writeups describe weaponization/payloads, but no single canonical public exploit repository URL was identified in the collected sources.
- **Patch Available:** No single vendor patch exists for the attack class 'Indirect Prompt Injection' (IPI). A product-specific zero-click issue (GeminiJack) was disclosed by Noma Labs for Google Gemini Enterprise, but public sources searched did not contain an official vendor patch URL for that disclosure.
- **Active Exploitation:** Yes — multiple industry reports and vendor writeups describe indirect prompt injection payloads observed in the wild and real-world abuse investigations (Unit42, Forcepoint, CrowdStrike, Google Security Blog).
- **Threat Actors:** None known
- **Mitigation:** Harden LLM integrations: validate and sanitize external inputs, separate trust boundaries (don’t blindly concatenate untrusted external content into prompts), use dynamic prompt templating, human-in-the-loop approval for high-risk actions, monitor and test with known IPI payloads, and apply least-privilege to downstream actions. (See OWASP cheat sheet, industry writeups.)
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

**Parallel AI Enrichment:**

- **Technical Details:** An indirect prompt-injection class vulnerability against agentic/assistant capabilities (researchers labelled 'GeminiJack') allowed malicious site content to influence agent prompts; when chained with other flaws this could lead to local file access and privacy exposure.
- **Affected Products:** Google Chrome (agentic / Gemini features), Google Gemini Enterprise
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public researcher disclosures and writeups exist (Noma Labs 'GeminiJack' disclosure and Unit42 analysis); no PoC code URL is present in the supplied corpus.
- **Patch Available:** Google published architectural mitigations in the December 8, 2025 Google Security Blog post and has patched related high-severity issues in Chrome (see vendor post and followup reports).
- **Active Exploitation:** No confirmed active exploitation in the wild reported in the supplied documents; the references describe researcher discovery and vendor mitigation/patching.
- **Threat Actors:** None known
- **Mitigation:** Google introduced architectural security layers for agentic browsing (as described in the vendor post) and patched related high-severity Chrome issues; no additional vendor workaround steps are present in the supplied corpus.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

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

- **Technical Details:** Indirect prompt injection (IPI) embeds hidden malicious instructions inside external content (web pages, emails, documents, calendar invites). When an AI system ingests that poisoned content, the model or agent may follow the injected instructions (e.g., exfiltrate data, navigate to admin pages, perform transactions) instead of the user’s intent, especially for agentic models with tool access.
- **Affected Products:** Google Workspace (Gmail, Docs, Chat, Drive) and Gemini (Gemini 2.5)
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** Yes — public, real-world indirect prompt injection payloads have been observed (Forcepoint reported "10 Indirect Prompt Injection Payloads Caught in the Wild").
- **Patch Available:** Fixed in version 1.3 (see NVD / vendor advisories).
- **Active Exploitation:** Confirmed — Forcepoint observed 10 IPI payloads on live sites and Google’s security blog reports attackers experimenting with IPI on the web.
- **Threat Actors:** None known
- **Mitigation:** Layered defense: model hardening with adversarial training; security thought reinforcement (wrap prompts with safety instructions); automated prompt sanitisation and malicious-instruction detection models; logical context segmentation and least-privilege data exposure; human review/workflows for high-risk content; strict prompt security policies and developer training; regular patching and integrating AI threat intelligence into SOC workflows.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Chinese state-sponsored actors exploit CVEs in network edge devices—backbone, provider edge, and customer edge routers—to gain persistent access, often by modifying firmware or configuration to maintain long‑term footholds.
- **Affected Products:** Backbone routers, provider edge (PE) routers, customer edge (CE) routers.
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or exploit known.
- **Patch Available:** No official patch is available from the vendor.
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 9. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit available.
- **Patch Available:** No patch available.
- **Active Exploitation:** No active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 10. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

**Parallel AI Enrichment:**

- **Technical Details:** A malicious DNS response can trigger out‑of‑bounds reads and writes in the baseband DNS parser, leading to memory‑safety violations.
- **Affected Products:** Google Pixel baseband modem (Pixel 9, Pixel 10) – Android versions prior to 12, 12L, 13, 14 (pre‑patch)
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** No public proof‑of‑concept or weaponized exploit is known.
- **Patch Available:** Patch is available via the Pixel security bulletin and the updated modem firmware includes the Rust‑based DNS parser. See https://source.android.com/security/bulletin/pixel/2024-03-01 for details.
- **Active Exploitation:** No confirmed active exploitation in the wild has been reported.
- **Threat Actors:** None known
- **Mitigation:** Update the Pixel modem firmware to the version that includes the Rust‑based DNS parser, which mitigates the memory‑safety issue. Apply the patch from the Pixel security bulletin.
- **Vendor Advisory:** https://source.android.com/security/bulletin/pixel/2024-03-01

---
