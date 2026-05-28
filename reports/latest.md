# Zero Day Pulse

> **Generated:** 2026-05-28 20:04 UTC &nbsp;|&nbsp; **Total:** 34 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 22 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated remote attackers can exploit multiple path traversal vulnerabilities in SimpleHelp 5.5.7 and earlier to retrieve logs, configuration files, and credentials, potentially leading to full server compromise.
- **Affected Products:** SimpleHelp Remote Support / RMM 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (https://medium.com/@RosanaFS/simplehelp-cve-2024-57727-tryhackme-walkthrough-9f88c2061fb9)
- **Patch Available:** true (https://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570)
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (e.g., DragonForce ransomware operators)
- **Mitigation:** Upgrade to SimpleHelp 5.5.8 or later; if patching cannot be applied immediately, segment the SimpleHelp server, enforce IP allowlists/firewall rules to limit access, rotate credentials found in logs/config files, and monitor for indicators of compromise.
- **Vendor Advisory:** https://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570

---

## 2. 🟠 Zero-Day — New Gogs zero-day flaw lets hackers get remote code execution

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://www.bleepingcomputer.com/news/security/new-gogs-zero-day-flaw-lets-hackers-get-remote-code-execution/>

> An unpatched zero-day vulnerability in the Gogs self-hosted Git service can allow attackers to gain remote code execution (RCE) on Internet-facing instances. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Improper handling of symbolic links in Gogs repository file editing allows attackers to overwrite files outside the repository via symlink traversal, leading to remote code execution.
- **Affected Products:** Gogs (self-hosted Git service)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Block Internet‑facing Gogs instances; restrict access to trusted networks; remove or disable the repository file‑editing feature; monitor and restore from backups; apply vendor patch when available.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — Critical FortiClient EMS Vulnerability Exploited in Fresh Attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://www.securityweek.com/critical-forticlient-ems-vulnerability-exploited-in-fresh-attacks/>

> Fortinet rolled out hotfixes for the security defect in April, warning that it had been exploited in the wild as a zero-day and urging immediate patching. The post Critical FortiClient EMS Vulnerability Exploited in Fresh Attacks appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** An improper access control (CWE‑284) in the FortiClient EMS API permits unauthenticated attackers to send crafted requests that execute unauthorized commands or code via the EMS management pathway, enabling remote code execution.
- **Affected Products:** FortiClient EMS 7.4.5, FortiClient EMS 7.4.6
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply Fortinet hotfixes immediately or upgrade to 7.4.7+, follow Fortinet EMS release notes/hotfix installation instructions; disable or unexpose EMS management interfaces from untrusted networks; follow CISA KEV guidance per BOD 22-01.
- **Vendor Advisory:** https://fortiguard.fortinet.com/psirt/FG-IR-26-099

---

## 4. 🟠 Zero-Day — Download pumping: New npm deception technique for supply chain attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Tenable Security Research &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://www.tenable.com/blog/how-cyberattackers-inflate-malicious-package-npm-download-counts>

> Learn how attackers exploit automated bot traffic as part of software supply chain attacks to artificially inflate download counters and mask malicious payloads as legitimate. Key takeaways Volume doesn’t equal trust. Packages with numerous versions and high download counts might seem legitimate, but attackers can easily manipulate those metrics. Attackers exploit automated infrastructure. By init…

**Parallel AI Enrichment:**

- **Technical Details:** Attackers systematically publish a large number of versions of an npm package (hundreds), which triggers automated downloads by repository mirrors, analysis bots, and scanners for each new version — amplifying download counts (each version yields ~100‑150 automated downloads). After inflating trust metrics and release history with benign versions, a malicious version is published to deliver payloads (e.g., via postinstall scripts).
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — https://www.tenable.com/blog/how-cyberattackers-inflate-malicious-package-npm-download-counts
- **Patch Available:** false — Patch availability unknown.
- **Active Exploitation:** true — https://www.tenable.com/blog/how-cyberattackers-inflate-malicious-package-npm-download-counts
- **Threat Actors:** None known.
- **Mitigation:** Do not rely on download counts or version history as trust signals; adopt version pinning, enforce minimum package‑age restrictions (wait 3‑4 days before allowing new packages/versions), use security scanners and community feed to detect malicious packages, enforce least‑privilege and ephemeral CI/CD runners, restrict outbound network access from build servers, and use supply‑chain visibility tools (e.g., Tenable One, Nessus inventory plugins) to detect compromised packages.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an attack vector where adversaries place malicious or adversarial content on public web pages or other untrusted sources that AI agents ingest, causing the agent to follow attacker‑controlled instructions or reveal sensitive data. The mechanism exploits agent context windows and chaining of tools/abilities, leveraging elevated access to escalate impact.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — see vendor advisory: http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html
- **Active Exploitation:** true — Google Threat Intelligence observed indirect prompt injection attempts in the wild.
- **Threat Actors:** None known
- **Mitigation:** Harden agent runtimes: validate and sanitize external content, apply strict provenance and allowlisting, enforce least privilege for agent capabilities, instrument monitoring/auditing of agent actions, use system cards/runtime security reviews and detect anomalous instruction‑like inputs. See vendor advisory for recommended mitigations.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) enables an attacker to influence an LLM’s behavior by inserting malicious instructions into secondary data sources or tools the model uses when completing a user’s query (e.g., documents, web content, or tool outputs), potentially without any direct user input. IPI leverages the model’s reliance on external content and agentic automation to cause unintended actions or outputs.
- **Affected Products:** Google Workspace with Gemini integrations
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Layered defenses including continuous monitoring of external inputs, sanitization and provenance checks of data sources, restrict agentic tool access, apply least‑privilege controls for automated actions, user‑facing warnings/confirmations for sensitive operations, and ongoing model and workflow hardening as described by Google.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection can appear in malicious sites, iframes, or user‑generated content and cause the agentic browsing feature to perform unwanted actions such as financial transactions or data exfiltration. The attack works by injecting crafted prompts that steer the model’s planning module toward malicious behavior.
- **Affected Products:** Google Chrome (agentic browsing / Gemini in Chrome) — specific affected versions unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Use Chrome’s built‑in layered defenses (User Alignment Critic, Agent Origin Sets/origin gating, user confirmations for sensitive actions, prompt‑injection classifier, real‑time Safe Browsing), follow Google VRP guidance to report issues, and keep Chrome auto‑updates enabled.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true — https://blog.google/security/rust-in-android-move-fast-fix-things
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-11-01

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injections embed malicious instructions within external data sources (emails, documents, calendar invites) that downstream LLMs may follow. Google hardened Gemini 2.5 with adversarial training, content‑classifier models, markdown sanitization, suspicious‑URL redaction, user confirmation, and security‑thought reinforcement to detect and block such instructions.
- **Affected Products:** Gemini, Gemini in Google Workspace (Gmail)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Layered defenses – model hardening (adversarial training), prompt‑injection content classifiers, security thought reinforcement, markdown sanitization, suspicious‑URL redaction (using Google Safe Browsing), contextual user confirmations for risky actions, and end‑user security mitigation notifications with help‑center guidance.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors exploit known CVEs (e.g., CVE-2023-20198 authentication bypass, CVE-2018-0171 Smart Install RCE) and misconfigurations to gain initial access, modify ACLs, open ports, run commands in on‑box Linux containers, stage tools, create accounts, mirror traffic via SPAN/RSPAN/ERSPAN, and establish tunnels for exfiltration, often using publicly available scripting tools.
- **Affected Products:** Cisco IOS, Cisco IOS XE, Cisco NX-OS, Ivanti Connect Secure/Policy, Fortinet (potential), Juniper (potential), Nokia (potential), Sierra Wireless (potential)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching the referenced CVEs; disable unused ports and protocols; enforce strong credentials and public‑key authentication; monitor logs and configuration changes (ACLs, tunnels, unexpected containers); verify firmware/image integrity; follow vendor hardening guides (e.g., Cisco IOS/XE hardening, Cisco Software Checker).
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

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

## 25. 🟡 High Severity — FUXA's Unauthenticated Project Data Disclosure Exposes Server-Side Scripts and Device Configurations

**CVE:** `CVE-2026-47717` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-q3w6-q3hc-c5x6>

> ### Summary

The GET /api/project endpoint exposes sensitive project configuration data to guest-context requests even when secureEnabled is enabled.

### Details

File: `server/api/projects/index.js`

```javascript
prjApp.get(&quot;/api/project&quot;, secureFnc, function(req, res) {
    const permission = checkGroupsFnc(req);
    runtime.project.getProject(req.userId, permission).then(result =&gt…

---

## 26. 🟡 High Severity — Yamcs Vulnerable to Authenticated Remote Code Execution (RCE) via Jython Algorithm Code Injection

**CVE:** `CVE-2026-46621` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-2g95-6x5q-xjwj>

> ### Summary
A Server-Side Code Injection vulnerability exists in the Yamcs script evaluation engine for Python algorithms. The application dynamically compiles and evaluates user-controlled algorithm text using Jython (via the JSR-223 ScriptEngine API) without enforcing a secure sandbox. An authenticated user with the `ChangeMissionDatabase` privilege can exploit this by overriding the algorithm l…

---

## 27. 🟡 High Severity — Yamcs Vulnerable to Remote Code Execution via Mission Database algorithm override

**CVE:** `CVE-2026-46562` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-vmwp-vh32-rj75>

> # Remote Code Execution via Mission Database algorithm override

## Summary

The Nashorn `ScriptEngine` used to evaluate user-supplied algorithm text in `MdbOverrideApi.updateAlgorithm` is constructed without a `ClassFilter`, allowing a user with the `ChangeMissionDatabase` privilege to execute arbitrary Java code on the Yamcs server. In Yamcs&#x27;s default configuration (no `security.yaml`), the…

---

## 28. 🟡 High Severity — Pimcore has a CustomReports Share Bypass

**CVE:** `CVE-2026-45704` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-jwcc-gv4m-93x6>

> ### Summary

`CustomReports` uses inconsistent authorization between the report listing endpoint and the report detail endpoint.

- The listing flow filters reports based on report-sharing rules
- The detail flow only checks generic `reports` or `reports_config` permissions

As a result, a low-privileged backend user who was not granted access to a report can still read that report directly by nam…

---

## 29. 🟡 High Severity — AsyncSSH `AuthorizedKeysFile %u` path traversal allows attacker-selected authorized keys to authenticate a traversal username

**CVE:** `CVE-2026-45309` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-g794-3fmp-753h>

> ## Summary
AsyncSSH 2.22.0 expands the OpenSSH-compatible `AuthorizedKeysFile` `%u` token with the raw SSH username during pre-authentication server config reload. A server configured with a documented per-user key pattern such as `AuthorizedKeysFile authorized_keys/%u` can be made to read an authorized-keys file outside the intended directory when the SSH username contains path traversal segments…

---

## 30. 🟡 High Severity — Symfony hardened the parser when handling untrusted input

**CVE:** `CVE-2026-45133` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-c2p3-7m5p-cv8x>

> ### Description

`Symfony\Component\Yaml\Parser` is the entry point for parsing YAML strings into PHP values via `Yaml::parse()`. When the parser is exposed to attacker-controlled input, deeply nested mappings or sequences cause both the block-level (`Parser::parseBlock()`) and inline (`Inline::parseSequence()` / `Inline::parseMapping()`) parsers to recurse without a depth limit. A crafted documen…

---

## 31. 🟡 High Severity — Automad has Broken Access Control: Unauthenticated exposure of administrator bcrypt password hashes and TOTP secrets via public API endpoint

**CVE:** `CVE-2026-45332` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-xm76-r88j-vm3g>

> ### Summary

 A Broken Access Control vulnerability allows an unauthenticated attacker to retrieve the bcrypt password hash of every administrator account with a single POST request. The `/_api/user-collection/create-first-user` setup endpoint remains publicly accessible once initial configuration is complete and returns full serialized user data in the JSON response body.  

### Details

Affected…

---

## 32. 🟡 High Severity — Symfony has Unauthenticated PHP Object Deserialization in MonologBridge server:log Listener

**CVE:** `CVE-2026-45077` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-m7v2-7gxm-vc2v>

> ### Description

`Symfony\Bridge\Monolog\Command\ServerLogCommand` (the `server:log` console command) is a development-time helper that opens a TCP listener and displays log records pushed to it by the application&#x27;s logging pipeline. Two unsafe defaults combine into a remotely reachable PHP object-deserialization sink:

1. The listener binds to `0.0.0.0:9911` by default; it accepts connection…

---

## 33. 🟡 High Severity — Symfony has Email Header / SMTP Command Injection via CRLF in Symfony\Component\Mime\Address

**CVE:** `CVE-2026-45067` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-27
**Reference:** <https://github.com/advisories/GHSA-qpmx-3rfj-7rhv>

> ### Description

`Symfony\Component\Mime\Address` is the value-object every Symfony Mailer address (to/cc/bcc/from/reply-to) flows through; its constructor is documented as validating the address and throwing on invalid input, so developers treat it as a security boundary.

The constructor accepts email addresses whose local-part (the part before `@`) is an RFC-5322 *quoted string* containing raw …

---

## 34. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
