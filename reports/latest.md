# Zero Day Pulse

> **Generated:** 2026-10-27 21:32 UTC &nbsp;|&nbsp; **Total:** 44 &nbsp;|&nbsp; 🔴 KEV: 2 &nbsp;|&nbsp; 🟠 Zero-Day: 13 &nbsp;|&nbsp; 🟡 High: 29 &nbsp;|&nbsp; ✨ Enriched: 0

---

## 1. 🔴 CISA KEV — CVE-2026-48356 — Adobe Commerce and Magento Unrestricted Upload of File with Dangerous Type Vulnerability

**CVE:** `CVE-2026-48356` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-48356>

> Vendor: Adobe | Product: Commerce and Magento. Adobe Commerce and Magento contain an unrestricted upload of file with dangerous type vulnerability that could result in arbitrary code execution in the context of the current user, potentially gaining elevated access or control over the victim&#x27;s account or session. Required action: Apply mitigations in accordance with vendor instructions, ensuri…

---

## 2. 🔴 CISA KEV — CVE-2026-111497 — Google Brotli Unchecked Return Value Vulnerability

**CVE:** `CVE-2026-111497` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-111497>

> Vendor: Google | Product: Brotli. Google Brotli contains an unchecked return value vulnerability that allows a remote unauthenticated attacker to corrupt adjacent decoder state memory, disclose sensitive memory contents, cause a denial of service, or potentially execute arbitrary code using a crafted Brotli-compressed stream. Required action: Apply mitigations in accordance with vendor instruction…

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

## 5. 🟠 Zero-Day — Strands Agents: Local Privilege Escalation via Symlink Attack in Default Session File Storage

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://github.com/advisories/GHSA-3w55-933p-8pv5>

> ## Summary

The `FileSessionManager` defaults to storing session data in `/tmp/strands/sessions/` (a world-writable directory) using predictable file paths and a write pattern (`open(path + &quot;.tmp&quot;, &quot;w&quot;)` → `os.replace()`) that follows symbolic links. A local attacker can exploit this to overwrite arbitrary files or inject malicious session data for persistent prompt injection.
…

---

## 6. 🟠 Zero-Day — CISA confirms PHP2Shell vulnerabilities now exploited in attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-confirms-php2shell-vulnerabilities-now-exploited-in-attacks/>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has added the PHP2Shell  vulnerabilities to its catalog of actively exploited security flaws and ordered federal agencies to patch their systems by Thursday. [...]

---

## 7. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

---

## 8. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

---

## 9. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

---

## 10. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

---

## 11. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 12. 🟠 Zero-Day — Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite

**CVE:** `CVE-2025-66376` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Tue, 21 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a>

> Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite Executive summary A group of Russian state-supported cyber actors has been targeting and compromising various Western government and commercial organizations using the Zimbra Collaboration Suite (ZCS) software since at least July 2025. The Russian state-supported advanced persistent threat …

---

## 13. 🟠 Zero-Day — iOS, macOS 27.2 Patch 286 Bugs; Fix for Exploited Flaw Backported to iOS 18

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://www.securityweek.com/ios-macos-27-2-patch-286-bugs-fix-for-exploited-flaw-backported-to-ios-18/>

> Apple patched 286 vulnerabilities in iOS and macOS 27.2 and brought the fix for an exploited CoreGraphics zero-day to older iPhones. The post iOS, macOS 27.2 Patch 286 Bugs; Fix for Exploited Flaw Backported to iOS 18 appeared first on SecurityWeek .

---

## 14. 🟠 Zero-Day — Apple backports CoreGraphics zero-day patches to older iPhones

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://www.bleepingcomputer.com/news/apple/apple-backports-coregraphics-zero-day-patches-to-older-iphones/>

> ​Apple has backported security patches released last month to older iPhones and iPads, addressing a zero-day bug exploited in &quot;extremely sophisticated&quot; targeted attacks on iOS devices. [...]

---

## 15. 🟠 Zero-Day — This is Fine: What NetScaler Zero-Days Tell Us About the New Normal

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://www.securityweek.com/this-is-fine-what-netscaler-zero-days-tell-us-about-the-new-normal/>

> Keep your patch management pipelines primed in case another round of Citrix NetScaler patches get released soon. The post This is Fine: What NetScaler Zero-Days Tell Us About the New Normal appeared first on SecurityWeek .

---

## 16. 🟡 High Severity — Chinese Government-linked Cyber Threat Actors Combine Automated and Hands-on Hacking Tools to Steal Sensitive Data

**CVE:** `CVE-2014-6278` | `CVE-2015-3306` | `CVE-2015-5477` | `CVE-2016-3081` | `CVE-2019-11510` | `CVE-2021-22205` | `CVE-2021-3199` | `CVE-2023-22894` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Tue, 06 Oc
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-281a>

> Advisory at a Glance Title Chinese Government-linked Cyber Threat Actors Combine Automated and Hands-on Hacking Tools to Steal Sensitive Data Original Publication October 8, 2026 Executive Summary Chinese government-linked cyber threat actors, enabled by the Integrity Technology Group, are combining automated scanning tools, large-scale botnets, and hands-on exploitation techniques to target and s…

---

## 17. 🟡 High Severity — #StopRansomware: SafePay Ransomware

**CVE:** `CVE-2020-3259` | `CVE-2023-20269` | `CVE-2023-27532` | `CVE-2024-40711` | `CVE-2024-40766` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 19 Oc
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-293a>

> Advisory at a Glance Title #StopRansomware: SafePay Ransomware Original Publication October 20, 2026 Executive Summary This advisory details recent activity by the SafePay ransomware group. SafePay actors have been highly active since August 2024, targeting businesses and critical infrastructure across North America, South America, Europe, and Australia. SafePay actors typically gain access to net…

---

## 18. 🟡 High Severity — MLflow CrewAI autologging records LLM provider API keys in logged trace spans

**CVE:** `CVE-2026-116691` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://github.com/advisories/GHSA-j7qq-vr8c-xvw3>

> ### Summary

`mlflow.crewai.autolog()` leaks CrewAI LLM provider API keys into MLflow trace telemetry.

When a CrewAI `Agent` is instrumented with MLflow autologging, MLflow serializes the agent&#x27;s `__dict__` and converts its fields to strings. The `llm` field contains the CrewAI LLM object, whose string representation includes its `api_key` in plaintext.

As a result, an application that call…

---

## 19. 🟡 High Severity — MLflow vulnerable to remote code execution on unauthenticated servers via third-party scorer deserialization importing caller-placed artifact modules

**CVE:** `CVE-2026-116692` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://github.com/advisories/GHSA-26p8-2jq9-3vq9>

> ## Summary

MLflow 3.12.0 introduced registration and deserialization support for third-party scorers in OSS MLflow. During scorer deserialization, the server accepts a request-controlled Python module path beneath one of four allowed package prefixes, imports that module, obtains a request-controlled class, and instantiates it synchronously.

An HTTP caller can combine this behavior with MLflow&#…

---

## 20. 🟡 High Severity — dd-trace: ReDOS in URL query string obfuscation

**CVE:** `CVE-2026-116693` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://github.com/advisories/GHSA-x94g-w73q-hpcw>

> ### Summary

A regular expression used to obfuscate URL query strings can consume excessive CPU when processing certain attacker-controlled input. This can stall request processing and cause denial of service in applications using affected HTTP tracing integrations.

### Details

The default query-string obfuscation pattern can exhibit excessive backtracking. The pattern is applied synchronously w…

---

## 21. 🟡 High Severity — Model Context Protocol Python SDK: Server bearer-token authentication accepts tokens issued for a different resource server

**CVE:** `CVE-2026-116684` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://github.com/advisories/GHSA-w4fh-qvv9-3v23>

> ### Summary
In affected versions, the SDK&#x27;s server-side bearer authentication had no way to check that a token was issued for your server (its audience). Where one authorization server issues tokens for several services, a valid token for another service was also accepted by your MCP server.

### Am I affected?
Yes, if your HTTP server uses the SDK&#x27;s bearer authentication (`auth=AuthSett…

---

## 22. 🟡 High Severity — Model Context Protocol Python SDK: HTTP client transports followed cross-origin redirects carrying custom headers and bodies

**CVE:** `CVE-2026-116685` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://github.com/advisories/GHSA-5h93-6whr-6q8j>

> ### Summary
In affected versions, the SDK&#x27;s Streamable HTTP and SSE client transports followed HTTP redirects to any host. If the configured MCP endpoint answered with a redirect to a different origin:

- custom headers set on the client (for example an `X-API-Key` credential) were sent to that origin, and
- on a `307` or `308` redirect the request body was re-sent there too.

The SDK&#x27;s …

---

## 23. 🟡 High Severity — Model Context Protocol Python SDK: Client fetched server-chosen $ref URLs while validating tool results against output schemas

**CVE:** `CVE-2026-116686` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://github.com/advisories/GHSA-rwrf-2pqf-9j8j>

> ### Summary
In affected versions, when a connected MCP server declared an `outputSchema` for a tool, the SDK&#x27;s client validated each `call_tool` result with `jsonschema`&#x27;s default resolver, which fetches any `$ref` it cannot resolve locally by opening the URL. A server could therefore put an `http://`, `https://` or `file://` reference in a tool&#x27;s output schema and make the client:
…

---

## 24. 🟡 High Severity — Neko: Authorization bypass in legacy WebRTC input handling

**CVE:** `CVE-2026-116679` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://github.com/advisories/GHSA-5cp7-fp4j-wwcv>

> ### Impact

When legacy mode is enabled and `session.implicit_hosting` is enabled, the legacy WebRTC data channel incorrectly authorizes input events due to a logic error in `LegacyIsHost()`.

As a result, an authenticated room member may be able to send mouse and keyboard input through the legacy WebRTC control channel even when controls are locked or the member would otherwise not be authorized …

---

## 25. 🟡 High Severity — Atlantis: OS command injection through PR-controlled Terraform workspace enables RCE during plan

**CVE:** `CVE-2026-116676` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://github.com/advisories/GHSA-rjh2-4xgw-p2hj>

> ### Summary

Atlantis passes the Terraform `workspace` value from a pull request&#x27;s `atlantis.yaml` into a shell command without quoting or escaping it.

A contributor whose pull request is eligible for an Atlantis plan can include shell metacharacters in the workspace name and execute arbitrary commands as the Atlantis service account. This does not require custom workflows, `allow_custom_wor…

---

## 26. 🟡 High Severity — FileBrowser: Symlink following escapes user scope allowing arbitrary file read outside the served directory

**CVE:** `CVE-2026-116682` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://github.com/advisories/GHSA-mgqf-5mf5-prfj>

> ## Summary

File read paths resolve symbolic links with `filepath.EvalSymlinks` and then operate on the resolved target without re-checking that the target still lies inside the user&#x27;s source/scope. 

A symlink located inside a user&#x27;s accessible directory that points outside the scope (for example to `/etc/passwd`, another tenant&#x27;s directory, SSH keys, or container secrets) is follo…

---

## 27. 🟡 High Severity — CTFer.io's CTFd Terraform Provider allows a local or remote attacker to read team passwords in state as non sensitive values

**CVE:** `CVE-2026-116683` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://github.com/advisories/GHSA-vg84-c5mg-76xh>

> ### Impact

CTFer.io&#x27;s CTFd Terraform Provider stores `ctfd_team.password` as non-sensitive values (CWE-522). A local or remote attacker, who can have access to the Terraform state, can read team passwords without the need for the state password for decryption.

### Patches

Patched in v2.8.2.

### Workarounds

No workaround exist, yet CTFer.io recommends you keep your state in safe environme…

---

## 28. 🟡 High Severity — Authlib: Unvalidated request_uri fetch in JWT-secured authorization request (JAR) leading to SSRF

**CVE:** `CVE-2026-114620` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://github.com/advisories/GHSA-x4rv-c3wx-4cr8>

> ### Summary

Authlib&#x27;s RFC 9101 (JAR) extension passes the attacker-controlled `request_uri` authorization parameter straight to the `get_request_object()` fetch hook with no validation, at a pre-authentication endpoint. Authlib already defines the pre-registration allowlist for this (`request_uris` client metadata and `require_request_uri_registration` server metadata) but the extension neve…

---

## 29. 🟡 High Severity — Authlib incomplete algorithm-confusion fix permits HMAC forgery with prefixed public keys

**CVE:** `CVE-2026-114615` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://github.com/advisories/GHSA-7vr2-2fgp-9w7p>

> ## Summary

`OctKey.import_key()` carries the only guard that stops an asymmetric public key from being used as an
HMAC secret in `authlib.jose`. That guard is `raw_key.startswith(POSSIBLE_UNSAFE_KEYS)` — anchored at
byte 0 — while the loader that consumes the identical bytes on the asymmetric path
(`cryptography.hazmat.primitives.serialization.load_pem_public_key` / `load_pem_x509_certificate`)
s…

---

## 30. 🟡 High Severity — PhpSpreadsheet: SSRF whitelist bypass via unre-validated HTTP redirect in Drawing::setPath external image loading

**CVE:** `CVE-2026-108360` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://github.com/advisories/GHSA-2phh-27fw-q4gc>

> ## Summary
PhpSpreadsheet&#x27;s `Worksheet\Drawing::setPath()` validates an external-image URL against an operator-supplied `isWhitelisted` callback **once**, on the initial URL only, then fetches it with `file_get_contents()` using a stream context that does **not** set `follow_location =&gt; 0`. A whitelisted host that returns an HTTP `302 Location:` redirect to an internal target is therefore …

---

## 31. 🟡 High Severity — PhpSpreadsheet: XmlScanner Bypass via ISO-2022 Escape Sequences Allows XXE and Denial of Service

**CVE:** `CVE-2026-108358` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://github.com/advisories/GHSA-3x94-m842-937c>

> ### Summary
PhpSpreadsheet&#x27;s `XmlScanner::scan()` uses a regex pattern that only accounts for NULL byte (0x00) interleaving when detecting `&lt;!DOCTYPE`. ISO-2022 escape sequences (0x1B bytes) inserted between the characters of the pattern break the regex match entirely, allowing DOCTYPE declarations with entity definitions to pass through undetected. This enables Denial of Service via quadr…

---

## 32. 🟡 High Severity — PhpSpreadsheet: XmlScanner Bypass via Double-Encoded unentity() TOCTOU Allows XXE and Denial of Service

**CVE:** `CVE-2026-108357` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://github.com/advisories/GHSA-rxj4-h86g-25gc>

> ### Summary
The SpreadsheetML XML reader (`Reader\Xml`) scans file content **twice** through `XmlScanner::scan()`, and each scan runs an `unentity()` callback that calls `html_entity_decode()` **after** the pattern check. By double-encoding the `&lt;` character as `&amp;#38;#60;`, the first scan decodes `&amp;#38;` to `&amp;` (forming `&amp;#60;`), and the second scan decodes `&amp;#60;` to `&lt;`…

---

## 33. 🟡 High Severity — compress zstd: Panic on two-block frames

**CVE:** `CVE-2026-116591` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://github.com/advisories/GHSA-fpmh-frq8-7rj8>

> ### Summary

A crafted ~27 KB two-block zstd frame makes DecodeAll and the streaming decoder panic with an out-of-range slice index instead of returning a decode error. The same bytes decode fine with the reference zstd. Any program that decompresses untrusted zstd input can be crashed by it. Reproduced on v1.20.0 and v1.20.1.

Released in https://github.com/klauspost/compress/releases/tag/v1.20.2…

---

## 34. 🟡 High Severity — Datadog dd-trace-py: ReDoS in URL query string obfuscation

**CVE:** `CVE-2026-116588` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://github.com/advisories/GHSA-3633-r77q-h3v3>

> ### Summary

A regular expression used to obfuscate URL query strings can consume excessive CPU when processing certain attacker-controlled input. This can stall request processing and cause denial of service in applications using affected HTTP tracing integrations.

### Details

The default query-string obfuscation pattern can exhibit excessive backtracking. The pattern is applied synchronously w…

---

## 35. 🟡 High Severity — vLLM: Request-controlled mm_processor_kwargs.code_revision allows remote code execution

**CVE:** `CVE-2026-114053` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://github.com/advisories/GHSA-h3rc-6mm3-gc2m>

> ## Summary

An untrusted multimodal request can set `mm_processor_kwargs.code_revision`. When vLLM serves a model whose Hugging Face processor uses dynamic `auto_map` code and the operator enabled `--trust-remote-code`, this request value reaches `AutoProcessor.from_pretrained` and selects the Python revision imported by Transformers.

This lets a client replace the operator-reviewed processor mod…

---

## 36. 🟡 High Severity — Flexible GraphRAG: Cypher/Graph Injection via broken string-escaping in FalkorDB adapter (_escape()) - full graph wipe from ingested-document content

**CVE:** `CVE-2026-114510` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://github.com/advisories/GHSA-vqrg-773h-4wxc>

> **Description**
def _escape(v: str) -&gt; str:
    return str(v).replace(&quot;&#x27;&quot;, &quot;\\&#x27;&quot;).replace(&quot;\\&quot;, &quot;\\\\&quot;)
The escaping order is backwards, exactly like the classic HTML double-escape bug: step 1 inserts a literal backslash in front of every &#x27;, then step 2 re-matches that just-inserted backslash and doubles it. For an input ending in a single …

---

## 37. 🟡 High Severity — LiteLLM: Privilege Escalation to Proxy Admin via Cross-Domain Reuse of the Salt Key

**CVE:** `CVE-2026-114612` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://github.com/advisories/GHSA-7hp6-4w63-5g45>

> ### Summary

An authenticated user with `internal_user` privileges can escalate to `proxy_admin` and achieve remote code execution. The proxy uses one encryption key for two purposes: sealing secrets at rest and minting session tokens. An attacker exploits this by requesting a new API key with a crafted metadata field containing a forged admin credential as the &quot;secret&quot; value. The proxy …

---

## 38. 🟡 High Severity — MessagePack: Unbounded memory leak in msgpack C extension on strict_map_key validation failure

**CVE:** `CVE-2026-114613` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://github.com/advisories/GHSA-j586-36cw-2gc2>

> ### Impact

The msgpack-python C extension (`msgpack._cmsgpack`) leaks a decoded map value when deserialization rejects a key with `strict_map_key=True` (the default). Repeated malformed inputs can cause unbounded process memory growth and denial of service in applications that deserialize attacker-controlled MessagePack data. Both `unpackb()` and the streaming `Unpacker` API are affected. The pur…

---

## 39. 🟡 High Severity — fpdf2 implicitly loads external URLs and local image paths when rendering attacker-controlled content

**CVE:** `CVE-2026-114609` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://github.com/advisories/GHSA-rw7v-4hrq-x6r9>

> ## Summary

`fpdf2` implicitly dereferences image resource references supplied to rendering APIs. If an application passes untrusted HTML, SVG, template data, or image paths into those APIs, `fpdf2` may issue outbound HTTP(S) requests or attempt to open local filesystem paths.

This behavior is relevant in applications that render untrusted or user-provided input without sanitizing or restricting …

---

## 40. 🟡 High Severity — Agno: Arbitrary code execution via `eval()` on `field_type` in `FunctionCall`

**CVE:** `CVE-2026-35002` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://github.com/advisories/GHSA-m4w4-3r8h-jw98>

> ### Impact
Agno versions prior to 2.3.24 contain an arbitrary code execution vulnerability
in the model execution component. The `field_type` parameter on a `FunctionCall`
input field was passed to Python&#x27;s built-in `eval()`, allowing an attacker who
could influence that value to execute arbitrary Python code in the Agno process.

This is a code injection flaw (CWE-95) with full impact to con…

---

## 41. 🟡 High Severity — Ajenti has potential Remote Code Execution

**CVE:** `CVE-2026-27975` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://github.com/advisories/GHSA-vcw3-r3fx-j444>

> ### Impact

An unauthenticated user could gain access to a server to execute arbitrary code on this server.

### Patches

This is fixed in the version 2.2.13. Users should upgrade to this version as soon as possible.

---

## 42. 🟡 High Severity — CVE-2026-109618: PHP-CGI Pointer Underflow → Remote Code Execution (CVSS 9.2)

**CVE:** `CVE-2026-109618` | `CVE-2019-11043` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://seclists.org/fulldisclosure/2026/Oct/38>

> Posted by jose on Oct 27 CVE-2026-109618: Pointer underflow in PHP&#x27;s CGI SAPI enables unauthenticated remote code execution. Affected: ALL PHP versions 5.x through 8.4.26 with cgi.fix_pathinfo=1 (default configuration). Same vulnerability class as CVE-2019-11043 (PHP-FPM, CVSS 9.8, patched 2019) — the CGI SAPI never received the equivalent fix. Fix: PHP 8.5.12, 8.4.27, 8.3.36, 8.2.35 (schedul…

---

## 43. 🟡 High Severity — Brotli2Shell: Frequently asked questions for Google Brotli decoder vulnerability (CVE-2026-111497)

**CVE:** `CVE-2026-111497` &nbsp;|&nbsp; **Source:** Tenable Security Research &nbsp;|&nbsp; **Published:** 2026-10-27
**Reference:** <https://www.tenable.com/blog/brotli2shell-frequently-asked-questions-for-google-brotli-decoder-cve-2026-111497>

> Researchers have demonstrated remote code execution through CVE-2026-111497, an out-of-bounds write in Google&#x27;s Brotli decoder library, and public proofs-of-concept (PoCs) are available. Software that uses the decoder includes Node.js, .NET, Bun, Envoy Proxy, Istio, Python HTTP clients and PHP for Windows. Key Takeaways CVE-2026-111497, known as Brotli2Shell and by several other names, is an …

---

## 44. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
