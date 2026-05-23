# Zero Day Pulse

> **Generated:** 2026-05-23 01:55 UTC &nbsp;|&nbsp; **Total:** 20 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 8 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE‑2024‑57727 is an unauthenticated path‑traversal vulnerability in SimpleHelp that allows attackers to download arbitrary files from the server (e.g., serverconfig.xml containing hashed passwords). Exploitation can lead to full server compromise, especially when combined with other SimpleHelp flaws such as arbitrary file upload and privilege escalation.
- **Affected Products:** SimpleHelp versions 5.5.7 and earlier (including v5.5, v5.4 up to 5.4.9, v5.3 up to 5.3.8)
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true - https://horizon3.ai/attack-research/disclosures/critical-vulnerabilities-in-simplehelp-remote-support-software/
- **Patch Available:** true - https://simple-help.com/kb---security-vulnerabilities-01-2025
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors, including groups such as DragonForce as reported by Sophos
- **Mitigation:** Upgrade immediately to patched SimpleHelp versions (v5.5.8, v5.4.10, v5.3.9); isolate or stop internet‑exposed SimpleHelp instances; hunt for compromise indicators such as unexpected API tokens and suspicious executables; apply vendor‑provided patches; follow CISA mitigation guidance if patching is not immediately possible.
- **Vendor Advisory:** https://simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — We hardened zizmor's GitHub Actions static analyzer

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Trail of Bits Blog &nbsp;|&nbsp; **Published:** 2026-05-22
**Reference:** <https://blog.trailofbits.com/2026/05/22/we-hardened-zizmors-github-actions-static-analyzer/>

> In March 2026, attackers exploited a pull_request_target misconfiguration in the aquasecurity/trivy-action GitHub Action to exfiltrate organization and repository secrets, then used those credentials to backdoor LiteLLM on PyPI (see Trivy’s post-mortem for the full timeline). zizmor is a static analyzer that GitHub Actions users run to catch exactly these misconfigurations before they ship. When G…

**Parallel AI Enrichment:**

- **Technical Details:** Attackers exploited a pull_request_target misconfiguration in the aquasecurity/trivy-action to run malicious code during CI runs. The injected malware (TeamPCP Cloud stealer) captured runner memory, harvested SSH, cloud, and Kubernetes secrets, encrypted the data with AES‑256+RSA‑4096, and exfiltrated it. Using the stolen credentials, they published malicious LiteLLM versions 1.82.7 and 1.82.8 to PyPI, enabling further compromise.
- **Affected Products:** aquasecurity/trivy-action (GitHub Action), LiteLLM 1.82.7, LiteLLM 1.82.8, zizmor
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Update zizmor to the latest version with full YAML anchor support; avoid using pull_request_target in GitHub Actions; enforce least‑privilege CI/CD credentials; monitor for unauthorized PyPI package releases; rotate any compromised secrets immediately.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) – attackers place malicious instructions or payloads in web content, comments, or other untrusted inputs which AI agents ingest; when agents incorporate that content into their context or execution (e.g., code‑review actions, agent plugins), injected instructions can override intended prompts or cause unauthorized actions ("Comment and Control" is an example exploiting AI agents' elevated access).
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Treat external/untrusted content as adversarial input; apply input sanitization and filtering, implement strict prompt/role separation and safety policies, least‑privilege for agent actions, on‑model mitigations (e.g., model‑level instruction resistance), runtime checks and human‑in‑the‑loop for high‑risk actions, restrict agent access to code execution or secrets, and patch vendor components when advisories are issued.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection works by embedding malicious instructions into auxiliary data sources or tool outputs that the LLM consumes, causing the model to execute those instructions as part of its response generation.
- **Affected Products:** Google Workspace (Gemini integration)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (http://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads)
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Implement continuous monitoring of data sources, enforce strict content filtering for LLM inputs, and restrict or audit automated agentic actions within Workspace.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The primary new threat facing all agentic browsers is indirect prompt injection—malicious instructions hidden in web content (pages, iframes, user‑generated content) that can influence an agentic model to take unwanted actions (e.g., financial transactions or data exfiltration). Chrome limits model exposure with origin gating, uses a separate User Alignment Critic to vet actions, runs a real‑time prompt‑injection classifier, enforces deterministic checks on model‑generated URLs, and requires user confirmations for sensitive actions.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Key mitigations include: a User Alignment Critic that vets agent actions; origin gating (Origin Sets) to restrict readable/writable origins; a real‑time prompt‑injection classifier; deterministic checks on model‑generated URLs; mandatory user confirmations and transparent work‑log for critical steps; continuous red‑teaming, monitoring and response; and updated Vulnerability Rewards Program (VRP) guidance for reporting agentic‑capability vulnerabilities.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow in unsafe Rust code of the CrabbyAVIF image decoder could overwrite adjacent memory. Android’s Scudo hardened allocator placed guard pages around secondary allocations, making the overflow non‑exploitable.
- **Affected Products:** Android platform (CrabbyAVIF component)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true – https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Update Android devices to the security patch level 2025-11-01 or later, which includes the CrabbyAVIF fix (link above). If immediate update is not possible, ensure Scudo is enabled to retain the non‑exploitable state.
- **Vendor Advisory:** https://source.android.com/security/bulletin/2025-11-01

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection — hidden malicious instructions embedded in external data sources (emails, documents, calendar invites, web content) that instruct generative AI systems to exfiltrate data or perform unauthorized actions; attack leverages AI systems that ingest multiple external data sources without adequate provenance, policy enforcement, or context isolation.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Layered defense strategy: provenance and source validation, content sanitization/filters, strict policy enforcement and action gating, least‑privilege for data access, telemetry and anomaly detection, and user confirmations for high‑risk actions. Use model‑restricted action interfaces and deny unsafe content by default.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state‑sponsored actors infiltrated and backdoored major telecom routers and leveraged compromised devices and trusted connections to pivot, modify routers for persistent long‑term access to networks.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon (UNCXXXXX), OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Inventory SD‑WAN and router devices; apply vendor updates; isolate and rebuild compromised devices; rotate credentials; implement network segmentation and monitoring per CISA guidance.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** GRU Unit 26165 conducts espionage by abusing spear‑phishing and malicious calendar invites to trigger Outlook NTLM relay (CVE‑2023‑23397), delivering arbitrary code via crafted WinRAR archives (CVE‑2023‑38831), and exploiting XSS/command execution flaws in Roundcube Webmail (CVE‑2020‑12641, CVE‑2020‑35730, CVE‑2021‑44026). Compromised systems are leveraged with native tools (Impacket, PsExec, Certipy) for lateral movement, Active Directory data exfiltration, and credential theft, while vulnerable SOHO devices and VPNs provide footholds.
- **Affected Products:** IP camera brands/models (various), RARLAB WinRAR (CVE-2023-38831), Roundcube Webmail (CVE-2020-12641, CVE-2020-35730, CVE-2021-44026), Microsoft Outlook (CVE-2023-23397), exposed VPN infrastructure, corporate VPNs, SOHO device models
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true - https://aka.ms/CVE-2023-23397ScriptDoc
- **Patch Available:** true - https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a
- **Active Exploitation:** true
- **Threat Actors:** GRU Unit 26165 (APT28 / Fancy Bear / Forest Blizzard / Blue Delta)
- **Mitigation:** Apply vendor patches and firmware updates; disable or harden NTLM and legacy protocols; harden email infrastructure and monitor for NTLM relay and suspicious calendar invites; implement network segmentation and Zero Trust controls; restrict RDP/VPN access and monitor logs; disable remote access on IP cameras, update firmware, and place cameras behind firewalls.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — Trend Micro warns of Apex One zero-day exploited in the wild

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-05-22
**Reference:** <https://www.bleepingcomputer.com/news/security/trend-micro-warns-of-apex-one-zero-day-exploited-in-attacks/>

> Japanese cybersecurity software company Trend Micro has addressed an Apex One zero-day vulnerability exploited in attacks targeting Windows systems. [...]

**Parallel AI Enrichment:**

- **Technical Details:** A directory traversal vulnerability in the on‑premises Apex One server allows a pre‑authenticated attacker with access to the Apex One Server to modify key server files/tables enabling code injection or malicious modifications.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — https://success.trendmicro.com/en-US/solution/KA-0023430
- **Active Exploitation:** true — Bleeping Computer, SecurityWeek, SecurityAffairs, CISA
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Apply Trend Micro’s vendor updates/patches; restrict network access to Apex One Server, harden server access, monitor logs for suspicious file modifications.
- **Vendor Advisory:** https://success.trendmicro.com/en-US/solution/KA-0023430

---

## 11. 🟠 Zero-Day — Paved With Intent: ROADtools and Nation-State Tactics in the Cloud

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Unit 42 (Palo Alto) &nbsp;|&nbsp; **Published:** 2026-05-22
**Reference:** <https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/>

> Open-source framework ROADtools is being misused by threat actors for cloud intrusions. Learn how to identify its malicious use. The post Paved With Intent: ROADtools and Nation-State Tactics in the Cloud appeared first on Unit 42 .

---

## 12. 🟠 Zero-Day — TrendAI Patches Apex One Zero-Day Exploited in the Wild

**CVE:** `CVE-2026-34926` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-05-22
**Reference:** <https://www.securityweek.com/trendai-patches-apex-one-zero-day-exploited-in-the-wild/>

> CVE-2026-34926 is a directory traversal flaw that can be exploited against the on-premise version of Apex One. The post TrendAI Patches Apex One Zero-Day Exploited in the Wild appeared first on SecurityWeek .

---

## 13. 🟡 High Severity — Nezha Monitoring: Nezha WebSocket server stream discloses cross-tenant server telemetry to authenticated members

**CVE:** `CVE-2026-47124` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://github.com/advisories/GHSA-hvv7-hfrh-7gxj>

> ### Summary

Any authenticated non-admin member can connect to the server-status WebSocket and receive telemetry for all servers, including servers owned by other users. The normal server list API filters objects by `HasPermission`, but the WebSocket stream treats the presence of any authenticated user as authorization for the full unfiltered server list.

### Details

The server WebSocket route i…

---

## 14. 🟡 High Severity — Nezha Monitoring: RoleMember can run shell on every server (cross-tenant RCE) via POST /api/v1/cron

**CVE:** `CVE-2026-46716` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://github.com/advisories/GHSA-99gv-2m7h-3hh9>

> ## Summary

`nezha`&#x27;s dashboard supports two user roles: `RoleAdmin` (Role==0) and `RoleMember` (Role==1). The cron routes `POST /api/v1/cron` and `PATCH /api/v1/cron/:id` are wired through `commonHandler` (any authenticated user) rather than `adminHandler`, and the per-server permission check on cron creation has a vacuous-true bypass.

A `RoleMember` user can create a scheduled cron task wi…

---

## 15. 🟡 High Severity — Arcane: Missing admin authorization on global variables endpoint

**CVE:** `CVE-2026-47125` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://github.com/advisories/GHSA-jpjh-jm2p-39hh>

> ## Summary

The `PUT /api/environments/{id}/templates/variables` endpoint, which writes the system-wide `.env.global` file used for variable substitution in every project&#x27;s compose file, is missing an admin authorization check. Any authenticated non-admin user can call this endpoint with their bearer token or API key and overwrite the global environment variables that are merged into every pr…

---

## 16. 🟡 High Severity — Parse Server: Pre-authentication denial of service via client version header regex backtracking

**CVE:** `CVE-2026-47138` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://github.com/advisories/GHSA-38m6-82c8-4xfm>

> ### Impact

An unauthenticated attacker who knows a publicly-known Parse Application ID can submit a single HTTP request whose client SDK version field contains adversarial input that triggers polynomial backtracking in a request-header parser. The parsing runs before session authentication and before rate limiting on every `/parse/*` request, so the request consumes seconds to minutes of synchron…

---

## 17. 🟡 High Severity — Nezha Monitoring: RoleMember can fire other users' cron tasks via AlertRule.FailTriggerTasks (no ownership check)

**CVE:** `CVE-2026-47120` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://github.com/advisories/GHSA-rxf6-wjh4-jfj6>

> ## Summary

`createAlertRule` and `createService` (and their `update*` siblings) accept `FailTriggerTasks []uint64` and `RecoverTriggerTasks []uint64` — IDs of cron tasks to fire when the alert/service trips. The validation function only validates the alert&#x27;s `Rules.Ignore` server map; it never checks that the cron task IDs in `FailTriggerTasks` / `RecoverTriggerTasks` belong to the caller.

…

---

## 18. 🟡 High Severity — Nezha Monitoring: RoleMember-reachable SSRF with full response-body reflection via POST /api/v1/notification

**CVE:** `CVE-2026-46717` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://github.com/advisories/GHSA-w4g9-mxgg-j532>

> ## Summary

nezha&#x27;s dashboard supports two user roles: `RoleAdmin` (Role==0) and `RoleMember` (Role==1). The notification routes `POST /api/v1/notification` and `PATCH /api/v1/notification/:id` are wired through `commonHandler` rather than `adminHandler` — so a `RoleMember` user can call them. These handlers synchronously `Send()` an HTTP request to a user-controlled URL and reflect the *enti…

---

## 19. 🟡 High Severity — CISA Adds Exploited Langflow and Trend Micro Apex One Vulnerabilities to KEV

**CVE:** `CVE-2025-34291` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-22
**Reference:** <https://thehackernews.com/2026/05/cisa-adds-exploited-langflow-and-trend.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Thursday added two security flaws impacting Langflow and Trend Micro Apex One to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

The vulnerabilities in question are listed below -


  CVE-2025-34291 (CVSS score: 9.4) - An origin validation error vulnerability in Langflow that could

---

## 20. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
