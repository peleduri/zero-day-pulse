# Zero Day Pulse

> **Generated:** 2026-07-03 13:32 UTC &nbsp;|&nbsp; **Total:** 33 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 21 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path traversal vulnerability in the SimpleHelp web application's file-download endpoint. An unauthenticated remote attacker can submit crafted HTTP requests containing path traversal sequences (e.g., '../') to escape the intended download directory and read arbitrary files from the SimpleHelp host. Exposed files include server configuration files (e.g., serverconfig.xml) containing hashed user passwords and integration/secret keys. These secrets allow the attacker to pivot deeper into the SimpleHelp server and the endpoints it manages. The vulnerability can be chained with CVE-2024-57728 (privilege escalation) and CVE-2024-57729 (arbitrary file upload) for full server takeover.
- **Affected Products:** SimpleHelp Remote Support / Remote Monitoring and Management (RMM), versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Yes — a public proof-of-concept exists. OffSec published a technical write-up and PoC for CVE-2024-57727. Source: https://www.offsec.com/blog/cve-2024-57727
- **Patch Available:** Yes — patched in SimpleHelp version 5.5.8, released on January 8, 2025. Vendor advisory: https://www.simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know
- **Active Exploitation:** Yes — confirmed active exploitation in the wild. Per CISA advisory AA25-163a (published June 12, 2025), ransomware actors have targeted organizations through unpatched SimpleHelp RMM instances since January 2025. In a confirmed February 2025 incident, ransomware actors exploited an unpatched SimpleHelp instance at a utility billing software provider and used that access to compromise downstream utility billing customers in a double-extortion scheme.
- **Threat Actors:** None known
- **Mitigation:** Upgrade SimpleHelp to version 5.5.8 or later immediately (the vendor states there are no workarounds). Defenders should also: (1) identify any SimpleHelp instance on the network running version 5.5.7 or earlier, (2) review SimpleHelp servers for the indicators of compromise listed in CISA AA25-163a, and (3) hunt for activity using the detection signatures (Snort/YARA) provided in that advisory.
- **Vendor Advisory:** https://www.simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — Critical Cursor AI Code Editor Flaws Could Lead to OS-Level Remote Code Execution

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-03
**Reference:** <https://www.securityweek.com/critical-cursor-ai-ide-flaws-could-lead-to-os-level-remote-code-execution/>

> The DuneSlide vulnerabilities enable zero-click prompt injection attacks that escape Cursor&#x27;s sandbox and execute arbitrary code on the underlying operating system. The post Critical Cursor AI Code Editor Flaws Could Lead to OS-Level Remote Code Execution appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Two related sandbox-escape vulnerabilities collectively named 'DuneSlide' enable zero-click remote code execution on the underlying OS from within Cursor IDE's AI agent. (1) CVE-2026-50548 (CWE-22 path traversal): Cursor's sandbox grants write access to the terminal command's working_directory; a zero-click prompt injection (via MCP server request or poisoned web search result) coerces the LLM agent to set the run_terminal_cmd working_directory parameter to an attacker-supplied path outside the project workspace, which Cursor blindly adds to the sandbox's allowed-write list — enabling overwrite of the cursorsandbox helper and arbitrary OS-level code execution. (2) CVE-2026-50549 (CWE-59 improper link resolution): before a Write operation, Cursor canonicalizes the target path to verify it stays in-bounds; if canonicalization fails (e.g., symlink target missing or unreadable), Cursor falls back to the original symlink path and writes without approval. An attacker instructs the agent to create a write-only in-workspace symlink pointing outside the workspace; the failed canonicalization causes Cursor to ignore the out-of-bounds target and write through the symlink to an arbitrary location, again allowing the cursorsandbox helper to be overwritten. Both attacks require no user interaction beyond a benign prompt.
- **Affected Products:** Cursor IDE (desktop) versions prior to 3.0 (i.e., Cursor 2.x and earlier)
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit has been published as of 2026-07-03.
- **Patch Available:** Yes — Cursor IDE 3.0, released on April 2, 2026, patches both CVE-2026-50548 and CVE-2026-50549. Official advisories: https://github.com/cursor/cursor/security/advisories/GHSA-3p48-7v9f-v5cw and https://github.com/cursor/cursor/security/advisories/GHSA-3v8f-48vw-3mjx
- **Active Exploitation:** No confirmed in-the-wild exploitation has been reported. The vulnerabilities were responsibly disclosed to Cursor on February 19, 2026, fixed in Cursor 3.0 on April 2, 2026, and publicly disclosed on July 1-3, 2026 by Cato AI Labs and reported by SecurityWeek. The CVEs have not been added to the CISA KEV catalog as of 2026-07-03.
- **Threat Actors:** None known
- **Mitigation:** Update to Cursor IDE version 3.0 (released April 2, 2026), which patches both CVE-2026-50548 and CVE-2026-50549. Until patched, harden by avoiding untrusted MCP servers and untrusted web content that can reach the agent, reviewing agent-issued terminal commands, restricting Cursor's file/process privileges, and running Cursor with least-privilege user accounts.
- **Vendor Advisory:** https://github.com/cursor/cursor/security/advisories/GHSA-3p48-7v9f-v5cw (CVE-2026-50548) and https://github.com/cursor/cursor/security/advisories/GHSA-3v8f-48vw-3mjx (CVE-2026-50549); Cursor's general security disclosure page: https://cursor.com/security

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI): adversaries seed malicious instructions into web content or retrieval stores that AI agents browse or retrieve from; when the agent consumes that content (via browsing or retrieval-augmented generation), it may follow adversarial instructions or disclose secrets. The attack leverages browsing/retrieval/data-reuse components rather than a traditional software bug.
- **Affected Products:** AI web-browsing agents and retrieval-augmented systems (general), Google Gemini Enterprise (reported GeminiJack case). No comprehensive product/version list available.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Research disclosures and demonstrations exist (Forcepoint disclosed 10 in-the-wild IPI payloads; Noma Labs reported a GeminiJack zero-click vulnerability leveraging IPI techniques). Public research PoCs/demos have been reported in the supplied corpus.
- **Patch Available:** No official vendor patch has been reported in the provided corpus; Google published a security blog advisory describing detection and mitigation work: http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html
- **Active Exploitation:** Yes — multiple reports and vendor advisory indicate in-the-wild IPI payloads and at least one zero-click research finding (GeminiJack). Sources: Google Security Blog (vendor advisory), Forcepoint disclosures, Noma Labs GeminiJack report.
- **Threat Actors:** None known
- **Mitigation:** Vendor and researcher guidance emphasizes continuous mitigation: monitoring/detection of IPI payloads, restricting or hardening browsing and retrieval components, and sanitizing or validating external content before use in prompts or RAG pipelines. See vendor advisory and researcher disclosures.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is a class of attack against LLM-powered applications (e.g., Workspace with Gemini) where an attacker influences the LLM's behavior by injecting malicious instructions into external data or tools the LLM consumes while fulfilling a user query - such as content in emails, documents, calendar invites, or fetched web pages. The injected instructions can cause data exfiltration, suppression of legitimate content, unauthorized actions (e.g., deleting events, executing commands), or financial fraud, and may succeed without any direct input from the victim user.
- **Affected Products:** Google Workspace with Gemini (Gmail, Docs, Calendar, and other Workspace data sources), Gemini 2.5 models
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes - public proof-of-concept and weaponized payloads exist in the wild. Forcepoint X-Labs documented 10 IPI payloads deployed on live websites (April 22, 2026). Sources: https://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads and https://blog.google/security/prompt-injections-web/
- **Patch Available:** No single patch is associated with this vulnerability class. Google treats IPI as an evolving, continuously mitigated threat. Defenses are continuously improved via the layered defense strategy. Advisory: http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html
- **Active Exploitation:** Yes - confirmed active exploitation in the wild. Sources: (1) Google's Common Crawl research found 32% increase in malicious prompt-injection attempts (Nov 2025-Feb 2026) - https://blog.google/security/prompt-injections-web/; (2) Forcepoint X-Labs documented 10 weaponized IPI payloads on live websites (April 22, 2026) - https://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads; (3) Google's advisory references real-world IPI abuse via emails, documents, and calendar invites.
- **Threat Actors:** None known
- **Mitigation:** Google's layered defense strategy: (1) Deterministic defenses - user confirmation prompts for risky actions, URL sanitization, tool-chaining policies, centralized Policy Engine; (2) ML-based defenses - retraining on synthetic vulnerability data; (3) LLM-based defenses - iterative prompt engineering and system instruction refinement; (4) Gemini model hardening; (5) Markdown sanitization; (6) Safe Browsing URL redaction; (7) End-user security notifications; (8) Proactive discovery via red-teaming and the Google AI Vulnerability Rewards Program.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** An indirect prompt-injection (hidden or attacker-controlled content in web pages/data sources) is interpreted by the agent/LLM as instructions. GeminiJack (the reported zero-click issue) abused insufficient policy enforcement in a WebView/data-source boundary in Chrome/Gemini, allowing attacker-controlled content to be treated as model instructions and leading to possible data-exfiltration or unauthorized actions.
- **Affected Products:** Google Chrome (versions prior to 143.0.7499.192), Google Gemini / Gemini Enterprise
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — public proof-of-concept code for CVE-2026-0628 has been published (example: GitHub repository fevar54/CVE-2026-0628-POC); researcher writeups (Noma Labs) also describe the issue.
- **Patch Available:** Yes — Google released a fix. NVD and vendor reporting indicate the Chrome fix is included in builds at/after 143.0.7499.192 (see Google blog and NVD entry).
- **Active Exploitation:** No confirmed in-the-wild exploitation of the specific GeminiJack / CVE-2026-0628 has been reported. However, the attack class (indirect prompt injection) has been observed in the wild by multiple industry teams.
- **Threat Actors:** None known
- **Mitigation:** Update Chrome to the fixed build (upgrade to Chrome 143.0.7499.192 or later). Follow Google’s layered defenses for agentic browsing (prompt-injection hardening, origin restrictions, restrict unsafe AI actions) as described in the vendor blog and release notes.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Out-of-bounds read vulnerability (CWE-125) in the CrabbyAVIF AVIF parser/decoder shipped in AOSP. The flaw stems from incorrect bounds-check logic across multiple code paths in unsafe Rust blocks handling NV12 YUV planes (alpha plane, Y plane, UV planes), chroma width calculation, plane size calculation, and row bytes. An attacker could craft an AVIF image to trigger OOB reads during decode, with potential for a remote code execution chain. Exploitation requires combining this bug with additional vulnerabilities.
- **Affected Products:** Google Android 16 (AOSP), CrabbyAVIF package (AVIF parser/decoder)
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** No public proof-of-concept or weaponized exploit exists. The issue was caught before release and mitigated by Android's Scudo hardened allocator. No public PoC is available.
- **Patch Available:** Yes — patched in the Android Security Bulletin published 2025-08-01 (security patch level 2025-08-05). Code fix commit: https://android.googlesource.com/platform/external/rust/crabbyavif/+/87124e11e14f2f6fed75d57f5723ddab37cd4bff. Advisory: https://source.android.com/docs/security/bulletin/2025-08-01
- **Active Exploitation:** No confirmed active exploitation in the wild. The Google Security Blog post characterizes this as a 'near-miss' that was caught before release and was further disrupted by Android's Scudo allocator mitigations. SentinelOne's vulnerability database lists 'Known Exploited: No'. Feedly's CVE database reports 'No evidence of proof of exploitation at the moment'.
- **Threat Actors:** None known
- **Mitigation:** Apply the Android Security Bulletin 2025-08-01 patch level (2025-08-05 or later). The vulnerability was also disrupted at runtime by Android's Scudo hardened allocator. General hardening: continue adopting memory-safe languages (Rust) for new Android code, audit unsafe blocks for bounds-check correctness, and keep Android devices on current security patch levels.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is an attack vector in which an adversary plants hidden malicious instructions inside external data sources (e.g., emails, documents, calendar invites, web pages) that are later retrieved and processed by an AI assistant. Because the LLM cannot reliably distinguish user-supplied instructions from instructions present in third-party content, the injected instructions can override the user's intent and cause the assistant to exfiltrate sensitive data, delete/modify content (such as calendar events), invoke tools/plugins, or perform other unauthorized actions. The attack is unauthenticated at the AI layer (network reachable) and requires only that the victim's AI process the attacker-controlled content, making it the generative-AI analogue of traditional content-borne attacks.
- **Affected Products:** Google Gemini app, Gemini in Google Workspace (including Gmail, Google Calendar, Google Docs integration), and Gemini 2.5 models
- **CVSS Score:** 9.3
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes. Public proof-of-concept exploits exist for the broader class of indirect prompt injection attacks against generative AI systems. The blog specifically cites 'EchoLeak' (CVE-2025-32711), a 0-click indirect prompt injection and image-rendering exfiltration PoC disclosed by Aim Labs researchers against Microsoft 365 Copilot, as a real-world example of the attack class. Sources: https://nvd.nist.gov/vuln/detail/cve-2025-32711 ; https://checkmarx.com/zero-post/echoleak-cve-2025-32711-show-us-that-ai-security-is-challenging/
- **Patch Available:** Yes — Google states these defenses are being actively deployed across Gemini. Specifically, the Gemini 2.5 model family has been hardened through adversarial training, and the content classifiers, thought reinforcement, markdown/URL sanitization, HITL confirmation framework, and user-facing mitigation notifications are integrated into Gemini in Workspace and the Gemini app. Advisory URL: http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html
- **Active Exploitation:** The Google Security Blog post itself does not report confirmed in-the-wild exploitation of Gemini. However, the broader indirect-prompt-injection class has been actively exploited against AI assistants in the wild. Independent reporting includes: (1) Unit 42 (Palo Alto Networks) — observed web-based indirect prompt injection in the wild targeting AI agents with impacts including data exfiltration, unauthorized transactions, and SEO/phishing manipulation (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/); (2) 0din — documented 'Phishing for Gemini' indirect prompt injection via hidden white-text email instructions that hijack Gemini in Workspace summaries to deliver fake Google support pages (https://0din.ai/blog/phishing-for-gemini); (3) Miggo — semantic attack against Google Gemini via weaponized calendar invites enabling a calendar authorization bypass (https://www.miggo.io/post/weaponizing-calendar-invites-a-semantic-attack-on-google-gemini). No CVE is assigned to the Google blog post itself.
- **Threat Actors:** None known
- **Mitigation:** Google recommends a layered defense strategy applied inside Gemini rather than a single fix: (1) Prompt-injection content classifiers — proprietary ML models that detect and filter malicious instructions embedded in emails, files, and other processed content; (2) Security thought reinforcement — targeted system-level instructions that remind the LLM to follow the user's request and ignore adversarial instructions; (3) Markdown sanitization and suspicious-URL redaction — strips/blocks external image renders and rewrites suspicious links using Google Safe Browsing; (4) User confirmation framework ('Human-In-The-Loop') — requires explicit user confirmation before the assistant takes risky actions such as deleting calendar events; (5) End-user security mitigation notifications — contextual banners and help-center links shown to users when an attack has been detected/blocked. Supporting practices: AI red-teaming, adversarial evaluation, threat modeling, and alignment with Google's Secure AI Framework (SAIF).
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors exploit known CVEs in network edge devices (routers, VPNs, firewalls) through chained vulnerabilities for initial access (e.g., CVE-2023-46805+CVE-2024-21887 on Ivanti; CVE-2023-20198+CVE-2023-20273 on Cisco IOS XE; CVE-2024-3400 on Palo Alto GlobalProtect), then pivot via trusted interconnections, maintain persistence by modifying ACLs and installing SSH keys, harvest credentials/traffic via packet capture and protocol mirroring, and evade detection by clearing logs and using virtualized containers. MITRE ATT&CK techniques observed: T1190, T1068, T1199, T1095, T1027, T1562.004, T1071, T1571, T1572, T1048.003.
- **Affected Products:** Cisco IOS XE Software (web UI feature enabled, fixed in 17.9.4a, 17.6.6a, 17.3.8a, 16.12.10a), Cisco IOS XR Software (NCS 540, 560, 5500, 5700 Series with hybrid IPv4 ACL configured, fixed in 7.11.2), Ivanti Connect Secure (9.x, 22.x), Ivanti Policy Secure (9.x, 22.x, fixed in 9.1R14.5, 9.1R17), Palo Alto Networks PAN-OS with GlobalProtect enabled (PAN-OS 11.1: < 11.1.0-h3, < 11.1.1-h1, < 11.1.2-h3; PAN-OS 11.0: < 11.0.0-h3 through < 11.0.4-h1; PAN-OS 10.2: < 10.2.0-h3 through < 10.2.9-h1); additionally targeted vendors include Fortinet firewalls, Juniper firewalls, Microsoft Exchange, Nokia routers/switches, Sierra Wireless devices, and SonicWall firewalls
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS vector unavailable. Individual CVE vectors: CVE-2023-20198: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H (10.0); CVE-2023-20273: CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H (7.2); CVE-2024-3400: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H (10.0); CVE-2025-20144: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:N/I:L/A:N (4.0); CVE-2023-46805: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N (8.2); CVE-2024-21887: CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H (9.1).
- **Exploit Available:** Yes — Public exploits and weaponized exploitation confirmed for all referenced CVEs. All CVEs are in CISA's Known Exploited Vulnerabilities (KEV) Catalog. GreyNoise observed 110+ malicious IPs exploiting CVE-2023-20198 (Feb 2025); Recorded Future documented RedMike (Salt Typhoon) exploiting Cisco devices Dec 2024–Jan 2025. Source URLs: https://www.greynoise.io/blog/greynoise-observes-active-exploitation-of-cisco-vulnerabilities-tied-to-salt-typhoon-attacks ; https://www.recordedfuture.com/research/redmike-salt-typhoon-exploits-vulnerable-devices
- **Patch Available:** Yes — Official vendor patches exist for all referenced CVEs. Cisco IOS XE (CVE-2023-20198/CVE-2023-20273): fixed in 17.9.4a, 17.6.6a, 17.3.8a, 16.12.10a — https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxe-webui-privesc-j22SaA4z. Cisco IOS XR (CVE-2025-20144): fixed in 7.11.2 — https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ncs-hybridacl-crMZFfKQ. Ivanti (CVE-2023-46805/CVE-2024-21887): patched in Connect Secure 9.1R14.5, 9.1R17, 22.x — https://forums.ivanti.com/s/article/CVE-2023-46805-Authentication-Bypass-CVE-2024-21887-Command-Injection-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure-Gateways. Palo Alto PAN-OS (CVE-2024-3400): fixed in 10.2.9-h1, 11.0.4-h1, 11.1.2-h3, and later — https://security.paloaltonetworks.com/CVE-2024-3400
- **Active Exploitation:** Yes — Confirmed active exploitation in the wild. CISA AA25-239A (Sep 3, 2025): global malicious operations active since at least 2021 targeting telecommunications, ISPs, lodging, transportation, and military infrastructure. GreyNoise (Feb 24, 2025): 110+ malicious IPs exploiting CVE-2023-20198; Salt Typhoon used CVE-2023-20198+CVE-2023-20273 to compromise 5 telecom networks Dec 2024–Jan 2025. Recorded Future (Feb 13, 2025): RedMike (Salt Typhoon) exploited Cisco telecom devices Dec 2024–Jan 2025. Cisco Talos (Feb 20, 2025): Salt Typhoon gained initial access to telecoms via legitimate login credentials after exploiting CVEs. CISA KEV Catalog: all CVEs listed as actively exploited. Note: AA25-239A states "Exploitation of zero-day vulnerabilities has not been observed to date" — exploitation relies on known n-day CVEs. Sources: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a ; https://www.greynoise.io/blog/greynoise-observes-active-exploitation-of-cisco-vulnerabilities-tied-to-salt-typhoon-attacks ; https://www.recordedfuture.com/research/redmike-salt-typhoon-exploits-vulnerable-devices ; https://cyberscoop.com/cisco-talos-salt-typhoon-initial-access/
- **Threat Actors:** Salt Typhoon (also tracked as RedMike, OPERATOR PANDA, UNC5807, GhostEmperor) — PRC state-sponsored cyber threat actors
- **Mitigation:** Prioritize patching edge devices per CISA KEV Catalog; audit network device configurations against authorized baselines; review remote access, ACLs, and transport protocols; audit for unexpected GRE/tunneling, external IPs in TACACS+/RADIUS/ACLs, unauthorized packet capture/mirroring, or unexpected virtual containers; implement change-management; disable unnecessary management interfaces (e.g., Cisco IOS XE Web UI); enforce MFA on all administrative access; for CVE-2025-20144 remove duplicate ACEs until ≤31 identical entries across object groups; apply vendor patches per individual CVE advisories.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Campaign-level TTPs: spearphishing and reconstituted password-spraying credential attacks; advisory provides IOCs/STIX for detection. (Campaign-level threat, not a single-vulnerability exploit chain.)
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit for a specific software vulnerability reported; industry emulation/assessment templates (AttackIQ) exist to emulate the actor's TTPs.
- **Patch Available:** No vendor patch — advisory describes an active threat campaign (not a discrete, patchable software vulnerability).
- **Active Exploitation:** Yes — CISA/FBI report active targeting of Western logistics entities and technology companies (ongoing campaign reported since 2022).
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) — 85th Main Special Service Center (Unit 26165).
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 10. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

**Parallel AI Enrichment:**

- **Technical Details:** The blog post is a thought-leadership article rather than a vulnerability-specific advisory. It discusses general browser attack mechanisms: exploitation of rendering logic, JavaScript execution, document handling, and memory safety weaknesses, followed by sandbox escape and privilege escalation in an exploit chain. It also references phishing, credential theft, malicious downloads, session hijacking, clickjacking, cross-site scripting, HTML smuggling, and web-based social engineering as browser-mediated attack paths.
- **Affected Products:** Chromium-based browsers (general; no specific products or versions identified)
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No specific PoC or weaponized exploit is referenced in this blog post.
- **Patch Available:** Patch availability not applicable. The blog post does not reference a specific vulnerability or vendor patch.
- **Active Exploitation:** No specific active exploitation is reported in this blog post. It cites general context from the CrowdStrike 2026 Global Threat Report (42% of vulnerabilities exploited pre-disclosure) and the Verizon 2026 DBIR (vulnerability exploitation surpassed stolen credentials as the top breach entry point in 2025).
- **Threat Actors:** None known
- **Mitigation:** The blog recommends a defense-in-depth browser security strategy rather than relying on patching alone. CrowdStrike promotes Falcon Secure Access, which uses JavaScript Language Randomization (JSLR) — a moving-target defense that continuously randomizes the browser's JavaScript runtime environment to make zero-day exploitation harder. The solution also blocks phishing and adversary-in-the-middle techniques, protects session tokens against hijacking and MFA bypass, and prevents credential theft and data exfiltration at the point of execution, extending coverage to managed and unmanaged devices.
- **Vendor Advisory:** https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/

---

## 11. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 12. 🟠 Zero-Day — Google, FBI Disrupt NetNut Residential Proxy Network Powered by Millions of Devices

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-03
**Reference:** <https://www.securityweek.com/google-fbi-disrupt-netnut-residential-proxy-network-powered-by-millions-of-devices/>

> NetNut rented access to millions of compromised devices, allowing cybercriminals and nation-state actors to mask their identities during attacks. The post Google, FBI Disrupt NetNut Residential Proxy Network Powered by Millions of Devices appeared first on SecurityWeek .

---

## 13. 🟡 High Severity — 9router has an Incomplete Fix: Local-Only Access Gate Bypass in 9router via Host Header SpoofING

**CVE:** `CVE-2026-49353` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-6g2f-w7g3-77vf>

> ## Summary

The fix for CVE-2026-46339 (unauthenticated RCE via unprotected MCP plugin routes) introduced a local-only access gate in `src/dashboardGuard.js` that restricts spawn-capable routes (`/api/mcp/*`, `/api/tunnel/*`, `/api/cli-tools/*`) to loopback requests. The gate determines &quot;local&quot; by inspecting the `Host` and `Origin` HTTP headers rather than the TCP source address. When 9r…

---

## 14. 🟡 High Severity — 9router's Hardcoded Default fallback JWT Secret  Allows Authentication Bypass

**CVE:** `CVE-2026-49352` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-jphh-m39h-6gwx>

> ### Summary
9router uses a publicly known hardcoded string `&quot;9router-default-secret-change-me&quot;` as the fallback of JWT secret for all Dashboard session JWTs when the `JWT_SECRET` environment variable is not set. Because this secret is committed in the public repository and unchanged across all releases, any unauthenticated remote attacker can forge a valid `auth_token` cookie and gain fu…

---

## 15. 🟡 High Severity — LaunchServer FileServerHandler has an unauthenticated path traversal issue

**CVE:** `CVE-2026-54617` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-5g75-477j-2c2f>

> ### Summary
An unauthenticated path traversal in the LaunchServer HTTP file server (`FileServerHandler`) lets any remote actor read **any file** readable by the LaunchServer process (e.g. `../../../../etc/passwd`). This is a generic arbitrary-file-read primitive, so the fix must address the traversal itself, not any specific file.

The readable files include the server&#x27;s own secrets, which tu…

---

## 16. 🟡 High Severity — Algernon vulnerable to server-side script source disclosure on Windows via NTFS filename

**CVE:** `CVE-2026-52792` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-mm6c-5j6x-hq8m>

> ### Summary

Algernon selects its file handler from `filepath.Ext()` (engine/handlers.go:134), which does not treat the NTFS-equivalent names `x.lua::$DATA`, `x.lua.`, or `x.lua ` as `.lua`. On Windows, an unauthenticated client appends one of these suffixes to any server-side script on a public path and receives its raw source instead of executed output, leaking embedded secrets such as database …

---

## 17. 🟡 High Severity — Steeltoe: OAEP setting silently selects PKCS#1 v1.5 padding

**CVE:** `CVE-2026-50268` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-4j9m-h44m-2hv8>

> ### Summary

Configuring `encrypt:rsa:algorithm=OAEP` does not enable OAEP encryption. Due to an incorrect BouncyCastle transformation string, the `OAEP` setting selects PKCS#1 v1.5, which is the same algorithm as the `DEFAULT` setting.

### Impact

Operators who configure `encrypt:rsa:algorithm=OAEP` to obtain CCA2-secure padding receive PKCS#1 v1.5 instead. Currently, `Decrypt()` is called only …

---

## 18. 🟡 High Severity — Steeltoe's static JWKS cache shared across schemes and never invalidated

**CVE:** `CVE-2026-50202` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-7fqc-p256-7pwj>

> ### Summary

The JWT signing key cache in `TokenKeyResolver` uses `kid` as the sole cache key without namespacing by authority. In applications with multiple `JwtBearer` schemes pointing to different identity providers, a key fetched for one scheme can satisfy token validation for another. Additionally, cached keys have no expiration, so rotated or revoked keys remain trusted until the application…

---

## 19. 🟡 High Severity — Steeltoe's env sanitizer misses connection strings — leaks embedded DB passwords

**CVE:** `CVE-2026-50200` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-q62h-354g-5r85>

> ### Summary

The `Sanitizer` component in the Environment actuator redacts configuration values by matching the configuration key name against a suffix list. The default list (`password`, `secret`, `key`, `token`, `.*credentials.*`, `vcap_services`) does not cover the standard .NET pattern `ConnectionStrings:&lt;name&gt;` or Steeltoe Connectors&#x27; `Steeltoe:Client:&lt;type&gt;:Default:Connectio…

---

## 20. 🟡 High Severity — SimpleSAMLphp HTTP-Artifact TLS validator confusion allows cross-IdP authentication bypass

**CVE:** `CVE-2026-49283` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-6929-8p9f-26jx>

> ## Summary

SimpleSAMLphp&#x27;s HTTP-Artifact receive path can treat an unsigned embedded SAML `Response` as cryptographically valid for the wrong IdP.

In the `HTTPArtifact::receive()` flow, the SOAP `ArtifactResponse` receives a TLS-based validator from `SOAPClient::addSSLValidator()`. The embedded SAML `Response` then receives a validator that delegates signature validation to that outer `Arti…

---

## 21. 🟡 High Severity — Linuxfabrik Monitoring Plugins: Sudoers may be able to obtain privilege escalation via /usr/bin/apt-get arguments

**CVE:** `CVE-2026-52817` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-8w6w-23mq-h8rg>

> ### Summary
In the [Debian.sudoers](https://github.com/Linuxfabrik/monitoring-plugins/blob/main/assets/sudoers/Debian.sudoers) file, `apt-get` is allowed for the nagios user. The full command including the arguments are not enforced and can therefore be choosen arbitrarily. This allows to easily get a root shell as the nagios user:

### PoC
By choosing a particular argument, you can get (as a nagi…

---

## 22. 🟡 High Severity — zebrad has persistent on-disk corruption of Sapling/Orchard subtree roots after chain fork via pop_tip

**CVE:** `CVE-2026-52733` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-2gf8-q9rr-jq3h>

> ### Am I affected

You are affected if:

1. You run `zebrad` up to and including `v4.4.1`.
2. Your node participates in a network where chain forks occur (mainnet, testnet, or any network with multiple miners).

All default configurations are affected. The corruption persists across restarts because it is written to RocksDB.

### Summary

When `pop_tip` removes the tip block during a chain fork, s…

---

## 23. 🟡 High Severity — Mautic vulnerable to Path Traversal via Campaign Import

**CVE:** `CVE-2026-9559` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-6r9h-4h75-7q4x>

> ### Summary
A path traversal vulnerability exists in the campaign import feature of Mautic 7. When extracting uploaded ZIP files during campaign imports, a flaw in the validation logic allows file paths to escape the intended temporary directories. 

### Impact
An authenticated user with campaign import privileges (`campaign:imports:create`) can write arbitrary PHP files to sensitive system direct…

---

## 24. 🟡 High Severity — Mautic has Server-Side Template Injection (SSTI) in Theme Templates

**CVE:** `CVE-2026-9558` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-9fx4-7cmj-47vg>

> ### Summary
A Server-Side Template Injection (SSTI) vulnerability exists in Mautic&#x27;s theme engine. The platform renders uploaded Twig templates without a sandbox or strict function restrictions. Authenticated users with permissions to create or upload themes can abuse this to execute arbitrary code.

### Impact
An authenticated user with theme upload and creation privileges can bypass boundar…

---

## 25. 🟡 High Severity — Mautic Focus component Vulnerable to SSRF

**CVE:** `CVE-2026-9557` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-jmv8-8j9j-rcpc>

> ### Summary
A Server-Side Request Forgery (SSRF) vulnerability exists in the Mautic Focus component (`MauticFocusBundle`). Under certain conditions, insufficiency in validating user-supplied URLs allows authenticated users to trigger outbound HTTP requests from the hosting server.

### Impact
An authenticated user with access to the Mautic panel can exploit this vulnerability to perform internal p…

---

## 26. 🟡 High Severity — zebrad has mempool transaction admission denial via single-peer inbound queue saturation

**CVE:** `CVE-2026-52732` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-4fc2-h7jh-287c>

> ### Am I affected

You are affected if:

1. You run `zebrad` up to and including `v4.4.1`.
2. Your node accepts inbound P2P connections (`network.listen_addr` is set, which is the default).
3. Your node&#x27;s mempool is active (node is synced near the chain tip).

All default configurations are affected.

### Summary

A single unauthenticated P2P peer can monopolize all 25 inbound mempool downloa…

---

## 27. 🟡 High Severity — Dragonfly Manager OAuth provider client_secret disclosure via unauthenticated GET /api/v1/oauth

**CVE:** `CVE-2026-49254` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-4q9j-6299-gxmr>

> ### Summary

The Dragonfly Manager exposes `GET /api/v1/oauth` and `GET /api/v1/oauth/:id` to unauthenticated clients. The response body deserializes the entire `manager/models.Oauth` struct, which includes the `client_secret` field. Any network-reachable attacker can read the OAuth client secrets configured for `github` or `google` providers, defeating the confidentiality guarantee of those secre…

---

## 28. 🟡 High Severity — joserfc: HS256/HS384/HS512 verify accepts empty/nil HMAC key (cross-language sibling of CVE-2026-45363)

**CVE:** `CVE-2026-49852` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-gg9x-qcx2-xmrh>

> ### Summary

`joserfc.jwt.decode` accepts attacker-forged HMAC-signed tokens when the
caller-supplied verification key is the empty string or `None`.
`HMACAlgorithm.sign` and `HMACAlgorithm.verify` in
[`src/joserfc/_rfc7518/jws_algs.py:62-70`](https://github.com/authlib/joserfc/blob/1ddca8f3c73ff47e3bc3ac06cb0c08a9535677ec/src/joserfc/_rfc7518/jws_algs.py#L62-L70) feed whatever
`OctKey.get_op_key(…

---

## 29. 🟡 High Severity — Craft CMS: Authorization bypass in `entries/move-to-section` via missing target-section save check

**CVE:** `CVE-2026-50280` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-43cq-c2gq-pfpw>

> ### Summary

The `EntriesController::actionMoveToSection()` endpoint checks only whether the current user can view the destination section, but it does not require permission to save entries into that section. A low-privileged authenticated control-panel user who can move an entry out of its current section can therefore move that entry into a different section where they have read access but no w…

---

## 30. 🟡 High Severity — Ransomware Groups Turn to Citrix Bleed 2, BYOVD, and Supply Chain Credentials

**CVE:** `CVE-2025-5777` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://thehackernews.com/2026/07/ransomware-groups-turn-to-citrix-bleed.html>

> Threat actors associated with the Anubis ransomware operation have been observed exploiting the Citrix Bleed 2 (CVE-2025-5777) vulnerability to obtain initial access.

&quot;Although tactics differ between affiliates, common patterns emerged in tradecraft through use of legitimate Remote Management and Monitoring (RMM) tooling, credential access, and hands-on-keyboard procedures used for lateral

---

## 31. 🟡 High Severity — Langroid: Path traversal in the file tools allows read/write outside configured current directory

**CVE:** `CVE-2026-50181` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-fg23-3346-88f5>

> ### Summary

Langroid&#x27;s `ReadFileTool` and `WriteFileTool` appear to treat `curr_dir` as the intended working-directory boundary for file operations. However, the tools only change the process working directory to `curr_dir` and then operate on the user-supplied `file_path` without resolving and enforcing that the final path remains inside `curr_dir`.

As a result, a tool caller can supply pa…

---

## 32. 🟡 High Severity — Kerberos Hub private key (X-Kerberos-Hub-PrivateKey) leaked to cross-host redirect target due to redirect-following HTTP client without CheckRedirect

**CVE:** `CVE-2026-50192` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-h5gx-45rj-2h5j>

> ### Summary

The Kerberos Hub upload path sends the agent&#x27;s Hub credentials in the custom `X-Kerberos-Hub-PrivateKey` and `X-Kerberos-Hub-PublicKey` request headers to the operator-configured Hub URL (`config.HubURI`). The HTTP client used (`&amp;http.Client{}` in `UploadKerberosHub`) is constructed without a `CheckRedirect` policy, so it follows HTTP redirects automatically. Go&#x27;s `net/h…

---

## 33. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
