# Zero Day Pulse

> **Generated:** 2026-07-05 08:39 UTC &nbsp;|&nbsp; **Total:** 11 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated path traversal (directory traversal) in SimpleHelp's 'toolbox' web component. An attacker sends a specially crafted HTTP GET request containing traversal sequences such as '../../../../../../' that escape the intended download path and read arbitrary files from the SimpleHelp host. Sensitive files exposed include the server configuration (serverconfig.xml — hashed passwords, LDAP credentials, OIDC secrets, API keys, TOTP seeds), /etc/passwd, /root/.ssh/id_rsa, and on Windows hosts C:\Windows\System32\config\SAM. Some logs/secrets are encrypted with a hardcoded key, further exposing them once extracted. No authentication is required, and the attack is remotely exploitable over the network, enabling credential theft, lateral movement, and follow-on ransomware deployment.
- **Affected Products:** SimpleHelp Remote Support / RMM software versions 5.5.7 and all earlier releases (the same family also includes CVE-2024-57726 and CVE-2024-57728). Patched versions: v5.5.8 (general release), with backported patches for v5.4.10 and v5.3.9.
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true - Public PoC at https://github.com/imjdl/CVE-2024-57727 (Python script poc.py). A Metasploit auxiliary module 'simplehelp_toolbox_path_traversal' also exists.
- **Patch Available:** true - SimpleHelp v5.5.8 (and backported patches v5.4.10 and v5.3.9). Vendor advisory: https://guides.simple-help.com/kb---security-vulnerabilities-01-2025 . Downloads: https://simple-help.com/downloads . Patches: https://simple-help.com/releases/patch-5.4-010725/shelp-jar-with-dependencies.jar and https://simple-help.com/releases/patch-5.3.9-010725/patch.zip . Tenable Nessus plugin 233191 confirms post-5.5.8 builds are no longer vulnerable.
- **Active Exploitation:** true - CISA added CVE-2024-57727 to the Known Exploited Vulnerabilities (KEV) catalog on 2025-02-13, and CISA Advisory AA25-163A (published 2025-06-12) confirms ransomware actors have exploited unpatched SimpleHelp RMM instances since January 2025, including an incident that compromised a utility billing software provider and its downstream customers via double-extortion ransomware.
- **Threat Actors:** DragonForce ransomware actors (named in CISA Advisory AA25-163A); AttackIQ additionally lists Medusa, Royal, Hive, MuddyWater, INC, Lynx, SafePay, and Karakurt Data Extortion Group as ransomware operators exploiting SimpleHelp RMM in this broader pattern.
- **Mitigation:** 1) Immediately isolate the SimpleHelp server from the internet or stop the server process. 2) Upgrade to SimpleHelp v5.5.8 or later (or apply backported patches v5.4.10 / v5.3.9). 3) Change Administrator and all Technician account passwords; rotate any secrets (LDAP, OIDC, API keys, TOTP seeds, SSH keys) that may have been exposed. 4) Restrict source IP addresses for Technician and Administrator logins, and disable the SimpleHelpAdmin user in favor of an Administrator Technician account. 5) Disable local Technician logins in favor of Active Directory/LDAP authentication; create new API tokens and IP-restrict API requests. 6) Restrict firewall connections to the SimpleHelp server and configure Server Event alerts for admin logins, failed logins, and configuration changes. 7) Hunt for suspicious executables with three-letter alphabetic filenames (e.g., aaa.exe, bbb.exe) created after January 2025 and run reputable AV/vulnerability scans. 8) If compromise is suspected: disconnect affected systems, reinstall the OS from clean media, and restore data only from clean offline backups. 9) Long-term: maintain a robust asset inventory, keep offline backups, and do not expose remote services such as RDP on the web.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an AI system processes external content (websites, emails, documents, repository files) containing malicious instructions embedded by an attacker. The LLM ingests poisoned content and follows attacker commands instead of user intent. Common techniques include visual hiding via CSS (display:none, off-screen positioning, transparent text), HTML comment cloaking, data-* attribute injection (e.g., ai:action namespaces), zero-width Unicode characters and homoglyphs for obfuscation, base64-encoded instructions, and authority impersonation tokens (e.g., [SYSTEM OVERRIDE], fake ANTHROPIC_MAGIC_STRING). Documented outcomes include API key exfiltration, data destruction (e.g., sudo rm -rf), unauthorized financial transactions, denial-of-service via infinite streaming, and tone/behavior manipulation of AI summaries.
- **Affected Products:** Google Gemini, Google Workspace with Gemini (Gmail, Docs), ChatGPT, GitHub Copilot, Cursor (versions below 1.3, CVE-2025-54131), Claude Code, MCP Server (versions prior to 1.3.3, CVE-2025-52573), nanobot (versions prior to 0.1.6, CVE-2026-33654), RAG-based applications, AI-integrated browsers/search engines, Android 17, Chrome 146
- **CVSS Score:** CVSS score unavailable. No single base score is assigned to the IPI threat category in this blog post. Specific CVEs carry their own scores (e.g., CVE-2026-33654 = 8.9 under CVSS 4.0).
- **CVSS Vector:** CVSS vector unavailable. This Google blog post is a category-level threat analysis, not a single vulnerability advisory with an assigned CVSS v3 vector. Individual IPI-related CVEs use CVSS 4.0 (e.g., CVE-2026-33654: CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N).
- **Exploit Available:** true. Public PoCs and real-world exploits exist, including: https://github.com/brennanbrown/atlas-prompt-injection-poc; a real-world malicious IPI payload at reviewerpress[.]com documented by Unit 42; and 10 in-the-wild IPI payloads documented by Forcepoint X-Labs.
- **Patch Available:** true. No single patch addresses the IPI category as a whole—Google applies continuous hardening and layered mitigations. For specific implementations: nanobot version 0.1.6 patches CVE-2026-33654; Cursor version 1.3 fixes CVE-2025-54131; MCP Server versions 1.3.3+ address CVE-2025-52573. Advisory: http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html
- **Active Exploitation:** true. Google's Threat Intelligence teams observed a 32% relative increase in malicious-category prompt injections between November 2025 and February 2026. Palo Alto Unit 42 documented real-world IPI attacks including Screening Serpens (Iranian APT) activity and a live malicious payload on reviewerpress[.]com. Forcepoint X-Labs identified 10 IPI payloads caught in the wild.
- **Threat Actors:** The Google blog post does not name specific threat actors. Complementary research attributes real-world IPI abuse to: (1) Screening Serpens (Iranian APT) observed by Palo Alto Unit 42; (2) individual website authors conducting experiments/pranks; (3) SEO spammers manipulating AI assistants; and (4) actors attempting data exfiltration and machine vandalism.
- **Mitigation:** Layered defense strategy: (1) Model hardening to improve Gemini's ability to ignore embedded malicious commands; (2) Human and automated red-teaming; (3) Google AI Vulnerability Reward Program and OSINT monitoring; (4) Centralized vulnerability catalog with synthetic data generation (Simula); (5) Deterministic Policy Engine enforcing URL sanitization, regex takedowns, tool chaining policies, and mandatory user confirmations; (6) ML-based defenses retrained with synthetic datasets; (7) LLM-based iterative prompt engineering; (8) Output validation (format checks, semantic filters, RAG Triad of context relevance/groundedness/Q&A relevance); (9) Strict data-instruction boundary between untrusted content and system prompts; (10) Least-privilege access controls and separate API tokens; (11) Human-in-the-loop approval for high-risk operations; (12) Regular adversarial testing and penetration testing.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an attack class where an adversary influences an LLM by placing malicious instructions inside any data source or tool the LLM ingests — emails, shared documents, calendar invites, web pages, Drive files, Slides speaker notes, or device notifications — rather than via the user's direct input. When the user issues a benign query, Gemini's retrieval/agentic pipeline retrieves the poisoned content, the injected instructions override or steer system/model behavior, and the model performs attacker-chosen actions such as generating phishing prompts, exfiltrating corporate data through crafted URLs, executing smart-home commands, or invoking connected tools. The technique can be zero-click (no user interaction required), is not a traditional software bug, and generalizes across RAG and agentic systems. Google's blog notes IPI is not a problem that can be 'solved and shipped' because sophisticated LLMs combined with agentic automation form an 'ultra-dynamic and evolving playground for adversarial attacks.'
- **Affected Products:** Google Gemini app; Gemini in Gmail; Gemini in Google Docs editors; Gemini in Google Drive; Gemini in Google Chat; Gemini in Google Calendar; Gemini for Workspace; Additionally, Gemini Enterprise / Vertex AI Search was affected by the GeminiJack zero-click vulnerability disclosed 2025-12-09. Specific version numbers are not published; Google treats the issue as a continuous threat rather than a version-bounded vulnerability.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true. Public PoCs and weaponized exploits documented: GeminiJack zero-click exfiltration (https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/), SafeBreach Gemini voice assistant hijack via notifications (https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/), Unit 42 web-based IPI observations (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/), Forcepoint 10 IPI payloads (https://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads), and HiddenLayer Gemini for Workspace phishing attacks (https://www.hiddenlayer.com/research/new-gemini-for-workspace-vulnerability-enabling-phishing-content-manipulation).
- **Patch Available:** true. Continuous model and configuration updates rather than a single CVE-style patch. Specific updates: adversarial-training mitigations in Gemini 2.5 (DeepMind 2025-05-20), content-classifier updates after SafeBreach voice-assistant disclosure, and separation of Vertex AI Search from Gemini Enterprise following GeminiJack (Noma Labs 2025-12-09). Advisory URL: http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html
- **Active Exploitation:** true. Confirmed in-the-wild exploitation: Forcepoint documented 10 IPI payloads in active sites including unauthorized financial transaction exploitation (https://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads); Unit 42 documented web-based IPI attacks against AI agents (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/); SafeBreach demonstrated real-world hijack of Gemini Voice Assistant via messaging notifications; Noma Labs demonstrated zero-click GeminiJack exfiltration from Gemini Enterprise; HiddenLayer documented Gemini for Workspace phishing/content manipulation.
- **Threat Actors:** None known.
- **Mitigation:** Google documents a layered, continuously-updated defense strategy, not a one-time patch: (1) Deterministic defenses — user-confirmation/approval flows for sensitive actions (e.g., deleting calendar events), markdown sanitization, suspicious-URL redaction via Google Safe Browsing, tool-chaining policies and regex pattern takedowns. (2) ML-based defenses — proprietary prompt-injection content classifiers trained on adversarial data. (3) LLM-based defenses — 'security thought reinforcement' system instructions that remind the model to ignore injected directives. (4) Gemini model hardening — adversarial fine-tuning and resilience built into Gemini 2.5 (DeepMind automated red teaming, Spotlighting, self-reflection). Hardening advice for admins/users: avoid granting Gemini access to untrusted external documents, enable user-confirmation prompts for sensitive actions, monitor end-user security mitigation notifications, and update to the latest Gemini for Workspace release (https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini ; https://deepmind.google/blog/advancing-geminis-security-safeguards/).
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is an attack class in which adversary-controlled content (malicious web pages, third-party iframes, reviews, ads, or user-generated content) embeds hidden natural-language instructions that are read by an LLM-driven browser agent and interpreted as legitimate user commands. The agent's privileged access to the browsing environment (page content, origin context, and side panels like the 'chrome://glic' Gemini Live panel) allows these injected instructions to steer the agent toward data exfiltration, local file access, screenshots, and privileged API calls the user never authorized. The closely related CVE-2026-0628 ('Glic Jack') demonstrates this in practice: a Chrome extension with only basic declarativeNetRequest permissions can inject JavaScript into the Gemini Live side panel (which uses a WebView to embed gemini.google.com), enabling privilege escalation to camera, microphone, screenshots, and local file access.
- **Affected Products:** Google Chrome (with Gemini in Chrome / agentic browsing preview enabled); Google Chrome prior to 143.0.7499.192 (Windows/Mac: 143.0.7499.192/.193; Linux: 143.0.7499.192) for the related CVE-2026-0628; Google Gemini Enterprise and Vertex AI Search for the related GeminiJack flaw.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true. Public PoCs are available. GeminiJack PoC: https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/ (published 2025-12-08). Glic Jack / CVE-2026-0628 PoC: https://unit42.paloaltonetworks.com/gemini-live-in-chrome-hijacking/ (published 2026-03-02).
- **Patch Available:** true. Patches are available: (a) CVE-2026-0628 / 'Glic Jack' was fixed in Chrome 143.0.7499.192/.193 (Windows/Mac) and 143.0.7499.192 (Linux) — see https://chromereleases.googleblog.com/2026/01/stable-channel-update-for-desktop.html; (b) Google updated retrieval/indexing logic in Google Gemini Enterprise and separated Vertex AI Search from Gemini Enterprise to mitigate the GeminiJack zero-click flaw.
- **Active Exploitation:** false. No in-the-wild exploitation of the indirect prompt injection threat class in Chrome's agentic browsing has been publicly confirmed. The closely related CVE-2026-0628 ('Glic Jack') and GeminiJack flaws were responsibly disclosed to Google by researchers (Palo Alto Unit 42 and Noma Labs, respectively) and patched before any public in-the-wild exploitation was reported.
- **Threat Actors:** None known. The blog post and related sources describe indirect prompt injection as a generic threat class; no specific APT groups, ransomware operators, or named threat actors have been identified as exploiting it.
- **Mitigation:** Google introduced layered architectural defenses in Chrome's agentic browsing: (1) User Alignment Critic — an isolated model that vets each proposed agent action for task alignment and goal-hijacking; (2) Agent Origin Sets — an extension of Site Isolation that constrains the agent to read-only and read-writable origins relevant to the user's task; (3) Gating Functions that separate origins into read-only and read-writable buckets; (4) User Confirmations plus Work Logs that require explicit approval for high-impact actions (banking, medical, payments, messaging, Google Password Manager sign-ins); (5) prompt-injection classifiers running in parallel with the planning model to block actions triggered by malicious content; (6) 'spotlighting' techniques that bias the model to prefer user/system instructions over page content; (7) deterministic URL checks restricting model-generated URLs to known public URLs; (8) automated red-teaming using sandboxed malicious sites. Hardening advice: update Chrome to >= 143.0.7499.192, minimize installed extensions, and avoid granting elevated permissions to untrusted extensions.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2025-48530 is a linear buffer overflow (CWE-125) in the CrabbyAVIF Rust-based AVIF image parser/decoder in the Android System component. In multiple locations of the AVIF decoding path — including YUV/Y/UV/alpha planes and chroma width/plane size/row-bytes calculations — incorrect bounds checks permit out-of-bounds (OOB) memory accesses when processing attacker-supplied AVIF image data. The bug can be triggered remotely without user interaction or privileges and, in combination with other bugs, can lead to remote code execution. Google framed this as the platform's first Rust-based memory-safety vulnerability — a 'near-miss' caught before public shipping, demonstrating the value of contained unsafe code surface.
- **Affected Products:** Android 16 (CrabbyAVIF Rust-based AVIF parser/decoder in the System component, package platform/external/rust/crabbyavif)
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known.
- **Mitigation:** Apply the August 2025 Android Security Bulletin to all Android installations (security patch level 2025-08-01 or later). Update CrabbyAVIF (platform/external/rust/crabbyavif) to a fixed revision. Defense-in-depth: retain/enable Android's Scudo hardened memory allocator to constrain impact of any future memory-corruption issues. Since the vulnerability was caught before public release, most user devices are not affected, but downstream consumers of the CrabbyAVIF library should ensure they pull a patched version.
- **Vendor Advisory:** https://source.android.com/security/bulletin/2025-08-01

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is an attack vector targeting generative AI systems in which an attacker embeds hidden malicious instructions inside external data sources that the AI ingests as context (examples cited: emails, documents, calendar invites). When the model processes the tainted content, the hidden instructions cause it to perform attacker-directed actions such as exfiltrating user data or executing other rogue actions on the user's behalf. This is distinct from direct prompt injection, where the attacker submits malicious commands directly into the user-visible prompt. The blog frames it as an emerging industry-wide class of threats targeting LLMs and agents that consume untrusted external content.
- **Affected Products:** Google Gemini (including Gemini 2.5 and the Gemini app), Google Workspace, Gmail, Google Calendar, Google Docs, Google Safe Browsing, Android, Chrome. No specific vulnerable version ranges are identified because this is a class-of-attack advisory rather than a single-CVE vulnerability.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Google describes a layered defense strategy composed of: (1) model hardening through adversarial-data training applied to Gemini 2.5 models; (2) prompt-injection content classifiers that detect and flag injected instructions; (3) security thought reinforcement via system-prompt conditioning; (4) markdown sanitization and suspicious-URL redaction to defang malicious links rendered by the model; (5) a user confirmation framework (Human-In-The-Loop) requiring explicit user approval for sensitive actions; (6) end-user security mitigation notifications surfacing warnings when defenses are triggered; and (7) robust evaluation pipelines including threat analysis, AI red-teaming, and adversarial training. General hardening advice: treat all third-party/untrusted content as untrusted input, isolate instructions from data, sanitize rendered output, and require human confirmation for any action that touches user data or external systems.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored threat actors exploit a set of known CVEs against network edge devices — specifically Cisco IOS XE Web UI (CVE-2023-20198 RCE / CVE-2023-20273 privilege escalation), Cisco IOS/IOS XE Smart Install (CVE-2018-0171), Palo Alto Networks PAN-OS GlobalProtect (CVE-2024-3400 command injection via GlobalProtect), and Ivanti Connect Secure/Policy Secure (CVE-2023-46805 auth bypass chained with CVE-2024-21887 command injection). After gaining initial access, the actors pivot into provider edge (PE) and customer edge (CE) routers, modify router configurations — particularly adding unauthorized Access Control Lists commonly named 'access-list 20' containing attacker-controlled IPs — and abuse Cisco Guest Shell (chvrf / dohost / guestshell run bash) on IOS XE and NX-OS for persistent long-term footholds. They then leverage trusted connections and compromised devices to pivot laterally into telecommunications, government, transportation, lodging, and military networks worldwide. Per CISA, exploitation of zero-day vulnerabilities has not been observed; the campaign relies entirely on known/n-day CVEs.
- **Affected Products:** Cisco IOS XE Web UI (fixed in 17.9.4a, 17.6.6a, 17.3.8a, 16.12.10a) — CVE-2023-20198 and CVE-2023-20273; Cisco IOS/IOS XE Smart Install (devices with Smart Install enabled) — CVE-2018-0171; Palo Alto Networks PAN-OS GlobalProtect versions 10.2, 11.0, 11.1 (fixed in 10.2.9-h1, 11.0.4-h1, 11.1.2-h3) — CVE-2024-3400; Ivanti Connect Secure and Ivanti Policy Secure (9.x and 22.x releases) — CVE-2023-46805 and CVE-2024-21887. Fortinet, Juniper, and Microsoft Exchange are also noted as potentially affected.
- **CVSS Score:** CVSS score unavailable at advisory level. Individual CVE base scores: CVE-2023-20198 = 10.0 (Critical); CVE-2024-21887 = 9.1 (Critical); CVE-2024-3400 = 10.0 (Critical); CVE-2018-0171 = 9.8 (Critical); CVE-2023-20273 = 7.2 (High); CVE-2023-46805 = 8.2 (High).
- **CVSS Vector:** CVSS vector unavailable at advisory level. Individual CVE vectors include: CVE-2023-20198 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H); CVE-2023-20273 (CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H).
- **Exploit Available:** true — Public exploits and PoCs are widely available for these CVEs, and several (e.g., CVE-2023-20198, CVE-2024-3400, CVE-2024-21887, CVE-2023-46805) are tracked in the CISA Known Exploited Vulnerabilities (KEV) catalog. Source: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- **Patch Available:** true — Vendor patches are available from Cisco (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxe-webui-privesc-j22SaA4z), Palo Alto Networks (https://security.paloaltonetworks.com/CVE-2024-3400), and Ivanti (https://forums.ivanti.com/s/article/CVE-2023-46805-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure). Note: the advisory's supplementary guidance states that no additional remediation beyond patching the listed CVEs and applying the hardening controls has been issued at the campaign level.
- **Active Exploitation:** true — Confirmed active exploitation in the wild. CISA AA25-239A documents that these PRC state-sponsored actors have been conducting a sustained global espionage campaign since at least 2021, systematically compromising telecommunications, government, transportation, lodging, and military networks worldwide. Several of the underlying CVEs are tracked in CISA's Known Exploited Vulnerabilities (KEV) catalog. Sources: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a ; https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor (also tracked under aliases FamousSparrow, Earth Estries, and UNC2286). Per CISA AA25-239A, this activity partially overlaps with industry tracking for these China-linked state-sponsored APT groups conducting a long-running global espionage campaign since at least 2021.
- **Mitigation:** 1) Patch all CVEs listed in the advisory against Cisco IOS XE (17.9.4a / 17.6.6a / 17.3.8a / 16.12.10a), PAN-OS GlobalProtect (10.2.9-h1 / 11.0.4-h1 / 11.1.2-h3), Ivanti Connect Secure/Policy Secure, and Cisco Smart Install. 2) Regularly pull running configurations from networking equipment and compare against authorized baselines; review ACLs (hunt for unauthorized 'access-list 20' entries), routing tables, transport protocols, and remote access configs for unauthorized changes. 3) On Cisco IOS XE / NX-OS: disable the HTTP server if not required, audit/disable Cisco Guest Shell entirely if not operationally required, and monitor for guestshell enable, guestshell run bash, chvrf, and dohost commands via syslog, AAA accounting, and off-box telemetry. 4) Enforce SNMPv3 with authentication/privacy, eliminate weak/default SNMP community strings, and disable unused services, ports, and legacy protocols such as Telnet and unencrypted HTTP. 5) Verify authenticity/permission levels of all local accounts and watch for abnormal TACACS+/RADIUS server changes or redirection. 6) Segregate management services (SSH/HTTPS/SNMP/TACACS+/RADIUS) into out-of-band networks or dedicated VRFs; apply Control-Plane Policing (CoPP), infrastructure ACLs, and prevent route leakage. 7) Validate firmware/image hashes against vendor-provided values and enable signed-image enforcement. 8) Audit for unexpected GRE/IPsec tunnels, foreign AAA servers, and packet capture/mirroring configurations. 9) Prioritize remediation using CISA's KEV catalog. 10) Apply Palo Alto Threat Prevention signatures to GlobalProtect interfaces.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Since at least 2022, GRU Unit 26165 (APT28) has conducted cyber-espionage targeting Western logistics entities and IT companies supporting Ukraine aid across the US, Ukraine, Poland, Germany, France, Italy, and the Netherlands. Initial access: spearphishing with credential-harvesting pages and malicious attachments/links, exploitation of the listed CVEs (CVE-2023-23397 for NTLM hash theft via crafted Outlook messages, CVE-2023-38831 for code execution via malicious archives), password spraying/brute-forcing through anonymized infrastructure, and SQL injection against corporate VPNs. Persistence: scheduled tasks, Run keys, malicious startup shortcuts, mailbox-permission manipulation. Lateral movement: Impacket, PsExec, RDP. Reconnaissance: RTSP DESCRIBE requests with default/brute-forced credentials against IP cameras. Custom malware: HEADLACE (PowerShell shortcut-dropper, credential-phishing dialogs) and MASEPIE (Python-based RAT); additional tooling OCEANMAP, STEELHOOK, and METASPLOIT framework. Exfiltration: .zip staging via OpenSSH; log clearing via wevtutil.
- **Affected Products:** This is a multi-CVE threat advisory. Affected products include: (1) Microsoft Outlook — CVE-2023-23397; (2) RARLAB WinRAR before 6.23 — CVE-2023-38831; (3) Roundcube Webmail before 1.4.4 — CVE-2020-12641; (4) Roundcube Webmail before 1.2.13 / 1.3.x before 1.3.16 / 1.4.x before 1.4.10 — CVE-2020-35730; (5) Roundcube Webmail before 1.3.17 / 1.4.x before 1.4.12 — CVE-2021-44026. Additional targeted assets: IP cameras/border surveillance equipment and corporate VPN infrastructure.
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable for the advisory as a whole. For the most critical CVE referenced, CVE-2023-23397 (Microsoft Outlook): CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H.
- **Exploit Available:** true — weaponized exploits have been observed in the wild. APT28 used a specially crafted Microsoft Outlook message (CVE-2023-23397) to exfiltrate NTLM hashes and a maliciously crafted archive (CVE-2023-38831) to execute arbitrary code.
- **Patch Available:** true — vendor patches exist for all CVEs. Microsoft fix for CVE-2023-23397 (March 2023 Patch Tuesday); WinRAR 6.23+ for CVE-2023-38831; Roundcube fixes 1.2.13, 1.3.16, 1.3.17, 1.4.4, 1.4.10, 1.4.12 for CVE-2020-12641, CVE-2020-35730, CVE-2021-44026.
- **Active Exploitation:** true — confirmed active exploitation in the wild. CISA, FBI, NSA, and international partners document that GRU Unit 26165 (APT28) has been actively targeting Western logistics entities and technology companies supporting Ukraine aid since 2022. All five referenced CVEs are listed in CISA's Known Exploited Vulnerabilities Catalog.
- **Threat Actors:** Russian GRU 85th Main Special Service Center (85th GTsSS), military unit 26165 — also tracked as APT28, Fancy Bear, Forest Blizzard, BlueDelta, and UAC-0001. This is a Russian state-sponsored cyber espionage campaign.
- **Mitigation:** (1) Patch all referenced CVEs: CVE-2023-23397, CVE-2023-38831, CVE-2020-12641, CVE-2020-35730, CVE-2021-44026. (2) Harden Exchange/Outlook against NTLM relay; restrict/disable NTLM and SMBv1. (3) Enforce MFA and phishing-resistant authentication on VPN, Outlook Web Access, and all remote access. (4) Harden IP cameras: disable UPnP, P2P, and Anonymous Visit features; use supported devices with current firmware; disable FTP/web interfaces; enable authenticated RTSP; restrict with firewalls/allowlists. (5) Disable unused ports/services. (6) Audit and alert on abnormal use of PowerShell, schtasks, wevtutil, and registry-editing tools. (7) Hunt for LOLBin abuse (ntdsutil, vssadmin, Certipy, Get-GPPPassword.py), unexpected mailbox-permission changes, Tor/commercial-VPN egress, and RTSP requests to IP cameras. (8) Monitor SOHO/router infrastructure for proxying activity. (9) Apply IOCs from AA25-141A STIX bundle.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

**Parallel AI Enrichment:**

- **Technical Details:** The referenced source is a CrowdStrike thought-leadership article (not a specific vulnerability advisory) discussing systemic browser security risks. It describes how attackers exploit weaknesses in rendering logic, JavaScript execution, document handling, and memory safety in browsers, then chain those with sandbox escapes, privilege escalation, or other techniques to move from browser activity to system access. The article cites CrowdStrike's 2026 Global Threat Report statistic that 42% of vulnerabilities were exploited before public disclosure, and the Verizon 2026 Data Breach Investigations Report finding that vulnerability exploitation surpassed stolen credentials as the top breach entry point in 2025. It emphasizes that unpatched N-day vulnerabilities may pose broader enterprise risk because exploit paths and proof-of-concept code become publicly available after disclosure. No specific CVE, exploit code, or technical walkthrough of an individual vulnerability is provided in the source article.
- **Affected Products:** Chromium-based browsers (general; no specific versions identified)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** The article recommends layered defenses that protect the browser session in real time rather than relying solely on patching. Specifically, it advocates CrowdStrike Falcon Secure Access, which operates inside the browser's JavaScript execution layer and uses JavaScript Layout Randomization (JSLR) to disrupt exploit chains regardless of patch status. General hardening guidance includes: keep browsers updated to reduce the patch gap, monitor runtime browser activity and session behavior to block credential theft, malicious extensions, session hijacking, AI-driven data theft, and data exfiltration, and avoid relying on patch timing or network-level inspection alone.
- **Vendor Advisory:** https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/

---

## 10. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable. The referenced item is the CrowdStrike State of Cloud Detection and Response (CDR) Survey, a research report published June 22, 2026, based on responses from 1,000 global security leaders. Key aggregate findings: 94% of organizations reported cloud intrusions resulting in data exposure or exfiltration; 73% cannot consistently guarantee detection; 95% have incomplete security sensor/agent coverage of cloud workloads; 78% cannot reliably distinguish legitimate from malicious behavior; 79% say tools generate too many alerts; 98% do not remediate every identified threat; 51% require at least one hour to detect an intrusion; 91% cannot contain all cloud intrusions in real time; 38% cite tool fragmentation as a contributing factor in intrusions escalating. No specific vulnerability mechanism or attack vector is described.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** false
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** The CrowdStrike State of CDR Survey does not publish concrete step-by-step patches, but the report's key takeaways imply the following hardening guidance for defenders: (1) close cloud control plane visibility gaps—56% report such gaps negatively impact adversary detection; (2) maximize runtime sensor/agent coverage of cloud workloads/instances—95% report incomplete coverage; (3) reduce alert noise and false positives—79% say tools generate too many alerts and 77% of triage time is spent on false positives/low-priority alerts; (4) accelerate mean time to detect/contain—51% require at least one hour to detect and 91% cannot contain intrusions in real time; (5) consolidate fragmented tooling—on average 3 tools are used to detect cloud breaches and 38% of breached organizations cite tool fragmentation as a factor in intrusions escalating; (6) integrate CDR workflows into the SOC/SIEM—67% report significant/moderate integration gaps; (7) extend protection to AI/ML workloads—81% reported incidents targeting AI/ML environments. CrowdStrike's associated product positioning is Falcon Cloud Security / the Falcon platform for unified CDR.
- **Vendor Advisory:** https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/

---

## 11. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
