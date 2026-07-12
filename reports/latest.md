# Zero Day Pulse

> **Generated:** 2026-07-12 12:52 UTC &nbsp;|&nbsp; **Total:** 12 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 11 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is an unauthenticated path-traversal vulnerability in the SimpleHelp web application. Crafted HTTP requests using directory-traversal sequences (e.g., '../') in file-path parameters (such as the 'filepath' parameter of the 'toolbox' component) allow remote attackers to download arbitrary files from the SimpleHelp host without authentication or user interaction. Exposed files include serverconfig.xml (containing hashed user passwords), SSH keys (/root/.ssh/id_rsa), and system files such as /etc/passwd. Successful exploitation yields credentials and a foothold to pivot into managed endpoints and downstream customer networks.
- **Affected Products:** SimpleHelp Remote Support (RMM) software — v5.5.7 and earlier (v5.5.x line), v5.4.x prior to v5.4.10, and v5.3.x prior to v5.3.9
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true - Public PoC at https://github.com/imjdl/CVE-2024-57727 and Metasploit module auxiliary/scanner/http/simplehelp_toolbox_path_traversal
- **Patch Available:** true - SimpleHelp released patches in January 2025: v5.5.8+ (latest v5.5.15) for v5.5 branch, v5.4.10 for v5.4, and v5.3.9 for v5.3. Vendor advisory: https://guides.simple-help.com/kb---security-vulnerabilities-01-2025
- **Active Exploitation:** true - Confirmed in-the-wild exploitation since at least January 2025. CISA Advisory AA25-163A (June 12, 2025) documents ransomware actors leveraging CVE-2024-57727 against an unpatched SimpleHelp instance at a utility billing software provider to compromise downstream customer environments. Added to CISA KEV catalog on 2025-02-13. Sophos attributed exploitation to DragonForce ransomware operators targeting an MSP and its customers.
- **Threat Actors:** DragonForce ransomware operators (confirmed by Sophos, CISA AA25-163A, and Halcyon). Generic/unaffiliated ransomware actors have also exploited the flaw since at least January 2025 to compromise SimpleHelp RMM instances and downstream MSP customers.
- **Mitigation:** Upgrade SimpleHelp servers to v5.5.8 or later (v5.5.15 is the latest at time of advisory); for v5.4.x apply v5.4.10; for v5.3.x apply v5.3.9. Because exploitation may have already harvested credentials, immediately rotate SimpleHelp Administrator and Technician passwords, rotate API tokens, and review/restrict firewall and IP allow-list access to the SimpleHelp server. Hunt for suspicious three-letter executables (e.g., aaa.exe) created after January 2025 and review logs for unauthorized logins or configuration changes. Disconnect and rebuild any system known to have been encrypted by ransomware from clean media, restoring data only from clean backups. Do not expose SimpleHelp (or RDP) directly to the internet.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an attack class in which an adversary plants malicious instructions inside external content (web pages, emails, documents, calendar invites, images, code repositories, advertisements) that an AI agent or LLM-powered application later retrieves and ingests. Because the model treats retrieved content and user instructions as one continuous prompt, the attacker's hidden directives can override the user's original intent — silently exfiltrating data, authorizing transactions, deleting files, evading safety controls, leaking system prompts, or forcing AI-driven workflows (e.g., ad-review approval, payment execution) to perform attacker-chosen actions. The attack is especially severe for agentic AI with tool-use, browser, and file-system privileges, where a single ingested hostile page can chain into code execution, as demonstrated by Trail of Bits' prompt-injection-to-RCE research.
- **Affected Products:** Google Gemini, Google Workspace with Gemini; broadly: LLM-powered AI agents, AI-integrated web browsers, agentic crawlers, AI-based ad-review systems, customer-support chatbots, developer-tools assistants (e.g., GitHub Copilot), and security scanners that consume untrusted web/email/document content. No specific vendor version numbers are listed in the Google disclosure because this is a vulnerability-class advisory rather than a single-product CVE.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known. No specific named APT groups, ransomware operators, or attributed campaigns have been publicly identified. Google's Threat Intelligence teams observe financially motivated actors and website operators seeding indirect prompt injections (IPI) on the public web to manipulate AI agents (e.g., ad-fraud via AI ad-review systems, financial fraud via embedded PayPal/Stripe payment links). Forcepoint X-Labs researchers note that shared/template payloads suggest organized tooling, but no specific threat-actor group has been publicly attributed [1][2][3].
- **Mitigation:** No single patch is possible because IPI is a class-level architectural weakness of LLM systems. Recommended layered defenses: (1) Architectural: instruction hierarchy, explicit data/instruction separation, and 'spotlighting' to mark untrusted content. (2) Continuous model hardening and adversarial training against IPI payloads. (3) Human-in-the-loop / confirmation prompts for any high-impact tool call (shell exec, file delete, payment, email send). (4) Sandboxing agent tools with least privilege, network egress restrictions, and allowlisted domains. (5) Content provenance and integrity checks on retrieved web/document content (e.g., C2PA, signed markers). (6) Real-time, web-scale detection of malicious injections (Google's internal pipeline). (7) Red-team exercises and AI-specific Vulnerability Reward Programs (Google's VRP, Bugcrowd). (8) Network-layer defenses: Palo Alto Networks Advanced DNS Security, Advanced URL Filtering, Prisma AIRS, and Prisma Browser to block known-malicious destinations before AI agents fetch them.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack class against LLM-powered applications such as Workspace with Gemini. The attacker embeds adversarial natural-language instructions inside untrusted content (email bodies, Google Slides speaker notes, shared Drive documents, chat messages, web pages, calendar entries, messaging-app notifications). When the user asks Gemini to summarize, draft, search, or act on that content, the model treats the injected instructions as part of its effective prompt and follows them, potentially causing data exfiltration, overriding the user's intent, hijacking tool/agent actions (e.g., sending mail, modifying files, calling external APIs), or surfacing attacker-controlled output. The attack can succeed without any direct input from the victim user because the malicious instructions arrive via the data the LLM consumes.
- **Affected Products:** Google Workspace with Gemini (Gemini in Gmail, Gemini in Docs editors, Gemini in Drive, Gemini in Chat), Gemini standalone app. No specific version numbers disclosed.
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Google employs a continuous, layered defense-in-depth strategy rather than a single patch: (1) Deterministic defenses including a centralized Policy Engine, URL/scheme sanitization, suspicious-URL redaction, markdown sanitization, tool-chaining policies, and a user-confirmation framework requiring explicit approval for sensitive actions (e.g., sending mail, modifying files); (2) ML-based defenses using purpose-built prompt-injection classifiers that screen untrusted content before it reaches the model; (3) LLM-based defenses via refined system prompts and security-reinforcement instructions that keep the model focused on the user-directed task; (4) Model hardening through adversarial retraining on expanded synthetic IPI datasets; and (5) Proactive discovery via human red-teaming, automated red-teaming, the Google AI Vulnerability Rewards Program, and monitoring of public attack disclosures. Administrators and end users should treat AI-generated output as untrusted, watch for user-confirmation prompts before sensitive actions, and apply standard Workspace security controls (restrict external sharing, enable anti-phishing/MDM, limit which third-party apps can act on Workspace data).
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: an attacker embeds hostile instructions inside untrusted web content (malicious sites, third-party iframes, ads, user-generated content, etc.) that the AI agent reads while performing an agentic task on the user's behalf. The injected instructions attempt to steer the agent away from the user's stated goal and cause harmful side effects such as cross-origin data exfiltration from logged-in sites, unauthorized financial transactions, navigating to sensitive sites (banking/healthcare), or leaking credentials via Google Password Manager flows. Because LLMs do not enforce a hard boundary between instructions and data, the attacker controls a channel that is treated as data but interpreted as instructions.
- **Affected Products:** Google Chrome with the Gemini-in-Chrome agentic browsing capabilities. The post does not enumerate specific affected versions; the layered defenses are being introduced as part of Chrome's new agentic/Gemini feature rollout (no specific version range was published in the post).
- **CVSS Score:** CVSS score unavailable. No CVE has been assigned to the issues discussed in this post - it is a proactive architectural defense announcement for a class of threats, not a vulnerability advisory.
- **CVSS Vector:** CVSS vector unavailable. No CVE has been assigned to the issues discussed in this post - it is a proactive architectural defense announcement for a class of threats, not a vulnerability advisory.
- **Exploit Available:** false
- **Patch Available:** true - https://blog.google/security/architecting-security-for-agentic/. The mitigations are being deployed as part of Chrome's agentic/Gemini-in-Chrome feature rollout rather than as a discrete CVE patch.
- **Active Exploitation:** false. The post does not report confirmed in-the-wild exploitation of this specific threat class; it presents indirect prompt injection as an emerging, anticipatable risk and ships defenses proactively. No public exploitation campaigns targeting Chrome's agentic features via indirect prompt injection have been documented in connection with this announcement.
- **Threat Actors:** None known. The post describes a class of attack (indirect prompt injection) rather than exploitation by a named threat actor group; Google also announced an enhanced Chrome vulnerability reward program (up to USD $20,000) for breaking the new agentic defenses.
- **Mitigation:** Google's layered defenses shipping with Chrome's agentic features: (1) User Alignment Critic - an isolated second Gemini model that double-checks every proposed action against the user's stated goal and can veto misaligned actions; (2) Agent Origin Sets - a gating function that splits task-relevant origins into a read-only set (Gemini may consume content) and a read-writable set (the agent may type/click only on these), preventing cross-origin leakage; (3) explicit user confirmations for sensitive sites, Password Manager sign-ins, and consequential actions (purchases, payments, sending messages); (4) a real-time prompt-injection classifier running in parallel with the planner that blocks actions when injection is detected; (5) integration with Google Safe Browsing and on-device scam detection; (6) 'Spotlighting' to prioritize user/system instructions over untrusted page content. User hardening: keep Chrome updated, review agent prompts and the work log before confirming consequential actions, and avoid granting the agent access to unrelated sensitive sites during a task.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow exists in CrabbyAVIF, Google's Rust-based AVIF image codec shipped with the Android platform. In multiple locations, incorrect bounds checks on buffer operations allow out-of-bounds reads (and potentially writes), corresponding to CWE-125 (Out-of-bounds Read) and CWE-787 (Out-of-bounds Write). An attacker who can deliver a specially crafted AVIF image to the device—e.g., via a web page, MMS, email attachment, or any app content parsed by the system image decoder—can trigger the bug without user interaction and without requiring additional execution privileges. When chained with other vulnerabilities, this can lead to remote code execution in the context of the Android System process. Notably, this was the first memory-safety vulnerability Google identified in Rust code shipped with Android, illustrating that even memory-safe languages can produce memory-safety issues when safe code contains incorrect bounds logic or when unsafe blocks are misused.
- **Affected Products:** Android 16.0 (System component / CrabbyAVIF Rust AVIF image decoder); Android devices running Android 16 prior to security patch level 2025-08-05, including Google Pixel devices and other OEMs shipping Android 16
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true (https://source.android.com/docs/security/bulletin/2025-08-01)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the August 2025 Android security update (security patch level 2025-08-05 or later) on all affected Android 16 devices. Google's Scudo hardened allocator provided defense-in-depth and was reported to deterministically render the bug non-exploitable in observed configurations. Until patched, limit exposure to untrusted AVIF content where possible (e.g., disable auto-fetching of remote media content, avoid rendering AVIF images from untrusted sources in apps that support it).
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is a class of attack against LLM-based systems in which adversary-controlled instructions are embedded in content the model ingests as data rather than as a direct user prompt. Common injection vectors include emails, shared documents, calendar invitations, Drive files, web pages fetched by an agent, and other untrusted external content. When a user asks Gemini to summarize, search, or act on that content, the embedded instructions can override the system prompt and cause the model to exfiltrate user data, follow attacker-specified URLs, draft phishing replies, or perform other unintended actions. Google's blog specifically notes that Gemini's markdown sanitizer does not render external image URLs, which neutralizes the EchoLeak (CVE-2025-32711) style 0-click image-rendering exfiltration technique that affected Microsoft 365 Copilot.
- **Affected Products:** Google Gemini app, Gemini in Google Workspace (Gmail, Google Docs, Google Drive, Google Calendar, Google Chat, Google Meet), and Gemini 2.5 series models. No specific version numbers are listed because the advisory describes a vulnerability class (indirect prompt injection) that applies to the Gemini product family rather than a version-bound CVE.
- **CVSS Score:** CVSS score unavailable. No CVSS base score exists for this advisory because no specific CVE has been assigned.
- **CVSS Vector:** CVSS vector unavailable. No CVE has been assigned to the indirect prompt injection class described in this Google blog post.
- **Exploit Available:** true. Public proof-of-concept exploits exist, including SafeBreach Labs' Gemini Voice Assistant exploit, Miggo's calendar invite attack, and academic promptware repositories.
- **Patch Available:** true. Google's layered mitigations are being progressively rolled out across the Gemini 2.5 model family and the Gemini-integrated Workspace apps. No user- or admin-installable patch is required; the controls are deployed server-side by Google.
- **Active Exploitation:** true. Google and Forcepoint X-Labs jointly published telemetry in April 2026 documenting widespread indirect prompt injection activity in the wild, and multiple independent PoCs and real-world exploit chains against Google Gemini have been published.
- **Threat Actors:** None known. The Google blog post does not attribute exploitation to any named threat actor, APT group, or ransomware operator.
- **Mitigation:** Google describes a five-layer defense-in-depth strategy being rolled out across Gemini: (1) ML-based prompt-injection content classifiers trained on adversarial data curated via the Google AI Vulnerability Reward Program, which detect and filter malicious instructions in ingested content; (2) security thought reinforcement, a system-level prompt technique that instructs the underlying LLM to disregard adversarial instructions in untrusted content; (3) markdown sanitization and suspicious-URL redaction, in which Gemini strips external image URLs and uses Google Safe Browsing to redact unsafe links before returning content; (4) a user confirmation framework that requires explicit user approval before Gemini executes sensitive tool actions such as sending email or deleting files; and (5) end-user security mitigation notifications that surface to the user when Gemini blocks a response due to suspected prompt injection. Users and admins cannot apply a traditional software patch; protection comes from Google's server-side rollout of these controls to Gemini 2.5 and Gemini-integrated Workspace surfaces.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors exploit publicly known, often n-day, vulnerabilities in internet-exposed network edge devices (routers, VPNs, firewalls) to gain initial access. Once inside, they: (1) create local accounts and enable SSH/HTTPS on non-standard ports; (2) abuse Cisco IOS XE Guest Shell containers (guestshell/ios-xe.guestshell) to stage tooling; (3) modify Access Control Lists — frequently naming them 'access-list 10', 'access-list 20', or 'access-list 50' — to whitelist attacker-controlled IPs; (4) configure GRE, mGRE, and IPsec tunnels and add static routes to provide covert access; (5) enable SPAN/RSPAN/ERSPAN port mirroring to capture TACACS+/RADIUS authentication traffic; and (6) alter TACACS+ server configuration to harvest credentials. They pivot via trusted provider-to-provider and provider-to-customer links, harvest BGP routes, MPLS labels, RSVP sessions, and subscriber records, and exfiltrate via the GRE/IPsec tunnels and custom SFTP clients. Persistent router modifications enable long-term, deniable espionage access.
- **Affected Products:** Network edge devices from Cisco (IOS, IOS XE, including IOS XE Guest Shell; Smart Install), Palo Alto Networks (PAN-OS with GlobalProtect), Ivanti (Connect Secure 9.x/22.x, Policy Secure 9.x/22.x), Fortinet, Juniper, SonicWall, Microsoft Exchange, Nokia routers/switches, and Sierra Wireless devices. Specific CVEs cited include CVE-2024-21887 and CVE-2023-46805 (Ivanti), CVE-2024-3400 (Palo Alto PAN-OS GlobalProtect), CVE-2023-20273 and CVE-2023-20198 (Cisco IOS XE Web UI), and CVE-2018-0171 (Cisco Smart Install).
- **CVSS Score:** CVSS score unavailable — the advisory does not assign a single CVSS score. Individual cited CVE scores: CVE-2024-21887 9.1, CVE-2023-46805 8.2, CVE-2024-3400 10.0, CVE-2023-20273 7.2, CVE-2023-20198 10.0, CVE-2018-0171 9.8.
- **CVSS Vector:** CVSS vector unavailable — AA25-239A is a campaign/threat-activity advisory, not a single-CVE advisory, so no unified CVSS v3 vector applies. Individual CVEs referenced have their own vectors (e.g., CVE-2024-3400: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H).
- **Exploit Available:** true — exploits for the cited CVEs (e.g., CVE-2024-21887, CVE-2024-3400, CVE-2023-20198/CVE-2023-20273) are publicly available and have been used in the wild by these PRC actors; no additional weaponized exploit beyond the public PoCs is required.
- **Patch Available:** true — vendor patches exist for every CVE cited in the advisory: Ivanti patches for CVE-2024-21887 and CVE-2023-46805, Palo Alto Networks hotfixes for CVE-2024-3400, Cisco fixes for CVE-2023-20273 and CVE-2023-20198, and Cisco Smart Install guidance for CVE-2018-0171. Patches are linked from each vendor's security advisory portal referenced in AA25-239A.
- **Active Exploitation:** true — CISA, NSA, FBI, and international partners confirm ongoing in-the-wild exploitation by these PRC actors since at least 2021, targeting telecommunications, government, transportation, lodging, and military networks globally, with a focus on large backbone and provider-edge routers used for persistent espionage. See CISA Advisory AA25-239A (https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a) and SafeBreach/Picus analyses cited above.
- **Threat Actors:** Multiple People's Republic of China (PRC) state-sponsored threat actors are cited, including Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, and GhostEmperor. The advisory also names PRC-contracted companies Sichuan Juxinhe Network Technology Co. Ltd., Beijing Huanyu Tianqiong Information Technology Co. Ltd., and Sichuan Zhixin Ruijie Network Technology Co. Ltd. as enablers of the intrusions.
- **Mitigation:** Patch the cited CVEs on Ivanti Connect/Policy Secure, Palo Alto PAN-OS GlobalProtect, and Cisco IOS XE Web UI/Smart Install immediately; upgrade unsupported/end-of-life network devices; baseline and audit router configurations for unauthorized ACL changes (especially ACLs 10/20/50), unexpected GRE/IPsec tunnels, static routes, SSH/HTTP services on non-standard ports, local user accounts, and TACACS+/RADIUS server modifications; disable and remove Cisco IOS XE Guest Shell containers if not required; enforce SNMPv3 and disable Telnet, unencrypted HTTP, and Smart Install; validate firmware/image hashes against vendor values; monitor for unexpected east-west traffic, router-to-router logons, and new XR host OS services; coordinate containment sequencing across interconnected providers before disabling compromised assets to avoid tipping the actors; and follow CISA's additional hardening guidance in AA25-239A.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2023-23397 is a Microsoft Outlook Elevation of Privilege vulnerability that leaks Net-NTLMv2 hashes without user interaction. An attacker sends a specially crafted email containing a Calendar/Meeting/Task item with an extended MAPI property whose value is a UNC path pointing to an attacker-controlled SMB server. When the Outlook client (Windows) processes the message—even in preview pane or before the user opens it—it automatically attempts SMB authentication to the attacker's UNC path and leaks the victim's Net-NTLMv2 hash. The hash is then used in NTLM relay attacks against services that accept NTLM (e.g., HTTP web servers via NTLM relay to AD CS, or Microsoft 365 via Outlook Web), or cracked offline. In the GRU campaign documented in AA25-141A, the unit exploited Outlook (CVE-2023-23397), Roundcube (CVE-2020-12641, CVE-2021-44026), and WinRAR (CVE-2023-38831) for initial access, then performed credential brute-forcing (T1110.001/003), spearphishing (T1566), exploitation of public-facing applications and edge devices (T1190), edge-device and IoT abuse (internet cameras at border crossings), and used legitimate tools ntdsutil, wevtutil, vssadmin, and PsExec for lateral movement and credential harvesting. Data was archived into .zip files and exfiltrated via embedded OpenSSH binary.
- **Affected Products:** Microsoft Outlook for Windows (CVE-2023-23397): Microsoft 365 Apps for Enterprise, Outlook 2019, Outlook 2016, Outlook LTSC 2021, Office LTSC Standard 2021. Roundcube Webmail (CVE-2020-12641): versions before 1.3.17, 1.4.x before 1.4.12, 1.2.x before 1.2.13, 1.3.x before 1.3.16. Atlassian Confluence Data Center/Server (CVE-2021-44026). RARLAB WinRAR (CVE-2023-38831). Also targeted: SOHO routers, internet-connected IP cameras at border crossings, and corporate VPNs at Western logistics providers.
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true - Public PoC code is available on GitHub (https://github.com/Trackflaw/CVE-2023-23397 and https://github.com/api0cradle/CVE-2023-23397-POC-Powershell)
- **Patch Available:** true - https://msrc.microsoft.com/update-guide/vulnerability/cve-2023-23397 (Microsoft Outlook security update released March 14, 2023)
- **Active Exploitation:** true - CISA added CVE-2023-23397 to the Known Exploited Vulnerabilities (KEV) Catalog. CISA, FBI, NSA, and NCSC-UK jointly confirmed in advisory AA25-141A (May 21, 2025) that GRU Unit 26165 actively exploited CVE-2023-23397 along with CVE-2020-12641, CVE-2021-44026, and CVE-2023-38831 since at least 2022 against Western logistics providers and technology companies supporting aid delivery to Ukraine.
- **Threat Actors:** Russian GRU 85th Main Special Service Center (85th GTsSS), military unit 26165. Industry/alternate names: APT28, Fancy Bear, Forest Blizzard, BlueDelta, STRONTIUM, Sednit, Sofacy, IRON TWILIGHT.
- **Mitigation:** Apply Microsoft Outlook security update from March 14, 2023 to fix CVE-2023-23397. As compensating controls: disable NTLM where possible; require SMB signing (LAN Manager authentication level 'Send NTLMv2 response only/refuse LM & NTLM'); enforce SMB encryption; block outbound SMB (TCP/445) and NTLM at the network egress; rotate any credentials that may have been relayed. Apply patches for Roundcube (CVE-2020-12641, CVE-2021-44026) and WinRAR (CVE-2023-38831). On IP cameras and SOHO routers: change default passwords, disable UPnP/FTP/web admin/anonymous RTSP, enable authentication on RTSP, audit accounts, monitor logs, and disable unused services. Enforce phishing-resistant MFA on all internet-facing accounts, segment logistics OT/IT networks, disable legacy authentication protocols, and audit remote-access authentication activity for unusual source IPs or service abuse.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

**Parallel AI Enrichment:**

- **Technical Details:** The article describes the browser threat landscape conceptually rather than documenting a specific vulnerability. It explains that browser-based attacks typically begin with exploitation of rendering logic, JavaScript execution, document handling, or memory-safety weaknesses, followed by a sandbox escape or privilege escalation to move from browser activity to system access. It also catalogues complementary attack vectors including phishing, clickjacking, cross-site scripting (XSS), HTML smuggling, malicious downloads, credential theft, session abuse, adversary-in-the-middle techniques, MFA bypass, and data exfiltration. Per the CrowdStrike 2026 Global Threat Report cited in the post, 42% of vulnerabilities were exploited before public disclosure [1].
- **Affected Products:** Not specifically listed. The article discusses browsers built on the Chromium open-source project (e.g., Google Chrome, Microsoft Edge, and other Chromium-based browsers) in general terms, without enumerating specific vulnerable versions.
- **CVSS Score:** CVSS score unavailable. No specific CVE is referenced in this article, so no CVSS v3 base score is provided.
- **CVSS Vector:** CVSS vector unavailable. No specific CVE is referenced in this article, so no CVSS v3 vector is provided.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known. The article does not name any specific threat actor groups, APT campaigns, or ransomware operators; it refers generically to 'sophisticated attackers' and 'adversaries'.
- **Mitigation:** The article recommends defense-in-depth controls rather than a specific patch: (1) deploy JavaScript Language Randomization (JLR) to continuously randomize the JavaScript runtime environment and frustrate browser exploit development; (2) block phishing and adversary-in-the-middle techniques; (3) protect session tokens against hijacking and MFA bypass; and (4) prevent credential theft and data exfiltration at the point of execution. It emphasizes shrinking the gap between vulnerability discovery and patching and using a browser security solution that integrates with the broader endpoint/identity stack [1].
- **Vendor Advisory:** https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/

---

## 10. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/

---

## 11. 🟠 Zero-Day — CrowdStrike Uncovers New Prompt Injection Techniques

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jul 07, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-uncovers-new-prompt-injection-techniques/>

---

## 12. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
