# Zero Day Pulse

> **Generated:** 2026-08-29 01:15 UTC &nbsp;|&nbsp; **Total:** 57 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 19 &nbsp;|&nbsp; 🟡 High: 38 &nbsp;|&nbsp; ✨ Enriched: 0

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

## 4. 🟠 Zero-Day — PaperCut releases second emergency patch for exploited flaws

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://www.bleepingcomputer.com/news/security/papercut-releases-second-emergency-patch-for-exploited-flaws/>

> PaperCut has released a second emergency security update for two actively exploited vulnerabilities in its PaperCut NG and MF print management software after researchers discovered multiple ways to bypass the initial fixes. [...]

---

## 5. 🟠 Zero-Day — Vikunja has an incomplete fix for CVE-2026-35595: Write-only user can detach shared project from parent hierarchy via parent_project_id=0

**CVE:** `CVE-2026-55064` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-44v6-7fxq-vgf4>

> ## Summary

The fix for CVE-2026-35595 (project re-parenting privilege escalation) only gates reparent operations when `parent_project_id &gt; 0`. A user with Write (but not Admin) permission on a shared child project can detach it from its parent by sending `parent_project_id: 0`, bypassing the Admin requirement. This severs the recursive CTE permission inheritance chain, potentially disrupting t…

---

## 6. 🟠 Zero-Day — Over 8,300 Gitea servers vulnerable to code execution attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://www.bleepingcomputer.com/news/security/over-8-300-gitea-servers-vulnerable-to-code-execution-attacks/>

> Over 8,300 Internet-exposed Gitea instances are still unpatched against a critical security flaw exploited in ongoing remote code execution attacks, according to cybersecurity watchdog Shadowserver. [...]

---

## 7. 🟠 Zero-Day — PaperCut NG/MF Critical Zero-Day Exploited in the Wild

**CVE:** `CVE-2026-81578` | `CVE-2026-82078` | `CVE-2023-27350` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild>

> Overview On August 27, 2026, PaperCut Software published an urgent security advisory stating that it is investigating active exploitation of a vulnerability affecting PaperCut NG and PaperCut MF. PaperCut has confirmed customer incidents and is treating the issue as a security emergency. At the initial time of disclosure, the vulnerability had not been assigned a CVE identifier, and PaperCut had n…

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

## 15. 🟠 Zero-Day — Yamcs's WebSocket subscription handlers omit the privilege checks their REST siblings enforce

**CVE:** `CVE-2026-55545` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-fwww-cp23-7f5g>

> **Asset / scope:** Yamcs 5.12.7 WebSocket topics (`packets`, `algorithm-status`, `mdb-changes`)

## Summary

Several WebSocket subscription handlers do not perform the privilege check that their REST counterparts
enforce, so a principal subscribing over WebSocket receives data the REST API would have scoped or denied.

## Root cause

- `packets` (`PacketsApi.subscribePackets`) performs no `ReadPac…

---

## 16. 🟠 Zero-Day — Klever: Marketplace settlement mints KLV when referral % + royalty % exceed the bid (negative seller share silently skipped)

**CVE:** `CVE-2026-54754` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-p7gw-2pcp-5pf8>

> ## Summary

When a marketplace order is settled (`MarketBuy` / `BuyItNow`, and auction `Claim`), the buyer&#x27;s
payment is split three ways — **referral**, **royalties**, and the **seller (market-order owner)
remainder**:

```
marketOwnerAmount = CurrentBid − referralAmount − royaltiesAmount
```

Referral and royalties are paid out **unconditionally**, but the seller remainder is only paid
**whe…

---

## 17. 🟠 Zero-Day — China-Made ZBT Routers Ship With Two Implants Giving Unauthenticated Attackers Root Access

**CVE:** `CVE-2026-74232` | `CVE-2026-74233` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://thehackernews.com/2026/08/china-made-zbt-routers-ship-with-two.html>

> VulnCheck has disclosed two previously undocumented factory implants in firmware for routers built by Shenzhen Zhibotong Electronics (ZBT), each of which gives an unauthenticated remote attacker the ability to run commands as root on affected devices.

The implants, named SPEAKINGSTONE and DARKLANTERN by the company&#x27;s zero-day research team, are tracked as CVE-2026-74232 and CVE-2026-74233.

---

## 18. 🟠 Zero-Day — PaperCut Releases Emergency Patch for Exploited Zero-Day

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://www.securityweek.com/papercut-releases-emergency-patch-for-exploited-zero-day/>

> A CVE identifier has not yet been assigned, but PaperCut is urging NG/MF users to install patches and implement mitigations. The post PaperCut Releases Emergency Patch for Exploited Zero-Day appeared first on SecurityWeek .

---

## 19. 🟠 Zero-Day — PaperCut Zero-Day Exploited in Attacks, Affecting All NG and MF Versions

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://thehackernews.com/2026/08/papercut-zero-day-exploited-in-attacks.html>

> PaperCut has alerted customers that bad actors are actively exploiting a vulnerability impacting all versions of its PaperCut NG and PaperCut MF print management software in zero-day attacks.

The company has released an emergency patch for v25 and v26 to address the issue. It said it&#x27;s &quot;aware of confirmed customer incidents and is treating this matter with the highest priority.&quot; An

---

## 20. 🟡 High Severity — MapFish Print has XXE that allows reading arbitrary files of certain types

**CVE:** `CVE-2026-55848` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-5v29-34h8-v68r>

> ### Summary
XXE on MapFish Print allows reading arbitrary files of certain types. Eg /etc/passwd or k8 secrets and certs.

https://github.com/mapfish/mapfish-print/commit/13020c0fbc299e5f604e4e66066311c4bf04d507

### Details
To trigger the XXE it is required to host a remote script and dtd file. When using the Print feature its possible to send the attacker server url as url of the gml layer.

The…

---

## 21. 🟡 High Severity — SeaweedFS: Path traversal in the S3 gateway X-Amz-Copy-Source header allows cross-bucket object read

**CVE:** `CVE-2026-55874` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-56wq-x3wv-3ff4>

> ### Summary
The SeaweedFS S3 API gateway did not reject `..` path segments in the `X-Amz-Copy-Source` header used by `CopyObject` and `UploadPartCopy`. The request URL path was hardened against traversal in 4.30 (CVE-2026-54917), but the copy-source header was only checked for emptiness, so a `..` segment in the copy source survived into the server-side filer path and resolved into a different buc…

---

## 22. 🟡 High Severity — arc has unauthenticated cluster node admission when `cluster.shared_secret` is unset

**CVE:** `CVE-2026-55678` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-p378-jp5r-gpgw>

> ## Summary

Arc Enterprise clustering accepts cluster join requests without authentication when `cluster.enabled=true` but `cluster.shared_secret` is not configured. The coordinator validates HMAC authentication only if a shared secret is non-empty; otherwise, a network attacker who can reach the coordinator port can send a join request with attacker-controlled node addresses and role. Accepted no…

---

## 23. 🟡 High Severity — PrivateBin has reflected JSON injection in backend responses via unescaped REQUEST_URI

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

## 24. 🟡 High Severity — PrivateBin has stored Cross-Side-Scripting (XSS) vulnerability in attachment download link via dangerous MIME types with required user-interaction

**CVE:** `CVE-2026-55696` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-f2xf-7x3g-4272>

> ### Summary

Stored cross-site scripting (XSS) in PrivateBin&#x27;s attachment download link. An anonymous attacker can create a paste with a **text/html** attachment that, with certain user interaction, bypasses protections similar to CVE-2022-24833. When a victim opens the &quot;Download attachment&quot; link in a new tab, the attacker&#x27;s inline JavaScript executes in the PrivateBin instance…

---

## 25. 🟡 High Severity — Pimcore Vulnerable to Remote Code Execution via DataObject Class-Definition Field Name

**CVE:** `CVE-2026-55634` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-9x44-4gxf-8c25>

> ## Overview

A DataObject **class-definition field name** is concatenated, without an identifier allowlist, into the PHP class source that Pimcore generates for every DataObject class (`protected $&lt;fieldName&gt;;`). A user holding only the ordinary `objects` (DataObjects) permission can import a class definition whose field name closes the property and injects arbitrary PHP into the generated c…

---

## 26. 🟡 High Severity — Pimcore Hotspotimage getDataFromResource() unrestricted Serialize::unserialize over object-store column (PHP Object Injection, CWE-502)

**CVE:** `CVE-2026-55220` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-w23p-wrp7-ch38>

> ## Summary

`Pimcore\Model\DataObject\ClassDefinition\Data\Hotspotimage::getDataFromResource()` deserializes the `*__hotspots` object-store column through the `Pimcore\Tool\Serialize::unserialize()` wrapper **without a class allowlist** (the wrapper&#x27;s `$allowedClasses` parameter defaults to `true`, i.e. fully unrestricted). Because the persistence layer always stores this column as PHP-`seria…

---

## 27. 🟡 High Severity — Pimcore: Insufficient Permission Check on Class Definition Creation Endpoint Allows Privilege Escalation

**CVE:** `CVE-2026-55212` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-f97c-ph8j-8vff>

> ### Summary
The Studio API class definition creation endpoint in `pimcore/studio-backend-bundle` is guarded by the `objects` permission instead of the `classes` permission, allowing any standard editor-level user to create class definitions without admin privileges. Class definition creation is a structural admin operation that generates new database tables and PHP class files on the server. Addit…

---

## 28. 🟡 High Severity — Pimcore: SQL Injection via Column Name in DateFilter allows authenticated user to extract arbitrary database data including admin password hashes

**CVE:** `CVE-2026-55208` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-79cw-hfcc-7mw9>

> ## Summary

An authenticated user extracts the admin password hash and any other database content through a time-based blind SQL injection in the `DateFilter` column key parameter. The `POST /pimcore-studio/api/website-settings` endpoint (and 11 other listing endpoints) accepts a `columnFilters` array where the `key` field is interpolated directly into SQL with only manual backtick wrapping. The `…

---

## 29. 🟡 High Severity — MariaDB's connector leaks the cleartext password to an MitM despite `ssl: true`

**CVE:** `CVE-2026-55215` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-cqhc-2h57-wpxf>

> ### Summary
When SSL/TLS is enabled but no CA / server certificate is provided, the
connector verifies the server&#x27;s identity using fingerprint validation. The
check is effective,  the connection is ultimately rejected when it fails, 
but it happens *after* the authentication exchange. As a result, the
credentials are sent before validation occurs, so an active man-in-the-middle
who presents t…

---

## 30. 🟡 High Severity — plone.app.event vulnerable to denial of service via iCalendar import

**CVE:** `CVE-2026-55247` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-r82h-mqw3-fc56>

> ### Impact
By abusing the iCalendar import functionality, a logged-in editor could take the whole site offline, make the server reach into the internal network and read calendar files off disk (SSRF), and store XSS.

### Patches
The problem has been patched in `plone.app.event`.

* For Plone 6.2: upgrade to `plone.app.event` 6.0.1
* For Plone 6.1: upgrade to `plone.app.event` 5.2.4
* For Plone 6.0…

---

## 31. 🟡 High Severity — Incus has a project restriction bypass in instance copy across projects

**CVE:** `CVE-2026-55622` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-c9f5-j9c3-mhrg>

> ### Summary
Missing authorization checks exist for instance copying where an attacker knowing the name of a project that they don&#x27;t have access to and the name of an instance in that project can copy the instance to a new project. This issue could allow an attacker to access secrets in instances they are not authorized to access.

### Details
`cmd/incusd/instances.go` authorizes `POST /1.0/in…

---

## 32. 🟡 High Severity — Incus has a project restriction bypass for custom volume copy across projects

**CVE:** `CVE-2026-55621` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-64f3-v33m-w89f>

> ### Summary

Missing authorization checks exist for custom volume copying where an attacker who knows the name of a project that they don&#x27;t have access to and the name of a custom volume in that project can copy the custom volume to a new project. This issue could allow an attacker to access secrets in custom volumes they are not authorized to access.

### Details

The storage volume creation…

---

## 33. 🟡 High Severity — plone.app.portlets vulnerable to denial of service via RSS feed portlet

**CVE:** `CVE-2026-55248` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-x5g3-w747-2h8q>

> ### Impact
By adding an RSS portlet, and giving this a link to a very large file, a member can cause a denial of service attack, because Plone will use lots of memory. The member could also use different urls to try to get information about the internal network and open port numbers (SSRF). A malicious RSS feed could cause stored XSS, when the url of a feed item is a javascript url.

### Patches
T…

---

## 34. 🟡 High Severity — 9router: Unauthenticated `/v1` proxy access via `Host`-header spoofing → open AI relay + SSRF

**CVE:** `CVE-2026-55641` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-86m2-fcxq-5q7c>

> ## Summary

9router&#x27;s request guard decides a request is &quot;local&quot; (and therefore exempt from API-key auth on the `/v1` LLM proxy) by reading the **client-controlled `Host` header**. Because 9router binds `0.0.0.0` by default (and the CLI misleadingly prints &quot;localhost&quot;), a remote, unauthenticated attacker who can reach the port can send `Host: localhost` to be treated as lo…

---

## 35. 🟡 High Severity — Bifrost's SSRF deny-list is incomplete: isPublicIP permits CGNAT, IPv6 6to4/NAT64, and site-local in FetchAndEncodeURL

**CVE:** `CVE-2026-55245` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-w98g-5w9p-p3rc>

> ## Summary

`isPublicIP` in `core/providers/utils/fetch.go` — the SSRF deny-list that gates `FetchAndEncodeURL` — does not reject several routable address ranges that map onto internal infrastructure. Carrier-Grade NAT (`100.64.0.0/10`, RFC 6598), IPv6 6to4 (`2002::/16`), NAT64 (`64:ff9b::/96` and `64:ff9b:1::/48`), and deprecated IPv6 site-local (`fec0::/10`) are all classified as public and perm…

---

## 36. 🟡 High Severity — piccolo-admin has a privilege escalation issue - admin to superuser via session-token disclosure in GET /api/tables/sessions/.

**CVE:** `CVE-2026-55485` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-2gh4-jmwq-rr8w>

> ## Summary

`piccolo_admin` uses a helper called `superuser_validators` to gate access to the user and session tables for non-superusers. The helper rejects `PUT`, `PATCH`, `DELETE`, and `POST`, but **does not reject `GET`**.

The `sessions` table stores live session tokens **in plaintext**, and the token column is not marked `secret=True`, so it is included in every `GET` response. Any non-superu…

---

## 37. 🟡 High Severity — WsgiDAV MySQL provider has a blind SQL injection

**CVE:** `CVE-2026-55509` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-p6gw-4frg-j7jw>

> ### Summary

The sample `MySQLBrowserProvider` builds its SQL queries by concatenating strings, and the record key from the request URL goes straight into the WHERE clause with no escaping. Any user who can reach a share backed by this provider can inject SQL through the URL. Since these read shares are commonly published without authentication, an anonymous attacker can read arbitrary data from t…

---

## 38. 🟡 High Severity — Snipe-IT vulnerable to cross-company asset maintenance re-parenting via API update

**CVE:** `CVE-2026-55516` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-575r-357h-fhch>

> ### Impact
The API endpoint for updating asset maintenance records allows an authorized user to change the asset_id of an existing maintenance record to an asset outside their company scope.

In a Full Multiple Company Support / multi-company deployment, this allows a user from Company A to attach or move a maintenance record onto an asset belonging to Company B. The endpoint appears to authorize …

---

## 39. 🟡 High Severity — Snipe-IT has CSS Injection via `header_color` Setting

**CVE:** `CVE-2026-55481` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-w7qw-5wfv-gwx9>

> ### Impact

Because `default.blade.php` is the base layout loaded on every authenticated page, all active user sessions are affected immediately upon the next page load after the payload is saved. An attacker who has compromised an admin account (or who is a malicious insider) can use this to silently exfiltrate session tokens from all other users, including other administrators.

Additionally, th…

---

## 40. 🟡 High Severity — Snipe-IT's API Location Creation Bypasses FMCS Parent-Child Company Boundary Validation

**CVE:** `CVE-2026-55472` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-8w8c-8mx9-52cw>

> ### Impact
When Full Multiple Companies Support and scope_locations_fmcs are both enabled, the API endpoint for creating locations can still create a child location under a parent location from a different company. The code detects the invalid parent/child company mismatch, but it appears not to return immediately, so the request continues and the record is still saved. The equivalent Web flow cor…

---

## 41. 🟡 High Severity — Yamcs vulnerable to authenticated remote code execution via unescaped StreamSQL `LIKE` pattern compiled by Janino (`LikeExpression`)

**CVE:** `CVE-2026-55565` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-c64q-hj4j-375f>

> ## Summary
Yamcs compiles StreamSQL query expressions to Java at runtime with Janino. The `LIKE` operator inserts the user-supplied pattern into the generated Java **unescaped**, inside a `&quot;...&quot;` literal, so a pattern containing `&quot;` breaks out and injects arbitrary Java (e.g. a `static{}` block that runs an OS command when the compiled filter class loads). Result: RCE as the OS user…

---

## 42. 🟡 High Severity — Yamcs vulnerable to Remote Code Execution via instance-template argument YAML injection (createInstance)

**CVE:** `CVE-2026-55559` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-73mf-m39p-wpm9>

> ### Summary

`templateArgs` sent to `POST /api/instances` (and `PATCH /api/instances/{instance}`) are written into the rendered instance config as raw text, then parsed as YAML and loaded. Yamcs instantiates each `services:` entry by its `class:`, so injecting YAML through a template arg lets you add a `services:` entry for `org.yamcs.ProcessRunner` and run a command on the host. The args aren&#x2…

---

## 43. 🟡 High Severity — Yamcs's Missing Authorization on Role and Privilege Enumeration Endpoints Allows Any Authenticated User to Disclose Full Security Configuration

**CVE:** `CVE-2026-55547` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-cvw4-55pp-3hfq>

> ## Summary

Missing authorization checks on three IAM API endpoints (`GET /api/roles`, `GET /api/roles/{name}`, `GET /api/privileges`) allow any authenticated user — regardless of their assigned permissions — to enumerate the complete list of system privileges and role definitions. An attacker with only a low-privilege account (e.g., a read-only operator) can retrieve the full privilege taxonomy o…

---

## 44. 🟡 High Severity — Yamcs Core API has Multiple Missing Function Level Access Control vulnerabilities

**CVE:** `CVE-2026-55521` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-962x-ccwf-8x6p>

> ### Summary
Multiple Missing Function Level Access Control vulnerabilities exist in the Yamcs Core API. These vulnerabilities allow any authenticated user, regardless of their assigned roles or privileges (e.g., an unprivileged &quot;Guest&quot;), to bypass intended access controls. An attacker can exploit these flaws to extract sensitive telemetry metadata, disrupt satellite communication link pr…

---

## 45. 🟡 High Severity — Yamcs vulnerable to authenticated RCE via StreamSQL aggregate-compiler column-name injection in Yamcs `executeSql`

**CVE:** `CVE-2026-55511` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-3g44-3m7x-cgg2>

> ## Overview

Yamcs compiles StreamSQL expressions to Java on the fly with the Janino `SimpleCompiler` (no restrictive class-loading policy or expression sandbox). When a StreamSQL aggregate such as `sum(...)` is applied to a **column**, the column&#x27;s *name* is interpolated **unescaped** into the generated Java source. Because Yamcs accepts arbitrary characters in a double-quoted column identif…

---

## 46. 🟡 High Severity — Vikunja vulnerable to authenticated cross-tenant kanban-bucket relocation via `project_view_id` mass-assignment

**CVE:** `CVE-2026-55067` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-569v-q83c-3j3g>

> ## Summary

`POST /api/v1/projects/{project}/views/{view}/buckets/{bucket}` mass-assigns the request body&#x27;s `project_view_id` onto the bucket row. The permission check only verifies that the URL-supplied bucket already belongs to the URL-supplied `(project, view)` pair; the body&#x27;s `project_view_id` is never validated. Any signed-in user can therefore take one of their own buckets and gra…

---

## 47. 🟡 High Severity — Vikunja has cross-tenant IDOR in kanban move-task endpoint via unauthorized body task_id

**CVE:** `CVE-2026-55066` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-5pg6-m483-7vrg>

> ## Summary

The kanban endpoint `POST /api/v1/projects/{project}/views/{view}/buckets/{bucket}/tasks`
moves a task into a bucket. The task is identified by `task_id` in the **request
body**. The endpoint&#x27;s authorization check (`TaskBucket.CanUpdate`) only verifies
that the caller may update the *project/view/bucket named in the URL* — it never
checks any permission on `task_id`.

Any authenti…

---

## 48. 🟡 High Severity — Pocket-ID has an Open Redirect on the OIDC /authorize page via unvalidated redirect_uri with prompt=none

**CVE:** `CVE-2026-55834` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-2wvm-8mvp-22qv>

> ### Summary
The OIDC authorization page in the pocket-id frontend redirects the browser to an attacker-controlled URL without consulting the backend redirect_uri allow-list when the request uses prompt=none. An attacker who knows a valid client_id can craft an /authorize link that sends a victim (or a victim&#x27;s browser doing a silent re-auth) to any external https URL, enabling phishing and OA…

---

## 49. 🟡 High Severity — Trestle has Server-Side Template Injection (SSTI) via Recursive Template Re-evaluation of Untrusted Data

**CVE:** `CVE-2026-54757` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-jw39-3688-r4rx>

> ### Impact

A Server-Side Template Injection (SSTI) vulnerability exists in multiple locations of trestle&#x27;s Jinja2 rendering pipeline due to a systemic pattern: **untrusted data is re-parsed as Jinja2 template source code without sandboxing**. This advisory tracks the root cause across all affected code paths.

The core anti-pattern is: treating runtime data (rendered output, included Markdow…

---

## 50. 🟡 High Severity — KubeVela Terraform remote loader DoS via unbounded file read

**CVE:** `CVE-2026-55108` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-fmgp-q6jx-gg3x>

> ### Summary

KubeVela&#x27;s Terraform remote configuration loader can be abused to make `vela-core` read an unbounded byte stream into memory, causing an out-of-memory kill and a control-plane denial of service.

The issue is reachable when a user with permission to create or update a `core.oam.dev/v1beta1` `ComponentDefinition` registers a Terraform `remote` schematic that points to a malicious …

---

## 51. 🟡 High Severity — Hatchet allows cross-tenant write/DoS to other tenants' workers via Dispatcher gRPC UpsertWorkerLabels and Unsubscribe

**CVE:** `CVE-2026-54746` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-8x7x-83cf-c3pg>

> ### Summary

A **cross-tenant write / DoS** vulnerability in the Hatchet `Dispatcher` gRPC service allows any holder of a normal tenant-scoped API token (the lowest credential Hatchet issues — an `OWNER` of a brand-new tenant) to overwrite the affinity labels of, or disconnect from the dispatcher, any worker UUID belonging to any other tenant on the same Hatchet instance. The two affected RPCs — `…

---

## 52. 🟡 High Severity — Phalcon: Non-constant-time HMAC verification in `Encryption\Crypt::decrypt` (timing side-channel)

**CVE:** `CVE-2026-54736` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://github.com/advisories/GHSA-8jqh-95g6-7jpj>

> ## Summary

`Phalcon\Encryption\Crypt` provides authenticated encryption: when `useSigning` is enabled (the default), `encrypt()` appends an HMAC tag and `decrypt()` verifies it before returning the plaintext. The verification compares the attacker-supplied tag against the freshly computed HMAC using PHP/Zephir identity comparison (`!==`), which the Zephir compiler lowers to `!ZEPHIR_IS_IDENTICAL(…

---

## 53. 🟡 High Severity — ownCloud Flaw Exploited to Steal Nuclear Records From Philippine Research Body

**CVE:** `CVE-2023-49105` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://thehackernews.com/2026/08/snowflake-github-actions-flaw-lets.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Thursday added a critical security flaw impacting ownCloud to its Known Exploited Vulnerabilities (KEV) catalog following reports that a Chinese-speaking threat actor weaponized the vulnerability to target a nuclear research body in the Philippines.

The vulnerability, tracked as CVE-2023-49105 (CVSS score: 9.8), is a case of

---

## 54. 🟡 High Severity — OpenAI Agents Exploited Linux Kernel Flaw on Company’s Own Systems

**CVE:** `CVE-2026-53362` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://www.securityweek.com/openai-agents-exploited-linux-kernel-flaw-on-companys-own-systems/>

> CISA has added the exploited flaw, CVE-2026-53362, to its KEV catalog, alongside a JFrog vulnerability exploited by OpenAI agents. The post OpenAI Agents Exploited Linux Kernel Flaw on Company’s Own Systems appeared first on SecurityWeek .

---

## 55. 🟡 High Severity — Two Unitree G1 EDU Humanoid Robot Flaws Enable Root RCE, One Starts Over Bluetooth

**CVE:** `CVE-2026-76639` | `CVE-2026-76640` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://thehackernews.com/2026/08/two-unitree-g1-edu-humanoid-robot-flaws.html>

> Security researcher Olivier Laflamme has disclosed two independent root remote code execution (RCE) chains affecting the Unitree G1 EDU, including a Bluetooth Low Energy (BLE) path that can reach root on the robot&#x27;s Locomotion PC.

The flaws are tracked as CVE-2026-76639 and CVE-2026-76640, with the first involving a network-adjacent path through chat_go and bashrunner and the

---

## 56. 🟡 High Severity — Critical cPanel Flaw Could Let One Hosting Customer Take Root Control of a Whole Server

**CVE:** `CVE-2026-65643` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-08-28
**Reference:** <https://thehackernews.com/2026/08/critical-cpanel-flaw-could-let-one.html>

> cPanel has released patches for a security flaw affecting domain parking and addon domain functionality in cPanel and WebHost Manager (WHM), which could allow code execution as the root user.

The vulnerability, assigned the CVE identifier CVE-2026-65643, impacts all supported versions of cPanel &amp; WHM.

cPanel described the issue as a critical security vulnerability and said that an

---

## 57. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
