# Zero Day Pulse

> **Generated:** 2026-07-09 01:50 UTC &nbsp;|&nbsp; **Total:** 26 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 16 &nbsp;|&nbsp; 🟡 High: 10 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Multiple unauthenticated path traversal vulnerabilities in SimpleHelp (≤ 5.5.7) allow crafted HTTP requests to read/download arbitrary files (including server configuration files containing secrets and hashed passwords) from the host.
- **Affected Products:** SimpleHelp remote support / RMM software — versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** false
- **Patch Available:** true (SimpleHelp 5.5.8; vendor advisory: https://guides.simple-help.com/kb---security-vulnerabilities-01-2025)
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Upgrade to SimpleHelp 5.5.8 or later (vendor fix); if unable to patch, apply vendor/CISA mitigations or discontinue use per guidance.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — Critical Vulnerability Exposes GitHub Agentic Workflows to Prompt Injection

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://www.securityweek.com/critical-vulnerability-exposes-github-agentic-workflows-to-prompt-injection/>

> Researchers show how attackers can use a crafted public GitHub Issue to trick AI-powered workflows into exposing data from private repositories without authentication. The post Critical Vulnerability Exposes GitHub Agentic Workflows to Prompt Injection appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** An unauthenticated attacker can open a crafted public GitHub Issue that injects natural-language instructions into an AI-driven Agentic Workflow. Because the agent reads untrusted issue content, holds standing read access to other (including private) repositories, and can post responses publicly, a prompt-injection (e.g., prefixing with the word “Additionally”) bypasses guardrails and causes the agent to fetch files (such as README.md) from private repos and publish them as public comments. The attack abuses workflow design and permissions rather than a traditional code bug.
- **Affected Products:** GitHub Agentic Workflows configurations that process untrusted public input (e.g., issues/PRs), have read access to private repositories (including cross-repo/org tokens), and can post output publicly
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true - PoC: https://github.com/sasinomalabs/poc/actions/runs/23909666039; Issue: https://github.com/sasinomalabs/poc/issues/153
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** - Avoid the “lethal trifecta”: do not combine (1) untrusted public input to agents, (2) standing access to private data, and (3) public posting. Disable agent responses to public issues/PRs or require human-in-the-loop review before any public output. - Apply least privilege: scope tokens to a single repo, remove cross-repo/org read where not strictly needed, prefer read-only tokens, and restrict issues:write. - Use architectural guardrails: sandbox agent tools, sanitize inputs, and add an output scanning/detection step before posting. - Update and audit workflows/templates to eliminate prompt-to-shell or prompt-to-sensitive-sink paths; adopt patched/safer templates and regularly review action configurations for AWI exposure.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — CISA orders feds to prioritize patching Langflow auth bypass flaw

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-prioritize-patching-langflow-auth-bypass-flaw/>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) gave federal agencies until Friday to patch an actively exploited vulnerability in the Langflow visual framework for building AI agents. [...]

**Parallel AI Enrichment:**

- **Technical Details:** An authentication/authorization bypass in Langflow endpoints (notably the POST /api/v1/build_public_tmp/{flow_id}/flow public-flow build path) allows unauthenticated actors to build/trigger public flows and in some cases perform code injection, delete API keys or achieve unauthenticated RCE depending on the specific flaw and endpoint.
- **Affected Products:** Langflow (affected versions vary by advisory; at least reported as "Langflow versions 1.6.9 and prior" in an authoritative alert; earlier CVEs affected versions before 1.3.0).
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — public PoC/exploit(s) reported (examples: https://www.exploit-db.com/exploits/52597, GitHub advisory shows exploitation steps https://github.com/langflow-ai/langflow/security/advisories/GHSA-vwmf-pq79-vjvx).
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true — multiple authoritative sources report in-the-wild exploitation.
- **Threat Actors:** None known
- **Mitigation:** Apply vendor advisories/updates if available; otherwise limit exposure by restricting Langflow access from the internet, block or restrict the public-flow endpoints, isolate instances on internal networks, and rotate credentials/API keys after suspected compromise.
- **Vendor Advisory:** https://github.com/langflow-ai/langflow/security/advisories/GHSA-vwmf-pq79-vjvx

---

## 4. 🟠 Zero-Day — CISA Adds 4 Actively Exploited Adobe, Joomla, and Langflow Flaws to KEV

**CVE:** `CVE-2026-48282` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://thehackernews.com/2026/07/cisa-adds-4-actively-exploited-adobe.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added four security flaws to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

The vulnerabilities are listed below -


  CVE-2026-48282 (CVSS score: 10.0) - A path traversal vulnerability in Adobe ColdFusion that could lead to arbitrary code execution in the context of the

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal in Adobe ColdFusion allowing an attacker to send a specially crafted HTTP request to upload a malicious file to a web‑accessible location; the attacker then accesses the uploaded file via the web server to trigger execution of arbitrary code in the context of the running user, enabling remote code execution and further host compromise.
- **Affected Products:** Adobe ColdFusion 2025 (update 10), Adobe ColdFusion 2023 (update 21)
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — weaponized exploit observed in the wild (sources: http://cisa.gov/news-events/alerts/2026/07/07/cisa-adds-one-known-exploited-vulnerability-catalog, http://securityweek.com/critical-adobe-coldfusion-vulnerability-exploited-in-attacks)
- **Patch Available:** true — Adobe released ColdFusion 2025 update 10 and ColdFusion 2023 update 21 (see reporting: http://securityweek.com/critical-adobe-coldfusion-vulnerability-exploited-in-attacks). Vendor advisory URL unavailable.
- **Active Exploitation:** true — confirmed (see CISA KEV addition and reporting)
- **Threat Actors:** None known
- **Mitigation:** Apply vendor patches immediately (ColdFusion 2025 update 10 or ColdFusion 2023 update 21). Prioritize remediation for internet‑exposed ColdFusion instances per CISA KEV guidance and investigate systems for prior compromise before patching; additionally, restrict access to admin interfaces and monitor web server logs for suspicious uploads (primary evidence supports patching and CISA prioritization).
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack class where adversarial instructions are embedded in external content (web pages, PDFs, URLs, documents). When an AI agent fetches, summarizes, or browses that content, the hidden instructions can influence or override the agent’s behavior (especially in high-trust contexts such as browser agents or automated summarization). IPI is realized via poisoned web content, hidden text, or crafted URLs that the agent treats as trusted input.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — public PoCs exist (example: https://github.com/brennanbrown/atlas-prompt-injection-poc; PayloadsAllTheThings prompt-injection entries).
- **Patch Available:** false — vendors have published mitigation guidance and layered defenses rather than a single downloadable patch.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: treat external content as untrusted; apply input sanitization/content filtering and provenance/trust checks; constrain and limit agent actions (least privilege); harden system prompts and avoid automatic sensitive operations; logging/monitoring and human-in-the-loop for risky actions.
- **Vendor Advisory:** https://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html, https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini, https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks, https://openai.com/index/designing-agents-to-resist-prompt-injection/

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an adversarial technique where attackers embed malicious instructions inside data sources, documents, URLs, or tools that an LLM consults while fulfilling a user query; the model can then follow those injected instructions or exfiltrate data across documents instead of following the user's intent. Attack paths include hidden/obfuscated payloads in documents, cross-document data exfiltration, and weaponized content served from third-party sites that LLM agents ingest during multi-source reasoning.
- **Affected Products:** Gemini (including Gemini in Google Drive), Gemini Advanced, NotebookLM Pro, Google Workspace apps using Gemini (Gmail, Docs editors, Drive, Chat) — specific versions unavailable
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — weaponized/observed payloads reported (see Forcepoint and independent researcher reports).
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: discovery/cataloging (human and automated red‑teaming, VRP), synthetic data generation to produce attack variants, deterministic controls (user confirmations, URL sanitization, tool-chaining policies, regex takedowns via a centralized policy engine), ML-based defenses retrained on synthetic/augmented data, LLM-based defenses via prompt/system-instruction tuning, and model hardening to improve the model’s ability to ignore embedded harmful instructions. Also run end-to-end simulations across Workspace apps to measure effectiveness and iterate.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** A cross-site scripting (XSS) weakness in Chrome's WebView tag / Gemini integration permits script injection into privileged/privileged‑context pages and can be abused by a malicious extension or web content to escalate privileges, access local files and exfiltrate data. Related research (GeminiJack) shows indirect prompt-injection techniques against Gemini agentic features that allow zero-click or hidden content to subvert agent prompts and force unsafe actions.
- **Affected Products:** Google Chrome (WebView tag / Gemini integration) — affected versions not specified
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Exploit Available:** true — PoC: https://github.com/fevar54/CVE-2026-0628-POC
- **Patch Available:** true — Google has released a patch (see vendor advisory: http://security.googleblog.com/2025/12/architecting-security-for-agentic.html)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor patch / update Chrome immediately; follow Google's layered-defenses guidance (block/restrict prompt injections, restrict origin access, limit agentic features); remove or disable untrusted extensions and restrict Gemini/agentic browsing until patched.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow in CrabbyAVIF (an AVIF image codec used in Android). A specially crafted AVIF file could trigger the overflow and enable remote code execution; the issue was assigned CVE-2025-48530.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://source.android.com/docs/security/bulletin/2025-12-01 ; http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) hides malicious instructions inside external data sources (emails, documents, web pages, notifications). When a generative model ingests or summarizes that content, the hidden instructions can become part of the model's effective prompt and cause unintended behavior such as data exfiltration or unauthorized actions.
- **Affected Products:** Gemini app, Gemini in Workspace (Gmail, Docs editors, Drive, Chat)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — public PoC/research demonstrations reported (example coverage: https://devops.com/mozilla-shows-the-danger-of-indirect-prompt-injections-in-ai-coding-agents/)
- **Patch Available:** false
- **Active Exploitation:** true — industry reports and lab write-ups describe IPI techniques being observed/exploited in 2025–2026 (examples: Vectra, HelpNetSecurity, SafeBreach)
- **Threat Actors:** None known
- **Mitigation:** Layered mitigations: model resilience/adversarial robustness, prompt-injection content classifiers, security-thought reinforcement, markdown sanitization, suspicious-URL redaction, user-confirmation framework (HITL) for sensitive actions, and monitoring/rapid response.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors target large backbone / provider-edge / customer-edge routers and use compromised devices and trusted interconnections to pivot; they modify router configuration and infrastructure (examples in the advisory include modified ACLs) to maintain persistent, long-term access and exfiltrate data.
- **Affected Products:** Cisco, Palo Alto, Ivanti, Fortinet (potential), Juniper, Microsoft Exchange (specific versions not provided)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false (no public PoC/weaponized exploit found; CISA states exploitation of zero-day vulnerabilities has not been observed) https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a
- **Patch Available:** false (no single official vendor patch/remediation published in response to the campaign as described in the advisory)
- **Active Exploitation:** true (CISA reports these PRC-aligned actors are targeting and compromising networks globally; note: CISA also states exploitation of zero-day vulnerabilities has not been observed)
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Use vendor-recommended device OS versions and keep them updated; upgrade unsupported devices; compare firmware/image hashes to vendor-provided values and enable signed image enforcement; restrict and monitor management-plane access and trusted connections; segment networks and apply least privilege for management.
- **Vendor Advisory:** Vendor advisory URL unavailable.

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

## 14. 🟠 Zero-Day — CrowdStrike Uncovers New Prompt Injection Techniques

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jul 07, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-uncovers-new-prompt-injection-techniques/>

---

## 15. 🟠 Zero-Day — Designing for the inevitable: System prompt leakage and mitigations in generative AI applications

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** AWS Security Blog &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://aws.amazon.com/blogs/security/designing-for-the-inevitable-system-prompt-leakage-and-mitigations-in-generative-ai-applications/>

> System prompts form the foundation of generative AI applications. A system prompt is a collection of instructions and operational context provided to a large language model (LLM) that shapes how the model behaves and interacts with users and tools. System prompts often contain proprietary information, including role definitions, behavioral guidelines, tool descriptions and usage instructions, […]

---

## 16. 🟠 Zero-Day — CISA orders feds to patch max severity ColdFusion flaw by Friday

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-max-severity-coldfusion-flaw-by-friday/>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has ordered government agencies to patch an actively exploited maximum-severity flaw in the Adobe ColdFusion commercial web app development platform by Friday. [...]

---

## 17. 🟡 High Severity — Serena: Unauthenticated Flask dashboard on fixed port enables DNS rebinding → memory poisoning → RCE

**CVE:** `CVE-2026-49471` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://github.com/advisories/GHSA-37h2-6p4f-mp3q>

> ### Summary

Serena&#x27;s built-in web dashboard exposes an unauthenticated Flask API on a fixed, predictable port (TCP 24282, hardcoded as `0x5EDA` in `constants.py`). The server has no authentication, no CSRF protection, and no Host header validation. A DNS rebinding attack allows a malicious webpage to reach this API from any browser and write arbitrary content to the agent&#x27;s persistent m…

---

## 18. 🟡 High Severity — NL Portal: IDOR allows any authenticated user to complete and tamper with another user's taak

**CVE:** `CVE-2026-49464` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://github.com/advisories/GHSA-6h3c-r723-7fx3>

> ## Impact

In versions from 1.5.0 up to and including 3.0.0, any authenticated portal user could complete and tamper with another user&#x27;s open task by submitting it on their behalf. The task submission endpoint accepted a task ID and a payload, but it never checked whether the task actually belonged to the user making the call.

An attacker who held a valid login (a normal `burger` OAuth token…

---

## 19. 🟡 High Severity — NL Portal: Missing per-user authorization on document and decision GraphQL queries in nl-portal-backend-libraries

**CVE:** `CVE-2026-49463` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://github.com/advisories/GHSA-qpm9-h556-mwxm>

> ## Impact

In versions up to and including 3.0.0, two parts of the GraphQL API returned data without checking whether the data belonged to the logged-in user:

- **Document content.** A logged-in user could download the raw content of any document by its ID, regardless of who owned it. The resolver has lacked an authentication parameter since the initial commit of the project (2022-11-22) — so eve…

---

## 20. 🟡 High Severity — Joro: Unauthenticated Cross-Origin Plugin Upload Leads to RCE

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

## 21. 🟡 High Severity — DSpace has possible Remote Code Execution (RCE)  through Velocity Templates used by LDN

**CVE:** `CVE-2026-49832` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://github.com/advisories/GHSA-9x82-rm84-c6x7>

> ## Overview

Remote Code Execution (RCE) is possible via Velocity Templates used by DSpace for [COAR Notify/LDN messages](https://wiki.lyrasis.org/spaces/DSDOC9x/pages/379126679/COAR+Notify). _This vulnerability impacts DSpace versions 8.0 &lt;= 8.3, 9.0 &lt;= 9.2._ The attacker MUST already have DSpace administrator credentials in order to perform the attack.

This attack is related to the path t…

---

## 22. 🟡 High Severity — Nuclio: Unsanitized cron trigger event headers/body injected into CronJob shell command leads to persistent RCE

**CVE:** `CVE-2026-52831` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://github.com/advisories/GHSA-v5px-423j-pf7p>

> ## Summary

Nuclio controller builds a `curl` invocation string for each cron trigger and stores it as the `args` of a Kubernetes CronJob container (`/bin/sh`, `-c`, `&lt;command&gt;`). Two fields in the trigger specification flow into this string without adequate sanitization:

- `event.headers` keys — interpolated verbatim inside double-quoted `--header` arguments (`lazy.go:2150`); any key conta…

---

## 23. 🟡 High Severity — async-tar PAX extension-header desync enables tar entry/content smuggling

**CVE:** `CVE-2026-53600` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://github.com/advisories/GHSA-35rm-7j9c-2f7m>

> ## Summary

`async-tar` v0.6.0 mis-applies a buffered PAX `size` extension to an intermediary
extension header (a GNU longname `L`, a GNU longlink `K`, or a PAX `x`/`g`
header) instead of to the next *file* entry. POSIX requires a PAX extended-header
record set to describe the next file entry, never an intervening extension
header. Because `poll_next_raw` (`src/archive.rs`) threads the buffered PA…

---

## 24. 🟡 High Severity — Ubiquiti Patches Critical UniFi Flaws Across Connect, Talk, Access, Protect, and OS

**CVE:** `CVE-2026-50746` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://thehackernews.com/2026/07/ubiquiti-patches-critical-unifi-flaws.html>

> Ubiquiti has shipped updates to address multiple critical security flaws impacting UniFi Connect, UniFi Talk, UniFi Access, UniFi Protect, and UniFi OS that could result in privilege escalation and arbitrary command execution.

The list of vulnerabilities is as follows -


  CVE-2026-50746 (CVSS score: 10.0) - An improper access control vulnerability in UniFi Connect Application that an attacker

---

## 25. 🟡 High Severity — 15-Year-Old GhostLock Flaw Enables Root and Container Escape on Most Linux Distros

**CVE:** `CVE-2026-43499` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://thehackernews.com/2026/07/15-year-old-ghostlock-flaw-enables-root.html>

> Researchers at Nebula Security have disclosed GhostLock (CVE-2026-43499), a 15-year-old Linux kernel flaw that lets any logged-in user take full root control of a machine that has not been patched.

The vulnerable code has shipped by default in essentially every mainstream distribution since 2011. The flaw needs no special permission, no unusual settings, and no network

---

## 26. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
