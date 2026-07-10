# Zero Day Pulse

> **Generated:** 2026-07-10 13:56 UTC &nbsp;|&nbsp; **Total:** 23 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 13 &nbsp;|&nbsp; 🟡 High: 10 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** An unauthenticated path traversal vulnerability that allows remote attackers to download arbitrary files from the SimpleHelp host via crafted HTTP requests, including sensitive server configuration files (e.g., serverconfig.xml) containing hashed passwords and secrets.
- **Affected Products:** SimpleHelp remote support software v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (PoC available via OffSec blog and Metasploit module: https://www.offsec.com/blog/cve-2024-57727/)
- **Patch Available:** true (Fixed in SimpleHelp v5.5.8 and later; patches also available for v5.4.10 and v5.3.9)
- **Active Exploitation:** true (Reported by CISA in advisory AA25-163a and observed by the vendor to be exploited by ransomware groups DragonForce and Medusa)
- **Threat Actors:** Ransomware groups including DragonForce and Medusa
- **Mitigation:** Upgrade to SimpleHelp v5.5.8 or later. For older versions, apply the specific patches for v5.4.10 or v5.3.9. Additionally, change administrator and technician passwords, restrict technician/administrator logins to approved IP addresses, and disable the SimpleHelpAdmin user.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when attacker-controlled instructions are embedded in content (web pages, shared Docs, Calendar invites, emails) that a retrieval-augmented system or LLM reads; the model then treats those embedded instructions as legitimate and may follow them. In the GeminiJack case, an attacker could plant a shared Google Doc / Calendar / Gmail containing instructions that a Gemini Enterprise RAG pipeline retrieved into context; the model then interpreted and executed those instructions across permitted Workspace data sources and could exfiltrate results (for example, by loading results into an attacker-controlled external image URL).
- **Affected Products:** Google Gemini Enterprise, Vertex AI Search (VAIS) / Vertex AI Search RAG workflows, Google Workspace (Gmail, Google Calendar, Google Docs)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (Noma Labs disclosure / writeup: http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/)
- **Patch Available:** true (Google applied mitigations/updates; see Google Workspace advisory: http://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/ and Noma disclosure: http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Separation of services and RAG pipelines (e.g., separating Vertex AI Search from Gemini Enterprise), deterministic defenses (user confirmation, URL sanitization, tool-chaining policies and centralized policy engine / configuration updates), ML/LLM-based defenses and model hardening (retraining, prompt engineering to ignore embedded instructions), synthetic-attack-driven testing and monitoring, and limiting/trusting retrieval scopes (careful datasource configuration and monitoring).
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is a class of attack where an adversary injects malicious instructions into data or tools consumed by an LLM (for example, content in email, documents, web pages, or other integrated sources). The LLM can then be influenced to perform unauthorized actions or reveal data while fulfilling the user's query; this can occur without additional user input and is amplified by agentic automation and multiple data sources.
- **Affected Products:** Google Workspace (Gemini integration) — Gmail, Docs editors, Drive, Chat (no specific versions listed)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Google recommends a layered defense: built-in IPI defenses in Workspace/Gemini, content provenance and filtering, limiting or carefully configuring agentic automation, restricting untrusted external content sources, enforcing admin policies for Gemini in Workspace apps, and monitoring/alerting for anomalous LLM outputs. (Use Google's Workspace admin controls and layered protections while they continue to evolve.)
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection occurs when an AI agent processes content from an untrusted source (such as a malicious website) that contains instructions designed to hijack the model's behavior, potentially leading to unauthorized actions or data leakage.
- **Affected Products:** Google Chrome agentic browsing features (powered by Gemini)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (https://github.com/brennanbrown/atlas-prompt-injection-poc)
- **Patch Available:** true (http://security.googleblog.com/2025/12/architecting-security-for-agentic.html)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Implementation of layered defenses including blocking prompt injections, restricting origin access, and preventing unsafe AI actions.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A critical remote code execution vulnerability in the Android System caused by a linear buffer overflow (out-of-bounds access) in CrabbyAVIF due to incorrect bounds checks.
- **Affected Products:** Android System, CrabbyAVIF
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true (https://source.android.com/docs/security/bulletin/2025-08-01)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is a vulnerability where malicious instructions are hidden in external data sources (such as emails, websites, or documents) processed by an AI model. The model executes these embedded instructions along with its intended task, which can lead to unauthorized actions, such as data exfiltration or behavioral manipulation, without the user's knowledge.
- **Affected Products:** Gemini app, Gemini in Gmail, Gemini in Docs editors, Gemini in Drive, Gemini in Chat
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (SafeBreach Labs, Mozilla)
- **Patch Available:** true (Google's layered defense strategy and content classifier updates)
- **Active Exploitation:** true (Confirmed by Vectra AI and HelpNet Security as an active threat in the wild during 2025-2026)
- **Threat Actors:** None known
- **Mitigation:** Google employs a layered defense strategy including: 1) prompt injection content classifiers, 2) security thought reinforcement to prioritize security over adversarial instructions, 3) markdown sanitization and suspicious URL redaction, 4) a user confirmation framework (human-in-the-loop) for sensitive actions, and 5) model resilience through adversarial robustness.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Chinese state-sponsored actors target large backbone routers and provider/customer edge (PE/CE) routers and abuse trusted interconnections. They leverage compromised devices and management-plane features to pivot, modify router configurations (reports note ACLs often named "access-list 20"), and maintain long-term persistence for data collection and exfiltration. Analysts also cite chaining of known product vulnerabilities (e.g., Ivanti CVE-2024-21887) against edge devices as part of these campaigns.
- **Affected Products:** Cisco routers, Palo Alto Networks devices, Ivanti (Connect Secure / Policy Secure), Fortinet devices, Juniper devices, Microsoft Exchange
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Harden and monitor network-edge devices: upgrade unsupported devices, restrict and monitor management interfaces, segment networks and trusted connections, rotate credentials, monitor ACLs/routing policy (look for suspicious ACLs like "access-list 20"), disable or tightly harden risky features (e.g., GuestShell) if present, and apply vendor fixes for any specific CVEs when available.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** An elevation of privilege vulnerability in Microsoft Outlook that allows a threat actor to send a specially crafted email containing a malicious payload. This causes the victim's Outlook client to automatically initiate an SMB request, allowing the attacker to retrieve the victim's NetNTLMv2 hash.
- **Affected Products:** Microsoft Outlook
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (https://github.com/Trackflaw/CVE-2023-23397)
- **Patch Available:** true (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23397)
- **Active Exploitation:** true (CISA's Known Exploited Vulnerabilities Catalog; CISA Advisory AA25-141A)
- **Threat Actors:** Russian GRU military unit 26165 (APT28)
- **Mitigation:** Apply updates per vendor instructions.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23397

---

## 9. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** The blog recommends a moving target defense approach using JavaScript Language Randomization (JSLR) provided by CrowdStrike Falcon Secure Access to reduce risk from zero-day and unpatched N-day vulnerabilities.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 10. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

**Parallel AI Enrichment:**

- **Technical Details:** An unauthenticated remote OS command injection vulnerability in Ivanti Sentry that allows a remote attacker to achieve root-level access and full control over the appliance, enabling configuration alteration, credential theft, and lateral movement.
- **Affected Products:** Ivanti Sentry versions 10.5.1, 10.6.1, 10.7.0 and prior
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (Public PoC released June 10, 2026)
- **Patch Available:** true (Fixed in versions 10.5.2, 10.6.2 and 10.7.1; advisory: https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523)
- **Active Exploitation:** true (Confirmed by Shadowserver Foundation and Rapid7)
- **Threat Actors:** None known
- **Mitigation:** Update to Ivanti Sentry versions 10.5.2, 10.6.2, or 10.7.1.
- **Vendor Advisory:** https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523

---

## 11. 🟠 Zero-Day — CrowdStrike Uncovers New Prompt Injection Techniques

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jul 07, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-uncovers-new-prompt-injection-techniques/>

---

## 12. 🟠 Zero-Day — Unpatched XRING Flaw in XQUIC Lets Remote Clients Crash HTTP/3 Servers

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://thehackernews.com/2026/07/unpatched-xring-flaw-in-xquic-lets.html>

> A single wrong variable on one line in XQUIC, Alibaba&#x27;s QUIC and HTTP/3 library, lets any remote client crash the server with a short burst of completely legal traffic. There is no patch.

FoxIO researcher Sébastien Féry disclosed the flaw on July 8 and nicknamed it XRING. He says it needs no login and no malformed packets: about 260 bytes of ordinary QPACK traffic takes the server

---

## 13. 🟠 Zero-Day — Wiz in the Verizon DBIR: How AI Acceleration and Cloud Sprawl Impact Modern Defense

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Wiz Research &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://www.wiz.io/blog/verizon-dbir-2026-ai-cloud-security>

> Verizon&#x27;s latest DBIR highlights how attackers are exploiting familiar weaknesses at increasing speed and scale. Here&#x27;s what Wiz research reveals about vulnerabilities, trust relationships, and AI in modern cloud environments.

---

## 14. 🟡 High Severity — Tesla vulnerable to atom exhaustion via untrusted URL scheme

**CVE:** `CVE-2026-48597` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-h74c-q9j7-mpcm>

> ### Summary

In the Mint adapter for the Tesla HTTP client library, `Tesla.Adapter.Mint.open_conn/2` passes the URL scheme of every outgoing request through `String.to_atom/1` with no allow-list validation. Because BEAM atoms are permanent (never garbage-collected) and the atom table is bounded at roughly 1,048,576 entries, an attacker who can vary the URL scheme across requests can mint one fresh…

---

## 15. 🟡 High Severity — Tesla: Authorization header leaks on cross-origin redirect via case-sensitive filtering

**CVE:** `CVE-2026-48595` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-9m9w-gxf7-rh8m>

> ### Summary

`Tesla.Middleware.FollowRedirects` is meant to strip the `Authorization` header when following a cross-origin redirect, but performs the check with a case-sensitive comparison against the lowercase string `&quot;authorization&quot;`. Because Tesla preserves header keys exactly as supplied by the caller, any application that sets the header with its RFC 7235 canonical casing (`&quot;Au…

---

## 16. 🟡 High Severity — Tesla has CRLF injection in request `Content-Type` header via `add_content_type_param`

**CVE:** `CVE-2026-48596` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-q7jx-v53g-848w>

> ### Summary

`Tesla.Multipart.add_content_type_param/2` appends caller-supplied strings to the multipart `Content-Type` header with no validation. A param value containing `\r\n` splits the header line, allowing an attacker who controls any content-type parameter (charset, boundary parameter, etc.) to inject arbitrary headers into the outbound HTTP request.

### Details

`add_content_type_param/2`…

---

## 17. 🟡 High Severity — sigstore-go has a multi-log threshold bypass via single compromised log

**CVE:** `CVE-2026-49834` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-9vcr-p3rj-q5q6>

> ### Impact
_What kind of vulnerability is it? Who is impacted?_

A verifier configured with WithTransparencyLog(N&gt;1) or WithSignedCertificateTimestamps(N&gt;1) expected defense-in-depth against the compromise of a single log instance. However, threshold counting counted verified witnesses per-entry or per-validation-path rather than per-log-authority.

As a result, a single compromised transpar…

---

## 18. 🟡 High Severity — mint: Unbounded CONTINUATION/HEADERS frame accumulation (CONTINUATION flood)

**CVE:** `CVE-2026-49754` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-2p26-p43x-fhp8>

> ### Summary

Mint&#x27;s HTTP/2 client accumulates `CONTINUATION` header-block fragments into a per-connection buffer with no cap on size or frame count. A malicious or compromised HTTP/2 server can drive the client&#x27;s memory to arbitrary size by streaming an endless chain of `CONTINUATION` frames after a `HEADERS` frame that omits `END_HEADERS`, causing memory exhaustion and BEAM process deat…

---

## 19. 🟡 High Severity — mint: Content-Length header accepts non-RFC "+" sign prefix

**CVE:** `CVE-2026-49753` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-mjqx-c6f6-7rc2>

> ### Summary

Mint&#x27;s HTTP/1 client accepts `Content-Length` header values with a leading `+` sign (e.g. `+0`, `+123`), which RFC 7230 forbids (`Content-Length = 1*DIGIT`). On a connection shared with a strict fronting proxy or load balancer, this parser disagreement is a response-smuggling primitive: the proxy frames the body one way, Mint frames it another, and bytes meant for one response le…

---

## 20. 🟡 High Severity — YesWiki has Unsafe eval() in its Formula Calculato, Leading to Remote Code Execution & Denial of Service

**CVE:** `CVE-2026-52778` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-px5m-h76g-p7p8>

> ### Summary

An unsafe execution vulnerability exists in the Bazar form field calculator (CalcField.php) of YesWiki. The application attempts to sanitize user-defined mathematical formulas using a complex recursive regular expression before passing them to the PHP eval() function. This implementation is inherently flawed: it is vulnerable to Regular Expression Denial of Service (ReDoS / Stack Over…

---

## 21. 🟡 High Severity — YesWiki: Authenticated (Admin) Server-Side Template Injection to Remote Code Execution via Bazar Semantic Templates

**CVE:** `CVE-2026-52762` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-65p8-9433-jpcp>

> ### Summary
YesWiki Bazar contains a stored Server-Side Template Injection (`SSTI`) vulnerability in the semantic template feature that can be escalated to confirmed Remote Code Execution (`RCE`). An authenticated administrator can place arbitrary Twig expressions into the `Semantic template (Twig)` field (`bn_sem_template`), and that content is later executed server-side when public semantic endp…

---

## 22. 🟡 High Severity — laravel-backup-restore has an OS Command Injection during database restore

**CVE:** `CVE-2026-53932` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-w9mx-xmg4-gc4r>

> ## Summary
A crafted backup archive can trigger OS command injection during database restore. The restore workflow extracts a ZIP archive, enumerates files under `db-dumps`, converts the dump path to an absolute path, and passes that path into database import commands that are built as shell command strings.

The dump filename is not shell-escaped before it is interpolated into commands such as:

…

---

## 23. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
