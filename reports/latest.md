# Zero Day Pulse

> **Generated:** 2026-06-09 01:56 UTC &nbsp;|&nbsp; **Total:** 29 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 16 &nbsp;|&nbsp; 🟡 High: 13 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated path traversal allowing attackers to read sensitive files such as logs, configuration files, and credentials via crafted requests against SimpleHelp RMM.
- **Affected Products:** SimpleHelp remote support / RMM, versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof‑of‑concept available (e.g., Offsec blog at http://offsec.com/blog/cve-2024-57727)
- **Patch Available:** Yes – vendor has released a patch; see vendor advisory (http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability) and SimpleHelp blog (http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know)
- **Active Exploitation:** Confirmed – CISA advisory reports ransomware actors exploiting unpatched SimpleHelp RMM in the wild since January 2025.
- **Threat Actors:** DragonForce ransomware group and other unidentified ransomware actors
- **Mitigation:** Upgrade to a fixed SimpleHelp version. If a patch is unavailable, isolate/unexpose SimpleHelp instances, restrict network access, and follow CISA guidance (https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a).
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — PHPSpreadsheet has a patch bypass for CVE-2026-34084 

**CVE:** `CVE-2026-45034` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-87m4-826x-3crx>

> ## Summary

CVE-2026-34084 was patched by the helper `File::prohibitWrappers`. The helper calls `parse_url($filename, PHP_URL_SCHEME)` and then checks `is_string($scheme) &amp;&amp; strlen($scheme) &gt; 1` to reject stream wrappers such as `phar://`, `php://`, `data://` or `expect://`. The check is not equivalent to &quot;does the path contain a wrapper&quot;. When the input has the form `phar:///…

**Parallel AI Enrichment:**

- **Technical Details:** The helper File::prohibitWrappers calls parse_url($filename, PHP_URL_SCHEME) and then checks is_string($scheme) && strlen($scheme) > 1 to reject stream wrappers such as phar://, php://, data:// or expect://. When the input has the form phar:///path/file.phar/inner with three or more slashes after the scheme, parse_url returns boolean false instead of the scheme string, causing the is_string branch to be skipped and the wrapper check to be bypassed.
- **Affected Products:** PHPOffice/PhpSpreadsheet
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or exploit identified.
- **Patch Available:** Patch is available via the advisory at https://github.com/advisories/GHSA-87m4-826x-3crx
- **Active Exploitation:** No confirmed reports of active exploitation found.
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor advisory/patch from the GHSA link or implement additional validation to detect schemes even when parse_url returns false (e.g., explicit pattern matching for known wrappers or normalize/strip extra slashes before parse_url).
- **Vendor Advisory:** https://github.com/advisories/GHSA-87m4-826x-3crx

---

## 3. 🟠 Zero-Day — Critical Check Point VPN Zero-Day Exploited in the Wild (CVE-2026-50751)

**CVE:** `CVE-2026-50751` | `CVE-2026-50752` | `CVE-2024-24919` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://www.rapid7.com/blog/post/etr-critical-check-point-vpn-zero-day-exploited-in-the-wild-cve-2026-50751>

> Overview On June 8, 2026, Check Point published a security advisory for CVE-2026-50751 , a critical authentication bypass vulnerability affecting Check Point Remote Access VPN, Mobile Access, and Spark Firewall products. The vulnerability affects deployments configured to use the deprecated IKEv1 key exchange protocol where gateways accept legacy Remote Access clients and do not require a machine …

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability affects deployments that use the deprecated IKEv1 key exchange protocol where gateways accept legacy Remote Access clients and do not require a machine certificate. It is an improper authentication flaw (CWE‑287) caused by a logic flow weakness in how Remote Access and Mobile Access handle legacy IKEv1 authentication.
- **Affected Products:** Check Point Remote Access VPN, Check Point Mobile Access, Check Point Spark Firewall
- **CVSS Score:** 9.3
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit is known.
- **Patch Available:** No official patch currently available.
- **Active Exploitation:** Active exploitation has been reported, with activity dating back to May 7, 2026.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — Gogs patches critical zero-day enabling remote code execution

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://www.bleepingcomputer.com/news/security/gogs-patches-critical-zero-day-enabling-remote-code-execution/>

> Gogs has patched a critical security zero-day flaw that can allow attackers to compromise Internet-facing instances and access any repositories (including private ones). [...]

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal/symlink handling flaw in Gogs repository file‑editing functionality allows attackers to overwrite files outside the repository (via symlink), leading to remote code execution.
- **Affected Products:** Gogs
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC available at https://github.com/zAbuQasem/gogs-CVE-2025-8110
- **Patch Available:** Gogs has released a patch; vendor patch URL: https://github.com/gogs/gogs/releases
- **Active Exploitation:** Confirmed active exploitation; over 700 Gogs instances compromised, and the vulnerability is listed in the CISA Known Exploited Vulnerabilities (KEV) catalog.
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor patch immediately; if the patch cannot be applied, take affected instances offline or restrict network exposure, disable web‑based editing features, and audit/restore overwritten files.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — Check Point links VPN zero-day attacks to Qilin ransomware gang

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://www.bleepingcomputer.com/news/security/check-point-links-vpn-zero-day-attacks-to-qilin-ransomware-gang/>

> Israeli cybersecurity company Check Point has released security updates to patch a critical flaw affecting Remote Access VPN and Mobile Access deployments, which was exploited in zero-day attacks. [...]

**Parallel AI Enrichment:**

- **Technical Details:** A logic flow weakness in Remote Access and Mobile Access certificate validation during deprecated IKEv1 key exchange allows an unauthenticated remote attacker to bypass user authentication and establish a VPN connection without valid credentials.
- **Affected Products:** Check Point Remote Access VPN, Mobile Access (SSL VPN), Spark Firewall; versions R80.20.X, R80.40, R81, R81.10, R81.10.X, R81.20, R82, R82.00.X, R82.10 (when using deprecated IKEv1).
- **CVSS Score:** 9.3
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC disclosed.
- **Patch Available:** Patch is available – hotfixes are provided via the vendor support advisory.
- **Active Exploitation:** Yes – active exploitation has been confirmed, with activity reported from May 7, 2026 and increased in early June; at least one incident linked to a Qilin ransomware affiliate.
- **Threat Actors:** Qilin ransomware gang (at least one confirmed incident); otherwise financially motivated ransomware affiliates.
- **Mitigation:** Apply the Check Point hotfixes immediately. If patching cannot be performed, disable legacy remote access client support, configure Remote Access VPN to use IKEv2 only, require machine‑certificate authentication, enable IPS with latest signatures, and review logs for suspicious activity.
- **Vendor Advisory:** https://support.checkpoint.com/results/sk/sk185033

---

## 6. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection via content poisoning: an attacker creates a crafted Google Doc/Calendar/Gmail, shares it with a target, and Gemini Enterprise’s retrieval system pulls the malicious content into its context, causing the model to execute attacker‑controlled commands.
- **Affected Products:** Google Gemini Enterprise
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC available at https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/
- **Patch Available:** Patch not yet released; mitigation provided by Google security team.
- **Active Exploitation:** Confirmed active exploitation; increase of malicious IPI attempts reported and a disclosed zero‑click exploit (GeminiJack).
- **Threat Actors:** None known
- **Mitigation:** Apply Google’s mitigation fixing instruction/content confusion in the RAG pipeline; restrict sharing of Google Docs/Calendar/Gmail with untrusted parties; employ content sanitization and monitor for abnormal prompt injection activity.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 7. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) injects malicious instructions into data sources or tools the LLM uses while fulfilling a user query; an attacker can influence model behavior (including zero‑click cases) by poisoning external content or tool outputs that the agentic LLM ingests. CVE‑2025‑54131 can be triggered when chained with IPI and was fixed in version 1.3.
- **Affected Products:** Google Workspace with Gemini integrations / Gemini Enterprise (fixed in version 1.3)
- **CVSS Score:** -999.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept or weaponized exploit is known.
- **Patch Available:** Fixed in version 1.3; details referenced in NVD entry.
- **Active Exploitation:** No confirmed active exploitation in the wild; only research disclosure by Noma Labs.
- **Threat Actors:** None known
- **Mitigation:** Implement layered defenses: data provenance controls, instrumented tool access, input/output sanitization, continuous monitoring and hardening.
- **Vendor Advisory:** http://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections

---

## 8. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: malicious web content injects prompts into the agentic browser's AI, causing it to perform unintended actions; mitigated by layered defenses and a secondary AI agent.
- **Affected Products:** Chrome (agentic/Gemini-enabled builds; specific versions not listed)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC or weaponized exploit reported.
- **Patch Available:** No separate patch URL; mitigation is described in the vendor advisory.
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Enable Chrome's new layered defenses for agentic browsing, which include site‑origin restrictions and a secondary AI agent to detect and block indirect prompt injection.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 9. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC or exploit information unavailable.
- **Patch Available:** Patch information unavailable.
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 10. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when hidden or external instructions embedded in documents, web content, emails, or other data sources are ingested by an AI system and cause it to follow attacker‑supplied instructions (e.g., exfiltrate data or perform unauthorized actions). Google’s advisory explains IPIs target the prompt lifecycle and recommends layered controls at ingestion, parsing, execution, and output stages.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No single public, vendor‑issued PoC; independent researchers have published in‑the‑wild payloads and PoCs (see Forcepoint report).
- **Patch Available:** No vendor patch; Google published defensive guidance and layered‑mitigation recommendations at the advisory URL.
- **Active Exploitation:** Yes – multiple security vendors and researchers reported in‑the‑wild indirect prompt injection payloads and detections.
- **Threat Actors:** None known
- **Mitigation:** Use defense‑in‑depth: sanitize and classify external inputs before they reach LLMs, strip or neutralize embedded instructions, apply strict context separation, use model output filters and hallucination detection, enforce least‑privilege access for models, and monitor for anomalous behavior. See Google advisory for detailed controls.
- **Vendor Advisory:** http://blog.google/security/mitigating-prompt-injection-attacks

---

## 11. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

---

## 12. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 13. 🟠 Zero-Day — Dulwich has unbounded memory allocation in receive-pack from crafted thin packs

**CVE:** `CVE-2026-47734` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-xrvj-v92f-53gj>

> ## Impact

An uncontrolled-resource-consumption (memory exhaustion) denial-of-service vulnerability (CWE-400 / CWE-789).

A client with push access could push a tiny crafted thin pack (~174 bytes)  whose delta header declares a huge   dest_size. When dulwich ingested it via  add_thin_pack / apply_delta, it would  allocate hundreds of MB of memory based on that attacker-controlled size, with no rel…

---

## 14. 🟠 Zero-Day — ⚡ Weekly Recap: Instagram Account Hacks, Android Zero-Day, GitHub Worm and More

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://thehackernews.com/2026/06/weekly-recap-instagram-account-hacks.html>

> Monday again. The weekend was meant to be quiet. It wasn&#x27;t. Last week had poisoned packages, a broken AI helper, and a worm tearing through repos. The ugly part: basic tricks still worked.

A chatbot got fooled. A bot token got leaked inside the malware. The same old mistakes showed up again. And while everyone chased the loud stuff, quieter attackers sat in inboxes for months, reading mail a…

---

## 15. 🟠 Zero-Day — Everest Forms Vulnerability Exploited to Hack WordPress Sites

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://www.securityweek.com/everest-forms-vulnerability-exploited-to-hack-wordpress-sites/>

> The flaw allows attackers to execute arbitrary code remotely and has been exploited in the wild for two months. The post Everest Forms Vulnerability Exploited to Hack WordPress Sites appeared first on SecurityWeek .

---

## 16. 🟠 Zero-Day — SolarWinds Serv-U Vulnerability Exploited in the Wild

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://www.securityweek.com/solarwinds-patches-exploited-serv-u-vulnerability/>

> Unauthenticated attackers can exploit the flaw via specially crafted POST requests that crash the Serv-U service. The post SolarWinds Serv-U Vulnerability Exploited in the Wild appeared first on SecurityWeek .

---

## 17. 🟡 High Severity — Arc has an authenticated arbitrary local-file read via DuckDB I/O functions that bypasses RBAC table-level checks

**CVE:** `CVE-2026-47735` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-p2j4-c4g6-rpf5>

> ### Summary

Arc&#x27;s user-SQL validator (`internal/api/query.go:ValidateSQLRequest`) blocked only `read_parquet(` and `arc_partition_agg(` via regex denylist. The broader DuckDB I/O function family — `read_csv_auto`, `read_csv`, `read_json`, `read_json_auto`, `read_text`, `read_blob`, `glob`, `parquet_metadata`, `parquet_schema`, `read_xlsx`, etc. — was not blocked. RBAC table-reference extract…

---

## 18. 🟡 High Severity — nebula-mesh: GET /api/v1/audit-log discloses all entries to any operator

**CVE:** `CVE-2026-47726` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-qm33-p5p9-f8vg>

> `internal/api/audit.go:12` — `handleGetAuditLog` does no admin check. The route is bearer-auth gated only; any operator API key returns the full audit log via `store.ListAuditEntries` (up to limit=1000). This includes cross-tenant actor names, host/CA/operator IDs, action timestamps, and masked-IP entries from rate-limit refusals — enough surface for a tenant to enumerate the server&#x27;s activit…

---

## 19. 🟡 High Severity — nebula-mesh's web UI lacks CSRF tokens on /ui/* mutating endpoints

**CVE:** `CVE-2026-47725` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-273q-qgh5-wrj6>

> Every `/ui/*` POST / PUT / PATCH / DELETE route processes the request as soon as the session cookie validates. `SameSite=Lax` on the session cookie prevents most cross-site form submits but does not protect:

- top-level form-submit navigations from third-party pages (some browsers still send Lax cookies on top-level POSTs)
- same-registrable-domain attackers (sibling-subdomain XSS, subdomain take…

---

## 20. 🟡 High Severity — nebula-mesh: API endpoints lack ownership checks, enabling cross-operator privilege escalation

**CVE:** `CVE-2026-47724` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-598g-h2vc-h5vg>

> The `/api/v1/*` route surface trusts the bearer token alone for authorisation on most endpoints. The codebase itself admits this at `internal/api/hosts.go:384`: *&quot;API trusts the bearer token for authorisation; per-CA ownership is enforced only in the Web layer.&quot;*

The Web UI gates state-changing routes through `loadAccessibleCA` (`internal/web/cas.go`); CA-management endpoints in `intern…

---

## 21. 🟡 High Severity — nebula-mesh: Web UI and API responses lack security headers (CSP, X-Frame-Options, HSTS, etc.)

**CVE:** `CVE-2026-47723` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-w7w5-5gcp-38rw>

> None of the response paths in `internal/web/` or `internal/api/` set the standard browser-security headers. `grep` for `Content-Security-Policy`, `X-Frame-Options`, `Strict-Transport-Security`, `X-Content-Type-Options`, `Referrer-Policy` returns zero matches across the codebase.

## Impact
The admin UI signs CA certificates, mints API keys (returned inline once per page), displays TOTP QR codes, a…

---

## 22. 🟡 High Severity — nebula-mesh: Host advanced overrides allow YAML injection into agent config.yml

**CVE:** `CVE-2026-47722` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-7hp6-g3pq-3pc3>

> `internal/configgen/generator.go:86,108,119` interpolates the operator-supplied `ListenHost` and `TunDevice` fields raw into a `text/template` that produces the agent&#x27;s `config.yml`. `internal/web/advanced.go:20-35` accepts both with only `strings.TrimSpace` — no character or shape validation.

## Exploit
An operator (or attacker with any operator key, given the cross-tenant CRUD advisory) se…

---

## 23. 🟡 High Severity — FUXA: Unauthenticated SSRF via Socket.IO DEVICE_WEBAPI_REQUEST and DEVICE_PROPERTY with response reading

**CVE:** `CVE-2026-47719` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-w86f-rf9w-h3x6>

> ## Summary

An unauthenticated attacker (Alice) connects to FUXA&#x27;s Socket.IO endpoint and emits a `device-webapi-request` event whose `property.address` field names an arbitrary URL. FUXA&#x27;s `DEVICE_WEBAPI_REQUEST` handler at `server/runtime/index.js:296` calls `axios.get(address)` server-side and broadcasts the full response body back on the same event via `io.emit`. The companion handle…

---

## 24. 🟡 High Severity — Netty: Unix-socket fd receive leaks descriptors when peer sends two at once

**CVE:** `CVE-2026-45536` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-w573-9ffj-6ff9>

> netty_unix_socket_recvFd sets msg_control to `char control[CMSG_SPACE(sizeof(int))]` (line 940) — 24 bytes on 64-bit Linux. A peer-sent SCM_RIGHTS cmsg carrying two ints has cmsg_len = CMSG_LEN(8) = 24, which fits exactly with no MSG_CTRUNC, so the kernel installs both fds in the receiving process. The subsequent check `cmsg-&gt;cmsg_len == CMSG_LEN(sizeof(int))` (line 972, expected 20) fails, the…

---

## 25. 🟡 High Severity — Netty: HAProxy SSL TLV parsing leaks retained slice on invalid TLV length

**CVE:** `CVE-2026-44893` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-cc37-9q2j-3hfv>

> When decoding a PP2_TYPE_SSL TLV, HAProxyMessage.readNextTLV() first calls `header.retainedSlice(header.readerIndex(), length)` and only then reads the 1-byte client field and 4-byte verify field. If the attacker sets the TLV length below 5, the subsequent readByte/readInt throws IndexOutOfBoundsException. HAProxyMessageDecoder only catches HAProxyProtocolException around this call, so the IOOBE p…

---

## 26. 🟡 High Severity — Netty has Unbounded Direct Memory Consumption in its RedisDecoder

**CVE:** `CVE-2026-44890` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-6ghj-frrj-jjj3>

> ### Summary
An attacker can cause DoS by sending crafted Redis payloads across multiple connections without `\r\n`. This exhausts the server&#x27;s direct memory pool (OutOfDirectMemoryError), preventing legitimate connections from being processed.

### Details
io.netty.handler.codec.redis.RedisDecoder decodes the length of bulk strings and array headers using the `decodeLength` method. This metho…

---

## 27. 🟡 High Severity — Critical Check Point VPN Flaw Exploited to Bypass Passwords in IKEv1 Setups

**CVE:** `CVE-2026-50751` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://thehackernews.com/2026/06/critical-check-point-vpn-flaw-exploited.html>

> Check Point has warned of active exploitation of a critical vulnerability impacting Remote Access VPN and Mobile Access deployments that are configured to use the deprecated IKEv1 key exchange protocol.

The vulnerability, tracked as CVE-2026-50751 (CVSS score: 9.3), is a case of a logic flow weakness in certificate validation that allows an unauthenticated remote attacker to bypass user

---

## 28. 🟡 High Severity — GeoNode contains a server-side request forgery vulnerability in the service registration endpoint

**CVE:** `CVE-2026-39922` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-hw9r-6m78-w6h3>

> GeoNode versions 4.4.5 and 5.0.2 (and prior within their respective releases) contain a server-side request forgery vulnerability in the service registration endpoint that allows authenticated attackers to trigger outbound network requests to arbitrary URLs by submitting a crafted service URL during form validation. Attackers can probe internal network targets including loopback addresses, RFC1918…

---

## 29. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
