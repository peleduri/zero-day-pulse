# Zero Day Pulse

> **Generated:** 2026-08-21 06:24 UTC &nbsp;|&nbsp; **Total:** 42 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 20 &nbsp;|&nbsp; 🟡 High: 22 &nbsp;|&nbsp; ✨ Enriched: 0

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

## 3. 🟠 Zero-Day — node-opcua: Unbounded nonce cache enables unauthenticated heap exhaustion DoS

**CVE:** `CVE-2026-54156` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://github.com/advisories/GHSA-6wvw-vrw4-363w>

> **Summary**
A process-global nonce cache with no eviction policy allows an unauthenticated remote attacker to exhaust server heap memory by repeatedly opening sessions, causing the node-opcua server process to crash.

**Affected versions:** &lt;= 2.165.0
**Tested version:** 2.165.0
**CVSS Score:** 7.5 (High)
**CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
**CWE:** CWE-770 Allocation …

---

## 4. 🟠 Zero-Day — Velero vulnerable to file path traversal when extracting from backup's tarball

**CVE:** `CVE-2026-32637` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://github.com/advisories/GHSA-j2g6-362q-6qc6>

> ### Impact
_What kind of vulnerability is it? Who is impacted?_
If the attacker compromises the backup&#x27;s object storage backend and uploads a malicious backup tarball including file names like the following:
* ../../../tmp/escape_1              -&gt; file created at /tmp/escape_1
* ../../../../../../../../tmp/escape_2 -&gt; file created at /tmp/escape_2
* ../../../tmp/cron_poc              -&…

---

## 5. 🟠 Zero-Day — Attackers Exploit Zimbra SNMP Flaw for Unauthenticated Remote Code Execution

**CVE:** `CVE-2026-73570` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://thehackernews.com/2026/08/attackers-exploit-zimbra-snmp-flaw-for.html>

> A now-patched security flaw impacting Zimbra Collaboration (ZCS) has come under active exploitation in the wild, according to the Polish Computer Emergency Response Team (CERT Polska).

The vulnerability in question is CVE-2026-73570 (CVSS score: 8.9), which refers to a case of command injection that can lead to remote code execution.

&quot;A remote code execution vulnerability exists in Zimbra

---

## 6. 🟠 Zero-Day — Critical Zimbra RCE flaw now actively exploited in attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://www.bleepingcomputer.com/news/security/critical-zimbra-rce-flaw-now-actively-exploited-in-attacks/>

> CERT Polska, the Polish Computer Emergency Response Team (CERT), warned that attackers have begun exploiting a critical vulnerability in Zimbra Collaboration Suite (ZCS). [...]

---

## 7. 🟠 Zero-Day — [0day-rubbish] ONE Reporter 13.1 Authenticated RCE / privilege escalation via CommandExecutor (8.8)

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://seclists.org/fulldisclosure/2026/Aug/75>

> Posted by disclosure via Fulldisclosure on Aug 19 0day Rubbish Research Team is publicly disclosing a vulnerability in ONE Reporter 13.1. Type: Authenticated RCE / privilege escalation via CommandExecutor (CWE-78) CVSS: 8.8 (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H) Impact: Low-privilege user executes arbitrary commands as local-admin service account Authentication: authenticated Full technica…

---

## 8. 🟠 Zero-Day — [0day-rubbish] RoboTask 11.0.5.1229 Unauthenticated REST API remote task execution (9.8)

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://seclists.org/fulldisclosure/2026/Aug/73>

> Posted by disclosure via Fulldisclosure on Aug 19 0day Rubbish Research Team is publicly disclosing a vulnerability in RoboTask 11.0.5.1229. Type: Unauthenticated REST API remote task execution (CWE-306) CVSS: 9.8 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) Impact: Unauthenticated attacker enumerates and triggers pre-existing tasks with Administrator privileges Authentication: unauthenticated /…

---

## 9. 🟠 Zero-Day — [0day-rubbish] ActiveFax Server 10.70 Unauthenticated LPD Ghostscript %pipe% SYSTEM RCE (9.8)

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://seclists.org/fulldisclosure/2026/Aug/72>

> Posted by disclosure via Fulldisclosure on Aug 19 0day Rubbish Research Team is publicly disclosing a vulnerability in ActiveFax Server 10.70. Type: Unauthenticated LPD Ghostscript %pipe% SYSTEM RCE (CWE-78) CVSS: 9.8 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) Impact: Unauthenticated attacker executes arbitrary commands as SYSTEM via an LPD print job Authentication: unauthenticated / pre-auth …

---

## 10. 🟠 Zero-Day — [0day-rubbish] Tornado 2.11.3 Unauthenticated arbitrary file write to root RCE (storeTo=file: to cron) (9.8)

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://seclists.org/fulldisclosure/2026/Aug/71>

> Posted by disclosure via Fulldisclosure on Aug 19 0day Rubbish Research Team is publicly disclosing a vulnerability in Tornado 2.11.3. Type: Unauthenticated arbitrary file write to root RCE (storeTo=file: to cron) (CWE-22) CVSS: 9.8 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H) Impact: Unauthenticated attacker writes arbitrary files and achieves root command execution via cron Authentication: una…

---

## 11. 🟠 Zero-Day — [0day-rubbish] Datalore On-Premises 2026.2.3 Unauthenticated RCE via InteractiveReport access-mapping flaw (9.8)

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://seclists.org/fulldisclosure/2026/Aug/70>

> Posted by disclosure via Fulldisclosure on Aug 19 0day Rubbish Research Team is publicly disclosing a vulnerability in Datalore On-Premises 2026.2.3. Type: Unauthenticated RCE via InteractiveReport access-mapping flaw (CWE-306) CVSS: 9.8 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H) Impact: Anonymous attacker executes arbitrary code in the notebook agent container Authentication: unauthenticated …

---

## 12. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

---

## 13. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

---

## 14. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

---

## 15. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

---

## 16. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 17. 🟠 Zero-Day — Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite

**CVE:** `CVE-2025-66376` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Tue, 21 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a>

> Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite Executive summary A group of Russian state-supported cyber actors has been targeting and compromising various Western government and commercial organizations using the Zimbra Collaboration Suite (ZCS) software since at least July 2025. The Russian state-supported advanced persistent threat …

---

## 18. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

---

## 19. 🟠 Zero-Day — [0day-rubbish] VMS 6.48.809 Authenticated command injection to root RCE (8.8)

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://seclists.org/fulldisclosure/2026/Aug/76>

> Posted by disclosure via Fulldisclosure on Aug 19 0day Rubbish Research Team is publicly disclosing a vulnerability in VMS 6.48.809. Type: Authenticated command injection to root RCE (CWE-78) CVSS: 8.8 (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H) Impact: Authenticated attacker executes arbitrary commands as root via unsanitized command injection Authentication: authenticated Full technical analy…

---

## 20. 🟠 Zero-Day — [0day-rubbish] Gemini 7.3.0 Authenticated SQL injection to xp_cmdshell RCE (8.8)

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://seclists.org/fulldisclosure/2026/Aug/74>

> Posted by disclosure via Fulldisclosure on Aug 19 0day Rubbish Research Team is publicly disclosing a vulnerability in Gemini 7.3.0. Type: Authenticated SQL injection to xp_cmdshell RCE (CWE-89) CVSS: 8.8 (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H) Impact: Authenticated user executes OS commands via stacked SQL and xp_cmdshell as sa/sysadmin Authentication: authenticated Full technical analysis…

---

## 21. 🟡 High Severity — Mailpit: WebSocket origin check bypass via percent-encoded path (regression of CVE-2026-22689)

**CVE:** `CVE-2026-67448` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://github.com/advisories/GHSA-8r62-w5wh-fc5m>

> ## Summary

The cross-site WebSocket hijacking fix was reimplemented as an origin check gated on a raw-URI prefix test, but Go&#x27;s ServeMux routes on the percent-decoded path, so requesting /%61pi/events reaches the WebSocket handler while skipping the only origin control, and the upgrader itself accepts every origin. Confirmed at HEAD 408b30d. Affects 1.29.0 through 1.30.5.

## The defect

Two…

---

## 22. 🟡 High Severity — gettext-converter: Prototype pollution in js2i18next() via crafted translation keys

**CVE:** `CVE-2026-55451` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://github.com/advisories/GHSA-f4jp-rw7w-ccwg>

> ### Impact

`js2i18next()` is vulnerable to prototype pollution. When converting translations, it splits nested keys on the key separator (default `##`) and uses each segment as a dynamic object key while building the output object. A key whose segment is `__proto__` (e.g. `__proto__##gcPolluted`) causes the converter to resolve `Object.prototype` as the nested write target and assign the translat…

---

## 23. 🟡 High Severity — Winter: Authenticated Twig sandbox escape in CMS SecurityPolicy (bypass of CVE-2024-54149)

**CVE:** `CVE-2024-54149` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://github.com/advisories/GHSA-8cfw-pcwh-v63w>

> ### Impact

Affected versions of Winter CMS allow authenticated backend users with CMS template-editing permissions to escape the Twig sandbox (&quot;safe mode&quot;) that is meant to restrict what template code can do. Using any of the following permissions, an attacker can read and modify arbitrary database records, execute arbitrary SQL (including DDL such as `DROP TABLE`), exfiltrate sensitive…

---

## 24. 🟡 High Severity — netty-incubator-codec-ohttp BinaryHttpParser: Unauthenticated CPU-exhaustion DoS via infinite loop in field-section decoding

**CVE:** `CVE-2026-63202` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://github.com/advisories/GHSA-4899-mpch-38p3>

> # BinaryHttpParser: Unauthenticated CPU-exhaustion DoS via infinite loop in field-section decoding

- **ID:** BHTTP-LOOP-001
- **Severity:** High
- **CVSS v3.1:** 7.5 — `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H`
- **CWE:** CWE-835 (Loop with Unreachable Exit Condition) — secondary CWE-400 (Uncontrolled Resource Consumption)
- **Affected component:** `codec-bhttp` → `io.netty.incubator.codec.bh…

---

## 25. 🟡 High Severity — Laravel Backpack CRUD: HasMany/MorphMany relation fields allow cross-tenant record re-parenting (IDOR) via attachManyRelation

**CVE:** `CVE-2026-57570` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://github.com/advisories/GHSA-42vx-43vc-x6pr>

> ## Vulnerability Details

Affected area: HasMany / MorphMany relation handling during CRUD create and update operations  
CWE: CWE-862 — Missing Authorization  
Severity: Medium  
CVSS: 6.5 — CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:N

### Summary

Backpack CRUD contained an authorization issue in the way certain HasMany and MorphMany relationship fields were processed during create and update o…

---

## 26. 🟡 High Severity — django CMS: Clipboard copy IDOR discloses unauthorized plugin content

**CVE:** `CVE-2026-54622` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://github.com/advisories/GHSA-4xfr-4p46-gc6p>

> ### Summary
  The clipboard copy paths of the `copy_plugins` admin endpoint validate only   the target (the user&#x27;s own clipboard) and skip source-side authorization. A staff user can copy plugins out of a placeholder they have no permission on   into their clipboard, then read the (secret) content.

  ### Details
  In `cms/admin/placeholderadmin.py`, `_copy_plugin_to_clipboard` and   `_copy_p…

---

## 27. 🟡 High Severity — Wagtail: Improper permission handling in image preview

**CVE:** `CVE-2026-54261` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://github.com/advisories/GHSA-r6p4-grq7-xm4m>

> ### Impact
Due to a missing permission check on the image preview endpoint, a user with access to the Wagtail admin can preview any image. The existing data of the image object itself is not exposed. The vulnerability is not exploitable by an ordinary site visitor without access to the Wagtail admin.

### Patches
Patched versions have been released as Wagtail 7.0.8, 7.3.3, 7.4.2.

### Workarounds
…

---

## 28. 🟡 High Severity — Wagtail: Improper restriction handling on Documents and Images chosen endpoints

**CVE:** `CVE-2026-54259` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://github.com/advisories/GHSA-h54r-xq46-qwqm>

> ### Impact
The Documents and Images chooser&#x27;s chosen endpoint incorrectly listed items for which the user has not been granted choose permission. A user with access to the Wagtail admin could see the filename and name and URLs of documents and images in those collections.

The vulnerability is not exploitable by an ordinary site visitor without access to the Wagtail admin.

### Patches
Patche…

---

## 29. 🟡 High Severity — netty-incubator-codec-ohttp: [OHttpServerCodec] Native Direct-Memory Leak on AEAD Decryption Failure Leads to Gateway Denial of Service

**CVE:** `CVE-2026-54251` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://github.com/advisories/GHSA-vmr9-j6wf-pmh2>

> The **netty-incubator-codec-ohttp** library implements Oblivious HTTP (OHTTP) gateway and client functionality using Netty&#x27;s `ByteBuf` memory management. When an OHTTP gateway processes encrypted client requests, it allocates a pooled direct (native off-heap) `ByteBuf` to hold the decrypted plaintext before the AEAD tag is verified. If the AEAD tag check fails — meaning the ciphertext is inva…

---

## 30. 🟡 High Severity — Fleet: SQL injection in Okta conditional access endpoint allows host-controlled compromise of the Fleet database

**CVE:** `CVE-2026-54245` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://github.com/advisories/GHSA-7q96-f8xw-jv5j>

> ### Summary

A SQL injection vulnerability in Fleet&#x27;s Okta conditional access integration could allow an attacker who controls a single enrolled host to read or modify arbitrary data in the Fleet database, including stored session tokens. Disclosed session tokens may be replayed to act as a global administrator, which on a managed fleet leads to remote code execution on enrolled hosts.

### I…

---

## 31. 🟡 High Severity — Laravel Backpack CRUD: OS command injection in Stats::makeCurlRequest via attacker-controlled Host header (pre-auth)

**CVE:** `CVE-2026-54182` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://github.com/advisories/GHSA-mrc5-3mm3-45c5>

> ## Summary

`Backpack\CRUD\Stats::makeCurlRequest` builds a shell command using unescaped input that originates from the HTTP `Host` header, then passes it to `exec()`. A specially crafted Host header can break out of the shell argument and cause the server to execute arbitrary OS commands as the web user.

The vulnerable code path is reached from `BackpackServiceProvider::boot()` on every HTTP re…

---

## 32. 🟡 High Severity — Laravel Backpack CRUD: CRUD panel query scopes are not enforced on Update, Delete, and Reorder (cross-tenant IDOR)

**CVE:** `CVE-2026-54180` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://github.com/advisories/GHSA-vgmv-8xjc-6rch>

> ## Summary

Backpack CRUD&#x27;s list and read operations correctly apply any query scopes
registered via `addClause()` / `addBaseClause()` (e.g. tenant isolation, user
ownership). However, the **Update**, **Delete**, and **Reorder** operations
bypassed these scopes, fetching records directly from the unscoped model query.

An authenticated user who knows or can guess a record&#x27;s primary key c…

---

## 33. 🟡 High Severity — Laravel Backpack CRUD: HasUploadFields keeps the attacker-supplied file extension — public-disk uploads of `shell.php` reach the webserver

**CVE:** `CVE-2026-54177` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://github.com/advisories/GHSA-8q2w-pv9p-mjvc>

> ## Summary

`HasUploadFields` (used via `CrudTrait` on Backpack-managed models) and the `withFiles()` uploader preserve the client-supplied file extension without validation. On installations using a `public` disk with `php artisan storage:link`, this allows an authenticated administrator to upload a file with a server-executable extension that the web server will pass to the PHP interpreter - if …

---

## 34. 🟡 High Severity — Tekton Pipelines-as-Code: Unscoped GitHub App installation token allows unauthorized access to private repositories via remote task resolution

**CVE:** `CVE-2026-54168` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://github.com/advisories/GHSA-6f2p-296r-cc28>

> ### Impact
When Pipelines-as-Code is configured with a GitHub App installed across multiple repositories, the installation token issued during webhook processing is not scoped to the triggering repository by default. The token retains access to all repositories in the GitHub App installation.

This allows a user with push access to any repository in the installation to craft a PipelineRun with a r…

---

## 35. 🟡 High Severity — Pipelines-as-Code GitHub App token request can be redirected via untrusted Enterprise Host header

**CVE:** `CVE-2026-54167` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://github.com/advisories/GHSA-f5f4-3hh4-f54m>

> ## Impact

Pipelines-as-Code installations using the GitHub App provider are vulnerable to GitHub App credential exfiltration through the webhook endpoint.

Affected versions accepted the `X-GitHub-Enterprise-Host` request header as the GitHub Enterprise API host during GitHub App token generation. For GitHub webhook events containing an `installation.id`, Pipelines-as-Code generated a GitHub App …

---

## 36. 🟡 High Severity — Ember has unneutralized terminal escape/control sequences from Caddy logs injected into the operator's TUI

**CVE:** `CVE-2026-54162` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://github.com/advisories/GHSA-x3g7-qrwc-f6c5>

> ## Summary

Ember&#x27;s interactive TUI renders fields taken from the monitored Caddy server&#x27;s access logs — most notably the request URI — straight to the operator&#x27;s terminal without neutralising terminal escape or control sequences (CWE-150). Those log fields are populated from arbitrary, unauthenticated HTTP requests, so any remote client can embed ANSI/OSC/CSI control bytes that the…

---

## 37. 🟡 High Severity — node-opcua missing nonce verification in UserNameIdentityToken authentication

**CVE:** `CVE-2026-54155` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://github.com/advisories/GHSA-mq36-523m-x7vv>

> **Summary**
A missing nonce verification in the UserNameIdentityToken authentication handler allows an unauthenticated remote attacker to forge a password token that extracts as an empty string, and to replay captured authentication tokens across sessions.

**Affected versions:** &lt;= 2.165.0
**Tested version:** 2.165.0
**CVSS Score:** 8.1 (High)
**CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/…

---

## 38. 🟡 High Severity — next-video: Unauthenticated arbitrary file read via /api/video request handler

**CVE:** `CVE-2026-54150` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://github.com/advisories/GHSA-2p39-2jf3-fv2q>

> ### Impact

The HTTP route handler exported by `next-video/request-handler` — which the README instructs consumers to mount at `/api/video` — allows an unauthenticated remote attacker to read arbitrary `.json` files from the production filesystem of any application following the documented setup.

The handler&#x27;s `GET` endpoint accepts a `url` query parameter and uses it to locate and serve a J…

---

## 39. 🟡 High Severity — LangChain MongoDB has NoSQL Operator Injection in MongoDBSaver.list() leading to cross-tenant data exposure

**CVE:** `CVE-2026-55253` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://github.com/advisories/GHSA-533j-2v4q-mw5h>

> # Executive Summary

A NoSQL injection issue exists in the langgraph-checkpoint-mongodb and
langgraph-store-mongodb libraries. MongoDBSaver.list() and MongoDBStore.search() methods
accept a filter parameter that is incorporated into MongoDB queries without sufficient validation.
Because MongoDB query operator keys (those prefixed with $) are not rejected during filter
construction, a caller with c…

---

## 40. 🟡 High Severity — Critical GitLab Flaw Exploited Shortly After Disclosure

**CVE:** `CVE-2026-19478` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://www.securityweek.com/critical-gitlab-flaw-exploited-shortly-after-disclosure/>

> CVE-2026-19478 can be exploited without authentication to modify or delete public projects and user data. The post Critical GitLab Flaw Exploited Shortly After Disclosure appeared first on SecurityWeek .

---

## 41. 🟡 High Severity — Cudy WR3000: Hard-coded JWT Secret to Root Command Injection

**CVE:** `CVE-2026-71960` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-08-20
**Reference:** <https://seclists.org/fulldisclosure/2026/Aug/68>

> Posted by Nir Yehoshua on Aug 19 Hello Full Disclosure list, Cipher Security Labs has published details for two vulnerabilities affecting Cudy WR3000 hardware revision 2.0 running firmware before version 2.5.24. CVE-2026-71960 - Hard-coded JWT Secret Authentication Bypass Severity: Critical, CVSS 9.3 The device firmware contains a hard-coded HMAC signing secret used by the Mosquitto MQTT JWT authe…

---

## 42. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
