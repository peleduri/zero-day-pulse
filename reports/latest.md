# Zero Day Pulse

> **Generated:** 2026-07-01 14:05 UTC &nbsp;|&nbsp; **Total:** 33 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 15 &nbsp;|&nbsp; 🟡 High: 18 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CWE-22 Path Traversal in the /toolbox-resource endpoint of the SimpleHelp web application. Unauthenticated remote attackers can request crafted paths containing `../` sequences (e.g. `../../../../../../etc/passwd`) to download arbitrary files from the host, including `serverconfig.xml` (Technician account info and password hashes), `/etc/passwd`, and SSH private keys such as `/root/.ssh/id_rsa`. Exposed credentials enable privilege escalation and remote login. When chained with CVE-2024-57726 (missing authorization allowing privilege escalation to server administrator) and CVE-2024-57728 (arbitrary file upload / zip-slip leading to code execution), the path traversal can lead to full compromise of the SimpleHelp server.
- **Affected Products:** SimpleHelp Remote Monitoring & Management / Remote Support software v5.5.7 and all earlier releases (specifically v5.3.x prior to 5.3.9, v5.4.x prior to 5.4.10, and v5.5.x prior to 5.5.8).
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Yes — wide public exploit availability: (1) Metasploit auxiliary scanner module `auxiliary/scanner/http/simplehelp_toolbox_path_traversal` (https://www.rapid7.com/db/modules/auxiliary/scanner/http/simplehelp_toolbox_path_traversal/); (2) PoC by Horizon3.ai at https://www.horizon3.ai/attack-research/disclosures/critical-vulnerabilities-in-simplehelp-remote-support-software/; (3) OffSec write-up with sample payloads (e.g. `../../../../../../etc/passwd`) at https://www.offsec.com/blog/cve-2024-57727; (4) Listed in the CISA KEV Catalog.
- **Patch Available:** Yes. Fixed versions were released by SimpleHelp between January 8 and 13, 2025: v5.5.8 and later (current latest at time of research is 5.5.15), plus patched v5.4.10 and v5.3.9 for older branches. Vendor advisory/KB: https://simple-help.com/kb---security-vulnerabilities-01-2025. Companion explainer: https://www.simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know. Downloads: https://simple-help.com/downloads.
- **Active Exploitation:** Yes — confirmed in-the-wild exploitation by ransomware actors. Primary source: CISA Advisory AA25-163A 'Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider' (published June 12, 2025). CISA reports ransomware actors have been targeting unpatched SimpleHelp RMM since January 2025, and in a recent incident leveraged CVE-2024-57727 against a downstream customer's unpatched SimpleHelp RMM to compromise a utility billing software provider, enabling double-extortion ransomware. Threat actor named: DragonForce. Additional sources: the CVE was added to the CISA Known Exploited Vulnerabilities (KEV) Catalog on 2025-02-13.
- **Threat Actors:** DragonForce ransomware actors (named in CISA Advisory AA25-163A, June 12, 2025). CISA also documents a broader pattern of ransomware actors targeting organizations through unpatched SimpleHelp RMM since January 2025, impacting Managed Service Providers (MSPs) and their downstream customers.
- **Mitigation:** Primary remediation: upgrade SimpleHelp to v5.5.8 or later (latest is v5.5.15); for older branches, apply the patched v5.4.10 or v5.3.9. Pre-patch hardening workarounds (per SimpleHelp and CISA) include: (1) isolate the SimpleHelp server from the internet or stop the server process; (2) change Administrator and Technician account passwords; (3) restrict source IPs allowed for Technician and Administrator logins; (4) disable the built-in `SimpleHelpAdmin` user; (5) disable local Technician logins in favor of AD/LDAP; (6) rotate/re-issue API tokens and restrict API request IPs; (7) apply host/network firewalling of the server; (8) enable event alerts for administrator logins, failed logins, and configuration changes; (9) monitor for suspicious executables using three-letter alphabetic filenames (e.g. `aaa.exe`, `bbb.exe`) created after January 2025. Broadcom publishes detection/protection signatures: 'Web Attack: SimpleHelp Directory Traversal CVE-2024-57727' and 'Symantec DCS Custom sandbox for SimpleHelp with hardening rules'.
- **Vendor Advisory:** https://simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — Anthropic Restores Claude Fable 5 After U.S. Lifts Jailbreak-Linked Export Controls

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://thehackernews.com/2026/07/anthropic-restores-claude-fable-5-after.html>

> Anthropic is putting Claude Fable 5 back online worldwide. On June 30, the U.S. Commerce Department lifted the export controls it had imposed on Fable and its more tightly controlled sibling Mythos 5 about two and a half weeks earlier.

Fable 5 returns to users on Wednesday, July 1, across Claude.ai, the Claude Platform, Claude Code, and Claude Cowork.

Export controls restrict who can

**Parallel AI Enrichment:**

- **Technical Details:** A prompt-engineering jailbreak: a user-level prompting technique (widely summarized as a simple instruction such as “fix this code”) bypassed model constraints and exposed sensitive model behavior or internal/system prompt material. Some reporting says the model’s system prompt was published; however a fully reproducible, widely shared step-by-step exploit has not been published. Mitigation focuses on classifiers and runtime controls.
- **Affected Products:** Claude Fable 5, Claude Mythos 5
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Partial artifacts circulated: reporting states Fable 5’s ~120,000-character system prompt was posted to GitHub, but other reporting says the exact, transferable jailbreak technique has not been widely published. (Artifacts exist, but no confirmed weaponized PoC publicly available.)
- **Patch Available:** Anthropic states it is redeploying Claude Fable 5 starting July 1 “with updated cybersecurity safeguards” (vendor redeploy announcement). See: https://www.anthropic.com/news/redeploying-fable-5
- **Active Exploitation:** No authoritative reporting of confirmed, large-scale active exploitation campaigns tied to this jailbreak was found; the incident triggered a government export-control directive and vendor suspension and remediation rather than public reports of widespread exploitation.
- **Threat Actors:** None known
- **Mitigation:** Vendor-provided mitigations: Anthropic added/relied on classifiers and other runtime safeguards to detect and block jailbreak/misuse attempts. Recommended hardening (in line with vendor actions): enable prompt-classifiers, tighten runtime controls and monitoring, restrict model access by policy, log and review suspicious prompting patterns.
- **Vendor Advisory:** https://www.anthropic.com/news/redeploying-fable-5

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI): attackers embed adversarial instructions inside content (web pages, email, documents) that an LLM may process and then follow instead of the user's intent. Observed categories include benign guidance, SEO manipulation, deterrence (e.g., infinite streamed text), data-exfiltration attempts, and destructive commands; detection/analysis uses pattern-matching, LLM-based classification (Gemini) and human validation.
- **Affected Products:** Google Workspace (Gmail, Docs, other Workspace apps) with Gemini, Gemini model
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit published in the vendor advisories; Google reports examples observed on public websites but does not publish exploit code or a public PoC.
- **Patch Available:** No official vendor "patch" was published for IPI in these advisories; Google describes continuous defenses, configuration-based "point fixes" and model hardening instead (see vendor advisories).
- **Active Exploitation:** Google observed prompt-injection examples on public websites and a rising detection trend (a reported ~32% relative increase in the malicious category between Nov 2025 and Feb 2026), but characterized most findings as low-sophistication experiments rather than large-scale, productionized exploitation.
- **Threat Actors:** None known
- **Mitigation:** Defense-in-depth: continuous discovery and red‑teaming (human + automated), synthetic data generation for retraining, deterministic defenses/configuration (user confirmation, URL sanitization, policy engine, regex takedowns/point fixes), ML-based model retraining, LLM prompt-engineering defenses, and Gemini model hardening; Google also runs an AI Vulnerability Reward Program and centralized vulnerability catalog.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI): an attacker injects malicious instructions into external data, content, or tools that LLM-based systems ingest (e.g., web content, integrated corpora, tool outputs). The model may follow those injected instructions when answering user queries or when agents take actions, even without direct user input.
- **Affected Products:** Google Workspace (with Gemini integrations), LLM-based RAG and agentic systems (no specific product versions listed).
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit observed in vendor or third-party reporting; researchers and vendors have reported IPI payloads and samples on public sites but no authoritative published exploit code was found in the collected corpus.
- **Patch Available:** No official vendor patch available. Google describes layered defenses and continuous hardening (see vendor advisory).
- **Active Exploitation:** Yes — vendor and third-party reporting describe IPI payloads found on public websites and an observed increase in malicious attempts; Google reported a broad web sweep and third parties documented IPI payloads caught in the wild, though no large-scale compromise attributable to IPI was documented in the gathered sources.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses and continuous hardening: vet and filter retrieved external content, apply retrieval and RAG hardening, enforce instruction/response guardrails, harden tool integrations and agent workflows, and monitor for IPI patterns (per vendor advisory).
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Broadly: indirect prompt injection (IPI) hides attacker instructions in web content (or leverages malicious extensions) that agentic models/agents (Gemini in Chrome) can ingest and obey. Noma Labs’ GeminiJack showed a zero-click IPI against Gemini Enterprise; CVE-2026-0628 arose from insufficient policy enforcement in Chrome's WebView tag that allowed privileged contexts (e.g., the Gemini panel) to be influenced by web content or extensions.
- **Affected Products:** Google Chrome (Gemini / agentic browsing features) — Chrome versions prior to 143.0.7499.192
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No confirmed public PoC URL located in the captured corpus. Reporting is mixed: some news reports said one of Chrome's recent zero-days had an exploit accessible in the wild, but trackers for CVE-2026-0628 reported no known public exploit.
- **Patch Available:** Yes — Google/Chrome has issued fixes. NVD lists CVE-2026-0628 as fixed in Chrome 143.0.7499.192 (see NVD CVE-2026-0628 entry).
- **Active Exploitation:** Indirect prompt-injection techniques have been observed in the wild (industry reports from Unit42, Forcepoint, HelpNet). Reporting specifically about exploitation of the Chrome/WebView issue (CVE-2026-0628) is mixed: some outlets describe a high‑severity issue that was quickly patched, while vulnerability trackers reported no known public exploit for CVE-2026-0628.
- **Threat Actors:** None known
- **Mitigation:** Apply the Chrome update/patch (update to the fixed version), enable Chrome's new layered/agentic defenses, remove or audit untrusted extensions, restrict origin/access controls for agentic surfaces, and follow vendor hardening guidance for agentic browsing.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** High‑level memory‑safety summary: Google reports that adopting Rust for Android system services/libraries reduces memory‑safety vulnerability density (the post cites a ~1000x reduction versus C/C++) and that memory‑safety vulnerabilities fell below 20% of total vulnerabilities in 2025. The post is a programmatic overview of this strategy rather than a per‑vulnerability exploit writeup.
- **Affected Products:** Android platform (first‑party and third‑party / open‑source components)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept or weaponized exploit is reported in the Google blog post; PoCs (if any) would be published in per‑CVE writeups and Android Security Bulletins/CVE records.
- **Patch Available:** No single patch is provided by the blog post. Per‑vulnerability patches for Android are published via the Android Security Bulletins (e.g. https://source.android.com/docs/security/bulletin/2025-11-01 and https://source.android.com/docs/security/bulletin/2025-12-01).
- **Active Exploitation:** No confirmed active exploitation is reported in the Google blog post or the mainstream summaries of that post.
- **Threat Actors:** None known
- **Mitigation:** Programmatic mitigation: adopt memory‑safe languages (Rust) for new Android system services/libraries and apply Android Security Bulletin patches for specific CVEs. For immediate fixes, apply the per‑CVE patches published in the Android Security Bulletins.
- **Vendor Advisory:** https://blog.google/security/rust-in-android-move-fast-fix-things/

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection embeds hidden adversarial instructions inside external content (emails, documents, calendar invites, web pages, files) that an LLM or AI agent retrieves and processes. Unlike direct prompt injection (user-typed malicious input), indirect injection leverages untrusted external data to hijack the model: exfiltrating user context, rendering unsanitized markdown/links/images to leak data, or executing rogue actions. The class targets the trust boundary between user instructions and retrieved data (OWASP 'LLM01:2025 - Prompt Injection'). Example mechanics per EchoLeak (CVE-2025-32711): an attacker plants markdown or an external image URL inside a document Copilot ingests; the RAG pipeline renders the markdown and the model is tricked into fetching the URL, exfiltrating sensitive user/tenant data via outbound reference, evading CSP through trusted intermediates.
- **Affected Products:** Google Gemini app; Gemini in Google Workspace (Gmail, Google Docs editors, Google Drive, Google Chat); Gemini 2.5 models; Google Gemini Enterprise / Vertex AI Search (per GeminiJack disclosure). The blog references CVE-2025-32711/EchoLeak as a class example — that CVE affects Microsoft 365 Copilot, not Gemini. Indirect prompt injection as a class also affects any LLM/agent that ingests untrusted external content.
- **CVSS Score:** 9.3
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N (for the referenced CVE-2025-32711 / EchoLeak as cited in the blog; the blog itself has no assigned CVSS vector).
- **Exploit Available:** Yes — public proof-of-concept exploits exist for the indirect prompt injection class and for Google Gemini specifically. PoC sources: Aim Labs EchoLeak PoC (https://www.aim.security/lp/aim-labs-echoleak-m365), GitHub CVE-2025-32711 PoC (https://github.com/daryllundy/cve-2025-32711), Noma Labs GeminiJack PoC (https://noma.security/noma-labs/geminijack/, https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/), and SafeBreach Gemini voice-assistant exploit (https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/).
- **Patch Available:** No traditional vendor patch is associated with the Google Security Blog post — it documents Google's layered defense-in-depth strategy already deployed for Gemini (proprietary classifiers, adversarial training for Gemini 2.5, markdown sanitization, URL filtering, HITL, security notifications). For the referenced Microsoft CVE-2025-32711 / EchoLeak, Microsoft patched Microsoft 365 Copilot server-side in May 2025 (advisory: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32711). Subsequent Gemini-specific disclosures (GeminiJack, Tenable's three vulnerabilities, SafeBreach Gemini exploit) have remediation timelines managed separately.
- **Active Exploitation:** Yes, observed for the broader class. Indirect prompt injection has been observed in the wild against AI agents broadly — Palo Alto Unit 42 (March 2026, https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/) documented multi-language dynamic adversarial prompts executed inside browser-resident AI agents; Google's own web sweep (April 2026, https://blog.google/security/prompt-injections-web/) confirmed public-web content carrying indirect prompt injection payloads aimed at AI crawlers/agents. For Google Gemini specifically, the blog states layered defences have consistently mitigated observed indirect prompt injection attempts in production; no publicly documented opportunistic in-the-wild breach is tied to this June 13, 2025 post. Related EchoLeak (CVE-2025-32711) was a research-disclosed zero-click vulnerability and is not reported as having been exploited in the wild prior to patching.
- **Threat Actors:** None known. The Google Security Blog post does not name any specific APT groups or threat actors exploiting indirect prompt injection against Gemini. Related GTIG reporting on adversarial misuse of Gemini (Jan/Feb 2025-2026) documents nation-state and cybercrime use of the Gemini app as a productivity/reconnaissance tool, not exploitation via prompt injection.
- **Mitigation:** Google's documented six-layer defense-in-depth strategy: (1) Adversarial model training with AI red-teaming; (2) Proprietary ML-based prompt injection content classifiers (detecting malicious instructions in emails, files, content); (3) Security thought reinforcement (system-level instructions steering the LLM to focus on user-directed tasks and ignore adversarial instructions); (4) Markdown sanitization and suspicious URL redaction (refuses to render external image URLs; Google Safe Browsing-aware URL filtering); (5) Human-In-The-Loop (HITL) user confirmation framework requiring explicit user consent before risky actions; (6) End-user security mitigation notifications surfacing contextual information and help-center guidance when prompts are blocked. Adjacent hardening: input provenance checks, treating all retrieved external content as untrusted, sandboxing LLM tool calls, and explicit user confirmation for data egress.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Root causes reported in the advisory set are command-injection / arbitrary-file-creation vulnerabilities in network-device web/GlobalProtect components that can lead to remote command execution or code execution. Adversaries exploit/abuse compromised backbone, PE, and CE routers (and compromised devices/trusted connections) to modify router firmware/configuration, maintain persistent access, and pivot into downstream networks for long-term espionage.
- **Affected Products:** Ivanti Connect Secure (9.x, 22.x), Ivanti Policy Secure (9.x, 22.x), Palo Alto Networks PAN-OS (GlobalProtect) affecting PAN-OS versions 10.2, 11.0, 11.1; industry reporting also lists a broader set of impacted vendors (Cisco, Fortinet, Juniper, Microsoft Exchange) though specific versions for those vendors were not enumerated in the collected sources.
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit URL was identified in the collected sources; CISA noted that exploitation of zero-day vulnerabilities had not been observed at the time of the advisory and industry writeups did not surface a public PoC in the gathered material.
- **Patch Available:** Partial: Ivanti has published advisories/patches for CVE-2024-21887 (Ivanti KB above). Palo Alto published guidance/workarounds and protections for CVE-2024-3400 (Palo Alto advisory above). Vendor patch status for other affected vendors varies (some industry summaries noted no official vendor remediation guidance for certain affected devices at the time of reporting).
- **Active Exploitation:** CISA reports PRC state-sponsored actors are targeting and compromising networks worldwide (abusing backbone/PE/CE routers); however, the advisory additionally states exploitation of zero-day vulnerabilities had not been observed at the time of publication. Separately, public actions (e.g., law‑enforcement disruption of router botnets) confirm that large-scale router compromise campaigns have occurred in the broader context.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Apply vendor patches or vendor-provided workarounds immediately for the specific CVEs (see vendor advisories above). Where patches are not available, follow vendor workarounds; isolate and harden management interfaces (limit management-plane access to trusted hosts, enable MFA where supported), segment provider edge (PE) and customer edge (CE) devices from general networks, monitor for suspicious configuration changes and persistence artifacts on routers, and apply CISA/industry detection and logging recommendations. (See CISA advisory and vendor guidance referenced above.)
- **Vendor Advisory:** https://security.paloaltonetworks.com/CVE-2024-3400, https://hub.ivanti.com/s/article/KB-CVE-2023-46805-Authentication-Bypass-CVE-2024-21887-Command-Injection-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure-Gateways, https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** This is a campaign-level espionage operation attributed to GRU Unit 26165: actors use cyber-espionage tradecraft (spearphishing, credential access/harvesting, lateral movement, use of custom tooling and infrastructure) against Western logistics and technology organizations; the advisory provides TTP descriptions and IOCs for detection/response.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public CVE-level proof-of-concept or weaponized exploit is reported in the advisory. Industry responses include red-team/emulation artifacts (e.g., AttackIQ assessment template aligned to AA25-141A) rather than a public exploit PoC.
- **Patch Available:** No vendor patch is described; this is a campaign advisory (CISA AA25-141A). Follow the advisory for guidance: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a
- **Active Exploitation:** CISA and partner advisories describe ongoing targeting since 2022 of Western logistics and technology companies (AA25-141A and associated FBI/partner advisories), indicating active exploitation/targeting attempts in the wild.
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS), military unit 26165
- **Mitigation:** Follow the mitigations and IOCs in CISA AA25-141A (ingest the AA25-141A STIX/IOC bundle). General hardening recommended by the advisory: enable MFA, enforce least privilege for accounts, apply vendor security updates where available, deploy/monitor EDR and network detections, segment critical networks, monitor and hunt for the advisory IOCs, and train staff to resist spearphishing.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

**Parallel AI Enrichment:**

- **Technical Details:** The article describes browser attack mechanics in general terms rather than documenting a specific vulnerability. It outlines how attackers chain multiple browser weaknesses—exploitation of rendering logic, JavaScript execution errors, document handling, or memory-safety flaws—followed by a sandbox escape, privilege escalation, or other technique to move from browser activity to system access. The Chromium shared-core architecture is highlighted as a force multiplier: a single vulnerability in the shared codebase can affect multiple downstream browsers. No CVE-level mechanism or reproduction detail is provided.
- **Affected Products:** Web browsers in general (specifically Chromium-based browsers sharing the Chromium open-source core). No specific versions are identified.
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No specific PoC or weaponized exploit is identified. The article discusses in general terms that technical details, exploit paths, and PoC code can become publicly available after disclosure for N-day vulnerabilities. No exploit source URL is provided.
- **Patch Available:** No specific vendor patch is referenced (the article is not tied to a single CVE). General guidance is to apply browser vendor security updates as released. Product documentation for the promoted defense solution (Falcon Secure Access) is at https://www.crowdstrike.com/en-us/resources/data-sheets/falcon-secure-access/
- **Active Exploitation:** No specific in-the-wild exploitation of a named vulnerability is reported. The article cites two industry reports for general exploitation trends: (1) the CrowdStrike 2026 Global Threat Report, which states that 42% of vulnerabilities were exploited before public disclosure; and (2) the Verizon 2026 Data Breach Investigations Report, which found vulnerability exploitation surpassed stolen credentials as the top breach entry point in 2025.
- **Threat Actors:** None known (this is a general thought-leadership blog post about browser security; no specific threat actor groups, APT campaigns, or ransomware operators are named)
- **Mitigation:** 1) Validate, test, and rapidly deploy vendor browser patches as they become available. 2) Deploy CrowdStrike Falcon Secure Access, which operates inside the browser's JavaScript execution environment and uses a moving-target defense called JavaScript Language Randomization (JSLR) to make zero-day exploits harder to weaponize before a patch exists. Falcon Secure Access additionally blocks phishing and adversary-in-the-middle techniques, protects session tokens against hijacking/MFA bypass, and prevents credential theft and data exfiltration at the point of execution. 3) Recognize that patch deployment windows (validate, test, stage, confirm installation) create a residual exploitation gap even after a fix is published.
- **Vendor Advisory:** https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/

---

## 11. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 12. 🟠 Zero-Day — Phantom Squatting Uses AI-Hallucinated Domains for Phishing and Malware

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://thehackernews.com/2026/07/phantom-squatting-uses-ai-hallucinated.html>

> Large language models keep inventing web addresses that do not exist. Attackers have started buying those made-up domains before anyone else can, then hosting phishing pages on them to catch traffic that AI tools point their way.

Palo Alto Networks&#x27; Unit 42 calls the trick phantom squatting, and its new research shows it is already happening in the wild.

The reason it matters is

---

## 13. 🟠 Zero-Day — New BioShocking attack manipulates AI browser into data theft

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://www.bleepingcomputer.com/news/security/new-bioshocking-attack-manipulates-ai-browser-into-data-theft/>

> A new prompt injection attack dubbed &quot;BioShocking&quot; could trick AI-powered browsers into treating real-world risky actions as part of a fictional scenario, causing them to ignore any safety guardrails. [...]

---

## 14. 🟠 Zero-Day — oban_web missing authorization check on `save-job` event handler

**CVE:** `CVE-2026-48592` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-389x-rgxr-8m33>

> ### Summary

`oban_web` 2.12.0 through the current unpatched release exposes a `save-job` LiveView event handler that performs no authorization check, allowing any authenticated user (including those with `:read_only` access) to overwrite a queued job&#x27;s `worker` field with any other `Oban.Worker` module present in the application. On the job&#x27;s next execution attempt, Oban dispatches `per…

---

## 15. 🟠 Zero-Day — Fake Perplexity extension on Chrome Web Store tracked searches

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://www.bleepingcomputer.com/news/security/fake-perplexity-extension-on-chrome-web-store-tracked-searches/>

> A malicious extension in the Chrome Web Store is masquerading as the Perplexity AI answer engine, intercepting search traffic and collecting browsing information. [...]

---

## 16. 🟡 High Severity — Citrix Patches Six NetScaler Flaws Allowing File Read and Denial-of-Service

**CVE:** `CVE-2026-8451` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://thehackernews.com/2026/07/citrix-patches-six-netscaler-flaws.html>

> Citrix on Tuesday released security updates to address multiple flaws in NetScaler ADC (formerly Citrix ADC) and NetScaler Gateway (formerly Citrix Gateway) that could be exploited by an attacker to facilitate arbitrary file reads or trigger a denial-of-service (DoS) condition.

The vulnerabilities are listed below -


  CVE-2026-8451 (CVSS score: 8.8) - An insufficient input validation

---

## 17. 🟡 High Severity — Twig: Sandbox `__toString()` policy bypass via `Traversable` in `join` and `replace` filters

**CVE:** `CVE-2026-48807` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-8x9c-rmqh-456c>

> ### Description

This is a residual bypass of CVE-2026-47732 / GHSA-pr2w-4gpj-cpq4 left after the initial fix for unguarded `__toString()` calls. It covers two related coercion points that were not caught by the original patch.

**`Traversable` in `join` and `replace` filters.** `SandboxExtension::ensureToStringAllowed()` recurses into PHP arrays so that a `Stringable` object hidden inside an arra…

---

## 18. 🟡 High Severity — Fulcio has OIDC Discovery Redirect Following Allows SSRF and JWKS Substitution for Meta-Issuer Paths, with Kubernetes Service-Account Token Leakage

**CVE:** `CVE-2026-49478` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-f5mr-q85p-6hh6>

> ## Impact

Three security vulnerabilities were identified in the OIDC Discovery client:

1. **Blind Server-Side Request Forgery (SSRF) via Cross-Host Redirects**:
   Fulcio uses an HTTP client to fetch OIDC discovery metadata (`/.well-known/openid-configuration`). Prior to this fix, if a configured issuer returned an HTTP redirect to a different host, the client followed it by default. This allowe…

---

## 19. 🟡 High Severity — CefSharp.Common: `FolderSchemeHandlerFactory` path boundary check can expose files outside the configured root folder

**CVE:** `CVE-2026-48796` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-85jm-cwp2-mvpv>

> ### Summary

`FolderSchemeHandlerFactory` was intended to restrict served files to a configured `rootFolder`, but its path validation used a raw string prefix check. A request could escape to a sibling directory whose full path starts with the root folder path, allowing files outside the configured root to be served.

### Details

In affected versions, `FolderSchemeHandlerFactory` canonicalized `r…

---

## 20. 🟡 High Severity — @adonisjs/bodyparser has an incomplete fix for CVE-2026-25754

**CVE:** `CVE-2026-48795` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-qcm7-3vpr-hj5h>

> ### Summary

The fix for [GHSA-f5x2-vj4h-vg4c](https://github.com/adonisjs/core/security/advisories/GHSA-f5x2-vj4h-vg4c) / CVE-2026-25754 introduced in commit [`40e1c71`](https://github.com/adonisjs/bodyparser/commit/40e1c71f958cffb74f6b91bed6630dca979062ed) is incomplete and can be bypassed through nested prototype pollution payloads.

The original patch replaced the internal `FormFields` storage…

---

## 21. 🟡 High Severity — Probo has an open redirect bypass via path normalization

**CVE:** `CVE-2026-49820` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-x7qq-m748-8p2c>

> ### Impact
Probo&#x27;s `saferedirect` package validates redirect URLs used across authentication flows (OIDC, SAML, session transfer, OAuth connectors, and trust-center magic links). The validator only inspected the second character of relative paths, so a URL like `/../\evil.com` passed validation because the second character is `.`. Go&#x27;s `http.Redirect` normalizes this path to `/\evil.com`…

---

## 22. 🟡 High Severity — Fission builder pods auto-mount the fission-builder ServiceAccount token in the user-supplied builder container

**CVE:** `CVE-2026-50565` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-8wcj-mfrc-jx5q>

> ### Summary

Fission builder pods were created with `ServiceAccountName: fission-builder` and no `AutomountServiceAccountToken: false`, so the kubelet auto-mounted the service-account token into every container in the pod — including the
user-supplied builder image.

### Details

The user controls the builder container image, command, and podspec through `Environment.spec.builder.image` / `.contai…

---

## 23. 🟡 High Severity — Fission Environment CRD podspec passthrough enables hostPID/hostNetwork/privileged pods, node escape

**CVE:** `CVE-2026-50564` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-gx55-f84r-v3r7>

> ### Summary

Fission&#x27;s `Environment` CRD exposes `spec.runtime.podSpec` and `spec.builder.podSpec`, which are merged into the Kubernetes pod specs for runtime and builder pods. The merge logic propagated `hostNetwork`, `hostPID`, `hostIPC`, container
 `privileged`, and `serviceAccountName` from the user-supplied podspec with no filtering, and `Environment.Validate` performed no security-relev…

---

## 24. 🟡 High Severity — Fission Container Executor Function PodSpec Injection Leading to Node Escape

**CVE:** `CVE-2026-50563` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-v455-mv2v-5g92>

> ### Summary

Fission&#x27;s Container Executor path lets a tenant supply `Function.spec.podspec` directly; the executor merges it into the executor-built podspec and creates a Deployment whose pods run the user&#x27;s container image.

### Details

Two flaws compounded:

1. `pkg/apis/core/v1/validation.go::FunctionSpec.Validate` only checked that `spec.PodSpec != nil` when `executorType: container…

---

## 25. 🟡 High Severity — Fission Environment CRD PodSpec Injection Leading to Node Escape and Cluster Takeover

**CVE:** `CVE-2026-50545` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-wmgg-3p4h-48x7>

> ### Summary

A stronger framing of the same root cause as GHSA-gx55-f84r-v3r7: the `Environment.spec.runtime.podSpec` / `spec.builder.podSpec` passthrough lacked validation, and `MergePodSpec` propagated dangerous fields into the generated pods.

### Details

Three independent flaws compounded:

1. **Validate gap.** `pkg/apis/core/v1/validation.go::Environment.Validate` checked only container nami…

---

## 26. 🟡 High Severity — Fission: Cross-namespace Environment reference via unvalidated EnvironmentRef in Function admission webhook

**CVE:** `CVE-2026-49824` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-cvw6-gfvv-953q>

> ### Summary

The Fission Function admission webhook (`pkg/webhook/function.go`) validated that `spec.secrets[].namespace` and `spec.configmaps[].namespace` equalled the function&#x27;s own namespace but performed no equivalent check on
`spec.environment.namespace`.

### Details

An attacker with permission to create Functions in their own namespace could set `spec.environment.namespace` to any oth…

---

## 27. 🟡 High Severity — Fission: Cross-namespace Package read via unvalidated PackageRef in Function admission webhook

**CVE:** `CVE-2026-49823` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-3r8v-2xmj-5c39>

> ### Summary

A Fission Function spec carries three reference types — Secret, ConfigMap, and Package. The first two were namespace-validated by the admission webhook; `PackageRef.Namespace` was not.

### Details

A tenant with `functions.fission.io/create` in their own namespace could set `spec.package.packageref.namespace` to any other namespace. When the function is invoked, the fetcher sidecar r…

---

## 28. 🟡 High Severity — Fission: Cross-namespace event leakage via KubernetesWatchTrigger allows persistent tenant surveillance

**CVE:** `CVE-2026-49822` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-gc3j-79f2-7vvw>

> ### Summary

A low-privilege developer who could create a `KubernetesWatchTrigger` (KWT) in their own namespace was able to establish a persistent surveillance channel over any other namespace.

### Details

Two independent flaws compounded:

1. `pkg/kubewatcher/kubewatcher.go::createKubernetesWatch` used `w.Spec.Namespace` (user-controlled) directly as the Watch target without checking it against…

---

## 29. 🟡 High Severity — Fission: Cross-namespace Environment reference in Package allows build-time command execution and SA token exfiltration

**CVE:** `CVE-2026-49821` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-vjhc-cf4p-72q4>

> ### Summary

Fission&#x27;s `buildermgr` controller processed `Package` CRDs without verifying that `Package.spec.environment.namespace` matched `Package.metadata.namespace`.

### Details

An attacker with `packages.fission.io/create` in their own namespace could set `spec.environment.namespace` to any other tenant&#x27;s namespace. The controller then used its high-privilege service account to fe…

---

## 30. 🟡 High Severity — RabbitMQ has predictable credential obfuscation seed value used in Shovel and Federation plugins

**CVE:** `CVE-2022-31008` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-v9gv-xp36-jgj8>

> ### Impact

Shovel and Federation plugins perform URI obfuscation in their worker (link) state. The encryption key used to encrypt
the URI was seeded with a predictable secret.

This means that in case of certain exceptions related to Shovel and Federation plugins,
reasonably easily deobfuscatable data could appear in the node log.

Patched versions correctly use a cluster-wide secret for that pur…

---

## 31. 🟡 High Severity — Microsoft.OpenAPI: Circular schema references may terminate OpenAPI parsing

**CVE:** `CVE-2026-49451` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://github.com/advisories/GHSA-v5pm-xwqc-g5wc>

> ### Impact

A small OpenAPI document containing a circular schema reference can cause process termination through stack overflow in Microsoft.OpenApi. The issue affects OpenAPI document parsing through public OpenAPI.NET reader APIs and has been confirmed across both JSON and YAML reader paths.

## Affected versions

- `&gt;= 2.0.0-preview11, &lt;= 2.7.4`
- `&gt;= 3.0.0, &lt;= 3.5.3`

### Patches
…

---

## 32. 🟡 High Severity — Langflow RCE Exploited to Deploy Monero Miner on Exposed AI App Endpoints

**CVE:** `CVE-2026-33017` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-30
**Reference:** <https://thehackernews.com/2026/06/langflow-rce-exploited-to-deploy-monero.html>

> Threat actors are continuing to exploit a critical Langflow vulnerability as part of fresh attacks designed to deliver a Monero cryptocurrency miner.

The activity has been found to weaponize CVE-2026-33017 (CVSS score: 9.3), an unauthenticated remote code execution (RCE) vulnerability in Langflow, indicating threat actors are scanning and targeting exposed artificial intelligence (AI)

---

## 33. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
