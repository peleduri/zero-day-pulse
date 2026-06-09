# Zero Day Pulse

> **Generated:** 2026-06-09 19:56 UTC &nbsp;|&nbsp; **Total:** 31 &nbsp;|&nbsp; 🔴 KEV: 3 &nbsp;|&nbsp; 🟠 Zero-Day: 17 &nbsp;|&nbsp; 🟡 High: 11 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🔴 CISA KEV — CVE-2026-11645 — Google Chromium V8 Out-of-Bounds Read and Write Vulnerability

**CVE:** `CVE-2026-11645` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-11645>

> Vendor: Google | Product: Chromium V8. Google Chromium V8 out-of-bounds read and write vulnerability that could allow a remote attacker to execute arbitrary code inside a sandbox via a crafted HTML page. This vulnerability could affect multiple web browsers that utilize Chromium, including, but not limited to, Google Chrome, Microsoft Edge, and Opera. Required action: Apply mitigations per vendor …

**Parallel AI Enrichment:**

- **Technical Details:** Out‑of‑bounds read and write in V8 allows crafted JavaScript/HTML to corrupt memory, leading to arbitrary code execution inside the renderer sandbox.
- **Affected Products:** Google Chrome < 149.0.7827.103 (Windows 149.0.7827.102, macOS 149.0.7827.103, Linux 149.0.7827.102); other Chromium‑based browsers (Microsoft Edge, Opera) that embed the vulnerable V8 version
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor updates immediately; follow BOD 22-01 guidance for cloud services; if patches cannot be applied, discontinue use or isolate affected systems; limit exposure by blocking untrusted HTML content, using content filters and script‑blocking extensions.
- **Vendor Advisory:** https://chromereleases.googleblog.com/

---

## 2. 🔴 CISA KEV — CVE-2026-7473 — Arista Extensible Operating System Incomplete Comparison with Missing Factors Vulnerability

**CVE:** `CVE-2026-7473` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-7473>

> Vendor: Arista | Product: Extensible Operating System. Arista Extensible Operating System (EOS) contains an incomplete comparison with missing factors vulnerability when the switch incorrectly decapsulate and forwards other unexpected tunneled packet with a destination IP matching its configured decapsulation IP. Required action: Apply mitigations per vendor instructions, follow applicable BOD 22-…

**Parallel AI Enrichment:**

- **Technical Details:** When an Arista EOS device is configured as a tunnel endpoint (VXLAN VTEP, GRE endpoint, or IP decap group), it may decapsulate packets whose destination IP matches the configured decap IP without verifying the tunnel protocol type, causing unexpected decapsulation and forwarding of non‑configured tunnel traffic.
- **Affected Products:** Arista EOS 4.36.x, 4.35.x, 4.34.x, 4.33.x, 4.32.x, 4.31.x, 4.30.x, trains older than 4.30.x, trains newer than 4.36.x; platforms 7020R, 7280R/R2, 7500R/R2 (limited exposure on 7280R3, 7500R3, 7800R3)
- **CVSS Score:** 5.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:N/I:L/A:N
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply ACLs on upstream devices or on the decapsulation switch to restrict tunnel types/ports/IPs (examples for VXLAN, GRE, GUE, IP‑in‑IP using IP/MAC ACLs and UDF‑based MAC ACLs). Follow BOD 22‑01 guidance for cloud services; discontinue use if mitigations are unavailable.
- **Vendor Advisory:** https://www.arista.com/en/support/advisories-notices/security-advisory/24005-security-advisory-0137

---

## 3. 🔴 CISA KEV — CVE-2026-20245 — Cisco Catalyst SD-WAN Manager Improper Encoding or Escaping of Output Vulnerability

**CVE:** `CVE-2026-20245` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-20245>

> Vendor: Cisco | Product: Catalyst SD-WAN Manager. Cisco Catalyst SD-WAN Manager formerly SD-WAN vManage contains an improper encoding or escaping of output vulnerability. This vulnerability could allow an authenticated, local attacker to execute arbitrary commands as root by supplying a crafted file to the affected system. Required action: Apply mitigations per vendor instructions, follow applicab…

**Parallel AI Enrichment:**

- **Technical Details:** Improper encoding/escaping of CLI output allows an authenticated, local attacker to inject crafted input that is executed as a root command, resulting in privilege escalation.
- **Affected Products:** Cisco Catalyst SD-WAN Manager (formerly SD-WAN vManage)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Apply mitigations per Cisco's advisory, follow BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **Vendor Advisory:** https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-privesc-4uxFrdzx

---

## 4. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path‑traversal (directory traversal) vulnerability in SimpleHelp 5.5.7 and earlier that lets an unauthenticated remote attacker craft requests to traverse directories and read arbitrary files (e.g., logs, configuration files, credentials) from the server.
- **Affected Products:** SimpleHelp Remote Support / Remote Monitoring and Management (RMM) — versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (including groups linked to DragonForce and other ransomware operators)
- **Mitigation:** Immediately upgrade SimpleHelp to version 5.5.8 or later; if patching is delayed, restrict network access to the SimpleHelp server (block inbound access from untrusted networks, apply firewall rules, use network segmentation), rotate credentials and secrets found on compromised instances, review logs for suspicious access, and follow CISA/vendor incident‑response guidance.
- **Vendor Advisory:** https://www.simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 5. 🟠 Zero-Day — Microsoft’s June 2026 Patch Tuesday Addresses 198 CVEs ( CVE-2026-49160, CVE-2026-50507)

**CVE:** `CVE-2026-49160` | `CVE-2026-50507` | `CVE-2025-10263` | `CVE-2026-8863` &nbsp;|&nbsp; **Source:** Tenable Security Research &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.tenable.com/blog/microsofts-june-2026-patch-tuesday-addresses-198-cves-cve-2026-49160-cve-2026-50507>

> 32 Critical 166 Important 0 Moderate 0 Low Microsoft addresses 198 CVEs in the largest Patch Tuesday release, including three zero-days. Microsoft patched 198 CVEs in its June 2026 Patch Tuesday release, with 32 rated critical and 166 rated as important. Our counts omitted 6 CVEs that were already addressed by Microsoft via servicing and do not require additional customer action to resolve as well…

**Parallel AI Enrichment:**

- **Technical Details:** Denial‑of‑service vulnerability in HTTP.sys where specially crafted HTTP/2 requests with a large number of headers trigger resource exhaustion in the HTTP/2/HTTP/3 stack, causing service disruption.
- **Affected Products:** Windows HTTP.sys
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the June 2026 Microsoft updates. As a temporary measure, configure the MaxHeadersCount registry setting to limit the number of headers in HTTP/2 and HTTP/3 requests and consider rate‑limiting suspicious HTTP/2 traffic.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-49160

---

## 6. 🟠 Zero-Day — Microsoft June 2026 Patch Tuesday fixes 3 zero-day, 200 flaws

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.bleepingcomputer.com/news/microsoft/microsoft-june-2026-patch-tuesday-fixes-3-zero-day-200-flaws/>

> Today is Microsoft&#x27;s June 2026 Patch Tuesday, with security updates for 200 flaws and three publicly disclosed zero-day vulnerabilities. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true - https://www.bleepingcomputer.com/news/microsoft/microsoft-june-2026-patch-tuesday-fixes-3-zero-day-200-flaws/
- **Patch Available:** true - https://msrc.microsoft.com/update-guide/
- **Active Exploitation:** true - https://www.bleepingcomputer.com/news/microsoft/microsoft-june-2026-patch-tuesday-fixes-3-zero-day-200-flaws/
- **Threat Actors:** None known
- **Mitigation:** Apply Microsoft June 2026 updates immediately; follow vendor guidance.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/

---

## 7. 🟠 Zero-Day — CISA gives feds 3 days to patch Check Point VPN bug exploited as zero-day

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-check-point-flaw-exploited-by-ransomware-gangs/>

> CISA has ordered U.S. government agencies to secure their Check Point Remote Access VPN and Mobile Access deployments against a critical vulnerability exploited in zero-day attacks by Qilin ransomware affiliates. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Authentication‑bypass logic flaw in IKEv1 VPN handling that allows remote unauthenticated attackers to bypass user authentication and establish VPN connections without valid credentials.
- **Affected Products:** Check Point Remote Access VPN, Check Point Mobile Access; Security Gateways R82.10 Jumbo Hotfix Take 19
- **CVSS Score:** 9.3
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Qilin ransomware affiliate
- **Mitigation:** Apply Check Point hotfixes/patches per vendor advisory; if immediate patching not possible, disable/decommission deprecated IKEv1 VPN services where feasible and restrict access to management interfaces; follow vendor hardening guidance in SK185033.
- **Vendor Advisory:** https://blog.checkpoint.com/security/check-point-releases-important-hotfix-for-vulnerabilities-in-deprecated-ikev1-vpn-protocol/

---

## 8. 🟠 Zero-Day — LiteLLM Flaw CVE-2026-42271 Exploited in the Wild, Chains to Unauthenticated RCE

**CVE:** `CVE-2026-42271` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://thehackernews.com/2026/06/litellm-flaw-cve-2026-42271-exploited.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Monday added a high-severity flaw impacting BerriAI LiteLLM to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

The vulnerability, tracked as CVE-2026-42271 (CVSS score: 8.7), is a command injection vulnerability that could allow any authenticated user to run arbitrary commands on the

**Parallel AI Enrichment:**

- **Technical Details:** Command injection vulnerability in LiteLLM's MCP/server test endpoints that permits execution of arbitrary commands by an authenticated user; chaining with CVE‑2026‑48710 enables unauthenticated remote code execution against vulnerable deployments.
- **Affected Products:** LiteLLM (BerriAI) proxy server versions >= 1.74.2 and < 1.83.7
- **CVSS Score:** 8.7
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** true — https://github.com/BerriAI/litellm/releases
- **Active Exploitation:** true — https://thehackernews.com/2026/06/litellm-flaw-cve-2026-42271-exploited.html
- **Threat Actors:** None known
- **Mitigation:** Upgrade to patched release (>= 1.83.7). If patch cannot be applied immediately, restrict access to LiteLLM management/MCP endpoints (network ACLs, firewall rules), require/verify authentication, isolate deployments, and monitor for anomalous process execution and suspicious outbound connections.
- **Vendor Advisory:** https://github.com/BerriAI/litellm/releases

---

## 9. 🟠 Zero-Day — PHPSpreadsheet has a patch bypass for CVE-2026-34084 

**CVE:** `CVE-2026-45034` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-87m4-826x-3crx>

> ## Summary

CVE-2026-34084 was patched by the helper `File::prohibitWrappers`. The helper calls `parse_url($filename, PHP_URL_SCHEME)` and then checks `is_string($scheme) &amp;&amp; strlen($scheme) &gt; 1` to reject stream wrappers such as `phar://`, `php://`, `data://` or `expect://`. The check is not equivalent to &quot;does the path contain a wrapper&quot;. When the input has the form `phar:///…

**Parallel AI Enrichment:**

- **Technical Details:** A fix for CVE-2026-34084 added File::prohibitWrappers which calls parse_url($filename, PHP_URL_SCHEME) and rejects a scheme only when is_string($scheme) && strlen($scheme) > 1. If a filename uses the form phar:///path/file.phar/inner (three or more slashes), parse_url returns boolean false for the scheme, causing the is_string check to be skipped and the helper to fail to detect the phar stream wrapper, allowing the earlier vulnerability to be bypassed.
- **Affected Products:** PHPOffice/PhpSpreadsheet versions 1.30.2 and earlier, 2.0.0 through 2.1.14
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — http://github.com/advisories/GHSA-87m4-826x-3crx
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Sanitize and validate filenames by explicitly detecting wrappers (e.g., check for known wrapper prefixes like "phar://", "php://", "data://", or use a more robust parse that treats multiple slashes), upgrade when an official patch is available, and avoid loading untrusted filenames. If immediate mitigation required, add a custom check for substrings matching "://" or use a stricter whitelist of allowed file path patterns.
- **Vendor Advisory:** http://github.com/advisories/GHSA-87m4-826x-3crx

---

## 10. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when adversarial content seeded on web pages or external content sources influences AI agents that browse or ingest that content, causing them to follow malicious instructions or leak sensitive data. Attack vector: poisoned web content or third‑party sources referenced by AI agents’ browsing/RAG pipelines.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply defense‑in‑depth: validate and sanitize external content before use; apply source reputation and allowlists; use prompt‑layering and instruction‑sanitization techniques; limit agent permissions and data exfiltration capabilities; monitor telemetry for anomalous model outputs; keep models and retrieval pipelines updated. (Mitigations summarized from Google Security Blog guidance.)
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 11. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

---

## 12. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

---

## 13. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

---

## 14. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 15. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

---

## 16. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 17. 🟠 Zero-Day — Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now

**CVE:** `CVE-2026-11645` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://thehackernews.com/2026/06/chrome-v8-zero-day-cve-2026-11645.html>

> Google has released security updates to address 74 vulnerabilities, including one that has come under active exploitation in the wild.

The high-severity vulnerability, tracked as CVE-2026-11645 (CVSS score: 8.8), has been described as an out-of-bounds memory access in V8, Chrome&#x27;s JavaScript and WebAssembly engine.

&quot;Out-of-bounds read and write in V8 in Google Chrome prior to 149.0.782…

---

## 18. 🟠 Zero-Day — Check Point VPN Zero-Day Exploited in Qilin Ransomware Attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.securityweek.com/check-point-vpn-zero-day-exploited-in-qilin-ransomware-attacks/>

> The authentication bypass vulnerability allows attackers to establish VPN connections without a valid password. The post Check Point VPN Zero-Day Exploited in Qilin Ransomware Attacks appeared first on SecurityWeek .

---

## 19. 🟠 Zero-Day — Google patches new Chrome zero-day flaw exploited in the wild

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.bleepingcomputer.com/news/security/google-patches-fifth-chrome-zero-day-bug-exploited-in-attacks-this-year/>

> Google has released emergency updates to patch another Chrome zero-day vulnerability that has been exploited in the wild, the fifth such flaw patched since the start of the year. [...]

---

## 20. 🟠 Zero-Day — Dulwich has unbounded memory allocation in receive-pack from crafted thin packs

**CVE:** `CVE-2026-47734` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-xrvj-v92f-53gj>

> ## Impact

An uncontrolled-resource-consumption (memory exhaustion) denial-of-service vulnerability (CWE-400 / CWE-789).

A client with push access could push a tiny crafted thin pack (~174 bytes)  whose delta header declares a huge   dest_size. When dulwich ingested it via  add_thin_pack / apply_delta, it would  allocate hundreds of MB of memory based on that attacker-controlled size, with no rel…

---

## 21. 🟡 High Severity — Veeam Backup & Replication RCE Flaw Lets Domain Users Run Remote Code

**CVE:** `CVE-2026-44963` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://thehackernews.com/2026/06/veeam-backup-replication-rce-flaw-lets.html>

> Veeam has released security patches to address a critical flaw in its Backup &amp; Replication software that could result in remote code execution.

Tracked as CVE-2026-44963, the vulnerability carries a CVSS score of 9.4 out of a maximum of 10.0.

&quot;A vulnerability allowing remote code execution (RCE) on the Backup Server by an authenticated domain user,&quot; Veeam said in a Tuesday advisory…

---

## 22. 🟡 High Severity — SEC Consult SA-20260608-0 :: Privilege Escalation via Binary Planting in Genetec-provided RabbitMQ in multiple Genetec products

**CVE:** `CVE-2026-25112` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://seclists.org/fulldisclosure/2026/Jun/2>

> Posted by SEC Consult Vulnerability Lab via Fulldisclosure on Jun 08 SEC Consult Vulnerability Lab Security Advisory &lt; 20260608-0 &gt; ======================================================================= title: Privilege Escalation via Binary Planting product: Genetec-provided RabbitMQ in multiple Genetec products vulnerable version: Multiple products, see below. fixed version: Multiple prod…

---

## 23. 🟡 High Severity — Arc has an authenticated arbitrary local-file read via DuckDB I/O functions that bypasses RBAC table-level checks

**CVE:** `CVE-2026-47735` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-p2j4-c4g6-rpf5>

> ### Summary

Arc&#x27;s user-SQL validator (`internal/api/query.go:ValidateSQLRequest`) blocked only `read_parquet(` and `arc_partition_agg(` via regex denylist. The broader DuckDB I/O function family — `read_csv_auto`, `read_csv`, `read_json`, `read_json_auto`, `read_text`, `read_blob`, `glob`, `parquet_metadata`, `parquet_schema`, `read_xlsx`, etc. — was not blocked. RBAC table-reference extract…

---

## 24. 🟡 High Severity — nebula-mesh: GET /api/v1/audit-log discloses all entries to any operator

**CVE:** `CVE-2026-47726` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-qm33-p5p9-f8vg>

> `internal/api/audit.go:12` — `handleGetAuditLog` does no admin check. The route is bearer-auth gated only; any operator API key returns the full audit log via `store.ListAuditEntries` (up to limit=1000). This includes cross-tenant actor names, host/CA/operator IDs, action timestamps, and masked-IP entries from rate-limit refusals — enough surface for a tenant to enumerate the server&#x27;s activit…

---

## 25. 🟡 High Severity — nebula-mesh's web UI lacks CSRF tokens on /ui/* mutating endpoints

**CVE:** `CVE-2026-47725` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-273q-qgh5-wrj6>

> Every `/ui/*` POST / PUT / PATCH / DELETE route processes the request as soon as the session cookie validates. `SameSite=Lax` on the session cookie prevents most cross-site form submits but does not protect:

- top-level form-submit navigations from third-party pages (some browsers still send Lax cookies on top-level POSTs)
- same-registrable-domain attackers (sibling-subdomain XSS, subdomain take…

---

## 26. 🟡 High Severity — nebula-mesh: API endpoints lack ownership checks, enabling cross-operator privilege escalation

**CVE:** `CVE-2026-47724` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-598g-h2vc-h5vg>

> The `/api/v1/*` route surface trusts the bearer token alone for authorisation on most endpoints. The codebase itself admits this at `internal/api/hosts.go:384`: *&quot;API trusts the bearer token for authorisation; per-CA ownership is enforced only in the Web layer.&quot;*

The Web UI gates state-changing routes through `loadAccessibleCA` (`internal/web/cas.go`); CA-management endpoints in `intern…

---

## 27. 🟡 High Severity — nebula-mesh: Web UI and API responses lack security headers (CSP, X-Frame-Options, HSTS, etc.)

**CVE:** `CVE-2026-47723` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-w7w5-5gcp-38rw>

> None of the response paths in `internal/web/` or `internal/api/` set the standard browser-security headers. `grep` for `Content-Security-Policy`, `X-Frame-Options`, `Strict-Transport-Security`, `X-Content-Type-Options`, `Referrer-Policy` returns zero matches across the codebase.

## Impact
The admin UI signs CA certificates, mints API keys (returned inline once per page), displays TOTP QR codes, a…

---

## 28. 🟡 High Severity — nebula-mesh: Host advanced overrides allow YAML injection into agent config.yml

**CVE:** `CVE-2026-47722` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-7hp6-g3pq-3pc3>

> `internal/configgen/generator.go:86,108,119` interpolates the operator-supplied `ListenHost` and `TunDevice` fields raw into a `text/template` that produces the agent&#x27;s `config.yml`. `internal/web/advanced.go:20-35` accepts both with only `strings.TrimSpace` — no character or shape validation.

## Exploit
An operator (or attacker with any operator key, given the cross-tenant CRUD advisory) se…

---

## 29. 🟡 High Severity — FUXA: Unauthenticated SSRF via Socket.IO DEVICE_WEBAPI_REQUEST and DEVICE_PROPERTY with response reading

**CVE:** `CVE-2026-47719` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-w86f-rf9w-h3x6>

> ## Summary

An unauthenticated attacker (Alice) connects to FUXA&#x27;s Socket.IO endpoint and emits a `device-webapi-request` event whose `property.address` field names an arbitrary URL. FUXA&#x27;s `DEVICE_WEBAPI_REQUEST` handler at `server/runtime/index.js:296` calls `axios.get(address)` server-side and broadcasts the full response body back on the same event via `io.emit`. The companion handle…

---

## 30. 🟡 High Severity — Netty: Unix-socket fd receive leaks descriptors when peer sends two at once

**CVE:** `CVE-2026-45536` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-w573-9ffj-6ff9>

> netty_unix_socket_recvFd sets msg_control to `char control[CMSG_SPACE(sizeof(int))]` (line 940) — 24 bytes on 64-bit Linux. A peer-sent SCM_RIGHTS cmsg carrying two ints has cmsg_len = CMSG_LEN(8) = 24, which fits exactly with no MSG_CTRUNC, so the kernel installs both fds in the receiving process. The subsequent check `cmsg-&gt;cmsg_len == CMSG_LEN(sizeof(int))` (line 972, expected 20) fails, the…

---

## 31. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
