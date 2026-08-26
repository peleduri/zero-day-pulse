# Zero Day Pulse

> **Generated:** 2026-08-26 06:26 UTC &nbsp;|&nbsp; **Total:** 41 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 18 &nbsp;|&nbsp; 🟡 High: 23 &nbsp;|&nbsp; ✨ Enriched: 0

---

## 1. 🟠 Zero-Day — Improve Router Hygiene to Protect Against Russian State-Sponsored Targeting

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Wed, 08 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a>

> Russian Government-Sponsored Activity Targets Poorly Configured and Vulnerable Devices Across Critical Sectors Executive summary Russian Federal Security Service (FSB) Center 16 cyber actors continue to exploit poorly configured and vulnerable networking devices worldwide, opportunistically compromising multiple critical infrastructure sector networks. This joint Cybersecurity Advisory (CSA) build…

---

## 2. 🟠 Zero-Day — August 2026 Patch Tuesday: One Exploited Zero-Day and 62 Critical Vulnerabilities Among 415 CVEs

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Aug 11, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-august-2026/>

---

## 3. 🟠 Zero-Day — PraisonAI: Origin-validation bypass (startswith prefix match) enables unauthenticated cross-site request forgery against the PraisonAI MCP HTTP server

**CVE:** `CVE-2026-55532` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-pvph-5j39-v8qc>

> ### Summary

The PraisonAI MCP server exposes an HTTP-stream transport (praisonai mcp serve --transport http-stream) that binds to localhost and, by default, has no API key. Its only access control for browser-originated requests is an Origin allowlist, which the code implements as required by the MCP 2025-11-25 security guidance. The allowlist check uses a prefix match (request_origin.startswith(…

---

## 4. 🟠 Zero-Day — PraisonAI: [Auth Bypass] PraisonAI async Jobs API (`/api/v1/runs`) has no authentication — unauthenticated job execution, result theft, cancel and delete

**CVE:** `CVE-2026-55539` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-2jgc-f764-c5r2>

> ### Summary
PraisonAI&#x27;s async **Jobs API** (the FastAPI service in `praisonai/jobs/`) installs its router with no authentication middleware, no router-level dependency, and no per-route auth check. Any caller who can reach the jobs server can submit agent jobs (executed against the operator&#x27;s configured LLM credentials), list every job in the shared store, read other jobs&#x27; results, …

---

## 5. 🟠 Zero-Day — praisonaiagents vulnerable to SSRF in web_crawl tool via redirect-following and DNS rebinding (validate-then-fetch gap)

**CVE:** `CVE-2026-55524` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-vg6p-v9vm-6fgj>

> The web_crawl tool performs its SSRF check only on the initial URL: it resolves the hostname once
with socket.gethostbyname and rejects private/loopback/link-local results. It then passes the URL to
a fetcher that uses httpx.Client(follow_redirects=True) - or urllib.request.urlopen when httpx is
absent, which also follows redirects - and re-resolves the hostname at connect time, with no further
va…

---

## 6. 🟠 Zero-Day — praisonaiagents has a `web_crawl` SSRF protection bypass via unchecked redirect targets

**CVE:** `CVE-2026-55523` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-8hjw-25cg-g52h>

> ## Summary

`praisonaiagents.tools.web_crawl_tools.web_crawl()` validates the initial URL and blocks direct loopback/private destinations by default, but the default httpx fallback still uses `httpx.Client(follow_redirects=True)` and does not revalidate redirect targets.

An attacker-controlled public URL can pass the initial host check, redirect to loopback/private/cloud metadata infrastructure, …

---

## 7. 🟠 Zero-Day — praisonaiagents web_crawl vulnerable to SSRF via redirect-following

**CVE:** `CVE-2026-55525` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-5r34-2g38-6569>

> ### Summary
`web_crawl` (an exported, model-callable tool) validates only the INITIAL URL&#x27;s resolved IP against a private/loopback blocklist, then fetches with `httpx.Client(follow_redirects=True)` and never re-validates redirect targets. 

An attacker who controls the agent&#x27;s crawl target (a malicious task, or prompt injection inside any page the agent already crawls) supplies a public …

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

## 14. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

---

## 15. 🟠 Zero-Day — browse-mcp has an arbitrary file write via unconfined download and state paths

**CVE:** `CVE-2026-55557` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-m9mq-7m7q-xc6p>

> ### Impact
`browser_download` wrote a fetched file to `join(save_dir, filename)` with no validation of `save_dir`, and `browser_save_state` / `browser_load_state` honored an explicit `path` unchanged. The MCP caller controls these arguments (a malicious MCP client, or an autonomous agent steered by indirect prompt injection on a visited page), so an attacker could supply an arbitrary `save_dir` (o…

---

## 16. 🟠 Zero-Day — mcp-shell — Security Disabled by Default in Bare-Binary Deploy Path + Shell Interpreter in Secure-Mode Allowlist

**CVE:** `CVE-2026-55580` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-f5pj-2738-996m>

> mcp-shell` at commit `17ac0eef5c9a5a42b8fb132d3d034973d55a5433` has two issues that together mean neither the default deploy path nor the recommended &quot;secure mode&quot; delivers the restriction they&#x27;re marketed as providing. Filing these together because the two failure modes bracket the full intended audience — the from-source path gets users who skip security config entirely, the Docke…

---

## 17. 🟠 Zero-Day — PraisonAI has a Browser Server WebSocket origin validation bypass via unanchored regex (patch bypass of CVE-2026-40289 / GHSA-8x8f-54wf-vv92)

**CVE:** `CVE-2026-55536` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-6g6r-q6gw-w8fg>

> ### Summary

`praisonai/browser/server.py` validates incoming WebSocket connections using a Chrome
extension Origin check. The regex `chrome-extension://[a-z0-9]{32}` is applied with
`re.match()`, which **only anchors at the start of the string, not the end**. Any Origin
header with more than 32 alphanumeric characters after `chrome-extension://` — including
non-alphanumeric trailing characters — …

---

## 18. 🟠 Zero-Day — PraisonAI: [Path Traversal] agent tools escape the configured workspace via symlinks

**CVE:** `CVE-2026-55540` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-ch89-h4r2-c8f8>

> ### Summary
PraisonAI&#x27;s `praisonai.code` tool wrappers (exported as `CODE_TOOLS` for agents) expose a `workspace` setting that the module itself treats as a path-traversal **security boundary** — `read_file`, `write_file`, `apply_diff`, and `search_replace` explicitly call `is_path_within_directory()` and return `&quot;… is outside the workspace&quot;` on violations. That boundary is enforced…

---

## 19. 🟡 High Severity — CISA Warns of Exploited Gitea Vulnerability

**CVE:** `CVE-2026-60004` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-08-26
**Reference:** <https://www.securityweek.com/cisa-warns-of-exploited-gitea-vulnerability/>

> CVE-2026-60004 is a remote code execution vulnerability patched by Gitea developers in late July with the release of version 1.27.1. The post CISA Warns of Exploited Gitea Vulnerability appeared first on SecurityWeek .

---

## 20. 🟡 High Severity — JupyterHub has Unauthenticated Denial of Service via Unbounded Username Logging on Failed Login

**CVE:** `CVE-2026-54338` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-p43p-whwx-q52h>

> ### Impact

Invalid input to login resulted in unbounded logging output. Only form-based Authenticators (the default PAM Authenticator, but not the more widely used OAuthenticator) are affected.

### Patches

Upgrade to 5.5.0.

### Workarounds

Use an Authenticator that doesn&#x27;t use a login form, such as OAuthenticator.

---

## 21. 🟡 High Severity — Chainlist has SSRF via MCP SSE and streamable-http transports that allows unauthenticated internal network access

**CVE:** `CVE-2026-45019` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-hvfh-5mj3-5f3j>

> ### Am I affected?

Only if your deployment sets `features.mcp.enabled = true` in `.chainlit/config.toml`. **MCP has been disabled by default since v2.7.0**, so most Chainlit deployments are not affected. No authentication is required: `/mcp` is reachable by any client that can open a session.

### Summary

When MCP is enabled (`features.mcp.enabled = true`), the `POST /mcp` endpoint for `sse` and…

---

## 22. 🟡 High Severity — Chainlit has command injection via MCP stdio transport that allows unauthenticated remote code execution

**CVE:** `CVE-2026-45018` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-w3fx-mc44-mf6j>

> ### Am I affected?

Only if your deployment sets `features.mcp.enabled = true` in `.chainlit/config.toml`. **MCP has been disabled by default since v2.7.0**, so most Chainlit deployments are not affected. No authentication is required: `/mcp` is reachable by any client that can open a session.

### Summary

When MCP is enabled (`features.mcp.enabled = true`), the `POST /mcp` endpoint for `stdio` t…

---

## 23. 🟡 High Severity — consciousness-explorer / sublinear-time-solver MCP export_state has an arbitrary file write

**CVE:** `CVE-2026-55609` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-xc9g-j69q-37xw>

> ### Impact
An arbitrary file write vulnerability (CWE-73, External Control of File Name or Path) exists in the `consciousness-explorer` component of `sublinear-time-solver`. The MCP `export_state` (and `import_state`) tool accepted a user-supplied `filepath` argument and passed it directly to `fs.writeFileSync` / `fs.readFileSync` without constraining the destination or rejecting path traversal. A…

---

## 24. 🟡 High Severity — mediasoup: SCTP state cookie lacks cryptographic authentication, enabling unauthorized association establishment (RFC 9260 violation)

**CVE:** `CVE-2026-55663` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-p7x2-g5cq-fhmq>

> ### Summary

mediasoup&#x27;s built-in SCTP stack (introduced in v3.20.0) authenticates SCTP state cookies using only hardcoded magic byte sequences rather than a per-instance HMAC keyed with a secret, violating RFC 9260 Section 5.1.3. An on-path attacker targeting a PlainTransport with SCTP enabled (and no SRTP/DTLS protection) can craft a forged COOKIE-ECHO chunk that passes all validation, esta…

---

## 25. 🟡 High Severity — gRPC Erlang package's path bindings are overridable by query string and request body

**CVE:** `CVE-2026-48599` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-mwr4-5g34-j5cq>

> ### Summary

In the HTTP-to-gRPC transcoding layer of the `grpc` Hex package, query-string and request-body parameters can silently overwrite path-bound fields when building the decoded protobuf request struct. An authenticated attacker who can reach a transcoded endpoint can substitute any path-bound identifier (e.g. `user_id` from `/users/{user_id}/profile`) with an arbitrary value, bypassing au…

---

## 26. 🟡 High Severity — gRPC Erlang package vulnerable to Remote Code Execution with attacker-controlled gRPC payloads

**CVE:** `CVE-2026-48853` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-grp7-v8xh-rj7h>

> ### Summary

`GRPC.Codec.Erlpack.decode/2` calls `:erlang.binary_to_term/1` directly on the raw gRPC message body without the `:safe` option. Any unauthenticated peer that can reach a gRPC endpoint with `Content-Type: application/grpc+erlpack` can crash the entire BEAM node via atom table exhaustion or, if a decoded fun term flows into a call site that invokes it, achieve remote code execution ins…

---

## 27. 🟡 High Severity — genieacs-mcp: DNS rebinding reaches local GenieACS MCP Streamable HTTP transport

**CVE:** `CVE-2026-55637` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-cmwv-wf9p-p8wx>

> `genieacs-mcp` exposes a local Streamable HTTP MCP endpoint that accepts attacker-controlled `Host` and `Origin` headers. A malicious web page can use DNS rebinding to route browser requests to a victim&#x27;s loopback MCP listener while preserving the attacker origin. The server accepts the request, initializes an MCP session, lists GenieACS tools, and can invoke tools against the configured Geni…

---

## 28. 🟡 High Severity — qwed Vulnerable to Authenticated Remote Code Execution via Unsafe SymPy `parse_expr()`

**CVE:** `CVE-2026-55585` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-q27q-98j4-9pfv>

> ### Summary

The `qwed` package (version 5.1.1) passes attacker-controlled input directly to SymPy&#x27;s `parse_expr()` function without a restricted namespace. Because `parse_expr()` internally calls Python&#x27;s `eval()`, any authenticated tenant can execute arbitrary Python code inside the API server process. The attack requires only a standard user account, which is freely obtainable through…

---

## 29. 🟡 High Severity — Echo: Encoded slash (%2F) bypasses route-level protection and exposes static files

**CVE:** `CVE-2026-55677` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-vfp3-v2gw-7wfq>

> ### Summary

Echo&#x27;s router and static file handler disagree on URL path decoding. The router matches routes using the raw encoded path (preserving `%2F` as-is), while `StaticDirectoryHandler` unescapes `%2F` to `/` before resolving filesystem paths. This allows an attacker to bypass route-level access controls and read static files without authorization.

### Details

**Root cause 1 — `router…

---

## 30. 🟡 High Severity — nextcloud-mcp-server: Unauthenticated `POST /webhooks/nextcloud` allows arbitrary vector data deletion when `WEBHOOK_SECRET` is unset ( default )

**CVE:** `CVE-2026-55640` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-8vh3-g2qg-2h2c>

> ## Summary
The `POST /webhooks/nextcloud` endpoint has no authentication by default: `WEBHOOK_SECRET` defaults to `None` and is never required by startup validation. When unset, the receiver accepts any unauthenticated POST. The `user_id` is taken directly from the attacker-supplied payload and passed to Qdrant, allowing an unauthenticated attacker to delete or corrupt vector embeddings for any us…

---

## 31. 🟡 High Severity — utcp-gql SSRF: CVE-2026-44661 fix not applied to the GraphQL and WebSocket plugins

**CVE:** `CVE-2026-12210` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-ppx3-28rw-8fpf>

> ### Summary

The fix for CVE-2026-44661 (commit `5b16e43`) added the `ensure_secure_url()` / `is_secure_url()` helpers and wired them into the three HTTP-family plugins, but it did not reach the GraphQL or WebSocket plugins. The GraphQL plugin (`utcp-gql`) still uses the `startswith` prefix check that the fix explicitly replaced, so `http://127.0.0.1.attacker.example` and `http://localhost.evil.co…

---

## 32. 🟡 High Severity — qwed-mcp has Unsafe SymPy `parse_expr()` Remote Code Execution via Unsanitized Math Expression Input

**CVE:** `CVE-2026-55546` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-mw6r-2hvm-4rp2>

> ### Summary

`verify_math_expression()` in `qwed-mcp` v0.2.0 passes attacker-controlled strings directly to SymPy&#x27;s `parse_expr()` without restricting `global_dict` or validating the expression&#x27;s AST. Because `parse_expr()` internally calls `eval()` and Python automatically injects the current module&#x27;s `__builtins__` when no explicit restriction is set, an attacker can embed arbitra…

---

## 33. 🟡 High Severity — PraisonAI: Authentication fail-open in Recipe server allows unauthenticated access when API key or JWT auth is configured without a secret

**CVE:** `CVE-2026-55533` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-gfq8-hmph-9gjv>

> ### Summary

The PraisonAI Recipe HTTP server silently allows unauthenticated requests when `auth` is configured as `api-key` or `jwt` but the corresponding secret is missing.

This creates an authentication fail-open condition. An operator can start the Recipe server with authentication enabled, including on a non-localhost interface, but the server still accepts unauthenticated requests if no AP…

---

## 34. 🟡 High Severity — PraisonAI vulnerable to Server-Side Request Forgery via DNS rebinding bypass in webhook_url validation

**CVE:** `CVE-2026-55535` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-hmfx-4v44-9qw9>

> ### Summary
The `webhook_url` field in the Jobs API silently passes validation when DNS resolution fails (`socket.gaierror`), enabling DNS rebinding attacks. An attacker&#x27;s domain can initially resolve to a public IP (passing validation) then switch to an internal IP before the server makes the HTTP request.

### Details
The validator catches `socket.gaierror` and silently allows the URL:

```…

---

## 35. 🟡 High Severity — PraisonAI: Webhook SSRF via DNS fail-open in `JobSubmitRequest.validate_webhook_url()` — bypass of CVE-2026-40114

**CVE:** `CVE-2026-55537` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-rg5q-pp8p-f7jm>

> ### Summary

`praisonai/jobs/models.py::JobSubmitRequest.validate_webhook_url()` validates webhook
URLs by resolving the hostname and checking whether the IP is private. When DNS
resolution fails (`socket.gaierror`), the validator **silently passes** the URL via
`except socket.gaierror: pass`. Additionally, even when DNS succeeds at validation time,
the webhook is fired much later by `JobExecutor.…

---

## 36. 🟡 High Severity — praisonaiagents: ast_grep_rewrite rewrites arbitrary files without the @require_approval gate enforced on every sibling mutation tool

**CVE:** `CVE-2026-55530` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-cfxv-8fw8-rwpv>

> **Target:** PraisonAI (`MervinPraison/PraisonAI`)
**Affected component:** `praisonaiagents/tools/ast_grep_tool.py` — `ast_grep_rewrite`
**Affected versions:** master at `ce97667156a116c50b4a3d1aa21e09f048903fda`; reproduced against the current `praisonaiagents` PyPI release (`praisonaiagents` &lt;= 1.6.52).

## Summary

Tools in `praisonaiagents/tools/` that modify on-disk state or run code are un…

---

## 37. 🟡 High Severity — praisonaiagents has an SSRF protection bypass in `spider_tools._host_is_blocked()` via DNS-resolved hostnames (`127.0.0.1.nip.io`)

**CVE:** `CVE-2026-55526` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-x44h-65qv-cw74>

> ### Summary

`praisonaiagents/tools/spider_tools.py` contains an SSRF protection bypass. The function
`_host_is_blocked()` validates URLs against a list of blocked IP literals and hostname
aliases, but **never performs DNS resolution**. Any hostname that resolves to a private or
loopback IP address — including public wildcard DNS services like `127.0.0.1.nip.io` —
bypasses the protection entirely.…

---

## 38. 🟡 High Severity — PraisonAI MCP HTTP server has unauthenticated unbounded session accumulation (memory exhaustion; session TTL never enforced)

**CVE:** `CVE-2026-55531` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-wv94-5qcp-6m36>

> ### Summary

The PraisonAI MCP HTTP-stream server creates a new in-memory session on every initialize request and never removes it. The cleanup routine that would expire sessions (_cleanup_sessions) is defined but never called anywhere in the codebase, and the configured session TTL is never enforced. There is no cap on the number of sessions. Because initialize requires no authentication and the …

---

## 39. 🟡 High Severity — PraisonAI has an origin validation bypass in MCP HTTP Stream transport that allows browser-mediated unauthenticated tool execution on local MCP server

**CVE:** `CVE-2026-55529` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://github.com/advisories/GHSA-wj6g-v78p-6fx3>

> ### Summary

PraisonAI&#x27;s MCP HTTP Stream transport uses an unsafe prefix match when validating the `Origin` header. The default localhost allowlist includes origins such as `http://localhost`, and the validation accepts any origin that starts with an allowed value.

As a result, an attacker-controlled origin such as `http://localhost.evil.example` passes the localhost origin check.

When the …

---

## 40. 🟡 High Severity — Attackers Target miniOrange SAML Flaws That Can Grant WordPress Admin Access

**CVE:** `CVE-2026-61979` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-08-25
**Reference:** <https://thehackernews.com/2026/08/attackers-target-miniorange-saml-flaws.html>

> Bad actors are attempting to exploit two severe unauthenticated authentication bypasses in the Xecurify miniOrange SAML 2.0 Single Sign On plugin that make it possible for an attacker to sign in as any WordPress user, including administrators.

The vulnerabilities, as disclosed by Patchstack, are listed below -


  CVE-2026-61979 (CVSS score: 8.1) - An unauthenticated privilege escalation

---

## 41. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
