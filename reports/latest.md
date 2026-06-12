# Zero Day Pulse

> **Generated:** 2026-06-12 02:14 UTC &nbsp;|&nbsp; **Total:** 28 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 16 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a directory traversal vulnerability in SimpleHelp Remote Support Software that allows unauthenticated attackers to read arbitrary files on the server via crafted path inputs.
- **Affected Products:** SimpleHelp Remote Support Software version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit is known.
- **Patch Available:** http://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570
- **Active Exploitation:** Confirmed active exploitation reported by ransomware actors.
- **Threat Actors:** Ransomware actors (unspecified groups)
- **Mitigation:** Update SimpleHelp installations to version 5.5.8 or later, which contains the security fixes.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — Criminal AI-as-a-Service in 2026: How the Underground Market Is Operationalizing Cybercrime

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://www.rapid7.com/blog/post/tr-criminal-ai-underground-market-operationalizing-cybercrime-2026>

> Introduction The underground market for criminally oriented generative AI has moved beyond the early hype surrounding &#x27;malicious chatbots.&#x27; The gradual integration of AI as a productivity layer within cybercrime operations has become the dominant story, indicating that while the potential for fully autonomous AI hacking systems is possible, attackers are not embracing them as expected. I…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit reported; exploit availability unavailable.
- **Patch Available:** Patch available: none; Patch/advisory URL unavailable.
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) leverages external web content or retrieved documents to inject instructions that override model or system prompts, enabling exfiltration or unintended actions; GeminiJack is a zero‑click IPI that embeds malicious payloads inside Google Gemini Enterprise’s retrieval pipeline.
- **Affected Products:** Google Gemini Enterprise, RAG and agentic LLM systems
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Proof‑of‑concept exploits are publicly available via Noma Labs blog (http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability) and an arXiv paper (https://arxiv.org/abs/2601.07072).
- **Patch Available:** Official mitigation guidance is published by Google in the advisory; no specific patch is provided.
- **Active Exploitation:** Reports indicate IPI payloads have been observed in the wild (Forcepoint and Google analyses), but no publicly disclosed active exploitation campaigns or known threat‑actor groups are identified.
- **Threat Actors:** None known
- **Mitigation:** Follow Google guidance: harden retrieval and agent pipelines, sanitize and filter retrieved content, implement retrieval provenance checks, restrict execution of instructions from untrusted sources, and apply principle of least privilege for agents.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when adversarial instructions are embedded in data sources (files, web content, plugins, tool outputs) that an LLM retrieves during query processing, enabling attacker‑supplied instructions to influence model behavior, including zero‑click scenarios where users need not interact.
- **Affected Products:** Google Workspace (including Gemini), Gemini Enterprise
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC/weaponized exploit reported in vendor advisory; public PoCs not identified in sources.
- **Patch Available:** Vendor mitigation guidance published by Google (see advisory URL); no specific patch or versioned fix referenced.
- **Active Exploitation:** Confirmed active exploitation: 10 indirect prompt injection payloads observed in the wild (Forcepoint) and the GeminiJack zero‑click vulnerability discovered by Noma Labs.
- **Threat Actors:** None known
- **Mitigation:** Multi‑layered defenses by Google for Workspace and Gemini – content filtering, retrieval/model hardening, platform controls, continuous detection/response. General mitigations: restrict external content access, enforce strict sharing policies, enable Workspace security controls, monitor for anomalous agent behavior.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is a threat where untrusted content (e.g., malicious sites, third‑party iframes, or user‑generated reviews) injects prompts that cause the AI agent in Chrome to perform unintended actions such as financial transactions or data exfiltration.
- **Affected Products:** Google Chrome (with Gemini agentic capabilities)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept exploit is known.
- **Patch Available:** The layered defenses described in the advisory (user alignment critic, origin‑isolation, user confirmations, real‑time detection) are the official mitigation, available at the advisory URL.
- **Active Exploitation:** No confirmed active exploitation in the wild has been reported.
- **Threat Actors:** None known
- **Mitigation:** Deploy the user alignment critic, enforce origin‑isolation for the agent, require user confirmations for sensitive actions, and enable real‑time detection of prompt‑injection attempts.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit or PoC is mentioned.
- **Patch Available:** No official patch is referenced in the blog post.
- **Active Exploitation:** No reports of active exploitation are mentioned.
- **Threat Actors:** None known
- **Mitigation:** Adopt Rust for new Android components and follow memory‑safety coding practices.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack where hidden malicious instructions are embedded in external data sources (emails, documents, calendar invites, web content, retrieved knowledge) that a generative AI system ingests during retrieval or context assembly, causing the model to follow attacker‑provided instructions (e.g., exfiltrate data or perform unauthorized actions).
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC/weaponized exploit reported; exploit availability unknown.
- **Patch Available:** Patch unavailable; guidance/mitigations provided in vendor advisory above.
- **Active Exploitation:** Yes—security researchers reported in‑the‑wild indirect prompt injection payloads (Forcepoint disclosure of 10 IPI payloads and related industry reports).
- **Threat Actors:** None known
- **Mitigation:** Layered defense—input validation and sanitization, retrieval filtering and provenance checks, context isolation and least privilege, model/system‑level policy enforcement and instruction‑following constraints, monitoring and anomaly detection, human review for high‑risk actions. See vendor advisory for specific recommendations.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Exploitation leverages known remote code execution and authentication‑bypass vulnerabilities in Cisco IOS XE (CVE-2023-20198, CVE-2023-20273, CVE-2018-0171) and Ivanti Connect Secure (CVE-2024-21887), allowing attackers to gain unauthorized access to routers and network infrastructure.
- **Affected Products:** Ivanti Connect Secure, Cisco IOS XE, Cisco IOS/IOS XE
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public exploits for the listed CVEs (CVE-2023-20198, CVE-2018-0171, CVE-2023-20273, CVE-2024-21887) are known to exist, but no direct PoC URLs are provided in the advisory.
- **Patch Available:** Patches are available from the respective vendors for CVE-2024-21887 (Ivanti Connect Secure), CVE-2023-20273 (Cisco IOS XE), CVE-2023-20198 (Cisco IOS XE), and CVE-2018-0171 (Cisco IOS/IOS XE).
- **Active Exploitation:** Confirmed active exploitation of CVE-2023-20198, CVE-2018-0171, CVE-2023-20273, and CVE-2024-21887 has been observed.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching; disable unused ports and protocols; require public‑key authentication for administrative roles; change default credentials; use vendor‑recommended OS versions and keep them updated; monitor firmware/software integrity and perform hash verification.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit available.
- **Patch Available:** No official patch available.
- **Active Exploitation:** Confirmed active exploitation reported in the wild.
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS) (also known as APT28)
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** CVE‑2026‑50507: missing authentication in a critical BitLocker function allows an unauthenticated attacker with physical access to bypass device encryption. CVE‑2026‑26142: deserialization of untrusted data in Nuance PowerScribe leads to remote code execution. CVE‑2026‑44815: stack‑based buffer overflow in the Windows DHCP Client Service can be triggered by a rogue DHCP server when the DhcpGetOriginalSubnetMask API is called. CVE‑2026‑45648: out‑of‑bounds write in the NSPI RPC interface of Active Directory enables remote code execution.
- **Affected Products:** Windows (multiple components), Extended Security Updates (ESU), Microsoft Office, Nuance PowerScribe, Windows DHCP Client Service, Active Directory Domain Services, Device Health Attestation, Windows Media, Windows Graphics Component, Kerberos KDC
- **CVSS Score:** 6.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Proof‑of‑concept exploit exists for CVE‑2026‑50507 (BitLocker bypass); other CVEs have public details but no specific exploit links cited.
- **Patch Available:** Microsoft has published security updates for the listed CVEs; each CVE entry in MSRC includes the advisory and update/patch details.
- **Active Exploitation:** No evidence of active exploitation in the wild for CVE‑2026‑50507; no confirmed active exploitation reported for the other listed CVEs.
- **Threat Actors:** None known
- **Mitigation:** Pre‑patch mitigations include restricting/auditing applications that call DhcpGetOriginalSubnetMask for CVE‑2026‑44815 and noting the physical‑access requirement for the BitLocker bypass (CVE‑2026‑50507); other CVEs rely on Microsoft’s published mitigation guidance.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/

---

## 11. 🟠 Zero-Day — ShinyHunters Exploits Oracle PeopleSoft Zero-Day (CVE-2026-35273) to Breach Universities

**CVE:** `CVE-2026-35273` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://thehackernews.com/2026/06/shinyhunters-exploits-oracle-peoplesoft.html>

> The ShinyHunters extortion crew exploited an unpatched flaw in Oracle PeopleSoft to break into enterprise systems, steal data, and demand payment to keep it private. The campaign hit universities hardest.

Google&#x27;s Mandiant attributes it to the group it tracks as UNC6240, and dates the activity between May 27 and June 9. Oracle did not publish its advisory until June 10, so the bug was a

---

## 12. 🟠 Zero-Day — ‘GreatXML’ Zero-Day Exploit Bypasses BitLocker

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://www.securityweek.com/greatxml-zero-day-exploit-bypasses-bitlocker/>

> The PoC exploits Microsoft Defender’s offline scan to spawn a SYSTEM shell when rebooting in Recovery Mode. The post ‘GreatXML’ Zero-Day Exploit Bypasses BitLocker appeared first on SecurityWeek .

---

## 13. 🟡 High Severity — GeoServer DB2 DataStore Extension has a JNDI Vulnerability via Store Connection

**CVE:** `CVE-2025-27511` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-g628-r368-6vh7>

> ## Summary

Administrator can perform JNDI attack through specially crafted DB2 jdbc url leading to Remote Code Execution (RCE).

## Impact

If GeoServer has DB2 extension installed, this vulnerability can lead to executing arbitrary code.

## Details

Authenticated users can access Vector Data Sources page to creating a new data store through db2 jdbc connection, performing JNDI attack due to unr…

---

## 14. 🟡 High Severity — Russh SSH message fields were decoded through allocation-first parsers before field-specific bounds

**CVE:** `CVE-2026-48110` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-4r3c-5hpg-58qr>

> # SSH message fields were decoded through allocation-first parsers before field-specific bounds

### Summary

Several `russh` client and server message handlers decoded attacker-controlled SSH strings, name-lists, and byte fields into owned allocations before applying field-specific bounds. A remote SSH peer could send oversized, high-fanout, or malformed length-prefixed fields and make the librar…

---

## 15. 🟡 High Severity — AWS Advanced Go Wrapper has Privilege Escalation in Aurora PostgreSQL instance

**CVE:** `CVE-2026-11401` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-r236-5pc3-3qcp>

> Aurora PostgreSQL is a fully managed relational database engine that&#x27;s compatible with PostgreSQL.

An issue in Aurora PostgreSQL using the AWS Go Wrapper waa identified, see CVE-2026-11401.


Impact
An issue in AWS Wrappers for Amazon Aurora PostgreSQL may allow for privilege escalation to rds_superuser role. A low privilege authenticated user can create a crafted function that could be exec…

---

## 16. 🟡 High Severity — Russh: SSH identification parsing accepted non-canonical client banners and did not bound pre-banner input

**CVE:** `CVE-2026-48108` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-76r6-x97p-67vr>

> ### Summary

`russh` did not enforce the SSH identification-string rules as deliberately as OpenSSH. In particular, the server-side identification reader used the same permissive path as the client, allowing pre-banner lines from clients, and the reader did not enforce a bounded number of pre-banner lines.

For a library server built on `russh`, this could allow a remote peer to hold connection se…

---

## 17. 🟡 High Severity — WsgiDAV encoded dot segments can escape filesystem share roots

**CVE:** `CVE-2026-48099` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-wxq4-cc2q-338q>

> ### Impact
WsgiDAV 4.3.3 can allow a WebDAV request path containing an encoded parent-directory segment to escape the configured filesystem share root in a specific path layout.

### Patches
The issue is fixed with version 4.3.4.

### Preconditions

The practical impact depends on the deployment.

The deployment uses a filesystem-backed WsgiDAV share.

The attacker can send WebDAV requests accepte…

---

## 18. 🟡 High Severity — Netty HAProxy: Unbalanced Reference Count in Nested PP2_TYPE_SSL TLV Parsing Leads to Memory Exhaustion

**CVE:** `CVE-2026-48059` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-h2qv-fj59-j46j>

> ### Impact
The HAProxy PROXY protocol v2 codec in netty leaks native or heap memory on every connection when a client sends a syntactically valid header containing nested `PP2_TYPE_SSL` TLVs (type-length-value records) at depth two or greater. The leak occurs on the successful parse path — no exception is thrown, the message fires downstream, the decoder removes itself, and the application release…

---

## 19. 🟡 High Severity — Kolibri has Unauthenticated Server-Side Request Forgery (SSRF) in RemoteFacilityUserViewset

**CVE:** `CVE-2026-48053` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-4mj9-pf4r-cqrc>

> ## Summary

Several Kolibri API endpoints accept an unvalidated `baseurl` parameter and fetch attacker-controlled URLs from the Kolibri server, reflecting the response body back to the caller. The original report identified two endpoints on the `RemoteFacilityUser*` viewsets; remediation review found two further reflection points on the same pattern. The GET endpoint was unauthenticated.

## Affec…

---

## 20. 🟡 High Severity — Arc: Unauthenticated access to Go debug pprof endpoints leaks runtime state and enables CPU-burn DoS

**CVE:** `CVE-2026-48050` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-j93g-rp6m-j32m>

> ### Summary

Arc registers Go&#x27;s `net/http/pprof` handlers at `/debug/pprof/*` via `app.Use(pprof.New())` in `internal/api/server.go`, and `/debug/pprof` is added to `PublicPrefixes` in `cmd/arc/main.go`. The auth middleware short-circuits before the token check on prefix match, so the endpoints are reachable without any authentication.

### Impact

Any network-reachable caller (no token requi…

---

## 21. 🟡 High Severity — @hapi/inert has a static-file confinement bypass via sibling-prefix path

**CVE:** `CVE-2026-48049` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-rcvq-m9j9-6f4g>

> ### Impact
`@hapi/inert` serves static files from a directory configured with `path` (in the `directory` / `file` handlers) or `relativeTo` (for `h.file()`), with confinement enforced by the `confine` option (default `true`). Before the patch, the confinement check compared the resolved absolute path against the confine directory using a raw string-prefix test, so a sibling directory whose absolut…

---

## 22. 🟡 High Severity — python-zeroconf: Unbounded TC-deferred queue allows LAN-local memory exhaustion via spoofed-source flood

**CVE:** `CVE-2026-48045` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-9663-mqmp-p9mm>

> ### Impact

`AsyncListener.handle_query_or_defer` retained every truncated (TC-bit) incoming query in `self._deferred[addr]` and armed a per-addr timer in `self._timers[addr]` that flushed the reassembled query within ~500 ms (RFC 6762 §18.5). Neither the per-addr list nor the number of distinct `addr` keys was capped, and the dedup check (`for incoming in reversed(deferred): if incoming.data == m…

---

## 23. 🟡 High Severity — Meta Ads MCP: Unauthenticated HTTP MCP Tool Execution Leaks Operator Meta Access Token

**CVE:** `CVE-2026-48039` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-9gw6-46qc-99vr>

> # Unauthenticated HTTP MCP Tool Execution Leaks Operator Meta Access Token

| Field            | Value |
| ---------------- | ----- |
| Repository       | pipeboard-co/meta-ads-mcp |
| Affected version | ≤ 1.0.101 (commit 496c988 ~ 7d14226); Versions 1.0.102–1.0.105 lack git tags, so patch status is unconfirmed. |
| Vulnerability    | CWE-287 — Improper Authentication |
| Severity         | Critic…

---

## 24. 🟡 High Severity — @hapi/wreck: Sensitive credential headers leak across cross-port and cross-scheme redirects

**CVE:** `CVE-2026-48022` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-x426-x7cc-3fpc>

> ### Impact
Wreck strips credential headers (Authorization, Cookie, Proxy-Authorization) before following a cross-origin redirect, but the origin check compares hostnames only and ignores scheme and port. As a result, credentials are forwarded intact across same-host port changes and HTTPS-to-HTTP downgrades, allowing a co-tenant on an adjacent port or a network-position attacker capable of forging…

---

## 25. 🟡 High Severity — Netty's Lack of Lifecycle Cleanup Leads to Pooled ByteBuf Leak in RedisArrayAggregator

**CVE:** `CVE-2026-48006` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-6jv9-x5w9-2ccm>

> ### Impact
The RedisArrayAggregator handler permanently leaks pooled direct-memory buffers when a Redis pipeline connection closes before a RESP array aggregate completes. The handler retains child messages in per-handler state (`depths` field) but defines no `channelInactive`, `handlerRemoved`, or `exceptionCaught` method to release them when the pipeline tears down. Because the leaked buffers ar…

---

## 26. 🟡 High Severity — PDM: Project-Controlled `.pdm-plugins` Content Executes Before CLI Parsing

**CVE:** `CVE-2026-47781` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-qq6c-99pv-prvf>

> ## Summary

PDM automatically loads project-local plugin paths from `.pdm-plugins` during `Core` initialization. Because this path is added via `site.addsitedir()`, attacker-controlled `.pth` files inside the project plugin directory are processed and can execute Python code before normal CLI handling begins.

This allows arbitrary code execution with the privileges of the user running `pdm` from …

---

## 27. 🟡 High Severity — free5GC UDR has improper `ueId` validation in EE subscription handlers that allows arbitrary identifier persistence

**CVE:** `CVE-2026-47780` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-6gxq-gpr8-xgjp>

> ### Summary
The free5GC UDR accepts arbitrary non-3GPP ueId values in the EE subscription creation and query flows because the regular expression used for validation ends with the catch-all alternative |.+. This causes the validation logic to accept any non-empty string rather than restricting input to expected SUPI/GPSI-style formats. In a tested deployment, a crafted value such as ARBITRARY_STRI…

---

## 28. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
