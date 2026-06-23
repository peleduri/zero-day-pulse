# Zero Day Pulse

> **Generated:** 2026-06-23 19:49 UTC &nbsp;|&nbsp; **Total:** 46 &nbsp;|&nbsp; 🔴 KEV: 4 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 32 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🔴 CISA KEV — CVE-2025-67038 — Lantronix EDS5000 Code Injection Vulnerability

**CVE:** `CVE-2025-67038` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2025-67038>

> Vendor: Lantronix | Product: EDS5000. Lantronix EDS5000 contains a code injection vulnerability that could allow attackers to inject arbitrary OS commands into the username parameter. Injected commands are executed with root privileges. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (s…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is a code injection flaw in the HTTP RPC module of the Lantronix EDS5000. It occurs when the module executes a shell command to write logs during user authentication, which allows an attacker to inject arbitrary OS commands into the username parameter. These injected commands are executed with root privileges.
- **Affected Products:** Lantronix EDS5000 2.1.0.0R3
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** Public proof-of-concept (PoC) exploits are reported to exist on GitHub, although a specific URL was not provided in the citations.
- **Patch Available:** No official patch or remediation guidance is currently available from the vendor [6].
- **Active Exploitation:** Confirmed active exploitation has been reported; the vulnerability is included in the CISA Known Exploited Vulnerabilities (KEV) catalog as of the provided input metadata.
- **Threat Actors:** None known
- **Mitigation:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk guidance and CISA’s “Forensics Triage Requirements”.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 2. 🔴 CISA KEV — CVE-2026-34910 — Ubiquiti UniFi OS Improper Input Validation Vulnerability

**CVE:** `CVE-2026-34910` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-34910>

> Vendor: Ubiquiti | Product: UniFi OS. Ubiquiti UniFi OS contains an improper input validation vulnerability which could allow a malicious actor with access to the network to conduct command injection. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s…

**Parallel AI Enrichment:**

- **Technical Details:** Improper Input Validation allows a remote unauthenticated attacker with network access to perform command injection on UniFi OS devices, leading to arbitrary command execution and potential root-level compromise.
- **Affected Products:** UniFi OS (all versions up to disclosure)
- **CVSS Score:** 10.0
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Exploit Available:** No public proof‑of‑concept or weaponized exploit is known.
- **Patch Available:** Ubiquiti released firmware updates addressing this issue (Security Advisory Bulletin 064). Apply the latest UniFi OS firmware.
- **Active Exploitation:** No confirmed active exploitation in the wild has been reported.
- **Threat Actors:** None known
- **Mitigation:** Update UniFi OS to the latest version, restrict management interface exposure (firewall, VPN, trusted IP ranges), audit account activity, rotate credentials, segment management networks, and follow vendor guidance.
- **Vendor Advisory:** https://community.ui.com/releases/Security-Advisory-Bulletin-064-064/84811c09-4cf4-42ab-bd61-cc994445963b

---

## 3. 🔴 CISA KEV — CVE-2026-34909 — Ubiquiti UniFi OS Path Traversal Vulnerability

**CVE:** `CVE-2026-34909` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-34909>

> Vendor: Ubiquiti | Product: UniFi OS. Ubiquiti UniFi OS contains a path traversal vulnerability which could allow a malicious actor with access to the network to access files on the underlying system that could be manipulated to access an underlying account. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Up…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-34909 is a Path Traversal (CWE‑22) flaw in the UniFi OS web service. An attacker with network access can craft a request that traverses directories and reads arbitrary files on the underlying system, potentially exposing configuration data or credentials. When combined with other UniFi OS bugs (improper access control and command injection), this can be leveraged to achieve unauthenticated remote code execution with root privileges.
- **Affected Products:** All UniFi OS devices (including UniFi Dream Machine, Dream Machine Pro, Cloud Gateway, NVR, Protect, Access, Talk, Connect, and any hardware running UniFi OS).
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Exploit Available:** Public proof‑of‑concept and detection tool are available. Bishop Fox published a full unauthenticated RCE chain and a GitHub detection script (https://github.com/BishopFox/CVE-2026-34908-check).
- **Patch Available:** Ubiquiti has released security updates that address CVE-2026-34909 and CVE-2026-34908. The fix is included in the UniFi OS firmware updates referenced in Security Advisory Bulletin 064.
- **Active Exploitation:** Confirmed. The vulnerability was added to the CISA Known Exploited Vulnerabilities (KEV) catalog on 16 June 2026 based on evidence of active exploitation, and Bishop Fox’s research confirms a working exploit chain.
- **Threat Actors:** None known
- **Mitigation:** Apply the latest UniFi OS firmware (or hardware‑specific version) that contains the fix (Bulletin 064). If immediate patching is not possible, block external access to the UniFi OS management interface (default TCP 11443) and restrict it to trusted networks or VPN. Rotate all admin credentials, API keys, and secrets after patching. Monitor for unexpected configuration changes, new admin accounts, or suspicious device adoption activity. Segment the management network and enforce least‑privilege access controls.
- **Vendor Advisory:** https://community.ui.com/releases/Security-Advisory-Bulletin-064-064/84811c09-4cf4-42ab-bd61-cc994445963b

---

## 4. 🔴 CISA KEV — CVE-2026-34908 — Ubiquiti UniFi OS Improper Access Control Vulnerability

**CVE:** `CVE-2026-34908` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-34908>

> Vendor: Ubiquiti | Product: UniFi OS. Ubiquiti UniFi OS contains an improper access control vulnerability which could allow a malicious actor with access to the network to make unauthorized changes to the system. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidanc…

**Parallel AI Enrichment:**

- **Technical Details:** Improper Access Control (CWE‑1284) flaw in the UniFi OS server management interface that lets any unauthenticated network‑adjacent attacker bypass access restrictions and make unauthorized system changes (configuration, policy, etc.) without credentials.
- **Affected Products:** Ubiquiti UniFi OS devices: UDM, UDM‑Pro, UDM‑SE, UDM‑Pro‑Max
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Exploit Available:** No public proof‑of‑concept or weaponized exploit is known. No exploit has been reported in the wild.
- **Patch Available:** An official vendor patch is available (see vendor advisory).
- **Active Exploitation:** No confirmed active exploitation has been reported.
- **Threat Actors:** None known
- **Mitigation:** Apply the official vendor patch immediately. Restrict management interface access to trusted networks only (IP‑whitelisting, firewall rules, network segmentation). Block external access to UniFi OS management ports (8080, 8443, 443) from untrusted segments. Enable strict ACLs and VPN‑only access for administrators. Monitor logs for unauthorized configuration changes and unauthenticated API calls. Deploy intrusion detection/monitoring for abnormal UniFi OS activity. Follow CISA BOD 26‑04 guidance for cloud services or discontinue use if mitigation cannot be applied.
- **Vendor Advisory:** https://community.ui.com/releases/Security-Advisory-Bulletin-064-064/84811c09-4cf4-42ab-bd61-cc994445963b

---

## 5. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a directory/path traversal vulnerability in SimpleHelp that permits unauthenticated attackers to craft HTTP requests which traverse the server filesystem and read arbitrary files (for example, configuration files, /etc/passwd, SSH private keys). The weakness can be chained with other vulnerabilities to escalate access; exploitation is achievable remotely via the SimpleHelp web interface.
- **Affected Products:** SimpleHelp remote support / SimpleHelp RMM: version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — public proof‑of‑concept exists (Metasploit auxiliary module msf6 auxiliary/scanner/http/simplehelp_toolbox_path_traversal).
- **Patch Available:** Yes — patches available in SimpleHelp versions 5.5.8 and later. Vendor advisory: http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know
- **Active Exploitation:** Confirmed — active exploitation reported in the wild by ransomware actors; CISA added CVE-2024-57727 to its Known Exploited Vulnerabilities (KEV) Catalog and vendor reporting and third‑party writeups document observed ransomware use (including incidents impacting a utility‑billing software provider).
- **Threat Actors:** Ransomware actors (observed groups include DragonForce and Medusa)
- **Mitigation:** If immediate patching is not possible: isolate the SimpleHelp server from the internet or stop the server process; disable file‑browsing functionality; restrict access to the SimpleHelp web interface with network controls (firewalls, allow‑lists); apply host hardening. If ransomware encryption occurs: disconnect affected systems, reinstall from clean media, and restore from known‑good backups.
- **Vendor Advisory:** http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 6. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an AI system processes external content (e.g., website, email, document) that contains hidden malicious instructions. The AI, while parsing this poisoned content, may silently follow the attackers commands rather than the intended user request, potentially leading to data exfiltration, system disruption, or other malicious outcomes.
- **Affected Products:** Google AI agents (Gemini), Google Workspace, Chrome Enterprise, Android
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No exploit available.
- **Patch Available:** No patch available.
- **Active Exploitation:** Limited active exploitation observed; several malicious indirect prompt injection payloads have been found on public websites, with a 32% increase in detections between November 2025 and February 2026.
- **Threat Actors:** None known
- **Mitigation:** Apply input/output validation and sanitization, enforce human oversight, employ layered defense strategies, continuously monitor for IPI patterns, and participate in Googles AI Vulnerability Reward Program for reporting. Additional hardening measures are described in Googles continuous approach to mitigating indirect prompt injections.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 7. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) allows an attacker to influence the behavior of a large language model by injecting malicious instructions into the data, tools, or context the model consumes while processing a user query. This can happen without any direct user input, exploiting the multi-source nature of AI-enhanced applications such as Workspace with Gemini.
- **Affected Products:** Google Workspace (including Gemini Enterprise)
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) available
- **Patch Available:** No official patch; mitigations are achieved through continuous monitoring, layered defenses, and model hardening.
- **Active Exploitation:** Yes  active exploitation has been observed (e.g., 10 indirect prompt injection payloads caught in the wild).
- **Threat Actors:** None known
- **Mitigation:** Google employs a layered, continuous defense strategy that includes human redteam simulations, automated redteaming frameworks, an AI Vulnerability Rewards Program, monitoring of publicly disclosed attacks, deterministic defenses (user confirmation, URL sanitization, toolchaining policies) managed via a centralized policy engine, MLbased defenses trained on synthetic data, LLMbased defenses refined through prompt engineering, and model hardening of Gemini to ignore injected malicious instructions.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 8. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection occurs when attacker‑controlled web content is ingested by an LLM‑driven agent, subtly modifying the prompt to cause unintended actions. In Chrome’s Gemini agentic browsing, this can be chained with CVE‑2025‑54131 to achieve arbitrary command execution. Google mitigates by scanning pages with a separate User Alignment Critic model and requiring user confirmation for high‑risk actions.
- **Affected Products:** Google Chrome (pre‑patch Gemini AI agentic browsing), Google Gemini Enterprise (GeminiJack), Cursor (< 1.3)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoCs are available; Forcepoint documented 10 real‑world payloads and Noma Labs released the GeminiJack PoC.
- **Patch Available:** Yes – Chrome released patches for CVE‑2025‑1028 and CVE‑2025‑54131. Patch details are available at Unit42 and NVD.
- **Active Exploitation:** Yes – real‑world payloads have been observed in the wild (Forcepoint’s 10 IPI payloads and GeminiJack discovered by Noma Labs).
- **Threat Actors:** None known
- **Mitigation:** Enable the User Alignment Critic layer and keep Chrome up‑to‑date; the layered defense includes deterministic rules, model‑level protections, isolation boundaries, and user‑oversight prompts.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 9. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** An integer overflow in the Android Framework can be triggered to achieve arbitrary code execution and local privilege escalation without user interaction.
- **Affected Products:** Android Framework (core system layer) on Android OS versions 14, 15, 16, and 16‑qpr2
- **CVSS Score:** 8.4
- **CVSS Vector:** CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** No public proof‑of‑concept is available; however, the vulnerability is listed in the CISA Known Exploited Vulnerabilities Catalog, indicating exploits are being used in the wild.
- **Patch Available:** A security patch is available as part of the Android 2026‑06‑05 security patch level, distributed via Google Play System Updates and OTA updates.
- **Active Exploitation:** Confirmed – Google’s June 2026 Android Security Bulletin and the CISA catalog both note limited, targeted exploitation.
- **Threat Actors:** None known
- **Mitigation:** Apply the Android 2026‑06‑05 security patch (or later) as soon as possible. Until then, enable Google Play Protect, enforce SELinux enforcing mode, restrict installation of untrusted apps, and consider disabling non‑essential services.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2026/2026-06-01

---

## 10. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection involves embedding hidden malicious instructions in external data sources (e.g., emails, documents, calendar invites) that, when processed by a generative AI system such as Gemini, can cause the model to exfiltrate data or perform unauthorized actions. The attack bypasses direct user input by leveraging the AIs ability to ingest and act on external content.
- **Affected Products:** Google Gemini (Gemini 2.5 and later), Gemini in Google Workspace, Gemini app
- **CVSS Score:** -9999.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit is known.
- **Patch Available:** No official patch has been released; mitigation is provided via layered defenses.
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known.
- **Mitigation:** Google employs a layered security approach that includes (1) promptinjection content classifiers, (2) security thought reinforcement to keep the model focused on the users intent, (3) markdown sanitization and suspicious URL redaction using Safe Browsing, (4) a userconfirmation framework for highrisk actions, and (5) enduser security mitigation notifications with helpcenter guidance. Model hardening with adversarial training (Gemini 2.5) further reduces susceptibility.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 11. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

---

## 12. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 13. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 14. 🟠 Zero-Day — Algerian Man Extradited to US for Running Cybercrime Marketplaces

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://www.securityweek.com/algerian-man-extradited-to-us-for-running-cybercrime-marketplaces/>

> 26-year-old Abdellah Belmili faces up to 30 years in prison for allegedly operating the marketplaces Market0Day and Spoxy. The post Algerian Man Extradited to US for Running Cybercrime Marketplaces appeared first on SecurityWeek .

---

## 15. 🟡 High Severity — OctoPrint has possible file exfiltration via query parameters on upload endpoints

**CVE:** `CVE-2026-54134` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-j4h9-pm27-4rfw>

> ### Impact

OctoPrint versions up until and including 1.11.7 as well as 2.0.0rc1 and 2.0.0rc2 contain a vulnerability that allows an attacker with the `FILE_UPLOAD` permission to exfiltrate files from the host that OctoPrint has read access to, by moving them into the upload folder where they then can be downloaded from. This vulnerability was already reported as [GHSA-m9jh-jf9h-x3h2/CVE-2025-4806…

---

## 16. 🟡 High Severity — AVideo has an incomplete fix of CVE-2026-33482: sanitizeFFmpegCommand still allows a single '&' (background operator), giving OS command execution at the same execAsync sh -c sink

**CVE:** `CVE-2026-55173` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-wc3f-xc32-435f>

> ### Summary

The fix for CVE-2026-33482 (GHSA-pmj8-r2j7-xg6c) is incomplete. That advisory reported that `sanitizeFFmpegCommand()` (`plugin/API/standAlone/functions.php`) failed to strip `$(...)` command substitution, allowing OS command injection at the `execAsync()` `sh -c` sink. The fix (commit `25c8ab90`) added `$`, `(`, `)`, `{`, `}`, `\n`, `\r` to the denylist character class and a `str_repl…

---

## 17. 🟡 High Severity — Gogs's Unauthenticated Jupyter Notebook (ipynb) Sanitizer allows arbitrary data: URIs leading to XSS

**CVE:** `CVE-2026-52816` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-3w28-36p9-w929>

> ## Summary

The Jupyter Notebook (ipynb) sanitizer endpoint at `POST /-/api/sanitize_ipynb` allows arbitrary `data:` URIs without proper restrictions, potentially leading to Cross-Site Scripting (XSS). The endpoint uses `bluemonday.UGCPolicy()` with `p.AllowURLSchemes(&quot;data&quot;)` which permits all data URI schemes including `data:text/html`, enabling attackers to inject malicious HTML/JavaS…

---

## 18. 🟡 High Severity — OpenAM Authenticated Privilege Escalation via Raw Token Disclosure Session RPC

**CVE:** `CVE-2026-45048` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-vvhj-w2jq-263q>

> ## Summary

Description

An insufficient authorization (CWE-285) and information exposure (CWE-200) issue in OpenAM&#x27;s session management endpoint allows a low-privileged authenticated user to retrieve active session credentials belonging to other users, including those with higher privileges. This affects OpenAM Community Edition through version 16.0.6 and was patched in version 16.1.1.

This…

---

## 19. 🟡 High Severity — Gogs has Path Traversal in organization name that results in RCE through Git hooks

**CVE:** `CVE-2026-52813` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-c39w-43gm-34h5>

> ### Summary

Organization names containing path traversal sequences (`../`) are accepted by Gogs, and repositories under them are written to paths following these path traversals. This allows storing/retrieving data for repositories at arbitrary locations on the filesystem.
By creating nested structure of Git repositories, one can overwrite the other&#x27;s `hooks` configuration to result in Remot…

---

## 20. 🟡 High Severity — Gogs: LFS dedupe path leaks private repo content across tenants

**CVE:** `CVE-2026-52812` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-6p9m-q3jp-47h4>

> Summary

Git LFS storage is content-addressed by OID alone (`&lt;LFS-root&gt;/&lt;oid[0]&gt;/&lt;oid[1]&gt;/&lt;oid&gt;`) but per-repo authorization lives in the `lfs_object` table keyed `(repo_id, oid)`. `serveUpload` skips re-uploading when the OID file already exists on disk and inserts a new `(repo_id, oid)` row pointing at it **without verifying the request body hashes to the OID being claime…

---

## 21. 🟡 High Severity — Gogs vulnerable to RCE via git rebase --exec argument injection in pull request merge

**CVE:** `CVE-2026-52806` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-qf6p-p7ww-cwr9>

> # Gogs: RCE via `git rebase --exec` Argument Injection in PR Merge

## Summary

Gogs allows authenticated users to achieve Remote Code Execution (RCE) on the server by creating a pull request with a specially crafted branch name that injects the `--exec` flag into the `git rebase` command during the &quot;Rebase before merging&quot; merge operation.

## Severity

**Critical** - CVSS 3.1 Base Score…

---

## 22. 🟡 High Severity — Gogs has a Migration Redirect Bypass that Leads to Internal Repository Theft

**CVE:** `CVE-2026-52805` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-g2f5-gjr4-qjvm>

> # Migration URL validation bypass via HTTP redirect to blocked internal endpoints

## Summary

A Server-Side Request Forgery (SSRF) vulnerability exists in the repository migration functionality. The application validates only the initially submitted URL hostname, but `git clone --mirror` follows HTTP redirects. An authenticated user can submit a public URL that redirects to a blocked internal end…

---

## 23. 🟡 High Severity — Gogs Vulnerable to Privilege Escalation via Collaboration Access Mode Validation

**CVE:** `CVE-2026-52804` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-4565-r4x7-hg8j>

> ## Summary

A repository admin collaborator can escalate their privileges to owner-level access by exploiting an off-by-one error in the `ChangeCollaborationAccessMode` function.

## Vulnerable Code

In `internal/database/repo_collaboration.go`, line 129:

```go
func (r *Repository) ChangeCollaborationAccessMode(userID int64, mode AccessMode) error {
    // Discard invalid input
    if mode &lt;= …

---

## 24. 🟡 High Severity — Gogs has the ability to import local repositories via Mirror Settings

**CVE:** `CVE-2026-52801` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-23
**Reference:** <https://github.com/advisories/GHSA-wv27-2vqp-j7g5>

> ### Summary
The Gogs Mirror Settings functionality provide an alternative way from the well protected New Migration functionality for any authenticated users to import local repositories. This issue stems from a lack of validation of SaveAddress function.

### Details
Here is the function implementation of the secure New Migration functionality.
&lt;img width=&quot;1200&quot; height=&quot;755&quot…

---

## 25. 🟡 High Severity — @actual-app/web has CSV Formula Injection in Transaction Export via Imported Payee/Notes Fields

**CVE:** `CVE-2026-50179` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-xqjm-27pc-rvwm>

> ## Summary

`exportToCSV` and `exportQueryToCSV` in `packages/loot-core/src/server/transactions/export/export-to-csv.ts` pass user-controlled `Payee`, `Notes`, `Account`, and `Category` strings to `csv-stringify` with no `cast` callback and no formula-prefix neutralization. Strings that begin with `=`, `+`, `-`, `@`, tab, or carriage return survive verbatim into the exported CSV. When the victim (…

---

## 26. 🟡 High Severity — @budibase/backend-core has potential SSRF DNS rebinding bypass in outbound fetch validation

**CVE:** `CVE-2026-54353` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-gfq7-5x4g-3xhf>

> Summary

Authenticated users with automation permissions can bypass Budibase&#x27;s SSRF blacklist through DNS rebinding.

The outbound fetch flow validates a hostname against the blacklist before the request is sent, but the actual socket connection later performs a separate DNS lookup through node-fetch. Since the validated IPs are never pinned to the connection, an attacker-controlled hostname …

---

## 27. 🟡 High Severity — Budibase has arbitrary file read by workspace-builder via PWA-zip symlink upload

**CVE:** `CVE-2026-54352` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-w7mq-r738-x278>

> ## Summary

`POST /api/pwa/process-zip` at `packages/server/src/api/routes/static.ts:24` accepts a builder-uploaded `.zip`, extracts it with `extract-zip@2.0.1` into a temp directory, then for each entry listed in `icons.json` validates the icon path, opens it, and streams the bytes into MinIO. The resulting object is served back via `GET /api/assets/{appId}/pwa/{uuid}.png`.

`extract-zip@2.0.1` p…

---

## 28. 🟡 High Severity — Budibase: POST /api/attachments/:datasourceId/url is unauthenticated and lets anonymous callers mint S3 PUT pre-signed URLs using stored datasource IAM credentials

**CVE:** `CVE-2026-50137` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-35c4-rvc8-frhm>

> ## Summary

The Budibase server route `POST /api/attachments/:datasourceId/url` ([`packages/server/src/api/routes/static.ts`](https://github.com/Budibase/budibase/blob/56d2a984/packages/server/src/api/routes/static.ts)) is registered with **only** the `recaptcha` middleware. There is no `authorized(...)` middleware in the chain. The controller (`packages/server/src/api/controllers/static/index.ts:…

---

## 29. 🟡 High Severity — Budibase: Unauthenticated S3 signed upload URL generation allows arbitrary writes with stored datasource credentials

**CVE:** `CVE-2026-50136` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-jj36-r9w3-3pfh>

> The application server exposes an unauthenticated endpoint that generates S3 `PutObject` presigned URLs using credentials stored in a workspace datasource. The route is protected only by the recaptcha middleware and does not require authentication, table permission, datasource permission, or builder access. A public caller who knows a workspace ID and S3 datasource ID can request a signed upload U…

---

## 30. 🟡 High Severity — scimPatch vulnerable to prototype pollution via unfiltered keys in patch

**CVE:** `CVE-2026-48170` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-9m6g-wc8r-q59c>

> ## Summary

`scim-patch` performs prototype pollution when applying a SCIM PATCH operation whose `value` object contains a key like `&quot;__proto__.someProp&quot;`. After one such patch,
`Object.prototype.someProp` is set process-wide, affecting every plain object in the Node process.

Any service that calls `scimPatch()` on attacker-controlled JSON (i.e. any SCIM endpoint accepting `PATCH` from …

---

## 31. 🟡 High Severity — Budibase: SSRF via OAuth2 token endpoint URL reaches internal hosts and cloud metadata

**CVE:** `CVE-2026-48153` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-4q6h-8p4v-67vq>

> ## Summary

`fetchToken` in the OAuth2 SDK makes a POST to a builder-supplied URL with plain node-fetch, skipping the `blacklist.isBlacklisted` check that every other outbound fetch path in the codebase uses. The Joi schema for the OAuth2 URL has no scheme or host restriction. Alice, a builder, points an OAuth2 config at `http://169.254.169.254/...` or `http://127.0.0.1:5984/`; the server connects…

---

## 32. 🟡 High Severity — Gogs has SSRF in webhook deliveries

**CVE:** `CVE-2026-47267` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-c4v7-xg93-qf8g>

> ### Summary
The fix for  CVE-2022-1285 prevents adding webooks or running webhooks with URLs with a hostname that resolves in localCIDRs. However, webhooks still follow redirects allowing to access hostname inside localCIDRs.

This was already communicated in the initial report but it looks like there was a bit of a miscommunication.

### Details

By creating a webook pointing to any URL that will…

---

## 33. 🟡 High Severity — @actual-app/sync-server's missing authorization on GET /secret/:name allows non-admin OpenID users to enumerate admin-configured bank-sync secrets

**CVE:** `CVE-2026-46700` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-3f62-qv96-4p78>

> ## Summary

In `@actual-app/sync-server`, the `GET /secret/:name` endpoint (`app-secrets.js:53`) checks only that the caller has a valid session — it does not verify the caller is an admin. The sibling `POST /secret/` handler does enforce an admin check in OpenID mode, exposing an authorization asymmetry. Any authenticated non-admin (BASIC) user in OpenID multi-user deployments can probe the secre…

---

## 34. 🟡 High Severity — Glances: XML-RPC Server Missing Host Header Validation Enables DNS Rebinding Attack

**CVE:** `CVE-2026-46611` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-w856-8p3r-p338>

> ### Summary

The Glances XML-RPC server (`glances -s`, implemented in `glances/server.py`) does not validate the HTTP `Host` header, leaving it vulnerable to DNS rebinding attacks.  CVE-2026-32632 (patched in 4.5.2) added `TrustedHostMiddleware` to the REST/WebUI server; the MCP server has had equivalent protection since 4.5.1. The XML-RPC server received neither fix and has no `allowed-hosts` con…

---

## 35. 🟡 High Severity — OpenDJ Pre-Auth RCE via Java Deserialization in JMX RMI

**CVE:** `CVE-2026-46495` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-43x2-g84q-fmqx>

> ## Summary

**Description**

A Deserialization of Untrusted Data (CWE-502) issue in OpenDJ&#x27;s JMX RMI connector allows an unauthenticated remote attacker to deserialize arbitrary Java objects on the server. The vulnerability exists because the platform reads and processes attacker-controlled bytes prior to authentication. This affects OpenDJ Community Edition through 5.1.0. This has been patch…

---

## 36. 🟡 High Severity — OpenAM SAML2 Cluster Cookie-Hash-Redirect Path has Pre-authentication Reflected XSS via `FSUtils.postToTarget`

**CVE:** `CVE-2026-44793` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-fhrq-3gmx-p879>

> ## Summary

Certain federation endpoints do not consistently apply output encoding when rendering user-supplied parameters into HTML responses. Under a non-default configuration used in some clustered deployments, this inconsistency can result in reflected XSS in the OpenAM origin without authentication.

---

## 37. 🟡 High Severity — Inspektor Gadget: Unprivileged container can crash USDT note parser via crafted ELF (no shipped gadget affected)

**CVE:** `CVE-2026-44778` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-7cfq-5mhv-jrp9>

> ## Summary

A malicious container can crash or destabilize the privileged Inspektor Gadget process when a **gadget using USDT probes** is deployed. The vulnerability is in the USDT note parser (`pkg/uprobetracer/usdt.go`) which is invoked when a gadget with a `SEC(&quot;usdt/...&quot;)` section attaches to a target binary. An unprivileged process can place a crafted ELF binary at the expected libr…

---

## 38. 🟡 High Severity — Paymenter has Blind Unauthenticated SSRF on the Paypal gateway module

**CVE:** `CVE-2026-44583` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-7wwh-xcc3-9fcg>

> ### Summary
The PayPal webhook endpoint `/extensions/paypal/webhook` processes the `PAYPAL-CERT-URL` HTTP header without validation, allowing attackers to control server-side HTTP request destinations.

### Technical details:

The `/extensions/paypal/webhook` endpoint processes incoming webhook requests and trusts the value of the `PAYPAL-CERT-URL` HTTP header without validation.

This value is pa…

---

## 39. 🟡 High Severity — OpenAM has pre-auth Reflected XSS in OAuth2 / OIDC response_mode=form_post via state parameter (FormPostResponse.ftl)

**CVE:** `CVE-2026-44203` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-fq9h-c788-fx73>

> ### Summary

The OAuth 2.0 / OpenID Connect authorization endpoint does not sufficiently sanitize certain user-supplied parameters before incorporating them into the HTML response generated for the `form_post` response mode. This may allow an attacker to inject content into the rendered page in the context of the OpenAM origin.

---

## 40. 🟡 High Severity — OpenAM Authenticated Server-Side Request Forgery (SSRF) via `/sessionservice`

**CVE:** `CVE-2026-44202` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-c556-q2mh-477v>

> OpenAM (Open Identity Platform) is an open-source Identity and Access Management (IAM) platform derived from ForgeRock OpenAM, providing SSO, OAuth2, SAML, and OpenID Connect capabilities. It is widely deployed in enterprise environments as a central authentication gateway.

The `/sessionservice` endpoint, used for internal session management operations, does not sufficiently restrict the URLs tha…

---

## 41. 🟡 High Severity — xwiki-pro-macros has remote code execution from page title and content via excerpt-include macro

**CVE:** `CVE-2026-44179` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-w56x-9778-rppx>

> ### Summary
The excerpt-include macro does not properly escape the title of the included page and executes the content of the excerpt with the macro&#x27;s rights. Therefore, it is vulnerable to XWiki syntax injection via the included page&#x27;s title and content, allowing remote code execution for any user who can edit a page.

### Details
The title of the included page isn&#x27;t escaped in [Ex…

---

## 42. 🟡 High Severity — OpenAM has LDAP Injection via `_queryId` Parameter

**CVE:** `CVE-2026-41573` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-2vg8-q4c2-5cw3>

> OpenAM (Open Identity Platform) is an open-source IAM platform providing SSO, OAuth2, SAML, and OpenID Connect capabilities. The CREST REST API layer exposes user query endpoints under `/json/{realm}/users`. In `IdentityResourceV1.queryCollection()`, the HTTP query parameter `_queryId` is passed to a `CrestQuery` object with `escapeQueryId` **explicitly set to `false`**, bypassing the escape prote…

---

## 43. 🟡 High Severity — AVideo has an Authorize.Net Webhook Signature Bypass that Enables Wallet Balance Inflation via Forged Payment Data

**CVE:** `CVE-2026-33731` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-95jh-7r58-xmxw>

> ## Summary

The Authorize.Net webhook handler at `plugin/AuthorizeNet/webhook.php` contains a signature verification bypass that allows an attacker to forge webhook requests with arbitrary payment amounts and target user IDs. By supplying a valid transaction ID from a small legitimate purchase, the attacker bypasses signature validation and credits arbitrary wallet balances to any user account via…

---

## 44. 🟡 High Severity — ComfyUI-Manager has an Unprotected Alternate Channel (CWE-420)

**CVE:** `CVE-2025-67303` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-95pq-hr8p-f5g7>

> ### Impact

An **Unprotected Alternate Channel (CWE-420)** vulnerability was discovered in ComfyUI-Manager versions prior to 3.38.

#### Vulnerability Details

In affected versions, ComfyUI-Manager stored its configuration in the `user/default/ComfyUI-Manager/` directory, which was accessible via ComfyUI&#x27;s web APIs without proper access control. This unprotected alternate channel allowed remo…

---

## 45. 🟡 High Severity — AVideo Vulnerable to Unauthenticated .env File Exposure via Official Docker Compose Configuration

**CVE:** `CVE-2026-33692` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-wf69-r4mx-43rr>

> ## Vulnerability Details

**CWE**: CWE-538 - Insertion of Sensitive Information into Externally-Accessible File or Directory

The official `docker-compose.yml` (line 61) mounts the entire project root directory as the Apache document root:

```yaml
volumes:
  - &quot;./:/var/www/html/AVideo&quot;
```

This causes the `.env` file — which contains database credentials, admin passwords, and infrastru…

---

## 46. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
