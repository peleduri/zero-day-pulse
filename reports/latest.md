# Zero Day Pulse

> **Generated:** 2026-06-01 11:08 UTC &nbsp;|&nbsp; **Total:** 11 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 9 &nbsp;|&nbsp; 🟡 High: 2 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is an unauthenticated directory traversal vulnerability in SimpleHelp server (versions 5.5.7 and earlier) that permits attackers to retrieve arbitrary files, such as configuration files containing hashed or reversible passwords, enabling credential theft and further compromise.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) server and client – versions 5.5.7 and earlier (including 5.4.10)
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Public proof‑of‑concept walkthroughs are available (e.g., Medium/TryHackMe write‑ups). No vendor‑released exploit code.
- **Patch Available:** Yes – patches released in SimpleHelp version 5.5.8 (and later). Details at https://simple-help.com/kb---security-vulnerabilities-01-2025 and downloads at https://simple-help.com/downloads.
- **Active Exploitation:** Yes – confirmed active exploitation reported by CISA and security vendors.
- **Threat Actors:** DragonForce ransomware group
- **Mitigation:** Isolate or stop the vulnerable SimpleHelp server, upgrade immediately to version 5.5.8 or later, determine installed version via /allversions, perform threat hunting, restrict exposure of remote services, and apply compensating controls as needed.
- **Vendor Advisory:** https://simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — Critical WP Maps Pro Flaw Actively Exploited to Create Admin Accounts

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://thehackernews.com/2026/06/critical-wp-maps-pro-flaw-actively.html>

> Threat actors are attempting to actively exploit a critical security flaw impacting WP Maps Pro, a WordPress plugin that has had over 15,000 sales on the Envato Market, to create malicious administrator accounts on susceptible sites.

WP Maps Pro allows site owners to embed customizable Google Maps and OpenStreetMap with markers, listings, and advanced location features on WordPress sites. It is

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated AJAX action wpgmp_temp_access_ajax is registered with wp_ajax_nopriv_ and protected only by a nonce (fc-call-nonce) that is exposed on the frontend via wp_localize_script. An attacker can POST action with check_temp=false, triggering wpgmp_temp_access_support(), which calls wp_insert_user() to create an administrator account and returns a magic login URL that invokes wp_set_auth_cookie(), giving full admin takeover.
- **Affected Products:** WP Maps Pro (wp-google-map-gold) <= 6.1.0
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** Public proof‑of‑concept exploit available on GitHub: https://github.com/xShadow-Here/CVE-2026-8732
- **Patch Available:** Patched in WP Maps Pro version 6.1.1 (released May 20, 2026). Details at https://www.wordfence.com/blog/2026/05/15000-wordpress-sites-affected-by-administrator-account-creation-vulnerability-in-wp-maps-pro-wordpress-plugin/
- **Active Exploitation:** Yes – Wordfence reported active exploitation, blocking 2,858 attacks in 24 hours; also reported by The Hacker News.
- **Threat Actors:** None known
- **Mitigation:** Update WP Maps Pro to version 6.1.1 or later. Apply the Wordfence firewall rule (premium/response users received it May 18 2026; free users June 17 2026). As a temporary workaround, block admin‑ajax POSTs for action wpgmp_temp_access_ajax or add a capability check, or remove/disable the plugin until patched.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an AI system reads content (e.g., a website, email, or document) that includes malicious instructions, leading the model to silently follow those instructions. The blog categorizes observed IPI attempts into harmless pranks, helpful guidance, SEO manipulation, deterring AI agents, and malicious actions like data exfiltration and destruction.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit or PoC is known at this time.
- **Patch Available:** No official patch is available at this time.
- **Active Exploitation:** Confirmed active exploitation has been observed, with a reported 32% increase in malicious IPI detections over the specified period.
- **Threat Actors:** None known
- **Mitigation:** Implement a layered defense strategy, continuously harden AI models, conduct red‑team pressure testing, and participate in the AI Vulnerability Reward Program for ongoing detection and remediation.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an attack vector where malicious instructions are injected into external data sources or tools that a complex AI system (e.g., Workspace with Gemini) consumes during response generation; these instructions can influence LLM behavior even without user input.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC or weaponized exploit reported
- **Patch Available:** No vendor patch; Google describes layered mitigations and continuous monitoring rather than a single patch (see advisory).
- **Active Exploitation:** No confirmed reports of active exploitation in the wild reported in the advisory.
- **Threat Actors:** None known
- **Mitigation:** Google recommends a layered defense: monitoring the web for known IPI patterns, hardened input handling, provenance and trust signals, instruction‑scoping, tool/data access controls, continuous monitoring and updates, and other hardening measures described in the advisory.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability allows a malicious web page to inject crafted prompts into the Gemini AI agent, causing it to execute unintended actions. This indirect prompt injection bypasses origin restrictions and can lead to unsafe AI behaviors.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public exploit for CVE-2026-0628 reported; see LinkedIn post.
- **Patch Available:** Patch unavailable.
- **Active Exploitation:** Confirmed active exploitation reported in a public LinkedIn post.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Data summary indicates a reduction in memory‑safety vulnerabilities due to adoption of Rust across Android components; specific vulnerability mechanism details not provided.
- **Affected Products:** Android platform (first‑party and third‑party open‑source components across C, C++, Java, Kotlin, and Rust)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** None known
- **Patch Available:** Patch information not specified in provided sources; vendor advisory URL unavailable.
- **Active Exploitation:** No confirmed active exploitation reported in the provided sources.
- **Threat Actors:** None known
- **Mitigation:** Ongoing migration to Rust for new code and prevention‑focused memory‑safety strategy; no specific workaround provided.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection — hidden or embedded instructions in external data sources (emails, documents, calendar invites, web content) are fetched by an AI agent and concatenated into prompts, causing the model to execute or disclose sensitive information. The attack chain often combines data‑sourcing, prompt construction, policy/whitelist bypass, and action execution. Research shows examples targeting coding assistants and developer tools.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Public PoCs are available; see Forcepoint report, Infosecurity Magazine article, and the Cursor GitHub security advisory.
- **Patch Available:** Patch not applicable (mitigations and guidance published; no single product patch).
- **Active Exploitation:** In‑the‑wild payloads have been reported by researchers (Forcepoint, Infosecurity). No large‑scale confirmed campaigns are known.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses including: input sanitization and validation, least‑privilege access to external data, strict output handling and redaction, provenance and source validation, runtime policy enforcement (command whitelists/blacklists), human‑in‑the‑loop for sensitive actions, telemetry and anomaly detection, and secure prompt design.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors focus on compromising routers (backbone, PE, CE), modifying firmware or configuration to maintain persistent, long‑term access, and leveraging trusted connections to pivot into other networks for espionage.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit available: None known/public PoC unavailable.
- **Patch Available:** Patch information varies by vendor; check vendor advisories.
- **Active Exploitation:** Confirmed active exploitation reported: Yes — PRC state-sponsored actors targeting telecommunications, government, transportation, lodging, and military infrastructure.
- **Threat Actors:** Salt Typhoon; OPERATOR PANDA; RedMike; UNC5807; GhostEmperor
- **Mitigation:** Mitigation: segment networks, restrict and harden management access, update firmware, apply vendor hardening guidance, monitor and isolate compromised devices.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Actors gain initial footholds by exploiting public vulnerabilities (e.g., WinRAR CVE‑2023‑38831) and via spearphishing/password spraying. After compromise they use tools like Impacket, PsExec, RDP, Certipy and ADExplorer to move laterally, modify Exchange mailbox permissions, archive data, and exfiltrate information.
- **Affected Products:** WinRAR (CVE-2023-38831), Roundcube Webmail (versions listed in advisory)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploitation of CVE-2023-38831 (WinRAR) is documented; no public PoC linked in the advisory.
- **Patch Available:** Vendor fixes are available for CVE-2023-38831 and Roundcube CVEs via vendor advisories referenced in the CVE records; specific URLs are not provided in the CSA.
- **Active Exploitation:** Confirmed active exploitation since 2022 with observed intrusions and exploitation of CVE‑2023‑38831 and other techniques; advisory provides specific IOCs and dates.
- **Threat Actors:** GRU 85th Main Special Service Center (unit 26165) — known as APT28, Fancy Bear, Forest Blizzard, BlueDelta
- **Mitigation:** Network segmentation, deploy endpoint detection & response (EDR), enforce multi‑factor authentication (MFA), implement application allow‑listing, restrict VPN access, monitor logs, harden IP cameras (disable UPnP/P2P, enable authenticated RTSP), and maintain regular patching of vulnerable software.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 10. 🟡 High Severity — Recent Palo Alto Networks Vulnerability Exploited for Weeks

**CVE:** `CVE-2026-0257` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://www.securityweek.com/recent-palo-alto-networks-vulnerability-exploited-for-weeks/>

> Hackers began exploiting CVE-2026-0257, an authentication bypass in Palo Alto Networks PAN-OS, four days after public disclosure. The post Recent Palo Alto Networks Vulnerability Exploited for Weeks appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Authentication override cookie misuse – the GlobalProtect authentication‑override cookies can be forged when the certificate used to encrypt/decrypt those cookies is reused with other services, enabling an attacker to craft valid cookies and gain an unauthorized VPN session via the portal/gateway.
- **Affected Products:** PAN‑OS GlobalProtect portal/gateway – PAN‑OS 12.1 (<12.1.4‑h6), 11.2 (<11.2.4‑h17, <11.2.7‑h14, <11.2.10‑h7, <11.2.12), 11.1 (<11.1.4‑h33, ...), 10.2 (<10.2.7‑h34, ...); Prisma Access older builds.
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** Public proof‑of‑concept script published on GitHub (https://github.com/sfewer-r7/CVE-2026-0257); Rapid7 confirmed exploit.
- **Patch Available:** Yes – vendor published PAN‑OS fixes; see advisory for patched versions.
- **Active Exploitation:** Confirmed – Rapid7 observed successful exploitation beginning May 17, 2026; SecurityWeek reported exploitation within weeks of disclosure; CISA added the CVE to its KEV catalog on 05/29/2026.
- **Threat Actors:** None known
- **Mitigation:** Apply vendor patches immediately; if patches cannot be applied, disable the authentication‑override feature or generate a dedicated certificate exclusive to that feature. Follow CISA KEV guidance for federal agencies.
- **Vendor Advisory:** https://security.paloaltonetworks.com/CVE-2026-0257

---

## 11. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
