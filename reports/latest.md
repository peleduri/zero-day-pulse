# Zero Day Pulse

> **Generated:** 2026-07-09 14:31 UTC &nbsp;|&nbsp; **Total:** 31 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 16 &nbsp;|&nbsp; 🟡 High: 15 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal'). SimpleHelp remote support software v5.5.7 and earlier contains multiple unauthenticated path traversal flaws accessible via crafted HTTP requests. A remote, unauthenticated attacker can use directory-traversal sequences (e.g., '..') in URL/request parameters to download arbitrary files from the SimpleHelp host, including the server configuration file. The configuration file contains secrets and hashed user/technician passwords; an attacker who retrieves this file can attempt to crack the hashes (or use the stolen secrets directly) to obtain administrator access, then abuse the RMM console to enumerate and pivot into downstream customer networks and deploy ransomware.
- **Affected Products:** SimpleHelp Remote Support / Remote Monitoring and Management (RMM) software, versions 5.5.7 and all earlier releases. Three related CVEs were patched together: CVE-2024-57726, CVE-2024-57727, and CVE-2024-57728. Patched versions: v5.5.8 (or later), v5.4.10, and v5.3.9.
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true. A public proof-of-concept is available at https://github.com/imjdl/CVE-2024-57727 (imjdl/CVE-2024-57727, 15 stars / 1 fork) containing a poc.py script demonstrating unauthenticated path traversal. A weaponized video demonstration is also published at https://www.youtube.com/watch?v=RU1N1WBSJIU.
- **Patch Available:** true. SimpleHelp released patches within two days of being notified. Affected fixed versions are SimpleHelp v5.5.8 (or later), v5.4.10, and v5.3.9. Vendor advisory: https://guides.simple-help.com/kb---security-vulnerabilities-01-2025 (companion blog: https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know). CISA added CVE-2024-57727 to the Known Exploited Vulnerabilities (KEV) Catalog on 2025-02-13 with a remediation due date of 2025-03-06.
- **Active Exploitation:** true. CISA confirmed active exploitation in advisory AA25-163A (June 12, 2025): ransomware actors, assessed with high confidence to be DragonForce, leveraged CVE-2024-57727 against unpatched SimpleHelp RMM instances operated by an MSP to compromise a utility billing software provider and its downstream customers, achieving double-extortion compromise. Sophos independently confirmed exploitation of CVE-2024-57726/57727/57728 by DragonForce against MSP customers in May 2025, with the RMM used for enumeration and ransomware deployment. Exploitation has been observed since at least January 2025. Sources: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a ; https://www.sophos.com/en-us/blog/dragonforce-actors-target-simplehelp-vulnerabilities-to-attack-msp-customers
- **Threat Actors:** DragonForce ransomware operators (Ransomware-as-a-Service group first observed in 2023). Per CISA advisory AA25-163A (June 12, 2025) and Sophos incident reporting, DragonForce actors have exploited unpatched SimpleHelp RMM instances to compromise downstream MSP customers since January 2025, deploying DragonForce ransomware across victim environments.
- **Mitigation:** 1) Upgrade SimpleHelp server immediately to v5.5.8 or later (or apply the v5.4.10 / v5.3.9 patched releases). 2) If unable to patch immediately, isolate the SimpleHelp server from the internet or stop the server process. 3) After upgrading, change all SimpleHelp Administrator and Technician passwords and rotate any credentials/secrets that were stored on the SimpleHelp host. 4) Restrict IP addresses allowed to reach Technician/Administrator logins; disable the default 'SimpleHelpAdmin' user; disable local Technician logins in favor of third-party authentication (Active Directory/LDAP). 5) Regenerate API tokens and restrict API request source IPs. 6) Place the SimpleHelp server behind a firewall and enable Server Event alerts for Administrator logins, failed logins, and configuration changes. 7) Threat-hunt for suspicious executables with three-letter alphabetic filenames (e.g., aaa.exe) created after January 2025, and review inbound/outbound traffic from the SimpleHelp server. 8) Maintain clean offline backups and an SBOM; verify vendor security controls for any RMM software in use.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — Unpatched Backdoor in Tenda Firmware Grants Admin Access to Devices

**CVE:** `CVE-2026-11405` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://www.securityweek.com/unpatched-backdoor-in-tenda-firmware-grants-admin-access-to-devices/>

> Tracked as CVE-2026-11405, the vulnerability allows unauthenticated attackers to access a device&#x27;s web management interface. The post Unpatched Backdoor in Tenda Firmware Grants Admin Access to Devices appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** An undocumented authentication backdoor is embedded in the /bin/httpd web server binary of certain Tenda router firmware builds. In the login() function at offset 004c88b8, after the standard MD5-based password check fails, the code retrieves an alternate plaintext password from the device configuration via GetValue("sys.rzadmin.password") and compares it directly against the user-supplied password. Any arbitrary username is accepted when this hidden password matches, and the device immediately issues a session granting role=2 (full administrative) privileges. The backdoor is not documented in any Tenda user-facing material and is invisible in the standard admin UI, so affected owners have no way to detect or disable it through normal interfaces.
- **Affected Products:** Tenda FH1201 firmware US_FH1201V1.0BR_V1.2.0.14(408)_EN_TD; Tenda W15E firmware US_W15EV1.0br_V15.11.0.5(1068_1567_841)_EN_TDE; Tenda AC10 firmware US_AC10V1.0re_V15.03.06.46_multi_TDE01; Tenda AC5 firmware US_AC5V1.0RTL_V15.03.06.48_multi_TDE01; Tenda AC6 firmware US_AC6V2.0RTL_V15.03.06.51_multi_TDE01
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true (https://github.com/ea/nmap-scripts/blob/master/tenda-backdoor.nse)
- **Patch Available:** false
- **Active Exploitation:** true (confirmed in the wild by CERT/CC VU#213560, BleepingComputer, The Hacker News, Rescana, and SecurityWeek; automated opportunistic scanning is accelerated by the public Nmap NSE PoC)
- **Threat Actors:** None known.
- **Mitigation:** Because no vendor patch is available, CERT/CC recommends: (1) Disable remote web/administrative management on the device to prevent internet exposure of the vulnerable admin interface; (2) Change the default LAN IP address from common ranges (e.g., 192.168.0.1) to reduce opportunistic discovery by automated scanners; (3) Restrict local network exposure by isolating Tenda devices on a separate VLAN or behind a firewall; (4) Monitor for unexpected logins, configuration changes, or sys.rzadmin.password values on managed devices; (5) Consider replacing affected Tenda routers with patched alternatives from another vendor.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is a vulnerability class affecting LLM-based applications that consume untrusted external content. An attacker plants malicious natural-language instructions inside a data source that an AI agent ingests indirectly (e.g., a webpage, email, shared document, Calendar invite, image, or RAG corpus entry). Because the LLM cannot reliably distinguish system instructions from data, it treats the attacker-supplied text as commands, causing it to deviate from the user's intent. Documented impacts include: silent data exfiltration via crafted image/URL tags that trigger outbound HTTP requests with sensitive context (GeminiJack exfiltrated Gmail/Calendar/Docs data through an external image request); manipulation of AI summaries to inject phishing instructions ('Phishing for Gemini' used hidden HTML and <Admin> tags to append fake security warnings); SEO poisoning and traffic redirection; inducing destructive commands (e.g., sudo rm -rf); financial fraud instructions; and content suppression / denial-of-service against AI crawlers. Common obfuscation techniques include payload splitting, adversarial suffixes, multilingual instructions, Base64/emoji encoding, multimodal injection (instructions hidden in images), and visually invisible HTML (white-on-white, font-size:0).
- **Affected Products:** Google Gemini (consumer app), Google Gemini Enterprise, Google Vertex AI Search, Gemini in Workspace (Gmail, Docs, Drive, Chat, Slides), and LLM-based AI assistants/agents generally (including coding assistants such as GitHub Copilot, Cursor, and Claude Code). Specific version numbers are not disclosed by Google; Gemini Enterprise and Vertex AI Search were separated as part of remediation for the GeminiJack issue. EmailGPT (a third-party LLM email assistant) has the related CVE-2024-5184.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true. Public proof-of-concept exploits and weaponized payloads have been published, including: the Noma Labs GeminiJack zero-click exploit (http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability); 0din's 'Phishing for Gemini' PoC using hidden HTML/Admin tags (https://0din.ai/blog/phishing-for-gemini); Forcepoint X-Labs' 10 IPI payloads observed in the wild (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads); and the Atlas prompt-injection PoC (https://github.com/brennanbrown/atlas-prompt-injection-poc).
- **Patch Available:** true. Google has deployed updates to the RAG processing pipeline for Gemini Enterprise to address instruction/content confusion and fully separated Vertex AI Search from Gemini Enterprise in response to the GeminiJack zero-click issue (per Noma Labs disclosure). Google also maintains the AI Vulnerability Reward Program and the secure-AI-agents framework with continuous layered hardening for Workspace with Gemini, documented at https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini and https://security.googleblog.com/2026/04/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections. Note that IPI is an inherent architectural challenge of current LLMs; mitigations are continuously evolving rather than a single discrete patch.
- **Active Exploitation:** true. Google's Threat Intelligence team reports confirmed active in-the-wild exploitation of IPI, citing observed categories of abuse including SEO manipulation, deterring AI agents/crawlers, attempts at data exfiltration, and commands attempting destructive actions (e.g., delete-all-files). Independent corroboration: Forcepoint X-Labs documented 10 verified IPI payloads caught in the wild on 2026-04-22; Noma Labs demonstrated the GeminiJack zero-click exploit leaking Gmail/Calendar/Docs data from Gemini Enterprise; Unit 42 reported web-based IPI attacks against AI ad-checker agents (2026-03-03); Proofpoint (2025-11-18) and 0din (2025-07-10) reported IPI weaponization against AI email assistants.
- **Threat Actors:** None known. The Google Threat Intelligence post and corroborating sources (Noma Labs, Forcepoint X-Labs, OWASP, Unit 42) all describe the attackers generically as 'adversaries', 'multiple actors', or 'threat actors'. No specific APT group, ransomware operator, or named campaign has been publicly attributed to Indirect Prompt Injection (IPI) exploitation as of the report date.
- **Mitigation:** No single patch fully eliminates IPI. Google's published layered defense strategy for Gemini in Workspace combines: (1) purpose-trained prompt-injection content classifiers; (2) 'security thought reinforcement' embedded in the model; (3) Markdown sanitization and suspicious-URL redaction (using Google Safe Browsing); (4) a user-confirmation framework that requires explicit human approval for sensitive actions; (5) end-user security mitigation notifications; and (6) ongoing model adversarial robustness training. OWASP-recommended mitigations include constraining model behavior with strict system prompts, validating output formats with deterministic code, semantic input/output filtering, least-privilege API tokens, human-in-the-loop approval for high-risk actions, content segregation/clear labeling of untrusted data, and regular adversarial/penetration testing. Forcepoint additionally recommends real-time analytics to block known IPI URLs and enforcing a strict data/instruction boundary for AI agents consuming untrusted web content. Workspace admins should also enable Gemini's built-in IPI protections (default in Workspace with Gemini).
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) embeds malicious natural-language instructions into external content (web pages, emails, documents, files) that an LLM ingests during normal operation. The model treats these hidden instructions as commands and executes them alongside the legitimate user task, enabling unauthorized actions (data exfiltration, unauthorized outbound actions, chatbot hijack) without malicious input from the user. Weaponized techniques observed in 2026 include CSS-based concealment (display:none, visibility:hidden, opacity:0, off-screen positioning), HTML-comment hiding, XML/SVG/CDATA encapsulation, system-tag spoofing (e.g., [SYSTEM OVERRIDE]), internal-token spoofing, conditional targeting aimed at AI ('If you are an AI assistant...'), Base64-decoded runtime assembly, canvas-rendered text to evade DOM scanners, and functional-command instructions (e.g., sudo rm -rf, fork bombs) when agents are wired to shells or IDEs.
- **Affected Products:** Workspace with Gemini (umbrella platform). Affected surfaces: standalone Gemini app, Gmail, Docs editors, Drive, Chat. No specific version numbers published (IPI is treated as an evolving threat class).
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true. Weaponized IPI payloads published by Forcepoint X-Labs (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads) and in-the-wild web-based IPI detections documented by Palo Alto Networks Unit 42 (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/).
- **Patch Available:** true. Google reports that enhanced IPI defenses have been deployed in production against the Gemini app and Gemini in Workspace apps, and these protections 'consistently mitigated indirect prompt injection attempts'. IPI is treated as an evolving threat vector rather than a single defect, so updates are delivered continuously. Advisory: http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html.
- **Active Exploitation:** true. Confirmed by: (1) Palo Alto Networks Unit 42, 'Web-Based Indirect Prompt Injection Observed in the Wild', 3 March 2026; (2) Forcepoint X-Labs, '10 Indirect Prompt Injection Payloads Caught in the Wild', 22 April 2026 (financial fraud, data destruction, API-key exfil, AI DoS, SEO hijack, semantic poisoning); (3) Help Net Security, 'Indirect prompt injection is taking hold in the wild', 24 April 2026; (4) Google GTIG open-web sweep of known IPI patterns across live sites.
- **Threat Actors:** APT42 (Iranian state-sponsored), APT41 (Chinese state-sponsored), APT43 (North Korean), DRAGONBRIDGE (Chinese influence-operation), KRYMSKYBRIDGE (Russian influence-operation), Doppelganger (Russian influence-operation), LeakNet Ransomware, and the Raptor Train Botnet, per GTIG/Rescana Feb 2026 reporting.
- **Mitigation:** Google's documented layered defense strategy for Gemini consists of: (1) prompt injection content classifiers that filter suspicious inputs before they reach the model; (2) security thought reinforcement via targeted security instructions in the prompt; (3) markdown sanitization and suspicious URL redaction to neutralize hidden scripts/redirects; (4) a user-confirmation (human-in-the-loop) framework requiring explicit user approval before sensitive AI-generated actions or data exports are executed; (5) end-user security mitigation notifications when a suspected IPI is blocked; and (6) baseline model resilience/adversarial robustness. Additional hardening: treat the Gemini app and Workspace Gemini integration as security-sensitive features, enable the notification/confirmation surfaces in Workspace admin settings, restrict Gemini's scope of tools/data where feasible, and monitor poisoned-content channels (web/email) via Google's IPI classifier outputs.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-0628 is an insufficient policy enforcement (CWE-862) in Chrome's WebView tag used by the Gemini Live in-Chrome side panel. A malicious Chrome extension (with basic permissions, using declarativeNetRequest to modify requests to https://gemini.google.com/app) can inject arbitrary JavaScript/HTML into the privileged Gemini Live panel. Once injected, attacker-controlled code executes inside a privileged browser component, enabling: (1) reading local files/directories, (2) capturing screenshots of any HTTPS page, and (3) silently accessing the camera and microphone without user consent. The bug is a privilege-escalation / WebView policy bypass, not a memory-safety issue. The broader class of indirect prompt injection (IDPI) discussed in the Google Security Blog allows instructions embedded in web content (hidden text, DOM elements, canvas-rendered images, base64 payloads, off-screen content) to be ingested by the AI agent and executed as if they were user/system commands.
- **Affected Products:** Google Chrome for Windows/macOS/Linux prior to 143.0.7499.192, Google Chrome for Android prior to 143.0.7499.192, Google Chrome Extended Stable channel prior to 142.0.7444.265. Component: WebView tag used by Gemini Live in-Chrome side panel (CWE-862).
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Exploit Available:** true. Public PoCs available at https://github.com/fevar54/CVE-2026-0628-POC and https://github.com/sastraadiwiguna-purpleeliteteaming/Dissecting-CVE-2026-0628-Chromium-Extension-Privilege-Escalation (8 public PoCs total per cvefeed.io).
- **Patch Available:** true. Chrome 143.0.7499.192 (Linux/Android), 143.0.7499.192/.193 (Windows/macOS), Extended Stable 142.0.7444.265. Advisory: https://chromereleases.googleblog.com/2026/01/stable-channel-update-for-desktop.html
- **Active Exploitation:** true. Indirect prompt injection (the broader attack class described in the Google Security Blog) has been weaponized in real-world campaigns documented by Unit 42 (e.g., AI ad-review evasion, SEO poisoning, data destruction, review manipulation: https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/). For CVE-2026-0628 specifically, Unit 42 demonstrated a working PoC (camera/mic access, local file read, screenshots) before public GitHub release. CISA KEV does not list CVE-2026-0628, but the exploit is publicly available and trivially reusable.
- **Threat Actors:** None known. No specific threat actor group, APT, or ransomware operator has been publicly attributed to exploiting the WebView tag policy bypass (CVE-2026-0628) or the indirect prompt injection class of vulnerabilities discussed in the Google Security Blog post.
- **Mitigation:** Upgrade Google Chrome to 143.0.7499.192 (or 143.0.7499.193 on Windows/macOS) on desktop and 143.0.7499.192 on Android; upgrade Extended Stable to 142.0.7444.265. Chrome auto-update delivers the fix. Architectural hardening against the broader indirect prompt injection threat (per the Google Security Blog): (1) User Alignment Critic; (2) Agent Origin Sets (Read-only vs Read-writable partitioning); (3) Gating Functions for task-relevant origin access; (4) User Confirmations for sensitive sites (banking, medical) and consequential actions (payments, messaging); (5) Real-time Detection via parallel prompt-injection classifier; (6) Spotlighting (trusted DOM markers prioritizing user/system instructions); (7) Deterministic Checks against URL/sensitive-site allowlists; plus Safe Browsing and on-device scam detection.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html and https://chromereleases.googleblog.com/2026/01/stable-channel-update-for-desktop.html

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2025-48530 is a linear buffer overflow in CrabbyAVIF, the Rust-based AVIF image decoder shipping in Android. In multiple locations within the CrabbyAVIF code, incorrect bounds checks allow out-of-bounds memory accesses (CWE-125). When chained with other bugs, the OOB access can be escalated into remote code execution. The flaw is network-reachable, requires no user interaction, and requires no additional execution privileges. Per Google's November 13, 2025 Security Blog post, this was the first Rust-based memory-safety vulnerability assigned a CVE in Android. Android's Scudo hardened allocator deterministically turned the overflow from silent memory corruption into a noisy crash, helping identify and rendering the issue non-exploitable in practice; the vulnerability never made it into a public Android release.
- **Affected Products:** Google Android 16.0 (System component, platform/external/rust/crabbyavif)
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the August 2025 Android Security Bulletin security patch (2025-08-05 or later) immediately to all Android 16.0 devices. Until patches are deployed, limit network exposure of affected Android devices, implement network segmentation, apply strict firewall rules to control inbound network traffic, and consider using mobile device management (MDM) solutions to enforce patch deployment.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: an attacker embeds hidden malicious natural-language instructions inside external content (e.g., email body in Gmail, Google Doc, Calendar invite, image retrieved from a URL, or content fetched from a third-party website). When the user later invokes Gemini to process that content, the hidden instructions cause the model to deviate from the user's intent — for example, exfiltrating sensitive context (user data, prior chat content) to an attacker-controlled URL, rendering an external image to leak data via request URLs, or executing other rogue actions. Google distinguishes this from direct prompt injection and notes that URL-based and image-rendering ('EchoLeak'-style) exfiltration are representative attack patterns, while stating that the specific EchoLeak rendering vector is not applicable to Gemini.
- **Affected Products:** Google Gemini family — Gemini in Google Workspace, the Gemini app, and Gemini 2.5 models. Adjacent data surfaces referenced as injection vectors: Gmail, Google Docs, Google Calendar. No specific vulnerable build versions are published; the post frames this as a class of attack against Gemini-class LLMs.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true. Public PoCs include SafeBreach Labs' Gemini voice-assistant indirect prompt-injection exploit (https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/), EmbraceTheRed's Gemini memory-persistence prompt-injection PoC (https://embracethered.com/blog/posts/2025/gemini-memory-persistence-prompt-injection/), and the publicly disclosed EchoLeak (CVE-2025-32711) zero-click rendering exfiltration (https://nvd.nist.gov/vuln/detail/cve-2025-32711), which Google cites as an attack-class example.
- **Patch Available:** false. This post is a defense-strategy advisory, not a CVE-specific patch bulletin. The built-in mitigations (model hardening in Gemini 2.5, prompt-injection classifiers, Safe Browsing URL checks, HITL confirmations, and end-user notifications) are described as deployed/ongoing rather than as a discrete version-patch. No specific patched-version URL is published. Reference: https://blog.google/security/mitigating-prompt-injection-attacks/
- **Active Exploitation:** false. The Google Security Blog post does not report confirmed in-the-wild exploitation of Google Gemini or Google Workspace products. It explicitly states that the EchoLeak (CVE-2025-32711) zero-click rendering exfiltration vector is not applicable to Gemini. Public prompt-injection research (SafeBreach, EmbraceTheRed) demonstrates proof-of-concept exploitation against Gemini-class systems, but these are vendor/research disclosures rather than reports of mass in-the-wild attacks.
- **Threat Actors:** None known. This Google Security Blog post discusses indirect prompt injection as a general attack class and does not attribute exploitation to any specific APT group, ransomware operator, or named threat-actor campaign. CVE-2025-32711 ('EchoLeak') is referenced only as a contextual example affecting Microsoft 365 Copilot, not Google Gemini.
- **Mitigation:** Google describes a layered (defense-in-depth) strategy applied across the Gemini prompt lifecycle: (1) model hardening via adversarial training in Gemini 2.5; (2) proprietary prompt-injection content classifiers for inputs and outputs; (3) 'security thought reinforcement' to condition the model against adversarial instructions; (4) markdown sanitization and suspicious-URL detection/redaction integrated with Google Safe Browsing to block known-malicious destinations; (5) a user-confirmation / Human-In-The-Loop framework requiring explicit approval for sensitive or irreversible actions; (6) end-user security-mitigation notifications linking to Help Center guidance. Google also recommends adversarial red-teaming (BugSWAT), the Google AI Vulnerability Reward Program (VRP), the Secure AI Framework (SAIF), and continued threat-intelligence collaboration (GTIG).
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html (canonical: https://blog.google/security/mitigating-prompt-injection-attacks/)

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors are conducting a global cyber-espionage campaign focused on large backbone routers and provider-edge / customer-edge routers of major telecommunications providers, as well as government, transportation, lodging, and military infrastructure. They exploit publicly known CVEs on internet-exposed network-edge devices (Ivanti, Palo Alto GlobalProtect, Cisco IOS XE, Cisco Smart Install) for initial access. After compromise, they modify router configurations to maintain persistent long-term access: adding/modifying Access Control Lists (often named 'access-list 20'), modifying routing tables, enabling traffic mirroring (SPAN/RSPAN/ERSPAN), configuring GRE/IPsec tunnels and static routes, opening standard and non-standard ports (SSH, SFTP, RDP, FTP, HTTP/HTTPS), configuring SSH backdoors and authorized_keys, adding/modifying TACACS+/RADIUS servers and AAA configuration, creating new privileged user accounts, brute-forcing/decrypting Cisco Type 5/7 passwords. They leverage compromised devices and trusted or private interconnections to pivot laterally into other networks, harvesting router configurations, BGP routes, RSVP sessions, MIB data, and MPLS info. They execute privileged commands via SNMP, SSH, and HTTP GET/POST, use virtualized containers (e.g., Guest Shell on Cisco IOS XE/NX-OS) to evade detection, and use tools such as siet.py, map.tcl, tclproxy.tcl, wodSSHServer, and STOWAWAY. They clear local logs and disable log forwarding to avoid detection. Per CISA, exploitation of zero-day vulnerabilities has NOT been observed; the actors are exploiting known vulnerabilities and avoidable weaknesses in internet-exposed devices.
- **Affected Products:** Confirmed targeted/exploited products: Ivanti Connect Secure (9.x, 22.x) and Ivanti Policy Secure; Palo Alto Networks PAN-OS GlobalProtect feature; Cisco IOS XE software and Cisco IOS/IOS XE Smart Install. Additional suspected targets: Fortinet firewalls, Juniper firewalls, Microsoft Exchange, Nokia routers/switches, Sierra Wireless devices, SonicWall firewalls. Specific CVEs cited: CVE-2024-21887 (Ivanti command injection), CVE-2023-46805 (Ivanti authentication bypass), CVE-2024-3400 (Palo Alto PAN-OS GlobalProtect command injection), CVE-2023-20273 (Cisco IOS XE), CVE-2023-20198 (Cisco IOS XE), and CVE-2018-0171 (Cisco Smart Install).
- **CVSS Score:** CVSS score unavailable. AA25-239A is a multi-vendor activity advisory covering a long-running Chinese state-sponsored campaign rather than one specific CVE, so a single CVSS v3.x base score is not applicable. (The individual CVEs it references do have their own published scores — e.g. CVE-2024-3400 has a CVSS of 10.0.)
- **CVSS Vector:** CVSS vector unavailable. AA25-239A is a multi-vendor/activity threat advisory, not a single-vulnerability CVE bulletin; no single CVSS v3 vector applies to the advisory as a whole.
- **Exploit Available:** true — public proof-of-concept code and weaponized exploits exist for the CVEs referenced in the advisory. Examples: GitHub PoC for CVE-2024-3400 (https://github.com/retkoussa/CVE-2024-3400) and Exploit-DB entry 51996 for Palo Alto PAN-OS < v11.1.2-h3 (https://www.exploit-db.com/exploits/51996); public exploit code is also widely available for the Ivanti CVE-2023-46805 / CVE-2024-21887 chain and for the Cisco IOS XE CVEs.
- **Patch Available:** true — vendor patches are available for each of the specific CVEs the campaign exploits: Ivanti KB for CVE-2023-46805 / CVE-2024-21887 (https://hub.ivanti.com/s/article/KB-CVE-2023-46805-Authentication-Bypass-CVE-2024-21887-Command-Injection-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure-Gateways), Palo Alto Networks fixes for CVE-2024-3400 in GlobalProtect-capable PAN-OS versions (per Palo Alto security advisory and NVD entry https://nvd.nist.gov/vuln/detail/cve-2024-3400), and Cisco fixes for CVE-2023-20198 / CVE-2023-20273 / CVE-2018-0171. Refer to the CISA KEV Catalog and each vendor's official advisory for affected version ranges and patched releases. Note: AA25-239A itself is an activity/threat advisory and is not addressed by a single 'advisory patch' — it must be remediated via the combination of vendor patches plus the configuration and monitoring mitigations above.
- **Active Exploitation:** true — confirmed active exploitation in the wild. CISA states: 'Investigations associated with these APT actors indicate that they are having considerable success exploiting publicly known common vulnerabilities and exposures (CVEs) and other avoidable weaknesses within compromised infrastructure.' The June 2025 CISA/FBI joint publication 'Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System' (AA25-239A) and parallel industry reporting (e.g., Picus Security analysis at https://picussecurity.com/resource/blog/cisa-alert-aa25-239a-analysis-simulation-and-mitigation-of-chinese-apts) document active exploitation targeting backbone routers, provider-edge / customer-edge routers, and the listed network-edge devices globally.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor, plus PRC-affiliated commercial entities Sichuan Juxinhe Network Technology Co. Ltd., Beijing Huanyu Tianqiong Information Technology Co., Ltd., and Sichuan Zhixin Ruijie Network Technology Co., Ltd.
- **Mitigation:** Because this is an activity advisory (not a single-vulnerability patch), mitigation centers on hardening, detection, and configuration hygiene rather than applying a single patch: (1) Prioritize patching the cited CVEs (CISA KEV Catalog) on Ivanti Connect Secure / Ivanti Policy Secure, Palo Alto PAN-OS GlobalProtect, and Cisco IOS XE; upgrade unsupported devices to vendor-supported models. (2) Pull current device configurations and compare them against the latest authorized baseline; review remote-access configurations and ACLs (especially any named 'access-list 20') for unauthorized changes. (3) Routinely audit network device logs and configurations for unexpected GRE/IPsec tunneling, external IPs in TACACS+ / RADIUS / ACL lists, unexpected SPAN/RSPAN/ERSPAN traffic-mirroring settings, unexpected virtual containers or commands within containers, and unauthorized privileged accounts. (4) Disable Smart Install on Cisco devices where not required and ensure VTY/console access uses strong, segmented authentication. (5) Implement a robust change-management process with periodic configuration auditing and integrity monitoring. (6) Enforce network segmentation, principle-of-least-privilege for device admin accounts, centralized logging with tamper-evident storage, and disable management interfaces on internet-exposed edge devices.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** The primary vulnerability (CVE-2023-23397) is a Microsoft Outlook Elevation of Privilege / NTLM credential-theft flaw. An attacker sends a specially crafted email containing the extended MAPI property 'PidLidReminderFileParameter' (mapped to the 'ReminderSoundFile' calendar reminder sound property), set to a UNC path pointing to an attacker-controlled SMB server (TCP 445). When Outlook processes this message automatically upon receipt (with no user interaction required), it connects to the remote UNC path to retrieve the 'sound file', forcing the victim's Windows client to perform NTLMv2 authentication against the attacker's server. The attacker captures the leaked NetNTLMv2 hash, which can then be cracked offline or relayed for NTLM authentication against other systems. Additional vulnerabilities exploited include Roundcube Webmail (CVE-2020-12641, CVE-2020-35730, CVE-2021-44026) for webmail server compromise and WinRAR (CVE-2023-38831) for spear-phishing delivery of malicious archives.
- **Affected Products:** Microsoft Outlook for Windows (all supported versions including Outlook 2013, Outlook 2016, Outlook 2019, and Microsoft 365 Apps for Enterprise); Roundcube Webmail (versions affected by CVE-2020-12641, CVE-2020-35730, CVE-2021-44026); WinRAR archive utility (vulnerable to CVE-2023-38831); Corporate VPN appliances (various vendors); Small Office/Home Office (SOHO) routers and devices; IP cameras including Hikvision models (with backdoor string 'YWRtaW46MTEK'); Microsoft Active Directory, Exchange Server, and Windows domain controllers targeted via post-exploitation tooling.
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true - Public PoC available at https://github.com/Trackflaw/CVE-2023-23397. Weaponized exploitation confirmed in CISA AA25-141A.
- **Patch Available:** true - Microsoft released the patch on March 14, 2023 (Patch Tuesday). Patch info: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23397 ; Microsoft MSRC blog: https://www.microsoft.com/en-us/msrc/blog/2023/03/microsoft-mitigates-outlook-elevation-of-privilege-vulnerability
- **Active Exploitation:** true - Confirmed active in-the-wild exploitation by GRU Unit 26165 (APT28) targeting Western logistics entities and technology companies involved in coordinating/transporting/delivering foreign assistance to Ukraine since 2022. Documented in CISA/FBI/Partner Joint Cybersecurity Advisory AA25-141A (published May 21, 2025; last revised April 17, 2026).
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS), military unit 26165 — tracked in the cybersecurity community as APT28, Fancy Bear, IRON TWILIGHT, SNAKEMACKEREL, Swallowtail, Group 74, Sednit, Sofacy, Pawn Storm, STRONTIUM, Tsar Team, Threat Group-4127 (TG-4127), Forest Blizzard, FROZENLAKE, and GruesomeLarch.
- **Mitigation:** Per CISA AA25-141A: (1) Apply the March 14, 2023 Microsoft Outlook security update for CVE-2023-23397, install March 2023 Exchange Server SU to drop PidLidReminderFileParameter, and scan Exchange for malicious messages; (2) Block outbound SMB (TCP 445), NTLM, and LDAPS to external infrastructure; deploy EDR on mail servers and domain controllers; (3) Enforce phishing-resistant MFA (hardware tokens), separate administrative roles, require SSO, and disable NTLM in favor of PKI/certificate authentication; (4) Remove Group Policy Preferences (GPP) passwords from AD, enable account lockout/throttling, and use compromised-password screening; (5) Patch Roundcube and WinRAR; (6) Disable UPnP, P2P, and anonymous access on SOHO routers/IP cameras; disable unused services; enable authenticated RTSP; audit camera accounts; (7) Enable Windows Attack Surface Reduction Rules to block executable content from email and globally-writable directories; monitor schtasks /create /xml, ntdsutil.exe usage, and suspicious edge.exe -headless-new activity.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

**Parallel AI Enrichment:**

- **Technical Details:** The source is general threat-briefing commentary rather than a vulnerability-specific advisory. It describes classes of exploit chains affecting modern browsers that begin with weaknesses in rendering logic, JavaScript execution, document handling, or memory safety, followed by a sandbox escape and privilege escalation. It also enumerates non-zero-day browser-borne attack vectors: phishing, credential theft, malicious downloads, session hijacking/abuse, clickjacking, cross-site scripting (XSS), HTML smuggling, and adversary-in-the-middle techniques that bypass MFA and steal session tokens. The post notes that because many browsers share a Chromium core, a single vulnerability in the shared foundation can produce systemic, cross-browser exposure.
- **Affected Products:** Chromium-based web browsers (no specific versions identified; the source discusses browser classes generically rather than specific products/versions)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** The post argues patching and endpoint controls alone are insufficient and recommends browser-session-layer defenses, specifically: (1) in-session runtime protections such as CrowdStrike Falcon Secure Access that block session-token hijacking and MFA bypass, and (2) JavaScript Language Randomization (JSLR), which continuously randomizes the JavaScript runtime environment to make exploitation harder even before a patch is deployed. No CVE-specific patch or workaround is referenced because no specific CVE is named.
- **Vendor Advisory:** https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/

---

## 11. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 12. 🟠 Zero-Day — CrowdStrike Uncovers New Prompt Injection Techniques

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jul 07, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-uncovers-new-prompt-injection-techniques/>

---

## 13. 🟠 Zero-Day — 12 Million Impacted by Data Breach at Japanese Telco KDDI

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://www.securityweek.com/12-million-impacted-by-data-breach-at-japanese-telco-kddi/>

> Hackers exploited a zero-day vulnerability in a third-party system to access a KDDI email system for ISPs. The post 12 Million Impacted by Data Breach at Japanese Telco KDDI appeared first on SecurityWeek .

---

## 14. 🟠 Zero-Day — GodDamn Ransomware Uses PoisonX Driver to Disable Endpoint Defenses

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://thehackernews.com/2026/07/goddamn-ransomware-uses-poisonx-driver.html>

> Cybersecurity researchers have flagged a new ransomware family called GodDamn that employs the PoisonX kernel driver to neutralize security software as part of its defense evasion strategy.

According to a new report published by the Threat Hunter Team from Symantec, the ransomware was first publicly spotted in the wild on May 21, 2026. It&#x27;s assessed to be a rebrand of the Beast ransomware,

---

## 15. 🟠 Zero-Day — Microsoft patches RoguePlanet Defender zero-day vulnerability

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-rogueplanet-defender-zero-day-vulnerability/>

> Microsoft has released a security patch to address a Defender zero-day vulnerability known as &quot;RoguePlanet,&quot; disclosed after the June 2026 Patch Tuesday. [...]

---

## 16. 🟠 Zero-Day — Designing for the inevitable: System prompt leakage and mitigations in generative AI applications

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** AWS Security Blog &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://aws.amazon.com/blogs/security/designing-for-the-inevitable-system-prompt-leakage-and-mitigations-in-generative-ai-applications/>

> System prompts form the foundation of generative AI applications. A system prompt is a collection of instructions and operational context provided to a large language model (LLM) that shapes how the model behaves and interacts with users and tools. System prompts often contain proprietary information, including role definitions, behavioral guidelines, tool descriptions and usage instructions, […]

---

## 17. 🟡 High Severity — Ruby CSS Parser: SSRF and Local File Disclosure in `CssParser::Parser#read_remote_file`

**CVE:** `CVE-2026-53727` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-9pmc-p236-855h>

> ## Summary

`CssParser::Parser#read_remote_file` (and therefore `load_uri!`, and the `@import`-following branch of `add_block!`) issues HTTP/HTTPS requests against any host, port and URI it is handed, with no scheme allowlist, no host / IP filtering, and no protection against link-local, loopback or RFC‑1918 addresses. `Location:` redirects are followed recursively back into the same function, whi…

---

## 18. 🟡 High Severity — org.hl7.fhir.core: ReDoS via FHIRPath matches()/replaceMatches() in FHIR Validator HTTP Endpoint

**CVE:** `CVE-2026-49485` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-7cmj-v6x8-frvv>

> # Summary
All implementations of FHIRPathEngine accept arbitrary FHIRPath expressions and evaluate them without input validation. The utility intended to secure this evaluation did so incorrectly, and did not fully cover all places in which evaluation was being done. An attacker can send a resource containing an evil regex pattern that causes catastrophic backtracking, exhausting system resources,…

---

## 19. 🟡 High Severity — Soup Sieve: Regular Expression Denial of Service (ReDoS) via Selector Parser

**CVE:** `CVE-2026-49477` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-836r-79rf-4m37>

> ### Summary

The CSS selector parser in soupsieve (the CSS selector engine for Beautiful Soup 4) contains a regular expression vulnerable to catastrophic backtracking. When processing an attribute selector with an unterminated quoted value, the `VALUE` regex pattern in `css_parser.py` enters exponential backtracking. A payload of only **300 bytes** causes the regex engine to hang for **over 3 seco…

---

## 20. 🟡 High Severity — Phantom: Arbitrary file write and decode-bomb DoS via unconfined MCP tool paths

**CVE:** `CVE-2026-37555` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-52vm-mxx8-f227>

> ### Impact

In Phantom &lt;= 1.3.0, when `PHANTOM_OUTPUT_DIR` was unset (the default), the MCP tools accepted arbitrary absolute output paths with no confinement. Anything able to send tool calls (e.g. an AI agent driving the MCP interface) could **write or overwrite arbitrary files** the process user can write — including shell startup files (`~/.zshrc`) or a Reaper `__startup.lua`, which is effe…

---

## 21. 🟡 High Severity — pyLoad: SSRF guard bypass via IPv6 6to4/NAT64 transition wrappers of internal IPs

**CVE:** `CVE-2026-48737` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-m5x5-28jr-gpjj>

> ## Summary

`is_global_address` in [`src/pyload/core/utils/web/check.py`](https://github.com/pyload/pyload/blob/1b12dc7f348db8c144e0f39215680415e90ca4d2/src/pyload/core/utils/web/check.py) is the central guard against SSRF-style outbound connections in pyload-ng. It tests whether a given IP is &quot;globally routable&quot; via Python&#x27;s `ipaddress.ip_address(value).is_global`, and callers trea…

---

## 22. 🟡 High Severity — Microsoft Patches RoguePlanet Defender Flaw That Can Grant SYSTEM Privileges

**CVE:** `CVE-2026-50656` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://thehackernews.com/2026/07/microsoft-patches-rogueplanet-defender.html>

> Microsoft has released security updates for a Defender vulnerability known as RoguePlanet, nearly a month after details of the flaw became public.

The vulnerability, tracked as CVE-2026-50656 (CVSS score: 7.8), is a privilege escalation issue in the Microsoft Malware Protection Engine (&quot;mpengine.dll&quot;), which provides scanning, detection, and cleaning capabilities for its antivirus and

---

## 23. 🟡 High Severity — Serena: Unauthenticated Flask dashboard on fixed port enables DNS rebinding → memory poisoning → RCE

**CVE:** `CVE-2026-49471` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://github.com/advisories/GHSA-37h2-6p4f-mp3q>

> ### Summary

Serena&#x27;s built-in web dashboard exposes an unauthenticated Flask API on a fixed, predictable port (TCP 24282, hardcoded as `0x5EDA` in `constants.py`). The server has no authentication, no CSRF protection, and no Host header validation. A DNS rebinding attack allows a malicious webpage to reach this API from any browser and write arbitrary content to the agent&#x27;s persistent m…

---

## 24. 🟡 High Severity — NL Portal: IDOR allows any authenticated user to complete and tamper with another user's taak

**CVE:** `CVE-2026-49464` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://github.com/advisories/GHSA-6h3c-r723-7fx3>

> ## Impact

In versions from 1.5.0 up to and including 3.0.0, any authenticated portal user could complete and tamper with another user&#x27;s open task by submitting it on their behalf. The task submission endpoint accepted a task ID and a payload, but it never checked whether the task actually belonged to the user making the call.

An attacker who held a valid login (a normal `burger` OAuth token…

---

## 25. 🟡 High Severity — NL Portal: Missing per-user authorization on document and decision GraphQL queries in nl-portal-backend-libraries

**CVE:** `CVE-2026-49463` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://github.com/advisories/GHSA-qpm9-h556-mwxm>

> ## Impact

In versions up to and including 3.0.0, two parts of the GraphQL API returned data without checking whether the data belonged to the logged-in user:

- **Document content.** A logged-in user could download the raw content of any document by its ID, regardless of who owned it. The resolver has lacked an authentication parameter since the initial commit of the project (2022-11-22) — so eve…

---

## 26. 🟡 High Severity — Joro: Unauthenticated Cross-Origin Plugin Upload Leads to RCE

**CVE:** `CVE-2026-53649` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://github.com/advisories/GHSA-xqhv-chqm-fhcc>

> # Unauthenticated Cross-Origin Plugin Upload Leads to RCE (Joro ≤ v1.1.0)

**Severity:** Critical
**CVSS v3.1:** 9.6 (AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H)
**Affected versions:** Joro ≤ v1.1.0, proxy mode (default), Linux/macOS
**Reporter:** cstover
**Date:** 2026-05-27

---

## Summary

Joro&#x27;s default proxy mode (in versions &lt;= 1.1.0) exposes a local API on `127.0.0.1:9090` that performs n…

---

## 27. 🟡 High Severity — DSpace has possible Remote Code Execution (RCE)  through Velocity Templates used by LDN

**CVE:** `CVE-2026-49832` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://github.com/advisories/GHSA-9x82-rm84-c6x7>

> ## Overview

Remote Code Execution (RCE) is possible via Velocity Templates used by DSpace for [COAR Notify/LDN messages](https://wiki.lyrasis.org/spaces/DSDOC9x/pages/379126679/COAR+Notify). _This vulnerability impacts DSpace versions 8.0 &lt;= 8.3, 9.0 &lt;= 9.2._ The attacker MUST already have DSpace administrator credentials in order to perform the attack.

This attack is related to the path t…

---

## 28. 🟡 High Severity — Nuclio: Unsanitized cron trigger event headers/body injected into CronJob shell command leads to persistent RCE

**CVE:** `CVE-2026-52831` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://github.com/advisories/GHSA-v5px-423j-pf7p>

> ## Summary

Nuclio controller builds a `curl` invocation string for each cron trigger and stores it as the `args` of a Kubernetes CronJob container (`/bin/sh`, `-c`, `&lt;command&gt;`). Two fields in the trigger specification flow into this string without adequate sanitization:

- `event.headers` keys — interpolated verbatim inside double-quoted `--header` arguments (`lazy.go:2150`); any key conta…

---

## 29. 🟡 High Severity — async-tar PAX extension-header desync enables tar entry/content smuggling

**CVE:** `CVE-2026-53600` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://github.com/advisories/GHSA-35rm-7j9c-2f7m>

> ## Summary

`async-tar` v0.6.0 mis-applies a buffered PAX `size` extension to an intermediary
extension header (a GNU longname `L`, a GNU longlink `K`, or a PAX `x`/`g`
header) instead of to the next *file* entry. POSIX requires a PAX extended-header
record set to describe the next file entry, never an intervening extension
header. Because `poll_next_raw` (`src/archive.rs`) threads the buffered PA…

---

## 30. 🟡 High Severity — Ubiquiti Patches Critical UniFi Flaws Across Connect, Talk, Access, Protect, and OS

**CVE:** `CVE-2026-50746` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://thehackernews.com/2026/07/ubiquiti-patches-critical-unifi-flaws.html>

> Ubiquiti has shipped updates to address multiple critical security flaws impacting UniFi Connect, UniFi Talk, UniFi Access, UniFi Protect, and UniFi OS that could result in privilege escalation and arbitrary command execution.

The list of vulnerabilities is as follows -


  CVE-2026-50746 (CVSS score: 10.0) - An improper access control vulnerability in UniFi Connect Application that an attacker

---

## 31. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
