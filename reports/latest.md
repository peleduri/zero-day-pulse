# Zero Day Pulse

> **Generated:** 2026-06-01 21:21 UTC &nbsp;|&nbsp; **Total:** 19 &nbsp;|&nbsp; 🔴 KEV: 1 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 6 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🔴 CISA KEV — CVE-2024-21182 — Oracle WebLogic Server Unspecified Vulnerability

**CVE:** `CVE-2024-21182` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2024-21182>

> Vendor: Oracle | Product: WebLogic Server. Oracle WebLogic contains an unspecified vulnerability that could allow an unauthenticated attacker with network access via T3, IIOP to compromise Oracle WebLogic Server. Successful attacks of this vulnerability can result in unauthorized access to critical data or complete access to all Oracle WebLogic Server accessible data. Required action: Apply mitiga…

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated attacker can use network protocols T3 and IIOP to gain access to Oracle WebLogic Server, leading to full compromise.
- **Affected Products:** Oracle WebLogic Server (Core component)
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** Public PoC reported on social media (X).
- **Patch Available:** Oracle listed CVE-2024-21182 in its July 2024 CPU and provides patches via the Oracle CPU updates.
- **Active Exploitation:** CISA listed the vulnerability in the KEV program on 2026-06-01, and a public PoC was reported on social media.
- **Threat Actors:** None known
- **Mitigation:** Apply the Oracle CPU patches per the advisory; if a patch is unavailable, follow BOD 22-01 guidance for cloud services or discontinue use of the affected component.
- **Vendor Advisory:** https://www.oracle.com/security-alerts/cpujul2024verbose.html

---

## 2. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal vulnerability allowing unauthenticated remote attackers to read arbitrary files (e.g., logs, configuration files, credentials) by traversing directories.
- **Affected Products:** SimpleHelp Remote Support / Remote Monitoring and Management (RMM) v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploitation reported by ransomware actors; no publicly available PoC URL.
- **Patch Available:** Patch released: SimpleHelp 5.5.8 (available at https://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570)
- **Active Exploitation:** Yes – confirmed active exploitation in the wild reported by CISA and security news sources.
- **Threat Actors:** DragonForce ransomware operators and other ransomware actors
- **Mitigation:** Upgrade to SimpleHelp v5.5.8 or later; if immediate patching is not possible, isolate the SimpleHelp service from the public Internet, restrict access to trusted IPs or VPN, and rotate any compromised credentials.
- **Vendor Advisory:** https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 3. 🟠 Zero-Day — Critical WP Maps Pro Flaw Actively Exploited to Create Admin Accounts

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://thehackernews.com/2026/06/critical-wp-maps-pro-flaw-actively.html>

> Threat actors are attempting to actively exploit a critical security flaw impacting WP Maps Pro, a WordPress plugin that has had over 15,000 sales on the Envato Market, to create malicious administrator accounts on susceptible sites.

WP Maps Pro allows site owners to embed customizable Google Maps and OpenStreetMap with markers, listings, and advanced location features on WordPress sites. It is

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated attackers can send crafted AJAX requests to the wpgmp_temp_access_ajax endpoint in WP Maps Pro (≤ 6.1.0), triggering logic that creates a new admin user without proper authorization.
- **Affected Products:** WP Maps Pro <= 6.1.0
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit or PoC available for CVE-2026-8732.
- **Patch Available:** Patched in WP Maps Pro version 6.1.0. See advisory at http://wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/wp-google-map-gold
- **Active Exploitation:** Yes, active exploitation has been reported. Threat actors are actively exploiting the vulnerability to create malicious administrator accounts (see The Hacker News report).
- **Threat Actors:** None known
- **Mitigation:** Update WP Maps Pro to version > 6.1.0 (or the latest patched release). If immediate update is not possible, temporarily disable the WP Maps Pro plugin or block access to the wpgmp_temp_access_ajax AJAX action via a web‑application firewall.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when adversarial content on public web pages or other external sources manipulates an AI agent by contaminating its input context (e.g., embedding malicious prompts in pages the agent fetches), causing the agent to execute attacker instructions or reveal sensitive data.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit reported; researchers observed indirect prompt injection payloads on public websites (examples published by Forcepoint).
- **Patch Available:** Patch unavailable
- **Active Exploitation:** Researchers (Google Threat Intelligence, Forcepoint) observed IPI payloads on public websites and reported abusive attempts; however, no confirmed large‑scale successful compromises by named threat actors have been published.
- **Threat Actors:** None known
- **Mitigation:** Follow Google/industry guidance: reduce model access to untrusted web content, implement input validation and content filtering, use prompt/context sanitization and query provenance, apply least‑privilege for agent actions, and monitor for IPI indicators. (See Google Security Blog and Forcepoint write‑up.)
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack technique where malicious instructions are embedded in data sources (web content, documents, tools) consumed by an LLM‑based system; these instructions influence model behavior during query completion without direct user input.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC exploit for a specific vulnerability; public payload examples documented by Forcepoint and other researchers.
- **Patch Available:** No vendor patch model applies; Google described continuous mitigation controls and layered defenses in the advisory.
- **Active Exploitation:** Reports of indirect prompt injection payloads observed in the wild by Forcepoint and Infosecurity Magazine; no confirmed targeted exploitation groups identified.
- **Threat Actors:** None known
- **Mitigation:** Google recommends layered defenses (input sanitization, provenance checks, policy‑based filtering, model hardening and guardrails, principled tool access controls, continuous monitoring) as described in the advisory; Forcepoint published example payloads and detection guidance.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is when untrusted web content (malicious sites, third‑party iframes, or user‑generated content) contains input that causes an agent to take unwanted actions (data exfiltration, financial transactions). Google mitigates this with a separate User Alignment Critic model that vets actions, Agent Origin Sets to restrict origins, a parallel prompt‑injection classifier, and user‑facing confirmations and work logs.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept or weaponized exploit reported.
- **Patch Available:** No traditional patch; defenses are integrated into Chrome. Advisory URL: https://blog.google/security/architecting-security-for-agentic/
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Use Chrome’s built‑in layered defenses; enable the latest Chrome updates, rely on Safe Browsing, enforce user confirmations for sensitive actions, avoid sharing credentials with agents, and limit agent access to sensitive sites.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) or weaponized exploit reported; exploit status unavailable.
- **Patch Available:** Patch not available; vendor advisory URL unavailable.
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known.
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injections (IPI) occur when malicious instructions are embedded in external data sources (emails, documents, calendar invites, image URLs) which an LLM or AI assistant ingests and follows, potentially causing data exfiltration or unsafe actions.
- **Affected Products:** Gemini 2.5, Gemini in Google Workspace, Gemini app
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public weaponized exploit from Google; PoC disclosed by PromptArmor at http://promptarmor.com/resources/notion-ai-unpatched-data-exfiltration
- **Patch Available:** Google implemented layered, in‑product mitigations (model hardening in Gemini 2.5, content classifiers, markdown sanitization, suspicious‑URL redaction, user confirmation/HITL, end‑user notifications). No separate patch URL.
- **Active Exploitation:** No confirmed widespread active exploitation reported by Google. Independent disclosure shows a targeted exploit against Notion AI, remediation deployed 2026‑01‑07.
- **Threat Actors:** None known
- **Mitigation:** Implement layered defenses—model hardening/adversarial training, content classifiers, security‑thought reinforcement, markdown sanitization/redaction of external URLs/images, explicit user confirmation for risky actions, suspicious‑URL detection (Safe Browsing), and contextual security notifications. For third‑party products apply vendor‑provided patches (e.g., Notion remediation deployed 2026‑01‑07).
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors target large backbone, provider edge (PE), and customer edge (CE) routers, leveraging compromised devices and trusted connections to pivot into other networks, and modify routers to maintain persistent, long‑term access.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown; no public PoC cited.
- **Patch Available:** Patch information unavailable.
- **Active Exploitation:** Confirmed global targeting and active compromise reported by CISA/NSA; specific per‑vulnerability details unavailable.
- **Threat Actors:** Salt Typhoon; OPERATOR PANDA; RedMike; UNC5807; GhostEmperor
- **Mitigation:** Monitor routers for unauthorized firmware modifications, harden network segmentation, restrict administrative access, apply vendor updates, and follow CISA/NSA mitigation guidance.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Unit 26165 employs spearphishing, credential spraying/brute force, exploitation of Internet‑facing services and specific CVEs (Outlook CVE‑2023‑23397, WinRAR CVE‑2023‑38831, Roundcube CVEs), malware (HEADLACE, MASEPIE), mailbox permission manipulation for sustained email collection, DLL search‑order hijacking, scheduled tasks/run keys/startup shortcuts for persistence, and data exfiltration via OpenSSH and periodic EWS queries.
- **Affected Products:** Microsoft Outlook/Exchange (CVE-2023-23397), WinRAR (CVE-2023-38831), Roundcube Webmail (CVE-2020-12641, CVE-2020-35730, CVE-2021-44026), various SOHO device firmware and corporate VPNs.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoCs for specific CVEs may exist; CSA does not list PoC URLs.
- **Patch Available:** Vendor‑specific patches are available; see the respective vendor advisories (e.g., Microsoft, WinRAR, Roundcube).
- **Active Exploitation:** Confirmed active exploitation in the wild; reported by CISA advisory AA25-141A, DoD CSA PDF, and SafeBreach coverage.
- **Threat Actors:** GRU Unit 26165 (tracked as APT28 / Fancy Bear / Forest Blizzard / Blue Delta)
- **Mitigation:** Audit and harden email and remote‑access systems; enable MFA; monitor and hunt for listed TTPs/IOCs (mailbox permission manipulation, scheduled tasks, DLL hijacking, unusual use of ntdsutil/wevtutil/vssadmin/ADExplorer/OpenSSH/schtasks); disable/harden NTLM and legacy protocols; patch affected CVEs; secure IP cameras (authenticated RTSP, audit accounts, enable logging).
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 11. 🟠 Zero-Day — Race Against Time: Why Faster Vulnerability Alerts Matter

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://www.bleepingcomputer.com/news/security/race-against-time-why-faster-vulnerability-alerts-matter/>

> Attackers are exploiting vulnerabilities faster than many organizations can identify and patch them. SecAlerts explains why faster vulnerability alerts can help reduce exposure and improve response times. [...]

---

## 12. 🟠 Zero-Day — ⚡ Weekly Recap: New Linux Flaw, PAN-OS Exploit, AI-Powered Attacks, OAuth Phishing and More

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://thehackernews.com/2026/06/weekly-recap-new-linux-flaw-pan-os.html>

> Monday hit like a cron job with anger issues.

A busted auth path here, a repo-side faceplant there, some &quot;patched-ish&quot; thing already getting chewed on in the wild, and then the usual bonus round: poisoned dev tools, sketchy forum chatter, phishing kits pretending to be productivity, and AI lowering the bar for people who already thought &#x27;curl | sh&#x27; had a personality.

The vibe…

---

## 13. 🟠 Zero-Day — Microsoft says it will not pursue security researchers after zero-day backlash

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Record by Recorded Future &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://therecord.media/microsoft-says-it-will-not-pursue-security-researchers-disclosure>

> Microsoft said it is taking the feedback seriously, adding: “To be clear about our approach to legal matters, we have no intention to pursue action against individuals conducting or publishing their security research.”

---

## 14. 🟡 High Severity — Critical Windows Netlogon Vulnerability in Attackers’ Crosshairs

**CVE:** `CVE-2026-41089` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://www.securityweek.com/critical-windows-netlogon-vulnerability-in-attackers-crosshairs/>

> Organizations are advised to patch CVE-2026-41089 as soon as possible, given its severity, the potential ongoing exploitation. The post Critical Windows Netlogon Vulnerability in Attackers’ Crosshairs appeared first on SecurityWeek .

---

## 15. 🟡 High Severity — praisonai-platform: Any workspace member can add arbitrary user as owner via POST /workspaces/{id}/members

**CVE:** `CVE-2026-47413` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://github.com/advisories/GHSA-8g2p-pqm3-fcfh>

> ## Summary

**Type:** Privilege escalation / cross-tenant member injection. The `POST /workspaces/{workspace_id}/members` endpoint is gated only by `require_workspace_member(workspace_id)` (default `min_role=&quot;member&quot;`) and forwards the request body&#x27;s `user_id` and `role` straight into `MemberService.add(workspace_id, user_id, role)`, which has no caller-permission check. A user with…

---

## 16. 🟡 High Severity — Nezha's authenticated agents can forge service-monitor results for other users' services

**CVE:** `CVE-2026-48119` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://github.com/advisories/GHSA-4g6j-g789-rghm>

> #### Summary

Nezha accepts service-monitor `TaskResult` messages from an authenticated agent based only on whether the reported service ID exists. The dashboard authenticates the agent and derives the reporter server ID from the gRPC stream, but the service-monitor result worker does not verify that the reporter server was selected for that service, belongs to the service owner, or was actually a…

---

## 17. 🟡 High Severity — CVE-2026-0826: How an Old Bug Can Feed AI-Powered Impersonation

**CVE:** `CVE-2026-0826` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://www.rapid7.com/blog/post/ve-cve-2026-0826-how-an-old-bug-can-feed-ai-powered-impersonation>

> One of the more persistent myths in security is that old bug classes become old problems. They don’t. They just show up in different places, under different conditions, and usually at the exact moment we’ve convinced ourselves not to pay attention to them. That’s part of what makes enterprise voice infrastructure so interesting. Earlier this year, we wrote about a critical vulnerability in Grandst…

---

## 18. 🟡 High Severity — Recent Palo Alto Networks Vulnerability Exploited for Weeks

**CVE:** `CVE-2026-0257` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://www.securityweek.com/recent-palo-alto-networks-vulnerability-exploited-for-weeks/>

> Hackers began exploiting CVE-2026-0257, an authentication bypass in Palo Alto Networks PAN-OS, four days after public disclosure. The post Recent Palo Alto Networks Vulnerability Exploited for Weeks appeared first on SecurityWeek .

---

## 19. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
