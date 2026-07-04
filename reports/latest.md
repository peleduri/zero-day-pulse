# Zero Day Pulse

> **Generated:** 2026-07-04 01:47 UTC &nbsp;|&nbsp; **Total:** 15 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is an unauthenticated path traversal vulnerability (CWE-22) in the SimpleHelp web application. Certain HTTP endpoints fail to properly sanitize user-supplied input in file paths, allowing remote unauthenticated attackers to craft HTTP GET requests containing directory-traversal sequences (e.g., '../../../../') to read arbitrary files from the SimpleHelp host outside the installation directory. Attackers can exfiltrate sensitive files including serverconfig.xml (containing technician account info and password hashes), LDAP credentials, OIDC client secrets, API keys, TOTP seeds, SSH private keys (/root/.ssh/id_rsa), /etc/passwd, and C:\Windows\System32\config\SAM. Stolen credentials and configuration data are then leveraged for privilege escalation, lateral movement, and ransomware deployment. The vulnerability is unauthenticated and exploitable remotely over the network with low attack complexity.
- **Affected Products:** SimpleHelp Remote Support Software v5.5.7 and all earlier releases (v5.5.x, v5.4.x, v5.3.x)
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Yes. Public proof-of-concept exploits and weaponized modules are publicly available: (1) GitHub PoC repository at https://github.com/imjdl/CVE-2024-57727, (2) ProjectDiscovery Nuclei template at https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2024/CVE-2024-57727.yaml, (3) Metasploit auxiliary module 'simplehelp_toolbox_path_traversal' (use auxiliary/scanner/http/simplehelp_toolbox_path_traversal).
- **Patch Available:** Yes. Official vendor patches were released by SimpleHelp on January 8, 2025 (v5.5.8 and v5.4.10) and January 13, 2025 (v5.3.9). Patches are available via the SimpleHelp Download Page and the official advisory at https://guides.simple-help.com/kb---security-vulnerabilities-01-2025.
- **Active Exploitation:** Yes. Confirmed active exploitation in the wild has been reported since January 2025. CISA published Advisory AA25-163A on June 12, 2025 documenting ransomware actors exploiting unpatched SimpleHelp RMM instances to compromise a utility billing software provider and its downstream customers. CISA has added CVE-2024-57727 to the Known Exploited Vulnerabilities (KEV) Catalog. Sources: CISA AA25-163A (https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a), Broadcom/Symantec protection bulletin, Picus Security analysis, and Industrial Cyber reporting.
- **Threat Actors:** DragonForce ransomware actors (per CISA Advisory AA25-163A)
- **Mitigation:** 1) Upgrade immediately: v5.5 users to v5.5.8 or later; v5.4 users to v5.4.10 (overwrite lib/shelp-jar-with-dependencies.jar); v5.3 users to v5.3.9 (overwrite secure_utils.jar, secure_nlink.jar, secure_shelp.jar in the lib directory). 2) Change the Administrator password and all Technician account passwords using local logins. 3) Restrict IP addresses for Technician and Administrator logins. 4) Regenerate all API tokens and restrict API request IP addresses. 5) Restrict firewall connections to the SimpleHelp server; place it behind a VPN where possible. 6) Configure Server Event alerts for Administrator logins, failed login attempts, and configuration changes. 7) Audit for suspicious executables with short alphabetic filenames (e.g., aaa.exe, bbb.exe) created after January 2025, and review SimpleHelp Remote Access directories (%APPDATA%\JWrapper-Remote Access, /opt/JWrapper-Remote Access, /Library/Application Support/JWrapper-Remote Access).
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — Unpatched Flaws Disclosed in Filesystem Bundled Into Millions of Embedded Devices

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-03
**Reference:** <https://thehackernews.com/2026/07/unpatched-flaws-disclosed-in-filesystem.html>

> Security firm runZero has disclosed seven vulnerabilities in FatFs, a small filesystem library that lets a device read and write the FAT and exFAT formats used on USB drives and SD cards.

The flaws matter because FatFs is nearly everywhere. It ships inside the firmware that runs security cameras, drones, industrial controllers, hardware crypto wallets, and other devices built on

**Parallel AI Enrichment:**

- **Technical Details:** Seven distinct vulnerabilities in ChaN's FatFs R0.16 and earlier: (1) CVE-2026-6682: FAT32 integer overflow in mount_volume() via fasize *= fs->n_fats, producing attacker-controlled file-size metadata (CWE-190). (2) CVE-2026-6687: Long filename handling where fno.fname can reach 255 chars and callers copy into short fixed buffers (CWE-120). (3) CVE-2026-6688: Stack buffer overflow in f_getlabel() due to unchecked exFAT label length XDIR_NumLabel (CWE-121). (4) CVE-2026-6685: Unsigned-subtraction wrap in f_read()/f_write() dirty-cache skip logic causing stale-cache handling (CWE-191). (5) CVE-2026-6683: Divide-by-zero in exFAT sync/write paths when n_fatent - 2 equals zero (CWE-369). (6) CVE-2026-6686: Uninitialized-cluster exposure in f_lseek() extending files beyond EOF without zero-filling (CWE-908). (7) CVE-2026-6684: Malformed GPT partition table triggers unbounded scan loop (CWE-835, pre-R0.16). Attack vector is primarily local/physical media (SD card, USB drive); some bugs reachable via OTA/firmware update pipelines.
- **Affected Products:** ChaN FatFs R0.16 and earlier; downstream bundlers include ESP-IDF, STM32Cube middleware, Zephyr RTOS, MicroPython, ArduPilot, RT-Thread, Arm Mbed, Samsung TizenRT, SWUpdate. Affected device categories: security cameras, drones, industrial controllers, hardware crypto wallets, and other IoT/embedded devices.
- **CVSS Score:** 7.6
- **CVSS Vector:** CVE-2026-6682/6687/6688 (High): CVSS:3.1/AV:P/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H; CVE-2026-6685 (Medium): CVSS:3.1/AV:P/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:H; CVE-2026-6686 (Medium): CVSS:3.1/AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N; CVE-2026-6683/6684 (Medium): CVSS:3.1/AV:P/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Exploit Available:** Yes - public PoC available at https://github.com/runZeroInc/vulns-2026-fatfs-chance. The repository contains a test harness, QEMU-based exploit example, and malformed filesystem images. No weaponized in-the-wild exploit reported.
- **Patch Available:** Partial. Only CVE-2026-6684 is fixed in upstream FatFs R0.16 (https://elm-chan.org/fsw/ff/updates.html). The other six CVEs (CVE-2026-6682, -6683, -6685, -6686, -6687, -6688) have no upstream fix; downstream vendors (ESP-IDF, Zephyr, MicroPython, etc.) must patch individually. Primary advisory: https://www.runzero.com/blog/fatfs-bugs/
- **Active Exploitation:** No confirmed active exploitation in the wild as of disclosure date (July 3, 2026). PoC code is publicly available but no observed in-the-wild abuse has been reported. Sources: https://thehackernews.com/2026/07/unpatched-flaws-disclosed-in-filesystem.html and https://www.runzero.com/blog/fatfs-bugs/
- **Threat Actors:** None known
- **Mitigation:** No upstream patch for 6 of 7 CVEs (only CVE-2026-6684 fixed in R0.16). Recommended actions: (1) Firmware integrators: audit vendored FatFs version, add filename length validation (CVE-2026-6687), validate exFAT label length in f_getlabel (CVE-2026-6688), add GPT entry-count validation (CVE-2026-6684), check overflow in mount_volume (CVE-2026-6682), and harden wrapper code. (2) Device users: limit physical access to USB/SD ports, monitor OEM firmware updates, avoid untrusted media. (3) Track downstream patches from ESP-IDF, Zephyr, MicroPython, SWUpdate, etc.
- **Vendor Advisory:** https://www.runzero.com/blog/fatfs-bugs/

---

## 3. 🟠 Zero-Day — Critical Cursor AI Code Editor Flaws Could Lead to OS-Level Remote Code Execution

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-03
**Reference:** <https://www.securityweek.com/critical-cursor-ai-ide-flaws-could-lead-to-os-level-remote-code-execution/>

> The DuneSlide vulnerabilities enable zero-click prompt injection attacks that escape Cursor&#x27;s sandbox and execute arbitrary code on the underlying operating system. The post Critical Cursor AI Code Editor Flaws Could Lead to OS-Level Remote Code Execution appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Two zero-click prompt-injection vulnerabilities (DuneSlide: CVE-2026-50548, CVE-2026-50549) allow maliciously-crafted/poisoned web results or malicious MCPs to cause the agent to modify working_directory and write files outside the workspace, escaping Cursor's sandbox and enabling OS-level remote code execution under the user's privileges.
- **Affected Products:** Cursor IDE (versions before 3.0)
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) or weaponized exploit was found in the referenced sources; the original disclosure (Cato AI Labs) describes exploitation technique but does not publish exploit code.
- **Patch Available:** Cursor released a patch (addressed in Cursor 3.0); vendor advisory URL unavailable.
- **Active Exploitation:** No confirmed reports of active exploitation in the wild were found in the referenced sources.
- **Threat Actors:** None known
- **Mitigation:** Update to Cursor 3.0 or later (which addresses the issues); if immediate update is not possible, disable or restrict AI agent features, run the editor with stricter sandboxing/least-privilege, and avoid processing untrusted/poisoned web results.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is a web-based attack class where adversaries embed covert or explicit instructions into web content (or other data sources) that an AI agent ingests; the agent treats those instructions as actionable and can follow them (often via multi-stage/deferred commands), enabling data exfiltration, policy bypass, or unauthorized actions.
- **Affected Products:** Google Gemini (including Gemini in Workspace), Gemini Enterprise integrations, AI-enabled browsers and other AI agents that ingest web content
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — public proofs-of-concept and research demos exist (e.g., public PoC repositories demonstrating IPI HTML payloads; see GitHub PoC example and published research such as Noma's GeminiJack report).
- **Patch Available:** No single vendor "patch" was published; Google describes a continuous/layered defense and provides guidance (see: https://blog.google/security/prompt-injections-web/ and Workspace guidance https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini).
- **Active Exploitation:** Yes — Google and third-party researchers observed indirect prompt-injection payloads on the public web and reported an increase in malicious content; specific research teams (Google, Forcepoint/others) and vendor researchers have documented in-the-wild examples, and research disclosures (e.g., Noma Labs’ GeminiJack) describe real-world findings.
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses: restrict or disable agent web browsing for high-risk tasks, apply content/prompt sanitization and origin attribution, require human review for sensitive actions, monitor/alert on anomalous agent behavior, and apply workspace-level content controls as recommended by Google.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) hides malicious instructions inside external data sources (web pages, files, memory, tool outputs). When an LLM or RAG/agent system retrieves that external content during query processing, the hidden instructions can influence model behavior (including without direct user input). End-to-end exploit demonstrations span RAG and agentic systems and use crafted web/payload content or stored conversation memory to change model outputs.
- **Affected Products:** Google Workspace, Gemini (specific versions not listed)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proofs-of-concept and exploit demonstrations exist (examples: GitHub PoC for AI browsers: https://github.com/brennanbrown/atlas-prompt-injection-poc; Unit42 writeup: https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/; academic end-to-end IPI research: http://arxiv.org/pdf/2601.07072).
- **Patch Available:** No single vendor 'patch' (IPI is an attack technique). Google published an advisory and mitigation guidance for Workspace/Gemini: http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html
- **Active Exploitation:** Yes — multiple industry reports describe IPI observed in the wild (Unit42, CrowdStrike/industry writeups, Forcepoint/others).
- **Threat Actors:** None known
- **Mitigation:** Vendor and community guidance recommends a layered defense: limit/validate external retrieval, apply provenance/trust checks and retrieval filters, sandbox and restrict agentic tool access, sanitize inputs and retrieved content, apply RAG QA and guardrails, monitor for anomalous prompts and payloads. See vendor advisory and OWASP/industry guidance for details.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Insufficient policy enforcement in Chrome's WebView tag allowed script injection into privileged pages (can be triggered via indirect prompt injection or a malicious extension). Tracked as GeminiJack / CVE-2026-0628.
- **Affected Products:** Google Chrome prior to 143.0.7499.192
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof-of-concept (PoC) available (GitHub: https://github.com/fevar54/CVE-2026-0628-POC).
- **Patch Available:** Yes — Google released fixes (addressed in Chrome 143.0.7499.192). Vendor advisory: https://blog.google/security/architecting-security-for-agentic/
- **Active Exploitation:** No confirmed active exploitation reported in the wild according to public trackers and vendor/industry reports.
- **Threat Actors:** None known
- **Mitigation:** Update Chrome to 143.0.7499.192 or later (vendor patch); apply Chrome/enterprise hardening for agentic/Gemini integrations and restrict untrusted extensions and WebView content.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Out-of-bounds access in the CrabbyAvif AVIF parser/decoder (incorrect bounds checking when handling NV12 / AVIF data) that can produce memory corruption and potentially remote code execution when processing crafted AVIF images.
- **Affected Products:** Android System component (CrabbyAvif / external/rust/crabbyavif)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) or weaponized exploit located in public sources (searched project repos and vulnerability pages).
- **Patch Available:** Official vendor fix distributed via the Android Security Bulletin (August 2025) as referenced in search results; specific advisory URL not located in the searched corpus.
- **Active Exploitation:** No confirmed active exploitation reported in the searched sources (no incident reports or advisory text describing exploitation found).
- **Threat Actors:** None known
- **Mitigation:** Apply the Android Security Bulletin update (August 2025) that addresses CVE-2025-48530. If immediate patching is not possible, mitigate by blocking or sandboxing untrusted AVIF input / disabling the AVIF handler and limiting exposure to untrusted AVIF media.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Pre-authenticated OS command-injection in Ivanti Sentry that allows a remote unauthenticated attacker to execute arbitrary OS commands and achieve root-level code execution on affected appliances, enabling configuration changes, credential theft, data access and lateral movement.
- **Affected Products:** Ivanti Sentry (appliance) — versions before R10.5.2, R10.6.2, and R10.7.1
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Exploit Available:** Yes — public proof-of-concept (PoC) exploit code has been published (example: GitHub PoC repository).
- **Patch Available:** Yes — Ivanti released patched Sentry versions R10.5.2, R10.6.2 and R10.7.1 (see vendor advisory URL above).
- **Active Exploitation:** Confirmed — multiple sources (Shadowserver, Rapid7 and independent researchers) reported active exploitation in the wild following disclosure.
- **Threat Actors:** None known
- **Mitigation:** Upgrade affected Ivanti Sentry appliances to the patched versions (R10.5.2, R10.6.2, R10.7.1). If immediate patching is not possible, isolate the appliance, restrict network access to management interfaces, monitor logs/alerts and apply compensating network controls until upgrades can be applied.
- **Vendor Advisory:** https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523?language=en_US

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** The threat actors exploit publicly known vulnerabilities (CVE-2024-21887, CVE-2023-46805, CVE-2024-3400, CVE-2023-20273, CVE-2023-20198, and CVE-2018-0171) in internet-facing network edge devices — primarily large backbone routers of major telecom providers, plus provider edge (PE) and customer edge (CE) routers from Cisco, Ivanti, and Palo Alto Networks. Once inside, they modify router configurations to maintain long-term persistent access: adding/altering Access Control Lists (frequently named 'access-list 20') to permit actor-controlled IPs; configuring GRE, mGRE, or IPsec tunnels and static routes for command-and-control and exfiltration; enabling traffic mirroring (SPAN, RSPAN, ERSPAN) to capture authentication traffic such as RADIUS/TACACS+; abusing the Cisco GuestShell containerized Linux environment to run Python scripts and the 'JumbledPath' obfuscation utility while evading syslog capture; abusing SNMP for device enumeration; and clearing logs and disabling log forwarding. They then pivot via trusted provider-to-provider and customer connections into additional networks. Detection evasion uses double URL encoding (e.g., /%2577eb%2575i_%2577sma_Http). No zero-day exploitation has been observed — all listed CVEs are publicly known and patched.
- **Affected Products:** Ivanti Connect Secure (versions 9.x, 22.x) and Ivanti Policy Secure; Palo Alto Networks PAN-OS (versions 10.2 prior to 10.2.9-h1, 11.0 prior to 11.0.4-h1, 11.1 prior to 11.1.2-h3) with GlobalProtect enabled; Cisco IOS XE Software (Web UI feature enabled) and Cisco NX-OS (GuestShell container); Cisco IOS/IOS XE Software Smart Install feature. Suspected additional targets include Fortinet firewalls, Juniper firewalls, Microsoft Exchange servers, Nokia routers/switches, Sierra Wireless devices, and SonicWall firewalls.
- **CVSS Score:** 9.6
- **CVSS Vector:** CVSS vector unavailable. CISA Advisory AA25-239A aggregates multiple distinct CVEs each with its own vector — no single CVSS v3 vector applies to the advisory as a whole. Individual vectors include CVE-2024-21887 CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H, CVE-2018-0171 CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, and CVE-2023-20198 CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H.
- **Exploit Available:** Yes — publicly weaponized and PoC exploit code exists for the underlying CVEs. The actors leverage publicly available tooling including siet.py (Cisco Smart Install), map.tcl, tclproxy.tcl, wodSSHServer, STOWAWAY (multi-hop proxy), ShadowPad loader, PAExec, and the JumbledPath utility (Cisco GuestShell). Public PoCs and exploits are widely available in repositories referenced in vendor advisories: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxe-webui-privesc-j22SaA4z and https://security.paloaltonetworks.com/CVE-2024-3400.
- **Patch Available:** Yes — official vendor patches are available for every CVE listed in AA25-239A. Patches are listed in CISA's Known Exploited Vulnerabilities (KEV) Catalog and the corresponding vendor security advisories: Ivanti (https://hub.ivanti.com/s/article/CVE-2023-46805-Authentication-Bypass-CVE-2024-21887-Command-Injection-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure-Gateways), Palo Alto Networks (https://security.paloaltonetworks.com/CVE-2024-3400), and Cisco (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxe-webui-privesc-j22SaA4z and https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20180328-smi2).
- **Active Exploitation:** Yes — confirmed active exploitation in the wild is the central focus of CISA Advisory AA25-239A (Sep 3, 2025), co-authored with the NSA and partners. The advisory documents PRC state-sponsored actors actively compromising telecommunications, government, transportation, lodging, and military infrastructure networks globally. This is supported by the U.S. Department of Justice/FBI Salt Typhoon indictments, NSA press releases, the accompanying FBI PIN/IC3 CSA, and corroborating reporting from SafeBreach, Picus Security, AttackIQ, and Forward Networks. CISA explicitly notes: 'Exploitation of zero-day vulnerabilities has not been observed to date' — the actors rely on exploiting unpatched, publicly known n-day vulnerabilities for initial access and long-term persistence.
- **Threat Actors:** Salt Typhoon (also tracked as FamousSparrow, Earth Estries, UNC2286), OPERATOR PANDA, RedMike, UNC5807, and GhostEmperor — all PRC state-sponsored cyber threat actors.
- **Mitigation:** 1) Immediately prioritize patching all CVEs listed in CISA's Known Exploited Vulnerabilities (KEV) Catalog that are referenced in AA25-239A. 2) Disable Cisco Smart Install (no vstack director) and disable Cisco GuestShell where not operationally required. 3) Disable outbound connections from network/management interfaces and disable unused ports/protocols. 4) Audit running router configurations against authorized baselines; look for unauthorized GRE/IPsec tunnels, changes to TACACS+/RADIUS servers, external IPs in ACLs (especially 'access-list 20'), and packet capture/mirroring configurations. 5) Change default passwords and use strong cryptographic algorithms. 6) Implement robust change management and periodic configuration auditing. 7) Verify Cisco GuestShell status via 'show guestshell' (NX-OS) or 'show app-hosting detail' (IOS XE); an 'Activated' or 'RUNNING' state warrants deeper investigation. 8) Monitor for the public PoC tooling (siet.py, STOWAWAY, ShadowPad, JumbledPath) and associated IOCs in the advisory's STIX bundle.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Campaign-level espionage: spearphishing/targeted emails, credential harvesting and abuse of operational infrastructure and tooling; industry reporting linking the campaign cites exploitation of known vulnerabilities in victim environments (example: CVE-2023-23397 — Outlook ReminderSoundFile abuse leading to NTLM credential leakage to an attacker-controlled SMB server).
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof-of-concept code exists for at least one vulnerability discussed in related reporting (notably CVE-2023-23397 — public PoCs and community scripts are available); the CISA campaign advisory itself is campaign-level and does not publish PoC code.
- **Patch Available:** For CVE-2023-23397 Microsoft released a security update in March 2023; for the campaign, CISA and partners issued mitigations and IOCs/STIX via the AA25-141A advisory.
- **Active Exploitation:** Yes — the advisory reports an active Russian GRU campaign (Unit 26165) targeting Western logistics entities and technology companies (activity observed since 2022); CISA/FBI joint advisory and industry partners document observed targeting and provide IOCs.
- **Threat Actors:** Russian GRU (Unit 26165 / 85th GTsSS), tracked by industry as APT28 (aka Fancy Bear)
- **Mitigation:** CISA/partners recommend applying vendor security updates, use MFA, monitor authentication and mail logs, ingest and block IOCs/STIX from the advisory, harden mail- and file-sharing exposure (reduce NTLM/SMB exposure where possible), and follow CISA/FBI recommended detection and response guidance.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 11. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

---

## 12. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 13. 🟠 Zero-Day — In Other News: Canadian Hacker Jailed, Open Source Zero-Days, Two Sentenced for ATM Jackpotting

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-03
**Reference:** <https://www.securityweek.com/in-other-news-canadian-hacker-jailed-open-source-zero-days-two-sentenced-for-atm-jackpotting/>

> Noteworthy stories that might have slipped under the radar: Anonymous-linked Canadian hacker jailed, researcher drops zero-days in open source projects, Venezuelans sentenced in the US over ATM jackpotting. The post In Other News: Canadian Hacker Jailed, Open Source Zero-Days, Two Sentenced for ATM Jackpotting appeared first on SecurityWeek .

---

## 14. 🟠 Zero-Day — Google, FBI Disrupt NetNut Residential Proxy Network Powered by Millions of Devices

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-03
**Reference:** <https://www.securityweek.com/google-fbi-disrupt-netnut-residential-proxy-network-powered-by-millions-of-devices/>

> NetNut rented access to millions of compromised devices, allowing cybercriminals and nation-state actors to mask their identities during attacks. The post Google, FBI Disrupt NetNut Residential Proxy Network Powered by Millions of Devices appeared first on SecurityWeek .

---

## 15. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
