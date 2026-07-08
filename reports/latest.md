# Zero Day Pulse

> **Generated:** 2026-07-08 01:26 UTC &nbsp;|&nbsp; **Total:** 33 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 21 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Multiple path-traversal vulnerabilities (CVE-2024-57727) in SimpleHelp <= v5.5.7 allow unauthenticated HTTP requests to retrieve arbitrary files from the host (including server configuration, secrets, and hashed user passwords) via crafted requests.
- **Affected Products:** SimpleHelp remote support / RMM, versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploitation has been observed in the wild (ransomware actors per CISA). No public proof-of-concept (PoC) or public exploit URL is present in the supplied corpus.
- **Patch Available:** Yes — SimpleHelp published advisory/guidance and released patches for the vulnerabilities in SimpleHelp 5.5.7 and earlier (see vendor advisory URL).
- **Active Exploitation:** Confirmed — CISA reports ransomware actors exploited unpatched SimpleHelp RMM to compromise a utility billing software provider and states unpatched SimpleHelp instances have been targeted since January 2025 (CISA advisory).
- **Threat Actors:** None known
- **Mitigation:** Apply vendor-published patches/updates immediately (update off vulnerable SimpleHelp instances to the vendor-fixed version). If patching is not possible, follow vendor/CISA mitigations (restrict or remove external exposure, discontinue use, or otherwise block access to the service) and assume potential compromise for downstream customers per CISA/NVD guidance.
- **Vendor Advisory:** http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — Critical Gitea Flaw Under Active Exploitation, Researchers Warn

**CVE:** `CVE-2026-20896` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://www.securityweek.com/critical-gitea-flaw-under-active-exploitation-researchers-warn/>

> Attackers are exploiting the critical Gitea vulnerability CVE-2026-20896 to bypass authentication with a single HTTP header and access vulnerable repositories and secrets. The post Critical Gitea Flaw Under Active Exploitation, Researchers Warn appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Authentication-bypass / impersonation via reverse-proxy header authentication: the official Docker image shipped with REVERSE_PROXY_TRUSTED_PROXIES = * by default, allowing any source to be treated as a trusted proxy; combined with header-based auth (e.g., X-WEBAUTH-USER), an attacker can spoof that header to impersonate any user and bypass authentication.
- **Affected Products:** Gitea (official Docker image — all versions up to and including 1.26), Gogs (mentioned in some vulnerability trackers)
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC/PoC-collection references and exploit-tracking entries exist (e.g., GitHub PoC-collector repos), and reporting indicates exploit code/references are being collected; see tracked PoC index and coverage in news reporting.
- **Patch Available:** Yes — Gitea published fixes in releases 1.26.3 and 1.26.4 (see vendor advisory URLs above).
- **Active Exploitation:** Yes — multiple public reports (SecurityWeek, The Hacker News and other vuln-intel pages) state that threat actors are exploiting the authentication-bypass in internet-accessible Gitea instances.
- **Threat Actors:** None known
- **Mitigation:** Upgrade to the patched Gitea releases (1.26.3 / 1.26.4). If upgrade is not immediately possible, restrict/disable reverse-proxy header authentication or tighten REVERSE_PROXY_TRUSTED_PROXIES (do not use '*'), and ensure header-based auth is only used behind strictly trusted proxies.
- **Vendor Advisory:** https://blog.gitea.com/release-of-1.26.3-and-1.26.4/, https://github.com/go-gitea/gitea/security/advisories/GHSA-f75j-4cw6-rmx4

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when attacker-controlled instructions are embedded inside external data sources (web pages, files, or other content) that an AI agent ingests; the hidden or obfuscated instructions influence the model’s outputs (causing it to execute attacker directives or disclose data) without the attacker directly querying the model.
- **Affected Products:** Google Workspace (Gemini), AI agents / agentized browsers (general)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof-of-concept demonstrations and captured payloads have been published (e.g., a public GitHub PoC demonstrating IPI behavior and vendor reports with captured payloads).
- **Patch Available:** Official vendor mitigations/advisories available (Google Security Blog post and Google Workspace knowledge article describing layered defenses and continuous mitigations).
- **Active Exploitation:** Yes — multiple security vendors and researchers have reported captured IPI payloads and in-the-wild activity (industry reports and vendor blog posts describe observed attempts and payloads).
- **Threat Actors:** None known
- **Mitigation:** Apply layered defenses: restrict and sanitize untrusted external content before including it in model context; scope and limit model context size and privileges; harden system prompts/instructions (instruction-locking), filter/block known payload patterns, monitor for indicators of IPI, and deploy vendor-provided updates/configurations (see vendor advisories).
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when adversarial or malicious instructions are embedded in external content (emails, documents, web pages, files, or tool outputs) that an LLM ingests while fulfilling a user request; those hidden instructions become part of the model's effective prompt (e.g., during summarization or agent tool use) and can cause the model to divulge sensitive data or take unintended actions.
- **Affected Products:** Gemini app, Gmail, Docs editors, Google Drive, Google Chat
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit URL known; third-party reports document IPI payloads observed in the wild but do not publish an official exploit URL.
- **Patch Available:** No discrete vendor "patch"; Google deploys layered mitigations and model hardening described in the vendor advisory and Workspace help pages.
- **Active Exploitation:** Yes — multiple public reports document IPI payloads and web-based IPI incidents observed in the wild; Google states its layered protections have mitigated attempts. (See vendor advisory and third-party reporting for details.)
- **Threat Actors:** None known
- **Mitigation:** Google describes a layered defense: model resilience/hardening, prompt-injection content classifiers, security thought reinforcement, markdown sanitization, suspicious-URL redaction, and a user-confirmation (human-in-the-loop) framework plus continuous monitoring and iterative improvements.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Insufficient policy/authorization enforcement in the WebView/Gemini side-panel ("Gemini Live/side panel") context allowed a malicious extension or web content to bypass policy, hijack the Gemini panel and escalate privileges or access local files and sensitive data.
- **Affected Products:** Google Chrome / Chromium prior to 143.0.7499.192
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof-of-concept code is available (example: GitHub repository fevar54/CVE-2026-0628-POC).
- **Patch Available:** Yes — Google released a Chrome fix (vulnerability addressed for Chrome builds >= 143.0.7499.192). See the Google Security Blog advisory and the NVD entry for CVE-2026-0628 for the fixed build.
- **Active Exploitation:** No confirmed reports of active in‑the‑wild exploitation in the cited sources (reporting indicates the issue was patched quickly and no confirmed exploited campaigns were documented).
- **Threat Actors:** None known
- **Mitigation:** Apply the official Chrome update (upgrade to 143.0.7499.192 or later). Additional hardening: restrict extension installs and permissions, use Chrome’s layered defenses for agentic features (restrict origin access, block prompt injection), and disable untrusted extensions until patched.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow / out-of-bounds access in the CrabbyAVIF AVIF parser/decoder (incorrect bounds checking in multiple locations) that can lead to remote code execution (assigned CVE-2025-48530).
- **Affected Products:** Android System (CrabbyAvif AVIF parser/decoder), webmproject/CrabbyAvif (Rust implementation), Android platform external/crabbyavif
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** No widely-published public PoC or weaponized exploit was found in the collected corpus; social posts and databases discuss the CVE but do not show a confirmed public weaponized exploit.
- **Patch Available:** Yes — fixes were published via Android vendor updates / security bulletin and repository fixes (see Android Security Bulletin and platform/external/rust/crabbyavif).
- **Active Exploitation:** No confirmed active exploitation in the wild reported in the collected sources (vendor/DB listings indicate not known to be exploited).
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor Android security update / upgrade CrabbyAvif to the patched commit (no alternative runtime workaround reported).
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection arises when LLM applications compose developer/system instructions and third‑party content into a single natural‑language context; adversarial instructions embedded in external content (emails, web pages, docs, calendar items) can influence model behavior, causing data exfiltration or other unauthorized actions unless isolated, classified, or sanitized.
- **Affected Products:** Gemini (Gemini app), Gemini in Workspace apps (Gmail, Docs, Drive, Chat)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof-of-concept demonstrations and PoC code exist (e.g., public GitHub PoC) and industry reports document live payloads observed in the wild.
- **Patch Available:** No vendor software "patch" reported; Google published advisory/guidance instead (see vendor_advisory URL).
- **Active Exploitation:** Yes — multiple industry and research reports document in‑the‑wild indirect prompt injection payloads and detections; public PoCs have been published and live payloads have been observed.
- **Threat Actors:** None known
- **Mitigation:** Google recommends a layered defense: prompt-injection content classifiers, security thought‑reinforcement, Markdown sanitization/suspicion handling, adversarial model training, isolation/containment of third‑party content, and other input-sanitization and architectural controls.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors target large backbone routers and edge devices (provider-edge and customer-edge routers), leverage compromised devices and trusted connections to pivot, and modify router configurations (e.g., adding/modifying ACLs) to maintain persistent, long-term access and exfiltrate data.
- **Affected Products:** Cisco, Palo Alto, Ivanti, potentially Fortinet, Juniper, Microsoft Exchange, and others (breadth of affected vendors reported by analyst summaries).
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) or weaponized exploit reported in the cited sources; multiple sources state there are no known exploits in the wild at the time of the advisory.
- **Patch Available:** No official vendor patch or remediation guidance identified in the cited sources; vendors have not published a consolidated patch advisory (no vendor patch URL found).
- **Active Exploitation:** CISA reports that exploitation of zero-day vulnerabilities had not been observed to date; analysts describe ongoing espionage operations targeting backbone/edge routers but the cited segments do not document confirmed zero-day exploitation in the wild.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Upgrade unsupported network devices to vendor-supported models; harden and monitor backbone / provider-edge (PE) and customer-edge (CE) routers (detect unauthorized config changes such as unexpected ACLs), restrict management-plane access, segment networks and monitor trusted interconnections for anomalous traffic.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** GRU unit 26165 (APT28) has used an Outlook NTLM vulnerability (CVE-2023-23397) to collect NTLM hashes and has targeted Western logistics and technology companies using espionage TTPs; the joint advisory provides additional TTP, infrastructure, and IOCs (AA25-141A STIX).
- **Affected Products:** Microsoft Outlook (CVE-2023-23397); other affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Advisory reports weaponization of CVE-2023-23397 by GRU unit 26165, but the collected sources do not include a public proof-of-concept (PoC) or public exploit URL.
- **Patch Available:** CISA/FBI advisory notes the actors weaponized CVE-2023-23397 (an Outlook NTLM issue) but does not include an explicit vendor patch URL in the advisory itself.
- **Active Exploitation:** Yes — CISA/FBI joint advisory reports an active campaign targeting Western logistics entities and technology companies (activity reported since 2022).
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center, unit 26165 (commonly tracked as APT28 / Fancy Bear).
- **Mitigation:** See CISA AA25-141A STIX and the joint advisory for full IOCs; key mitigations include applying vendor security updates, monitoring and ingesting AA25-141A IOCs/STIX, hardening email and authentication (reduce/disable NTLM where possible, enforce MFA), network segmentation and monitoring for the listed TTPs.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

**Parallel AI Enrichment:**

- **Technical Details:** Browser exploit chains commonly target rendering logic, JavaScript execution, document handling, or memory-safety weaknesses and then chain to sandbox escape and privilege escalation to move from browser activity to system access.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) or weaponized exploit is provided or linked in the CrowdStrike blog; the article states that many zero-days are exploited before disclosure but does not supply PoC code or exploit URLs.
- **Patch Available:** No specific vendor patch or advisory is referenced in the CrowdStrike blog; the article discusses patching challenges and timing but does not list an official patch URL for a particular vulnerability.
- **Active Exploitation:** The blog cites industry reports that many vulnerabilities are actively exploited before public disclosure (CrowdStrike cites 42% exploited before disclosure per its 2026 Global Threat Report and the Verizon DBIR trend); the article supports that active exploitation of zero-days occurs generally but does not report confirmed exploitation tied to a single, specific CVE/advisory.
- **Threat Actors:** None known
- **Mitigation:** Use defenses that operate inside the browser session (e.g., runtime protections such as JavaScript Language Randomization), block phishing and session/token abuse, prevent credential theft and data exfiltration at execution time, and accelerate patch validation and deployment across managed and unmanaged devices.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 12. 🟠 Zero-Day — Chinese hackers develop LONGLEASH malware to expand ORB network

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://www.bleepingcomputer.com/news/security/chinese-hackers-develop-longleash-malware-to-expand-orb-network/>

> Chinese hackers tracked as &#x27;UAT-7810&#x27; are actively evolving their malware to expand their Operational Relay Box (ORB) network by compromising internet-facing networking devices, primarily unpatched Ruckus routers. [...]

---

## 13. 🟡 High Severity — Weblate SSRF: outbound URL guard misses some private ranges

**CVE:** `CVE-2026-50127` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-vmfc-9982-2m45>

> ### Impact

Weblate&#x27;s `VCS_RESTRICT_PRIVATE` did not properly account for some transitional IPv6 ranges, multicast addresses, or some semi-private IPv4 ranges, which allowed some addresses to bypass private range restrictions.

### Patches

* https://github.com/WeblateOrg/weblate/pull/19768

### Resources

The issue was reported by @tonghuaroot via GitHub, and the same user also provided the …

---

## 14. 🟡 High Severity — oasdiff does not enforce --allow-external-refs=false on the git-revision load path (SSRF / local file read)

**CVE:** `CVE-2026-53508` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-2jcc-mxv7-p3f9>

> ## Summary

From **v1.13.2** through **v1.18.0**, oasdiff did not enforce `--allow-external-refs=false` (library: `openapi3.Loader.IsExternalRefsAllowed = false`) when loading a spec from a **git revision** (the `rev:path` form, e.g. `main:openapi.yaml`). External `$ref`s were resolved on that load path even when external refs were explicitly disabled, so the mitigation silently did not apply ther…

---

## 15. 🟡 High Severity — Goploy: Cross-namespace IDOR and RCE via body-supplied row id in project and project_file handlers

**CVE:** `CVE-2026-53552` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-26rh-24rg-j3vv>

> ### Summary

`Project.AddFile`, `Project.EditFile`, `Project.RemoveFile`, and `Project.Edit` in `cmd/server/api/project/handler.go` accept a project or project-file row id from the JSON body and act on it without checking that the project belongs to the caller&#x27;s namespace. The corresponding `model.ProjectFile.GetData` and `model.Project.GetData` queries filter only by row id. A user holding t…

---

## 16. 🟡 High Severity — Kite has an authenticated cluster RBAC bypass in /api/v1/overview

**CVE:** `CVE-2026-53487` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-gvhc-wv3v-7pf8>

> ## Summary

Authenticated Kite users with any role can request `/api/v1/overview` for a cluster that their roles do not permit by selecting that cluster with `x-cluster-name`. The overview route is registered before `middleware.RBACMiddleware()` and `GetOverview` only checks `len(user.Roles) &gt; 0`, so it returns aggregate Kubernetes inventory and capacity data from unauthorized clusters.

The is…

---

## 17. 🟡 High Severity — ratex-parser has unbounded parser recursion that leads to stack overflow (process abort)

**CVE:** `CVE-2026-53531` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-4w5h-hx6r-28q7>

> ### Summary


RaTeX’s recursive-descent parser recurses one (or more) native stack frame per nesting level at `{`, `\left`, `\sqrt{`, `^{`, etc, with **no maximum depth limit**. A short, ~10 KB input of nested groups overflows the 8 MB main-thread stack and aborts the process. With `panic = &quot;abort&quot;` (`Cargo.toml:48`), and because a Rust stack overflow is always a fatal `SIGABRT` regardle…

---

## 18. 🟡 High Severity — @better-auth/oauth-provider's OAuth authorization-code grant allows concurrent redemption when two token requests race the find-then-delete primitive

**CVE:** `CVE-2026-53518` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-7w99-5wm4-3g79>

> ### Am I affected?

Users are affected if all of the following are true:

- Their project depends on `@better-auth/oauth-provider` at a version `&gt;= 1.6.0, &lt; 1.6.11`, or uses the embedded plugin in `better-auth &gt;= 1.4.8-beta.7, &lt; 1.6.0`, or enables the legacy `oidc-provider` or `mcp` plugins from `better-auth/plugins`.
- Their application exposes `/api/auth/oauth2/token` (or the legacy …

---

## 19. 🟡 High Severity — @better-auth/sso provider registration has server-side request forgery via unvalidated OIDC endpoints

**CVE:** `CVE-2026-53513` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-5rr4-8452-hf4v>

> ### Am I affected?

Users are affected if all of the following are true:

- Their application uses `@better-auth/sso` at a version `&gt;= 0.1.0, &lt; 1.6.11` on the stable line, or any `1.7.0-beta.x` on the pre-release line.
- The `sso()` plugin is added to their application&#x27;s `betterAuth({ plugins: [...] })` array.
- Any user with a valid Better Auth session can reach `POST /sso/register` (t…

---

## 20. 🟡 High Severity — Better Auth: OAuth refresh-token rotation forks the token family on concurrent redemption

**CVE:** `CVE-2026-53517` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-392p-2q2v-4372>

> ### Am I affected?

Users are affected if all of the following are true:

- Their project depends on `@better-auth/oauth-provider` at a version `&gt;= 1.6.0, &lt; 1.6.11`, or uses the embedded plugin in `better-auth &gt;= 1.4.8-beta.7, &lt; 1.6.0`.
- At least one OAuth client served by their application&#x27;s authorization server requests the `offline_access` scope, so refresh tokens are minted.
…

---

## 21. 🟡 High Severity — Better Auth: OAuth refresh-token replay via missing client authentication on oidc-provider and mcp plugins

**CVE:** `CVE-2026-53512` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-pw9m-5jxm-xr6h>

> ### Am I affected?

Users are affected if all of the following are true:

- Their application uses `better-auth` and has enabled at least one of: `oidcProvider()` (imported from `better-auth/plugins/oidc-provider`), or `mcp()` (imported from `better-auth/plugins/mcp`).
- Their application has at least one confidential OAuth client registered (any client with `type: &quot;web&quot; | &quot;native&q…

---

## 22. 🟡 High Severity — @aborruso/ckan-mcp-server: SSRF via base_url allows access to internal networks (Potential fix bypass of CVE-2026-33060)

**CVE:** `CVE-2026-53509` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-g84h-j7jj-x32p>

> ### Summary
A known vulnerability CVE-2026-33060 indicated tools including ckan_package_search and sparql_query that accept a base_url parameter had the risk of making HTTP requests to arbitrary endpoints without restriction. A fix was applied to filter out ip addresses. However, a method to bypass exists.

### Details
CKAN MCP Server validates caller-supplied CKAN server URLs by inspecting only t…

---

## 23. 🟡 High Severity — Open WebUI has Blind Server Side Request Forgery in its Image Edit Functionality

**CVE:** `CVE-2026-34225` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-jgx9-jr5x-mvpv>

> ### Summary
There is a blind server side request forgery in the functionality that allows editing an image via a prompt. The affected function will perform a GET request on the URL provided by the user. There is no restriction on the domain of the provided URL allowing the local address space to be interacted with. Since the SSRF is blind (the response cannot be read) impact is port scanning of th…

---

## 24. 🟡 High Severity — Open WebUI vulnerable to stored XSS via unescaped markdown token in MarkdownTokens.svelte leading to full account takeover and RCE via functions

**CVE:** `CVE-2025-46719` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-9f4f-jv96-8766>

> ### Summary

A vulnerability in the way certain html tags in chat messages are rendered allows attackers to inject JavaScript code into a chat transcript. The JavaScript code will be executed in the user&#x27;s browser every time that chat transcript is opened, allowing attackers to retrieve the user&#x27;s access token and gain full control over their account. Chat transcripts can be shared with …

---

## 25. 🟡 High Severity — EGroupware has Authenticated RCE via Malicious eTemplate Upload

**CVE:** `CVE-2026-40187` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-8737-2x9g-xjj7>

> ## Summary

An authenticated administrator can achieve OS-level Remote Code Execution (RCE) by uploading a malicious eTemplate XML file (`.xet`) to the VFS `/etemplates` mount.

The `Widget::expand_name()` method passes template widget attribute values directly into a PHP `eval()` call with only double-quote escaping applied - **backtick characters are not escaped**.

In PHP, backticks inside a do…

---

## 26. 🟡 High Severity — New API: SSRF Protection Bypass via Unresolved Hostname in Notification URLs

**CVE:** `CVE-2026-33655` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-6qcr-qxgr-m7fv>

> ## Summary

The default SSRF protection configuration did not apply IP filtering to hostnames. With `ApplyIPFilterForDomain` disabled by default, URL validation checked domain allow/block rules but did not resolve a hostname and validate the resolved IP address. Authenticated users could configure notification URLs for Webhook, Bark, or Gotify notifications and point a hostname at an internal or m…

---

## 27. 🟡 High Severity — EGroupware has a Remote Code Execution Vulnerability

**CVE:** `CVE-2026-27823` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-h9qx-v5xp-ph8p>

> ## Summary
A critical vulnerability has been identified in EGroupware that may lead to Remote Code Execution (RCE).
The issue allows an authenticated attacker to execute arbitrary commands on the server. If user self-registration is enabled, the vulnerability may be exploitable without prior authentication.

The vulnerability stems from improper authorization checks combined with a file write prim…

---

## 28. 🟡 High Severity — Critical Adobe ColdFusion Vulnerability Exploited in Attacks

**CVE:** `CVE-2026-48282` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://www.securityweek.com/critical-adobe-coldfusion-vulnerability-exploited-in-attacks/>

> Hackers are exploiting a recently patched critical vulnerability (CVE-2026-48282) in Adobe ColdFusion that carries a CVSS score of 10/10. The post Critical Adobe ColdFusion Vulnerability Exploited in Attacks appeared first on SecurityWeek .

---

## 29. 🟡 High Severity — Suspected China-Aligned Hackers Exploit Roundcube Flaws Against Universities

**CVE:** `CVE-2024-42009` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://thehackernews.com/2026/07/suspected-china-aligned-hackers-exploit.html>

> A suspected China-aligned threat activity cluster has been observed exploiting Roundcube webmail software belonging to physics and engineering departments of U.S. and Canadian universities as part of a new campaign.

The activity involves the exploitation of now-patched, critical security flaws in the open-source email solution, such as CVE-2024-42009 (CVSS score: 9.3), to siphon credentials,

---

## 30. 🟡 High Severity — CERT/CC Warns of Hidden Admin Backdoor in Tenda Router Firmware

**CVE:** `CVE-2026-11405` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://thehackernews.com/2026/07/certcc-warns-of-hidden-admin-backdoor.html>

> Several versions of firmware released by Chinese network device manufacturer Tenda have been found to embed an undocumented authentication backdoor that enables administrative access to the devices&#x27; web management interfaces, the CERT Coordination Center (CERT/CC) warned Monday.

&quot;An attacker can exploit this vulnerability, tracked as CVE-2026-11405, to bypass the password verification p…

---

## 31. 🟡 High Severity — OPNsense XPATH Injection (CVE-2026-53582)

**CVE:** `CVE-2026-53582` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://seclists.org/fulldisclosure/2026/Jul/18>

> Posted by evan on Jul 06 SUMMARY: a stored XPATH injection allows any user with just ca manager/certificate manager perms to leak any secret key/any value in config.xml, thus achieving privilege escalation and potentially remote code execution. this can also likely be chained via csrf and some clever hiding. see https://github.com/opnsense/core/security/advisories/GHSA-xww7-76m6-mh2r == VULN == th…

---

## 32. 🟡 High Severity — BeyondTrust Patches Critical Auth Bypass Flaws in Remote Support and PRA

**CVE:** `CVE-2026-40138` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://thehackernews.com/2026/07/beyondtrust-patches-critical-auth.html>

> BeyondTrust has released updates to address two critical security flaws affecting Remote Support (RS) and Privileged Remote Access (PRA) products that, if successfully exploited, could allow unauthenticated attackers to take control of susceptible devices.

The vulnerabilities are listed below -


  CVE-2026-40138 (CVSS score: 9.2) - A pre-authentication vulnerability exists in the

---

## 33. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
