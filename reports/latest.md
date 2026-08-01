# Zero Day Pulse

> **Generated:** 2026-08-01 01:30 UTC &nbsp;|&nbsp; **Total:** 26 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 9 &nbsp;|&nbsp; 🟡 High: 17 &nbsp;|&nbsp; ✨ Enriched: 0

---

## 1. 🟠 Zero-Day — Improve Router Hygiene to Protect Against Russian State-Sponsored Targeting

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Wed, 08 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a>

> Russian Government-Sponsored Activity Targets Poorly Configured and Vulnerable Devices Across Critical Sectors Executive summary Russian Federal Security Service (FSB) Center 16 cyber actors continue to exploit poorly configured and vulnerable networking devices worldwide, opportunistically compromising multiple critical infrastructure sector networks. This joint Cybersecurity Advisory (CSA) build…

---

## 2. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 8. 🟠 Zero-Day — Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite

**CVE:** `CVE-2025-66376` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Tue, 21 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a>

> Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite Executive summary A group of Russian state-supported cyber actors has been targeting and compromising various Western government and commercial organizations using the Zimbra Collaboration Suite (ZCS) software since at least July 2025. The Russian state-supported advanced persistent threat …

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

---

## 10. 🟡 High Severity — WPGraphQL has deprecated `user` field on SendPasswordResetEmailPayload that leaks user existence + profile (defeats explicit anti-enumeration design)

**CVE:** `CVE-2026-54768` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-31
**Reference:** <https://github.com/advisories/GHSA-jhh7-832h-f8hv>

> ## Summary

The `sendPasswordResetEmail` mutation in WPGraphQL is explicitly designed to prevent user enumeration. The resolver in `src/Mutation/SendPasswordResetEmail.php` states in a code comment:

`// We obsfucate the actual success of this mutation to prevent user enumeration.`

The mutation always returns `success: true` regardless of whether the supplied username/email belongs to an existing…

---

## 11. 🟡 High Severity — sigstore-go fails to check signature timestamps against a signing key's validity period

**CVE:** `CVE-2026-54787` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-31
**Reference:** <https://github.com/advisories/GHSA-wqqc-jjcq-vfxm>

> sigstore-go fails to check signature timestamps against a signing key&#x27;s validity period for self-managed long-lived keys without certificates.

## Impact

To verify a bundle with a self-managed long-lived key, the key needs to be wrapped in an `ExpiringKey` type that implies expiration semantics:

```go
signatureVerifier, _ := signature.LoadDefaultVerifier(publicKey)
expiredKey := root.NewExp…

---

## 12. 🟡 High Severity — @apostrophecms/file pretty-URL Vulnerable to Unauthenticated SSRF via Host header

**CVE:** `CVE-2026-53607` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-31
**Reference:** <https://github.com/advisories/GHSA-34pj-2622-jvxq>

> ### Summary

When `prettyUrls: true` is enabled on `@apostrophecms/file` (a documented SEO
feature for serving uploaded files at clean URLs), the public pretty-URL
handler builds the upstream URL using the raw `Host` HTTP request header:

```js
proxyUrl = `${req.protocol}://${req.get(&#x27;host&#x27;)}${uglyUrl}`
```

That URL is then `fetch`&#x27;ed and the response body + headers are streamed
st…

---

## 13. 🟡 High Severity — Thumbor treats ALLOWED_SOURCES string patterns as unescaped regex, allowing hostname bypass via wildcard dot

**CVE:** `CVE-2026-53500` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-31
**Reference:** <https://github.com/advisories/GHSA-6x26-6r6f-m537>

> ## Summary

The `ALLOWED_SOURCES` configuration is meant to restrict which hosts Thumbor&#x27;s HTTP loader may fetch images from. Plain-string entries in that list (the overwhelming majority of real-world and documented configurations) are passed directly to `re.match()` without escaping. Because `.` is a regex wildcard, every dot in a domain name becomes a bypass vector: `s.glbimg.com` silently …

---

## 14. 🟡 High Severity — vault-addr annotation SSRF -- webhook makes outbound HTTP call to attacker URL during admission; vault-serviceaccount enables cluster-wide SA token theft via TokenRequest API

**CVE:** `CVE-2026-54725` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-31
**Reference:** <https://github.com/advisories/GHSA-r2v3-8gwf-7ghm>

> ## Summary

The vault-secrets-webhook reads the `vault.security.banzaicloud.io/vault-addr` annotation from any ConfigMap or Secret being admitted and uses it as the Vault server address without any validation or allowlist. When a ConfigMap or Secret contains a value prefixed with `vault:`, the webhook&#x27;s admission handler synchronously calls the Vault API at the attacker-supplied address from …

---

## 15. 🟡 High Severity — hashi-vault-js has a path traversal and query parameter injection

**CVE:** `CVE-2026-55100` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-31
**Reference:** <https://github.com/advisories/GHSA-g956-2f74-rmv7>

> ## Summary

The `hashi-vault-js` library is vulnerable to path traversal and query string injection due to the lack of proper encoding of identifiers in path segments and query strings. This allows attackers to manipulate the request URL and potentially access unintended downstream endpoints or inject malicious parameters if untrusted input is passed to the library.

## Details

There are zero cal…

---

## 16. 🟡 High Severity — dssrf: any users using 1.1.1.1 DNS is impacted by SSRF

**CVE:** `CVE-2026-54729` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-31
**Reference:** <https://github.com/advisories/GHSA-5846-7qm3-r52j>

> ## Summary

is_url_safe can treat localhost as safe when DNS resolver 1.1.1.1 returns NXDOMAIN because dns.resolve4 yields no address and no dns.lookup fallback occurs, allowing server-side request forgery.

## POC

Example to simulate 1.1.1.1 in version before 1.5.0 of dssrf:

```js
import { is_url_safe } from &#x27;../dist/helpers.js&#x27;;
import dns from &#x27;dns&#x27;;


dns.setServers([&#x2…

---

## 17. 🟡 High Severity — Capsule has an incomplete fix of CVE-2026-22872: TenantResource RawItems and Generators still allow cluster-scoped resource creation (cross-tenant privilege escalation)

**CVE:** `CVE-2026-65835` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-31
**Reference:** <https://github.com/advisories/GHSA-jr6p-8pjj-mfx6>

> ### Summary
CVE-2026-22872 (GHSA-qjjm-7j9w-pw72) reported that a Tenant Owner could create cluster-scoped resources
(e.g. `ClusterRole`, `ValidatingWebhookConfiguration`) through a `TenantResource`, because the controller
applies them with its cluster-admin ServiceAccount and `SetNamespace` is ineffective for cluster-scoped
kinds. The v0.13.0 fix added a cluster-scope rejection guard, but **only o…

---

## 18. 🟡 High Severity — re2: Global `String.prototype.match` with an empty-matchable pattern never advances → infinite loop with unbounded native memory growth (DoS)

**CVE:** `CVE-2026-68499` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-31
**Reference:** <https://github.com/advisories/GHSA-6hxr-mr5r-9836>

> ## Summary

`String.prototype.match` with a **global** `RE2` collects all matches in a native loop that advances the cursor by the match length. A **zero-width (empty) match** has length 0, so the cursor never advances: the same empty match is found forever and appended to an ever-growing native vector. Any pattern that can match the empty string (`a*`, `b?`, `x{0,3}`, `(a)|`, `(?:)`, …) therefore…

---

## 19. 🟡 High Severity — Sylius Mollie Plugin has unauthenticated IDOR that leaks order token and customer PII

**CVE:** `CVE-2026-68501` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-31
**Reference:** <https://github.com/advisories/GHSA-x83g-979r-f5fh>

> ### Impact
Two unauthenticated Mollie shop endpoints look up orders by a sequential integer `orderId`
with no ownership or session check. Chained, they expose customer PII.

`GET /{_locale}/thank-you` (`PageRedirectController::thankYouAction`, route
`sylius_mollie_shop_thank_you_page_redirect`) loads the order with `findOneBy([&#x27;id&#x27; =&gt; $orderId])`
and returns a `302` whose `Location` h…

---

## 20. 🟡 High Severity — Sylius Mollie Plugin vulnerable to payment status forgery via the payment webhook

**CVE:** `CVE-2026-68500` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-31
**Reference:** <https://github.com/advisories/GHSA-rc52-c4hv-w89p>

> ### Impact
  The shop payment webhook `POST /{_locale}/update-payment` (route
  `sylius_mollie_shop_payment_webhook`) accepts two independent, attacker-controlled
  parameters: `id` (the Mollie payment ID, verified against Mollie&#x27;s API) and `orderId` (the
  Sylius order ID, read directly from the database). The handler never verifies that the
  Mollie payment belongs to the referenced order.
…

---

## 21. 🟡 High Severity — Netty: HTTP/2 decompression leaks ByteBuf reference count when the decompressor channel is already closed (Direct memory leak / OOM DoS)

**CVE:** `CVE-2026-56819` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-31
**Reference:** <https://github.com/advisories/GHSA-93wv-jw9v-4972>

> ### Summary

A remote, unauthenticated peer can leak one direct `ByteBuf` per HTTP/2 `DATA` frame in
applications that enable HTTP/2 content decompression via `DelegatingDecompressorFrameListener`.
When a `DATA` frame is processed for a stream whose decompressor has already been closed,
`Http2Decompressor.decompress(...)` retains the frame buffer but never releases it on the error
path, so its ref…

---

## 22. 🟡 High Severity — Natural Language Toolkit (NLTK): DNS-rebinding SSRF filter bypass in nltk.pathsec.urlopen (nltk.download / nltk.data.load) defeats ENFORCE mode

**CVE:** `CVE-2026-12075` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-31
**Reference:** <https://github.com/advisories/GHSA-qvv7-cg9c-w4x3>

> ### Summary
`nltk.pathsec` provides an SSRF filter that NLTK documents as a security control, blocking loopback, private, link-local, and multicast ranges (including obfuscated forms) and recommending strict `ENFORCE` mode for security-sensitive environments. The filter is bypassable by DNS rebinding: `validate_network_url()` resolves the hostname and checks the resulting IP, but the actual HTTP c…

---

## 23. 🟡 High Severity — Natural Language Toolkit (NLTK) has path traversal in FramenetCorpusReader.frame() that allows arbitrary XML file read, bypassing the nltk.pathsec sandbox (ENFORCE=True)

**CVE:** `CVE-2026-12074` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-31
**Reference:** <https://github.com/advisories/GHSA-xh95-f55m-82fw>

> ### Summary
`FramenetCorpusReader.frame(name)` interpolates a caller-supplied frame name into an XML file path that is read with the builtin `open()`, bypassing `CorpusReader.open()` and the `nltk.pathsec` sandbox — including strict `ENFORCE=True` mode. A `../` sequence in the name escapes the corpus root, yielding an arbitrary XML file read whose parsed content is returned to the caller.


### De…

---

## 24. 🟡 High Severity — Wings exposes node configuration secrets through egg configuration-file templating

**CVE:** `CVE-2026-52855` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-31
**Reference:** <https://github.com/advisories/GHSA-pfvc-3p5h-x7h6>

> ### Impact

**Type:** Exposure of sensitive information / insufficiently protected credentials
leading to privilege escalation and full node compromise.

Wings exposes its **entire** daemon configuration to the egg configuration-file
templating engine. When Wings renders a server&#x27;s configuration files, any
`{{config.&lt;path&gt;}}` placeholder in a replacement value is resolved against the
fu…

---

## 25. 🟡 High Severity — Critical Code Execution Vulnerability Patched in TeamCity

**CVE:** `CVE-2026-63077` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-31
**Reference:** <https://www.securityweek.com/critical-code-execution-vulnerability-patched-in-teamcity/>

> Tracked as CVE-2026-63077, the security defect can be exploited without authentication via the agent polling protocol. The post Critical Code Execution Vulnerability Patched in TeamCity appeared first on SecurityWeek .

---

## 26. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
