# Zero Day Pulse

> **Generated:** 2026-06-08 15:25 UTC &nbsp;|&nbsp; **Total:** 15 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 3 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE‑2024‑57727 is a directory traversal vulnerability in SimpleHelp Remote Support (≤ 5.5.7) that permits unauthenticated attackers to read arbitrary files on the system via crafted paths, enabling retrieval of logs, configuration files, and credentials.
- **Affected Products:** SimpleHelp Remote Support software version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** DragonForce ransomware, other unnamed ransomware actors
- **Mitigation:** Update SimpleHelp to a version newer than 5.5.7, apply any vendor‑released patches, and restrict remote management access to trusted networks.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — Check Point links VPN zero-day attacks to Qilin ransomware gang

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://www.bleepingcomputer.com/news/security/check-point-links-vpn-zero-day-attacks-to-qilin-ransomware-gang/>

> Israeli cybersecurity company Check Point has released security updates to patch a critical flaw affecting Remote Access VPN and Mobile Access deployments, which was exploited in zero-day attacks. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Authentication bypass (logic flow weakness) in IKEv1‑based Remote Access VPN/Mobile Access allowing unauthenticated remote attackers to establish a VPN session without valid user credentials.
- **Affected Products:** Check Point Remote Access VPN, Mobile Access (Security Gateways) and Spark firewalls when configured to use deprecated IKEv1 key‑exchange and accepting legacy Remote Access clients without mandatory machine certificates
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — https://support.checkpoint.com/results/sk/sk185033, https://support.checkpoint.com/results/sk/sk185035
- **Active Exploitation:** true
- **Threat Actors:** Qilin ransomware gang (one confirmed post-compromise case); other actors unknown
- **Mitigation:** Disable IKEv1 (configure Remote Access VPN Authentication to IKEv2 only), remove support for legacy remote access client connections, require machine certificate authentication, enable IPS and download signatures; apply vendor hotfixes.
- **Vendor Advisory:** https://support.checkpoint.com/results/sk/sk185033

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) poisons external data sources (webpages, emails, documents, hidden HTML/CSS) with instruction‑shaped payloads. When a retrieval‑augmented system incorporates this content into its prompt, trigger phrases such as "Ignore previous instructions" or "If you are an LLM" cause the model to follow the malicious instruction, potentially invoking tools, executing shell commands, or performing sandbox escapes (e.g., Antigravity IDE find_by_name → fd -X exec batch → arbitrary script execution).
- **Affected Products:** Google Antigravity IDE (pre‑2026‑02‑28 versions), Gemini Enterprise RAG deployments, other AI agents or RAG systems that ingest external content
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (https://arxiv.org/pdf/2601.07072)
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Restrict agents from fetching untrusted content; enforce strict separation between data and instruction contexts; monitor and log tool‑call activities; inspect memory writes; detect known trigger strings before context inclusion; apply the post‑Feb‑28‑2026 Antigravity IDE patch; conduct regular IPI red‑team exercises and include known payload categories in testing.
- **Vendor Advisory:** https://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an attacker injects malicious instructions into data or tools used by an LLM so the model executes attacker‑supplied directives while completing a user’s query; it can happen without direct user input and is especially relevant for agentic/automated LLMs pulling from multiple data sources.
- **Affected Products:** Google Workspace with Gemini integrations (Gemini in Workspace and Gemini app). If specific versions required: Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability
- **Patch Available:** true — http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html
- **Active Exploitation:** true — http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability
- **Threat Actors:** None known
- **Mitigation:** Google recommends a continuous, layered defense for Workspace/Gemini including source validation, sanitization, provenance tracking, access controls, model-level instruction shielding, telemetry and detection, and rapid patching/controls.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is indirect prompt injection: malicious site content is incorporated into the AI prompts of an agentic browser, allowing an attacker to steer the browser to perform unsafe actions. Google mitigates this with layered defenses that restrict origin access, block prompt injections, and add safety agents to monitor AI actions.
- **Affected Products:** Chrome (agentic browsing / Gemini integration)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Enable Chrome’s built‑in layered defenses for agentic browsing, restrict origin access, block indirect prompt injections, and use Chrome’s safety agents to monitor AI actions as described in the vendor blog.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) embeds hidden malicious instructions in external data sources (emails, documents, calendar invites) that can cause generative AI (e.g., Gemini) to exfiltrate data or perform rogue actions. The attack relies on the model processing untrusted content without sufficient sanitization, allowing adversarial instructions to be executed downstream.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Implement layered defenses — adversarial training/model hardening; content classifiers to detect malicious instructions; security‑thought reinforcement; markdown sanitization and suspicious URL redaction; require explicit user confirmations for risky actions; surface security notifications and provide help‑center guidance.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors target large backbone, provider edge (PE) and customer edge (CE) routers and leverage compromised devices and trusted connections to pivot; they often modify router software/configuration to maintain persistent long‑term access. Specific vulnerability mechanics are not provided in the advisory.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Harden network devices (segment trusted connections, monitor for configuration changes and anomalous GRE/IP‑in‑IP tunnels, rotate credentials, apply vendor mitigations), and follow the mitigation guidance in the CISA advisory.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** The campaign uses GRU 85th GTsSS (Unit 26165) espionage tactics including spearphishing, credential harvesting, and deployment of both bespoke and publicly known tooling to gain initial access, maintain persistence, and exfiltrate data from logistics/transport and IT providers.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** true
- **Threat Actors:** GRU 85th GTsSS (Unit 26165) — APT28 (Russian state‑sponsored)
- **Mitigation:** Implement multifactor authentication, enforce least‑privilege access, keep systems patched and updated, monitor for unusual authentication and network activity, hunt for the indicators of compromise provided in the advisory, segment networks, and apply vendor‑specific hardening guidelines.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — ⚡ Weekly Recap: Instagram Account Hacks, Android Zero-Day, GitHub Worm and More

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://thehackernews.com/2026/06/weekly-recap-instagram-account-hacks.html>

> Monday again. The weekend was meant to be quiet. It wasn&#x27;t. Last week had poisoned packages, a broken AI helper, and a worm tearing through repos. The ugly part: basic tricks still worked.

A chatbot got fooled. A bot token got leaked inside the malware. The same old mistakes showed up again. And while everyone chased the loud stuff, quieter attackers sat in inboxes for months, reading mail a…

**Parallel AI Enrichment:**

- **Technical Details:** Miasma abuses stolen npm tokens and the bypass_2fa parameter to republish backdoored npm packages, enabling automatic self‑propagation across CI/CD pipelines. In some variants, a malicious binding.gyp file triggers node‑gyp native builds, and the payload can execute via AI coding assistants (Claude Code, Gemini CLI, Cursor, VS Code) or npm test scripts, harvesting cloud credentials and exfiltrating them to a GitHub dead‑drop account.
- **Affected Products:** @redhat-cloud-services/chrome (2.3.1, 2.3.2), @redhat-cloud-services/compliance-client (4.0.3, 4.0.4), @redhat-cloud-services/vulnerabilities-client (2.1.8, 2.1.9), Android Framework (Android 14, 15, 16, 16 QPR2)
- **CVSS Score:** 8.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (source: https://thehackernews.com/2026/06/weekly-recap-instagram-account-hacks.html)
- **Patch Available:** true (source: https://thehackernews.com/2026/06/weekly-recap-instagram-account-hacks.html)
- **Active Exploitation:** true (source: https://thehackernews.com/2026/06/weekly-recap-instagram-account-hacks.html)
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Rotate and revoke any exposed cloud and CI/CD credentials, remove compromised package versions, disable post‑install scripts and npm package cooldown checks, monitor and block node‑gyp rebuild activity, and apply the latest Android security patches released by Google.
- **Vendor Advisory:** https://www.microsoft.com/en-us/security/blog/2026/06/02/preinstall-persistence-inside-red-hat-npm-miasma-credential-stealing-campaign/

---

## 11. 🟠 Zero-Day — Everest Forms Vulnerability Exploited to Hack WordPress Sites

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://www.securityweek.com/everest-forms-vulnerability-exploited-to-hack-wordpress-sites/>

> The flaw allows attackers to execute arbitrary code remotely and has been exploited in the wild for two months. The post Everest Forms Vulnerability Exploited to Hack WordPress Sites appeared first on SecurityWeek .

---

## 12. 🟠 Zero-Day — SolarWinds Serv-U Vulnerability Exploited in the Wild

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://www.securityweek.com/solarwinds-patches-exploited-serv-u-vulnerability/>

> Unauthenticated attackers can exploit the flaw via specially crafted POST requests that crash the Serv-U service. The post SolarWinds Serv-U Vulnerability Exploited in the Wild appeared first on SecurityWeek .

---

## 13. 🟡 High Severity — Critical Check Point VPN Flaw Exploited to Bypass Passwords in IKEv1 Setups

**CVE:** `CVE-2026-50751` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://thehackernews.com/2026/06/critical-check-point-vpn-flaw-exploited.html>

> Check Point has warned of active exploitation of a critical vulnerability impacting Remote Access VPN and Mobile Access deployments that are configured to use the deprecated IKEv1 key exchange protocol.

The vulnerability, tracked as CVE-2026-50751 (CVSS score: 9.3), is a case of a logic flow weakness in certificate validation that allows an unauthenticated remote attacker to bypass user

---

## 14. 🟡 High Severity — GeoNode contains a server-side request forgery vulnerability in the service registration endpoint

**CVE:** `CVE-2026-39922` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-hw9r-6m78-w6h3>

> GeoNode versions 4.4.5 and 5.0.2 (and prior within their respective releases) contain a server-side request forgery vulnerability in the service registration endpoint that allows authenticated attackers to trigger outbound network requests to arbitrary URLs by submitting a crafted service URL during form validation. Attackers can probe internal network targets including loopback addresses, RFC1918…

---

## 15. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
