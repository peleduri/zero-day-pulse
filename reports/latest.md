# Zero Day Pulse

> **Generated:** 2026-06-29 19:35 UTC &nbsp;|&nbsp; **Total:** 15 &nbsp;|&nbsp; 🔴 KEV: 1 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 4 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🔴 CISA KEV — CVE-2026-48558 — SimpleHelp Authentication Bypass Vulnerability

**CVE:** `CVE-2026-48558` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-06-29
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-48558>

> Vendor: SimpleHelp  | Product: SimpleHelp. SimpleHelp contains an authentication bypass vulnerability in the OIDC authentication flow. When OIDC authentication is configured, identity tokens submitted during login are accepted without verifying their cryptographic signature. In a vulnerable configuration, a remote, unauthenticated attacker can submit a forged token containing arbitrary identity cl…

**Parallel AI Enrichment:**

- **Technical Details:** When OIDC is enabled, SimpleHelp accepted submitted OpenID Connect identity tokens without verifying their cryptographic signature; an unauthenticated attacker can submit a forged token with arbitrary identity claims to create a fully authenticated "Technician" session (which can also bypass MFA in some configurations).
- **Affected Products:** SimpleHelp versions 5.5.15 and earlier; SimpleHelp 6.0 pre-release versions.
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit PoC or weaponized exploit code located in the collected sources; IOCs and detection guidance / exploitation details published by security researchers (Horizon3, etc.).
- **Patch Available:** No official vendor patch located in the collected sources as of 2026-06-29; public mitigations and detection guidance published by CISA and industry (see CISA advisory).
- **Active Exploitation:** Yes — confirmed active exploitation reported in the wild by CISA and corroborated by industry reporting (ransomware actors exploiting unpatched SimpleHelp instances).
- **Threat Actors:** Ransomware actors (CISA reported exploitation); some industry reporting attributes attacks to known ransomware groups.
- **Mitigation:** Follow CISA and industry mitigations: apply vendor fixes if/when released; if immediate patching is unavailable, restrict access to SimpleHelp management interfaces, disable OIDC on exposed instances or remove OIDC identity providers until fixed, apply network access controls (IP allowlists), and deploy detection/IOCs provided by researchers.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 2. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** A path traversal (directory traversal) vulnerability in SimpleHelp that allows unauthenticated remote attackers to read arbitrary/sensitive files on the server via crafted requests to the service.
- **Affected Products:** SimpleHelp remote support / RMM software, versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — a public proof-of-concept implementation is available (GitHub repo imjdl/CVE-2024-57727).
- **Patch Available:** Yes — SimpleHelp published vendor guidance and provided fixes; see vendor KB: https://guides.simple-help.com/kb---security-vulnerabilities-01-2025 (vendor guidance) and vendor statement that vulnerabilities were patched (SimpleHelp blog).
- **Active Exploitation:** Yes — CISA reports ransomware actors likely leveraged CVE-2024-57727 against unpatched SimpleHelp RMM instances to access downstream customers (see CISA advisory).
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor-provided patch/update immediately. If you cannot patch immediately: isolate or restrict network access to the SimpleHelp instance (firewall rules), monitor logs and network traffic for suspicious access, and investigate/rotate exposed credentials. (Vendor guidance + CISA advisory recommend patching and remediation steps.)
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is adversarial content placed on the public web (or dynamically constructed in-browser) that aims to influence AI agents which browse or ingest that content, causing them to follow malicious instructions. Attackers may assemble prompts at runtime (dynamic execution) and can chain IPI with product-specific vulnerabilities to escalate to command execution or data exfiltration (examples: zero-click IPI in Google Gemini and other CVEs referenced).
- **Affected Products:** Google Gemini, Microsoft Copilot Studio (ShareLeak / CVE-2026-21520), MS-Agent, EmailGPT service, and other AI agent platforms / agent-enabled applications (versions vary; some individual CVEs reference specific product versions).
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Researcher proof-of-concept demonstrations have been reported (e.g., Noma Labs’ GeminiJack zero-click discovery). The corpus does not show a widely distributed weaponized exploit, though public IPI payloads have been observed on websites.
- **Patch Available:** No single vendor patch applies to the Google blog’s IPI findings; Google published an advisory/analysis. Individual product CVEs referenced in the corpus have their own fixes (e.g., a chained vulnerability fixed in v1.3), but the advisory itself is guidance rather than a software patch.
- **Active Exploitation:** Yes — Google observed indirect prompt-injection payloads on public web sites and researcher reports show real-world IPI-based discoveries (e.g., Noma Labs’ GeminiJack zero-click in Google Gemini); media and vendor writeups also report IPI-related CVEs being identified in products.
- **Threat Actors:** None known
- **Mitigation:** Follow vendor guidance and hardening: monitor and block known IPI payloads on the public web, validate and restrict browsing/ingest sources, isolate model contexts and prompts, sanitize and filter external content, and apply product-specific patches when available.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when an attacker injects malicious instructions into external data or tools an LLM will consume while completing a user’s query, allowing the attacker to influence the LLM’s behavior even without direct user input.
- **Affected Products:** Gemini, Gemini in Google Workspace apps (Google Workspace)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) or weaponized exploit identified in the vendor advisory or the reporting examined.
- **Patch Available:** No single vendor "patch" — Google describes continuous, layered platform defenses and guidance (see vendor advisory and Workspace knowledge articles) rather than a one-off patch.
- **Active Exploitation:** Google has observed and reported indirect prompt injection attempts on the public web and notes an increase in malicious attempts; reporting describes attempts in the wild but does not attribute large-scale, named-actor exploitation in the vendor advisory.
- **Threat Actors:** None known
- **Mitigation:** Google recommends a layered, continuous defense for IPI: platform-side LLM hardening and runtime defenses, content provenance/validation and sanitization, monitoring and detection, and administrative/policy controls applied to Gemini and Gemini-in-Workspace. See vendor guidance for details.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt-injection + implementation flaw: a condition allowed code to be injected/intercepted into hxxps://gemini.google.com/app when that web app was loaded inside the privileged Gemini panel. Because the panel runs with elevated capabilities, injected code could perform privileged actions (access local files/directories, take screenshots, access camera/microphone, etc.).
- **Affected Products:** Google Chrome (Gemini "Live in Chrome" agentic panel — desktop builds fixed by the Chrome stable-channel update released in early January 2026)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit was published in the collected sources; Unit42 reproduced the issue and responsibly disclosed it to Google and Google fixed it prior to Unit42’s publication.
- **Patch Available:** Yes — Google issued a fix in early January 2026 (Chrome stable-channel update referenced by NVD; see Chrome stable-channel update advisory).
- **Active Exploitation:** No confirmed active exploitation reported in the collected sources; vendor fix was applied before public disclosure.
- **Threat Actors:** None known
- **Mitigation:** Apply the Chrome update; follow Google’s agentic-layered defenses: enable Safe Browsing/on-device AI, use Chrome’s User Alignment Critic, enforce Agent Origin Sets (origin gating), run the prompt-injection classifier, require confirmations for sensitive navigations/actions. For enterprises, restrict/monitor extensions and deploy browser protections (e.g., Prisma Browser, advanced URL/DNS filtering).
- **Vendor Advisory:** https://chromereleases.googleblog.com/2026/01/stable-channel-update-for-desktop.html

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** The blog post reports 2025 Android memory-safety metrics: (1) memory-safety vulnerabilities fell below 20% of total Android vulnerabilities; (2) Rust change density is ~0.2 memory-safety vulnerabilities per million lines of code vs ~1,000/MLOC for C/C++; (3) Rust changes have ~4x lower rollback rate and ~25% less time in code review; (~4% of Android Rust code is in unsafe blocks). The referenced CVE-2025-48530 is a linear buffer overflow in the CrabbyAVIF AVIF parser/decoder caused by incorrect bounds checks producing out-of-bounds accesses on NV12/YUV planes, alpha plane, Y plane, UV planes, and chroma width calculation. Scudo hardened allocator turned the OOB into a crash via guard pages, making it 'non-exploitable' and preventing it from reaching a public release. RCE is theoretically possible only when chained with other bugs.
- **Affected Products:** Android platform code (C, C++, Java, Kotlin, Rust — first-party and open source); CrabbyAVIF AVIF parser/decoder on Android 16 / Android 16.0 (CVE-2025-48530)
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/C:H/I:H/A:H
- **Exploit Available:** No public PoC or weaponized exploit known. The blog post states CVE-2025-48530 was 'non-exploitable' and 'never made it into a public release.' SentinelOne's vulnerability database confirms: 'no public exploit code currently available.' (Source: https://www.sentinelone.com/vulnerability-database/cve-2025-48530/)
- **Patch Available:** Yes. CVE-2025-48530 (CrabbyAVIF) was fixed in the Android Security Bulletin. Patch level 2025-11-01 (November 2025 bulletin: https://source.android.com/docs/security/bulletin/2025-11-01). CVE.org references the August 2025 bulletin as well (https://source.android.com/security/bulletin/2025-08-01).
- **Active Exploitation:** No confirmed in-the-wild exploitation. The blog post states CVE-2025-48530 was 'non-exploitable' and 'never made it into a public release.' SentinelOne reports 'Not known to be exploited.' (Source: https://www.sentinelone.com/vulnerability-database/cve-2025-48530/)
- **Threat Actors:** None known
- **Mitigation:** Google's primary strategy is: (1) continue shifting new Android platform code to Rust; (2) rely on memory-safety-hardened allocators like Scudo with guard pages that turn OOB writes into crashes. For the specific CVE-2025-48530 (CrabbyAVIF), the patch was delivered in Android Security Bulletin November 2025 (patch level 2025-11-01). Developers should treat bounds-checking failures in image parsers as high-priority fixes.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection hides malicious instructions inside external data sources (web pages, documents, emails, calendar invites, retrieval results) that are fetched or included in an LLM/agent context; when the model processes that content it can follow the hidden instructions (e.g., exfiltrate data or perform unauthorized actions).
- **Affected Products:** Google Gemini, LLM-based generative AI services and integrations (browsing/agents/connectors) — no specific product/version list available
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoCs and payload collections have been reported (research PoCs / payload repositories and industry write-ups describe PoCs and payloads).
- **Patch Available:** No vendor patch was published; Google published guidance and a layered defense strategy instead (see advisory URL).
- **Active Exploitation:** Yes — industry reporting indicates indirect prompt injection payloads/techniques have been observed in the wild.
- **Threat Actors:** None known
- **Mitigation:** Use a layered defense: retrieval scoping and filters, intent-aware input inspection, input/output sanitization and validation, isolation/sandboxing of retrieved content, provenance/authentication of sources, avoid placing sensitive data in model contexts, human-in-the-loop for sensitive actions, and keep LLMs out of critical control loops.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors exploit publicly known CVEs in edge network devices for initial access (no zero-day exploitation observed in this advisory), then modify router configurations for persistence (adding ACL entries that allow actor IPs), create privileged accounts, alter TACACS+/AAA and SNMP settings to capture credentials or persist, enable native packet-capture or mirror traffic (SPAN/RSPAN/ERSPAN) for collection, and establish persistent GRE/IPsec tunnels for covert communications and exfiltration.
- **Affected Products:** Ivanti Connect Secure / Policy Secure (9.x, 22.x) (CVE-2024-21887), Palo Alto Networks PAN-OS GlobalProtect (PAN-OS 10.2/11.0/11.1; fixed in 10.2.9-h1, 11.0.4-h1, 11.1.2-h3) (CVE-2024-3400), Cisco IOS XE Web UI (CVE-2023-20198, CVE-2023-20273; first-fixed trains 17.9.4a, 17.6.6a, 17.3.8a, 16.12.10a), Cisco IOS/IOS XE Smart Install (CVE-2018-0171); (other potential targets named: Fortinet, Juniper, Microsoft Exchange, Nokia routers/switches, Sierra Wireless, SonicWall)
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — CISA and associated vendor/industry reporting confirm active exploitation of multiple publicly known CVEs (see KEV/vendor advisories). The advisory and industry write-ups do not publish a single consolidated public PoC URL for a weaponized exploit in the advisory corpus reviewed.
- **Patch Available:** Yes — vendors have released fixes/hotfixes for the specific affected products (Cisco IOS XE first-fixed trains, Palo Alto PAN-OS hotfix releases, Ivanti patches). See vendor advisories (Cisco, Palo Alto Networks, Ivanti) and CISA/KEV guidance for exact patched versions.
- **Active Exploitation:** Confirmed — the advisory and Appendix B list multiple CVEs that have been exploited in the wild and CISA directs prioritizing remediation via the Known Exploited Vulnerabilities (KEV) catalog; vendor advisories and industry reporting corroborate exploitation of several listed CVEs.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize KEV-listed patches; harden and limit internet-facing management surfaces; restrict/disable Smart Install and unused management services; enforce MFA and phishing-resistant authentication, network segmentation/zero-trust for provider/edge networks; monitor router configs, ACLs, TACACS+/AAA changes, Embedded Packet Capture/PCAP files, and unusual GRE/IPsec tunnels; follow vendor-specific hardening guidance.
- **Vendor Advisory:** https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxe-webui-privesc-j22SaA4z, https://security.paloaltonetworks.com/CVE-2024-3400/, https://www.ivanti.com/blog/security-update-for-ivanti-connect-secure-and-ivanti-policy-secure-gateways

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Campaign-level cyber espionage activity: Russian GRU operators have targeted Western logistics entities and technology companies involved in coordination, transport, and delivery of foreign assistance to Ukraine. The provided corpus describes actor and sector targeting (campaign context) rather than a single CVE or exploit chain; granular IOCs/TTP lists are not present in the extracted segments.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) or weaponized exploit is indicated in the advisory corpus for a specific software vulnerability.
- **Patch Available:** Patch not applicable / no vendor patch indicated (this is a campaign advisory, not a vendor-disclosed vulnerability).
- **Active Exploitation:** Yes — multiple government advisories report an ongoing Russian state-sponsored campaign actively targeting Western logistics entities and technology companies (reported since 2022). Sources: CISA joint advisory and corroborating FBI / national CERT advisories.
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU), 85th Main Special Service Center (85th GTsSS), military unit 26165; tracked in reporting under names including APT-28 / GRU-associated groups.
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

**Parallel AI Enrichment:**

- **Technical Details:** Pre-auth OS command-injection in Ivanti Sentry that allows a remote, unauthenticated attacker to execute operating-system commands and achieve remote code execution / full control of the appliance, enabling configuration changes, credential theft, data access, and lateral movement.
- **Affected Products:** Ivanti Sentry — versions before R10.5.2, R10.6.2 and R10.7.1
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — public proof-of‑concept (PoC) published (e.g., WatchTowr analysis and GitHub PoC repo).
- **Patch Available:** Yes — Ivanti released updates (fixed in R10.5.2, R10.6.2 and R10.7.1); see vendor advisory: https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523?language=en_US
- **Active Exploitation:** Confirmed — multiple reports (Shadowserver, CISA Known Exploited Vulnerabilities listing, independent incident reports) document active exploitation in the wild following PoC disclosure.
- **Threat Actors:** None known
- **Mitigation:** Upgrade immediately to the patched R10.5.2 / R10.6.2 / R10.7.1 releases; until patched, isolate or remove exposed Sentry appliances from the public internet and restrict network access to management interfaces per vendor guidance.
- **Vendor Advisory:** https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523?language=en_US

---

## 11. 🟠 Zero-Day — Microsoft Removes 119 Edge Extensions That Hid Malware in Images and Fonts

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-29
**Reference:** <https://thehackernews.com/2026/06/microsoft-removes-119-edge-extensions.html>

> Microsoft has shut down a long-running malicious extension operation on the Edge Add-ons store that hid its payloads inside ordinary image and font files, then woke up days after install to steal credentials and run ad fraud.

The company calls it StegoAd, a mash-up of steganography and adware, and ties 119 extensions to a single threat actor it says has been active since at least 2021.

---

## 12. 🟡 High Severity — Critical SimpleHelp flaw exploited to deploy new stealer malware

**CVE:** `CVE-2026-48558` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-29
**Reference:** <https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-simplehelp-flaw-deploy-new-djinn-infostealer-taskweaver-malware/>

> Hackers are exploiting a recently disclosed critical vulnerability (CVE-2026-48558) in SimpleHelp to deploy Djinn Stealer, a previously undocumented cross-platform information stealer targeting Windows, macOS, and Linux. [...]

---

## 13. 🟡 High Severity — Hackers now exploit critical Oracle E-Business flaw in attacks

**CVE:** `CVE-2026-46817` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-29
**Reference:** <https://www.bleepingcomputer.com/news/security/new-oracle-e-business-suite-flaw-now-exploited-in-attacks/>

> Attackers have begun exploiting a critical vulnerability (CVE-2026-46817) in the Oracle E-Business Suite (EBS) financial application, according to threat intelligence company Defused. [...]

---

## 14. 🟡 High Severity — Public PoC Released for Critical libssh2 CVE-2026-55200 Client-Side SSH Flaw

**CVE:** `CVE-2026-55200` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-29
**Reference:** <https://thehackernews.com/2026/06/public-poc-released-for-critical.html>

> A public proof-of-concept is now out for CVE-2026-55200, a critical flaw in libssh2 that lets a malicious or compromised SSH server trigger memory corruption on a connecting client, with possible code execution. No credentials, no user interaction. The bug affects every release up to and including 1.11.1 and carries a CVSS 4.0 score of 9.2.

libssh2 is a client-side SSH library, not a server.

---

## 15. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
