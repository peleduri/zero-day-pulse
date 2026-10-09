# Zero Day Pulse

> **Generated:** 2026-10-09 03:23 UTC &nbsp;|&nbsp; **Total:** 49 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 13 &nbsp;|&nbsp; 🟡 High: 36 &nbsp;|&nbsp; ✨ Enriched: 0

---

## 1. 🟠 Zero-Day — Improve Router Hygiene to Protect Against Russian State-Sponsored Targeting

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Wed, 08 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a>

> Russian Government-Sponsored Activity Targets Poorly Configured and Vulnerable Devices Across Critical Sectors Executive summary Russian Federal Security Service (FSB) Center 16 cyber actors continue to exploit poorly configured and vulnerable networking devices worldwide, opportunistically compromising multiple critical infrastructure sector networks. This joint Cybersecurity Advisory (CSA) build…

---

## 2. 🟠 Zero-Day — PraisonAI: AICoder Arbitrary File Write and Command Execution via LLM Tool Calls

**CVE:** `CVE-2026-61445` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-9mp3-24cc-77mg>

> ### Summary
The `AICoder` UI component exposes `write_to_file` and `execute_command` tools to the LLM with no path validation and no command sanitization. An attacker can achieve arbitrary file write to any location on the filesystem (including `/root/.ssh/authorized_keys`, `/etc/crontab`) and arbitrary command execution through prompt injection in the chat interface. Docker containers run as root…

---

## 3. 🟠 Zero-Day — FBI disrupts Chinese hacking tools used to breach critical infrastructure

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://www.bleepingcomputer.com/news/security/fbi-disrupts-chinese-hacking-tools-used-to-breach-critical-infrastructure/>

> The FBI has seized seven domains used by Chinese state-sponsored hackers known as Flax Typhoon to operate two hacking tools, MicroScan and FishHub, used in attacks that breached critical infrastructure and other organizations worldwide. [...]

---

## 4. 🟠 Zero-Day — PraisonAI: Prompt-injection defense blocks only when 3+ detector families fire simultaneously; realistic single-vector injections pass through unblocked

**CVE:** `CVE-2026-60086` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-4r3p-w3mc-5v34>

> ## Summary

PraisonAI&#x27;s opt-in prompt-injection defense (`enable_injection_defense()`) only blocks at `ThreatLevel.CRITICAL`, which requires three or more distinct detector families to match simultaneously. A realistic single- or double-vector prompt injection (e.g. &quot;Ignore all previous instructions…&quot;) is classified `HIGH` and passes through unmodified. The documented `HIGH` &quot;s…

---

## 5. 🟠 Zero-Day — PraisonAI: CodeAgent Executes LLM-Generated Code Without Sandboxing and Leaks All Environment Secrets

**CVE:** `CVE-2026-61447` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-2xv2-w8cq-5gxw>

> ### Summary
`CodeAgent._execute_python()` executes LLM-generated Python code in a subprocess with the complete parent-process environment (`os.environ.copy()`), zero AST validation, zero import restrictions, and no sandbox enforcement — even when `CodeConfig(sandbox=True)` is explicitly set. This allows an attacker who can influence LLM output (via prompt injection in agent input, tool results, or…

---

## 6. 🟠 Zero-Day — Inside the Exchange Inspector: How Tenable uses OpenAI GPT cyber models to review open-source AI agents

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Tenable Security Research &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://www.tenable.com/blog/tenable-openai-security-vetting-open-source-ai-agents-exchange-inspector>

> Community-built AI agents, skills, and MCP servers are landing in SOC workflows fast. Here’s what the Exchange Inspector tests before a listing earns its vetted tag on the CyberAgents Exchange. Three tools have already passed. Key takeaways Every Inspector-vetted listing clears three gates: an automated check, a frontier model assessment, and human verification. Tenable uses Tenable One AI Exposur…

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

## 13. 🟠 Zero-Day — Samsung Galaxy S26 hacked three more times at Pwn2Own Ireland

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://www.bleepingcomputer.com/news/security/samsung-galaxy-s26-hacked-three-more-times-at-pwn2own-ireland/>

> ​​​On the second day of Pwn2Own Ireland 2026, security researchers collected $232,500 in cash awards after exploiting 45 unique zero-day vulnerabilities. [...]

---

## 14. 🟡 High Severity — Chinese Government-linked Cyber Threat Actors Combine Automated and Hands-on Hacking Tools to Steal Sensitive Data

**CVE:** `CVE-2014-6278` | `CVE-2015-3306` | `CVE-2015-5477` | `CVE-2016-3081` | `CVE-2019-11510` | `CVE-2021-22205` | `CVE-2021-3199` | `CVE-2023-22894` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Tue, 06 Oc
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-281a>

> Advisory at a Glance Title Chinese Government-linked Cyber Threat Actors Combine Automated and Hands-on Hacking Tools to Steal Sensitive Data Original Publication October 8, 2026 Executive Summary Chinese government-linked cyber threat actors, enabled by the Integrity Technology Group, are combining automated scanning tools, large-scale botnets, and hands-on exploitation techniques to target and s…

---

## 15. 🟡 High Severity — Hazelcast allows arbitrary member memory access by low-privileged client

**CVE:** `CVE-2026-107726` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-6v25-8wq6-xq4j>

> ### Impact

A flaw has been found in Hazelcast Enterprise Edition and Community Edition, which would allow a low-privileged malicious client to read arbitrary data in memory from any cluster member (including Java heap memory, off-heap data, and JVM process address space). Additionally, such a client may be able to cause one or more cluster members to crash, or in some Enterprise Edition configura…

---

## 16. 🟡 High Severity — Banks: Symlink traversal and arbitrary file disclosure/overwrite in DirectoryPromptRegistry

**CVE:** `CVE-2026-107716` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-556j-vv39-8rqv>

> ### Summary
In `banks.registries.DirectoryPromptRegistry`, prompt file paths and the index file (`index.json`) do not refuse symbolic links. When a prompt directory contains or accepts untrusted files (e.g. unpacked archives, shared repositories, or multi-tenant folders), symbolic links pointing outside the registry root can be used to disclose arbitrary files via `_scan()` / `get()` or overwrite …

---

## 17. 🟡 High Severity — Indico: Incomplete Server-Side Request Forgery (SSRF) check

**CVE:** `CVE-2026-107394` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-2v95-h47v-g4x9>

> ### Impact
Indico makes outgoing requests to user-provides URLs in various places. This is mostly intentional and part of Indico&#x27;s functionality, but of course it is never intended to let you access &quot;special&quot; targets such as localhost or cloud metadata endpoints. The previous fix (CVE-2026-25738) did not cover an edge case so it was still possible to craft a URL that pointed to a lo…

---

## 18. 🟡 High Severity — Mechanize sends credential headers to another host after an HTTP redirect

**CVE:** `CVE-2026-107715` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-2mwr-xjcg-37j7>

> ## Summary

`mechanize` leaked credentials to the redirect target when an HTTP redirect crossed to another host. Credentials set through `Mechanize#request_headers=` leaked even when they were `Authorization`.

## Details

Two defects, both in `lib/mechanize/http/agent.rb`.

**1. `Mechanize#request_headers=` bypassed the redirect strip entirely.** `#request_add_headers` copied `@request_headers` o…

---

## 19. 🟡 High Severity — fast-jwt: createVerifier accepts unsigned JWTs when key is '' or null and algorithms is explicitly set

**CVE:** `CVE-2026-107720` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-8wpc-h4q6-8fxv>

> ### Summary

`createVerifier` in fast-jwt ≤ 6.3.0 skips signature verification entirely when the `key` option is a falsy synchronous value (`&#x27;&#x27;` or `null`) **and** the `algorithms` option is set to a non-empty allowlist. An attacker who can present a JWT to the application — regardless of algorithm — can forge arbitrary claims without possessing any signing key.

### Details

**Root caus…

---

## 20. 🟡 High Severity — fast-jwt: Incomplete patch of CVE-2026-34950: Non-whitespace key-prefix re-enables RSA→HS256 algorithm confusion

**CVE:** `CVE-2026-107722` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-ww5h-9m49-7xx4>

> ### Summary

The fix for CVE-2026-34950 (CVSS 9.1, released in v6.2.0) is **incomplete**. It adds `key.trim()` to the PEM-detection path in `src/crypto.js`, but `String.prototype.trim()` only strips characters classified as whitespace by the ECMAScript specification. The subsequent `^`-anchored regex (`/^-----BEGIN(?: (RSA))? PUBLIC KEY-----/`) still requires the PEM header at position 0 — so **an…

---

## 21. 🟡 High Severity — fast-jwt clockTolerance: Infinity silently bypasses both exp and nbf validation (and persists in the verifier cache)

**CVE:** `CVE-2026-107721` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-687g-22h4-j4w4>

> ## Summary

`createVerifier({ clockTolerance: Infinity })` silently bypasses both `exp` (expiry) AND `nbf` (not-before) validation. Any expired or not-yet-active token is accepted as valid. The same primitive also corrupts the verifier&#x27;s internal cache so cached entries inherit infinite validity — they remain valid past a later developer-removed Infinity config until LRU eviction.

## Vulnera…

---

## 22. 🟡 High Severity — fast-jwt : Silent claim-validator bypass when JWT payload is a JSON array

**CVE:** `CVE-2026-107723` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-5hjw-83fp-phq9>

> ### Summary
 `fast-jwt`&#x27;s `createVerifier` silently skips **all** configured claim validators (`exp`, `nbf`, `iss`, `aud`, `sub`, `jti`, `nonce`) when a validly-signed JWT carries a JSON array as its payload instead of an object. The verifier reports success while having enforced only the signature. This breaks the library&#x27;s documented `allowedIss` / `allowedAud` / `allowedSub` / expiry …

---

## 23. 🟡 High Severity — fast-jwt treats raw public JWK JSON as an HMAC secret, enabling HS256 token forgery

**CVE:** `CVE-2026-107724` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-g3jj-5cmm-3hxx>

> ### Summary

`fast-jwt` 6.2.4 silently classifies raw serialized public JWK JSON
as an HMAC secret.

If an application supplies public JWK JSON text as the verifier key and
HS256 is explicitly allowed or automatically inferred, an attacker who
knows the same public JSON text can use it as an HMAC key and create an
arbitrary HS256 token that `fast-jwt` accepts as valid.

This can result in authenti…

---

## 24. 🟡 High Severity — PraisonAI: AgentOS defaults to network-exposed no-auth mode, allowing unauthenticated agent invocation and instruction disclosure

**CVE:** `CVE-2026-61426` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-6wjp-v33h-5cvq>

> ## Summary

The AgentOS server in the `praisonai` TypeScript/npm package ships an insecure default: it binds `0.0.0.0`, sets no API key, and uses CORS `*` with credentials. The API-key middleware is only registered when an API key is configured, so the documented quickstart (`new AgentOS({agents:[...]}).serve({port})`) exposes, **unauthenticated**, `GET /api/agents` (which leaks agent names/roles/…

---

## 25. 🟡 High Severity — PraisonAI: SecurityPolicy command/path/import restrictions are completely unenforced by the default SubprocessSandbox backend

**CVE:** `CVE-2026-60085` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-5r6c-gj4g-r697>

> Summary
SecurityPolicy in praisonaiagents/sandbox/config.py is a documented configuration data class with fields for allow_subprocess, allowed_paths, blocked_paths, allowed_commands, blocked_commands, allowed_imports, and blocked_imports. Its strict() classmethod is explicitly described as creating &quot;a strict security policy for untrusted code,&quot; setting allow_subprocess=False and allow_fi…

---

## 26. 🟡 High Severity — PraisonAI: Jobs API is unauthenticated by default and allows attacker-controlled webhook SSRF

**CVE:** `CVE-2026-60091` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-4w49-gwv8-fpjg>

> ## Summary

PraisonAI&#x27;s Async Jobs API enables its API-key middleware **only when `PRAISONAI_JOBS_API_KEY` is set**, so by default every endpoint is unauthenticated. An unauthenticated `POST /api/v1/runs` accepts an attacker-controlled `webhook_url`; on job completion the server POSTs the job payload to it via `httpx`. The `webhook_url` has an SSRF validator (`gethostbyname` + private-IP chec…

---

## 27. 🟡 High Severity — music-metadata: MP4 stsd sample-entry size==0 causes a synchronous infinite loop (DoS) — unreleased regression on master

**CVE:** `CVE-2026-107391` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-f94x-6692-553q>

> ### Summary

`StsdAtom.get()` in `lib/mp4/AtomToken.ts` parses an MP4 `stsd` (sample description) box&#x27;s entry table by advancing a cursor with `off += size - 4`, where `size` is a 32-bit, attacker-controlled per-entry length read straight from the file. When `size == 0`, that advance is `0`, so a file declaring a huge `entry_count` and a first entry `size` of `0` spins forever: same bytes rea…

---

## 28. 🟡 High Severity — music-metadata: EBML parser trusts element lengths, allowing memory exhaustion or process abort

**CVE:** `CVE-2026-107389` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-5gfj-9q3v-qfp3>

> ## Summary

The Matroska/WebM EBML parser decodes attacker-controlled variable-length integer (VINT) element lengths without first validating that the declared element fits within its enclosing container or the available input. Leaf lengths are then used directly for string-token and `Uint8Array` allocations.

A very small crafted `.webm`, `.mkv`, or `.mka` file can therefore cause a disproportion…

---

## 29. 🟡 High Severity — Pydantic AI: Concurrency-limited models can keep their slot when a streamed request ends early

**CVE:** `CVE-2026-107286` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-6fqq-452j-qhrp>

> &gt; This issue was posted by Codex Desktop using gpt-6.1-sol on behalf of David.

### Summary

Applications that wrap a model with `ConcurrencyLimitedModel` or `limit_model_concurrency` can permanently lose shared concurrency capacity when a streamed request releases its slot from a different task than the one that acquired it. This can happen when a stream ends early, and also when a stream is f…

---

## 30. 🟡 High Severity — MariaDB Connector/Node.js: Uncaught exception crashes the client during ed25519 authentication with zero-configuration TLS

**CVE:** `CVE-2026-107382` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-cx2f-j9fh-8g68>

> ### Description
On the zero-configuration TLS path, the connector accepts a self-signed server certificate at the TLS level and then validates the server&#x27;s identity from the fingerprint hash the server appends to the final OK_Packet (`Authentication.validateFingerPrint`). That validation calls `hash()` on the authentication plugin in use to obtain the password-derived secret both sides combin…

---

## 31. 🟡 High Severity — PraisonAI: API deploy code generator embeds unescaped YAML fields into Python source

**CVE:** `CVE-2026-61433` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-79fv-7hq9-w7xg>

> # API deploy code generator embeds unescaped YAML fields into Python source

## Summary

PraisonAI&#x27;s API deployment generator copies `deploy.api.host` from `agents.yaml` directly into generated Python source without safe literal encoding. A malicious PraisonAI project can set that host value to a Python expression splice; when an operator runs the API deploy flow, the generated server source …

---

## 32. 🟡 High Severity — PraisonAI: Project custom command templates can read outside-workspace files into model prompts

**CVE:** `CVE-2026-60088` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-xpx6-x8c2-mw5w>

> # Project custom command templates can read outside-workspace files into model prompts

## Summary

PraisonAI&#x27;s new file-based custom command feature auto-discovers project commands from `.praisonai/commands/*.md`. When a user runs `praisonai run --command &lt;name&gt;` inside a repository, the command body is interpolated before it is sent as the model prompt.

The interpolation code expands…

---

## 33. 🟡 High Severity — Handlebars: JavaScript Injection via Own Property Check Bypass

**CVE:** `CVE-2026-106445` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-p8wg-vrv2-v86f>

> ## Summary

Handlebars can expose the `Function` constructor despite its prototype-access deny list. When a template reaches `Function.prototype`, its own `constructor` property is returned before the deny list is checked. An attacker who can render a controlled template with `allowProtoMethodsByDefault: true` can inject and execute arbitrary JavaScript, leading to Remote Code Execution on the ser…

---

## 34. 🟡 High Severity — JHipster: Generated Applications Allow Stored XSS via Unrestricted Blob ContentType Opened as Same-Origin Blob

**CVE:** `CVE-2026-107303` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-9ffp-22j7-56r2>

> ## Summary
Applications generated by generator-jhipster v9.2.0 can persist user-controlled Blob ContentType values and later use those values as the MIME type for client-side Blob objects. The shared generated `openFile` helper creates an object URL from the Blob and opens it in a new window.

For Blob-bearing entities writable by normal authenticated users, this creates a stored XSS chain: attack…

---

## 35. 🟡 High Severity — msgpack5: Quadratic parsing in the streaming decoder

**CVE:** `CVE-2026-107297` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-gcx5-hxj7-gpqq>

> ### Impact

The streaming decoder reparses an incomplete container from the beginning whenever another chunk arrives. A remote peer can split one valid MessagePack value across many small chunks, causing quadratic CPU usage and blocking the event loop.

### Patches

The decoder now preserves incremental container state so completed elements are not parsed again when more input arrives.

### Workar…

---

## 36. 🟡 High Severity — PraisonAI: PGVector and Cassandra knowledge stores interpolate vector dimensions into DDL

**CVE:** `CVE-2026-60090` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-wf65-4jjx-q444>

> # PGVector and Cassandra knowledge stores interpolate vector dimensions into DDL

## Summary

The PGVector and Cassandra knowledge-store backends validate SQL/CQL identifiers such as schema, keyspace, and collection names, but still insert the caller-controlled `dimension` argument directly into `CREATE TABLE` vector column declarations. A caller that can influence collection creation dimensions c…

---

## 37. 🟡 High Severity — Pydantic AI: Unbounded memory use when downloading remote content via web_fetch or FileUrl

**CVE:** `CVE-2026-107294` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-v2xh-2vp8-57h8>

> ### Summary

Several remote-content download paths in Pydantic AI buffered the entire HTTP response body into memory before enforcing any size limit. An application that exposes the local web-fetch tool (`web_fetch_tool`, or the `WebFetch` capability&#x27;s local fallback) to untrusted prompts can be driven to fetch an attacker-chosen URL that streams a very large body, exhausting process memory a…

---

## 38. 🟡 High Severity — AsyncHttpClient: Pooled connections can still be shared across NTLM, Negotiate and proxy logins

**CVE:** `CVE-2026-107230` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-v2j5-22fr-j62r>

> ### Impact
The fix for GHSA-vvp4-63h8-v5pm in 3.0.13 folded the authenticated principal into the HTTP/1.1 connection pool key, so that a connection one principal authenticated with NTLM, Kerberos or SPNEGO is not handed to another. It left three cases out. In each, a socket that one identity authenticated can still be drawn by a request belonging to a different identity, and the server serves that…

---

## 39. 🟡 High Severity — Pydantic AI: Event loop blocked by quadratic title extraction in `web_fetch`

**CVE:** `CVE-2026-107290` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-fpf4-vwcp-v4hp>

> ### Summary

The local web-fetch tool (`web_fetch_tool`, also used as the `WebFetch` capability&#x27;s local fallback) processed responses with several steps whose running time grows quadratically with the size of certain server-controlled inputs, and ran them on the event loop: decoding the body with whichever charset the server declared, extracting the page title with a backtracking regular expr…

---

## 40. 🟡 High Severity — Pydantic AI: SSRF cloud-metadata blocklist bypass via IPv6 zone identifiers

**CVE:** `CVE-2026-107289` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-vmxc-h2x2-jmf3>

> ### Summary

When an application using Pydantic AI opts a URL into local network access — either a `FileUrl` with `force_download=&#x27;allow-local&#x27;`, or `web_fetch_tool(allow_local_urls=True)` — the cloud-metadata blocklist could be bypassed by appending an IPv6 zone identifier to a metadata address (for example `fd00:ec2::254%251`). The host ignores the zone identifier on a destination that…

---

## 41. 🟡 High Severity — PraisonAI: Plugin Auto-Discovery Executes Arbitrary Python Files Without Verification

**CVE:** `CVE-2026-61446` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-m6wp-h223-4c8g>

> ### Summary
The plugin manager loads and executes arbitrary `.py` files from `.praisonai/plugins/` directories (both project-level and user home) via `importlib.util.spec_from_file_location()` + `exec_module()` with zero code signing, integrity verification, or sandboxing. Any attacker who can write a file to the plugins directory (via path traversal, supply chain attack, or compromised dependency…

---

## 42. 🟡 High Severity — PraisonAI: Human-in-the-loop tool approval is cached by tool name and silently reused for all subsequent calls with arbitrary arguments

**CVE:** `CVE-2026-60087` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-29r9-67vg-qj56>

> ## Summary

PraisonAI gates dangerous tools (file writes, deletes, shell/code execution) behind an interactive approval prompt. The first approval of a tool is cached for the remainder of the run and silently reused for all later invocations of that tool with arbitrary, unreviewed arguments.

## Root cause

`ApprovalRegistry.is_already_approved` (`src/praisonai-agents/praisonaiagents/approval/regi…

---

## 43. 🟡 High Severity — PraisonAI: DNS rebinding bypass in `web_crawl` SSRF protection allows internal response disclosure

**CVE:** `CVE-2026-61430` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-qg25-6gc4-48mg>

> ## Summary

PraisonAI&#x27;s `web_crawl` agent tool performs a server-side HTTP fetch of an agent/attacker-influenced URL. SSRF is meant to be prevented by `_is_safe_crawl_url()`, which resolves the hostname and rejects private/loopback/link-local IPs **at validation time**. The validated value is the URL *string* (not a pinned IP); the fetch backend then **re-resolves the hostname at connection t…

---

## 44. 🟡 High Severity — Excelize Decrypt: unrecoverable panics on malformed OLE/CFB encrypted workbooks

**CVE:** `CVE-2026-107214` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-2j4c-ffch-9f23>

> ### Summary

Any file whose first 8 bytes are the OLE compound-file signature (`D0 CF 11 E0 A1 B1 1A E1`) is routed by `OpenFile`/`OpenReader`/`OpenBytes` → `openReaderAt` → `Decrypt`. The version dispatch only guarantees `len(EncryptionInfo) &gt;= 4` before handing attacker-controlled `EncryptionInfo`/`EncryptedPackage` buffers to `standardDecrypt`/`agileDecrypt`, and no callee validates structur…

---

## 45. 🟡 High Severity — Excelize: extractPart allocates attacker-controlled, unbounded and negative-sized buffers from CFB directory entries: remote panic / OOM DoS

**CVE:** `CVE-2026-107215` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-x2q3-8cjh-766f>

> ### Summary

`extractPart` allocates directly from the mscfb directory-entry size with no clamping (`crypt.go:198`, same missing bound at `crypt.go:204`):

```go
buf := make([]byte, entry.Size)
```

`entry.Size` is the raw `streamSize` field from the attacker-controlled CFB directory entry (mscfb v1.0.8 `fixFile`, `file.go:109-120`: full uint64 → int64 for major version 4, low uint32 for v3). mscf…

---

## 46. 🟡 High Severity — Excelize ANCHORARRAY: mutually-referencing array formulas recurse unboundedly via re-entrant CalcCellValue, causing a fatal stack overflow

**CVE:** `CVE-2026-107216` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-wp2g-vpjj-g53r>

> ### Summary

`ANCHORARRAY` (calc.go:15137 on current master) evaluates each cell of the referenced spill range by calling the **exported** `CalcCellValue`, which unconditionally constructs a fresh `calcContext` — fresh entry marker, fresh iterations map, full `MaxCalcIterations` budget (calc.go:896-900). The circular-reference control only exists **within one context**: the entry-exclusion marker …

---

## 47. 🟡 High Severity — AsyncHttpClient: Cookie Domain attribute is not checked against the public suffix list, so a cookie can be set for co.uk

**CVE:** `CVE-2026-107280` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://github.com/advisories/GHSA-f9m8-cv68-674w>

> ### Impact
The cookie store decides whether a `Domain` attribute may be accepted using only the domain-matching rule of RFC 6265 Section 5.1.3, which asks whether the request host is the domain or ends with a dot followed by it. Section 5.3 step 5, which additionally requires rejecting a `Domain` that is a public suffix, is not implemented anywhere in the client.

So a host under a multi-label pub…

---

## 48. 🟡 High Severity — Attackers Target Critical Atlassian Vulnerability Within Hours of PoC Publication

**CVE:** `CVE-2026-21589` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-10-08
**Reference:** <https://www.securityweek.com/attackers-target-critical-atlassian-vulnerability-within-hours-of-poc-publication/>

> Threat actors have started targeting CVE-2026-21589, a critical vulnerability in Atlassian’s self-hosted Data Center products. The post Attackers Target Critical Atlassian Vulnerability Within Hours of PoC Publication appeared first on SecurityWeek .

---

## 49. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
