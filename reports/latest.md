# Zero Day Pulse

> **Generated:** 2026-10-01 02:48 UTC &nbsp;|&nbsp; **Total:** 29 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 15 &nbsp;|&nbsp; 🟡 High: 14 &nbsp;|&nbsp; ✨ Enriched: 0

---

## 1. 🟠 Zero-Day — Improve Router Hygiene to Protect Against Russian State-Sponsored Targeting

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Wed, 08 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a>

> Russian Government-Sponsored Activity Targets Poorly Configured and Vulnerable Devices Across Critical Sectors Executive summary Russian Federal Security Service (FSB) Center 16 cyber actors continue to exploit poorly configured and vulnerable networking devices worldwide, opportunistically compromising multiple critical infrastructure sector networks. This joint Cybersecurity Advisory (CSA) build…

---

## 2. 🟠 Zero-Day — September 2026 Patch Tuesday: Two Exploited Zero-Days and 113 Critical Vulnerabilities Among 972 CVEs

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Sep 08, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-september-2026/>

---

## 3. 🟠 Zero-Day — PyJWT.decode() reintroduces options-dict mutation, enabling silent claim-verification bypass on dict reuse

**CVE:** `CVE-2026-103001` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-30
**Reference:** <https://github.com/advisories/GHSA-gvp8-978c-rx2q>

> ### Summary

`PyJWT.decode()`/`decode_complete()` mutates a caller-supplied `options` dict in place whenever `verify_signature` is falsy, adding `verify_exp`/`verify_nbf`/`verify_iat`/`verify_aud`/`verify_iss`/`verify_sub`/`verify_jti` keys directly onto that object. If application code reuses the same `options` dict across calls (a config object, a module-level constant, a wrapper&#x27;s `self.op…

---

## 4. 🟠 Zero-Day — Cisco Warns of Attackers Exploiting Critical Authentication Bypass in SD-WAN Manager

**CVE:** `CVE-2026-76504` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-09-30
**Reference:** <https://thehackernews.com/2026/09/cisco-warns-of-attackers-exploiting.html>

> Attackers are exploiting a new critical zero-day flaw in Cisco Catalyst SD-WAN Manager, the system companies use to manage their Cisco SD-WAN networks, Cisco said in an advisory on September 30.

The flaw, CVE-2026-76504, could allow a remote attacker with no login access to use the Manager&#x27;s API as the admin user. Fixed releases are available, and there is no workaround. It carries a

---

## 5. 🟠 Zero-Day — Critical Cisco Catalyst SD-WAN Manager API authentication bypass exploited in the wild (CVE-2026-76504)

**CVE:** `CVE-2026-76504` | `CVE-2026-20127` | `CVE-2026-20182` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-09-30
**Reference:** <https://www.rapid7.com/blog/post/etr-critical-cisco-catalyst-sd-wan-manager-api-authentication-bypass-exploited-in-the-wild-cve-2026-76504>

> Overview On September 30, 2026, Cisco published a security advisory for CVE-2026-76504 , a critical API authentication bypass vulnerability affecting Cisco Catalyst SD-WAN Manager. The vulnerability has a CVSSv3.1 score of 9.8 and results from improper handling of URL encoding ( CWE-177 ). An unauthenticated, remote attacker can send a crafted HTTP request that bypasses an authentication rule for …

---

## 6. 🟠 Zero-Day — Russian APT Star Blizzard Uses ‘RedFlick’ Infection Chain in Recent Attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-09-30
**Reference:** <https://www.securityweek.com/russian-apt-star-blizzard-uses-redflick-infection-chain-in-recent-attacks/>

> The state-sponsored group has launched larger-scale phishing campaigns to deploy the CosmicPulse backdoor. The post Russian APT Star Blizzard Uses ‘RedFlick’ Infection Chain in Recent Attacks appeared first on SecurityWeek .

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

## 13. 🟠 Zero-Day — Threat Brief: NetScaler Zero Days CVE-2026-88771 and CVE-2026-88772 Exploited in the Wild (Updated September 30)

**CVE:** `CVE-2026-88771` | `CVE-2026-88772` &nbsp;|&nbsp; **Source:** Unit 42 (Palo Alto) &nbsp;|&nbsp; **Published:** 2026-09-30
**Reference:** <https://unit42.paloaltonetworks.com/netscaler-zero-days-exploited/>

> Unit 42 is aware of possible 0-day activity against NetScaler devices. Citrix reports CVE-2026-88771, CVE-2026-88772 have been exploited in the wild. The post Threat Brief: NetScaler Zero Days CVE-2026-88771 and CVE-2026-88772 Exploited in the Wild (Updated September 30) appeared first on Unit 42 .

---

## 14. 🟠 Zero-Day — DIVD says Zammad zero-days enabled AI-driven network breach

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-09-30
**Reference:** <https://www.bleepingcomputer.com/news/security/divd-says-zammad-zero-days-enabled-ai-driven-network-breach/>

> The Dutch Institute for Vulnerability Disclosure (DIVD) says that the breach of its network was possible by exploiting a chain of two zero-day vulnerabilities in the open-source Zammad ticketing system. [...]

---

## 15. 🟠 Zero-Day — Bitget hacked via zero-day in third-party security products

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-09-30
**Reference:** <https://www.bleepingcomputer.com/news/security/bitget-hacked-via-zero-day-in-third-party-security-products/>

> Cryptocurrency exchange Bitget revealed today that attackers who stole $387.5 million last week breached its systems after exploiting a zero-day flaw in third-party security products. [...]

---

## 16. 🟡 High Severity — fastify vulnerable to header validation bypass via incomplete schema case normalization

**CVE:** `CVE-2026-84428` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-30
**Reference:** <https://github.com/advisories/GHSA-9q9j-q6p8-xq58>

> ### Impact

Fastify lowercases header-schema property names before compiling the schema, because Node.js stores request header names in lowercase. That normalization was incomplete: it lowercased only top-level `properties` keys and the root `required` array, and did not lowercase the JSON Schema Draft 7 `dependencies` keyword (its trigger keys and dependent property names) or names in nested subs…

---

## 17. 🟡 High Severity — Russh: Unbounded memory exhaustion via CHANNEL_OPEN flood during a client-stalled rekey

**CVE:** `CVE-2026-102821` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-30
**Reference:** <https://github.com/advisories/GHSA-35g8-35p8-c8fw>

> ## Summary

A russh **server** can be driven to unbounded heap growth (process OOM / kill) by
a peer that speaks only standard SSH messages, in the **default configuration**.

The peer starts a key re-exchange (sends `SSH_MSG_KEXINIT`) but never sends the
follow-up `SSH_MSG_KEX_ECDH_INIT`, leaving the server&#x27;s kex state machine in
`SessionKexState::InProgress` **indefinitely**. While a rekey …

---

## 18. 🟡 High Severity — Astro: Netlify Image CDN allowlist bypass enables SSRF

**CVE:** `CVE-2026-102983` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-30
**Reference:** <https://github.com/advisories/GHSA-4233-jc72-56c5>

> ## Summary

The `@astrojs/netlify` adapter generated regular expressions for Netlify Image CDN remote-image allowlists without anchoring them to the beginning of the URL. Netlify evaluates these expressions with `RegExp.test()`, so an allowed image origin appearing anywhere in a URL, including its path or query string, could satisfy the allowlist.

For example, an application allowing `images.exam…

---

## 19. 🟡 High Severity — russh: negotiating a MAC-requiring block cipher (CTR/CBC) with mac=none causes a slice-index-out-of-range panic

**CVE:** `CVE-2026-102822` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-30
**Reference:** <https://github.com/advisories/GHSA-p8qx-h547-fjw9>

> ### Summary
`SshBlockCipher` implementations (AES-CBC, AES-CTR, 3DES-CBC, etc.) report `needs_mac() == true`, meaning they are documented/intended to always be paired with a separate integrity MAC. However, key-exchange negotiation only checks `needs_mac()` inside the *fallback* branch of MAC algorithm selection (used when no common MAC algorithm exists). If both peers&#x27; preferred MAC lists si…

---

## 20. 🟡 High Severity — Russh: Missing X25519 zero-point validation in hybrid ML-KEM key exchange

**CVE:** `CVE-2026-102824` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-30
**Reference:** <https://github.com/advisories/GHSA-w3jg-pjxf-73p4>

> ## Vulnerability

The hybrid ML-KEM 768 + X25519 key exchange implementation in `russh/src/kex/hybrid_mlkem.rs` does not validate that the remote peer&#x27;s X25519 public key is not the zero point (all-zero 32-byte value). This allows a remote peer to force the X25519 contribution to the combined shared secret to zero, reducing the hybrid KEX to a single-algorithm exchange.

Affected code at HEAD…

---

## 21. 🟡 High Severity — LiteLLM: Authenticated SSRF and provider-credential exfiltration via unvalidated request-body routing parameters

**CVE:** `CVE-2026-84377` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-30
**Reference:** <https://github.com/advisories/GHSA-3cv6-jpf6-8222>

> ### Impact

Any authenticated LiteLLM proxy user could redirect an outbound provider call to a destination they control and cause the proxy to send its own configured provider credentials to that destination. The proxy&#x27;s request-body validation was a denylist that did not cover every sensitive parameter and did not inspect parameters nested inside other request fields, so a caller could suppl…

---

## 22. 🟡 High Severity — From SELECT to SYSADMIN with SQL Copilot (CVE-2026-65669)

**CVE:** `CVE-2026-65669` &nbsp;|&nbsp; **Source:** Embrace The Red (Prompt Injection Research) &nbsp;|&nbsp; **Published:** 2026-09-30
**Reference:** <https://embracethered.com/blog/posts/2026/from-select-to-sysadmin-sql-copilot-bluehat-asia/>

> Two weeks back I presented at BlueHat Asia 2026 about my research on Microsoft’s Copilot in SSMS, the SQL Server Management Studio. This post is a write up about the talk, which covered CVE-2026-65669 , a SQL Server Elevation of Privilege Vulnerability rated critical by Microsoft. So, make sure your installations are up-to-date. The slides of the presentation can be found here . BlueHat Asia 2026 …

---

## 23. 🟡 High Severity — Attackers Exploit Zimbra Flaw to Deploy Web Shells and Harvest Authentication Secrets

**CVE:** `CVE-2026-73570` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-09-30
**Reference:** <https://thehackernews.com/2026/09/attackers-exploit-zimbra-flaw-to-deploy.html>

> Threat actors have weaponized a now-patched security flaw in Zimbra Collaboration Suite (ZCS) to deploy web shells and access mailbox data, according to findings from the Microsoft Security Research team.

The attack exploits CVE-2026-73570 (CVSS score: 8.9), an unauthenticated operating system command injection flaw that can lead to remote code execution when Simple Network Management Protocol

---

## 24. 🟡 High Severity — jackson-databind retains every unknown raw type ID 

**CVE:** `CVE-2026-91776` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-30
**Reference:** <https://github.com/advisories/GHSA-wv8q-qhhj-9h54>

> ### Summary

With `@JsonTypeInfo(use = Id.NAME, defaultImpl = ...)`, every distinct unknown
raw type ID selects the same fallback deserializer but is retained as a
separate key in `TypeDeserializerBase._deserializers`. An attacker who can
repeatedly supply new unknown type IDs can grow this process-lifetime cache
without a configured bound.

### Details

The affected path is `TypeDeserializerBase.…

---

## 25. 🟡 High Severity — Axios: Header Injection via Inherited headers After Minimal Interceptor

**CVE:** `CVE-2026-101904` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-30
**Reference:** <https://github.com/advisories/GHSA-j8rh-479h-cp32>

> ## Summary

Axios request interceptors may return a replacement config object. If an interceptor returns a plain object without an own `headers` property, `dispatchRequest()` later evaluates `config.headers` and can resolve an inherited `Object.prototype.headers` value. In a process where another vulnerability has polluted `Object.prototype.headers`, axios can send attacker-controlled headers.

Ax…

---

## 26. 🟡 High Severity — Axios: CIDR-form NO_PROXY entries are ignored, causing proxy exclusion bypass for internal IP ranges

**CVE:** `CVE-2026-101899` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-30
**Reference:** <https://github.com/advisories/GHSA-44g4-m2mj-wpvx>

> ## Summary

Axios supports proxy environment variables and evaluates `NO_PROXY` exclusions in the Node.js adapter. CIDR-form `NO_PROXY` entries such as `127.0.0.0/8`, `10.0.0.0/8`, or `169.254.169.254/32` are not interpreted as IP ranges. As a result, a request to an IP address inside a configured CIDR exclusion can still be sent through the configured proxy.

This affects deployments that rely on…

---

## 27. 🟡 High Severity — Axios: maxRedirects: 0 is not enforced by the fetch adapter, allowing redirect-based SSRF

**CVE:** `CVE-2026-101907` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-30
**Reference:** <https://github.com/advisories/GHSA-r4gj-5m52-g5wh>

> ## Summary

Axios exposes `maxRedirects` to limit redirect following, and `maxRedirects: 0` is used by applications as a redirect-based SSRF guard. The Node HTTP adapter enforces this option. The fetch adapter does not read it and does not set a Fetch API `redirect` mode, so the runtime default of `redirect: &#x27;follow&#x27;` applies.

Applications are affected when they rely on `maxRedirects: 0…

---

## 28. 🟡 High Severity — Axios: HTTP/2 adapter bypasses configured DNS lookup and proxy controls

**CVE:** `CVE-2026-101898` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-30
**Reference:** <https://github.com/advisories/GHSA-3pq3-5fj3-cg6v>

> ## Summary

Axios for Node.js does not apply configured DNS lookup or proxy controls when a request uses `httpVersion: 2`. The HTTP/1 adapter path wraps and forwards `config.lookup`, builds normal request options, and applies proxy routing through `setProxy()`. The HTTP/2 path builds a session with `http2.connect()` using only `options.http2Options`, which drops the top-level `lookup`, `agent`, an…

---

## 29. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
