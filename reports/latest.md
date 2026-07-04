# Zero Day Pulse

> **Generated:** 2026-07-04 18:56 UTC &nbsp;|&nbsp; **Total:** 12 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 11 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 9

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path traversal (directory traversal) vulnerability in the SimpleHelp web application. It allows unauthenticated remote attackers to craft malicious URLs to read sensitive files from the server, such as system files like /etc/passwd and private SSH keys, by manipulating file path inputs.
- **Affected Products:** SimpleHelp remote support software version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N
- **Exploit Available:** Yes, a public proof-of-concept exists. A Metasploit module 'auxiliary/scanner/http/simplehelp_toolbox_path_traversal' has been developed for this vulnerability, as documented by OffSec (http://offsec.com/blog/cve-2024-57727).
- **Patch Available:** Yes, SimpleHelp has released patches to address this vulnerability. Users are urged to upgrade to the latest version as described in the vendor's security advisory: https://simple-help.com/kb---security-vulnerabilities-01-2025
- **Active Exploitation:** Confirmed active exploitation in the wild has been reported. CISA advisory AA25-163A states that ransomware actors have been targeting organizations using unpatched versions of SimpleHelp RMM since January 2025. The vulnerability was added to CISA's Known Exploited Vulnerabilities (KEV) Catalog on February 13, 2025.
- **Threat Actors:** DragonForce
- **Mitigation:** Update to the latest SimpleHelp version. Additional mitigations include: isolating the SimpleHelp server from the internet or stopping the server process; disabling file browsing functionality or restricting it to trusted users; implementing network-level security controls (firewalls) to limit access to the web interface; and using Symantec DCS Custom sandbox with hardening rules.
- **Vendor Advisory:** https://simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — Unpatched Flaws Disclosed in Filesystem Bundled Into Millions of Embedded Devices

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-03
**Reference:** <https://thehackernews.com/2026/07/unpatched-flaws-disclosed-in-filesystem.html>

> Security firm runZero has disclosed seven vulnerabilities in FatFs, a small filesystem library that lets a device read and write the FAT and exFAT formats used on USB drives and SD cards.

The flaws matter because FatFs is nearly everywhere. It ships inside the firmware that runs security cameras, drones, industrial controllers, hardware crypto wallets, and other devices built on

**Parallel AI Enrichment:**

- **Technical Details:** Seven vulnerabilities were disclosed in the FatFs library, ranging from CVSS 4.6 to 7.6. Key vulnerabilities include: CVE-2026-6682 (integer overflow in FAT32 mount causing memory corruption/RCE); CVE-2026-6687 (stack overflow in exFAT label length field); CVE-2026-6688 (long filename overflow in downstream wrappers); CVE-2026-6685 (unsigned-subtraction wrap in dirty-cache handling causing OOB memory effects); CVE-2026-6683 (exFAT divide-by-zero causing crash/bricking); CVE-2026-6686 (uninitialized cluster exposure leading to info leak); and CVE-2026-6684 (GPT entry-count abuse causing mount-time DoS).
- **Affected Products:** FatFs (versions prior to R0.16 for CVE-2026-6684), Espressif ESP-IDF, STMicroelectronics STM32Cube middleware, Zephyr RTOS, MicroPython, ArduPilot, RT-Thread, Mbed, Samsung TizenRT, SWUpdate
- **CVSS Score:** 7.6
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes, runZero released a companion repository containing proof-of-concept disk images, a test harness, and a working QEMU-based exploit example: https://github.com/runZeroInc/vulns-2026-fatfs-chance
- **Patch Available:** An upstream fix was released in FatFs R0.16 for CVE-2026-6684 (GPT partition-scan loop DoS). For the other six vulnerabilities, there is no upstream fix, and downstream vendors must apply their own patches.
- **Active Exploitation:** As of runZero's July 1, 2026 disclosure, no active exploitation in the wild has been reported.
- **Threat Actors:** None known
- **Mitigation:** Update to FatFs R0.16 to mitigate CVE-2026-6684. For other flaws: audit wrapper code around FatFs, implement strict validation for filenames and file sizes, limit physical access to removable media ports, and monitor for downstream vendor firmware updates.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an AI system processes content—such as websites, emails, or documents—that contains malicious instructions. When the AI reads this poisoned content, it may silently follow the attacker's commands instead of the user's original intent. This is typically operationalized by seeding malicious prompts on public web pages that AI agents are likely to browse.
- **Affected Products:** AI systems and assistants capable of browsing the web, including Gemini
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof-of-concept research and payload lists are available, including resources at https://greshake.github.io/ and the PayloadsAllTheThings repository at https://swisskyrepo.github.io/PayloadsAllTheThings/Prompt%20Injection/.
- **Patch Available:** No single official patch has been released as IPI is a systemic vulnerability class; however, Google is continuously hardening its AI models and products to mitigate these threats.
- **Active Exploitation:** Confirmed active exploitation in the wild. Google's monitoring of the public web via Common Crawl identified a variety of attempts, including malicious destruction, SEO manipulation, and AI agent deterrence. A relative increase of 32% in the malicious category was observed between November 2025 and February 2026.
- **Threat Actors:** None known
- **Mitigation:** Mitigation involves hardening AI models and products, employing a layered defense strategy, and using red-teaming and external research via the AI Vulnerability Reward Program.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an attacker influences an LLM's behavior by injecting malicious instructions into external data or tools (such as emails, calendar invites, or logs) that the LLM processes while completing a user's query.
- **Affected Products:** Google Workspace with Gemini, Gemini app, Gemini in Gmail, Gemini in Docs, Gemini in Drive, Gemini in Chat
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof-of-concept (PoC) research exists, including work by HiddenLayer (https://www.hiddenlayer.com/research/new-gemini-for-workspace-vulnerability-enabling-phishing-content-manipulation), SafeBreach Labs (https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/), and Tenable Research (https://www.tenable.com/security/research/tra-2025-10).
- **Patch Available:** No official single patch is available; Google employs a continuous, layered defense strategy to mitigate the vulnerability.
- **Active Exploitation:** Confirmed active exploitation in the wild has been reported by Forcepoint (identifying 10 payloads) and HelpNet Security.
- **Threat Actors:** None known
- **Mitigation:** Google implements a comprehensive, layered defense strategy to mitigate IPI across Gemini and Workspace applications.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection occurs when an attacker places malicious instructions within web content that are then processed by an AI agent's LLM as legitimate instructions, allowing the attacker to hijack the agent's behavior.
- **Affected Products:** Google Chrome (specifically agentic AI browsing features powered by Gemini)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** A benign proof-of-concept demonstration of indirect prompt injection vulnerabilities in AI-powered browsers is available at http://github.com/brennanbrown/atlas-prompt-injection-poc
- **Patch Available:** Google is introducing a new security architecture featuring layered defenses to block prompt injections, restrict origin access, and prevent unsafe AI actions (see http://security.googleblog.com/2025/12/architecting-security-for-agentic.html).
- **Active Exploitation:** Google identifies indirect prompt injection as the primary new threat facing all agentic browsers, but no specific active exploitation campaigns are reported in the provided advisory.
- **Threat Actors:** None known
- **Mitigation:** Implementation of Google's new security architecture for Chrome, which utilizes layered defenses to block prompt injections, restricts origin access, and prevents unsafe AI actions.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Near-miss linear buffer overflow in the Rust-based CrabbyAVIF component (memory‑corruption via linear buffer overflow in AVIF handling code); blog gives no lower-level exploit primitives or input vectors.
- **Affected Products:** Android platform (first‑party and third‑party/open‑source code); Rust-based CrabbyAVIF component (near-miss)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit reported in the vendor blog or the collected search results.
- **Patch Available:** Vendor states the issue was avoided before shipping (fixes applied before release); vendor advisory (blog post) is the primary reference: http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Continue use of memory‑safe languages (Rust) for new code, reduce unsafe usage, apply vendor updates; the vendor recommends preventive memory‑safety strategy (fuzzing/review) rather than per-issue workarounds.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors target large backbone, provider-edge (PE) and customer-edge (CE) routers and abuse network-edge devices and trusted connections to pivot; they modify router configurations to maintain persistent, long-term access (e.g., persistent configuration/ACL changes and use of compromised devices to pivot).
- **Affected Products:** Cisco, Palo Alto Networks, Ivanti, Fortinet, Juniper, Microsoft Exchange (specific versions unavailable)
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit reported in the supplied corpus; multiple sources state there are no known exploits in the wild.
- **Patch Available:** No official vendor patch or remediation guidance reported in the supplied corpus.
- **Active Exploitation:** CISA and corroborating sources report active targeting/compromise campaigns against networks worldwide, but they also state exploitation of zero-day vulnerabilities has not been observed and there are no known public exploits in the supplied corpus.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Harden and monitor network-edge devices: regularly pull running configurations and compare to authorized baselines; harden or disable GuestShell/management shells where present; restrict and review trusted connections and ACLs; increase logging and monitoring; segment networks and perform forensic review for persistence indicators.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** The campaign employs a variety of attack vectors: weaponizing CVE-2023-23397 to steal NTLM hashes and credentials via crafted Outlook calendar invitations; leveraging CVE-2023-38831 to execute arbitrary code through malicious WinRAR archives; using Roundcube vulnerabilities (CVE-2020-12641, CVE-2020-35730, CVE-2021-44026) for shell command execution and email access; and exploiting internet-facing infrastructure such as VPNs through SQL injection and other public vulnerabilities.
- **Affected Products:** Microsoft Outlook, WinRAR, Roundcube Webmail, Corporate VPNs, IP Cameras
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** Public proof-of-concept and weaponized exploits exist for the vulnerabilities used in this campaign, specifically CVE-2023-23397 (Outlook), CVE-2023-38831 (WinRAR), and various Roundcube Webmail vulnerabilities.
- **Patch Available:** Official patches have been released for the exploited vulnerabilities, including Microsoft's patch for CVE-2023-23397, RARLAB's patch for CVE-2023-38831, and updates for Roundcube Webmail (CVE-2020-12641, CVE-2020-35730, CVE-2021-44026).
- **Active Exploitation:** Confirmed active cyber espionage campaign targeting Western logistics entities and technology companies involved in coordinating assistance to Ukraine, as reported in CISA Advisory AA25-141A.
- **Threat Actors:** Russian GRU Unit 26165 (85th GTsSS), also tracked as APT28, Fancy Bear, Forest Blizzard, and Blue Delta.
- **Mitigation:** General security mitigations include implementing network segmentation, adopting Zero Trust principles, and configuring host firewalls. Specific hardening includes enabling Windows attack surface reduction (ASR) rules to block executable content from email and preventing file execution from writable directories like Downloads. For IP cameras, the advisory recommends updating firmware, disabling unnecessary remote access, and using firewalls or VPNs to restrict access.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

**Parallel AI Enrichment:**

- **Technical Details:** The blog discusses general browser vulnerability mechanisms, including the exploitation of rendering logic, JavaScript execution, document handling, and memory safety weaknesses, often followed by sandbox escapes and privilege escalation.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Information on whether a public PoC exists is unavailable as the blog discusses browser vulnerabilities in general.
- **Patch Available:** Information on whether a specific patch is available is unavailable as the blog discusses browser vulnerabilities in general.
- **Active Exploitation:** The blog mentions a general trend where 42% of vulnerabilities were exploited before public disclosure (CrowdStrike 2026 Global Threat Report), but no specific active exploitation is reported for a single vulnerability.
- **Threat Actors:** None known
- **Mitigation:** The blog recommends a moving target defense approach called JavaScript Language Randomization (JSLR) to randomize the JavaScript runtime environment, as implemented in CrowdStrike Falcon Secure Access.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 12. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
