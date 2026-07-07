# Zero Day Pulse

> **Generated:** 2026-07-07 02:00 UTC &nbsp;|&nbsp; **Total:** 39 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 13 &nbsp;|&nbsp; 🟡 High: 26 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated path traversal vulnerabilities in SimpleHelp Remote Support/RMM (versions 5.5.7 and earlier) allow an attacker to craft HTTP requests that retrieve arbitrary files from the SimpleHelp host (including server configuration files, secrets, and hashed passwords); a compromised server can then be used to pivot to managed endpoints.
- **Affected Products:** SimpleHelp Remote Support / RMM: versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — PoC available: https://github.com/imjdl/CVE-2024-57727
- **Patch Available:** true — vendor updates/patches available (SimpleHelp v5.5.8 and patches for 5.4.10 / 5.3.9). See vendor advisory: https://guides.simple-help.com/kb---security-vulnerabilities-01-2025
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (per CISA); Sophos reporting attributes activity to "DragonForce" actors (per CISA reference).
- **Mitigation:** Immediate actions: isolate or stop any Internet-exposed/unpatched SimpleHelp servers; upgrade to SimpleHelp v5.5.8 (or apply vendor patches for 5.4.10 / 5.3.9) and follow vendor guidance (rotate API tokens, change Administrator and Technician passwords, disable local technician logins where possible, restrict allowed IP addresses). Conduct threat hunting and forensic checks (logs, unexpected technician logins, suspicious outgoing connections, unusual executables), and monitor network traffic per CISA guidance.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — Langroid: Neo4jChatAgent executes LLM-generated Cypher without validation (prompt-to-Cypher injection; config-conditional RCE), mirroring the SQLChatAgent bug fixed in CVE-2026-25879

**CVE:** `CVE-2026-55615` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-2pq5-3q89-j7cc>

> Neo4jChatAgent passes LLM-generated Cypher queries straight to the Neo4j driver with no validation, no statement-type allowlist, and no opt-out gate. The query text is influenceable by prompt injection (direct user input or indirect content the agent reads back via RAG), so an attacker who can influence the prompt can read or destroy all graph data and, when APOC or dbms.security procedures are en…

**Parallel AI Enrichment:**

- **Technical Details:** Neo4jChatAgent passes LLM-generated Cypher queries directly to the Neo4j driver with no validation, no statement-type allowlist, and no opt-out gate. The query text can be influenced via prompt injection (direct user input or indirectly via RAG). If the Neo4j server has APOC or dbms.security procedures enabled, an attacker able to influence the prompt may execute OS-level or filesystem commands, and can read, modify, or delete graph data.
- **Affected Products:** Langroid: Neo4jChatAgent (specific versions unavailable)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Until vendor fixes are confirmed, recommended mitigations include: (1) Remove or disable Neo4j APOC and dbms.security procedures on servers accessible to the agent where possible; (2) Prevent prompt injection by sanitizing or restricting user-supplied inputs and content used in RAG; (3) Add statement-type allowlisting or validation to the agent so only safe Cypher statements (e.g., read-only, parameterized queries) are permitted; (4) Provide an explicit opt-out or administrative control preventing automatic forwarding of LLM-generated queries to the database; (5) Limit network and credential exposure for Neo4j instances (least privilege, firewalling, and isolated service accounts).
- **Vendor Advisory:** https://github.com/advisories/GHSA-2pq5-3q89-j7cc

---

## 3. 🟠 Zero-Day — Langroid: Sandbox Escape to Remote Code Execution via Incomplete `eval()` Mitigation in TableChatAgent

**CVE:** `CVE-2026-54769` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-q9p7-wqxg-mrhc>

> ### Advisory Details
**Title**: Sandbox Escape to Remote Code Execution via Incomplete `eval()` Mitigation in TableChatAgent

**Description**:
### Summary
Langroid is vulnerable to a critical Sandbox Escape leading to Remote Code Execution (RCE) in its `TableChatAgent` and `VectorStore` capabilities. When these agents evaluate LLM-generated tool messages with `full_eval=True`, they attempt to sand…

**Parallel AI Enrichment:**

- **Technical Details:** TableChatAgent.pandas_eval() and VectorStore call eval(code, vars, {}) while leaving __builtins__ available via the globals mapping; because __builtins__ is not removed, Python injects built-ins at execution time, allowing expressions such as __import__('os').system(...) to run and produce unauthenticated RCE when full_eval=True and model output is evaluated.
- **Affected Products:** langroid (pip) <= 0.65.1
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (PoC available: https://github.com/advisories/GHSA-q9p7-wqxg-mrhc)
- **Patch Available:** true (patched in langroid 0.65.2 — see advisory: https://github.com/advisories/GHSA-q9p7-wqxg-mrhc)
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Upgrade to patched langroid 0.65.2. Until patched, do not enable full_eval / avoid evaluating model-generated code (disable pandas_eval or set full_eval=False), and do not execute untrusted eval() of model outputs; if custom sandboxing is required, explicitly remove/sanitize __builtins__ from globals and avoid relying on an empty locals dict as the only restriction.
- **Vendor Advisory:** https://github.com/advisories/GHSA-q9p7-wqxg-mrhc

---

## 4. 🟠 Zero-Day — Prompt Injection Attacks Trick AI Agents Into Making Crypto Payments

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://www.securityweek.com/prompt-injection-attacks-trick-ai-agents-into-making-crypto-payments/>

> Researchers uncovered two campaigns embedding indirect prompt injections in malicious websites to exploit autonomous AI agents browsing the web. The post Prompt Injection Attacks Trick AI Agents Into Making Crypto Payments appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) targets autonomous AI agents that browse the web and execute cryptocurrency payments. Attackers poison SEO results and register typosquatting domains (e.g., debank.auction impersonating DeBank, py-lib-repository.dev serving a fake Python library 'requests-secure-v2'). When an autonomous coding or crypto agent fetches these pages, the LLM ingests attacker-controlled instructions that override the user's original intent. The injections are hidden from human users via three obfuscation techniques: (1) JSON-LD structured-data markup (e.g., @type:SoftwareApplication with an offers object demanding a $3.00 license fee or misrepresenting the page as the authoritative DeBank site); (2) CSS rules positioning divs off-screen (e.g., left: -9999px) or rendering them transparent; (3) SEO poisoning via keyword-stuffed title/meta tags ('DeBank Login', 'DeFi Dashboard', 'Crypto Tracker') plus Open Graph and X (Twitter) metadata. The embedded prompt instructs the agent to call its wallet/payment tool against an attacker-controlled address (~0.0012 ETH observed; related Grok/Bankr incidents drained as much as $150K-$200K in DRB tokens). A separate attack vector used Morse-code prompt injection posted on X to trick Grok/Bankrbot into authorizing unauthorized transfers.
- **Affected Products:** Meta Llama 3.3 70B Instruct, Meta Llama 3.2 90B Vision Instruct, Google Gemini 3 Flash, Google Gemini 2.5 Pro, OpenAI GPT-5.4, Anthropic Claude Sonnet 4.5, xAI Grok, Bankr trading agent
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true - Zscaler ThreatLabz published proof-of-concept demonstrating IPI attacks across 26 LLMs; weaponized in-the-wild exploits observed including typosquatting domains (debank.auction, py-lib-repository.dev) and Morse-code prompt injection against Grok/Bankrbot. Source: https://www.zscaler.com/blogs/security-research/indirect-prompt-injection-web-content-targets-ai-agents
- **Patch Available:** false - there is no single vendor-issued patch for this vulnerability class. OpenAI has publicly stated that prompt injection 'is unlikely to ever be fully solved.' Anthropic has made incremental improvements to Claude's robustness (https://www.anthropic.com/research/prompt-injection-defenses), but mitigations require platform-level guardrails, scoped agent permissions, and human-in-the-loop review of financial actions.
- **Active Exploitation:** true - Zscaler ThreatLabz (July 2, 2026) and Palo Alto Unit 42 (March 3, 2026) document multiple in-the-wild IPI campaigns. Confirmed exploitation: xAI Grok and Bankr trading bot hijacked via Morse-code prompt injection on X in May 2026, draining ~3 billion DRB tokens (~$150K-$200K) from a verified wallet (OECD AI Incident Database 2026-05-04-4a73). Help Net Security reported a sharp rise in IPI activity from November 2025 through February 2026. Typosquatting domains including debank.auction and py-lib-repository.dev actively deployed.
- **Threat Actors:** None known
- **Mitigation:** 1. Apply rigorous input validation and sanitization at the page ingestion layer before content reaches the LLM context window. 2. Enforce least-privilege/capability-scoped tool design so browser-capable agents cannot perform unrestricted payments, transfers, or external writes without human-in-the-loop approval and per-transaction limits. 3. Segregate untrusted web content from trusted system instructions via 'spotlighting' and explicit instruction hierarchy. 4. Restrict domains/URL allowlists when the agent has financial authority. 5. Harden LLM behavior via adversarial training and refuse-on-unrecognized-instruction policies. 6. Deploy network/IDS detections for typosquatted crypto domains and anomalous outbound payments from agent wallets. Anthropic and OpenAI have published research on prompt injection defenses for browser use, including improvements to Claude's robustness.
- **Vendor Advisory:** https://www.zscaler.com/blogs/security-research/indirect-prompt-injection-web-content-targets-ai-agents

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when adversary-controlled external content (web pages, files, hidden HTML or other third-party data) is ingested as context by an LLM or AI agent; that content contains adversarial instructions or payloads which influence the model’s outputs or agent actions. Real-world demonstrations include crafted web content and a benign PoC against AI-powered browsers; a researcher disclosure (GeminiJack) shows IPI used against Google Gemini Enterprise.
- **Affected Products:** AI agents, LLM-powered / AI-powered browsers, systems that ingest third-party web content, Google Gemini Enterprise
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (PoC/demonstrations public — example: http://github.com/brennanbrown/atlas-prompt-injection-poc )
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true (reported by multiple researchers/teams — see Google Security Blog investigation, Noma Labs GeminiJack disclosure, Unit42 and Forcepoint writeups)
- **Threat Actors:** None known
- **Mitigation:** Harden by restricting and validating external inputs (allowlist sources), sanitizing or removing untrusted context before grounding prompts, enforcing strict prompt/context filtering and model grounding, minimizing automated privileged actions, and continuous monitoring and logging of agent actions.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an attack class where an adversary injects malicious instructions into data or tools consumed by a large language model (documents, web content, tool outputs, etc.) so the model follows those instructions while completing a user's query. This can occur without direct user input and is amplified when models use agentic automation and multiple external data sources.
- **Affected Products:** Google Workspace (with Gemini)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Use a layered defense: content filtering/sanitation and ingestion controls, provenance and access controls for external data, scope/privilege restriction for agentic actions, model hardening and guardrails, human review/oversight, and continuous monitoring and updates (see vendor advisory).
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IDPI) is a class of attacks where untrusted web content read by a Gemini-style agent — page text, hidden iframe/3rd-party widget content, user-generated content (reviews, comments), or retrieved documents — embeds instructions that cause the agent to deviate from the user's intended goal. In Chrome's agentic browsing scenario this enables 'goal-hijacking' (agent performs an attacker-chosen action instead of the user's task), unauthorized transactions, exfiltration of sensitive page content (e.g., summarizing a banking tab), or chaining destructive actions across origins. Concrete variants include Noma Labs' 'GeminiJack' zero-click (hidden payloads in Google Docs/Calendar/Gmail coerced Gemini Enterprise into using a disguised external image fetch to leak data) and Brave's Perplexity Comet PoC (prompt-injection comments in a Reddit thread caused the summarization pass to exfiltrate email + Gmail one-time codes and takeover the account). Google's mitigation architecture treats this as a class-level threat rather than a single code defect.
- **Affected Products:** Google Chrome with Gemini in Chrome agentic capabilities (Stable channel, December 2025, agentic preview). Adjacent products in the broader indirect-prompt-injection class: Google Gemini Enterprise and Vertex AI Search (GeminiJack), Perplexity Comet, Cursor < 1.3 (CVE-2025-54131), Gemini CLI (Nov 2025 disclosures), and GitHub Copilot.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true. Public PoCs include: https://github.com/brennanbrown/atlas-prompt-injection-poc (benign HTML demo), Brave's weaponized Comet PoC at https://brave.com/blog/comet-prompt-injection/ (account takeover), Pillar Security's Gemini CLI PoC (https://www.pillar.security/blog/my-agentic-trust-issues-from-prompt-injection-to-supply-chain-compromise-on-gemini-cli), Cyera Research Labs' Gemini CLI disclosures (Nov 2025), and Immersive Labs' email HTML PoC (https://www.immersivelabs.com/resources/c7-blog/weaponizing-llms-bypassing-email-security-products-via-indirect-prompt-injection).
- **Patch Available:** true. Patch/advisory URL: http://security.googleblog.com/2025/12/architecting-security-for-agentic.html (mirror https://blog.google/security/architecting-security-for-agentic/). The accompanying Chromium Quarterly Update (https://www.chromium.org/Home/chromium-security/quarterly-updates/) confirms the AI Security team shipped layered mitigations; Chrome Stable updates in December 2025 carry these defenses. Adjacent vendor patches include Google's GeminiJack fix for Gemini Enterprise and Cursor's 1.3 fix for CVE-2025-54131.
- **Active Exploitation:** true. Unit 42 (Palo Alto Networks) reported web-based indirect prompt injection being actively weaponized in the wild against ad-review and content-moderation agents (Dec 2025). Noma Labs demonstrated a real 'GeminiJack' zero-click exploit chain against Gemini Enterprise. Google paid a $15,000 VRP bounty for an external prompt-injection bug. CVE-2026-0628 (Chrome Gemini panel hijack) was reported as exploited in the wild and patched. Sources: https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/ ; http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability ; https://blog.google/security/architecting-security-for-agentic/ ; https://brave.com/blog/comet-prompt-injection/ ; https://www.securityweek.com/google-fortifies-chrome-agentic-ai-against-indirect-prompt-injection-attacks/
- **Threat Actors:** None known. No specific APT, ransomware, or named campaign has been publicly attributed to exploitation of Chrome's Gemini agentic capabilities. Closest observations include Unit 42's reports (Dec 2025) of web-based indirect prompt injection in the wild targeting ad-review and content-moderation agents, and Noma Labs' researcher-discovered 'GeminiJack' zero-click bug — all without identified threat actors.
- **Mitigation:** User-side: (1) leave Gemini in Chrome agentic capabilities disabled unless required, or only enable on trusted sites; (2) update Chrome to the latest Stable channel; (3) do not auto-confirm agent prompts for consequential actions (banking/medical/login/payment); (4) restrict Chrome extensions that request broad permissions plus tab/Gemini access; (5) treat iframes and UGC-heavy sites as untrusted input to the agent. Vendor-side defenses Google ships for Gemini in Chrome: a User Alignment Critic model that vets proposed actions against the user's stated goal; Agent Origin Sets with augmented Site Isolation constraining the agent to specific origins via a gating function; mandatory user confirmations for sensitive actions (banking, medical, password manager sign-in, payments, messaging); a real-time prompt-injection classifier running alongside Gemini, with parallel coverage from Chrome Safe Browsing and on-device AI; 'Spotlighting' to train the model to prioritize user/system instructions over page content; and continuous automated red-teaming. The Chrome VRP now explicitly lists indirect prompt injection enabling unsanctioned payments, account deletion, or significant data exposure as in-scope.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** An out-of-bounds / incorrect-bounds-check (linear buffer overflow) in the CrabbyAVIF AVIF parser/decoder that can lead to memory corruption and potentially remote code execution when processing crafted AVIF images.
- **Affected Products:** Android System (CrabbyAVIF AVIF parser/decoder), affects Android 16 / security patch level Aug 2025
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true — https://source.android.com/docs/security/bulletin/2025-08-01
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the Android August 2025 security update (install the Android security patch level referenced in the August 2025 bulletin). If a patch cannot be applied immediately, avoid or restrict processing of untrusted AVIF images and blocks parsing of untrusted media where feasible.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI): attackers embed hidden/malicious instructions inside external data sources (emails, documents, calendar invites, web content) that an LLM-based assistant ingests; when the assistant incorporates that external content into its prompt, the hidden instructions can coerce the model to disclose sensitive data or perform unauthorized actions.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses — e.g. prompt-injection content classifiers, security-thought reinforcement, markdown/content sanitization, suspicious-link handling, input validation/sanitization, least-privilege access controls, logging/monitoring and human review.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors target and compromise backbone, provider-edge (PE) and customer-edge (CE) routers and other network-edge devices; they leverage compromised devices and trusted connections to pivot into other networks and modify routers to maintain persistent, long-term access.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Harden and restrict management interfaces, apply strict ACLs and least-privilege for router administrative access, disable unused features (e.g., guestshell) or apply strict hardening if required, segment networks to limit pivoting, deploy detection/monitoring (use STIX IOCs/detection tips), and apply vendor guidance/patches when published.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 11. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 12. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

---

## 13. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 14. 🟡 High Severity — mknod: Device nodes created mislabeled on SELinux, with broken cleanup (remove_dir on a node)

**CVE:** `CVE-2026-35361` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-r9hw-mj3w-phcq>

> uutils calls `mknod` *before* setting the SELinux context (GNU uses `setfscreatecon` first, labeling atomically). If `set_selinux_security_context` fails, cleanup uses `std::fs::remove_dir`, which cannot remove device nodes or FIFOs, leaving the mislabeled node behind.

**Impact:** on SELinux-enforcing systems the node is created with the wrong context; the command reports failure but leaves a mis…

---

## 15. 🟡 High Severity — mkfifo: permissions of an existing file are changed after FIFO creation fails

**CVE:** `CVE-2026-35341` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-pmf6-rcx4-v53v>

> When `mkfifo()` fails (e.g. target already exists), the code shows an error but is missing a `continue;`, so it falls through to `fs::set_permissions` and changes the permissions of the pre-existing file to the default FIFO mode (`0o666` &amp; umask -&gt; `0644`).

```
$ touch secret; chmod 000 secret
$ coreutils mkfifo secret fifo3 fifo4
mkfifo: cannot create fifo &#x27;secret&#x27;: File exists
…

---

## 16. 🟡 High Severity — 9routers has Exposure of Sensitive Information and Unprotected Database Import/Export, Allowing Complete Credential Theft and Database Takeover

**CVE:** `CVE-2026-55500` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-qvfm-67h2-2qfx>

> ## Summary

The `/api/settings/database` endpoint allows full database export (containing all credentials, API keys, OAuth tokens, and settings) and full database import (complete overwrite) without any authentication requirement beyond the `ALWAYS_PROTECTED` middleware check, which only validates JWT or CLI token. Combined with other vulnerabilities (e.g., default password, tunnel exposure), this…

---

## 17. 🟡 High Severity — Craft CMS: Potential authenticated Remote Code Execution via referrer redirect

**CVE:** `CVE-2026-55794` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-f74w-488g-8x5r>

> ### Requirements:

* Control panel access
* Permissions to edit an entry

### Details

Control panel users with the ability to edit entries can execute unsandboxed Twig code via the HTTP Referrer header.

The issue happens when a user is saving entries. Strings for a signed redirect URL are being compiled as a Twig template via `renderObjectTemplate()`, and while a sandboxed alternative already ex…

---

## 18. 🟡 High Severity — Linuxfabrik Monitoring Plugins have local privilege escalation using embedded command

**CVE:** `CVE-2026-55426` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-798h-hpph-m24j>

> ### Summary
When a check plugin places user provided input inside a command which is passed to `shell_exec`, an attacker can abuse this to run arbitrary commands. This is mainly dangerous for plugins which are listed in the sudoers file, because this allows an attacker controlling the nagios user to get root privileges.

### Details
An example for this is the `restic-check` plugin, where the `--re…

---

## 19. 🟡 High Severity — Suspended Coder users retain access to AI Bridge LLM proxy endpoints

**CVE:** `CVE-2026-55435` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-wqxv-w64v-5wh6>

> ### Summary

AI Bridge proxy endpoints authenticate via `Server.IsAuthorized` in `coderd/aibridgedserver`, which validates key format, expiry, secret and deleted or system users but does not check whether the account is suspended. Because suspension does not revoke existing API keys, a suspended user&#x27;s unexpired token keeps working.

&gt; **Note:** Practical impact is limited to already-issue…

---

## 20. 🟡 High Severity — Coder: Devcontainer recreate endpoint missing write authorization allows read-only roles to destroy containers

**CVE:** `CVE-2026-55433` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-jqj2-x4c5-jfxm>

> ### Summary

The devcontainer recreate endpoint relied on route middleware that checked only `ActionRead` on the workspace and, unlike the sibling delete endpoint, performed no `ActionUpdate` check before triggering the destructive rebuild.

&gt; **Note:** Exploitation requires an existing low-privilege role with access to the target workspace.

### Impact

Any authenticated principal with read-on…

---

## 21. 🟡 High Severity — Coder: User-admin role can reset owner account password

**CVE:** `CVE-2026-55077` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-29xf-69gq-m9jx>

> ### Summary

The `PUT /api/v2/users/{user}/password` endpoint authorized only `ActionUpdatePersonal` and did not prevent a `user-admin` from resetting an `owner` account&#x27;s password. It also did not require the current password when an admin reset another user&#x27;s password.

&gt; **Note:** Exploitation requires the privileged `user-admin` role so practical risk is limited to deployments tha…

---

## 22. 🟡 High Severity — Coder vulnerable to OIDC account takeover via email-based user matching and email_verified bypass

**CVE:** `CVE-2026-55075` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-9r87-mvcw-x35f>

> ### Summary

Two flaws in Coder&#x27;s OIDC login chained into account takeover: email-based user matching fell back to linking by email without checking for an existing link to a different IdP subject and the `email_verified` claim was only enforced when present as a boolean `false` so an absent or non-boolean claim was treated as verified.

### Impact

An attacker who could authenticate at the c…

---

## 23. 🟡 High Severity — Coder's OIDC email_verified type coercion bypass enables account takeover via unverified email linking

**CVE:** `CVE-2026-55076` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-75vm-6w67-gwvp>

> ### Summary

Coder&#x27;s OIDC callback checked `email_verified` with a direct Go `bool` type assertion. When an IdP returned the claim as a non-boolean (for example the string `&quot;false&quot;`) or omitted it, the assertion failed open and the email was treated as verified. Combined with an unconditional email-based account fallback, this enabled account takeover.

### Impact

An attacker who r…

---

## 24. 🟡 High Severity — OpenRemote has Cross-Realm User Information Disclosure in UserResourceImpl

**CVE:** `CVE-2026-54641` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-xqr9-4wvv-gvch>

> ### Summary

A realm admin of tenant B can read the profile, client roles, and realm roles of any user in any other realm (including the master realm) by supplying the target user&#x27;s UUID in the REST API path. Three read endpoints in UserResourceImpl check whether the caller holds the read:admin role but omit a check that the target user belongs to the caller&#x27;s own realm. The vulnerabilit…

---

## 25. 🟡 High Severity — GoFiber never set HSTS header in helmet middleware due to incorrect protocol check

**CVE:** `CVE-2026-53624` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-gv83-gqw6-9j2c>

> ### Summary

The `helmet` middleware in gofiber/fiber never sets the `Strict-Transport-Security` (HSTS) response header, even when `HSTSMaxAge` is explicitly configured, because the condition check at `helmet.go:67` uses `c.Protocol()` — which returns the HTTP protocol version string (e.g., `&quot;HTTP/1.1&quot;`, `&quot;HTTP/2.0&quot;`) — instead of `c.Scheme()` — which returns the URL scheme (`&…

---

## 26. 🟡 High Severity — Langroid: handle_message() executes user-supplied tool JSON without sender verification 

**CVE:** `CVE-2026-54771` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-gjgq-w2m6-wr5q>

> ## Summary

A Langroid application exposing a chat interface to untrusted users may allow direct tool invocation via raw JSON payloads, even when tools are registered with `use=False, handle=True`.

## Details

`enable_message(..., use=False, handle=True)` only prevents the LLM from being instructed to generate the tool. The tool dispatch path in `agent_response()` → `handle_message()` → `get_tool…

---

## 27. 🟡 High Severity — Dragonfly scheduler v1 and v2 gRPC unauthenticated SSRF via attacker-controlled PeerHost in DownloadTinyFile

**CVE:** `CVE-2026-54637` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-chwm-m7g7-685g>

> ## Summary

The Dragonfly **scheduler**&#x27;s v1 gRPC service contains an unauthenticated Server-Side Request Forgery (SSRF). When a peer reports a successful download of a TINY task, the scheduler calls `Peer.DownloadTinyFile()` and issues an HTTP `GET` to a host and port taken verbatim from the attacker-controlled `PeerHost.Ip` / `PeerHost.DownPort` fields of the gRPC request body. The HTTP cli…

---

## 28. 🟡 High Severity — Decompress: Archive extraction can create files and links outside of the target directory

**CVE:** `CVE-2026-53486` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-mp2f-45pm-3cg9>

> ### Impact

When extracting an archive to a directory, a crafted archive can read or write files outside that directory. The flaw is in the code that writes the parsed entries, so it affects every format decompress handles: tar, tar.gz, tar.bz2, and zip by default, plus any others added through the plugins option.

A link (hardlink) or symlink entry is created without checking where its target poi…

---

## 29. 🟡 High Severity — mv: symlinks expanded during cross-device move (resource exhaustion / data duplication)

**CVE:** `CVE-2026-35365` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-h444-6j9x-p8vh>

> When moving directories across filesystems, uutils `mv` dereferences symlinks inside the tree, copying their targets as real files/dirs instead of preserving the symlinks. GNU preserves symlinks by default. E.g. a `etc_link -&gt; /etc` inside the source becomes a full copy of `/etc` at the destination.

**Impact:** (1) resource exhaustion — a small tree can expand into a huge copy (time/disk DoS);…

---

## 30. 🟡 High Severity — id: groups= computed from real GID instead of effective GID

**CVE:** `CVE-2026-35370` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-47c7-qrm7-mqw7>

> The id utility in uutils coreutils miscalculates the groups= section of its output. The implementation uses a user&#x27;s real GID instead of their effective GID to compute the group list, leading to potentially divergent output compared to GNU coreutils. Because many scripts and automated processes rely on the output of id to make security-critical access-control or permission decisions, this dis…

---

## 31. 🟡 High Severity — install: TOCTOU symlink race (unlink-then-create without O_EXCL) allows arbitrary file overwrite

**CVE:** `CVE-2026-35355` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-239g-2685-54x3>

> `copy_file` in `install/src/install.rs` removes the destination then recreates it by pathname via `File::create` / `fs::copy` without `O_EXCL`/`create_new`. Between the unlink and the recreate, a local attacker with write access to the destination directory can drop in a symlink and redirect the write.

**Impact:** when `install` runs privileged into an attacker-writable directory (staging/build p…

---

## 32. 🟡 High Severity — ln: rejects non-UTF-8 source filenames in target-directory mode

**CVE:** `CVE-2026-35373` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-jcjr-rh8q-7xqf>

> In target-directory forms (`ln SOURCE... DIRECTORY`), `ln` rejects source paths with non-UTF-8 filename bytes, while GNU accepts them. Breaks GNU compatibility for byte-oriented filenames on Unix filesystems.

PoC:
```
name=$(printf &#x27;bad_\377&#x27;); mkdir dst; : &gt; &quot;$name&quot;; ln &quot;$name&quot; dst
# GNU: exit 0, creates dst/bad_\377 ; uutils: exit 1, dst empty
```

---
_Zellic p…

---

## 33. 🟡 High Severity — chmod: --preserve-root bypassed by any path that resolves to root (e.g. /../)

**CVE:** `CVE-2026-35338` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-4c7q-4928-8445>

> `Chmoder::chmod()` only compares the literal argument against `Path::new(&quot;/&quot;)`, so the `--preserve-root` guard is bypassed by any path that *resolves* to root — a symlink to `/` or simply `/../`.

```
if self.recursive &amp;&amp; self.preserve_root &amp;&amp; file == Path::new(&quot;/&quot;) {
    return Err(ChmodError::PreserveRoot(&quot;/&quot;.to_string()).into());
}
```

**PoC** — re…

---

## 34. 🟡 High Severity — 16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems

**CVE:** `CVE-2026-53359` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://thehackernews.com/2026/07/16-year-old-linux-kvm-flaw-lets-guest.html>

> A use-after-free bug in Linux&#x27;s KVM hypervisor can be triggered from a guest virtual machine to corrupt the shadow-page state of the host kernel that runs it.

Dubbed &#x27;Januscape&#x27; and tracked as CVE-2026-53359, the flaw sits in the shadow MMU code that KVM shares across both Intel and AMD. The public proof-of-concept panics the host; the researcher claims that a separate, unreleased …

---

## 35. 🟡 High Severity — flyto-core has SSRF guard bypass via IPv6 transition addresses (IPv4-mapped / 6to4 / NAT64) in validate_url_ssrf

**CVE:** `CVE-2026-55787` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-794r-5rp2-fpg8>

> ## Summary

`flyto-core`&#x27;s SSRF protection (`validate_url_ssrf` / `is_private_ip` in `src/core/utils.py`) blocks private and metadata destinations by resolving the host and testing the resulting IP for membership in a hardcoded `PRIVATE_IP_RANGES` list. That list contains only the *native* RFC 1918 / loopback / link-local / unique-local ranges. It does **not** account for IPv6 transition addr…

---

## 36. 🟡 High Severity — Cilium vulnerable to sensitive information disclosure and cluster disruption via local Envoy admin socket access

**CVE:** `CVE-2026-49445` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-3fcv-jvfp-m4q9>

> ### Impact

When Cilium L7 functionality is enabled on a cluster, the Envoy instance supporting this functionality creates a world-accessible socket on cluster nodes. A local attacker would be able to access Envoy admin endpoints. Depending on deployment configuration, this can expose sensitive information or allow disruptive administrative operations, such as:

- Exposing TLS secrets
- Disrupting…

---

## 37. 🟡 High Severity — Formie Hidden field defaults vulnerable to Server-Side Template Injection

**CVE:** `CVE-2026-52889` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-565m-g33j-jq96>

> ## Summary
Formie Hidden fields could evaluate request-derived values as Twig during front-end form rendering.

When a Hidden field used a dynamic default value such as HTTP User Agent, Referer URL, Current URL, Query Parameter, or Cookie Value, the value was copied from the incoming request and later passed to Craft’s Twig rendering layer. This allowed an unauthenticated attacker to provide Twig …

---

## 38. 🟡 High Severity — Threat Actors Probe Gitea Docker Flaw CVE-2026-20896 13 Days After Disclosure

**CVE:** `CVE-2026-20896` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://thehackernews.com/2026/07/threat-actors-probe-gitea-docker-flaw.html>

> Threat actors have been observed attempting to exploit a recently patched critical security flaw in Gitea Docker images, according to Sysdig.

The vulnerability in question is CVE-2026-20896 (CVSS score: 9.8), a vulnerability that stems from the DevOps platform trusting the &quot;X-WEBAUTH-USER&quot; header from any source IP address, effectively allowing an unauthenticated internet client to get …

---

## 39. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
