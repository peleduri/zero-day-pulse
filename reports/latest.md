# Zero Day Pulse

> **Generated:** 2026-06-12 09:56 UTC &nbsp;|&nbsp; **Total:** 29 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 13 &nbsp;|&nbsp; 🟡 High: 16 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE‑2024‑57727 is a directory traversal flaw in SimpleHelp 5.5.7 and earlier that lets unauthenticated remote attackers read arbitrary files on the system, including logs, configuration files, and credentials.
- **Affected Products:** SimpleHelp remote support software version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or exploit URL is known.
- **Patch Available:** A fix is available in SimpleHelp version 5.5.8 or later; see the vendor advisory for details.
- **Active Exploitation:** Yes – ransomware actors have been reported leveraging CVE‑2024‑57727 in real‑world attacks.
- **Threat Actors:** Ransomware actors (unspecified groups)
- **Mitigation:** Upgrade SimpleHelp to version 5.5.8 or later. Until then, limit file system permissions for the SimpleHelp service and isolate it on a separate network segment.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — Criminal AI-as-a-Service in 2026: How the Underground Market Is Operationalizing Cybercrime

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://www.rapid7.com/blog/post/tr-criminal-ai-underground-market-operationalizing-cybercrime-2026>

> Introduction The underground market for criminally oriented generative AI has moved beyond the early hype surrounding &#x27;malicious chatbots.&#x27; The gradual integration of AI as a productivity layer within cybercrime operations has become the dominant story, indicating that while the potential for fully autonomous AI hacking systems is possible, attackers are not embracing them as expected. I…

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated stack‑based buffer overflow in SDP parsing for ICE handling, allowing remote code execution as root when ICE is enabled.
- **Affected Products:** HP Poly VVX 150, 250, 350, 450; HP Poly Trio 8300, 8500, 8800
- **CVSS Score:** 9.2
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Rapid7 published a Metasploit module for defender testing (https://www.rapid7.com/blog/post/ve-cve-2026-0826-critical-unauthenticated-stack-buffer-overflow-hp-poly-vvx-trio-voip-phones-fixed/)
- **Patch Available:** HP firmware/UCS update via Poly Lens released June 1, 2026 (https://support.hp.com/us-en/document/ish_15052661-15052687-16/hpsbpy04083)
- **Active Exploitation:** No public in‑the‑wild exploitation observed at time of disclosure.
- **Threat Actors:** None known
- **Mitigation:** Disable ICE if not required; segment voice VLAN; inventory devices and firmware versions; apply HP UCS firmware via Poly Lens; validate remediation with Rapid7 Metasploit module.
- **Vendor Advisory:** https://support.hp.com/us-en/document/ish_15052661-15052687-16/hpsbpy04083

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when external web content or retrieved documents contain adversarial instructions that are incorporated into an AI agent's prompt or context (e.g., via RAG or agent retrieval), causing the model to follow malicious instructions. GeminiJack is a zero‑click IPI‑style exploit against Google Gemini Enterprise.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Proof‑of‑concepts published by Noma Labs (GeminiJack) and Forcepoint (10 IPI payloads).
- **Patch Available:** Patch unavailable. Google and other vendors recommend mitigations; no vendor patch URL available.
- **Active Exploitation:** Confirmed active exploitation reported by Google Threat Intelligence and Noma Labs (GeminiJack zero‑click IPI).
- **Threat Actors:** None known
- **Mitigation:** Mitigations include continuous monitoring for IPI, hardening retrieval and sanitization in RAG/agents, restricting autonomous agent actions, safe browsing and content filtering, robust canonicalization and provenance checks on retrieved content, and vendor‑provided hardening guidance.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) attacks embed malicious instructions in external data sources (web pages, documents, emails, links) that an LLM ingests during a user request; the injected instructions aim to manipulate model behavior or exfiltrate data. Google’s mitigation pipeline includes detection classifiers, markdown sanitization, suspicious URL redaction, security thought reinforcement, user confirmation framework, deterministic policy controls, ML/LLM retraining, and model hardening.
- **Affected Products:** Google Workspace with Gemini (Gmail, Docs editors, Drive, Chat, Gemini app)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept or weaponized exploit is available.
- **Patch Available:** No vendor patch is available; mitigations are continuous layered defenses described in the advisory.
- **Active Exploitation:** Public reporting indicates IPI attempts have been observed and studied; however, no confirmed large‑scale active exploitation campaign attributed to specific threat actors has been reported.
- **Threat Actors:** None known
- **Mitigation:** Use Google’s layered defenses: prompt‑injection content classifiers, markdown sanitization and suspicious URL redaction (Safe Browsing), user‑confirmation framework for risky actions, end‑user security mitigation notifications, deterministic policy engine for rapid config fixes (regex takedowns, URL sanitization, tool‑chaining), synthetic‑data generation for ML/LLM retraining, and ongoing red‑team/VRP engagement.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The primary risk is indirect prompt injection where malicious web content influences agentic browser prompts; Google describes layered defenses to detect and mitigate such injections and to restrict origin access and unsafe AI actions.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit unavailable
- **Patch Available:** Chrome security features/defenses described in the vendor blog; official vendor advisory URL above (no discrete patch link provided)
- **Active Exploitation:** No confirmed active exploitation reported
- **Threat Actors:** None known
- **Mitigation:** Apply Chrome’s updated agentic security features described by Google (layered defenses to block prompt injections, restrict origin access, and prevent unsafe AI actions); follow Chrome updates and enable the latest browser version.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit/PoC information unavailable.
- **Patch Available:** Patch information unavailable.
- **Active Exploitation:** No confirmed active exploitation reported in the referenced post.
- **Threat Actors:** None known
- **Mitigation:** Use memory-safety strategies (adopt Rust for new code, reduce C/C++ usage, apply secure-coding reviews); detailed mitigation steps unavailable.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when untrusted external content retrieved by an AI system contains hidden instructions that manipulate the model’s behavior (e.g., exfiltrate data, override higher-level constraints). Attack path typically requires the agent to fetch external content into its prompt context (emails, web pages, documents), and the malicious content leverages the model’s instruction‑following tendency. Mitigations include provenance checks, sanitization, explicit instruction sealing, and limiting retrieval of untrusted sources.
- **Affected Products:** Google Workspace integrations and systems that perform retrieval from external content into prompts (generic)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No confirmed public weaponized exploit tied to this specific Google blog advisory; separate CVEs (e.g., CVE-2025-46059, CVE-2025-54131) have PoCs in some reports. "Proof-of-concept availability varies by vulnerability; none provided in the Google advisory."
- **Patch Available:** No single "patch" – Google describes a layered defense and mitigations for indirect prompt injection in the blog post; vendor advisory URL provided.
- **Active Exploitation:** Reports indicate increasing IPI attempts in the wild (see SecurityWeek, Forcepoint, Infosecurity summaries). No confirmed attribution to specific actor groups for the Google advisory.
- **Threat Actors:** None known
- **Mitigation:** Implement defense-in-depth including content provenance controls, retrieval sanitization, input/output filters, model behavior constraints, strict access controls, telemetry and monitoring, and continuous threat analysis as described in the Google Security Blog post.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC‑linked APTs exploit known, publicly disclosed vulnerabilities and weak/default configurations on edge routers, firewalls, NAS, and IoT devices to gain initial access (no zero‑days observed). They create persistence by adding accounts, modifying router configs, enabling on‑box containers, using SPAN/ERSPAN or GRE/MPLS tunnels for covert exfiltration, and leveraging compromised devices to pivot. A large Mirai‑based botnet (Integrity Tech) was used to manage compromised devices and proxy actor operations.
- **Affected Products:** Cisco IOS/IOS XE, Ivanti Connect Secure/Policy, Ivanti MobileIron, FortiOS/FortiProxy, Juniper Junos, F5 Big‑IP, MikroTik RouterOS, Zyxel (NAS/USG/ZyWALL), Netgate pfSense, QNAP QTS/QuTS, Apache Solr/ActiveMQ/Superset, Ubiquiti UniFi, NETGEAR routers, Telstra Smart Modem, Hikvision web servers, Tenda, DrayTek Vigor, Zyxel, Totolink, D‑Link, Contec SolarView, Cisco Small Business RV series, and many SOHO routers, firewalls, NAS, and IoT devices
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoCs exist for some referenced CVEs and Mirai‑based botnet malware is public; investigators observed Mirai‑derived payloads and numerous CVE exploitation chains (see Joint CSA Appendix). Specific PoC URLs vary by CVE.
- **Patch Available:** Official vendor patches are available for many of the exploited CVEs; organizations should apply vendor firmware/software updates per vendor advisories (see CISA and Joint CSA for CVE lists and vendor guidance).
- **Active Exploitation:** Yes — confirmed large‑scale active exploitation since at least 2021, including thousands–hundreds of thousands of compromised devices, operational botnet activity (Mirai‑derived) and targeted compromises of telecommunications and critical infrastructure devices (CISA AA25-239A; Joint CSA; Canadian advisory).
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor, Integrity Technology Group (Integrity Tech), Flax Typhoon, RedJuliett, Ethereal Panda
- **Mitigation:** Prioritize patching known exploited CVEs; disable unused management services/protocols (HTTP, Telnet, SNMPv1/v2c); restrict management interfaces to secured networks; enforce strong non‑default credentials and phishing‑resistant MFA/public‑key auth for admins; validate firmware/image integrity (hash checks); monitor logs and configuration integrity; segment IoT and management networks; remove or replace EOL devices; follow vendor hardening guides (Cisco, Fortinet, etc.).
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details: long-running cyber espionage campaign using initial access via compromised credentials, spearphishing and living-off-the-land tooling to conduct reconnaissance, credential harvesting, and long-term access to logistics and technology networks.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit referenced in the advisory; exploit availability: None known.
- **Patch Available:** No vendor-specific patch referenced in the advisory; mitigations and detection guidance provided by CISA/FBI/NNSA advisory links.
- **Active Exploitation:** Confirmed active exploitation reported by CISA/FBI/NCSC/NSA in advisory — targeting Western logistics entities and technology companies since 2022.
- **Threat Actors:** GRU 85th GTsSS (Unit 26165) — Russian state-sponsored actors (aka APT28)
- **Mitigation:** Mitigations: implement multi-factor authentication, enforce least privilege, patch and harden internet-facing assets, monitor for anomalous access, use EDR/endpoint monitoring, follow CISA/FBI detection and response guidance in the advisory links.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 10. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** Improper link resolution before file access ('link following') in Microsoft Defender allows an authorized attacker to elevate privileges locally.
- **Affected Products:** Various Microsoft products across Windows components and Microsoft Defender
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoCs were reported for at least some of the disclosed issues; references include CrowdStrike and BleepingComputer write‑ups.
- **Patch Available:** Microsoft released security updates as part of the June 2026 Patch Tuesday; patches are available via the Security Update Guide, Windows Update, and associated KB articles.
- **Active Exploitation:** Confirmed active exploitation for at least one zero‑day prior to patching; reported by CrowdStrike and BleepingComputer.
- **Threat Actors:** None known
- **Mitigation:** Apply Microsoft’s June 2026 security updates immediately; use vendor‑provided workarounds where described.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/

---

## 11. 🟠 Zero-Day — Anthropic Disputes Fable 5 AI Jailbreak

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://www.securityweek.com/anthropic-disputes-fable-5-ai-jailbreak/>

> An AI hacker claims to have achieved a prompt-based jailbreak shortly after Fable 5’s launch, but Anthropic says it’s not a real jailbreak. The post Anthropic Disputes Fable 5 AI Jailbreak appeared first on SecurityWeek .

---

## 12. 🟠 Zero-Day — CISA orders feds to patch actively exploited Ivanti flaw by Sunday

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-gives-feds-3-days-to-patch-ivanti-flaw-exploited-in-attacks/>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) ordered government agencies to patch an actively exploited Ivanti Sentry flaw within three days, as mandated by the newly issued Binding Operational Directive (BOD) 26-04. [...]

---

## 13. 🟠 Zero-Day — ShinyHunters Exploits Oracle PeopleSoft Zero-Day (CVE-2026-35273) to Breach Universities

**CVE:** `CVE-2026-35273` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://thehackernews.com/2026/06/shinyhunters-exploits-oracle-peoplesoft.html>

> The ShinyHunters extortion crew exploited an unpatched flaw in Oracle PeopleSoft to break into enterprise systems, steal data, and demand payment to keep it private. The campaign hit universities hardest.

Google&#x27;s Mandiant attributes it to the group it tracks as UNC6240, and dates the activity between May 27 and June 9. Oracle did not publish its advisory until June 10, so the bug was a

---

## 14. 🟡 High Severity — GeoServer DB2 DataStore Extension has a JNDI Vulnerability via Store Connection

**CVE:** `CVE-2025-27511` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-g628-r368-6vh7>

> ## Summary

Administrator can perform JNDI attack through specially crafted DB2 jdbc url leading to Remote Code Execution (RCE).

## Impact

If GeoServer has DB2 extension installed, this vulnerability can lead to executing arbitrary code.

## Details

Authenticated users can access Vector Data Sources page to creating a new data store through db2 jdbc connection, performing JNDI attack due to unr…

---

## 15. 🟡 High Severity — Russh SSH message fields were decoded through allocation-first parsers before field-specific bounds

**CVE:** `CVE-2026-48110` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-4r3c-5hpg-58qr>

> # SSH message fields were decoded through allocation-first parsers before field-specific bounds

### Summary

Several `russh` client and server message handlers decoded attacker-controlled SSH strings, name-lists, and byte fields into owned allocations before applying field-specific bounds. A remote SSH peer could send oversized, high-fanout, or malformed length-prefixed fields and make the librar…

---

## 16. 🟡 High Severity — AWS Advanced Go Wrapper has Privilege Escalation in Aurora PostgreSQL instance

**CVE:** `CVE-2026-11401` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-r236-5pc3-3qcp>

> Aurora PostgreSQL is a fully managed relational database engine that&#x27;s compatible with PostgreSQL.

An issue in Aurora PostgreSQL using the AWS Go Wrapper waa identified, see CVE-2026-11401.


Impact
An issue in AWS Wrappers for Amazon Aurora PostgreSQL may allow for privilege escalation to rds_superuser role. A low privilege authenticated user can create a crafted function that could be exec…

---

## 17. 🟡 High Severity — Russh: SSH identification parsing accepted non-canonical client banners and did not bound pre-banner input

**CVE:** `CVE-2026-48108` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-76r6-x97p-67vr>

> ### Summary

`russh` did not enforce the SSH identification-string rules as deliberately as OpenSSH. In particular, the server-side identification reader used the same permissive path as the client, allowing pre-banner lines from clients, and the reader did not enforce a bounded number of pre-banner lines.

For a library server built on `russh`, this could allow a remote peer to hold connection se…

---

## 18. 🟡 High Severity — WsgiDAV encoded dot segments can escape filesystem share roots

**CVE:** `CVE-2026-48099` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-wxq4-cc2q-338q>

> ### Impact
WsgiDAV 4.3.3 can allow a WebDAV request path containing an encoded parent-directory segment to escape the configured filesystem share root in a specific path layout.

### Patches
The issue is fixed with version 4.3.4.

### Preconditions

The practical impact depends on the deployment.

The deployment uses a filesystem-backed WsgiDAV share.

The attacker can send WebDAV requests accepte…

---

## 19. 🟡 High Severity — Netty HAProxy: Unbalanced Reference Count in Nested PP2_TYPE_SSL TLV Parsing Leads to Memory Exhaustion

**CVE:** `CVE-2026-48059` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-h2qv-fj59-j46j>

> ### Impact
The HAProxy PROXY protocol v2 codec in netty leaks native or heap memory on every connection when a client sends a syntactically valid header containing nested `PP2_TYPE_SSL` TLVs (type-length-value records) at depth two or greater. The leak occurs on the successful parse path — no exception is thrown, the message fires downstream, the decoder removes itself, and the application release…

---

## 20. 🟡 High Severity — Kolibri has Unauthenticated Server-Side Request Forgery (SSRF) in RemoteFacilityUserViewset

**CVE:** `CVE-2026-48053` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-4mj9-pf4r-cqrc>

> ## Summary

Several Kolibri API endpoints accept an unvalidated `baseurl` parameter and fetch attacker-controlled URLs from the Kolibri server, reflecting the response body back to the caller. The original report identified two endpoints on the `RemoteFacilityUser*` viewsets; remediation review found two further reflection points on the same pattern. The GET endpoint was unauthenticated.

## Affec…

---

## 21. 🟡 High Severity — Arc: Unauthenticated access to Go debug pprof endpoints leaks runtime state and enables CPU-burn DoS

**CVE:** `CVE-2026-48050` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-j93g-rp6m-j32m>

> ### Summary

Arc registers Go&#x27;s `net/http/pprof` handlers at `/debug/pprof/*` via `app.Use(pprof.New())` in `internal/api/server.go`, and `/debug/pprof` is added to `PublicPrefixes` in `cmd/arc/main.go`. The auth middleware short-circuits before the token check on prefix match, so the endpoints are reachable without any authentication.

### Impact

Any network-reachable caller (no token requi…

---

## 22. 🟡 High Severity — @hapi/inert has a static-file confinement bypass via sibling-prefix path

**CVE:** `CVE-2026-48049` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-rcvq-m9j9-6f4g>

> ### Impact
`@hapi/inert` serves static files from a directory configured with `path` (in the `directory` / `file` handlers) or `relativeTo` (for `h.file()`), with confinement enforced by the `confine` option (default `true`). Before the patch, the confinement check compared the resolved absolute path against the confine directory using a raw string-prefix test, so a sibling directory whose absolut…

---

## 23. 🟡 High Severity — python-zeroconf: Unbounded TC-deferred queue allows LAN-local memory exhaustion via spoofed-source flood

**CVE:** `CVE-2026-48045` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-9663-mqmp-p9mm>

> ### Impact

`AsyncListener.handle_query_or_defer` retained every truncated (TC-bit) incoming query in `self._deferred[addr]` and armed a per-addr timer in `self._timers[addr]` that flushed the reassembled query within ~500 ms (RFC 6762 §18.5). Neither the per-addr list nor the number of distinct `addr` keys was capped, and the dedup check (`for incoming in reversed(deferred): if incoming.data == m…

---

## 24. 🟡 High Severity — Meta Ads MCP: Unauthenticated HTTP MCP Tool Execution Leaks Operator Meta Access Token

**CVE:** `CVE-2026-48039` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-9gw6-46qc-99vr>

> # Unauthenticated HTTP MCP Tool Execution Leaks Operator Meta Access Token

| Field            | Value |
| ---------------- | ----- |
| Repository       | pipeboard-co/meta-ads-mcp |
| Affected version | ≤ 1.0.101 (commit 496c988 ~ 7d14226); Versions 1.0.102–1.0.105 lack git tags, so patch status is unconfirmed. |
| Vulnerability    | CWE-287 — Improper Authentication |
| Severity         | Critic…

---

## 25. 🟡 High Severity — @hapi/wreck: Sensitive credential headers leak across cross-port and cross-scheme redirects

**CVE:** `CVE-2026-48022` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-x426-x7cc-3fpc>

> ### Impact
Wreck strips credential headers (Authorization, Cookie, Proxy-Authorization) before following a cross-origin redirect, but the origin check compares hostnames only and ignores scheme and port. As a result, credentials are forwarded intact across same-host port changes and HTTPS-to-HTTP downgrades, allowing a co-tenant on an adjacent port or a network-position attacker capable of forging…

---

## 26. 🟡 High Severity — Netty's Lack of Lifecycle Cleanup Leads to Pooled ByteBuf Leak in RedisArrayAggregator

**CVE:** `CVE-2026-48006` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-6jv9-x5w9-2ccm>

> ### Impact
The RedisArrayAggregator handler permanently leaks pooled direct-memory buffers when a Redis pipeline connection closes before a RESP array aggregate completes. The handler retains child messages in per-handler state (`depths` field) but defines no `channelInactive`, `handlerRemoved`, or `exceptionCaught` method to release them when the pipeline tears down. Because the leaked buffers ar…

---

## 27. 🟡 High Severity — PDM: Project-Controlled `.pdm-plugins` Content Executes Before CLI Parsing

**CVE:** `CVE-2026-47781` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-qq6c-99pv-prvf>

> ## Summary

PDM automatically loads project-local plugin paths from `.pdm-plugins` during `Core` initialization. Because this path is added via `site.addsitedir()`, attacker-controlled `.pth` files inside the project plugin directory are processed and can execute Python code before normal CLI handling begins.

This allows arbitrary code execution with the privileges of the user running `pdm` from …

---

## 28. 🟡 High Severity — free5GC UDR has improper `ueId` validation in EE subscription handlers that allows arbitrary identifier persistence

**CVE:** `CVE-2026-47780` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-6gxq-gpr8-xgjp>

> ### Summary
The free5GC UDR accepts arbitrary non-3GPP ueId values in the EE subscription creation and query flows because the regular expression used for validation ends with the catch-all alternative |.+. This causes the validation logic to accept any non-empty string rather than restricting input to expected SUPI/GPSI-style formats. In a tested deployment, a crafted value such as ARBITRARY_STRI…

---

## 29. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
