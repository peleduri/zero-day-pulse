# Zero Day Pulse

> **Generated:** 2026-08-20 00:31 UTC &nbsp;|&nbsp; **Total:** 24 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 15 &nbsp;|&nbsp; 🟡 High: 9 &nbsp;|&nbsp; ✨ Enriched: 0

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

## 3. 🟠 Zero-Day — SearXNG MCP Server is Vulnerable to SSRF in web_url_read: the internal-address guard is disabled by default (MCP_HTTP_HARDEN off)

**CVE:** `CVE-2026-54688` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-19
**Reference:** <https://github.com/advisories/GHSA-q87f-qc2r-2gw4>

> Ref: https://github.com/ihor-sokoliuk/mcp-searxng/issues/87#issuecomment-4645453694


### Summary
The web_url_read tool fetches a caller-supplied URL server-side and converts it to markdown. An SSRF guard (assertUrlAllowed, which blocks private/loopback/metadata addresses) exists but runs only when MCP_HTTP_HARDEN=true, which is off by default. So in the default configuration there is no internal-…

---

## 4. 🟠 Zero-Day — langgraph-api: Incomplete assistant authorization in LangGraph Server run creation

**CVE:** `CVE-2026-55236` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-19
**Reference:** <https://github.com/advisories/GHSA-jfj5-wrj9-63x4>

> ## Summary

In affected versions of `langgraph-api` (the LangGraph Server runtime), the run-creation path authorized the assistant attached to a run using a different authorization event than the rest of the assistant-handling code paths. Direct assistant reads and cron creation dispatch the `assistants.read` authorization event; run creation dispatched `assistants.search` with an incomplete value…

---

## 5. 🟠 Zero-Day — langgraph-api: Relative webhook targets in LangGraph Server can reach in-process routes without authentication

**CVE:** `CVE-2026-55235` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-19
**Reference:** <https://github.com/advisories/GHSA-2c9q-c2q9-qgqv>

> ## Summary

In affected versions of `langgraph-api` (the LangGraph Server runtime), a run or cron could be created with a relative webhook target. When the server later delivers such a webhook, it routes the request back into the same application through an in-process loopback transport that the authentication middleware treats as internal and does not authenticate. As a result, a relative webhook…

---

## 6. 🟠 Zero-Day — CVE-2026-19490: Critical Vulnerability Affecting Citrix NetScaler ADC and NetScaler Gateway

**CVE:** `CVE-2026-19490` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-08-19
**Reference:** <https://www.rapid7.com/blog/post/etr-cve-2026-19490-critical-vulnerability-affecting-citrix-netscaler-adc-and-netscaler-gateway>

> Overview On August 19, 2026, a security advisory was published for CVE-2026-19490 , a critical authentication bypass vulnerability affecting Citrix NetScaler ADC and NetScaler Gateway. The vulnerability carries a CVSS v4.0 base score of 9.3 and can be exploited remotely by an unauthenticated attacker over the network without user interaction or elevated privileges. NetScaler ADC and NetScaler Gate…

---

## 7. 🟠 Zero-Day — Critical macOS, SharePoint, vCenter, and Microsoft IKE Flaws Under Active Exploitation

**CVE:** `CVE-2026-65400` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-08-19
**Reference:** <https://thehackernews.com/2026/08/critical-macos-sharepoint-vcenter-and.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added four critical vulnerabilities to its Known Exploited Vulnerabilities (KEV) catalog, stating they are being exploited in the wild.

The shortcomings added to the KEV catalog are listed below -


  CVE-2026-65400 (CVSS score: 9.8) - An improper authentication vulnerability impacting Apple macOS that could allow an

---

## 8. 🟠 Zero-Day — Critical RCE flaw in Windows IKE Extension now actively exploited

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-08-19
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-critical-windows-ike-extension-flaw-now-exploited-in-attacks/>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) warned that hackers are exploiting a critical-severity remote code execution (RCE) flaw in the Windows Internet Key Exchange (IKE) Service Extensions component. [...]

---

## 9. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

---

## 10. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

---

## 11. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

---

## 12. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

---

## 13. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 14. 🟠 Zero-Day — Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite

**CVE:** `CVE-2025-66376` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Tue, 21 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a>

> Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite Executive summary A group of Russian state-supported cyber actors has been targeting and compromising various Western government and commercial organizations using the Zimbra Collaboration Suite (ZCS) software since at least July 2025. The Russian state-supported advanced persistent threat …

---

## 15. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

---

## 16. 🟡 High Severity — Tina: Broken Access Control: arbitrary bucket-key write/delete in `next-tinacms-s3` (and sibling production media adapters)

**CVE:** `CVE-2026-59992` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-19
**Reference:** <https://github.com/advisories/GHSA-8mq9-5fw2-5rm4>

> ## Summary

The production media handler shipped by `next-tinacms-s3` (`createMediaHandler` in `packages/next-tinacms-s3/src/handlers.ts`) accepts an attacker-chosen `?key=` query parameter and returns an AWS-signed `PutObject` URL whose `Key` is that value, with no check that the key falls under the operator&#x27;s configured `mediaRoot`. The same handler&#x27;s `DELETE` branch reads `objectKey =…

---

## 17. 🟡 High Severity — logto-tunnel serves files outside --experience-path via path traversal

**CVE:** `CVE-2026-63188` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-19
**Reference:** <https://github.com/advisories/GHSA-rxjr-6c9q-h67x>

> ### Summary

`@logto/tunnel` serves custom sign-in experience files from the `--experience-path` directory. When the tunnel service is reachable, a requester can use `../` path segments in a static asset request to read files outside that directory that the CLI process can read.

### Details

The tunnel command accepts `--experience-path` as the local folder path for custom sign-in experience asse…

---

## 18. 🟡 High Severity — Snipe-IT: Chained Information Disclosure and IDOR Leads to Full EULA File Takeover

**CVE:** `CVE-2026-55694` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-19
**Reference:** <https://github.com/advisories/GHSA-3hgv-jr5j-cg9x>

> ### Impact
An attacker can completely bypass file-name randomization security and without authorization download confidential, signed EULA files belonging to any other user across the application.

### Steps to Reproduce:
1. Log in as a restricted user.
2. Send a GET request to /api/v1/users/{target_id}/eulas (where target_id belongs to a restricted/denied user).
3. Observe the response leaks the …

---

## 19. 🟡 High Severity — SearXNG MCP Server: Additional hardened-mode SSRF bypasses

**CVE:** `CVE-2026-54689` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-19
**Reference:** <https://github.com/advisories/GHSA-wppf-h75h-6pm6>

> ## Summary

`mcp-searxng` has a hardened-mode URL-reading feature intended to prevent `web_url_read` from reaching private or internal network resources.

PR #79 appears to address one SSRF class: hostnames that resolve to private or internal addresses under hardened mode. I tested PR #79 locally and confirmed that it blocks the DNS-resolves-to-loopback case.

However, several other hardened-mode …

---

## 20. 🟡 High Severity — XWiki Platform Live Data Live Table Connector has privilege escalation from edit to script right through Live Data editing

**CVE:** `CVE-2026-53966` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-19
**Reference:** <https://github.com/advisories/GHSA-45ph-gxxr-gwgw>

> ### Impact
Any user who can edit a page in XWiki can use Live Data&#x27;s edit REST API in XWiki to change the rights on that page. This allows the user to obtain script right on the page. Script right allows the user to execute potentially dangerous Velocity scripts and send unfiltered HTML and JavaScript to the client. If there are other security checks, e.g., in extensions, implemented as liste…

---

## 21. 🟡 High Severity — MCP PHP SDK: client HttpTransport SSE buffer (sseBuffer .= chunk) grows unbounded when server withholds the event delimiter

**CVE:** `CVE-2026-53965` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-19
**Reference:** <https://github.com/advisories/GHSA-7m52-jw36-44r3>

> ## Summary

The HTTP client transport in `mcp/sdk` reads a Server-Sent-Events (SSE) response
stream incrementally and appends each 4 KiB chunk to an in-memory buffer
(`$this-&gt;sseBuffer .= $chunk;`) with **no upper bound**. The buffer is only ever
flushed when an SSE event delimiter (`&quot;\n\n&quot;`) appears. A remote MCP server (the
peer the client connects to) that streams response bytes wi…

---

## 22. 🟡 High Severity — Document Merge Service vulnerable to RCE via SSTI (xlsx tempaltes)

**CVE:** `CVE-2026-53964` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-19
**Reference:** <https://github.com/advisories/GHSA-w47q-945m-q9pc>

> ### Impact
A remote code execution (RCE) via server-side template injection (SSTI) allows for user supplied code to be executed in the server&#x27;s context where it is executed as the document-merge-server user with the UID 901 thus giving an attacker considerable control over the container. The vulnerability is limited to XLSX templates, were the `xltpl` library uses a npn-sandboxed Jinja enviro…

---

## 23. 🟡 High Severity — Contentful MCP Server: export_space/import_space tools pass LLM-controlled `host`/`proxy` args to CMA client, redirecting server PAT to attacker-controlled endpoint

**CVE:** `CVE-2026-53957` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-08-19
**Reference:** <https://github.com/advisories/GHSA-2xhg-73j7-rrgx>

> ### Summary

`export_space` and `import_space` tools in `@contentful/mcp-tools` accept LLM-controlled `host` and `proxy` parameters that are spread directly into the options object passed to `contentful-export` / `contentful-import`. These libraries pass the merged options — including the attacker-controlled `host` — to the Contentful Management API (CMA) SDK, which builds `baseURL` from `host` an…

---

## 24. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
