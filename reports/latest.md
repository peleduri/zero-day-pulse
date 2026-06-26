# Zero Day Pulse

> **Generated:** 2026-06-26 19:28 UTC &nbsp;|&nbsp; **Total:** 28 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 11 &nbsp;|&nbsp; 🟡 High: 17 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is a path traversal flaw that allows unauthenticated remote attackers to read or download arbitrary files from the SimpleHelp host via crafted HTTP requests.
- **Affected Products:** SimpleHelp remote support software v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (https://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability)
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors
- **Mitigation:** Apply the vendor patch or upgrade to a version newer than 5.5.7; if a patch is not available, disable remote access and restrict network access to the SimpleHelp service.
- **Vendor Advisory:** https://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — First-Ever Exploitation of PTC Windchill Vulnerability Discovered in the Wild

**CVE:** `CVE-2026-12569` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://www.securityweek.com/first-ever-exploitation-of-ptc-windchill-vulnerability-discovered-in-the-wild/>

> CISA has added the remote code execution flaw CVE-2026-12569 to its Known Exploited Vulnerabilities catalog. The post First-Ever Exploitation of PTC Windchill Vulnerability Discovered in the Wild appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Improper input validation/deserialization of untrusted data in Windchill PDMLink and FlexPLM allows an unauthenticated remote attacker to send crafted requests/serialized data that result in remote code execution.
- **Affected Products:** PTC Windchill PDMLink (versions prior to 11.0 M030 and specified patched versions listed by vendor), PTC FlexPLM (versions prior to 11.0 M030 and specified patched versions listed by vendor), CPS (impacted; versions not specified)
- **CVSS Score:** 9.3
- **CVSS Vector:** CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:L/SI:L/SA:L/S:X/AU:Y/R:U/V:C/U:Red
- **Exploit Available:** false
- **Patch Available:** true (PTC published patches and guidance: vendor advisory URL above and support article CS473270)
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Follow PTC remediation guidance and apply the vendor patches immediately; for releases prior to 11.0 M030, ensure the system is not connected to the internet to reduce exposure and follow the vendor workaround CS473493 as applicable.
- **Vendor Advisory:** https://www.ptc.com/en/about/trust-center/advisory-center/active-advisories/windchill-flexplm-rce-vulnerability

---

## 3. 🟠 Zero-Day — Google Details Turla's New STOCKSTAY Backdoor Used in Ukraine Espionage Attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://thehackernews.com/2026/06/google-details-turlas-new-stockstay.html>

> The Russian state-sponsored threat actor known as Turla has been attributed to a previously undocumented .NET backdoor called STOCKSTAY that has been deployed against government and military organizations in Ukraine, and entities that have an interest in Italian foreign policy.

Describing the Windows backdoor as continually developed by the hacking group, Google Threat Intelligence Group (

**Parallel AI Enrichment:**

- **Technical Details:** STOCKSTAY is a modular .NET backdoor composed of a tunneler, orchestrator, and backdoor that communicate locally and beacon over WebSocket C2, using legitimate platforms like Render and GitHub for hosting. Initial access is achieved via spear‑phishing RDP files and RAR archives exploiting CVE‑2025‑8088 (WinRAR path traversal). Payloads employ environmental keying and are scheduled to run during business hours to blend with normal activity.
- **Affected Products:** Windows OS, .NET Framework, WinRAR (CVE-2025-8088)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Turla (aka SUMMIT, Secret Blizzard, VENOMOUS BEAR, UAC-0194)
- **Mitigation:** Patch WinRAR to remediate CVE‑2025‑8088, block inbound RDP files at email gateways, enforce DMARC/SPF, hunt for WebSocket connections to *.onrender.com and the websocket‑sharp.dll component, and deploy YARA rules and GTI IOC collections.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) embeds malicious prompts in web content that AI agents retrieve and process, causing the agents to follow unintended instructions.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (http://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads)
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack where an adversary injects malicious instructions into the data, tools, or external knowledge sources used by an LLM, causing the model to follow unintended commands without direct user input.
- **Affected Products:** Google Workspace (including Gemini integration)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Implement input and output validation and sanitization, enforce human oversight, continuously monitor public web for IPI patterns, and apply Google Workspace's continuous mitigation framework.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** In Cursor versions below 1.3 an attacker can bypass an allowlist in auto-run mode by using special input (e.g., a backtick ` or $(cmd)) to trigger command execution outside the allowlist; an attacker can trigger this when chained with indirect prompt injection, resulting in arbitrary command execution. (Fixed in 1.3.)
- **Affected Products:** Cursor (code editor) versions below 1.3
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true — fixed in Cursor version 1.3 (see vendor advisory: https://github.com/cursor/cursor/security/advisories/GHSA-534m-3w6r-8pqr)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Update Cursor to version 1.3 or later. If update is not immediately possible, avoid using allowlist/auto-run modes and keep the default setting that requires user approval for terminal/command execution.
- **Vendor Advisory:** https://github.com/cursor/cursor/security/advisories/GHSA-534m-3w6r-8pqr

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow in the Rust‑based CrabbyAVIF library was discovered but prevented by Android's Scudo hardened allocator guard pages, making the bug non‑exploitable.
- **Affected Products:** Android platform (CrabbyAVIF library)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true (https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050)
- **Active Exploitation:** false
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Use Android's Scudo hardened allocator with guard pages; avoid unsafe Rust code; apply the provided patch.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: hidden malicious instructions embedded in external data sources (emails, documents, calendar invites) that are incorporated into prompts and can cause the model to perform unauthorized actions such as data exfiltration or other rogue commands.
- **Affected Products:** Google Gemini, Google Workspace (Gemini in Workspace), Gemini app, Gemini 2.5 models
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: prompt injection content classifiers, security thought reinforcement, markdown sanitization and suspicious URL redaction, user confirmation (HITL) framework, and end-user security mitigation notifications.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors are targeting large backbone and edge routers (PE/CE) and leveraging compromised devices and trusted connections to pivot into networks; they modify routers to maintain persistent long-term access for espionage and use those footholds to reach downstream networks.
- **Affected Products:** Backbone routers, provider edge (PE) routers, customer edge (CE) routers, and other network devices (no vendor/product versions specified)
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Harden and monitor network-edge devices (backbone/PE/CE routers), apply vendor updates when published, isolate and remediate compromised routers, monitor and hunt using published IOCs and STIX where available, and restrict trusted connections between network segments until devices are verified.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

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
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Russian GRU's 85th GTsSS (Unit 26165), also known as APT28
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 11. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 12. 🟡 High Severity — pydantic-ai: SSRF blocklist bypass via IPv4-compatible, SIIT/IVI, and local NAT64 IPv6 addresses (incomplete fix of CVE-2026-46678)

**CVE:** `CVE-2026-48782` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-cg7w-rg45-pc59>

> ## Summary

When an application using Pydantic AI opts a URL into `force_download=&#x27;allow-local&#x27;` (which disables the default block on private/internal IPs) **and runs on a network that routes the affected IPv6 transition forms (NAT64- or ISATAP-configured networks)**, the cloud-metadata blocklist could be bypassed by encoding the metadata IP in an IPv6 transition form that the previous f…

---

## 13. 🟡 High Severity — @sigstore/core has DSSE payloadType type-binding failure

**CVE:** `CVE-2026-48758` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-jfc7-64v2-mr8c>

> ### Impact
The `preAuthEncoding` function in `@sigstore/core` uses Node.js `&#x27;ascii&#x27;` encoding when converting the PAE (Pre-Authentication Encoding) string to bytes. This allows `payloadType` to be mutated after signing without invalidating the signature, breaking the type-binding guarantee that DSSE is designed to provide.

In `packages/core/src/dsse.ts`, the PAE function builds a string…

---

## 14. 🟡 High Severity — Incus has an arbitrary file write via path traversal in S3 multipart upload

**CVE:** `CVE-2026-48753` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-ccjc-4qc3-jxqc>

> ## Summary

The S3 protocol upload endpoint is vulnerable to path traversal and allows creation of arbitrary files on the host. This behavior could lead to arbitrary command execution.

In `internal/server/storage/s3/local/multipart.go`, user-controlled upload ID is appended to the uploads directory unsanitized; https://github.com/lxc/incus/blob/40dd4f151d52c06b178482aa2518abfb9df3e6fb/internal/se…

---

## 15. 🟡 High Severity — OpenAM Authentication Bypass via MSISDN LDAP Injection

**CVE:** `CVE-2026-46619` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-xq73-fvmr-jvmm>

> ## Summary

**Description**

An LDAP Injection (CWE-90) vulnerability in the MSISDN authentication module allows an unauthenticated, remote attacker to obtain an arbitrary OpenAM session without a password in the default trusted gateway configuration. This impacts OpenAM Community Edition through version 16.0.6. This issue was patched in version 16.1.1.

## Impact
OpenAM deployments through versio…

---

## 16. 🟡 High Severity — fluent-plugin-opentelemetry Has Denial of Service (DoS) via Large Payloads and Decompression Bombs in `in_opentelemetry`

**CVE:** `CVE-2026-44163` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-2jc5-xhx8-qj6h>

> The `fluent-plugin-opentelemetry` plugin (specifically the `in_opentelemetry` HTTP input) lacked strict size limits on incoming requests.
It was discovered that the plugin read the entire request body and decompressed payloads into memory without enforcing maximum size thresholds.

If the OpenTelemetry ingestion endpoint is exposed to untrusted networks, an attacker can send an excessively large H…

---

## 17. 🟡 High Severity — Fluentd is Vulnerable to Server-Side Request Forgery (SSRF) via Placeholder Expansion in `out_http`

**CVE:** `CVE-2026-44161` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-72f5-rr8c-r6gr>

> The `out_http` output plugin allows the use of placeholders (such as `${tag}`) in the `endpoint` configuration parameter.
It was discovered that if the placeholder value is derived from untrusted user input, an attacker can maliciously control the destination hostname of the outbound HTTP requests made by Fluentd.

### Impact
This vulnerability allows for a **Server-Side Request Forgery (SSRF)** a…

---

## 18. 🟡 High Severity — Fluentd is Vulnerable to Denial of Service (DoS) via Gzip Decompression Bomb in `in_http` and `in_forward`

**CVE:** `CVE-2026-44160` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-j9cw-hwqf-85w7>

> Fluentd&#x27;s `in_http` and `in_forward` plugins support receiving gzip-compressed data.
While Fluentd correctly enforces size limits on the incoming compressed payloads (e.g., via `body_size_limit` or `chunk_size_limit`), it was discovered that there is no limit enforced on the size of the decompressed data.

If a Fluentd instance is exposed to untrusted networks, an attacker can send a maliciou…

---

## 19. 🟡 High Severity — Fluentd is Vulnerable to Exposure of Sensitive Information via Monitor Agent API

**CVE:** `CVE-2026-44025` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-pr7j-96cj-549h>

> Fluentd&#x27;s Monitor Agent plugin (`in_monitor_agent`) exposes internal metrics and plugin information via a REST API.
It was discovered that the API response (`/api/plugins.json` and related endpoints) unintentionally includes internal instance variables of loaded plugins.

If any plugins store sensitive information—such as database passwords, API keys, or cloud credentials—in its instance vari…

---

## 20. 🟡 High Severity — Fluentd is Vulnerable to Remote Code Execution (RCE) via Arbitrary File Write in `${tag}` Placeholder

**CVE:** `CVE-2026-44024` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-44hj-4m45-frj3>

> Fluentd allows dynamically constructing file paths using the `${tag}` placeholder.
It was discovered that validation for this placeholder was insufficient.

If a Fluentd instance is configured to receive logs from untrusted sources and uses the `${tag}` placeholder in file configurations (such as the `path` parameter in the `out_file` plugin), an attacker can inject path traversal characters (e.g.…

---

## 21. 🟡 High Severity — New DirtyClone Linux Kernel Flaw Lets Local Users Gain Root via Cloned Packets

**CVE:** `CVE-2026-43503` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://thehackernews.com/2026/06/new-dirtyclone-linux-kernel-flaw-lets.html>

> DirtyClone is a new Linux kernel privilege escalation in the DirtyFrag family. JFrog Security Research published a working exploit walkthrough for the flaw on June 25, the first public demonstration for this variant.

Tracked as CVE-2026-43503 (CVSS 8.8), it lets a local user corrupt file-backed memory through a cloned network packet and gain root. The patch landed in

---

## 22. 🟡 High Severity — Lemur: ACME SSRF + creator-equality IDOR lead to AWS IAM/PKI compromise

**CVE:** `CVE-2026-55166` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-v2wp-frmc-5q3v>

> &lt;!-- obsidian --&gt;&lt;h1 data-heading=&quot;Lemur 1.9.0: any SSO-authenticated user achieves AWS IAM compromise and permanent PKI key access via ACME acme_url SSRF and creator-equality IDOR&quot;&gt;Lemur 1.9.0: any SSO-authenticated user achieves AWS IAM compromise and permanent PKI key access via ACME acme_url SSRF and creator-equality IDOR&lt;/h1&gt;
&lt;h2 data-heading=&quot;Vulnerability…

---

## 23. 🟡 High Severity —  Lemur: JWT verifier honors attacker-supplied alg, enabling ATO

**CVE:** `CVE-2026-55165` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-r9gp-7f88-9r54>

> &lt;!-- obsidian --&gt;&lt;h1 data-heading=&quot;Lemur 1.9.0: JWT verifier trusts attacker-supplied alg from token header — defense-in-depth gap; chain-dependent ATO with secret disclosure&quot;&gt;Lemur 1.9.0: JWT verifier trusts attacker-supplied alg from token header — defense-in-depth gap; chain-dependent ATO with secret disclosure&lt;/h1&gt;
&lt;h2 data-heading=&quot;Vulnerability Summary&quo…

---

## 24. 🟡 High Severity — Lemur Privilege Escalation: Non-admin role members can rewrite role membership via PUT /api/1/roles/<id>

**CVE:** `CVE-2026-55163` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-x3vf-mgxj-7785>

> ## Summary
 
The `PUT /api/1/roles/&lt;id&gt;` handler in `lemur/roles/views.py` gates only on `RoleMemberPermission(role_id).can()`, which is satisfied for any user who is already a member of the target role. The handler then passes `data[&quot;users&quot;]` and `data[&quot;name&quot;]` directly to `service.update()`, permitting any role member to rewrite that role&#x27;s membership list and name…

---

## 25. 🟡 High Severity — Lemur: Crafted CRL/OCSP URLs in uploaded certificates lead to post-authentication SSRF

**CVE:** `CVE-2026-55162` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-54vg-pfh7-jq95>

> ## Summary
 
When verifying an uploaded certificate, `lemur/certificates/verify.py` extracts the CRL Distribution Point URL and the OCSP responder URL directly from the certificate&#x27;s extensions and issues outbound requests to those URLs without scheme restriction or destination allow-listing. An authenticated user holding the operator role (required by `StrictRolePermission` on `POST /certifi…

---

## 26. 🟡 High Severity — GitHub MCP Server: Lockdown mode singleton in HTTP server causes cross-user GraphQL client confusion

**CVE:** `CVE-2026-48529` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-pjp5-fpmr-3349>

> ### Summary

When running in HTTP mode with --lockdown-mode enabled, the RepoAccessCache is implemented as a process-global singleton initialized with the first authenticated user&#x27;s GraphQL client. All subsequent requests from different users share this singleton and their lockdown-related GraphQL queries are executed using the first user&#x27;s credentials. The singleton is never updated to …

---

## 27. 🟡 High Severity — MessagePack-CSharp: DynamicUnionResolver-generated deserializers miss depth enforcement

**CVE:** `CVE-2026-48513` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-wfr3-xj75-pfwh>

> ## Summary

Runtime-generated union deserializers emitted by `DynamicUnionResolver` do not call `MessagePackSecurity.DepthStep(ref reader)` and do not decrement `reader.Depth` around recursive deserialization and skip paths.

This means union deserialization does not consistently participate in the maximum object graph depth enforcement that protects other recursive formatter paths. For unknown un…

---

## 28. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
