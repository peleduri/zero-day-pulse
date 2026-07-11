# Zero Day Pulse

> **Generated:** 2026-07-11 07:32 UTC &nbsp;|&nbsp; **Total:** 25 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 11 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** A set of unauthenticated path traversal (CWE-22) flaws in SimpleHelp (≤5.5.7) allow attackers to craft HTTP requests with directory-traversal payloads (e.g., ../../ sequences) to download arbitrary files from the host (including server configuration, hashed passwords, private keys), enabling credential theft, privilege escalation, lateral movement and follow-on ransomware.
- **Affected Products:** SimpleHelp Remote Support / Remote Monitoring and Management (RMM) software — versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true — public proof-of-concept and Metasploit/Rapid7 module exist (e.g., OffSec writeup: https://www.offsec.com/blog/cve-2024-57727)
- **Patch Available:** true — vendor has released updated SimpleHelp versions addressing CVE-2024-57727 (see vendor advisory URL above)
- **Active Exploitation:** true — confirmed active exploitation reported by CISA and industry reporting
- **Threat Actors:** None known
- **Mitigation:** Immediate actions: isolate or stop any SimpleHelp 5.5.7-or-earlier servers from the internet; upgrade SimpleHelp to the vendor’s patched releases; apply vendor-recommended workarounds if patching is delayed (restrict inbound access, disable file-browsing features, firewall access, perform threat hunting and log review). Treat potentially exposed systems as compromised until verified.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — Weekly Metasploit Update: Exploits for FlowiseAI CSV Agent and MacOS Package Kit

**CVE:** `CVE-2026-41264` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-07-11
**Reference:** <https://www.rapid7.com/blog/post/pt-weekly-metasploit-update-exploits-for-flowiseai-csv-agent-and-macos-package-kit>

> More AI, more software, more bugs! AI, it&#x27;s all you hear about nowadays and everyone&#x27;s got an opinion on it. Here at Metasploit, we care less about those opinions and more about the growing attack surface all this new software brings with it (yeehaw exploits!). Take for example the new Flowise CSV Agent Prompt Injection RCE brought to you by Takahiro Yokoyama and zdi-disclosures. Flowise…

**Parallel AI Enrichment:**

- **Technical Details:** The CSV Agent node constructs prompts from untrusted CSV data and evaluates LLM-generated Python code without adequate sandboxing. An unauthenticated attacker who can send prompts (or control a chatflow/server response) can use prompt-injection to get the LLM to return a malicious Python script which the CSV Agent then executes via its run method, resulting in remote code execution as the user running the Flowise server.
- **Affected Products:** Flowise <= 3.0.13, flowise-components <= 3.0.13 (patched in 3.1.0)
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true — public PoC available (ZDI/Trend Micro PoC referenced in advisories) and Metasploit exploit module published (see Rapid7 Metasploit update)
- **Patch Available:** true — patched in Flowise 3.1.0 (see vendor advisory: https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-3hjv-c53m-58jj)
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Upgrade to Flowise 3.1.0 (vendor patch). If immediate upgrade is not possible: disable or remove CSV Agent nodes, run Flowise with least privilege and network isolation, block outbound connections from Flowise to untrusted model/response servers, and apply strict input validation / code-evaluation restrictions (the vendor fix disallows imports in the CSV Agent and hardens python-code validation).
- **Vendor Advisory:** https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-3hjv-c53m-58jj

---

## 3. 🟠 Zero-Day — mcp-atlassian: Arbitrary file read via missing path validation in confluence_upload_attachment

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-g5r6-gv6m-f5jv>

> ### Summary
`confluence_upload_attachment` passes `file_path` directly to `open(file_path, &quot;rb&quot;)` with no path validation. Any authenticated MCP client — or an AI agent manipulated via prompt injection — can read any file the server process can access and exfiltrate it to Confluence as an attachment.

### Details
Root cause: `src/mcp_atlassian/confluence/attachments.py`, `_upload_attachm…

**Parallel AI Enrichment:**

- **Technical Details:** confluence_upload_attachment passes an attacker-controlled file_path directly to open(file_path, "rb") without path validation, allowing arbitrary file reads (e.g., /proc/self/environ, ~/.ssh/id_ed25519) which are then uploaded to Confluence as attachments. Root cause in src/mcp_atlassian/confluence/attachments.py: open(file_path, "rb") is called with no validate_safe_path() check.
- **Affected Products:** mcp-atlassian (< 0.22.0); patched in 0.22.0
- **CVSS Score:** 7.7
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Exploit Available:** true — public PoC / demonstration video referenced in advisory: https://github.com/advisories/GHSA-g5r6-gv6m-f5jv
- **Patch Available:** true — patched in mcp-atlassian 0.22.0 (see advisory: https://github.com/advisories/GHSA-g5r6-gv6m-f5jv)
- **Active Exploitation:** true — confirmed proof-of-concept and demonstrated exfiltration (including prompt-injection driven upload of /proc/self/environ) reported in the advisory: https://github.com/advisories/GHSA-g5r6-gv6m-f5jv
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor patch (upgrade to mcp-atlassian 0.22.0) or add validate_safe_path(file_path) before opening uploaded file paths. Also rotate any credentials/secrets if compromise is suspected and restrict or harden any AI-agent/tooling that can call the upload API.
- **Vendor Advisory:** https://github.com/advisories/GHSA-g5r6-gv6m-f5jv

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI): adversaries embed or ‘seed’ instructions in external content (web pages, files, calendar invites, etc.) that LLM-enabled agents ingest; the injected text can alter model behavior or contaminate outputs. PoC demos show how crafted HTML/text on live pages can influence AI-driven browsing/assistant flows.
- **Affected Products:** LLM-based agents and AI-enabled browsers/assistants (examples: Google Gemini and other AI browsing/assistant agents) — no product/version ranges published
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — public PoC available (e.g. https://github.com/brennanbrown/atlas-prompt-injection-poc)
- **Patch Available:** false
- **Active Exploitation:** true — observed in the wild (see Unit42, Forcepoint X‑Labs, HelpNetSecurity coverage)
- **Threat Actors:** None known
- **Mitigation:** Layered mitigations and hardening: reduce trust in unvetted external content, sanitize or filter content, restrict or require explicit user authorization for web/third-party browsing and actions, detection/blocking of known payload patterns, and vendor-side content-trust policies and model hardening (no single "patch" — a layered approach is recommended).
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is when adversarial instructions are hidden inside external data the LLM processes (web content, files, etc.), causing the model to follow the embedded malicious instructions instead of the user’s intent. Attack surface includes multi-source content and agentic automation. Defenses described include prompt-injection content classifiers, security-thought reinforcement, markdown sanitization and suspicious-URL redaction, user-confirmation framework, end-user security notifications, deterministic policy/config fixes, ML retraining, and model hardening.
- **Affected Products:** Gemini app, Gemini in Workspace apps (Gmail, Docs editors, Drive, Chat)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — public reports/payloads observed (see Unit42 and Forcepoint)
- **Patch Available:** false
- **Active Exploitation:** true — in-the-wild IPI activity and payloads reported
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses: prompt-injection content classifiers, security thought-reinforcement (surrounding system instructions), markdown sanitization and suspicious URL redaction (Safe Browsing), user confirmation framework (explicit approval for risky actions), end-user mitigation notifications, deterministic (config/policy) fixes for immediate threats, ML-based retraining with synthetic variant generation, and model hardening of Gemini.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (aka GeminiJack) — malicious web content can craft inputs that influence Gemini’s agentic behavior (an indirect prompt injection), causing the model/agent to perform or reveal privileged actions; public reporting tied this class of injection to CVE-2026-0628 in Chrome’s Gemini component, which allowed script injection into privileged contexts and (per disclosures) local file access and privacy invasion.
- **Affected Products:** Google Chrome (agentic browsing / Gemini integration), Google Gemini Enterprise, Google Workspace apps using Gemini (Gmail, Docs, Drive, Chat)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true; public PoC available: http://github.com/fevar54/CVE-2026-0628-POC
- **Patch Available:** true; vendor advisory / patch information: http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Apply the Chrome security update / patch, follow Google’s layered-defense guidance for Gemini in Workspace (update Workspace clients / services), and until patched limit or disable agentic browsing/Gemini integrations for high-risk users. Follow Google support guidance for Gemini in Gmail/Docs/Drive/Chat.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow in the CrabbyAVIF AVIF parser/decoder (unsafe Rust block led to incorrect bounds/OOB accesses) that could lead to memory corruption and potential remote code execution if reached; the issue was identified and not shipped.
- **Affected Products:** CrabbyAVIF (Android platform: platform/external/rust/crabbyavif) — specific affected Android OS versions not stated
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true (fix present in Android source: https://android.googlesource.com/platform/external/rust/crabbyavif/)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the patch/upgrade in Android's platform external/rust/crabbyavif (update to the patched CrabbyAVIF in the Android source or upstream CrabbyAvif); vendor guidance indicates the issue was fixed before shipping. No separate temporary mitigation guidance was published.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injections are hidden or embedded malicious instructions in external data sources (emails, files, calendar invites, URLs) that can manipulate an LLM’s output or cause it to exfiltrate data or perform unsafe actions when the model ingests that content. The attack leverages how prompts are composed from multiple content sources (user input + external content) and can be mitigated by content-classification, model hardening, sanitization, and human-in-the-loop confirmation.
- **Affected Products:** Gemini 2.5, Google Workspace (Gmail, Docs)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true — http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: adversarial model training / model hardening (Gemini 2.5), prompt-injection content classifiers to detect and filter malicious instructions, security-thought-reinforcement to steer the model, markdown sanitization and suspicious-URL redaction, contextual user confirmation (HITL) for risky actions, and end-user security notifications and help-center guidance.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state‑sponsored actors target backbone, provider‑edge (PE) and customer‑edge (CE) routers and other network‑edge devices; they leverage compromised devices and trusted interconnections to pivot, and they modify router configurations (including observed ACL naming patterns) to maintain persistent long‑term access and exfiltrate data.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Harden and upgrade network edge devices: upgrade unsupported devices to vendor‑supported hardware/software, apply strict hardening controls (disable or tightly restrict risky features), follow CISA detection/hunting guidance and network monitoring for configuration changes and unusual egress.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** An attacker can send a specially crafted email that contains a malicious external/UNC/SMB URL. When Outlook automatically attempts to retrieve or render the external content, it will authenticate to the attacker-controlled SMB/NTLM endpoint and leak Net-NTLMv2 authentication hashes, enabling credential theft, relay or offline cracking and subsequent lateral movement.
- **Affected Products:** Microsoft Outlook for Windows
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — public PoC exists (e.g., https://github.com/Trackflaw/CVE-2023-23397) and multiple vendors/industry reports document weaponization.
- **Patch Available:** true — Microsoft released security updates (see MSRC update guide: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23397)
- **Active Exploitation:** true
- **Threat Actors:** Russian GRU (85th GTsSS, Unit 26165 — tracked as APT28)
- **Mitigation:** Apply Microsoft security updates (March 14, 2023) immediately; follow Microsoft investigation and detection guidance; block or inspect outbound SMB/NTLM authentication to untrusted hosts; disable automatic retrieval of external content where feasible; monitor for NTLM authentication attempts to external hosts and investigate anomalous NTLM hashes.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23397

---

## 11. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

---

## 12. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 13. 🟠 Zero-Day — CrowdStrike Uncovers New Prompt Injection Techniques

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jul 07, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-uncovers-new-prompt-injection-techniques/>

---

## 14. 🟠 Zero-Day — Unpatched XRING Flaw in XQUIC Lets Remote Clients Crash HTTP/3 Servers

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://thehackernews.com/2026/07/unpatched-xring-flaw-in-xquic-lets.html>

> A single wrong variable on one line in XQUIC, Alibaba&#x27;s QUIC and HTTP/3 library, lets any remote client crash the server with a short burst of completely legal traffic. There is no patch.

FoxIO researcher Sébastien Féry disclosed the flaw on July 8 and nicknamed it XRING. He says it needs no login and no malformed packets: about 260 bytes of ordinary QPACK traffic takes the server

---

## 15. 🟡 High Severity — SiYuan: Stored XSS to RCE via Unsanitized Attribute View Asset Cell Content

**CVE:** `CVE-2026-50551` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-56mp-4f3v-fgj2>

> SiYuan v3.6.5 and earlier versions contain a stored cross-site scripting (XSS) vulnerability in the Attribute View (database) asset cell renderer that escalates to remote code execution (RCE) in the Electron desktop client. This is a neighbor-bug of CVE-2026-44588: the fix for -44588 used `escapeAriaLabel()` (double-escapes `&lt;`), but the AV asset renderers were left using the weaker `escapeAttr…

---

## 16. 🟡 High Severity — prestashop/ps_facetedsearch: PHP Object Injection in faceted search cache allows unauthenticated RCE

**CVE:** `CVE-2026-54159` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-m5f5-28qr-9g9r>

> ### Impact

A PHP Object Injection vulnerability affects the PrestaShop module `ps_facetedsearch`.

The module rebuilds the selected search filters from the request URL. The value of a slider filter (**price** or **weight**) is taken from the URL without sufficient validation, then stored in an internal filter-block cache where it is serialized and later read back with a raw native `unserialize()`…

---

## 17. 🟡 High Severity — SiYuan: Stored XSS to RCE via attribute-view cell rendering in genAVValueHTML()

**CVE:** `CVE-2026-54158` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-5xfx-xj4h-5p7r>

> ### Summary

The attribute-view (database) cell renderer `genAVValueHTML` interpolates cell content raw in four of its branches: `text`, `url`, `phone`, and `mAsset`. A cell value like `&lt;/textarea&gt;&lt;img src=x onerror=&quot;...&quot;&gt;` or `&quot;&gt;&lt;img src=x onerror=&quot;...&quot;&gt;` breaks out of its surrounding tag and runs arbitrary JavaScript in the renderer when the victim o…

---

## 18. 🟡 High Severity — File Browser: Command Injection via Authentication Hook Shell Substitution (Pre-Authentication RCE)

**CVE:** `CVE-2026-54088` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-m93h-4hw7-5qcm>

> ## Overview

The Hook Authentication feature in File Browser allows administrators to delegate login verification to an external shell command. User-supplied credentials (username and password) are interpolated into this command string using `os.Expand` without sanitization. An **unauthenticated remote attacker** can inject shell metacharacters in the username or password field at the login screen…

---

## 19. 🟡 High Severity — SiYuan: Unauthenticated Admin API Access via Blanket chrome-extension:// Origin Allowlist

**CVE:** `CVE-2026-54069` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-hvr9-72v2-fff3>

> ## Summary

SiYuan Note&#x27;s kernel HTTP server unconditionally trusts all `chrome-extension://` origins, granting `RoleAdministrator` access to every installed browser extension without any authentication. Combined with the default empty `AccessAuthCode` on desktop installs, any Chrome/Chromium extension -- including a compromised legitimate extension via supply chain attack -- can make fully a…

---

## 20. 🟡 High Severity — Authorizer: Unvalidated redirect_uri in /authorize leaks OAuth2 tokens to attacker-controlled URL

**CVE:** `CVE-2026-54072` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-h29v-hj44-q8cv>

> ## Summary

The `/authorize` endpoint accepts any `redirect_uri` without validating it against `AllowedOrigins`. When `response_type=token` or `response_type=id_token`, the server appends `access_token`, `id_token`, and `refresh_token` as query parameters and issues a 302 redirect to the attacker-supplied URL. An unauthenticated attacker can obtain the required `client_id` from the public `/graphq…

---

## 21. 🟡 High Severity — SiYuan: Stored XSS to RCE via CSS-snippet <style> breakout in renderSnippet()

**CVE:** `CVE-2026-54067` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-mvjr-vv3c-w4qv>

> ### Summary

A CSS snippet body containing `&lt;/style&gt;` breaks out of its surrounding `&lt;style&gt;` tag when `renderSnippet()` interpolates it via `insertAdjacentHTML`. A payload like `&lt;/style&gt;&lt;img src=x onerror=&quot;...&quot;&gt;` runs arbitrary JavaScript in the renderer. On Electron desktop builds the renderer runs with `nodeIntegration:true`, so `require(&#x27;child_process&#x2…

---

## 22. 🟡 High Severity — MCP Atlassian: DNS-rebinding TOCTOU bypass of the SSRF fix (CVE-2026-27826)

**CVE:** `CVE-2026-27826` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-489g-7rxv-6c8q>

> ### Summary
GHSA-7r34-79r5-rcc9&#x27;s fix added `validate_url_for_ssrf`, which resolves the attacker-controlled `X-Atlassian-{Jira,Confluence}-Url` header host **once at middleware time** and trusts the result. But the outbound request is later built with the **raw hostname** and **re-resolves at connect time with no IP pinning**. An attacker-controlled rebinding DNS name returns a public IP on t…

---

## 23. 🟡 High Severity — Kimai has Server-Side Request Forgery in Invoice PDF Rendering via Markdown Image URLs

**CVE:** `CVE-2026-49865` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-pj8j-p4g4-4vw8>

> ### Summary

Kimai 2.56.0 contains a server-side request forgery vulnerability in its invoice PDF preview and generation workflow. If an attacker can control Markdown content that is later rendered into an invoice PDF, such as `Customer.invoiceText`, the server-side PDF renderer will fetch remote image URLs embedded in Markdown image syntax.

This allows the application server to issue outbound re…

---

## 24. 🟡 High Severity — API Platform Core vulnerable to cross-user attribute leak in JSON:API and HAL item normalizers due to missing isCacheKeySafe gate

**CVE:** `CVE-2026-49858` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-pjhx-3c3w-9v23>

> ### Impact

`#[ApiProperty(security: ...)]` is evaluated per request to decide whether a property is exposed. The `componentsCache` arrays in `ApiPlatform\JsonApi\Serializer\ItemNormalizer` and `ApiPlatform\Hal\Serializer\ItemNormalizer` are keyed on `$context[&#x27;cache_key&#x27;]`, which is set unconditionally before delegating to the parent normalizer. The component structure (attributes, rela…

---

## 25. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
