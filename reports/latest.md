# Zero Day Pulse

> **Generated:** 2026-06-29 15:27 UTC &nbsp;|&nbsp; **Total:** 14 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 4 &nbsp;|&nbsp; ✨ Enriched: 6

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Directory traversal vulnerability allowing attackers to read sensitive files via path traversal
- **Affected Products:** SimpleHelp remote support software version 5.5.7 or earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit is known
- **Patch Available:** Patch released; see vendor advisory URL
- **Active Exploitation:** Ransomware actors have exploited the vulnerability in the wild, leveraging CVE-2024-57727
- **Threat Actors:** Ransomware actors
- **Mitigation:** Apply the vendor patch; if patching cannot be done immediately, restrict network access to SimpleHelp RMM, use network segmentation, and monitor logs
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

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

- **Technical Details:** Indirect prompt injection: malicious or crafted web content is incorporated into the agent’s prompt (without being direct user input), allowing hidden instructions to influence the AI agent’s behavior and potentially cause unsafe actions or unauthorized data access.
- **Affected Products:** Google Chrome (agentic browsing / Gemini AI)
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit reported in the reviewed sources
- **Patch Available:** No specific vendor patch for this indirect prompt injection was announced in the reviewed sources; Google described defenses and protections being added to Chrome's agentic features.
- **Active Exploitation:** No confirmed public reports of active exploitation in the wild in the reviewed sources
- **Threat Actors:** None known
- **Mitigation:** Google described layered defenses for agentic browsing: blocking prompt injections, restricting origin access, and adding protections to prevent unsafe AI actions (apply these Chrome security features and follow vendor guidance).
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

- **Technical Details:** Indirect prompt injection (IPI) occurs when malicious instructions are embedded in external data sources (web pages, emails, documents, calendar invites, PR descriptions, etc.) that are ingested into an AI agent's prompt/context; the agent can then follow those hidden instructions (e.g., exfiltrate data, execute actions) unless defenses (model hardening, prompt sanitation, context segmentation, runtime checks, confirmations) prevent it.
- **Affected Products:** Google Workspace AI-powered services (Gmail, Docs, Calendar), Google Gemini (Gemini 2.5), Google Gemini CLI Action, GitHub Copilot Agent, Microsoft 365 Copilot
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — public proof-of-concept exploits have been reported/demonstrated against Gemini CLI Action and GitHub Copilot Agent (SecurityWeek) and EchoLeak PoC for Microsoft 365 Copilot (Cycode).
- **Patch Available:** No official patch indicated; vendor guidance recommends layered defenses and model/hardening updates (see advisory).
- **Active Exploitation:** Yes — reports indicate real-world experiments and confirmed exploited vectors: Gemini CLI Action and GitHub Copilot Agent prompt-injection incidents (SecurityWeek) and EchoLeak in Microsoft 365 Copilot (reported by Cycode).
- **Threat Actors:** None known
- **Mitigation:** Adopt a layered defense strategy including input validation and sanitization, purpose-built ML detectors for malicious instructions, logical context segmentation (separating system vs. user inputs), runtime content filtering and monitoring, least-privilege for AI tools, human review/confirmation dialogs for destructive actions, and user security notifications and training.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Chinese state-sponsored actors exploit network-device CVEs on routers and network edge devices, modify configurations for persistent access, and use traffic mirroring (SPAN/RSPAN/ERSPAN) for surveillance.
- **Affected Products:** backbone routers, provider edge (PE) routers, customer edge (CE) routers, network edge devices
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit reported.
- **Patch Available:** No official vendor patch currently available.
- **Active Exploitation:** Confirmed active exploitation of backbone and edge routers by Chinese state-sponsored actors, as reported in multiple sources.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Apply vendor detection tips and hardening guidance when available, monitor router configurations, disable unused services, segment networks, and simulate attacks to validate defenses.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

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
- **Exploit Available:** Exploit unavailable.
- **Patch Available:** No official vendor patch referenced in the advisory.
- **Active Exploitation:** No confirmed active exploitation reported in the advisory.
- **Threat Actors:** Russian GRU (85th Main Special Service Center, Unit 26165)
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisory/aa25-141a

---

## 9. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 10. 🟠 Zero-Day — Microsoft Removes 119 Edge Extensions That Hid Malware in Images and Fonts

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-29
**Reference:** <https://thehackernews.com/2026/06/microsoft-removes-119-edge-extensions.html>

> Microsoft has shut down a long-running malicious extension operation on the Edge Add-ons store that hid its payloads inside ordinary image and font files, then woke up days after install to steal credentials and run ad fraud.

The company calls it StegoAd, a mash-up of steganography and adware, and ties 119 extensions to a single threat actor it says has been active since at least 2021.

**Parallel AI Enrichment:**

- **Technical Details:** StegoAd used steganography to hide executable JavaScript payloads inside images (PNG, WebP) and WOFF2 font files; extensions provided legitimate functionality, waited (3–5 days) and performed checks (DevTools detection, server-side validation, probabilistic execution), fetched stego files from C2, decoded via layered transforms (case/digit swaps, Base64, XOR), verified signatures, then executed code delivering modules for credential theft, cookie/session exfiltration, affiliate hijacking, ad injection and an RCE backdoor.
- **Affected Products:** Microsoft Edge (Edge Add‑ons store extensions / Chromium-based Edge extensions — extension IDs listed in Microsoft technical report)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept code published; Microsoft published indicators of compromise and technical report/IOCs for detection rather than an exploit PoC.
- **Patch Available:** No vendor 'patch' required or released for a software vulnerability: Microsoft removed all 119 malicious extensions from the Edge Add-ons store, suspended developer accounts, and deployed updated detection/protections (see advisory).
- **Active Exploitation:** Yes — Microsoft observed an active, long-running campaign (StegoAd) that delivered delayed steganographic payloads which in analyzed samples performed ad fraud, credential/session theft and a remote-code-execution backdoor; Microsoft removed the extensions and published IOCs.
- **Threat Actors:** Microsoft did not publicly name an actor; Microsoft ties 119 extensions to a single actor active since at least 2021. Independent reporting links overlap to previously observed operations (reporting mentions possible ties to DarkSpectre/GhostPoster).
- **Mitigation:** Remove/compare installed extensions against Microsoft’s published list; change passwords for sensitive accounts and enable strong 2FA (hardware/FIDO2 recommended); keep Edge and extensions updated; limit extension permissions and install only from verified publishers; follow Microsoft’s published IOCs and platform protections.
- **Vendor Advisory:** https://microsoftedge.github.io/edgevr/posts/Inside-StegoAd-How-We-Disrupted-a-Massive-Malicious-Extension-Campaign/

---

## 11. 🟡 High Severity — Critical SimpleHelp flaw exploited to deploy new stealer malware

**CVE:** `CVE-2026-48558` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-29
**Reference:** <https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-simplehelp-flaw-deploy-new-djinn-infostealer-taskweaver-malware/>

> Hackers are exploiting a recently disclosed critical vulnerability (CVE-2026-48558) in SimpleHelp to deploy Djinn Stealer, a previously undocumented cross-platform information stealer targeting Windows, macOS, and Linux. [...]

---

## 12. 🟡 High Severity — Hackers now exploit critical Oracle E-Business flaw in attacks

**CVE:** `CVE-2026-46817` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-29
**Reference:** <https://www.bleepingcomputer.com/news/security/new-oracle-e-business-suite-flaw-now-exploited-in-attacks/>

> Attackers have begun exploiting a critical vulnerability (CVE-2026-46817) in the Oracle E-Business Suite (EBS) financial application, according to threat intelligence company Defused. [...]

---

## 13. 🟡 High Severity — Public PoC Released for Critical libssh2 CVE-2026-55200 Client-Side SSH Flaw

**CVE:** `CVE-2026-55200` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-29
**Reference:** <https://thehackernews.com/2026/06/public-poc-released-for-critical.html>

> A public proof-of-concept is now out for CVE-2026-55200, a critical flaw in libssh2 that lets a malicious or compromised SSH server trigger memory corruption on a connecting client, with possible code execution. No credentials, no user interaction. The bug affects every release up to and including 1.11.1 and carries a CVSS 4.0 score of 9.2.

libssh2 is a client-side SSH library, not a server.

---

## 14. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
