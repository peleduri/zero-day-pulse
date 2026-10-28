# Zero Day Pulse

> **Generated:** 2026-10-28 21:57 UTC &nbsp;|&nbsp; **Total:** 43 &nbsp;|&nbsp; 🔴 KEV: 2 &nbsp;|&nbsp; 🟠 Zero-Day: 16 &nbsp;|&nbsp; 🟡 High: 25 &nbsp;|&nbsp; ✨ Enriched: 0

---

## 1. 🔴 CISA KEV — CVE-2026-46300 — Linux Kernel Missing Initialization of a Variable Vulnerability

**CVE:** `CVE-2026-46300` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-46300>

> Vendor: Linux | Product: Kernel. Linux Kernel contains a missing initialization of a variable vulnerability that could allow for unintended modification of page-cache-backed data via failure to preserve the shared-fragment marker during socket buffer coalescing, causing ESP input processing to decrypt shared fragments in place. This vulnerability can be chained with CVE-2026-109618 and CVE-2026-10…

---

## 2. 🔴 CISA KEV — CVE-2026-41709 — Broadcom VMWare ESX Insufficient Logging Vulnerability

**CVE:** `CVE-2026-41709` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-41709>

> Vendor: Broadcom | Product: VMware ESX. Broadcom VMWare ESX contains an insufficient logging vulnerability that could allow a malicious actor with admin access to perform certain operations without being logged. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance…

---

## 3. 🟠 Zero-Day — Improve Router Hygiene to Protect Against Russian State-Sponsored Targeting

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Wed, 08 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a>

> Russian Government-Sponsored Activity Targets Poorly Configured and Vulnerable Devices Across Critical Sectors Executive summary Russian Federal Security Service (FSB) Center 16 cyber actors continue to exploit poorly configured and vulnerable networking devices worldwide, opportunistically compromising multiple critical infrastructure sector networks. This joint Cybersecurity Advisory (CSA) build…

---

## 4. 🟠 Zero-Day — October 2026 Patch Tuesday: 1,413 CVEs Include Three Zero-Days and 75 Critical Vulnerabilities

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Oct 13, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-october-2026/>

---

## 5. 🟠 Zero-Day — Echo static file middleware route protection bypass via encoded dot-dot traversal

**CVE:** `CVE-2026-118654` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://github.com/advisories/GHSA-3pmx-cf9f-34xr>

> ## Summary

Echo v5.2.0 contains a bypass of the fix for GHSA-vfp3-v2gw-7wfq. The fix rejects encoded path separators such as `%2F` and `%5C` before static file path unescaping, but two traversal forms still bypass route-level middleware protections for static files.

The primary bypass uses encoded dot-dot segments. A request such as `/public/%2E%2E/admin/secret.txt` passes the encoded-separator …

---

## 6. 🟠 Zero-Day — Hackers now scanning systems for recently-patched Oracle flaw

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://www.bleepingcomputer.com/news/security/hackers-now-scanning-systems-for-recently-patched-oracle-flaw/>

> Attackers have begun probing the Internet for systems unpatched against a recently disclosed critical Oracle E-Business Suite (EBS) vulnerability. [...]

---

## 7. 🟠 Zero-Day — ShinyHunters-Exploited Oracle PeopleSoft Zero-Day Turns Out to Be Three Chained Flaws

**CVE:** `CVE-2026-35273` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://thehackernews.com/2026/10/shinyhunters-exploited-oracle.html>

> The critical Oracle PeopleSoft bug that ShinyHunters has exploited since May is not one flaw but three chained together, the researchers who reported it said this week.

Oracle patched all three under a single identifier, CVE-2026-35273, in June. Its root is a server-side request forgery (SSRF) that reaches an internal management interface because PeopleSoft trusts its own loopback address

---

## 8. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

---

## 9. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

---

## 10. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

---

## 11. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

---

## 12. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 13. 🟠 Zero-Day — Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite

**CVE:** `CVE-2025-66376` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Tue, 21 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a>

> Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite Executive summary A group of Russian state-supported cyber actors has been targeting and compromising various Western government and commercial organizations using the Zimbra Collaboration Suite (ZCS) software since at least July 2025. The Russian state-supported advanced persistent threat …

---

## 14. 🟠 Zero-Day — Electrum: Malicious server can replace a just-broadcast tx and try to trick user into RBF-ing it

**CVE:** `CVE-2026-117601` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://github.com/advisories/GHSA-6jp4-8v48-cc5v>

> ### Summary

The main Electrum server the client connects to is trusted with mempool (&quot;unconfirmed&quot;) transactions. This is documented [design](https://electrum.readthedocs.io/en/latest/faq.html#does-electrum-trust-servers). [0]

However now someone figured out a way to practically exploit it:
- when the client broadcasts a new tx1, a malicious server can swallow it,
- and update the clie…

---

## 15. 🟠 Zero-Day — Happy DOM has cookie scope forgery: no DNS-label boundary on Domain= matching , attacker origin sets victim cookies

**CVE:** `CVE-2026-118661` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://github.com/advisories/GHSA-5fpq-26gf-qwcr>

> ### Summary
A cookie-scoping bug in happy-dom lets an attacker origin set cookies that a victim origin then receives, diverging from browser semantics.

### Details
happy-dom matches Domain=example.com against notexample.com (endsWith without a DNS-label boundary), diverging from browser semantics (verified 20.11.6 npm latest: cookieMatchesURL(Domain=example.com, url=http://notexample.com) = true)…

---

## 16. 🟠 Zero-Day — Volt Typhoon Used Covert Silent Train Network in Four Zero-Day Exploitation Campaigns

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://thehackernews.com/2026/10/volt-typhoon-used-covert-silent-train.html>

> The China-nexus cyber espionage group known as Volt Typhoon has been attributed to a now-disrupted covert access network dubbed Silent Train that has been put to use for zero-day exploitation and strategic access.

&quot;First identified in late 2023, Silent Train uses rotating chains of compromised SOHO, IoT, and enterprise infrastructure,&quot; Lumen Technologies Black Lotus Labs said in a repor…

---

## 17. 🟠 Zero-Day — Volt Typhoon hides zero-day attacks using 'Silent Train' framework

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://www.bleepingcomputer.com/news/security/volt-typhoon-hides-zero-day-attacks-using-silent-train-framework/>

> Chinese state-sponsored hacking group Volt Typhoon has been using a framework that relies on rotating chains of connected devices compromised on demand, including for zero-day attacks targeting high-value systems. [...]

---

## 18. 🟠 Zero-Day — Japan's GMO Offers $1 Million Bounty to Catch Hackers Behind FX Trading Cloud Breach

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://thehackernews.com/2026/10/japans-gmo-offers-1-million-bounty-to.html>

> Japan&#x27;s GMO Internet Group is offering up to $1 million in total for tips that help catch the attackers who breached its Onamae.com Desktop Cloud service, after refusing to pay an extortion demand.

The reward program opened on October 28 and pays only if a tip helps lead to an arrest or an international wanted notice. The service hosts Windows desktops used for FX trading,

---

## 19. 🟡 High Severity — Chinese Government-linked Cyber Threat Actors Combine Automated and Hands-on Hacking Tools to Steal Sensitive Data

**CVE:** `CVE-2014-6278` | `CVE-2015-3306` | `CVE-2015-5477` | `CVE-2016-3081` | `CVE-2019-11510` | `CVE-2021-22205` | `CVE-2021-3199` | `CVE-2023-22894` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Tue, 06 Oc
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-281a>

> Advisory at a Glance Title Chinese Government-linked Cyber Threat Actors Combine Automated and Hands-on Hacking Tools to Steal Sensitive Data Original Publication October 8, 2026 Executive Summary Chinese government-linked cyber threat actors, enabled by the Integrity Technology Group, are combining automated scanning tools, large-scale botnets, and hands-on exploitation techniques to target and s…

---

## 20. 🟡 High Severity — #StopRansomware: SafePay Ransomware

**CVE:** `CVE-2020-3259` | `CVE-2023-20269` | `CVE-2023-27532` | `CVE-2024-40711` | `CVE-2024-40766` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 19 Oc
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-293a>

> Advisory at a Glance Title #StopRansomware: SafePay Ransomware Original Publication October 20, 2026 Executive Summary This advisory details recent activity by the SafePay ransomware group. SafePay actors have been highly active since August 2024, targeting businesses and critical infrastructure across North America, South America, Europe, and Australia. SafePay actors typically gain access to net…

---

## 21. 🟡 High Severity — Mem0: Cross-tenant conversation leak via unescaped delimiter collision in session-scope key (_build_session_scope)

**CVE:** `CVE-2026-116575` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://github.com/advisories/GHSA-5324-3w58-qpp2>

> Summary

_build_session_scope() in mem0/memory/main.py builds the conversation-history scope key used to fetch/store the last N raw messages by naively joining caller-supplied user_id/agent_id/run_id values with unescaped &amp; and = delimiters:

def _build_session_scope(filters):
    parts = []
    for key in sorted([&quot;user_id&quot;, &quot;agent_id&quot;, &quot;run_id&quot;]):
        val = f…

---

## 22. 🟡 High Severity — vLLM: Permissive default CORS origins allow cross-origin requests to the vLLM HTTP server

**CVE:** `CVE-2026-115917` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://github.com/advisories/GHSA-vvpg-rrww-wpmh>

> ### Summary

The OpenAI-compatible server registers Starlette `CORSMiddleware` with
`allowed_origins` defaulting to `[&quot;*&quot;]`, and performs no authentication unless
`--api-key` (or `VLLM_API_KEY`) is configured. A web page on any origin can send
requests to a vLLM server that the victim&#x27;s browser can reach (for example
`localhost` or an internal/VPN address) and read the responses. Th…

---

## 23. 🟡 High Severity — vLLM: DoS via unbounded chat_template Jinja2 rendering exhausts the renderer thread pool

**CVE:** `CVE-2026-115911` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://github.com/advisories/GHSA-542m-9234-8gvf>

> ### Summary
vLLM renders chat templates by passing the resolved Jinja2 source to `tokenizer.apply_chat_template()`, which compiles and `.render()`s it in an `ImmutableSandboxedEnvironment`. The sandbox prevents code-execution escapes but imposes **no wall-clock timeout, no output-size cap, and no nested-loop or binop limit**. The render runs in a `ThreadPoolExecutor` whose `max_workers` defaults t…

---

## 24. 🟡 High Severity — Go JOSE: Panic during CBC-HMAC processing

**CVE:** `CVE-2026-116585` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://github.com/advisories/GHSA-4w3g-jfj2-cw2q>

> ### Summary

Decrypting a ciphertext with &quot;A128CBC-HS256&quot;, &quot;A192CBC-HS384&quot;, or &quot;A256CBC-HS512&quot; can result in a panic on untrusted input.

Note this advisory is the same as https://github.com/go-jose/go-jose/security/advisories/GHSA-6mp9-8xrw-74r4.

### Details

Insufficient validation of parameters can lead to attempting to index into an empty buffer. See https://gith…

---

## 25. 🟡 High Severity — systeminformation has path traversal in Linux networkStats() that allows symlink-based file disclosure outside /sys/class/net

**CVE:** `CVE-2026-116673` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://github.com/advisories/GHSA-4vjg-vx72-qq4g>

> ### Summary

On Linux, `systeminformation@5.33.13` builds `/sys/class/net/&lt;iface&gt;` paths from the caller-supplied `networkStats(iface)` value without checking that the resolved path stays inside `/sys/class/net`. A caller who can create a symlink fixture and control the value passed to this API can make the function return the first line of a file readable by the Node process.

### Details

…

---

## 26. 🟡 High Severity — graphql-scalars PhoneNumber scalar is vulnerable to regular expression denial of service

**CVE:** `CVE-2026-115887` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://github.com/advisories/GHSA-x8rm-f576-gq67>

> ## Summary

The regular expression behind `GraphQLPhoneNumber` since 1.24.1 backtracks exponentially. A string made of a run of digits followed by one character that makes the match fail (for example `&quot;1&quot;.repeat(30) + &quot;x&quot;`) blocks the JavaScript thread for seconds, and every additional digit doubles the time.

graphql-js calls `parseLiteral` while *validating* a document and `p…

---

## 27. 🟡 High Severity — Autobahn Python: permessage-brotli inflates a whole frame before maxMessagePayloadSize is checked (incomplete fix of GHSA-hxp9-w8x3-p566)

**CVE:** `CVE-2026-116579` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://github.com/advisories/GHSA-pjh6-c8mg-3x7m>

> ### Summary

permessage-brotli inflates each frame fully before checking maxMessagePayloadSize, so one 421-byte frame makes the server allocate about 545 MiB even with a 1 MiB message limit (brotli expands about 1,000,000:1). Any unauthenticated client can exhaust server memory this way on servers that enable permessage-brotli. This bypasses the GHSA-hxp9-w8x3-p566 fix.

### Details

In 26.7.1 the…

---

## 28. 🟡 High Severity — zip: Critical Parser Differential & Security Control Bypass via Dual-Header Inconsistencies (Zip Cloaking) Leading to Arbitrary File Overwrite & RCE

**CVE:** `CVE-2026-115905` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://github.com/advisories/GHSA-m665-v7pm-7grj>

> ## Summary
A critical architectural parser differential exists in the `zip` crate (`&lt;= 9.0.4`) between random-access archive readers (`ZipArchive`) and streaming readers (`ZipStreamReader`). `ZipArchive` considers the Central Directory File Header (CDFH) authoritative and ignores the filename declared in the Local File Header (LFH). In contrast, `ZipStreamReader` relies exclusively on the Local…

---

## 29. 🟡 High Severity — LangGraph JavaScript custom authentication may permit cross-user Store access

**CVE:** `CVE-2026-118668` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://github.com/advisories/GHSA-4hm6-w6qq-w73v>

> ## Summary

LangGraph deployments using JavaScript or TypeScript custom authentication may fail to apply Store authorization changes returned by an authorization handler. In affected deployments, an authenticated user may be able to access Store data outside their authorized namespace.

## Required conditions

A deployment is affected only when all of the following conditions apply:

- It uses an …

---

## 30. 🟡 High Severity — filelock: StrictSoftFileLock and SoftReadWriteLock adopt a protocol directory another user created first, losing mutual exclusion

**CVE:** `CVE-2026-112911` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://github.com/advisories/GHSA-9c4x-gm8v-wgc4>

> `StrictSoftFileLock`, `AsyncStrictSoftFileLock`, `SoftReadWriteLock` and `AsyncSoftReadWriteLock` keep their whole ownership state as files in a directory derived from the lock path (`&lt;path&gt;.filelock/claims`, `&lt;path&gt;.rw/{gen,holders}`). When that directory already exists they adopt it after checking only that it is a real directory, not who owns it. Another local user who can create na…

---

## 31. 🟡 High Severity — filelock: SoftFileLock removes a live holder's marker when another user forges the PID in a writable marker

**CVE:** `CVE-2026-112939` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://github.com/advisories/GHSA-rfpc-qcw5-3pc4>

> `SoftFileLock`, `MarkerSoftFileLock`, `SoftFileLease`, their async variants and a `FileLock` that has fallen back to a soft lock on `ENOSYS` decide from the record inside the marker file whether its owner is gone. The marker is the file whose presence says a process holds the lock. They do not check who could have written that record.

A local user who can write the marker but cannot remove it rew…

---

## 32. 🟡 High Severity — filelock: Symlink swap during SoftFileLock's writability check leaks whether a path exists and is writable by the lock taker

**CVE:** `CVE-2026-112912` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://github.com/advisories/GHSA-9j6q-wvj5-jgjg>

> `raise_on_not_writable_file()` is the check that `SoftFileLock` and the locks sharing its acquire path run before every attempt. It looks at the lock path with `os.lstat`, so that it judges a planted symlink (a file that points at another path) by itself. When the node has no owner-write bit, it then calls `os.access(filename, os.W_OK)`, which follows symlinks. A local user who can create entries …

---

## 33. 🟡 High Severity — filelock: StrictSoftFileLock follows a symbolic link swapped in at <path>.filelock and creates claim files in a directory another local user chooses

**CVE:** `CVE-2026-112938` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://github.com/advisories/GHSA-m462-7rxw-wvpg>

> `StrictSoftFileLock` and `AsyncStrictSoftFileLock` check `&lt;path&gt;.filelock` (the coordination directory that holds the lock&#x27;s state) with one `lstat` call on its name. `lstat` reports what a name is without following a symbolic link (a file that redirects to another path). After that check, the code reaches `&lt;path&gt;.filelock/claims` by pathname for every later operation (`mkdir`, sc…

---

## 34. 🟡 High Severity — Happy DOM: SSRF via iframe and link stylesheet when parsing untrusted HTML

**CVE:** `CVE-2026-118660` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://github.com/advisories/GHSA-c8p4-j97h-3vg8>

> ## Summary
happy-dom v20.8.9 makes real server-side HTTP requests to arbitrary URLs when parsing HTML containing `&lt;iframe&gt;` or `&lt;link rel=&quot;stylesheet&quot;&gt;` elements. This behavior is enabled by default (`disableIframePageLoading: false`, `disableCSSFileLoading: false`). When an application uses happy-dom to parse untrusted HTML on the server side, an attacker can trigger Server-…

---

## 35. 🟡 High Severity — GraphQL Tools: Per-request connection parameters persist into later users' WebSocket authentications

**CVE:** `CVE-2026-118665` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://github.com/advisories/GHSA-434m-5hcj-pxf3>

> # Stale authentication state in `@graphql-tools/executor-legacy-ws`: per-request `extensions.connectionParams` persist in executor closure state and are replayed in a later caller&#x27;s `connection_init`

## Report metadata

| Field | Value |
| --- | --- |
| Package | `@graphql-tools/executor-legacy-ws` (npm, `pkg:npm/%40graphql-tools/executor-legacy-ws`) |
| Repository | https://github.com/ardat…

---

## 36. 🟡 High Severity — GraphQL Tools: Shared legacy executor routes one subscription's results to a different caller

**CVE:** `CVE-2026-118666` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://github.com/advisories/GHSA-mp66-8ww2-pcwm>

> # Cross-tenant subscription data leak in `@graphql-tools/executor-legacy-ws`: a shared `websocket.onmessage` is replaced on every `subscribe()`, and `DATA` frames are delivered without checking the protocol operation id

## Report metadata

| Field | Value |
| --- | --- |
| Package | `@graphql-tools/executor-legacy-ws` (npm, `pkg:npm/%40graphql-tools/executor-legacy-ws`) |
| Repository | https://g…

---

## 37. 🟡 High Severity — Echo has a Static Middleware Double-Unescape Path Traversal

**CVE:** `CVE-2026-118655` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://github.com/advisories/GHSA-xwq5-6cqp-vx96>

> ## Summary

Commit a9ede66a (PR #3006, issue #2599) silently fixed a path traversal vulnerability in the Echo web framework&#x27;s static file middleware.

## Vulnerability

The static middleware double-unescaped URL paths. Go&#x27;s net/http already decodes Request.URL.Path, but middleware/static.go unconditionally called url.PathUnescape() again:

```go
// BEFORE (vulnerable)
pathUnescape := tru…

---

## 38. 🟡 High Severity — Highcharts Dashboards parses sidebar component labels as HTML

**CVE:** `CVE-2026-118252` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://github.com/advisories/GHSA-rcqf-f6h2-ccg9>

> ### Impact
The component language strings shown in the edit mode sidebar are parsed as HTML rather than inserted as text. An attacker who controls those language options can supply markup carrying event handlers, which execute in the origin of the page hosting the dashboard once the sidebar renders the affected labels. Exploitation requires that untrusted data reach the Dashboards language configu…

---

## 39. 🟡 High Severity — Highcharts Dashboards: `__proto__` data table id writes sync listeners to `Object.prototype`

**CVE:** `CVE-2026-118243` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://github.com/advisories/GHSA-jqgh-w3cc-7jqw>

> ### Impact
The data cursor keeps its listener and state bookkeeping in plain objects keyed by data table id, so a table id of `__proto__` supplied in the `dataPool` connector configuration resolves to `Object.prototype` when a sync registers its listeners, and the registration creates a property on `Object.prototype` named after the sync state and holding the internal listener array. The property …

---

## 40. 🟡 High Severity — Echo's middleware.Static: `%2F`-encoded path bypasses route/group middleware guarding a statically-served path

**CVE:** `CVE-2026-118650` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://github.com/advisories/GHSA-375p-5qhx-8wq4>

> ## Summary

When `middleware.Static` is mounted globally (`e.Use(middleware.Static(...))`) and an application relies on a **route- or group-level middleware guard** to restrict a path that also falls under the served static root, a `%2F`-encoded request bypasses that guard while the file is still served. This is the same encoding/decoding mismatch fixed for `StaticFS`/`StaticDirectoryHandler` in C…

---

## 41. 🟡 High Severity — Hackers Target Critical Oracle E-Business Suite RCE Flaw Days After Security Patch

**CVE:** `CVE-2026-101767` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://thehackernews.com/2026/10/hackers-target-critical-oracle-e.html>

> Threat actors are beginning to probe for a newly patched critical vulnerability in Oracle E-Business Suite (EBS), according to threat intelligence firm Defused Cyber.

The vulnerability in question is CVE-2026-101767 (CVSS score: 9.8) , a case of improper authentication in the Oracle Application Object Library of Oracle E-Business Suite. It was patched by Oracle last week as part of its Critical

---

## 42. 🟡 High Severity — Adobe Fixes 8 Critical Campaign Classic Flaws Allowing Code Execution and Security Bypass

**CVE:** `CVE-2026-104351` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-10-28
**Reference:** <https://thehackernews.com/2026/10/adobe-fixes-8-critical-campaign-classic.html>

> Adobe has released patches to address multiple critical security flaws in Campaign Classic that, if successfully exploited, could result in arbitrary code execution, security feature bypass, and privilege escalation.

The list of eight vulnerabilities is as follows -


  CVE-2026-104351 (CVSS score: 9.9) - A code injection vulnerability that could lead to arbitrary code execution.

---

## 43. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
