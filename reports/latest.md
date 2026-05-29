# Zero Day Pulse

> **Generated:** 2026-05-29 14:37 UTC &nbsp;|&nbsp; **Total:** 25 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 11 &nbsp;|&nbsp; 🟡 High: 14 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal vulnerability allowing unauthenticated remote attackers to retrieve logs, configuration files, and credentials from SimpleHelp 5.5.7 and earlier.
- **Affected Products:** SimpleHelp remote support software v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (https://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570)
- **Active Exploitation:** true
- **Threat Actors:** DragonForce ransomware; generic ransomware actors
- **Mitigation:** Upgrade to SimpleHelp 5.5.8; restrict network access to SimpleHelp services; monitor logs for anomalous activity.
- **Vendor Advisory:** http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — Gogs Zero-Day Exposes Servers to Remote Code Execution

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://www.securityweek.com/gogs-zero-day-exposes-servers-to-remote-code-execution/>

> The critical-severity issue, assigned a CVSS score of 9.4, is an argument injection flaw that can be exploited by authenticated attackers via pull requests with malicious branch names. The post Gogs Zero-Day Exposes Servers to Remote Code Execution appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Argument injection / improper handling of branch names in pull requests and symbolic links allow authenticated attackers to overwrite files outside repositories, leading to remote code execution.
- **Affected Products:** Gogs (self‑hosted Git service)
- **CVSS Score:** 9.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Restrict internet access to Gogs instances, apply network‑level controls, disable repository file editing or pull‑request based editing where possible, monitor for suspicious activity; patch when vendor advisory released.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) requires an attacker to inject malicious text into the prompt or context window of an AI model. When the model processes this crafted input—such as content injected into a Claude Code context window or hidden code on a web page—the attacker can steer the model’s responses or trigger unintended behavior.
- **Affected Products:** Claude Code
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack technique where adversaries inject malicious instructions into data sources or tools that a large language model (LLM) consumes, causing the LLM to follow those instructions and alter its behavior even without direct user input. IPI targets systems that combine multiple data sources and agentic automation, leveraging untrusted content (e.g., documents, web pages, tool outputs) to manipulate model outputs.
- **Affected Products:** Google Workspace (Gemini integration and Workspace apps) — specific versions unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** false
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known.
- **Mitigation:** Layered defenses including source validation, sandboxing/limiting agentic tool actions, content filtering and sanitization, provenance and trust signals for data sources, and monitoring / behavioral anomaly detection. Vendor-specific continuous mitigation approaches are described in the Google Security Blog advisory.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is the primary threat: malicious or third‑party web content can influence agentic AI prompts or agent behavior by injecting instructions or data indirectly; Chrome’s mitigations include layered defenses to block prompt injections, restrict origin access, and prevent unsafe AI actions.
- **Affected Products:** Chrome (agentic browsing / Gemini integration) — specific versions not stated
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use Chrome’s updated agentic‑security features and layered defenses; site‑origin restrictions, prompt injection blockers, and other architectural mitigations described in Google’s advisory; follow vendor advisory for deployment guidance.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) embeds malicious instructions in external data sources (emails, documents, calendar invites) so that downstream generative AI models ingest that data and execute unintended actions or exfiltrate data. The attack leverages trust in external content and model behavior to cause rogue outputs.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Use layered defense strategy — validate and sanitize external inputs, restrict model access to sensitive data, use instruction filters and model-level guardrails, telemetry and monitoring, continuous threat hunting and updates.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** APT actors exploit publicly known CVEs in edge/network devices (e.g., CVE-2023-20198 via WSMA endpoints, CVE-2023-20273 for post‑auth command injection). They gain access through web UI or authentication bypasses, then chain to command execution, install tools via guest shells, modify ACLs, create accounts, alter TACACS+/RADIUS settings, and use PCAP, SPAN/RSPAN/ERSPAN, GRE/MPLS tunnels for data exfiltration.
- **Affected Products:** Cisco IOS, Cisco IOS XE, Cisco NX-OS, Ivanti Connect Secure, Ivanti Policy, Fortinet (potential), Juniper (potential), Nokia routers/switches (potential), Sierra Wireless devices, SonicWall (potential)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching known exploited CVEs; inventory and monitor edge devices; verify firmware/software integrity via hash comparisons; audit configurations and change management; alert on creation of PCAP/monitor sessions and unexpected ACLs or TACACS+/RADIUS servers; disable unused ports/protocols; enforce strong credential and key‑based admin authentication; disable outbound connections from management interfaces; use vendor hardening guides (Cisco IOS/XE hardening, Software Checker) and follow CISA/NSA/FBI guidance for threat hunting and incident response.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Campaign leverages spearphishing, credential harvesting, malicious shortcuts and user‑interaction malware (e.g., HEADLACE), abusing IP cameras and supply‑chain/third‑party logistics technologies to gain access and conduct espionage.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS), military unit 26165 (also tracked as APT28)
- **Mitigation:** Follow CSA mitigations — enhance email defenses and phishing training, enforce multi‑factor authentication, apply vendor security updates where available, restrict remote access, segment networks, monitor for indicators of compromise, and follow CISA/Defensive guidance in the advisory.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 10. 🟠 Zero-Day — Microsoft calls zero-day releases ‘never justifiable’ as researcher threatens to drop more

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Record by Recorded Future &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more>

> Each vulnerability was published with working proof-of-concept code to the Microsoft-owned code repository GitHub, making them immediately available to both attackers and security professionals.

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more
- **Patch Available:** false — Patch availability unknown
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42826

---

## 11. 🟠 Zero-Day — Kimsuky Deploys HTTPSpy, Expands Arsenal with HelloDoor and VS Code Tunnels

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://thehackernews.com/2026/05/kimsuky-deploys-httpspy-expands-arsenal.html>

> The North Korean state-sponsored threat actor known as Kimsuky (aka Velvet Chollima) has been attributed to a fresh set of cyber attacks targeting South Korean military and corporate entities through March and April 2026.

&quot;Kimsuky employed a range of tailored social engineering tactics, such as spoofing security software installation pages and crafting a fake Webex meeting page that leverage…

---

## 12. 🟡 High Severity — Dulwich has an arbitrary file write via NTFS-hostile tree entries on Windows

**CVE:** `CVE-2026-42305` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-897w-fcg9-f6xj>

> ## Impact

Arbitrary file write leading to remote code execution when cloning or checking out a malicious Git repository on Windows.

Dulwich&#x27;s path-element validator accepted tree entries whose filenames contained bytes that Windows interprets as structural path syntax:

  - \ — the Windows path separator. A single tree entry named .git\hooks\pre-commit.exe was treated as one valid filename …

---

## 13. 🟡 High Severity — nono: Sandbox escape on Linux via D-Bus: `systemd-run --user`

**CVE:** `CVE-2026-47128` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-27vp-2mmc-vmh3>

> ### Summary

The nono Landlock/seccomp policies allow access to local Unix domain sockets (concrete and abstract). This allows an easy sandbox escape by talking to the per-user systemd dbus socket.

Threat scenario: Running Aider, Claude Code, OpenCode or similar tools with &quot;allow bash&quot; policy so that it can invoke arbitrary host tools like `make`, `gcc`, etc. to write code.

### Reprodu…

---

## 14. 🟡 High Severity — local-deep-research has an SSRF bypass in `safe_get`

**CVE:** `CVE-2026-46526` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-g23j-2vwm-5c25>

> ### Summary
The URL checking logic in local-deep-research has a logical flaw that could be bypassed by attackers, leading to SSRF attacks.

### Details
The current project uses `validate_url` to validate the input URL. The main logic is to perform security checks on the host portion of the URL extracted by urlparse to prevent SSRF attacks.

&lt;img width=&quot;1173&quot; height=&quot;1107&quot; al…

---

## 15. 🟡 High Severity — compliance-trestle Vulnerable to Remote Code Execution via Recursive Server-Side Template Injection (SSTI)

**CVE:** `CVE-2026-46439` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-gg2g-p7xc-qqmm>

> A High severity Server-Side Template Injection (SSTI) vulnerability exists in the `trestle author jinja` command. The command recursively evaluates rendered templates, allowing an attacker to achieve arbitrary command execution with privileges of the running process by injecting malicious payloads into data fields (such as SSP documents or Lookup Tables).

**The vulnerability does not require atta…

---

## 16. 🟡 High Severity — compliance-trestle Vulnerable to SSRF in Remote Fetching Subsystem

**CVE:** `CVE-2026-46380` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-w76h-q7c6-jpjp>

> A source code audit led to the discovery of three significant security vulnerabilities in the trestle/core/remote/cache.py module.

**Finding 1 (Critical): SSRF (CWE-918)**
The HTTPSFetcher._do_fetch() method passes a user-supplied URL directly to requests.get() without validation. This allows an attacker to perform Server-Side Request Forgery, targeting internal services or cloud metadata endpoin…

---

## 17. 🟡 High Severity — OpenCTI: Privilege escalation via graphQL API is abusable by organization admins, due to incorrect ACL on userEdit relationAdd

**CVE:** `CVE-2026-44730` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-q537-qhj4-wcjx>

> ### Summary
An organization admin can escalate their privileges by adding a user from a different organization with higher privileges, to their own organization.

### Impact
Full platform access, access to sensitive or proprietary information.

---

## 18. 🟡 High Severity — OpenBao's cross-namespace lease revocation via legacy sys/revoke path bypasses ACL

**CVE:** `CVE-2026-45808` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-v8v8-cm84-m686>

> # Impact

OpenBao&#x27;s namespaces provide multi-tenant separation. A tenant who intentionally leaks lease identifiers can have their lease and underlying credential revoked or renewed by a user in another tenant via the legacy, undocumented `sys/revoke` and `sys/renew` endpoints.

# Patch

This will be addressed in v2.5.4.

---

## 19. 🟡 High Severity — Symfony's Mailtrap Mailer Webhook Parser Never Verifies the X-Mt-Signature HMAC — Unauthenticated Webhook Event Injection

**CVE:** `CVE-2026-45755` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-59f3-vp2f-mp9w>

> ### Description

The Mailtrap mailer bridge ships a webhook request parser used to authenticate and decode the event callbacks Mailtrap POSTs to an application&#x27;s webhook endpoint. Its `doParse(Request $request, #[\SensitiveParameter] string $secret)` method receives the configured webhook secret but never reads it; it decodes and returns the payload unconditionally, ignoring the `X-Mt-Signatu…

---

## 20. 🟡 High Severity — Symfony's Mailjet Mailer Webhook Parser Never Verifies the Configured Secret — Unauthenticated Webhook Event Injection

**CVE:** `CVE-2026-45754` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-64hg-93w9-fc35>

> ### Description

The Mailjet mailer bridge and the LOX24 SMS notifier bridge both ship webhook request parsers used to authenticate and decode the event callbacks each provider POSTs to an application&#x27;s webhook endpoint. Their `doParse(Request $request, #[\SensitiveParameter] string $secret)` methods receive the configured webhook secret but never read it; they convert and return the payload …

---

## 21. 🟡 High Severity — opentelemetry-go's Schema ParseFile leaks file descriptors on each parse

**CVE:** `CVE-2026-45287` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-995v-fvrw-c78m>

> ### Summary

`go.opentelemetry.io/otel/schema/v1.0` and `go.opentelemetry.io/otel/schema/v1.1` leaks one file descriptor on each successful `ParseFile` call. `ParseFile` opens the schema file and passes it to `Parse` without closing it; repeated parsing in a long-running process can exhaust the process file descriptor limit and cause denial of service. The severity is low because exploitation depe…

---

## 22. 🟡 High Severity — opentelemetry-go's baggage parsing no longer caps raw header length

**CVE:** `CVE-2026-41178` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-5wrp-cwcj-q835>

> ### Summary

https://github.com/open-telemetry/opentelemetry-go/pull/7880 removed raw-length rejection and it causes `Parse` to process arbitrarily large/invalid baggage headers and log errors, enabling DoS via oversized inputs.


### Details

The commit removes the upfront baggage-string length check and the per-member size guard in parsing. `Parse` now walks the entire input with `strings.SplitS…

---

## 23. 🟡 High Severity — Capsule TenantResource RawItems Cluster-Scoped Resource Creation Vulnerability

**CVE:** `CVE-2026-22872` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-qjjm-7j9w-pw72>

> # TenantResource RawItems Cluster-Scoped Resource Creation Vulnerability


## Summary

The Capsule Controller runs with cluster-admin privileges. Although the TenantResource RawItems processing logic forcibly sets the namespace, this is ineffective for cluster-scoped resources. Tenant administrators can leverage the Controller&#x27;s elevated privileges to create cluster-scoped resources (such as …

---

## 24. 🟡 High Severity — Capsule Namespace Hijacking via subresource

**CVE:** `CVE-2026-30963` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-2ww6-hf35-mfjm>

> ### Summary
To defend against namespace hijacking achieved through update/patch operations on namespaces, Capsule uses a webhook to validate update requests targeting namespaces. However, in Kubernetes, the namespace/finalize and namespace/status subresource APIs can also modify various fields of a namespace, including the metadata field. The webhook does not define interception rules for these su…

---

## 25. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
