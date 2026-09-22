# Zero Day Pulse

> **Generated:** 2026-09-22 20:35 UTC &nbsp;|&nbsp; **Total:** 51 &nbsp;|&nbsp; 🔴 KEV: 4 &nbsp;|&nbsp; 🟠 Zero-Day: 21 &nbsp;|&nbsp; 🟡 High: 26 &nbsp;|&nbsp; ✨ Enriched: 0

---

## 1. 🔴 CISA KEV — CVE-2026-94127 — F5 BIG-IP APM Heap-based Buffer Overflow Vulnerability

**CVE:** `CVE-2026-94127` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-94127>

> Vendor: F5 | Product: BIG-IP APM. F5 BIG-IP APM contains a heap-based buffer overflow vulnerability when access policy and an OAuth profile are configured on a virtual server. This vulnerability could allow an unauthenticated attacker to perform remote code execution. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing S…

---

## 2. 🔴 CISA KEV — CVE-2026-93952 — Arista VeloCloud Orchestrator Improper Input Validation Vulnerability

**CVE:** `CVE-2026-93952` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-93952>

> Vendor: Arista | Product: VeloCloud Orchestrator. Arista VeloCloud Orchestrator (VCO) on-prem contains an improper input validation vulnerability that may allow a remote attacker to access privileged internal functionality and impact the VCO host. Successful exploitation may compromise the confidentiality, integrity, and availability of the orchestrator and data managed by the orchestrator. Requir…

---

## 3. 🔴 CISA KEV — CVE-2026-93616 — Check Point Multiple Products Path Traversal Vulnerability

**CVE:** `CVE-2026-93616` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-93616>

> Vendor: Check Point | Product: Multiple Products. Check Point Security Management Server, Multi-Domain Security Management Server, Log Server, Multi-Domain Log Server, and SmartEvent contain a path traversal vulnerability that allows an unauthenticated attacker to upload and execute arbitrary scripts. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance wi…

---

## 4. 🔴 CISA KEV — CVE-2026-85102 — Check Point Multiple Products Improper Certificate Validation Vulnerability

**CVE:** `CVE-2026-85102` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-85102>

> Vendor: Check Point | Product: Multiple Products. Check Point Security Gateway and Check Point Spark Firewall using Site to Site VPN or Remote Access VPN contain an improper certificate validation vulnerability which could allow an unauthenticated remote attacker to execute arbitrary code on the Gateway. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance…

---

## 5. 🟠 Zero-Day — Improve Router Hygiene to Protect Against Russian State-Sponsored Targeting

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Wed, 08 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a>

> Russian Government-Sponsored Activity Targets Poorly Configured and Vulnerable Devices Across Critical Sectors Executive summary Russian Federal Security Service (FSB) Center 16 cyber actors continue to exploit poorly configured and vulnerable networking devices worldwide, opportunistically compromising multiple critical infrastructure sector networks. This joint Cybersecurity Advisory (CSA) build…

---

## 6. 🟠 Zero-Day — September 2026 Patch Tuesday: Two Exploited Zero-Days and 113 Critical Vulnerabilities Among 972 CVEs

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Sep 08, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-september-2026/>

---

## 7. 🟠 Zero-Day — Check Point warns of Management Server zero-day exploited in attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://www.bleepingcomputer.com/news/security/check-point-patches-management-server-zero-day-exploited-in-attacks/>

> Check Point Software released emergency hotfixes to address a critical Security Management Server vulnerability that could let attackers run arbitrary scripts. [...]

---

## 8. 🟠 Zero-Day — @aborruso/ckan-mcp-server has SSRF via DNS-name → internal IP — incomplete fix of CVE-2026-53509

**CVE:** `CVE-2026-61612` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://github.com/advisories/GHSA-798p-78g2-v556>

> ## Summary
The SSRF guard `validateServerUrl` (added for CVE-2026-33060, extended for CVE-2026-53509) validates only the **hostname string** and never resolves DNS. Any caller-supplied `server_url` whose hostname *resolves* to an internal address passes the guard, so the server issues requests to **loopback and cloud metadata (`169.254.169.254`)**. This is a third bypass of the same guard, still p…

---

## 9. 🟠 Zero-Day — @roomi-fields/notebooklm-mcp has a path traversal in vault.batch tool that allows arbitrary file write outside intended vault directory

**CVE:** `CVE-2026-61647` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://github.com/advisories/GHSA-jjhp-8crj-mppq>

> ## Summary

The `vault_batch` MCP tool (and the equivalent `POST /batch-to-vault` HTTP endpoint) accepted a caller-supplied `vault_dir` path that was passed directly to `path.resolve()` + `fs.mkdir()` with no containment check. A caller — or a prompt-injected LLM driving the MCP — could therefore create directories and write `.md` / `.json` answer files anywhere the server process can write.

The …

---

## 10. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

---

## 11. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

---

## 12. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

---

## 13. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

---

## 14. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 15. 🟠 Zero-Day — Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite

**CVE:** `CVE-2025-66376` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Tue, 21 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a>

> Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite Executive summary A group of Russian state-supported cyber actors has been targeting and compromising various Western government and commercial organizations using the Zimbra Collaboration Suite (ZCS) software since at least July 2025. The Russian state-supported advanced persistent threat …

---

## 16. 🟠 Zero-Day — MCP Atlassian: Arbitrary File Read via Upload Attachment Tools

**CVE:** `CVE-2026-77270` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://github.com/advisories/GHSA-f26r-j276-ggg4>

> ## Summary

The upload attachment tools in both Confluence and Jira accept arbitrary file paths without path traversal validation. The upload_attachment methods read any file accessible to the server process and upload it to a Confluence page or Jira issue. Despite the existence of a validate_safe_path utility function (used correctly in download operations), the upload paths do not use it. This a…

---

## 17. 🟠 Zero-Day — ShinyHunters claims FBI hack, data theft in PeopleSoft zero-day breach

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/>

> The ShinyHunters extortion gang claims it breached FBI systems using a new Oracle PeopleSoft zero-day vulnerability, gaining access to internal services and stealing sensitive data on employees and job applicants. [...]

---

## 18. 🟠 Zero-Day — CVE-2026-17613: Penpot cross-team file takeover via import-binfile (unpatched in 2.17.2)

**CVE:** `CVE-2026-17613` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://seclists.org/fulldisclosure/2026/Sep/47>

> Posted by Louis Sanchez via Fulldisclosure on Sep 22 Posting this as an update rather than a first disclosure. The advisory went public on 2026-08-04 with no vendor fix. Penpot has shipped two releases since then, 2.17.1 and 2.17.2 -- the latter 14 days ago, on 2026-08-27 -- and I re-checked the code this morning: the missing permission check is still missing in both, and in every release before t…

---

## 19. 🟠 Zero-Day — [0day-rubbish] TigerGraph Community Edition 4.2.4 Default credentials plus GSQL TO_CSV arbitrary file write to SSH code execution (9.8)

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://seclists.org/fulldisclosure/2026/Sep/64>

> Posted by disclosure via Fulldisclosure on Sep 22 0day Rubbish Research Team is publicly disclosing a vulnerability in TigerGraph Community Edition 4.2.4. Type: Default credentials plus GSQL TO_CSV arbitrary file write to SSH code execution (CWE-798) CVSS: 9.8 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) Impact: command execution as the tigergraph service user (uid 1001), which owns the engine, graph dat…

---

## 20. 🟠 Zero-Day — [0day-rubbish] Teltonika RutOS 00.07.06.21 Authenticated ipsec.lua logread command injection with reflected output (8.8)

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://seclists.org/fulldisclosure/2026/Sep/63>

> Posted by disclosure via Fulldisclosure on Sep 22 0day Rubbish Research Team is publicly disclosing a vulnerability in Teltonika RutOS 00.07.06.21. Type: Authenticated ipsec.lua logread command injection with reflected output (CWE-78) CVSS: 8.8 (AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) Impact: root command execution on the router, with command output reflected into the JSON response Authentication: au…

---

## 21. 🟠 Zero-Day — Check Point Warns of Management Server Zero-Day Exploited in Targeted Attacks

**CVE:** `CVE-2026-93616` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://thehackernews.com/2026/09/check-point-warns-of-management-server.html>

> Attackers exploited a previously unknown flaw in Check Point&#x27;s Security Management Server in a handful of targeted attacks on July 23, the company said.

The flaw, CVE-2026-93616, allows an attacker who can access the server&#x27;s web service to run scripts on it without logging in. Check Point released a fix on September 22 for the server that controls firewall policies for the Check Point

---

## 22. 🟠 Zero-Day — Researcher Drops BigDiskBuster Zero-Day PoC That Blocks Microsoft Defender Updates

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://thehackernews.com/2026/09/researcher-drops-bigdiskbuster-zero-day.html>

> A zero-day proof-of-concept tool that stops Microsoft Defender from installing platform and signature updates by filling all available disk space was published on GitHub on September 19.

The tool, called BigDiskBuster, has no patch, no CVE, and no Microsoft advisory. Its author, Abdelhamid Naceri, is a former Microsoft security researcher whose earlier Defender exploits were used in

---

## 23. 🟠 Zero-Day — D-Link warns of max severity zero-day bug in DIR-822A routers

**CVE:** `CVE-2026-86296` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://www.bleepingcomputer.com/news/security/d-link-warns-of-max-severity-zero-day-bug-in-dir-822a-routers/>

> D-Link warned customers of a maximum-severity vulnerability (CVE-2026-86296) with public proof-of-concept (PoC) exploit code and no patch, affecting legacy DIR-822A dual-band Wi-Fi routers. [...]

---

## 24. 🟠 Zero-Day — New CVSS 10.0 VeloCloud Orchestrator Flaw Actively Exploited in Certificate-Based Setups

**CVE:** `CVE-2026-93952` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://thehackernews.com/2026/09/new-cvss-100-velocloud-orchestrator.html>

> Attackers are exploiting a new flaw in on-premises VeloCloud Orchestrator (VCO), the server that manages the Edge devices in a VeloCloud SD-WAN, Arista said on September 22.

The flaw, tracked as CVE-2026-93952, may allow a remote attacker with no login access to privilege internal functions and affect the VCO host. Only orchestrators set up to authenticate their Edges with certificates are

---

## 25. 🟠 Zero-Day — New Windows Defender zero-day blocks Microsoft antivirus updates

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://www.bleepingcomputer.com/news/security/new-windows-defender-zero-day-blocks-microsoft-antivirus-updates/>

> Over the weekend, security researcher Abdelhamid Naceri (also known as Nightmare Eclipse) released another Microsoft Defender zero-day exploit that blocks antivirus updates. [...]

---

## 26. 🟡 High Severity — MCP Atlassian: Arbitrary file read via confluence_upload_attachment allows exfiltration of server credentials

**CVE:** `CVE-2026-77259` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://github.com/advisories/GHSA-6cr4-ccf3-x7h4>

> ### Summary

Missing path validation in `confluence_upload_attachment` allows any authenticated MCP client to read arbitrary files from the server filesystem and exfiltrate their contents to Confluence. On Linux deployments, `/proc/self/environ` yields all runtime secrets in a single call.

---
### Details

`AttachmentsMixin.upload_attachment()` in `src/mcp_atlassian/confluence/attachments.py` ope…

---

## 27. 🟡 High Severity — MCP Atlassian: SSRF redirect protection missing for basic-auth and OAuth authentication branches

**CVE:** `CVE-2026-77261` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://github.com/advisories/GHSA-6529-c226-h328>

> ### Summary

`_make_ssrf_safe_hook()` blocks HTTP redirects to private/internal IPs by validating the `Location` header before the client follows a `3xx` response. The problem is that this hook is only attached in one of three authentication branches — the header-PAT path. Basic auth and OAuth branches skip it entirely, so if the connected Atlassian server returns a redirect to something like `htt…

---

## 28. 🟡 High Severity — MCP Atlassian: SSRF via DNS Rebinding in Header-Based Authentication Flow

**CVE:** `CVE-2026-77265` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://github.com/advisories/GHSA-49xv-9743-pw8w>

> ## Summary

The SSRF protection for header-based authentication uses a validate-then-use pattern vulnerable to DNS rebinding. validate_url_for_ssrf resolves the hostname via DNS and checks that the resolved IP is globally routable. However, the actual HTTP request happens later, during which the DNS record may have changed to point to an internal IP (127.0.0.1, 169.254.169.254, etc.). The SSRF red…

---

## 29. 🟡 High Severity — MCP Atlassian: Path traversal in upload_attachment allows arbitrary file read (incomplete fix for CVE-2026-27825)

**CVE:** `CVE-2026-77269` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://github.com/advisories/GHSA-h7wj-5v37-59r2>

> ### Summary

The `confluence_upload_attachment` and `confluence_upload_attachments` MCP tools accept a `file_path` parameter and do not validate that the path is confined to an allowed directory before opening the file. An attacker who can call these tools can read any file accessible to the MCP server process (SSH keys, .env files, API credentials) and exfiltrate it by uploading it to Confluence.…

---

## 30. 🟡 High Severity — MCP Atlassian: Arbitrary local file READ via unconstrained file_path in upload_attachment (Confluence + Jira)

**CVE:** `CVE-2026-77260` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://github.com/advisories/GHSA-f4p7-qx46-wc5j>

> ## Summary

This is an arbitrary local file READ vulnerability on the Confluence and Jira `upload_attachment` tool paths. It&#x27;s the symmetric counterpart of the file-write vulnerability you patched as CVE-2026-27825. The write direction was fixed; the read direction was left open.

**Reporter:** Sean Valentine
**Severity:** High (Critical in LLM-driven / prompt-injection deployments)
**Affecte…

---

## 31. 🟡 High Severity — MCP Atlassian: HTTP upload tools accept arbitrary server-local file paths

**CVE:** `CVE-2026-77257` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://github.com/advisories/GHSA-mrq8-fv7v-hhjg>

> # sooperset/mcp-atlassian: HTTP upload tools can attach arbitrary server-local files

Date: 2026-05-05
Target: `sooperset/mcp-atlassian`
Commit: `d8bc78698a63cb6b321c7ca796d6329d448f7f6d`

## Summary

`mcp-atlassian` supports HTTP/SSE deployment for persistent, remote, and multi-user use. In that mode, write-capable Jira and Confluence attachment flows accept caller-controlled server-local file pa…

---

## 32. 🟡 High Severity — MCP Atlassian: ENABLED_TOOLS / Toolset authorization bypass

**CVE:** `CVE-2026-77243` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://github.com/advisories/GHSA-3r68-hf9h-887v>

> ### Summary

`ENABLED_TOOLS` and `TOOLSETS` filters are enforced at `tools/list` time only. `tools/call` dispatches from the full unfiltered tool registry (73 tools). Any user with access to the server endpoint that knows a tool name can invoke it directly. Tool names are not secret since mcp-atlassian is open source. Any direct JSON-RPC call bypasses the restriction entirely.

`READ_ONLY_MODE` is…

---

## 33. 🟡 High Severity — MCP Atlassian: Arbitrary File Read & Exfiltration (Confused Deputy) in JIRA update_issue

**CVE:** `CVE-2026-77255` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://github.com/advisories/GHSA-2xj6-xx86-cwwc>

> ### Summary
A critical Confused Deputy (Arbitrary File Read &amp; Exfiltration) vulnerability in the Atlassian MCP server (Python) allows an AI agent to exfiltrate sensitive host files and environment secrets. By providing absolute system paths to the attachments parameter of the update_issue tool, an agent can force the privileged MCP process to read and upload any file it has access to—including…

---

## 34. 🟡 High Severity — MCP Atlassian: JIRA_PROJECTS_FILTER / CONFLUENCE_SPACES_FILTER allow forbidden-project content exfiltration (one LIVE-proven on Atlassian Cloud)

**CVE:** `CVE-2026-77251` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://github.com/advisories/GHSA-w66g-j6c4-hcfc>

> ### Summary

`mcp-atlassian` is a popular community MCP server wrapper exposing Jira / Confluence to MCP clients. Operators commonly restrict the surface to a small allowlist of projects/spaces via the `JIRA_PROJECTS_FILTER` and `CONFLUENCE_SPACES_FILTER` environment variables, which the README documents as the principal mechanism for limiting attacker-controlled MCP clients (= prompt-injected LLM…

---

## 35. 🟡 High Severity — MCP Atlassian: MCP HTTP Client Server-Local File Exfiltration via Unvalidated Attachment Upload Path

**CVE:** `CVE-2026-77246` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://github.com/advisories/GHSA-wv8v-v4c5-v75j>

> ### Summary

The `mcp-atlassian` server exposes an MCP tool (`confluence_upload_attachment` and the Jira attachment variant) that accepts an arbitrary server-side file path and opens it for upload without any path validation. When the server is deployed in HTTP transport mode (`streamable-http` or `sse`), a remote, unauthenticated attacker can supply attacker-controlled Atlassian service headers (…

---

## 36. 🟡 High Severity — MCP Atlassian: Unauthenticated arbitrary local file read via upload_attachment file_path, chained with missing auth on streamable-http transport

**CVE:** `CVE-2026-77248` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://github.com/advisories/GHSA-cc5h-2pwp-pvcc>

> ### Summary
In the documented multi-user HTTP deployment (`--transport streamable-http` with global operator Atlassian credentials), sooperset/mcp-atlassian exposes all tools to **unauthenticated network clients**, and the `upload_attachment` tool reads an attacker-supplied `file_path` with **no path validation**. Chained, an unauthenticated network attacker reads arbitrary files on the MCP server…

---

## 37. 🟡 High Severity — Unleash: Clone-feature lets a user copy a feature from a project they cannot read

**CVE:** `CVE-2026-76910` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://github.com/advisories/GHSA-8xcj-9hfr-fh9j>

> ### Summary

The clone-feature endpoint supports copying features across projects, but it does not verify that the caller can access the source project. A user with _create_ permissions in one project can clone a feature from another project they cannot read and then inspect the copied configuration.

This vulnerability cannot be confirmed without Enterprise access. Report is based on a circumstan…

---

## 38. 🟡 High Severity — Graylog: Manager-to-Owner privilege escalation on saved searches and dashboards

**CVE:** `CVE-2026-69190` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://github.com/advisories/GHSA-m9c2-85gv-8xr5>

> ### Impact

A vulnerability was found in Graylog&#x27;s API endpoint for updating saved searches and dashboards. A user with edit permissions on a dashboard or saved search could grant owner permissions to an arbitrary account, which could then be used to delete the respective saved search or dashboard or to remove the original owner&#x27;s access. 

### Patches

This issue has been patched in the…

---

## 39. 🟡 High Severity — Hatchet: Cross-Tenant Durable Task Event Log Disclosure via Missing Authorization Check

**CVE:** `CVE-2026-63342` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://github.com/advisories/GHSA-g26x-m427-f48f>

> ### Summary

The `GET /api/v1/stable/durable-tasks/{durable-task}` endpoint (`listDurableEventLog`) is missing tenant authorization validation, allowing any authenticated user to read durable task event logs from any tenant.


### Impact
This CVE requires the attacker to successfully guess the target UUID.
Any authenticated Hatchet user can read durable task event logs from any other tenant, expos…

---

## 40. 🟡 High Severity — Hatchet: SSRF via Unsigned UnsubscribeURL in SNS UnsubscribeConfirmation Handler

**CVE:** `CVE-2026-61681` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://github.com/advisories/GHSA-fjwv-jf2v-j499>

> ### Summary
  The SNS `UnsubscribeConfirmation` handler in `internal/integrations/ingestors/sns/sns.go` makes an unvalidated
  `http.Get()` call to `payload.UnsubscribeURL` without any URL restriction. Because `UnsubscribeURL` is intentionally
  excluded from the `BuildSignature()` signed field list, an attacker can replace this field in a legitimately
  AWS-signed message with an arbitrary intern…

---

## 41. 🟡 High Severity — wlc may disclose API tokens to project-configured URLs

**CVE:** `CVE-2026-62364` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://github.com/advisories/GHSA-3mqq-hv9c-85hc>

> ### Impact

wlc could send an unscoped API token to an unintended server when run inside a directory tree containing attacker-controlled project configuration.

If `.weblate`, `.weblate.ini`, or `weblate.ini` defines an API url, and the user supplies a token with `WLC_KEY` or `--key` without also pinning the URL, wlc would send the token to the project-configured URL.

Impacted users are those run…

---

## 42. 🟡 High Severity — deepstream: PATCH_MULTI action bypasses Valve permission system allowing unauthorized record writes

**CVE:** `CVE-2026-63116` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://github.com/advisories/GHSA-89vx-jh4q-vg3w>

> ## Summary

The `RECORD_ACTION.PATCH_MULTI` action is not registered in the Valve permission system&#x27;s `RULES_MAP` (`src/services/permission/valve/rules-map.ts`). When `ConfigPermission.canPerformAction()` is called for a PATCH_MULTI message, `getRulesForMessage()` returns `null` because the action is missing from the map. This triggers an unconditional allow (`callback(..., null, true)`), com…

---

## 43. 🟡 High Severity — OpenCVE: Server-Side Request Forgery (SSRF) in notifications

**CVE:** `CVE-2026-62282` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://github.com/advisories/GHSA-ch3g-4xvr-674q>

> ### Impact

OpenCVE contains a Server-Side Request Forgery (SSRF) vulnerability in the notification testing functionality for both Webhook and Slack integrations.

An authenticated user with permission to configure notification channels can trigger test requests to arbitrary HTTP(S) endpoints. Insufficient validation of target destinations allows requests to be sent to hosts reachable from the Ope…

---

## 44. 🟡 High Severity — psd-tools composite/numpy has uncontrolled memory allocation via crafted PSD geometry

**CVE:** `CVE-2026-59991` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://github.com/advisories/GHSA-8q6g-vjhf-jp8m>

> ### Summary
`PSDImage.composite()` (and `.numpy()`) allocate the output image buffer from the PSD&#x27;s header geometry (width × height × channels × depth, and per-layer rectangles) before validating those values against the actual file contents. A tiny crafted PSD declaring huge dimensions causes a multi-gigabyte allocation. Critically, `composite()` then returns a (black) image with only a warn…

---

## 45. 🟡 High Severity — microsandbox: Secret values exposed in world-readable process arguments

**CVE:** `CVE-2026-61670` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://github.com/advisories/GHSA-m8f5-rh7h-vgg3>

> ## Summary

When the SDK spawns a sandbox, the `msb sandbox` child process receives the full network configuration as an inline `--network-config &lt;json&gt;` command-line argument, and any per-sandbox environment as repeated `--env KEY=VALUE` arguments. On Linux a process&#x27;s arguments are world-readable via `/proc/&lt;pid&gt;/cmdline`, and on both Linux and macOS they are visible to other lo…

---

## 46. 🟡 High Severity — CVE-2026-44756: Pre-Auth RCE in SAP EPP Processing (ICM, Web Dispatcher, disp+work)

**CVE:** `CVE-2026-44756` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://seclists.org/fulldisclosure/2026/Sep/65>

> Posted by Raschin Tavakoli via Fulldisclosure on Sep 22 nullFaktor Security Advisory &lt; 2026-09-10 &gt; =========================================================== Title: Pre-Authentication Remote Code Execution in SAP Extended Passport (EPP) processing library Affected Components: ICM, SAP Web Dispatcher, dialog work processes Vulnerability: Stack based Buffer Overflow CVE: CVE-2026-44756 Impac…

---

## 47. 🟡 High Severity — Critical Bifrost AI Gateway Flaw Lets Attackers Run Commands Without Credentials

**CVE:** `CVE-2026-90898` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://thehackernews.com/2026/09/critical-bifrost-ai-gateway-flaw-lets.html>

> A critical vulnerability in Bifrost, an open-source AI gateway that routes requests to more than 20 LLM providers, allows an unauthenticated attacker to run arbitrary commands on the gateway server with a single HTTP request.

The flaw, tracked as CVE-2026-90898 (CVSS score: 9.8), affects all versions of the Bifrost HTTP transport before 2.1.0 when management authentication is

---

## 48. 🟡 High Severity — SharePoint Flaw Initially Listed as Spoofing by Microsoft Enables Authenticated RCE

**CVE:** `CVE-2026-65660` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://thehackernews.com/2026/09/sharepoint-flaw-initially-listed-as.html>

> A SharePoint Server vulnerability that Microsoft initially classified as a spoofing flaw with a CVSS score of 6.5 actually enables authenticated remote code execution, according to full technical details published today by Viettel Cyber Security researcher Dinh Ho Anh Khoa.

The flaw, CVE-2026-65660, affects SharePoint Server 2016, 2019, and Subscription Edition. Patches have been

---

## 49. 🟡 High Severity — Zyxel and Veeam Flaws Under Active Exploitation With Command and SYSTEM Access

**CVE:** `CVE-2026-7273` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-09-22
**Reference:** <https://thehackernews.com/2026/09/zyxel-and-veeam-flaws-under-active.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Monday added a now-patched security flaw impacting Zyxel GS1900 series switches to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

The vulnerability, tracked as CVE-2026-7273 (CVSS score: 8.8), is a stack-based buffer overflow vulnerability that could result in arbitrary operating

---

## 50. 🟡 High Severity — nginx ignition has TOTP Reuse During Validity Window

**CVE:** `CVE-2026-61630` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-21
**Reference:** <https://github.com/advisories/GHSA-hf33-q6cf-c66f>

> ### Summary
Any user that has enabled the OTP 2FA can have their TOTP reused during the standard 30 second validity window.

### Details
The https://github.com/pquerna/otp package [doesn&#x27;t include](https://github.com/pquerna/otp/issues/61) checking for already used TOTPs within its the validity window. This requires each application that uses the package to implement their own method of track…

---

## 51. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
