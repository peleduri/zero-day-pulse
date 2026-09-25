# Zero Day Pulse

> **Generated:** 2026-09-25 16:02 UTC &nbsp;|&nbsp; **Total:** 29 &nbsp;|&nbsp; 🔴 KEV: 2 &nbsp;|&nbsp; 🟠 Zero-Day: 11 &nbsp;|&nbsp; 🟡 High: 16 &nbsp;|&nbsp; ✨ Enriched: 0

---

## 1. 🔴 CISA KEV — CVE-2026-67279 — Mikrotik RouterOS Improper Enforcement of Behavioral Workflow Vulnerability

**CVE:** `CVE-2026-67279` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-09-25
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-67279>

> Vendor: MikroTik | Product: RouterOS. Mikrotik RouterOS contains an improper enforcement of behavioral workflow vulnerability that could allow an unauthenticated client to open a session channel and send an exec request. This vulnerability can be chained to achieve unauthenticated exploitation of CVE-2026-86060. Required action: Apply mitigations in accordance with vendor instructions, ensuring co…

---

## 2. 🔴 CISA KEV — CVE-2026-65660 — Microsoft SharePoint Code Injection Vulnerability

**CVE:** `CVE-2026-65660` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-09-25
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-65660>

> Vendor: Microsoft | Product: SharePoint. Microsoft SharePoint contains a code injection vulnerability which could allow an authorized attacker to execute code over a network. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Require…

---

## 3. 🟠 Zero-Day — Improve Router Hygiene to Protect Against Russian State-Sponsored Targeting

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Wed, 08 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a>

> Russian Government-Sponsored Activity Targets Poorly Configured and Vulnerable Devices Across Critical Sectors Executive summary Russian Federal Security Service (FSB) Center 16 cyber actors continue to exploit poorly configured and vulnerable networking devices worldwide, opportunistically compromising multiple critical infrastructure sector networks. This joint Cybersecurity Advisory (CSA) build…

---

## 4. 🟠 Zero-Day — September 2026 Patch Tuesday: Two Exploited Zero-Days and 113 Critical Vulnerabilities Among 972 CVEs

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Sep 08, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-september-2026/>

---

## 5. 🟠 Zero-Day — Roundcube Pre-Auth SQL Injection Flaw Actively Exploited in the Wild

**CVE:** `CVE-2026-48842` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-09-25
**Reference:** <https://thehackernews.com/2026/09/roundcube-pre-auth-sql-injection-flaw.html>

> The Canadian Centre for Cyber Security has warned that a now-patched Roundcube Webmail vulnerability is being actively exploited in the wild.

The vulnerability in question is CVE-2026-48842 (CVSS score: 8.1), a pre-authentication SQL injection in the virtuser_query plugin of Roundcube Webmail versions 1.6.x before 1.6.16 and 1.7.x before 1.7.1.

The issue stems from a preg_replace() backslash

---

## 6. 🟠 Zero-Day — DBHub HTTP transport DNS rebinding allows unauthenticated browser-origin SQL execution

**CVE:** `CVE-2026-61742` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-24
**Reference:** <https://github.com/advisories/GHSA-fm8p-53ww-hf6w>

> ### Summary

DBHub `0.21.2` exposes an unauthenticated HTTP MCP endpoint when started with the documented HTTP transport mode, for example `--transport http --port 8080`.

The HTTP server attempts to protect browser-origin access by checking whether the `Origin` hostname equals the `Host` hostname, then reflecting the validated `Origin` into `Access-Control-Allow-Origin`. This does not stop DNS re…

---

## 7. 🟠 Zero-Day — Unpatched OnePlus Flaws Let Installed Android Apps Gain Root Without Permissions

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-09-24
**Reference:** <https://thehackernews.com/2026/09/unpatched-oneplus-flaws-let-installed.html>

> A OnePlus 15 running the latest OxygenOS can be rooted by a malicious app the owner installs, one that asks for no special permissions. A researcher, Rasmus Moorats, chained two flaws in OnePlus&#x27;s own software to gain root access, the highest level of control over an Android phone.

OnePlus told him the same flaws affect many more of its own devices and those of OPPO, though it has not

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

## 14. 🟡 High Severity — code16 Sharp vulnerable to stored XSS via iframe srcdoc Attribute

**CVE:** `CVE-2026-61823` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-25
**Reference:** <https://github.com/advisories/GHSA-qxg3-46rw-79j8>

> ### Impact
A Stored Cross-Site Scripting (XSS) vulnerability exists in the rich text editor due to improper sanitization of the srcdoc attribute on &lt;iframe&gt; elements.

While the underlying Symfony HtmlSanitizer correctly HTML-encodes special characters inside the attribute value (e.g., converting &lt;script&gt; to &amp;lt;script&amp;gt;), the HTML specification mandates that browsers automat…

---

## 15. 🟡 High Severity — WSO2 and Adobe Commerce Flaws Exploited in Attacks, Added to CISA KEV

**CVE:** `CVE-2026-5430` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-09-25
**Reference:** <https://thehackernews.com/2026/09/wso2-and-adobe-commerce-flaws-exploited.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA), on Thursday, added two critical security flaws impacting WSO2 and Adobe Commerce and Magento to its Known Exploited Vulnerabilities (KEV) catalog, based on evidence of active exploitation.

The vulnerabilities are listed below -


  CVE-2026-5430 (CVS score: 9.8) - A path traversal vulnerability in  WSO2 API Control Plane,

---

## 16. 🟡 High Severity — Contao: Server-Side Request Forgery (SSRF) via Unvalidated RSS Feed URL in Feed Reader Module

**CVE:** `CVE-2026-57232` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-24
**Reference:** <https://github.com/advisories/GHSA-87mg-5grr-rhwh>

> ### Summary

The Feed Reader front-end module passes RSS feed URLs from its configuration directly to `$this-&gt;feedIo-&gt;read($url)` without any scheme validation or private-IP blocklist. A backend user with module-edit permissions can configure an arbitrary URL pointing to internal network services, cloud-provider metadata endpoints, or loopback addresses, causing the server to fetch those res…

---

## 17. 🟡 High Severity — Ash: Private action arguments can be set by user input via string-keyed params and atomic changesets

**CVE:** `CVE-2026-55736` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-24
**Reference:** <https://github.com/advisories/GHSA-f4hc-ppw9-4hhw>

> ### Summary

Ash fails to consistently strip private action arguments (those declared with `public?: false`) when a changeset is built from an untrusted parameter map. Private arguments are meant to be set only by trusted server-side code, but a caller who controls the parameters supplied to an action can inject a value for one. Any actor able to submit parameters to an action that defines a priva…

---

## 18. 🟡 High Severity — Cline: Cross-Origin WebSocket Hijacking in Cline Hub Dashboard (`/browser` endpoint)

**CVE:** `CVE-2026-59723` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-24
**Reference:** <https://github.com/advisories/GHSA-3cj3-hqcr-g934>

> ### Summary

The Cline Hub dashboard server (`@cline/cline-hub`), launched via the `cline dashboard` CLI command, accepts WebSocket connections on the `/browser` endpoint without validating the HTTP `Origin` header. When `ROOM_SECRET` is not set—the default for local (`127.0.0.1`) binds—`isAuthorizedBrowserRequest()` returns `true` unconditionally, allowing any website a developer visits to open a…

---

## 19. 🟡 High Severity — @bytebase/dbhub's read-only mode does not prevent database writes

**CVE:** `CVE-2026-61788` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-24
**Reference:** <https://github.com/advisories/GHSA-mwwr-p57h-56pf>

> ### Summary
 
Setting `readonly = true` on the `execute_sql` tool does not make the connection read-only. The connectors are written to set PostgreSQL `default_transaction_read_only=on` (and open SQLite in `readOnly` mode), but that code is gated on a config value that is never populated, so it never runs. The only thing left enforcing read-only is a classifier that inspects the first keyword of e…

---

## 20. 🟡 High Severity — http4s-scala-xml has an XML External Entity (XXE) processing issue

**CVE:** `CVE-2026-61741` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-24
**Reference:** <https://github.com/advisories/GHSA-cjx3-73hr-rpw7>

> http4s-scala-xml provides `EntityDecoder[F, scala.xml.Elem]` instances that parse XML message bodies. These decoders used a `javax.xml.parsers.SAXParserFactory` obtained from `SAXParserFactory.newInstance` without any security configuration.  With the JDK&#x27;s default settings, the parser resolves DOCTYPE declarations, external general and parameter entities, and external DTDs.

An application t…

---

## 21. 🟡 High Severity — phpMyFAQ has SQL Injection in `StopWords::add()` — Unescaped Stop Word Insertion

**CVE:** `CVE-2026-56738` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-24
**Reference:** <https://github.com/advisories/GHSA-rw77-vq4g-x3hp>

> ## Summary

The `StopWords::add()` method in phpMyFAQ builds a SQL `INSERT` statement using `sprintf()` and inserts the user-supplied stop word value directly into the query string **without calling the application&#x27;s database escaping function** on it. A sibling method, `StopWords::update()`, which modifies an *existing* stop word, correctly escapes the same kind of input. The omission is iso…

---

## 22. 🟡 High Severity — ixo Blockchain x/bonds DID-resolved payer drain + x/entity ICA authorization bypass

**CVE:** `CVE-2026-61604` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-24
**Reference:** <https://github.com/advisories/GHSA-w3rp-4cm2-4wgc>

> Impact

  Type: Improper authorization leading to unauthorized movement of user funds.

  The x/bonds module moved funds from an address that was resolved from a DID verification method, without verifying that the resolved address belonged to the transaction signer. Affected handlers included MsgMakeOutcomePayment, MsgBuy, MsgSell, MsgSwap, and MsgWithdrawShare, as well as the batch order processo…

---

## 23. 🟡 High Severity — Language Servers for AWS vulnerable to arbitrary file write

**CVE:** `CVE-2026-12958` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-24
**Reference:** <https://github.com/advisories/GHSA-6v3r-4p5c-mrp5>

> ## Summary
Language Servers for AWS (the aws/language-servers project) provides the Language Server Protocol implementations that power AWS developer tooling, including the Amazon Q Developer agentic chat experience, across IDEs such as VS Code, JetBrains, Visual Studio, and Eclipse.

Missing symlink validation in Language Servers for AWS may allow an arbitrary file write outside of the workspace …

---

## 24. 🟡 High Severity — Language Servers for AWS Vulnerable to Arbitrary Code Execution

**CVE:** `CVE-2026-12957` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-24
**Reference:** <https://github.com/advisories/GHSA-xhcr-j4j9-3gh7>

> ### Summary
Language Servers for AWS (the aws/language-servers project) provide the underlying language-server runtime that powers Amazon Q Developer&#x27;s AI coding assistance across its IDE plugins (Visual Studio Code, JetBrains, Eclipse, and
Visual Studio).

Improper trust boundary enforcement in Language Servers for AWS may allow for arbitrary code execution. If a local user opens a malicious…

---

## 25. 🟡 High Severity — ZITADEL: Actions V1 sandbox escape: host file read via require()

**CVE:** `CVE-2026-85057` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-24
**Reference:** <https://github.com/advisories/GHSA-fgmf-7rf8-m6vf>

> ### Summary

A vulnerability in ZITADEL Actions V1 allows an organization Action author to read files from the ZITADEL host filesystem through the JavaScript `require()` module loader. On common self-hosted deployments this can be chained to steal bootstrap credentials (including the Login Client PAT) and escalate from a single-tenant organization owner to instance administrator.

### Impact

ZITA…

---

## 26. 🟡 High Severity — Snipe-IT: Stored XSS via Custom Field name in asset-list column headers

**CVE:** `CVE-2026-62368` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-24
**Reference:** <https://github.com/advisories/GHSA-p9h3-gvpq-5539>

> ### Impact
A user with the &quot;customfields.create&quot; permission can store HTML/JS in a Custom Field name, which is later rendered as an asset-list column title WITHOUT escaping at app/Presenters/AssetPresenter.php line 364 (&#x27;title&#x27; =&gt; $field-&gt;name) and injected into the table header by the bundled bootstrap-table plugin. It executes for anyone who opens an asset list (e.g. /h…

---

## 27. 🟡 High Severity — Dozzle label filters do not restrict container event and statistics streams

**CVE:** `CVE-2026-62286` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-24
**Reference:** <https://github.com/advisories/GHSA-xcw9-qmmf-vqxj>

> ## Summary

Dozzle supports per-user label filters in `users.yml` that are documented as an access-control boundary: &quot;Filters are used to restrict the containers that a user can see&quot; and &quot;the `guest` user can only see containers with the label `com.example.app` … useful for restricting access to specific containers&quot; (docs/guide/authentication.md). This is the mechanism operator…

---

## 28. 🟡 High Severity — Snipe-IT: 2FA bypass via the API token flow

**CVE:** `CVE-2026-63493` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-24
**Reference:** <https://github.com/advisories/GHSA-hxcx-9h4f-42xx>

> ### Impact

An attacker who knows a victim&#x27;s password fully bypasses that account&#x27;s 2FA and obtains a persistent token with full API access as the user (read and write across the user&#x27;s permissions, including admin if the victim is an admin).

The token is an API credential, not a web/UI session (using it on web routes redirects to `/login`), but the REST API covers essentially the …

---

## 29. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
