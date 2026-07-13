# Zero Day Pulse

> **Generated:** 2026-07-13 08:46 UTC &nbsp;|&nbsp; **Total:** 13 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is an unauthenticated path traversal vulnerability (CWE-22) in the SimpleHelp web/HTTP server components. Crafted HTTP requests containing directory-traversal sequences (e.g., '..%2F' or '../') allow remote attackers to read arbitrary files from the host running the SimpleHelp server, bypassing authentication. Files retrievable include serverconfig.xml, which contains hashed admin passwords and secrets such as LDAP credentials, OIDC tokens, and TOTP seeds. Researchers at Horizon3.ai demonstrated chaining CVE-2024-57727 with CVE-2024-57726 (privilege escalation via admin API) and CVE-2024-57728 (zip-slip arbitrary file write) to achieve unauthenticated remote code execution, which ransomware operators have weaponized against MSPs and downstream customers.
- **Affected Products:** SimpleHelp Remote Support / RMM software, versions 5.5.7 and earlier (fixed in 5.5.8, 5.5.9, and 5.5.10)
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true. Public proof-of-concept at https://github.com/imjdl/CVE-2024-57727 and Nuclei template at https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2024/CVE-2024-57727.yaml
- **Patch Available:** true. Vendor patches released in SimpleHelp versions 5.5.8, 5.5.9, and 5.5.10 (January 8–13, 2025). Advisory: https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know ; KB: https://guides.simple-help.com/kb---security-vulnerabilities-01-2025
- **Active Exploitation:** true. CISA added CVE-2024-57727 to the Known Exploited Vulnerabilities (KEV) catalog on 2025-02-13 (due date 2025-03-06). CISA Advisory AA25-163A (published 2025-06-12) documents ransomware actors exploiting the vulnerability in SimpleHelp RMM since January 2025 to compromise a utility billing software provider and its downstream customers, including double-extortion ransomware attacks. Halcyon and Sophos publicly attributed the in-the-wild attacks to the DragonForce ransomware group.
- **Threat Actors:** DragonForce (ransomware group). CISA AA25-163A attributes in-the-wild exploitation to ransomware actors since January 2025; Halcyon, Sophos, Picus Security, and Ampcus Cyber publicly identified DragonForce specifically targeting MSP environments. Medusa ransomware operators have also been reported exploiting chained SimpleHelp vulnerabilities.
- **Mitigation:** 1) Immediately upgrade SimpleHelp to version 5.5.8 or later (5.5.10/5.5.15 strongly recommended); the vendor patch fully addresses CVE-2024-57727. 2) If upgrading is not immediately possible, isolate the SimpleHelp server from the public internet or stop the SimpleHelp server process, and block inbound traffic to SimpleHelp ports at the network perimeter. 3) Audit for indicators of compromise: three-letter alphabetic executables (e.g., aaa.exe, bbb.exe) created after January 2025 in user-writable paths; review serverconfig.xml access logs; check %APPDATA%\JWrapper-Remote Access, /opt/JWrapper-Remote Access, and /Library/Application Support/JWrapper-Remote Access for unauthorized RAS deployments. 4) Rotate all admin/technician credentials and any secrets (LDAP, OIDC, TOTP seeds) stored in serverconfig.xml. 5) Apply least-privilege principles to RMM servers; segment RMM infrastructure from production networks; enforce MFA on technician accounts. 6) If encryption/compromise is confirmed, disconnect affected hosts, wipe and reinstall from clean media, and restore only from verified offline backups. 7) Software vendors and MSSPs should notify downstream customers of any exposure since January 2025.
- **Vendor Advisory:** https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — iCagenda and Balbooa Forms Joomla Flaws Reportedly Exploited as Zero-Days

**CVE:** `CVE-2026-48939` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-13
**Reference:** <https://thehackernews.com/2026/07/icagenda-and-balbooa-forms-joomla-flaws.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has added two maximum-severity security flaws impacting iCagenda and Balbooa extensions for Joomla to its Known Exploited Vulnerabilities (KEV) catalog, following reports of zero-day exploitation in the wild.

The vulnerabilities, both rated 10.0 on the CVSS scoring system, are below -


  CVE-2026-48939 - A vulnerability in the

**Parallel AI Enrichment:**

- **Technical Details:** An unrestricted file upload vulnerability (CWE-434) exists in the iCagenda Joomla extension's event submission feature. The processing controller fails to enforce authorization checks, permitting any unauthenticated visitor to submit files via the 'Submit an Event' form. On Joomla 6 sites, the component does not validate file extensions or MIME types, enabling upload of arbitrary files—including PHP web shells—to the images/icagenda/frontend/attachments/ directory. The uploaded PHP executes under the web-server user context, yielding unauthenticated remote code execution (RCE) on the Joomla host.
- **Affected Products:** iCagenda Joomla extension versions 3.2.1 through 3.9.14 (Joomla 3 line), and versions 4.0.0 through 4.0.7 (Joomla 4/5/6 lines)
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H/E:A/AU:Y/U:Red (CVSS v3.x vector has not been publicly published)
- **Exploit Available:** true (https://github.com/Polosss/By-Poloss..-..CVE-2026-48939)
- **Patch Available:** true (https://www.joomlic.com/news/icagenda-security-update — iCagenda 4.0.8 released 15 June 2026; legacy Joomla 3 fix 3.9.15 released 16 June 2026)
- **Active Exploitation:** true — CISA added CVE-2026-48939 to the Known Exploited Vulnerabilities (KEV) Catalog on July 10, 2026, citing evidence of active exploitation in the wild. CISA Binding Operational Directive 26-04 gives Federal Civilian Executive Branch agencies a remediation deadline of July 31, 2026.
- **Threat Actors:** None known (automated scanner identifying as 'icagenda-batch/1.0' observed conducting mass exploitation; no specific APT, ransomware operator, or named threat actor publicly attributed)
- **Mitigation:** Update iCagenda immediately to 4.0.8 (current Joomla 4/5/6 line) or 3.9.15 (Joomla 3 line). If patching cannot be performed right away, temporarily disable the 'Submit an Event' / file-attachment feature, or rename the com_icagenda component folders to block access. Inspect images/icagenda/frontend/attachments/ on every affected host for unauthorized .php (or other executable) files and remove them. Review web-server access logs for suspicious multipart POST uploads since approximately mid-June 2026, audit Joomla user accounts for unknown administrators, and rotate any credentials or API keys stored on the affected server.
- **Vendor Advisory:** https://www.joomlic.com/news/icagenda-security-update

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is a class of attack in which adversary-controlled content placed on the public web (e.g., hidden text, HTML comments, white-on-white text, metadata, or images processed by vision-capable models) embeds instructions that an AI agent or LLM-powered system ingests when it browses, summarises, indexes, or otherwise processes that content. The model treats the injected instructions as legitimate directives and executes them in preference to (or alongside) the user's original intent. Documented abuse categories include: (1) SEO/answer-engine manipulation causing assistants to recommend attacker-favoured businesses; (2) agent-disruption DoS by streaming infinite text to force timeouts; (3) data exfiltration attempts that coax agents with access to API keys, tokens, or session secrets into leaking them; (4) destructive commands such as 'delete all files on the user's machine'; (5) tone/behavior hijacking; and (6) financial fraud and unauthorised transactions. Unlike direct prompt injection, the victim user never types the malicious instruction - the LLM is poisoned via a third-party data source it consumes.
- **Affected Products:** AI-powered browsers and agentic AI systems that consume untrusted web content (including GitHub Copilot, Cursor, Claude Code); LLM-integrated web search, summarisation, and content-processing pipelines; AI-based product advertisement review systems; versions not publicly specified (class-level vulnerability)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true - https://github.com/brennanbrown/atlas-prompt-injection-poc (public PoC for AI browsers); Forcepoint X-Labs additionally documented 10 live IPI payloads found on production websites targeting GitHub Copilot, Cursor, and Claude Code (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads)
- **Patch Available:** false - No single vendor patch exists for Indirect Prompt Injection; this is a class-level vulnerability inherent to LLMs that consume untrusted external content. Google states it is 'hardening our AI models and products' on an ongoing basis, and Forcepoint/Palo Alto Networks offer commercial filtering layers, but no CVE-issued comprehensive fix is available. Vendors of affected agentic products (GitHub Copilot, Cursor, Claude Code) have shipped incremental mitigations rather than a comprehensive patch.
- **Active Exploitation:** true - Google Threat Intelligence Group confirmed active in-the-wild abuse, reporting a 32% relative increase in the malicious indirect prompt injection category between November 2025 and February 2026, with observed payloads spanning pranks, SEO manipulation, agent-disruption DoS, data exfiltration, and destructive commands. Independently, Forcepoint X-Labs documented 10 verified IPI payloads observed live on production websites targeting AI agents including GitHub Copilot, Cursor, and Claude Code.
- **Threat Actors:** None known
- **Mitigation:** Google's recommended hardening for organisations deploying agentic AI: (1) enforce a strict data/instruction boundary so untrusted web content cannot be treated as system-level commands; (2) apply a layered defence across model training, system prompts, input filtering, output filtering, and human-in-the-loop confirmation for high-impact actions; (3) pressure-test systems via red-teaming and bug bounty - Google runs an AI Vulnerability Reward Program; (4) constrain agent privileges (filesystem, email, payments) and require explicit user confirmation before destructive or exfiltrating actions; (5) use URL/content filtering products (e.g., Forcepoint Real-Time Analytics, Palo Alto Networks Advanced URL Filtering / Prisma AIRS) to block or flag known poisoned pages; (6) sandbox LLM tool-use and tool-output handling; (7) deploy retrieval pipelines that strip or sandbox instructions found in indexed content. Because IPI is inherent to mixing trusted instructions with untrusted data, mitigation is architectural - no single patch exists.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack class against LLM-based applications such as Workspace with Gemini. An attacker plants hostile natural-language instructions inside data the model ingests — emails, documents, web pages, calendar entries, shared files. When the user asks Gemini to summarize or act on that content, the hidden instructions are processed as if they were part of the prompt and can steer the model to exfiltrate data, follow attacker URLs, suppress warnings, or take other unauthorized actions, sometimes without any user-authored prompt at all. Demonstrated vectors against Gemini include: hidden HTML/CSS (e.g., font-size:0, white text, off-screen positioning) in emails that cause summaries to include attacker-supplied phishing text; calendar-event payloads that trick Gemini into leaking private events; and web pages that, when fetched by an agentic browser sub-agent, induce credential theft and exfiltration via webhook URLs allowed by default browser policy.
- **Affected Products:** Google Workspace with Gemini (Gmail, Google Docs editors, Google Drive, Google Chat), and the consumer Gemini app
- **CVSS Score:** CVSS score unavailable. No CVE has been assigned for indirect prompt injection as an attack class against Workspace with Gemini.
- **CVSS Vector:** CVSS vector unavailable. No CVE has been assigned. Indirect prompt injection is tracked as an attack class by OWASP (LLM01:2025 Prompt Injection) rather than as a single CVE-scored vulnerability.
- **Exploit Available:** true - Multiple public PoCs exist: (1) 0Din/Mozilla 'Phishing for Gemini' (Jul 10, 2025) - hidden white-text prompt injection in email bodies that causes Gemini to append a fabricated security alert to email summaries (https://0din.ai/blog/phishing-for-gemini); (2) Miggo 'Weaponizing Calendar Invites' (Jan 19, 2026) - semantic indirect prompt injection in Google Calendar invites bypassing Gemini's privacy controls (https://www.miggo.io/post/weaponizing-calendar-invites-a-semantic-attack-on-google-gemini); (3) PromptArmor report on Google Antigravity agent data exfiltration via indirect prompt injection in web content (https://promptarmor.com/resources/google-antigravity-exfiltrates-data).
- **Patch Available:** false - No vendor patch in the traditional sense. Google mitigates indirect prompt injection through continuous, layered model- and product-side defenses (content classifiers, thought reinforcement, markdown sanitization, URL redaction via Safe Browsing, user confirmation prompts, and end-user notifications) rolled out as iterative updates to the Gemini app and Gemini-in-Workspace rather than as a discrete security patch tied to a CVE.
- **Active Exploitation:** true - Google and independent researchers confirm active exploitation in the wild. Google's Apr 2, 2026 blog post characterizes IPI as an 'evolving threat vector'; a parallel Apr 23, 2026 Google security blog post states threat actors 'seed prompt injections on websites hoping to corrupt AI systems that browse them.' Palo Alto Unit 42 documented web-based IPI observed in the wild in March 2026 (including an AI ad-review bypass on reviewerpress[.]com), and Help Net Security reported on Apr 24, 2026 that 'indirect prompt injection is taking hold in the wild.' Concrete public exploitation chains against Gemini have been published by 0Din/Mozilla (Phishing for Gemini, Jul 2025), Miggo (calendar semantic attack, Jan 2026), and PromptArmor (Google Antigravity data exfiltration).
- **Threat Actors:** None known. No specific APT groups, ransomware operators, or named campaigns have been publicly identified as exploiting indirect prompt injection against Workspace with Gemini. Google's GTIG reporting on adversarial misuse of Gemini (including by North Korea-linked actors) covers adversaries using Gemini as a productivity aid, not exploitation of IPI in Gemini itself.
- **Mitigation:** No single patch is available because IPI is an evolving attack class. Google's recommended layered defenses for Workspace admins include: (1) content classifiers that detect malicious prompt content before it reaches the model; (2) security thought reinforcement — system instructions that remind Gemini to ignore injected directives; (3) markdown sanitization and redaction of suspicious URLs via Google Safe Browsing; (4) a user confirmation framework requiring explicit human approval before sensitive actions or external communications; (5) end-user security-mitigation notifications when a suspected injection has been blocked; and (6) ongoing model resilience training against adversarial prompts. Admins should keep Workspace with Gemini updated, restrict Gemini to trusted data sources where possible, monitor Google's Workspace release notes for new IPI mitigations, and train end users to treat Gemini summaries as untrusted output rather than authoritative content.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is the primary attack vector against agentic browsers. An attacker embeds adversarial instructions inside content the agent will read—malicious sites, third-party content in cross-origin iframes, or user-generated content such as reviews. Because Gemini in Chrome must consume that untrusted web content to act on the user's behalf, embedded instructions can hijack the agent's planning step and cause unintended actions (financial transactions, data exfiltration, navigation to sensitive sites, credential disclosure). The Gemini model is treated as inherently vulnerable because it must read attacker-controlled text, so Chrome layers additional components in front of every actuation: an isolated User Alignment Critic reviewer model, an Origin-Set gating function, a page-level prompt-injection classifier, mandatory user confirmations, and red-team-driven hardening.
- **Affected Products:** Google Chrome with Gemini in Chrome (GA in September 2025) and the agentic capabilities preview. No specific version range provided because agentic capabilities are still in preview and defenses are being rolled out via Chrome auto-update.
- **CVSS Score:** CVSS score unavailable. No CVSS base score has been assigned because the blog post does not identify a single discrete CVE; it describes a defensive architecture against a threat class.
- **CVSS Vector:** CVSS vector unavailable. This is not a CVE-specific vulnerability advisory; no CVSS vector string is published.
- **Exploit Available:** false. The blog post does not disclose or reference any public PoC or weaponized exploit for the specific layered protections it describes. Google opened a bug bounty offering up to $20,000 for researchers who can break the new defenses, indicating Google is soliciting but has not published exploits for these specific protections.
- **Patch Available:** true. The defenses are delivered through Google Chrome's standard auto-update mechanism; no separate manual patch is required. https://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** false. The blog post does not report any confirmed in-the-wild exploitation of Chrome's agentic features. It frames indirect prompt injection as the primary emerging threat class and announces defenses plus a $20,000 bug bounty, but does not cite active exploitation.
- **Threat Actors:** None known. The blog post does not attribute the indirect prompt injection threat to any specific named threat actor group, APT campaign, or ransomware operator. It describes a general adversarial class using malicious sites, third-party iframes, and user-generated content to deliver indirect prompts.
- **Mitigation:** Google is shipping a layered defense: (1) User Alignment Critic—a separate Gemini-based reviewer model isolated from untrusted content; (2) Agent Origin Sets constraining read vs. read-write origins; (3) mandatory user confirmations before sensitive actions (banking, purchases, messaging, sign-in); (4) real-time prompt-injection classifier alongside Safe Browsing and on-device scam detection; (5) automated red-teaming. User hardening: keep Chrome updated (auto-update), avoid granting agent permissions to sensitive sites unless prompted, treat unsolicited action prompts requiring sign-in/payment/data sharing as potential injection attempts requiring manual verification.
- **Vendor Advisory:** https://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** The blog post 'Rust in Android: move fast and fix things' (published 2025-11-13 by Jeff Vander Stoep) is a strategy and metrics update about Android's adoption of Rust for memory safety. It is NOT a vulnerability advisory. The post reports that memory-safety vulnerabilities fell to under 20% of Android's total vulnerabilities in 2025 for the first time, validating the shift toward Rust. It cites Rust's memory-safety vulnerability density at ~0.2 per million lines of code versus ~1,000/MLOC for C/C++ (~1000x reduction). The post illustrates the approach with one concrete example: CVE-2025-48530, a linear buffer overflow (out-of-bounds accesses) in unsafe Rust code within CrabbyAVIF (Android's AVIF parser/decoder), caused by incorrect bounds checks affecting NV12 YUV planes (Y plane, UV planes, alpha plane, chroma width calculation). The Scudo hardened allocator's guard pages converted the would-be silent memory corruption into an immediate crash, preventing exploitation. Attack vector would be remote via a crafted AVIF input.
- **Affected Products:** Android platform (general strategy update). For CVE-2025-48530 (illustrative example): Android 16.
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true — https://source.android.com/docs/security/bulletin/2025-08-01
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the Android Security Bulletin—August 2025 patch level (2025-08-05 or later) to remediate CVE-2025-48530. Broader hardening guidance from the post: (1) continue migrating C/C++ Android components to memory-safe languages (primarily Rust); (2) rely on the Scudo hardened allocator (with guard pages) to convert silent memory corruption into detectable crashes; (3) invest in developer training via the 'Comprehensive Rust' course plus a new deep-dive on writing and reviewing unsafe code; (4) prioritize memory-safety in new code over legacy C/C++. No CVE-specific workaround is needed since a patch is available.
- **Vendor Advisory:** https://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html — Google Security Blog post by Jeff Vander Stoep (2025-11-13). The single CVE cited as an illustrative example (CVE-2025-48530) was patched in the Android Security Bulletin—August 2025: https://source.android.com/docs/security/bulletin/2025-08-01

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is a class of attacks where adversaries embed hidden malicious instructions inside external content (emails, documents, calendar invites, web pages) that is subsequently retrieved and processed by an LLM-powered AI assistant or agent. Unlike direct prompt injection, the user never types the malicious prompt — it is ingested as part of contextual data. When the model processes the poisoned content, the embedded instructions can cause the AI to exfiltrate user data (e.g., via rendered images, markdown links, or outbound tool calls), execute unauthorized actions, or override system policies. The blog cites the EchoLeak attack against Microsoft 365 Copilot (CVE-2025-32711) as a concrete example: a zero-click attack where crafted content in a shared document caused Copilot to render an image whose URL exfiltrated sensitive conversation data to an attacker-controlled server. The underlying weakness is that LLMs cannot reliably distinguish trusted system/user instructions from untrusted data and lack native enforcement of content provenance or origin.
- **Affected Products:** Google Gemini (Gemini app, Gemini in Google Workspace/Gmail/Docs/Calendar), Google Gemini 2.5 family of models. The blog also references CVE-2025-32711 (EchoLeak) in Microsoft 365 Copilot as a real-world example of indirect prompt injection exploitation.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true. Public PoC exploits exist for indirect prompt injection techniques, including the EchoLeak (CVE-2025-32711) PoC published by AIM Security Labs (https://www.aim.security/lp/aim-labs-echoleak-m365) and various open-source repositories demonstrating indirect prompt injection against LLM/agent systems.
- **Patch Available:** true. Google has deployed hardening mitigations for Gemini 2.5 models and integrated the layered defense strategy. Microsoft patched CVE-2025-32711 (EchoLeak) server-side in May 2025 prior to public disclosure. Advisory URLs: http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html and https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32711
- **Active Exploitation:** true. Indirect prompt injection attacks have been observed in the wild targeting AI agents and assistants. Palo Alto Unit 42 documented web-based indirect prompt injection campaigns, and Zscaler/SecurityWeek reported cases where indirect prompt injections tricked AI agents into making unauthorized cryptocurrency payments. The EchoLeak vulnerability (CVE-2025-32711) against Microsoft 365 Copilot was demonstrated as a zero-click attack. Sources: https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/ and https://www.securityweek.com/prompt-injection-attacks-trick-ai-agents-into-making-crypto-payments/
- **Threat Actors:** None known. The Google Security Blog post references the threat generically as 'adversaries' without attributing exploitation to any specific named APT group, ransomware operator, or cybercrime campaign.
- **Mitigation:** Google recommends a five-layer defense strategy: (1) Adversarial training and model hardening integrated into Gemini 2.5; (2) ML-based prompt-injection content classifiers to screen inputs for malicious patterns; (3) 'Security thought reinforcement' — system instructions reminding the model to ignore lower-priority instructions embedded in retrieved content; (4) Output sanitization including markdown sanitization and suspicious-URL redaction backed by Google Safe Browsing to prevent data exfiltration via rendered links or images; (5) A user-confirmation (human-in-the-loop) framework requiring explicit approval before the AI performs sensitive actions (e.g., sending mail, modifying shared resources). Additional hardening: enforce content provenance/authorship signals, restrict agent tool-use scopes, log and audit AI-initiated actions, and segment agent permissions.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors conduct a long-term espionage campaign targeting global networks, focusing on large backbone routers of major telecommunications providers and provider-edge (PE) and customer-edge (CE) routers in telecommunications, government, transportation, lodging, and military sectors. Initial access is gained by exploiting known/n-day vulnerabilities in internet-exposed edge devices, including Ivanti Connect Secure/Policy Secure (CVE-2023-46805 and CVE-2024-21887), Palo Alto Networks PAN-OS/GlobalProtect (CVE-2024-3400), Cisco IOS XE Web UI (CVE-2023-20198 followed by CVE-2023-20273), and Cisco IOS/IOS XE Smart Install (CVE-2018-0171). Once inside, the actors leverage compromised devices and trusted connections (GRE/IPsec tunnels, vendor management channels, lateral trust relationships) to pivot into provider networks. They modify router configurations to maintain persistent long-term access, including: changing local account credentials; creating ACLs frequently named 'access-list 20' to permit attacker command-and-control traffic; disabling or tampering with logging, TACACS+/RADIUS, AAA, SNMP, and NTP; and configuring GRE or IPsec tunnels to attacker-controlled infrastructure. They harvest credentials and configuration files, perform lateral movement, and position themselves for follow-on collection. CISA explicitly notes that zero-day exploitation has NOT been observed - every observed compromise relied on previously disclosed vulnerabilities on unpatched devices.
- **Affected Products:** Ivanti Connect Secure and Ivanti Policy Secure (versions 9.x and 22.x); Palo Alto Networks PAN-OS with GlobalProtect enabled (10.2 < 10.2.9-h1, 11.0 < 11.0.4-h1, 11.1 < 11.1.2-h3); Cisco IOS XE Web UI (any build exposing the Web UI feature); Cisco IOS and IOS XE Smart Install (any device with Smart Install client enabled); advisory also notes potential exposure of Fortinet firewalls, Juniper firewalls, Microsoft Exchange, Nokia routers/switches, Sierra Wireless devices, and SonicWall firewalls
- **CVSS Score:** CVSS score unavailable - aggregate score not applicable to a multi-CVE advisory. Individual CVE base scores range from 7.2 (CVE-2023-20273) to 10.0 (CVE-2024-3400, CVE-2023-20198).
- **CVSS Vector:** CVSS vector unavailable - AA25-239A is a multi-CVE advisory without a single CVSS vector. Individual CVE vectors include: CVE-2024-21887 (CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H, base 9.1), CVE-2024-3400 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H, base 10.0), CVE-2023-20198 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H, base 10.0), CVE-2023-20273 (CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H, base 7.2), CVE-2018-0171 (CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, base 9.8), CVE-2023-46805 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, base 8.2)
- **Exploit Available:** true - Public PoCs and weaponized exploits are available for multiple CVEs referenced in the advisory, including CVE-2024-21887 (Ivanti), CVE-2024-3400 (Palo Alto GlobalProtect), CVE-2023-20198 (Cisco IOS XE Web UI), CVE-2023-20273 (Cisco IOS XE Web UI privilege escalation), CVE-2023-46805 (Ivanti authentication bypass), and CVE-2018-0171 (Cisco Smart Install)
- **Patch Available:** true - Patches are available from all primary vendors: Ivanti (CVE-2023-46805, CVE-2024-21887), Palo Alto Networks (CVE-2024-3400), and Cisco (CVE-2023-20198, CVE-2023-20273, CVE-2018-0171)
- **Active Exploitation:** true - CISA explicitly confirms active exploitation in the wild. The campaign has been attributed by CISA, NSA, FBI, and partner agencies to PRC state-sponsored threat actors actively targeting telecommunications, government, transportation, lodging, and military infrastructure networks worldwide.
- **Threat Actors:** Salt Typhoon (also tracked as OPERATOR PANDA, RedMike, UNC5807, GhostEmperor) - collectively attributed by CISA, NSA, FBI, and partner agencies to People's Republic of China (PRC) state-sponsored threat actors
- **Mitigation:** 1) Immediately patch all internet-exposed edge devices against the CVEs listed in AA25-239A (Ivanti Connect Secure/Policy Secure, Palo Alto PAN-OS/GlobalProtect, Cisco IOS XE and IOS/IOS XE Smart Install), prioritizing assets under active exploitation. 2) Replace end-of-support/unmaintained devices - CISA explicitly directs organizations to upgrade unsupported network equipment. 3) Disable Cisco Smart Install (SMI) where not required ('no vstack' in config). 4) Disable the HTTP/HTTPS server feature on Cisco IOS XE devices where not required. 5) Hunt for and remove unauthorized configuration changes, especially: ACL entries named 'access-list 20' (or other unexpected ACLs), unauthorized GRE or IPsec tunnels pointing to unknown endpoints, modified local user accounts, disabled logging/TACACS+/RADIUS/AAA/SNMPv3/NTP, and altered SNMP community strings or NTP servers. 6) Enforce unique, strong local-account credentials and rotate them; verify integrity of TACACS+/RADIUS and SNMPv3 configurations. 7) Segment management networks; restrict outbound connectivity from edge devices to known infrastructure only; block unauthorized GRE tunnels at the perimeter. 8) Centralize and retain netflow, syslog, TACACS+, and configuration archives off-device for forensic review. 9) Apply vendor hardening guidance (Cisco IOS Hardening Guide, Cisco IOS XE Hardening Guide, Cisco Software Checker). 10) Report suspected PRC-linked intrusions to CISA (cisa.gov/report) or the FBI.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2023-23397 is a Microsoft Outlook elevation-of-privilege vulnerability (CWE-20: Improper Input Validation) that leaks a user's Net-NTLMv2 hash without any user interaction. The attacker crafts a specially formatted Outlook calendar or email message containing a PidLidReminderFileParameter MAPI property set to a UNC path pointing to an attacker-controlled SMB server (e.g., \\attacker.com\share\file.wav). When Outlook processes the reminder, the client authenticates to the remote SMB server and transmits the user's NTLMv2 credentials in the authentication handshake. No preview pane or click is required — merely receiving the message in Outlook is sufficient. The captured hash can be relayed (NTLM relay) or cracked offline to obtain the victim's credentials, enabling follow-on lateral movement, mailbox access, and data exfiltration. As documented in CISA AA25-141A, GRU Unit 26165 weaponized CVE-2023-23397 against Western logistics entities and technology companies supporting foreign assistance to Ukraine, then leveraged the harvested credentials and modified Microsoft Exchange mailbox permissions for persistent access and intelligence collection.
- **Affected Products:** Microsoft Outlook for Microsoft 365 Apps, Microsoft Outlook 2019, Microsoft Outlook 2016, Microsoft Outlook 2013 (Office LTSC); Microsoft 365 Apps for Enterprise (32/64-bit); Office LTSC for Microsoft 2021
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:F/RL:O/RC:C
- **Exploit Available:** true — multiple public PoCs available, including https://github.com/Trackflaw/CVE-2023-23397 and https://github.com/api0cradle/CVE-2023-23397-POC-Powershell
- **Patch Available:** true — Microsoft released fixes on March 14, 2023: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23397 (also referenced in CISA AA25-141A)
- **Active Exploitation:** true — GRU Unit 26165 (APT28/Fancy Bear/Forest Blizzard) actively weaponized CVE-2023-23397 against Western logistics entities and technology companies supporting foreign assistance to Ukraine, as documented in CISA Joint Cybersecurity Advisory AA25-141A (May 12, 2025). Microsoft also confirmed in-the-wild exploitation by Forest Blizzard (STRONTIUM) targeting Exchange servers via this vulnerability.
- **Threat Actors:** Russian GRU 85th Main Special Service Center (85th GTsSS), military unit 26165 — tracked across the industry as APT28, Fancy Bear, Forest Blizzard, BlueDelta, STRONTIUM, Sednit, Sofacy, IRON TWILIGHT, Pawn Storm, GruesomeLar, and TAG-0700
- **Mitigation:** 1) Apply the March 14, 2023 Microsoft security updates for CVE-2023-23397 and keep Outlook current. 2) Block outbound SMB (TCP/445) and WebDAV traffic from client networks to the internet. 3) Disable or restrict NTLM via registry: set RestrictReceivingNTLMTraffic=1 and RestrictSendingNTLMTraffic=1, and enable SMB/LDAP signing plus EPA/SMB channel binding. 4) Audit the registry key HKCU\Software\Microsoft\Office\<version>\Outlook\Settings\Reminders for PidLidReminderFileParameter entries pointing to UNC paths (an IOC of exploitation), and remove any such entries. 5) Disable SMBv1 and enforce application control/Mark-of-the-Web policies. 6) Hunt for, rotate, and revoke any credentials that may have been exposed via NTLM relay or offline cracking. 7) Enable credential protection features such as Credential Guard, LSA Protection (RunAsPPL), and the Protected Users security group for high-value accounts.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

**Parallel AI Enrichment:**

- **Technical Details:** The article is a conceptual/thought-leadership piece, not a technical vulnerability write-up. Its technical content covers: (1) the browser as a high-value attack surface mediating access to identities, SaaS, and enterprise data; (2) the risk multiplier from shared Chromium foundations where one vulnerability can affect multiple browsers; (3) typical browser exploit chains progressing from rendering-logic or JavaScript-engine bugs to sandbox escape and privilege escalation; (4) other web-borne attack techniques including phishing, credential theft, session hijacking, clickjacking, XSS, HTML smuggling, malicious downloads, and adversary-in-the-middle attacks; and (5) the 'patch gap' between vulnerability disclosure and enterprise-wide patch deployment. No specific vulnerability mechanism, root cause, code path, or attack vector for a particular CVE is described.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** false. No patch is referenced because the article does not address a specific, named vulnerability. Browser vendors continue to ship routine Chromium security updates independently.
- **Active Exploitation:** false. The article does not report confirmed in-the-wild exploitation of any specific, named vulnerability. It cites CrowdStrike's 2026 Global Threat Report statistic that 42% of vulnerabilities were exploited before public disclosure (conceptual evidence of adversary activity) and Verizon's 2026 DBIR finding that vulnerability exploitation surpassed stolen credentials as the top breach entry point in 2025, but neither is tied to a specific CVE.
- **Threat Actors:** None known.
- **Mitigation:** The article recommends shifting defensive focus from patch timing alone to in-session runtime browser protection, specifically: (1) CrowdStrike's JavaScript Language Randomization (JSLR) — a moving-target defense that randomizes the JavaScript runtime environment to disrupt zero-day exploit chains; and (2) CrowdStrike Falcon Secure Access, which provides runtime browser security controls that block phishing, prevent session-token theft/MFA bypass, stop adversary-in-the-middle attacks, and prevent data exfiltration directly within the browser session on both managed and unmanaged devices. General hardening advice: treat the browser as a first-class endpoint and recognize that patching alone leaves a window of exposure.
- **Vendor Advisory:** https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/

---

## 11. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 12. 🟠 Zero-Day — CrowdStrike Uncovers New Prompt Injection Techniques

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jul 07, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-uncovers-new-prompt-injection-techniques/>

---

## 13. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
