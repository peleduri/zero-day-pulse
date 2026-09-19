# Zero Day Pulse

> **Generated:** 2026-09-19 01:58 UTC &nbsp;|&nbsp; **Total:** 26 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 11 &nbsp;|&nbsp; 🟡 High: 15 &nbsp;|&nbsp; ✨ Enriched: 0

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

## 3. 🟠 Zero-Day — Convoy: Cross-Tenant Source IDOR Leaks Plaintext Message Broker Credentials

**CVE:** `CVE-2026-81505` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-p5vg-v7mj-f6q4>

> ## Summary
frain-dev/convoy (all versions up to and including v26.6.2, no patch
available) lets any authenticated caller who is authorized on at least one
project read ANY OTHER project&#x27;s &quot;Source&quot; record by ID via
GET /api/v1/projects/{projectID}/sources/{sourceID} -- regardless of whether
that Source actually belongs to the project named in the URL. The response
includes the Source…

---

## 4. 🟠 Zero-Day — ToolHive: containerized MCP servers can reach host services via host.docker.internal, enabling lateral movement

**CVE:** `CVE-2026-58197` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-qg2g-g9w3-m5h8>

> ## Summary

A containerized MCP server running with the default `network` permission profile (`insecure_allow_all: true`) can reach host-local services via `host.docker.internal`. This includes the ToolHive API itself, other ToolHive-managed MCP server proxies, and any other service listening on the host&#x27;s localhost. Combined with the unauthenticated ToolHive API and MCP proxy endpoints, this…

---

## 5. 🟠 Zero-Day — A Vault with a Heap-View: The Uncomfortable Space Between AgentCore Harness and Identity

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Unit 42 (Palo Alto) &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://unit42.paloaltonetworks.com/securing-aws-agentcore-harness-credentials/>

> Analysis of how default configurations in AWS AgentCore Harness allow prompt injection to exfiltrate credentials, and key steps to secure your agents. The post A Vault with a Heap-View: The Uncomfortable Space Between AgentCore Harness and Identity appeared first on Unit 42 .

---

## 6. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

---

## 7. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

---

## 8. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

---

## 9. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

---

## 10. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 11. 🟠 Zero-Day — Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite

**CVE:** `CVE-2025-66376` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Tue, 21 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a>

> Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite Executive summary A group of Russian state-supported cyber actors has been targeting and compromising various Western government and commercial organizations using the Zimbra Collaboration Suite (ZCS) software since at least July 2025. The Russian state-supported advanced persistent threat …

---

## 12. 🟡 High Severity — Mnemosyne has JWT signature verification bypass sync server that allows authentication bypass

**CVE:** `CVE-2026-59163` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-xcw4-53cc-hv32>

> ### Summary

The Mnemosyne sync server&#x27;s authentication check decoded JWT bearer tokens but never verified their HMAC-SHA256 signatures. Any well-formed token was accepted, allowing an unauthenticated attacker to impersonate any user and read or modify their sync data.

**Severity: Critical**

CVSS 3.1: AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N = 9.1

Assumes the sync server endpoint is network-rea…

---

## 13. 🟡 High Severity — Perses's missing authorization in datasource proxy allows cross-scope secret disclosure

**CVE:** `CVE-2026-63199` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-4227-9989-jrhx>

> ### Impact

The datasource proxy authorizes the caller on the Datasource scope, then resolves and decrypts any Secret named in the request body with no Secret-scope check.

Datasource and Secret are distinct, independently grantable role scopes, so an operator can grant datasource access without secret access. The proxy and the service to create a datasource does not verify that the operator has t…

---

## 14. 🟡 High Severity — Perses's project query parameter authorization bypass exposes cross-project resources

**CVE:** `CVE-2026-63458` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-cjgj-2fwf-4c2w>

> ### Impact
_What kind of vulnerability is it?_

An authenticated user who is only a viewer on project team-a requests GET /api/v1/projects/team-a/dashboards?project=finance-secret (or simply GET /api/v1/datasources?project=finance-secret) and receives the full list of the finance-secret project&#x27;s dashboards and datasource specifications, despite having no role on that project. This defeats Pe…

---

## 15. 🟡 High Severity — Process Compose: Browser DNS rebinding lets websites control local process-compose MCP tools

**CVE:** `CVE-2026-77339` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-5gm3-9crp-6g3v>

> ## Summary

A malicious website can use DNS rebinding to control a developer&#x27;s local process-compose MCP SSE listener when MCP SSE is enabled. The vulnerable path accepts browser-origin requests before any Host validation, Origin validation, or caller-secret check, then dispatches the requests into process-compose MCP tools.

This advisory covers `https://github.com/F1bonacc1/process-compose`…

---

## 16. 🟡 High Severity — AnyCable: Telemetry Subsystem Contains Hardcoded Authentication Token and Transmits CLI Arguments Including Secrets

**CVE:** `CVE-2026-63406` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-w72w-9qmj-c9qm>

> ### Summary
The telemetry subsystem embeds a hardcoded auth token (`&quot;secret&quot;`) in the public source and transmits raw CLI arguments—including `--secret`, `--jwt_secret`, and `--http_rpc_secret` values—to a third-party telemetry endpoint.

### Details
In `telemetry/config.go` line 12, `var authToken = &quot;secret&quot;` is committed in the public repository and used to authenticate to `h…

---

## 17. 🟡 High Severity — AnyCable: Pusher REST API Does Not Verify Request Body MD5 Enabling Signed-Request Replay with Arbitrary Body

**CVE:** `CVE-2026-63405` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-5p54-whvp-x327>

> ### Summary
The Pusher-compatible REST API includes `body_md5` in the HMAC signature string but never computes or verifies the MD5 of the received HTTP body, allowing anyone who observes a signed request to replay it with an entirely different body.

### Details
In `pusher/http.go`, the `Handler` function extracts `body_md5` from the URL query string (line 169) and includes it verbatim in `stringT…

---

## 18. 🟡 High Severity — kcp front-proxy does not strip inbound X-Remote-* identity headers, allowing any authenticated client to inject groups/warrants and impersonate system:masters in any workspace

**CVE:** `CVE-2026-61682` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-c8w2-fgvx-vhv4>

> # Summary

The kcp front-proxy fails to strip client-supplied identity headers before forwarding requests to shards. Any authenticated tenant can inject their own `X-Remote-Group` and `X-Remote-Extra-*` headers, which the shard trusts as a verified identity assertion — allowing a low-privilege user to escalate to cluster administrator (`system:masters`) and read, write, or delete resources in any …

---

## 19. 🟡 High Severity — Capsule: Tenant owner bypasses Capsule's forbidden namespace/service/node label and annotation enforcement

**CVE:** `CVE-2026-61672` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-gjw4-3v3v-rqxg>

> ## Summary

Capsule lets a cluster administrator forbid specific metadata keys that tenant owners must not place on their own resources: `Tenant.spec.namespaceOptions.forbiddenLabels` / `forbiddenAnnotations` (namespaces), `Tenant.spec.serviceOptions.forbiddenLabels` / `forbiddenAnnotations` (Services), and the cluster-wide forbidden worker-node labels/annotations. These lists are an isolation con…

---

## 20. 🟡 High Severity — LMDeploy has Remote Code Execution by Pickle Deserialization via handle_zmq_recv in lmdeploy/lmdeploy/pytorch/disagg/conn/engine_conn.py

**CVE:** `CVE-2025-66455` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-2vh9-42vm-xmv2>

> ## Summary

LMDeploy&#x27;s PyTorch DistServe/PD-disaggregation control plane used
`recv_pyobj()` to deserialize messages received through a ZeroMQ PULL
socket. PyZMQ implements `recv_pyobj()` using Python pickle
deserialization, which can execute arbitrary code while reconstructing
an object.

The peer address used by the receiver was supplied through the
`POST /distserve/p2p_connect` HTTP endpoi…

---

## 21. 🟡 High Severity — Semantic MediaWiki affected by reflected XSS in `Special:Ask` via a forged cursor pagination token

**CVE:** `CVE-2026-77616` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-cx86-7xwp-w9wf>

> ## Reflected XSS via a forged cursor pagination token

#### Failure mode

`Special:Ask` accepts a `cursor` query parameter for keyset pagination (added in 7.0.0). The token is decoded by `CursorEncoder`, which is an **unsigned** base64url-encoded JSON blob, so its contents are fully attacker-controlled. When the cursor&#x27;s sort anchor does not match the request&#x27;s `sort=` / `order=`, `Query…

---

## 22. 🟡 High Severity — org.xwiki.rendering:xwiki-rendering-xml has an Eval Injection issue

**CVE:** `CVE-2025-53837` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-26vp-8gxg-v4pg>

> ### Impact
Any user who can edit their own user profile or any other document can execute arbitrary script macros including Groovy and Python macros that allow remote code execution including unrestricted read and write access to all wiki contents. The reason is that rendering output is included as content of HTML macros without further escaping and it is thus possible to close the HTML macro and …

---

## 23. 🟡 High Severity — Opencast: Stored XSS in Paella player via WebVTT/DFXP caption cue text

**CVE:** `CVE-2026-77615` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-m6c8-jcw2-5r25>

> ## Summary

The Opencast Paella player renders caption cue text into `innerHTML` without escaping. The captions canvas clears `_captionsContainer.innerHTML` and then appends each active cue with `_captionsContainer.innerHTML += cue`, so HTML inside a WebVTT or DFXP cue becomes live DOM and executes in the Opencast origin.

The caption track is read from any media package element with a `captions/*…

---

## 24. 🟡 High Severity — Microsoft Patches CVSS 10.0 Azure AI Foundry Flaw Enabling Unauthorized Privilege Escalation

**CVE:** `CVE-2026-85889` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://thehackernews.com/2026/09/microsoft-patches-cvss-100-azure-ai.html>

> Microsoft has released fixes for a maximum-severity security flaw in Azure AI Foundry that could be exploited to achieve privilege escalation. No customer action is required.

The vulnerability, tracked as CVE-2026-85889, carries a CVSS score of 10.0.

&quot;Missing authentication for critical function in Azure AI Foundry allows an unauthorized attacker to elevate privileges over a network,&quot;

---

## 25. 🟡 High Severity — Critical Orkes Conductor Vulnerability Exploited in Attacks

**CVE:** `CVE-2026-58138` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://www.securityweek.com/critical-orkes-conductor-vulnerability-exploited-in-attacks/>

> CVE-2026-58138 is an unauthenticated remote code execution vulnerability that attackers can exploit via inline workflow definitions. The post Critical Orkes Conductor Vulnerability Exploited in Attacks appeared first on SecurityWeek .

---

## 26. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
