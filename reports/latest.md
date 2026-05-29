# Zero Day Pulse

> **Generated:** 2026-05-29 02:01 UTC &nbsp;|&nbsp; **Total:** 26 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 14 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** An unauthenticated path traversal vulnerability enables remote attackers to traverse directories and read arbitrary files (including logs, configuration files, and credentials) on vulnerable SimpleHelp servers.
- **Affected Products:** SimpleHelp 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (unspecified groups)
- **Mitigation:** Upgrade SimpleHelp to version 5.5.8 or later. If immediate patching is not possible, disable remote access to the SimpleHelp service and monitor for anomalous file access.
- **Vendor Advisory:** http://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570

---

## 2. 🟠 Zero-Day — New Gogs zero-day flaw lets hackers get remote code execution

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://www.bleepingcomputer.com/news/security/new-gogs-zero-day-flaw-lets-hackers-get-remote-code-execution/>

> An unpatched zero-day vulnerability in the Gogs self-hosted Git service can allow attackers to gain remote code execution (RCE) on Internet-facing instances. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Improper handling of symbolic links in Gogs' repository file editing feature allows an attacker to craft symlinks that cause file overwrite outside the repository, which can be leveraged to execute arbitrary code on the host.
- **Affected Products:** Gogs (self‑hosted Git service)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (source: http://wiz.io/blog/wiz-research-gogs-cve-2025-8110-rce-exploit)
- **Patch Available:** false
- **Active Exploitation:** true (sources: http://diamatix.com/active-gogs-vulnerability-code-execution-2026, http://securityweek.com/unpatched-gogs-zero-day-exploited-for-months, http://thehackernews.com/2025/12/unpatched-gogs-zero-day-exploited.html, http://bleepingcomputer.com/news/security/unpatched-gogs-zero-day-rce-flaw-actively-exploited-in-attacks)
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — Critical FortiClient EMS Vulnerability Exploited in Fresh Attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://www.securityweek.com/critical-forticlient-ems-vulnerability-exploited-in-fresh-attacks/>

> Fortinet rolled out hotfixes for the security defect in April, warning that it had been exploited in the wild as a zero-day and urging immediate patching. The post Critical FortiClient EMS Vulnerability Exploited in Fresh Attacks appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Improper access control (CWE-284) in FortiClient EMS allows an unauthenticated attacker to execute unauthorized code or commands via crafted requests.
- **Affected Products:** FortiClient EMS 7.4.5, FortiClient EMS 7.4.6
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Install the FortiClient EMS hotfix for 7.4.5 and 7.4.6; upgrade to 7.4.7 when available. If unable to patch, restrict network access to EMS, isolate EMS management interfaces, and monitor for suspicious activity.
- **Vendor Advisory:** https://fortiguard.fortinet.com/psirt/FG-IR-26-099

---

## 4. 🟠 Zero-Day — Download pumping: New npm deception technique for supply chain attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Tenable Security Research &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://www.tenable.com/blog/how-cyberattackers-inflate-malicious-package-npm-download-counts>

> Learn how attackers exploit automated bot traffic as part of software supply chain attacks to artificially inflate download counters and mask malicious payloads as legitimate. Key takeaways Volume doesn’t equal trust. Packages with numerous versions and high download counts might seem legitimate, but attackers can easily manipulate those metrics. Attackers exploit automated infrastructure. By init…

**Parallel AI Enrichment:**

- **Technical Details:** Attackers publish large numbers of benign package versions to public registries, triggering automated mirrors, scanners and analysis bots to download each version (approx. 100–150 automated downloads per version), thereby inflating download counts and creating a dense version history; after establishing apparent legitimacy attackers later publish malicious payloads (example: “ambar-src” had 724 versions, ~50,000 downloads) — Tenable validated via PoC that version flooding and direct tarball requests produce inflated metrics.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true - https://www.tenable.com/blog/how-cyberattackers-inflate-malicious-package-npm-download-counts
- **Patch Available:** false
- **Active Exploitation:** true - https://www.tenable.com/blog/how-cyberattackers-inflate-malicious-package-npm-download-counts
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Do not rely on download counts or version history; use version pinning, enforce minimum package‑age restrictions (3–4 days), use ephemeral CI/CD runners, enforce least‑privilege network access, and use security tooling/registry features like npm package‑age checks and stronger publisher authentication.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is adversarially crafted content seeded on public web pages that persuades or overrides an AI agent's system/user instructions when the agent browses or ingests that content, causing it to reveal secrets, execute privileged actions, or perform malicious tasks. Attack vectors include specially formatted payloads embedded in web pages, code‑review contexts, or documentation that an AI tool will parse.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Treat web content as untrusted; restrict AI agent browsing and elevated privileges; sanitize and canonicalize scraped content; apply strict instruction‑guardrails and output filters; monitor for IPI patterns and block known payloads; apply vendor patches where specific product issues are identified (e.g., Anthropic patched Claude Code).
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) leverages data or tool inputs fed to a large language model (LLM) to embed malicious instructions. By contaminating these inputs, an attacker can steer the LLM's response or trigger unwanted actions without the user providing explicit malicious prompts.
- **Affected Products:** Google Workspace (Gemini integration)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Implement layered defenses: 1) Apply content‑filtering on data inputs to LLMs; 2) Deploy real‑time analytics to detect and block IPI URLs (Stage 3 redirect); 3) Enforce strict validation of tool outputs used by the LLM; 4) Monitor for known IPI indicators of compromise.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The primary issue is indirect prompt injection (IPI): untrusted web content can influence an agentic browser's AI by injecting prompts via web pages or third‑party resources, causing unintended or unsafe AI actions. Defenses focus on detecting and blocking IPI, constraining origin‑based access, and adding runtime checks to prevent unsafe agent behaviors.
- **Affected Products:** Chrome (agentic browsing / Gemini integration) — specific versions unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Use Chrome's new layered defenses for agentic browsing: block prompt injections, restrict origin access, prevent unsafe AI actions; follow vendor guidance to limit agentic features on untrusted sites and apply least‑privilege origin access.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Linear buffer overflow in CrabbyAVIF (unsafe Rust) was neutralized by Android's Scudo hardened allocator, which added guard pages surrounding allocations, turning the overflow into a non‑exploitable crash.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true - https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Deploy and maintain the Scudo hardened allocator, improve crash reporting to detect overflow attempts, conduct unsafe‑Rust code reviews and training, and encapsulate unsafe blocks.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack where malicious instructions are embedded in external data sources (emails, documents, calendar invites, web content) that are then ingested by generative AI systems or AI agents, causing the model or agent to execute unauthorized actions (data exfiltration or command execution) by treating the hidden instructions as part of user prompts or context. Attack vectors include poisoned third‑party content, comments in code/repos, or crafted files that are consumed by automated agents.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true.
- **Threat Actors:** None known.
- **Mitigation:** Layered defenses: input sanitization and provenance checks; minimizing sensitive data in contexts; strict tool/agent capability gating and permissions; model instruction filtering and red‑teaming; monitoring and anomaly detection; use of content provenance and content signatures; user confirmation for high‑risk actions.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors target large backbone routers and provider edge (PE) and customer edge (CE) routers, modify router firmware/configuration to maintain persistent, long‑term access, and pivot via compromised devices and trusted connections into government, telecom, transportation, lodging, and military networks.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor, Chinese state-sponsored actors (general)
- **Mitigation:** Apply vendor‑provided router patches if available; isolate and rebuild compromised routers; restrict and monitor management interfaces; apply strong authentication (MFA) for admin access; segment networks and limit trust relationships; monitor for persistence (firmware/configuration changes), rotate credentials and keys; implement network telemetry and detection for anomalous routing/traffic.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 12. 🟠 Zero-Day — Microsoft Slams Public Zero-Day Disclosures Amid GitHub Researcher Account Removal

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://thehackernews.com/2026/05/microsoft-slams-public-zero-day.html>

> Microsoft has come out strongly in favor of Coordinated Vulnerability Disclosure (CVD), urging the research community to share their findings and give affected vendors an opportunity to better understand the impact and address them before they are publicly disclosed.

The development comes after a researcher named Chaotic Eclipse (aka Nightmare-Eclipse) disclosed details of multiple zero-day

---

## 13. 🟡 High Severity — Dulwich has an arbitrary file write via NTFS-hostile tree entries on Windows

**CVE:** `CVE-2026-42305` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-897w-fcg9-f6xj>

> ## Impact

Arbitrary file write leading to remote code execution when cloning or checking out a malicious Git repository on Windows.

Dulwich&#x27;s path-element validator accepted tree entries whose filenames contained bytes that Windows interprets as structural path syntax:

  - \ — the Windows path separator. A single tree entry named .git\hooks\pre-commit.exe was treated as one valid filename …

---

## 14. 🟡 High Severity — nono: Sandbox escape on Linux via D-Bus: `systemd-run --user`

**CVE:** `CVE-2026-47128` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-27vp-2mmc-vmh3>

> ### Summary

The nono Landlock/seccomp policies allow access to local Unix domain sockets (concrete and abstract). This allows an easy sandbox escape by talking to the per-user systemd dbus socket.

Threat scenario: Running Aider, Claude Code, OpenCode or similar tools with &quot;allow bash&quot; policy so that it can invoke arbitrary host tools like `make`, `gcc`, etc. to write code.

### Reprodu…

---

## 15. 🟡 High Severity — local-deep-research has an SSRF bypass in `safe_get`

**CVE:** `CVE-2026-46526` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-g23j-2vwm-5c25>

> ### Summary
The URL checking logic in local-deep-research has a logical flaw that could be bypassed by attackers, leading to SSRF attacks.

### Details
The current project uses `validate_url` to validate the input URL. The main logic is to perform security checks on the host portion of the URL extracted by urlparse to prevent SSRF attacks.

&lt;img width=&quot;1173&quot; height=&quot;1107&quot; al…

---

## 16. 🟡 High Severity — compliance-trestle Vulnerable to Remote Code Execution via Recursive Server-Side Template Injection (SSTI)

**CVE:** `CVE-2026-46439` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-gg2g-p7xc-qqmm>

> A High severity Server-Side Template Injection (SSTI) vulnerability exists in the `trestle author jinja` command. The command recursively evaluates rendered templates, allowing an attacker to achieve arbitrary command execution with privileges of the running process by injecting malicious payloads into data fields (such as SSP documents or Lookup Tables).

**The vulnerability does not require atta…

---

## 17. 🟡 High Severity — compliance-trestle Vulnerable to SSRF in Remote Fetching Subsystem

**CVE:** `CVE-2026-46380` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-w76h-q7c6-jpjp>

> A source code audit led to the discovery of three significant security vulnerabilities in the trestle/core/remote/cache.py module.

**Finding 1 (Critical): SSRF (CWE-918)**
The HTTPSFetcher._do_fetch() method passes a user-supplied URL directly to requests.get() without validation. This allows an attacker to perform Server-Side Request Forgery, targeting internal services or cloud metadata endpoin…

---

## 18. 🟡 High Severity — OpenCTI: Privilege escalation via graphQL API is abusable by organization admins, due to incorrect ACL on userEdit relationAdd

**CVE:** `CVE-2026-44730` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-q537-qhj4-wcjx>

> ### Summary
An organization admin can escalate their privileges by adding a user from a different organization with higher privileges, to their own organization.

### Impact
Full platform access, access to sensitive or proprietary information.

---

## 19. 🟡 High Severity — OpenBao's cross-namespace lease revocation via legacy sys/revoke path bypasses ACL

**CVE:** `CVE-2026-45808` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-v8v8-cm84-m686>

> # Impact

OpenBao&#x27;s namespaces provide multi-tenant separation. A tenant who intentionally leaks lease identifiers can have their lease and underlying credential revoked or renewed by a user in another tenant via the legacy, undocumented `sys/revoke` and `sys/renew` endpoints.

# Patch

This will be addressed in v2.5.4.

---

## 20. 🟡 High Severity — Symfony's Mailtrap Mailer Webhook Parser Never Verifies the X-Mt-Signature HMAC — Unauthenticated Webhook Event Injection

**CVE:** `CVE-2026-45755` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-59f3-vp2f-mp9w>

> ### Description

The Mailtrap mailer bridge ships a webhook request parser used to authenticate and decode the event callbacks Mailtrap POSTs to an application&#x27;s webhook endpoint. Its `doParse(Request $request, #[\SensitiveParameter] string $secret)` method receives the configured webhook secret but never reads it; it decodes and returns the payload unconditionally, ignoring the `X-Mt-Signatu…

---

## 21. 🟡 High Severity — Symfony's Mailjet Mailer Webhook Parser Never Verifies the Configured Secret — Unauthenticated Webhook Event Injection

**CVE:** `CVE-2026-45754` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-64hg-93w9-fc35>

> ### Description

The Mailjet mailer bridge and the LOX24 SMS notifier bridge both ship webhook request parsers used to authenticate and decode the event callbacks each provider POSTs to an application&#x27;s webhook endpoint. Their `doParse(Request $request, #[\SensitiveParameter] string $secret)` methods receive the configured webhook secret but never read it; they convert and return the payload …

---

## 22. 🟡 High Severity — opentelemetry-go's Schema ParseFile leaks file descriptors on each parse

**CVE:** `CVE-2026-45287` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-995v-fvrw-c78m>

> ### Summary

`go.opentelemetry.io/otel/schema/v1.0` and `go.opentelemetry.io/otel/schema/v1.1` leaks one file descriptor on each successful `ParseFile` call. `ParseFile` opens the schema file and passes it to `Parse` without closing it; repeated parsing in a long-running process can exhaust the process file descriptor limit and cause denial of service. The severity is low because exploitation depe…

---

## 23. 🟡 High Severity — opentelemetry-go's baggage parsing no longer caps raw header length

**CVE:** `CVE-2026-41178` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-5wrp-cwcj-q835>

> ### Summary

https://github.com/open-telemetry/opentelemetry-go/pull/7880 removed raw-length rejection and it causes `Parse` to process arbitrarily large/invalid baggage headers and log errors, enabling DoS via oversized inputs.


### Details

The commit removes the upfront baggage-string length check and the per-member size guard in parsing. `Parse` now walks the entire input with `strings.SplitS…

---

## 24. 🟡 High Severity — Capsule TenantResource RawItems Cluster-Scoped Resource Creation Vulnerability

**CVE:** `CVE-2026-22872` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-qjjm-7j9w-pw72>

> # TenantResource RawItems Cluster-Scoped Resource Creation Vulnerability


## Summary

The Capsule Controller runs with cluster-admin privileges. Although the TenantResource RawItems processing logic forcibly sets the namespace, this is ineffective for cluster-scoped resources. Tenant administrators can leverage the Controller&#x27;s elevated privileges to create cluster-scoped resources (such as …

---

## 25. 🟡 High Severity — Capsule Namespace Hijacking via subresource

**CVE:** `CVE-2026-30963` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-2ww6-hf35-mfjm>

> ### Summary
To defend against namespace hijacking achieved through update/patch operations on namespaces, Capsule uses a webhook to validate update requests targeting namespaces. However, in Kubernetes, the namespace/finalize and namespace/status subresource APIs can also modify various fields of a namespace, including the metadata field. The webhook does not define interception rules for these su…

---

## 26. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
