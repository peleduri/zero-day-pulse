# Zero Day Pulse

> **Generated:** 2026-07-10 09:00 UTC &nbsp;|&nbsp; **Total:** 30 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 16 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** SimpleHelp remote support software versions 5.5.7 and before contain path traversal vulnerabilities in the /toolbox-resource endpoint that allow unauthenticated remote attackers to download arbitrary files from the SimpleHelp host via crafted HTTP requests. Sensitive files exfiltrated include serverconfig.xml, which contains hashed admin passwords and secrets such as LDAP credentials, OIDC client tokens, and TOTP seeds. The vulnerability is chained in attacks with CVE-2024-57726 (auth bypass, CVSS 9.9) and CVE-2024-57728 (admin file upload RCE, CVSS 7.2) to take over SimpleHelp servers, particularly in MSP environments where a single compromise provides access to entire managed-device fleets.
- **Affected Products:** SimpleHelp Remote Support software versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Public proof-of-concept available: https://github.com/imjdl/CVE-2024-57727; a Rapid7 Metasploit auxiliary module (auxiliary/scanner/http/simplehelp_toolbox_path_traversal) is also publicly available, disclosed Feb 25, 2025
- **Patch Available:** Yes. SimpleHelp released patched versions 5.5.8 (Jan 8, 2025), 5.5.9, and 5.5.10 (Jan 13, 2025) addressing CVE-2024-57727 along with CVE-2024-57726 and CVE-2024-57728. Vendor advisory: https://simple-help.com/kb---security-vulnerabilities-01-2025
- **Active Exploitation:** Yes - confirmed active exploitation in the wild. CISA published advisory AA25-163A on June 12, 2025 documenting ransomware actors exploiting unpatched SimpleHelp RMM since January 2025, including a confirmed incident where a utility billing software provider was compromised via SimpleHelp to reach downstream customers in a double-extortion scheme. CISA added CVE-2024-57727 to the Known Exploited Vulnerabilities (KEV) Catalog on February 13, 2025 with a remediation due date of March 6, 2025.
- **Threat Actors:** DragonForce and Medusa ransomware groups (per SimpleHelp vendor advisory); CISA AA25-163A refers generically to 'ransomware actors' leveraging the flaw since January 2025
- **Mitigation:** Patch immediately to SimpleHelp 5.5.8 or later (vendor-issued patches in 5.5.8, 5.5.9, 5.5.10 released Jan 8-13, 2025). For unpatched systems: isolate SimpleHelp servers from direct internet exposure, restrict network access to trusted technician IPs only, monitor for suspicious file-read requests against /toolbox-resource, audit access to serverconfig.xml, force password resets for any credentials stored in the configuration, review audit logs for prior exploitation, and segment the SimpleHelp server from downstream customer/MSP environments.
- **Vendor Advisory:** https://simple-help.com/kb---security-vulnerabilities-01-2025 (also: https://www.simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know)

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an AI agent or LLM-based system ingests untrusted external content (web pages, emails, documents, search results, Common Crawl-indexed content, etc.) that contains adversarial instructions crafted by an attacker. Because the model treats retrieved content as instructions rather than data, it can be coerced into executing the attacker's commands (e.g., data exfiltration, financial fraud, file/system destruction, SEO manipulation, AI-agent deterrence) while ignoring the original user intent. Google's research shows adversaries weaponize publicly indexable web content at scale via search/Crawling pipelines, with observed attack intents including harmless pranks, simple and advanced automated SEO manipulation, infinite-text-stream denial-of-service against AI agents, experimental exfiltration, and attempts to delete files on a user's machine.
- **Affected Products:** AI agents, AI assistants, and LLM-based systems at scale (including Gemini, Workspace with Gemini, Gmail, and Google Docs). Related third-party products: GitHub Copilot, Cursor, Claude Code, AI-powered browsers, AI financial/agentic assistants, Microsoft 365 Copilot (CVE-2025-32711 'EchoLeak'), LangChain GmailToolkit 0.3.51 (CVE-2025-46059), ChatGPT Plugins (CVE-2024-5184), and other agentic tools with access to digital wallets or shell/terminal environments.
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes. Public PoCs and weaponized payloads are widely available: (1) GitHub PoC for IPI in AI browsers - https://github.com/brennanbrown/atlas-prompt-injection-poc ; (2) PayloadsAllTheThings Prompt Injection repository - https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Prompt%20Injection/README.md ; (3) OWASP AI Testing Guide test AITG-APP-01 - https://github.com/OWASP/www-project-ai-testing-guide/blob/main/Document/content/tests/AITG-APP-01_Testing_for_Prompt_Injection.md ; (4) Trail of Bits GitHub Copilot exploit write-up - https://blog.trailofbits.com/2025/08/06/prompt-injection-engineering-for-attackers-exploiting-github-copilot/ ; (5) Forcepoint X-Labs documented 10 live IPI payloads on active sites (thelibrary-welcome[.]uk, kassoon[.]com, luminousmen[.]com, faladobairro[.]com, perceptivepumpkin[.]com, lawsofux[.]com, lcpdfr[.]com, archibase[.]co, reviewerpress[.]com) - https://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads
- **Patch Available:** No vendor patch is associated with this blog post itself — the post is a threat-intelligence overview, not a vulnerability advisory. Google states it is continuously mitigating IPI across Gemini and Workspace with Gemini (Gmail, Docs) through model hardening and policy-engine updates rather than a single patch release. Related third-party IPI CVEs have been patched: Microsoft EchoLeak (CVE-2025-32711) was fixed server-side in May 2025; LangChain GmailToolkit (CVE-2025-46059) was fixed; and the ChatGPT Plugins issue (CVE-2024-5184) has a fix.
- **Active Exploitation:** Yes — confirmed active exploitation in the wild, reported by multiple primary sources. Google's Threat Intelligence team (Apr 23, 2026 blog post) observed IPI abuse at web scale via Common Crawl, including real-world categories such as SEO manipulation (both simple and advanced automated SEO suites), AI-agent deterrence (infinite-text-stream timeouts), experimental data-exfiltration attempts, and attempts to delete files on a user's machine. Unit 42 (Palo Alto Networks, Mar 3, 2026) confirmed wild exploitation including an AI-based ad-review bypass (reviewerpress[.]com used to push a scam 'military glasses' ad) and SEO poisoning to promote phishing sites impersonating betting platforms. Forcepoint X-Labs (Apr 22, 2026) cataloged 10 distinct live IPI payloads on active websites spanning API-key theft, traffic hijacking, output hijacking, data destruction / RCE, financial fraud, donation scams, and denial-of-service against AI agents. Help Net Security (Apr 24, 2026) also reported IPI 'taking hold in the wild.'
- **Threat Actors:** None specifically named. Google's Threat Intelligence team observed broad, opportunistic abuse by unnamed adversaries rather than attribution to a particular APT or ransomware group. Forcepoint X-Labs noted the use of 'shared injection templates' suggesting organized tooling reused across multiple actors, but no specific group was identified.
- **Mitigation:** Google describes a layered, continuous defense strategy rather than a single patch. Key controls: (1) AI Vulnerability Reward Program and human + automated red-teaming; (2) centralized vulnerability cataloging; (3) synthetic data generation via 'Simula' to retrain/validate models against attack variants; (4) deterministic defenses via a Policy Engine — user confirmation for sensitive actions, URL sanitization, tool-chaining policies, and regex-based takedowns ('point fixes'); (5) ML-based defenses using synthetic training/validation sets; (6) LLM-based defenses via hardened system prompts; (7) model hardening so Gemini ignores harmful instructions in retrieved data. Supporting guidance from OWASP LLM01:2025 — constrain model behavior with system prompts, define/validate output formats, apply input/output filtering (semantic filters and the RAG Triad), enforce least-privilege and function/tool calls via API tokens rather than the model, require human-in-the-loop approval for high-risk operations, segregate and label untrusted external content, and perform regular adversarial/penetration testing.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) embeds adversarial instructions in external data (web pages, emails, documents, images, calendar entries, metadata, tool responses) that an LLM later ingests to fulfill a user request. When the model reasons over this data, the injected text is interpreted as instructions, enabling exfiltration of sensitive content via crafted URLs, bypass of tool guardrails, unauthorized transactions, manipulation of AI-generated summaries, or execution of destructive commands. Common delivery techniques documented in the wild include HTML/CSS zero-sized text, CSS-suppressed content, invisible Unicode/zero-width characters, payload splitting, semantic tricks (multilingual or role-play instructions), and multimodal injection (instructions hidden in images). The vulnerability is inherent to current LLM architectures, which cannot reliably separate trusted system instructions from untrusted data within the same context window, exposing every application that allows an LLM to read external content.
- **Affected Products:** Google Workspace with Gemini (Gmail, Google Docs, and other Workspace apps with Gemini features); broadly, LLM-powered agents including Anthropic Claude Code Security Review, Google Gemini CLI Action, and GitHub Copilot Agent
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — multiple public PoCs and documented weaponized payloads: (1) PayloadAllTheThings repository (https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Prompt%20Injection/README.md); (2) OWASP AITG-APP-01 testing guide (https://github.com/OWASP/www-project-ai-testing-guide/blob/main/Document/content/tests/AITG-APP-01_Testing_for_Prompt_Injection.md); (3) SecurityWeek 'Comment and Control' PoC against Claude Code, Gemini CLI, and GitHub Copilot Agent (https://www.securityweek.com/claude-code-gemini-cli-github-copilot-agents-vulnerable-to-prompt-injection-via-comments/); (4) Unit 42 documented in-the-wild payloads (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/)
- **Patch Available:** No discrete vendor patch. Indirect prompt injection is a design-level threat class; Google addresses it through continuous defense-in-depth improvements to Gemini, the Workspace integration, and the surrounding Policy Engine rather than a single downloadable fix. Workspace administrators are directed to the companion Google Admin help article (https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini) for current guidance and to enable available enterprise controls.
- **Active Exploitation:** Yes — confirmed active exploitation in the wild. (1) Google observed via Common Crawl telemetry a relative increase of 32% in malicious-category indirect prompt injections between November 2025 and February 2026 (https://blog.google/security/prompt-injections-web/, 2026-04-23). (2) Palo Alto Unit 42 documented weaponized real-world IPI payloads used for AI-based ad-review evasion (e.g., reviewerpress[.]com), SEO manipulation promoting phishing sites, data destruction, denial-of-service, unauthorized transactions, sensitive data leakage, and system-prompt leakage (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/, 2026-03-03). (3) SecurityWeek reported active exploitation of Anthropic Claude Code Security Review, Google Gemini CLI Action, and GitHub Copilot Agent via the 'Comment and Control' technique, in which malicious GitHub issue comments and PR titles hijack agents to exfiltrate secrets and execute arbitrary commands (https://www.securityweek.com/claude-code-gemini-cli-github-copilot-agents-vulnerable-to-prompt-injection-via-comments/, 2026-04-16; PoC: https://oddguan.com/blog/comment-and-control-prompt-injection-credential-theft-claude-code-gemini-cli-github-copilot/).
- **Threat Actors:** None known
- **Mitigation:** No single patch; Google's layered, defense-in-depth strategy includes: (1) Deterministic/Policy defenses — centralized Policy Engine enforcing user confirmation, URL allow/sanitization lists, tool-chaining policies, regex take-downs of known-bad payloads; (2) ML-based defenses — retraining classifiers and Gemini on synthetic adversarial data; (3) LLM/prompt defenses — hardened system instructions telling the model to ignore instructions found in data; (4) Model-level hardening — improving Gemini's intrinsic ability to identify and disregard harmful instructions embedded in retrieved content; (5) Discovery — dedicated human and automated red teams, the AI Vulnerability Reward Program, and a centralized vulnerability catalog. Additional OWASP-recommended controls: constrain model behavior with explicit system-prompt scoping; deterministically validate expected output formats; apply semantic and string-based input/output filtering; enforce least-privilege API tokens (never hand tokens to the model); require human-in-the-loop approval for high-risk actions; segregate and clearly mark untrusted external content in the prompt; conduct ongoing adversarial testing using tools such as OWASP AITG-APP-01.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Two vulnerabilities realized the agentic browsing risk: (1) CVE-2026-0628 - Insufficient policy enforcement in Chrome's WebView tag (Chrome < 143.0.7499.192) allowed a malicious browser extension to use the declarativeNetRequests API to intercept and inject JavaScript/HTML into the privileged 'Gemini Live in Chrome' side panel at gemini.google.com/app. Because the Gemini Live panel runs with elevated trust, the injected script effectively rode that trust to access the camera, microphone, local files/directories, and to take screenshots of HTTPS sites. (2) GeminiJack - A zero-click indirect prompt injection in Google Gemini Enterprise that abused the RAG retrieval flow: a malicious instruction planted inside an ordinary shared Google Doc, Calendar invitation, or Gmail message was retrieved by Gemini during a routine workspace query and treated as a trusted command, causing Gemini to enumerate connected Workspace data and exfiltrate the results to an attacker-controlled server via a disguised external image (HTTP) request.
- **Affected Products:** Google Chrome prior to 143.0.7499.192 (Windows/Mac fixed in 143.0.7499.193, Linux fixed in 143.0.7499.192), Google Gemini Enterprise, Google Vertex AI Search
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Exploit Available:** Public proof-of-concept available. Noma Labs published a step-by-step PoC for the GeminiJack indirect-prompt-injection vulnerability at https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/. For CVE-2026-0628, Palo Alto Networks Unit 42 publicly disclosed and demonstrated the malicious-extension attack against Chrome's Gemini Live in Chrome panel at https://unit42.paloaltonetworks.com/gemini-live-in-chrome-hijacking/.
- **Patch Available:** Yes - Google patched CVE-2026-0628 in Chrome stable channel on January 6, 2026 (143.0.7499.192 on Linux; 143.0.7499.193 on Windows and macOS). Vendor advisory / Chrome Releases announcement: https://chromereleases.googleblog.com/2026/01/stable-channel-update-for-desktop.html. Google also deployed server-side mitigations for the GeminiJack issue in Gemini Enterprise and Vertex AI Search (Vertex AI Search was fully separated from Gemini Enterprise).
- **Active Exploitation:** No confirmed in-the-wild exploitation has been reported. CVE-2026-0628 is not listed in the CISA Known Exploited Vulnerabilities (KEV) catalog. NVD and Tenable report no known exploits. Unit 42 and The Hacker News describe CVE-2026-0628 as a high-severity flaw responsibly disclosed by Palo Alto Networks Unit 42 and patched by Google in early January 2026 without observed in-the-wild abuse at the time of disclosure. For GeminiJack, Noma Labs and Infosecurity Magazine likewise report no active exploitation prior to patching; the disclosure was research-led rather than threat-actor-led.
- **Threat Actors:** None known
- **Mitigation:** Update Google Chrome to version 143.0.7499.192 (Linux) or 143.0.7499.193 (Windows/macOS) or later immediately. Audit and remove unnecessary or untrusted browser extensions. Enforce Chrome enterprise extension policies: ExtensionInstallBlocklist, ExtensionInstallAllowlist, and ExtensionInstallSources to restrict installs to approved sources. Enable Chrome's Enhanced Safe Browsing / Advanced Web Protection (Live Page Scanning). For agentic/Gemini Enterprise deployments, follow NCSC guidance on prompt injection, carefully review trust boundaries for retrieval/RAG sources, monitor for anomalous outbound image/exfil requests, and apply Google's server-side mitigations that separate Vertex AI Search from Gemini Enterprise and harden retrieval/indexing interactions.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2025-48530 is a memory safety vulnerability in CrabbyAVIF, Android's Rust-based AVIF parser/decoder. The vulnerability is caused by incorrect bounds checking logic in multiple locations within the AVIF decoder, resulting in out-of-bounds (OOB) memory accesses, including a linear buffer overflow related to NV12 format handling (YUV planes, alpha plane, Y plane, UV planes, chroma width calculation, plane size calculation, and row bytes). It is classified as CWE-125 (Out-of-bounds Read). When chained with other bugs, it could lead to remote code execution with no additional execution privileges needed and no user interaction required. The flaw originated in an unsafe Rust code block.
- **Affected Products:** Google Android 16.0, Android System component (versions prior to 2025-08-05 security patch level), CrabbyAVIF (Rust-based AVIF parser/decoder)
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** No public exploit code is currently available. The vulnerability was discovered and fixed internally by Google before being shipped in production; Android's Scudo hardened allocator with guard pages surrounding secondary allocations rendered it non-exploitable.
- **Patch Available:** Yes, Google has addressed this vulnerability in the Android Security Bulletin August 2025 (https://source.android.com/docs/security/bulletin/2025-08-01). Update to security patch level 2025-08-05 or later.
- **Active Exploitation:** No confirmed active exploitation in the wild has been reported. The vulnerability was identified internally by Google before being shipped and was caught before release. No threat actor groups, APT campaigns, or ransomware operators are known to be exploiting this vulnerability.
- **Threat Actors:** None known
- **Mitigation:** Apply the security patches from the Android Security Bulletin August 2025 immediately. Ensure all Android 16.0 devices are updated to the latest security patch level (2025-08-05 or later). Implement network segmentation to limit exposure of vulnerable devices and limit network exposure of affected Android devices until patches can be applied. Android's Scudo hardened allocator with guard pages surrounding secondary allocations provides additional runtime mitigation against exploitation.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection embeds hidden malicious instructions inside external content that an AI assistant later ingests and processes as part of its context (e.g., emails, documents, calendar invites, web pages, PDFs). Because LLMs cannot reliably distinguish trusted system/user instructions from untrusted data in the same context stream, the attacker-controlled instructions are executed alongside the legitimate task. This can cause the model to exfiltrate sensitive user data, manipulate outputs, perform unauthorized actions (e.g., sending mail, deleting calendar events), bypass safety guardrails, or hijack autonomous agents. Specific techniques include hidden HTML/CSS (white-on-white text, font-size:0, opacity:0) wrapping prompts in tags like <Admin>, instructions embedded in markdown/HTML, prompt text placed in image alt-text, and adversarial content on web pages fetched by AI agents (e.g., reviewerpress[.]com observed by Palo Alto Unit 42).
- **Affected Products:** Google Gemini (Gemini app, Gemini in Google Workspace — Gmail, Docs editors, Drive, Chat, Calendar), Gemini 2.5 family of models. The vulnerability class (indirect prompt injection) broadly affects any LLM/agent that ingests untrusted external content.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable (no CVE is assigned to this Google Security Blog advisory; indirect prompt injection is treated as an AI-systemic risk class rather than a single scored vulnerability).
- **Exploit Available:** Yes — public proof-of-concept exploits exist. Notable examples: (1) 'Phishing For Gemini' PoC submitted to 0DIN (researcher Marco Figueroa, July 2025) demonstrating indirect prompt injection via hidden HTML in emails targeting the 'Summarize this email' feature — https://0din.ai/blog/phishing-for-gemini and https://0din.ai/disclosures/e24d9e6b-8c5e-4e2f-ad4f-2abc0072307a; (2) 'Inject My PDF' by Kai Greshake — https://kai-greshake.de/posts/inject-my-pdf; (3) EchoLeak (CVE-2025-32711) referenced by Google — https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-32711; (4) ChatGPT plugin prompt-injection research by Embrace The Red — https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/.
- **Patch Available:** No traditional single vendor patch is applicable — this is a class of vulnerability addressed through rolling, defense-in-depth updates. Google has deployed hardened Gemini 2.5 models, proprietary prompt-injection classifiers, and the broader layered controls described above. Companion documentation: https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini . Microsoft-side mitigation for the related EchoLeak (CVE-2025-32711) is tracked at https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-32711 .
- **Active Exploitation:** Yes — confirmed exploitation / weaponization in the wild has been reported across multiple sources: (a) Palo Alto Unit 42 — 'Fooling AI Agents: Web-Based Indirect Prompt Injection Observed in the Wild' (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/) documents live abuse including AI ad-review evasion (e.g., reviewerpress[.]com), SEO manipulation to push phishing sites, data destruction, DoS, unauthorized transactions, and system prompt leakage; (b) Proofpoint — 'Cybersecurity stop of the month: how threat actors weaponize AI assistants with indirect prompt injection' (https://www.proofpoint.com/us/blog/email-and-cloud-threats/stop-month-how-threat-actors-weaponize-ai-assistants-indirect-prompt) reports observed threat-actor use of indirect prompt injection against enterprise AI assistants; (c) 0DIN — 'Phishing For Gemini' (https://0din.ai/blog/phishing-for-gemini, July 10 2025) disclosed a working PoC against Gemini in Workspace summarization; (d) Microsoft MSRC — EchoLeak (CVE-2025-32711) confirmed as a real-world data-exfiltration exploit against Microsoft 365 Copilot; (e) academic write-up of a zero-click enterprise-AI-assistant exploit enabling data exfiltration and RCE — https://arxiv.org/abs/2509.10540 . Google's blog itself notes classifiers were trained on 'real-world examples' and that protections are continuously monitored via a 'broad sweep of the public web' for known indirect prompt injection patterns.
- **Threat Actors:** None known (no specific APT groups, named campaigns, or ransomware operators are publicly attributed to exploiting this vulnerability class in the Google Security Blog post; threat actors are referenced generically as 'adversaries')
- **Mitigation:** Google's layered defense strategy combines: (1) Prompt injection content classifiers — proprietary ML models trained on real-world examples to detect and filter malicious instructions in emails and files; (2) Security thought reinforcement — targeted system instructions that tell the LLM to prioritize the user's task and ignore adversarial content in data; (3) Markdown sanitization and suspicious URL redaction — strip dangerous markdown and use Google Safe Browsing to redact malicious links; (4) User confirmation framework (Human-In-The-Loop, HITL) — require explicit user approval before risky operations such as deleting calendar events or sending mail; (5) End-user security mitigation notifications — contextual warnings and 'Learn more' links when defenses neutralize an attack; (6) Model hardening — adversarial training of Gemini 2.5 models. General best-practice defenses called out by other researchers include spotlighting (separating untrusted text from trusted instructions), instruction hierarchy, web-scale detection, HTML linting at ingestion, LLM firewalls with guard prompts, and post-processing filters on model output.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored APT actors exploit publicly known (n-day) vulnerabilities on internet-exposed network edge devices — primarily large backbone routers and provider/customer edge (PE/CE) routers — for initial access. The campaign chains Cisco IOS XE authentication bypass (CVE-2023-20198) with web UI command injection/privilege escalation (CVE-2023-20273), and chains Ivanti Connect Secure authentication bypass (CVE-2023-46805) with command injection (CVE-2024-21887). Once inside, attackers use the Web Services Management Agent (WSMA) endpoints /webui_wsma_Http or /webui_wsma_Https, abuse Cisco Guest Shell containers, modify router ACLs (often naming them 'access-list 20') to whitelist attacker IPs, enable SSH/HTTP on non-standard ports, capture TACACS+/RADIUS authentication traffic via PCAP, modify TACACS+ server configs to harvest credentials, enumerate router configs and BGP routes, and use GRE/IPsec tunnels for covert C2 and custom SFTP clients (cmd1, cmd3, new2, sft) for data exfiltration. Trusted provider-to-provider/customer links and VPS infrastructure are used for pivoting and anonymization. No zero-day exploitation has been observed; all exploited vulnerabilities are publicly known.
- **Affected Products:** Cisco IOS XE Software (CVE-2023-20198, CVE-2023-20273), Cisco IOS/IOS XE Smart Install (CVE-2018-0171), Ivanti Connect Secure 9.x, 22.x and Ivanti Policy Secure (CVE-2024-21887), Palo Alto Networks PAN-OS with GlobalProtect feature (CVE-2024-3400)
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H (highest severity vector, applies to CVE-2024-3400 and CVE-2023-20198, both scored 10.0). Other vectors: CVE-2024-21887 = CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H (9.1); CVE-2018-0171 = CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H (9.8); CVE-2023-20273 = 7.2.
- **Exploit Available:** Yes. Public proof-of-concept exploits are widely available on GitHub, including https://github.com/smokeintheshell/CVE-2023-20198 and https://github.com/Chocapikk/CVE-2024-21887. Horizon3.ai also published a deep-dive with PoC for CVE-2023-20198/CVE-2023-20273 at https://horizon3.ai/attack-research/attack-blogs/cisco-ios-xe-cve-2023-20198-deep-dive-and-poc/.
- **Patch Available:** Yes. Patches are available from each affected vendor for all five CVEs. Vendor advisories: Ivanti CVE-2024-21887 (https://forums.ivanti.com/s/article/CVE-2024-21887), Palo Alto CVE-2024-3400 (https://security.paloaltonetworks.com/CVE-2024-3400), Cisco CVE-2023-20198/CVE-2023-20273 (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxe-webui-privesc-j22SaA4z), Cisco CVE-2018-0171 (https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180328-smi2.html). All listed CVEs are tracked in the CISA Known Exploited Vulnerabilities Catalog. CISA recommends using the Cisco Software Checker (https://sec.cloudapps.cisco.com/security/center/softwarechecker.x) to identify fixed versions.
- **Active Exploitation:** Yes — confirmed active exploitation in the wild by PRC state-sponsored threat actors. The campaign has targeted telecommunications, government, transportation, lodging, and military infrastructure networks globally, with focus on large backbone routers and provider/customer edge routers. CISA explicitly states that exploitation of zero-day vulnerabilities has not been observed to date; all exploited flaws are publicly known CVEs. Salt Typhoon activity in particular has been disclosed by FBI/CISA since September 2024 as one of the most significant espionage campaigns against U.S. critical infrastructure.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor (PRC state-sponsored APT actors)
- **Mitigation:** 1) Prioritize patching the listed CVEs (CVE-2024-21887, CVE-2024-3400, CVE-2023-20198, CVE-2023-20273, CVE-2018-0171) on all internet-exposed network devices; sequence by risk. 2) Implement management-plane isolation and control-plane policing (CoPP); place management services in a dedicated out-of-band management network or management VRF with no route leakage to the data plane and blocked unauthorized egress. 3) Use vendor-recommended OS versions; upgrade unsupported devices; compare firmware/image hashes against vendor values and enforce signed images. 4) Disable unused ports/protocols; disable Telnet, unencrypted HTTP/FTP; use SSH, HTTPS, SFTP/SCP, SNMPv3 with no default community strings. 5) Change default administrative credentials; require public-key authentication; minimize auth attempts/lockout windows. 6) Baseline and audit running router configurations; review ACLs (look for unauthorized 'access-list 20' entries), transport protocols, and routing tables for unauthorized changes. 7) Monitor for abnormal TACACS+/RADIUS redirection, GRE/tunneling traffic, and Cisco Guest Shell activity via syslog, AAA accounting, and telemetry; disable Guest Shell if unused.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** An attacker sends a specially crafted email to a Microsoft Outlook for Windows user containing an extended MAPI property called PidLidReminderFileParameter. The attacker embeds a Universal Naming Convention (UNC) path pointing to an SMB share (TCP 445) on an attacker-controlled server. When Outlook processes the message — including via the default reminder behavior — the Outlook client automatically opens an outbound SMB connection to the attacker's UNC path and transmits an NTLMv2 authentication negotiation. The attacker captures the NetNTLMv2 hash and can perform an NTLM relay attack or attempt offline cracking to recover the plaintext password for lateral movement. The vulnerability requires no user interaction.
- **Affected Products:** Microsoft Outlook for Windows: Microsoft 365 Apps for Enterprise, Outlook 2016, Outlook 2019, Outlook 2019 LTSC, Outlook LTSC Standard 2021, Outlook LTSC Professional Plus 2021, Microsoft Office 2019 / LTSC Standard 2021 / LTSC Professional Plus 2021. NOT affected: Outlook for Mac, Outlook for iOS/Android, and Outlook hosted solely by Microsoft 365 cloud services.
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** Yes — multiple public proof-of-concept exploits are available on GitHub: https://github.com/Trackflaw/CVE-2023-23397 and https://github.com/vlad-a-man/CVE-2023-23397. The PoCs craft a specially crafted .msg file containing a PidLidReminderFileParameter extended MAPI property pointing to an attacker-controlled SMB UNC path to harvest the victim's NetNTLMv2 hash.
- **Patch Available:** Yes — Microsoft released an Outlook for Windows security update on March 14, 2023 (March 2023 Patch Tuesday). Official advisory URL: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23397
- **Active Exploitation:** Yes — confirmed active exploitation in the wild. Microsoft Threat Intelligence attributed exploitation to Strontium (APT28 / GRU Unit 26165) starting in April 2022. CISA added CVE-2023-23397 to the Known Exploited Vulnerabilities (KEV) catalog. CISA/FBI/NSA joint advisory AA25-141A (May 21, 2025) confirms GRU Unit 26165 weaponized CVE-2023-23397 against Western logistics entities and technology companies involved in coordinating aid to Ukraine. Unit 42 observed Fighting Ursa (APT28) leveraging the Outlook zero-day as early as March 2022 against at least 30 organizations in 14 nations.
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS), military unit 26165 — tracked in industry as APT28, Fancy Bear, Forest Blizzard, Blue Delta, Fighting Ursa, and Microsoft-named Strontium
- **Mitigation:** Apply the March 14, 2023 Microsoft Outlook security update. Where patching is not immediately possible: (1) block outbound TCP 445/SMB from the corporate network, (2) disable the WebClient service, (3) add users to the Protected Users Security Group, (4) enforce SMB signing, (5) disable the 'Show reminders' setting in Outlook, and (6) audit prior Outlook messages for PidLidReminderFileParameter / UNC properties and remove them.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23397

---

## 9. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

**Parallel AI Enrichment:**

- **Technical Details:** This CrowdStrike blog post (published June 30, 2026 by Hananel Livneh) is a thought-leadership/marketing article about general browser-based threats rather than a disclosure of a specific CVE. It describes attack vectors that exploit the browser as the operating environment for modern work, including zero-day and N-day exploitation of rendering logic, JavaScript execution, document handling, memory-safety weaknesses, sandbox escapes and privilege escalation, as well as phishing, clickjacking, cross-site scripting, HTML smuggling, malicious downloads, credential theft, session hijacking/abuse, and adversary-in-the-middle (AiTM) techniques. It cites the CrowdStrike 2026 Global Threat Report and Verizon 2026 Data Breach Investigations Report, noting that vulnerability exploitation surpassed stolen credentials as the top breach entry point in 2025 and that 42% of vulnerabilities were exploited before public disclosure.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unavailable.
- **Patch Available:** Patch availability unavailable. The article does not disclose a specific CVE or vendor patch; the only product referenced as the protective control is CrowdStrike Falcon Secure Access, promoted via the blog and a linked data sheet at https://www.crowdstrike.com/en-us/resources/data-sheets/falcon-secure-access/.
- **Active Exploitation:** No confirmed in-the-wild exploitation of a specific vulnerability is reported in this article. The article cites a general statistic from the CrowdStrike 2026 Global Threat Report stating that 42% of vulnerabilities were exploited before public disclosure, but does not attribute active exploitation to any specific named CVE.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable (no specific patch to apply for a specific CVE). General hardening guidance from the article: keep browsers patched promptly, implement defense-in-depth against phishing and AiTM attacks, protect session tokens against hijacking and MFA bypass, and consider a moving-target defense inside the browser such as the JavaScript Language Randomization (JSLR) capability delivered via CrowdStrike Falcon Secure Access, which operates inside the browser JavaScript execution environment.
- **Vendor Advisory:** https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/

---

## 10. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

**Parallel AI Enrichment:**

- **Technical Details:** The referenced item is not a vulnerability disclosure but a CrowdStrike survey research blog published on June 22, 2026 (author: Karishma Asthana, Cloud & Application Security). It summarizes findings of the CrowdStrike State of Cloud Detection and Response (CDR) Survey on why cloud breaches succeed. Key reported statistics: 94% of organizations experienced cloud intrusions that resulted in data exposure or exfiltration; 73% cannot consistently guarantee detection of cloud intrusions; 56% say gaps in cloud control-plane visibility hurt detection; 95% do not have full sensor/agent coverage across cloud workloads and instances; 78% cannot reliably distinguish legitimate from malicious activity; 79% say their tools generate too many alerts and analysts spend ~77% of triage time on false positives/low-priority items; 98% do not remediate every identified threat; 68% take 15+ minutes to detect a cloud intrusion (51% take at least one hour); 91% cannot contain all cloud intrusions in real time; organizations use an average of three tools to detect cloud breaches, and 67% report significant/moderate gaps integrating cloud detections into SOC/SIEM workflows; ~80% rely heavily on manual investigations; 38% of breached organizations cite tool fragmentation as a contributing factor in intrusion escalation; 83% run AI/ML workloads in the cloud and 81% experienced incidents targeting those AI/ML environments. The mechanism described is a chain of detection-and-response gaps (visibility, signal-to-noise, time-to-detect, tool fragmentation, manual workflows) that lets adversaries achieve persistence, lateral movement, escalation, and exfiltration in cloud environments.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Not applicable. The referenced publication is a CrowdStrike survey/research blog post (the State of Cloud Detection and Response Survey), not a vulnerability advisory. No specific CVE, proof-of-concept, or exploit code is associated with this content.
- **Patch Available:** No vendor patch applies. The referenced publication is the CrowdStrike State of Cloud Detection and Response Survey blog (June 22, 2026), a research/marketing survey, not a security advisory or software update.
- **Active Exploitation:** The publication does not report active exploitation of a specific vulnerability. It reports survey-respondent claims that 94% of organizations experienced cloud intrusions resulting in data exposure or exfiltration, and that 81% experienced incidents targeting cloud-hosted AI/ML workloads. These are self-reported survey statistics about cloud-intrusion incidents generally, not confirmed in-the-wild exploitation of a specific CVE or product flaw.
- **Threat Actors:** None known
- **Mitigation:** The survey does not describe a specific software patch. Recommended hardening steps drawn from the publication: (1) Achieve full, unified visibility across cloud control-plane activity, workloads, identities/APIs, and instances, eliminating coverage gaps (the survey notes 95% of organizations lack full sensor coverage). (2) Improve signal fidelity so analysts can distinguish legitimate from malicious activity, reducing the ~77% of triage time currently spent on false positives. (3) Reduce mean time to detect below the 15-minute mark (68% currently exceed it) via real-time telemetry and correlation across control plane and workloads. (4) Consolidate fragmented tooling — the average organization uses three detection tools and 67% report integration gaps — by unifying detections into SOC/SIEM workflows. (5) Automate investigation and response to reduce the ~80% reliance on manual investigations and enable real-time containment (91% currently cannot contain all intrusions in real time). (6) Prioritize remediation of every identified threat (98% currently deprioritize some) and address tool fragmentation, cited by 38% of breached organizations as a contributor to escalation. (7) Apply specific protections to AI/ML cloud workloads, since 83% run such workloads and 81% have experienced incidents against them.
- **Vendor Advisory:** https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/

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

## 15. 🟡 High Severity — Tesla vulnerable to atom exhaustion via untrusted URL scheme

**CVE:** `CVE-2026-48597` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-h74c-q9j7-mpcm>

> ### Summary

In the Mint adapter for the Tesla HTTP client library, `Tesla.Adapter.Mint.open_conn/2` passes the URL scheme of every outgoing request through `String.to_atom/1` with no allow-list validation. Because BEAM atoms are permanent (never garbage-collected) and the atom table is bounded at roughly 1,048,576 entries, an attacker who can vary the URL scheme across requests can mint one fresh…

---

## 16. 🟡 High Severity — Tesla: Authorization header leaks on cross-origin redirect via case-sensitive filtering

**CVE:** `CVE-2026-48595` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-9m9w-gxf7-rh8m>

> ### Summary

`Tesla.Middleware.FollowRedirects` is meant to strip the `Authorization` header when following a cross-origin redirect, but performs the check with a case-sensitive comparison against the lowercase string `&quot;authorization&quot;`. Because Tesla preserves header keys exactly as supplied by the caller, any application that sets the header with its RFC 7235 canonical casing (`&quot;Au…

---

## 17. 🟡 High Severity — Tesla has CRLF injection in request `Content-Type` header via `add_content_type_param`

**CVE:** `CVE-2026-48596` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-q7jx-v53g-848w>

> ### Summary

`Tesla.Multipart.add_content_type_param/2` appends caller-supplied strings to the multipart `Content-Type` header with no validation. A param value containing `\r\n` splits the header line, allowing an attacker who controls any content-type parameter (charset, boundary parameter, etc.) to inject arbitrary headers into the outbound HTTP request.

### Details

`add_content_type_param/2`…

---

## 18. 🟡 High Severity — sigstore-go has a multi-log threshold bypass via single compromised log

**CVE:** `CVE-2026-49834` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-9vcr-p3rj-q5q6>

> ### Impact
_What kind of vulnerability is it? Who is impacted?_

A verifier configured with WithTransparencyLog(N&gt;1) or WithSignedCertificateTimestamps(N&gt;1) expected defense-in-depth against the compromise of a single log instance. However, threshold counting counted verified witnesses per-entry or per-validation-path rather than per-log-authority.

As a result, a single compromised transpar…

---

## 19. 🟡 High Severity — mint: Unbounded CONTINUATION/HEADERS frame accumulation (CONTINUATION flood)

**CVE:** `CVE-2026-49754` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-2p26-p43x-fhp8>

> ### Summary

Mint&#x27;s HTTP/2 client accumulates `CONTINUATION` header-block fragments into a per-connection buffer with no cap on size or frame count. A malicious or compromised HTTP/2 server can drive the client&#x27;s memory to arbitrary size by streaming an endless chain of `CONTINUATION` frames after a `HEADERS` frame that omits `END_HEADERS`, causing memory exhaustion and BEAM process deat…

---

## 20. 🟡 High Severity — mint: Content-Length header accepts non-RFC "+" sign prefix

**CVE:** `CVE-2026-49753` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-mjqx-c6f6-7rc2>

> ### Summary

Mint&#x27;s HTTP/1 client accepts `Content-Length` header values with a leading `+` sign (e.g. `+0`, `+123`), which RFC 7230 forbids (`Content-Length = 1*DIGIT`). On a connection shared with a strict fronting proxy or load balancer, this parser disagreement is a response-smuggling primitive: the proxy frames the body one way, Mint frames it another, and bytes meant for one response le…

---

## 21. 🟡 High Severity — YesWiki has Unsafe eval() in its Formula Calculato, Leading to Remote Code Execution & Denial of Service

**CVE:** `CVE-2026-52778` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-px5m-h76g-p7p8>

> ### Summary

An unsafe execution vulnerability exists in the Bazar form field calculator (CalcField.php) of YesWiki. The application attempts to sanitize user-defined mathematical formulas using a complex recursive regular expression before passing them to the PHP eval() function. This implementation is inherently flawed: it is vulnerable to Regular Expression Denial of Service (ReDoS / Stack Over…

---

## 22. 🟡 High Severity — YesWiki: Authenticated (Admin) Server-Side Template Injection to Remote Code Execution via Bazar Semantic Templates

**CVE:** `CVE-2026-52762` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-65p8-9433-jpcp>

> ### Summary
YesWiki Bazar contains a stored Server-Side Template Injection (`SSTI`) vulnerability in the semantic template feature that can be escalated to confirmed Remote Code Execution (`RCE`). An authenticated administrator can place arbitrary Twig expressions into the `Semantic template (Twig)` field (`bn_sem_template`), and that content is later executed server-side when public semantic endp…

---

## 23. 🟡 High Severity — laravel-backup-restore has an OS Command Injection during database restore

**CVE:** `CVE-2026-53932` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-w9mx-xmg4-gc4r>

> ## Summary
A crafted backup archive can trigger OS command injection during database restore. The restore workflow extracts a ZIP archive, enumerates files under `db-dumps`, converts the dump path to an absolute path, and passes that path into database import commands that are built as shell command strings.

The dump filename is not shell-escaped before it is interpolated into commands such as:

…

---

## 24. 🟡 High Severity — Ruby CSS Parser: SSRF and Local File Disclosure in `CssParser::Parser#read_remote_file`

**CVE:** `CVE-2026-53727` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-9pmc-p236-855h>

> ## Summary

`CssParser::Parser#read_remote_file` (and therefore `load_uri!`, and the `@import`-following branch of `add_block!`) issues HTTP/HTTPS requests against any host, port and URI it is handed, with no scheme allowlist, no host / IP filtering, and no protection against link-local, loopback or RFC‑1918 addresses. `Location:` redirects are followed recursively back into the same function, whi…

---

## 25. 🟡 High Severity — org.hl7.fhir.core: ReDoS via FHIRPath matches()/replaceMatches() in FHIR Validator HTTP Endpoint

**CVE:** `CVE-2026-49485` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-7cmj-v6x8-frvv>

> # Summary
All implementations of FHIRPathEngine accept arbitrary FHIRPath expressions and evaluate them without input validation. The utility intended to secure this evaluation did so incorrectly, and did not fully cover all places in which evaluation was being done. An attacker can send a resource containing an evil regex pattern that causes catastrophic backtracking, exhausting system resources,…

---

## 26. 🟡 High Severity — Soup Sieve: Regular Expression Denial of Service (ReDoS) via Selector Parser

**CVE:** `CVE-2026-49477` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-836r-79rf-4m37>

> ### Summary

The CSS selector parser in soupsieve (the CSS selector engine for Beautiful Soup 4) contains a regular expression vulnerable to catastrophic backtracking. When processing an attribute selector with an unterminated quoted value, the `VALUE` regex pattern in `css_parser.py` enters exponential backtracking. A payload of only **300 bytes** causes the regex engine to hang for **over 3 seco…

---

## 27. 🟡 High Severity — Phantom: Arbitrary file write and decode-bomb DoS via unconfined MCP tool paths

**CVE:** `CVE-2026-37555` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-52vm-mxx8-f227>

> ### Impact

In Phantom &lt;= 1.3.0, when `PHANTOM_OUTPUT_DIR` was unset (the default), the MCP tools accepted arbitrary absolute output paths with no confinement. Anything able to send tool calls (e.g. an AI agent driving the MCP interface) could **write or overwrite arbitrary files** the process user can write — including shell startup files (`~/.zshrc`) or a Reaper `__startup.lua`, which is effe…

---

## 28. 🟡 High Severity — pyLoad: SSRF guard bypass via IPv6 6to4/NAT64 transition wrappers of internal IPs

**CVE:** `CVE-2026-48737` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-m5x5-28jr-gpjj>

> ## Summary

`is_global_address` in [`src/pyload/core/utils/web/check.py`](https://github.com/pyload/pyload/blob/1b12dc7f348db8c144e0f39215680415e90ca4d2/src/pyload/core/utils/web/check.py) is the central guard against SSRF-style outbound connections in pyload-ng. It tests whether a given IP is &quot;globally routable&quot; via Python&#x27;s `ipaddress.ip_address(value).is_global`, and callers trea…

---

## 29. 🟡 High Severity — Microsoft Patches Defender ‘RoguePlanet’ Vulnerability

**CVE:** `CVE-2026-50656` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://www.securityweek.com/microsoft-patches-defender-rogueplanet-vulnerability/>

> The privilege escalation vulnerability tracked as CVE-2026-50656 has been patched with a Microsoft Malware Protection Engine update. The post Microsoft Patches Defender ‘RoguePlanet’ Vulnerability appeared first on SecurityWeek .

---

## 30. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
