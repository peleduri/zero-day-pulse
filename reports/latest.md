# Zero Day Pulse

> **Generated:** 2026-10-21 20:58 UTC &nbsp;|&nbsp; **Total:** 35 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 11 &nbsp;|&nbsp; 🟡 High: 24 &nbsp;|&nbsp; ✨ Enriched: 0

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

## 3. 🟠 Zero-Day — PHP2Shell: Two Unpatched Critical PHP RCE Flaws (CVSS 9.2) Trigger Emergency Security Alert

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-10-21
**Reference:** <https://thehackernews.com/2026/10/php2shell-two-unpatched-critical-php.html>

> This story is developing and was written before PHP&#x27;s scheduled 14:00 UTC release on October 21. Once the release is out, the affected and fixed versions below are confirmed by the official advisory.

PHP will ship an out-of-cycle security release at 14:00 UTC today, October 21, for two critical vulnerabilities that its security team has rated 9.2 on the CVSS v4.0 scale but has not described.…

---

## 4. 🟠 Zero-Day — A2A Java SDK: Android synchronous POST forwards credentials across authorities after incomplete redirect fix

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

## 11. 🟠 Zero-Day — Storybook: Missing origin validation in Storybook preview allows code injection from malicious websites

**CVE:** `CVE-2026-114125` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-21
**Reference:** <https://github.com/advisories/GHSA-f2ph-cmg5-wxc8>

> **Summary:** A malicious website may be able to cause unauthorized file changes in a developer’s project while an affected Storybook development server is running. Under additional conditions, a changed file could be executed by a local runtime with the developer’s privileges. We are not aware of exploitation in the wild.

## Who is impacted?

You are impacted if you run a Storybook dev server in …

---

## 12. 🟡 High Severity — Chinese Government-linked Cyber Threat Actors Combine Automated and Hands-on Hacking Tools to Steal Sensitive Data

**CVE:** `CVE-2014-6278` | `CVE-2015-3306` | `CVE-2015-5477` | `CVE-2016-3081` | `CVE-2019-11510` | `CVE-2021-22205` | `CVE-2021-3199` | `CVE-2023-22894` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Tue, 06 Oc
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-281a>

> Advisory at a Glance Title Chinese Government-linked Cyber Threat Actors Combine Automated and Hands-on Hacking Tools to Steal Sensitive Data Original Publication October 8, 2026 Executive Summary Chinese government-linked cyber threat actors, enabled by the Integrity Technology Group, are combining automated scanning tools, large-scale botnets, and hands-on exploitation techniques to target and s…

---

## 13. 🟡 High Severity — #StopRansomware: SafePay Ransomware

**CVE:** `CVE-2020-3259` | `CVE-2023-20269` | `CVE-2023-27532` | `CVE-2024-40711` | `CVE-2024-40766` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 19 Oc
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-293a>

> Advisory at a Glance Title #StopRansomware: SafePay Ransomware Original Publication October 20, 2026 Executive Summary This advisory details recent activity by the SafePay ransomware group. SafePay actors have been highly active since August 2024, targeting businesses and critical infrastructure across North America, South America, Europe, and Australia. SafePay actors typically gain access to net…

---

## 14. 🟡 High Severity — Pillow: Image.quantize() with empty palette leaks uninitialized stack memory

**CVE:** `CVE-2026-112898` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-21
**Reference:** <https://github.com/advisories/GHSA-rfgq-q3w2-pmv2>

> ```
============================================================================
Image.quantize() with empty palette leaks uninitialized stack memory
Location: src/libImaging/Palette.c:216  in ImagingPaletteCacheUpdate()
Commit:   a707c6b21c313880d0771e54965d142dd42358b6
============================================================================
```

When an application lets a user supply the pal…

---

## 15. 🟡 High Severity — Pillow: P;2L and P;4L decoders may read 1 to 3 bytes past the passed buffer size

**CVE:** `CVE-2026-112394` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-21
**Reference:** <https://github.com/advisories/GHSA-4558-3h8r-v8xp>

> ### Summary

On `main`, even with the guard in #9725, it&#x27;s possible to have these decoders read 1 to 3 bytes past the end of the passed buffer with a suitable width/height.

### Details

`ImagingRawDecode` and the `P;2L` / `P;4L` unpackers disagree about how many bytes a line of data occupies.

The raw decoder derives the line size from the bits per pixel

```c
state-&gt;bytes = (state-&gt;xs…

---

## 16. 🟡 High Severity — Vitest: Servers misapply `server.fs.deny`, serving `.env`, private keys, `.git`, and the API token file

**CVE:** `CVE-2026-112948` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-21
**Reference:** <https://github.com/advisories/GHSA-p458-7748-mcp3>

> ### Summary

In Vitest 5, Vite&#x27;s `server.fs.deny` is not applied as intended on Vitest&#x27;s dev servers. Depending on the server, files that Vite refuses to serve by default (such as `.env`, private keys and certificates, `.npmrc`, and `.git`) or Vitest&#x27;s own API token file (`.vitest-secret-token`) can be read over plain HTTP by a client that can reach the server. In Browser Mode with …

---

## 17. 🟡 High Severity — Vitest: Windows backslash traversal bypasses the @vitest/mocker redirect allowlist fix

**CVE:** `CVE-2026-112950` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-21
**Reference:** <https://github.com/advisories/GHSA-xp26-3454-mjgp>

> ## Summary

The path traversal fix released for [GHSA-82fw-gwwq-j7x9](https://github.com/vitest-dev/vitest/security/advisories/GHSA-82fw-gwwq-j7x9) can be bypassed on Windows by using a backslash in the redirect URL pathname.

The fixed code joins an attacker-controlled URL pathname with the Vite root using `node:path/posix`, then passes that string to Vite&#x27;s file allowlist check. On Windows,…

---

## 18. 🟡 High Severity — ApostropheCMS: Exposure of Sensitive Information via predictable export filenames

**CVE:** `CVE-2026-112953` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-21
**Reference:** <https://github.com/advisories/GHSA-5gc8-frw3-3vqm>

> ## Summary

When a user exports content through `@apostrophecms/import-export`, the module copies the generated archive into uploadfs at `/exports/` and returns a public URL under `/uploads/exports/`. The filename is fully deterministic: site `shortName`, document type, a `YYYYMMDDHHmmss` timestamp, and the format extension. There is no secret token.

Anyone who can guess that path can download th…

---

## 19. 🟡 High Severity — djust: Arbitrary absolute-path file read in the find_handlers_for_template MCP tool

**CVE:** `CVE-2026-113731` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-21
**Reference:** <https://github.com/advisories/GHSA-r57g-mc79-8hj2>

> ### Affected version / file / line
Version: djust v1.1.4 (latest release, published 2026-09-23). File: python/djust/mcp/server.py:354-433 (MCP tool find_handlers_for_template). Confirmed identical on the commit used for triage, a7e4fafd1667b4db0b1465652d4a63cb17117a07.

### Description
```
@mcp.tool()
def find_handlers_for_template(template_path: str) -&gt; str:
    &quot;&quot;&quot;
    Args:
  …

---

## 20. 🟡 High Severity — ApostropheCMS: POST /api/v1/@apostrophecms/doc/slugTaken discloses existence of private/admin-only content to any authenticated user

**CVE:** `CVE-2026-112952` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-21
**Reference:** <https://github.com/advisories/GHSA-f66c-mpj2-3r8h>

> ### Summary
The `slugTaken` endpoint returns a boolean indicating whether a slug is in use across
all document types and visibility levels, with no permission or type filter. Any logged-in
user (including editors) can enumerate the slug space of private pages, drafts, and
archived content.

### Details
`POST /api/v1/@apostrophecms/doc/slugTaken` with body `{ &quot;slug&quot;: &quot;target-slug&quo…

---

## 21. 🟡 High Severity — ApostropheCMS: GET /api/v1/@apostrophecms/page/:id bypasses viewRole restriction and exposes viewPermission-gated fields to lower-privileged users

**CVE:** `CVE-2026-112957` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-21
**Reference:** <https://github.com/advisories/GHSA-vh56-5m88-39rq>

> ### Summary
The `getOne` REST endpoint for pages does not apply `viewRole` type-level restrictions
or `viewPermission` field-level redaction. An editor-level user who knows a document
`_id` can read the full content of admin-only pages and their privileged fields, while
the `getAll` endpoint correctly enforces both restrictions.

### Details
**Finding 3 — viewRole bypass:**
`modules/@apostrophecms…

---

## 22. 🟡 High Severity — ApostropheCMS sanitize-html: unbounded recursion when re-sanitizing the fallback of a discarded iframe (stack overflow, nestingLimit not enforced)

**CVE:** `CVE-2026-113650` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-21
**Reference:** <https://github.com/advisories/GHSA-c9rx-x947-fp3h>

> ### Summary

Since 2.18.0, when an `&lt;iframe&gt;` is not allowed and `disallowedTagsMode` is `&#x27;discard&#x27;` (the defaults),
its raw-text content is re-sanitized by a recursive call to `sanitizeHtml(text, options)` (the change
from #5564, fixing #5550). The recursion has no bound and starts each nested call with a fresh state.
Two consequences, both absent from 2.17.7 and 2.17.4:

1. A few…

---

## 23. 🟡 High Severity — virtualenv bash activate runs commands from an environment name with a backslash before $

**CVE:** `CVE-2026-113725` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-21
**Reference:** <https://github.com/advisories/GHSA-vxj4-q4g9-crj7>

> ### Summary

The bash `activate` script escapes the environment name for only one of the two passes bash makes over `PS1`, so a
backslash in the name undoes the escaping and a name containing `\$(...)` runs as commands in the user&#x27;s shell each
time bash draws the prompt.

### Affected area

`src/virtualenv/activation/bash/activate.sh`, the block that prepends the environment name to `PS1`.

#…

---

## 24. 🟡 High Severity — Vite: Cross origin script execution through Vite custom middleware

**CVE:** `CVE-2026-112945` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-21
**Reference:** <https://github.com/advisories/GHSA-9jrq-w75r-8gcw>

> ### Summary

When accessing a malicious site while a dev server using Vite is running, that site was able to load scripts in a page served by the dev server.

### Impact

Only apps that match the following conditions are affected:

- the dev server passes an unchanged browser request URL to `server.transformIndexHtml`: this is normally used for `server.middlewareMode: true` or `appType: &#x27;cust…

---

## 25. 🟡 High Severity — Vite: First 4 bytes of files outside of `server.fs` setting is exposed by `?vite-wasm-instance`

**CVE:** `CVE-2026-112947` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-21
**Reference:** <https://github.com/advisories/GHSA-vfpm-58rq-9qcg>

> ### Summary

The first 4 bytes of files outside of `server.fs` setting can be returned to the browser by a request containing `?vite-wasm-instance`.

### Impact

 Only apps that match one of the following conditions are affected:

- explicitly expose the Vite dev server to the network using `--host` or the [`server.host`](https://vite.dev/config/server-options#server-host) option
- there&#x27;s a …

---

## 26. 🟡 High Severity — virtualenv activate runs commands from the environment name in zsh with PROMPT_SUBST

**CVE:** `CVE-2026-113726` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-21
**Reference:** <https://github.com/advisories/GHSA-5vjq-rrrf-7h2q>

> ### Impact

zsh users activate an environment with the bash `activate` script, which puts the environment name into `PS1`. Since
21.13.0 the script escapes backslashes, dollar signs and backticks in that name, but only when `BASH_VERSION` is set, so
zsh gets the raw value. With the `PROMPT_SUBST` option set, zsh runs parameter expansion, command substitution and
arithmetic expansion on `PS1` each …

---

## 27. 🟡 High Severity — virtualenv activation scripts run code from a path that contains a placeholder name

**CVE:** `CVE-2026-113776` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-21
**Reference:** <https://github.com/advisories/GHSA-8rjx-v5ww-45pp>

> ### Impact

`ViaTemplateActivator.instantiate_template` replaces the placeholders in an activation template one key at a time, each across the whole text. When a value that it already substituted and quoted contains the name of a later placeholder, the later pass rewrites that name inside the quoted literal. The inserted value brings its own quotes, which close the outer literal, and the rest of t…

---

## 28. 🟡 High Severity — Slack Morphism verifier errors disclose valid HMACs in the logs

**CVE:** `CVE-2026-113799` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-21
**Reference:** <https://github.com/advisories/GHSA-26w4-8w32-4x3v>

> ### Summary

Slack Morphism exposes the correct Slack request HMAC when signature verification fails.

For an invalid request, `slack-morphism` computes the correct signature for the attacker-controlled timestamp and request body and stores it in `SlackEventWrongSignatureError.generated_hash`. The error&#x27;s `Debug` and `Display` representations expose that value, and the default Axum listener e…

---

## 29. 🟡 High Severity — Threat Brief: Critical Vulnerabilities in PHP: CVE-2026-109618, CVE-2026-109619

**CVE:** `CVE-2026-109618` | `CVE-2026-109619` &nbsp;|&nbsp; **Source:** Unit 42 (Palo Alto) &nbsp;|&nbsp; **Published:** 2026-10-21
**Reference:** <https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/>

> CVE-2026-109618 and CVE-2026-109619 are Critical vulnerabilities in PHP, a scripting language used globally for web servers and CMS systems. The post Threat Brief: Critical Vulnerabilities in PHP: CVE-2026-109618, CVE-2026-109619 appeared first on Unit 42 .

---

## 30. 🟡 High Severity — OpenChoreo: Authorization bypass on WorkflowRun update allows cross-project takeover of workflow runs

**CVE:** `CVE-2026-113727` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-21
**Reference:** <https://github.com/advisories/GHSA-46r4-q7wv-32fc>

> ## Summary

The OpenChoreo API server authorized `PUT .../workflowruns/{runName}` against ownership metadata taken from the request body, while the object it actually mutated was selected by the URL path. Nothing forced the two to agree.

A `WorkflowRun`&#x27;s membership in a project and component is carried entirely by its `openchoreo.dev/project` and `openchoreo.dev/component` labels. Because t…

---

## 31. 🟡 High Severity — ApostropheCMS: Unauthenticated resource exhaustion via pre-auth aposBigUpload processing in @apostrophecms/import-export

**CVE:** `CVE-2026-113711` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-21
**Reference:** <https://github.com/advisories/GHSA-86wm-68pq-5jwq>

> ## Summary

A potential unauthenticated denial-of-service vulnerability exists in the chunked import upload path used by `@apostrophecms/import-export`.

The affected import API routes invoke:

`self.apos.http.bigUploadMiddleware()`

before the actual import handler performs its authentication check.

Because no `authorize` callback is supplied to `bigUploadMiddleware()`, unauthenticated requests …

---

## 32. 🟡 High Severity — CISA Orders Federal Agencies to Patch Exploited Plex2Shell, Siemens, and SiteGuard Flaws

**CVE:** `CVE-2026-96652` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-10-21
**Reference:** <https://thehackernews.com/2026/10/cisa-orders-federal-agencies-to-patch.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added four vulnerabilities to its Known Exploited Vulnerabilities (KEV) catalog, including four vulnerabilities impacting Plex Media Server that&#x27;s collectively called Plex2Shell.

The vulnerabilities are listed below -


  CVE-2026-96652 (CVSS score: 5.3) - Plex Media Server Server-Side Request Forgery (SSRF)

---

## 33. 🟡 High Severity — A2A Java SDK: Push notification credentials logged in cleartext on protobuf parse failure

**CVE:** `CVE-2026-111762` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-20
**Reference:** <https://github.com/advisories/GHSA-x32g-jvvm-4725>

> ### *Impact.** Push notification bearer tokens and authentication credentials submitted by clients are written to server log files in cleartext. Any operator, log aggregation system, or attacker with log access can read these secrets and use them to authenticate to the client&#x27;s push notification endpoints, potentially sending forged task status updates.

**Where.** `transport/rest/src/main/ja…

---

## 34. 🟡 High Severity — A2A Java SDK has Server-Side Request Forgery (SSRF) in push-notification delivery

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

## 35. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
