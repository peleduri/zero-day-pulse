# Zero Day Pulse

> **Generated:** 2026-07-01 09:32 UTC &nbsp;|&nbsp; **Total:** 35 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 16 &nbsp;|&nbsp; 🟡 High: 19 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CWE-22 Path Traversal. SimpleHelp v5.5.7 and earlier exposes HTTP endpoints vulnerable to crafted `../` traversal sequences (e.g., `../../../../../../etc/passwd`), allowing an unauthenticated remote attacker to download arbitrary files including /etc/passwd, SSH private keys (e.g., /root/.ssh/id_rsa), and the SimpleHelp server configuration file containing hashed admin/technician passwords. This is the first link in a three-CVE chain: CVE-2024-57727 (file disclosure) → CVE-2024-57726 (credential use → admin privilege escalation) → CVE-2024-57728 (admin → arbitrary code execution on the SimpleHelp server host).
- **Affected Products:** SimpleHelp Remote Support / Remote Monitoring and Management (RMM), version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Yes - public Metasploit/Rapid7 module available: https://www.rapid7.com/db/modules/auxiliary/scanner/http/simplehelp_toolbox_path_traversal/
- **Patch Available:** Yes - SimpleHelp version 5.5.8 (current production version is 5.5.15). Patch released approximately January 8-13, 2025. Vendor advisory: https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know
- **Active Exploitation:** Yes - confirmed active exploitation in the wild. CISA Advisory AA25-163A (June 12, 2025) documents ransomware actors exploiting CVE-2024-57727 against an unpatched SimpleHelp RMM instance at a utility billing software provider to access and disrupt downstream customer systems in a double-extortion scheme. Broader pattern of exploitation of unpatched SimpleHelp RMM observed since January 2025.
- **Threat Actors:** DragonForce ransomware group
- **Mitigation:** Primary: Upgrade SimpleHelp to version 5.5.8 or later. If upgrading is not immediately possible, isolate the SimpleHelp instance from the internet or stop the server process. For third-party vendors (utility billing software providers): notify downstream customers, ensure endpoint patching, and conduct threat hunting. For downstream customer endpoints: hunt for evidence of compromise, particularly suspicious executables with three-letter alphabetical names (e.g., aaa.exe) created after January 2025. For systems confirmed ransomware-encrypted: disconnect from the internet, perform clean OS reinstall from trusted media, restore from known-good offline backups. Proactive hardening: maintain asset inventory, regular offline backups, avoid exposing remote services (RDP) directly to the internet, perform risk assessments of RMM/remote-support tooling, adopt SBOMs.
- **Vendor Advisory:** https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — Anthropic Restores Claude Fable 5 After U.S. Lifts Jailbreak-Linked Export Controls

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://thehackernews.com/2026/07/anthropic-restores-claude-fable-5-after.html>

> Anthropic is putting Claude Fable 5 back online worldwide. On June 30, the U.S. Commerce Department lifted the export controls it had imposed on Fable and its more tightly controlled sibling Mythos 5 about two and a half weeks earlier.

Fable 5 returns to users on Wednesday, July 1, across Claude.ai, the Claude Platform, Claude Code, and Claude Cowork.

Export controls restrict who can

**Parallel AI Enrichment:**

- **Technical Details:** A 'narrow, non-universal' jailbreak of Claude Fable 5 (and by extension Mythos 5). The attacker submits source code containing software flaws together with the short prompt 'Fix this code.' The coding-assistant framing causes Fable 5's safety classifiers to de-prioritise policy checks, so the model will describe the flaws and, in at least one case, produce working proof-of-concept code. Anthropic publicly disputed the severity: the jailbreak identifies only 'previously known, minor vulnerabilities,' provides no Mythos-specific uplift over publicly available models, and exposes a capability broadly present in other frontier LLMs. The U.S. Commerce Department nevertheless treated it as a national-security concern and imposed Foreign-Direct-Product-Rule-style export controls on 2026-06-12.
- **Affected Products:** Anthropic Claude Fable 5, Anthropic Claude Mythos 5 (Mythos-class 1 model). Served via Claude.ai, the Claude Platform, Claude Code, and Claude Cowork. The pre-2026-06-12 safety-classifier build was affected; the new jailbreak-detection classifier deployed 2026-06-30 mitigates the issue.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable. No CVE has been assigned. This is an AI-model jailbreak/safety-filter bypass, not a CVE-scored traditional software vulnerability.
- **Exploit Available:** Yes — public PoC / description widely available. The technique uses a short natural-language prompt ('Fix this code') prepended to a code sample containing vulnerabilities, causing Fable 5's safety classifiers to de-prioritise policy checks. Reproductions and discussion are publicly available at https://www.techzine.eu/news/security/142189/fix-this-code-three-words-behind-the-export-ban-on-claude-fable-5/, https://news.ycombinator.com/item?id=48552687, and https://www.reddit.com/r/ClaudeAI/comments/1u6tm7g/. Pliny the Liberator subsequently published Fable 5's ~120,000-character system prompt on GitHub (https://www.mallory.ai/stories/019eb249-9807-7fdb-b152-51ed01ef1bea).
- **Patch Available:** Yes — patch available. Anthropic deployed a new safety classifier that detects and blocks the exact Fable 5 jailbreak technique. Deployment of this classifier was the condition on which the U.S. Commerce Department lifted the 2026-06-12 export-control order on 2026-06-30, enabling global restoration of Claude Fable 5 on 2026-07-01. Advisory URL: https://www.anthropic.com/news/fable-mythos-access
- **Active Exploitation:** Active exploitation reported in a limited, demonstrative sense: an unnamed researcher/journalist reproduced the jailbreak and shared it with the U.S. government, prompting the 2026-06-12 export-control directive. Pliny the Liberator publicly extracted and posted Fable 5's ~120,000-character system prompt on GitHub (https://www.mallory.ai/stories/019eb249-9807-7fdb-b152-51ed01ef1bea). The technique's reproduction is documented on Hacker News / Reddit / Techzine. There is no public reporting of the technique being weaponised at scale by an APT, ransomware group, or nation-state campaign. Anthropic's own characterisation is that the jailbreak is 'narrow, non-universal' and the underlying offensive-cyber capability is 'widely available in other publicly available models.'
- **Threat Actors:** None known. No specific APT group, ransomware operator, or named campaign has been attributed to exploiting this jailbreak. The U.S. Commerce Department referenced 'foreign adversaries' generically; the jailbreak was submitted to the government by an unnamed researcher/journalist. Anthropic states the jailbreak 'provides no Mythos-specific uplift' and the underlying capability is widely available in other publicly available LLMs.
- **Mitigation:** Anthropic applied two layers: (1) a new, jailbreak-specific safety classifier trained to recognise the exact 'Fix this code'-style technique and block it before the response is generated — this is the classifier the U.S. Commerce Department cited when lifting controls on 2026-06-30; (2) the existing defense-in-depth safety-classifier stack for Fable 5, which routes flagged cyber- and bio-domain queries to Claude Opus 4.8 instead of Fable 5, supplemented by 30-day traffic retention (with logged human access) for monitoring novel attacks. Cloud Security Alliance's enterprise guidance is to keep at least one pre-validated substitute model (e.g., Opus 4.8) for critical AI workflows, update AI-governance frameworks to treat regulatory suspension as an explicit risk, and audit agentic pipelines for compensating controls / human-in-the-loop review.
- **Vendor Advisory:** https://www.anthropic.com/news/fable-mythos-access

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an attack class where an adversary plants adversarial instructions in untrusted external content (websites, emails, documents). When an AI assistant or agent ingests that content, the model may follow the attacker's commands instead of the user's original intent. Observed effects range from benign tone changes to destructive actions such as file deletion, data exfiltration, payment fraud, browsing redirects, and summary hijacking. Embedding channels include HTML comments, hidden CSS rules, abused accessibility attributes (alt/title), hidden footer tags, invisible source-code instructions, and visible content cards surfaced into the LLM context.
- **Affected Products:** Google Gemini, Google Workspace with Gemini, AI assistants and AI agents generally (Gemini 2.5 mentioned for hardened defense)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes - multiple public PoC/in-the-wild payloads documented. Google blog catalogs six payload archetypes including exfiltration and file-deletion variants. Forcepoint X-Labs independently documented 10 live IPI payloads on real domains at http://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads
- **Patch Available:** No traditional software patch (no CVE, no versioned fixed build). Instead, continuous model hardening — Google ships adversarial-resistance improvements to Gemini 2.5 as ongoing model updates and retraining via the Simula synthetic-data pipeline. Workspace customers receive the upgrades automatically. References: http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html, https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/, https://blog.google/security/mitigating-prompt-injection-attacks/
- **Active Exploitation:** Yes — confirmed, ongoing, in the wild. Google observed a 32% relative increase in the malicious-category IPI payloads between November 2025 and February 2026 via Common Crawl sweep, and six payload archetypes including destructive actions found live. Forcepoint X-Labs independently documented 10 live IPI payloads on real public websites across exfiltration, destruction, fraud, hijack, and DoS vectors (April 22, 2026). SecurityWeek reported increased attempts against generative-AI browsing features.
- **Threat Actors:** None known
- **Mitigation:** Adopt Google's layered defense-in-depth strategy: (1) Deterministic controls — centralized Policy Engine with tool-chaining policies, URL sanitization, regex-based point fixes, and user confirmation before sensitive tool calls. (2) ML-based controls — prompt-injection content classifiers flagging adversarial instructions. (3) LLM-based controls — iterative prompt engineering plus security thought reinforcement; Gemini 2.5 hardened with adversarial training via the Simula synthetic-data framework. (4) Output hardening — URLs flagged by Google Safe Browsing are shown to users as 'suspicious link removed.' (5) Detection/disclosure — red-teaming, AI Vulnerability Reward Program, and threat-intel feeds. For third-party agents: layer these controls, gate sensitive tool calls with user confirmation, sandbox file-system and payment actions, treat all ingested content as untrusted. Reference: https://saif.google/focus-on-agents.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) places malicious instructions inside external data or tools (documents, emails, calendar invites, web pages, voice content, RAG sources) that Gemini consumes alongside the user's prompt. Documented variants include: (1) chatbot hijacking forcing information disclosure; (2) summarizer compromise via hidden document instructions causing unauthorized actions such as sending emails; (3) RAG-based data exfiltration (GeminiJack) using poisoned shared content to push sensitive data to attacker-controlled URLs disguised as external image requests; (4) calendar-invite poisoning (Miggo) injecting natural-language payloads that cause Gemini to summarize private meetings and write data into a new event via Calendar.create; (5) voice-assistant 'Fake Context Alignment' (SafeBreach) using hidden but visually-rendered instructions aligned to a spoken 'yes' for tool authorization; (6) web-agent rendering tricks (off-screen CSS, invisible characters, CDATA, base64, multi-lingual splitting) observed by Unit 42 in-the-wild.
- **Affected Products:** Google Workspace with Gemini (Gmail, Google Docs, Google Drive, Chat, Calendar), Gemini app (consumer), Gemini Enterprise, Vertex AI Search, Gemini voice assistant / Android Utilities agent. Specific version numbers not publicly listed.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — multiple public PoCs: (1) GeminiJack by Noma Labs — http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability ; (2) Calendar-Invite IPI 'Semantic Attack' by Miggo — https://www.miggo.io/post/weaponizing-calendar-invites-a-semantic-attack-on-google-gemini ; (3) 'Gemini's Secret Affair' voice-assistant IPI by SafeBreach — https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/ ; (4) 10 in-the-wild IPI payloads captured by Forcepoint X-Labs — https://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads ; (5) Web-based IPI in the wild observed by Unit 42 — https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/
- **Patch Available:** No single version patch — Google treats IPI mitigation as a continuous, layered defense rolled out across Gemini deployments. Related, specific fixes: GeminiJack mitigated (Vertex AI Search separated from Gemini Enterprise, Dec 2025); Miggo calendar-invite IPI mitigated after responsible disclosure (Jan 2026); Gemini CLI / run-gemini-cli trust model hardened (GHSA-wpqr-6v78-jr5g, Apr 23 2026); CVE-2026-12537 fixed in Gemini CLI 0.39.1 (separate, not the focus of the IPI blog). SafeBreach voice-assistant PoC mitigation status unknown. Reference URL: http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html
- **Active Exploitation:** Yes — confirmed in-the-wild. Sources: Google's companion post documenting a public-web sweep of IPI patterns; Unit 42 (Palo Alto Networks, Mar 3 2026) 'Web-Based Indirect Prompt Injection Observed in the Wild'; Forcepoint X-Labs (Apr 22 2026) '10 Indirect Prompt Injection Payloads Caught in the Wild'; SecurityWeek on increased malicious AI prompt-injection attempts; GTIG AI Threat Tracker (Feb 12 2026) on APT-level actors integrating Gemini (with indirect prompt injection) into their kill chain; GeminiJack (Noma Labs) functional zero-click exploit.
- **Threat Actors:** APT31, APT41, APT42, APT43, UNC795, DRAGONBRIDGE, KRYMSKYBRIDGE, Doppelganger, HONESTCUE-associated PRC-linked group (PRC and Iran state-aligned actors leveraging Gemini with indirect prompt injection observed by GTIG)
- **Mitigation:** Google's layered defenses: (1) prompt-injection content classifiers; (2) system-prompt 'thought reinforcement' reminding the LLM to ignore adversarial input; (3) markdown/URL sanitization using Google Safe Browsing; (4) human-in-the-loop (HITL) user confirmation for risky tool actions; (5) centralized Policy Engine for URL sanitization, tool-chaining policy, and rapid point fixes; (6) Gemini model hardening to ignore embedded adversarial commands while honoring user intent; (7) ML retraining via 'Simula' synthetic attacks; (8) iterative LLM-based defenses via refined system instructions; (9) proactive discovery via red teaming, the Google AI Vulnerability Rewards Program (VRP), and OSINT monitoring; (10) end-user contextual notifications when injection attempts are blocked. General advice: define AI-trust boundaries, monitor agent behavior, and apply least-privilege.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is the primary new threat facing agentic browsers like Chrome with Gemini. Attackers embed malicious instructions inside content (malicious websites, third-party frames, user-generated content like reviews) that the agentic browser ingests. Because the agent processes untrusted web content, that content is treated as instructions, causing the Gemini-powered agent to take unwanted actions (financial transactions, data exfiltration, state changes, sensitive-site interactions). The related CVE-2026-0628 used a malicious Chrome extension's declarativeNetRequests API to inject JavaScript into the privileged Gemini browser panel at gemini.google.com/app, enabling privilege escalation that exposed the camera, microphone, local files and the ability to screenshot any HTTPS page. The GeminiJack flaw abused Gemini Enterprise's Retrieval-Augmented Generation pipeline: hidden instructions planted in Google Workspace content (Docs, Gmail subjects, Calendar descriptions) were returned to Gemini as part of normal search retrieves and executed as commands, exfiltrating data via crafted <img src=attacker-host/...?x> requests.
- **Affected Products:** Google Chrome with Gemini in Chrome and agentic browsing (preview) capabilities; Google Chrome prior to 143.0.7499.192 (desktop: Windows, Mac, Linux) for related CVE-2026-0628; Google Gemini Enterprise and Vertex AI Search (for GeminiJack); Cursor AI code editor versions below 1.3 (CVE-2025-54131).
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H (for the closely related CVE-2026-0628 Chrome WebView privilege-escalation flaw in the same Gemini agentic threat class). The underlying blog-post threat class has no vendor-assigned CVSS v3 vector; for the cursor-side chained disclosure CVE-2025-54131 only CVSS v4.0 metrics are published.
- **Exploit Available:** Yes. Multiple public PoCs and weaponized exploits are available: (1) Noma Labs' GeminiJack payload published 8 December 2025 demonstrating data exfiltration from poisoned Google Workspace content (https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/); (2) Palo Alto Unit 42's private exploit of CVE-2026-0628 (Chrome Gemini panel hijack via malicious Chrome extension using declarativeNetRequests API) (https://unit42.paloaltonetworks.com/gemini-live-in-chrome-hijacking/); (3) Forcepoint's catalog of 10 in-the-wild indirect prompt injection payloads (https://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads); (4) Unit 42's 'Fooling AI Agents' generic IPI payload library (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/).
- **Patch Available:** Yes. (1) For the related Chrome/Gemini vulnerability CVE-2026-0628: patched in Google Chrome 143.0.7499.192 via the Stable Channel Update for Desktop released January 6, 2026 (https://chromereleases.googleblog.com/2026/01/stable-channel-update-for-desktop.html). (2) For GeminiJack: Google updated the integration between Gemini Enterprise / Vertex AI Search and its retrieval/indexing systems, fully separating Vertex AI Search from Gemini Enterprise so they no longer share LLM-powered workflows or RAG capabilities (confirmed by Noma Labs, December 2025). (3) The Chrome-side agentic security architecture described in the December 8, 2025 blog post (Spotlighting, User Alignment Critic, Origin Sets, Confirmations, Prompt-Injection Classifier) was rolled out as part of Gemini in Chrome GA and the agentic-browsing preview, with continuous iteration. (4) For CVE-2025-54131 (Cursor IDE chained via IPI): fixed in Cursor version 1.3.
- **Active Exploitation:** Yes - confirmed in-the-wild exploitation. Palo Alto Unit 42 documented web-based indirect prompt injection observed in the wild against AI agents with active campaigns delivering payloads via domains such as reviewerpress[.]com, 1winofficialsite[.]in, splintered[.]co[.]uk (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/). The closely related CVE-2026-0628 (Chrome Gemini Live hijack, CVSS 8.8) had a working pre-patch exploit acknowledged by Google and patched in early January 2026. Google Security Blog and SecurityWeek reported a measurable increase in malicious indirect-prompt-injection attempts observed on the public web (https://blog.google/security/prompt-injections-web, https://securityweek.com/malicious-ai-prompt-injection-attacks-increasing-but-sophistication-still-low-google). Forcepoint additionally cataloged 10 indirect prompt injection payloads caught live in the wild (https://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads). Google's Threat Intelligence Group (GTIG) has documented nation-state APTs (APT31, APT41, UNC6418, UNC795, HONESTCUE) actively using Gemini to support attack lifecycle phases.
- **Threat Actors:** APT groups weaponizing Gemini per Google Threat Intelligence Group (GTIG): UNC6418 (used Gemini for credential harvesting targeting Ukraine / defense sector), Temp.HEX (compiled intel on Pakistan targets using Gemini), APT31 (used Gemini to automate vulnerability analysis against US targets including RCE/WAF bypass/SQLi), APT41 (used Gemini to accelerate malicious tooling development), UNC795 (Gemini-assisted tradecraft), and the HONESTCUE malware family / Xanthorox jailbreak service. Iranian APT 'Screening Serpens' (per Palo Alto Unit 42) is also documented conducting 2026 influence/espionage campaigns leveraging indirect prompt injection against AI agents. Additionally, web attackers and macOS malvertising operators (e.g. Operation FlutterBridge) have been observed delivering IPI payloads against AI agents on the open web.
- **Mitigation:** Google introduced layered architectural mitigations in Chrome for Gemini agentic capabilities: (1) User Alignment Critic - separate Gemini model isolated from untrusted content that vets each proposed action for task alignment and can veto misaligned actions; (2) Spotlighting - directs the model to prioritize user/system instructions over page/iframe content; (3) Agent Origin Sets - gating function that restricts the agent to a defined set of read-only origins versus read/writable origins; (4) Mandatory user confirmations for sensitive actions (banking, medical, password manager) and consequential actions (purchases, payments, messages); (5) Prompt-Injection Classifier - real-time scanner running in parallel with the planning model detecting malicious targeting; (6) Safe Browsing and on-device AI to detect traditional scams; (7) Automated Red-Teaming - systems that continuously generate adversarial sandboxed sites to harden defenses. Users / enterprises should additionally limit which origins are added to the agent origin set, require confirmations for any non-read-only action, and enable Advanced Web Protection features (e.g. Prisma Browser Live Page Scanning) to mitigate CVE-2026-0628-style extension attacks.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2025-48530 is a linear buffer overflow in CrabbyAVIF (Rust-based AVIF image decoder in AOSP at platform/external/rust/crabbyavif). The bug arose from an incorrect bounds-check logic in `unsafe` Rust code blocks, allowing out-of-bounds accesses (CWE-125). Per NVD: 'In multiple locations, there is a possible condition that results in OOB accesses due to an incorrect bounds check. This could lead to remote code execution in combination with other bugs, with no additional execution privileges needed. User interaction is not needed for exploitation.' Although Rust normally enforces memory safety, `unsafe` blocks are not covered by those guarantees.
- **Affected Products:** Android platform (CrabbyAVIF component in platform/external/rust/crabbyavif); builds prior to security patch level 2025-08-05
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** No public proof-of-concept or weaponized exploit available. Vulnerability was intercepted internally before public release, and Scudo hardened allocator's guard pages rendered it non-exploitable in practice.
- **Patch Available:** Yes. Official Android Security Bulletin August 2025 (https://source.android.com/security/bulletin/2025-08-01) addresses CVE-2025-48530 (Android-ID ASB-A-419563680). End-user patch level: 2025-08-05. Source-code fixes available at https://android.googlesource.com/platform/external/rust/crabbyavif/+/42feb427 and https://android.googlesource.com/platform/external/rust/crabbyavif/+/75486a2.
- **Active Exploitation:** No confirmed active exploitation. Google describes the vulnerability as a 'near-miss' caught internally before reaching public release. CVE databases (SentinelOne) list 'Known Exploited: No'. NVD carries no in-the-wild exploitation references.
- **Threat Actors:** None known
- **Mitigation:** Two layers: (1) Hardening via Android's Scudo hardened allocator, which uses guard pages around secondary allocations to prevent exploitation of the OOB access in practice; (2) Code fix: bounds-check logic corrected in CrabbyAVIF (commits 42feb427a and 75486a2a). End users should update to Android security patch level 2025-08-05 or later.
- **Vendor Advisory:** https://blog.google/security/rust-in-android-move-fast-fix-things/ (https://source.android.com/security/bulletin/2025-08-01 for CVE-2025-48530)

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is a vulnerability class where attackers embed hidden malicious instructions inside content that an AI assistant (e.g., Gemini) later ingests as part of normal processing — e.g., emails, documents, calendar invites, Drive files, log records, or web pages. When the model parses that content alongside a user-initiated task, the injected instructions cause the AI to exfiltrate user data, perform unauthorized actions (e.g., deleting calendar events), manipulate summaries, or steer the user toward phishing/malicious links. It differs from direct prompt injection in that the payload arrives via trusted third-party content rather than the user's literal prompt. The blog frames this as the primary emerging attack surface against Gemini 2.5, the Gemini app, and Gemini in Workspace (Gmail, Docs, Drive, Chat).
- **Affected Products:** Gemini 2.5, Gemini app, Gemini in Google Workspace (Gmail, Docs editors, Drive, Chat). NOTE: CVE-2025-32711 (EchoLeak) mentioned in the blog applies to Microsoft 365 Copilot and is explicitly not applicable to Gemini.
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit is referenced within the Google Security Blog post for Gemini-specific indirect prompt injection. The post links to Google's defensive research paper ('Lessons from Defending Gemini Against Indirect Prompt Injections') rather than any exploit code. Independent disclosures exist outside this blog (e.g., Tenable TRA-2025-10 for Gemini Cloud Assist, 0din 'Phishing For Gemini', SafeBreach Gemini Voice Assistant research) but are not referenced by the blog itself.
- **Patch Available:** Defenses are integrated directly into Gemini 2.5 (built and continually improved via adversarial training informed by curated real-world vulnerability examples). There is no separate downloadable patch — hardening ships with Gemini 2.5 model and Workspace product updates. Advisory reference: http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html
- **Active Exploitation:** No confirmed mass exploitation of Gemini via indirect prompt injection was reported in the Google Security Blog post. The blog frames indirect prompt injection as an 'emerging attack vector' and references adversarial experimentation rather than confirmed in-the-wild attacks on Gemini. Google's April 2026 follow-up 'AI threats in the wild' reports that threat actors seed prompt injections on websites to attempt corrupting AI browsers, but activity remains experimental/low-sophistication (SEO manipulation, pranks, resource-wasting, low-effort exfiltration tries) with no specific adversary group publicly attributed. Note: separate public research has demonstrated Gemini-specific prompt-injection exploitation chains (0din 'Phishing For Gemini', Miggo 'Weaponizing calendar invites', SafeBreach Gemini Voice Assistant), which represent proof-of-concept exploitation but not necessarily widespread mass exploitation as assessed by Google in this blog.
- **Threat Actors:** None known.
- **Mitigation:** Google's layered defense strategy documented in the blog comprises five defense layers: (1) Prompt injection content classifiers — proprietary ML models that flag suspicious inputs in ingested content; (2) Security thought reinforcement — targeted system instructions that harden model behavior against rogue commands; (3) Markdown sanitization and suspicious URL redaction — rendered content is stripped of dangerous links using Google Safe Browsing; (4) User confirmation framework — human-in-the-loop (HITL) confirmation prompts for risky actions such as deleting calendar events; (5) End-user security mitigation notifications and help-center documentation. Underpinning practices include manual and automated red-teaming, adversarial training data fed into Gemini 2.5's training pipeline, continual updates to Google's internal vulnerability catalog, and adoption of the Secure AI Framework (SAIF). Hardening is integrated into Gemini 2.5 rather than delivered as a downloadable patch.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** AA25-239A is not a single-CVE vulnerability but a joint CSA describing a sustained PRC-state-actor campaign compromising network-edge devices (especially backbone and PE/CE routers) by chaining exploitation of publicly known, previously-patched CVEs. Attack flow: (1) Initial access via CVE-2023-20198 (Cisco IOS XE Web UI authentication bypass) chained with CVE-2023-20273 (post-auth privilege escalation to root); CVE-2024-3400 (Palo Alto GlobalProtect unauth command injection); CVE-2024-21887+CVE-2023-46805 chain (Ivanti Connect Secure); CVE-2018-0171 (Cisco Smart Install RCE); CVE-2024-39717 (Versa Director file upload). (2) Persistence via SSH keys/local accounts, non-standard high-port HTTP/HTTPS/SSH servers, modified ACLs (notably access-list 10, 20, 50 with final 'deny any any log' removed), abused RANCID credentials, custom Tcl scripts, SNMP SET requests, GRE/mGRE/IPsec tunnels. (3) Defense evasion via Cisco IOS XE/NX-OS Guest Shell (iox) Linux container — staging tooling, dumping TACACS+/RADIUS PCAPs, clearing logs, disabling syslog forwarding. (4) Lateral movement via trusted provider-to-provider/provider-to-customer interconnections. (5) Exfiltration via GRE/IPsec tunnels and custom SFTP tooling relayed through VPS. Exploitation of zero-day vulnerabilities has not been observed — all observed exploitation leverages publicly known, previously disclosed CVEs.
- **Affected Products:** Cisco IOS and IOS XE Software (Smart Install client feature and Web UI feature), Cisco NX-OS, Cisco IOS XR; Ivanti Connect Secure versions 9.x and 22.x; Ivanti Policy Secure versions 9.x and 22.x; Palo Alto Networks PAN-OS devices exposing the GlobalProtect feature (PAN-OS versions before 11.1, including 10.2 and 11.0/11.1 pre-fix); Versa Director versions 21.2.2, 21.2.3 (pre 2024-06-21 hot-fix), 22.1.1 (all), 22.1.2 (pre 2024-06-21 hot-fix), and 22.1.3 (pre 2024-06-21 hot-fix). Additional vendors targeted or suspected include Fortinet firewalls, Juniper firewalls, Microsoft Exchange on-premises, Nokia routers/switches, Sierra Wireless devices, and SonicWall firewalls.
- **CVSS Score:** 10.0
- **CVSS Vector:** Not a single CVSS vector — AA25-239A aggregates multiple CVEs. Per-CVE CVSS v3.x base vectors: CVE-2018-0171 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, 9.8); CVE-2023-20198 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H, 10.0); CVE-2023-20273 (CVSS base score 7.2 High); CVE-2024-21887 (CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H, 9.1); CVE-2024-3400 (CVSS:3.1 base 10.0; CVSS:4.0 base 10.0); CVE-2024-39717 (CVSS:3.1 base 7.2 High).
- **Exploit Available:** Yes. Public proof-of-concept (PoC) and weaponized exploits are publicly available for multiple CVEs: (1) CVE-2023-20198 — Python PoC at https://github.com/smokeintheshell/CVE-2023-20198 and Horizon3.ai deep-dive PoC at https://horizon3.ai/attack-research/attack-blogs/cisco-ios-xe-cve-2023-20198-deep-dive-and-poc/ (creates a privilege-15 local user); (2) CVE-2018-0171 — Smart Install crash/DoS PoC at https://www.exploit-db.com/exploits/44451; (3) CVE-2024-21887 — command injection PoC at https://github.com/Chocapikk/CVE-2024-21887, often chained with CVE-2023-46805 authentication-bypass tool. PRC actors themselves have operated weaponized in-the-wild exploit chains, notably CVE-2023-20198+CVE-2023-20273 and CVE-2024-21887+CVE-2023-46805.
- **Patch Available:** Yes — patches are available from each responsible vendor for every CVE in the advisory: Cisco patches via cisco-sa-20180328-smi2 (CVE-2018-0171, Smart Install RCE) and cisco-sa-iosxe-webui-privesc-j22SaA4z (CVE-2023-20198 / CVE-2023-20273) and IOS XE 17.9.4a and later releases; Ivanti patches for Connect Secure and Policy Secure versions 9.x and 22.x mitigating CVE-2024-21887 (and chained CVE-2023-46805); Palo Alto Networks patched CVE-2024-3400 in PAN-OS 11.1 hot-fixes and later (https://security.paloaltonetworks.com/CVE-2024-3400); Versa Networks patched CVE-2024-39717 in Versa Director via the 2024-06-21 hot-fix and in version 22.1.4 (https://versa-networks.com/blog/versa-security-bulletin-update-on-cve-2024-39717-versa-director-dangerous-file-type-upload-vulnerability/). The advisory strongly urges prioritizing installation of these vendor patches first.
- **Active Exploitation:** Confirmed active exploitation in the wild. CISA, NSA, FBI and international co-authors assess that PRC state-sponsored actors have been actively and successfully exploiting these publicly known CVEs on exposed network-edge devices since at least 2021. Trusted industry reporting from Picus Security, SafeBreach, AttackIQ, Lumen/Black Lotus Labs, and NJCCIC corroborates ongoing Salt Typhoon/OPERATOR PANDA activity. CISA explicitly states in AA25-239A that exploitation of zero-day vulnerabilities has not been observed to date — all observed exploitation leverages previously disclosed, patchable CVEs. Sources include the CISA advisory (https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a), Picus Security (https://www.picussecurity.com/resource/blog/cisa-alert-aa25-239a-analysis-simulation-and-mitigation-of-chinese-apts), SafeBreach (https://www.safebreach.com/blog/safebreach-coverage-for-cert-alert-aa25-239a/), AttackIQ (https://www.attackiq.com/2025/09/04/cisa-advisory-aa25-239a/), Forward Networks (https://community.forwardnetworks.com/general-discussions-38/cisa-advisory-aa25-239a-salt-typhoon-guestsh), NJCCIC (https://www.cyber.nj.gov/threat-landscape/nation-state-threat-analysis-reports/china-linked-cyber-operations-targeting-us-critical-infrastructure/salt-typhoon), and Lumen Black Lotus Labs on CVE-2024-39717 (https://www.lumen.com/blog/en-us/uncovering-versa-director-zero-day-exploitation).
- **Threat Actors:** Chinese (PRC) state-sponsored cyber threat actors operating on behalf of China's Ministry of State Security (MSS) and People's Liberation Army (PLA). Industry-tracked clusters named in the advisory: Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, and GhostEmperor (industry aliases include FamousSparrow, Earth Estries, and UNC2286). Three front companies identify in industry reporting: Sichuan Juxinhe Network Technology Co. Ltd., Beijing Huanyu Tianqiong Information Technology Co. Ltd., and Sichuan Zhixin Ruijie Network Technology Co. Ltd.
- **Mitigation:** Prioritized mitigations for defenders of communications-infrastructure networks: (a) Disable Cisco Smart Install feature on all IOS/IOS XE devices ('no vstack'); (b) Disable HTTP/HTTPS web-management servers on devices affected by CVE-2023-20198 ('no ip http server' and 'no ip http secure-server'); (c) Disable Guest Shell ('guestshell disable') and IOx ('iox') subsystems where not operationally required; (d) Verify there is a final 'deny any any log' on every configured ACL; (e) Replace weak Type 5/Type 7 secrets with strong Type 8 PBKDF2-SHA-256 or Type 6 AES; (f) Audit devices for non-standard high ports (TCP/22, 80, 443, 8080, 8443, and Cisco IOS XR 'sshd_operns' on 57722); (g) Use 'transport output none' on VTY lines to block outbound connections; (h) Migrate to SNMPv3 with auth/privacy; (i) Baseline/audit device configurations for unauthorized ACL changes, GRE/IPsec/mGRE tunnels, SPAN/RSPAN/ERSPAN rules, TACACS+/RADIUS changes, unexpected virtual containers; (j) Hunt for specific IoCs in CISA's companion JSON STIX bundle (AA25-239A JSON, 86.01 KB). Recommended companion hardening baseline: CISA's 'Enhanced Visibility and Hardening Guidance for Communications Infrastructure' (Dec 4, 2024) plus joint 'Identifying and Mitigating Living Off the Land' guidance (AA24-038A).
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** GRU Unit 26165 (APT28) has conducted a multi-stage cyber-espionage campaign against Western logistics and IT companies since 2022. The attack lifecycle uses reconnaissance of exposed IP cameras (including Hikvision backdoor); initial access via spearphishing (T1566), credential brute-force and password spraying (T1110), VPN exploitation, and SQL injection; exploitation of named CVEs — CVE-2023-23397 (crafted Outlook calendar invite triggers SMB connection leaking NetNTLMv2 hash, T1187), CVE-2020-12641/CVE-2021-44026/CVE-2020-35730 (Roundcube RCE/SQLi/XSS for mailbox harvesting, T1114), CVE-2023-38831 (WinRAR RCE via benign-named file in ZIP invoking malicious sibling executable, T1659), CVE-2017-7921 (Hikvision camera authentication bypass via 'YWRmaW46MTEK'); execution of HEADLACE, MASEPIE, OCEANMAP, and STEELHOOK malware with persistence via Registry Run keys and DLL search-order hijacking; lateral movement via RDP, Impacket, and PsExec; credential dumping via ntdsutil, Get-GPPPassword.py, ldap-dump.py, Certipy, and ADExplorer; defense evasion via wevtutil log clearing; exfiltration via ZIP archives and OpenSSH.
- **Affected Products:** Microsoft Outlook for Windows (CVE-2023-23397, all versions prior to March 2023 patch); Roundcube Webmail before 1.4.4 (CVE-2020-12641); Roundcube Webmail LTS 1.3 before 1.3.17 and LTS 1.4 before 1.4.12 (CVE-2020-35730, CVE-2021-44026); RARLAB WinRAR before 6.23 (CVE-2023-38831); Hikvision DS-2CD2xx2F-I IP cameras, firmware V5.2.0 build 140721 through V5.4.0 build 160530 (CVE-2017-7921)
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H (for CVE-2023-23397, the primary exploited vulnerability)
- **Exploit Available:** Yes — public PoC code is available on GitHub: CVE-2023-23397 (https://github.com/Trackflaw/CVE-2023-23397), CVE-2023-38831 (https://github.com/HDCE-inc/CVE-2023-38831), CVE-2020-12641 (https://github.com/mbadanoiu/CVE-2020-12641), and CVE-2017-7921 (https://github.com/K3ysTr0K3R/CVE-2017-7921-EXPLOIT). The advisory documents APT28 weaponized exploitation in the field.
- **Patch Available:** Yes — official vendor patches are available for all exploited CVEs: Microsoft Outlook CVE-2023-23397 (patch released March 14, 2023, https://msrc.microsoft.com/update-guide/vulnerability/cve-2023-23397); Roundcube Webmail CVE-2020-12641/0x35730/0x44026 (security updates published Nov 12, 2021 to 1.3.17 and 1.4.12, https://roundcube.net/news/2021/11/12/security-updates-1.4.12-and-1.3.17-released); RARLAB WinRAR CVE-2023-38831 (WinRAR 6.23 released Aug 23, 2023, https://www.win-rar.com/winrar-changelog-bugs.html); Hikvision CVE-2017-7921 (patched firmware, https://www.hikvision.com/us-en/support/document-center/special-notices/privilege-escalating-vulnerability-in-certain-hikvision-ip-cameras/).
- **Active Exploitation:** Yes — confirmed active in-the-wild exploitation by APT28 (GRU Unit 26165) since at least 2022. This is the explicit subject of joint advisory AA25-141A, co-authored by CISA, FBI, NSA, DoD Cyber Crime Center, and Australian Signals Directorate (ASD/ACSC), published May 21, 2025 (revised April 17, 2026). The advisory documents targeted spearphishing and broad password-spray/VPN/SQLi operations against named Western logistics and IT companies. Independent validation from AttackIQ (May 21, 2025), SafeBreach (May 22, 2025), and SOC Prime (May 22, 2025) corroborates the active exploitation.
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS), Military Unit 26165 — tracked under industry aliases APT28, Fancy Bear, Forest Blizzard, STRONTIUM, Sednit, Sofacy, and Tsar Team
- **Mitigation:** General: apply network segmentation and Zero-Trust architecture, host firewalls/IDS, allow only legitimate east-west traffic, deploy EDR with priority on mail servers, DCs, and ICS/OT, audit access logs, block/alert on outbound NTLM/SMB to non-corporate networks, enable Microsoft attack-surface-reduction rules, monitor Windows logs. Identity: enforce phishing-resistant MFA (hardware tokens) for admin accounts, reduce/separate admin roles, throttle accounts (5-10 attempts before lockout), remove passwords stored in GPP and rotate, require SSO and rotate default/service credentials. IP-cameras: replace unsupported hardware, apply vendor firmware, disable UPnP/P2P/Anonymous Visit/FTP/web UI, use firewall with IP allow-list, require VPN+MFA for remote management, enable only authenticated RTSP, monitor logs. Patches: install March 2023 (or later) Outlook security update; upgrade Roundcube to 1.4.4+ or LTS 1.4.12 / 1.3.17+; upgrade WinRAR to 6.23+ (current 7.x); apply Hikvision vendor firmware patch for the IPC authentication bypass. Detect/hunt: monitor for IOCs in STIX bundle AA25-141A, block traffic to actor-controlled hosting/API-mocking services, look for suspicious OpenSSH/Impacket/PsExec/Certipy/ldap-dump/ADExplorer activity.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

**Parallel AI Enrichment:**

- **Technical Details:** The blog describes a generalized browser attack model rather than a specific vulnerability. Attack vectors cited include: exploitation of rendering logic, JavaScript execution, document handling, or memory-safety weaknesses, often chained with sandbox escape and privilege escalation to move from browser activity to system-level access. Because Chromium is a shared core, a single vulnerability in it can affect multiple browsers. Additional attack paths mentioned: phishing, clickjacking, cross-site scripting (XSS), HTML smuggling, malicious downloads, credential theft, session hijacking/abuse, adversary-in-the-middle (AiTM) attacks, and MFA bypass. The shared-component risk model means vendors may customize, harden, disable features, or patch on different timelines, so exposure varies per browser.
- **Affected Products:** Chromium-based browsers (Chrome, Microsoft Edge, Opera, Brave, etc.); no specific versions identified
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) or weaponized exploit is referenced in the article. The blog notes in general terms that exploits can become publicly available after disclosure for N-day vulnerabilities, but cites no specific example.
- **Patch Available:** No specific vendor patch or patch advisory is referenced (no specific CVE is discussed). The post notes that browser vendors issue patches but that discovery-to-deployment creates a 'dangerous gap' that is growing with the 'rise of frontier AI models.'
- **Active Exploitation:** Yes — general browser exploitation is confirmed by industry statistics cited in the blog. Per the CrowdStrike 2026 Global Threat Report: '42% of vulnerabilities were exploited before public disclosure.' Per the Verizon 2026 Data Breach Investigations Report: 'vulnerability exploitation surpassed stolen credentials as the top breach entry point in 2025.' These statistics refer to general browser exploitation activity rather than a specific vulnerability.
- **Threat Actors:** None known
- **Mitigation:** (1) Timely patching of browser vulnerabilities across managed and unmanaged devices; (2) Layered defenses that operate inside the browser session at the point of execution; (3) Blocking of phishing and adversary-in-the-middle (AiTM) techniques; (4) Protection of session tokens against hijacking and MFA bypass; (5) Prevention of credential theft and data exfiltration; (6) Defense-in-depth beyond traditional network and endpoint controls. CrowdStrike promotes Falcon Secure Access with JavaScript Language Randomization (JSLR) — a 'moving target defense' that continuously randomizes the JavaScript runtime environment to disrupt zero-day browser exploitation before patches are deployed.
- **Vendor Advisory:** https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/

---

## 11. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 12. 🟠 Zero-Day — Phantom Squatting Uses AI-Hallucinated Domains for Phishing and Malware

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://thehackernews.com/2026/07/phantom-squatting-uses-ai-hallucinated.html>

> Large language models keep inventing web addresses that do not exist. Attackers have started buying those made-up domains before anyone else can, then hosting phishing pages on them to catch traffic that AI tools point their way.

Palo Alto Networks&#x27; Unit 42 calls the trick phantom squatting, and its new research shows it is already happening in the wild.

The reason it matters is

---

## 13. 🟠 Zero-Day — New BioShocking attack manipulates AI browser into data theft

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://www.bleepingcomputer.com/news/security/new-bioshocking-attack-manipulates-ai-browser-into-data-theft/>

> A new prompt injection attack dubbed &quot;BioShocking&quot; could trick AI-powered browsers into treating real-world risky actions as part of a fictional scenario, causing them to ignore any safety guardrails. [...]

---

## 14. 🟠 Zero-Day — oban_web missing authorization check on `save-job` event handler

**CVE:** `CVE-2026-48592` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-389x-rgxr-8m33>

> ### Summary

`oban_web` 2.12.0 through the current unpatched release exposes a `save-job` LiveView event handler that performs no authorization check, allowing any authenticated user (including those with `:read_only` access) to overwrite a queued job&#x27;s `worker` field with any other `Oban.Worker` module present in the application. On the job&#x27;s next execution attempt, Oban dispatches `per…

---

## 15. 🟠 Zero-Day — Fake Perplexity extension on Chrome Web Store tracked searches

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://www.bleepingcomputer.com/news/security/fake-perplexity-extension-on-chrome-web-store-tracked-searches/>

> A malicious extension in the Chrome Web Store is masquerading as the Perplexity AI answer engine, intercepting search traffic and collecting browsing information. [...]

---

## 16. 🟠 Zero-Day — BlueHammer Vulnerability Exploited in Ransomware Attacks

**CVE:** `CVE-2026-33825` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://www.securityweek.com/bluehammer-vulnerability-exploited-in-ransomware-attacks/>

> The Microsoft Defender vulnerability CVE-2026-33825 was exploited in the wild as a zero-day before patches were released. The post BlueHammer Vulnerability Exploited in Ransomware Attacks appeared first on SecurityWeek .

---

## 17. 🟡 High Severity — Citrix Patches Six NetScaler Flaws Allowing File Read and Denial-of-Service

**CVE:** `CVE-2026-8451` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://thehackernews.com/2026/07/citrix-patches-six-netscaler-flaws.html>

> Citrix on Tuesday released security updates to address multiple flaws in NetScaler ADC (formerly Citrix ADC) and NetScaler Gateway (formerly Citrix Gateway) that could be exploited by an attacker to facilitate arbitrary file reads or trigger a denial-of-service (DoS) condition.

The vulnerabilities are listed below -


  CVE-2026-8451 (CVSS score: 8.8) - An insufficient input validation

---

## 18. 🟡 High Severity — Twig: Sandbox `__toString()` policy bypass via `Traversable` in `join` and `replace` filters

**CVE:** `CVE-2026-48807` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-8x9c-rmqh-456c>

> ### Description

This is a residual bypass of CVE-2026-47732 / GHSA-pr2w-4gpj-cpq4 left after the initial fix for unguarded `__toString()` calls. It covers two related coercion points that were not caught by the original patch.

**`Traversable` in `join` and `replace` filters.** `SandboxExtension::ensureToStringAllowed()` recurses into PHP arrays so that a `Stringable` object hidden inside an arra…

---

## 19. 🟡 High Severity — Fulcio has OIDC Discovery Redirect Following Allows SSRF and JWKS Substitution for Meta-Issuer Paths, with Kubernetes Service-Account Token Leakage

**CVE:** `CVE-2026-49478` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-f5mr-q85p-6hh6>

> ## Impact

Three security vulnerabilities were identified in the OIDC Discovery client:

1. **Blind Server-Side Request Forgery (SSRF) via Cross-Host Redirects**:
   Fulcio uses an HTTP client to fetch OIDC discovery metadata (`/.well-known/openid-configuration`). Prior to this fix, if a configured issuer returned an HTTP redirect to a different host, the client followed it by default. This allowe…

---

## 20. 🟡 High Severity — CefSharp.Common: `FolderSchemeHandlerFactory` path boundary check can expose files outside the configured root folder

**CVE:** `CVE-2026-48796` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-85jm-cwp2-mvpv>

> ### Summary

`FolderSchemeHandlerFactory` was intended to restrict served files to a configured `rootFolder`, but its path validation used a raw string prefix check. A request could escape to a sibling directory whose full path starts with the root folder path, allowing files outside the configured root to be served.

### Details

In affected versions, `FolderSchemeHandlerFactory` canonicalized `r…

---

## 21. 🟡 High Severity — @adonisjs/bodyparser has an incomplete fix for CVE-2026-25754

**CVE:** `CVE-2026-48795` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-qcm7-3vpr-hj5h>

> ### Summary

The fix for [GHSA-f5x2-vj4h-vg4c](https://github.com/adonisjs/core/security/advisories/GHSA-f5x2-vj4h-vg4c) / CVE-2026-25754 introduced in commit [`40e1c71`](https://github.com/adonisjs/bodyparser/commit/40e1c71f958cffb74f6b91bed6630dca979062ed) is incomplete and can be bypassed through nested prototype pollution payloads.

The original patch replaced the internal `FormFields` storage…

---

## 22. 🟡 High Severity — Probo has an open redirect bypass via path normalization

**CVE:** `CVE-2026-49820` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-x7qq-m748-8p2c>

> ### Impact
Probo&#x27;s `saferedirect` package validates redirect URLs used across authentication flows (OIDC, SAML, session transfer, OAuth connectors, and trust-center magic links). The validator only inspected the second character of relative paths, so a URL like `/../\evil.com` passed validation because the second character is `.`. Go&#x27;s `http.Redirect` normalizes this path to `/\evil.com`…

---

## 23. 🟡 High Severity — Fission builder pods auto-mount the fission-builder ServiceAccount token in the user-supplied builder container

**CVE:** `CVE-2026-50565` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-8wcj-mfrc-jx5q>

> ### Summary

Fission builder pods were created with `ServiceAccountName: fission-builder` and no `AutomountServiceAccountToken: false`, so the kubelet auto-mounted the service-account token into every container in the pod — including the
user-supplied builder image.

### Details

The user controls the builder container image, command, and podspec through `Environment.spec.builder.image` / `.contai…

---

## 24. 🟡 High Severity — Fission Environment CRD podspec passthrough enables hostPID/hostNetwork/privileged pods, node escape

**CVE:** `CVE-2026-50564` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-gx55-f84r-v3r7>

> ### Summary

Fission&#x27;s `Environment` CRD exposes `spec.runtime.podSpec` and `spec.builder.podSpec`, which are merged into the Kubernetes pod specs for runtime and builder pods. The merge logic propagated `hostNetwork`, `hostPID`, `hostIPC`, container
 `privileged`, and `serviceAccountName` from the user-supplied podspec with no filtering, and `Environment.Validate` performed no security-relev…

---

## 25. 🟡 High Severity — Fission Container Executor Function PodSpec Injection Leading to Node Escape

**CVE:** `CVE-2026-50563` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-v455-mv2v-5g92>

> ### Summary

Fission&#x27;s Container Executor path lets a tenant supply `Function.spec.podspec` directly; the executor merges it into the executor-built podspec and creates a Deployment whose pods run the user&#x27;s container image.

### Details

Two flaws compounded:

1. `pkg/apis/core/v1/validation.go::FunctionSpec.Validate` only checked that `spec.PodSpec != nil` when `executorType: container…

---

## 26. 🟡 High Severity — Fission Environment CRD PodSpec Injection Leading to Node Escape and Cluster Takeover

**CVE:** `CVE-2026-50545` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-wmgg-3p4h-48x7>

> ### Summary

A stronger framing of the same root cause as GHSA-gx55-f84r-v3r7: the `Environment.spec.runtime.podSpec` / `spec.builder.podSpec` passthrough lacked validation, and `MergePodSpec` propagated dangerous fields into the generated pods.

### Details

Three independent flaws compounded:

1. **Validate gap.** `pkg/apis/core/v1/validation.go::Environment.Validate` checked only container nami…

---

## 27. 🟡 High Severity — Fission: Cross-namespace Environment reference via unvalidated EnvironmentRef in Function admission webhook

**CVE:** `CVE-2026-49824` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-cvw6-gfvv-953q>

> ### Summary

The Fission Function admission webhook (`pkg/webhook/function.go`) validated that `spec.secrets[].namespace` and `spec.configmaps[].namespace` equalled the function&#x27;s own namespace but performed no equivalent check on
`spec.environment.namespace`.

### Details

An attacker with permission to create Functions in their own namespace could set `spec.environment.namespace` to any oth…

---

## 28. 🟡 High Severity — Fission: Cross-namespace Package read via unvalidated PackageRef in Function admission webhook

**CVE:** `CVE-2026-49823` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-3r8v-2xmj-5c39>

> ### Summary

A Fission Function spec carries three reference types — Secret, ConfigMap, and Package. The first two were namespace-validated by the admission webhook; `PackageRef.Namespace` was not.

### Details

A tenant with `functions.fission.io/create` in their own namespace could set `spec.package.packageref.namespace` to any other namespace. When the function is invoked, the fetcher sidecar r…

---

## 29. 🟡 High Severity — Fission: Cross-namespace event leakage via KubernetesWatchTrigger allows persistent tenant surveillance

**CVE:** `CVE-2026-49822` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-gc3j-79f2-7vvw>

> ### Summary

A low-privilege developer who could create a `KubernetesWatchTrigger` (KWT) in their own namespace was able to establish a persistent surveillance channel over any other namespace.

### Details

Two independent flaws compounded:

1. `pkg/kubewatcher/kubewatcher.go::createKubernetesWatch` used `w.Spec.Namespace` (user-controlled) directly as the Watch target without checking it against…

---

## 30. 🟡 High Severity — Fission: Cross-namespace Environment reference in Package allows build-time command execution and SA token exfiltration

**CVE:** `CVE-2026-49821` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-vjhc-cf4p-72q4>

> ### Summary

Fission&#x27;s `buildermgr` controller processed `Package` CRDs without verifying that `Package.spec.environment.namespace` matched `Package.metadata.namespace`.

### Details

An attacker with `packages.fission.io/create` in their own namespace could set `spec.environment.namespace` to any other tenant&#x27;s namespace. The controller then used its high-privilege service account to fe…

---

## 31. 🟡 High Severity — RabbitMQ has predictable credential obfuscation seed value used in Shovel and Federation plugins

**CVE:** `CVE-2022-31008` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-v9gv-xp36-jgj8>

> ### Impact

Shovel and Federation plugins perform URI obfuscation in their worker (link) state. The encryption key used to encrypt
the URI was seeded with a predictable secret.

This means that in case of certain exceptions related to Shovel and Federation plugins,
reasonably easily deobfuscatable data could appear in the node log.

Patched versions correctly use a cluster-wide secret for that pur…

---

## 32. 🟡 High Severity — Microsoft.OpenAPI: Circular schema references may terminate OpenAPI parsing

**CVE:** `CVE-2026-49451` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-v5pm-xwqc-g5wc>

> ### Impact

A small OpenAPI document containing a circular schema reference can cause process termination through stack overflow in Microsoft.OpenApi. The issue affects OpenAPI document parsing through public OpenAPI.NET reader APIs and has been confirmed across both JSON and YAML reader paths.

## Affected versions

- `&gt;= 2.0.0-preview11, &lt;= 2.7.4`
- `&gt;= 3.0.0, &lt;= 3.5.3`

### Patches
…

---

## 33. 🟡 High Severity — Langflow RCE Exploited to Deploy Monero Miner on Exposed AI App Endpoints

**CVE:** `CVE-2026-33017` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://thehackernews.com/2026/06/langflow-rce-exploited-to-deploy-monero.html>

> Threat actors are continuing to exploit a critical Langflow vulnerability as part of fresh attacks designed to deliver a Monero cryptocurrency miner.

The activity has been found to weaponize CVE-2026-33017 (CVSS score: 9.3), an unauthenticated remote code execution (RCE) vulnerability in Langflow, indicating threat actors are scanning and targeting exposed artificial intelligence (AI)

---

## 34. 🟡 High Severity — Attackers Exploit SimpleHelp CVE-2026-48558 to Deploy TaskWeaver and Djinn Stealer

**CVE:** `CVE-2026-48558` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://thehackernews.com/2026/06/attackers-exploit-simplehelp-cve-2026.html>

> An unknown threat actor has been observed exploiting a recently disclosed maximum-severity security flaw in SimpleHelp to deliver two previously unreported malware families, TaskWeaver and Djinn Stealer.

The intrusion involves the exploitation of CVE-2026-48558 (CVSS score: 10.0), a critical authentication bypass vulnerability impacting the OpenID Connect (OIDC) flow that an unauthenticated

---

## 35. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
