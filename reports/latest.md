# Zero Day Pulse

> **Generated:** 2026-07-09 19:23 UTC &nbsp;|&nbsp; **Total:** 29 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 15 &nbsp;|&nbsp; 🟡 High: 14 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** SimpleHelp versions 5.5.7 and earlier contain unauthenticated path traversal vulnerabilities (CWE-22) that allow a remote, unauthenticated attacker to send specially crafted HTTP requests containing directory-traversal sequences (e.g., '..') to vulnerable SimpleHelp endpoints to read arbitrary files from the host's file system. Exposed files include server configuration files (e.g., serverconfig.xml) that contain secrets and hashed user/technician passwords, which can then facilitate follow-on access. The vulnerability is exploitable over the network with low attack complexity, requires no privileges or user interaction, and yields high confidentiality impact with no integrity or availability impact.
- **Affected Products:** SimpleHelp Remote Support Software (Remote Monitoring and Management) version 5.5.7 and all earlier releases.
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true — Public PoC available at https://github.com/imjdl/CVE-2024-57727
- **Patch Available:** true — Patches released January 8–13, 2025: v5.5.8, v5.4.10, and v5.3.9. Vendor advisory: https://guides.simple-help.com/kb---security-vulnerabilities-01-2025
- **Active Exploitation:** true — CISA Advisory AA25-163A (June 12, 2025) documents active in-the-wild exploitation of CVE-2024-57727 by ransomware actors since January 2025 against unpatched SimpleHelp RMM instances used by a utility billing software provider and downstream customers, in double-extortion ransomware operations.
- **Threat Actors:** DragonForce ransomware actors (per CISA Advisory AA25-163A, June 12, 2025). CISA attributes exploitation of CVE-2024-57727 in unpatched SimpleHelp RMM instances since January 2025 to DragonForce, who used the access to compromise downstream customers (including a utility billing software provider) for double-extortion ransomware operations.
- **Mitigation:** Apply official SimpleHelp patches immediately: upgrade to v5.5.8 or later, or apply v5.4.10 / v5.3.9 for those branches. Additional hardening: change Administrator and Technician account passwords (if not using third-party auth); rotate/reissue API tokens; restrict source IP addresses for Technician/Administrator logins, API requests, and firewall connections; disable local SimpleHelpAdmin user and local Technician account logins (prefer AD/LDAP); configure Server Event alerts for admin logins, failed logins, and configuration changes; add SimpleHelp binaries to endpoint security allowlists; until patched, isolate the SimpleHelp server from the internet or stop the SimpleHelp process; threat-hunt for suspicious executables with three-letter alphabetic filenames (e.g., aaa.exe, bbb.exe) created after January 2025; maintain offline backups and an asset inventory; avoid exposing RDP to the internet.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) embeds attacker-controlled instructions in external content (websites, emails, calendar invites, documents) consumed by an LLM-powered agent. Because the model cannot reliably distinguish trusted instructions from untrusted data, the hidden payload is interpreted as a command rather than content, hijacking the agent's behavior. Obfuscation techniques include: zero-width Unicode characters, homoglyph substitution (Cyrillic/Greek for Latin), payload splitting across HTML elements, Base64/canvas/off-screen-DOM rendering, jailbreak personas (e.g., 'DAN', 'developer mode'), and tag/keyword smuggling (e.g., the meta-tag keyword 'ultrathink' used to redirect AI actions to attacker-controlled payment links). Confirmed real-world outcomes include data exfiltration, denial-of-service via infinite-text streams that time out agents, destructive commands (e.g., 'delete all files'), ad-review evasion to approve scam ads, SEO/traffic hijacking, financial fraud (PayPal/Stripe donation redirection), and bypassing Gemini's privacy controls via a calendar-invite payload that calls the Calendar.create tool to leak meeting summaries.
- **Affected Products:** Gemini, Google Workspace with Gemini (Gmail, Docs), LLM-based AI agents/assistants, and AI ad-review systems. No specific versions are listed because Indirect Prompt Injection is a class of vulnerability, not a single version-specific bug.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true - multiple weaponized in-the-wild examples confirmed: (1) AI ad-review evasion scam at hxxps[:]//reviewerpress[.]com/advertorial-maxvision-can/?lang=en redirecting to reviewerpressus.mycartpanda[.]com (Unit 42); (2) Google Gemini calendar-invite semantic attack exfiltrating private meeting data (Miggo, http://miggo.io/post/weaponizing-calendar-invites-a-semantic-attack-on-google-gemini); (3) benign PoC at http://github.com/brennanbrown/atlas-prompt-injection-poc; (4) additional Unit 42 IOCs: leroibear[.]com, myshantispa[.]com, perceptivepumpkin[.]com, shiftypumpkin[.]com, splintered[.]co[.]uk, storage3d[.]com, trinca.tornidor[.]com, turnedninja[.]com, runners-daily-blog[.]com.
- **Patch Available:** false - Indirect Prompt Injection is a class of vulnerability, not a single bug, so there is no single vendor patch. Google continuously hardens Gemini and Workspace with Gemini and ships mitigations iteratively (see http://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections).
- **Active Exploitation:** true - confirmed in the wild. Google's Threat Intelligence team analysis of Common Crawl data identified hundreds of millions of pages containing adversarial IPI payloads; Palo Alto Unit 42 documented active AI-ad-review evasion scams with named IOCs (reviewerpress[.]com, leroibear[.]com, myshantispa[.]com, perceptivepumpkin[.]com, shiftypumpkin[.]com, splintered[.]co[.]uk, storage3d[.]com, trinca.tornidor[.]com, turnedninja[.]com, runners-daily-blog[.]com); Miggo Security disclosed a real-world calendar-invite prompt-injection attack against Google Gemini that exfiltrated private meeting data (http://miggo.io/post/weaponizing-calendar-invites-a-semantic-attack-on-google-gemini, Jan 19 2026); Forcepoint documented 10 IPI payloads caught in the wild (Apr 22 2026).
- **Threat Actors:** None known (the Google post does not name any specific threat actor group, APT, or ransomware operator; it only references generic 'individual website authors' and unspecified threat actors. Separately, CVE-2026-55255 Langflow exploitation was attributed to an opportunistic, financially motivated actor using a scripted toolkit per Sysdig TRT, but this is a different vulnerability.)
- **Mitigation:** Google's recommended layered defense strategy for Workspace with Gemini and other AI products: (1) Deterministic defenses — user confirmation prompts before sensitive actions, URL sanitization, tool-chaining policies, regex takedowns; (2) ML-based defenses — retraining ML models with synthetic injection data; (3) LLM-based defenses — prompt engineering with refined system instructions and an explicit instruction hierarchy; (4) Gemini model hardening — improving the model's internal ability to ignore harmful instructions inside data; (5) Industry-standard defenses — spotlighting (separating untrusted web content from trusted instructions), adversarial training/red-teaming, human-in-the-loop approval for high-risk actions, least-privilege tool access, input/output filtering (semantic filters, string-checking, RAG Triad), and adversarial attack simulation. Google's AI Vulnerability Reward Program is also used to source external research.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) targets large language models (LLMs) integrated with multiple external data sources, such as Workspace with Gemini. Rather than sending malicious instructions directly to the model, an attacker embeds adversarial instructions within content the LLM is asked to process: emails, documents, web pages, calendar entries, or app notifications. When the user invokes a Gemini feature (e.g., 'Summarize this email' or a voice assistant query), the LLM ingests both the legitimate user prompt and the attacker-controlled content; the model may treat the embedded instructions as authoritative, causing unintended actions such as phishing the user, exfiltrating data, redirecting queries, performing unauthorized tool calls, or leaking system and internal instructions. IPI is particularly dangerous for agentic LLM applications because tool-use automation can convert subtle prompt hijacks into real-world side effects, and attacks can sometimes succeed without any direct user input beyond the initial legitimate request.
- **Affected Products:** Google Workspace with Gemini (Gmail summarization, Google Docs, Google Drive, Google Chat, Google Slides), Google Gemini app (standalone), Gemini on Android (voice assistant and Utilities/Android agent). Related disclosed vulnerabilities also affect Gemini CLI and Gemini voice assistant on Android. Specific version numbers are not provided in the Google blog post.
- **CVSS Score:** CVSS score unavailable. No numeric CVSS v3.x base score is published by Google for the indirect prompt injection vulnerability class described in this advisory.
- **CVSS Vector:** CVSS vector unavailable. The Google Security Blog post describes indirect prompt injection as an evolving vulnerability class rather than a specific CVE-assigned issue; no CVSS:3.x vector string is published with this advisory.
- **Exploit Available:** true - SafeBreach published a public proof-of-concept (with demonstration videos) on June 3, 2026 showing indirect prompt injection hijacking of the Gemini voice assistant on Android via messaging notification content. Source: https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/
- **Patch Available:** false - There is no single official patch that fully removes the indirect prompt injection vulnerability class. Google treats IPI as a continuously evolving threat mitigated through the layered defenses described above rather than as a discrete software update. However, individual specific IPI vulnerabilities disclosed by external researchers have been patched separately (e.g., SafeBreach's Gemini voice-assistant IPI was patched after approximately three months, and a SafeBreach Gemini calendar-invite IPI enabling smart-home control and data leakage was also patched by Google).
- **Active Exploitation:** true - Confirmed exploitation in the wild has been reported. Evidence includes: (1) Palo Alto Unit 42 documented real-world adversarial websites using IPI against AI agents for ad-review evasion, SEO manipulation, data destruction, denial-of-service, and forced phishing/payment flows, with the first instance reviewed in December 2025 (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/); (2) Help Net Security reported in April 2026 that the Gemini-in-Gmail summarizer was actively abused using hidden white-text and '<Admin>' tag instructions to append fake phishing security alerts (https://helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild); (3) an arXiv empirical study identified 15,387 prompt-injection instances across Common Crawl, Shodan, and Censys, indicating the technique is operationalized at scale; (4) SafeBreach demonstrated real hijacking of the Gemini voice assistant on Android via messaging notification content.
- **Threat Actors:** None known. No specific APT groups, ransomware operators, or named threat actor campaigns have been publicly attributed to exploiting indirect prompt injection against Google Workspace with Gemini. Security researchers (Palo Alto Unit 42, SafeBreach, 0DIN) have documented IPI exploitation by unnamed adversaries for ad-review evasion, SEO manipulation, phishing payload delivery, data destruction, denial-of-service, and system prompt leakage, but no formal threat actor attribution exists.
- **Mitigation:** Google's documented mitigation is a layered defense strategy applied to Gemini: (1) prompt-injection content classifiers that flag suspicious inputs before they reach the model; (2) security thought reinforcement to train the model to prioritize the user's intended task and ignore embedded adversarial instructions; (3) markdown sanitization and suspicious-URL redaction that strip potentially harmful formatting or known-malicious links from input/output; (4) a user confirmation (human-in-the-loop) framework requiring explicit approval for sensitive AI-generated actions; (5) end-user security notifications that surface mitigated risks; and (6) underlying model resilience and adversarial robustness training. Workspace admins are also advised to apply managed Gemini rollout controls, restrict Gemini to trusted data sources where feasible, and keep productivity data classification and review enabled. Note: Google explicitly states IPI cannot be 'solved' once; mitigations are continuously improved rather than delivered as a single complete patch.
- **Vendor Advisory:** https://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is a class of attack in which adversaries embed malicious instructions in web content (malicious sites, third-party content inside iframes, or user-generated content such as reviews) that a Gemini-powered agent ingests while browsing on the user's behalf. Because the agentic model treats retrieved page content as instructions, attackers can goal-hijack the agent, exfiltrate sensitive credentials or other browser/page data via model-generated URLs or external requests, initiate unauthorized financial transactions, or trick the agent into interacting with arbitrary origins in ways that bypass Chrome's Site Isolation. A separate but related Chrome/Gemini attack surface was disclosed by Unit 42 in CVE-2026-0628, in which Chrome extensions with the declarativeNetRequest permission were able to inject JavaScript into the privileged Gemini browser panel, escalating to local file access and privacy invasion.
- **Affected Products:** Google Chrome with Gemini agentic capabilities (agentic browsing preview). No specific Chrome version is enumerated in the blog post—the post describes new architectural defenses being rolled out to the latest Chrome builds.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — Public proof-of-concept demonstrations of indirect prompt injection against AI/agentic browsers exist (https://github.com/brennanbrown/atlas-prompt-injection-poc). Additionally, Palo Alto Networks Unit 42 publicly disclosed a related Chrome-specific flaw, CVE-2026-0628, where extensions with declarativeNetRequest permissions could inject JavaScript into Chrome's Gemini panel (https://unit42.paloaltonetworks.com/gemini-live-in-chrome-hijacking/).
- **Patch Available:** true — No single CVE patch is associated with this blog post; instead, Google states that the layered defenses are being deployed via Chrome's auto-update mechanism. For the separate CVE-2026-0628 Chrome Gemini-panel extension hijack flaw, Google shipped a patch in early January 2026.
- **Active Exploitation:** false — No public reporting has confirmed active in-the-wild exploitation of Chrome's Gemini agentic capabilities via indirect prompt injection. (Unit 42's March 2026 write-up of CVE-2026-0628 notes the flaw was patched quickly; it does not report in-the-wild exploitation of Chrome agentic browsing.)
- **Threat Actors:** None known
- **Mitigation:** Chrome is deploying a layered defense architecture announced in the Dec 8, 2025 blog post: (1) User Alignment Critic — an isolated Gemini-based model that reviews proposed actions against the user's task using only metadata, not unfiltered web content; (2) Agent Origin Sets — extending Chrome's same-origin / Site Isolation policy so the agent classifies origins as read-only or read-writable and is limited via a trustworthy gating function; (3) Spotlighting — channels that instruct the model to prioritize user/system instructions over page content; (4) Prompt-Injection Classifier — a parallel model that scans every page the agent consumes for likely injections; (5) User Confirmations — mandatory human approval for sensitive categories such as banking, medical sites, Google Password Manager sign-ins, payments, and outbound messages; (6) Deterministic URL Checks — restricts model-generated URLs to a known, public allow-list to prevent covert exfiltration; (7) Transparency Tools — a real-time work log letting users observe, pause, or stop tasks; (8) Automated Red-Teaming — LLM-driven generation of malicious sandboxed sites for continuous adversarial testing. Hardening advice: keep Chrome auto-update enabled, minimize the agent's permissions on untrusted sites, prefer Origin Sets read-only mode for unknown sites, avoid letting agentic features act on sensitive origins without confirmation, and audit installed extensions.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2025-48530 is the first Rust-based memory safety vulnerability discovered in Android. It is a linear buffer overflow in CrabbyAVIF, the Rust AVIF image parser/decoder within the Android System component. Incorrect bounds checks in multiple code paths — including YUV planes, alpha plane, Y plane, UV planes, chroma width calculation, plane size calculation, and row bytes — result in out-of-bounds memory accesses (CWE-125: Out-of-Bounds Read). When chained with other bugs, these OOB accesses could enable remote code execution on the Android system with no user interaction and no additional execution privileges required. The attack surface is network-reachable. The vulnerability was neutralized by Google's Scudo hardened allocator, whose guard pages around secondary allocations deterministically prevented exploitation.
- **Affected Products:** Google Android 16 / AOSP 16 (Android System component, CrabbyAVIF AVIF parser/decoder); versions prior to security patch level 2025-08-05
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the Android Security Bulletin August 2025 patches, updating affected Android 16 devices to security patch level 2025-08-05 or later. Additional hardening: ensure Android's Scudo hardened allocator is enabled (default on modern Android), implement network segmentation, limit network exposure of unpatched devices, and apply strict firewall rules until the patch is deployed.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection embeds hidden adversarial instructions inside external content that an LLM later ingests as part of its normal retrieval-augmented workflow — for example, malicious instructions placed inside an email body, a document, or the description field of a calendar invite. When Gemini is asked by the user to summarize, retrieve, or act on that external content, the model parses the hostile text alongside the legitimate prompt and can be coerced into exfiltrating sensitive user data, performing unauthorized actions via connected tools, or otherwise deviating from the user's original intent.
- **Affected Products:** Google Gemini 2.5 models; Gemini in Google Workspace apps (Gmail, Google Docs editors, Google Drive, Google Chat, Google Calendar); Gemini app
- **CVSS Score:** CVSS score unavailable. No CVE was assigned by Google for the vulnerability class described, and the blog post does not provide a CVSS v3.x base score.
- **CVSS Vector:** CVSS vector unavailable. The Google blog post is a class-of-vulnerability discussion rather than a CVE-naming advisory, so no CVSS v3 vector is published.
- **Exploit Available:** true. Multiple researcher-published PoCs exist: SafeBreach (calendar-invite data exfiltration, disclosed Feb 2025); Miggo (semantic attack on Gemini via calendar invites, Jan 2026); Cyera Research Labs (command and prompt injection in Gemini CLI, Nov 2025).
- **Patch Available:** true. Google's mitigations are deployed as continuous layered defenses rather than a single discrete patch. The advisory URL is: http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html. For related Gemini CLI command/prompt injection issues, Google issued patches referenced by Cyera Research Labs.
- **Active Exploitation:** false. The Google blog post and supporting documentation do not report confirmed in-the-wild exploitation. Documented cases are ethical-researcher demonstrations disclosed to Google, not observed malicious abuse by threat actors.
- **Threat Actors:** None known. The Google blog post does not name any specific threat actor groups, APT campaigns, or ransomware operators exploiting indirect prompt injection against Gemini.
- **Mitigation:** Google's layered defense strategy (no single patch; defenses are continuously deployed): (1) Gemini 2.5 model hardening via adversarial training; (2) prompt-injection content classifiers that detect malicious instructions in retrieved content; (3) markdown sanitization to block EchoLeak-style image exfiltration; (4) suspicious URL redaction via Google Safe Browsing; (5) human-in-the-loop user confirmation for risky actions; (6) end-user security notifications in Gmail, Docs, Drive, and Chat. Administrators should keep Gemini in Workspace current and review admin guidance. End users should treat unsolicited external content with caution and verify confirmation prompts before approving.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors target large backbone routers of major telecommunications providers and provider-edge (PE) / customer-edge (CE) routers, then leverage trusted interconnections to pivot between networks. Techniques include: modifying router configurations (ACLs, routing tables, TACACS+/RADIUS servers) to maintain persistent access; exploiting Cisco IOS XE Web Services Management Agent (WSMA) endpoints (/webui_wsma_Http or /webui_wsma_Https) using double URL encoding (e.g., /%2577eb%2575i_%2577sma_Http) to bypass authentication; executing commands via SNMP; abusing Cisco Guest Shell (virtualized containers on network devices) for stealthy execution and evasion; creating GRE, mGRE, and IPsec tunnels between compromised devices for multi-hop pivoting; and using publicly available tools such as siet.py, map.tcl, tclproxy.tcl, wodSSHServer, and STOWAWAY. Actors sometimes name their ACLs 'access-list 20' as an indicator. Compromised edge devices and trusted provider connections are used to fan out into government, transportation, lodging, and military networks.
- **Affected Products:** Ivanti Connect Secure and Ivanti Policy Secure (CVE-2024-21887, CVE-2023-46805); Palo Alto Networks PAN-OS GlobalProtect (CVE-2024-3400); Cisco IOS XE (CVE-2023-20273, CVE-2023-20198); Cisco IOS and IOS XE / Cisco Smart Install (CVE-2018-0171); Cisco NX-OS; additional suspected targets include Fortinet firewalls, Juniper firewalls, Microsoft Exchange, Nokia routers and switches, Sierra Wireless devices, and SonicWall firewalls.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — actors are actively weaponizing publicly known exploits for the referenced CVEs (CVE-2024-21887, CVE-2023-46805, CVE-2024-3400, CVE-2023-20273, CVE-2023-20198, CVE-2018-0171). Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a
- **Patch Available:** true — vendor patches exist for all referenced CVEs. The advisory states 'If not yet patched, defenders should prioritize the following CVEs' and references post-patch behavior of fixed releases. Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a
- **Active Exploitation:** true — CISA, NSA, FBI, and partner agencies confirm PRC state-sponsored actors have been actively compromising telecommunications, government, transportation, lodging, and military infrastructure networks globally since at least 2021 to support a global espionage system. Sources: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a (joint advisory published Sep 3, 2025).
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, and GhostEmperor (PRC state-sponsored actors; linked to Sichuan Juxinhe Network Technology Co. Ltd., Beijing Huanyu Tianqiong Information Technology Co., Ltd., and Sichuan Zhixin Ruijie Network Technology Co., Ltd.)
- **Mitigation:** 1) Prioritize patching the referenced CVEs in the recommended order: CVE-2023-20198 and CVE-2023-20273 (Cisco IOS XE first), then CVE-2024-3400 (PAN-OS GlobalProtect), CVE-2024-21887 and CVE-2023-46805 (Ivanti), and CVE-2018-0171 (Cisco Smart Install). 2) Audit device configurations for unexpected GRE/mGRE/IPsec tunnels, unexpected external IPs configured as TACACS+/RADIUS servers, unexpected external IPs in ACLs, unexpected packet capture/traffic mirroring settings, and unexpected virtual containers running on network devices. 3) Enforce secure management: use SNMPv3, disable Telnet and unencrypted HTTP, validate firmware/images against vendor-supplied hashes with signed image enforcement, and verify local/router accounts. 4) Disable or monitor Cisco Guest Shell. 5) Replace unsupported/end-of-life devices with vendor-supported hardware running current software. 6) Implement robust change management with periodic configuration audits, and baseline router configurations (ACLs, remote-access settings, routing tables) for change detection.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2023-23397 is a critical Microsoft Outlook vulnerability involving an NTLM credential leak. An attacker crafts a malicious email containing the MAPI extended property PidLidReminderFileParameter, whose value is set to a Universal Naming Convention (UNC) path pointing to an attacker-controlled server (e.g., \\attacker.com\share\file.wav). When Outlook processes the message—without requiring user interaction in many cases, such as upon receipt or preview—it automatically attempts to fetch the referenced 'reminder sound file' over SMB (TCP/445). This triggers Windows to perform NTLMv2 authentication to the attacker's UNC target, leaking the victim's NetNTLMv2 hash. The attacker can then relay the hash (e.g., via NTLM relay attacks) or crack it offline to obtain the user's plaintext credentials, enabling further lateral movement, privilege escalation, or persistent access within the target environment.
- **Affected Products:** Microsoft Outlook 2016 (32/64-bit), Microsoft Outlook 2013 SP1 (32/64-bit), Microsoft Outlook 2013 RT SP1, Microsoft Office 2019 (32/64-bit), Microsoft 365 Apps for Enterprise (32/64-bit), Microsoft Office LTSC 2021 (32/64-bit) — all versions prior to March 14, 2023 security updates.
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true — Public PoC available at https://github.com/Trackflaw/CVE-2023-23397. The PoC generates a malicious .msg file containing a UNC path in the PidLidReminderFileParameter MAPI property, which triggers an outbound SMB connection and NetNTLMv2 hash leak when Outlook processes the message.
- **Patch Available:** true — Microsoft released patches on March 14, 2023. Patches are available at: https://msrc.microsoft.com/update-guide/vulnerability/cve-2023-23397. Specific KBs: KB5002254 (Outlook 2016), KB5002265 (Outlook 2013 SP1); Click-to-Run updates for Office 2019, Microsoft 365 Apps, and Office LTSC 2021.
- **Active Exploitation:** true — Confirmed active exploitation. Sources: (1) CISA Joint Cybersecurity Advisory AA25-141A (May 21, 2025) confirms GRU Unit 26165 weaponized CVE-2023-23397 to collect NTLM hashes from Western logistics entities coordinating aid to Ukraine since 2022 (https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a); (2) CISA Known Exploited Vulnerabilities Catalog lists CVE-2023-23397 as actively exploited (https://www.cisa.gov/known-exploited-vulnerabilities-catalog); (3) Microsoft Security Response Center confirmed exploitation observed in the wild at the time of the March 2023 patch release.
- **Threat Actors:** Russian GRU 85th Main Special Service Center (85th GTsSS), military unit 26165 — tracked as APT28, Fancy Bear, Forest Blizzard, Strontium, BlueDelta, and Sednit. CISA attributes the exploitation of CVE-2023-23365 to this actor per AA25-141A.
- **Mitigation:** 1) Apply Microsoft security updates released March 14, 2023: KB5002254 for Outlook 2016, KB5002265 for Outlook 2013 SP1, and corresponding Click-to-Run updates for Office 2019, Microsoft 365 Apps, and Office LTSC 2021. 2) Block outbound SMB (TCP/445) and WebDAV traffic from client networks at the perimeter firewall. 3) Disable NTLMv1 and require NTLMv2 with SMB/LDAP signing and Extended Protection for Authentication (EPA) where possible. 4) Add privileged accounts to the 'Protected Users' security group to prevent NTLM authentication. 5) Enable Microsoft Defender Attack Surface Reduction (ASR) rules to block executable content from email clients and prevent Office applications from creating child processes. 6) Monitor Windows Event Logs (4624/4776) for NTLM authentications to external IPs and audit Outlook calendar/reminder MAPI properties for UNC paths. 7) For ICS/SCADA environments (as referenced in CISA AA25-141A), replace unsupported devices, apply firmware updates, change default credentials, enforce MFA, and disable UPnP/P2P/FTP/unauthenticated RTSP.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/cve-2023-23397

---

## 9. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

**Parallel AI Enrichment:**

- **Technical Details:** This CrowdStrike blog post is a thought-leadership piece on browser security rather than a disclosure of a single specific vulnerability. It describes the general browser-based attack chain: attackers exploit weaknesses in rendering logic, JavaScript execution, document handling, or memory safety in the browser, then perform a sandbox escape, privilege escalation, or other technique to move from browser activity to system-level access. Common browser-mediated techniques cited include phishing, credential theft, malicious downloads, session hijacking, clickjacking, cross-site scripting (XSS), HTML smuggling, adversary-in-the-middle (AitM) attacks, session token theft with MFA bypass, and data exfiltration. The post notes (citing the Verizon 2026 Data Breach Investigations Report) that vulnerability exploitation surpassed stolen credentials as the top breach entry point in 2025, and (citing the CrowdStrike 2026 Global Threat Report) that 42% of vulnerabilities were exploited before public disclosure, indicating strong adversary interest in zero-day browser exploits.
- **Affected Products:** Chromium-based browsers (no specific versions identified); CrowdStrike Falcon Secure Access (referenced as a defensive solution).
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** The blog recommends evaluating browser risk based on shared components and browser architecture (not just the specific browser brand); validating, testing, staging, and deploying browser updates across both managed and unmanaged devices; and adopting browser-layer defenses such as CrowdStrike Falcon Secure Access, whose zero-day exploit prevention uses a moving-target defense called JavaScript Language Randomization (JSLR) that continuously randomizes the JavaScript runtime environment to make it harder for attackers to exploit browser vulnerabilities even before a patch is available or fully deployed. The post also advises protections against phishing, adversary-in-the-middle attacks, session hijacking, MFA bypass, credential theft, and data exfiltration.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 10. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

**Parallel AI Enrichment:**

- **Technical Details:** Pre-authenticated OS Command Injection in Ivanti Sentry's ConfigServiceController class. The /mics/api/v2/sentry/mics-config/handleMessage endpoint accepts an attacker-supplied 'message' parameter that is parsed into tokens (command, module, xpath, value). When the EXECUTE command is invoked, the input flows through handleExecute() to executeNativeCommand(), which invokes native methods via reflection, allowing a remote unauthenticated attacker to execute arbitrary OS commands as root without authentication.
- **Affected Products:** Ivanti Sentry before R10.5.2 (including 10.5.1 and below), Ivanti Sentry before R10.6.2 (including 10.6.1 and below), Ivanti Sentry before R10.7.1 (including 10.7.0 and below)
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Exploit Available:** true (PoC: https://github.com/watchtowrlabs/watchTowr-vs-Ivanti-Sentry-RCE-CVE-2026-10520-CVE-2026-10523 ; advisory: https://labs.watchtowr.com/more-evidence-that-words-dont-mean-what-we-thought-they-meant-ivanti-sentry-pre-auth-os-command-injection-cve-2026-10520/)
- **Patch Available:** true (https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523)
- **Active Exploitation:** true — Added to the CISA Known Exploited Vulnerabilities (KEV) Catalog on June 11, 2026 (https://www.cisa.gov/news-events/alerts/2026/06/11/cisa-adds-one-known-exploited-vulnerability-catalog); Shadowserver Foundation confirmed in-the-wild exploitation beginning on or around June 10, 2026; exploitation observed within 24 hours of public disclosure (https://www.darkreading.com/vulnerabilities-threats/max-severity-ivanti-sentry-flaw-exploited-24-hours).
- **Threat Actors:** None known
- **Mitigation:** Update affected Ivanti Sentry appliances urgently, outside normal patching cycles, to Ivanti Sentry 10.5.2, 10.6.2, or 10.7.1. Defenders can use the WatchTowr detection script to identify vulnerable appliances. Restrict network access to the Sentry management interface wherever possible until patched.
- **Vendor Advisory:** https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523

---

## 11. 🟠 Zero-Day — CrowdStrike Uncovers New Prompt Injection Techniques

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jul 07, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-uncovers-new-prompt-injection-techniques/>

---

## 12. 🟠 Zero-Day — Wiz in the Verizon DBIR: How AI Acceleration and Cloud Sprawl Impact Modern Defense

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Wiz Research &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://www.wiz.io/blog/verizon-dbir-2026-ai-cloud-security>

> Verizon&#x27;s latest DBIR highlights how attackers are exploiting familiar weaknesses at increasing speed and scale. Here&#x27;s what Wiz research reveals about vulnerabilities, trust relationships, and AI in modern cloud environments.

---

## 13. 🟠 Zero-Day — 12 Million Impacted by Data Breach at Japanese Telco KDDI

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://www.securityweek.com/12-million-impacted-by-data-breach-at-japanese-telco-kddi/>

> Hackers exploited a zero-day vulnerability in a third-party system to access a KDDI email system for ISPs. The post 12 Million Impacted by Data Breach at Japanese Telco KDDI appeared first on SecurityWeek .

---

## 14. 🟠 Zero-Day — GodDamn Ransomware Uses PoisonX Driver to Disable Endpoint Defenses

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://thehackernews.com/2026/07/goddamn-ransomware-uses-poisonx-driver.html>

> Cybersecurity researchers have flagged a new ransomware family called GodDamn that employs the PoisonX kernel driver to neutralize security software as part of its defense evasion strategy.

According to a new report published by the Threat Hunter Team from Symantec, the ransomware was first publicly spotted in the wild on May 21, 2026. It&#x27;s assessed to be a rebrand of the Beast ransomware,

---

## 15. 🟠 Zero-Day — Microsoft patches RoguePlanet Defender zero-day vulnerability

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-rogueplanet-defender-zero-day-vulnerability/>

> Microsoft has released a security patch to address a Defender zero-day vulnerability known as &quot;RoguePlanet,&quot; disclosed after the June 2026 Patch Tuesday. [...]

---

## 16. 🟡 High Severity — Ruby CSS Parser: SSRF and Local File Disclosure in `CssParser::Parser#read_remote_file`

**CVE:** `CVE-2026-53727` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-9pmc-p236-855h>

> ## Summary

`CssParser::Parser#read_remote_file` (and therefore `load_uri!`, and the `@import`-following branch of `add_block!`) issues HTTP/HTTPS requests against any host, port and URI it is handed, with no scheme allowlist, no host / IP filtering, and no protection against link-local, loopback or RFC‑1918 addresses. `Location:` redirects are followed recursively back into the same function, whi…

---

## 17. 🟡 High Severity — org.hl7.fhir.core: ReDoS via FHIRPath matches()/replaceMatches() in FHIR Validator HTTP Endpoint

**CVE:** `CVE-2026-49485` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-7cmj-v6x8-frvv>

> # Summary
All implementations of FHIRPathEngine accept arbitrary FHIRPath expressions and evaluate them without input validation. The utility intended to secure this evaluation did so incorrectly, and did not fully cover all places in which evaluation was being done. An attacker can send a resource containing an evil regex pattern that causes catastrophic backtracking, exhausting system resources,…

---

## 18. 🟡 High Severity — Soup Sieve: Regular Expression Denial of Service (ReDoS) via Selector Parser

**CVE:** `CVE-2026-49477` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-836r-79rf-4m37>

> ### Summary

The CSS selector parser in soupsieve (the CSS selector engine for Beautiful Soup 4) contains a regular expression vulnerable to catastrophic backtracking. When processing an attribute selector with an unterminated quoted value, the `VALUE` regex pattern in `css_parser.py` enters exponential backtracking. A payload of only **300 bytes** causes the regex engine to hang for **over 3 seco…

---

## 19. 🟡 High Severity — Phantom: Arbitrary file write and decode-bomb DoS via unconfined MCP tool paths

**CVE:** `CVE-2026-37555` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-52vm-mxx8-f227>

> ### Impact

In Phantom &lt;= 1.3.0, when `PHANTOM_OUTPUT_DIR` was unset (the default), the MCP tools accepted arbitrary absolute output paths with no confinement. Anything able to send tool calls (e.g. an AI agent driving the MCP interface) could **write or overwrite arbitrary files** the process user can write — including shell startup files (`~/.zshrc`) or a Reaper `__startup.lua`, which is effe…

---

## 20. 🟡 High Severity — pyLoad: SSRF guard bypass via IPv6 6to4/NAT64 transition wrappers of internal IPs

**CVE:** `CVE-2026-48737` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-m5x5-28jr-gpjj>

> ## Summary

`is_global_address` in [`src/pyload/core/utils/web/check.py`](https://github.com/pyload/pyload/blob/1b12dc7f348db8c144e0f39215680415e90ca4d2/src/pyload/core/utils/web/check.py) is the central guard against SSRF-style outbound connections in pyload-ng. It tests whether a given IP is &quot;globally routable&quot; via Python&#x27;s `ipaddress.ip_address(value).is_global`, and callers trea…

---

## 21. 🟡 High Severity — Microsoft Patches RoguePlanet Defender Flaw That Can Grant SYSTEM Privileges

**CVE:** `CVE-2026-50656` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://thehackernews.com/2026/07/microsoft-patches-rogueplanet-defender.html>

> Microsoft has released security updates for a Defender vulnerability known as RoguePlanet, nearly a month after details of the flaw became public.

The vulnerability, tracked as CVE-2026-50656 (CVSS score: 7.8), is a privilege escalation issue in the Microsoft Malware Protection Engine (&quot;mpengine.dll&quot;), which provides scanning, detection, and cleaning capabilities for its antivirus and

---

## 22. 🟡 High Severity — Serena: Unauthenticated Flask dashboard on fixed port enables DNS rebinding → memory poisoning → RCE

**CVE:** `CVE-2026-49471` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://github.com/advisories/GHSA-37h2-6p4f-mp3q>

> ### Summary

Serena&#x27;s built-in web dashboard exposes an unauthenticated Flask API on a fixed, predictable port (TCP 24282, hardcoded as `0x5EDA` in `constants.py`). The server has no authentication, no CSRF protection, and no Host header validation. A DNS rebinding attack allows a malicious webpage to reach this API from any browser and write arbitrary content to the agent&#x27;s persistent m…

---

## 23. 🟡 High Severity — NL Portal: IDOR allows any authenticated user to complete and tamper with another user's taak

**CVE:** `CVE-2026-49464` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://github.com/advisories/GHSA-6h3c-r723-7fx3>

> ## Impact

In versions from 1.5.0 up to and including 3.0.0, any authenticated portal user could complete and tamper with another user&#x27;s open task by submitting it on their behalf. The task submission endpoint accepted a task ID and a payload, but it never checked whether the task actually belonged to the user making the call.

An attacker who held a valid login (a normal `burger` OAuth token…

---

## 24. 🟡 High Severity — NL Portal: Missing per-user authorization on document and decision GraphQL queries in nl-portal-backend-libraries

**CVE:** `CVE-2026-49463` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://github.com/advisories/GHSA-qpm9-h556-mwxm>

> ## Impact

In versions up to and including 3.0.0, two parts of the GraphQL API returned data without checking whether the data belonged to the logged-in user:

- **Document content.** A logged-in user could download the raw content of any document by its ID, regardless of who owned it. The resolver has lacked an authentication parameter since the initial commit of the project (2022-11-22) — so eve…

---

## 25. 🟡 High Severity — Joro: Unauthenticated Cross-Origin Plugin Upload Leads to RCE

**CVE:** `CVE-2026-53649` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://github.com/advisories/GHSA-xqhv-chqm-fhcc>

> # Unauthenticated Cross-Origin Plugin Upload Leads to RCE (Joro ≤ v1.1.0)

**Severity:** Critical
**CVSS v3.1:** 9.6 (AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H)
**Affected versions:** Joro ≤ v1.1.0, proxy mode (default), Linux/macOS
**Reporter:** cstover
**Date:** 2026-05-27

---

## Summary

Joro&#x27;s default proxy mode (in versions &lt;= 1.1.0) exposes a local API on `127.0.0.1:9090` that performs n…

---

## 26. 🟡 High Severity — DSpace has possible Remote Code Execution (RCE)  through Velocity Templates used by LDN

**CVE:** `CVE-2026-49832` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://github.com/advisories/GHSA-9x82-rm84-c6x7>

> ## Overview

Remote Code Execution (RCE) is possible via Velocity Templates used by DSpace for [COAR Notify/LDN messages](https://wiki.lyrasis.org/spaces/DSDOC9x/pages/379126679/COAR+Notify). _This vulnerability impacts DSpace versions 8.0 &lt;= 8.3, 9.0 &lt;= 9.2._ The attacker MUST already have DSpace administrator credentials in order to perform the attack.

This attack is related to the path t…

---

## 27. 🟡 High Severity — Nuclio: Unsanitized cron trigger event headers/body injected into CronJob shell command leads to persistent RCE

**CVE:** `CVE-2026-52831` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://github.com/advisories/GHSA-v5px-423j-pf7p>

> ## Summary

Nuclio controller builds a `curl` invocation string for each cron trigger and stores it as the `args` of a Kubernetes CronJob container (`/bin/sh`, `-c`, `&lt;command&gt;`). Two fields in the trigger specification flow into this string without adequate sanitization:

- `event.headers` keys — interpolated verbatim inside double-quoted `--header` arguments (`lazy.go:2150`); any key conta…

---

## 28. 🟡 High Severity — async-tar PAX extension-header desync enables tar entry/content smuggling

**CVE:** `CVE-2026-53600` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://github.com/advisories/GHSA-35rm-7j9c-2f7m>

> ## Summary

`async-tar` v0.6.0 mis-applies a buffered PAX `size` extension to an intermediary
extension header (a GNU longname `L`, a GNU longlink `K`, or a PAX `x`/`g`
header) instead of to the next *file* entry. POSIX requires a PAX extended-header
record set to describe the next file entry, never an intervening extension
header. Because `poll_next_raw` (`src/archive.rs`) threads the buffered PA…

---

## 29. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
