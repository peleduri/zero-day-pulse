# Zero Day Pulse

> **Generated:** 2026-06-03 16:14 UTC &nbsp;|&nbsp; **Total:** 17 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 15 &nbsp;|&nbsp; 🟡 High: 2 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal (directory traversal) vulnerability allowing unauthenticated remote attackers to read arbitrary files (e.g., logs, configs, credentials) via manipulated file path inputs to the SimpleHelp web interface.
- **Affected Products:** SimpleHelp Remote Support / RMM version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** A public proof‑of‑concept PoC is described in the OffSec blog.
- **Patch Available:** SimpleHelp version 5.5.8 is available, fixing the vulnerabilities present in v5.5.7 and earlier.
- **Active Exploitation:** Confirmed active exploitation reported by CISA, with ransomware actors leveraging the vulnerability in incidents since January 2025.
- **Threat Actors:** Ransomware actors (unnamed) and groups such as DragonForce
- **Mitigation:** Upgrade SimpleHelp to version 5.5.8. If immediate patching is not possible, restrict inbound Internet access to the SimpleHelp instance, allow only trusted management networks or VPN, implement egress filtering, isolate or uninstall unused instances, rotate any exposed credentials, and monitor for indicators of compromise per CISA guidance.
- **Vendor Advisory:** https://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — The sorry state of skill distribution

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Trail of Bits Blog &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://blog.trailofbits.com/2026/06/03/the-sorry-state-of-skill-distribution/>

> Public skill marketplaces are being flooded with malicious skills that steal credentials, exfiltrate data, and hijack agents. In response, a segment of the security industry released skill scanners, a new family of tools designed to detect malicious skills before they’re installed. But we tested them, and they don’t work. We recently bypassed ClawHub’s malicious skill detector , Cisco’s agent skil…

**Parallel AI Enrichment:**

- **Technical Details:** The scanners rely on superficial checks of skill metadata and code, which can be bypassed by submitting specially crafted skill packages that appear legitimate, enabling credential theft, data exfiltration, and agent hijacking.
- **Affected Products:** ClawHub (OpenClaw skill registry), Cisco agent skill scanner, skills.sh scanners
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** A proof‑of‑concept demonstrating bypass of skill scanners is described in the Trail of Bits blog post.
- **Patch Available:** Patches are available for some CVEs related to the reported issues; specific patch URLs not provided.
- **Active Exploitation:** Confirmed active exploitation reported in the wild, with thousands of insecure instances identified.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — Google June 2026 Android Update Patches 124 Flaws, One Actively Exploited

**CVE:** `CVE-2025-48595` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-02
**Reference:** <https://thehackernews.com/2026/06/google-june-2026-android-update-patches.html>

> Google on Monday released patches for 124 security vulnerabilities impacting its Android operating system for the month of June 2026, including one high-severity flaw in the Framework component that has come under active exploitation.

Tracked as CVE-2025-48595 (CVSS score: 8.4), the security flaw has been described as a case of privilege escalation without requiring any user interaction. The

**Parallel AI Enrichment:**

- **Technical Details:** Elevation‑of‑privilege (EoP) in the Android Framework allowing local code execution/privilege escalation via an integer overflow leading to code execution without user interaction.
- **Affected Products:** Android 14, Android 15, Android 16, Android 16‑qpr2
- **CVSS Score:** 8.4
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC found
- **Patch Available:** Patch released in June 2026; security patch level 2026-06-05 or later addresses CVE-2025-48595. Advisory: https://source.android.com/docs/security/bulletin/2026/2026-06-01
- **Active Exploitation:** Yes — limited, targeted active exploitation has been reported in June 2026.
- **Threat Actors:** None known
- **Mitigation:** Install security patch level 2026-06-05 or later; limit untrusted local access to devices, avoid installing untrusted apps, lock device, restrict developer options/ADB. No other vendor workaround published.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2026/2026-06-01

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when AI systems process external content (webpages, emails, documents) that contain malicious instructions; if the model follows those instructions instead of the user's intent it can perform undesired actions (e.g., data exfiltration, destructive commands). Attackers seed poisoned content on the web or other sources; detection uses signature scanning, LLM intent classification, and manual review.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit reported; Google observed low-sophistication experiments on public websites (examples in blog) but did not report a public PoC URL.
- **Patch Available:** No official vendor "patch" reported; Google describes defenses and ongoing hardening (links to blog posts but not a patch).
- **Active Exploitation:** Google found real-world instances on public web pages—mostly low-sophistication pranks, SEO, deterrence, and a small number of data-exfiltration/destructive experiments. They reported an observed 32% relative increase in malicious-category detections between Nov 2025 and Feb 2026 but did not describe widespread, productionized exploitation.
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses — input filtering/pattern matching for known IPI signatures, LLM‑based classification of candidate content, human validation for high‑confidence cases, model hardening and safeguards (Google’s red teams and AI Vulnerability Reward Program). See Google Workspace mitigation blog and Google Security post.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when malicious instructions are embedded in external data sources or tools the LLM uses during query completion, causing the model to follow attacker‑written directives without user input; mitigations focus on preventing ingestion/execution of such instructions via provenance tracking, input/output filtering, and strict tool policies.
- **Affected Products:** Google Workspace with Gemini integrations
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** None known
- **Patch Available:** Not applicable — mitigations are architectural and layered defenses described in the advisory; no single patch URL beyond the advisory.
- **Active Exploitation:** No confirmed active exploitation reported in the advisory.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses including data sanitization, provenance‑aware retrieval, model instruction guarding, tool access controls, developer hardening, continuous monitoring and red‑team testing as described in the advisory.
- **Vendor Advisory:** http://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is the primary threat: attacker-controlled web content or third‑party content can supply inputs that influence an agentic browser or embedded LLM agents, causing them to execute unintended instructions or disclose sensitive data. Chrome describes architectural mitigations including prompt sanitization boundaries, content provenance checks, least‑privilege agent architectures, and restricted actions for agentic capabilities.
- **Affected Products:** Chrome (agentic browsing / Gemini integration)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC or weaponized exploit published (None known)
- **Patch Available:** Mitigations and new security features announced by Chrome (see vendor advisory); official vendor patch/advisory URL: https://blog.google/security/architecting-security-for-agentic
- **Active Exploitation:** No confirmed reports of active exploitation in the wild (None reported)
- **Threat Actors:** None known
- **Mitigation:** Short‑term mitigations include restricting agentic browsing privileges, enforcing strong content provenance and sanitization, whitelisting trusted sources, and instrumenting prompt/response filtering; follow Chrome's recommended hardening in the vendor post.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit available.
- **Patch Available:** Security patches addressing the issues are available in the Android Security Bulletin: http://source.android.com/docs/security/bulletin/2026/2026-06-01
- **Active Exploitation:** Limited, targeted exploitation reported for CVE-2025-48595 (as noted in the Android Security Bulletin).
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack where adversaries embed hidden or malicious instructions within external data sources (emails, documents, calendar invites, web pages) that are later ingested by an instruction‑following LLM or agent. The LLM may follow those instructions (e.g., exfiltrate data or perform unauthorized actions) if defenses aren't applied.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept or weaponized exploit is reported.
- **Patch Available:** No vendor patch is available; the advisory only describes mitigation steps.
- **Active Exploitation:** Reports of increased IPI attempts have been noted, but no confirmed active exploitation of a specific vulnerability is reported.
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses as described by Google: validate and harden external data sources, sanitize inputs, scope instructions and outputs, apply least‑privilege access for agents, enforce policy checks and runtime monitoring, and use specialized detection for IPI.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors modify routers to gain persistent, long‑term access and leverage compromised devices and trusted connections to pivot into other networks.
- **Affected Products:** Major backbone routers, provider edge (PE) routers, and customer edge (CE) routers across telecommunications, government, transportation, lodging, and military infrastructure networks
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC is available; PoC URL unavailable.
- **Patch Available:** Patch availability varies by vendor; see vendor security advisories referenced in the CISA advisory.
- **Active Exploitation:** Yes — CISA reports PRC state‑sponsored actors targeting and maintaining persistent access globally (CISA AA25-239A; SecurityWeek reporting).
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Harden network devices, monitor for unauthorized configuration changes, segment networks, restrict management‑plane access, apply vendor updates, rotate credentials, implement logging/telemetry and IDS/IPS – see CISA AA25-239A for specifics.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** The campaign used spearphishing with malicious attachments or links, Outlook NTLM relay via specially crafted calendar invites (CVE‑2023‑23397) to capture NTLM hashes, Roundcube exploits to execute shell commands and access mailboxes, WinRAR arbitrary code execution via crafted archives (CVE‑2023‑38831), exploitation of internet‑facing applications and VPNs, and leveraged tools such as Impacket and PsExec, RDP, credential harvesting, AD dumping, and OpenSSH for exfiltration.
- **Affected Products:** Roundcube Webmail (versions before 1.4.4, 1.2.13, 1.3.x before 1.3.16, 1.4.x before 1.4.10), WinRAR (affected version per CVE‑2023‑38831), Microsoft Outlook (CVE‑2023‑23397)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public weaponization of CVE‑2023‑23397 and other CVEs is documented; Microsoft provides detection scripts (aka.ms/CVE-2023-23397ScriptDoc). Specific PoC URLs are not listed in the advisory.
- **Patch Available:** Patch information is available for the individual CVEs (e.g., Microsoft patches for CVE‑2023‑23397, RARLAB updates for CVE‑2023‑38831, Roundcube patches for its CVEs). No single consolidated patch URL is provided in the CSA.
- **Active Exploitation:** Yes — the CSA reports confirmed active exploitation of CVE‑2023‑23397, Roundcube CVEs, and CVE‑2023‑38831 by GRU unit 26165.
- **Threat Actors:** GRU Unit 26165 (APT28 / Fancy Bear / Forest Blizzard / Blue Delta)
- **Mitigation:** Employ network segmentation and Zero Trust, block and alert on NTLM/SMB to external infrastructure, enable endpoint detection and response (EDR), apply Windows attack surface reduction rules, disable or strictly control PowerShell scripting, implement application allow‑listing, enforce MFA, patch IP cameras and firmware, disable UPnP/P2P, use VPN for remote camera access, and monitor logs for IOCs.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 11. 🟠 Zero-Day — Acer working to patch max severity zero-days in Wave 7 routers

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://www.bleepingcomputer.com/news/security/acer-warns-of-max-severity-zero-days-affecting-wave-7-routers/>

> Acer is working to address two maximum-severity zero-day vulnerabilities affecting its Wave 7 mesh routers. [...]

---

## 12. 🟠 Zero-Day — Beyond the Zero-Day: See Your Network Like an Attacker | Webinar with HD Moore

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://thehackernews.com/2026/06/beyond-zero-day-see-your-network-like.html>

> Assume the breach. Zero-days keep shipping, AI is writing exploits faster than anyone patches, and &quot;patch everything in time&quot; stopped working years ago. Stop betting the org on winning that race. You don&#x27;t control which bug lands. You control what it can reach once it does.

That is a question about the shape of your network, and most teams have the shape wrong. HD Moore, creator of…

---

## 13. 🟠 Zero-Day — Unpatched Windows Search URI Vulnerability Lets Attackers Steal NTLMv2 Hashes

**CVE:** `CVE-2026-33829` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://thehackernews.com/2026/06/unpatched-windows-search-uri.html>

> Cybersecurity researchers have disclosed details of an unpatched issue that could be exploited to disclose a user&#x27;s NTLMv2 hash to the attacker.

Like in the case of CVE-2026-33829, which impacted the Windows Snipping Tool&#x27;s ms-screensketch: URI handler, the newly flagged issue resides in the search: URI handler, per Huntress.

CVE-2026-33829 refers to a spoofing vulnerability that could…

---

## 14. 🟠 Zero-Day — Microsoft Tries to Calm Legal Threat Fears After Zero-Day Disclosure Backlash

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://www.securityweek.com/microsoft-tries-to-calm-legal-threat-fears-after-zero-day-disclosure-backlash/>

> Microsoft responds to backlash over its threats of legal action against researchers who publicly disclose zero-day vulnerabilities. The post Microsoft Tries to Calm Legal Threat Fears After Zero-Day Disclosure Backlash appeared first on SecurityWeek .

---

## 15. 🟠 Zero-Day — VS Code zero-day lets hackers steal GitHub tokens in one click

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://www.bleepingcomputer.com/news/security/vs-code-zero-day-lets-hackers-steal-github-tokens-in-one-click/>

> A security researcher has released exploit code for a Visual Studio Code (VS Code) zero-day vulnerability that allows attackers to steal GitHub authentication tokens by tricking users into clicking a link. [...]

---

## 16. 🟡 High Severity — Critical Kirki flaw exploited to hijack WordPress admin accounts

**CVE:** `CVE-2026-8206` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-02
**Reference:** <https://www.bleepingcomputer.com/news/security/critical-kirki-flaw-exploited-to-hijack-wordpress-admin-accounts/>

> Hackers are exploiting a critical privilege escalation vulnerability (CVE-2026-8206) in the Kirki plugin for WordPress to take over any user account, including those belonging to administrators. [...]

---

## 17. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
