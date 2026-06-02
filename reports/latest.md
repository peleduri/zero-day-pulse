# Zero Day Pulse

> **Generated:** 2026-06-02 02:31 UTC &nbsp;|&nbsp; **Total:** 18 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 12 &nbsp;|&nbsp; 🟡 High: 6 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Multiple path traversal / directory traversal vulnerabilities in SimpleHelp 5.5.7 and earlier (including CVE-2024-57727) allowed unauthenticated remote attackers to read configuration files, logs, and credentials by traversing filesystem paths via crafted requests.
- **Affected Products:** SimpleHelp remote support / RMM – versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proofs-of-concept / weaponized exploits reported in incident analyses and scanning activity; no specific public PoC URL available.
- **Patch Available:** Yes – SimpleHelp released version 5.5.8 with fixes. Vendor advisory: https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know
- **Active Exploitation:** Confirmed – CISA advisory reports ransomware actors exploited unpatched SimpleHelp (AA25-163A).
- **Threat Actors:** Ransomware actors (unspecified groups); e.g., DragonForce referenced in reporting
- **Mitigation:** Update to SimpleHelp 5.5.8 or later; if immediate patching is impossible, isolate/unexpose SimpleHelp from untrusted networks, restrict access via firewall/VPN, rotate credentials, review logs, and apply network segmentation.
- **Vendor Advisory:** https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — Critical WP Maps Pro Flaw Actively Exploited to Create Admin Accounts

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://thehackernews.com/2026/06/critical-wp-maps-pro-flaw-actively.html>

> Threat actors are attempting to actively exploit a critical security flaw impacting WP Maps Pro, a WordPress plugin that has had over 15,000 sales on the Envato Market, to create malicious administrator accounts on susceptible sites.

WP Maps Pro allows site owners to embed customizable Google Maps and OpenStreetMap with markers, listings, and advanced location features on WordPress sites. It is

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated privilege escalation via the wpgmp_temp_access_ajax AJAX action registered for unauthenticated users (wp_ajax_nopriv_) protected only by a nonce that is exposed to the frontend via wp_localize_script; invoking the handler with check_temp=false creates an administrator user and returns a magic login URL that calls wp_set_auth_cookie() to authenticate the attacker.
- **Affected Products:** WP Maps Pro (wp-google-map-gold) — all versions ≤ 6.1.0; patched in 6.1.1
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** Public PoC available at https://github.com/xShadow-Here/CVE-2026-8732
- **Patch Available:** Yes — patched in version 6.1.1; patch details documented on Patchstack.
- **Active Exploitation:** Yes — active exploitation reported by Wordfence (blocking thousands of attempts) and covered by The Hacker News.
- **Threat Actors:** None known
- **Mitigation:** Update WP Maps Pro to version 6.1.1 or newer; apply Wordfence firewall rules (premium or free) to block exploitation attempts; restrict or temporarily disable the plugin until patched.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is a class of attacks where adversarial instructions are embedded in third‑party web content or payloads the AI agent ingests, causing the agent to alter behavior or reveal sensitive information. Researchers observed multiple real‑world payloads designed to manipulate agent prompts and outputs.
- **Affected Products:** AI agents and web‑facing AI assistants that ingest third‑party web content
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public weaponized exploit or PoC URL reported in the cited sources ("No public PoC reported").
- **Patch Available:** No official vendor patch reported. Vendor post does not list a patch; mitigation guidance provided in vendor blog.
- **Active Exploitation:** Yes — security researchers reported IPI payloads observed in the wild (reports describe 10 IPI payloads caught in the wild).
- **Threat Actors:** None known
- **Mitigation:** Apply input provenance and filtering; bound and validate external content before including in prompts; implement prompt sanitization and strict parsing rules; require explicit user confirmation for high‑risk actions; use allowlists and content provenance metadata.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack vector where an adversary inserts malicious instructions into data sources or tools that an LLM‑powered application consumes (e.g., documents, web content, or integrated apps). The LLM may execute or follow those instructions while completing a user’s query, even when the user provides no direct input. IPI leverages the model’s tendency to follow contextual instructions and the complexity of multi‑source agentic automation to influence model behavior.
- **Affected Products:** Google Workspace with Gemini integrations
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC or weaponized exploit specified in the advisory; exploit unavailable
- **Patch Available:** No single "patch"; vendor published mitigations and layered defenses at the advisory URL
- **Active Exploitation:** No confirmed active exploitation reported in the advisory; researchers have discovered IPI payloads in the wild (see Forcepoint reporting).
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses as described by vendor: content provenance controls, input/output filters, model instruction strictness, tool sandboxing, data‑source validation, continuous monitoring, and developer hardening guidance.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Insufficient policy enforcement in the WebView (Gemini panel) allowed extensions using declarativeNetRequest/basic permissions to inject JavaScript into the privileged Gemini Live panel (chrome://glic / gemini.google.com/app). Code executing in that panel could access camera/microphone, take screenshots, and read local files – effectively elevating privileges via the browser component. Attack vector: trick user into installing malicious extension which injects script into the Gemini panel to abuse privileged APIs.
- **Affected Products:** Google Chrome (versions < 143.0.7499.192)
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit disclosed; vulnerability was responsibly disclosed and patched (no known public PoC URLs).
- **Patch Available:** Yes — Google released a Chrome stable‑channel update in early January 2026 (fixed in 143.0.7499.192/.193). See Chrome release blog: https://chromereleases.googleblog.com/2026/01/stable-channel-update-for-desktop.html and the Google Security Blog advisory.
- **Active Exploitation:** No confirmed widespread active exploitation reported in the wild prior to patch; responsibly disclosed and patched (Unit42 and Google coordinated disclosure).
- **Threat Actors:** None known
- **Mitigation:** Update Chrome to the patched versions (>= 143.0.7499.192/.193). As hardening: restrict extension installation policies, limit declarativeNetRequest rules exposure, enable enterprise extension controls, use runtime protections (adblockers / URL filtering), and follow Google’s layered defenses for agentic browsing (origin sets, alignment critic, prompt‑injection classifiers).
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow in the Rust crate "crabbyavif" could have allowed out‑of‑bounds memory writes if the vulnerable code were executed.
- **Affected Products:** Android platform – Rust crate "crabbyavif" (specific version not disclosed)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit is known; the vulnerability never made it into a public release.
- **Patch Available:** Patch released at https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050
- **Active Exploitation:** No confirmed active exploitation in the wild has been reported.
- **Threat Actors:** None known
- **Mitigation:** Android’s Scudo hardened allocator placed guard pages around secondary allocations, deterministically rendering the overflow non‑exploitable.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) embeds hidden or adversarial instructions inside external data sources (emails, documents, calendar invites, web content, retrieved text) that AI agents or LLM‑based features may ingest during retrieval or context construction, causing the model to disclose sensitive data or perform unauthorized actions by following the injected instructions.
- **Affected Products:** Google Gemini, Gemini in Workspace, Google Workspace GenAI integrations
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public proof‑of‑concept or weaponized exploit disclosed; researchers have published examples of indirect prompt injection payloads observed in the wild.
- **Patch Available:** No single 'patch' — Google published layered defense guidance and Workspace/Gemini mitigations in its vendor advisory (see URL above).
- **Active Exploitation:** Researchers have reported 10 indirect prompt injection payloads observed in the wild (Forcepoint, Infosecurity) and analysis by multiple vendors; no confirmed wide‑scale active exploitation campaign attributed to specific threat actors.
- **Threat Actors:** None known
- **Mitigation:** Implement layered defenses: input/output sanitization and filtering of retrieved content, provenance and integrity checks, retrieval scope limitations, strict access controls and least privilege, explicit system- and user-level instruction separation, prompt constraints and instruction scrubbing, model hardening and monitoring, anomaly detection and logging; follow Google's advisory for configuration specifics.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors target large backbone routers and provider edge (PE) and customer edge (CE) routers, leverage compromised devices and trusted connections to pivot into other networks, and modify router configurations/firmware to maintain persistent, long-term access for espionage and lateral movement.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unavailable.
- **Patch Available:** Patch information unavailable.
- **Active Exploitation:** Confirmed active exploitation reported by CISA (AA25-239A) and allied advisories.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Restrict and harden router management interfaces (limit access to trusted IPs, use strong authentication and MFA), monitor and validate router configuration and firmware integrity, apply vendor updates/patches when available, segment networks and management planes, disable unused services/ports, implement network monitoring and anomaly detection for unusual routing/config changes, and rotate and protect credentials.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit or PoC is available.
- **Patch Available:** No official patch has been released for this advisory.
- **Active Exploitation:** Confirmed active exploitation has been reported by multiple agencies.
- **Threat Actors:** Russian GRU 85th GTsSS (Unit 26165), also known as APT28.
- **Mitigation:** Implement recommended defensive controls: monitor for indicators of compromise, enforce network segmentation, apply multi‑factor authentication, and keep systems patched.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — Race Against Time: Why Faster Vulnerability Alerts Matter

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://www.bleepingcomputer.com/news/security/race-against-time-why-faster-vulnerability-alerts-matter/>

> Attackers are exploiting vulnerabilities faster than many organizations can identify and patch them. SecAlerts explains why faster vulnerability alerts can help reduce exposure and improve response times. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC/weaponized exploit tied to this article; exploit availability unavailable for a specific vulnerability in the article.
- **Patch Available:** Patch information unavailable.
- **Active Exploitation:** The article does not report confirmed active exploitation for the discussed vulnerability; related active exploits are documented for other CVEs in linked sources.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟠 Zero-Day — ⚡ Weekly Recap: New Linux Flaw, PAN-OS Exploit, AI-Powered Attacks, OAuth Phishing and More

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://thehackernews.com/2026/06/weekly-recap-new-linux-flaw-pan-os.html>

> Monday hit like a cron job with anger issues.

A busted auth path here, a repo-side faceplant there, some &quot;patched-ish&quot; thing already getting chewed on in the wild, and then the usual bonus round: poisoned dev tools, sketchy forum chatter, phishing kits pretending to be productivity, and AI lowering the bar for people who already thought &#x27;curl | sh&#x27; had a personality.

The vibe…

---

## 12. 🟠 Zero-Day — Microsoft says it will not pursue security researchers after zero-day backlash

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Record by Recorded Future &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://therecord.media/microsoft-says-it-will-not-pursue-security-researchers-disclosure>

> Microsoft said it is taking the feedback seriously, adding: “To be clear about our approach to legal matters, we have no intention to pursue action against individuals conducting or publishing their security research.”

---

## 13. 🟡 High Severity — Critical Windows Netlogon Vulnerability in Attackers’ Crosshairs

**CVE:** `CVE-2026-41089` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://www.securityweek.com/critical-windows-netlogon-vulnerability-in-attackers-crosshairs/>

> Organizations are advised to patch CVE-2026-41089 as soon as possible, given its severity, the potential ongoing exploitation. The post Critical Windows Netlogon Vulnerability in Attackers’ Crosshairs appeared first on SecurityWeek .

---

## 14. 🟡 High Severity — praisonai-platform: Any workspace member can add arbitrary user as owner via POST /workspaces/{id}/members

**CVE:** `CVE-2026-47413` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://github.com/advisories/GHSA-8g2p-pqm3-fcfh>

> ## Summary

**Type:** Privilege escalation / cross-tenant member injection. The `POST /workspaces/{workspace_id}/members` endpoint is gated only by `require_workspace_member(workspace_id)` (default `min_role=&quot;member&quot;`) and forwards the request body&#x27;s `user_id` and `role` straight into `MemberService.add(workspace_id, user_id, role)`, which has no caller-permission check. A user with…

---

## 15. 🟡 High Severity — Nezha's authenticated agents can forge service-monitor results for other users' services

**CVE:** `CVE-2026-48119` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://github.com/advisories/GHSA-4g6j-g789-rghm>

> #### Summary

Nezha accepts service-monitor `TaskResult` messages from an authenticated agent based only on whether the reported service ID exists. The dashboard authenticates the agent and derives the reporter server ID from the gRPC stream, but the service-monitor result worker does not verify that the reporter server was selected for that service, belongs to the service owner, or was actually a…

---

## 16. 🟡 High Severity — CVE-2026-0826: How an Old Bug Can Feed AI-Powered Impersonation

**CVE:** `CVE-2026-0826` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://www.rapid7.com/blog/post/ve-cve-2026-0826-how-an-old-bug-can-feed-ai-powered-impersonation>

> One of the more persistent myths in security is that old bug classes become old problems. They don’t. They just show up in different places, under different conditions, and usually at the exact moment we’ve convinced ourselves not to pay attention to them. That’s part of what makes enterprise voice infrastructure so interesting. Earlier this year, we wrote about a critical vulnerability in Grandst…

---

## 17. 🟡 High Severity — Recent Palo Alto Networks Vulnerability Exploited for Weeks

**CVE:** `CVE-2026-0257` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-01
**Reference:** <https://www.securityweek.com/recent-palo-alto-networks-vulnerability-exploited-for-weeks/>

> Hackers began exploiting CVE-2026-0257, an authentication bypass in Palo Alto Networks PAN-OS, four days after public disclosure. The post Recent Palo Alto Networks Vulnerability Exploited for Weeks appeared first on SecurityWeek .

---

## 18. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
