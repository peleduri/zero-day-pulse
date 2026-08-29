# Zero Day Pulse

> **Generated:** 2026-08-29 20:05 UTC &nbsp;|&nbsp; **Total:** 17 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 7 &nbsp;|&nbsp; ✨ Enriched: 0

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

## 3. 🟠 Zero-Day — RestrictedPython guard hooks can be shadowed via positional-only arguments

**CVE:** `CVE-2026-55830` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-ffg3-p8fm-mjx2>

> ### Impact

RestrictedPython rewrites sensitive operations to go through guard hooks. Attribute access becomes `_getattr_(obj, name)`, item access becomes `_getitem_(obj, key)`, writes go through `_write_`, and print goes through `_print_`. The embedding application supplies these hooks to enforce its policy.

Argument-name validation rejects these protected names for regular arguments, `*args`, `…

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

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

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

---

## 9. 🟠 Zero-Day — Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite

**CVE:** `CVE-2025-66376` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Tue, 21 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a>

> Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite Executive summary A group of Russian state-supported cyber actors has been targeting and compromising various Western government and commercial organizations using the Zimbra Collaboration Suite (ZCS) software since at least July 2025. The Russian state-supported advanced persistent threat …

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

---

## 11. 🟡 High Severity — Five Critical WordPress Plugin and Theme Flaws Enable Site Takeover or RCE

**CVE:** `CVE-2026-76581` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-08-29
**Reference:** <https://thehackernews.com/2026/08/five-critical-wordpress-plugin-and.html>

> Multiple critical security flaws have been disclosed in WordPress plugins and themes, including WPMU DEV Dashboard, Avada, TranslatePress, Pods, and GiveWP, that could lead to authentication bypass, account takeover, and arbitrary code execution.

The vulnerabilities, according to Wordfence and Patchstack, are listed below -


  CVE-2026-76581 (CVSS score: 9.8) - An authentication bypass flaw in

---

## 12. 🟡 High Severity — MapFish Print has XXE that allows reading arbitrary files of certain types

**CVE:** `CVE-2026-55848` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-5v29-34h8-v68r>

> ### Summary
XXE on MapFish Print allows reading arbitrary files of certain types. Eg /etc/passwd or k8 secrets and certs.

https://github.com/mapfish/mapfish-print/commit/13020c0fbc299e5f604e4e66066311c4bf04d507

### Details
To trigger the XXE it is required to host a remote script and dtd file. When using the Print feature its possible to send the attacker server url as url of the gml layer.

The…

---

## 13. 🟡 High Severity — SeaweedFS: Path traversal in the S3 gateway X-Amz-Copy-Source header allows cross-bucket object read

**CVE:** `CVE-2026-55874` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-56wq-x3wv-3ff4>

> ### Summary
The SeaweedFS S3 API gateway did not reject `..` path segments in the `X-Amz-Copy-Source` header used by `CopyObject` and `UploadPartCopy`. The request URL path was hardened against traversal in 4.30 (CVE-2026-54917), but the copy-source header was only checked for emptiness, so a `..` segment in the copy source survived into the server-side filer path and resolved into a different buc…

---

## 14. 🟡 High Severity — arc has unauthenticated cluster node admission when `cluster.shared_secret` is unset

**CVE:** `CVE-2026-55678` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-p378-jp5r-gpgw>

> ## Summary

Arc Enterprise clustering accepts cluster join requests without authentication when `cluster.enabled=true` but `cluster.shared_secret` is not configured. The coordinator validates HMAC authentication only if a shared secret is non-empty; otherwise, a network attacker who can reach the coordinator port can send a join request with attacker-controlled node addresses and role. Accepted no…

---

## 15. 🟡 High Severity — PrivateBin has reflected JSON injection in backend responses via unescaped REQUEST_URI

**CVE:** `CVE-2026-55891` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-xrjc-c68j-hp7w>

> ## Vulnerability Details

A reflected JSON injection allows an attacker to return arbitrary data in the JSON endpoints (like ` /?jsonld=` and `/?pasteid`).

### Root Cause

`Request::getRequestUri()` sanitizes `$_SERVER[&#x27;REQUEST_URI&#x27;]` with `FILTER_SANITIZE_URL`:

```php
public function getRequestUri()
{
    $uri = array_key_exists(&#x27;REQUEST_URI&#x27;, $_SERVER) ? filter_var($_SERVER…

---

## 16. 🟡 High Severity — PrivateBin has stored Cross-Side-Scripting (XSS) vulnerability in attachment download link via dangerous MIME types with required user-interaction

**CVE:** `CVE-2026-55696` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-f2xf-7x3g-4272>

> ### Summary

Stored cross-site scripting (XSS) in PrivateBin&#x27;s attachment download link. An anonymous attacker can create a paste with a **text/html** attachment that, with certain user interaction, bypasses protections similar to CVE-2022-24833. When a victim opens the &quot;Download attachment&quot; link in a new tab, the attacker&#x27;s inline JavaScript executes in the PrivateBin instance…

---

## 17. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
