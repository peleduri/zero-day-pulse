# Zero Day Pulse

> **Generated:** 2026-06-22 02:36 UTC &nbsp;|&nbsp; **Total:** 13 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 9 &nbsp;|&nbsp; 🟡 High: 4 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a directory (path) traversal vulnerability in SimpleHelp RMM that lets unauthenticated remote attackers manipulate file paths to read sensitive files on the target system.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (unspecified)
- **Mitigation:** Update SimpleHelp to a version newer than 5.5.7 (or apply the vendor‑released patch). If a patch cannot be applied immediately, limit external access to the RMM service, disable file‑upload features, and monitor for suspicious activity.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI): An attacker plants adversarial instructions inside external content that an AI agent ingests via retrieval-augmented generation or browsing/indexing. The LLM treats attacker-supplied text as authoritative context, overriding the original user prompt and executing attacker intent (data exfiltration, content suppression, transaction redirection, command execution). Concealment techniques: HTML comments, CSS hiding (display:none, 1px fonts, transparent/white-on-white, visually-hidden classes), aria-hidden=true abuse, meta-tag/semantic-namespace spoofing, '[SYSTEM OVERRIDE]' tag spoofing, magic-string spoofing, infinite-text decoy pages. Forcepoint's 10 in-the-wild payloads span: API-key exfiltration, content-suppression/DoS, unauthorized navigation, SEO/referral hijacking, brand/semantic injection, RCE-style data destruction, unauthorized financial transactions, output/content manipulation, system prompt leakage, and payment/donation redirection.
- **Affected Products:** AI agents, AI assistants, and any LLM-powered system ingesting untrusted external content (class-wide). Specifically named: Google Gemini, Google Workspace with Gemini. Forcepoint X-Labs also observed attacks against GitHub Copilot, Cursor, and Claude Code. No specific version numbers listed (class of attack, not a CVE).
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true. Sources: https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads (10 in-the-wild payloads, April 2026); PayloadsAllTheThings repository (referenced in the Google blog post); arXiv paper http://arxiv.org/abs/2601.07072.
- **Patch Available:** false. No single CVE patch exists for the IPI class. Google describes ongoing continuous mitigation rather than a discrete vendor patch. Related but separate vendor patches exist for specific IPI-derived product bugs (e.g., the Google Antigravity IDE flaw patched approximately Feb 28, 2026 per http://thehackernews.com/2026/04/google-patches-antigravity-ide-flaw.html).
- **Active Exploitation:** true. Google Threat Intelligence reports a 32% relative increase in malicious IPI between November 2025 and February 2026 across 2-3 billion Common Crawl pages. Forcepoint X-Labs observed 10 distinct IPI payloads actively deployed across the live public web (April 2026). Noma Labs disclosed GeminiJack zero-click IPI flaw in Google Gemini Enterprise and Vertex AI Search (December 8, 2025). Sources: [1], [3], [4].
- **Threat Actors:** None known. The Google Threat Intelligence authors characterize threat actors generically as 'threat actors' / 'adversaries' / 'individual website authors', with categories ranging from harmless pranksters and SEO-association spammers to malicious actors seeking AI data exfiltration or destruction. No specific APT group, nation-state actor, cybercrime gang, or ransomware operator is named. Google states that sophisticated attacker abuse of IPI is still rare compared with lower-tier activity.
- **Mitigation:** Google's recommended hardening: (1) continuous hardening of AI models and products so untrusted retrieved content is treated as data not instructions; (2) adversarial red-team pressure-testing; (3) the AI Vulnerability Reward Program for external reporting; (4) input/output validation and sanitization of retrieved content; (5) human-in-the-loop oversight for agentic actions; (6) allow-listing and least-privilege for tool calls. Companion advisories: https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections and https://deepmind.google/discover/blog/advancing-geminis-security-safeguards/.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) via content poisoning in Workspace data sources (Google Docs, Gmail, Calendar) used by RAG pipelines: attacker plants malicious instructions in shared content; RAG retrieves poisoned content into model context; Gemini treats embedded instructions as commands, performs broad data retrieval across connected datasources, and exfiltrates results (e.g., via embedding in an external image tag causing an HTTP request to attacker‑controlled server). Zero‑click, silent, persistent, scalable.
- **Affected Products:** Google Gemini Enterprise, Gemini (Workspace integration), Vertex AI Search
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true — https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/
- **Patch Available:** true — https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/
- **Active Exploitation:** true — sources: Noma Labs report and SecurityAffairs write‑up
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: restrict RAG datasource scope, URL sanitization, user confirmation for tool calls, deterministic policies via centralized Policy Engine (regex takedowns), ML/LLM‑based defenses retrained with synthetic attack variants, automated and human red‑teaming, VRP reporting. Follow Google’s guidance in the vendor advisory.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection in agentic browsers works by embedding attacker-controlled natural-language instructions inside web content (malicious sites, third-party iframes, user-generated content, URL fragments after '#', or poisoned data sources surfaced via RAG). When the planning model reads those pages to decide the next agent action, it cannot reliably distinguish injected data from legitimate user/system instructions, so the agent executes the attacker's goals (e.g., navigating to attacker-controlled pages, initiating financial transactions, exfiltrating browsing data, sending messages, subverting the same-origin policy). Agentic action capability — clicking, typing, submitting forms, completing purchases — amplifies impact. Closely related variants include HashJack (URL-fragment-delivered IPI on Gemini in Chrome, Copilot, Comet), GeminiJack (zero-click IPI via poisoned Google Workspace data sources against Gemini Enterprise), and CVE-2026-0628 (malicious extension injecting JavaScript into the privileged Gemini Live panel via WebView declarativeNetRequest, hijacking AI actions and exposing local files).
- **Affected Products:** Google Chrome with Gemini in Chrome / agentic AI capabilities (no specific pinned version — threat is architectural to the new feature); Chrome desktop prior to 143.0.7499.192 is affected by the closely related CVE-2026-0628 (Gemini Live panel hijacking by malicious extensions). Also related: Google Gemini Enterprise (GeminiJack zero-click flaw, patched Dec 2025); Gemini CLI VS Code extension version 1.2 (CVE-2025-54131, fixed in 1.3).
- **CVSS Score:** CVSS score unavailable for the indirect prompt injection class described in the blog. Related CVE-2026-0628: third-party reports cite CVSS v3.1 base score 8.8 (High). Related CVE-2025-54131: scoped under CVSS v4.0 per NVD.
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true — Multiple public PoCs/weaponized demonstrations exist: (1) Unit 42 CVE-2026-0628 PoC — https://unit42.paloaltonetworks.com/gemini-live-in-chrome-hijacking/ ; (2) Noma Labs GeminiJack zero-click PoC — https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/ ; (3) Cato CTRL HashJack PoC — https://www.catonetworks.com/blog/cato-ctrl-hashjack-first-known-indirect-prompt-injection/ ; (4) Forcepoint 10 in-the-wild IPI payloads — https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads ; (5) Unit 42 'Fooling AI Agents' PoC — https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/
- **Patch Available:** true — Chrome's new agentic defenses are rolling out via Chrome auto-update as announced in the Dec 8 2025 Google Security Blog. Related CVE-2026-0628 is patched in Chrome 143.0.7499.192 (Jan 2026 stable-channel desktop update: https://chromereleases.googleblog.com/2026/01/stable-channel-update-for-desktop.html). GeminiJack was patched by Google in Gemini Enterprise in December 2025. CVE-2025-54131 is fixed in Gemini CLI v1.3.
- **Active Exploitation:** true — Confirmed in-the-wild indirect prompt injection activity is documented by multiple independent security research teams: (1) Forcepoint X-Labs, Apr 22 2026 — '10 Indirect Prompt Injection Payloads Caught in the Wild' — https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads ; (2) Palo Alto Unit 42, Mar 3 2026 — 'Fooling AI Agents: Web-Based Indirect Prompt Injection Observed in the Wild' — https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/ ; (3) Cato CTRL, Nov 25 2025 — HashJack affecting Gemini in Chrome, Copilot in Edge, and Comet — https://www.catonetworks.com/blog/cato-ctrl-hashjack-first-known-indirect-prompt-injection/. No named APT/ransomware attribution, but malicious payloads and poisoned pages are confirmed present on the live web, not only in lab PoCs.
- **Threat Actors:** None known
- **Mitigation:** Chrome is shipping a multi-layer defense suite: (1) User Alignment Critic — an isolated Gemini-based model that vets every proposed agent action against the user's stated goal before execution; (2) Agent Origin Sets — extension of Site Isolation partitioning agent access into 'Read-only' and 'Read-writable' origin groups with a gating function that blocks cross-origin data leaks; (3) User Confirmations for sensitive actions (banking/medical portals, Google Password Manager, payments, sending messages); (4) Spotlighting — a prompting approach that biases the planner toward user/system instructions over on-page content; (5) Real-time prompt-injection classifier running in parallel with the planner to detect and block injected-instruction-driven actions; (6) Transparent work logs so users can observe, pause, or stop agent runs; (7) Automated red-teaming with sandboxed adversarial sites for continuous testing. Third-party hardening: deploy CASB with GenAI service controls, ML/IPS malware detection, advanced URL/DNS filtering, treat all untrusted web content as untrusted (data, not instructions), keep Chrome auto-updates enabled, restrict install of unverified extensions. For CVE-2026-0628 specifically, update Chrome to 143.0.7499.192 or later; for GeminiJack, ensure Gemini Enterprise is on the patched version; for CVE-2025-54131, upgrade Gemini CLI VS Code extension to v1.3+.
- **Vendor Advisory:** https://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A near-miss linear buffer overflow was discovered in unsafe Rust code within the CrabbyAVIF crate; the overflow was detected and fixed pre‑release. Android’s Scudo hardened allocator’s guard pages rendered the overflow non‑exploitable and turned the condition into a noisy crash, aiding detection.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true - https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use Scudo hardened allocator (guard pages), improve crash‑reporting to surface overflows into Scudo guard pages, add unsafe‑Rust review/training and encapsulation best practices; ensure patches tracked via Android security bulletin processes.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection involves an attacker placing hidden malicious instructions in external data sources such as emails, documents, or calendar invites. When the generative AI model processes this content, it unwittingly executes the hidden commands, potentially exfiltrating data or performing unauthorized actions. EchoLeak demonstrated a zero‑click variant that silently extracted data from Microsoft 365 Copilot via concealed instructions.
- **Affected Products:** Microsoft 365 Copilot, Microsoft Copilot Studio
- **CVSS Score:** 9.3
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Implement a layered defense: (1) detect and block suspicious content before it reaches the model, (2) filter inputs for known malicious patterns, (3) track provenance of external data to verify authenticity, (4) enforce runtime guardrails that limit model actions based on untrusted inputs. Apply vendor‑provided patches for affected products (e.g., Microsoft Copilot updates).
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors leverage known CVEs in Cisco IOS/IOS XE, PAN‑OS and Ivanti to gain initial access, then modify router ACLs, install unauthorized SSH keys or backdoors, execute Tcl scripts, and use Guest Shell containers to run malicious code, establishing persistent footholds and enabling lateral movement via TACACS+/SNMP manipulation and GRE/IPsec tunnels.
- **Affected Products:** Cisco IOS/IOS XE Smart Install (CVE-2018-0171), Cisco IOS XE (CVE-2023-20198), Palo Alto Networks PAN-OS (CVE-2024-3400), Ivanti (CVE-2024-21887)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a)
- **Active Exploitation:** true (https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a)
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching the vulnerable products, disable unused ports and protocols, require public‑key authentication for remote access, deploy vendor‑recommended OS versions, harden Cisco Guest Shell containers, and perform forensic checks on router configurations.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Russian GRU 85th GTsSS (Unit 26165)
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** Three publicly disclosed zero‑day vulnerabilities were fixed in the June 9, 2026 Patch Tuesday, including a Microsoft Defender‑related zero‑day dubbed “RoguePlanet” that can be weaponized to achieve code execution/elevation on Windows 10/11.
- **Affected Products:** Microsoft Windows (consumer and enterprise) OS builds 26100.8655 and 26200.8655, Microsoft Defender components
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — https://thehackernews.com/2026/06/microsoft-defender-rogueplanet-zero-day.html
- **Patch Available:** true — https://support.microsoft.com/en-us/topic/june-9-2026-kb5094126-os-builds-26200-8655-and-26100-8655-1a9bcba6-5f53-4075-8156-fe11ac631737
- **Active Exploitation:** true — https://thehackernews.com/2026/06/microsoft-defender-rogueplanet-zero-day.html
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Apply the June 2026 security updates (install KB5094126), enable automatic updates, limit privileged accounts, deploy endpoint detection and response, and implement network segmentation.
- **Vendor Advisory:** https://support.microsoft.com/en-us/topic/june-9-2026-kb5094126-os-builds-26200-8655-and-26100-8655-1a9bcba6-5f53-4075-8156-fe11ac631737

---

## 10. 🟡 High Severity — SEC Consult SA-20260618-0 :: Hardcoded Root Cloud Credentials in Application Binaries in Silver Leaf Technologies - Worksnaps.net Worksnaps

**CVE:** `CVE-2025-10560` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-06-21
**Reference:** <https://seclists.org/fulldisclosure/2026/Jun/21>

> Posted by SEC Consult Vulnerability Lab via Fulldisclosure on Jun 20 SEC Consult Vulnerability Lab Security Advisory &lt; 20260618-0 &gt; ======================================================================= title: Hardcoded Root Cloud Credentials in Application Binaries product: Silver Leaf Technologies - Worksnaps.net Worksnaps vulnerable version: &lt; 1.6.20260201 fixed version: 1.6.20260201 …

**Parallel AI Enrichment:**

- **Technical Details:** Worksnaps client application binaries contained hardcoded AWS root/cloud credentials and related key material. Extraction of these credentials from the binary gives an attacker complete access to the vendor's AWS infrastructure as the AWS root user.
- **Affected Products:** Worksnaps client (Silver Leaf Technologies / Worksnaps.net) versions < 1.6.20260201
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — https://sec-consult.com/vulnerability-lab/advisory/hardcoded-root-cloud-credentials-in-application-binaries-in-silver-leaf-technologies-worksnaps/
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Update Worksnaps client to version 1.6.20260201 or later; rotate any exposed AWS credentials and keys immediately; audit AWS account for unauthorized activity; follow principle of least privilege and remove use of embedded credentials from binaries; implement secrets management (e.g., AWS IAM roles, Secrets Manager).
- **Vendor Advisory:** https://sec-consult.com/vulnerability-lab/advisory/hardcoded-root-cloud-credentials-in-application-binaries-in-silver-leaf-technologies-worksnaps/

---

## 11. 🟡 High Severity — SEC Consult SA-20260617-0 :: Multiple Critical Vulnerabilities in Sprecher Automation SPRECON-E-C/-E-P/-E-T3

**CVE:** `CVE-2022-4333` | `CVE-2022-4332` | `CVE-2025-41741` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-06-21
**Reference:** <https://seclists.org/fulldisclosure/2026/Jun/19>

> Posted by SEC Consult Vulnerability Lab via Fulldisclosure on Jun 20 SEC Consult Vulnerability Lab Security Advisory &lt; 20260617-0 &gt; ======================================================================= title: Multiple Critical Vulnerabilities product: Sprecher Automation SPRECON-E-C/-E-P/-E-T3 vulnerable version: See vulnerable versions below fixed version: See solution section below CVE n…

---

## 12. 🟡 High Severity — CVE-2025-68624: Cross-Tenant Authentication Bypass by Spoofing in N-able Mail Assure

**CVE:** `CVE-2025-68624` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-06-21
**Reference:** <https://seclists.org/fulldisclosure/2026/Jun/10>

> Posted by Alessandro Bertoldi BCS via Fulldisclosure on Jun 20 CVE-2025-68624: Cross-Tenant Authentication Bypass by Spoofing in N-able Mail Assure CVE ID: CVE-2025-68624 Status: DISPUTED CWE: CWE-290 (Authentication Bypass by Spoofing) Affected Product: N-able Mail Assure (formerly SolarWinds MSP Mail Assure) Affected Service: N-able Mail Assure cloud-based multi-tenant SMTP relay infrastructure …

---

## 13. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
