# Zero Day Pulse

> **Generated:** 2026-05-29 20:07 UTC &nbsp;|&nbsp; **Total:** 35 &nbsp;|&nbsp; 🔴 KEV: 1 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 20 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🔴 CISA KEV — CVE-2026-0257 — Palo Alto Networks PAN-OS Authentication Bypass Vulnerability

**CVE:** `CVE-2026-0257` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-0257>

> Vendor: Palo Alto Networks | Product: PAN-OS. Palo Alto Networks PAN-OS contains an authentication bypass vulnerability that allows attackers to bypass security restrictions and establish an unauthorized VPN connection. Required action: Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailabl…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is an authentication bypass in the GlobalProtect portal and gateway that allows an unauthenticated remote attacker to bypass authentication and establish an unauthorized VPN connection, potentially leading to high‑impact confidentiality and integrity breaches.
- **Affected Products:** PAN-OS 12.1 < 12.1.4-h6, PAN-OS 12.1.5‑12.1.6, PAN-OS 11.2 < 11.2.11, PAN-OS 10.2 versions, Prisma Access versions
- **CVSS Score:** 4.7
- **CVSS Vector:** CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:L/VI:N/VA:N/SC:H/SI:H/SA:N/E:U/AU:N/R:A/V:D/RE:M/U:Amber
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor‑provided upgrades to the fixed PAN‑OS/Prisma Access builds. If patching cannot be done immediately, restrict GlobalProtect portal and gateway access to trusted zones, disable User‑ID Authentication Portal if not required, and follow BOD 22‑01 guidance for cloud services per CISA KEV guidance.
- **Vendor Advisory:** https://security.paloaltonetworks.com/CVE-2026-0257

---

## 2. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Multiple unauthenticated path traversal vulnerabilities in SimpleHelp 5.5.7 and earlier allow an attacker to retrieve logs, configuration files, and credentials, and to log in with high‑privilege accounts.
- **Affected Products:** SimpleHelp remote support/RMM v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** DragonForce ransomware group
- **Mitigation:** Upgrade to SimpleHelp v5.5.8, block internet access to the management console, restrict access via firewall or VPN, rotate all credentials, and monitor logs for indicators of compromise.
- **Vendor Advisory:** http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 3. 🟠 Zero-Day — vm2 has a CVE-2023-37903 patch bypass: nesting:true without explicit require still allows full RCE

**CVE:** `CVE-2026-47137` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-m4wx-m65x-ghrr>

> ## Summary

The fix for GHSA-8hg8-63c5-gwmx (CVE-2023-37903) introduced a check in `nodevm.js` line 263 that blocks the combination `nesting: true` + `require: false`. However, the check uses strict equality (`options.require === false`), which is trivially bypassed by omitting the `require` option entirely.

When `require` is not specified, `options.require` is `undefined`, not `false`. The stric…

**Parallel AI Enrichment:**

- **Technical Details:** A check added to nodevm.js uses strict equality (options.require === false) to block nesting:true + require:false, but omitting the require option leaves options.require undefined, bypassing the guard. Destructuring later defaults require to false, enabling the insecure combination and full RCE via nested NodeVM requiring vm2.
- **Affected Products:** vm2 (nodejs sandbox)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true (https://github.com/advisories/GHSA-m4wx-m65x-ghrr; https://github.com/patriksimek/vm2/security/advisories/GHSA-8hg8-63c5-gwmx)
- **Patch Available:** true (https://github.com/advisories/GHSA-m4wx-m65x-ghrr)
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Ensure require is explicitly set to false when creating NodeVMs (do not rely on omission), upgrade to patched vm2 release referenced in the vendor advisory, or avoid using vm2 nesting:true until patched.
- **Vendor Advisory:** https://github.com/advisories/GHSA-m4wx-m65x-ghrr

---

## 4. 🟠 Zero-Day — Gogs Zero-Day Exposes Servers to Remote Code Execution

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://www.securityweek.com/gogs-zero-day-exposes-servers-to-remote-code-execution/>

> The critical-severity issue, assigned a CVSS score of 9.4, is an argument injection flaw that can be exploited by authenticated attackers via pull requests with malicious branch names. The post Gogs Zero-Day Exposes Servers to Remote Code Execution appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Authenticated attackers can craft pull‑request branch names that inject arguments into Gogs' internal commands. The injected arguments create symlinks or path traversals, enabling file overwrite outside the repository and resulting in remote code execution.
- **Affected Products:** Gogs
- **CVSS Score:** 9.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (https://github.com/zAbuQasem/gogs-CVE-2025-8110)
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Restrict write access to trusted users, enforce strict validation of branch names in pull requests, disable automatic execution of repository hooks, apply network segmentation, and monitor logs for unexpected file writes.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) involves adversarial instructions hidden within benign web content (e.g., comments, hidden code, or payloads on websites) that AI agents or code assistants may ingest when browsing or using web content; the attack leverages the agent’s tendency to follow contextual instructions, causing data exfiltration, API key theft, destructive commands, or fraudulent actions when the model executes or synthesizes code or actions based on the injected prompts.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Harden agent input handling by restricting web-browsing/data-sourcing to trusted domains, sanitize and filter untrusted web content, apply prompt sandboxing and instruction-override defenses, enforce least privilege for any code-execution interfaces (limit network and credential access), enable content provenance/trust signals, and apply vendor‑recommended mitigations in official advisories.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack technique where adversaries inject malicious instructions into data or tools consumed by an LLM‑based system (e.g., content in documents, web pages, or integrated tools). The model may execute or follow those instructions while completing user queries, potentially without direct user input. IPI is an evolving threat against complex AI applications with multiple data sources and agentic automation.
- **Affected Products:** Google Workspace (including Workspace apps integrating Gemini); Gemini
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** true — http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html
- **Active Exploitation:** true — http://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads; http://recordedfuture.com/research/emerging-enterprise-security-risks-of-ai
- **Threat Actors:** None known
- **Mitigation:** Apply Google Workspace mitigations and layered defenses per advisory (data‑source validation, tool access restrictions, content sanitization, model prompt hardening, monitoring/telemetry, user education, contextual policy enforcement). Follow vendor guidance in the advisory.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) allows malicious or adversarial web content, third‑party content (e.g., iframes), or user‑generated content to influence an agentic model’s planner to take unwanted actions such as financial transactions or data exfiltration. Chrome mitigates this via a User Alignment Critic, Origin Sets, deterministic URL checks, parallel prompt‑injection classifiers, and user confirmations for sensitive actions.
- **Affected Products:** Chrome (agentic/Gemini-enabled browsing features)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Enable Chrome’s auto‑updates; rely on Origin Sets and user confirmations; ensure agents run with read‑only origins and require explicit user interaction for sensitive steps; follow Google VRP reporting rules; use the built‑in prompt‑injection classifier and User Alignment Critic as described in the advisory.
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
- **Exploit Available:** false
- **Patch Available:** true — https://source.android.com/docs/security/bulletin/2025-11-01
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection embeds malicious instructions in external data sources (emails, files, calendar invites) so an LLM acting on those sources executes adversarial instructions or exfiltrates data; attacks depend on prompting lifecycle weaknesses and unpredictable external content handling.
- **Affected Products:** Gemini (including Gemini in Google Workspace), Gemini app, Gmail, Docs, Calendar integrations
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Layered defenses — model hardening (Gemini 2.5 adversarial training), prompt‑injection content classifiers, security thought reinforcement, markdown sanitization and suspicious‑URL redaction, user confirmation (Human‑In‑The‑Loop) framework, end‑user security notifications, plus red‑team testing and ongoing monitoring.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors exploit publicly known CVEs (not zero‑days) to gain access to edge/backbone routers and pivot via trusted connections; they modify ACLs, open ports, create accounts, enable HTTP/HTTPS services, run containers (Guest Shell) to execute scripts (e.g., TCL/Python), capture traffic via SPAN/RSPAN/ERSPAN, alter routing (BGP), and collect configuration and subscriber data for long‑term persistence and espionage.
- **Affected Products:** Cisco IOS, Cisco IOS XE, Cisco NX-OS, Ivanti Connect Secure/Policy, Fortinet, Juniper, Nokia, Sierra Wireless, SonicWall
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon (and reporting aliases OPERATOR PANDA, RedMike, UNC5807, GhostEmperor)
- **Mitigation:** Prioritize patching known exploited CVEs; monitor and verify firmware/software integrity (hash checks), review device logs/configs for unexpected ACLs, AAA changes, tunnels, packet captures, virtual containers; disable unused ports/protocols; enforce strong credentials and public‑key auth; Cisco‑specific hardening (Guest Shell controls, IOS/XE hardening guides, Cisco Software Checker); follow CISA/NSA/FBI guidance.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 11. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 12. 🟠 Zero-Day — ChatGPhish Vulnerability Turns ChatGPT Web Summaries Into a Phishing Surface

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://thehackernews.com/2026/05/chatgphish-vulnerability-turns-chatgpt.html>

> Cybersecurity researchers have disclosed details of a vulnerability in OpenAI ChatGPT that leverages the artificial intelligence (AI) assistant&#x27;s implicit trust in Markdown links and images to trigger prompt injections and open the door to phishing attacks.

The technique has been codenamed ChatGPhish by Permiso Security.

&quot;The chatgpt.com response renderer trusts Markdown links and Mark…

---

## 13. 🟠 Zero-Day — Axios has a Patch Bypass: Proxy-Authorization Header Injection via Prototype Pollution — Incomplete Null-Prototype Fix

**CVE:** `CVE-2026-44489` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-654m-c8p4-x5fp>

> # [Patch Bypass] Proxy-Authorization Header Injection via Prototype Pollution — Incomplete Null-Prototype Fix in Axios 1.15.2

## Summary

The `Object.create(null)` fix introduced in Axios 1.15.2 (GHSA-q8qp-cvcw-x6jj) protects the **top-level config object** from prototype pollution. However, **nested objects** created by `utils.merge()` (e.g., `config.proxy`) are still constructed as plain `{}` w…

---

## 14. 🟠 Zero-Day — Microsoft calls zero-day releases ‘never justifiable’ as researcher threatens to drop more

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Record by Recorded Future &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more>

> Each vulnerability was published with working proof-of-concept code to the Microsoft-owned code repository GitHub, making them immediately available to both attackers and security professionals.

---

## 15. 🟠 Zero-Day — Kimsuky Deploys HTTPSpy, Expands Arsenal with HelloDoor and VS Code Tunnels

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://thehackernews.com/2026/05/kimsuky-deploys-httpspy-expands-arsenal.html>

> The North Korean state-sponsored threat actor known as Kimsuky (aka Velvet Chollima) has been attributed to a fresh set of cyber attacks targeting South Korean military and corporate entities through March and April 2026.

&quot;Kimsuky employed a range of tailored social engineering tactics, such as spoofing security software installation pages and crafting a fake Webex meeting page that leverage…

---

## 16. 🟡 High Severity — Koel Vulnerable to SSRF via Podcast Episode Enclosure URLs

**CVE:** `CVE-2026-47260` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-7j2f-6h2r-6cqc>

> ## Summary

Koel validates the podcast feed URL via the `SafeUrl` rule (DNS resolution + public IP check), but the individual episode `&lt;enclosure url=&quot;...&quot;&gt;` values extracted from the RSS XML are stored directly into the database without any SSRF validation. When a user plays an episode, the server downloads the full HTTP response from the unvalidated enclosure URL via `Http::sink(…

---

## 17. 🟡 High Severity — Sparkle's AppInstaller post-stage-1 XPC listener accepts unvalidated connections, allowing spoofed appcast item data injection

**CVE:** `CVE-2026-47122` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-g3hp-f6mg-559v>

> ## Summary

AppInstaller post-stage-1 XPC listener accepts unvalidated connections, allowing spoofed appcast item data injection.

## Details

`Autoupdate/AppInstaller.m`&#x27;s `shouldAcceptNewConnection:` only enforces `SUCodeSigningVerifier validateConnection:` before stage 1 completes. After `_performedStage1Installation = YES`, new connections to the registered Mach service `&lt;bundleId&gt;-…

---

## 18. 🟡 High Severity — russh server userauth state is not reset when authentication principal changes

**CVE:** `CVE-2026-46705` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-hpv4-5h6f-wqr3>

> ### Summary
The `russh` server authentication path keeps internal userauth state across `SSH_MSG_USERAUTH_REQUEST` messages without separating that state when the request principal changes.

RFC 4252 allows the `user name` and `service name` fields to change between authentication requests. The issue is not that such changes are invalid. The issue is that russh-owned authentication state, such as …

---

## 19. 🟡 High Severity — Metasploit Wrap Up 05/29/2026

**CVE:** `CVE-2026-43284` | `CVE-2026-43500` | `CVE-2026-3055` | `CVE-2022-28368` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-05-29-2026>

> More Linux LPEs Hark the age of the Linux LPE has arrived. This week’s release follows up on recent work bringing new Linux LPEs to Metasploit users. Copy Fail seemed to have kicked off a trend of similar bugs and hot on its heels is Dirty Frag. Dirty Frag is actually two vulnerabilities in a trenchcoat, individually identified as CVE-2026-43284 and CVE-2026-43500. Each is exploitable individually…

---

## 20. 🟡 High Severity — amazon-redshift-python-driver vulnerable to Remote Code Execution via eval() Injection

**CVE:** `CVE-2026-8838` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-29h4-r29x-hchv>

> ### Summary
amazon-redshift-python-driver is the official Python connector for Amazon Redshift. In versions 2.1.13 and earlier, the driver insufficiently validates data received from the server during query result processing. A rogue server or man-in-the-middle could leverage this to execute arbitrary code on the client.

### Impact
When a client connects to a rogue server implementing the Postgre…

---

## 21. 🟡 High Severity — AgenticMail API/storage and outbound relay hardening fixes

**CVE:** `CVE-2026-47255` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-wjjv-3mj2-39hf>

> The current upstream main branch at commit 7e0206d was reviewed, and the fix-first patch set was rebased on 2026-05-18. The patches cover: validated and bound inactive-agent hour filtering; storage SQL identifier validation; metadata-backed ownership checks for raw storage SQL; blocking direct storage metadata access through raw SQL; fail-closed outbound worker secret handling; SMTP envelope/heade…

---

## 22. 🟡 High Severity — unbounded-spsc: Sender::send pointer-as-value transmute causes OOB read and fake-Arc drop under TX/RX race

**CVE:** `CVE-2026-46690` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-6m57-8r3p-pqx6>

> ## Summary

`Sender::send` in `src/lib.rs` contains an `unsafe` block in the `DISCONNECTED` arm that transmutes a **raw pointer** (`*mut Producer&lt;T&gt;`) into the bytes of a **value-level** `Consumer&lt;T&gt;`. The author&#x27;s intent, visible in the surrounding comment at lines 386-390, was a value transmute. The shipped code is one level of indirection off.

The resulting `Consumer&lt;T&gt;`…

---

## 23. 🟡 High Severity — IPAM controller service account granted unnecessary full access to Secrets

**CVE:** `CVE-2026-47190` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-49pm-43hf-6xfq>

> ### Impact

IPAM is the IP address Manager for Cluster API Provider Metal3. The IPAM controller&#x27;s ClusterRole granted full CRUD permissions (create, delete, get, list, patch, update, watch) on core/v1 Secrets. The controller never accesses Secrets during normal operation. If the controller pod were compromised (e.g. via supply chain attack or container escape), an attacker could leverage thes…

---

## 24. 🟡 High Severity — NodeVM observability builtins leak host process and HTTP request data

**CVE:** `CVE-2026-47141` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-9g8x-92q2-p28f>

> ## Summary

`NodeVM` exposes some process-wide observability builtins when they are allowed through `require.builtin`.

The following builtins are not blocked by the dangerous builtin denylist:

```text
diagnostics_channel
async_hooks
perf_hooks
```

These modules are process-wide, not sandbox-local. Sandboxed code can use them to observe host application data across the vm2 boundary.

**Note**: I…

---

## 25. 🟡 High Severity — NodeVM network builtin exclusions bypass via internal _http_client and _http_server

**CVE:** `CVE-2026-47139` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-r9pm-gxmw-wv6p>

> ## Summary

`NodeVM` supports excluding public network builtins from the wildcard builtin option. With this configuration direct access to `http`, `https`, `http2`, `net`, `dgram`, `tls`, `dns`, and `dns/promises` is blocked.

However, Node.js also exposes underscored internal HTTP builtins such as `_http_client` and `_http_server`. These are not blocked when the public modules are excluded.

Sand…

---

## 26. 🟡 High Severity — vm2 sandbox escape via JSPI-backed Promise `.finally()` species bypass

**CVE:** `CVE-2026-47210` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-6j2x-vhqr-qr7q>

> ### Summary
A sandbox escape vulnerability in `vm2` allows arbitrary code execution in the host process when untrusted code is executed with async support on runtimes exposing WebAssembly JSPI (`WebAssembly.promising` / `WebAssembly.Suspending`). In the tested configuration, a JSPI-backed Promise can reach `Promise.prototype.finally()` in a way that bypasses the expected Promise-species hardening …

---

## 27. 🟡 High Severity — vm2 is Vulnerable to Sandbox Breakout Through Promise Species

**CVE:** `CVE-2026-47208` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-76w7-j9cq-rx2j>

> ### Summary

VM2 suffers from a sandbox breakout vulnerability. This allows attackers to write code which can escape from the VM2 sandbox and execute arbitrary commands on the host system.

### Details

The `localPromise` constructor was changed to call `this.then(undefined, eater)` to ensure a rejected promise is always used. However, this is missing a call to `resetPromiseSpecies` to ensure that…

---

## 28. 🟡 High Severity — Gotenberg has an SSRF deny-list bypass in IsPublicIP via IPv6 6to4 / NAT64 / site-local prefixes

**CVE:** `CVE-2026-45741` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-86m8-88fq-xfxp>

> ### Summary

`IsPublicIP` in `pkg/gotenberg/outbound.go` incorrectly classifies IPv6 6to4 / NAT64 / deprecated site-local addresses as public IPs, allowing an unauthenticated attacker to reach internal destinations (e.g., cloud metadata services at `169.254.169.254`) via a single crafted DNS AAAA record. This is a variant of CVE-2026-44430 (modelcontextprotocol/registry).

### Details

`IsPublicIP…

---

## 29. 🟡 High Severity — Rapid7 Observed Exploitation of PAN-OS GlobalProtect Authentication Bypass Vulnerability (CVE-2026-0257)

**CVE:** `CVE-2026-0257` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://www.rapid7.com/blog/post/etr-rapid7-observed-exploitation-of-pan-os-globalprotect-authentication-bypass-vulnerability-cve-2026-0257>

> Overview On May 13, 2026, Palo Alto Networks published a security advisory for CVE-2026-0257, a medium severity authentication bypass affecting PAN-OS and Prisma Access when a specific configuration is present. Successful exploitation of this vulnerability allows a remote unauthenticated attacker to successfully establish a VPN connection through the GlobalProtect gateway of an affected appliance.…

---

## 30. 🟡 High Severity — axios Vulnerable to Credential Theft and Response Hijacking via Prototype Pollution Gadget in Config Merge

**CVE:** `CVE-2026-44495` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-3g43-6gmg-66jw>

> ## Summary

Axios versions before the fixed releases contain prototype-pollution gadgets in request config processing. If another vulnerability in the same JavaScript process has already polluted `Object.prototype.transformResponse`, affected Axios versions may treat that inherited value as request configuration or as an option validator.

Axios does not itself create the prototype pollution. Expl…

---

## 31. 🟡 High Severity — axios Vulnerable to Full Man-in-the-Middle via Prototype Pollution Gadget in `config.proxy`

**CVE:** `CVE-2026-44494` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-35jp-ww65-95wh>

> # Vulnerability Disclosure: Full Man-in-the-Middle via Prototype Pollution Gadget in `config.proxy`

## Summary

The Axios library is vulnerable to a Prototype Pollution &quot;Gadget&quot; attack that allows any `Object.prototype` pollution in the application&#x27;s dependency tree to be escalated into a **full Man-in-the-Middle (MITM) attack** — intercepting, reading, and modifying all HTTP traff…

---

## 32. 🟡 High Severity — Froxlor has privilege escalation in SSH key synchronization via symlinked `authorized_keys` path

**CVE:** `CVE-2026-41236` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-mq5v-pxpm-8jw2>

> ### Summary
Froxlor 2.3.6 contains a symlink-following flaw in the root-owned SSH key synchronization path used for customer FTP users. The provisioning code appends public keys to `~/.ssh/authorized_keys` under a customer-controlled home directory without verifying that the target path is not a symbolic link.

If an attacker controls a shell-enabled customer account and can modify files inside th…

---

## 33. 🟡 High Severity — GitHub CLI has an incorrect authorization header in API requests to TUF repository mirrors via `gh attestation`, `gh release verify`, and `gh release verify-asset` commands

**CVE:** `CVE-2026-48501` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-29
**Reference:** <https://github.com/advisories/GHSA-8xvp-7hj6-mcj9>

> ### Summary

GitHub CLI incorrectly includes an authorization header in API requests to TUF repository mirrors via `gh attestation`, `gh release verify`, and `gh release verify-asset` commands.

 **Affected users:**

  - Authenticated `github.com` users who previously ran `gh attestation` commands, `gh release verify`, or `gh release verify-asset`: the `github.com` token was included in requests t…

---

## 34. 🟡 High Severity — Dulwich has an arbitrary file write via NTFS-hostile tree entries on Windows

**CVE:** `CVE-2026-42305` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-28
**Reference:** <https://github.com/advisories/GHSA-897w-fcg9-f6xj>

> ## Impact

Arbitrary file write leading to remote code execution when cloning or checking out a malicious Git repository on Windows.

Dulwich&#x27;s path-element validator accepted tree entries whose filenames contained bytes that Windows interprets as structural path syntax:

  - \ — the Windows path separator. A single tree entry named .git\hooks\pre-commit.exe was treated as one valid filename …

---

## 35. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
