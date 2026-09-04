# Zero Day Pulse

> **Generated:** 2026-09-04 15:24 UTC &nbsp;|&nbsp; **Total:** 35 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 21 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Improve Router Hygiene to Protect Against Russian State-Sponsored Targeting

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Wed, 08 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a>

> Russian Government-Sponsored Activity Targets Poorly Configured and Vulnerable Devices Across Critical Sectors Executive summary Russian Federal Security Service (FSB) Center 16 cyber actors continue to exploit poorly configured and vulnerable networking devices worldwide, opportunistically compromising multiple critical infrastructure sector networks. This joint Cybersecurity Advisory (CSA) build…

**Parallel AI Enrichment:**

- **Technical Details:** FSB Center 16 actors scan Internet address ranges for exposed SNMP agents accepting common or default community strings, then use spoofed SNMP Set-Requests to copy router configurations and transfer them through TFTP. The actors also target Cisco Smart Install and web-based management portals. CVE-2018-0171 allows a crafted Smart Install message on TCP port 4786 to trigger a buffer overflow, device reload, denial of service, or arbitrary code execution; CVE-2008-4128 is a CSRF flaw in the Cisco IOS 12.4 HTTP administration interface that can permit execution of administrative commands.
- **Affected Products:** Cisco IOS Software and Cisco IOS XE Software running the Smart Install client on vulnerable releases; Cisco 871 Integrated Services Router running Cisco IOS 12.4 for CVE-2008-4128. Cisco IOS XR, Cisco NX-OS, and Cisco Smart Install director configurations are not affected by CVE-2018-0171.
- **CVSS Score:** 9.8 (CVE-2018-0171); 4.3 (CVE-2008-4128)
- **CVSS Vector:** CVE-2018-0171: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H; CVE-2008-4128: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Exploit Available:** true - https://github.com/AlrikRr/Cisco-Smart-Exploit; https://www.exploit-db.com/exploits/6476
- **Patch Available:** Partially: true for CVE-2018-0171 - https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20180328-smi2; no current vendor patch identified for CVE-2008-4128, so legacy equipment should be isolated, mitigated, or replaced.
- **Active Exploitation:** true - CISA reports ongoing Russian FSB Center 16 exploitation of vulnerable networking devices and says the actors previously exploited CVE-2018-0171 and CVE-2008-4128; CVE-2008-4128 was also added to CISA's Known Exploited Vulnerabilities Catalog: https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a
- **Threat Actors:** Russian FSB Center 16; aliases reported by CISA include Berserk Bear, Energetic Bear, Crouching Yeti, Dragonfly, Ghost Blizzard, and Static Tundra.
- **Mitigation:** Disable Cisco Smart Install and, where it is not required, disable SNMPv1/v2; use SNMPv3 with authPriv, non-default credentials, read-only access, and MIB/OID allowlisting. Restrict management protocols with ACLs, block exposed TFTP, Smart Install, and SNMP ports where feasible, update device software, and replace end-of-life equipment.
- **Vendor Advisory:** CVE-2018-0171: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20180328-smi2; CVE-2008-4128: URL unavailable.

---

## 2. 🟠 Zero-Day — August 2026 Patch Tuesday: One Exploited Zero-Day and 62 Critical Vulnerabilities Among 415 CVEs

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Aug 11, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-august-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-68820 is a CWE-416 use-after-free vulnerability in the kernel-mode Windows Ancillary Function Driver for WinSock (AFD.sys). A locally authenticated low-privileged attacker can run a specially crafted application and win a race condition involving concurrent socket state access; the resulting memory corruption can provide kernel read/write capability and SYSTEM privileges. The attack is local, high-complexity, requires no user interaction, and is not independently exploitable remotely over the internet.
- **Affected Products:** Windows 10 Version 1607 (32-bit/x64, affected from 10.0.14393.0 to before 10.0.14393.9418), Windows 10 Version 1809 (32-bit/x64, from 10.0.17763.0 to before 10.0.17763.9121), Windows 10 Version 21H2 (32-bit/ARM64/x64, from 10.0.19044.0 to before 10.0.19044.7663), Windows 10 Version 22H2 (32-bit/ARM64/x64, from 10.0.19045.0 to before 10.0.19045.7663), Windows 11 Version 23H2 (ARM64/x64, from 10.0.22631.0 to before 10.0.22631.7517), Windows 11 Version 24H2 (ARM64/x64, from 10.0.26100.0 to before 10.0.26100.9168), Windows 11 Version 25H2 (ARM64/x64, from 10.0.26200.0 to before 10.0.26200.9168), Windows 11 Version 26H1 (ARM64/x64, from 10.0.28000.0 to before 10.0.28000.2704), Windows Server 2012 and Server Core (x64, from 6.2.9200.0 to before 6.2.9200.26280), Windows Server 2012 R2 and Server Core (x64, from 6.3.9600.0 to before 6.3.9600.23338), Windows Server 2016 and Server Core (x64, from 10.0.14393.0 to before 10.0.14393.9418), Windows Server 2019 and Server Core (x64, from 10.0.17763.0 to before 10.0.17763.9121), Windows Server 2022 (x64, from 10.0.20348.0 to before 10.0.20348.5499), Windows Server 2025 and Server Core (x64, from 10.0.26100.0 to before 10.0.26100.33296)
- **CVSS Score:** 7.0
- **CVSS Vector:** CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true - https://research.checkpoint.com/2026/shattering-the-dream-when-a-job-offer-becomes-a-zero-day-attack/ (weaponized exploit observed in the Lazarus campaign; no public PoC code reported)
- **Patch Available:** true - https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-68820
- **Active Exploitation:** true - Microsoft reports exploitation detected; Check Point Research documented Lazarus using CVE-2026-68820 in Operation Dream Job: https://research.checkpoint.com/2026/shattering-the-dream-when-a-job-offer-becomes-a-zero-day-attack/
- **Threat Actors:** Lazarus Group (DPRK-linked), operating in the Operation Dream Job campaign
- **Mitigation:** Install Microsoft's August 11, 2026 security updates on all affected Windows builds and reboot as required; for Windows 10 Version 1607 and Windows Server 2016, KB5120418 updates the system to OS Build 14393.9418, with SSU KB5120236 recommended first where applicable. If patching is delayed, restrict untrusted local or remote interactive logons and investigate suspicious SYSTEM-level activity or Lazarus-related compromise indicators.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-68820

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection occurs when an AI system processes attacker-controlled content such as a website, email, or document containing malicious instructions. The model may silently follow those instructions instead of the user's intent; observed web examples sought SEO manipulation, resource exhaustion, data exfiltration, or destruction, including attempts to delete files.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** >null<
- **CVSS Vector:** Vector unavailable.
- **Exploit Available:** true - https://greshake.github.io/
- **Patch Available:** false
- **Active Exploitation:** true - https://blog.google/security/prompt-injections-web/ (Google observed malicious IPI attempts and a 32% increase in the malicious category from November 2025 to February 2026, while noting that activity had not yet been productionized at scale.)
- **Threat Actors:** None known.
- **Mitigation:** Treat retrieved web, email, and document content as untrusted; apply least privilege to agents, restrict side effects, and require approval for sensitive actions. Google also describes hardening its AI products, red-team pressure testing Gemini, and an AI Vulnerability Reward Program.
- **Vendor Advisory:** URL unavailable.

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection occurs when malicious instructions are embedded in external data such as websites, emails, or documents that Gemini processes. The model may confuse those instructions with legitimate commands, potentially causing unauthorized actions, data disclosure, or manipulation of its response without direct malicious input from the user.
- **Affected Products:** Google Gemini app; Gemini in Google Workspace apps: Gmail, Docs editors, Drive, and Chat (specific versions not specified).
- **CVSS Score:** :null
- **CVSS Vector:** Vector unavailable.
- **Exploit Available:** true - https://www.immersivelabs.com/resources/c7-blog/weaponizing-llms-bypassing-email-security-products-via-indirect-prompt-injection
- **Patch Available:** false - no discrete versioned patch was identified; Google describes continuous configuration, prompt, model-training, and defense updates instead.
- **Active Exploitation:** true - https://blog.google/security/prompt-injections-web/ (Google observed malicious indirect prompt-injection attempts in the wild and reported a 32% relative increase from November 2025 to February 2026; activity was generally low sophistication and not attributed to named campaigns).
- **Threat Actors:** None known.
- **Mitigation:** Google uses layered defenses including prompt-injection classifiers, security-focused instruction reinforcement, Markdown sanitization, suspicious-URL redaction, model hardening, contextual user confirmation, and security notifications. Users should treat external content as untrusted, heed Gemini warnings, avoid links and shared files from unknown senders, and report malicious content.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection occurs when malicious instructions are embedded in websites, third-party iframe content, or user-generated content that Chrome’s agentic browsing system processes. The planning model may treat those instructions as trusted directions, causing unwanted actions such as financial transactions or sensitive-data exfiltration. Google describes defenses including an isolated User Alignment Critic, origin gating, user confirmations, and real-time prompt-injection detection.
- **Affected Products:** Google Chrome with Gemini in Chrome/agentic browsing capabilities; specific impacted versions not specified.
- **CVSS Score:** .
- **CVSS Vector:** Vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false - no confirmed in-the-wild exploitation of Chrome’s agentic capabilities was reported; separate research has documented general web-based indirect prompt-injection activity: https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/
- **Threat Actors:** None known.
- **Mitigation:** Use Chrome’s agentic safeguards, including origin restrictions, user confirmation for logins, payments, messages, and other sensitive actions, and the ability to pause or stop tasks. Keep Chrome updated and avoid allowing agents to access unrelated authenticated sites or sensitive data.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2025-48530 is an incorrect bounds-check condition in multiple Android locations that permits out-of-bounds memory accesses. The issue affects the CrabbyAVIF component and could enable remote code execution when combined with other vulnerabilities, without requiring additional privileges or user interaction. Google described it as a linear buffer overflow that was caught before public release, while Scudo guard pages made exploitation deterministically non-exploitable.
- **Affected Products:** Google Android 16 (affected; addressed by security patch level 2025-08-01 or later)
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true - https://source.android.com/docs/security/bulletin/2025-08-01
- **Active Exploitation:** false - no confirmed active exploitation reported; Google states the vulnerability never made it into a public release.
- **Threat Actors:** None known.
- **Mitigation:** Install the Android security update with patch level 2025-08-01 or later, preferably the latest update provided by the device manufacturer. Android's Scudo hardened allocator also provides defense-in-depth against this issue.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection occurs when an attacker embeds hidden instructions in external data such as emails, documents, web pages, or calendar content that an AI system processes as context. The injected content can manipulate Gemini into revealing sensitive information, generating unauthorized tool calls, or performing other actions. Google's research models the attack as a malicious payload causing a function call that exfiltrates private data through an externally executed system.
- **Affected Products:** Gemini 2.5 models, Gemini app, Gemini in Google Workspace apps including Gmail and Docs; exact affected application versions are not specified.
- **CVSS Score:** ]
- **CVSS Vector:** Vector unavailable.
- **Exploit Available:** true - https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/
- **Patch Available:** false - no standalone versioned vendor patch was identified; Google has deployed and continues updating integrated mitigations described at https://blog.google/security/mitigating-prompt-injection-attacks/.
- **Active Exploitation:** true - https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/; web-based indirect prompt injection has been reported as actively weaponized in real-world activity, although no named group exploiting Gemini specifically was identified.
- **Threat Actors:** None known.
- **Mitigation:** Use Google's layered defenses: adversarial model hardening, prompt-injection classifiers, security-thought reinforcement, Markdown and URL sanitization, suspicious-link redaction, user confirmation for sensitive actions, and end-user security notifications. Organizations should also apply human-in-the-loop approval and restrict the privileges and external data accessible to AI agents.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 8. 🟠 Zero-Day — Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite

**CVE:** `CVE-2025-66376` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Tue, 21 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a>

> Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite Executive summary A group of Russian state-supported cyber actors has been targeting and compromising various Western government and commercial organizations using the Zimbra Collaboration Suite (ZCS) software since at least July 2025. The Russian state-supported advanced persistent threat …

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2025-66376 is a stored cross-site scripting vulnerability in Zimbra’s Classic UI caused by improper sanitization of CSS @import directives in HTML email. A malicious JavaScript payload executes when a user merely views the crafted email, allowing collection and exfiltration of email, directory, authentication, and other sensitive data through the victim’s authenticated webmail session.
- **Affected Products:** Zimbra Collaboration Suite (ZCS) 10.0.0–10.0.17, Zimbra Collaboration Suite (ZCS) 10.1.0–10.1.12; specifically the Classic UI
- **CVSS Score:** 6.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N
- **Exploit Available:** true - https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a
- **Patch Available:** true - https://wiki.zimbra.com/wiki/Zimbra_Security_Advisories
- **Active Exploitation:** true - https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a; CISA reports successful exploitation by LAUNDRY BEAR and lists CVE-2025-66376 in its Known Exploited Vulnerabilities Catalog.
- **Threat Actors:** LAUNDRY BEAR; also tracked as Void Blizzard, CL-STA-1114, and TA488 (formerly UNK_PitStop)
- **Mitigation:** Immediately upgrade ZCS to 10.1.13 or 10.0.18 or later. If patching is not immediately feasible, use an alternative mail client and avoid the Classic ZCS webmail client; monitor for suspicious SOAP requests, DNS activity, and outbound connections, and revoke exposed application passcodes, 2FA scratch keys, and passwords after suspected compromise.
- **Vendor Advisory:** https://wiki.zimbra.com/wiki/Zimbra_Security_Advisories

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** This is a coordinated Chinese cyber-espionage campaign rather than a single CVE-defined vulnerability. The actors exploit publicly known vulnerabilities on internet-exposed network-edge devices, including routers and firewalls, then modify routing, access-control, authentication, and tunneling configurations to maintain persistence and pivot through trusted connections. They also use packet capture, traffic mirroring, virtualized containers such as Cisco Guest Shell, and compromised routers to collect credentials and network traffic.
- **Affected Products:** Ivanti Connect Secure and Ivanti Policy Secure (CVE-2024-21887; versions not specified), Palo Alto Networks PAN-OS GlobalProtect (CVE-2024-3400; versions not specified), Cisco IOS XE (CVE-2023-20273 and CVE-2023-20198; versions not specified), Cisco IOS and IOS XE Smart Install (CVE-2018-0171; versions not specified).
- **CVSS Score:** :null
- **CVSS Vector:** Vector unavailable.
- **Exploit Available:** true - https://github.com/frostbits-security/SIET
- **Patch Available:** true - https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a (apply the applicable vendor updates for the listed CVEs; there is no single patch for the broader campaign).
- **Active Exploitation:** true - https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a
- **Threat Actors:** PRC state-sponsored APT actors; activity overlaps with Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, and GhostEmperor. CISA does not adopt a specific commercial naming convention for these actors.
- **Mitigation:** Patch the listed CVEs and keep network-device operating systems on vendor-supported, fully updated releases. Isolate management planes, restrict management services to approved administrators and networks, use SNMPv3 and strong authentication, disable unused ports and protocols, and monitor configuration changes, tunnels, packet capture, Guest Shell, and unexpected local accounts.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Sangoma Switchvox Vulnerabilities Exploited in the Wild

**CVE:** `CVE-2026-9586` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-09-04
**Reference:** <https://www.securityweek.com/sangoma-switchvox-vulnerabilities-exploited-in-the-wild/>

> Tracked as CVE-2026-9586, the unauthenticated SQL injection flaw can be exploited remotely for arbitrary code execution. The post Sangoma Switchvox Vulnerabilities Exploited in the Wild appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** The unauthenticated /pa endpoint parses XML beginning with <PolycomIPPhone> and directly concatenates the user-controlled PhoneIP value into PostgreSQL queries without sanitization or parameterization. A remote attacker can send a crafted HTTP request to execute arbitrary SQL as the PostgreSQL superuser, perform database operations, and chain the injection to remote code execution on the Switchvox appliance.
- **Affected Products:** Sangoma Switchvox SMB Edition 8.2.2.1 through versions prior to 8.4.0.2, including 8.3 build 104997
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true - https://horizon3.ai/attack-research/disclosures/cve-2026-9586-sangoma-switchvox-rce/
- **Patch Available:** true - https://sangomakb.atlassian.net/wiki/spaces/Switchvox/pages/1802371073/Switchvox+-+Release+Notes+Version+8.4.0.2+July+14+2026
- **Active Exploitation:** true - Horizon3 observed valid exploitation attempts on honeypots on August 30, 2026; CISA added CVE-2026-9586 to the KEV Catalog on September 2, 2026: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- **Threat Actors:** Unidentified threat actors; observed activity includes cryptominer deployment. No named APT or ransomware group has been reported.
- **Mitigation:** Upgrade Switchvox SMB to 8.4.0.2 or later. Because exploitation is active, investigate exposed systems for compromise, review Switchvox database logs and indicators of compromise, and restrict internet access to the management interface until patched.
- **Vendor Advisory:** https://sangomakb.atlassian.net/wiki/spaces/Switchvox/pages/1802371073/Switchvox+-+Release+Notes+Version+8.4.0.2+July+14+2026

---

## 11. 🟠 Zero-Day — New CrowdStrike 'FalconFlank' zero-day grants SYSTEM privileges

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-09-04
**Reference:** <https://www.bleepingcomputer.com/news/security/new-crowdstrike-falconflank-zero-day-grants-system-privileges/>

> An anonymous security researcher who uses the &quot;Nightmare Eclipse&quot; handle released a CrowdStrike Falcon zero-day exploit named &quot;FalconFlank&quot; that lets attackers escalate privileges on up-to-date Windows systems. [...]

---

## 12. 🟠 Zero-Day — Google warns of new Chrome zero-day flaw exploited in attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-09-04
**Reference:** <https://www.bleepingcomputer.com/news/security/google-warns-of-new-chrome-zero-day-flaw-exploited-in-attacks/>

> Google has updated the Chrome browser to address an actively exploited high-severity zero-day flaw in the V8 engine and 11 other vulnerabilities. [...]

---

## 13. 🟠 Zero-Day — Google Patches 6th Chrome Zero-Day of 2026

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-09-04
**Reference:** <https://www.securityweek.com/google-patches-6th-chrome-zero-day-of-2026/>

> Google’s Chrome 152 security update resolves 12 vulnerabilities, including a high-severity type confusion flaw in the V8 engine. The post Google Patches 6th Chrome Zero-Day of 2026 appeared first on SecurityWeek .

---

## 14. 🟠 Zero-Day — Google Releases Chrome Update to Patch Actively Exploited V8 Zero-Day

**CVE:** `CVE-2026-85046` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-09-04
**Reference:** <https://thehackernews.com/2026/09/google-releases-chrome-update-to-patch.html>

> Google on Thursday released security updates to patch 12 vulnerabilities, including one that has come under active exploitation in the wild.

The high-severity vulnerability, tracked as CVE-2026-85046 (CVSS score: 8.8), has been described as a type confusion bug in V8, Chrome&#x27;s JavaScript and WebAssembly engine.

&quot;Type confusion in V8 in Google Chrome prior to 152.0.7977.82 allowed a rem…

---

## 15. 🟡 High Severity — 12-Year-Old PostgreSQL Vulnerability Enables Database, Server Takeover

**CVE:** `CVE-2026-6471` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-09-04
**Reference:** <https://www.securityweek.com/12-year-old-postgresql-vulnerability-enables-database-server-takeover/>

> Dubbed PostGREShell, CVE-2026-6471 turns low-level replication access into code execution, permanent superuser privileges and a persistent database backdoor. The post 12-Year-Old PostgreSQL Vulnerability Enables Database, Server Takeover appeared first on SecurityWeek .

---

## 16. 🟡 High Severity — Over 440,000 Exploit Attempts Target Super Forms and Elementor Pro RCE Flaws

**CVE:** `CVE-2026-14894` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-09-04
**Reference:** <https://thehackernews.com/2026/09/over-440000-exploit-attempts-target.html>

> Threat actors are exploiting two critical security flaws in WordPress plugins Super Forms and Elementor Pro, according to findings from Wordfence.

The vulnerabilities in question are -


  CVE-2026-14894 (CVSS score: 9.8) - A missing file type validation vulnerability in Super Forms – Drag &amp; Drop Form Builder that allows unauthenticated attackers to upload files of any type, including

---

## 17. 🟡 High Severity — SiYuan: Encrypted-notebook key-derivation material and wrapped notebook keys disclosed to anonymous readers, enabling offline master-password cracking

**CVE:** `CVE-2026-72801` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-03
**Reference:** <https://github.com/advisories/GHSA-8x84-r2ff-h8pq>

> **CVE:** This vulnerability corresponds to [CVE-2026-72801](https://nvd.nist.gov/vuln/detail/CVE-2026-72801).

### Summary

Two `CheckAuth`-only endpoints disclose the complete offline attack material for the encrypted-notebook master password, plus the wrapped per-notebook key needed to use it. Both are reachable by the publish `RoleReader` token and by the anonymous account when `Publish.Auth.En…

---

## 18. 🟡 High Severity — SiYuan: Missing publish-access filter on getBlockAttrs and batchGetBlockAttrs discloses block attributes (name, alias, memo, custom fields) of protected documents

**CVE:** `CVE-2026-72803` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-03
**Reference:** <https://github.com/advisories/GHSA-qvq9-hq6p-v378>

> **CVE:** This vulnerability corresponds to [CVE-2026-72803](https://nvd.nist.gov/vuln/detail/CVE-2026-72803).

### Summary

`POST /api/attr/getBlockAttrs` and `POST /api/attr/batchGetBlockAttrs` return a block&#x27;s full attribute set (IAL) with no publish-access check. Both are `CheckAuth`-only, so they are reachable by the publish `RoleReader` token and by the anonymous account when `Publish.Au…

---

## 19. 🟡 High Severity — SiYuan: Password (protected) tier omitted in the attribute-view/database publish filter: Reader receives rows of protected documents without the password (publish mode)

**CVE:** `CVE-2026-72806` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-03
**Reference:** <https://github.com/advisories/GHSA-6mcf-g667-w3qv>

> **CVE:** This vulnerability corresponds to [CVE-2026-72806](https://nvd.nist.gov/vuln/detail/CVE-2026-72806).

### Summary

`FilterViewByPublishAccess`, the filter `renderAttributeView` applies for Reader sessions drops rows using only the hidden/forbidden check and never checks the publish password. Its three sibling filters all check both tiers. As a result, a publish `RoleReader` (or the anonym…

---

## 20. 🟡 High Severity — SiYuan: Second-order SSTI to arbitrary SQL via attribute-view template column (queryBlocks): malicious imported package executes SQL on victim kernel

**CVE:** `CVE-2026-72807` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-03
**Reference:** <https://github.com/advisories/GHSA-x67c-8pwr-m8g3>

> **CVE:** This vulnerability corresponds to [CVE-2026-72807](https://nvd.nist.gov/vuln/detail/CVE-2026-72807).

### Summary

Attribute-view (AV) template columns are live-evaluated on every render and expose the `queryBlocks` template function, which runs raw SQL on the read-write database handle (`SelectBlocksRawStmt`, using `?`→argument string substitution rather than parameter binding). AV mutat…

---

## 21. 🟡 High Severity — SiYuan: Missing publish-access filter on getFileAnnotation discloses private PDF annotations of forbidden/protected documents (publish mode)

**CVE:** `CVE-2026-72808` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-03
**Reference:** <https://github.com/advisories/GHSA-v7ph-r5r6-4jcj>

> **CVE:** This vulnerability corresponds to [CVE-2026-72808](https://nvd.nist.gov/vuln/detail/CVE-2026-72808).

### Summary

The `/api/asset/getFileAnnotation` endpoint returns the content of `.sya` PDF-annotation files with no publish-access check. It is gated by `CheckAuth` only, so it is reachable by the publish `RoleReader` token and by the anonymous account when `Publish.Auth.Enable` is `false…

---

## 22. 🟡 High Severity — SiYuan: SQL injection in backlink/mention search via unescaped stored and client input (publish mode): first-order (client keyword) and second-order (stored document title) breakout on read-write handle

**CVE:** `CVE-2026-72811` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-03
**Reference:** <https://github.com/advisories/GHSA-q2vg-7qgx-x5fc>

> **CVE:** This vulnerability corresponds to [CVE-2026-72811](https://nvd.nist.gov/vuln/detail/CVE-2026-72811).

### Summary

The backlink/mention search query (`kernel/model/backlink.go`) concatenates stored block metadata (title, name, alias, anchor text) and the client-supplied keyword into a SQL `MATCH`/search statement, escaping only the double-quote character (`&quot;`) and not the single quot…

---

## 23. 🟡 High Severity — SiYuan: Unauthenticated SQL execution and REGEXP injection via fullTextSearchAssetContent (publish mode): reader-reachable raw SQL (method 2) and unescaped REGEXP (method 3) on read-write asset-content DB

**CVE:** `CVE-2026-69083` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-03
**Reference:** <https://github.com/advisories/GHSA-fph3-ghq9-vw66>

> **CVE:** This vulnerability corresponds to [CVE-2026-69083](https://nvd.nist.gov/vuln/detail/CVE-2026-69083).

### Summary

The `/api/search/fullTextSearchAssetContent` endpoint exposes two SQL flaws on the asset-content database, both reachable by the publish `RoleReader` token and by the anonymous account when `Publish.Auth.Enable` is `false`:

1. **method 2** passes a client-supplied SQL statem…

---

## 24. 🟡 High Severity — SiYuan: Unauthenticated arbitrary SQL execution via searchEmbedBlock (publish mode) : reader-reachable raw statement on read-write handle, cross-notebook read/write

**CVE:** `CVE-2026-69084` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-03
**Reference:** <https://github.com/advisories/GHSA-vh22-h7hf-www7>

> **CVE:** This vulnerability corresponds to [CVE-2026-69084](https://nvd.nist.gov/vuln/detail/CVE-2026-69084).

### Summary

The `/api/search/searchEmbedBlock` endpoint passes a client-supplied SQL statement verbatim to the database with no validation. The endpoint is gated by `CheckAuth` only reachable by the publish RoleReader token, and by the anonymous account when `Publish.Auth.Enable` is `fal…

---

## 25. 🟡 High Severity — ApostropheCMS: Mutation-XSS / allowedTags bypass via literal `</textarea/>` solidus close

**CVE:** `CVE-2026-63670` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-03
**Reference:** <https://github.com/advisories/GHSA-jxwj-j7wr-gfrw>

> ### Summary
A mutation-XSS / allowedTags bypass: when `textarea` (or `xmp`) is included in `allowedTags`, an input containing a literal `&lt;/textarea/&gt;` (a solidus right after the RCDATA end-tag name) lets non-allowed markup such as `&lt;img src=x onerror=…&gt;` pass through `sanitizeHtml()` **live and unescaped**, even though `img`/`onerror` are not in the allowlist. A spec-compliant browser …

---

## 26. 🟡 High Severity — TOON: Prototype pollution when decoding untrusted TOON input

**CVE:** `CVE-2026-82404` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-03
**Reference:** <https://github.com/advisories/GHSA-p95v-992w-h6c3>

> ### Summary

Decoding attacker-controlled TOON containing a `__proto__`, `constructor`, or `prototype` key wrote through the object&#x27;s prototype chain instead of creating an own property, polluting `Object.prototype` for the whole runtime. The `expandPaths: &#x27;safe&#x27;` path (dotted keys such as `a.__proto__.x`) was the strongest vector; plain nested objects, tabular rows, and quoted keys…

---

## 27. 🟡 High Severity — Semaphore UI: Manager-to-owner privilege escalation via custom-role slug collision

**CVE:** `CVE-2026-73293` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-03
**Reference:** <https://github.com/advisories/GHSA-cxvf-gvfq-36w2>

> ## Summary

Semaphore resolves a project member&#x27;s effective permissions in `ProjectMiddleware` by looking up a role row whose slug matches the member&#x27;s assigned role, and overwrites the built-in permission bitmask with that row&#x27;s value. A member holding the built-in `manager` role creates a custom project role through `POST /api/project/{id}/roles`, a route gated only by the `CanMan…

---

## 28. 🟡 High Severity — Orval: RCE via OpenAPI path -> unescaped request-URL template literal (backtick breakout)

**CVE:** `CVE-2026-62681` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-03
**Reference:** <https://github.com/advisories/GHSA-fg9p-mrxr-hvq7>

> ### Summary

Orval emits the OpenAPI path into the generated request URL as a TEMPLATE LITERAL (`` `/users/...` ``) without escaping the backtick character. A path containing a backtick closes the template literal and injects a concatenation expression that is evaluated when the generated URL/request/key function is called, executing attacker-controlled code. Affects the axios, fetch, react-query,…

---

## 29. 🟡 High Severity — Orval: Import-time RCE via query parameter name -> computed-property-key injection in the zod cli

**CVE:** `CVE-2026-71865` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-03
**Reference:** <https://github.com/advisories/GHSA-653q-5476-x79g>

> ### Summary

orval&#x27;s zod client emits each query parameter name as a double-quoted key in the generated zod.object({...}) request-validation schema WITHOUT escaping the double quote. A &quot; in the query parameter name closes the key and lands in object-literal context, where an injected computed property key [expr] is evaluated when zod.object({...}) runs -- at MODULE IMPORT (export const O…

---

## 30. 🟡 High Severity — Orval: Import-time RCE via header parameter name -> computed-property-key injection in the zod client

**CVE:** `CVE-2026-71864` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-03
**Reference:** <https://github.com/advisories/GHSA-6437-gxhq-pqv8>

> ### Summary

orval&#x27;s zod client emits each header parameter name as a double-quoted key in the generated zod.object({...}) request-validation schema WITHOUT escaping the double quote. A &quot; in the header parameter name closes the key and lands in object-literal context, where an injected computed property key [expr] is evaluated when zod.object({...}) runs -- at MODULE IMPORT (export const…

---

## 31. 🟡 High Severity — VictoriaMetrics vmrestore: Path traversal via crafted backup part names escapes restore root

**CVE:** `CVE-2026-61625` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-03
**Reference:** <https://github.com/advisories/GHSA-8q3c-rjr9-xxrp>

> ### Summary
The VictoriaMetrics `vmrestore` utility does not validate backup part path components before writing restored files to the local filesystem. An attacker who can provide or modify a backup source can craft object names containing `..` path components that cause vmrestore to write files outside the intended `-storageDataPath` restore root, subject to the permissions of the `vmrestore` pr…

---

## 32. 🟡 High Severity — Cilium may unexpectedly allow ingress traffic from the local namespace when a Kubernetes NetworkPolicy is configured with an ipBlock match

**CVE:** `CVE-2026-56743` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-03
**Reference:** <https://github.com/advisories/GHSA-fm8w-2m5w-9j7r>

> ### Impact

Standard Kubernetes `NetworkPolicy` specifications using CIDR-based `ipBlock` rules without pod or namespace selectors erroneously generate a wildcard namespace allow rule under specific cluster configurations.

When Cilium deployment is configured with a specific custom `clusterName` (rather than the default `&quot;any&quot;` value), the parser incorrectly instantiates a pod selector …

---

## 33. 🟡 High Severity — unstructured: Server-Side Request Forgery in the URL-based partitioning

**CVE:** `CVE-2026-71428` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-03
**Reference:** <https://github.com/advisories/GHSA-4mvj-m6j5-pmf7>

> ### Summary

Server-Side Request Forgery in `unstructured`. The `url=` argument of `partition()`, `partition_html()`, and `partition_md()` is fetched via `requests.get()` with no host validation. The response body is returned as `Element` text, so this is a **full-read SSRF** — attackers reach loopback admin APIs, internal HTTP services, and cloud metadata endpoints, and read the response. 

`unst…

---

## 34. 🟡 High Severity — Critical Cisco Nexus 9000 Flaw Lets Unauthenticated Remote Attackers Run Code as Root

**CVE:** `CVE-2026-20212` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-09-03
**Reference:** <https://thehackernews.com/2026/09/critical-cisco-nexus-9000-flaw-lets.html>

> Cisco has released patches to address a critical security flaw affecting 10 Silicon One-based Nexus 9000 switches that could allow an unauthenticated, remote attacker to execute code as root, alongside an IOS XR hardening release bundling 7 umbrella CVEs, 2 of which are rated 9.8, with no workaround for any IOS XR version.

The Nexus vulnerability, tracked as CVE-2026-20212 (CVSS score: 9.8), is

---

## 35. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
