# Zero Day Pulse

> **Generated:** 2026-06-21 13:45 UTC &nbsp;|&nbsp; **Total:** 13 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 9 &nbsp;|&nbsp; 🟡 High: 4 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path traversal vulnerability in SimpleHelp Remote Monitoring and Management (versions ≤5.5.7) that enables unauthenticated attackers to read sensitive files by crafting malicious file paths.
- **Affected Products:** SimpleHelp remote support software 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit known
- **Patch Available:** Patch released; see Broadcom security bulletin: http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability
- **Active Exploitation:** Confirmed active exploitation by ransomware actors, as reported by CISA.
- **Threat Actors:** Ransomware actors (generic)
- **Mitigation:** Update SimpleHelp to a version newer than 5.5.7 (apply the vendor patch released shortly after discovery) and restrict external access to the RMM interface.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) – an adversary places malicious prompt‑style content on web resources or documents that an AI agent later browses or ingests. When the agent processes this content, the injected instructions can alter model behavior (e.g., exfiltrate data or execute unintended actions). GeminiJack demonstrates a zero‑click IPI against Google Gemini Enterprise via content the agent accessed.
- **Affected Products:** Google Gemini Enterprise (agent browsing/ingestion features); other web‑browsing/agent‑enabled LLM systems
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Public disclosure of the GeminiJack zero‑click IPI by Noma Labs (details at http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability). No public PoC code released.
- **Patch Available:** Vendor mitigation guidance published in the advisory (see vendor advisory URL). No separate patch download URL.
- **Active Exploitation:** Confirmed in‑the‑wild exploitation reported by Forcepoint (10 IPI payloads) and Noma Labs (GeminiJack).
- **Threat Actors:** None known
- **Mitigation:** Follow vendor guidance: restrict or sanitize web‑browsing/ingestion sources for agents; implement content filtering and input sanitization; use allow‑lists/block‑lists for external content; enforce least‑privilege access for agent capabilities; monitor agent outputs for anomalous instructions and exfiltration; keep security updates applied.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) inserts malicious instructions into data sources or tools consumed by LLMs (e.g., emails, docs, web content, code snippets). These instructions can influence agentic LLM behavior without direct user input by being fetched as part of multi-source context during query completion.
- **Affected Products:** Google Workspace (features integrating Gemini and multi-source agentic workflows)
- **CVSS Score:** -999.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** None known (no public PoC reported in the advisory)
- **Patch Available:** Not applicable — this is a mitigation/defense guidance post rather than a software patch; no single “patch” URL beyond the advisory guidance.
- **Active Exploitation:** None confirmed in the advisory; prior research notes IPI payloads observed in the wild, but no confirmed targeted exploitation of a specific Workspace vulnerability.
- **Threat Actors:** None known
- **Mitigation:** Multi‑layered defenses per Google advisory — continuous monitoring, input/output validation and sanitization, metadata provenance checks, hardened tool access controls, human review gates, and ongoing web sweeps for IPI patterns.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection in Gemini Enterprise enables an attacker to craft input that the AI model interprets as a command, leading to unintended actions such as local file reads or credential leakage.
- **Affected Products:** Google Chrome (Gemini component), fixed in version 1.3
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC disclosed by Noma Labs (see citations).
- **Patch Available:** Patch released by Google; details in the Unit42 analysis and NVD entry.
- **Active Exploitation:** Confirmed active exploitation reported; see Forcepoint X‑Labs blog.
- **Threat Actors:** None known
- **Mitigation:** Apply the Google‑provided patch (see Unit42/NVD); enable the new security architecture introduced in the blog post; restrict AI agent permissions and validate inputs.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Integer overflow in Android Framework leading to possible code execution/local privilege escalation.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 8.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or widely shared weaponized exploit reported; limited targeted exploitation in the wild. No public PoC URL found.
- **Patch Available:** Yes — Google released fixes in the June 2026 Android Security Bulletin.
- **Active Exploitation:** Confirmed limited/targeted active exploitation reported by Google and multiple security news outlets.
- **Threat Actors:** None known
- **Mitigation:** Install June 2026 Android security updates from device OEMs/carriers or apply vendor‑provided patches; restrict untrusted apps and follow least‑privilege app policies.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection embeds malicious instructions in external data sources (emails, documents, calendar invites, web pages, image metadata, etc.) that LLMs ingest; when the model reads such content it can treat hidden instructions as part of its prompt and execute actions like data exfiltration or performing operations (e.g., deleting calendar events) unless defenses block or sanitize the content.
- **Affected Products:** Gemini (Gemini app and Gemini in Workspace)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit reported in the vendor advisory; PoC unavailable
- **Patch Available:** Not applicable in traditional patch sense; vendor implemented model hardening and product‑level mitigations (see vendor advisory URL)
- **Active Exploitation:** No confirmed active exploitation reported in the vendor advisory.
- **Threat Actors:** None known
- **Mitigation:** Defense-in-depth — model hardening (Gemini 2.5 adversarial training), purpose‑built ML classifiers to detect malicious instructions, markdown sanitization, suspicious URL detection (Safe Browsing), system‑level safeguards requiring user confirmation for risky actions, end‑user security notifications, logging, red‑teaming, output validation and restricting agent actions; see vendor advisory for details and help center links.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors target backbone and edge routers, modify firmware/configurations to maintain long‑term persistent access, and leverage compromised devices and trusted connections to pivot into other networks for espionage.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept or weaponized exploit is listed in the advisory.
- **Patch Available:** No single vendor patch covers this advisory; mitigation guidance and vendor‑specific advisories are referenced in the CISA advisory.
- **Active Exploitation:** Yes – the advisory reports confirmed global exploitation of telecommunications backbone, provider edge (PE) and customer edge (CE) routers, and use of compromised devices to pivot.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Follow CISA hardening and mitigation steps: isolate and segment network, inventory and validate router configurations, rotate credentials, apply vendor firmware updates where available, remove unauthorized modifications, monitor for persistence indicators, apply network detection rules and block malicious infrastructure.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** APT28 (85th GTsSS, Unit 26165) targets organizations coordinating foreign assistance to Ukraine using: (1) spearphishing — Outlook 'MonikerLink' NTLM credential leakage via CVE-2023-23397; (2) Roundcube Webmail exploitation via CVE-2020-12641 (pre-1.4.4 RCE), CVE-2020-35730 (XSS), and CVE-2021-44026; (3) WinRAR archive spoofing via CVE-2023-38831; (4) credential guessing/brute force; (5) Microsoft Exchange mailbox permission modification for persistence; (6) exploitation of internet-facing corporate VPN appliances and SQL injection; (7) lateral movement using legitimate utilities (PSEXEC, ntdsutil, wevtutil, vssadmin); (8) abuse of trust relationships with business partners; (9) reconnaissance of ICS components in railway management; and (10) abuse of compromised SOHO routers and internet-connected IP cameras at ports/border crossings to monitor aid shipments. Indicators include YARA rule 'GENERIC_PSEXEC' and domains *.accesscam[.]org and *.giize[.]com (giize[.]org also reported).
- **Affected Products:** Target SECTORS (not single products): Western logistics entities, transportation/transit hubs, ports/airports, maritime, air-traffic management, IT services, defense industry. SECTOR-RELEVANT SOFTWARE (exploited in the campaign): Microsoft Outlook (pre-March 2023 patch — CVE-2023-23397); Roundcube Webmail before 1.4.4 (CVE-2020-12641), and additional Roundcube CVEs CVE-2020-35730 and CVE-2021-44026; RARLAB WinRAR before 6.23 (CVE-2023-38831). Also referenced attack surface: SOHO routers, internet-connected IP cameras, internet-exposed corporate VPN appliances, and Microsoft Exchange servers.
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** YES — confirmed weaponized in-the-wild exploitation. Independent detections reported by Microsoft Security Intelligence (https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Exploit:Win32/CVE-2023-38831) and SocPrime (https://socprime.com/blog/cve-2020-35730-cve-2021-44026-cve-2020-12641-exploit-detection-apt28-group-abuses-roundcube-flaws-in-spearphishing-espionage-attacks/).
- **Patch Available:** YES — patches exist for all referenced CVEs. Microsoft Outlook: March 2023 cumulative update (https://www.microsoft.com/en-us/msrc/blog/2023/03/microsoft-mitigates-outlook-elevation-of-privilege-vulnerability, https://nvd.nist.gov/vuln/detail/CVE-2023-23397). Roundcube Webmail: 1.4.4+ for CVE-2020-12641 and later releases for CVE-2020-35730 and CVE-2021-44026 (https://nvd.nist.gov/vuln/detail/cve-2020-12641). WinRAR: 6.23+ (https://nvd.nist.gov/vuln/detail/cve-2023-38831).
- **Active Exploitation:** YES — confirmed, ongoing, and documented. AA25-141A states the Russian GRU 85th GTsSS (Unit 26165) has been conducting this campaign since 2022 against dozens of Western logistics entities and IT companies across NATO member states, Ukraine, and international organizations. Reporting sources: CISA, FBI, NSA/DoD, ACSC Australia, plus Microsoft Security Intelligence and SocPrime for the specific CVE-chain weaponization.
- **Threat Actors:** APT28 (aka Fancy Bear, Forest Blizzard, BlueDelta, Strontium, Sednit, Sofacy) — Russian GRU 85th Main Special Service Center (85th GTsSS), military unit 26165
- **Mitigation:** Enforce phishing-resistant MFA (FIDO/certificate-based) on all accounts, especially privileged/management accounts; require strong unique passwords and disable legacy/password-only auth; block/replace unhardened SOHO routers and IoT devices; disable UPnP, peer-to-peer, and 'Anonymous Visit' features on IP cameras and routers; disable unused services such as FTP and web admin interfaces; enable authenticated RTSP only; audit and tune IP camera user accounts; configure and monitor logs on cameras and perimeter devices; segment business-critical networks from perimeter/IoT; apply all relevant vendor patches (Outlook CVE-2023-23397, WinRAR 6.23+, Roundcube 1.4.4+); and block/detect APT28 IOCs including *.accesscam[.]org and *.giize[.]com.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** A stack‑based buffer overflow (CWE‑121) in the NSPI RPC interface of Windows Active Directory Domain Services allows a domain‑authenticated attacker to provide crafted inputs that cause an out‑of‑bounds write, corrupt memory, and achieve remote code execution with low attack complexity and no user interaction.
- **Affected Products:** Windows Active Directory Domain Services
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit or PoC is known.
- **Patch Available:** Yes, a patch has been released. See the Microsoft advisory URL for details.
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Apply the Microsoft security update for CVE-2026-45648 as provided in the advisory. If immediate patching is not possible, restrict network access to the NSPI RPC interface and enforce strong domain authentication.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45648

---

## 10. 🟡 High Severity — SEC Consult SA-20260618-0 :: Hardcoded Root Cloud Credentials in Application Binaries in Silver Leaf Technologies - Worksnaps.net Worksnaps

**CVE:** `CVE-2025-10560` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-06-21
**Reference:** <https://seclists.org/fulldisclosure/2026/Jun/21>

> Posted by SEC Consult Vulnerability Lab via Fulldisclosure on Jun 20 SEC Consult Vulnerability Lab Security Advisory &lt; 20260618-0 &gt; ======================================================================= title: Hardcoded Root Cloud Credentials in Application Binaries product: Silver Leaf Technologies - Worksnaps.net Worksnaps vulnerable version: &lt; 1.6.20260201 fixed version: 1.6.20260201 …

**Parallel AI Enrichment:**

- **Technical Details:** Multiple Worksnaps client binaries contain hard‑coded AWS access keys and S3 bucket names. An attacker can decompile the .NET binaries (e.g., procUploadDirect.net45.v2.exe) to extract these credentials and then use AWS CLI or SDKs to access the vendor's production S3 buckets, potentially retrieving user screenshots and other data. The vulnerability is mitigated in version 1.6.20260201 by removing the embedded credentials and switching to presigned upload URLs.
- **Affected Products:** Worksnaps client (Windows) versions < 1.6.20260201
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof‑of‑concept techniques published in the SEC Consult advisory and GitHub Advisory.
- **Patch Available:** Patch available: vendor provides patched client version 1.6.20260201 (or higher). Download at https://www.worksnaps.net/www/download.shtml
- **Active Exploitation:** No confirmed active exploitation in the wild.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟡 High Severity — SEC Consult SA-20260617-0 :: Multiple Critical Vulnerabilities in Sprecher Automation SPRECON-E-C/-E-P/-E-T3

**CVE:** `CVE-2022-4333` | `CVE-2022-4332` | `CVE-2025-41741` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-06-21
**Reference:** <https://seclists.org/fulldisclosure/2026/Jun/19>

> Posted by SEC Consult Vulnerability Lab via Fulldisclosure on Jun 20 SEC Consult Vulnerability Lab Security Advisory &lt; 20260617-0 &gt; ======================================================================= title: Multiple Critical Vulnerabilities product: Sprecher Automation SPRECON-E-C/-E-P/-E-T3 vulnerable version: See vulnerable versions below fixed version: See solution section below CVE n…

---

## 12. 🟡 High Severity — CVE-2025-68624: Cross-Tenant Authentication Bypass by Spoofing in N-able Mail Assure

**CVE:** `CVE-2025-68624` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-06-21
**Reference:** <https://seclists.org/fulldisclosure/2026/Jun/10>

> Posted by Alessandro Bertoldi BCS via Fulldisclosure on Jun 20 CVE-2025-68624: Cross-Tenant Authentication Bypass by Spoofing in N-able Mail Assure CVE ID: CVE-2025-68624 Status: DISPUTED CWE: CWE-290 (Authentication Bypass by Spoofing) Affected Product: N-able Mail Assure (formerly SolarWinds MSP Mail Assure) Affected Service: N-able Mail Assure cloud-based multi-tenant SMTP relay infrastructure …

---

## 13. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
