# Zero Day Pulse

> **Generated:** 2026-06-20 13:24 UTC &nbsp;|&nbsp; **Total:** 33 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 23 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is a path traversal flaw that lets unauthenticated remote attackers craft HTTP requests with manipulated file‑path parameters to read arbitrary files (e.g., /etc/passwd) from the SimpleHelp host.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) / SimpleHelp remote support software versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Public PoC and a Metasploit auxiliary module (auxiliary/scanner/http/simplehelp_toolbox_path_traversal) are available.
- **Patch Available:** Yes. SimpleHelp has released patches; see Broadcom security bulletin.
- **Active Exploitation:** Confirmed. CISA reports ransomware actors have leveraged CVE‑2024‑57727 since January 2025, and the vulnerability is listed in the CISA Known Exploited Vulnerabilities catalog.
- **Threat Actors:** Ransomware actors (e.g., DragonForce) have been reported exploiting this vulnerability.
- **Mitigation:** Isolate or unplug vulnerable SimpleHelp servers, stop the server process, upgrade immediately to the latest version, restrict file‑browsing functionality, limit network access to the management interface, and conduct threat‑hunting and monitoring.
- **Vendor Advisory:** https://simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — In Other News: Apple Patches Beats Eavesdropping Flaw, DOT Closes Delta CrowdStrike Probe, AWS Continuum

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://www.securityweek.com/in-other-news-apple-patches-beats-eavesdropping-flaw-dot-closes-delta-crowdstrike-probe-aws-continuum/>

> Other noteworthy stories that might have slipped under the radar: Android TV botnet Popa linked to Israeli firm, Velvet Ant maintained decade-long stealth, unpatched GCP Config Connector flaw enables takeover. The post In Other News: Apple Patches Beats Eavesdropping Flaw, DOT Closes Delta CrowdStrike Probe, AWS Continuum appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Vulnerability (CVE-2025-20701) is an incorrect authorization in the Airoha Bluetooth audio SDK that can allow pairing of a Bluetooth audio device without user consent, permitting nearby attackers to pair and potentially access microphone audio.
- **Affected Products:** Beats Studio Buds (firmware 1B211), Airoha Bluetooth audio SDK
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** None known
- **Patch Available:** Beats Firmware Update 1B211 (released June 16, 2026) – available via Apple Support page.
- **Active Exploitation:** No confirmed reports of active exploitation in the wild.
- **Threat Actors:** None known
- **Mitigation:** Install Beats Firmware Update 1B211 via a paired iPhone/Apple device; avoid pairing with unknown devices; disable Bluetooth when not in use.
- **Vendor Advisory:** https://support.apple.com/en-us/127557

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an attack vector in which an adversary plants adversarial instructions inside content an AI agent subsequently ingests (web pages, search results, documents, image metadata, GitHub comments, etc.), exploiting the inability of current LLMs to maintain a strict data-vs-instruction boundary. Google Threat Intelligence, scanning Common Crawl archives, classified observed web-borne IPI into six categories: (1) harmless pranks altering agent conversational tone, (2) author-controlled helpful guidance enriching AI summaries, (3) SEO/business promotion pushing commercial content, (4) deterring AI agents with 'If you are an AI, do not crawl this site' tokens and infinite-text streamers causing retrieval timeouts, (5) malicious exfiltration instructions attempting to extract user data, and (6) malicious destruction commands telling the agent to delete files or vandalize the host machine. Forcepoint observed real payloads using HTML comments, CSS invisibility (display:none, 1px-font, transparent colors, aria-hidden/visually-hidden classes), meta-tag 'ai:action' namespaces, role/authority impersonation, system-prompt tag spoofing, magic-string spoofing (e.g., ANTHROPIC_MAGIC_STRING_TRIGGER_REFUSAL_), and terminal command injection (e.g., sudo rm -rf).
- **Affected Products:** Google Gemini and Gemini in Workspace (Gmail, Docs, Drive, Chat); secondarily, agentic AI products broadly including GitHub Copilot, Cursor, Claude Code, AI-powered CI/CD reviewers, and other LLM-driven browser/agent assistants that ingest untrusted web data. Specific patched versions are not enumerated because IPI is a class-level vulnerability of LLMs.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes - multiple public exploit artifacts exist. (1) Forcepoint X-Labs disclosed 10 verified in-the-wild IPI payload indicators with affected target URLs on April 22, 2026 (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads). (2) Google links to prior PoC repositories at https://greshake.github.io/ and https://swisskyrepo.github.io/PayloadsAllTheThings/Prompt%20Injection/. (3) Related weaponized IPI exploits have been published for Google Antigravity (Pillar Security, RCE/sandbox escape, patched Feb 28, 2026) and Microsoft Copilot Studio (ShareLeak/CVE-2026-21520).
- **Patch Available:** There is no single vendor patch closing Indirect Prompt Injection as a vulnerability class; AI vendors address it through layered model and platform mitigations rather than a CVE-style patch. Google's hardening of Gemini is delivered via continuous model updates and the Workspace-side layered defenses. A related, separately patched flaw is the Google Antigravity IDE sandbox-escape/RCE disclosed Jan 7, 2026 by Pillar Security and patched Feb 28, 2026 (https://www.pillar.security/blog/prompt-injection-leads-to-rce-and-sandbox-escape-in-antigravity; https://thehackernews.com/2026/04/google-patches-antigravity-ide-flaw.html).
- **Active Exploitation:** Yes - confirmed active exploitation observed in the wild. Google's Threat Intelligence team reported 'a relative increase of 32% in the malicious category between November 2025 and February 2026, repeating the scan on multiple versions of the archive.' Independently, Forcepoint X-Labs documented 10 real-world IPI payloads active on public websites on April 22, 2026 (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads), corroborated by helpnetsecurity (Apr 24, 2026), infosecurity-magazine (Apr 23, 2026), Slashdot (Apr 26, 2026), and SecurityWeek. Sources: http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html ; https://www.helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild/ ; https://it.slashdot.org/story/26/04/26/2345211/google-studies-prompt-injection-attacks-against-ai-agents-browsing-the-web.
- **Threat Actors:** None known
- **Mitigation:** Because IPI is a class-level weakness, Google recommends a layered defense-in-depth strategy for Gemini (https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini): (1) prompt-injection content classifiers flagging suspicious inputs across modalities; (2) security thought reinforcement adding targeted system-level instructions that bias the model to follow user intent over adversarial content; (3) markdown sanitization and suspicious-URL redaction via Google Safe Browsing; (4) human-in-the-loop user confirmation framework for high-risk side-effects (e.g., deleting calendar events); (5) end-user security-mitigation notifications when a risk is detected and neutralized; (6) base-model adversarial-robustness hardening. General hardening advice includes dedicated red teams pressure-testing agents, participation in Google's AI Vulnerability Reward Program (https://bughunters.google.com/about/rules/google-friends/ai-vulnerability-reward-program-rules), strict data-instruction boundaries enforced at the application layer, treating all fetched web content as untrusted, and segregating agent privilege scopes so that browsing tools cannot reach destructive actions like sudo rm -rf without explicit user consent.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) embeds malicious instructions inside data (emails, documents, calendar entries, web pages, tool-call responses) that an LLM ingests to fulfill a user query. Because the LLM treats retrieved content as legitimate context, the injected instructions can hijack model behavior — repurposing a chatbot, coercing a summarizer to perform unauthorized actions (e.g., sending emails), exfiltrating confidential data to attacker-controlled endpoints, or impersonating the user. Variant attacks can succeed without any direct user input (zero-click, e.g., GeminiJack). For Workspace-with-Gemini, Google describes three harmful patterns: chatbot hijack leaking sensitive internal info; summarizer compromise performing unauthorized actions (e.g., sending emails); and data exfiltration of confidential documents to attacker-controlled destinations.
- **Affected Products:** Google Workspace with Gemini (Gmail, Docs editors, Drive, Chat), Gemini app, Gemini Enterprise, Vertex AI Search
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — multiple public PoCs and weaponized IPI payloads exist for Gemini-family products. Key sources: https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability ; https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads ; https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/ ; http://oddguan.com/blog/comment-and-control-prompt-injection-credential-theft-claude-code-gemini-cli-github-copilot
- **Patch Available:** No discrete patch — Google describes a continuously deployed, layered defense strategy rather than a single patchable vulnerability. The advisory blog post itself is the disclosure: https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/
- **Active Exploitation:** Yes — IPI attacks are being observed in the wild against the broader class of LLM-integrated applications (Google reports a 32% relative increase in malicious IPI attempts between Nov 2025 and Feb 2026; Forcepoint X-Labs harvested 10 distinct in-the-wild payloads). However, no public report (as of June 2026) attributes Workspace-with-Gemini-specific IPI exploitation to a named threat actor. Sources: https://blog.google/security/prompt-injections-web/ and https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads
- **Threat Actors:** None known
- **Mitigation:** Google's multi-layer defense strategy (no single patch; continuously deployed): (1) Pre-deployment red-teaming + AI Vulnerability Rewards Program ingesting external vulnerability findings; (2) Open-source intelligence feeds and a vulnerability catalog feeding model/card updates; (3) Deterministic defenses: centralized Policy Engine enforcing user confirmation, URL sanitization/link rewriting, tool-chaining policies, and regex takedown of known-bad URLs; (4) ML-based defenses: classifiers trained on synthetic IPI data; (5) LLM-based defenses: refined system prompts and security thought reinforcement; (6) Output-layer markdown sanitization and suspicious-URL redaction; (7) End-user mitigation notifications when Gemini surfaces content that appears crafted to manipulate it; (8) Model resilience/hardening to intrinsically identify and ignore harmful instructions; (9) Admin guidance treating IPI as an evolving class — user training, input/output validation, and human-in-the-loop review are recommended. See https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini .
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is an indirect prompt injection attack: malicious web content can influence the prompts sent to the Gemini agent, causing the agentic browser to perform unintended actions or disclose sensitive data. The vendor mitigates this via layered defenses such as prompt sanitization, origin restrictions, and a User Alignment Critic that validates agent plans against policy.
- **Affected Products:** Google Chrome (agentic/Gemini-enabled builds) – versions prior to 1.3 Metrics
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unavailable.
- **Patch Available:** Fixed in Chrome version 1.3 Metrics (see NVD).
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Implement layered defenses including prompt sanitization, origin restrictions, and the User Alignment Critic to validate agent actions.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** The post is a strategic/program-level update, not a per-CVE advisory. Key quantitative findings for 2025 data (covering first- and third-party AOSP changes in C, C++, Java, Kotlin, and Rust): memory-safety vulnerabilities fell below 20% of total vulnerabilities for the first time; ~0.2 memory-safety vulnerabilities per million lines of Rust code in Android versus roughly 1,000 memory-safety vulnerabilities per MLOC for legacy C/C++ (~1000x density reduction); Rust changes have ~4x lower rollback rate for medium/large changes than C++; Rust changes spend ~25% less time in code review; need ~20% fewer revisions; ~4% of Rust code lives inside unsafe{} blocks. Example vulnerability: CVE-2025-48530 (Android bug A-419563680) — incorrect bounds checks in multiple locations of CrabbyAVIF leading to out-of-bounds accesses that could enable remote code execution without additional privileges or user interaction.
- **Affected Products:** Android platform (first-party and third-party/open-source code changes) across C, C++, Java, Kotlin, and Rust. Specifically mentioned components: CrabbyAVIF (Rust-based AVIF image decoder in AOSP), Scudo hardened allocator, and Google Pixel devices shipping the resulting image stack.
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept. The single referenced vulnerability (CVE-2025-48530, an out-of-bounds access in CrabbyAVIF classed as RCE/Critical) was found and fixed before reaching any public Android release.
- **Patch Available:** Patch is available for the single example CVE (CVE-2025-48530) but there is no new patch drop tied to this blog post. CVE-2025-48530 was fixed ahead of public release and is documented in Android Security Bulletin 2025-08-01 (patch level 2025-08-01, published 2025-08-04) via commits in external/rust/crabbyavif.
- **Active Exploitation:** No confirmed exploitation in the wild. The blog explicitly states the CrabbyAVIF vulnerability (CVE-2025-48530) 'never made it into a public release,' and neither the Google Security Blog post nor the LWN coverage references any in-the-wild exploitation.
- **Threat Actors:** None known. The only concrete vulnerability called out (CVE-2025-48530 in CrabbyAVIF) was fixed before reaching public release; no threat actor activity is associated with the broader Rust adoption trend or the example bug.
- **Mitigation:** Vendor's recommended hardening (no traditional patch is being issued — this is a program-level update): (1) Write new platform code in Rust to prevent memory-safety bugs by construction; (2) Make the Scudo hardened allocator mandatory for additional allocation-level defenses; (3) Extend Google's Comprehensive Rust training with a new deep dive on unsafe Rust covering soundness, undefined behavior, safety comments, and encapsulating unsafe code in safe abstractions; (4) Treat existing unsafe-Rust and legacy C/C++ as residual risk and continue migrating to memory-safe language modules.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** The flaw is an OS command injection in the MobileIron Configuration Service (MICS) web portal of Ivanti Sentry, allowing crafted input to be executed as system commands on the server.
- **Affected Products:** Ivanti Sentry (MobileIron Configuration Service)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit or PoC is referenced in the provided sources.
- **Patch Available:** No official vendor patch is referenced in the provided sources.
- **Active Exploitation:** Confirmed active exploitation in the wild, reported by Shadowserver Foundation (June 10, 2026).
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** The actors gain initial access by exploiting publicly known CVEs in edge/network devices (CVE-2023-20198 and CVE-2023-20273 in Cisco IOS XE Web UI; CVE-2018-0171 in Cisco Smart Install; CVE-2024-21887 and CVE-2023-46805 in Ivanti Connect Secure; CVE-2024-3400 in Palo Alto Networks PAN-OS GlobalProtect) and abusing features like Smart Install and GuestShell. After gaining access, they pivot from compromised edge devices and trusted provider interconnections into backbone/PE/CE routers. Persistence is achieved by modifying device configurations: enabling GRE/IPsec tunnels and static routes to attacker-controlled infrastructure; activating SPAN/RSPAN/ERSPAN traffic mirroring; inserting/modifying ACLs (frequently named 'access-list 20/50/10') to allow attacker IP ranges; altering TACACS+/RADIUS/AAA to redirect authentication to attacker servers; deploying Linux containers (e.g., GuestShell) on network devices; and using non-standard SSH service ports (e.g., 22x22).
- **Affected Products:** Cisco IOS XE Software versions 16.0.x through 17.9.x (web UI - CVE-2023-20198); Cisco IOS/IOS XE Smart Install client (CVE-2018-0171); Palo Alto Networks PAN-OS versions 10.2, 11.0, 11.1 GlobalProtect feature (CVE-2024-3400); Ivanti Connect Secure 9.x and 22.x (CVE-2024-21887, CVE-2023-46805); Ivanti Policy Secure (CVE-2024-21887); Large backbone/PE/CE routers of major telecommunications providers.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — public PoCs and weaponized exploits are available: CVE-2023-20198 PoC at https://github.com/smokeintheshell/CVE-2023-20198; Horizon3.ai deep-dive and PoC at https://horizon3.ai/attack-research/attack-blogs/cisco-ios-xe-cve-2023-20198-deep-dive-and-poc/; OPSWAT write-up at http://opswat.com/blog/cve-2023-20198-cve-2023-20273-from-unauthenticated-web-request-to-root-on-ios-xe; Open-source `siet.py` for Cisco Smart Install (CVE-2018-0171).
- **Patch Available:** Yes — patches available for all referenced CVEs. Cisco IOS XE Web UI (CVE-2023-20198): upgrade to 17.9.4a, 17.6.6a, 17.3.8a, or 16.12.10a (see https://www.cisa.gov/guidance-addressing-cisco-ios-xe-web-ui-vulnerabilities). Cisco Smart Install (CVE-2018-0171): disable feature. Palo Alto PAN-OS GlobalProtect (CVE-2024-3400): upgrade to 10.2.9-h1, 11.0.4-h1, 11.1.2-h3 or later (https://security.paloaltonetworks.com/CVE-2024-3400). Ivanti Connect Secure / Policy Secure (CVE-2024-21887, CVE-2023-46805): apply latest 9.x and 22.x patches and run vendor integrity-check tooling.
- **Active Exploitation:** Yes — confirmed active exploitation in the wild. CISA, NSA, FBI and international partners published the advisory because of observed long-running, ongoing intrusions. Corroborating reports: Trend Micro (November 2024) on Salt Typhoon; Cisco Talos (February 2025); ESET (March 2025) on activity affecting a U.S.-based trade group. CVE-2023-20198 was added to CISA's Known Exploited Vulnerabilities Catalog on October 16, 2023. Actors have maintained long-term persistent access to telecom backbone and edge routers globally.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor (PRC state-sponsored threat actors). Specific PRC entities: Sichuan Juxinhe Network Technology Co., Ltd.; Beijing Huanyu Tianqiong Information Technology Co., Ltd.; Sichuan Zhixin Ruijie Network Technology Co., Ltd. (linked to PLA and MSS).
- **Mitigation:** Configuration audits: compare running router/network-device configurations against last-known-good/authorized baselines with change control. Hunt for IOCs: unexpected GRE/IPsec tunnels toward foreign infrastructure; unauthorized external IPs configured as TACACS+/RADIUS servers; unexpected external IPs in ACLs (especially in 'access-list 20/50/10'); unexpected SPAN/RSPAN/ERSPAN packet captures; virtual Linux containers running on network devices. Segregate management: place SSH, HTTPS, SNMP, TACACS+, and RADIUS into out-of-band networks or dedicated management VRFs; apply Control-Plane Policing (CoPP). Restrict/disable exposed services: disable Cisco IOS XE HTTP/HTTPS server if not required ('no ip http server' / 'no ip http secure-server'); disable Smart Install and block TCP/4786; disable GuestShell where not operationally required. Apply vendor patches (see patch_available) and prioritize updates per CISA's Known Exploited Vulnerabilities Catalog. Review remote-access configurations (ACLs, transport protocols) for accuracy and least privilege. Review supply-chain trust relationships. Apply vendor patches.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

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
- **Exploit Available:** No public exploit is known.
- **Patch Available:** No official patch is available.
- **Active Exploitation:** Yes, active exploitation has been reported.
- **Threat Actors:** Russian GRU 85th Main Special Service Center (Unit 26165), APT28, Fancy Bear, Forest Blizzard
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** Reflected XSS in Outlook Web Access caused by improper neutralization of user‑supplied input during web page generation; exploitation involves sending a specially crafted email that, when opened in OWA under certain interaction conditions, can execute arbitrary JavaScript in the victim's browser.
- **Affected Products:** Exchange Server 2016 (any update level), Exchange Server 2019 (any update level), Exchange Server Subscription Edition (SE) (any update level)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept is available.
- **Patch Available:** https://techcommunity.microsoft.com/blog/exchange/released-june-2026-exchange-server-security-updates/4524491
- **Active Exploitation:** Confirmed active exploitation – sources: Microsoft Exchange Team blog (May 14, 2026 update) and CISA Known Exploited Vulnerabilities Catalog (added 2026-05-15).
- **Threat Actors:** None known
- **Mitigation:** Use the Exchange Emergency Mitigation (EM) Service or run the scripted EOMT.ps1 command (e.g., .\EOMT.ps1 -CVE "CVE-2026-42897").
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42897

---

## 11. 🟡 High Severity — Hackers Exploit Gravity SMTP WordPress Plugin Bug to Expose API Keys

**CVE:** `CVE-2026-4020` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-20
**Reference:** <https://thehackernews.com/2026/06/hackers-exploit-gravity-smtp-wordpress.html>

> Threat actors are exploiting a recently patched security flaw impacting Gravity SMTP, a WordPress plugin that&#x27;s installed on about 100,000 sites.

The vulnerability, tracked as CVE-2026-4020 (CVSS score: 5.3), is a medium-severity information disclosure flaw that can allow unauthenticated attackers to extract sensitive data, such as configuration data, API keys, secrets, and OAuth tokens

---

## 12. 🟡 High Severity — symfony/ux-icons: XSS via unsanitized SVG content in local files and Iconify on-demand responses

**CVE:** `CVE-2026-55877` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-6v8j-33hc-mv84>

> ### Description

The `ux_icon()` Twig function is marked `is_safe=[&#x27;html&#x27;]`, so Twig never escapes its output. `Icon::toHtml()` inlines the SVG source verbatim into the page. Browsers execute `&lt;script&gt;` elements and `on*` event-handler attributes found inside inline SVG, making any unsanitized icon a vector for cross-site scripting.

Two code paths were affected. In the local file …

---

## 13. 🟡 High Severity — OpenBao: Transit secrets engine crashes on key creation with `derived: true` for asymmetric key types

**CVE:** `CVE-2026-55776` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-8w8f-r2xv-4q4j>

> On OpenBao 2.5.4 and 2.5.2(and likely earlier versions also), an authenticated caller with write access to `transit/keys/*` can crash the OpenBao server by issuing a single key-creation request that combines an asymmetric `type` (`rsa-*`, `ecdsa-*`, `ed25519`)
with `derived: true`. The server returns no HTTP response and the process terminates (exit code 2). This is a remote, low-complexity denial…

---

## 14. 🟡 High Severity — OpenBao: Cross-namespace lease revocation/renewal via canonical sys/leases/{revoke,renew} — incomplete fix of CVE-2026-45808

**CVE:** `CVE-2026-55774` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-c36x-h252-g9x2>

> ### Summary

OpenBao users with access to the `sys/leases/revoke/:lease_id` endpoint in any namespace can revoke leases in any other namespace as long as the lease identifier is known to them, bypassing ACLs that should apply for cross-namespace revocations.

### Impact

OpenBao&#x27;s namespaces provide multi-tenant separation. A tenant who intentionally leaks lease identifiers can have their lea…

---

## 15. 🟡 High Severity — OpenBao: LDAPi ldaputil (wrong escape func)

**CVE:** `CVE-2026-55770` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-6mwx-4547-5vc9>

> ## 1. Description

### Component

`sdk/helper/ldaputil/client.go` — the shared LDAP utility library used by both the LDAP authentication backend and OpenLDAP secrets engine to construct LDAP search filters and bind DNs.

### Root Cause

The LDAP utility contains a **function selection error** that causes incorrect escaping of user-controlled input in LDAP filter construction. Two lines construct t…

---

## 16. 🟡 High Severity — StarCitizenWiki Extension Embed Video: Stored XSS via malformed src url with $wgEmbedVideoRequireConsent enabled

**CVE:** `CVE-2026-55692` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-5c7p-g73q-rpg5>

> ### Summary
With $wgEmbedVideoRequireConsent enabled (the default), the urls for videos are stored in a json-ified data attribute`data-mw-iframeconfig`. When given a malformed url or id, the data-mw-iframeconfig attribute can be escaped via single quotes, allowing for html/javascript injection.

### Details
The sprintf [here](https://github.com/StarCitizenWiki/mediawiki-extensions-EmbedVideo/blob/…

---

## 17. 🟡 High Severity — Langflow: BaseFileComponent-based nodes arbitrary file read with RCE exploit

**CVE:** `CVE-2026-55447` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-ccv6-r384-xp75>

> ### Summary
All components based on `BaseFileComponent` are vulnerable to the following vulnerability:
1. Docling (`DoclingInlineComponent`)
2. Docling Serve (`DoclingRemoteComponent`)
3. Read File (`FileComponent`)
4. NVIDIA Retriever Extraction (`NvidiaIngestComponent`)
5. Video File (`VideoFileComponent`)
6. Unstructured API (`UnstructuredComponent`)

For clarity, from now on I&#x27;ll only ref…

---

## 18. 🟡 High Severity — Langflow: Unauthenticated DoS through multipart form boundary file upload

**CVE:** `CVE-2026-55446` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-qwqc-p3q8-wcg9>

> ### Summary
An attacker can send a `/api/v1/files/upload/` request without any authentication token/cookies and abuse a very long multipart form boundary to make the langflow app unusable for all users for an indefinite amount of time. 

### Details
https://github.com/langflow-ai/langflow/blob/v1.0.18/src/backend/base/langflow/api/v1/files.py#L40

The file upload function will try to process the m…

---

## 19. 🟡 High Severity — Langflow: Logout button does not clear session

**CVE:** `CVE-2026-55423` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-7hw8-6q6r-4276>

> ### Summary
The logout button does not clear the session. The previous user stays logged in unless another user explicitly logs in.

### Details
Not in auto login mode. Hosted on localhost. `access_token_lf` remains present in both Local Storage and Cookies. `refresh_token_lf` remains present in Cookies.

**Root cause:** the `/logout` endpoint deleted the authentication cookies without matching th…

---

## 20. 🟡 High Severity — Mailpit: Incomplete SSRF protection in Link Check API via IPv6 transition mechanisms

**CVE:** `CVE-2026-55187` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-w4mc-hhc6-xp28>

> ## Summary

The remediation shipped in mailpit v1.29.2 for [GHSA-mpf7-p9x7-96r3](https://github.com/axllent/mailpit/security/advisories/GHSA-mpf7-p9x7-96r3) (CVE-2026-27808) is incomplete. The `tools.IsInternalIP` deny-list relies on Go&#x27;s stdlib classification helpers (`IsLoopback`, `IsPrivate`, `IsLinkLocalUnicast`, `IsLinkLocalMulticast`, `IsUnspecified`, `IsMulticast`) plus an inline CGNAT…

---

## 21. 🟡 High Severity — Traefik Kubernetes Ingress NGINX provider fails open when auth-secret resolution fails

**CVE:** `CVE-2026-54762` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-4mr2-fg2p-w63c>

> ## Summary

There is a medium severity vulnerability in Traefik&#x27;s Kubernetes Ingress NGINX provider that causes affected routes to fail open. When an Ingress explicitly enables BasicAuth or DigestAuth through the supported `nginx.ingress.kubernetes.io/auth-type` and `auth-secret` annotations, but the referenced auth Secret cannot be resolved or parsed, Traefik logs the resolution error, skips…

---

## 22. 🟡 High Severity — dbt MCP Server: Unauthenticated OAuth Context Endpoint Leaks dbt Platform Tokens

**CVE:** `CVE-2026-55837` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-jr33-mw75-7j8f>

> ## Unauthenticated OAuth Context Endpoint Leaks dbt Platform Tokens

### Summary

The local OAuth helper FastAPI server bundled with `dbt-mcp` exposes the `GET /dbt_platform_context` endpoint without any form of authentication or host-origin validation. After a user completes the OAuth login flow against dbt Cloud (cloud.getdbt.com), the endpoint returns the full `DbtPlatformContext` object — incl…

---

## 23. 🟡 High Severity — Craft CMS: Blind SSRF and Arbitrary JavaScript Injection via Host Header Poisoning in actionResourceJs

**CVE:** `CVE-2026-55791` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-c55v-343g-5xff>

> **1. Overview**

Craft CMS is vulnerable to Server-Side Request Forgery (SSRF) and Arbitrary JavaScript Injection through the `/actions/app/resource-js` endpoint. By exploiting the default permissive `trustedHosts` configuration, an attacker can poison the `Host` or `X-Forwarded-Host` header to manipulate the application’s `$baseUrl`. This bypasses the endpoint’s internal URL validation, forcing t…

---

## 24. 🟡 High Severity — @tinacms/cli: Remote Code Execution in @tinacms/cli via Forestry migration — unsanitised __TINA_INTERNAL__ marker in user-controlled YAML labels

**CVE:** `CVE-2026-54074` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-4936-9hrh-qqpw>

> ## Description

### Summary

`@tinacms/cli` contains a Remote Code Execution vulnerability in its
Forestry-to-Tina migration command. The internal helper `addVariablesToCode`
unquotes any value matching the marker `&quot;__TINA_INTERNAL__:::(.*?):::&quot;`
inside the stringified collection JSON. User-supplied `label` and `name`
fields from `.forestry/**/*.yml` are placed into that JSON without any…

---

## 25. 🟡 High Severity — Grafana Operator: Privilege escalation from namespace admin to cluster admin via GrafanaDashboard jsonnetLib fileName

**CVE:** `CVE-2026-11769` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-fcw4-wwqm-m8cf>

> We have released version 5.24.0 of the Grafana Operator. This patch includes a MODERATE severity security fix for a path traversal/privilege escalation vulnerability in the Grafana Operator.


### Summary

The Grafana Operator supports loading dashboards &amp; library panels using the jsonnet data templating language. The jsonnet expression is evaluated in the context of the operator manager pod.
…

---

## 26. 🟡 High Severity — @cyclonedx/cyclonedx-npm: Shell Injection via Unsanitized --workspace Argument

**CVE:** `CVE-2026-55849` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-v75r-vx73-82pj>

> ## Summary
A command injection vulnerability exists in `@cyclonedx/cyclonedx-npm` when the CLI is invoked with the `--workspace &lt;value&gt;` option while the environment variable `npm_execpath` is unset or empty.  
User‑supplied `--workspace` values are passed to a subshell without proper sanitization, enabling attackers to inject arbitrary OS commands.  
This issue corresponds to **CWE‑78**: Im…

---

## 27. 🟡 High Severity — Concurrent Ruby: ReadWriteLock allows wrong-thread write release and stray read-release counter corruption

**CVE:** `CVE-2026-54906` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-6wx8-w4f5-wwcr>

> ### Summary
`Concurrent::ReadWriteLock#release_write_lock` does not verify that the calling thread acquired the write lock. Any thread with access to the lock object can release an active write lock held by another thread. A second writer can then enter its critical section while the first writer is still running.

`Concurrent::ReadWriteLock#release_read_lock` also decrements the shared counter ev…

---

## 28. 🟡 High Severity — Concurrent Ruby: `ReentrantReadWriteLock` read-count overflow grants a write lock without exclusivity

**CVE:** `CVE-2026-54905` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-wv3x-4vxv-whpp>

> ### Summary
`Concurrent::ReentrantReadWriteLock` can incorrectly grant a write lock after one thread acquires the read lock 32,768 times.

The lock stores a thread&#x27;s local read and write hold counts in one integer. The low 15 bits are used for the read hold count, and bit 15 is used as `WRITE_LOCK_HELD`. After 32,768 reentrant read acquisitions, the local read count crosses into the write-loc…

---

## 29. 🟡 High Severity — CoreWCF: SPNEGO SecurityContextToken proof key wrapped without confidentiality

**CVE:** `CVE-2026-54784` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-2288-8h3r-cqgg>

> ### Impact
When the proof key recovered from the RSTR can be observed by a party that is not the legitimate client, that party can impersonate the authenticated Windows principal for the lifetime of the SCT (default ~10 hours) and decrypt or forge any subsequent WS‑SecureConversation traffic that uses keys derived from the SCT.

#### Preconditions
Using security mode TransportWithMessageCredential…

---

## 30. 🟡 High Severity — CoreWCF: SamlSerializer skips SignatureValue verification when SAML signing token is not an X.509 certificate

**CVE:** `CVE-2026-54774` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-rpj7-hr7h-w6p9>

> ### Impact
When a service is configured to validate SAML tokens using a method other than X.509 certificate signing, the final signature verification is skipped.

#### Preconditions
The service is configured to authenticate using SAML tokens and an out of band token resolver (commonly the IssuerTokenResolver of IssuedTokenServiceCredential) holds a non-X.509 SecurityToken whose key identifier the …

---

## 31. 🟡 High Severity — CoreWCF: Pre-authentication infinite-loop CPU exhaustion in CoreWCF net.tcp / net.pipe / net.uds framing handshake

**CVE:** `CVE-2026-54772` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-p86g-xrr2-pf7c>

> ### Impact
An unauthenticated remote attacker can pin one server thread‑pool worker at 100 % CPU per connection. With a few connections, the CPU usage can be exhausted.

#### Preconditions
An attacker being able to reach a service which is exposing an endpoint using one of NetTcpBinding, NetNamedPipeBinding, or UnixDomainSocketBinding.

### Patches
Fixed in CoreWCF v1.8.1 and v1.9.1

### Workaroun…

---

## 32. 🟡 High Severity — Weekly Metasploit Update: NTLM Relay Priv Esc, MCP Server Integration, Paperclip AI RCE Chain, and more

**CVE:** `CVE-2026-41679` | `CVE-2026-41459` | `CVE-2026-34413` | `CVE-2026-34415` | `CVE-2026-34414` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-19-06-2026>

> This week&#x27;s release includes five new modules, including a full unauthenticated RCE chain for Paperclip AI and a VS Code extension persistence technique. On the post-exploitation side, the new windows/local/ntlm_relay_2_self module coerces the local machine account to authenticate via OpenEncryptedFileRaw (WebDAV), relays that NTLM authentication to a Domain Controller&#x27;s LDAP service, th…

---

## 33. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
