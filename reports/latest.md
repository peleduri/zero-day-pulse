# Zero Day Pulse

> **Generated:** 2026-05-29 09:33 UTC &nbsp;|&nbsp; **Total:** 27 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 13 &nbsp;|&nbsp; 🟡 High: 14 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated path traversal in SimpleHelp web component lets remote attackers retrieve arbitrary files (including logs and configuration) and obtain credentials or session material, which can be used to authenticate as high‑privilege users.
- **Affected Products:** SimpleHelp Remote Support / RMM — versions 5.5.7 and earlier (SimpleHelp <=5.5.7)
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N
- **Exploit Available:** true — https://github.com/imjdl/CVE-2024-57727, https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2024/CVE-2024-57727.yaml
- **Patch Available:** true — https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (including DragonForce)
- **Mitigation:** Upgrade to SimpleHelp 5.5.8 immediately; if that is not possible, block access to SimpleHelp web interfaces from untrusted networks (firewall/VPN), rotate exposed credentials, monitor logs for suspicious activity, and deploy IDS/Nuclei detection templates.
- **Vendor Advisory:** https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — New Gogs zero-day flaw lets hackers get remote code execution

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://www.bleepingcomputer.com/news/security/new-gogs-zero-day-flaw-lets-hackers-get-remote-code-execution/>

> An unpatched zero-day vulnerability in the Gogs self-hosted Git service can allow attackers to gain remote code execution (RCE) on Internet-facing instances. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Improper handling of symbolic links in Gogs' repository file editing functionality allows an attacker to create or use symlinks to cause file overwrite outside the repository, enabling remote code execution by placing or modifying files on the host.
- **Affected Products:** Gogs (self‑hosted Git service)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known.
- **Mitigation:** Take Gogs instances offline from Internet exposure, restrict access (IP allowlists), disable repository file‑editing features or restrict to trusted users, monitor for suspicious file changes, apply network‑level protections and intrusion detection. Follow CISA/KEV guidance if available.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — Critical FortiClient EMS Vulnerability Exploited in Fresh Attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://www.securityweek.com/critical-forticlient-ems-vulnerability-exploited-in-fresh-attacks/>

> Fortinet rolled out hotfixes for the security defect in April, warning that it had been exploited in the wild as a zero-day and urging immediate patching. The post Critical FortiClient EMS Vulnerability Exploited in Fresh Attacks appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** An improper access control (CWE‑284) in FortiClient EMS allows unauthenticated attackers to send specially crafted requests to execute unauthorized commands or code on affected EMS versions.
- **Affected Products:** FortiClient EMS 7.4.5, 7.4.6
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — https://fortiguard.fortinet.com/psirt/FG-IR-26-099
- **Active Exploitation:** true — https://www.securityweek.com/critical-forticlient-ems-vulnerability-exploited-in-fresh-attacks/
- **Threat Actors:** None known
- **Mitigation:** Apply Fortinet’s out‑of‑band hotfix for EMS 7.4.5/7.4.6 or upgrade to FortiClient EMS 7.4.7 when available; restrict network access to EMS interfaces and follow vendor hardening guidance.
- **Vendor Advisory:** https://fortiguard.fortinet.com/psirt/FG-IR-26-099

---

## 4. 🟠 Zero-Day — Download pumping: New npm deception technique for supply chain attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Tenable Security Research &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://www.tenable.com/blog/how-cyberattackers-inflate-malicious-package-npm-download-counts>

> Learn how attackers exploit automated bot traffic as part of software supply chain attacks to artificially inflate download counters and mask malicious payloads as legitimate. Key takeaways Volume doesn’t equal trust. Packages with numerous versions and high download counts might seem legitimate, but attackers can easily manipulate those metrics. Attackers exploit automated infrastructure. By init…

**Parallel AI Enrichment:**

- **Technical Details:** Attackers flood the npm registry with multiple benign package versions; automated tools and mirrors download each version, artificially inflating download metrics. The high download count is then used to disguise malicious code embedded in later versions, making the package appear trustworthy.
- **Affected Products:** npm (Node Package Manager) registry
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** false
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Deploy asset‑inventory tools (e.g., Tenable One, Nessus) to catalog npm packages in use and monitor download count anomalies. Correlate sudden spikes with version releases and investigate packages with unusually high download volume before adoption.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) abuses trusted inputs on the web (e.g., documentation, code comments, web pages) to inject instructions that influence AI agents' behavior, weaponizing agents' elevated access and ability to process untrusted content (attack vector known as 'Comment and Control').
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Treat untrusted web content as adversarial, harden agent runtimes, sandbox and restrict elevated access, implement prompt injection filters and content provenance checks.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack technique where adversarial instructions are embedded within data or tools consumed by an LLM (e.g., Workspace with Gemini), causing the model to follow malicious instructions even without direct user input. Attack discovery includes human and automated red‑teaming, VRP submissions, OSINT, and synthetic‑data generation to create variants.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses: enable deterministic controls (URL sanitization, user confirmation, tool chaining policies), apply Google’s configuration‑based policy engine for rapid point fixes (e.g., regex takedowns), keep ML/LLM defenses updated with synthetic‑attack training data, participate in VRP and red‑teaming, and validate defenses via simulated end‑to‑end attack testing across Workspace apps.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Primary threat is indirect prompt injection—malicious or user‑generated web content influencing an agent’s planning model to perform unwanted actions (e.g., financial transactions or data exfiltration). Chrome mitigates by separating planning and vetting via a high‑trust User Alignment Critic that sees only action metadata, enforcing origin gating (Agent Origin Sets) to limit readable and writable origins, requiring user confirmations for sensitive actions, and running a prompt‑injection classifier in parallel with the planner to block content intentionally targeting the model.
- **Affected Products:** Chrome agentic capabilities (Gemini in Chrome); specific affected versions unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** false
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Implemented layered defenses in Chrome: User Alignment Critic, Agent Origin Sets (read-only and read-writable), deterministic user confirmations for sensitive actions, real-time prompt‑injection classifier and Safe Browsing integrations, continuous red‑teaming and monitoring, and updated VRP guidance.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Near‑miss linear buffer overflow in unsafe Rust in CrabbyAVIF; Scudo's guard pages converted the overflow into a noisy crash and prevented exploitation; assigned CVE‑2025‑48530 and fixed pre‑release.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Scudo hardened allocator (guard pages) made the overflow non‑exploitable; additional hardening and unsafe‑Rust review/training recommended.
- **Vendor Advisory:** https://source.android.com/security/bulletin/2025-08-01

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injections are hidden malicious instructions embedded in external data sources such as emails, documents, or calendar invites that aim to cause the AI model to exfiltrate data or perform unauthorized actions. Google mitigates this by hardening the Gemini 2.5 model with adversarial training, deploying content classifiers to detect malicious instructions, adding security‑thought reinforcement prompts, sanitizing markdown (including blocking external images and redacting suspicious URLs via Google Safe Browsing), and requiring explicit user confirmation for risky operations.
- **Affected Products:** Gemini (Google Workspace), Gemini app
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — https://blog.google/security/mitigating-prompt-injection-attacks/
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Layered defenses including Gemini 2.5 model hardening with adversarial training, purpose‑built ML detectors for malicious instructions, security thought reinforcement, markdown sanitization with suspicious URL redaction (Google Safe Browsing), contextual user confirmation (Human‑In‑The‑Loop), end‑user mitigation notifications, red‑team testing, and Help Center guidance (https://support.google.com/docs/answer/16204578).
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state‑sponsored actors compromise backbone/PE/CE routers and other network devices, modify router firmware/configurations to maintain persistent, long‑term access, and pivot via trusted connections into government, telecom, transportation, lodging, and military networks to exfiltrate intelligence.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Isolate affected devices from untrusted networks; audit and rotate credentials and keys; apply vendor firmware updates and patches where available; remove unauthorized persistent router modifications; restrict management plane access (ACLs, MFA, dedicated out‑of‑band management); monitor for anomalous router configurations and traffic; implement network segmentation and zero‑trust principles; use integrity checks and backups of router configurations; follow CISA AA25-239A recommended detection and hardening guidance.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 12. 🟠 Zero-Day — Kimsuky Deploys HTTPSpy, Expands Arsenal with HelloDoor and VS Code Tunnels

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://thehackernews.com/2026/05/kimsuky-deploys-httpspy-expands-arsenal.html>

> The North Korean state-sponsored threat actor known as Kimsuky (aka Velvet Chollima) has been attributed to a fresh set of cyber attacks targeting South Korean military and corporate entities through March and April 2026.

&quot;Kimsuky employed a range of tailored social engineering tactics, such as spoofing security software installation pages and crafting a fake Webex meeting page that leverage…

---

## 13. 🟠 Zero-Day — Microsoft Slams Public Zero-Day Disclosures Amid GitHub Researcher Account Removal

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://thehackernews.com/2026/05/microsoft-slams-public-zero-day.html>

> Microsoft has come out strongly in favor of Coordinated Vulnerability Disclosure (CVD), urging the research community to share their findings and give affected vendors an opportunity to better understand the impact and address them before they are publicly disclosed.

The development comes after a researcher named Chaotic Eclipse (aka Nightmare-Eclipse) disclosed details of multiple zero-day

---

## 14. 🟡 High Severity — Dulwich has an arbitrary file write via NTFS-hostile tree entries on Windows

**CVE:** `CVE-2026-42305` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-897w-fcg9-f6xj>

> ## Impact

Arbitrary file write leading to remote code execution when cloning or checking out a malicious Git repository on Windows.

Dulwich&#x27;s path-element validator accepted tree entries whose filenames contained bytes that Windows interprets as structural path syntax:

  - \ — the Windows path separator. A single tree entry named .git\hooks\pre-commit.exe was treated as one valid filename …

---

## 15. 🟡 High Severity — nono: Sandbox escape on Linux via D-Bus: `systemd-run --user`

**CVE:** `CVE-2026-47128` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-27vp-2mmc-vmh3>

> ### Summary

The nono Landlock/seccomp policies allow access to local Unix domain sockets (concrete and abstract). This allows an easy sandbox escape by talking to the per-user systemd dbus socket.

Threat scenario: Running Aider, Claude Code, OpenCode or similar tools with &quot;allow bash&quot; policy so that it can invoke arbitrary host tools like `make`, `gcc`, etc. to write code.

### Reprodu…

---

## 16. 🟡 High Severity — local-deep-research has an SSRF bypass in `safe_get`

**CVE:** `CVE-2026-46526` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-g23j-2vwm-5c25>

> ### Summary
The URL checking logic in local-deep-research has a logical flaw that could be bypassed by attackers, leading to SSRF attacks.

### Details
The current project uses `validate_url` to validate the input URL. The main logic is to perform security checks on the host portion of the URL extracted by urlparse to prevent SSRF attacks.

&lt;img width=&quot;1173&quot; height=&quot;1107&quot; al…

---

## 17. 🟡 High Severity — compliance-trestle Vulnerable to Remote Code Execution via Recursive Server-Side Template Injection (SSTI)

**CVE:** `CVE-2026-46439` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-gg2g-p7xc-qqmm>

> A High severity Server-Side Template Injection (SSTI) vulnerability exists in the `trestle author jinja` command. The command recursively evaluates rendered templates, allowing an attacker to achieve arbitrary command execution with privileges of the running process by injecting malicious payloads into data fields (such as SSP documents or Lookup Tables).

**The vulnerability does not require atta…

---

## 18. 🟡 High Severity — compliance-trestle Vulnerable to SSRF in Remote Fetching Subsystem

**CVE:** `CVE-2026-46380` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-w76h-q7c6-jpjp>

> A source code audit led to the discovery of three significant security vulnerabilities in the trestle/core/remote/cache.py module.

**Finding 1 (Critical): SSRF (CWE-918)**
The HTTPSFetcher._do_fetch() method passes a user-supplied URL directly to requests.get() without validation. This allows an attacker to perform Server-Side Request Forgery, targeting internal services or cloud metadata endpoin…

---

## 19. 🟡 High Severity — OpenCTI: Privilege escalation via graphQL API is abusable by organization admins, due to incorrect ACL on userEdit relationAdd

**CVE:** `CVE-2026-44730` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-q537-qhj4-wcjx>

> ### Summary
An organization admin can escalate their privileges by adding a user from a different organization with higher privileges, to their own organization.

### Impact
Full platform access, access to sensitive or proprietary information.

---

## 20. 🟡 High Severity — OpenBao's cross-namespace lease revocation via legacy sys/revoke path bypasses ACL

**CVE:** `CVE-2026-45808` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-v8v8-cm84-m686>

> # Impact

OpenBao&#x27;s namespaces provide multi-tenant separation. A tenant who intentionally leaks lease identifiers can have their lease and underlying credential revoked or renewed by a user in another tenant via the legacy, undocumented `sys/revoke` and `sys/renew` endpoints.

# Patch

This will be addressed in v2.5.4.

---

## 21. 🟡 High Severity — Symfony's Mailtrap Mailer Webhook Parser Never Verifies the X-Mt-Signature HMAC — Unauthenticated Webhook Event Injection

**CVE:** `CVE-2026-45755` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-59f3-vp2f-mp9w>

> ### Description

The Mailtrap mailer bridge ships a webhook request parser used to authenticate and decode the event callbacks Mailtrap POSTs to an application&#x27;s webhook endpoint. Its `doParse(Request $request, #[\SensitiveParameter] string $secret)` method receives the configured webhook secret but never reads it; it decodes and returns the payload unconditionally, ignoring the `X-Mt-Signatu…

---

## 22. 🟡 High Severity — Symfony's Mailjet Mailer Webhook Parser Never Verifies the Configured Secret — Unauthenticated Webhook Event Injection

**CVE:** `CVE-2026-45754` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-64hg-93w9-fc35>

> ### Description

The Mailjet mailer bridge and the LOX24 SMS notifier bridge both ship webhook request parsers used to authenticate and decode the event callbacks each provider POSTs to an application&#x27;s webhook endpoint. Their `doParse(Request $request, #[\SensitiveParameter] string $secret)` methods receive the configured webhook secret but never read it; they convert and return the payload …

---

## 23. 🟡 High Severity — opentelemetry-go's Schema ParseFile leaks file descriptors on each parse

**CVE:** `CVE-2026-45287` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-995v-fvrw-c78m>

> ### Summary

`go.opentelemetry.io/otel/schema/v1.0` and `go.opentelemetry.io/otel/schema/v1.1` leaks one file descriptor on each successful `ParseFile` call. `ParseFile` opens the schema file and passes it to `Parse` without closing it; repeated parsing in a long-running process can exhaust the process file descriptor limit and cause denial of service. The severity is low because exploitation depe…

---

## 24. 🟡 High Severity — opentelemetry-go's baggage parsing no longer caps raw header length

**CVE:** `CVE-2026-41178` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-5wrp-cwcj-q835>

> ### Summary

https://github.com/open-telemetry/opentelemetry-go/pull/7880 removed raw-length rejection and it causes `Parse` to process arbitrarily large/invalid baggage headers and log errors, enabling DoS via oversized inputs.


### Details

The commit removes the upfront baggage-string length check and the per-member size guard in parsing. `Parse` now walks the entire input with `strings.SplitS…

---

## 25. 🟡 High Severity — Capsule TenantResource RawItems Cluster-Scoped Resource Creation Vulnerability

**CVE:** `CVE-2026-22872` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-qjjm-7j9w-pw72>

> # TenantResource RawItems Cluster-Scoped Resource Creation Vulnerability


## Summary

The Capsule Controller runs with cluster-admin privileges. Although the TenantResource RawItems processing logic forcibly sets the namespace, this is ineffective for cluster-scoped resources. Tenant administrators can leverage the Controller&#x27;s elevated privileges to create cluster-scoped resources (such as …

---

## 26. 🟡 High Severity — Capsule Namespace Hijacking via subresource

**CVE:** `CVE-2026-30963` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-2ww6-hf35-mfjm>

> ### Summary
To defend against namespace hijacking achieved through update/patch operations on namespaces, Capsule uses a webhook to validate update requests targeting namespaces. However, in Kubernetes, the namespace/finalize and namespace/status subresource APIs can also modify various fields of a namespace, including the metadata field. The webhook does not define interception rules for these su…

---

## 27. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
