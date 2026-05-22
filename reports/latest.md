# Zero Day Pulse

> **Generated:** 2026-05-22 20:13 UTC &nbsp;|&nbsp; **Total:** 32 &nbsp;|&nbsp; 🔴 KEV: 1 &nbsp;|&nbsp; 🟠 Zero-Day: 13 &nbsp;|&nbsp; 🟡 High: 18 &nbsp;|&nbsp; ✨ Enriched: 0

---

## 1. 🔴 CISA KEV — CVE-2026-9082 — Drupal Core SQL Injection Vulnerability

**CVE:** `CVE-2026-9082` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-05-22
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-9082>

> Vendor: Drupal | Product: Core. Drupal Core contains a SQL injection vulnerability that could allow for privilege escalation and remote code execution via specially crafted requests sent with the database abstraction API. Required action: Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavaila…

---

## 2. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

---

## 3. 🟠 Zero-Day — We hardened zizmor's GitHub Actions static analyzer

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Trail of Bits Blog &nbsp;|&nbsp; **Published:** 2026-05-22
**Reference:** <https://blog.trailofbits.com/2026/05/22/we-hardened-zizmors-github-actions-static-analyzer/>

> In March 2026, attackers exploited a pull_request_target misconfiguration in the aquasecurity/trivy-action GitHub Action to exfiltrate organization and repository secrets, then used those credentials to backdoor LiteLLM on PyPI (see Trivy’s post-mortem for the full timeline). zizmor is a static analyzer that GitHub Actions users run to catch exactly these misconfigurations before they ship. When G…

---

## 4. 🟠 Zero-Day — Pydantic AI: SSRF cloud-metadata blocklist bypass via IPv4-mapped IPv6 (Incomplete fix of CVE-2026-25580)

**CVE:** `CVE-2026-46678` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-21
**Reference:** <https://github.com/advisories/GHSA-cqp8-fcvh-x7r3>

> ## Summary

When an application using Pydantic AI opts a URL into `force_download=&#x27;allow-local&#x27;` (which disables the default block on private/internal IPs), the cloud-metadata blocklist could be bypassed by encoding the metadata IP in an IPv6 transition form (IPv4-mapped IPv6, 6to4, or NAT64). Dual-stack and translated networks route the IPv6 wrapper to the underlying IPv4 endpoint, expo…

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

---

## 11. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 12. 🟠 Zero-Day — Trend Micro warns of Apex One zero-day exploited in the wild

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-05-22
**Reference:** <https://www.bleepingcomputer.com/news/security/trend-micro-warns-of-apex-one-zero-day-exploited-in-attacks/>

> Japanese cybersecurity software company Trend Micro has addressed an Apex One zero-day vulnerability exploited in attacks targeting Windows systems. [...]

---

## 13. 🟠 Zero-Day — Paved With Intent: ROADtools and Nation-State Tactics in the Cloud

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Unit 42 (Palo Alto) &nbsp;|&nbsp; **Published:** 2026-05-22
**Reference:** <https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/>

> Open-source framework ROADtools is being misused by threat actors for cloud intrusions. Learn how to identify its malicious use. The post Paved With Intent: ROADtools and Nation-State Tactics in the Cloud appeared first on Unit 42 .

---

## 14. 🟠 Zero-Day — TrendAI Patches Apex One Zero-Day Exploited in the Wild

**CVE:** `CVE-2026-34926` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-05-22
**Reference:** <https://www.securityweek.com/trendai-patches-apex-one-zero-day-exploited-in-the-wild/>

> CVE-2026-34926 is a directory traversal flaw that can be exploited against the on-premise version of Apex One. The post TrendAI Patches Apex One Zero-Day Exploited in the Wild appeared first on SecurityWeek .

---

## 15. 🟡 High Severity — CISA Adds Exploited Langflow and Trend Micro Apex One Vulnerabilities to KEV

**CVE:** `CVE-2025-34291` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-22
**Reference:** <https://thehackernews.com/2026/05/cisa-adds-exploited-langflow-and-trend.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Thursday added two security flaws impacting Langflow and Trend Micro Apex One to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

The vulnerabilities in question are listed below -


  CVE-2025-34291 (CVSS score: 9.4) - An origin validation error vulnerability in Langflow that could

---

## 16. 🟡 High Severity — Network-AI: Unauthenticated Cross-Origin MCP Tool Invocation via Empty Default Secret

**CVE:** `CVE-2026-46701` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-21
**Reference:** <https://github.com/advisories/GHSA-j3vx-cx2r-pvg8>

> # Unauthenticated Cross-Origin MCP Tool Invocation via Empty Default Secret

| Field            | Value |
| ---------------- | ----- |
| Repository       | Jovancoding/Network-AI |
| Affected version | v5.4.4 (commit c12686e181f231cf8d7bcf836a96d78f0f0877ac) |

## Summary

The MCP SSE server defaults to an empty secret (`process.env[&#x27;NETWORK_AI_MCP_SECRET&#x27;] ?? &#x27;&#x27;` at `bin/mcp-s…

---

## 17. 🟡 High Severity — Boxlite: Path Traversal Vulnerability Leads to Arbitrary File Write on the Host

**CVE:** `CVE-2026-46703` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-21
**Reference:** <https://github.com/advisories/GHSA-f396-4rp4-7v2j>

> #### Summary

Boxlite is a sandbox service that allows users to create lightweight virtual machines (Boxes) and run OCI containers within them. Boxlite allows users to specify the OCI image used by containers in the sandbox. However, when processing tar entries in OCI images, Boxlite does not account for the possibility that entries may be symlinks pointing to absolute paths. An attacker can craft…

---

## 18. 🟡 High Severity — BoxLite: Permission Bypass Allows Modification of Read-Only Files

**CVE:** `CVE-2026-46695` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-21
**Reference:** <https://github.com/advisories/GHSA-g6ww-w5j2-r7x3>

> #### Summary

Boxlite is a sandbox service that allows users to create lightweight virtual machines (Boxes) and launch OCI containers within them to run untrusted code.

One of the core security features claimed by Boxlite is the ability to mount host directories in read-only mode (read_only=True) into the VM via the virtiofs protocol (a host-guest shared filesystem protocol designed specifically …

---

## 19. 🟡 High Severity — containerd user ID handling bypass allows runAsNonRoot evasion

**CVE:** `CVE-2026-46680` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-21
**Reference:** <https://github.com/advisories/GHSA-fqw6-gf59-qr4w>

> ### Impact
A bug was found in containerd where containers launched with a numeric `User` directive that cannot be parsed as a 32-bit integer are incorrectly treated as a username. If a crafted image provides an `/etc/passwd` file mapping this large numeric string to root, the container ultimately runs as root (UID 0). This allows the Kubernetes `runAsNonRoot` restriction to be bypassed, causing un…

---

## 20. 🟡 High Severity — Twig: Arbitrary PHP code execution via `_self.(<string>)` macro-reference compilation

**CVE:** `CVE-2026-46640` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-21
**Reference:** <https://github.com/advisories/GHSA-45vw-wh46-2vx8>

> ### Description

The `obj.(expr)` dynamic-attribute syntax (added in 3.15.0 as the replacement for the deprecated `attribute()` function) lets the attribute be an arbitrary expression. When the receiver is `_self` (or any `{% import %}` alias) and the parenthesised expression is a string literal, `DotExpressionParser` short-circuits to the macro-call path and concatenates the attacker-controlled s…

---

## 21. 🟡 High Severity — Twig: `template_from_string()` escapes a SourcePolicy-driven sandbox via synthesized template name

**CVE:** `CVE-2026-46634` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-21
**Reference:** <https://github.com/advisories/GHSA-24x9-r6q4-q93w>

> ### Description

When the sandbox is enabled selectively via `SourcePolicyInterface` (and not globally), a sandboxed template that is allowed to call `template_from_string` and `include` can render an arbitrary inner template with no security policy enforcement.

`Environment::createTemplate()` compiles the inner string under a synthesized name (`__string_template__&lt;hash&gt;`), so a name/path-b…

---

## 22. 🟡 High Severity — Twig: PHP code injection via `{% use %}` template name

**CVE:** `CVE-2026-46633` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-21
**Reference:** <https://github.com/advisories/GHSA-7p85-w9px-jpjp>

> ### Description

`Compiler::string()` escapes `&quot;`, `$`, `\`, NUL and TAB when generating PHP double-quoted string literals, but does not escape single quotes. In `ModuleNode::compileConstructor()`, the template name from a `{% use %}` tag is compiled via `subcompile()` -&gt; `string()` and placed inside a surrounding PHP single-quoted string literal. A template name containing a single quote …

---

## 23. 🟡 High Severity — twig/intl-extra: Unbounded formatter memoisation in keyed on template-controlled arguments

**CVE:** `CVE-2026-46629` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-21
**Reference:** <https://github.com/advisories/GHSA-35wc-cvqg-78fp>

> ### Description

`IntlExtension` memoises every `\IntlDateFormatter` and `\NumberFormatter` it creates in instance-level arrays keyed on a hash that includes `locale`, `pattern`, `attrs` and other values that are ordinary named arguments of the `format_datetime` / `format_date` / `format_time` / `format_number` / `format_currency` filters. There is no size limit and no eviction.

A template that i…

---

## 24. 🟡 High Severity — Russh: Unchecked CryptoVec allocation and growth handling is reachable

**CVE:** `CVE-2026-46673` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-21
**Reference:** <https://github.com/advisories/GHSA-g9f8-wqj9-fjw5>

> ### Title
Unchecked `CryptoVec` allocation and growth handling was reachable from local agent inputs in current `russh` releases and from remote SSH traffic in historical pre-`0.58.0` releases

### Summary
`CryptoVec` used unchecked capacity growth, unchecked length arithmetic, and unsafe allocation/locking paths. In current `russh` releases, local SSH agent peers could still feed attacker-control…

---

## 25. 🟡 High Severity — FlaskBB: SSRF in get_image_info() via unrestricted avatar URL

**CVE:** `CVE-2026-46556` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-21
**Reference:** <https://github.com/advisories/GHSA-xq32-9g7q-7297>

> ###Summary
A Server-Side Request Forgery (SSRF) vulnerability in get_image_info() allows any authenticated user to force the server to send HTTP requests to arbitrary internal endpoints, including cloud metadata services (e.g., AWS 169.254.169.254). This is a blind SSRF with confirmed internal port scanning and internal API triggering capabilities. CVSS 6.5 Medium.

###Details
In flaskbb/utils/hel…

---

## 26. 🟡 High Severity — NocoDB: Missing File Size Enforcement in Upload-by-URL Allows Denial of Service via Disk Exhaustion

**CVE:** `CVE-2026-46551` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-21
**Reference:** <https://github.com/advisories/GHSA-99vc-2jx2-688p>

> ### Summary

The `uploadViaURL` path in the v1/v2 attachment API did not enforce `NC_ATTACHMENT_FIELD_SIZE` against the remote `content-length` or against the response stream. An authenticated user (Editor+) could direct the server to download arbitrarily large files, exhausting disk space and causing denial of service.

### Details

In `packages/nocodb/src/services/attachments.service.ts`, the HE…

---

## 27. 🟡 High Severity — NocoDB: OAuth Token Scope Not Enforced at ACL Layer Allows Scope Escalation

**CVE:** `CVE-2026-46549` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-21
**Reference:** <https://github.com/advisories/GHSA-m5qg-rvjq-727p>

> ### Summary

The OAuth token strategy attached `oauth_scope` and `oauth_granted_resources` to the request user, but the ACL middleware never consulted either. An OAuth token issued with a restricted scope (e.g. MCP-only) therefore inherited the full permissions of the underlying user across all routes; the `granted_resources.base_id` restriction was bypassed on org-level endpoints that don&#x27;t …

---

## 28. 🟡 High Severity — NocoDB: SSRF Protection Bypass in Notification Webhook Plugins (Slack, Discord, Mattermost, Teams)

**CVE:** `CVE-2026-46548` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-21
**Reference:** <https://github.com/advisories/GHSA-2c5x-4jgf-88mj>

> ### Summary

The `request-filtering-agent` SSRF protection was non-functional in the four notification webhook plugins (Slack, Discord, Mattermost, Teams) because `httpAgent` / `httpsAgent` were passed as part of the request **body** rather than the axios **config**. An authenticated user with hook-creation permission could direct outbound POST requests to arbitrary internal hosts.

### Details

`…

---

## 29. 🟡 High Severity — MCP Server Kubernetes: Tool Access Control Bypass via Presentation-Layer Filtering Without Execution-Layer Enforcement

**CVE:** `CVE-2026-46519` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-21
**Reference:** <https://github.com/advisories/GHSA-cr22-wjx7-2w6m>

> ## Summary

`mcp-server-kubernetes` exposes three environment variables (`ALLOW_ONLY_READONLY_TOOLS`, `ALLOW_ONLY_NON_DESTRUCTIVE_TOOLS`, `ALLOWED_TOOLS`) documented as access controls for restricting which Kubernetes operations are available. These controls are enforced at the tool discovery layer (`tools/list`) but not at the execution layer (`tools/call`). Any client that knows a tool name can …

---

## 30. 🟡 High Severity — Snappy : SSRF and local file read via the xsl-style-sheet option

**CVE:** `CVE-2026-46683` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-21
**Reference:** <https://github.com/advisories/GHSA-c5fp-p67m-gq56>

> ### Impact

It impacts applications where:
- the PHP daemon run with root permissions ;
- the application is either running outside a container or has sensitive file access ;

It could happens with this kind of workflows:

```php
$stylesheet = $_GET[&#x27;stylesheet&#x27;]; // = ‘file:///etc/passwd’
$pdf = new Knp\Snappy\Pdf(‘/usr/local/bin/wkhtmltopdf’);
 $pdf-&gt;generate(‘page.html’, ‘out.pdf’,…

---

## 31. 🟡 High Severity — Fission runtime pods automount the fission-fetcher service-account token into the user function   container, granting function code namespace-wide secret / configmap read

**CVE:** `CVE-2026-46617` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-21
**Reference:** <https://github.com/advisories/GHSA-85g2-pmrx-r49q>

> ### Summary

Fission runtime pods were created with `ServiceAccountName: fission-fetcher`, and the `fission-fetcher` ServiceAccount was granted namespace-wide `get` on `secrets` and `configmaps` (it needs that to load function code, env vars, and config). The runtime pod&#x27;s automounted token was reachable from inside the user&#x27;s function container at `/var/run/secrets/kubernetes.io/service…

---

## 32. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
