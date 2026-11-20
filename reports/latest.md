# Zero Day Pulse

> **Generated:** 2026-11-20 05:32 UTC &nbsp;|&nbsp; **Total:** 57 &nbsp;|&nbsp; 🔴 KEV: 2 &nbsp;|&nbsp; 📈 High EPSS: 2 &nbsp;|&nbsp; 🟠 Zero-Day: 8 &nbsp;|&nbsp; 🟡 High: 47 &nbsp;|&nbsp; 🎯 My Stack: 46 &nbsp;|&nbsp; ✨ Enriched: 0

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

## ⚡ Changed since last run (19)

- 🎯 New My Stack hit: CVE-2026-103033 [github] — ALTCHA: Nil-map panic (pre-verification DoS) in v1 parseServerSignature on malformed VerificationData <https://github.com/advisories/GHSA-gfwj-45pc-w6r5>
- 🎯 New My Stack hit: CVE-2026-114516 [linux, github, windows] — Etherpad: Pre-auth arbitrary file read <https://github.com/advisories/GHSA-mc8w-wjhw-45x5>
- 🎯 New My Stack hit: CVE-2026-58210 [github] — NATS Server allows unauthenticated memory exhaustion through incomplete MQTT CONNECT packets <https://github.com/advisories/GHSA-r72h-j7qq-v6qg>
- 🎯 New My Stack hit: CVE-2026-59988 [github] — django-docutils unsafe Docutils defaults allow local file disclosure, SSRF, and stored XSS <https://github.com/advisories/GHSA-86mf-q4h5-69gp>
- 🎯 New My Stack hit: CVE-2026-62337 [github] — snark-verifier: Halo 2 aggregation circuit mishandles point-at-infinity proof elements <https://github.com/advisories/GHSA-x26x-7f4v-cqx7>
- 🎯 New My Stack hit: CVE-2026-62955 [github] — baserCMS: Path Traversal Bypass via realpath() in BcThemeFileService (CVE-2026-30940 Patch Bypass) <https://github.com/advisories/GHSA-2pj4-v76f-wjvx>
- 🎯 New My Stack hit: CVE-2026-63344 [github] — Refitter allows arbitrary code execution through unescaped OpenAPI content-type values <https://github.com/advisories/GHSA-p32v-8v8j-j534>
- 🎯 New My Stack hit: CVE-2026-63345 [github] — Refitter allows arbitrary code execution through unescaped OpenAPI paths <https://github.com/advisories/GHSA-3fhm-p725-h3g3>
- 🎯 New My Stack hit: CVE-2026-63346 [github] — Refitter allows code execution through unescaped OpenAPI header parameter names <https://github.com/advisories/GHSA-58x9-vjvp-6mx8>
- 🎯 New My Stack hit: CVE-2026-63415 [github] — Jane: $ref resolution performs SSRF + LFI (path traversal) at code-generation time (jane-php) <https://github.com/advisories/GHSA-c3cj-3p6p-j822>
- 🎯 New My Stack hit: CVE-2026-77312 [github] — Flyto2 Core: Arbitrary file write via unguarded data.*/file.* modules (incomplete fix of CVE-2026-67429) <https://github.com/advisories/GHSA-p34x-fmph-9fjx>
- 🎯 New My Stack hit: CVE-2026-77313 [github] — Flyto2 Core: SSRF guard validates the resolved IP but connects by hostname, allowing DNS-rebinding TOCTOU <https://github.com/advisories/GHSA-pfg2-w999-497v>
- 🎯 New My Stack hit: CVE-2026-77315 [github] — Flyto2 Core: http.paginate follows server-supplied next-page URLs (Link header / cursor) without SSRF revalidation <https://github.com/advisories/GHSA-2mr3-rxrq-238c>
- 🎯 New My Stack hit: CVE-2026-77316 [github] — Flyto2 Core: SSRF guard bypass via DNS rebinding (validate_url_ssrf resolves-then-connects without pinning) <https://github.com/advisories/GHSA-6pm8-6f34-9v3g>
- 🎯 New My Stack hit: CVE-2026-77318 [python, github] — Jupyter MCP Server: Unauthenticated management routes can hijack the Jupyter backend in standalone HTTP mode <https://github.com/advisories/GHSA-24pw-rf5p-mgp7>
- 🎯 New My Stack hit: CVE-2026-77359 [python, github] — Jupyter MCP Server: Browser DNS rebinding can hijack the Jupyter backend through management routes <https://github.com/advisories/GHSA-9x8x-crjq-g64h>
- 🎯 New My Stack hit: CVE-2026-77377 [github] — Bolt: Server-Side Request Forgery (SSRF) in URL-upload and embed endpoints <https://github.com/advisories/GHSA-2535-j2pq-qq4r>
- 🎯 New My Stack hit: CVE-2026-77380 [github] — Bolt: Prevent SSRF due to unchecked followed redirects <https://github.com/advisories/GHSA-3xjf-9q55-vxw4>
- 🎯 New My Stack hit: CVE-2026-77382 [github] — falcon-rust: Discrete-Gaussian sampler runs at 2^-33 precision, far below Falcon&#x27;s requirement (reference KAT vectors no longer pass) <https://github.com/advisories/GHSA-25rm-9wvm-m38v>

---

## 🎯 My Stack Highlights

- 🟡 High Severity — NATS Server allows unauthenticated memory exhaustion through incomplete MQTT CONNECT packets — `CVE-2026-58210` — EPSS 1% — `github`
- 🟠 Zero-Day — CodeWhale: exec_shell parallel-readonly classifier auto-approves fd/rg/git grep exec flags enabling silent RCE — `CVE-2026-83816` — EPSS 1% — `github`
- 🟡 High Severity — Mistune: Quadratic-time DoS in parse_link_href via unbounded parenthesis scan on empty-label links — `CVE-2026-97698` — EPSS 1% — `python`, `github`
- 🟠 Zero-Day — CodeWhale: Automation auto_approve defaults to true, bypassing the task-path hardening fix for silent recurring agent execution — `CVE-2026-83817` — EPSS 1% — `github`
- 🟡 High Severity — Mistune: Quadratic-time DoS in inline image parsing (precedence_scan) bypasses not-is-image guards — `CVE-2026-97699` — EPSS 1% — `python`, `github`
- 🟡 High Severity — October: Media Library Crop Handler Bypasses Upload Extension Allowlist — `CVE-2026-63193` — EPSS 1% — `nginx`, `github`
- 🟡 High Severity — NATS Server: MQTT SUBSCRIBE Protocol Injection via Leaf Node/Route Forwarding allows arbitrary NATS command injection — `CVE-2026-58213` — EPSS <1% — `github`
- 🟡 High Severity — containerd image-triggered daemon crash via malformed digest in subject-annotated descriptor — `CVE-2026-95839` — EPSS <1% — `kubernetes`, `github`
- 🟡 High Severity — Next.js: Cross-user cache disclosure and poisoning in Next.js use cache with binary arguments — `CVE-2026-119349` — EPSS <1% — `github`
- 🟡 High Severity — k8s-mcp-server: Missing authentication on default SSE/HTTP transport allows unauthenticated Kubernetes tool execution — `CVE-2026-130007` — EPSS <1% — `kubernetes`, `github`
- 🟡 High Severity — Refitter allows arbitrary code execution through unescaped OpenAPI content-type values — `CVE-2026-63344` — EPSS <1% — `github`
- 🟡 High Severity — Refitter allows code execution through unescaped OpenAPI header parameter names — `CVE-2026-63346` — EPSS <1% — `github`
- 🟡 High Severity — Refitter allows arbitrary code execution through unescaped OpenAPI paths — `CVE-2026-63345` — EPSS <1% — `github`
- 🟡 High Severity — Jane: $ref resolution performs SSRF + LFI (path traversal) at code-generation time (jane-php) — `CVE-2026-63415` — EPSS <1% — `github`
- 🟡 High Severity — Model Context Protocol Python SDK: OAuth client could send credentials to an authorization server chosen by the MCP server — `CVE-2026-115563` — EPSS <1% — `python`, `github`
- 🟡 High Severity — snark-verifier: Halo 2 aggregation circuit mishandles point-at-infinity proof elements — `CVE-2026-62337` — EPSS <1% — `github`
- 🟡 High Severity — Effect: ReDoS in Schema.TemplateLiteral compiled regex — `CVE-2026-121707` — EPSS <1% — `github`
- 🟡 High Severity — gosaml2: Unauthenticated panic decrypting an EncryptedAssertion with a short or empty CipherValue — `CVE-2026-128073` — EPSS <1% — `github`
- 🟡 High Severity — Next.js: Cache poisoning of shared fallback shells in Cache Components via request-supplied placeholder route params — `CVE-2026-119350` — EPSS <1% — `github`
- 🟡 High Severity — Todoist MCP Server: Browser DNS rebinding lets websites write and delete Todoist data through local MCP server — `CVE-2026-76807` — EPSS <1% — `github`
- 🟡 High Severity — fzf: Predictable FIFO path in zsh completion allows local symlink attack / arbitrary file overwrite as the victim user (_fzf_feed_fifo) — `CVE-2026-121717` — EPSS <1% — `github`
- 🟡 High Severity — iSponsorBlockTV: SSRF via Malicious SSDP Response Spoofing in Local Device Discovery — `CVE-2026-77597` — EPSS <1% — `github`
- 🟡 High Severity — Gortex: Arbitrary file write / repo-confinement escape in `write_file` / `edit_file` / `move_inline` MCP tools → code execution — `CVE-2026-62964` — EPSS <1% — `github`
- 🟡 High Severity — DOMShell: domshell_eval classified as read-tier can execute side-effecting JavaScript without --allow-write — `CVE-2026-75518` — EPSS <1% — `github`
- 🟡 High Severity — Mareforma: Unsigned Claims Can Be Promoted to REPLICATED via Missing Signature Enforcement in Convergence Path — `CVE-2026-71535` — EPSS <1% — `python`, `github`
- 🟠 Zero-Day — baserCMS: Path Traversal Bypass via realpath() in BcThemeFileService (CVE-2026-30940 Patch Bypass) — `CVE-2026-62955` — EPSS n/a — `github`
- 🟡 High Severity — Etherpad: Pre-auth arbitrary file read — `CVE-2026-114516` — EPSS n/a — `linux`, `github`, `windows`
- 🟡 High Severity — ALTCHA: Nil-map panic (pre-verification DoS) in v1 parseServerSignature on malformed VerificationData — `CVE-2026-103033` — EPSS n/a — `github`
- 🟡 High Severity — falcon-rust: Discrete-Gaussian sampler runs at 2^-33 precision, far below Falcon&#x27;s requirement (reference KAT vectors no longer pass) — `CVE-2026-77382` — EPSS n/a — `github`
- 🟡 High Severity — Bolt: Prevent SSRF due to unchecked followed redirects — `CVE-2026-77380` — EPSS n/a — `github`
- 🟡 High Severity — Bolt: Server-Side Request Forgery (SSRF) in URL-upload and embed endpoints — `CVE-2026-77377` — EPSS n/a — `github`
- 🟡 High Severity — Jupyter MCP Server: Browser DNS rebinding can hijack the Jupyter backend through management routes — `CVE-2026-77359` — EPSS n/a — `python`, `github`
- 🟡 High Severity — Jupyter MCP Server: Unauthenticated management routes can hijack the Jupyter backend in standalone HTTP mode — `CVE-2026-77318` — EPSS n/a — `python`, `github`
- 🟡 High Severity — Flyto2 Core: SSRF guard bypass via DNS rebinding (validate_url_ssrf resolves-then-connects without pinning) — `CVE-2026-77316` — EPSS n/a — `github`
- 🟡 High Severity — Flyto2 Core: http.paginate follows server-supplied next-page URLs (Link header / cursor) without SSRF revalidation — `CVE-2026-77315` — EPSS n/a — `github`
- 🟡 High Severity — Flyto2 Core: SSRF guard validates the resolved IP but connects by hostname, allowing DNS-rebinding TOCTOU — `CVE-2026-77313` — EPSS n/a — `github`
- 🟡 High Severity — Flyto2 Core: Arbitrary file write via unguarded data.*/file.* modules (incomplete fix of CVE-2026-67429) — `CVE-2026-77312` — EPSS n/a — `github`
- 🟡 High Severity — django-docutils unsafe Docutils defaults allow local file disclosure, SSRF, and stored XSS — `CVE-2026-59988` — EPSS n/a — `github`
- 🟡 High Severity — NLTK: ARFF_Formatter Injects Weka ARFF Schema Directives via Attacker-Controlled Class Labels — `CVE-2026-129221` — EPSS n/a — `python`, `github`
- 🟡 High Severity — NLTK: Uncontrolled recursion in DependencyGraph traversal causes denial of service via deep dependency chains — `CVE-2026-129225` — EPSS n/a — `python`, `github`
- 🟡 High Severity — NLTK: Uncontrolled recursion in semantic-logic type parser causes denial of service via nested type strings — `CVE-2026-129226` — EPSS n/a — `python`, `github`
- 🟡 High Severity — NLTK: Uncontrolled recursion in Tree.fromlist causes denial of service via deeply nested list input — `CVE-2026-129227` — EPSS n/a — `python`, `github`
- 🟡 High Severity — NLTK: Uncontrolled recursion in Toolbox settings helpers causes denial of service via deeply nested input — `CVE-2026-129228` — EPSS n/a — `python`, `github`
- 🟡 High Severity — NLTK: Uncontrolled recursion in WordNet Synset hypernym walkers (max_depth/min_depth/hypernym_paths/hypernym_distances) causes DoS — `CVE-2026-129230` — EPSS n/a — `python`, `github`
- 🟡 High Severity — NLTK: StreamBackedCorpusView constructor os.stat leaks out-of-root file existence, size, and mtime bypassing pathsec ENFORCE — `CVE-2026-129233` — EPSS n/a — `github`
- 🟡 High Severity — NLTK: Untrusted search path in prover9/mace4 config allows local code execution via relative binary_location — `CVE-2026-129234` — EPSS n/a — `python`, `github`

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

## 3. 🟠 Zero-Day — VMware patches vCenter zero-day exploited in attacks since September

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-11-20
**Reference:** <https://www.bleepingcomputer.com/news/security/vmware-patches-vcenter-zero-day-exploited-in-attacks-since-september/>

> Broadcom has released security updates to fix a critical VMware vCenter Server authentication bypass vulnerability that Chinese-linked hackers have exploited in zero-day attacks since September 2026. [...]

---

## 4. 🟠 Zero-Day — baserCMS: Path Traversal Bypass via realpath() in BcThemeFileService (CVE-2026-30940 Patch Bypass)

**CVE:** `CVE-2026-62955` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-20
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-2pj4-v76f-wjvx>

> ### Summary

The security patch introduced in baserCMS 5.2.3 to address CVE-2026-30940 / [GHSA-c5c6-37vq-pjcq](https://github.com/baserproject/basercms/security/advisories/GHSA-c5c6-37vq-pjcq) is **incomplete**. The patch added a `realpath()`-based directory traversal check in `BcThemeFileService::getFullpath()`, but the check is **entirely skipped** when `realpath($baseDir)` returns `false` — whi…

---

## 5. 🟠 Zero-Day — Newly Patched VMware vCenter Flaw Exploited as Zero-Day by Chinese APT

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-11-19
**Reference:** <https://www.securityweek.com/newly-patched-vmware-vcenter-flaw-exploited-as-zero-day-by-chinese-apt/>

> Google says a China-linked espionage group exploited a critical VMware vCenter authentication bypass before Broadcom released a patch. The post Newly Patched VMware vCenter Flaw Exploited as Zero-Day by Chinese APT appeared first on SecurityWeek .

---

## 6. 🟠 Zero-Day — ThreatsDay: GPT-6.2 Jailbreak Flaws, BubbleLoader PNG Malware, $500M Ransom Demands + 17 More Stories

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-11-19
**Reference:** <https://thehackernews.com/2026/11/threatsday-gpt-62-jailbreak-flaws.html>

> The easiest way to fool someone is to give them something they already expect. A job offer. A message about a service outage. A familiar app. Nothing looks strange at first. And that&#x27;s the problem. This week&#x27;s stories show how ordinary things are being used to steal data, spread malware, and get people to hand over access.

There&#x27;s another shift worth watching. AI is making some att…

---

## 7. 🟠 Zero-Day — Critical VMware vCenter Zero-Day Flaw Lets Network Attackers Bypass Authentication

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-11-19
**Reference:** <https://thehackernews.com/2026/11/critical-vmware-vcenter-flaw-cvss-98.html>

> A critical flaw in VMware vCenter lets an attacker with network access bypass authentication and gain unauthorized access to the system, Broadcom, which owns VMware, said in an advisory published today.

Fixed versions are out for all supported branches, and the company lists no workaround. vCenter is the central console for managing an organization&#x27;s ESX hosts and virtual machines.

The

---

## 8. 🟠 Zero-Day — CodeWhale: exec_shell parallel-readonly classifier auto-approves fd/rg/git grep exec flags enabling silent RCE

**CVE:** `CVE-2026-83816` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 0.7% (percentile 55%)
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-3mgh-93r5-r7jf>

> ### Maintainer resolution

The CodeWhale maintainers validated this report. CodeWhale 0.8.67 and earlier are affected. Version 0.9.0 contains the fix in commit 208421b9d23d81cea3311a1eeb2a2ea81d637686. Users should upgrade to 0.9.0 or later. The original reporter analysis is preserved below.

## Summary
The interactive Agent profile of DeepSeek-TUI (CodeWhale) is explicitly documented to gate **ev…

---

## 9. 🟠 Zero-Day — CodeWhale: Automation auto_approve defaults to true, bypassing the task-path hardening fix for silent recurring agent execution

**CVE:** `CVE-2026-83817` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 0.7% (percentile 54%)
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-8hp3-xxrg-v9c8>

> ### Maintainer resolution

The CodeWhale maintainers validated this report. CodeWhale 0.8.67 and earlier are affected. Version 0.9.0 contains the fix in commit 208421b9d23d81cea3311a1eeb2a2ea81d637686. Users should upgrade to 0.9.0 or later. The original reporter analysis is preserved below.

## Summary
CVE-2026-45374 (GHSA-72w5-pf8h-xfp4) hardened the task path so auto-approval must be opted into…

---

## 10. 🟠 Zero-Day — European Commission confirms cyberattack, says hackers used AI tool

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Record by Recorded Future &nbsp;|&nbsp; **Published:** 2026-11-19
**Reference:** <https://therecord.media/european-commission-confirms-cyberattack-using-ai>

> POLITICO had reported CERT-EU had identified the attackers’ use of ARTEX, an open-source AI hacking platform that the FBI last week warned was being used both by criminals and state-sponsored groups.

---

## 11. 🟡 High Severity — Etherpad: Pre-auth arbitrary file read

**CVE:** `CVE-2026-114516` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-20
**My Stack:** `linux`, `github`, `windows`
**Reference:** <https://github.com/advisories/GHSA-mc8w-wjhw-45x5>

> ### Summary

An unauthenticated path‑traversal / arbitrary file read vulnerability in Etherpad&#x27;s /static/* handler allows any remote, unauthenticated user to read any file on the server&#x27;s filesystem (e.g. GET /static/plugins/ep_etherpad-lite/static/..%5C..%5C..%5C..%5C..%5C..%5C..%5Cetc/passwd returns /etc/passwd) available to the user running the etherpad software. Because the endpoint …

---

## 12. 🟡 High Severity — ALTCHA: Nil-map panic (pre-verification DoS) in v1 parseServerSignature on malformed VerificationData

**CVE:** `CVE-2026-103033` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-20
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-gfwj-45pc-w6r5>

> ### Summary

`parseServerSignature` in the v1 module only initializes `ServerSignatureVerificationData.Extra` inside the `if err == nil` branch after `url.ParseQuery(parsedPayload.VerificationData)`. Go&#x27;s `url.ParseQuery` returns the successfully-parsed pairs together with a non-nil error when the query string contains a malformed percent-escape. A subsequent loop unconditionally writes unkno…

---

## 13. 🟡 High Severity — falcon-rust: Discrete-Gaussian sampler runs at 2^-33 precision, far below Falcon&#x27;s requirement (reference KAT vectors no longer pass)

**CVE:** `CVE-2026-77382` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-20
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-25rm-9wvm-m38v>

> **Reporter:** Connor Webber
**Package:** `falcon-rust` (crates.io), repository `github.com/aszepieniec/falcon-rust`
**Affected:** v0.1.3 and the current `master` (HEAD `cfa1b35`). Regression introduced in commit `bf2cf00`.
**Component:** discrete-Gaussian sampler, `src/samplerz.rs` (`approx_exp`, `ber_exp`, `sampler_z`)
**Status:** Confirmed by source review and by empirical measurement of the cra…

---

## 14. 🟡 High Severity — Bolt: Prevent SSRF due to unchecked followed redirects

**CVE:** `CVE-2026-77380` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-20
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-3xjf-9q55-vxw4>

> ### Impact

The `/bolt/async/upload-url` and `/bolt/async/embed` endpoints validated only the **submitted** URL before fetching it server-side, but the fetch then **followed redirects to destinations that were never re-validated**. This allowed an authenticated user to bypass the SSRF guard (`UrlSafetyChecker`) and make the server issue requests to internal/cloud-metadata addresses.

### Patches

…

---

## 15. 🟡 High Severity — Bolt: Server-Side Request Forgery (SSRF) in URL-upload and embed endpoints

**CVE:** `CVE-2026-77377` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-20
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-2535-j2pq-qq4r>

> ### Impact

Two authenticated backend endpoints fetched a user-supplied URL server-side with no protection against internal targets.

### Patches

This has been patched in Bolt 6.1.4.

---

## 16. 🟡 High Severity — Jupyter MCP Server: Browser DNS rebinding can hijack the Jupyter backend through management routes

**CVE:** `CVE-2026-77359` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-20
**My Stack:** `python`, `github`
**Reference:** <https://github.com/advisories/GHSA-9x8x-crjq-g64h>

> Standalone `streamable-http` mode in `datalayer/jupyter-mcp-server` rejects forged `Host` and `Origin` headers on `/mcp`, but custom management routes mounted on the same application do not get the same browser-origin protection. A malicious website can keep an attacker origin while its hostname resolves to `127.0.0.1` or a private target address, then send `PUT /api/connect` to replace the MCP se…

---

## 17. 🟡 High Severity — Jupyter MCP Server: Unauthenticated management routes can hijack the Jupyter backend in standalone HTTP mode

**CVE:** `CVE-2026-77318` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-20
**My Stack:** `python`, `github`
**Reference:** <https://github.com/advisories/GHSA-24pw-rf5p-mgp7>

> Standalone `streamable-http` mode in `datalayer/jupyter-mcp-server` requires `MCP_TOKEN` for `/mcp`, but the custom management routes mounted on the same application do not enforce that token. An unauthenticated network caller can invoke `PUT /api/connect`, choose the Jupyter backend URL and token fields, reset the server context, and make the MCP server start a kernel client against attacker-cont…

---

## 18. 🟡 High Severity — Flyto2 Core: SSRF guard bypass via DNS rebinding (validate_url_ssrf resolves-then-connects without pinning)

**CVE:** `CVE-2026-77316` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-20
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-6pm8-6f34-9v3g>

> # [MEDIUM] SSRF guard bypass via DNS rebinding — validate_url_ssrf resolves-then-connects without pinning

- **CWE:** CWE-918 (SSRF) / CWE-367 (TOCTOU).
- **CVSS v3.1:** `AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:L/A:N` = **6.8 Medium** (AC:H — needs attacker-controlled DNS with a low/zero TTL and to flip the answer between the guard&#x27;s lookup and the connection&#x27;s lookup; S:C — reaches internal/metad…

---

## 19. 🟡 High Severity — Flyto2 Core: http.paginate follows server-supplied next-page URLs (Link header / cursor) without SSRF revalidation

**CVE:** `CVE-2026-77315` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-20
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-2mr3-rxrq-238c>

> ## Summary
`http.paginate` validates only the initial `base_url`, then follows server-supplied pagination targets (RFC 5988 `Link: rel=&quot;next&quot;` headers, cursor/offset URLs) in a loop **without revalidating each follow-up URL**. An attacker&#x27;s first-page response can point `next` at an internal address, causing a second-order SSRF whose internal body is aggregated into the returned ite…

---

## 20. 🟡 High Severity — Flyto2 Core: SSRF guard validates the resolved IP but connects by hostname, allowing DNS-rebinding TOCTOU

**CVE:** `CVE-2026-77313` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-20
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-pfg2-w999-497v>

> ## Summary
`validate_url_ssrf` resolves the hostname, checks the IP against private ranges, then **discards the IP and returns the hostname URL string**. aiohttp performs a fresh, independent DNS resolution at connect time. An attacker controlling DNS for a hostname (TTL 0, alternating public IP and internal IP) passes validation on the first lookup and connects to the internal IP on the second — …

---

## 21. 🟡 High Severity — Flyto2 Core: Arbitrary file write via unguarded data.*/file.* modules (incomplete fix of CVE-2026-67429)

**CVE:** `CVE-2026-77312` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-20
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-p34x-fmph-9fjx>

> # [CRITICAL] Arbitrary file write via unguarded `data.*` / `file.*` write modules — incomplete fix of GHSA-2956

- **CWE:** CWE-22 (Path Traversal) / CWE-73 (External Control of File Name or Path); impact reaches CWE-94 (code execution via file overwrite).
- **CVSS v3.1:** `AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H` = **9.3 Critical** (S:C because a write escapes the intended sandbox confinement into th…

---

## 22. 🟡 High Severity — django-docutils unsafe Docutils defaults allow local file disclosure, SSRF, and stored XSS

**CVE:** `CVE-2026-59988` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-20
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-86mf-q4h5-69gp>

> ## Summary

django-docutils before `0.30.0` rendered reStructuredText through Docutils without protected web-safe defaults. Public rendering paths, including `publish_doctree`, `publish_html_from_source`, `publish_html_from_doctree`, `publish_parts_from_doctree`, the `{% rst %}` template tag, the `rst` template filter, `DocutilsTemplates`, and `DocutilsView`, could process attacker-controlled RST …

---

## 23. 🟡 High Severity — Jane: $ref resolution performs SSRF + LFI (path traversal) at code-generation time (jane-php)

**CVE:** `CVE-2026-63415` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-20
**EPSS:** 0.3% (percentile 29%)
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-c3cj-3p6p-j822>

> ### Summary
jane-php resolves external `$ref` targets at code-generation time via `file_get_contents($ref)` (jane-php/json-schema-runtime/Reference.php::doResolve) with no scheme/path restriction. An attacker-controlled OpenAPI document can therefore cause: `$ref: &#x27;http://attacker/x&#x27;` -&gt; SSRF (HTTP GET at gen time; response inlined = RFI); `$ref: &#x27;/abs/file&#x27;` -&gt; LFI; `$re…

---

## 24. 🟡 High Severity — Refitter allows arbitrary code execution through unescaped OpenAPI content-type values

**CVE:** `CVE-2026-63344` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-20
**EPSS:** 0.4% (percentile 29%)
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-p32v-8v8j-j534>

> ### Summary

Refitter emits the spec&#x27;s content-type key (content map key in requestBody/responses) verbatim into a Refit `[Headers(&quot;Accept: &lt;ct&gt;&quot;, &quot;Content-Type: &lt;ct&gt;&quot;)]` attribute string without escaping
`&quot;`. A crafted value survives Refitter&#x27;s default OpenAPI validation, breaks out of the attribute and
the enclosing interface + namespace, injects a …

---

## 25. 🟡 High Severity — Refitter allows code execution through unescaped OpenAPI header parameter names

**CVE:** `CVE-2026-63346` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-20
**EPSS:** 0.4% (percentile 29%)
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-58x9-vjvp-6mx8>

> ### Summary

Refitter emits the spec&#x27;s header parameter name (parameters[].name with in: header) verbatim into a Refit `[Header(&quot;&lt;name&gt;&quot;)]` attribute string without escaping
`&quot;`. A crafted value survives Refitter&#x27;s default OpenAPI validation, breaks out of the attribute and
the enclosing interface + namespace, injects a top-level `file class` with a `[ModuleInitializ…

---

## 26. 🟡 High Severity — Refitter allows arbitrary code execution through unescaped OpenAPI paths

**CVE:** `CVE-2026-63345` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-20
**EPSS:** 0.4% (percentile 29%)
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-3fhm-p725-h3g3>

> ### Summary

Refitter emits each OpenAPI path (the paths-object key) verbatim into a Refit `[Get(&quot;&lt;path&gt;&quot;)]`
attribute string, without escaping `&quot;` or restricting characters. A crafted single-line, /-prefixed
path survives Refitter&#x27;s default OpenAPI validation yet closes the attribute string and the enclosing
interface + namespace, injects a top-level `file class` with a …

---

## 27. 🟡 High Severity — NATS Server allows unauthenticated memory exhaustion through incomplete MQTT CONNECT packets

**CVE:** `CVE-2026-58210` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-20
**EPSS:** 0.7% (percentile 55%)
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-r72h-j7qq-v6qg>

> ### Background

NATS.io is a high performance open source pub-sub distributed communication technology, built for the cloud, on-premise, IoT and edge computing.

The NATS Server supports MQTT clients, including authentication and parsing of MQTT `CONNECT` packets.

### Problem Description

An unauthenticated MQTT client could cause the server to retain large incomplete MQTT `CONNECT` packets befor…

---

## 28. 🟡 High Severity — snark-verifier: Halo 2 aggregation circuit mishandles point-at-infinity proof elements

**CVE:** `CVE-2026-62337` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-20
**EPSS:** 0.3% (percentile 23%)
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-x26x-7f4v-cqx7>

> ### Summary
The Halo 2 aggregation circuit could mishandle proof elements encoded as the point at infinity.

When an assigned proof point appeared in an MSM term with constant scalar one, the Halo 2 loader used a scalar-one shortcut that passed the assigned point directly into the EC sum helper. The EC sum implementation used by that path assumed its inputs were non-identity points, while assigned…

---

## 29. 🟡 High Severity — NLTK: ARFF_Formatter Injects Weka ARFF Schema Directives via Attacker-Controlled Class Labels

**CVE:** `CVE-2026-129221` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**My Stack:** `python`, `github`
**Reference:** <https://github.com/advisories/GHSA-9ffx-rrgx-mhgx>

> ## Description

### Summary

`nltk.classify.weka.ARFF_Formatter` writes class labels directly into the Weka ARFF `@ATTRIBUTE &#x27;-label-&#x27; {...}` declaration without any ARFF quoting or escaping. An attacker who can contribute class labels to a training dataset can include ARFF metacharacters such as `}`, newlines, `@ATTRIBUTE`, and `@DATA` to break out of the nominal label list and inject a…

---

## 30. 🟡 High Severity — NLTK: Uncontrolled recursion in DependencyGraph traversal causes denial of service via deep dependency chains

**CVE:** `CVE-2026-129225` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**My Stack:** `python`, `github`
**Reference:** <https://github.com/advisories/GHSA-xfcv-m889-fmqg>

> ## Root Cause
The dependency-graph traversal helpers recurse over dependency links without any depth
bound or visited set. `DependencyGraph._tree` (`nltk/parse/dependencygraph.py:404`)
recurses once per dependency link, `triples` (`nltk/parse/dependencygraph.py:432`) is a
recursive generator, and `get_cycle_path` (`nltk/parse/dependencygraph.py:520`) recurses
over dependencies. The neighbouring `c…

---

## 31. 🟡 High Severity — NLTK: Uncontrolled recursion in semantic-logic type parser causes denial of service via nested type strings

**CVE:** `CVE-2026-129226` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**My Stack:** `python`, `github`
**Reference:** <https://github.com/advisories/GHSA-w3pv-xfw4-ghr7>

> ## Root Cause
The semantic-logic type parser `read_type` (`nltk/sem/logic.py:866`) recurses on both
halves of every `&lt;a,b&gt;` complex type (`nltk/sem/logic.py:882-884`) with no depth or length
bound — only an `isinstance` assertion and a parenthesis-balance assertion. The
`LogicParser.MAX_PARSE_DEPTH` guard (`nltk/sem/logic.py:107,294`) protects the expression
parser but never runs on the `rea…

---

## 32. 🟡 High Severity — NLTK: Uncontrolled recursion in Tree.fromlist causes denial of service via deeply nested list input

**CVE:** `CVE-2026-129227` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**My Stack:** `python`, `github`
**Reference:** <https://github.com/advisories/GHSA-63wh-5r5m-wxr7>

> ## Root Cause
`Tree.fromlist` (`nltk/tree/tree.py:767`) converts a nested list into a `Tree` by recursing
once per nesting level (`nltk/tree/tree.py:780`) with no depth bound — its only validation
is `type(l) == list and len(l) &gt; 0`. The sibling constructor `Tree.fromstring` was hardened
with a `MAX_TREE_DEPTH` cap (`nltk/tree/tree.py:31,695`) that rejects adversarially deep
input with a bounde…

---

## 33. 🟡 High Severity — NLTK: Uncontrolled recursion in Toolbox settings helpers causes denial of service via deeply nested input

**CVE:** `CVE-2026-129228` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**My Stack:** `python`, `github`
**Reference:** <https://github.com/advisories/GHSA-f2h2-f4fc-p978>

> ## Root Cause
The Toolbox settings-tree helpers recurse over the parsed element tree without any depth
bound. `_to_settings_string` (`nltk/toolbox.py:418`), `remove_blanks`
(`nltk/toolbox.py:432`), `add_default_fields` (`nltk/toolbox.py:451`), `_sort_fields`
(`nltk/toolbox.py:484`), and `add_blank_lines` (`nltk/toolbox.py:502,516`) each recurse once
per element level with no depth counter or expli…

---

## 34. 🟡 High Severity — NLTK: Uncontrolled recursion in WordNet Synset hypernym walkers (max_depth/min_depth/hypernym_paths/hypernym_distances) causes DoS

**CVE:** `CVE-2026-129230` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**My Stack:** `python`, `github`
**Reference:** <https://github.com/advisories/GHSA-53pg-5qp8-mhvr>

> ## Summary

Four hypernym-walking methods on the WordNet `Synset` class in `nltk/corpus/reader/wordnet.py` (`max_depth`, `min_depth`, `hypernym_paths`, and `hypernym_distances`) traverse the hypernym pointer graph by direct recursion with no visited-node set and no depth cap. WordNet `data.&lt;pos&gt;` file content is untrusted corpus input in NLTK, the same trust boundary the project already trea…

---

## 35. 🟡 High Severity — NLTK: StreamBackedCorpusView constructor os.stat leaks out-of-root file existence, size, and mtime bypassing pathsec ENFORCE

**CVE:** `CVE-2026-129233` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-w674-vqhw-g3pg>

> ## Summary

`StreamBackedCorpusView`, a public API in `nltk/corpus/reader/util.py`, applies the pathsec sandbox to the file content it reads but not to the file metadata it probes in its constructor. When the view is created with a plain string fileid, `__init__` calls `os.stat(self._fileid).st_size` with no pathsec validation, so an application that passes an attacker influenced path to the const…

---

## 36. 🟡 High Severity — NLTK: Untrusted search path in prover9/mace4 config allows local code execution via relative binary_location

**CVE:** `CVE-2026-129234` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**My Stack:** `python`, `github`
**Reference:** <https://github.com/advisories/GHSA-cc5r-64rf-75hg>

> ## Summary
`Prover9Parent.config_prover9(binary_location=...)` (and `Mace`, which inherits it) accepts a relative `binary_location` and passes it as `path_to_bin` to `find_binary`, which disables the CWD-relative rejection guard. Unlike the boxer/senna/malt/repp siblings, prover9/mace apply no `os.path.isabs()` filter, so the resolved relative program path (e.g. `./prover9`) is executed from the c…

---

## 37. 🟡 High Severity — CVE-2026-114938 Portfolio Status: Impact of Java Vulnerability (CVE-2026-114938) on Palo Alto Networks Products (Severity: CRITICAL)

**CVE:** `CVE-2026-114938` &nbsp;|&nbsp; **Source:** Palo Alto Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 0.8% (percentile 56%)
**Reference:** <https://security.paloaltonetworks.com/CVE-2026-114938>

---

## 38. 🟡 High Severity — k8s-mcp-server: Missing authentication on default SSE/HTTP transport allows unauthenticated Kubernetes tool execution

**CVE:** `CVE-2026-130007` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 0.4% (percentile 32%)
**My Stack:** `kubernetes`, `github`
**Reference:** <https://github.com/advisories/GHSA-m932-63jc-4jqq>

> ## Summary
When k8s-mcp-server runs in its default SSE transport mode, the MCP `tools/call`
endpoint is dispatched with no authentication, session token, or Origin check.
Any client that can reach the listening port can enumerate and invoke the
server&#x27;s Kubernetes tools (including destructive/write tools) without credentials,
executing with the server&#x27;s configured cluster privileges.

##…

---

## 39. 🟡 High Severity — containerd image-triggered daemon crash via malformed digest in subject-annotated descriptor

**CVE:** `CVE-2026-95839` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 0.4% (percentile 35%)
**My Stack:** `kubernetes`, `github`
**Reference:** <https://github.com/advisories/GHSA-vwhp-8p66-mq4f>

> ### Impact

A bug in containerd&#x27;s image manifest processing causes an unrecovered panic when a child descriptor contains the `io.containerd.manifest.subject` annotation and a malformed digest. Pulling or importing such an image through the transfer service (including default CRI `PullImage` requests) crashes the containerd daemon. In Kubernetes environments, `kubelet` retries failed image pul…

---

## 40. 🟡 High Severity — Model Context Protocol Python SDK: OAuth client could send credentials to an authorization server chosen by the MCP server

**CVE:** `CVE-2026-115563` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 0.3% (percentile 26%)
**My Stack:** `python`, `github`
**Reference:** <https://github.com/advisories/GHSA-qx49-fqc8-xw99>

> ### Summary
In affected versions, the SDK&#x27;s OAuth client support (`mcp.client.auth`) let the MCP server a client connected to decide where the client&#x27;s OAuth credentials were sent:

- the authorization server metadata `issuer` was not validated on every discovery path, and
- stored or pre-provisioned client credentials were not bound to the authorization server they belong to.

A malicio…

---

## 41. 🟡 High Severity — Mistune: Quadratic-time DoS in parse_link_href via unbounded parenthesis scan on empty-label links

**CVE:** `CVE-2026-97698` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 0.7% (percentile 55%)
**My Stack:** `python`, `github`
**Reference:** <https://github.com/advisories/GHSA-phmp-hrw4-r36r>

> ## Resolution

**Fixed in Mistune 3.3.4.** Upgrade to 3.3.4 or later.

- Affected versions: `&lt; 3.3.4`
- First patched version: `3.3.4`
- Fix: https://github.com/lepture/mistune/compare/v3.3.3...v3.3.4

The reported payload was reproduced against the 3.3.3 release tag and verified to scale approximately linearly against the 3.3.4 release tag.

## Original report

The following report describes t…

---

## 42. 🟡 High Severity — Mistune: Quadratic-time DoS in inline image parsing (precedence_scan) bypasses not-is-image guards

**CVE:** `CVE-2026-97699` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 0.7% (percentile 53%)
**My Stack:** `python`, `github`
**Reference:** <https://github.com/advisories/GHSA-ww7q-mxrj-5ffg>

> ## Resolution

**Fixed in Mistune 3.3.4.** Upgrade to 3.3.4 or later.

- Affected versions: `&lt; 3.3.4`
- First patched version: `3.3.4`
- Fix: https://github.com/lepture/mistune/compare/v3.3.3...v3.3.4

The reported payload was reproduced against the 3.3.3 release tag and verified to scale approximately linearly against the 3.3.4 release tag.

## Original report

The following report describes t…

---

## 43. 🟡 High Severity — fzf: Predictable FIFO path in zsh completion allows local symlink attack / arbitrary file overwrite as the victim user (_fzf_feed_fifo)

**CVE:** `CVE-2026-121717` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 0.2% (percentile 7%)
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-7rj6-7pqx-v7rm>

> ### Summary

`shell/completion.zsh` feeds every trigger-driven zsh completion through a FIFO at a predictable, PID-based path in shared `/tmp` (`fzf-complete-fifo-$$`), without checking the failure of `rm -f`/`mkfifo`. On a multi-user host, another local user can pre-create that path as a symlink to a victim-writable file (e.g. `~/.bashrc`), causing the victim&#x27;s own completion to overwrite it…

---

## 44. 🟡 High Severity — Next.js: Cross-user cache disclosure and poisoning in Next.js use cache with binary arguments

**CVE:** `CVE-2026-119349` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 0.4% (percentile 34%)
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-rhh4-g77r-r9qj>

> Next.js App Router applications that pass binary arguments (such as Uint8Array or Blob values) to functions using the `use cache` directive can produce identical cache keys for distinct arguments, allowing cached results to be shared across users — cross-user disclosure of cached data or cache poisoning. This affects applications using `use cache` with binary arguments.

---

## 45. 🟡 High Severity — Next.js: Cache poisoning of shared fallback shells in Cache Components via request-supplied placeholder route params

**CVE:** `CVE-2026-119350` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 0.2% (percentile 13%)
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-vvgp-ww4w-46vf>

> Self-hosted Next.js applications served with `next start` and built with `cacheComponents: true` but without Partial Prefetching accept a request-supplied route param value as a prerender placeholder. One unauthenticated GET request can poison the fallback shell cache entry that a family of routes shares.

Such a route is served from a shell that keeps its never-prerenderable params as placeholder…

---

## 46. 🟡 High Severity — phpAfterShell and Critical PHP RCE Vulnerabilities: Everything You Need To Know

**CVE:** `CVE-2026-126714` &nbsp;|&nbsp; **Source:** Wiz Research &nbsp;|&nbsp; **Published:** 2026-11-19
**Reference:** <https://www.wiz.io/blog/phpaftershell-critical-php-rce-vulnerabilities-cve-2026-126714>

> Detect and mitigate phpAfterShell, and additional critical vulnerabilities from PHP&#x27;s November release that may enable remote code execution.

---

## 47. 🟡 High Severity — CVE-2026-123890: Critical Authentication Bypass in VMware vCenter

**CVE:** `CVE-2026-123890` | `CVE-2026-59309` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 22.9% (percentile 98%)
**Reference:** <https://www.rapid7.com/blog/post/etr-cve-2026-123890-critical-authentication-bypass-vmware-vcenter>

> Overview On November 19, 2026, Broadcom published VMware Security Advisory VMSA-2026-0009 , addressing five vulnerabilities in VMware products. The most severe of these, CVE-2026-123890 , is an authentication bypass using an alternate path or channel ( CWE-288 ) in the VMware Directory Service component of vCenter. Broadcom assigned the vulnerability a critical CVSSv3 score of 9.8 . A malicious ac…

---

## 48. 🟡 High Severity — Effect: ReDoS in Schema.TemplateLiteral compiled regex

**CVE:** `CVE-2026-121707` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 0.3% (percentile 23%)
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-7589-6fvf-x4pw>

> ### Impact

`Schema.TemplateLiteral` compiles each `Schema.String` span to the lazy wildcard `[\s\S]*?` and decodes input by running the resulting regular expression against it. When a template has two or more `Schema.String` spans, for example:

```ts
Schema.TemplateLiteral(Schema.String, &quot;:&quot;, Schema.String, &quot;:&quot;, Schema.String, &quot;X&quot;)
```

the regex contains several am…

---

## 49. 🟡 High Severity — iSponsorBlockTV: SSRF via Malicious SSDP Response Spoofing in Local Device Discovery

**CVE:** `CVE-2026-77597` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 0.2% (percentile 5%)
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-56v3-jrq2-4q9m>

> ### Summary
iSponsorBlockTV discovers local smart TV devices via SSDP (Simple Service Discovery Protocol). The `LOCATION` URL from SSDP responses is used to fetch device capabilities without URL validation. A local network attacker can craft a malicious SSDP response with a `LOCATION` pointing to any internal HTTP service, causing SSRF when the application fetches device information.

### Details
…

---

## 50. 🟡 High Severity — gosaml2: Unauthenticated panic decrypting an EncryptedAssertion with a short or empty CipherValue

**CVE:** `CVE-2026-128073` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 0.2% (percentile 14%)
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-5hj8-q7fv-qrj6>

> ### Summary

An attacker who can supply a crafted SAML Response for parsing can crash a `gosaml2` service provider by sending an `EncryptedAssertion` with AES-GCM encryption metadata and a `CipherValue` shorter than the GCM nonce size (12 bytes). The library panics with `slice bounds out of range` before any validation completes.

This is a **distinct issue from [GHSA-hwqm-qvj9-4jr2](https://githu…

---

## 51. 🟡 High Severity — October: Media Library Crop Handler Bypasses Upload Extension Allowlist

**CVE:** `CVE-2026-63193` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 0.6% (percentile 47%)
**My Stack:** `nginx`, `github`
**Reference:** <https://github.com/advisories/GHSA-mqwx-84vv-mp26>

> The Media Library upload handler validates the destination filename against an extension allowlist (`default_extensions`), rejecting types such as `php`, `phtml`, `html`, and `htm`. The image crop handler (`MediaManager::onCropImage` / `cropImage`) did not perform this check. The destination filename was taken from user input, the extension was extracted from it, and the staged bytes were written …

---

## 52. 🟡 High Severity — Todoist MCP Server: Browser DNS rebinding lets websites write and delete Todoist data through local MCP server

**CVE:** `CVE-2026-76807` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 0.2% (percentile 12%)
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-833v-v58w-294h>

> The self-hosted `todoist-mcp-http` server accepts browser-origin MCP requests with attacker-controlled `Host` and `Origin` headers. A malicious website can use DNS rebinding to route its own origin to a victim&#x27;s local `127.0.0.1` MCP server, then invoke Todoist MCP tools without a caller credential.

This affects `github.com/Doist/todoist-mcp` at commit `d2903e0d945d2a559d71c091337ad6380511e6…

---

## 53. 🟡 High Severity — Gortex: Arbitrary file write / repo-confinement escape in `write_file` / `edit_file` / `move_inline` MCP tools → code execution

**CVE:** `CVE-2026-62964` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 0.2% (percentile 5%)
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-w42c-h7hr-f67p>

> ### Summary
Gortex is an MCP server exposing `write_file`, `edit_file`, and `move_inline` tools. `resolveFilePath` **exempts absolute paths** from confinement, and the write handlers — unlike `read_file` / `get_symbol_source` — **never call `guardSymlinkWithinRepo`**. A single MCP `write_file` call with an absolute path writes any file the daemon user can, **outside every indexed repo root** (`Ato…

---

## 54. 🟡 High Severity — DOMShell: domshell_eval classified as read-tier can execute side-effecting JavaScript without --allow-write

**CVE:** `CVE-2026-75518` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 0.1% (percentile 1%)
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-vg83-hcp4-5qcc>

> ### Summary

The `domshell_eval` MCP tool (and the `eval` command inside `domshell_execute`) was classified as **read-tier**, allowing it to run without the `--allow-write` server flag. However, `eval` and the write-tier `js` command dispatch to the same handler in the extension and call CDP `Runtime.evaluate` with the raw expression string and no side-effect gate. Any JavaScript expression could …

---

## 55. 🟡 High Severity — Mareforma: Unsigned Claims Can Be Promoted to REPLICATED via Missing Signature Enforcement in Convergence Path

**CVE:** `CVE-2026-71535` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 0.1% (percentile 0%)
**My Stack:** `python`, `github`
**Reference:** <https://github.com/advisories/GHSA-8776-qf3h-26r3>

> ### Summary

`mareforma` 0.3.3 contains a critical integrity flaw in the REPLICATED convergence logic (`_maybe_update_replicated_unlocked()` in `mareforma/db/core.py:1300-1319`). The peer-selection SQL query that determines whether two independent claims &quot;agree&quot; on the same anchor does not verify that either claim carries a valid cryptographic signature from an enrolled validator key. Be…

---

## 56. 🟡 High Severity — NATS Server: MQTT SUBSCRIBE Protocol Injection via Leaf Node/Route Forwarding allows arbitrary NATS command injection

**CVE:** `CVE-2026-58213` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-19
**EPSS:** 0.4% (percentile 39%)
**My Stack:** `github`
**Reference:** <https://github.com/advisories/GHSA-qrcv-3558-gj4f>

> ### Background

NATS.io is a high performance open source pub-sub distributed communication technology, built for the cloud, on-premise, IoT and edge computing.

The NATS Server supports MQTT clients and can bridge MQTT activity into NATS subjects across routes and leafnode connections.

### Problem Description

An MQTT client could include protocol control characters in subscription filters that …

---

## 57. 🟡 High Severity — PHP Fixes 7 Critical Flaws, Including Bugs That Could Allow Remote Code Execution

**CVE:** `CVE-2026-115560` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-11-19
**Reference:** <https://thehackernews.com/2026/11/php-fixes-7-critical-flaws-including.html>

> The PHP Foundation has released security updates to address multiple critical security flaws that could be exploited to achieve remote code execution on affected deployments, including CVE-2026-115560.

The release of the patch follows an advance notice in which the project maintainers alerted users to multiple critical vulnerabilities affecting all supported PHP versions under specific

---
