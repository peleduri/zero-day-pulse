# Zero Day Pulse

> **Generated:** 2026-06-15 20:44 UTC &nbsp;|&nbsp; **Total:** 28 &nbsp;|&nbsp; 🔴 KEV: 2 &nbsp;|&nbsp; 🟠 Zero-Day: 11 &nbsp;|&nbsp; 🟡 High: 15 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🔴 CISA KEV — CVE-2026-54420 — LiteSpeed cPanel Plugin UNIX Symbolic Link (Symlink) Following Vulnerability

**CVE:** `CVE-2026-54420` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-54420>

> Vendor: LiteSpeed | Product: cPanel Plugin. LiteSpeed cPanel plugin contains a UNIX symbolic link (Symlink) following vulnerability that could allow a user with FTP or web shell access on a shared hosting server running CloudLinux/CageFS. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk …

**Parallel AI Enrichment:**

- **Technical Details:** The plugin mishandles user‑provided symbolic links (symlink following) on shared hosting with CloudLinux/CageFS, allowing an FTP or web‑shell user to create symlinks that the plugin follows, leading to unauthorized access to other users’ files (symlink traversal/privilege/resource access).
- **Affected Products:** LiteSpeed cPanel plugin before 2.4.8 (as distributed in LiteSpeed WHM PlugIn before 5.3.2.0)
- **CVSS Score:** 8.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N
- **Exploit Available:** true — https://nvd.nist.gov/vuln/detail/CVE-2026-54420
- **Patch Available:** true — https://www.litespeedtech.com/support/wiki/doku.php/litespeed_wiki:changelog
- **Active Exploitation:** true — https://www.cve.org/CVERecord?id=CVE-2026-54420 and https://nvd.nist.gov/vuln/detail/CVE-2026-54420
- **Threat Actors:** None known
- **Mitigation:** Immediately upgrade to LiteSpeed cPanel plugin 2.4.8 (WHM Plugin 5.3.2.0) per vendor advisory; as interim mitigations, restrict FTP/web shell access, disable the LiteSpeed cPanel plugin where feasible, apply CloudLinux/CageFS hardening and isolation, and follow CISA BOD 26-04 prioritization and forensics triage guidance. If unable to patch or mitigate, discontinue use.
- **Vendor Advisory:** https://www.litespeedtech.com/support/wiki/doku.php/litespeed_wiki:changelog

---

## 2. 🔴 CISA KEV — CVE-2026-20262 — Cisco Catalyst SD-WAN Manager Directory or Path Traversal Vulnerability

**CVE:** `CVE-2026-20262` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-20262>

> Vendor: Cisco | Product: Catalyst SD-WAN Manager. Cisco Catalyst SD-WAN Manager contains a directory or path traversal vulnerability that could allow an authenticated, remote attacker to create a file or overwrite any file on the filesystem of an affected system. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Securi…

**Parallel AI Enrichment:**

- **Technical Details:** Cisco Catalyst SD-WAN Manager contains a directory/path traversal vulnerability that could allow an authenticated, remote attacker to create or overwrite files on the filesystem of an affected system by supplying crafted input to traverse directories.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Apply vendor‑recommended mitigations and follow CISA BOD 26-04 guidance; if vendor patch unavailable, restrict access to SD-WAN Manager, enforce least privilege, isolate management interfaces, and monitor logs for anomalous file write activity.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Multiple unauthenticated path traversal vulnerabilities in SimpleHelp’s web interface allow remote attackers to traverse directories and read arbitrary sensitive files on the server, enabling further credential theft and system compromise.
- **Affected Products:** SimpleHelp remote support / RMM software versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (unspecified groups)
- **Mitigation:** Immediately update SimpleHelp to the vendor‑published fixed version (upgrade above 5.5.7), or if unable to patch: disable public access to the SimpleHelp web interface, restrict access via firewall/VPN, apply network segmentation, and monitor for indicators of compromise per CISA guidance.
- **Vendor Advisory:** https://www.broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) exploits arise when an attacker injects malicious instructions into the prompt context, causing AI agents to execute unintended actions; the paper presents end‑to‑end IPI exploits using natural queries and real‑world corpora across RAG and agentic systems.
- **Affected Products:** Google Gemini (AI service)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (source: http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability)
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

- **Technical Details:** An attacker injects malicious prompts into data sources or web pages accessed by the LLM, causing the model to execute unintended instructions. In the GeminiJack case, the injection occurs without any user input (zero‑click).
- **Affected Products:** Google Workspace (with Gemini), Google Gemini, Google Gemini Enterprise
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (source: http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability)
- **Patch Available:** false
- **Active Exploitation:** true (source: http://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads)
- **Threat Actors:** None known
- **Mitigation:** Implement continuous monitoring of prompt inputs, restrict or sandbox untrusted data sources, and enforce strict input validation and sanitization for all tools that feed data to Gemini. Apply any vendor‑issued hardening guidelines promptly.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is the primary threat—malicious web content can influence agentic AI browser agents by injecting prompts through page content or resources, leading agents to perform unsafe actions or exfiltrate data. Google describes layered defenses in Chrome to restrict origin access, sandbox agent actions, and filter unsafe instructions.
- **Affected Products:** Chrome (agentic/Gemini integration)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use the latest Chrome with the new layered defenses; restrict agentic features in untrusted contexts, follow Google’s guidance to limit origin access and enable safe‑by‑default agent restrictions.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A near‑miss linear buffer overflow in unsafe Rust code inside the CrabbyAVIF crate (CVE‑2025‑48530). The overflow would have written past a buffer, but Android’s Scudo hardened allocator placed guard pages around secondary allocations, causing a deterministic crash instead of exploitable behavior.
- **Affected Products:** CrabbyAVIF (Android platform component: platform/external/rust/crabbyavif)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true - https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use of Scudo hardened allocator (guard pages) to make the overflow non‑exploitable, improved crash reporting to surface overflows, assignment of CVE‑2025‑48530, and adoption of unsafe‑Rust training and review practices.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) hides malicious instructions inside external data sources (emails, documents, calendar invites, code comments, web pages). An AI agent that ingests such data (automated assistants, code interpreters, or tools that fetch external content) may treat attacker‑supplied text as instructions and perform data exfiltration, privileged actions, or other unintended behaviors. New variants include “Comment and Control” via collaborative platforms (e.g., GitHub comments) that influence multi‑step agent workflows.
- **Affected Products:** Google Gemini, Google Workspace (Workspace‑integrated Gemini), Microsoft Copilot Studio (ShareLeak/CVE-2026-21520), Anthropic Claude, GitHub Copilot (via GitHub comments)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true — http://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads, http://infosecurity-magazine.com/news/researchers-10-wild-indirect
- **Patch Available:** true — http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html, http://thehackernews.com/2026/04/google-patches-antigravity-ide-flaw.html
- **Active Exploitation:** true — http://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads, http://infosecurity-magazine.com/news/researchers-10-wild-indirect
- **Threat Actors:** None known
- **Mitigation:** Apply layered defenses — sanitize and isolate untrusted inputs, limit model access to sensitive data, use instruction‑blocking filters and provenance/trust signals, attacker‑detection telemetry, prompt hardening, model ensembling and policy layers; apply vendor patches and configuration recommendations from vendor advisories.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors target backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, modify routers to maintain persistent, long‑term access, and leverage compromised devices or trusted connections to pivot into other networks.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Apply CISA guidance: isolate and monitor network infrastructure, audit and harden router configurations, restrict management interfaces, implement strong authentication and logging, segment networks, and apply vendor‑recommended mitigations and detection signatures per advisory.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** The GRU‑linked campaign employs spear‑phishing emails with malicious attachments or links to obtain credentials, followed by deployment of custom remote‑access tools to exfiltrate data from logistics and technology organizations.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Russian GRU 85th GTsSS (Unit 26165), also known as APT28
- **Mitigation:** Implement multifactor authentication, enforce strong password policies, restrict privileged account access, segment networks separating logistics and technology environments, monitor for anomalous activity, and apply all relevant security updates.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 11. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

---

## 12. 🟠 Zero-Day — Cisco fixes SD-WAN vManage flaw exploited in zero-day attacks

**CVE:** `CVE-2026-20262` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://www.bleepingcomputer.com/news/security/cisco-fixes-sd-wan-vmanage-flaw-exploited-in-zero-day-attacks/>

> Cisco has released security updates to address a vulnerability in the Catalyst SD-WAN Manager, tracked as CVE-2026-20262, that was exploited in attacks to escalate to root privileges. [...]

---

## 13. 🟠 Zero-Day — ⚡ Weekly Recap: Chrome 0-Day, UniFi Exploits, macOS Stealers, VPN Flaw and More

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://thehackernews.com/2026/06/weekly-recap-chrome-0-day-unifi.html>

> Stuff broke again. Not in a movie way. An old tool was left exposed. An abandoned package was abused. A deprecated feature was still running in prod.

This week is the same lesson in a new form: phishing kits are easier to rent, AI names are useful bait, old login paths still fail, and forgotten software keeps becoming someone else&#x27;s entry point.

Scroll through the full Monday Cybersecurity

---

## 14. 🟡 High Severity — Starlette: Unvalidated request path concatenated into authority poisons request.url.hostname

**CVE:** `CVE-2026-54282` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-jp82-jpqv-5vv3>

> ### Summary

In affected versions, the HTTP request path is not validated before being used to reconstruct `request.url`. Because `request.url` is rebuilt by concatenating `{scheme}://{host}{path}` and re-parsing the result, a path that does not begin with `/` (for example `@google.com`) moves the authority boundary during re-parsing, so `request.url.hostname` and `request.url.netloc` become attac…

---

## 15. 🟡 High Severity — python-multipart: Semicolon treated as querystring field separator enables parameter smuggling

**CVE:** `CVE-2026-53538` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-6jv3-5f52-599m>

> ### Summary

`QuerystringParser` treated `;` as a field separator in `application/x-www-form-urlencoded` bodies, in addition to `&amp;`. The [WHATWG URL standard](https://url.spec.whatwg.org/#urlencoded-parsing), modern browsers, and Python&#x27;s `urllib.parse` (since the CVE-2021-23336 fix) treat only `&amp;` as a separator. This creates a parser differential: the same bytes are tokenized into d…

---

## 16. 🟡 High Severity — Tornado: Authorization header forwarded across cross-origin redirects in SimpleAsyncHTTPClient

**CVE:** `CVE-2026-49853` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-3x9g-8vmp-wqvf>

> ## Summary

When SimpleAsyncHTTPClient follows a 3xx redirect, it shallow-copies the original HTTPRequest, rewrites the URL, decrements max_redirects, and removes only the Host header. It does not clear Authorization, auth_username, auth_password, or auth_mode when the redirect target changes origin.

As a result, credentials intended for one origin can be forwarded to a different origin when foll…

---

## 17. 🟡 High Severity — Starlette: SSRF and NTLM credential theft via UNC paths in StaticFiles on Windows

**CVE:** `CVE-2026-48818` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-wqp7-x3pw-xc5r>

> ### Summary

When serving static files on Windows, `StaticFiles` resolves the requested path with [`os.path.realpath`](https://docs.python.org/3/library/os.path.html#os.path.realpath). If a UNC path (such as `\\attacker.com\share`) reaches the resolver, `realpath` causes the process to open a connection to the remote host over SMB (port 445). This is a server-side request forgery (SSRF) that leaks…

---

## 18. 🟡 High Severity — PyJWKClient: missing scheme allowlist enables CVE-2024-21643-class SSRF + token forgery via file://, ftp://, data: schemes

**CVE:** `CVE-2026-48522` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-993g-76c3-p5m4>

> &gt; [!NOTE]
&gt; The library does not directly return non-HTTP(S) URI contents to the attacker; the chained &quot;plant a JWKS to forge tokens&quot; scenario described in the original report requires additional application-layer flaws (attacker write access to a filesystem path, untrusted jku derivation) that this fix does not address. Severity is scored for the scheme-acceptance bug in isolation…

---

## 19. 🟡 High Severity — PyJWT: Public-key JWK accepted as HMAC secret enables forged HS256 tokens when mixed families are allowed

**CVE:** `CVE-2026-48526` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-xgmm-8j9v-c9wx>

> &gt; [!NOTE]
&gt; Exploitation requires a verifier configured with both symmetric and asymmetric algorithms in `algorithms=[…]` and a raw-JSON JWK as the `key=` argument, both contrary to documented usage, hence the High attack-complexity rating.

### Summary
When the verifier is decoding JSON Web Tokens, while supporting both asymmetric and HMAC algorithms, the library does not validate use of JS…

---

## 20. 🟡 High Severity — Symfony: Mailomat Mailer Webhook Parser Reads the HMAC Algorithm from the Request: Signature Algorithm Downgrade

**CVE:** `CVE-2026-48747` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-rrj9-5q2j-4gvr>

> ### Description

`Symfony\Component\Mailer\Bridge\Mailomat\Webhook\MailomatRequestParser::validateSignature()` parses the `X-MOM-Webhook-Signature` request header as `algo=signature` and passes the wire-supplied `$algo` directly to `hash_hmac()` when verifying the request against the configured webhook secret. The request therefore selects the HMAC primitive used to authenticate it.

PHP&#x27;s `h…

---

## 21. 🟡 High Severity — Symfony: IpUtils::PRIVATE_SUBNETS Omits IPv6 Transition Forms (6to4, NAT64, Teredo, IPv4-compatible): SSRF Bypass in NoPrivateNetworkHttpClient

**CVE:** `CVE-2026-48736` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-38cx-cq6f-5755>

> ### Description

`Symfony\Component\HttpClient\NoPrivateNetworkHttpClient` is documented as a decorator that blocks requests to private networks by default. The list of blocked subnets (`Symfony\Component\HttpFoundation\IpUtils::PRIVATE_SUBNETS` on 6.4+, a private constant in `NoPrivateNetworkHttpClient` on 5.4) enumerates RFC1918, loopback, link-local and IPv4-mapped IPv6 (`::ffff:0:0/96`) prefix…

---

## 22. 🟡 High Severity — @angular/service-worker: Sensitive Header Leakage on Cross-Origin Redirects in Angular Service Worker

**CVE:** `CVE-2026-54264` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-qxh6-94w6-9r5p>

> An information disclosure vulnerability exists in the `@angular/service-worker` package of the Angular framework. When the Service Worker fetches assets, it preserves metadata (such as headers) from the original request. However, on cross-origin redirects, the Service Worker fails to strip sensitive headers, violating the Fetch redirect algorithm. 

This allows a remote attacker to obtain sensitiv…

---

## 23. 🟡 High Severity — Angular: Template and Attribute Namespace Sanitization Bypass (XSS)

**CVE:** `CVE-2026-50557` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-f3m7-gqxr-g87x>

> An issue in the `@angular/compiler` and `@angular/core` packages allows bypassing element and attribute sanitization/validation through specific namespace workarounds.

Specifically, namespaced script elements (e.g., `&lt;svg:script&gt;` or `&lt;:svg:script&gt;`) were not properly identified as script elements by the Angular template preparser, allowing them to pass through template compilation wi…

---

## 24. 🟡 High Severity — node-tar applies PAX size override to intermediary GNU long-name/long-link headers, causing tar parser interpretation differential (file smuggling)

**CVE:** `CVE-2026-53655` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-vmf3-w455-68vh>

> ### Summary

`tar` (node-tar) applies a PAX extended header&#x27;s `size=` record (and other PAX
overrides) to the **next header entry of any type**, including intermediary
metadata headers such as a GNU long-name (`L`) or long-link (`K`) entry. Per
POSIX pax, a PAX extended header (`x`) describes the *next file entry*, not the
intermediary extension headers that may sit between the `x` header and…

---

## 25. 🟡 High Severity — @angular/service-worker: Request Credential & Cache Policy Stripping

**CVE:** `CVE-2026-50184` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-95qp-cmmw-mgqv>

> An issue in the `@angular/service-worker` package compromises the integrity of request-policy enforcement during request reconstruction. When the Angular Service Worker intercepts network requests for matched assets, it reconstructs a new `Request` object using an internal helper function.

During this reconstruction process, the helper function strips explicit client-defined safety parameters: th…

---

## 26. 🟡 High Severity — @angular/platform-server: URL Parser Differential leading to SSRF Allowlist Bypass

**CVE:** `CVE-2026-50168` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-xrxm-cp7j-8xf6>

> An issue in the `@angular/platform-server` package allows remote attackers to bypass host allowlist constraints and direct server-side outgoing requests to arbitrary external endpoints. This occurs due to a parser differential between the strict WHATWG URL parser used for allowlist validation and the lenient Domino URL parser used to initialize the server emulated DOM.

When a server-side request …

---

## 27. 🟡 High Severity — Angular Client Hydration DOM Clobbering & Response-Cache Poisoning

**CVE:** `CVE-2026-54267` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-rgjc-h3x7-9mwg>

> To optimize client-side bootstrap in Server-Side Rendered (SSR) environments, Angular supports **Hydration** via `provideClientHydration()`. During SSR, Angular serializes the application&#x27;s runtime state (such as cached `HttpClient` responses) and outputs it into the HTML stream as a `&lt;script&gt;` tag with a predictable identifier:

```html
&lt;script type=&quot;application/json&quot; id=&…

---

## 28. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
