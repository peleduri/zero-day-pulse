# Zero Day Pulse

> **Generated:** 2026-05-23 08:05 UTC &nbsp;|&nbsp; **Total:** 21 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 7 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal vulnerabilities in SimpleHelp RMM allow unauthenticated remote attackers to retrieve sensitive files (logs, configs, credentials) and potentially move laterally to compromise downstream customers.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) versions 5.5.7 and earlier
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** Public PoCs and walkthroughs are available (e.g., TryHackMe and Medium articles).
- **Patch Available:** Patch availability unclear; no official patch URL available.
- **Active Exploitation:** Confirmed active exploitation reported by CISA and security vendors; ransomware actors leveraged unpatched SimpleHelp RMM in the wild.
- **Threat Actors:** Ransomware actors (unspecified groups)
- **Mitigation:** Apply vendor updates if available; isolate/unplug affected RMM servers from internet; block or monitor SimpleHelp default ports; enforce network segmentation, multi‑factor authentication, rotate credentials, implement endpoint detection and response, and maintain regular backups.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 2. 🟠 Zero-Day — Drupal Core SQL Injection Bug Actively Exploited, Added to CISA KEV

**CVE:** `CVE-2026-9082` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://thehackernews.com/2026/05/drupal-core-sql-injection-bug-actively.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has added a recently patched critical security flaw impacting Drupal Core to its Known Exploited Vulnerabilities (KEV) catalog, based on evidence of active exploitation.

The vulnerability in question is CVE-2026-9082 (CVSS score: 6.5), an SQL injection vulnerability affecting all supported versions of Drupal Core.

&quot;Drupal Core

**Parallel AI Enrichment:**

- **Technical Details:** SQL injection in Drupal Core database abstraction layer allows an unauthenticated attacker to send specially crafted requests, resulting in arbitrary SQL execution on sites using PostgreSQL.
- **Affected Products:** Drupal Core (all supported versions) – PostgreSQL-backed installations
- **CVSS Score:** 6.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N
- **Exploit Available:** Public PoC and exploit reports published; example: https://www.tenable.com/blog/cve-2026-9082-highly-critical-sql-injection-vulnerability-in-drupal-core-sa-core-2026-004
- **Patch Available:** Yes — official Drupal patch available in SA-CORE-2026-004: https://www.drupal.org/sa-core-2026-004
- **Active Exploitation:** Confirmed active exploitation; reported by CISA KEV catalog and The Hacker News article.
- **Threat Actors:** None known
- **Mitigation:** Apply the SA-CORE-2026-004 patch immediately; temporarily restrict public access, deploy WAF rules to block exploit patterns, and audit PostgreSQL‑backed sites.
- **Vendor Advisory:** https://www.drupal.org/sa-core-2026-004

---

## 3. 🟠 Zero-Day — We hardened zizmor's GitHub Actions static analyzer

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Trail of Bits Blog &nbsp;|&nbsp; **Published:** 2026-05-22
**Reference:** <https://blog.trailofbits.com/2026/05/22/we-hardened-zizmors-github-actions-static-analyzer/>

> In March 2026, attackers exploited a pull_request_target misconfiguration in the aquasecurity/trivy-action GitHub Action to exfiltrate organization and repository secrets, then used those credentials to backdoor LiteLLM on PyPI (see Trivy’s post-mortem for the full timeline). zizmor is a static analyzer that GitHub Actions users run to catch exactly these misconfigurations before they ship. When G…

**Parallel AI Enrichment:**

- **Technical Details:** A `pull_request_target` workflow misconfiguration let untrusted code execute with access to repository and organization secrets. Attackers used stolen CI credentials to force‑push malicious tags to `aquasecurity/trivy-action` and `aquasecurity/setup-trivy`, and published litellm PyPI versions 1.82.7/1.82.8 containing malicious payloads. The pre‑hardening version of zizmor could not correctly analyze YAML anchors, missing the misconfiguration.
- **Affected Products:** aquasecurity/trivy-action (multiple malicious tags), aquasecurity/setup-trivy, litellm PyPI packages versions 1.82.7 and 1.82.8, zizmor (pre‑2026‑05‑22 version)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC is publicly released; the exploitation was observed through malicious litellm packages (see Trend Micro report).
- **Patch Available:** Trail of Bits released a hardened version of zizmor with fixes (see https://blog.trailofbits.com/2026/05/22/we-hardened-zizmors-github-actions-static-analyzer/). No official vendor patch for the GitHub Actions platform.
- **Active Exploitation:** Confirmed active exploitation reported by the Trivy advisory and Trend Micro/Snyk analyses.
- **Threat Actors:** TeamPCP
- **Mitigation:** Avoid using `pull_request_target` with untrusted code, restrict secret and token permissions, rotate any compromised credentials, remove or replace malicious Git tags, verify published packages (especially litellm), and run the hardened zizmor release for static analysis. Apply least‑privilege principles to actions and OIDC tokens.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) involves adversarial content on web pages or third‑party artifacts (e.g., comments, GitHub Action messages) that AI agents ingest, causing the agents to execute injected instructions. The "Comment and Control" technique weaponizes an AI agent's elevated access to process untrusted user data.
- **Affected Products:** Claude Code (versions prior to fixed releases)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof‑of‑concepts are described in the SentinelOne vulnerability database and The Hacker News article.
- **Patch Available:** A patch has been released for Anthropic's Claude Code; details at https://www.anthropic.com/security.
- **Active Exploitation:** Confirmed active exploitation has been reported in the wild, as described in the Google Security Blog.
- **Threat Actors:** None known
- **Mitigation:** Harden agents by filtering untrusted content, limiting agent privileges, sandboxing, using allowlists, and monitoring. Anthropic has published a patch for Claude Code.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when malicious instructions are injected into data sources or tools the LLM consults while fulfilling a user query (e.g., documents, web content, plugins). The LLM can be influenced to follow injected instructions because those instructions appear in contextual input or tool outputs, sometimes without explicit user input. IPI is an architectural/behavioral threat requiring layered mitigations rather than a single patch.
- **Affected Products:** Google Workspace (Gemini in Workspace, Gemini‑powered apps)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit for this specific Google advisory.
- **Patch Available:** No vendor patch (IPI is an application/architecture threat rather than a software bug).
- **Active Exploitation:** Reports of IPI‑style attacks in the wild have been published, but no public reports attribute active exploitation specifically to this Google advisory at time of publication.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses as recommended by Google: (1) input/data provenance and filtering, (2) instruction/context attribution and strict prompt engineering, (3) tool/data access controls and least privilege, (4) model-level instruction filters and refusal behaviors, (5) detection/monitoring and human‑in‑the‑loop review for high‑risk actions, (6) content validation and canonicalization of external data sources.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection occurs when malicious content on a website, iframe, or user‑generated input injects instructions that cause the AI agent to perform unintended actions such as financial transactions or data exfiltration. The injected prompt is treated as part of the agent’s planning input, leading it to execute the attacker‑supplied commands.
- **Affected Products:** Chrome (agentic browsing feature), Gemini in Chrome
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept exploit is known.
- **Patch Available:** No traditional patch has been released; security is addressed via architectural mitigations described in the vendor advisory.
- **Active Exploitation:** No confirmed active exploitation of Chrome’s agentic browsing feature has been reported.
- **Threat Actors:** None known
- **Mitigation:** Deploy a user‑alignment critic model isolated from untrusted content to vet agent actions; extend Chrome’s origin‑isolation into ‘Agent Origin Sets’ to limit accessible origins; require explicit user confirmation for sensitive actions (banking, medical sites, password manager, purchases); run a real‑time prompt‑injection classifier in parallel with the planning model; continuously red‑team with generated malicious sites.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Race condition in Rust‑based Android Binder (rust_binder) unsafe block removing nodes from a linked death_list without proper synchronization leading to linked‑list corruption, kernel panics and local denial‑of‑service.
- **Affected Products:** Linux kernel 6.18+ with Rust Binder driver enabled (CONFIG_ANDROID_BINDER_IPC_RUST=y); some Android downstream kernels with Rust Binder backports
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC known; no evidence of exploitation in the wild as of reports.
- **Patch Available:** Official patches available (Linux kernel fixes referenced in advisories). See kernel patch links in advisories.
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Apply official kernel patches or rebuild kernels without CONFIG_ANDROID_BINDER_IPC_RUST; restrict local access and monitor logs for rust_binder crashes. Scudo allocator reduces exploitability for buffer‑overflow issues in other Rust components.
- **Vendor Advisory:** https://blog.google/security/rust-in-android-move-fast-fix-things/

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injections embed hidden malicious instructions within external data sources that are later incorporated into AI prompts, leading to unauthorized actions such as data exfiltration or command execution.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept exploit is known for this vulnerability.
- **Patch Available:** No official patch has been released for this vulnerability.
- **Active Exploitation:** No confirmed active exploitation has been reported for this vulnerability.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors modify router configurations for lateral movement and use virtualized containers on network devices to evade detection, leveraging publicly known CVEs in Cisco IOS/IOS XE and Ivanti products to gain initial access.
- **Affected Products:** Cisco IOS XE, Cisco IOS, Ivanti
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept or weaponised exploit is referenced in the advisory.
- **Patch Available:** Patches have been released by the affected vendors (Cisco, Ivanti); see the advisory for details.
- **Active Exploitation:** Confirmed active exploitation has been reported; the advisory includes IOCs and notes that the actors are currently exploiting the listed CVEs.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching, disable unused ports/protocols, harden credentials, monitor firmware/software integrity, and follow Cisco Guest Shell mitigation and hardening guides.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** GRU Unit 26165 conducted spearphishing with malicious links to fake login pages, performed credential‑guessing/password spraying, exploited internet‑facing services and known CVEs (Outlook NTLM CVE‑2023‑23397, WinRAR CVE‑2023‑38831, Roundcube CVEs) to harvest NTLM hashes, access mailboxes, and move laterally using tools such as Impacket, PsExec, RDP, Certipy, and OpenSSH; they also manipulated mailbox permissions for sustained email collection and exfiltrated data via OpenSSH or attacker infrastructure.
- **Affected Products:** WinRAR (CVE-2023-38831), Microsoft Outlook/Exchange (CVE-2023-23397), Roundcube Webmail (CVE-2020-12641, CVE-2020-35730, CVE-2021-44026), IP camera firmware (various vendor‑specific CVEs)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes – CISA reports that the actors weaponized Outlook NTLM (CVE‑2023‑23397) and other listed CVEs in the campaign.
- **Patch Available:** No single vendor patch for this advisory; apply vendor/maintainer patches and updates for the affected products (see vendor CVE advisories).
- **Active Exploitation:** Confirmed – CISA reports active exploitation in this espionage campaign, including weaponized use of CVE‑2023‑23397 and other CVEs.
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS), military unit 26165 – tracked as APT28 / Fancy Bear / Forest Blizzard / Blue Delta.
- **Mitigation:** Apply vendor patches/firmware updates; enable EDR and monitoring on mail servers and domain controllers; block and alert on NTLM/SMB traffic to external hosts; enable Windows attack surface reduction rules and executable allow‑listing; implement network segmentation and zero‑trust principles; harden and update IP cameras and disable unnecessary remote access; collect and monitor Windows logs and alert on suspicious use of legitimate utilities.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟠 Zero-Day — LiteSpeed cPanel Plugin CVE-2026-48172 Exploited to Run Scripts as Root

**CVE:** `CVE-2026-48172` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://thehackernews.com/2026/05/litespeed-cpanel-plugin-cve-2026-48172.html>

> A maximum-severity security vulnerability impacting LiteSpeed User-End cPanel Plugin has come under active exploitation in the wild.

The flaw, tracked as CVE-2026-48172 (CVSS score: 10.0), relates to an instance of incorrect privilege assignment that an attacker could abuse to run arbitrary scripts with elevated permissions.

&quot;Any cPanel user (including an attacker or a compromised account) …

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

## 15. 🟡 High Severity — Nezha Monitoring: Nezha WebSocket server stream discloses cross-tenant server telemetry to authenticated members

**CVE:** `CVE-2026-47124` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://github.com/advisories/GHSA-hvv7-hfrh-7gxj>

> ### Summary

Any authenticated non-admin member can connect to the server-status WebSocket and receive telemetry for all servers, including servers owned by other users. The normal server list API filters objects by `HasPermission`, but the WebSocket stream treats the presence of any authenticated user as authorization for the full unfiltered server list.

### Details

The server WebSocket route i…

---

## 16. 🟡 High Severity — Nezha Monitoring: RoleMember can run shell on every server (cross-tenant RCE) via POST /api/v1/cron

**CVE:** `CVE-2026-46716` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://github.com/advisories/GHSA-99gv-2m7h-3hh9>

> ## Summary

`nezha`&#x27;s dashboard supports two user roles: `RoleAdmin` (Role==0) and `RoleMember` (Role==1). The cron routes `POST /api/v1/cron` and `PATCH /api/v1/cron/:id` are wired through `commonHandler` (any authenticated user) rather than `adminHandler`, and the per-server permission check on cron creation has a vacuous-true bypass.

A `RoleMember` user can create a scheduled cron task wi…

---

## 17. 🟡 High Severity — Arcane: Missing admin authorization on global variables endpoint

**CVE:** `CVE-2026-47125` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://github.com/advisories/GHSA-jpjh-jm2p-39hh>

> ## Summary

The `PUT /api/environments/{id}/templates/variables` endpoint, which writes the system-wide `.env.global` file used for variable substitution in every project&#x27;s compose file, is missing an admin authorization check. Any authenticated non-admin user can call this endpoint with their bearer token or API key and overwrite the global environment variables that are merged into every pr…

---

## 18. 🟡 High Severity — Parse Server: Pre-authentication denial of service via client version header regex backtracking

**CVE:** `CVE-2026-47138` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://github.com/advisories/GHSA-38m6-82c8-4xfm>

> ### Impact

An unauthenticated attacker who knows a publicly-known Parse Application ID can submit a single HTTP request whose client SDK version field contains adversarial input that triggers polynomial backtracking in a request-header parser. The parsing runs before session authentication and before rate limiting on every `/parse/*` request, so the request consumes seconds to minutes of synchron…

---

## 19. 🟡 High Severity — Nezha Monitoring: RoleMember can fire other users' cron tasks via AlertRule.FailTriggerTasks (no ownership check)

**CVE:** `CVE-2026-47120` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://github.com/advisories/GHSA-rxf6-wjh4-jfj6>

> ## Summary

`createAlertRule` and `createService` (and their `update*` siblings) accept `FailTriggerTasks []uint64` and `RecoverTriggerTasks []uint64` — IDs of cron tasks to fire when the alert/service trips. The validation function only validates the alert&#x27;s `Rules.Ignore` server map; it never checks that the cron task IDs in `FailTriggerTasks` / `RecoverTriggerTasks` belong to the caller.

…

---

## 20. 🟡 High Severity — Nezha Monitoring: RoleMember-reachable SSRF with full response-body reflection via POST /api/v1/notification

**CVE:** `CVE-2026-46717` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://github.com/advisories/GHSA-w4g9-mxgg-j532>

> ## Summary

nezha&#x27;s dashboard supports two user roles: `RoleAdmin` (Role==0) and `RoleMember` (Role==1). The notification routes `POST /api/v1/notification` and `PATCH /api/v1/notification/:id` are wired through `commonHandler` rather than `adminHandler` — so a `RoleMember` user can call them. These handlers synchronously `Send()` an HTTP request to a user-controlled URL and reflect the *enti…

---

## 21. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
