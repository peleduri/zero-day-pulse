# Zero Day Pulse

> **Generated:** 2026-06-16 10:52 UTC &nbsp;|&nbsp; **Total:** 35 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 13 &nbsp;|&nbsp; 🟡 High: 22 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated HTTP path traversal allows attackers to download arbitrary files from the SimpleHelp host, such as configuration files with secrets, enabling further compromise.
- **Affected Products:** SimpleHelp remote support / RMM server versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Public proof‑of‑concept and exploit details are available on the Offensive Security blog (https://offsec.com/blog/cve-2024-57727).
- **Patch Available:** SimpleHelp 5.5.8 (and 5.4.10) patch released; see vendor advisory.
- **Active Exploitation:** Yes – CISA reports ransomware actors have exploited unpatched SimpleHelp, and the CVE is listed in the KEV catalog.
- **Threat Actors:** Ransomware actors (including groups reported as ‘DragonForce’)
- **Mitigation:** Isolate or stop the vulnerable SimpleHelp server, upgrade immediately to version 5.5.8 or later, conduct threat hunting for malicious executables, block internet access to the RMM, enforce MFA, and apply network segmentation.
- **Vendor Advisory:** https://simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** IPI (Indirect Prompt Injection): attacker seeds malicious content in external corpora or web pages that AI agents (RAG/agentic systems) retrieve, causing the agent to execute attacker-controlled instructions—can be zero‑click when the agent autonomously browses or retrieves context.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC and in‑the‑wild payloads disclosed by researchers (e.g., Forcepoint/Antigravity RAG disclosures, Noma Labs GeminiJack report); specific exploit URLs: http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability, http://lyrie.ai/research/research/indirect-prompt-injection-goes-operational-wild-forcepoint-antigravity-rag
- **Patch Available:** Vendor guidance and mitigations published by Google (security blog) — advisory URL: http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html
- **Active Exploitation:** Confirmed research disclosures and in‑the‑wild payloads reported by multiple security teams (Forcepoint, Noma Labs) and academic work demonstrating end‑to‑end IPI exploits; see citations.
- **Threat Actors:** None known
- **Mitigation:** Follow vendor hardening guidance (sanitise retrieved content, retrieval filters, strict tool‑use policies for agents, RAG provenance checks, disable autonomous browsing for untrusted sources); see Google security blog for recommendations.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) embeds malicious instructions into data sources (emails, invites, documents) or tools used by LLMs; agentic automation and multi‑source contexts let injected instructions influence LLM behavior without explicit user input, enabling data exfiltration or task manipulation.
- **Affected Products:** Google Workspace (including Gemini in Workspace, Gemini app, Gemini Enterprise)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC reports (GeminiJack) from Noma Labs demonstrated a zero‑click IPI; details published on Noma Labs blog and covered by SecurityAffairs.
- **Patch Available:** Google describes layered defenses and mitigations in the advisory; no single “patch” — mitigations deployed by Google in Workspace/Gemini per advisory.
- **Active Exploitation:** Reports of GeminiJack (Noma Labs) demonstrating zero‑click IPI; public write‑ups indicate real exploitation and a responsible disclosure/fix process.
- **Threat Actors:** None known
- **Mitigation:** Google recommends layered defenses: content filtering/normalization of inputs, provenance‑based controls, model fine‑tuning and instruction‑safety layers, limiting agentic tool actions, telemetry/monitoring, and rapid patching/response in Workspace/Gemini.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: untrusted web content (pages, iframes, UGC, ads) manipulates the agent’s planning model to perform unwanted actions such as goal hijacking or data exfiltration. Chrome mitigates this by isolating the planner from untrusted content, using origin gating, a separate alignment critic, deterministic checks, and a real‑time prompt‑injection classifier.
- **Affected Products:** Agentic browsing features in Google Chrome (Gemini‑powered agentic capabilities)
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit reported in the advisory or cited coverage.
- **Patch Available:** No separate "patch" described; Google implemented architectural defenses in Chrome (layered mitigations) and relies on Chrome auto‑update to deliver changes. Vendor advisory URL provided above.
- **Active Exploitation:** No confirmed active exploitation reported in the advisory or referenced news coverage.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: user alignment critic (veto high‑risk actions), agent origin sets (read‑only vs read‑write origins), deterministic user confirmations for sensitive actions, real‑time prompt‑injection classifier, continuous red‑team testing and VRP engagement; keep Chrome auto‑updated and follow VRP guidance.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Adopting Rust for parts of Android reduced memory‑safety vulnerability density substantially; memory safety vulnerabilities fell below 20% of total vulnerabilities in 2025, attributed to Rust's ownership/borrowing model that prevents classes of memory errors present in C/C++.
- **Affected Products:** Android platform (C, C++, Java, Kotlin, Rust)
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** None known
- **Patch Available:** No official vendor patch available.
- **Active Exploitation:** No confirmed active exploitation reported
- **Threat Actors:** None known
- **Mitigation:** Adopt memory‑safe languages (Rust) for new code, continue code audits, fuzzing, automated testing, and vulnerability prevention strategies; prioritize fixes in unsafe code paths.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injections embed malicious instructions in external data sources (e.g., emails, documents, calendar invites) that are later incorporated into AI prompts, allowing attackers to steer model behavior, exfiltrate data, or trigger unauthorized actions.
- **Affected Products:** Gemini (Google Workspace Gemini, Gemini mobile app)
- **CVSS Score:** -0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** None known
- **Patch Available:** No official patch available.
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Implement layered defenses: model hardening/adversarial training; prompt‑injection content classifiers; security‑thought reinforcement; markdown sanitization and block external image rendering; suspicious URL detection/redaction (Safe Browsing); contextual user confirmation for risky actions; user‑facing security notifications and help‑center guidance.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors modify router configurations for lateral movement, deploy virtualized containers on network devices to evade detection, alter ACLs (e.g., "access-list 20"), open ports, enable HTTP/HTTPS servers, and execute commands via SNMP, SSH, web POSTs, or Tcl scripts (TCLproxy.tcl, map.tcl). Exploited CVEs (e.g., CVE‑2024‑21887, CVE‑2023‑20273, CVE‑2023‑20198, CVE‑2018‑0171) provide the initial foothold.
- **Affected Products:** Cisco IOS XE (various versions), Cisco IOS (various versions), Ivanti (product unspecified)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept exploit information is provided in the cited sources.
- **Patch Available:** Vendor patches for the impacted Cisco IOS XE vulnerabilities are available; see Cisco security advisories linked from the CISA advisory.
- **Active Exploitation:** Confirmed active exploitation of the listed CVEs by PRC‑state‑sponsored actors has been reported in the advisory.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching the known exploited CVEs; disable unused ports and protocols; change default credentials; require public‑key authentication; adopt vendor‑recommended OS versions; follow Cisco IOS/XE hardening guides and forensic guidance.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** The campaign leverages CVE-2023-38831 in WinRAR to execute malicious code when a crafted archive is opened, CVE-2023-23397 in Outlook to exploit NTLM authentication via specially crafted emails, and CVE-2020-35730/CVE-2020-12641 in Roundcube to inject commands through webmail interfaces.
- **Affected Products:** WinRAR (CVE-2023-38831), Microsoft Outlook (CVA-2023-23397), Roundcube (CVE-2020-35730, CVE-2020-12641).
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No publicly disclosed proof‑of‑concept exploit URLs are provided in the available sources.
- **Patch Available:** Patches are available for WinRAR (CVE-2023-38831), Microsoft Outlook (CVE-2023-23397), and Roundcube (CVE-2020-35730, CVE-2020-12641). See CISA advisory for details.
- **Active Exploitation:** Yes, active exploitation has been reported for WinRAR (CVE-2023-38831), Outlook (CVE-2023-23397), and Roundcube vulnerabilities as part of the Russian GRU campaign.
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS).
- **Mitigation:** Apply the latest security patches for WinRAR, Outlook, and Roundcube; enable attack surface reduction rules; activate authenticated RTSP on cameras; use endpoint detection and response (EDR) tools; monitor Windows event logs and authentication activity; harden IP cameras and review network traffic.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Windows 10, Windows 11, Microsoft Defender, Microsoft Malware Protection Engine, Exchange Server
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof‑of‑concepts are available; see CrowdStrike blog (https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/) and The Hacker News article (https://thehackernews.com/2026/06/microsoft-defender-rogueplanet-zero-day.html).
- **Patch Available:** Microsoft released June 2026 security updates (KB5094126) available at https://support.microsoft.com/en-us/topic/june-9-2026-kb5094126-os-builds-26200-8655-and-26100-8655-1a9bcba6-5f53-4075-8156-fe11ac631737
- **Active Exploitation:** Active exploitation reported for Microsoft Defender/Malware Protection Engine and Exchange Server zero‑day (CVE‑2026‑42897).
- **Threat Actors:** None known
- **Mitigation:** Install the June 2026 security update KB5094126 and apply any vendor‑recommended mitigations described in the advisory. If the patch cannot be applied, follow the workarounds or component disablements outlined in the advisory.
- **Vendor Advisory:** https://support.microsoft.com/en-us/topic/june-9-2026-kb5094126-os-builds-26200-8655-and-26100-8655-1a9bcba6-5f53-4075-8156-fe11ac631737

---

## 10. 🟠 Zero-Day — Tech Coalition ‘Athena’ Targets OSS Vulnerabilities Ahead of Disclosure

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://www.securityweek.com/tech-coalition-athena-targets-oss-vulnerabilities-ahead-of-disclosure/>

> Over two dozen organizations built a shared platform to triage vulnerabilities, fix them, and secure the software before patches arrive. The post Tech Coalition ‘Athena’ Targets OSS Vulnerabilities Ahead of Disclosure appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit or PoC information available.
- **Patch Available:** No official patch information available.
- **Active Exploitation:** Active exploitation information unavailable.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟠 Zero-Day — Fake Microsoft Alerts Used to Deploy North Korean NarwhalRAT Malware

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://thehackernews.com/2026/06/fake-microsoft-alerts-used-to-deploy.html>

> The North Korean state-sponsored hacking group known as ScarCruft (aka APT37) has been observed using spear-phishing messages impersonating Microsoft Account security notifications to deliver malware called NarwhalRAT.

&quot;The attack email contained a message impersonating an MS account security alert,&quot; the Genians Security Center (GSC) said. &quot;It was designed to create concern over po…

---

## 12. 🟠 Zero-Day — Cisco Releases Security Updates for Actively Exploited SD-WAN Manager Flaw

**CVE:** `CVE-2026-20262` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://thehackernews.com/2026/06/cisco-releases-security-updates-for.html>

> Cisco has released security updates for a medium-severity security flaw in Catalyst SD-WAN Manager that has come under active exploitation in the wild.

The vulnerability, tracked as CVE-2026-20262, carries a CVSS score of 6.5 out of 10.0.

&quot;A vulnerability in the web UI of Cisco Catalyst SD-WAN Manager, formerly SD-WAN vManage, could allow an authenticated, remote attacker to create a file o…

---

## 13. 🟠 Zero-Day — ⚡ Weekly Recap: Chrome 0-Day, UniFi Exploits, macOS Stealers, VPN Flaw and More

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://thehackernews.com/2026/06/weekly-recap-chrome-0-day-unifi.html>

> Stuff broke again. Not in a movie way. An old tool was left exposed. An abandoned package was abused. A deprecated feature was still running in prod.

This week is the same lesson in a new form: phishing kits are easier to rent, AI names are useful bait, old login paths still fail, and forgotten software keeps becoming someone else&#x27;s entry point.

Scroll through the full Monday Cybersecurity

---

## 14. 🟡 High Severity — Attackers Exploit Three Fortinet FortiSandbox Flaws, One Patched Last Week

**CVE:** `CVE-2026-39813` | `CVE-2026-39808` | `CVE-2026-25089` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://thehackernews.com/2026/06/attackers-exploit-three-fortinet.html>

> Bad actors are exploiting multiple security vulnerabilities in Fortinet FortiSandbox, according to threat intelligence firm Defused Cyber.

In a post shared on X, the company said it has observed exploitation of CVE-2026-39813, CVE-2026-39808, and CVE-2026-25089 over the past 24 hours.

CVE-2026-39813 (CVSS score: 9.1) refers to a path traversal vulnerability in FortiSandbox JRPC API that could

---

## 15. 🟡 High Severity — SEC Consult SA-20260610-0 :: Local Privilege Escalation in Slate Digital Connect (macOS)

**CVE:** `CVE-2026-24066` | `CVE-2026-24067` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://seclists.org/fulldisclosure/2026/Jun/7>

> Posted by SEC Consult Vulnerability Lab via Fulldisclosure on Jun 15 SEC Consult Vulnerability Lab Security Advisory &lt; 20260610-0 &gt; ======================================================================= title: Local Privilege Escalation product: Slate Digital Connect (macOS) vulnerable version: 1.37.0 fixed version: - CVE number: CVE-2026-24066, CVE-2026-24067 impact: high homepage:...

---

## 16. 🟡 High Severity — SEC Consult SA-20260609-0 :: Multiple Local Privilege Escalation Vulnerabilities in Waves Audio - Waves Central

**CVE:** `CVE-2026-24064` | `CVE-2026-24065` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://seclists.org/fulldisclosure/2026/Jun/6>

> Posted by SEC Consult Vulnerability Lab via Fulldisclosure on Jun 15 SEC Consult Vulnerability Lab Security Advisory &lt; 20260609-0 &gt; ======================================================================= title: Multiple Local Privilege Escalation Vulnerabilities product: Waves Audio - Waves Central vulnerable version: v13.0.8 - v16.6.0 fixed version: v16.6.2 CVE number: CVE-2026-24064, CVE-2…

---

## 17. 🟡 High Severity — CISA Flags LiteSpeed cPanel Plugin Flaw Exploited for Root Privilege Escalation

**CVE:** `CVE-2026-54420` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://thehackernews.com/2026/06/cisa-flags-litespeed-cpanel-plugin-flaw.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has added a security flaw impacting LiteSpeed cPanel Plugin to its Known Exploited Vulnerabilities (KEV) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the fixes by June 18, 2026.

The vulnerability in question is CVE-2026-54420 (CVSS score: 8.5), which has been described as a case of privilege

---

## 18. 🟡 High Severity — aws-cdk-lib: OS Command Injection in NodejsFunction Bundling

**CVE:** `CVE-2026-11417` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-999r-qq7v-r334>

> ### Summary
AWS CDK (`aws-cdk-lib`) is an open-source framework for defining cloud infrastructure in code and provisioning it through AWS CloudFormation. OS command injection in the `NodejsFunction` local bundling pipeline in `aws-cdk-lib` before 2.245.0 (2.246.0 on Windows) might allow a threat actor who controls the value of one or more bundling properties (`externalModules`, `define`, `loader`,…

---

## 19. 🟡 High Severity — Netty: QUIC stateless reset token material exposed through header-visible connection IDs

**CVE:** `CVE-2026-50009` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-cq4q-cv5g-r8q5>

> ### Summary
Netty QUIC exposes the stateless reset token on the network path when using the default HMAC-based connection-ID and stateless-reset-token generators. The reset token for the server&#x27;s current source connection ID can be derived from bytes that appear as the connection ID in QUIC headers after a source-CID rotation. An on-path attacker observing the headers can use the token to per…

---

## 20. 🟡 High Severity — Netty HTTP/3 QPACK Blocked Streams Memory Exhaustion

**CVE:** `CVE-2026-48748` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-4grm-h2qv-h6w6>

> ### Summary
A memory exhaustion vulnerability in the Netty HTTP/3 codec allows the creation of an infinite number of blocked streams, which can cause OOM error.

### Details
The vulnerability exists in `io.netty.handler.codec.http3.QpackDecoder#shouldWaitForDynamicTableUpdates`:

If a client sends a header referencing a table entry that the server hasn&#x27;t received yet, the server must pause th…

---

## 21. 🟡 High Severity — Starlette: Unvalidated request path concatenated into authority poisons request.url.hostname

**CVE:** `CVE-2026-54282` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-jp82-jpqv-5vv3>

> ### Summary

In affected versions, the HTTP request path is not validated before being used to reconstruct `request.url`. Because `request.url` is rebuilt by concatenating `{scheme}://{host}{path}` and re-parsing the result, a path that does not begin with `/` (for example `@google.com`) moves the authority boundary during re-parsing, so `request.url.hostname` and `request.url.netloc` become attac…

---

## 22. 🟡 High Severity — python-multipart: Semicolon treated as querystring field separator enables parameter smuggling

**CVE:** `CVE-2026-53538` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-6jv3-5f52-599m>

> ### Summary

`QuerystringParser` treated `;` as a field separator in `application/x-www-form-urlencoded` bodies, in addition to `&amp;`. The [WHATWG URL standard](https://url.spec.whatwg.org/#urlencoded-parsing), modern browsers, and Python&#x27;s `urllib.parse` (since the CVE-2021-23336 fix) treat only `&amp;` as a separator. This creates a parser differential: the same bytes are tokenized into d…

---

## 23. 🟡 High Severity — Tornado: Authorization header forwarded across cross-origin redirects in SimpleAsyncHTTPClient

**CVE:** `CVE-2026-49853` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-3x9g-8vmp-wqvf>

> ## Summary

When SimpleAsyncHTTPClient follows a 3xx redirect, it shallow-copies the original HTTPRequest, rewrites the URL, decrements max_redirects, and removes only the Host header. It does not clear Authorization, auth_username, auth_password, or auth_mode when the redirect target changes origin.

As a result, credentials intended for one origin can be forwarded to a different origin when foll…

---

## 24. 🟡 High Severity — Starlette: SSRF and NTLM credential theft via UNC paths in StaticFiles on Windows

**CVE:** `CVE-2026-48818` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-wqp7-x3pw-xc5r>

> ### Summary

When serving static files on Windows, `StaticFiles` resolves the requested path with [`os.path.realpath`](https://docs.python.org/3/library/os.path.html#os.path.realpath). If a UNC path (such as `\\attacker.com\share`) reaches the resolver, `realpath` causes the process to open a connection to the remote host over SMB (port 445). This is a server-side request forgery (SSRF) that leaks…

---

## 25. 🟡 High Severity — PyJWKClient: missing scheme allowlist enables CVE-2024-21643-class SSRF + token forgery via file://, ftp://, data: schemes

**CVE:** `CVE-2026-48522` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-993g-76c3-p5m4>

> &gt; [!NOTE]
&gt; The library does not directly return non-HTTP(S) URI contents to the attacker; the chained &quot;plant a JWKS to forge tokens&quot; scenario described in the original report requires additional application-layer flaws (attacker write access to a filesystem path, untrusted jku derivation) that this fix does not address. Severity is scored for the scheme-acceptance bug in isolation…

---

## 26. 🟡 High Severity — PyJWT: Public-key JWK accepted as HMAC secret enables forged HS256 tokens when mixed families are allowed

**CVE:** `CVE-2026-48526` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-xgmm-8j9v-c9wx>

> &gt; [!NOTE]
&gt; Exploitation requires a verifier configured with both symmetric and asymmetric algorithms in `algorithms=[…]` and a raw-JSON JWK as the `key=` argument, both contrary to documented usage, hence the High attack-complexity rating.

### Summary
When the verifier is decoding JSON Web Tokens, while supporting both asymmetric and HMAC algorithms, the library does not validate use of JS…

---

## 27. 🟡 High Severity — Symfony: Mailomat Mailer Webhook Parser Reads the HMAC Algorithm from the Request: Signature Algorithm Downgrade

**CVE:** `CVE-2026-48747` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-rrj9-5q2j-4gvr>

> ### Description

`Symfony\Component\Mailer\Bridge\Mailomat\Webhook\MailomatRequestParser::validateSignature()` parses the `X-MOM-Webhook-Signature` request header as `algo=signature` and passes the wire-supplied `$algo` directly to `hash_hmac()` when verifying the request against the configured webhook secret. The request therefore selects the HMAC primitive used to authenticate it.

PHP&#x27;s `h…

---

## 28. 🟡 High Severity — Symfony: IpUtils::PRIVATE_SUBNETS Omits IPv6 Transition Forms (6to4, NAT64, Teredo, IPv4-compatible): SSRF Bypass in NoPrivateNetworkHttpClient

**CVE:** `CVE-2026-48736` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-38cx-cq6f-5755>

> ### Description

`Symfony\Component\HttpClient\NoPrivateNetworkHttpClient` is documented as a decorator that blocks requests to private networks by default. The list of blocked subnets (`Symfony\Component\HttpFoundation\IpUtils::PRIVATE_SUBNETS` on 6.4+, a private constant in `NoPrivateNetworkHttpClient` on 5.4) enumerates RFC1918, loopback, link-local and IPv4-mapped IPv6 (`::ffff:0:0/96`) prefix…

---

## 29. 🟡 High Severity — @angular/service-worker: Sensitive Header Leakage on Cross-Origin Redirects in Angular Service Worker

**CVE:** `CVE-2026-54264` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-qxh6-94w6-9r5p>

> An information disclosure vulnerability exists in the `@angular/service-worker` package of the Angular framework. When the Service Worker fetches assets, it preserves metadata (such as headers) from the original request. However, on cross-origin redirects, the Service Worker fails to strip sensitive headers, violating the Fetch redirect algorithm. 

This allows a remote attacker to obtain sensitiv…

---

## 30. 🟡 High Severity — Angular: Template and Attribute Namespace Sanitization Bypass (XSS)

**CVE:** `CVE-2026-50557` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-f3m7-gqxr-g87x>

> An issue in the `@angular/compiler` and `@angular/core` packages allows bypassing element and attribute sanitization/validation through specific namespace workarounds.

Specifically, namespaced script elements (e.g., `&lt;svg:script&gt;` or `&lt;:svg:script&gt;`) were not properly identified as script elements by the Angular template preparser, allowing them to pass through template compilation wi…

---

## 31. 🟡 High Severity — node-tar applies PAX size override to intermediary GNU long-name/long-link headers, causing tar parser interpretation differential (file smuggling)

**CVE:** `CVE-2026-53655` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-vmf3-w455-68vh>

> ### Summary

`tar` (node-tar) applies a PAX extended header&#x27;s `size=` record (and other PAX
overrides) to the **next header entry of any type**, including intermediary
metadata headers such as a GNU long-name (`L`) or long-link (`K`) entry. Per
POSIX pax, a PAX extended header (`x`) describes the *next file entry*, not the
intermediary extension headers that may sit between the `x` header and…

---

## 32. 🟡 High Severity — @angular/service-worker: Request Credential & Cache Policy Stripping

**CVE:** `CVE-2026-50184` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-95qp-cmmw-mgqv>

> An issue in the `@angular/service-worker` package compromises the integrity of request-policy enforcement during request reconstruction. When the Angular Service Worker intercepts network requests for matched assets, it reconstructs a new `Request` object using an internal helper function.

During this reconstruction process, the helper function strips explicit client-defined safety parameters: th…

---

## 33. 🟡 High Severity — @angular/platform-server: URL Parser Differential leading to SSRF Allowlist Bypass

**CVE:** `CVE-2026-50168` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-xrxm-cp7j-8xf6>

> An issue in the `@angular/platform-server` package allows remote attackers to bypass host allowlist constraints and direct server-side outgoing requests to arbitrary external endpoints. This occurs due to a parser differential between the strict WHATWG URL parser used for allowlist validation and the lenient Domino URL parser used to initialize the server emulated DOM.

When a server-side request …

---

## 34. 🟡 High Severity — Angular Client Hydration DOM Clobbering & Response-Cache Poisoning

**CVE:** `CVE-2026-54267` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-rgjc-h3x7-9mwg>

> To optimize client-side bootstrap in Server-Side Rendered (SSR) environments, Angular supports **Hydration** via `provideClientHydration()`. During SSR, Angular serializes the application&#x27;s runtime state (such as cached `HttpClient` responses) and outputs it into the HTML stream as a `&lt;script&gt;` tag with a predictable identifier:

```html
&lt;script type=&quot;application/json&quot; id=&…

---

## 35. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
