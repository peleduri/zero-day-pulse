# Zero Day Pulse

> **Generated:** 2026-06-07 13:17 UTC &nbsp;|&nbsp; **Total:** 11 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 9 &nbsp;|&nbsp; 🟡 High: 2 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path (directory) traversal vulnerability allowing an unauthenticated or unauthorized actor to craft malicious download URLs/requests to read arbitrary files from the SimpleHelp server filesystem
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Public proof‑of‑concept is available; see https://offsec.com/blog/cve-2024-57727
- **Patch Available:** SimpleHelp 5.5.8 released – https://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570
- **Active Exploitation:** Confirmed – CISA advisory reports ransomware actors exploiting unpatched SimpleHelp instances (AA25-163A).
- **Threat Actors:** Ransomware actors (unspecified groups)
- **Mitigation:** Upgrade to SimpleHelp 5.5.8 or later; if patching is not possible, restrict network exposure by blocking access to management interfaces from untrusted networks, enforce firewall/IP allowlists, isolate public‑facing instances, monitor logs for suspicious file‑download requests, and rotate credentials.
- **Vendor Advisory:** https://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — New ChatGPT Lockdown Mode Limits Tools That Could Enable Data Exfiltration

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-06
**Reference:** <https://thehackernews.com/2026/06/new-chatgpt-lockdown-mode-limits-tools.html>

> OpenAI has begun rolling out a new Lockdown Mode to ChatGPT for eligible personal accounts to reduce the risk of data exfiltration arising from prompt injection attacks.

The feature is primarily designed for people and organizations that handle sensitive data and require stricter protection guarantees. Lockdown Mode is available to logged-in users across Free, Go, Plus, and Pro, and

**Parallel AI Enrichment:**

- **Technical Details:** Lockdown Mode deterministically disables or limits network‑capable features that could enable data exfiltration via prompt injection (live web browsing limited to cached content, image support disabled, Deep Research disabled, Agent Mode disabled, Canvas networking blocked, file downloads blocked). It relies on sandboxing, URL‑exfiltration protections, monitoring/enforcement, and enterprise controls such as RBAC and audit logs.
- **Affected Products:** ChatGPT (Free, Go, Plus, Pro, self-serve ChatGPT Business) and ChatGPT Enterprise/managed workspaces
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public proof‑of‑concept or exploit is known.
- **Patch Available:** Lockdown Mode is a configurable feature; no patch is required.
- **Active Exploitation:** No confirmed active exploitation has been reported.
- **Threat Actors:** None known
- **Mitigation:** Enable Lockdown Mode via Settings > Security (Advanced security) for eligible personal accounts; for managed workspaces, enable via workspace admin role‑based controls and restrict apps/actions to a trusted minimal set. Use compliance API logs for visibility. Note that Lockdown Mode reduces but does not eliminate risk.
- **Vendor Advisory:** http://help.openai.com/articles/20001061

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when adversarial instructions are embedded in external web content or documents that AI agents retrieve during browsing or RAG, causing the agent to follow attacker‑controlled prompts instead of user intent. Attack vector: poisoned web content or data sources that are incorporated into model context without sufficient filtering or provenance checks.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Proof‑of‑concept IPI payloads disclosed by Forcepoint (10 in‑the‑wild payloads) – see Forcepoint report.
- **Patch Available:** No official vendor patch available; see vendor advisory.
- **Active Exploitation:** Confirmed in‑the‑wild indirect prompt injection payloads reported by Forcepoint and highlighted by Google as an active concern.
- **Threat Actors:** None known
- **Mitigation:** Guidance published by Google recommends monitoring external content fetched by AI agents, applying input validation/whitelisting, context filtering, provenance tagging, and using least‑privilege RAG designs.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) injects malicious instructions into data or tools used by an LLM (e.g., calendar invites, documents, web content) so the model follows attacker instructions while fulfilling a user’s request.
- **Affected Products:** Google Workspace with Gemini (Gmail, Docs, Calendar and other Workspace apps)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit provided in the advisory.
- **Patch Available:** No vendor patch indicated; Google describes continuous defenses and updates rather than a single patch (see vendor advisory).
- **Active Exploitation:** The advisory does not report confirmed active exploitation.
- **Threat Actors:** None known
- **Mitigation:** Deterministic defenses (user confirmation, URL sanitization, tool‑chaining policies, centralized Policy Engine, regex takedowns) and ML‑based defenses (retraining with synthetic data), LLM‑based defenses (prompt engineering), and Gemini model hardening.
- **Vendor Advisory:** http://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection – attacker‑controlled web pages, iframes, or user‑generated documents are retrieved into an agent or RAG context and contain instructions that the model treats as authoritative, leading to goal hijacking or data exfiltration. In Cursor, a command‑injection bypass of the allow‑list in auto‑run mode allows arbitrary command execution when backticks or $(cmd) are used.
- **Affected Products:** Chrome agentic browsing (preview), Google Gemini Enterprise RAG integrations, Cursor <1.3 (CVE‑2025‑54131)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public write‑ups/demos of GeminiJack are available (see Noma Labs); no weaponised exploit URL is published.
- **Patch Available:** Mitigations are delivered via architectural changes in Chrome/Google Gemini (see blog) and a software patch for Cursor v1.3 (see NVD).
- **Active Exploitation:** Noma Labs reported a real‑world zero‑click RAG exfiltration (GeminiJack); coverage in Computerworld and SecurityWeek documents the concern, though no large‑scale campaign attribution is published.
- **Threat Actors:** None known
- **Mitigation:** Implement Google’s layered defenses: User Alignment Critic, origin‑set gating, deterministic URL checks, a parallel prompt‑injection classifier, Safe Browsing integration, and updated VRP rules. For Cursor, upgrade to v1.3. Additionally, restrict agent privileges, limit accessible origins/datasources, vet retrieved content before inclusion, and require user confirmation for sensitive actions.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Critical remote code execution (RCE) vulnerability in the System component that can be exploited without additional privileges and without user interaction.
- **Affected Products:** Android AOSP versions 13, 14, 15, 16
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit information unavailable.
- **Patch Available:** Patches are included in the Android 2025‑11‑01 security patch level; source code changes are available at https://android.googlesource.com/platform/packages/modules/Bluetooth/+/c69c78d7c4f623201f35831d32e6c401156e76cc
- **Active Exploitation:** Information on active exploitation unavailable.
- **Threat Actors:** None known
- **Mitigation:** Update devices to the latest Android version and enable Google Play Protect.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-11-01

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injections occur when hidden malicious instructions are embedded in external data sources (emails, documents, calendar invites) and parsed by LLMs; mitigations include classifier filtering, sanitization, reinforcement of model instructions, URL redaction, and HITL confirmations.
- **Affected Products:** Gemini app, Gmail, Docs, Slides (Google Workspace)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC or weaponized exploit referenced in the advisory — "vendors/PoC unavailable".
- **Patch Available:** No vendor patch concept; mitigations and model hardening (Gemini 2.5) rolled out.
- **Active Exploitation:** Advisory does not report confirmed active exploitation in the wild.
- **Threat Actors:** None known
- **Mitigation:** Multiple layered mitigations: model hardening (Gemini 2.5), prompt‑injection content classifiers, security thought reinforcement, markdown sanitization and suspicious URL redaction, user confirmation framework, end‑user security notifications; Help Center guidance linked.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors compromise backbone, provider edge, and customer edge routers, then modify the devices to establish persistent footholds and use trusted connections to pivot deeper into victim networks.
- **Affected Products:** Backbone routers, Provider Edge (PE) routers, Customer Edge (CE) routers
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit or PoC is known from the provided sources.
- **Patch Available:** No official vendor patch is mentioned in the advisory.
- **Active Exploitation:** No confirmed active exploitation reported in the advisory.
- **Threat Actors:** People's Republic of China (PRC) state‑sponsored actors, Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Actors used Outlook NTLM vulnerability (CVE-2023-23397) via crafted calendar invites to collect NTLM hashes; Roundcube CVEs (CVE-2020-12641, CVE-2020-35730, CVE-2021-44026) to execute shell commands and access mail; WinRAR CVE-2023-38831 to execute code from archives; lateral movement with Impacket, PsExec, RDP, Certipy, ADExplorer; exfiltration via OpenSSH binary.
- **Affected Products:** Roundcube Webmail (versions before 1.2.13, 1.3.x before 1.3.16, 1.4.x before 1.4.10), WinRAR (CVE-2023-38831), Microsoft Outlook (CVE-2023-23397)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** CISA documents weaponization of CVE-2023-23397, CVE-2023-38831, and Roundcube CVEs; public detection scripts (e.g., Microsoft aka.ms/CVE-2023-23397ScriptDoc) and various PoCs exist but no single public PoC repository is linked.
- **Patch Available:** Patches are vendor-specific for referenced CVEs; see vendor advisories for CVE-2023-23397 (Microsoft Outlook) and CVE-2023-38831 (WinRAR). No single vendor patch covers the advisory.
- **Active Exploitation:** CISA reports confirmed active exploitation in the wild by GRU unit 26165 using CVE-2023-23397, Roundcube CVEs, and CVE-2023-38831; the advisory includes IOCs and detection rules.
- **Threat Actors:** GRU unit 26165 (tracked as APT28 / Fancy Bear / Forest Blizzard / Blue Delta)
- **Mitigation:** Apply vendor patches for referenced CVEs; enable EDR, network segmentation, MFA; block/alert on NTLM to external hosts; harden mail and web infrastructure; apply IP camera firmware updates; implement allowlisting and attack‑surface reduction; follow the CISA mitigation checklist in the advisory.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟡 High Severity — Critical Everest Forms Pro flaw exploited to take over WordPress sites

**CVE:** `CVE-2026-3300` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-06
**Reference:** <https://www.bleepingcomputer.com/news/security/critical-everest-forms-pro-flaw-exploited-to-take-over-wordpress-sites/>

> Hackers are actively exploiting a critical vulnerability (CVE-2026-3300) in the Everest Forms Pro plugin, which lets them take complete control of a WordPress website. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Vulnerability is a PHP code injection in the plugin's "Complex Calculation" feature: user‑supplied form field values are improperly handled and inserted into code evaluated with eval(), enabling unauthenticated attackers to execute arbitrary PHP code and fully compromise the site.
- **Affected Products:** Everest Forms Pro (all versions up to and including 1.9.12)
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC available at http://atomicedge.io/cve-proof/cve-2026-3300-everest-forms-pro-version-1-9-12-critical-vulnerability-proof-of-concept
- **Patch Available:** Update Everest Forms Pro to 1.9.13 or newer. See patch guidance: http://fixitphill.com/wordpress/everest-forms-pro-cve-2026-3300-wordpress-rce-patch-guide
- **Active Exploitation:** Confirmed — multiple reports (Bleeping Computer, Wordfence, The Hacker News) indicate active exploitation in the wild targeting approximately 4,000 active installations.
- **Threat Actors:** None known
- **Mitigation:** Update Everest Forms Pro to 1.9.13 or newer; if immediate update is impossible, disable forms using the "Complex Calculation" feature, remove the plugin, or block exploit attempts via WAF/ModSecurity rules. Review logs and restore from clean backups if compromise is suspected.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
