# Zero Day Pulse

> **Generated:** 2026-06-02 10:01 UTC &nbsp;|&nbsp; **Total:** 17 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 11 &nbsp;|&nbsp; 🟡 High: 6 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** An unauthenticated attacker can send specially crafted HTTP requests that traverse directories and download arbitrary files from the SimpleHelp server host, such as configuration files containing credentials. The flaw can be combined with CVE‑2024‑57728 (authenticated file upload) to achieve remote code execution.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) versions 5.5.0‑5.5.7
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** DragonForce ransomware group
- **Mitigation:** Apply the SimpleHelp patches (versions 5.5.8‑5.5.10) immediately. For unpatched systems, restrict network access to the SimpleHelp service, monitor inbound/outbound traffic for suspicious requests, and conduct threat‑hunting for evidence of compromise.
- **Vendor Advisory:** https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is a technique where an attacker injects malicious instructions or content into an indirect input channel (such as user‑generated data, system logs, or API responses) that later becomes part of the prompt given to an LLM, causing the model to produce harmful or unintended outputs.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) enables an attacker to influence the behavior of a large language model by inserting malicious instructions into the data sources or auxiliary tools the model accesses, causing the model to execute those instructions when responding to a user's query, even without direct user input.
- **Affected Products:** Google Workspace (Gemini integration)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Google employs a layered defense strategy that includes continuous monitoring of data inputs, sanitization of user‑generated content, strict access controls for tools used by Gemini, and regular security updates to the Workspace environment.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection enables malicious web or third‑party content (including iframes or user‑generated content) to influence an agent’s planning model to perform unwanted actions (e.g., transactions or data exfiltration). Chrome’s defenses include a user alignment critic that vets actions, origin‑based read‑only/read‑writable gating, deterministic checks on model‑generated URLs, a real‑time prompt‑injection classifier, and required user confirmations for sensitive actions.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** true
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Use Chrome’s layered defenses: User Alignment Critic, Agent Origin Sets (read‑only and read‑writable gating), user confirmations for sensitive actions, real‑time indirect‑prompt‑injection detection, and keep Chrome auto‑update enabled. Refer to vendor advisory for configuration and VRP rules.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Android’s 2025 data shows a reduction in memory‑safety vulnerabilities after adopting Rust; the primary mechanism is prevention of memory‑safety bugs (use‑after‑free, buffer overflows, etc.) by writing new components in Rust and replacing risky C/C++ code, reducing vulnerability density and preventing classes of memory‑corruption exploits.
- **Affected Products:** Android platform (first‑party and third‑party/open‑source components across C, C++, Java, Kotlin, and Rust)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Continue migrating new and high‑risk components to memory‑safe languages (Rust), apply standard hardening (address sanitizer, fuzzing, review), and backport fixes for legacy C/C++ code; adopt least privilege and sandboxing for components handling untrusted input.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack vector where hidden or malicious instructions are embedded within external data sources (emails, documents, calendar invites, web content) consumed by generative AI systems; models may follow these instructions and exfiltrate data or perform unauthorized actions when prompts are contaminated or model context is untrusted.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false.
- **Patch Available:** false.
- **Active Exploitation:** true.
- **Threat Actors:** None known.
- **Mitigation:** Implement layered defenses including input provenance and integrity checks, model grounding and instruction sanitization, content filtering and red‑teaming, least‑privilege data access, output filtering/inspection, user prompts that limit tool access, and continuous monitoring and detection.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Initial access is achieved by exploiting publicly known CVEs (e.g., CVE‑2023‑20198, CVE‑2018‑0171, CVE‑2023‑20273, CVE‑2024‑21887). Persistence is established by enabling HTTP/HTTPS servers on Cisco devices and executing commands to maintain long‑term access.
- **Affected Products:** Cisco IOS XE, Cisco IOS, Ivanti
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a)
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching, apply Cisco hardening guidance, monitor firmware and software integrity, disable unused ports/protocols, change default credentials, require public‑key authentication, use vendor‑recommended OS versions, upgrade unsupported devices.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS) – also known as APT28 (Unit 26165).
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟠 Zero-Day — Race Against Time: Why Faster Vulnerability Alerts Matter

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://www.bleepingcomputer.com/news/security/race-against-time-why-faster-vulnerability-alerts-matter/>

> Attackers are exploiting vulnerabilities faster than many organizations can identify and patch them. SecAlerts explains why faster vulnerability alerts can help reduce exposure and improve response times. [...]

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

## 10. 🟠 Zero-Day — ⚡ Weekly Recap: New Linux Flaw, PAN-OS Exploit, AI-Powered Attacks, OAuth Phishing and More

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://thehackernews.com/2026/06/weekly-recap-new-linux-flaw-pan-os.html>

> Monday hit like a cron job with anger issues.

A busted auth path here, a repo-side faceplant there, some &quot;patched-ish&quot; thing already getting chewed on in the wild, and then the usual bonus round: poisoned dev tools, sketchy forum chatter, phishing kits pretending to be productivity, and AI lowering the bar for people who already thought &#x27;curl | sh&#x27; had a personality.

The vibe…

**Parallel AI Enrichment:**

- **Technical Details:** Local privilege escalation via fragmentation‑handling bugs in kernel networking/XFRM/ESP and rxrpc modules, enabling an unprivileged user to corrupt kernel memory and obtain root.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true https://github.com/v4bel/dirtyfrag
- **Patch Available:** true https://access.redhat.com/errata/RHSA-2026%3A16206
- **Active Exploitation:** true https://theregister.com/security/2026/05/08/dirty-frag-linux-flaw-one-ups-copyfail-with-no-patches-and-public-root-exploit/5237230
- **Threat Actors:** None known
- **Mitigation:** Apply vendor/kernel patches or live‑patches immediately; restrict local access; disable affected modules (esp, ipcomp, rxrpc, XFRM) where feasible; monitor for suspicious local activity.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟠 Zero-Day — Microsoft says it will not pursue security researchers after zero-day backlash

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Record by Recorded Future &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://therecord.media/microsoft-says-it-will-not-pursue-security-researchers-disclosure>

> Microsoft said it is taking the feedback seriously, adding: “To be clear about our approach to legal matters, we have no intention to pursue action against individuals conducting or publishing their security research.”

---

## 12. 🟡 High Severity — Critical Windows Netlogon Vulnerability in Attackers’ Crosshairs

**CVE:** `CVE-2026-41089` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://www.securityweek.com/critical-windows-netlogon-vulnerability-in-attackers-crosshairs/>

> Organizations are advised to patch CVE-2026-41089 as soon as possible, given its severity, the potential ongoing exploitation. The post Critical Windows Netlogon Vulnerability in Attackers’ Crosshairs appeared first on SecurityWeek .

---

## 13. 🟡 High Severity — praisonai-platform: Any workspace member can add arbitrary user as owner via POST /workspaces/{id}/members

**CVE:** `CVE-2026-47413` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://github.com/advisories/GHSA-8g2p-pqm3-fcfh>

> ## Summary

**Type:** Privilege escalation / cross-tenant member injection. The `POST /workspaces/{workspace_id}/members` endpoint is gated only by `require_workspace_member(workspace_id)` (default `min_role=&quot;member&quot;`) and forwards the request body&#x27;s `user_id` and `role` straight into `MemberService.add(workspace_id, user_id, role)`, which has no caller-permission check. A user with…

---

## 14. 🟡 High Severity — Nezha's authenticated agents can forge service-monitor results for other users' services

**CVE:** `CVE-2026-48119` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://github.com/advisories/GHSA-4g6j-g789-rghm>

> #### Summary

Nezha accepts service-monitor `TaskResult` messages from an authenticated agent based only on whether the reported service ID exists. The dashboard authenticates the agent and derives the reporter server ID from the gRPC stream, but the service-monitor result worker does not verify that the reporter server was selected for that service, belongs to the service owner, or was actually a…

---

## 15. 🟡 High Severity — CVE-2026-0826: How an Old Bug Can Feed AI-Powered Impersonation

**CVE:** `CVE-2026-0826` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://www.rapid7.com/blog/post/ve-cve-2026-0826-how-an-old-bug-can-feed-ai-powered-impersonation>

> One of the more persistent myths in security is that old bug classes become old problems. They don’t. They just show up in different places, under different conditions, and usually at the exact moment we’ve convinced ourselves not to pay attention to them. That’s part of what makes enterprise voice infrastructure so interesting. Earlier this year, we wrote about a critical vulnerability in Grandst…

---

## 16. 🟡 High Severity — Recent Palo Alto Networks Vulnerability Exploited for Weeks

**CVE:** `CVE-2026-0257` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://www.securityweek.com/recent-palo-alto-networks-vulnerability-exploited-for-weeks/>

> Hackers began exploiting CVE-2026-0257, an authentication bypass in Palo Alto Networks PAN-OS, four days after public disclosure. The post Recent Palo Alto Networks Vulnerability Exploited for Weeks appeared first on SecurityWeek .

---

## 17. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
