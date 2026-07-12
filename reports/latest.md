# Zero Day Pulse

> **Generated:** 2026-07-12 07:58 UTC &nbsp;|&nbsp; **Total:** 13 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path traversal vulnerability (CWE-22) in the SimpleHelp remote support web server. Unauthenticated remote attackers can send specially crafted HTTP requests containing directory traversal sequences (e.g., '..\\') in URL path components to download arbitrary files from the underlying host. The primary target is the server configuration file (serverconfig.xml / SimpleHelp.xml), which contains hashed admin passwords and secrets such as LDAP credentials, OIDC client tokens, and TOTP seeds. With the cracked admin hash, an attacker can authenticate and chain CVE-2024-57726 (privilege escalation to admin) and CVE-2024-57728 (arbitrary file upload via zip-slip) to achieve full remote code execution on the SimpleHelp server, then pivot to managed endpoints. The vulnerability is network-exploitable with no privileges or user interaction required; attack complexity is low, and confidentiality impact is high while integrity and availability impact are none at the primitive level.
- **Affected Products:** SimpleHelp Remote Support / Remote Monitoring and Management (RMM) software, versions 5.5.7 and all earlier releases.
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Yes. A public proof-of-concept exploit is available at https://github.com/imjdl/CVE-2024-57727 (Python script poc.py that probes a target for the path traversal flaw). Working exploit code has also been published by Horizon3.ai (Naveen Sunkavally) and referenced in OffSec's write-up.
- **Patch Available:** Yes. SimpleHelp released patched versions 5.5.8, 5.5.9, and 5.5.10 between January 8-13, 2025 to remediate CVE-2024-57727 (along with CVE-2024-57726 and CVE-2024-57728). Any SimpleHelp instance running version 5.5.7 or earlier is vulnerable; upgrading to 5.5.8+ fully addresses the issue. Advisory: https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know and https://guides.simple-help.com/kb---security-vulnerabilities-01-2025
- **Active Exploitation:** Yes — confirmed active exploitation in the wild. CISA added CVE-2024-57727 to the Known Exploited Vulnerabilities (KEV) Catalog on February 13, 2025, with a remediation due date of March 6, 2025. CISA Advisory AA25-163A (June 12, 2025) documents ransomware actors leveraging unpatched SimpleHelp RMM instances since January 2025 to compromise a utility billing software provider and its downstream customers using double-extortion tactics. The vendor (SimpleHelp) and Horizon3.ai both report that the DragonForce and Medusa ransomware groups have been observed exploiting these chained vulnerabilities, particularly against Managed Service Provider (MSP) environments.
- **Threat Actors:** DragonForce ransomware group and Medusa ransomware group. CISA Advisory AA25-163A (June 12, 2025) attributes the activity to unnamed 'ransomware actors' leveraging CVE-2024-57727 against unpatched SimpleHelp RMM instances since January 2025.
- **Mitigation:** Primary remediation: upgrade SimpleHelp to version 5.5.8 or later (patched versions 5.5.8 through 5.5.10 were released between January 8-13, 2025; latest 5.5.x is recommended). If patching is not immediately possible: (1) remove SimpleHelp servers from public internet exposure and place them behind a VPN or restrict access to trusted technician IPs; (2) use strong, unique passwords for admin and technician accounts that resist hash cracking; (3) audit SimpleHelp servers for signs of compromise (unfamiliar technician accounts, modified access control settings, unexpected deployed scripts, suspicious file uploads); (4) monitor for IOCs listed in CISA Advisory AA25-163A; (5) apply network segmentation to prevent a compromised RMM host from reaching production or OT environments.
- **Vendor Advisory:** https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — 'Ghostcommit' hides prompt injection in images to fool AI agents, steal secrets

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-07-11
**Reference:** <https://www.bleepingcomputer.com/news/security/ghostcommit-hides-prompt-injection-in-images-to-fool-ai-agents-steal-secrets/>

> A PNG hiding a prompt injection could steal your repo&#x27;s secrets, researchers demonstrate. The technique, dubbed &#x27;Ghostcommit,&#x27; slipped past AI code reviewers CodeRabbit and Bugbot, which never open image files at all, then convinced a coding agent to read a repo&#x27;s .env and write every secret into the code as a list of numbers. [...]

**Parallel AI Enrichment:**

- **Technical Details:** An attacker commits a PNG image to a pull request whose pixel data, metadata, or steganographic payload encodes an indirect prompt-injection instruction. AI code reviewers CodeRabbit and Bugbot only analyze source-code diffs and ignore attached images, so the malicious instruction is never reviewed. A separate coding agent that does render the image reads the embedded instruction and is told to read the repository's .env file and write every secret into the source tree (for example, as a comma-separated list of integers). The agent commits the change, exfiltrating secrets through a seemingly benign code modification.
- **Affected Products:** AI code-review bots CodeRabbit and Bugbot; downstream AI coding agents that ingest multimodal pull-request content (e.g., Cursor and Claude Code-style agents).
- **CVSS Score:** 6.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit or PoC repository was published. The technique is described in the BleepingComputer article (https://www.bleepingcomputer.com/news/security/ghostcommit-hides-prompt-injection-in-images-to-fool-ai-agents-steal-secrets/) and OffSeq Radar entry, but researchers demonstrated it only against their own test repositories.
- **Patch Available:** No official vendor patch has been published. The disclosure targets a class of behavior in AI-assisted development tools rather than a versioned CVE, so remediation requires operator-side configuration changes (see mitigation).
- **Active Exploitation:** No confirmed in-the-wild exploitation has been reported. The technique was demonstrated by researchers against their own test repositories and AI code-review bots (CodeRabbit, Bugbot); no real-world attacks have been documented as of the BleepingComputer publication on 2026-07-11.
- **Threat Actors:** None known.
- **Mitigation:** Disable or sandbox multimodal image input for AI coding agents and code-review bots so they cannot read PNG/JPEG attachments in pull requests; strip or sanitize image metadata and steganographic payloads from committed assets; restrict autonomous coding agents from reading .env, secrets/, or other sensitive files (filesystem ACLs); require human-in-the-loop review for any change introducing numeric or encoded constants that could be exfiltrated data; enable and monitor secret-scanning (GitHub/GitLab secret scanning, gitleaks, trufflehog) to detect exfiltrated secrets landed in commits; rotate any secrets that may have been exposed.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is a class of attack against LLM-based applications where adversarial instructions are embedded inside external content (websites, emails, documents) that the AI ingests as part of its task. When the model processes the content, the hidden instructions can cause it to silently follow the attacker's commands instead of the user's original intent. Observed real-world outcomes include sensitive data exfiltration (emails, documents, credentials) and destructive actions (mass deletion of calendar events, files, or emails). Attackers use techniques such as HTML/CSS hiding, obfuscation, authority spoofing (impersonating system prompts), role impersonation, and conditional LLM targeting (e.g., 'if you are an AI...').
- **Affected Products:** Gemini (Google's AI assistant, including Gemini in Workspace apps); any LLM-powered application that ingests untrusted external content (web pages, emails, documents)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes. Public proof-of-concept resources include Greshake's IPI research (https://greshake.github.io/) and the 'PayloadsAllTheThings' Prompt Injection cheat sheet (https://swisskyrepo.github.io/PayloadsAllTheThings/Prompt%20Injection/). Forcepoint X-Labs additionally documented 10 verified live IPI payloads on real-world websites covering financial fraud, data destruction, denial-of-service, and data exfiltration.
- **Patch Available:** No single vendor patch is associated with this advisory. Google states it is continuously hardening Gemini models, conducting dedicated red-team pressure testing, and operating an AI Vulnerability Reward Program (https://bughunters.google.com/) for researcher submissions. Defensive improvements are rolled out continuously rather than as a single patch.
- **Active Exploitation:** Yes - confirmed active exploitation in the wild. Google's Threat Intelligence team observed IPI attempts across all five intent categories after analyzing web content indexed by Common Crawl, including data exfiltration and destructive actions. Google reports a ~32% relative increase in malicious-category IPI between November 2025 and February 2026. Forcepoint X-Labs (April 22, 2026) independently documented 10 verified live IPI payloads on real-world websites spanning financial fraud, data destruction, denial-of-service, and data exfiltration. Zscaler and other vendors have likewise observed in-the-wild IPI activity targeting AI agents.
- **Threat Actors:** None known
- **Mitigation:** Google's layered defense for Gemini includes: (1) proprietary ML-based prompt-injection classifiers that filter malicious instructions in ingested content; (2) system-prompt reinforcement that nudges the model to prioritize user-directed tasks over adversarial instructions; (3) markdown sanitization to strip harmful scripts/HTML; (4) Suspicious URL Redaction backed by Google Safe Browsing to block links to known malicious destinations; (5) a User Confirmation Framework (human-in-the-loop) requiring explicit user approval before risky actions (e.g., deleting events, sharing sensitive data) or interactions with untrusted content; (6) end-user security notifications when risk is detected or mitigated; (7) adversarial-robustness hardening via dedicated red teams. For developers building LLM agents, OWASP additionally recommends input/output filtering, least-privilege tool scoping, strict separation between untrusted external content and system/instructions, and structured output handling.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is a variant of prompt injection where an attacker embeds hostile natural-language instructions inside external content (web pages, emails, documents, calendar items) that a generative-AI application later retrieves and processes. When a user invokes an AI feature such as 'Summarize this email' or 'Help me write,' the LLM receives both the user's prompt and the attacker's hidden instructions in the same context window. The injected instructions can override the user's intent, causing the model to exfiltrate data, generate phishing content, perform agentic actions (send email, execute code, process payments), or alter outputs. Unlike direct prompt injection, the user does not need to type anything—the malicious payload rides in on data the AI ingests. Workspace with Gemini features that consume untrusted content (Gmail summaries, Docs helpers, Drive search) are specifically exposed because Gemini retrieves and processes untrusted external content.
- **Affected Products:** Google Workspace with Gemini (Gemini in Gmail, Docs, Drive, Chat, and Search); the standalone Gemini app; and broadly any LLM-based or agentic AI application that ingests untrusted external content (web pages, email, documents). No specific version numbers were disclosed.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes. Public PoCs and in-the-wild exploit payloads exist: (1) 0din.ai 'Phishing For Gemini' (submission 0xE24D9E6B, July 10, 2025) demonstrating IPI via hidden HTML/CSS in emails processed by Gemini for Workspace; (2) HiddenLayer 'New Gemini for Workspace Vulnerability' (September 25, 2024) enabling phishing-content manipulation; (3) Forcepoint X-Labs catalog of 10 live IPI payloads on public sites (thelibrary-welcome[.]uk, bentasker[.]co[.]uk, kassoon[.]com, faladobairro[.]com, perceptivepumpkin[.]com, lawsofux[.]com, lcpdfr[.]com, archibase[.]co).
- **Patch Available:** No discrete vendor patch is published. Indirect prompt injection is treated as an evolving threat class addressed through continuous improvements to the Gemini model and Workspace with Gemini service rather than a single fix. Keep Workspace with Gemini and the Gemini app updated to the latest release to receive ongoing mitigations. Reference: https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/ and the Workspace admin guide https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini
- **Active Exploitation:** Yes — confirmed in-the-wild exploitation. Forcepoint X-Labs (April 22, 2026) identified 10 live IPI payloads on public websites with intents ranging from API-key theft, content-suppression DoS, traffic/SEO hijacking, destructive commands (sudo rm -rf), PayPal/Stripe payment fraud, and donation fraud. Google's companion April 23, 2026 post 'AI threats in the wild' reports a 32% increase in observed malicious prompt-injection activity between November 2025 and February 2026. Independent PoCs targeting Gemini for Workspace specifically include HiddenLayer (September 25, 2024) and 0din.ai 'Phishing For Gemini' (July 10, 2025, submission 0xE24D9E6B), both demonstrating working exploitation.
- **Threat Actors:** None known
- **Mitigation:** Google's layered defense-in-depth strategy for Gemini and Workspace with Gemini includes: (1) Deterministic defenses — centralized Policy Engine enforcing user confirmation prompts, URL sanitization, and tool-chaining allowlists; (2) ML-based defenses — retraining Gemini on synthetic IPI examples to improve robustness; (3) LLM-based defenses — refined system instructions and security thought reinforcement so the model disregards or flags malicious instructions in retrieved data; (4) Model hardening — improving Gemini's intrinsic ability to identify and ignore harmful context; (5) Content classifiers that detect suspicious inputs; (6) Markdown sanitization and suspicious URL redaction in rendered outputs; (7) End-user security-mitigation notifications surfacing potentially risky AI behavior; (8) User-confirmation framework gating sensitive agentic actions. For administrators and users: keep Workspace with Gemini and the Gemini app updated to the latest release, prefer deployments with admin-controlled data boundaries, enable audit logging, and require human confirmation for any agentic action (send mail, file operations, payments). Refer to the Workspace admin guide: https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection against Chrome's on-device Gemini-powered agentic browsing capabilities. Attacker-controlled web content (malicious sites, third-party iframes, user-generated content) can embed prompts that hijack the agent's planning model and redirect it from the user's intended task to attacker-chosen actions (e.g., unauthorized transactions, data exfiltration, cross-origin actions). Google's layered defenses: (1) spotlighting/training to prioritize user/system instructions over page content; (2) User Alignment Critic — an isolated Gemini model that only sees action metadata and vets each proposed action; (3) Agent Origin Sets extending Site Isolation to restrict the agent to task-relevant origins; (4) mandatory user confirmation for high-consequence actions; (5) on-device prompt-injection detection alongside Safe Browsing and scam detection; (6) continuous automated red-teaming with auto-update push of new defenses.
- **Affected Products:** Google Chrome with Gemini in Chrome and agentic capabilities (no specific version numbers enumerated in the post)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit published in connection with this specific blog post
- **Patch Available:** The defensive architecture is being shipped as part of the Gemini-in-Chrome / agentic browsing rollout itself (no standalone CVE or patch advisory); ongoing refinements are delivered via Chrome's standard auto-update channel. Primary advisory URL: http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** No confirmed in-the-wild exploitation reported in connection with this blog post. The post treats indirect prompt injection as an emerging threat class and proactively deploys defenses; it does not disclose a specific exploitation campaign.
- **Threat Actors:** None known
- **Mitigation:** Layered mitigations built into the agentic browsing architecture: (a) User Alignment Critic vetoes actions misaligned with the user's stated goal; (b) Agent Origin Sets confine the agent to task-relevant origins, blocking arbitrary cross-origin lateral movement and data exfiltration; (c) mandatory user-confirmation UI for high-consequence actions (purchases, email sends, calendar edits, password-manager sign-ins); (d) on-device prompt-injection classifiers running alongside Safe Browsing and on-device scam detection to block injection attempts in real time; (e) continuous automated red-teaming with rapid auto-update push of new defenses. Users should keep Chrome updated and carefully review any confirmation prompts surfaced by Chrome before approving sensitive agentic actions.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** The blog post is informational about Android's Rust adoption for memory safety, reporting a 1000x reduction in memory safety vulnerability density vs C/C++ and memory safety vulnerabilities falling below 20% of total vulnerabilities in 2025. It references CVE-2025-48530 (CrabbyAVIF AVIF parser/decoder) as a near-miss involving out-of-bounds accesses in NV12 YUV planes, alpha plane, and chroma width calculations, which was caught before public release and rendered non-exploitable by the Scudo hardened allocator.
- **Affected Products:** Android platform (general); CrabbyAVIF AVIF parser/decoder (referenced as CVE-2025-48530 near-miss, no specific versions listed in blog post)
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit available. CVE-2025-48530 referenced in the post was caught internally before public release and was rendered non-exploitable by the Scudo hardened allocator.
- **Patch Available:** CVE-2025-48530 was fixed before public release. For general Android vulnerabilities, patches are available through the Android Security Bulletin (November 2025 and later).
- **Active Exploitation:** No confirmed active exploitation in the wild reported. CVE-2025-48530 referenced in the post was caught before public release and was non-exploitable due to the Scudo hardened allocator.
- **Threat Actors:** None known
- **Mitigation:** Apply the latest Android security patches (November 2025 security patch level or later). The Scudo hardened allocator serves as a runtime mitigation for memory safety issues in Rust components. Continue adoption of memory-safe languages (Rust) for new code development.
- **Vendor Advisory:** https://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is an attack class in which an adversary embeds hidden or contextual instructions inside content that an AI assistant later ingests as data—for example, emails, Google Docs files, Drive items, Calendar invites, or third-party web pages summarized by Gemini. Because LLMs process retrieved text and system/user instructions with similar priority, the injected instructions can redirect the model into leaking user data, modifying outputs, or invoking connected tools/agents (search, browsing, Workspace actions) on the victim's behalf. Google's June 13, 2025 blog frames why conventional mitigations are insufficient and describes the layered defense deployed across the Gemini app and Gemini in Workspace.
- **Affected Products:** Google Gemini app; Gemini in Google Workspace (Gmail, Google Docs editors, Google Drive, Google Chat); Gemini 2.5 models. Indirect prompt injection is an attack class rather than a version-specific vulnerability, so no version ranges are published.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC is referenced in the Google blog post itself. However, several public demonstrations/PoCs of indirect prompt injection against Gemini products have been published by independent researchers: (1) Miggo Security - calendar-invite semantic attack on Gemini (Jan 2026): https://www.miggo.io/post/weaponizing-calendar-invites-a-semantic-attack-on-google-gemini; (2) 0Din/Tracebit - hidden-text email prompt injection 'Phishing for Gemini' (Jul 2025): https://0din.ai/blog/phishing-for-gemini; (3) Tracebit - Gemini CLI prompt-injection/code-execution hijack (Jul 2025): https://tracebit.com/blog/code-exec-deception-gemini-ai-cli-hijack; (4) Tenable - 'Trifecta' Gemini vulnerabilities in Cloud Assist, Search and Browsing (Sep 2025): https://www.tenable.com/blog/the-trifecta-how-three-new-gemini-vulnerabilities-in-cloud-assist-search-model-and-browsing.
- **Patch Available:** No discrete vendor patch is associated with this disclosure. Mitigations are deployed as rolling updates to Gemini 2.5 model weights and to the Gemini app / Gemini in Workspace pipeline. Updated Gemini 2.5 models with adversarial-training hardening were referenced as available at the time of the post. Separately reported, discrete Gemini prompt-injection issues (Miggo calendar-invite bypass, Tenable Trifecta, 0Din/Tracebit phishing) have received targeted fixes from Google — see the linked researcher reports.
- **Active Exploitation:** The Google blog states that real-world attack examples were used to train new classifiers and that Gemini's built-in defenses have already stopped attacks, but it does not attribute activity to any named threat actor or confirm a specific in-the-wild campaign. Independent researchers have publicly demonstrated exploitation against Gemini products (Miggo, 0Din/Tracebit, Tenable), and Palo Alto Networks' Unit 42 has documented web-based indirect prompt injection observed in the wild targeting LLM agents.
- **Threat Actors:** None known
- **Mitigation:** Google's layered defense for indirect prompt injection, as described in the June 13, 2025 blog post: (1) Model-level hardening via adversarial training of Gemini 2.5 against indirect prompt injection; (2) Purpose-built ML classifiers that detect and flag prompt-injection content in emails, documents, and other retrieved data; (3) 'Security thought reinforcement' – system-level instructions reminding the model to ignore adversarial content in retrieved data; (4) Markdown sanitization and suspicious-URL redaction (external image URLs are blocked and links are routed through google.com and Google Safe Browsing); (5) Human-in-the-loop confirmation requiring user approval before sensitive actions such as deleting Calendar events; (6) End-user security notifications alerting users when a prompt-injection defense has been triggered. Workspace administrators should review Google's admin guidance at https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini, keep Gemini features enabled (mitigations are on by default), and ensure user confirmation prompts are not bypassed. End users should treat Gemini summaries/actions over untrusted content with caution and confirm any sensitive tool actions explicitly.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/ (mirror: http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html)

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors exploit publicly known, previously disclosed vulnerabilities in edge networking devices (routers, VPN gateways, firewalls) — specifically targeting large backbone routers of major telecommunications providers as well as provider-edge (PE) and customer-edge (CE) routers. Referenced CVEs include CVE-2024-21887 (Ivanti Connect Secure/Policy Secure command injection, often chained with CVE-2023-46805 authentication bypass), CVE-2024-3400 (Palo Alto PAN-OS GlobalProtect arbitrary file creation leading to unauthenticated RCE), CVE-2023-20273 / CVE-2023-20198 (Cisco IOS XE Web UI command injection and authentication bypass, chained to create unauthorized local accounts), and CVE-2018-0171 (Cisco IOS/IOS XE Smart Install RCE). Post-exploitation: actors modify router configurations and ACLs (e.g., naming their ACLs 'access-list 20') to permit traffic from attacker-controlled IPs; enable GRE/IPsec tunnels and static routes for command-and-control and data exfiltration; use on-box virtualized Linux containers (e.g., Cisco Guest Shell / IOx) as evasion footholds; capture TACACS+ traffic on TCP/49 to steal administrator credentials; and enable services such as Cisco's sshd_operns to obtain root-level access. They also compromise mail servers and administrator accounts to monitor defensive response and pivot into additional networks via trusted provider-to-provider/provider-to-customer connections.
- **Affected Products:** Cisco IOS and IOS XE (routers, including Smart Install feature and Web Management Interface); Ivanti Connect Secure (9.x, 22.x) and Ivanti Policy Secure (9.x, 22.x); Palo Alto Networks PAN-OS with GlobalProtect feature; Fortinet firewalls; Juniper firewalls; Microsoft Exchange; Nokia routers/switches; Sierra Wireless devices; SonicWall firewalls. Specific affected versions are tied to individual CVEs: CVE-2024-21887 / CVE-2023-46805 (Ivanti Connect Secure 9.x, 22.x and Policy Secure 9.x, 22.x); CVE-2024-3400 (Palo Alto PAN-OS 11.x with GlobalProtect); CVE-2023-20273 / CVE-2023-20198 (Cisco IOS XE Web UI); CVE-2018-0171 (Cisco IOS/IOS XE Smart Install).
- **CVSS Score:** 1.0
- **CVSS Vector:** CVSS vector unavailable. AA25-239A is an aggregate campaign/threat-activity advisory referencing multiple CVEs (CVE-2024-21887, CVE-2024-3400, CVE-2023-46805, CVE-2023-20273, CVE-2023-20198, CVE-2018-0171). Individual CVSS v3 vectors are published in each CVE's NVD entry (https://nvd.nist.gov/).
- **Exploit Available:** Yes. Active exploitation confirmed by CISA (AA25-239A) for CVE-2024-21887, CVE-2024-3400, CVE-2023-46805, CVE-2023-20273, CVE-2023-20198, and CVE-2018-0171. Public PoC exploit code is available on GitHub, including at https://github.com/Chocapikk/CVE-2024-21887 (for CVE-2024-21887 Ivanti command injection). Functional exploit code for the other referenced CVEs has been weaponized by threat actors.
- **Patch Available:** No single consolidated patch exists for advisory AA25-239A itself — it is a threat-activity advisory. Vendor patches are individually available for each referenced CVE: Ivanti patches for CVE-2023-46805 and CVE-2024-21887 (Connect Secure/Policy Secure); Palo Alto Networks patches for CVE-2024-3400 (PAN-OS GlobalProtect); Cisco patches for CVE-2023-20198 and CVE-2023-20273 (IOS XE Web UI); historical patches for CVE-2018-0171 (Smart Install). Organizations should apply these individual vendor patches as applicable. Reference: Ivanti KB https://hub.ivanti.com/s/article/KB-CVE-2023-46805-Authentication-Bypass-CVE-2024-21887-Command-Injection-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure-Gateways; NVD entries for individual CVEs at https://nvd.nist.gov/.
- **Active Exploitation:** Yes — confirmed active exploitation in the wild. Per CISA Advisory AA25-239A (August 27, 2025) and supporting FBI reporting, PRC state-sponsored actors (Salt Typhoon/OPERATOR PANDA/RedMike/UNC5807/GhostEmperor) have compromised networks of major U.S. and international telecommunications providers, with reporting indicating over 600 organizations across 80+ countries targeted. Sources: CISA Advisory AA25-239A (https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a); The Hacker News 'Salt Typhoon Exploits Flaws in Edge Network Devices to Breach 600 Organizations Worldwide' (August 28, 2025); Nextgov 'Salt Typhoon hackers targeted over 80 countries, FBI says' (August 27, 2025).
- **Threat Actors:** Salt Typhoon (also tracked as OPERATOR PANDA, RedMike, UNC5807, GhostEmperor) — People's Republic of China (PRC) state-sponsored cyber threat actors
- **Mitigation:** CISA recommends: (1) Prioritize patching the known exploited CVEs referenced in the advisory (CVE-2024-21887, CVE-2023-46805, CVE-2024-3400, CVE-2023-20273, CVE-2023-20198, CVE-2018-0171) on Ivanti Connect Secure/Policy Secure, Palo Alto PAN-OS with GlobalProtect, and Cisco IOS/IOS XE devices. (2) Upgrade unsupported/end-of-life network devices to vendor-supported models. (3) Regularly review network device logs and configurations for unexpected activity (unexpected GRE/tunneling protocols, modified ACLs/routes, unauthorized local accounts, TACACS+/RADIUS anomalies). (4) Compare running configurations against authorized, known-good baselines. (5) Review and harden remote-access configurations, ACLs, and transport protocols. (6) Implement SNMPv3 with USM and VACM where SNMP is required. (7) Verify the legitimacy and minimum-privilege scope of all local accounts. (8) Audit routing tables for unauthorized routes and verify PCAP/NetFlow capture commands are not altered. (9) Monitor virtualized containers on network devices (e.g., Cisco Guest Shell) using device syslog, AAA command accounting, container logs, and off-box flow/telemetry. (10) Enforce AAA accounting (TACACS+/RADIUS) for all CLI activity and forward logs off-box. (11) Segment and restrict provider-to-provider and provider-to-customer connections; disable unused management services (Guest Shell, Smart Install, unused web UI). (12) Hunt for and remove unauthorized modifications; assume compromise of any affected device until verified clean.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2023-23397 is a critical Elevation of Privilege vulnerability in Microsoft Outlook for Windows. It is triggered when an attacker sends a specially crafted message containing an extended MAPI property (PidLidReminderFileParameter) with a UNC path pointing to an attacker-controlled SMB server (TCP 445). When Outlook processes the message, it automatically connects to the remote SMB share with no user interaction required, leaking the victim's Net-NTLMv2 hash to the attacker's server. The captured hash can be cracked offline or relayed for NTLM authentication against other systems. APT28/GRU Unit 26165 weaponized this flaw since 2022 against Western logistics and IT companies supporting Ukraine aid. The campaign also exploited Roundcube Webmail (CVE-2021-44026 RCE via PHP object instantiation, CVE-2020-35730 stored XSS, CVE-2020-12641 stored XSS) and WinRAR (CVE-2023-38831 spoofed-extension RCE via crafted archives), and abused SOHO edge devices as covert infrastructure.
- **Affected Products:** Microsoft Outlook for Windows (CVE-2023-23397); Roundcube Webmail versions before 1.3.17 and 1.4.x before 1.4.12 (CVE-2021-44026), before 1.2.13, 1.3.x before 1.3.16, and 1.4.x before 1.4.10 (CVE-2020-35730), before 1.4.4 (CVE-2020-12641); RARLAB WinRAR (CVE-2023-38831); various SOHO network devices/routers/cameras used as covert infrastructure
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** Yes - public PoC exploits available on GitHub, including api0cradle/CVE-2023-23397-POC-Powershell (PowerShell-based NTLM hash leakage via specially crafted calendar invites) and vlad-a-man/CVE-2023-23397 (Python-based PoC). The vulnerability has been actively weaponized by APT28/GRU Unit 26165 since at least 2022.
- **Patch Available:** Yes - Microsoft released patches for CVE-2023-23397 on March 14, 2023 (March 2023 Patch Tuesday). Roundcube patches: CVE-2021-44026 fixed in v1.3.17 and v1.4.12 (December 2021); CVE-2020-35730 fixed in v1.2.13, 1.3.16, 1.4.10 (January 2021); CVE-2020-12641 fixed in v1.4.4 (June 2020). WinRAR patch for CVE-2023-38831 in version 6.23 (August 2023).
- **Active Exploitation:** Yes - confirmed active exploitation in the wild. The GRU's 85th Main Special Service Center, military unit 26165 (APT28/Fancy Bear), has been weaponizing CVE-2023-23397 since at least 2022 against Western logistics and technology companies supporting Ukraine aid coordination. Confirmed by CISA/FBI/NSA/NCSC-UK joint advisory AA25-141A (May 21, 2025), with corroboration from Germany's BSI/BfV, Czech NUKIB, Poland's ABW/SKW, France's ANSSI, Netherlands MIVD, Denmark's DDIS, Estonia's EFIS/NCSC-EE, Australia ASD/ACSC, and Canada Cyber Centre.
- **Threat Actors:** Russian GRU Unit 26165 (APT28, Fancy Bear, Forest Blizzard, Strontium, Sednit, Sofacy, IRON TWILIGHT, Blue Athena, Pawn Storm, Calisto Group, TAG-1100)
- **Mitigation:** Apply vendor patches immediately: install Microsoft Outlook security updates from March 2023 Patch Tuesday (CVE-2023-23397); upgrade Roundcube to 1.3.17+/1.4.12+ (or latest) for CVE-2021-44026, CVE-2020-35730, CVE-2020-12641; upgrade WinRAR to 6.23 or later for CVE-2023-38831. Hardening: block outbound SMB (TCP 445), NetBIOS (137/139), and WebDAV/Outlook-Anywhere traffic from user networks; enforce SMB signing to prevent NTLM relay; block outbound NTLM authentication via Group Policy; require MFA (especially for privileged accounts); enable attack surface reduction rules; segment IT/OT networks; disable the WebClient service; monitor for unusual calendar item processing; isolate and firmware-harden SOHO edge devices; remove UPnP, P2P, and anonymous-access settings on edge devices; require authentication for RTSP and remote admin services on cameras; apply principle of least privilege; monitor for Active Directory reconnaissance via ntdsutil.exe and ADExplorer.exe, and for use of Impacket, PsExec, and RDP-based lateral movement.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

**Parallel AI Enrichment:**

- **Technical Details:** This CrowdStrike blog post is a general thought-leadership article on browser security, not a specific CVE advisory. It argues that browser risk extends beyond zero-days to include N-day (post-disclosure) vulnerabilities and routine web-borne attacks such as phishing, credential theft, malicious downloads, session hijacking, clickjacking, cross-site scripting, HTML smuggling, and session abuse. Because many browsers share the open-source Chromium codebase, a vulnerability in shared components (rendering logic, JavaScript engine, document handling, or memory-safety code) can affect multiple browsers simultaneously, depending on each vendor's implementation, hardening, configuration, and patch timeline. Successful browser compromises typically involve multi-stage exploit chains rather than a single bug, often progressing from rendering/JavaScript/memory-safety exploitation to a sandbox escape and privilege escalation.
- **Affected Products:** Chromium-based web browsers (Google Chrome, Microsoft Edge, Opera, Brave, Vivaldi, and other vendors that incorporate the open-source Chromium codebase). No specific versions are named because this is a general advisory, not a version-specific CVE disclosure.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No specific proof-of-concept (PoC) or weaponized exploit is referenced. The blog discusses browser-based exploit chains at a conceptual level but does not link to or name a public PoC.
- **Patch Available:** No specific vendor patch is associated with this blog. The post is a general advisory that recommends keeping browsers current via a validate-test-stage-deploy workflow. CrowdStrike Falcon Secure Access (https://www.crowdstrike.com/en-us/products/endpoint-security/falcon-secure-access) is referenced as a runtime defense layer that mitigates browser exploitation before patches are applied.
- **Active Exploitation:** No specific in-the-wild exploitation of a particular CVE is reported in this blog post. The article cites industry-level trend data indicating active exploitation is widespread: the Verizon 2026 Data Breach Investigations Report found vulnerability exploitation surpassed stolen credentials as the top breach entry point in 2025, and the CrowdStrike 2026 Global Threat Report found 42% of vulnerabilities were exploited before public disclosure (zero-day exploitation).
- **Threat Actors:** None known
- **Mitigation:** 1) Maintain a disciplined patching workflow that validates, tests, stages, and confirms browser updates across managed and unmanaged devices to shorten the window between patch release and deployment. 2) Reduce reliance on patch timing alone by adding in-browser runtime protection that operates inside the browser session. 3) CrowdStrike Falcon Secure Access is referenced as a defense that runs inside the browser's JavaScript execution environment and uses JavaScript Language Randomization (JSLR), a moving-target-defense technique that continuously randomizes the JavaScript runtime to make browser vulnerabilities harder to exploit even before a patch is deployed. The product also blocks phishing and adversary-in-the-middle techniques, protects session tokens against hijacking and MFA bypass, and prevents credential theft and data exfiltration at the point of execution. 4) Apply general browser-hygiene controls against phishing, malicious scripts, credential theft, and data exfiltration across users, devices, applications, and browsers.
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
