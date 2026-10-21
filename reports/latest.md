# Zero Day Pulse

> **Generated:** 2026-10-21 02:17 UTC &nbsp;|&nbsp; **Total:** 37 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 17 &nbsp;|&nbsp; 🟡 High: 20 &nbsp;|&nbsp; ✨ Enriched: 0

---

## 1. 🟠 Zero-Day — Improve Router Hygiene to Protect Against Russian State-Sponsored Targeting

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Wed, 08 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a>

> Russian Government-Sponsored Activity Targets Poorly Configured and Vulnerable Devices Across Critical Sectors Executive summary Russian Federal Security Service (FSB) Center 16 cyber actors continue to exploit poorly configured and vulnerable networking devices worldwide, opportunistically compromising multiple critical infrastructure sector networks. This joint Cybersecurity Advisory (CSA) build…

---

## 2. 🟠 Zero-Day — October 2026 Patch Tuesday: 1,413 CVEs Include Three Zero-Days and 75 Critical Vulnerabilities

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Oct 13, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-october-2026/>

---

## 3. 🟠 Zero-Day — A2A Java SDK: Android synchronous POST forwards credentials across authorities after incomplete redirect fix

**CVE:** `CVE-2026-111765` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://github.com/advisories/GHSA-4fpj-g9jf-9rgg>

> The GHSA-9rhm fix added this safe setting in
AndroidA2AHttpClient.createConnection():

    connection.setInstanceFollowRedirects(false);

The synchronous POST builder later overwrites it:

    private boolean followRedirects = true;

    public A2AHttpResponse post() throws IOException {
        HttpURLConnection connection = createConnection(&quot;POST&quot;, false);
        connection.setInstanc…

---

## 4. 🟠 Zero-Day — Russian APT28 Breaches NATO Naval Shipbuilder in NATO Country, Deploys New Reflective Loader

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://thehackernews.com/2026/10/russian-apt28-breaches-nato-naval.html>

> The Russia-linked state-sponsored threat actor tracked as APT28 (aka BlueDelta, Fancy Bear, and Forest Blizzard) has been attributed to attacks targeting two member states of the North Atlantic Treaty Organization (NATO).

The Symantec Threat Hunter Team, which is tracking the activity cluster under the moniker Swallowtail, involved the use of a backdoor called HOOKEDGE and a previously

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 10. 🟠 Zero-Day — Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite

**CVE:** `CVE-2025-66376` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Tue, 21 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a>

> Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite Executive summary A group of Russian state-supported cyber actors has been targeting and compromising various Western government and commercial organizations using the Zimbra Collaboration Suite (ZCS) software since at least July 2025. The Russian state-supported advanced persistent threat …

---

## 11. 🟠 Zero-Day — [0day-rubbish] TRENDnet TV-IP302PI firmware 1.02.38 authenticated NTP server-address OS command injection to root command execution via a shell-form system() call (7.2 High, PR:H)

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://seclists.org/fulldisclosure/2026/Oct/34>

> Posted by disclosure via Fulldisclosure on Oct 20 0day Rubbish Research Team is publicly disclosing a vulnerability in TRENDnet TV-IP302PI firmware 1.02.38, the closed-source IP surveillance camera from TRENDnet (United States). The camera&#x27;s application daemon is shipped at /hunt/hunt_server: an ARM 32-bit EABI5 version 5TE soft-float binary, dynamically linked against /lib/ld-linux.so.3, 4.5…

---

## 12. 🟠 Zero-Day — [0day-rubbish] Royal Render 9.1.26b: default-unauthenticated job submission on rrServer TCP 7773 reaches worker-side shell execution as the worker identity, measured root (8.1 High)

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://seclists.org/fulldisclosure/2026/Oct/33>

> Posted by disclosure via Fulldisclosure on Oct 20 0day Rubbish Research Team is publicly disclosing a vulnerability in Royal Render 9.1.26b, the closed-source render-farm job manager for VFX and animation studios from Binary Alchemy (proprietor Holger Schoenberger) of Ludwigsburg, Germany. Royal Render is a different product from the Royal Server gateway sold by Royal Apps GmbH of Austria; the two…

---

## 13. 🟠 Zero-Day — [0day-rubbish] ProSoft Technology RLX-IFH24E v2.2.44 unsigned firmware upgrade package to root command execution and full account-database overwrite (7.2)

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://seclists.org/fulldisclosure/2026/Oct/32>

> Posted by disclosure via Fulldisclosure on Oct 20 0day Rubbish Research Team is publicly disclosing a vulnerability in the ProSoft RLX-IFH24E, version v2.2.44, the industrial wireless radio from ProSoft Technology, Inc. (United States). The appliance is a closed-source embedded device and an OEM build of the MicroHard Systems IPx21 platform on the MHX-910 board design: an Intel IXP425 XScale proce…

---

## 14. 🟠 Zero-Day — [0day-rubbish] Parasoft Continuous Testing Platform 10.7.5-SNAPSHOT anonymous deserialization in the database restore path to JSP command execution as uid=1000 (9.8)

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://seclists.org/fulldisclosure/2026/Oct/31>

> Posted by disclosure via Fulldisclosure on Oct 20 0day Rubbish Research Team is publicly disclosing a vulnerability in Parasoft Continuous Testing Platform 10.7.5-SNAPSHOT, the closed-source commercial continuous-testing, service-virtualisation and environment-management product from Parasoft, a United States software-testing vendor headquartered in Monrovia, California. The affected component is …

---

## 15. 🟠 Zero-Day — [0day-rubbish] Exasol Database 7.1.30 docker-db form: shipped default SYS credential to PYTHON3 UDF os.popen command execution as uid=500(exadefusr), output returned in-band (8.8)

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://seclists.org/fulldisclosure/2026/Oct/30>

> Posted by disclosure via Fulldisclosure on Oct 20 0day Rubbish Research Team is publicly disclosing a vulnerability in Exasol Database 7.1.30, the in-memory MPP analytical database from Exasol AG (Germany), examined in its docker-db single-container deployment form. The SQL engine is a proprietary C implementation named EXASolution, the server process is exacts, clients speak a proprietary binary …

---

## 16. 🟠 Zero-Day — [0day-rubbish] Edimax BR-6478AC firmware v2.20 authenticated command injection in the setWAN WAN-configuration handler, root command execution (7.2)

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://seclists.org/fulldisclosure/2026/Oct/29>

> Posted by disclosure via Fulldisclosure on Oct 20 0day Rubbish Research Team is publicly disclosing a vulnerability in the Edimax BR-6478AC, firmware image BR6478AC_v2.20.bin, the dual-band AC1750 SOHO wireless router from Edimax Technology Co., Ltd. (Taiwan). A single authenticated POST that looks like an ordinary WAN settings submission reaches system() with a request-controlled username interpo…

---

## 17. 🟠 Zero-Day — [0day-rubbish] Edimax BR-6478AC firmware v2.20 authenticated command injection in the formWlanMP manufacturing-test handler, root command execution (7.2)

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://seclists.org/fulldisclosure/2026/Oct/28>

> Posted by disclosure via Fulldisclosure on Oct 20 0day Rubbish Research Team is publicly disclosing a vulnerability in the Edimax BR-6478AC, firmware image BR6478AC_v2.20.bin, the dual-band AC1750 SOHO wireless router from Edimax Technology Co., Ltd. (Taiwan). A single authenticated POST to a manufacturing radio-calibration route that is still registered in production firmware reaches system() wit…

---

## 18. 🟡 High Severity — Chinese Government-linked Cyber Threat Actors Combine Automated and Hands-on Hacking Tools to Steal Sensitive Data

**CVE:** `CVE-2014-6278` | `CVE-2015-3306` | `CVE-2015-5477` | `CVE-2016-3081` | `CVE-2019-11510` | `CVE-2021-22205` | `CVE-2021-3199` | `CVE-2023-22894` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Tue, 06 Oc
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-281a>

> Advisory at a Glance Title Chinese Government-linked Cyber Threat Actors Combine Automated and Hands-on Hacking Tools to Steal Sensitive Data Original Publication October 8, 2026 Executive Summary Chinese government-linked cyber threat actors, enabled by the Integrity Technology Group, are combining automated scanning tools, large-scale botnets, and hands-on exploitation techniques to target and s…

---

## 19. 🟡 High Severity — #StopRansomware: SafePay Ransomware

**CVE:** `CVE-2020-3259` | `CVE-2023-20269` | `CVE-2023-27532` | `CVE-2024-40711` | `CVE-2024-40766` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 19 Oc
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-293a>

> Advisory at a Glance Title #StopRansomware: SafePay Ransomware Original Publication October 20, 2026 Executive Summary This advisory details recent activity by the SafePay ransomware group. SafePay actors have been highly active since August 2024, targeting businesses and critical infrastructure across North America, South America, Europe, and Australia. SafePay actors typically gain access to net…

---

## 20. 🟡 High Severity — A2A Java SDK: Push notification credentials logged in cleartext on protobuf parse failure

**CVE:** `CVE-2026-111762` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://github.com/advisories/GHSA-x32g-jvvm-4725>

> ### *Impact.** Push notification bearer tokens and authentication credentials submitted by clients are written to server log files in cleartext. Any operator, log aggregation system, or attacker with log access can read these secrets and use them to authenticate to the client&#x27;s push notification endpoints, potentially sending forged task status updates.

**Where.** `transport/rest/src/main/ja…

---

## 21. 🟡 High Severity — A2A Java SDK has Server-Side Request Forgery (SSRF) in push-notification delivery

**CVE:** `CVE-2026-111761` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://github.com/advisories/GHSA-q78c-5jjq-57g8>

> ---

- **Ecosystem:** Maven
- **Affected package:** `org.a2aproject.sdk:a2a-java-sdk-server-common` (push-notification delivery)
- **Affected versions:** `&lt;= 1.2.0.Final` (and `1.2.1.Final-SNAPSHOT` on `main` prior to the fix)
- **Patched version:** _(the release that carries the fix)_
- **CWE:** CWE-918 (Server-Side Request Forgery)
- **Severity:** High
- **CVSS v3.1:** `CVSS:3.1/AV:N/AC:L/PR:…

---

## 22. 🟡 High Severity — Pillow: OOB read in TiffDecode.c tile and RGBA paths leaks heap memory into pixels

**CVE:** `CVE-2026-112404` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://github.com/advisories/GHSA-c6hw-5grf-ff96>

> ```
============================================================================
OOB read in TiffDecode.c tile and RGBA paths leaks heap memory into pixels
Location: src/libImaging/TiffDecode.c:483  in _decodeTile()
Commit:   a707c6b21c313880d0771e54965d142dd42358b6
============================================================================
```

Pillow reads past the end of a heap buffer when dec…

---

## 23. 🟡 High Severity — markdown-it: Quadratic-time rendering of a single multi-line link reference definition with default options (regression since 14.0)

**CVE:** `CVE-2026-111758` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://github.com/advisories/GHSA-gfr2-rv44-r23c>

> ### Summary

A link reference definition whose label or title is never closed is O(n²) in markdown-it 15.0.2 with default options. Continuation lines are pulled lazily with str += lineContent in src/rules_block/reference.ts, and the subsequent charCodeAt and slice calls flatten the V8 cons-string, copying everything collected so far; this runs before the rule decides the definition is invalid. It …

---

## 24. 🟡 High Severity — markdown-it: Quadratic-time denial of service in inline HTML parsing with html enabled

**CVE:** `CVE-2026-111766` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://github.com/advisories/GHSA-vfgh-jcmw-g37q>

> ### Summary

With `html: true`, markdown-it takes quadratic time to parse repeated unterminated HTML constructs inside a paragraph. This affects HTML comments (`&lt;!--`), processing instructions (`&lt;?`), declarations (`&lt;!A`), and CDATA sections (`&lt;![CDATA[`).

An attacker-controlled input of a few hundred kilobytes can block the Node.js event loop for seconds or tens of seconds. The defau…

---

## 25. 🟡 High Severity — MCP  TypeScript server SDK: Shared transport or server instances delivered one HTTP client's messages to another

**CVE:** `CVE-2026-111770` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://github.com/advisories/GHSA-jm63-cq47-j5jp>

> ### Summary
In affected versions, an MCP server reached over HTTP could deliver one client&#x27;s responses and notifications to another client. This happened when clients shared one stateless transport, or one `McpServer` or `Server` instance.

Messages were matched to a connection by JSON-RPC `id` alone. SDK clients number requests from 0, so ids collide in normal use.

### Am I affected?
Yes, i…

---

## 26. 🟡 High Severity — MCP TypeScript SDK: Server bearer authentication accepted tokens issued for another service

**CVE:** `CVE-2026-111771` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://github.com/advisories/GHSA-rvq5-wwqv-78pq>

> ### Summary
In affected versions, the SDK&#x27;s server-side bearer authentication had no way to check that a token was issued for your server (its audience). Where one authorization server issues tokens for several services, a valid token for another service was also accepted by your MCP server.

### Am I affected?
Yes, if your HTTP server uses `requireBearerAuth()` or `verifyBearerToken()`, its …

---

## 27. 🟡 High Severity — MCP TypeScript client SDK: HTTP client transports and OAuth requests followed cross-origin redirects and re-sent custom headers and request bodies

**CVE:** `CVE-2026-111769` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://github.com/advisories/GHSA-6prh-2h8m-c8cw>

> ### Summary
In affected versions, the SDK&#x27;s HTTP client transports and OAuth requests followed redirects to any origin.

If an MCP server or authorization server redirected a request to another origin, that origin received custom request headers (such as an `X-API-Key` set in `requestInit.headers`) and the `mcp-session-id` header. On a `307` or `308` it also received the request body, includi…

---

## 28. 🟡 High Severity — ApostropheCMS uploadfs Azure backend leaks account-level SAS token into every public attachment URL (sas: true)

**CVE:** `CVE-2026-113652` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://github.com/advisories/GHSA-hhph-8536-gfq5>

> ## Summary

When uploadfs is configured with the Azure backend and `sas: true` (a supported configuration introduced in uploadfs 1.25.0), `createContainer()` builds the `BlobServiceClient` from a URL that embeds the full SAS query string, and Azure SDK v12 derived clients inherit that query string. As a result, `getUrl()` returns a base URL carrying the complete account/container SAS signature (`?…

---

## 29. 🟡 High Severity — ApostropheCMS: Page REST API authorization bypass

**CVE:** `CVE-2026-113670` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://github.com/advisories/GHSA-2j32-q6rx-h844>

> **Summary**
The core page REST API reads full page documents with `.permission(false)` in `getOne` and in the `all=1` tree dump, bypassing page-type `viewRole`, `visibility: private`, and `visibility: loginRequired` checks. Unauthenticated visitors and low-privilege contributors can read admin-only and non-public page content by `_id`/slug.

**Details**
`packages/apostrophe/modules/@apostrophecms/…

---

## 30. 🟡 High Severity — ApostropheCMS: Host header controls server-side image fetch origin in @apostrophecms/ai-helper, enabling authenticated SSRF

**CVE:** `CVE-2026-113671` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://github.com/advisories/GHSA-527g-ff96-x6wj>

> ## Summary

The `@apostrophecms/ai-helper` package builds the URL for a server-side image fetch by resolving a storage-relative path against `req.baseUrl`. When the site does not set a global base URL (the default), `req.baseUrl` is derived from the incoming HTTP `Host` header. An authenticated editor can generate a base64 AI image (which is persisted without a stored `url`) and then send an unaut…

---

## 31. 🟡 High Severity — ApostropheCMS: Cross-domain session token in URL confers session takeover

**CVE:** `CVE-2026-113669` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://github.com/advisories/GHSA-hhvr-8m24-qqr3>

> **Summary**
Apostrophe&#x27;s cross-domain session migration emits a single-use session token as a URL query parameter and stores it in the Mongo cache. Any client that presents the token silently adopts the target user&#x27;s full session (including `passport.user`) with no credentials.

**Details**
`packages/apostrophe/modules/@apostrophecms/i18n/index.js`:
- Token generation on cross-host/local…

---

## 32. 🟡 High Severity — ApostropheCMS: CAPTCHA response token not URL-encoded

**CVE:** `CVE-2026-113667` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://github.com/advisories/GHSA-44qr-rrjg-2cqq>

> **Summary**
Form and login CAPTCHA verification interpolate the user-supplied widget token unencoded into the server-side verification URL/body, allowing a crafted token to inject query parameters into the reCAPTCHA/hCaptcha verify request.

**Details**
- `packages/form/lib/recaptcha.js:39` — `recaptchaUri = &#x27;https://www.google.com/recaptcha/api/siteverify?secret=${recaptchaSecret}&amp;respon…

---

## 33. 🟡 High Severity — ApostropheCMS: Authenticated projection-exclusion prototype-member deletion in @apostrophecms/db-connect causes process-wide denial of service

**CVE:** `CVE-2026-113666` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://github.com/advisories/GHSA-j5rq-xfvr-p969>

> ## Summary

`@apostrophecms/db-connect` ships an in-memory MongoDB emulation used by its SQLite, PostgreSQL, and multipostgres adapters. Its `unsetNestedField` helper walks an attacker-controlled dotted field path with no segment validation and calls `delete` on the resolved property. A low-privileged authenticated user (any role holding `view-draft`, which every editor and contributor has; reduce…

---

## 34. 🟡 High Severity — ApostropheCMS sanitize-html: nonTextTags discard region ends early on an implied close, letting <noscript> content render

**CVE:** `CVE-2026-113654` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://github.com/advisories/GHSA-x3q4-9hxx-gx8m>

> ## Summary

`sanitize-html` discards the *content* of every element in `nonTextTags`. It delimits that region
using htmlparser2&#x27;s close events, and ignores the `isImplied` flag htmlparser2 passes it. Closing a
still-open **ancestor** from inside a `&lt;noscript&gt;` makes htmlparser2 unwind its stack past the
`noscript`; the synthetic implied close it emits on the way ends the discard region …

---

## 35. 🟡 High Severity — Critical FortiSIEM Flaw Gets Public Exploit PoC for Unauthenticated Remote Code Execution

**CVE:** `CVE-2026-106173` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://thehackernews.com/2026/10/critical-fortisiem-flaw-gets-public.html>

> Cybersecurity researchers have released a proof-of-concept (PoC) exploit for a recently patched critical security flaw impacting Fortinet FortiSIEM that could result in arbitrary code execution.

The vulnerability, tracked as CVE-2026-106173 (CVSS score: 9.4), is a critical path traversal flaw that could allow an unauthenticated attacker to execute unauthorized code or commands via specially

---

## 36. 🟡 High Severity — @angular/router: Denial of Service via Unmatched Empty-Path Outlet Route Matching in Server-Side Rendering (SSR)

**CVE:** `CVE-2026-111752` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://github.com/advisories/GHSA-62vg-58rm-qff7>

> A denial of service (DoS) vulnerability was identified in `@angular/router` when Server-Side Rendering (SSR) is enabled on Node.js (V8).

During route recognition, `@angular/router` fails to validate whether an auxiliary outlet segment in the URL matches a route configured for that specific outlet name. Because unconfigured empty-path outlet groups (such as `a:/()`, `x:/(...)`, or `///(...)`) are …

---

## 37. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
