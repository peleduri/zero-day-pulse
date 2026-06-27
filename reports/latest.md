# Zero Day Pulse

> **Generated:** 2026-06-27 02:01 UTC &nbsp;|&nbsp; **Total:** 39 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 27 &nbsp;|&nbsp; ✨ Enriched: 7

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a directory traversal vulnerability that allows attackers to read sensitive files via path traversal.
- **Affected Products:** SimpleHelp remote support software (RMM) version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit reported.
- **Patch Available:** Patch released by SimpleHelp; patch applied within two days of reporting (see vendor advisory).
- **Active Exploitation:** Ransomware actors exploited unpatched SimpleHelp Remote Monitoring and Management to compromise a utility billing software provider (CISA advisory).
- **Threat Actors:** Ransomware actors
- **Mitigation:** Apply the SimpleHelp patch released for versions 5.5.7 and earlier; upgrade to a newer version.
- **Vendor Advisory:** http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — First-Ever Exploitation of PTC Windchill Vulnerability Discovered in the Wild

**CVE:** `CVE-2026-12569` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://www.securityweek.com/first-ever-exploitation-of-ptc-windchill-vulnerability-discovered-in-the-wild/>

> CISA has added the remote code execution flaw CVE-2026-12569 to its Known Exploited Vulnerabilities catalog. The post First-Ever Exploitation of PTC Windchill Vulnerability Discovered in the Wild appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Improper input validation (deserialization of untrusted data) allows a remote, unauthenticated attacker to execute arbitrary code via specially crafted requests.
- **Affected Products:** PTC Windchill PDMlink, PTC FlexPLM
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** Public reports of exploitation exist, but no specific PoC or weaponized exploit URL is provided in the evidence.
- **Patch Available:** PTC released patches and mitigations on June 17, 2026; patches are available via PTC eSupport. See vendor advisory for download links.
- **Active Exploitation:** Confirmed exploitation in the wild reported by SecurityWeek and added to CISA's KEV catalog. Sources: SecurityWeek article (first-ever exploitation) and CISA KEV entry.
- **Threat Actors:** None known
- **Mitigation:** Apply the patches released by PTC (June 17) and follow vendor guidance; if patch unavailable, restrict network access to Windchill/FlexPLM services and validate inputs.
- **Vendor Advisory:** http://ptc.com/en/about/trust-center/advisory-center/active-advisories/windchill-flexplm-rce-vulnerability

---

## 3. 🟠 Zero-Day — Google Details Turla's New STOCKSTAY Backdoor Used in Ukraine Espionage Attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://thehackernews.com/2026/06/google-details-turlas-new-stockstay.html>

> The Russian state-sponsored threat actor known as Turla has been attributed to a previously undocumented .NET backdoor called STOCKSTAY that has been deployed against government and military organizations in Ukraine, and entities that have an interest in Italian foreign policy.

Describing the Windows backdoor as continually developed by the hacking group, Google Threat Intelligence Group (

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) places covert or malicious instructions inside external data sources (web pages, documents, tools) that an LLM or an agentic AI system consumes, allowing the injected instructions to influence model behavior — including zero-click/indirect vectors where the user does not directly provide the malicious input.
- **Affected Products:** Google Workspace, Gemini (Gemini in Workspace)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) or weaponized exploit URL identified in vendor advisory or public reporting; third-party reporting notes IPI payloads observed in the wild but does not provide a public PoC URL.
- **Patch Available:** No single discrete 'patch' published; Google describes ongoing, deployed layered defenses and continuous improvements (see vendor advisory and Workspace knowledge base).
- **Active Exploitation:** Yes — multiple public reports and vendor analysis note indirect prompt injection attempts and payloads observed in the wild, though reporting does not attribute these to named APTs or provide a public exploit PoC.
- **Threat Actors:** None known
- **Mitigation:** Google describes a layered defense: continuous model hardening and LLM-resistance work, runtime defenses in Gemini and Workspace, content/tool filtering, and admin guidance via Workspace knowledge base. Operators are advised to apply Google’s Workspace security guidance and follow vendor recommendations in the linked advisory/knowledge-base.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack where adversaries embed (often hidden) natural-language instructions inside webpage content (hidden text, HTML comments, user-generated content). When an agentic AI ingests page content as context without distinguishing it from the user’s trusted instructions, the agent can treat those embedded instructions as commands and perform actions (navigate, access authenticated sessions, extract data, or exfiltrate secrets).
- **Affected Products:** Chrome (Gemini / agentic browsing in Chrome), Perplexity Comet, Brave Leo, other agentic browser assistants — exact affected versions unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC(s) have been published for at least some agentic browser implementations (Brave’s disclosure / demonstration against Perplexity Comet). No public weaponized exploit against a discrete Chrome CVE was found in the cited corpus.
- **Patch Available:** Google announced layered defenses for agentic browsing (User Alignment Critic, expanded origin isolation, user confirmations) rolled into Chrome/agentic feature updates rather than a single CVE-style patch; no discrete CVE patch URL was published in the cited corpus.
- **Active Exploitation:** Yes — researchers and vendors have reported indirect prompt injection (IPI) activity in the wild against agentic browsers and assistants (Google, Forcepoint, Brave, Help Net Security). These reports describe live IPI payloads and demonstrations (e.g., Brave’s disclosure of a PoC against Perplexity Comet) but do not attribute a single Chrome CVE exploitation event.
- **Threat Actors:** None known
- **Mitigation:** Mitigations include: separate untrusted page content from trusted user instructions; isolate agentic browsing and expand origin-isolation; require explicit user confirmations for security/privacy-sensitive actions; deploy an independent alignment/validation model (User Alignment Critic) to vet agent actions; and red-team testing and telemetry to detect IPI patterns.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI): hidden or adversarial instructions embedded in external data sources (emails, documents, calendar invites, web content) that cause a generative AI agent to perform unintended actions such as exfiltrating data or executing commands. The Google advisory frames IPI as an attack vector distinct from direct prompt injection and emphasizes that these injections arrive via external content the agent processes rather than direct user prompts.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) or weaponized exploit is referenced in the advisory or the supplied prior corpus; no PoC URL is provided in the cited materials.
- **Patch Available:** No vendor "patch" is described in the advisory; the vendor advisory is an advisory/guidance post (see vendor_advisory URL) describing layered defenses rather than a software patch.
- **Active Exploitation:** The Google advisory does not report confirmed active exploitation of this advisory's issue. Prior corpus mentions EchoLeak (a separate discovery in Microsoft 365 Copilot) as an example of a zero-click prompt-injection exfiltration case, but the advisory itself does not state confirmed in-the-wild exploitation tied to its guidance.
- **Threat Actors:** None known
- **Mitigation:** Use a layered defense: validate and filter external content before it reaches the agent, apply policy and access controls, instrument provenance and context checking, and limit model capabilities and sensitive-data access (the advisory recommends a continuous, multi-layered approach to mitigations).
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Chinese state‑sponsored actors abuse network edge devices—especially backbone, provider edge, and customer edge routers—to gain persistent access and pivot into other networks, often modifying router firmware and leveraging compromised devices.
- **Affected Products:** backbone routers, provider edge (PE) routers, customer edge (CE) routers, network switches
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept or weaponized exploit is known.
- **Patch Available:** No official patch has been released; no vendor remediation guidance is currently available.
- **Active Exploitation:** No confirmed active exploitation in the wild has been reported for AA25‑239A.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor, Chinese state‑sponsored actors
- **Mitigation:** Regularly pull all running configurations from networking equipment and compare against the latest authorized baselines. If a device must remain enabled, apply strict hardening controls as a high‑priority mitigation step.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No exploit available.
- **Patch Available:** No patch available.
- **Active Exploitation:** Active exploitation unavailable.
- **Threat Actors:** Russian GRU (APT28/Fancy Bear)
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 11. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 12. 🟠 Zero-Day — CISA sets urgent deadline to fix Cisco flaw exploited in attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-sets-urgent-deadline-to-fix-cisco-flaw-exploited-in-attacks/>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) is giving federal agencies until Sunday to patch a vulnerability in Cisco Unified Communications Manager Server that is being actively exploited. [...]

---

## 13. 🟡 High Severity — Subsonic API: any authenticated user can delete or read any other user's playlist (IDOR)

**CVE:** `CVE-2026-49338` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-hmgp-w9jm-vp95>

> ## Summary

In gonic, the Subsonic API endpoints `/rest/deletePlaylist.view` and `/rest/getPlaylist.view` perform no per-resource authorization. Once authenticated as *any* user (admin or not), an attacker can:

1. **Delete any playlist owned by any other user** (including admin) by passing its `id`.
2. **Read the full contents** (name, comment, song list) of any other user&#x27;s **private** (non…

---

## 14. 🟡 High Severity — gonic has arbitrary file write in createPlaylist: any authenticated user can write playlist M3U content to attacker-controlled path on the host

**CVE:** `CVE-2026-49340` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-4gxv-p5g5-j7w7>

> ## Summary

A logic error in `ServeCreateOrUpdatePlaylist` allows **any authenticated Subsonic user** (including non-admin) to write playlist M3U content to an attacker-controlled absolute filesystem path on the gonic host, and to create intermediate directories with `0o777` permissions.

The bug is independent of the playlist ownership IDOR fixed in [`6dd71e6`](https://github.com/sentriz/gonic/co…

---

## 15. 🟡 High Severity — pnpm: Repository config can expand victim environment secrets into registry requests before scripts run

**CVE:** `CVE-2026-55180` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-3qhv-2rgh-x77r>

> &lt;!-- maintainer-action:start --&gt;
## Maintainer Action Plan

This report is ready to review with the shared patch branch. Start with the PR and the expected fixed behavior, then use the detailed exploit narrative below only if you want to replay the original path.

- Advisory: `CAND-PNPM-122` / `GHSA-3qhv-2rgh-x77r`
- Advisory URL: https://github.com/pnpm/pnpm/security/advisories/GHSA-3qhv-2r…

---

## 16. 🟡 High Severity — Nezha Monitoring: Pre-auth path traversal via /dashboard.. prefix confusion leaks jwt_secret_key

**CVE:** `CVE-2026-53519` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-5c25-7vpj-9mqh>

> ### Summary
`fallbackToFrontend` in the dashboard&#x27;s `NoRoute` handler treats any URL whose **raw string** starts with `/dashboard` as an admin-frontend asset request. The check uses `strings.HasPrefix`, not a path-segment match, so the input `/dashboard../data/config.yaml` is accepted; `strings.TrimPrefix` leaves `../data/config.yaml`; and `path.Join(&quot;admin-dist&quot;, &quot;../data/conf…

---

## 17. 🟡 High Severity — Nezha Monitoring: Stored future DDNS profile ID allows unauthorized use of another user's DDNS profile context

**CVE:** `CVE-2026-53521` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-39g2-8x68-pmx8>

> ## Summary

`PATCH /server/{id}` accepts and persists nonexistent `ddns_profiles` IDs for a member-owned server. If another user later creates a DDNS profile with one of those IDs, the DDNS worker resolves the stored ID and dispatches an update using the other user&#x27;s DDNS profile configuration in the context of the attacker&#x27;s server.

This is a second-order authorization bypass: direct b…

---

## 18. 🟡 High Severity — pnpm Has an Integrity Check Bypass via Missing Lockfile Integrity Field

**CVE:** `CVE-2026-50021` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-q6j5-fjx5-2mc3>

> ## Summary

pnpm&#x27;s tarball extraction worker skips integrity verification when the `integrity` field is absent from the lockfile resolution. If an attacker can both modify `pnpm-lock.yaml` to remove the `integrity:` field and cause the referenced registry URL to serve altered package content, `pnpm install --frozen-lockfile` can install the altered package without an integrity error. npm&#x27…

---

## 19. 🟡 High Severity — pnpm: Unsafe default behavior breaks integrity check

**CVE:** `CVE-2026-50573` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-54hh-g5mx-jqcp>

> While it is unclear whether this should be classified as a vulnerability, it is being reported through this channel because the current behavior may represent an unsafe default.

## Summary

`pnpm install` in non-frozen mode can accept new remote package content after detecting that the downloaded tarball does not match the integrity recorded in `pnpm-lock.yaml`.

When a package is already locked …

---

## 20. 🟡 High Severity — YARD static cache reads raw traversal paths before router sanitization

**CVE:** `CVE-2026-49342` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-pxcc-8665-phx8>

> ### Summary
YARD&#x27;s static cache lookup reads a request path before the router&#x27;s path cleanup runs. When a server is configured with a document root, a traversal path such as `/../yard-cache-secret.html` is joined against that root and can return a readable sibling `.html` file outside the intended static tree. 

The potential security risk seems low, as only html-ending files can be read…

---

## 21. 🟡 High Severity — @microsoft/kiota-http-fetchlibrary: Bearer token and Cookie leak across origin on redirect due to case-mismatched scrub in fetchRequestAdapter

**CVE:** `CVE-2026-49336` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-396q-4vc8-28x9>

> ### Summary

`@microsoft/kiota-http-fetchlibrary`&#x27;s `RedirectHandler` is documented as stripping `Authorization` and `Cookie` from cross-origin redirect targets, but the default `scrubSensitiveHeaders` callback in `RedirectHandlerOptions` uses case-sensitive property deletion (`delete headers.Authorization`, `delete headers.Cookie`) on a headers object that `FetchRequestAdapter.getRequestFrom…

---

## 22. 🟡 High Severity — PhpWeasyPrint vulnerable to SSRF and local file disclosure via the attachment option

**CVE:** `CVE-2026-49359` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-x8g9-h984-pc36>

> ### Summary

`pontedilana/php-weasyprint` fetches the content of option values server-side via `file_get_contents()` when the value looks like a URL, without restricting the URL scheme. The `attachment` option of `Pdf` is the reachable sink: any value that passes `isOptionUrl()` (`filter_var(..., FILTER_VALIDATE_URL)`) is downloaded by the PHP process and embedded into the generated PDF. Because `…

---

## 23. 🟡 High Severity — PhpWeasyPrint vulnerable to PHAR deserialization via output filename (CVE-2023-28115 case-insensitive bypass)

**CVE:** `CVE-2026-49286` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-2fmj-p74r-3wjm>

> ### Summary

`pontedilana/php-weasyprint` guarded the output filename against the `phar://` stream wrapper with a case-sensitive blacklist:

```php
if (0 === \strpos($filename, &#x27;phar://&#x27;)) {
    throw new \InvalidArgumentException(&#x27;The output file cannot be a phar archive.&#x27;);
}
```

PHP stream wrappers are **case-insensitive**, so `PHAR://`, `Phar://`, etc. bypass the check and…

---

## 24. 🟡 High Severity — Hackney has unbounded buffer accumulation in WebSocket

**CVE:** `CVE-2026-47073` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-q8jg-fgj4-fphf>

> ### Summary

The WebSocket client in `src/hackney_ws.erl` imposes no upper bound on memory consumption across three distinct code paths. In each case, an attacker-controlled WebSocket server can exhaust the connecting process&#x27;s memory without any authentication or special client configuration.

### Details

**1. Handshake response buffer (`read_handshake_response/3`)**

The function accumulat…

---

## 25. 🟡 High Severity — Hackney: Cross-origin Redirect Leaks Authorization, Cookie, and Request Body

**CVE:** `CVE-2026-47070` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-h73q-4w9q-82h4>

> ### Summary

The HTTP/3 redirect handler in `src/hackney_h3.erl` forwards the original request headers (`Authorization`, `Cookie`, `Proxy-Authorization`) and, for 307/308 responses, the original request body to the redirect target without checking whether the target host matches the origin. When `follow_redirect` is enabled and a server responds with a cross-origin `Location`, hackney delivers the…

---

## 26. 🟡 High Severity — Hackney has SSRF allowlist bypass in hackney_url:normalize/2 via percent-encoded host

**CVE:** `CVE-2026-47076` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-pj7v-xfvx-wmjq>

> ### Summary

`hackney_url:normalize/2` URL-decodes the host component of a parsed URL, but the caller&#x27;s SSRF allowlist runs before normalization using OTP&#x27;s `uri_string:parse/1` and `inet:parse_address/1`, neither of which decodes percent-escapes in hostnames. A URL like `http://%31%32%37%2E%30%2E%30%2E%31/` presents an encoded, non-IP-looking host to the validator, which passes the allo…

---

## 27. 🟡 High Severity — Streamable HTTP mode exposes LINE Desktop read/send tools without MCP authentication

**CVE:** `CVE-2026-49357` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-4hf8-5mjm-rfgq>

> # Streamable HTTP mode exposes LINE Desktop read/send tools without MCP authentication

## Summary

`line-desktop-mcp` supports a `--http-mode` Streamable HTTP transport for use with clients such as n8n. In this mode the server binds to `0.0.0.0` and exposes the MCP `/mcp` endpoint without an MCP-layer authentication check. Any network client that can reach the port can initialize a session, list …

---

## 28. 🟡 High Severity — Aimeos Pagible CMS vulnerable to Server Side Request Forgery (SSRF) via DNS rebinding in admin proxy

**CVE:** `CVE-2026-49262` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-mmj8-wcvw-6789>

> ### Summary
The administrative proxy route (`cmsproxy`) in Aimeos Pagible CMS is vulnerable to a Server-Side Request Forgery (SSRF) attack via DNS Rebinding. A Time-of-Check to Time-of-Use (TOCTOU) race condition exists between the URL validation phase and the actual HTTP request phase, allowing attackers to access internal network resources and cloud metadata endpoints.

### Details
Before execut…

---

## 29. 🟡 High Severity — php-weasyprint: shell command injection via configurable WeasyPrint binary path due to inverted is_executable() guard (mirror of KnpLabs/snappy GHSA-vpr4-p6fq-85jc)

**CVE:** `CVE-2026-49260` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-f5gc-qxf8-mh9g>

> ### Summary

`pontedilana/php-weasyprint` builds the shell command for WeasyPrint by passing the binary path through `escapeshellarg()` first and then checking the *quoted* result with `is_executable()`. On POSIX `escapeshellarg(&#x27;/usr/local/bin/weasyprint&#x27;)` returns `&#x27;/usr/local/bin/weasyprint&#x27;` with the single-quote characters as part of the string, so `is_executable()` looks …

---

## 30. 🟡 High Severity — Nebula Mesh: Web UI lacks ownership checks, enabling cross-operator access to hosts and networks (read, block, delete)

**CVE:** `CVE-2026-49258` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-c6v2-3ffm-vcmc>

> ## Summary

The web UI (`/ui/*`) does not apply the per-operator CA scoping the JSON API received for GHSA-598g-h2vc-h5vg. Any authenticated non-admin operator (for example, one created via self-registration or OIDC) can access resources belonging to other operators.

## Impact

A non-admin operator can:

- **Block or delete any other operator&#x27;s host.** `POST /ui/hosts/{id}/block` and `DELETE…

---

## 31. 🟡 High Severity — mcp-pinot: Unauthenticated tool invocation via default oauth_enabled=False + host 0.0.0.0 bind

**CVE:** `CVE-2026-49257` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-73cv-556c-w3g6>

> ## Resolution

Fixed in [v3.1.0](https://github.com/startreedata/mcp-pinot/releases/tag/v3.1.0), released 2026-05-25. The fix was merged in [PR #95](https://github.com/startreedata/mcp-pinot/pull/95) at commit [`1c7d3f9`](https://github.com/startreedata/mcp-pinot/commit/1c7d3f9cd384854bf72c127d230bdb32299475ad).

The fix changes the default HTTP bind host to `127.0.0.1`, refuses non-loopback HTTP/…

---

## 32. 🟡 High Severity — deepstream is vulnerable to prototype pollution

**CVE:** `CVE-2026-49252` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-9v98-6g37-x9g6>

> ### Impact
Prototype pollution in deepstream server v &lt;=10.0.4. Potential privilege escalation from any authenticated user with write permission to any record.

### Patches
Yes, upgrade to v10.0.5

### Workarounds
Filter out all messages containing the path `__proto__`, `constructor`, `prototype`, **before they reach the server&#x27;s message pipeline**

---

## 33. 🟡 High Severity — Flawfinder output manipulation via untrusted filenames and source text

**CVE:** `CVE-2026-48813` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-4c3c-r6p8-c863>

> ### Impact

This vulnerability is an improper input neutralization issue leading to output manipulation, specifically, Terminal/ANSI Escape Sequence Injection and XML Injection:

* Terminal Output Spoofing: A malicious file whose name contains ANSI escape sequences can end up being included in flawfinder&#x27;s standard terminal output, with many effects. For example, this might allow an attacker …

---

## 34. 🟡 High Severity — turso-cli persists Turso platform JWT with world-readable (0o644) file permissions

**CVE:** `CVE-2026-48790` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-57f6-pvx8-hwj6>

> ### Summary

`turso-cli` persists the user&#x27;s Turso platform JWT to `settings.json` using Viper&#x27;s default `configPermissions` of `0o644`, leaving the credential file world-readable on standard Linux and macOS systems. Any other local UID on the host can read the file and recover the platform JWT, which grants full Turso platform access scoped to the user&#x27;s organizations.

### Impact
…

---

## 35. 🟡 High Severity — Weekly Metasploit Update: Modules for Audiobookshelf, LiteLLM, Next.js, Dalfox and more

**CVE:** `CVE-2025-25205` | `CVE-2026-42208` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://www.rapid7.com/blog/post/pt-weekly-metasploit-update-modules-for-audiobookshelf-litellm-next-js-dalfox-and-more>

> Help shape the future of Metasploit Framework We are planning future work in relation to the evasion capabilities present in Metasploit Framework, and how they function/are presented to users. We are currently accepting responses to our feedback form, which means that you can shape the future of how evasive capabilities are implemented in Metasploit Framework. The proposal for the changes can be f…

---

## 36. 🟡 High Severity — pydantic-ai: SSRF blocklist bypass via IPv4-compatible, SIIT/IVI, and local NAT64 IPv6 addresses (incomplete fix of CVE-2026-46678)

**CVE:** `CVE-2026-48782` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-cg7w-rg45-pc59>

> ## Summary

When an application using Pydantic AI opts a URL into `force_download=&#x27;allow-local&#x27;` (which disables the default block on private/internal IPs) **and runs on a network that routes the affected IPv6 transition forms (NAT64- or ISATAP-configured networks)**, the cloud-metadata blocklist could be bypassed by encoding the metadata IP in an IPv6 transition form that the previous f…

---

## 37. 🟡 High Severity — @sigstore/core has DSSE payloadType type-binding failure

**CVE:** `CVE-2026-48758` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://github.com/advisories/GHSA-jfc7-64v2-mr8c>

> ### Impact
The `preAuthEncoding` function in `@sigstore/core` uses Node.js `&#x27;ascii&#x27;` encoding when converting the PAE (Pre-Authentication Encoding) string to bytes. This allows `payloadType` to be mutated after signing without invalidating the signature, breaking the type-binding guarantee that DSSE is designed to provide.

In `packages/core/src/dsse.ts`, the PAE function builds a string…

---

## 38. 🟡 High Severity — New DirtyClone Linux Kernel Flaw Lets Local Users Gain Root via Cloned Packets

**CVE:** `CVE-2026-43503` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-26
**Reference:** <https://thehackernews.com/2026/06/new-dirtyclone-linux-kernel-flaw-lets.html>

> DirtyClone is a new Linux kernel privilege escalation in the DirtyFrag family. JFrog Security Research published a working exploit walkthrough for the flaw on June 25, the first public demonstration for this variant.

Tracked as CVE-2026-43503 (CVSS 8.8), it lets a local user corrupt file-backed memory through a cloned network packet and gain root. The patch landed in

---

## 39. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
