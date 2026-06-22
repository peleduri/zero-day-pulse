# Zero Day Pulse

> **Generated:** 2026-06-22 20:32 UTC &nbsp;|&nbsp; **Total:** 22 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 12 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is an unauthenticated path traversal vulnerability in the SimpleHelp web application that allows crafted HTTP requests to retrieve arbitrary files (e.g., serverconfig.xml, /etc/passwd, SSH keys) from the host.
- **Affected Products:** SimpleHelp remote support/RMM — versions 5.5.7 and earlier (patched in 5.5.8, 5.4.10, 5.3.9).
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC and Metasploit module exist (Rapid7/Metasploit auxiliary scanner and OffSec blog demonstrates PoC).
- **Patch Available:** Yes — SimpleHelp released patched versions (5.5.8; also 5.4.10 and 5.3.9). Advisory/patch URL: https://simple-help.com/kb---security-vulnerabilities-01-2025
- **Active Exploitation:** Confirmed — CISA reported ransomware actors leveraging unpatched SimpleHelp instances (CISA AA25-163A).
- **Threat Actors:** Ransomware actors, specifically DragonForce.
- **Mitigation:** Upgrade SimpleHelp to the latest patched version (5.5.8/5.4.10/5.3.9). If patch cannot be applied, isolate or stop the SimpleHelp server, restrict network access with firewall/IP restrictions, disable file‑browsing functionality, and perform threat hunting per CISA guidance.
- **Vendor Advisory:** https://simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when attacker‑controlled content (web pages, docs, emails, calendar invites) is retrieved by a RAG/agent pipeline and interpreted as model instructions; techniques include CSS‑hidden strings, HTML comments, system‑prompt spoofing, authority impersonation, and payloads that trigger agent actions such as financial transactions, shell commands, or data exfiltration. GeminiJack is a zero‑click chain exploiting this trust boundary in Google Gemini Enterprise.
- **Affected Products:** Google Gemini Enterprise (Vertex AI / Gemini RAG integrations)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Proof‑of‑concept attack techniques documented by Forcepoint/Lyrie and Noma Labs; no publicly released exploit binaries referenced.
- **Patch Available:** Google released mitigations and a patch for GeminiJack; details referenced in the vendor advisory and Noma Labs report.
- **Active Exploitation:** Yes – Forcepoint/Lyrie documented 10 in‑the‑wild IPI payloads targeting production AI agents, and Noma Labs reported a GeminiJack incident that was actively exploited before patching.
- **Threat Actors:** None known
- **Mitigation:** Implement layered defenses per Google guidance: restrict agent browsing of untrusted web content, sanitize and validate retrieved documents, avoid giving agents privileged actions (payments, navigation) without explicit human confirmation, run IPI red‑teaming, apply vendor updates/patches, and follow Google Workspace continuous IPI mitigations.
- **Vendor Advisory:** https://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an attack technique that injects malicious instructions into data or tools used by an LLM (including web content or integrated data sources), causing the model or its agentic automation to follow attacker‑supplied directives—even without direct user input. The attack surface includes multi‑source apps (e.g., Workspace + Gemini) and agentic automation that fetches external content.
- **Affected Products:** Google Workspace with Gemini (enterprise integrations using multiple data sources); "complex AI applications with multiple data sources" per advisory. If specific versions required: Affected products unavailable
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC or weaponized exploit reported in the cited sources.
- **Patch Available:** No official patch has been released; the advisory provides mitigation guidance.
- **Active Exploitation:** No confirmed active exploitation reported in the cited sources
- **Threat Actors:** None known
- **Mitigation:** Implement input/output validation and sanitization; enforce human oversight and controls for LLM agents; monitor public web for known IPI patterns; follow Google Workspace hardening guidance in the advisory.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection in Chrome's Gemini agentic browsing enables an attacker to chain prompts, leading to unauthorized local file access and privacy invasion.
- **Affected Products:** Google Chrome (Gemini agentic browsing) versions prior to 1.3
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof‑of‑concept disclosed by Noma Labs (http://noma.security/noma-labs/geminijack).
- **Patch Available:** Patched in Chrome version 1.3 (see NVD entry) and a Google security update released shortly after (Unit42 report).
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Update Chrome to version 1.3 or later; if updating is not possible, disable the Gemini/agentic browsing feature.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Linear buffer overflow in CrabbyAVIF; mitigated by Scudo allocator guard pages that make the overflow non‑exploitable.
- **Affected Products:** Android (versions containing the CrabbyAVIF component)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept or exploit is available.
- **Patch Available:** https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050
- **Active Exploitation:** No active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Apply the patch at https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050 and ensure the Scudo hardened allocator is enabled on Android devices.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injections embed hidden malicious instructions within external data sources (emails, documents, calendar invites) to manipulate LLM behavior and exfiltrate data or perform actions. Google’s defenses combine model resilience from adversarial training (Gemini 2.5), ML‑based instruction detectors, security‑thought reinforcement, markdown sanitization, suspicious‑URL redaction, and user confirmation for risky operations.
- **Affected Products:** Gemini (Google Workspace, Gemini app)
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit for this Google advisory reported.
- **Patch Available:** Patch unavailable; mitigations and model/feature updates have been implemented and are described in the advisory: http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html
- **Active Exploitation:** No confirmed active exploitation in the wild reported in the advisory.
- **Threat Actors:** None known
- **Mitigation:** Model hardening (Gemini 2.5 adversarial training), purpose‑built ML detectors for malicious instructions, security‑thought reinforcement, markdown sanitization and suspicious‑URL redaction, contextual user confirmation (HITL), end‑user security notifications and help‑center guidance.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** APT actors exploit publicly known CVEs and misconfigurations such as Cisco IOS XE web UI authentication bypass (CVE-2023-20198), Cisco Smart Install remote code execution (CVE-2018-0171), and Ivanti command injection (CVE-2024-21887). Attack methods include web UI auth bypass with double‑encoded paths, post‑auth command injection to gain root, using Guest Shell/LXC scripts (TCL, Python), creating unauthorized accounts, executing SNMP/SSH commands, and leveraging mirrored traffic (SPAN/RSPAN) for data collection and lateral movement.
- **Affected Products:** Cisco IOS/XE routers and switches (multiple versions affected by CVE-2023-20198, CVE-2023-20273, CVE-2018-0171), Ivanti Connect Secure/Policy (CVE-2024-21887), and other network devices such as Fortinet, Juniper, Nokia, Sierra Wireless, SonicWall (suspected targets).
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public exploits and tooling (e.g., siet.py, map.tcl, tclproxy.tcl) are publicly available, as noted in the advisory.
- **Patch Available:** Vendor patches are available for the listed CVEs, with links provided in the advisory (e.g., Cisco advisories for CVE-2023-20198 and CVE-2023-20273; Ivanti advisories for CVE-2024-21887).
- **Active Exploitation:** Yes—CISA reports that these APT actors have actively exploited the listed CVEs in the wild across Internet‑exposed devices.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching of the listed CVEs; disable all unused ports and protocols; use encrypted/authenticated management protocols (SSH/HTTPS); change default administrative credentials and require key‑based authentication; minimize management‑plane exposure; detect over‑encoding requests to WSMA endpoints and monitor the Proxy‑Uri‑Source header; follow CISA/NSA/FBI hardening guidance in the advisory.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable for a specific vulnerability.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit tied to the CSA reported in the advisory; exploit availability unavailable.
- **Patch Available:** No vendor patch specifically tied to this CSA; mitigation guidance provided in the advisory.
- **Active Exploitation:** Confirmed active targeting/operations by Russian GRU (85th GTsSS, unit 26165) against Western logistics entities and technology companies since 2022.
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS), military unit 26165 (also tracked as APT28/Fancy Bear).
- **Mitigation:** Follow hardening and detection mitigations in the joint CSA: implement multifactor authentication, patch and harden internet‑facing services, restrict remote access (VPN/RDP), monitor logs and network for indicators of compromise, apply network segmentation and least privilege, and follow the IOC and detection recommendations in the advisory.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

**Parallel AI Enrichment:**

- **Technical Details:** Improper symbolic link handling in the PutContents API lets an attacker create a symlink to a sensitive file and then write through it, overwriting configuration files (e.g., sshCommand) and achieving remote code execution.
- **Affected Products:** Gogs (self‑hosted git service)
- **CVSS Score:** 8.7
- **CVSS Vector:** CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N/E:A/AU:Y/R:U/V:C
- **Exploit Available:** Yes — public PoC available at https://github.com/zAbuQasem/gogs-CVE-2025-8110
- **Patch Available:** Yes — fixes merged to main; see GitHub commit/PRs https://github.com/gogs/gogs/commit/553707f3fd5f68f47f531cfcff56aa3ec294c6f6, https://github.com/gogs/gogs/pull/8078
- **Active Exploitation:** Confirmed – CISA added CVE-2025-8110 to its Known Exploited Vulnerabilities (KEV) catalog and reports cite active exploitation across hundreds of Gogs instances.
- **Threat Actors:** None known
- **Mitigation:** Restrict access to Gogs (VPN or IP allow‑list), disable open user registration, monitor Git/SSH configuration files for unexpected changes, follow CISA KEV guidance and apply the vendor‑provided fix once released.
- **Vendor Advisory:** https://github.com/gogs/gogs/commit/553707f3fd5f68f47f531cfcff56aa3ec294c6f6

---

## 10. 🟠 Zero-Day — What the Latest ShinyHunters Breaches Reveal About Modern Cyberattacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://www.securityweek.com/what-the-latest-shinyhunters-breaches-reveal-about-modern-cyberattacks/>

> Groups like ShinyHunters are demonstrating that attackers do not necessarily need malware or zero-day exploits to cause massive damage. The post What the Latest ShinyHunters Breaches Reveal About Modern Cyberattacks appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Attackers compromised a Free‑for‑Teacher account, used it to gain privileged access to the Canvas LMS backend, and exfiltrated student data. The exact vulnerability type (e.g., code flaw or configuration issue) is not publicly detailed.
- **Affected Products:** Instructure Canvas (Free-for-Teacher) 
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept or weaponized exploit has been reported.
- **Patch Available:** No official patch has been released; the vulnerability was mitigated by disabling the affected Free-for-Teacher service.
- **Active Exploitation:** Yes, active exploitation was confirmed; the attacker gained unauthorized access to production Canvas data and exfiltrated student information.
- **Threat Actors:** SHADOW-AETHER-015
- **Mitigation:** Disable the Canvas Free-for-Teacher service, rotate all API credentials, re‑authorize third‑party integrations, audit credential reuse across systems, and enforce multi‑factor authentication for all privileged accounts.
- **Vendor Advisory:** http://instructure.com/incident_update

---

## 11. 🟡 High Severity — Paymenter has Blind Unauthenticated SSRF on the Paypal gateway module

**CVE:** `CVE-2026-44583` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-7wwh-xcc3-9fcg>

> ### Summary
The PayPal webhook endpoint `/extensions/paypal/webhook` processes the `PAYPAL-CERT-URL` HTTP header without validation, allowing attackers to control server-side HTTP request destinations.

### Technical details:

The `/extensions/paypal/webhook` endpoint processes incoming webhook requests and trusts the value of the `PAYPAL-CERT-URL` HTTP header without validation.

This value is pa…

---

## 12. 🟡 High Severity — OpenAM has pre-auth Reflected XSS in OAuth2 / OIDC response_mode=form_post via state parameter (FormPostResponse.ftl)

**CVE:** `CVE-2026-44203` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-fq9h-c788-fx73>

> ### Summary

The OAuth 2.0 / OpenID Connect authorization endpoint does not sufficiently sanitize certain user-supplied parameters before incorporating them into the HTML response generated for the `form_post` response mode. This may allow an attacker to inject content into the rendered page in the context of the OpenAM origin.

---

## 13. 🟡 High Severity — OpenAM Authenticated Server-Side Request Forgery (SSRF) via `/sessionservice`

**CVE:** `CVE-2026-44202` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-c556-q2mh-477v>

> OpenAM (Open Identity Platform) is an open-source Identity and Access Management (IAM) platform derived from ForgeRock OpenAM, providing SSO, OAuth2, SAML, and OpenID Connect capabilities. It is widely deployed in enterprise environments as a central authentication gateway.

The `/sessionservice` endpoint, used for internal session management operations, does not sufficiently restrict the URLs tha…

---

## 14. 🟡 High Severity — xwiki-pro-macros has remote code execution from page title and content via excerpt-include macro

**CVE:** `CVE-2026-44179` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-w56x-9778-rppx>

> ### Summary
The excerpt-include macro does not properly escape the title of the included page and executes the content of the excerpt with the macro&#x27;s rights. Therefore, it is vulnerable to XWiki syntax injection via the included page&#x27;s title and content, allowing remote code execution for any user who can edit a page.

### Details
The title of the included page isn&#x27;t escaped in [Ex…

---

## 15. 🟡 High Severity — OpenAM has LDAP Injection via `_queryId` Parameter

**CVE:** `CVE-2026-41573` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-2vg8-q4c2-5cw3>

> OpenAM (Open Identity Platform) is an open-source IAM platform providing SSO, OAuth2, SAML, and OpenID Connect capabilities. The CREST REST API layer exposes user query endpoints under `/json/{realm}/users`. In `IdentityResourceV1.queryCollection()`, the HTTP query parameter `_queryId` is passed to a `CrestQuery` object with `escapeQueryId` **explicitly set to `false`**, bypassing the escape prote…

---

## 16. 🟡 High Severity — AVideo has an Authorize.Net Webhook Signature Bypass that Enables Wallet Balance Inflation via Forged Payment Data

**CVE:** `CVE-2026-33731` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-95jh-7r58-xmxw>

> ## Summary

The Authorize.Net webhook handler at `plugin/AuthorizeNet/webhook.php` contains a signature verification bypass that allows an attacker to forge webhook requests with arbitrary payment amounts and target user IDs. By supplying a valid transaction ID from a small legitimate purchase, the attacker bypasses signature validation and credits arbitrary wallet balances to any user account via…

---

## 17. 🟡 High Severity — ComfyUI-Manager has an Unprotected Alternate Channel (CWE-420)

**CVE:** `CVE-2025-67303` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-95pq-hr8p-f5g7>

> ### Impact

An **Unprotected Alternate Channel (CWE-420)** vulnerability was discovered in ComfyUI-Manager versions prior to 3.38.

#### Vulnerability Details

In affected versions, ComfyUI-Manager stored its configuration in the `user/default/ComfyUI-Manager/` directory, which was accessible via ComfyUI&#x27;s web APIs without proper access control. This unprotected alternate channel allowed remo…

---

## 18. 🟡 High Severity — AVideo Vulnerable to Unauthenticated .env File Exposure via Official Docker Compose Configuration

**CVE:** `CVE-2026-33692` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-wf69-r4mx-43rr>

> ## Vulnerability Details

**CWE**: CWE-538 - Insertion of Sensitive Information into Externally-Accessible File or Directory

The official `docker-compose.yml` (line 61) mounts the entire project root directory as the Apache document root:

```yaml
volumes:
  - &quot;./:/var/www/html/AVideo&quot;
```

This causes the `.env` file — which contains database credentials, admin passwords, and infrastru…

---

## 19. 🟡 High Severity — AVideo's Privilege Escalation via Unguarded Permission Parameters in signUp API Allows Self-Granting Upload/Stream/Meet Permissions

**CVE:** `CVE-2026-33684` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-8j8m-p79x-g4jm>

> ## Summary

The `set_api_signUp` method in the API plugin accepts `emailVerified`, `canUpload`, `canStream`, and `canCreateMeet` parameters from user-supplied input and applies them to newly created accounts without verifying that the request was authenticated with a valid APISecret. Any anonymous user who can solve a CAPTCHA can self-grant elevated permissions during account registration.

## Det…

---

## 20. 🟡 High Severity — OpenCTI has Semi-Blind SSRF via Unvalidated External URL in Data Ingestion Feature

**CVE:** `CVE-2026-21887` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-ffm6-vvph-g5f5>

> ### Summary
The OpenCTI platform’s data ingestion feature accepts user-supplied URLs without validation and uses the Axios HTTP client with its default configuration (allowAbsoluteUrls: true). This allows attackers to craft requests to arbitrary endpoints, including internal services, because Axios will accept and process absolute URLs.

This results in a semi-blind SSRF, as responses may not be f…

---

## 21. 🟡 High Severity — Paymenter vulnerable to Remote Code Execution via public file uploads

**CVE:** `CVE-2025-58048` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-22
**Reference:** <https://github.com/advisories/GHSA-5pm9-r2m8-rcmj>

> ### Impact

The ticket attachments functionality in Paymenter allows a malicious authenticated user to upload arbitrary files.

With the ability to execute arbitrary code, this vulnerability can be exploited in numerous ways, including but not limited to:
- Extracting sensitive data from the database (e.g. customer information).
- Reading credentials from .env or other configuration files.
- Runni…

---

## 22. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
