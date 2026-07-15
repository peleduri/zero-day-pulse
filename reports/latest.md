# Zero Day Pulse

> **Generated:** 2026-07-15 13:09 UTC &nbsp;|&nbsp; **Total:** 41 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 24 &nbsp;|&nbsp; 🟡 High: 17 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Improve Router Hygiene to Protect Against Russian State-Sponsored Targeting

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Wed, 08 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a>

> Russian Government-Sponsored Activity Targets Poorly Configured and Vulnerable Devices Across Critical Sectors Executive summary Russian Federal Security Service (FSB) Center 16 cyber actors continue to exploit poorly configured and vulnerable networking devices worldwide, opportunistically compromising multiple critical infrastructure sector networks. This joint Cybersecurity Advisory (CSA) build…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability involves the exploitation of poorly configured and vulnerable networking devices, utilizing outdated protocols (specifically SNMPv1 and SNMPv2), default credentials, and features such as Cisco Smart Install.
- **Affected Products:** Networking devices (e.g., Cisco routers with Smart Install enabled).
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) was explicitly mentioned, but active exploitation by state-sponsored actors is reported.
- **Patch Available:** Organizations are urged to upgrade software and firmware images to patch vulnerabilities (as recommended in CISA AA26-194A).
- **Active Exploitation:** Confirmed active exploitation in the wild by Russian government-sponsored actors as reported by CISA, NSA, and the FBI in advisory AA26-194A.
- **Threat Actors:** Russian Federal Security Service (FSB) Center 16
- **Mitigation:** Key hardening measures include: implementing SNMPv3, disabling SNMPv1 and SNMPv2, using strong and unique passwords, disabling Cisco Smart Install, blocking TFTP, SMI, and SNMP protocols at the firewall, and upgrading software and firmware images.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 2. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path traversal vulnerability allowing unauthenticated remote attackers to download arbitrary files from the SimpleHelp host via crafted HTTP requests. These files may include server configuration files (e.g., serverconfig.xml) containing hashed administrator passwords and secrets such as LDAP credentials, OIDC client tokens, and TOTP seeds.
- **Affected Products:** SimpleHelp remote support software v5.5.7 and before
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** A public proof-of-concept is available on GitHub at http://github.com/imjdl/CVE-2024-57727
- **Patch Available:** Official patches are available in SimpleHelp versions 5.5.8 through 5.5.10 (and up to 5.5.15), with specific patches also released for v5.4.10 and v5.3.9. Downloads are available at https://simple-help.com/downloads.
- **Active Exploitation:** Confirmed active exploitation has been reported by CISA (advisory aa25-163a) and the CISA KEV catalog, with ransomware groups DragonForce and Medusa observed exploiting the vulnerability since January 2025.
- **Threat Actors:** Ransomware groups including DragonForce and Medusa
- **Mitigation:** Upgrade to SimpleHelp v5.5.8 or later; apply patches for v5.4.10 or v5.3.9. Additional hardening includes changing Administrator and Technician passwords, restricting technician/admin login IP addresses, disabling the SimpleHelpAdmin user in favor of Administrator Technician accounts, disabling local technician logins in favor of LDAP/AD, restricting API request IPs, and implementing firewall restrictions on the server.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 3. 🟠 Zero-Day — CISA warns admins to patch actively exploited SharePoint flaws

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-07-15
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-warns-admins-to-patch-actively-exploited-sharepoint-flaws/>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) warned Tuesday that attackers are actively exploiting three vulnerabilities to hack Internet-exposed on-premises SharePoint Server instances. [...]

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerabilities include CVE-2026-45659, a remote code execution (RCE) flaw caused by deserialization of untrusted data; CVE-2026-56164, an elevation of privilege (EoP) flaw caused by missing authentication for a critical function; and CVE-2026-32201, a spoofing flaw caused by improper input validation.
- **Affected Products:** Microsoft SharePoint Server (Subscription Edition, 2019, 2016)
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** Confirmed active exploitation in the wild, but no specific public PoC URL is listed in the provided documentation.
- **Patch Available:** Microsoft has released comprehensive security updates for all supported versions of SharePoint Server (Subscription Edition, 2019, and 2016).
- **Active Exploitation:** Confirmed active exploitation has been reported by CISA, who added CVE-2026-45659 to its Known Exploited Vulnerabilities (KEV) catalog.
- **Threat Actors:** Storm2603-Warlock
- **Mitigation:** CISA urges the hardening of SharePoint instances and the immediate application of official Microsoft security updates.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — Two SonicWall SMA 1000 Zero-Days Exploited, One Could Enable Admin Commands

**CVE:** `CVE-2026-15409` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-15
**Reference:** <https://thehackernews.com/2026/07/two-sonicwall-sma-1000-zero-days.html>

> SonicWall has warned of active exploitation of two zero-day vulnerabilities impacting Secure Mobile Access (SMA) 1000 series appliances, one of which could be exploited to achieve arbitrary command execution.

The vulnerabilities are listed below -


  CVE-2026-15409 (CVSS score: 10.0) - A Server-side request forgery (SSRF) vulnerability that a remote unauthenticated attacker could exploit to

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-15409 is a server-side request forgery (SSRF) in the SMA1000 Appliance Work Place interface that allows a remote, unauthenticated attacker to force the appliance to make requests to unintended locations.
- **Affected Products:** SonicWall Secure Mobile Access (SMA) 1000 Series (including SMA6210, SMA7210, SMA8200v and Central Management Server) — impacted firmware versions reported: 12.4.3-03245, 12.4.3-03387, 12.4.3-03434, 12.5.0-02283, 12.5.0-02624, 12.5.0-02800
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) or exploit code is reported in the SonicWall advisory or CISA entry; the sources confirm active exploitation in the wild but do not publish a public PoC.
- **Patch Available:** Yes — SonicWall published hotfix releases. Vendor guidance: upgrade to the hotfix via MySonicWall (fixed versions reported: 12.4.3-03453 and 12.5.0-02835). See SonicWall advisory / MySonicWall for downloads.
- **Active Exploitation:** Yes — SonicWall PSIRT confirmed multiple incidents and active exploitation; CISA added the CVE to its Known Exploited Vulnerabilities (KEV) catalog.
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor hotfix immediately (via MySonicWall) and perform a thorough forensic analysis to look for indicators of compromise (IoCs) as recommended by SonicWall. (Vendor also lists fixed firmware versions.)
- **Vendor Advisory:** http://sonicwall.com/support/notices/product-notice-sma-1000-series-affected-by-multiple-vulnerabilities/kA1VN000001nv6D0AQ

---

## 5. 🟠 Zero-Day — Patch Tuesday - July 2026

**CVE:** `CVE-2026-55040` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-07-14
**Reference:** <https://www.rapid7.com/blog/post/em-patch-tuesday-july-2026>

> Microsoft is publishing 622 vulnerabilities on July 2026 Patch Tuesday , including a record-breaking 416 Windows vulnerabilities. Microsoft is aware of exploitation in the wild for two of the vulnerabilities published today, both of which are listed on CISA KEV, as well as public disclosure for one other. As usual, browser vulns are not included in the Patch Tuesday count above. Rapid7 noted last …

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-55040 is a critical JWT token authentication bypass vulnerability in Microsoft SharePoint that allows an unauthorized attacker to bypass security features and perform operations against the target SharePoint site as the user they identify as.
- **Affected Products:** Microsoft SharePoint Server Subscription Edition, Microsoft SharePoint Server 2019, Microsoft SharePoint Server 2016
- **CVSS Score:** 9.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N
- **Exploit Available:** A public technical analysis of the authentication bypass is available via Rapid7 at https://www.rapid7.com/blog/post/ve-cve-2026-55040-microsoft-sharepoint-jwt-token-authentication-bypass-fixed/
- **Patch Available:** Patches are available for SharePoint Server Subscription Edition, 2019, and 2016.
- **Active Exploitation:** No confirmed active exploitation has been reported. While Microsoft lists the exploitation status as "Exploitation More Likely," it was not included in the July 2026 Patch Tuesday list of zero-day vulnerabilities with "Exploitation Detected" status.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-55040

---

## 6. 🟠 Zero-Day — SonicWall warns of SMA1000 flaws exploited in zero-day attacks, patch now

**CVE:** `CVE-2026-15409` | `CVE-2026-15410` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-07-14
**Reference:** <https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-sma1000-flaws-exploited-in-zero-day-attacks-patch-now/>

> SonicWall warns that threat actors have been exploiting two SMA1000 vulnerabilities, tracked as CVE-2026-15409 and CVE-2026-15410, in zero-day attacks and urges customers to install the newly released security updates. [...]

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-15409 is a server-side request forgery (SSRF) in the SMA1000 Appliance Work Place interface that allows a remote, unauthenticated attacker to force the appliance to make requests to unintended locations.
- **Affected Products:** SonicWall Secure Mobile Access (SMA) 1000 Series (including SMA6210, SMA7210, SMA8200v and Central Management Server) — impacted firmware versions reported: 12.4.3-03245, 12.4.3-03387, 12.4.3-03434, 12.5.0-02283, 12.5.0-02624, 12.5.0-02800
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) or exploit code is reported in the SonicWall advisory or CISA entry; the sources confirm active exploitation in the wild but do not publish a public PoC.
- **Patch Available:** Yes — SonicWall published hotfix releases. Vendor guidance: upgrade to the hotfix via MySonicWall (fixed versions reported: 12.4.3-03453 and 12.5.0-02835). See SonicWall advisory / MySonicWall for downloads.
- **Active Exploitation:** Yes — SonicWall PSIRT confirmed multiple incidents and active exploitation; CISA added the CVE to its Known Exploited Vulnerabilities (KEV) catalog.
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor hotfix immediately (via MySonicWall) and perform a thorough forensic analysis to look for indicators of compromise (IoCs) as recommended by SonicWall. (Vendor also lists fixed firmware versions.)
- **Vendor Advisory:** http://sonicwall.com/support/notices/product-notice-sma-1000-series-affected-by-multiple-vulnerabilities/kA1VN000001nv6D0AQ

---

## 7. 🟠 Zero-Day — Microsoft Patches Record 622 Flaws, Including Two Zero-Days Under Active Attack

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-14
**Reference:** <https://thehackernews.com/2026/07/microsoft-patches-record-622-flaws.html>

> Microsoft shipped its largest Patch Tuesday on record today, and two of the fixes close holes that attackers are already exploiting. The release covers 622 of Microsoft&#x27;s own CVEs by its Security Update Guide count, more than triple June&#x27;s previous high of around 200.

Those two live bugs are the ones to grab first. Microsoft credits incident responders for both. Both are

**Parallel AI Enrichment:**

- **Technical Details:** Two primary zero-days are highlighted: CVE-2026-56164 is a missing authentication for critical function vulnerability in SharePoint Server allowing remote unauthenticated privilege escalation; CVE-2026-56155 is an AD FS vulnerability allowing local privilege escalation through weak access controls.
- **Affected Products:** Microsoft SharePoint Server, Active Directory Federation Services (AD FS)
- **CVSS Score:** 9.8
- **CVSS Vector:** CVE-2026-56164: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H; CVE-2026-56155: CVSS:3.1/AV:L/AC:L (partial)
- **Exploit Available:** Confirmed active exploitation in the wild; no public PoC URL is provided, though CVE-2026-56164 is reported as being detailed publicly.
- **Patch Available:** Official patches were released as part of the July 2026 Patch Tuesday update.
- **Active Exploitation:** Confirmed by Microsoft and reported by The Hacker News as being actively exploited in the wild.
- **Threat Actors:** None known; however, discovery is credited to Mandiant, Google's FLARE team, and Microsoft's DART unit.
- **Mitigation:** For CVE-2026-56164 (SharePoint), enabling AMSI in Full Mode on the server is recommended to blunt the attack.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/releaseNote/2026-Jul

---

## 8. 🟠 Zero-Day — Microsoft Patches Record 622 Vulnerabilities, Including Two Exploited Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-14
**Reference:** <https://www.securityweek.com/microsoft-patches-record-622-vulnerabilities-including-two-exploited-zero-days/>

> Two flaws in Active Directory and SharePoint Server have been exploited as zero-days, and a BitLocker bug was publicly disclosed. The post Microsoft Patches Record 622 Vulnerabilities, Including Two Exploited Zero-Days appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerabilities include: CVE-2026-56155 (AD FS): Insufficient granularity of access control allowing privilege escalation. CVE-2026-56164 (SharePoint): Missing authentication for a critical function allowing unauthorized network-based privilege escalation. CVE-2026-50661 (BitLocker): Security feature bypass allowing access to encrypted data.
- **Affected Products:** Active Directory Federation Services (AD FS), Microsoft Office SharePoint Server, Windows BitLocker
- **CVSS Score:** 7.8
- **CVSS Vector:** CVE-2026-56155: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H; others unavailable.
- **Exploit Available:** Exploits are known to exist for CVE-2026-56155 and CVE-2026-56164, which were exploited as zero-days.
- **Patch Available:** Yes, official patches were released by Microsoft as part of the July 2026 Patch Tuesday.
- **Active Exploitation:** Confirmed active exploitation in the wild for CVE-2026-56155 and CVE-2026-56164, reported as zero-days by SecurityWeek and the Government of Canada (Cyber.gc.ca).
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-56155, https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-56164, https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50661

---

## 9. 🟠 Zero-Day — Microsoft’s July 2026 Patch Tuesday Addresses 569 CVEs (CVE-2026-56155, CVE-2026-56164)

**CVE:** `CVE-2026-56155` | `CVE-2026-56164` &nbsp;|&nbsp; **Source:** Tenable Security Research &nbsp;|&nbsp; **Published:** 2026-07-14
**Reference:** <https://www.tenable.com/blog/microsofts-july-2026-patch-tuesday-addresses-569-cves-cve-2026-56155-cve-2026-56164>

> 56 Critical 510 Important 3 Moderate 0 Low Microsoft addresses 569 CVEs in the largest Patch Tuesday release yet. This month’s release includes three zero-days, two of which were exploited in the wild. Microsoft patched 569 CVEs in its July 2026 Patch Tuesday release, with 56 rated critical, 510 rated as important, and 3 rated as moderate. This marks the largest Patch Tuesday release ever, crushin…

**Parallel AI Enrichment:**

- **Technical Details:** Insufficient granularity of access control in Active Directory Federation Services (AD FS) allows an authorized attacker to elevate their privileges locally to administrator.
- **Affected Products:** Microsoft Active Directory Federation Services (AD FS)
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** No public proof-of-concept (PoC) URL known, but the vulnerability has been exploited in the wild.
- **Patch Available:** An official patch was released by Microsoft as part of the July 2026 Patch Tuesday.
- **Active Exploitation:** Confirmed active exploitation in the wild reported by CISA, which added the vulnerability to its Known Exploited Vulnerabilities (KEV) Catalog on July 14, 2026.
- **Threat Actors:** None known
- **Mitigation:** Apply the official security updates released in the Microsoft July 2026 Patch Tuesday.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 10. 🟠 Zero-Day — Microsoft July 2026 Patch Tuesday fixes massive 570 flaws, 3 zero-days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-07-14
**Reference:** <https://www.bleepingcomputer.com/news/microsoft/microsoft-july-2026-patch-tuesday-fixes-massive-570-flaws-3-zero-days/>

> Today is Microsoft&#x27;s July 2026 Patch Tuesday, and with it comes security updates for a record-breaking 570 flaws, including two zero-day vulnerabilities exploited in attacks and one publicly disclosed. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Insufficient granularity of access control in Active Directory Federation Services (AD FS) allows an authorized attacker to elevate privileges locally.
- **Affected Products:** Active Directory Federation Services (AD FS)
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H/E:F/RL:O/RC:C
- **Exploit Available:** Functional exploit code is available, according to Microsoft's MSRC advisory.
- **Patch Available:** Official fix issued by Microsoft on July 14, 2026.
- **Active Exploitation:** Confirmed active exploitation in the wild; the vulnerability has been added to CISA's Known Exploited Vulnerabilities (KEV) catalog.
- **Threat Actors:** None known
- **Mitigation:** Apply the official security update released by Microsoft on July 14, 2026.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-56155

---

## 11. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

---

## 12. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

---

## 13. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

---

## 14. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

---

## 15. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 16. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

---

## 17. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 18. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

---

## 19. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 20. 🟠 Zero-Day — July 2026 Patch Tuesday: Microsoft Patches 622 Vulnerabilities Including Two Exploited Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jul 14, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-july-2026/>

---

## 21. 🟠 Zero-Day — CrowdStrike Uncovers New Prompt Injection Techniques

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jul 07, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-uncovers-new-prompt-injection-techniques/>

---

## 22. 🟠 Zero-Day — Researcher Drops New Windows Zero-Day PoC Hours After Microsoft Patch Tuesday

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-15
**Reference:** <https://thehackernews.com/2026/07/researcher-drops-new-windows-zero-day.html>

> Security researcher Chaotic Eclipse (aka Nightmare-Eclipse) has released a new proof-of-concept (PoC) exploit called LegacyHive.

It has been described as a Windows User Profile Service arbitrary hive load elevation of privileges vulnerability. The Windows User Profile Service, also referred to as ProfSvc, is a core system component that manages user accounts and environments.

&quot;The PoC requi…

---

## 23. 🟠 Zero-Day — Progress Confirms Zero-Day Vulnerability Behind ShareFile Disruption

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-15
**Reference:** <https://www.securityweek.com/progress-confirms-zero-day-vulnerability-behind-sharefile-disruption/>

> The company has rolled out a fix and is restoring access for Storage Zones Controller customers who apply it. The post Progress Confirms Zero-Day Vulnerability Behind ShareFile Disruption appeared first on SecurityWeek .

---

## 24. 🟠 Zero-Day — Progress confirms ShareFile zero-day flaw behind Storage Zone shutdown

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-07-14
**Reference:** <https://www.bleepingcomputer.com/news/security/progress-confirms-sharefile-zero-day-flaw-behind-storage-zone-shutdown/>

> Progress Software has confirmed that a high-severity zero-day vulnerability is behind the emergency shutdown of ShareFile Storage Zone Controllers last week and has released security updates to patch the flaw. [...]

---

## 25. 🟡 High Severity — Woodpecker: Privilege escalation via unrestricted serviceAccountName in the Kubernetes backend

**CVE:** `CVE-2026-61549` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-14
**Reference:** <https://github.com/advisories/GHSA-qf34-295c-26v8>

> ### Impact

A privilege escalation vulnerability affects Woodpecker instances using the **Kubernetes backend**.

The pipeline option `backend_options.kubernetes.serviceAccountName` was passed directly to the pod spec without any admin gating.

**Who is impacted:** any operator running the Kubernetes backend. Any user with **Push** permission on a connected repository can run pipeline pods under an…

---

## 26. 🟡 High Severity — nebula-mesh: CA private key not zeroized on web mobile-bundle error paths

**CVE:** `CVE-2026-53604` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-14
**Reference:** <https://github.com/advisories/GHSA-2p2f-px33-4vv5>

> ## Impact

The web handler `renderMobileBundle` (`internal/web/handlers.go:1325`) passes the real `*pki.CAResolver` directly into `mobilebundle.Build`. Inside `Build` (`internal/mobilebundle/builder.go:54`), `resolver.LoadByID` decrypts the CA&#x27;s ed25519 private key into a `*pki.CAManager`, but `Build` never calls `CAManager.Wipe()` on any return path (success or any of the error paths at line…

---

## 27. 🟡 High Severity — Anyquery: Server-Side Request Forgery (SSRF) via Unrestricted SQLite Virtual Table Modules in Server Mode

**CVE:** `CVE-2026-54628` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-14
**Reference:** <https://github.com/advisories/GHSA-hwrq-8wxh-q4xv>

> ## Summary
Anyquery&#x27;s `server` mode does not restrict outbound HTTP requests initiated by its built-in SQLite virtual table modules (e.g., `json_reader`, `log_reader`). Unauthenticated attackers connecting to the MySQL-compatible server port can create virtual tables pointing to internal network endpoints or Cloud Metadata IPs (e.g., `http://169.254.169.254/latest/meta-data/`). This allows at…

---

## 28. 🟡 High Severity — Trivy: Helm chart tar bomb causes OOM via unbounded io.ReadAll in parser

**CVE:** `CVE-2026-54448` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-14
**Reference:** <https://github.com/advisories/GHSA-q3fv-x8vg-qqm4>

> ## Summary

When Trivy scans a Helm chart archive (`.tgz`), its custom tar unpacker reads each entry with `io.ReadAll(tr)` and no size limit. An attacker who can place a malicious `.tgz` file in the scanned path can craft a small compressed archive that decompresses to gigabytes, causing the Trivy process to be killed by the OS OOM killer.

## Affected configurations

Exploitation requires the att…

---

## 29. 🟡 High Severity — EasyAdmin: Stored Cross-Site Scripting (XSS) via uploaded files served inline in FileField and ImageField

**CVE:** `CVE-2026-54087` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-14
**Reference:** <https://github.com/advisories/GHSA-8559-gwj3-q37r>

> EasyAdmin&#x27;s `FileField` and `ImageField` accept browser-executable file types by default (`FileField` applies no MIME/extension restrictions; `ImageField`&#x27;s default `Image` constraint accepts SVG). When the upload directory is configured inside the public web root — as shown in the documentation — EasyAdmin links to the stored file inline (no download attribute or `Content-Disposition: a…

---

## 30. 🟡 High Severity — yutu: Arbitrary File Write via MCP `caption-download` Tool

**CVE:** `CVE-2026-50158` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-14
**Reference:** <https://github.com/advisories/GHSA-2c7f-fxww-6w6c>

> ## Arbitrary File Write via MCP `caption-download` Tool

### Summary

The `caption-download` MCP tool in yutu passes the caller-supplied `file` parameter directly to `os.Create()` at `pkg/caption/caption.go:272` without any path validation, canonicalization, or confinement to the `pkg.Root` boundary (`YUTU_ROOT`). A local attacker — or any process able to reach the HTTP MCP server — can write arbi…

---

## 31. 🟡 High Severity — n8n-MCP: Cross-tenant access to workflow version backups in multi-tenant HTTP deployments

**CVE:** `CVE-2026-54052` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-14
**Reference:** <https://github.com/advisories/GHSA-j6r7-6fhx-77wx>

> ## Impact

In multi-tenant HTTP deployments — where a single n8n-mcp server serves several tenants — the locally stored workflow version history (the automatic backups taken before workflow updates) was not isolated per tenant. An authenticated tenant could read workflow version snapshots belonging to other tenants, and could delete or destroy other tenants&#x27; stored backups.

A stored snapshot…

---

## 32. 🟡 High Severity — Woodpecker gRPC agent_id metadata can be spoofed- cross-tenant agent impersonation

**CVE:** `CVE-2026-50141` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-14
**Reference:** <https://github.com/advisories/GHSA-g7mm-9vx7-jm7h>

> ### Impact
A vulnerability in Woodpecker CI&#x27;s gRPC layer allowed any authenticated agent to impersonate any other agent on the same server by injecting a forged `agent_id` value into outgoing gRPC metadata. The server correctly verified the JWT token but then discarded the verified agent identity in favor of the client-supplied value.

### Patches
Direct patch: https://github.com/woodpecker-c…

---

## 33. 🟡 High Severity — Anyquery: Arbitrary File Write (AFW) which could lead to Remote Code Execution (RCE) via Unrestricted ATTACH DATABASE in Server Mode

**CVE:** `CVE-2026-50006` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-14
**Reference:** <https://github.com/advisories/GHSA-xrcf-6jh3-ggvx>

> ## Summary
Anyquery&#x27;s `server` mode does not disable or restrict native SQLite disk manipulation commands. Unauthenticated attackers connecting to the MySQL-compatible server port can use the `ATTACH DATABASE` command to write arbitrary SQLite databases to any path on the victim&#x27;s filesystem where the process has write permissions. This leads to Arbitrary File Write (AFW) which could lea…

---

## 34. 🟡 High Severity — SAP Patches CVSS 9.9 NetWeaver ABAP Flaw That Could Expose or Modify Data

**CVE:** `CVE-2026-44747` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-14
**Reference:** <https://thehackernews.com/2026/07/sap-patches-cvss-99-netweaver-abap-flaw.html>

> SAP has rolled out updates to address multiple vulnerabilities as part of its July 2026 security updates, including a critical flaw in SAP NetWeaver Application Server ABAP.

The vulnerability in question is CVE-2026-44747 (CVSS score: 9.9), an out-of-bounds write flaw that allows an authenticated attacker to leverage logical errors in memory management to cause a memory corruption that could

---

## 35. 🟡 High Severity — Fedify has an incomplete SSRF mitigation after GHSA-p9cg-vqcc-grcx: validatePublicUrl allows special-use IPv4 ranges

**CVE:** `CVE-2026-50131` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-14
**Reference:** <https://github.com/advisories/GHSA-xw9q-2mv6-9fr8>

> ### Summary

Fedify previously addressed SSRF/internal network access in GHSA-p9cg-vqcc-grcx by adding public URL validation before runtime document and media fetching. However, the current IPv4 validation logic appears incomplete.

The `validatePublicUrl()` protection relies on `isValidPublicIPv4Address()` to reject non-public IPv4 destinations. The function blocks common private and local ranges…

---

## 36. 🟡 High Severity — MKP: Unbounded Pod Log Read via Attacker-Controlled `limitBytes`/`tailLines` Causes Memory Exhaustion

**CVE:** `CVE-2026-50125` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-14
**Reference:** <https://github.com/advisories/GHSA-qw5r-ppcg-f8rj>

> ## Unbounded Pod Log Read via Attacker-Controlled `limitBytes`/`tailLines` Causes Memory Exhaustion

### Summary

The MKP (Model Context Protocol for Kubernetes) server exposes a `get_resource` MCP tool that proxies Kubernetes pod log requests. User-supplied `limitBytes` and `tailLines` parameters are parsed as unbounded `int64` values and forwarded directly to the Kubernetes API. The server then …

---

## 37. 🟡 High Severity — Wasmtime: Memory leak in C API with `externref` and `anyref` types

**CVE:** `CVE-2025-61670` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-14
**Reference:** <https://github.com/advisories/GHSA-vvp9-h8p2-xwfc>

> ### Impact

Wasmtime 37.0.0 and 37.0.1 have memory leaks in the C/C++ API when using bindings for the `anyref` or `externref` WebAssembly values. This is caused by a regression introduced during the development of 37.0.0 and all prior versions of Wasmtime are unaffected. If `anyref` or `externref` is not used in the C/C++ API then embeddings are also unaffected by the leaky behavior. The `wasmtime…

---

## 38. 🟡 High Severity — FacturaScripts: Unauthenticated Path Traversal in Static File Controllers Reads Private MyFiles Documents

**CVE:** `CVE-2026-45693` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-14
**Reference:** <https://github.com/advisories/GHSA-cv65-7cg8-r623>

> ### Summary

The static file controllers in FacturaScripts decide whether a request is authorized by looking at the URL string instead of the canonical filesystem path. A request that starts with an allow-listed folder name but contains a `../` segment in the middle ends up serving a file from a different directory than the one the URL pretended to point at. This makes any file inside the FacturaS…

---

## 39. 🟡 High Severity — FacturaScripts: Authenticated SQL injection in the FacturaScripts REST API filter parameter via parenthesis bypass in `Where::sqlColumn`

**CVE:** `CVE-2026-45262` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-14
**Reference:** <https://github.com/advisories/GHSA-5qmh-x653-g8qj>

> ## Summary

&gt; **Live PoC verified 2026-04-30** against a stock FacturaScripts master at `127.0.0.1:8081`. A scoped `ApiKey` with `fullaccess=0` and an `ApiAccess` row granting `allowget=1` on the `clientes` resource only (no other rights, no UI session, no admin) issued one `GET /api/3/clientes?filter[(0)UNION%20SELECT%20...]=` request and the response body contained the raw bcrypt hash of the …

---

## 40. 🟡 High Severity — OpenCost ServiceKey Endpoint Unauthorized Credential Overwrite/Injection

**CVE:** `CVE-2026-44300` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-14
**Reference:** <https://github.com/advisories/GHSA-wmj8-9953-vff5>

> ## Summary

OpenCost contains an unauthenticated  file write vulnerability in the `/serviceKey` endpoint that allows remote attackers to overwrite the GCP service account key file without authentication. This can lead to service disruption, credential theft, and potential privilege escalation within Kubernetes clusters.

---


## Affected Versions

- **OpenCost**: All versions up to and including …

---

## 41. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
