# Zero Day Pulse

> **Generated:** 2026-06-09 14:18 UTC &nbsp;|&nbsp; **Total:** 30 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 17 &nbsp;|&nbsp; 🟡 High: 13 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** An unauthenticated remote attacker can exploit a directory traversal flaw in SimpleHelp remote support software (≤ v5.5.7) to read sensitive files by supplying crafted file paths.
- **Affected Products:** SimpleHelp Remote Support Software version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (unspecified)
- **Mitigation:** Update SimpleHelp to version 5.5.8 or later. If immediate patching is not possible, restrict remote access, enforce least‑privilege network segmentation, and monitor for suspicious file‑access activity.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — CISA gives feds 3 days to patch Check Point VPN bug exploited as zero-day

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-check-point-flaw-exploited-by-ransomware-gangs/>

> CISA has ordered U.S. government agencies to secure their Check Point Remote Access VPN and Mobile Access deployments against a critical vulnerability exploited in zero-day attacks by Qilin ransomware affiliates. [...]

**Parallel AI Enrichment:**

- **Technical Details:** The flaw enables unauthenticated remote attackers to bypass password‑based authentication, granting access without valid credentials.
- **Affected Products:** Check Point Remote Access VPN, Check Point Mobile Access
- **CVSS Score:** 9.3
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Qilin ransomware affiliates
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — LiteLLM Flaw CVE-2026-42271 Exploited in the Wild, Chains to Unauthenticated RCE

**CVE:** `CVE-2026-42271` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://thehackernews.com/2026/06/litellm-flaw-cve-2026-42271-exploited.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Monday added a high-severity flaw impacting BerriAI LiteLLM to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

The vulnerability, tracked as CVE-2026-42271 (CVSS score: 8.7), is a command injection vulnerability that could allow any authenticated user to run arbitrary commands on the

**Parallel AI Enrichment:**

- **Technical Details:** Command‑injection vulnerability in LiteLLM (an AI gateway/proxy) that allows an authenticated user to execute arbitrary system commands via crafted input to the vulnerable component.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 8.7
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — PHPSpreadsheet has a patch bypass for CVE-2026-34084 

**CVE:** `CVE-2026-45034` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-87m4-826x-3crx>

> ## Summary

CVE-2026-34084 was patched by the helper `File::prohibitWrappers`. The helper calls `parse_url($filename, PHP_URL_SCHEME)` and then checks `is_string($scheme) &amp;&amp; strlen($scheme) &gt; 1` to reject stream wrappers such as `phar://`, `php://`, `data://` or `expect://`. The check is not equivalent to &quot;does the path contain a wrapper&quot;. When the input has the form `phar:///…

**Parallel AI Enrichment:**

- **Technical Details:** The patched helper File::prohibitWrappers calls parse_url($filename, PHP_URL_SCHEME) and checks is_string($scheme) && strlen($scheme) > 1 to reject stream wrappers (e.g., phar://, php://, data://, expect://). However, when an input uses three or more slashes after the scheme (e.g., phar:///path/file.phar/inner), parse_url returns boolean false for the scheme, causing the is_string check to be skipped and allowing the crafted path to bypass the wrapper‑prohibition check.
- **Affected Products:** PHPSpreadsheet
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** true
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Ensure the vendor patch is applied. As a workaround, validate paths for wrapper prefixes more robustly (e.g., explicitly detect known wrappers with a regex or normalize URLs before parse_url), and deny inputs containing known wrapper schemes or patterns such as phar://, php://, data:// regardless of slash count.
- **Vendor Advisory:** https://github.com/advisories/GHSA-87m4-826x-3crx

---

## 5. 🟠 Zero-Day — Critical Check Point VPN Zero-Day Exploited in the Wild (CVE-2026-50751)

**CVE:** `CVE-2026-50751` | `CVE-2026-50752` | `CVE-2024-24919` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://www.rapid7.com/blog/post/etr-critical-check-point-vpn-zero-day-exploited-in-the-wild-cve-2026-50751>

> Overview On June 8, 2026, Check Point published a security advisory for CVE-2026-50751 , a critical authentication bypass vulnerability affecting Check Point Remote Access VPN, Mobile Access, and Spark Firewall products. The vulnerability affects deployments configured to use the deprecated IKEv1 key exchange protocol where gateways accept legacy Remote Access clients and do not require a machine …

**Parallel AI Enrichment:**

- **Technical Details:** A logic flow weakness in IKEv1 handling allows remote unauthenticated attackers to bypass user authentication and establish a remote access VPN connection without a valid user password (improper authentication, CWE‑287).
- **Affected Products:** Check Point Remote Access VPN, Check Point Mobile Access, Check Point Spark Firewall
- **CVSS Score:** 9.3
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Qilin ransomware affiliate
- **Mitigation:** Apply the vendor hotfix immediately; disable IKEv1 where possible; require machine certificates for remote access; restrict management and remote access from untrusted networks; monitor VPN logs for anomalous connections.
- **Vendor Advisory:** http://blog.checkpoint.com/security/check-point-releases-important-hotfix-for-vulnerabilities-in-deprecated-ikev1-vpn-protocol

---

## 6. 🟠 Zero-Day — Gogs patches critical zero-day enabling remote code execution

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://www.bleepingcomputer.com/news/security/gogs-patches-critical-zero-day-enabling-remote-code-execution/>

> Gogs has patched a critical security zero-day flaw that can allow attackers to compromise Internet-facing instances and access any repositories (including private ones). [...]

**Parallel AI Enrichment:**

- **Technical Details:** A path‑traversal and symlink handling flaw in Gogs' repository file editing functionality (CVE‑2025‑8110) lets an attacker overwrite files outside the repository (including web‑root or executable files), leading to remote code execution.
- **Affected Products:** Gogs (self‑hosted Git service) – versions prior to patched release (specific versions not provided).
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor patch immediately; if a patch is unavailable, restrict internet access to Gogs instances, disable file‑editing features, remove or disallow symbolic links in repositories, and isolate/backup systems for forensic analysis.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 7. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an attack where adversarial content is placed in external web sources or retrieval corpora; AI agents or RAG systems retrieve this content and the injected instructions in the retrieved text influence the agent’s prompt or behavior, causing unintended actions or data exfiltration. Researchers demonstrated real‑world IPI and related zero‑click exploits (e.g., GeminiJack) using malicious content seeded in external corpora that is retrieved and executed by agentic systems.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Use multi‑layered defenses: avoid treating retrieved content as authoritative; sanitize and validate retrieval outputs; apply strict role and instruction separation (instruction/response parsing), input/output filtering, context window limits, source allowlists/blocklists, provenance checks, and RAG pipeline hardening. Follow Google’s vendor guidance: https://blog.google/security/prompt-injections-web/ and Workspace mitigation guidance: https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 8. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) embeds malicious instructions in data or tools used by LLMs (including retrieval sources and agentic tool outputs) to influence model behavior, possibly without user input; mitigations involve sanitizing retrievals, isolating tool outputs, and layered defenses.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false; advisory URL: http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Layered defense strategy: input filtering, retrieval sanitization, response filtering, hazard policies, monitoring, and continuous improvements; follow vendor guidance in advisory.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 9. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The primary threat is indirect prompt injection, where malicious sites influence an agentic browser's AI prompts or actions, potentially leading to unsafe behaviours. Chrome mitigates this by adding layered defenses that block prompt injections, restrict origin access, and prevent unsafe AI actions.
- **Affected Products:** Google Chrome (agentic/Gemini agentic browsing feature)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Enable the latest Chrome updates (which include the layered defenses), restrict or disable agentic/Gemini agentic browsing features where possible, and follow the guidance in the advisory URL. If updates cannot be applied, disable the agentic features and limit site permissions.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecturing-security-for-agentic.html

---

## 10. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known.
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 11. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 12. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

---

## 13. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 14. 🟠 Zero-Day — Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now

**CVE:** `CVE-2026-11645` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://thehackernews.com/2026/06/chrome-v8-zero-day-cve-2026-11645.html>

> Google has released security updates to address 74 vulnerabilities, including one that has come under active exploitation in the wild.

The high-severity vulnerability, tracked as CVE-2026-11645 (CVSS score: 8.8), has been described as an out-of-bounds memory access in V8, Chrome&#x27;s JavaScript and WebAssembly engine.

&quot;Out-of-bounds read and write in V8 in Google Chrome prior to 149.0.782…

---

## 15. 🟠 Zero-Day — Check Point VPN Zero-Day Exploited in Qilin Ransomware Attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.securityweek.com/check-point-vpn-zero-day-exploited-in-qilin-ransomware-attacks/>

> The authentication bypass vulnerability allows attackers to establish VPN connections without a valid password. The post Check Point VPN Zero-Day Exploited in Qilin Ransomware Attacks appeared first on SecurityWeek .

---

## 16. 🟠 Zero-Day — Google patches new Chrome zero-day flaw exploited in the wild

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://www.bleepingcomputer.com/news/security/google-patches-fifth-chrome-zero-day-bug-exploited-in-attacks-this-year/>

> Google has released emergency updates to patch another Chrome zero-day vulnerability that has been exploited in the wild, the fifth such flaw patched since the start of the year. [...]

---

## 17. 🟠 Zero-Day — Dulwich has unbounded memory allocation in receive-pack from crafted thin packs

**CVE:** `CVE-2026-47734` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-xrvj-v92f-53gj>

> ## Impact

An uncontrolled-resource-consumption (memory exhaustion) denial-of-service vulnerability (CWE-400 / CWE-789).

A client with push access could push a tiny crafted thin pack (~174 bytes)  whose delta header declares a huge   dest_size. When dulwich ingested it via  add_thin_pack / apply_delta, it would  allocate hundreds of MB of memory based on that attacker-controlled size, with no rel…

---

## 18. 🟡 High Severity — SEC Consult SA-20260608-0 :: Privilege Escalation via Binary Planting in Genetec-provided RabbitMQ in multiple Genetec products

**CVE:** `CVE-2026-25112` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-06-09
**Reference:** <https://seclists.org/fulldisclosure/2026/Jun/2>

> Posted by SEC Consult Vulnerability Lab via Fulldisclosure on Jun 08 SEC Consult Vulnerability Lab Security Advisory &lt; 20260608-0 &gt; ======================================================================= title: Privilege Escalation via Binary Planting product: Genetec-provided RabbitMQ in multiple Genetec products vulnerable version: Multiple products, see below. fixed version: Multiple prod…

---

## 19. 🟡 High Severity — Arc has an authenticated arbitrary local-file read via DuckDB I/O functions that bypasses RBAC table-level checks

**CVE:** `CVE-2026-47735` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-p2j4-c4g6-rpf5>

> ### Summary

Arc&#x27;s user-SQL validator (`internal/api/query.go:ValidateSQLRequest`) blocked only `read_parquet(` and `arc_partition_agg(` via regex denylist. The broader DuckDB I/O function family — `read_csv_auto`, `read_csv`, `read_json`, `read_json_auto`, `read_text`, `read_blob`, `glob`, `parquet_metadata`, `parquet_schema`, `read_xlsx`, etc. — was not blocked. RBAC table-reference extract…

---

## 20. 🟡 High Severity — nebula-mesh: GET /api/v1/audit-log discloses all entries to any operator

**CVE:** `CVE-2026-47726` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-qm33-p5p9-f8vg>

> `internal/api/audit.go:12` — `handleGetAuditLog` does no admin check. The route is bearer-auth gated only; any operator API key returns the full audit log via `store.ListAuditEntries` (up to limit=1000). This includes cross-tenant actor names, host/CA/operator IDs, action timestamps, and masked-IP entries from rate-limit refusals — enough surface for a tenant to enumerate the server&#x27;s activit…

---

## 21. 🟡 High Severity — nebula-mesh's web UI lacks CSRF tokens on /ui/* mutating endpoints

**CVE:** `CVE-2026-47725` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-273q-qgh5-wrj6>

> Every `/ui/*` POST / PUT / PATCH / DELETE route processes the request as soon as the session cookie validates. `SameSite=Lax` on the session cookie prevents most cross-site form submits but does not protect:

- top-level form-submit navigations from third-party pages (some browsers still send Lax cookies on top-level POSTs)
- same-registrable-domain attackers (sibling-subdomain XSS, subdomain take…

---

## 22. 🟡 High Severity — nebula-mesh: API endpoints lack ownership checks, enabling cross-operator privilege escalation

**CVE:** `CVE-2026-47724` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-598g-h2vc-h5vg>

> The `/api/v1/*` route surface trusts the bearer token alone for authorisation on most endpoints. The codebase itself admits this at `internal/api/hosts.go:384`: *&quot;API trusts the bearer token for authorisation; per-CA ownership is enforced only in the Web layer.&quot;*

The Web UI gates state-changing routes through `loadAccessibleCA` (`internal/web/cas.go`); CA-management endpoints in `intern…

---

## 23. 🟡 High Severity — nebula-mesh: Web UI and API responses lack security headers (CSP, X-Frame-Options, HSTS, etc.)

**CVE:** `CVE-2026-47723` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-w7w5-5gcp-38rw>

> None of the response paths in `internal/web/` or `internal/api/` set the standard browser-security headers. `grep` for `Content-Security-Policy`, `X-Frame-Options`, `Strict-Transport-Security`, `X-Content-Type-Options`, `Referrer-Policy` returns zero matches across the codebase.

## Impact
The admin UI signs CA certificates, mints API keys (returned inline once per page), displays TOTP QR codes, a…

---

## 24. 🟡 High Severity — nebula-mesh: Host advanced overrides allow YAML injection into agent config.yml

**CVE:** `CVE-2026-47722` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-7hp6-g3pq-3pc3>

> `internal/configgen/generator.go:86,108,119` interpolates the operator-supplied `ListenHost` and `TunDevice` fields raw into a `text/template` that produces the agent&#x27;s `config.yml`. `internal/web/advanced.go:20-35` accepts both with only `strings.TrimSpace` — no character or shape validation.

## Exploit
An operator (or attacker with any operator key, given the cross-tenant CRUD advisory) se…

---

## 25. 🟡 High Severity — FUXA: Unauthenticated SSRF via Socket.IO DEVICE_WEBAPI_REQUEST and DEVICE_PROPERTY with response reading

**CVE:** `CVE-2026-47719` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-w86f-rf9w-h3x6>

> ## Summary

An unauthenticated attacker (Alice) connects to FUXA&#x27;s Socket.IO endpoint and emits a `device-webapi-request` event whose `property.address` field names an arbitrary URL. FUXA&#x27;s `DEVICE_WEBAPI_REQUEST` handler at `server/runtime/index.js:296` calls `axios.get(address)` server-side and broadcasts the full response body back on the same event via `io.emit`. The companion handle…

---

## 26. 🟡 High Severity — Netty: Unix-socket fd receive leaks descriptors when peer sends two at once

**CVE:** `CVE-2026-45536` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-w573-9ffj-6ff9>

> netty_unix_socket_recvFd sets msg_control to `char control[CMSG_SPACE(sizeof(int))]` (line 940) — 24 bytes on 64-bit Linux. A peer-sent SCM_RIGHTS cmsg carrying two ints has cmsg_len = CMSG_LEN(8) = 24, which fits exactly with no MSG_CTRUNC, so the kernel installs both fds in the receiving process. The subsequent check `cmsg-&gt;cmsg_len == CMSG_LEN(sizeof(int))` (line 972, expected 20) fails, the…

---

## 27. 🟡 High Severity — Netty: HAProxy SSL TLV parsing leaks retained slice on invalid TLV length

**CVE:** `CVE-2026-44893` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-cc37-9q2j-3hfv>

> When decoding a PP2_TYPE_SSL TLV, HAProxyMessage.readNextTLV() first calls `header.retainedSlice(header.readerIndex(), length)` and only then reads the 1-byte client field and 4-byte verify field. If the attacker sets the TLV length below 5, the subsequent readByte/readInt throws IndexOutOfBoundsException. HAProxyMessageDecoder only catches HAProxyProtocolException around this call, so the IOOBE p…

---

## 28. 🟡 High Severity — Netty has Unbounded Direct Memory Consumption in its RedisDecoder

**CVE:** `CVE-2026-44890` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-6ghj-frrj-jjj3>

> ### Summary
An attacker can cause DoS by sending crafted Redis payloads across multiple connections without `\r\n`. This exhausts the server&#x27;s direct memory pool (OutOfDirectMemoryError), preventing legitimate connections from being processed.

### Details
io.netty.handler.codec.redis.RedisDecoder decodes the length of bulk strings and array headers using the `decodeLength` method. This metho…

---

## 29. 🟡 High Severity — Critical Check Point VPN Flaw Exploited to Bypass Passwords in IKEv1 Setups

**CVE:** `CVE-2026-50751` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://thehackernews.com/2026/06/critical-check-point-vpn-flaw-exploited.html>

> Check Point has warned of active exploitation of a critical vulnerability impacting Remote Access VPN and Mobile Access deployments that are configured to use the deprecated IKEv1 key exchange protocol.

The vulnerability, tracked as CVE-2026-50751 (CVSS score: 9.3), is a case of a logic flow weakness in certificate validation that allows an unauthenticated remote attacker to bypass user

---

## 30. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
