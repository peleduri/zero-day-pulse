# Zero Day Pulse

> **Generated:** 2026-07-10 19:18 UTC &nbsp;|&nbsp; **Total:** 27 &nbsp;|&nbsp; 🔴 KEV: 2 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 13 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🔴 CISA KEV — CVE-2026-56291 — Balbooa Forms Unrestricted Upload of File with Dangerous Type Vulnerability

**CVE:** `CVE-2026-56291` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-56291>

> Vendor: Balbooa | Product: Forms. Balbooa Forms contains an unrestricted upload of file with dangerous type vulnerability that allows an unauthenticated arbitrary file upload which could allow uploading of executable files leading to full RCE. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on …

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is an unauthenticated arbitrary file upload that allows attackers to upload executable files (such as PHP files), leading to full remote code execution (RCE).
- **Affected Products:** Balbooa Forms (com_baforms) up to version 2.4.0
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H/E:A/AU:Y/U:Red
- **Exploit Available:** true (https://mysites.guru/blog/balbooa-forms-unauthenticated-file-upload-flaw/)
- **Patch Available:** true (Version 2.4.1)
- **Active Exploitation:** true (CISA KEV)
- **Threat Actors:** None known
- **Mitigation:** Update Balbooa Forms to version 2.4.1 or newer.
- **Vendor Advisory:** https://mysites.guru/blog/balbooa-forms-unauthenticated-file-upload-flaw/

---

## 2. 🔴 CISA KEV — CVE-2026-48939 — iCagenda Unrestricted Upload of File with Dangerous Type Vulnerability

**CVE:** `CVE-2026-48939` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-48939>

> Vendor: iCagenda | Product: iCagenda. iCagenda contains an unrestricted upload of file with dangerous type vulnerability that allows the upload of arbitrary files in the file attachment feature, ultimately resulting in PHP code upload and execution. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Bas…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is an unrestricted upload of files with dangerous types in the file attachment feature of the iCagenda extension for Joomla, which allows the upload of arbitrary files and leads to PHP code execution.
- **Affected Products:** iCagenda extension for Joomla versions prior to 3.9.15 and 4.0.8
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (https://github.com/Polosss/By-Poloss..-..CVE-2026-48939)
- **Patch Available:** true (https://www.icagenda.com/docs/changelog/icagenda-3-9-15, https://www.icagenda.com/docs/changelog/icagenda-4-0-8)
- **Active Exploitation:** true (CISA KEV)
- **Threat Actors:** None known
- **Mitigation:** Update the iCagenda extension for Joomla to version 3.9.15 or 4.0.8.
- **Vendor Advisory:** https://www.icagenda.com/docs/changelog/icagenda-3-9-15, https://www.icagenda.com/docs/changelog/icagenda-4-0-8

---

## 3. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path traversal vulnerability that allows unauthenticated remote attackers to download arbitrary files from the SimpleHelp server host via crafted HTTP requests. This can be used to retrieve sensitive files such as serverconfig.xml, which contains hashed admin credentials and secrets.
- **Affected Products:** SimpleHelp remote support software v5.5.7 and before
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true. Proof-of-concept exists, including a Metasploit module (auxiliary/scanner/http/simplehelp_toolbox_path_traversal), as detailed at http://offsec.com/blog/cve-2024-57727
- **Patch Available:** true. Patches available in SimpleHelp versions 5.5.8 through 5.5.10, released between 8 and 13 January 2025.
- **Active Exploitation:** true. Reported by CISA (AA25-163a) and the vendor, noting exploitation by ransomware actors targeting MSP environments.
- **Threat Actors:** DragonForce, Medusa
- **Mitigation:** Upgrade to SimpleHelp v5.5.8 or later; change Administrator and Technician account passwords; restrict IP addresses for logins and API requests; disable the SimpleHelpAdmin user and local Technician account logins in favor of AD/LDAP authentication; and restrict firewall access to the SimpleHelp server.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI): AI systems that process external content (webpages, documents, email) can encounter embedded malicious instructions; when the model follows those instructions instead of the user's intent it can be manipulated. Observed goals include harmless pranks, SEO manipulation, deterrence (e.g., infinite text streams), data exfiltration, and destructive actions. Detection is difficult due to abundant benign examples and contextual ambiguity.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — public PoCs/demos exist (example: https://github.com/brennanbrown/atlas-prompt-injection-poc).
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses: pattern-based filtering to find candidate content, LLM-based contextual classification (to judge intent and placement), human validation for high-confidence triage; product hardening (model safeguards, red-team testing), threat intelligence sharing and vulnerability reward programs.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) allows an attacker to influence the behavior of a Large Language Model (LLM) by injecting malicious instructions into the data or tools the LLM accesses while completing a user's query. This can occur even without direct user input.
- **Affected Products:** Workspace with Gemini, Gemini Advanced, Gemini in Google Drive, NotebookLM PRO
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (Researcher report in http://kenhuangus.substack.com/p/indirect-prompt-injection-with-cross)
- **Patch Available:** true (Ongoing continuous mitigation described in http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html)
- **Active Exploitation:** true (Confirmed by reports of payloads caught in the wild in Doc 18 and status reports in Doc 13)
- **Threat Actors:** None known
- **Mitigation:** Google employs a layered defense strategy including: deterministic defenses (user confirmation, URL sanitization, tool chaining policies), ML-based defenses (retraining models using synthetic attack data), LLM-based defenses (refined system prompt engineering), and model hardening to improve the internal capability of Gemini to disregard harmful embedded commands.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: untrusted web content (malicious pages, third‑party iframes, or user-generated content) can influence an agentic planner model in Chrome to take unwanted actions (e.g., initiate financial transactions or exfiltrate sensitive data) by injecting prompts or malicious instructions into the content the model ingests. Chrome’s agentic design shares only task-relevant frames with the planner, but without strong isolation an agent compromised via prompt injection could act across origins or produce model-generated URLs that leak data.
- **Affected Products:** Google Chrome (agentic features / Gemini integration) — no specific versions provided.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses described by Google: an isolated User Alignment Critic to vet agent actions; Agent Origin Sets / origin-isolation to restrict which origins the agent may access; deterministic checks on model-generated URLs; a prompt-injection classifier running in parallel with the planner; user confirmations for critical steps; continuous red-teaming, monitoring and response; Chrome auto-update rollouts; and updated VRP guidance for reporting.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow and out-of-bounds (OOB) access vulnerability in the CrabbyAVIF Avif parser/decoder, leading to potential remote code execution (RCE).
- **Affected Products:** Android 16, CrabbyAVIF
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (Security patch level 2025-08-05)
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Update to the August 2025 Android security patch level (2025-08-05).
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injections involve hidden malicious instructions placed within external data sources (such as emails, documents, or calendar invites) that the AI processes, allowing the attacker to manipulate the AI to exfiltrate data or execute unauthorized actions.
- **Affected Products:** Gemini app, Gemini in Gmail, Gemini in Docs editors, Gemini in Drive, Gemini in Chat
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html)
- **Active Exploitation:** true (Google reports that their layered protections have consistently mitigated indirect prompt injection attempts)
- **Threat Actors:** None known
- **Mitigation:** Google uses a layered defense strategy including prompt injection content classifiers, security thought reinforcement, markdown sanitization, suspicious URL redaction, and a user confirmation framework.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Chinese state-sponsored actors exploit publicly known vulnerabilities (CVEs) in network edge devices, such as backbone and customer routers, to gain initial access. Once inside, they maintain persistence and conduct espionage by modifying routing tables, utilizing traffic mirroring (SPAN/RSPAN), establishing GRE/IPsec tunnels, and abusing Guest Shell containers on Cisco devices to execute scripts and stage data for exfiltration.
- **Affected Products:** Cisco IOS XE, Cisco IOS, Ivanti Connect Secure, Ivanti Policy Secure, Palo Alto Networks PAN-OS GlobalProtect, Fortinet firewalls, Juniper firewalls, Microsoft Exchange, Nokia routers and switches, Sierra Wireless devices, Sonicwall firewalls
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (Publicly available code and tools such as siet.py, map.tcl, tclproxy.tcl, and wodSSHServer are mentioned in the advisory)
- **Patch Available:** true (Patches are available for the exploited CVEs listed in the advisory, such as CVE-2023-20198, CVE-2018-0171, and CVE-2024-21887)
- **Active Exploitation:** true (CISA Alert AA25-239A confirms that PRC state-sponsored cyber threat actors are targeting networks globally)
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching the identified CVEs (e.g., CVE-2023-20198, CVE-2018-0171, CVE-2024-21887), upgrade unsupported network devices to supported ones, harden supply chain security, and monitor for anomalous outbound network traffic.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** The campaign utilized the weaponization of an Outlook NTLM vulnerability (CVE-2023-23397) to collect NTLM hashes from targets.
- **Affected Products:** Microsoft Outlook
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true; CISA Advisory AA25-141A reports a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies.
- **Threat Actors:** GRU unit 26165, APT-28
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

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

## 15. 🟡 High Severity — MCP Atlassian: DNS-rebinding TOCTOU bypass of the SSRF fix (CVE-2026-27826)

**CVE:** `CVE-2026-27826` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-489g-7rxv-6c8q>

> ### Summary
GHSA-7r34-79r5-rcc9&#x27;s fix added `validate_url_for_ssrf`, which resolves the attacker-controlled `X-Atlassian-{Jira,Confluence}-Url` header host **once at middleware time** and trusts the result. But the outbound request is later built with the **raw hostname** and **re-resolves at connect time with no IP pinning**. An attacker-controlled rebinding DNS name returns a public IP on t…

---

## 16. 🟡 High Severity — Kimai has Server-Side Request Forgery in Invoice PDF Rendering via Markdown Image URLs

**CVE:** `CVE-2026-49865` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-pj8j-p4g4-4vw8>

> ### Summary

Kimai 2.56.0 contains a server-side request forgery vulnerability in its invoice PDF preview and generation workflow. If an attacker can control Markdown content that is later rendered into an invoice PDF, such as `Customer.invoiceText`, the server-side PDF renderer will fetch remote image URLs embedded in Markdown image syntax.

This allows the application server to issue outbound re…

---

## 17. 🟡 High Severity — API Platform Core vulnerable to cross-user attribute leak in JSON:API and HAL item normalizers due to missing isCacheKeySafe gate

**CVE:** `CVE-2026-49858` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-pjhx-3c3w-9v23>

> ### Impact

`#[ApiProperty(security: ...)]` is evaluated per request to decide whether a property is exposed. The `componentsCache` arrays in `ApiPlatform\JsonApi\Serializer\ItemNormalizer` and `ApiPlatform\Hal\Serializer\ItemNormalizer` are keyed on `$context[&#x27;cache_key&#x27;]`, which is set unconditionally before delegating to the parent normalizer. The component structure (attributes, rela…

---

## 18. 🟡 High Severity — Tesla vulnerable to atom exhaustion via untrusted URL scheme

**CVE:** `CVE-2026-48597` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-h74c-q9j7-mpcm>

> ### Summary

In the Mint adapter for the Tesla HTTP client library, `Tesla.Adapter.Mint.open_conn/2` passes the URL scheme of every outgoing request through `String.to_atom/1` with no allow-list validation. Because BEAM atoms are permanent (never garbage-collected) and the atom table is bounded at roughly 1,048,576 entries, an attacker who can vary the URL scheme across requests can mint one fresh…

---

## 19. 🟡 High Severity — Tesla: Authorization header leaks on cross-origin redirect via case-sensitive filtering

**CVE:** `CVE-2026-48595` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-9m9w-gxf7-rh8m>

> ### Summary

`Tesla.Middleware.FollowRedirects` is meant to strip the `Authorization` header when following a cross-origin redirect, but performs the check with a case-sensitive comparison against the lowercase string `&quot;authorization&quot;`. Because Tesla preserves header keys exactly as supplied by the caller, any application that sets the header with its RFC 7235 canonical casing (`&quot;Au…

---

## 20. 🟡 High Severity — Tesla has CRLF injection in request `Content-Type` header via `add_content_type_param`

**CVE:** `CVE-2026-48596` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-10
**Reference:** <https://github.com/advisories/GHSA-q7jx-v53g-848w>

> ### Summary

`Tesla.Multipart.add_content_type_param/2` appends caller-supplied strings to the multipart `Content-Type` header with no validation. A param value containing `\r\n` splits the header line, allowing an attacker who controls any content-type parameter (charset, boundary parameter, etc.) to inject arbitrary headers into the outbound HTTP request.

### Details

`add_content_type_param/2`…

---

## 21. 🟡 High Severity — sigstore-go has a multi-log threshold bypass via single compromised log

**CVE:** `CVE-2026-49834` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-9vcr-p3rj-q5q6>

> ### Impact
_What kind of vulnerability is it? Who is impacted?_

A verifier configured with WithTransparencyLog(N&gt;1) or WithSignedCertificateTimestamps(N&gt;1) expected defense-in-depth against the compromise of a single log instance. However, threshold counting counted verified witnesses per-entry or per-validation-path rather than per-log-authority.

As a result, a single compromised transpar…

---

## 22. 🟡 High Severity — mint: Unbounded CONTINUATION/HEADERS frame accumulation (CONTINUATION flood)

**CVE:** `CVE-2026-49754` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-2p26-p43x-fhp8>

> ### Summary

Mint&#x27;s HTTP/2 client accumulates `CONTINUATION` header-block fragments into a per-connection buffer with no cap on size or frame count. A malicious or compromised HTTP/2 server can drive the client&#x27;s memory to arbitrary size by streaming an endless chain of `CONTINUATION` frames after a `HEADERS` frame that omits `END_HEADERS`, causing memory exhaustion and BEAM process deat…

---

## 23. 🟡 High Severity — mint: Content-Length header accepts non-RFC "+" sign prefix

**CVE:** `CVE-2026-49753` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-mjqx-c6f6-7rc2>

> ### Summary

Mint&#x27;s HTTP/1 client accepts `Content-Length` header values with a leading `+` sign (e.g. `+0`, `+123`), which RFC 7230 forbids (`Content-Length = 1*DIGIT`). On a connection shared with a strict fronting proxy or load balancer, this parser disagreement is a response-smuggling primitive: the proxy frames the body one way, Mint frames it another, and bytes meant for one response le…

---

## 24. 🟡 High Severity — YesWiki has Unsafe eval() in its Formula Calculato, Leading to Remote Code Execution & Denial of Service

**CVE:** `CVE-2026-52778` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-px5m-h76g-p7p8>

> ### Summary

An unsafe execution vulnerability exists in the Bazar form field calculator (CalcField.php) of YesWiki. The application attempts to sanitize user-defined mathematical formulas using a complex recursive regular expression before passing them to the PHP eval() function. This implementation is inherently flawed: it is vulnerable to Regular Expression Denial of Service (ReDoS / Stack Over…

---

## 25. 🟡 High Severity — YesWiki: Authenticated (Admin) Server-Side Template Injection to Remote Code Execution via Bazar Semantic Templates

**CVE:** `CVE-2026-52762` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-65p8-9433-jpcp>

> ### Summary
YesWiki Bazar contains a stored Server-Side Template Injection (`SSTI`) vulnerability in the semantic template feature that can be escalated to confirmed Remote Code Execution (`RCE`). An authenticated administrator can place arbitrary Twig expressions into the `Semantic template (Twig)` field (`bn_sem_template`), and that content is later executed server-side when public semantic endp…

---

## 26. 🟡 High Severity — laravel-backup-restore has an OS Command Injection during database restore

**CVE:** `CVE-2026-53932` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-09
**Reference:** <https://github.com/advisories/GHSA-w9mx-xmg4-gc4r>

> ## Summary
A crafted backup archive can trigger OS command injection during database restore. The restore workflow extracts a ZIP archive, enumerates files under `db-dumps`, converts the dump path to an absolute path, and passes that path into database import commands that are built as shell command strings.

The dump filename is not shell-escaped before it is interpolated into commands such as:

…

---

## 27. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
