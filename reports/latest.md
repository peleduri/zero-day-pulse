# Zero Day Pulse

> **Generated:** 2026-11-19 14:49 UTC &nbsp;|&nbsp; **Total:** 20 &nbsp;|&nbsp; 🔴 KEV: 3 &nbsp;|&nbsp; 📈 High EPSS: 3 &nbsp;|&nbsp; 🟠 Zero-Day: 3 &nbsp;|&nbsp; 🟡 High: 14 &nbsp;|&nbsp; 🎯 My Stack: 14 &nbsp;|&nbsp; ✨ Enriched: 0

---

## 🏁 Beat KEV

**Last 30 days**  
- All: collecting data since 2026-11-18 — Counted 0 · Earlier 0 · Same day/late 0 · Missed 0
- Edge devices: collecting data since 2026-11-18 — Counted 0 · Earlier 0 · Same day/late 0 · Missed 0
- Excluded: 4 warm-up, 0 old CVEs

**Last 90 days**  
- All: collecting data since 2026-11-18 — Counted 0 · Earlier 0 · Same day/late 0 · Missed 0
- Edge devices: collecting data since 2026-11-18 — Counted 0 · Earlier 0 · Same day/late 0 · Missed 0
- Excluded: 4 warm-up, 0 old CVEs

_Zero-days reported before a CVE ID exists can't be matched and count as missed._

---

## ⚡ Changed since last run (2)

- 📈 CVE-2026-40217 EPSS 17% → 62% (crossed 50%)
- 📈 CVE-2026-90817 EPSS 4% → 25% (crossed 10%)

---

## 🎯 My Stack Highlights

- 🟠 Zero-Day — NGINX2Root (CVE-2026-123007): Frequently asked questions about five critical NGINX vulnerabilities — `CVE-2026-123007`, `CVE-2026-123633`, `CVE-2026-123634`, `CVE-2026-121810`, `CVE-2026-113425`, `CVE-2026-118899`, `CVE-2026-120993`, `CVE-2026-125283`, `CVE-2026-123640`, `CVE-2026-120967` — EPSS 7% — `linux`, `nginx`, `github`
- 🟡 High Severity — Unauthenticated Remote Code Execution in NGINX: CVE-2026-123633 and CVE-2026-123007 — `CVE-2026-123633`, `CVE-2026-123007` — EPSS 7% — `nginx`
- 🟡 High Severity — PGPainless: Unbounded Compressed Packet Descent in inline-detach and MessageInspector leads to Denial of Service (DoS) — `CVE-2026-76088` — EPSS 1% — `github`
- 🟡 High Severity — OliveTin: Second-Order OS Command Injection via shellAfterCompleted — `CVE-2026-75506` — EPSS 1% — `github`
- 🟠 Zero-Day — mssql-mcp-core: SQL injection in mssql-mcp write tools via unparameterized table names and WHERE clauses — `CVE-2026-63129` — EPSS 1% — `github`
- 🟡 High Severity — LLMKube: Arbitrary Host File Read via Model.spec.source hostPath Injection — `CVE-2026-68903` — EPSS 0% — `kubernetes`, `github`
- 🟡 High Severity — Atomic Server: Unauthenticated `/setup` invite grants write access to the entire Drive — `CVE-2026-69157` — EPSS <1% — `docker`, `github`
- 🟡 High Severity — Atomic Server: Arbitrary file read via user-controlled `internalId` in the `/download` handler (leaks root agent private key) — `CVE-2026-69156` — EPSS <1% — `github`
- 🟡 High Severity — Atomic Server: Unauthenticated full-response SSRF in Atomic-Server /bookmark endpoint — `CVE-2026-69158` — EPSS <1% — `github`
- 🟡 High Severity — Miren Runtime: Authentication bypass in RPC layer: unverified TLS client certificates grant cluster superuser access — `CVE-2026-75521` — EPSS <1% — `github`
- 🟡 High Severity — ALTCHA PHP: verifySolution bypasses HMAC signature check when challenge signature is absent — `CVE-2026-71481` — EPSS <1% — `github`
- 🟡 High Severity — Chainguard SDK: AWS SigV4 token replay in auth/aws.VerifyToken — Chainguard-Audience/Chainguard-Identity binding headers not required in SignedHeaders — `CVE-2026-71861` — EPSS <1% — `aws`, `kubernetes`, `github`
- 🟡 High Severity — augment-virShell allows Command Injection in `grep()` via Unsanitized `searchPattern` — `CVE-2026-63496` — EPSS <1% — `node.js`, `github`
- 🟡 High Severity — Mustache for Ruby: RCE using built-in method access — `CVE-2026-130001` — EPSS n/a — `github`

---

## 1. 🔴 CISA KEV — Everything Is a Web Application, Including Your Firewall

**CVE:** `CVE-2026-109618` | `CVE-2026-109619` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 100.0% (percentile 100%)
**KEV:** in catalog, due 2026-10-29
**Reference:** <https://thehackernews.com/2026/11/everything-is-web-application-including.html>

> One of the early targets of PHP2Shell exploitation was the firewall. On October 28, Palo Alto Networks confirmed that attackers were exploiting the two PHP vulnerabilities, CVE-2026-109618 and CVE-2026-109619, against PAN-OS management interfaces exposed to the internet. Both flaws let anyone execute code on the web server without authentication. The disclosure itself went a little wrong.

---

## 2. 🔴 CISA KEV — 30 Years of Gatekeeper Asymmetry Doom: The Paradox that Makes Powerful LLMs More Vulnerable

**CVE:** `CVE-2021-44228` &nbsp;|&nbsp; **Source:** Check Point Research &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 100.0% (percentile 100%)
**KEV:** in catalog, due 2021-12-24 · ☠️ known ransomware use
**Reference:** <https://research.checkpoint.com/2026/30-years-of-gatekeeper-asymmetry-doom-the-paradox-that-makes-powerful-llms-more-vulnerable/>

> Abstract We give an exposition for a principle of gatekeeper asymmetry doom in information security, which states that “If the system vetting adversarial input has strictly less power than the system processing that input, without leveraging some hard problem, this will inevitably lead to doom.” We list a variety of examples where one can see […] The post 30 Years of Gatekeeper Asymmetry Doom: The…

---

## 3. 🔴 CISA KEV — Treat Your Honeypot Analysis Like Code: Git, Pull Requests and a Human Gate for AI [Guest Diary], (Wed, Nov 18th)

**CVE:** `CVE-2026-109618` &nbsp;|&nbsp; **Source:** SANS Internet Storm Center &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 100.0% (percentile 100%)
**KEV:** in catalog, due 2026-10-29
**Reference:** <https://isc.sans.edu/diary/rss/33534>

> [This is a Guest Diary by Kevin Truong, an ISC intern as part of the SANS.edu BACS program]

---

## 4. 🟠 Zero-Day — NGINX2Root (CVE-2026-123007): Frequently asked questions about five critical NGINX vulnerabilities

**CVE:** `CVE-2026-123007` | `CVE-2026-123633` | `CVE-2026-123634` | `CVE-2026-121810` | `CVE-2026-113425` | `CVE-2026-118899` | `CVE-2026-120993` | `CVE-2026-125283` | `CVE-2026-123640` | `CVE-2026-120967` &nbsp;|&nbsp; **Source:** Tenable Security Research &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 6.5% (percentile 94%)
**My Stack:** `linux`, `nginx`, `github`
**Reference:** <https://www.tenable.com/blog/nginx2root-cve-2026-123007-frequently-asked-questions-about-five-critical-nginx>

> Frequently asked questions about five critical NGINX remote code execution vulnerabilities and five additional flaws fixed in F5’s November 18 out-of-band release. Key takeaways NGINX2Root is associated with five critical remote code execution vulnerabilities in NGINX, and a separate, unpatched Linux kernel local privilege escalation (LPE) flaw that can be chained with the NGINX bugs to gain root.…

---

## 5. 🟠 Zero-Day — Critical Apache Roller RCE Flaw Under Active Exploitation, No Authentication Required

**CVE:** `CVE-2026-129448` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-11-18
**EPSS:** 1.2% (percentile 69%)
**Reference:** <https://thehackernews.com/2026/11/critical-apache-roller-rce-flaw-under.html>

> A critical security flaw in Apache Roller, an open-source, Java-based blogging platform, has come under active exploitation in the wild, according to the Apache Software Foundation (ASF)

The vulnerability, tracked as CVE-2026-129448 (CVSS score: 9.8), is a case of unauthenticated deserialization in the XML-RPC endpoint that could lead to remote code execution.

&quot;Deserialization of Untrusted

---

## 6. 🟠 Zero-Day — mssql-mcp-core: SQL injection in mssql-mcp write tools via unparameterized table names and WHERE clauses

**CVE:** `CVE-2026-63129` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 0.6% (percentile 47%)
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-2m9m-6cr5-9x25>

> Several tools in `mssql-mcp-core` built T-SQL by string-interpolating caller-supplied identifiers and predicates directly into the statement passed to the node-mssql `Request.query()` batch API. Only data values were parameterized.

Affected tools and inputs:
- `update_data`, `delete_data`: `tableName` and the free-form `whereClause` were interpolated raw.
- `insert_data`: `tableName` and column n…

---

## 7. 🟡 High Severity — PHP Readies Critical Security Updates to Patch Another RCE Flaw

**CVE:** `CVE-2026-115560` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-11-19
**Reference:** <https://www.securityweek.com/php-readies-critical-security-updates-to-patch-another-rce-flaw/>

> Affecting the session upload progress, CVE-2026-115560 was publicly disclosed two days after PHP2Shell patches landed. The post PHP Readies Critical Security Updates to Patch Another RCE Flaw appeared first on SecurityWeek .

---

## 8. 🟡 High Severity — PGPainless: Unbounded Compressed Packet Descent in inline-detach and MessageInspector leads to Denial of Service (DoS)

**CVE:** `CVE-2026-76088` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 0.7% (percentile 55%)
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-cvx8-9ff6-54xq>

> ### Summary
An architectural security boundary bypass in inline-detach and MessageInspector allows remote, unauthenticated attackers to force unbounded recursive decompression routines. By supplying a specially crafted OpenPGP message containing deeply nested compressed packet structures, an attacker can completely bypass the library&#x27;s built-in DoS protections (MAX_LAYER_DEPTH = 16), leading …

---

## 9. 🟡 High Severity — Miren Runtime: Authentication bypass in RPC layer: unverified TLS client certificates grant cluster superuser access

**CVE:** `CVE-2026-75521` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 0.3% (percentile 21%)
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-8fh7-7q4q-cq52>

> ### Summary

  The Miren Runtime RPC server (QUIC/HTTP3, default port `:8443`) requested TLS
  client certificates but never verified that a presented certificate chained to
  the cluster Certificate Authority. Because a client-certificate identity is
  granted a blanket RBAC bypass, any party able to reach the RPC listener could
  present a forged, self-signed certificate and be authenticated as …

---

## 10. 🟡 High Severity — OliveTin: Second-Order OS Command Injection via shellAfterCompleted

**CVE:** `CVE-2026-75506` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-18
**EPSS:** 0.6% (percentile 50%)
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-vc6p-m6vx-6cwq>

> ## Summary

OliveTin&#x27;s `shellAfterCompleted` post-execution hook injects unsanitized variables — including arbitrary command output (`output`), the authenticated username (`ot_username`), and the exit code (`exitCode`) — directly into a shell command template processed by `sh -c`. Unlike the main action&#x27;s argument handling, **no `checkShellArgumentSafety` validation is applied** to these…

---

## 11. 🟡 High Severity — LLMKube: Arbitrary Host File Read via Model.spec.source hostPath Injection

**CVE:** `CVE-2026-68903` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-18
**EPSS:** 0.5% (percentile 44%)
**My Stack:** `kubernetes`, `github`
**Reference:** <https://github.com/advisories/GHSA-jw3m-8q7m-f35r>

> ### Summary

LLMKube&#x27;s `ModelReconciler` accepts arbitrary absolute paths and `file://` URIs in the `Model.spec.source` field and propagates them to two distinct sinks without path allowlisting: (1) `os.Open()` inside the controller pod itself (`copyLocalModel`), and (2) a Kubernetes `HostPathVolumeSource` that mounts the attacker-supplied path into the inference pod&#x27;s init container. An…

---

## 12. 🟡 High Severity — Chainguard SDK: AWS SigV4 token replay in auth/aws.VerifyToken — Chainguard-Audience/Chainguard-Identity binding headers not required in SignedHeaders

**CVE:** `CVE-2026-71861` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-18
**EPSS:** 0.2% (percentile 12%)
**My Stack:** `aws`, `kubernetes`, `github`
**Reference:** <https://github.com/advisories/GHSA-wq26-3j2m-4hvv>

> ### Summary

The `auth/aws` package of the `chainguard.dev/sdk` Go library provides Chainguard&#x27;s AWS-backed identity federation (an AWS workload proves its identity to Chainguard by signing an AWS STS `GetCallerIdentity` request). Its verifier, `VerifyToken`, reads the `Chainguard-Audience` and `Chainguard-Identity` binding headers from a presented token but does not require them to be covere…

---

## 13. 🟡 High Severity — Vulnerability in Oracle OpenJDK (Java4Shell) Affecting Cisco Products: November 2026

**CVE:** `CVE-2026-114938` &nbsp;|&nbsp; **Source:** Cisco Security Advisories (PSIRT) &nbsp;|&nbsp; **Published:** 2026-11-18
**EPSS:** 0.8% (percentile 56%)
**Reference:** <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-nov2026-java-rce-eCa6ss9z?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Vulnerability%20in%20Oracle%20OpenJDK%20(Java4Shell)%20Affecting%20Cisco%20Products:%20November%202026%26vs_k=1>

> On November 17, 2026, Oracle announced the availability of fixes for a vulnerability in OpenJDK that could lead to remote code execution identified by CVE-2026-114938. The vulnerability affects OpenJDK Java 17.0.6 and later on x86-64 platforms when processing Base64 encoded content. For more information, see the Oracle Critical Security Patch Update Advisory - November 2026 and the OpenJDK Vulnera…

---

## 14. 🟡 High Severity — ALTCHA PHP: verifySolution bypasses HMAC signature check when challenge signature is absent

**CVE:** `CVE-2026-71481` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-18
**EPSS:** 0.3% (percentile 18%)
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-82w8-65qw-gch6>

> In altcha-org/altcha v2, the verifySolution method skips HMAC signature verification when the signature field is absent from the challenge payload, even when hmacSignatureSecret is configured.

An attacker who strips the signature key from the challenge JSON passes the condition as false, bypassing tamper-detection entirely. The PoW solution check then runs against unverified parameters — allowing…

---

## 15. 🟡 High Severity — Atomic Server: Unauthenticated full-response SSRF in Atomic-Server /bookmark endpoint

**CVE:** `CVE-2026-69158` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-18
**EPSS:** 0.3% (percentile 22%)
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-ff87-73jp-f3v4>

> ## Summary

Atomic-Server exposes a `GET /bookmark` endpoint that fetches an attacker-supplied URL server-side, parses the response, and reflects the fetched content back to the caller. The endpoint requires no authentication and performs no authorization of its own, and the underlying fetch helper applies no allow-list or private-IP deny-list. An unauthenticated attacker with network reach to the…

---

## 16. 🟡 High Severity — Atomic Server: Unauthenticated `/setup` invite grants write access to the entire Drive

**CVE:** `CVE-2026-69157` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-18
**EPSS:** 0.4% (percentile 33%)
**My Stack:** `docker`, `github`
**Reference:** <https://github.com/advisories/GHSA-pfwx-xjp4-qxcj>

> ## Summary

atomic-server provisions a well-known invite at `{server}/setup` with `write = true`, `target` = the Drive root, and `usagesLeft = 1`. Invite redemption **ignores the redeemer&#x27;s identity** (`for_agent: _` in `server/src/plugins/invite.rs:22`), so possession of the URL is the only requirement. An **unauthenticated** attacker who sends `GET /setup?public-key=&lt;attacker_key&gt;` ha…

---

## 17. 🟡 High Severity — Atomic Server: Arbitrary file read via user-controlled `internalId` in the `/download` handler (leaks root agent private key)

**CVE:** `CVE-2026-69156` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-18
**EPSS:** 0.3% (percentile 29%)
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-8vc4-8hjq-988p>

> ## Summary

The Commit apply path enforces **no allowlist of writable properties**, so any authenticated Agent can set the `internalId` string (datatype `string`, no character validation) on a resource it owns. The `/download` handler then uses that value **verbatim** as a filesystem path — `file_path.push(internal_id); NamedFile::open(file_path)` — with **no sanitization and no containment check*…

---

## 18. 🟡 High Severity — Mustache for Ruby: RCE using built-in method access

**CVE:** `CVE-2026-130001` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-18
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-5hrj-7fc3-cmx9>

> &gt; [!NOTE]
&gt; The vulnerability was fully disclosed to the maintainer in private prior to security advisories were enabled for the project.
&gt; This advisory presents a limited information for initial release to provide a time window for installing updates. Full information with PoCs would be added later.

## Summary
Mustache template engine for Ruby in versions 1.1.2 and earlier allows remot…

---

## 19. 🟡 High Severity — augment-virShell allows Command Injection in `grep()` via Unsanitized `searchPattern`

**CVE:** `CVE-2026-63496` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-18
**EPSS:** 0.2% (percentile 8%)
**My Stack:** `node.js`, `github`
**Reference:** <https://github.com/advisories/GHSA-xvcc-vqjv-phqh>

> ## Shell Command Injection in `grep()` via Unsanitized `searchPattern`

### Summary

The `grep()` function exported by `@augment-vir/node` inserts caller-controlled search patterns directly into a double-quoted shell command string without sanitization (`grep.ts:310`). When the constructed command is passed to `spawn()` with `shell: &#x27;bash&#x27;` (`shell.ts:98-99`), bash evaluates `$()` comman…

---

## 20. 🟡 High Severity — Unauthenticated Remote Code Execution in NGINX: CVE-2026-123633 and CVE-2026-123007

**CVE:** `CVE-2026-123633` | `CVE-2026-123007` &nbsp;|&nbsp; **Source:** Wiz Research &nbsp;|&nbsp; **Published:** 2026-11-18
**EPSS:** 6.5% (percentile 94%)
**My Stack:** `nginx`
**Reference:** <https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities>

> Two critical HTTP/2 flaws can allow attackers to compromise NGINX servers, putting the websites, APIs, and sensitive data they handle at risk.

---
