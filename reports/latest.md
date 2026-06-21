# Zero Day Pulse

> **Generated:** 2026-06-21 19:14 UTC &nbsp;|&nbsp; **Total:** 13 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 9 &nbsp;|&nbsp; 🟡 High: 4 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability enables attackers to traverse directories and read sensitive files on SimpleHelp Remote Support installations by supplying malicious path sequences.
- **Affected Products:** SimpleHelp Remote Support Software version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (unspecified)
- **Mitigation:** Apply the vendor‑provided patch/update to SimpleHelp version >5.5.7; if patching is not immediately possible, limit remote RMM access, enforce least‑privilege accounts, and monitor for abnormal file read activity.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) involves adversarial content on the web (e.g., hidden page elements, crafted text or comments) that is retrieved by an AI agent and causes it to follow attacker‑supplied instructions, leading to data leakage or undesired actions.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Input/output validation and sanitization; implement human oversight and controls for LLM use; monitor public web for IPI payloads; apply vendor hardening guidance.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** An indirect prompt injection (IPI) injects malicious instructions into the data or tools used by a large language model (LLM), influencing the LLM’s output without direct user interaction. GeminiJack is a zero‑click IPI exploit targeting Google Gemini integrated in Google Workspace, allowing an attacker to control Gemini’s behavior by manipulating the information it accesses.
- **Affected Products:** Google Workspace (Gemini integration)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability)
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Implement continuous monitoring for suspicious content, sanitize inputs and data sources accessed by Gemini, restrict agentic automation, and apply defense‑in‑depth controls to limit the impact of injected prompts.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection in Chrome's Gemini agentic browsing permits a malicious web page to craft inputs that are interpreted as commands by the AI agent, enabling actions such as local file access or privacy‑invasive behavior.
- **Affected Products:** Google Chrome (Gemini agentic browsing feature)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Enable the new security architecture for Gemini agentic browsing as outlined by Google, which adds isolation and validation layers to mitigate indirect prompt injection.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Multiple locations in the Android System component contain an incorrect bounds check that enables out-of-bounds (OOB) memory access. When chained with other bugs, this can lead to remote code execution (RCE) without user interaction and without requiring additional execution privileges. The bug is classified as CWE-125 (Out-of-bounds Read). Google highlights the specific instance as a linear buffer overflow in the Rust-based CrabbyAVIF image parser that was caught by Rust's memory-safety checks within unsafe FFI/hardware code before the code shipped to a public release, illustrating Rust's value in shifting vulnerability detection left.
- **Affected Products:** Google Android 16.0, Google Android (earlier versions), Android System component (including CrabbyAVIF Rust AVIF parser)
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true - https://source.android.com/docs/security/bulletin/2025-08-01
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the 2025-08-01 / 2025-08-05 Android Security Patch Level (i.e., the August 2025 Android Security Bulletin) on all affected Android devices. Defensive hardening if patching cannot be applied immediately: keep devices updated, enable Google Play Protect, deploy mobile device management (MDM) and mobile threat defense (MTD) to enforce patch levels, restrict network exposure of system services, and monitor for anomalous system-level activity / privilege-escalation attempts. For Rust-based code paths, minimize unsafe blocks and use Scudo guard pages so silent memory corruption is converted into detectable crashes.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** OS command injection in the MobileIron Configuration Service web portal allowing an unauthenticated remote attacker to execute arbitrary OS commands as root via crafted requests to vulnerable endpoints.
- **Affected Products:** Ivanti Sentry (MobileIron Configuration Service) – versions before R10.5.2, R10.6.2, and R10.7.1
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true - https://enigma-global.com/reports/cve-2026-10520-critical-ivanti-sentry-os-command-injection-actively-exploited-mqaltqap-twhb; https://horizon3.ai/attack-research/vulnerabilities/cve-2026-10520
- **Patch Available:** true - https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523?language=en_US
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply Ivanti‑provided updates to reach R10.5.2 / R10.6.2 / R10.7.1 or later; if patching is delayed, restrict access to the MICS web interface (network segmentation, firewall rules, VPN‑only access), disable/unexpose the service from the internet, and monitor logs for suspicious commands and indicators.
- **Vendor Advisory:** https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523?language=en_US

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors modify routers to maintain persistent, long‑term access and leverage compromised devices and trusted connections to pivot into other networks.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** People’s Republic of China (PRC) state-sponsored cyber threat actors
- **Mitigation:** Apply the latest firmware updates, segment network zones, monitor router configuration changes, disable unnecessary services, and enforce strict access controls on router management interfaces.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS), military unit 26165
- **Mitigation:** Follow CISA's recommended mitigations in the advisory (network segmentation, multi-factor authentication, monitoring for IOC/TTPs, patching known product vulnerabilities).
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** Microsoft's June 2026 Patch Tuesday addressed 206 CVEs including three publicly disclosed zero-days: (1) CVE-2026-45586 is an improper-link-resolution flaw (CWE-59) in the Windows Collaborative Translation Framework (CTFMON) service allowing an authorized local attacker to elevate privileges to SYSTEM; low-privileged local code execution plus minor user interaction is required. (2) CVE-2026-50507 is a protection-mechanism-failure (CWE-693) bypass in Windows BitLocker Device Encryption — an unauthenticated attacker with physical access to a powered-off or sleeping machine can defeat BitLocker pre-boot authentication and decrypt the disk; the underlying weakness lies in how the Windows Recovery Environment (WinRE) and pre-boot auth handle certain inputs (documented by researcher 'Chaotic Eclipse' under the YellowKey/GreenPlasma research, May–June 2026). (3) CVE-2026-49160 is an uncontrolled-resource-consumption (CWE-400) flaw in the HTTP/2 implementation of the kernel-mode HTTP driver (HTTP.sys): an unauthenticated remote attacker can send crafted HTTP/2 frames to exhaust resources and cause the target Windows host to deny service.
- **Affected Products:** Microsoft Windows (Windows 10, Windows 11, Windows Server 2022/2025), Microsoft Office, Microsoft Extended Security Updates (ESU), Azure, HTTP.sys, BitLocker, Windows Collaborative Translation Framework (CTFMON), Windows Kernel, Visual Studio, and SharePoint. The three zero-days specifically affect: (1) CVE-2026-45586 — Windows Collaborative Translation Framework (CTFMON) on supported Windows 10, Windows 11, and Windows Server releases; (2) CVE-2026-50507 — Windows BitLocker on Windows 10, Windows 11, and Windows Server 2022/2025; (3) CVE-2026-49160 — HTTP.sys on Windows 10 (including 1607), Windows 11, and Windows Server editions shipping the HTTP/2-capable kernel-mode HTTP driver.
- **CVSS Score:** 7.5 (CVE-2026-49160, HTTP.sys DoS — per NVD), 6.8 (CVE-2026-45586, CTFMON EoP — per Tenable, Medium), and approximately 6.8 for CVE-2026-50507 (BitLocker bypass with physical access vector). Additional Critical RCE CVEs in this release carry CVSS 9.8 (per Brinqa analysis).
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H (CVE-2026-49160, HTTP.sys DoS). CVE-2026-50507 (BitLocker bypass): CVSS:3.1/AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H (physical access, low complexity, no privileges, high CIA impact). CVE-2026-45586 (CTFMON EoP): CVSS:3.1/AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H (local, low complexity, low privileges, user interaction required).
- **Exploit Available:** true. Public PoC code and technical write-ups exist, particularly for the BitLocker bypass CVE-2026-50507. PoC sources include: https://threat-modeling.com/windows-bitlocker-yellowkey-bypass-cve-2026-45585/ and http://aviatrix.ai/threat-research-center/windows-bitlocker-zero-day-yellowkey-greenplasma-2026 (Chaotic Eclipse's YellowKey/GreenPlasma research, May–June 2026). The other two zero-days (CVE-2026-45586 CTFMON EoP and CVE-2026-49160 HTTP.sys DoS) were also publicly disclosed before patches were available.
- **Patch Available:** true. Microsoft released patches for CVE-2026-45586, CVE-2026-50507, CVE-2026-49160, and the additional 203 CVEs as part of the June 2026 Patch Tuesday on 9 June 2026. Advisory URLs: https://msrc.microsoft.com/update-guide/releaseNote/2026-Jun (consolidated), https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45586, https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50507, https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-49160.
- **Active Exploitation:** false. As of the 9 June 2026 Patch Tuesday, none of the three zero-days (CVE-2026-45586, CVE-2026-50507, CVE-2026-49160) had been observed being exploited in the wild. Microsoft's MSRC tags each as 'Publicly Disclosed' rather than 'Exploited', and CrowdStrike's June 9, 2026 Patch Tuesday analysis concludes 'No evidence in the wild' for all three. Reporting from CyberScoop and Redmondmag confirms these flaws were publicly known at release time but not actively weaponized.
- **Threat Actors:** None known. Microsoft's June 2026 release notes tag all three zero-days (CVE-2026-45586, CVE-2026-50507, CVE-2026-49160) as 'Publicly Disclosed' rather than 'Exploited'. CrowdStrike's June 9, 2026 analysis concludes 'No evidence in the wild' for all three, and reporting from CyberScoop and Redmondmag confirms the flaws were publicly known at release time but not actively weaponized by named threat actors.
- **Mitigation:** 1. Apply the June 2026 Microsoft security updates immediately (released 9 June 2026) — install the relevant KB for your Windows build (e.g. KB5094126 on Windows 11 24H2/25H2 for OS Builds 26200.8655 and 26100.8655), plus BitLocker, Office, SharePoint, and Visual Studio updates as applicable. 2. For CVE-2026-49160 (HTTP.sys) hardening prior to or alongside patching, set the MaxHeadersCount registry value under the HTTP/2 and HTTP/3 parameters (e.g. HKLM\SYSTEM\CurrentControlSet\Services\HTTP\Parameters) to cap headers accepted per HTTP/2/HTTP/3 request. 3. For CVE-2026-50507 (BitLocker): enforce strong physical-access controls (locked server rooms, BIOS/UEFI passwords, port/disk disablement), enable TPM + PIN pre-boot authentication where supported, and consider BitLocker Network Unlock as an additional layer. 4. For CVE-2026-45586 (CTFMON EoP): restrict who can log on interactively to Windows hosts, enforce least-privilege accounts, and monitor for unexpected CTFMON.exe child processes spawning SYSTEM-level activity.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/releaseNote/2026-Jun

---

## 10. 🟡 High Severity — SEC Consult SA-20260618-0 :: Hardcoded Root Cloud Credentials in Application Binaries in Silver Leaf Technologies - Worksnaps.net Worksnaps

**CVE:** `CVE-2025-10560` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-06-21
**Reference:** <https://seclists.org/fulldisclosure/2026/Jun/21>

> Posted by SEC Consult Vulnerability Lab via Fulldisclosure on Jun 20 SEC Consult Vulnerability Lab Security Advisory &lt; 20260618-0 &gt; ======================================================================= title: Hardcoded Root Cloud Credentials in Application Binaries product: Silver Leaf Technologies - Worksnaps.net Worksnaps vulnerable version: &lt; 1.6.20260201 fixed version: 1.6.20260201 …

**Parallel AI Enrichment:**

- **Technical Details:** Several Worksnaps client binaries contained hardcoded AWS access keys, secret keys, and S3 bucket names. Attackers can extract these credentials (e.g., using ILSpy and string analysis) to list S3 buckets, download screenshots, enumerate EC2 instances, and obtain comprehensive access to the AWS account. The vendor removed the credentials from binaries and switched to server‑side retrieval with pre‑signed URLs.
- **Affected Products:** Worksnaps (Windows client) versions < 1.6.20260201
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true (https://seclists.org/fulldisclosure/2026/Jun/21)
- **Patch Available:** true (https://www.worksnaps.net/www/download.shtml, advisory: https://sec-consult.com/vulnerability-lab/)
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Install patched client version 1.6.20260201 or later; rotate any exposed AWS credentials and review the AWS account for misuse; apply vendor server‑side fixes; perform a thorough security review.
- **Vendor Advisory:** https://sec-consult.com/vulnerability-lab/

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
