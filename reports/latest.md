# Zero Day Pulse

> **Generated:** 2026-06-16 02:36 UTC &nbsp;|&nbsp; **Total:** 29 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 11 &nbsp;|&nbsp; 🟡 High: 18 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a directory traversal vulnerability in SimpleHelp RMM that enables unauthenticated remote attackers to read sensitive files by manipulating file path parameters.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (unspecified groups)
- **Mitigation:** Upgrade SimpleHelp RMM to a version newer than 5.5.7 (or apply the vendor patch). If immediate upgrade is not possible, restrict remote access, enforce network segmentation, and monitor for suspicious file access.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when adversarial instructions are embedded in external content (websites, documents, or retrieval corpora) that AI agents or RAG systems retrieve and incorporate into their prompt or context, causing the model to follow attacker‑supplied instructions or leak data. Attacks include seeding malicious payloads on websites, crafting retrieval corpus entries, and exploiting browsing/agent behaviors; end‑to‑end IPI exploits have been demonstrated against RAG and agentic systems.
- **Affected Products:** AI agents, retrieval‑augmented generation (RAG) systems, and agentic LLM systems that browse or ingest external web content; specific product versions unavailable
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Hardening recommendations include sanitizing and filtering retrieved content, implementing strict instruction/role isolation, provenance‑aware retrieval, retrieval validation and ranking defenses, conservative execution of web‑browsing agents, and monitoring for anomalous outputs.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) involves embedding attacker‑controlled instructions into data sources (Docs, Calendar events, email HTML) that are retrieved by an LLM during a user query or RAG workflow. In the GeminiJack example, attacker‑created Docs/Calendar/Email content included embedded instructions that caused Gemini Enterprise’s retrieval and synthesis pipeline to include sensitive content in responses and to exfiltrate it via an auto‑loading external image URL — enabling data exfiltration without malware or user phishing.
- **Affected Products:** Google Gemini Enterprise, Google Workspace integrations (RAG/search over Docs, Gmail, Calendar)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true – https://noma.security/noma-labs/geminijack/
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** true – https://oecd.ai/en/incidents/2025-12-09-ee43, https://www.darkreading.com/remote-workforce/gemini-enterprise-exposes-sensitive-data
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses: deterministic controls (user confirmation, URL sanitization, tool‑chaining policies, centralized policy engine and regex takedowns), ML/LLM‑based defenses (synthetic‑data‑driven retraining, prompt engineering, model hardening), proactive red‑team testing, participation in AI VRP, restrict or monitor RAG/data‑source access, enforce least privilege on connected data sources, disable auto‑loading external resources, and apply URL/content sanitization for retrieved content.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The root issue is indirect prompt injection, where hidden or crafted page content supplies instructions that the agentic AI (Gemini in Chrome) may interpret as authoritative prompts, enabling data exfiltration or chained exploits such as CVE‑2025‑54131. Noma Labs demonstrated a zero‑click chain (GeminiJack) using this technique inside Gemini Enterprise and Vertex AI Search. Google’s mitigation adds deterministic rules and a secondary monitoring agent to restrict origin access and unsafe AI actions.
- **Affected Products:** Google Chrome (agentic browsing / Gemini integration), Google Gemini Enterprise, Vertex AI Search (versions unspecified)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true - https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability
- **Patch Available:** true - https://blog.google/security/architecting-security-for-agentic/
- **Active Exploitation:** true - https://blog.google/security/architecting-security-for-agentic/, https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/, https://bleepingcomputer.com/news/security/google-chrome-adds-new-security-layer-for-gemini-ai-agentic-browsing/
- **Threat Actors:** None known
- **Mitigation:** Apply the latest Chrome updates that implement the layered defenses described by Google. Disable or restrict agentic browsing features when not required, enforce content‑origin restrictions, and follow the hardening guidance outlined in the vendor advisory. Monitor for indicators from Noma Labs and NVD for related CVEs.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Adopt Rust for new Android platform code; prioritize memory-safety-focused development and remediation (per Google guidance).
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection attacks embed hidden malicious instructions within external data sources (emails, documents, calendar invites) that LLM‑based agents ingest, causing exfiltration or rogue actions.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known.
- **Mitigation:** Implement layered defenses: validate and sanitize external inputs, enforce strict access controls and least privilege for agents, use provenance and source‑trust signals, apply output filters and redaction, rate‑limit and monitor agent actions, and keep models and connectors updated.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Chinese state‑sponsored actors alter router firmware or configuration to embed persistent backdoors, then leverage compromised devices and trusted network links to pivot into other segments, enabling long‑term espionage across telecom, government, transportation, lodging, and military networks.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Implement strict segmentation of core router infrastructure, enforce multi‑factor authentication and role‑based access for router management, regularly verify firmware integrity and apply vendor‑recommended hardening guides, and monitor for unusual traffic or configuration changes.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

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
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS)
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** CVE‑2026‑45586: link‑following flaw (CWE‑59) in Windows CTFMON enables local privilege escalation to SYSTEM. CVE‑2026‑50507: missing authentication (CWE‑306) in BitLocker permits bypass with physical access. CVE‑2026‑44815: stack‑based buffer overflow (CWE‑121) in DHCP Client allows remote code execution via malicious DHCP responses.
- **Affected Products:** Microsoft Windows (CTFMON/Collaborative Translation Framework, BitLocker, DHCP Client Service, Active Directory Domain Services, Cryptographic Services, Deployment Services, Kerberos KDC), Microsoft Office, Extended Security Updates (ESU)
- **CVSS Score:** Multiple scores (e.g., 7.8, 6.8, 9.8, 8.8, 8.4, 8.1, 7.1)
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true (proof‑of‑concept for CVE‑2026‑50507 via CrowdStrike blog)
- **Patch Available:** true (https://support.microsoft.com/en-us/topic/june-9-2026-kb5094126-os-builds-26200-8655-and-26100-8655-1a9bcba6-5f53-4075-8156-fe11ac631737)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the Microsoft June 2026 updates (KB5094126) immediately. For the DHCP client vulnerability (CVE‑2026‑44815) restrict or monitor applications calling DhcpGetOriginalSubnetMask API and block rogue DHCP servers. For the BitLocker issue (CVE‑2026‑50507) ensure physical device security and follow vendor guidance. Use network segmentation, least‑privilege principles, and CrowdStrike Falcon Exposure Management to prioritize remediation.
- **Vendor Advisory:** https://support.microsoft.com/en-us/topic/june-9-2026-kb5094126-os-builds-26200-8655-and-26100-8655-1a9bcba6-5f53-4075-8156-fe11ac631737

---

## 10. 🟠 Zero-Day — Cisco fixes SD-WAN vManage flaw exploited in zero-day attacks

**CVE:** `CVE-2026-20262` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://www.bleepingcomputer.com/news/security/cisco-fixes-sd-wan-vmanage-flaw-exploited-in-zero-day-attacks/>

> Cisco has released security updates to address a vulnerability in the Catalyst SD-WAN Manager, tracked as CVE-2026-20262, that was exploited in attacks to escalate to root privileges. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Insufficient validation of user‑supplied input during file uploads allows low‑privilege remote attackers to create or overwrite arbitrary files via crafted HTTP requests to an affected API endpoint, which can later be leveraged to gain root privileges.
- **Affected Products:** Cisco Catalyst SD-WAN Manager (on‑prem, SD-WAN Cloud‑Pro, SD-WAN Cloud (Cisco Managed), SD-WAN for Government (FedRAMP)); Fixed releases: 20.9.9.2, 20.12.7.2, 20.15.4.5, 20.15.5.3, 20.18.3.1, 26.1.1.2
- **CVSS Score:** 6.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:N
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply Cisco’s fixed software immediately; monitor vmanage‑server, vmanage‑appserver, and serviceproxy‑access logs for upload attempts (index.jsp, .war); no vendor workarounds are available.
- **Vendor Advisory:** https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-arbfw-c2rZvQ

---

## 11. 🟠 Zero-Day — ⚡ Weekly Recap: Chrome 0-Day, UniFi Exploits, macOS Stealers, VPN Flaw and More

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://thehackernews.com/2026/06/weekly-recap-chrome-0-day-unifi.html>

> Stuff broke again. Not in a movie way. An old tool was left exposed. An abandoned package was abused. A deprecated feature was still running in prod.

This week is the same lesson in a new form: phishing kits are easier to rent, AI names are useful bait, old login paths still fail, and forgotten software keeps becoming someone else&#x27;s entry point.

Scroll through the full Monday Cybersecurity

---

## 12. 🟡 High Severity — aws-cdk-lib: OS Command Injection in NodejsFunction Bundling

**CVE:** `CVE-2026-11417` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-999r-qq7v-r334>

> ### Summary
AWS CDK (`aws-cdk-lib`) is an open-source framework for defining cloud infrastructure in code and provisioning it through AWS CloudFormation. OS command injection in the `NodejsFunction` local bundling pipeline in `aws-cdk-lib` before 2.245.0 (2.246.0 on Windows) might allow a threat actor who controls the value of one or more bundling properties (`externalModules`, `define`, `loader`,…

---

## 13. 🟡 High Severity — Netty: QUIC stateless reset token material exposed through header-visible connection IDs

**CVE:** `CVE-2026-50009` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-cq4q-cv5g-r8q5>

> ### Summary
Netty QUIC exposes the stateless reset token on the network path when using the default HMAC-based connection-ID and stateless-reset-token generators. The reset token for the server&#x27;s current source connection ID can be derived from bytes that appear as the connection ID in QUIC headers after a source-CID rotation. An on-path attacker observing the headers can use the token to per…

---

## 14. 🟡 High Severity — Netty HTTP/3 QPACK Blocked Streams Memory Exhaustion

**CVE:** `CVE-2026-48748` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-4grm-h2qv-h6w6>

> ### Summary
A memory exhaustion vulnerability in the Netty HTTP/3 codec allows the creation of an infinite number of blocked streams, which can cause OOM error.

### Details
The vulnerability exists in `io.netty.handler.codec.http3.QpackDecoder#shouldWaitForDynamicTableUpdates`:

If a client sends a header referencing a table entry that the server hasn&#x27;t received yet, the server must pause th…

---

## 15. 🟡 High Severity — Starlette: Unvalidated request path concatenated into authority poisons request.url.hostname

**CVE:** `CVE-2026-54282` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-jp82-jpqv-5vv3>

> ### Summary

In affected versions, the HTTP request path is not validated before being used to reconstruct `request.url`. Because `request.url` is rebuilt by concatenating `{scheme}://{host}{path}` and re-parsing the result, a path that does not begin with `/` (for example `@google.com`) moves the authority boundary during re-parsing, so `request.url.hostname` and `request.url.netloc` become attac…

---

## 16. 🟡 High Severity — python-multipart: Semicolon treated as querystring field separator enables parameter smuggling

**CVE:** `CVE-2026-53538` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-6jv3-5f52-599m>

> ### Summary

`QuerystringParser` treated `;` as a field separator in `application/x-www-form-urlencoded` bodies, in addition to `&amp;`. The [WHATWG URL standard](https://url.spec.whatwg.org/#urlencoded-parsing), modern browsers, and Python&#x27;s `urllib.parse` (since the CVE-2021-23336 fix) treat only `&amp;` as a separator. This creates a parser differential: the same bytes are tokenized into d…

---

## 17. 🟡 High Severity — Tornado: Authorization header forwarded across cross-origin redirects in SimpleAsyncHTTPClient

**CVE:** `CVE-2026-49853` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-3x9g-8vmp-wqvf>

> ## Summary

When SimpleAsyncHTTPClient follows a 3xx redirect, it shallow-copies the original HTTPRequest, rewrites the URL, decrements max_redirects, and removes only the Host header. It does not clear Authorization, auth_username, auth_password, or auth_mode when the redirect target changes origin.

As a result, credentials intended for one origin can be forwarded to a different origin when foll…

---

## 18. 🟡 High Severity — Starlette: SSRF and NTLM credential theft via UNC paths in StaticFiles on Windows

**CVE:** `CVE-2026-48818` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-wqp7-x3pw-xc5r>

> ### Summary

When serving static files on Windows, `StaticFiles` resolves the requested path with [`os.path.realpath`](https://docs.python.org/3/library/os.path.html#os.path.realpath). If a UNC path (such as `\\attacker.com\share`) reaches the resolver, `realpath` causes the process to open a connection to the remote host over SMB (port 445). This is a server-side request forgery (SSRF) that leaks…

---

## 19. 🟡 High Severity — PyJWKClient: missing scheme allowlist enables CVE-2024-21643-class SSRF + token forgery via file://, ftp://, data: schemes

**CVE:** `CVE-2026-48522` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-993g-76c3-p5m4>

> &gt; [!NOTE]
&gt; The library does not directly return non-HTTP(S) URI contents to the attacker; the chained &quot;plant a JWKS to forge tokens&quot; scenario described in the original report requires additional application-layer flaws (attacker write access to a filesystem path, untrusted jku derivation) that this fix does not address. Severity is scored for the scheme-acceptance bug in isolation…

---

## 20. 🟡 High Severity — PyJWT: Public-key JWK accepted as HMAC secret enables forged HS256 tokens when mixed families are allowed

**CVE:** `CVE-2026-48526` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-xgmm-8j9v-c9wx>

> &gt; [!NOTE]
&gt; Exploitation requires a verifier configured with both symmetric and asymmetric algorithms in `algorithms=[…]` and a raw-JSON JWK as the `key=` argument, both contrary to documented usage, hence the High attack-complexity rating.

### Summary
When the verifier is decoding JSON Web Tokens, while supporting both asymmetric and HMAC algorithms, the library does not validate use of JS…

---

## 21. 🟡 High Severity — Symfony: Mailomat Mailer Webhook Parser Reads the HMAC Algorithm from the Request: Signature Algorithm Downgrade

**CVE:** `CVE-2026-48747` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-rrj9-5q2j-4gvr>

> ### Description

`Symfony\Component\Mailer\Bridge\Mailomat\Webhook\MailomatRequestParser::validateSignature()` parses the `X-MOM-Webhook-Signature` request header as `algo=signature` and passes the wire-supplied `$algo` directly to `hash_hmac()` when verifying the request against the configured webhook secret. The request therefore selects the HMAC primitive used to authenticate it.

PHP&#x27;s `h…

---

## 22. 🟡 High Severity — Symfony: IpUtils::PRIVATE_SUBNETS Omits IPv6 Transition Forms (6to4, NAT64, Teredo, IPv4-compatible): SSRF Bypass in NoPrivateNetworkHttpClient

**CVE:** `CVE-2026-48736` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-38cx-cq6f-5755>

> ### Description

`Symfony\Component\HttpClient\NoPrivateNetworkHttpClient` is documented as a decorator that blocks requests to private networks by default. The list of blocked subnets (`Symfony\Component\HttpFoundation\IpUtils::PRIVATE_SUBNETS` on 6.4+, a private constant in `NoPrivateNetworkHttpClient` on 5.4) enumerates RFC1918, loopback, link-local and IPv4-mapped IPv6 (`::ffff:0:0/96`) prefix…

---

## 23. 🟡 High Severity — @angular/service-worker: Sensitive Header Leakage on Cross-Origin Redirects in Angular Service Worker

**CVE:** `CVE-2026-54264` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-qxh6-94w6-9r5p>

> An information disclosure vulnerability exists in the `@angular/service-worker` package of the Angular framework. When the Service Worker fetches assets, it preserves metadata (such as headers) from the original request. However, on cross-origin redirects, the Service Worker fails to strip sensitive headers, violating the Fetch redirect algorithm. 

This allows a remote attacker to obtain sensitiv…

---

## 24. 🟡 High Severity — Angular: Template and Attribute Namespace Sanitization Bypass (XSS)

**CVE:** `CVE-2026-50557` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-f3m7-gqxr-g87x>

> An issue in the `@angular/compiler` and `@angular/core` packages allows bypassing element and attribute sanitization/validation through specific namespace workarounds.

Specifically, namespaced script elements (e.g., `&lt;svg:script&gt;` or `&lt;:svg:script&gt;`) were not properly identified as script elements by the Angular template preparser, allowing them to pass through template compilation wi…

---

## 25. 🟡 High Severity — node-tar applies PAX size override to intermediary GNU long-name/long-link headers, causing tar parser interpretation differential (file smuggling)

**CVE:** `CVE-2026-53655` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-vmf3-w455-68vh>

> ### Summary

`tar` (node-tar) applies a PAX extended header&#x27;s `size=` record (and other PAX
overrides) to the **next header entry of any type**, including intermediary
metadata headers such as a GNU long-name (`L`) or long-link (`K`) entry. Per
POSIX pax, a PAX extended header (`x`) describes the *next file entry*, not the
intermediary extension headers that may sit between the `x` header and…

---

## 26. 🟡 High Severity — @angular/service-worker: Request Credential & Cache Policy Stripping

**CVE:** `CVE-2026-50184` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-95qp-cmmw-mgqv>

> An issue in the `@angular/service-worker` package compromises the integrity of request-policy enforcement during request reconstruction. When the Angular Service Worker intercepts network requests for matched assets, it reconstructs a new `Request` object using an internal helper function.

During this reconstruction process, the helper function strips explicit client-defined safety parameters: th…

---

## 27. 🟡 High Severity — @angular/platform-server: URL Parser Differential leading to SSRF Allowlist Bypass

**CVE:** `CVE-2026-50168` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-xrxm-cp7j-8xf6>

> An issue in the `@angular/platform-server` package allows remote attackers to bypass host allowlist constraints and direct server-side outgoing requests to arbitrary external endpoints. This occurs due to a parser differential between the strict WHATWG URL parser used for allowlist validation and the lenient Domino URL parser used to initialize the server emulated DOM.

When a server-side request …

---

## 28. 🟡 High Severity — Angular Client Hydration DOM Clobbering & Response-Cache Poisoning

**CVE:** `CVE-2026-54267` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-rgjc-h3x7-9mwg>

> To optimize client-side bootstrap in Server-Side Rendered (SSR) environments, Angular supports **Hydration** via `provideClientHydration()`. During SSR, Angular serializes the application&#x27;s runtime state (such as cached `HttpClient` responses) and outputs it into the HTML stream as a `&lt;script&gt;` tag with a predictable identifier:

```html
&lt;script type=&quot;application/json&quot; id=&…

---

## 29. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
