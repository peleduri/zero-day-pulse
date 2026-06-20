# Zero Day Pulse

> **Generated:** 2026-06-20 19:08 UTC &nbsp;|&nbsp; **Total:** 31 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 9 &nbsp;|&nbsp; 🟡 High: 22 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path traversal vulnerability in SimpleHelp RMM that lets unauthenticated remote attackers supply crafted traversal sequences to vulnerable endpoints, enabling reading of arbitrary files and exposure of sensitive data such as credentials.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Public proof‑of‑concept (PoC) write‑ups are available (e.g., OffSec blog).
- **Patch Available:** Yes — Broadcom (SimpleHelp vendor) released patches. https://www.broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability
- **Active Exploitation:** Yes — confirmed active exploitation by ransomware actors, reported in CISA advisory AA25-163A and multiple security vendor write‑ups.
- **Threat Actors:** Ransomware actors (unspecified ransomware groups)
- **Mitigation:** Apply the vendor-provided patches immediately; if patching is delayed, restrict network access to SimpleHelp management interfaces (firewall to trusted IPs), disable internet‑facing instances, monitor for suspicious activity, rotate any exposed credentials, and enforce host‑level controls such as strict file permissions and network segmentation.
- **Vendor Advisory:** https://www.broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI): Adversaries hide adversarial instructions in third-party content (web pages, blogs, forums/emails, GitHub comments, documents) that an LLM/AI-agent ingests during normal task execution (search, summarise, scrape, code assist). The model then follows attacker instructions instead of (or alongside) user intent. Delivery mechanisms documented: zero-sized text, CSS hiding (display:none, visibility:hidden), 1-pixel fonts, HTML attribute obfuscation, HTML comments, meta tags, dynamic client-side injection, multi-layer encoding, payload splitting, multilingual payloads. Observed payload classes: tone steering/pranks; 'helpful guidance' steering answers; SEO manipulation; resource-exhaustion streams to deter agents; data exfiltration (IP/credentials to attacker endpoint); file-deletion/destruction prompts; DAN/god-mode jailbreak and system-prompt spoofing. Related 'Task Injection' technique (Google Bug Hunters, Dec 11 2025) bypasses prompt-injection classifiers by resembling normal web text - disclosed and patched in OpenAI Operator.
- **Affected Products:** Google Gemini; Google Workspace with Gemini; broadly applicable to AI agents including ChatGPT, Microsoft Copilot, Claude Code, GitHub Copilot, Cursor, OpenAI Operator/CUA, AI ad-review systems, agentic crawlers, customer-support bots, and security scanners. No specific build/version numbers available.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes - multiple public PoCs/repos/IOCs available:
- PayloadsAllTheThings/Prompt-Injection: https://swisskyrepo.github.io/PayloadsAllTheThings/Prompt%20Injection/
- Forcepoint X-Labs '10 Indirect Prompt Injection Payloads Caught in the Wild' (Apr 22 2026): https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads
- IPI-proxy red-team toolkit: http://arxiv.org/html/2605.11868v1
- Google Bug Hunters 'Task Injection' PoC + GHSAs (GHSA-5289-qv3f-x67g, GHSA-25j5-vvch-9rf3): https://bughunters.google.com/blog/task-injection-exploiting-agency-of-autonomous-ai-agents
- Greshake et al. research: https://greshake.github.io/
- Common Crawl corpus: https://commoncrawl.org/
- **Patch Available:** Not applicable as a single-vendor-patch situation - IPI is an attack class affecting many vendors simultaneously. Google states it is 'continuously hardening' Gemini and Google Workspace with Gemini, plus running large-scale real-time telemetry on the open web to suppress IPI-bait pages (no specific commit/build published). Adjacent separately-patched issues: OpenAI patched Operator/CUA Task Injection flaws (Google Bug Hunters GHSAs GHSA-5289-qv3f-x67g, GHSA-25j5-vvch-9rf3) - https://bughunters.google.com/blog/task-injection-exploiting-agency-of-autonomous-ai-agents; Microsoft patched 'ShareLeak' / CVE-2026-21520 in Copilot Studio - http://thehackernews.com/2026/04/google-patches-antigravity-ide-flaw.html
- **Active Exploitation:** Yes - confirmed active exploitation in the wild. Google Threat Intelligence observed a 32% relative increase in malicious IPI detections between November 2025 and February 2026 across ~2-3 billion Common-Crawl page snapshots. Concrete in-the-wild incidents: AI-ad-review evasion on reviewerpress[.]com (Dec 2025, Palo Alto Unit 42); SEO poisoning on 1winofficialsite[.]in (Unit 42); Data-destruction IPI on splintered[.]co[.]uk (Unit 42); Forced-plan purchase IPI on llm7-landing.pages.dev (Unit 42); 10 distinct live IPI payloads documented by Forcepoint X-Labs (Apr 22 2026). Sources: http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html ; https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/ ; https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads ; https://www.securityweek.com/malicious-ai-prompt-injection-attacks-increasing-but-sophistication-still-low-google/
- **Threat Actors:** None known
- **Mitigation:** Layered defense / defense-in-depth required (no single mitigation suffices). Vendor-side (Google): continuous model + product hardening; red-team pressure-testing; AI Vulnerability Reward Program (bughunters.google.com); global-scale real-time telemetry over open web to detect/neutralize IPI-bait pages. Customer/enterprise-side deployment guidance: (1) Treat all externally-reachable content as untrusted input; enforce strict data-vs-instruction boundary when AI agents consume third-party content; (2) Input validation/sanitization of fetched content plus output validation; (3) Deterministic defenses - allowlists, runtime policy enforcement, action-class restrictions, egress controls; (4) Human-in-the-loop confirmation for security-sensitive actions (outbound data, shell exec, delete, pay); (5) UI design that visibly marks model-generated content vs user-visible content; (6) IPI-classifier and anomaly-detection layered in; (7) Correlate agent actions with EDR/browser/DNS/SSE/CSPM telemetry.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection injects malicious instructions into user‑controlled data sources (web pages, emails, documents). The LLM consumes this content, treats the hidden instructions as legitimate, and may execute actions like exfiltrating data, navigating to URLs, or performing transactions when agentic capabilities and credentials are present.
- **Affected Products:** Google Workspace with Gemini (Workspace’s RAG integrations / Gemini Enterprise)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Proof‑of‑concept techniques are described in Noma Labs’ GeminiJack write‑up and Forcepoint’s IPI payload blog.
- **Patch Available:** No single patch; mitigation is provided via continuous updates described in the Google blog post.
- **Active Exploitation:** Google observed limited‑sophistication IPI experiments; Noma Labs disclosed a zero‑click GeminiJack exploit; Forcepoint reported active IPI payloads in the wild.
- **Threat Actors:** None known
- **Mitigation:** Apply deterministic defenses (user confirmation, URL sanitization, tool‑chaining policies), enable the centralized Policy Engine, update workspace/Gemini security configurations per Google guidance, and employ ML/LLM retraining with synthetic data and red‑team testing.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection allows a malicious web page to embed crafted content that alters the prompts given to the Gemini AI agent, potentially causing the agent to perform unintended actions or disclose data.
- **Affected Products:** Google Chrome (versions supporting Gemini agentic browsing)
- **CVSS Score:** -9999.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit or PoC is known.
- **Patch Available:** Google has released a patch for the vulnerability shortly after disclosure.
- **Active Exploitation:** Yes, active exploitation has been reported.
- **Threat Actors:** None known
- **Mitigation:** Deploy the updated Chrome version that includes the new isolation architecture; enable security features that sandbox the Gemini agent and validate incoming prompts before processing.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit referenced.
- **Patch Available:** No specific vendor patch referenced; patch availability not applicable to this blog post.
- **Active Exploitation:** No confirmed active exploitation reported in association with this post.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection works by an attacker hiding malicious natural-language instructions inside external content that a generative-AI system later ingests as untrusted data. When the user later asks the model a benign question, the model conflates user instructions with the injected data instructions and executes attacker commands as if they were legitimate. Concrete attack styles described in the blog include: (a) hidden instructions in emails, documents, and Google Calendar invites that instruct the AI to exfiltrate user data or perform unauthorized actions; (b) URL-based data exfiltration where the model is tricked into rendering attacker-controlled links/images that pull in user context; (c) 0-click image-rendering exfiltration ('EchoLeak'-style) where a model-generated response image fetches victim data to an attacker host. Google notes Gemini is exposed to the same general technique because Gemini also retrieves untrusted external content, but the rendering/output step is hardened in Gemini to block this specific exfiltration channel.
- **Affected Products:** Gemini app; Gemini in Google Workspace (Gmail, Google Docs / Docs editors, Google Drive, Google Chat); Gemini 2.5 family of models (which received adversarial-training hardening). This is a class-of-vulnerability advisory, not a single-CVE product notice, so no specific vulnerable version numbers are listed.
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof-of-concept research exists for the broader indirect-prompt-injection class but the Google blog itself does not publish or link a PoC. Notable public research: the 'PromptPwnd' PoC demonstrating prompt injection in GitHub Actions / GitLab pipelines affecting AI coding agents including Google's Gemini CLI (disclosed publicly on Reddit and covered at cyberpress.org), and 0-click image-rendering data exfiltration commonly known as 'EchoLeak' (tracked as CVE-2025-32711 against third-party AI assistants, which does NOT apply to Gemini due to Google's markdown sanitization blocking the exfiltration URL). Sources: https://www.reddit.com/r/programming/comments/1pe3cew/prompt_injection_within_github_actions_google/ , http://cyberpress.org/claude-code-gemini-cli-and-github-copilot-vulnerable
- **Patch Available:** No traditional single-version vendor patch is published — the blog describes a class of attack mitigated by an already-deployed, continuously updated layered control set. Google states the defenses are applied across Workspace AI features (Gmail, Docs, Drive, Chat) and the Gemini app, and model hardening was rolled out as part of the Gemini 2.5 release. Administrative reference: https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini
- **Active Exploitation:** Confirmed observed activity against the broader threat class, but no specific named campaigns targeting Google's Gemini. Per Google's follow-up threat-intelligence analysis reported by SecurityWeek on 2026-04-27, Google observed a 32% increase in indirect prompt-injection attempts against AI systems reachable on the public web between November 2025 and February 2026, but characterized attacker sophistication as 'relatively low' and stated attackers 'have yet not productionized this research at scale'. The original 2025-06-13 blog (Adam Gavish, Google GenAI Security Team) describes the attack vector as 'emerging' and does not claim mass in-the-wild exploitation of Gemini itself.
- **Threat Actors:** None known. The Google Security Blog post (Adam Gavish, Google GenAI Security Team, 2025-06-13) refers only generically to 'attackers', 'adversaries', and 'threat actors'. Google's follow-on threat-intelligence study (reported via SecurityWeek, April 27, 2026) does not attribute observed indirect prompt injection attempts to any named APT group, ransomware operator, or specific campaign.
- **Mitigation:** Google's layered defense-in-depth strategy, applied at every stage of the prompt lifecycle: (1) ML-based prompt-injection content classifiers that scan emails and files for known malicious-instruction patterns before they reach the model; (2) 'security thought reinforcement' — targeted system/safety prompt instructions that steer the model to ignore adversarial commands in retrieved content; (3) markdown sanitization and suspicious-URL redaction — external image/markdown URLs are stripped or rewritten through Google Safe Browsing to prevent rendered-output exfiltration (this layer neutralizes EchoLeak-style 0-click leaks); (4) Human-In-The-Loop (HITL) user confirmation framework requiring explicit user approval for sensitive actions such as deleting calendar events or sending messages; (5) end-user security mitigation notifications — contextual alerts plus 'Learn more' links shown to the user when a defense fires; (6) model resilience and ecosystem — adversarial training (Gemini 2.5 hardened with adversarial examples), continuous AI red-teaming, the Secure AI Framework (SAIF), collaboration with the Coalition for Secure AI (CoSAI), and Google's AI Vulnerability Reward Program (VRP) for external researcher disclosure.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Chinese state‑sponsored actors target backbone, provider‑edge and customer‑edge routers, modify router firmware or configurations to embed persistent backdoors, and use compromised devices and trusted connections to pivot laterally across networks.
- **Affected Products:** Backbone routers (various vendors), Provider Edge (PE) routers, Customer Edge (CE) routers
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit available.
- **Patch Available:** No official patch available.
- **Active Exploitation:** Yes, active exploitation has been reported globally, as detailed in the CISA advisory and NSA/CSA guidance.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Implement strict access controls on router management interfaces, regularly apply firmware/security updates, segment network zones, disable unnecessary services, monitor for anomalous traffic, and use simulated attacks to validate defenses.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit publicly documented in AA25-141A; exploit_available: None known.
- **Patch Available:** Patch availability varies by affected vendor; no single vendor patch referenced in AA25-141A.
- **Active Exploitation:** Confirmed targeting/active espionage by Russian GRU 85th GTsSS (Unit 26165) against Western logistics and technology companies.
- **Threat Actors:** Russian GRU 85th Main Special Service Center (85th GTsSS), military unit 26165.
- **Mitigation:** Implement multifactor authentication, network segmentation, apply vendor‑specific patches, monitor for IOCs, restrict administrative privileges, and use endpoint detection and response as recommended in AA25-141A.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-44815 is a stack‑based buffer overflow in the Windows DHCP Client Service triggered by rogue DHCP responses that invoke the DhcpGetOriginalSubnetMask API. CVE-2026-42897 is a reflected cross‑site scripting flaw in Microsoft Exchange OWA that allows an attacker to inject malicious JavaScript that executes in a victim's browser.
- **Affected Products:** Microsoft Exchange Server (OWA) for CVE-2026-42897, Windows DHCP Client Service for CVE-2026-44815, Microsoft Defender for CVE-2026-41091 and CVE-2026-45498.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC or weaponized exploit: CVE‑2026‑42897 is reported as actively exploited in the wild; CVE‑2026‑41091 and CVE‑2026‑45498 are also confirmed as exploited. No single canonical public PoC URL is available.
- **Patch Available:** Microsoft published updates in June 2026 for the listed vulnerabilities; see Microsoft Security Update Guide entries for each CVE.
- **Active Exploitation:** Confirmed active exploitation for CVE‑2026‑42897, CVE‑2026‑41091, and CVE‑2026‑45498 per Microsoft and CISA/Known Exploited Vulnerabilities listings.
- **Threat Actors:** None known
- **Mitigation:** Apply the Microsoft June 2026 security updates. For CVE‑2026‑44815, audit and restrict applications that call the DhcpGetOriginalSubnetMask API. For the Exchange OWA XSS, implement server‑side input validation and apply any Microsoft‑recommended OWA hardening settings.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 10. 🟡 High Severity — Hackers Exploit Gravity SMTP WordPress Plugin Bug to Expose API Keys

**CVE:** `CVE-2026-4020` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-20
**Reference:** <https://thehackernews.com/2026/06/hackers-exploit-gravity-smtp-wordpress.html>

> Threat actors are exploiting a recently patched security flaw impacting Gravity SMTP, a WordPress plugin that&#x27;s installed on about 100,000 sites.

The vulnerability, tracked as CVE-2026-4020 (CVSS score: 5.3), is a medium-severity information disclosure flaw that can allow unauthenticated attackers to extract sensitive data, such as configuration data, API keys, secrets, and OAuth tokens

**Parallel AI Enrichment:**

- **Technical Details:** An unauthenticated Sensitive Information Exposure vulnerability lets attackers query Gravity SMTP endpoints and obtain detailed system configuration, API keys, secrets, and OAuth tokens configured for email integrations.
- **Affected Products:** Gravity SMTP WordPress plugin versions prior to 2.1.5
- **CVSS Score:** 5.3
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or exploit URL is known.
- **Patch Available:** Patch available – Gravity SMTP 2.1.5 released on 2026-03-17 (no URL provided).
- **Active Exploitation:** Confirmed active exploitation in the wild, reported by Wordfence and security media outlets; over 17 million exploit attempts have been blocked.
- **Threat Actors:** None known
- **Mitigation:** Update Gravity SMTP to version 2.1.5 or newer. If patching is not possible, monitor for the exploit request patterns, consider disabling the plugin, remove credentials from its settings, rotate any exposed API keys/secrets, and apply the Wordfence firewall rules released on May 5, 2026 (Premium/Care/Response) and June 4, 2026 (free).
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟡 High Severity — symfony/ux-icons: XSS via unsanitized SVG content in local files and Iconify on-demand responses

**CVE:** `CVE-2026-55877` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-6v8j-33hc-mv84>

> ### Description

The `ux_icon()` Twig function is marked `is_safe=[&#x27;html&#x27;]`, so Twig never escapes its output. `Icon::toHtml()` inlines the SVG source verbatim into the page. Browsers execute `&lt;script&gt;` elements and `on*` event-handler attributes found inside inline SVG, making any unsanitized icon a vector for cross-site scripting.

Two code paths were affected. In the local file …

---

## 12. 🟡 High Severity — OpenBao: Transit secrets engine crashes on key creation with `derived: true` for asymmetric key types

**CVE:** `CVE-2026-55776` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-8w8f-r2xv-4q4j>

> On OpenBao 2.5.4 and 2.5.2(and likely earlier versions also), an authenticated caller with write access to `transit/keys/*` can crash the OpenBao server by issuing a single key-creation request that combines an asymmetric `type` (`rsa-*`, `ecdsa-*`, `ed25519`)
with `derived: true`. The server returns no HTTP response and the process terminates (exit code 2). This is a remote, low-complexity denial…

---

## 13. 🟡 High Severity — OpenBao: Cross-namespace lease revocation/renewal via canonical sys/leases/{revoke,renew} — incomplete fix of CVE-2026-45808

**CVE:** `CVE-2026-55774` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-c36x-h252-g9x2>

> ### Summary

OpenBao users with access to the `sys/leases/revoke/:lease_id` endpoint in any namespace can revoke leases in any other namespace as long as the lease identifier is known to them, bypassing ACLs that should apply for cross-namespace revocations.

### Impact

OpenBao&#x27;s namespaces provide multi-tenant separation. A tenant who intentionally leaks lease identifiers can have their lea…

---

## 14. 🟡 High Severity — OpenBao: LDAPi ldaputil (wrong escape func)

**CVE:** `CVE-2026-55770` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-6mwx-4547-5vc9>

> ## 1. Description

### Component

`sdk/helper/ldaputil/client.go` — the shared LDAP utility library used by both the LDAP authentication backend and OpenLDAP secrets engine to construct LDAP search filters and bind DNs.

### Root Cause

The LDAP utility contains a **function selection error** that causes incorrect escaping of user-controlled input in LDAP filter construction. Two lines construct t…

---

## 15. 🟡 High Severity — StarCitizenWiki Extension Embed Video: Stored XSS via malformed src url with $wgEmbedVideoRequireConsent enabled

**CVE:** `CVE-2026-55692` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-5c7p-g73q-rpg5>

> ### Summary
With $wgEmbedVideoRequireConsent enabled (the default), the urls for videos are stored in a json-ified data attribute`data-mw-iframeconfig`. When given a malformed url or id, the data-mw-iframeconfig attribute can be escaped via single quotes, allowing for html/javascript injection.

### Details
The sprintf [here](https://github.com/StarCitizenWiki/mediawiki-extensions-EmbedVideo/blob/…

---

## 16. 🟡 High Severity — Langflow: BaseFileComponent-based nodes arbitrary file read with RCE exploit

**CVE:** `CVE-2026-55447` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-ccv6-r384-xp75>

> ### Summary
All components based on `BaseFileComponent` are vulnerable to the following vulnerability:
1. Docling (`DoclingInlineComponent`)
2. Docling Serve (`DoclingRemoteComponent`)
3. Read File (`FileComponent`)
4. NVIDIA Retriever Extraction (`NvidiaIngestComponent`)
5. Video File (`VideoFileComponent`)
6. Unstructured API (`UnstructuredComponent`)

For clarity, from now on I&#x27;ll only ref…

---

## 17. 🟡 High Severity — Langflow: Unauthenticated DoS through multipart form boundary file upload

**CVE:** `CVE-2026-55446` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-qwqc-p3q8-wcg9>

> ### Summary
An attacker can send a `/api/v1/files/upload/` request without any authentication token/cookies and abuse a very long multipart form boundary to make the langflow app unusable for all users for an indefinite amount of time. 

### Details
https://github.com/langflow-ai/langflow/blob/v1.0.18/src/backend/base/langflow/api/v1/files.py#L40

The file upload function will try to process the m…

---

## 18. 🟡 High Severity — Langflow: Logout button does not clear session

**CVE:** `CVE-2026-55423` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-7hw8-6q6r-4276>

> ### Summary
The logout button does not clear the session. The previous user stays logged in unless another user explicitly logs in.

### Details
Not in auto login mode. Hosted on localhost. `access_token_lf` remains present in both Local Storage and Cookies. `refresh_token_lf` remains present in Cookies.

**Root cause:** the `/logout` endpoint deleted the authentication cookies without matching th…

---

## 19. 🟡 High Severity — Mailpit: Incomplete SSRF protection in Link Check API via IPv6 transition mechanisms

**CVE:** `CVE-2026-55187` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-w4mc-hhc6-xp28>

> ## Summary

The remediation shipped in mailpit v1.29.2 for [GHSA-mpf7-p9x7-96r3](https://github.com/axllent/mailpit/security/advisories/GHSA-mpf7-p9x7-96r3) (CVE-2026-27808) is incomplete. The `tools.IsInternalIP` deny-list relies on Go&#x27;s stdlib classification helpers (`IsLoopback`, `IsPrivate`, `IsLinkLocalUnicast`, `IsLinkLocalMulticast`, `IsUnspecified`, `IsMulticast`) plus an inline CGNAT…

---

## 20. 🟡 High Severity — Traefik Kubernetes Ingress NGINX provider fails open when auth-secret resolution fails

**CVE:** `CVE-2026-54762` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-4mr2-fg2p-w63c>

> ## Summary

There is a medium severity vulnerability in Traefik&#x27;s Kubernetes Ingress NGINX provider that causes affected routes to fail open. When an Ingress explicitly enables BasicAuth or DigestAuth through the supported `nginx.ingress.kubernetes.io/auth-type` and `auth-secret` annotations, but the referenced auth Secret cannot be resolved or parsed, Traefik logs the resolution error, skips…

---

## 21. 🟡 High Severity — dbt MCP Server: Unauthenticated OAuth Context Endpoint Leaks dbt Platform Tokens

**CVE:** `CVE-2026-55837` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-jr33-mw75-7j8f>

> ## Unauthenticated OAuth Context Endpoint Leaks dbt Platform Tokens

### Summary

The local OAuth helper FastAPI server bundled with `dbt-mcp` exposes the `GET /dbt_platform_context` endpoint without any form of authentication or host-origin validation. After a user completes the OAuth login flow against dbt Cloud (cloud.getdbt.com), the endpoint returns the full `DbtPlatformContext` object — incl…

---

## 22. 🟡 High Severity — Craft CMS: Blind SSRF and Arbitrary JavaScript Injection via Host Header Poisoning in actionResourceJs

**CVE:** `CVE-2026-55791` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-c55v-343g-5xff>

> **1. Overview**

Craft CMS is vulnerable to Server-Side Request Forgery (SSRF) and Arbitrary JavaScript Injection through the `/actions/app/resource-js` endpoint. By exploiting the default permissive `trustedHosts` configuration, an attacker can poison the `Host` or `X-Forwarded-Host` header to manipulate the application’s `$baseUrl`. This bypasses the endpoint’s internal URL validation, forcing t…

---

## 23. 🟡 High Severity — @tinacms/cli: Remote Code Execution in @tinacms/cli via Forestry migration — unsanitised __TINA_INTERNAL__ marker in user-controlled YAML labels

**CVE:** `CVE-2026-54074` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-4936-9hrh-qqpw>

> ## Description

### Summary

`@tinacms/cli` contains a Remote Code Execution vulnerability in its
Forestry-to-Tina migration command. The internal helper `addVariablesToCode`
unquotes any value matching the marker `&quot;__TINA_INTERNAL__:::(.*?):::&quot;`
inside the stringified collection JSON. User-supplied `label` and `name`
fields from `.forestry/**/*.yml` are placed into that JSON without any…

---

## 24. 🟡 High Severity — Grafana Operator: Privilege escalation from namespace admin to cluster admin via GrafanaDashboard jsonnetLib fileName

**CVE:** `CVE-2026-11769` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-fcw4-wwqm-m8cf>

> We have released version 5.24.0 of the Grafana Operator. This patch includes a MODERATE severity security fix for a path traversal/privilege escalation vulnerability in the Grafana Operator.


### Summary

The Grafana Operator supports loading dashboards &amp; library panels using the jsonnet data templating language. The jsonnet expression is evaluated in the context of the operator manager pod.
…

---

## 25. 🟡 High Severity — @cyclonedx/cyclonedx-npm: Shell Injection via Unsanitized --workspace Argument

**CVE:** `CVE-2026-55849` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-v75r-vx73-82pj>

> ## Summary
A command injection vulnerability exists in `@cyclonedx/cyclonedx-npm` when the CLI is invoked with the `--workspace &lt;value&gt;` option while the environment variable `npm_execpath` is unset or empty.  
User‑supplied `--workspace` values are passed to a subshell without proper sanitization, enabling attackers to inject arbitrary OS commands.  
This issue corresponds to **CWE‑78**: Im…

---

## 26. 🟡 High Severity — Concurrent Ruby: ReadWriteLock allows wrong-thread write release and stray read-release counter corruption

**CVE:** `CVE-2026-54906` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-6wx8-w4f5-wwcr>

> ### Summary
`Concurrent::ReadWriteLock#release_write_lock` does not verify that the calling thread acquired the write lock. Any thread with access to the lock object can release an active write lock held by another thread. A second writer can then enter its critical section while the first writer is still running.

`Concurrent::ReadWriteLock#release_read_lock` also decrements the shared counter ev…

---

## 27. 🟡 High Severity — Concurrent Ruby: `ReentrantReadWriteLock` read-count overflow grants a write lock without exclusivity

**CVE:** `CVE-2026-54905` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-wv3x-4vxv-whpp>

> ### Summary
`Concurrent::ReentrantReadWriteLock` can incorrectly grant a write lock after one thread acquires the read lock 32,768 times.

The lock stores a thread&#x27;s local read and write hold counts in one integer. The low 15 bits are used for the read hold count, and bit 15 is used as `WRITE_LOCK_HELD`. After 32,768 reentrant read acquisitions, the local read count crosses into the write-loc…

---

## 28. 🟡 High Severity — CoreWCF: SPNEGO SecurityContextToken proof key wrapped without confidentiality

**CVE:** `CVE-2026-54784` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-2288-8h3r-cqgg>

> ### Impact
When the proof key recovered from the RSTR can be observed by a party that is not the legitimate client, that party can impersonate the authenticated Windows principal for the lifetime of the SCT (default ~10 hours) and decrypt or forge any subsequent WS‑SecureConversation traffic that uses keys derived from the SCT.

#### Preconditions
Using security mode TransportWithMessageCredential…

---

## 29. 🟡 High Severity — CoreWCF: SamlSerializer skips SignatureValue verification when SAML signing token is not an X.509 certificate

**CVE:** `CVE-2026-54774` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-rpj7-hr7h-w6p9>

> ### Impact
When a service is configured to validate SAML tokens using a method other than X.509 certificate signing, the final signature verification is skipped.

#### Preconditions
The service is configured to authenticate using SAML tokens and an out of band token resolver (commonly the IssuerTokenResolver of IssuedTokenServiceCredential) holds a non-X.509 SecurityToken whose key identifier the …

---

## 30. 🟡 High Severity — CoreWCF: Pre-authentication infinite-loop CPU exhaustion in CoreWCF net.tcp / net.pipe / net.uds framing handshake

**CVE:** `CVE-2026-54772` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-p86g-xrr2-pf7c>

> ### Impact
An unauthenticated remote attacker can pin one server thread‑pool worker at 100 % CPU per connection. With a few connections, the CPU usage can be exhausted.

#### Preconditions
An attacker being able to reach a service which is exposing an endpoint using one of NetTcpBinding, NetNamedPipeBinding, or UnixDomainSocketBinding.

### Patches
Fixed in CoreWCF v1.8.1 and v1.9.1

### Workaroun…

---

## 31. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
