# Zero Day Pulse

> **Generated:** 2026-06-21 02:31 UTC &nbsp;|&nbsp; **Total:** 11 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 9 &nbsp;|&nbsp; 🟡 High: 2 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a directory traversal flaw that lets unauthenticated attackers read arbitrary files on the system via crafted file‑path inputs.
- **Affected Products:** SimpleHelp remote support software version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit or PoC is known.
- **Patch Available:** Patch available; vendor released patches for SimpleHelp versions 5.5.7 and earlier (see vendor advisory).
- **Active Exploitation:** Confirmed active exploitation reported by ransomware actors in the wild.
- **Threat Actors:** Ransomware actors (unspecified)
- **Mitigation:** Apply the vendor patch for SimpleHelp versions 5.5.7 and earlier; if patching cannot be performed immediately, limit remote RMM access and enforce strict file‑path validation.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) seeds malicious instructions in web content or hidden site code which AI agents that browse or ingest web content may incorporate into their prompts, causing unintended behavior or data exfiltration. Researchers disclosed 10 in‑the‑wild payloads and examples of hidden‑site and comment‑based injection patterns.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoCs/weaponized exploits reported in‑the‑wild indirect prompt injection payloads (Forcepoint disclosure). Source: http://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads
- **Patch Available:** Vendor mitigation guidance published by Google; no single product patch listed. Source: http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html
- **Active Exploitation:** Yes — researchers and vendor telemetry observed in‑the‑wild indirect prompt injection attempts (Forcepoint, Google). Sources: Forcepoint blog and Google security blog.
- **Threat Actors:** None known
- **Mitigation:** Input/output validation and sanitization, restricting web‑browsing for agents, implementing human review and controls in RAG pipelines, pattern detection and filtering of known IPI payloads — per Google and industry guidance.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) enables attackers to inject malicious instructions into data or tools consumed by LLMs (including zero‑click scenarios). The attack surface rises with agentic automation and multiple data sources; Google’s mechanisms detect, catalog, synthesize variants, and apply deterministic and model‑based defenses.
- **Affected Products:** Google Workspace with Gemini
- **CVSS Score:** -9999.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit referenced in the advisory.
- **Patch Available:** No single "patch" – Google describes continuous, layered mitigations rather than a discrete vendor patch. Advisory: http://security.googleblog.com/2026/04/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/
- **Active Exploitation:** Advisory mentions monitoring public disclosures and proactive hunting but does not report confirmed active exploitation of Workspace/Gemini in this post.
- **Threat Actors:** None known
- **Mitigation:** Defense‑in‑depth: user confirmation, URL sanitization, tool‑chaining policies, centralized policy engine for config updates (regex takedowns/point fixes), synthetic‑data‑driven ML retraining, LLM prompt engineering, human and automated red‑teaming, AI VRP participation.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is a technique where malicious web content manipulates the AI model's prompt chain, leading to unauthorized actions or data leakage without user interaction.
- **Affected Products:** Google Chrome (agentic browsing) < version 1.3
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Proof‑of‑concept for GeminiJack published by Noma Labs; see their blog post.
- **Patch Available:** Patch released for Chrome Gemini (CVE‑2026‑0628); see Unit42 report for details.
- **Active Exploitation:** Confirmed active exploitation of indirect prompt injection payloads reported by Forcepoint X‑Labs.
- **Threat Actors:** None known
- **Mitigation:** Apply the layered defenses described by Google: enable deterministic rule checks, activate model‑level protections, and keep Chrome updated to benefit from runtime monitoring.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Android's safe-coding strategy focuses on shifting new code to memory-safe languages (Rust, alongside existing Java/Kotlin). Approximately 5 million lines of Rust have been shipped, with a memory-safety vulnerability density of ~0.2 per million lines versus ~1,000 per million lines for legacy C/C++. Memory-safety vulnerabilities fell from 76% of total Android vulnerabilities in 2019 to 24% in 2024 and below 20% in 2025. Safety mechanisms include encapsulation with clear safety invariants, scrutiny of unsafe{} blocks (which still enforce most of Rust's safety checks), and the Scudo hardened allocator with guard pages as defense-in-depth. The worked example CVE-2025-48530 is an out-of-bounds access (CWE-125) caused by an incorrect bounds check in multiple locations in the Android 16 System component, leading to potential remote code execution with no user interaction required.
- **Affected Products:** Android (Android 13, 14, 15, 16 — Framework, System, and various components; the worked example CVE-2025-48530 affects the Android 16 System component)
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** No public PoC or weaponized exploit available. The example vulnerability (CVE-2025-48530) 'never made it into a public release' before being caught, per the Google Security Blog post.
- **Patch Available:** Yes — Patches are available via the Android Security Bulletin—August 2025 (https://source.android.com/docs/security/bulletin/2025-08-01), which includes the fix for the example CVE-2025-48530. The specific memory-safety fix was applied before any public Android release shipped the vulnerable code.
- **Active Exploitation:** No confirmed active exploitation for CVE-2025-48530 (the example discussed in the blog post). The vulnerability was caught and fixed before reaching a public Android release, precluding in-the-wild exploitation. Note: an unrelated Qualcomm Adreno GPU vulnerability in the same August 2025 bulletin was reported as under active exploitation, but that is separate from the memory-safety/Rust strategy topic.
- **Threat Actors:** None known
- **Mitigation:** 1. Adopt memory-safe languages (Rust) for new native Android code; 2. Use encapsulation with clear safety invariants around unsafe code; 3. Rigorously scrutinize unsafe{} blocks (which still enforce most of Rust's safety checks); 4. Deploy the Scudo hardened allocator with guard pages as defense-in-depth for remaining C/C++; 5. Apply the August 2025 Android Security Bulletin patch level (2025-08-01 / 2025-08-05); 6. Complete Google's 'Comprehensive Rust' training for engineers reviewing unsafe code.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is a class of attack on LLM-driven AI assistants in which the attacker does not interact with the model directly but instead embeds hidden malicious instructions inside an external data source that the victim's AI agent will later ingest (e.g., emails, calendar invites/attachments, web pages, documents, logs). When the AI retrieves that content — for example, when a user asks Gemini to summarize their inbox — the model parses the malicious instructions alongside the legitimate content and treats them as if they were trusted system/user instructions. The agent can then exfiltrate data (emailing a private summary to an attacker-controlled address, leaking secrets via image-rendering of a Markdown URL), execute rogue tool calls (create calendar events, run shell commands, delete files, route payments via Stripe/PayPal), or alter its conversational behavior. Because the sensitive content originates from tool-grounded retrieval rather than the user's prompt, prior guardrails anchored on direct prompting are bypassed.
- **Affected Products:** Google Gemini 2.0 (incl. Gemini 2.0 Flash), Gemini 2.5 models, Gemini in Google Workspace, Gemini app, Gemini Cloud Assist, Gemini Search Personalization, and Gemini Enterprise Agent Platform / LangChain / Google MCP server integrations (protected by Model Armor).
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — multiple public PoCs and weaponized payloads exist: Miggo 'Weaponizing Calendar Invites' semantic attack on Google Gemini; EchoLeak (CVE-2025-32711) in Microsoft 365 Copilot; Tenable TRA-2025-10 (Gemini Cloud Assist) and TRA-2025-23 (Gemini Search Personalization); Pillar Security 'Anatomy of an Indirect Prompt Injection'; Forcepoint X-Labs' 10 verified in-the-wild IPI payloads on live websites; and OddGuan's credential-theft PoC against Claude Code, Gemini CLI, and GitHub Copilot Agents. OWASP maintains the LLM01:2025 Prompt Injection taxonomy.
- **Patch Available:** Not applicable as a single patch — Google is deploying the layered defenses proactively across Gemini 2.5 models, Gemini in Workspace, and the Gemini app. For adjacent specific issues, Google Cloud has published fixes: Gemini Cloud Assist (Tenable TRA-2025-10) and Gemini Search Personalization (Tenable TRA-2025-23). Microsoft patched CVE-2025-32711 (EchoLeak). Google added layered prompt-injection defenses to Chrome in December 2025.
- **Active Exploitation:** Yes — confirmed active exploitation in the wild. Forcepoint X-Labs identified 10 verified indirect prompt injection payloads on live websites (financial fraud, data destruction, search manipulation, credential-style exfiltration), and a Cloud Security Alliance research note concludes IPI 'has crossed the line from proof-of-concept to live exploitation.' Real-world Google Gemini exploits include the Miggo calendar-invite attack (responsible disclosure), Tenable TRA-2025-10 (Gemini Cloud Assist), and Tenable TRA-2025-23 (Gemini Search Personalization). Microsoft's EchoLeak (CVE-2025-32711, June 2025) was the first zero-click consumer-facing example.
- **Threat Actors:** None known by specific APT/ransomware name. Per Forcepoint X-Labs and Google researchers, in-the-wild operators appear to be using shared/organized tooling and templates, but no specific threat actor group, APT campaign, or ransomware operator has been publicly attributed to indirect prompt injection attacks.
- **Mitigation:** Google's layered defense strategy for Gemini products and analogous GenAI systems — six layers: (1) Prompt-injection content classifiers: proprietary ML models scan retrieved content (emails, files, web pages) to detect and block malicious instructions before they reach the model. (2) Security thought reinforcement: targeted system-level security instructions (and the 'instruction hierarchy' approach from the DeepMind paper) that steer the LLM to ignore adversarial content and treat retrieved data as untrusted. (3) Markdown sanitization and suspicious URL redaction: strip image-rendering/renderable-URL exfiltration paths and consult Google Safe Browsing to block suspicious links before the model returns them. (4) User confirmation framework (Human-in-the-Loop): require explicit user consent for high-risk tool calls (e.g., deleting a calendar event, sending an email, executing a shell command). (5) End-user security mitigation notifications: surface a contextual 'we blocked a suspected injection' notice in the UI plus a help-center link when an attack is mitigated. (6) Model hardening via adversarial data training: ongoing adversarial training (incl. Latent Adversarial Training / RL post-training) so the model robustly refuses poison-pill instructions in retrieved content. For Google Cloud enterprise customers: enable Model Armor (https://cloud.google.com/security/products/model-armor), which provides runtime protection against prompt injection, jailbreaking, malware, sensitive-data leakage, and harmful content for Gemini Enterprise Agent Platform, LangChain integrations, and external LLMs (OpenAI, Anthropic, Llama) via REST API. Google's AI Vulnerability Reward Program rules discourage accepting injection-vulnerable agent designs.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors target telecommunications backbone routers (provider edge and customer edge), modify router configurations/firmware to maintain persistent long‑term access, and pivot via trusted connections into other networks.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown / not listed.
- **Patch Available:** Patch information not specific to a single vendor; mitigation guidance provided in advisory. Patch URL: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a
- **Active Exploitation:** Yes — advisory reports state‑sponsored actors actively targeting networks worldwide.
- **Threat Actors:** Salt Typhoon; OPERATOR PANDA; RedMike; UNC5807; GhostEmperor
- **Mitigation:** Apply CISA advisory mitigation and hardening guidance: monitor and audit routers and network infrastructure, isolate management interfaces, rotate credentials, apply vendor firmware updates where available, segment networks, and remove persistent unauthorized modifications.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept or weaponised exploit is known.
- **Patch Available:** Patch unavailable.
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS)
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-44803 and CVE-2026-44812 are remote code execution flaws in the Windows Graphics Component that allow attackers to execute arbitrary code. CVE-2026-41091 is an elevation‑of‑privilege issue in Microsoft Defender caused by improper link resolution before file access.
- **Affected Products:** Windows Graphics Component (Windows 10, Windows 11); Microsoft Defender; Microsoft Exchange OWA
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit is known.
- **Patch Available:** Patches are available for most vulnerabilities as part of Microsoft’s June 2026 Patch Tuesday; however, certain vulnerabilities (e.g., CVE-2026-44803 and CVE-2026-44812) currently have no patches.
- **Active Exploitation:** Active exploitation has been confirmed for CVE-2026-41091 and CVE-2026-45498 (Microsoft Defender) and for other vulnerabilities added to the CISA KEV catalog.
- **Threat Actors:** None known
- **Mitigation:** Implement mitigation strategies such as applying available mitigations, using Falcon Exposure Management dashboards, and developing response plans for unpatched vulnerabilities.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 10. 🟡 High Severity — Hackers Exploit Gravity SMTP WordPress Plugin Bug to Expose API Keys

**CVE:** `CVE-2026-4020` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-20
**Reference:** <https://thehackernews.com/2026/06/hackers-exploit-gravity-smtp-wordpress.html>

> Threat actors are exploiting a recently patched security flaw impacting Gravity SMTP, a WordPress plugin that&#x27;s installed on about 100,000 sites.

The vulnerability, tracked as CVE-2026-4020 (CVSS score: 5.3), is a medium-severity information disclosure flaw that can allow unauthenticated attackers to extract sensitive data, such as configuration data, API keys, secrets, and OAuth tokens

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated attackers can query the Gravity SMTP plugin and obtain stored configuration files that contain API keys, secrets, and OAuth tokens, resulting in a sensitive information disclosure.
- **Affected Products:** Gravity SMTP WordPress plugin (versions < 2.1.5)
- **CVSS Score:** 5.3
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit URL is provided in the sources.
- **Patch Available:** Patch released on March 17th 2026 (version 2.1.5).
- **Active Exploitation:** Yes, active exploitation has been reported; over 17 million exploit attempts have been blocked as documented by Wordfence and other security analyses.
- **Threat Actors:** None known
- **Mitigation:** Upgrade Gravity SMTP to version 2.1.5 or later and monitor for abnormal request patterns that attempt to retrieve configuration data.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
