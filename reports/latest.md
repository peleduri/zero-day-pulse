# Zero Day Pulse

> **Generated:** 2026-09-18 10:14 UTC &nbsp;|&nbsp; **Total:** 41 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 9 &nbsp;|&nbsp; 🟡 High: 32 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Improve Router Hygiene to Protect Against Russian State-Sponsored Targeting

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Wed, 08 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a>

> Russian Government-Sponsored Activity Targets Poorly Configured and Vulnerable Devices Across Critical Sectors Executive summary Russian Federal Security Service (FSB) Center 16 cyber actors continue to exploit poorly configured and vulnerable networking devices worldwide, opportunistically compromising multiple critical infrastructure sector networks. This joint Cybersecurity Advisory (CSA) build…

**Parallel AI Enrichment:**

- **Technical Details:** FSB Center 16 actors scan Internet address ranges for exposed SNMP agents accepting common or default community strings, primarily to identify poorly configured routers. They also occasionally exploit Cisco Smart Install and web-based network-device management portals, including the referenced CVE-2018-0171 and CVE-2008-4128 vulnerabilities.
- **Affected Products:** Poorly configured or end-of-life networking devices, primarily internet-exposed routers; Cisco IOS and IOS XE devices using Smart Install (CVE-2018-0171; exact vulnerable releases are not specified in AA26-194A); Cisco IOS 12.4 on the Cisco 871 Integrated Services Router (CVE-2008-4128).
- **CVSS Score:** ://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a
- **CVSS Vector:** ://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a
- **Exploit Available:** true for referenced vulnerabilities. Public exploit material is documented for the referenced Cisco vulnerabilities; the CVE-2008-4128 record lists Exploit-DB entry 6476. Source: https://www.cve.org/CVERecord?id=CVE-2008-4128
- **Patch Available:** false for AA26-194A itself: this is a joint threat-activity advisory, not a single-product patch bulletin. Relevant products require their own vendor updates; Cisco's separate advisory for CVE-2018-0171 is https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20180328-smi2.
- **Active Exploitation:** true. CISA reports that Russian FSB Center 16 actors continue to exploit poorly configured and vulnerable networking devices worldwide, and identifies prior exploitation of CVE-2018-0171 and CVE-2008-4128.
- **Threat Actors:** Russian FSB Center 16; commonly used industry aliases include Berserk Bear, Energetic Bear, Crouching Yeti, Dragonfly, Ghost Blizzard, and Static Tundra.
- **Mitigation:** Update network-device software and firmware, patch known vulnerabilities, and replace or upgrade end-of-life devices with supported versions. Apply the relevant vendor remediation for any exposed Cisco devices and eliminate default or weak management credentials and publicly exposed management services.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a

---

## 2. 🟠 Zero-Day — September 2026 Patch Tuesday: Two Exploited Zero-Days and 113 Critical Vulnerabilities Among 972 CVEs

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Sep 08, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-september-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** The supplied CrowdStrike URL covers two exploited local elevation-of-privilege flaws: CVE-2026-81963 is improper link resolution before file access in the Windows Update Stack, while CVE-2026-85880 is a heap-based buffer overflow in Windows ALPC. The ALPC flaw can be exploited by an attacker able to execute code in a low-privilege AppContainer to escape the sandbox and obtain SYSTEM privileges.
- **Affected Products:** CVE-2026-81963: Windows 11 23H2, affected 10.0.22631.0 < 10.0.22631.7582; Windows 11 24H2, affected 10.0.26100.0 < 10.0.26100.9445; Windows 11 25H2, affected 10.0.26200.0 < 10.0.26200.9445; Windows 11 26H1, affected 10.0.28000.0 < 10.0.28000.2954; Windows Server 2025 and Server Core, affected 10.0.26100.0 < 10.0.26100.33438. CVE-2026-85880: Windows 10 1607, affected 10.0.14393.0 < 10.0.14393.9512; Windows 10 1809, affected 10.0.17763.0 < 10.0.17763.9245; Windows 10 21H2, affected 10.0.19044.0 < 10.0.19044.7725; Windows 10 22H2, affected 10.0.19045.0 < 10.0.19045.7725; Windows Server 2012, affected 6.2.9200.0 < 6.2.9200.26349; Windows Server 2012 R2, affected 6.3.9600.0 < 6.3.9600.23397; Windows Server 2016, affected 10.0.14393.0 < 10.0.14393.9512; Windows Server 2019, affected 10.0.17763.0 < 10.0.17763.9245; Windows Server 2022, affected 10.0.20348.0 < 10.0.20348.5622, including the corresponding Server Core variants where listed.
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true. Both vulnerabilities have confirmed weaponized exploitation in the wild, although the reviewed sources state that exploitation details have not been publicly shared and do not identify a public PoC.
- **Patch Available:** true. Microsoft released official fixes for both vulnerabilities through the MSRC advisories: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-81963 and https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-85880.
- **Active Exploitation:** true. CrowdStrike states that Microsoft confirmed both CVE-2026-81963 and CVE-2026-85880 were being exploited in the wild, and contemporaneous reporting describes them as actively exploited zero-days.
- **Threat Actors:** None known. The reports identify vulnerability discoverers, not a threat actor group, APT campaign, or ransomware operator.
- **Mitigation:** Apply Microsoft's September 8, 2026 security updates for both CVEs using the official MSRC advisories. If updates or vendor mitigations cannot be applied, CISA guidance calls for applying available vendor mitigations or discontinuing use of the affected product; prioritize these flaws because exploitation is confirmed.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-81963; https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-85880

---

## 3. 🟠 Zero-Day — A Vault with a Heap-View: The Uncomfortable Space Between AgentCore Harness and Identity

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Unit 42 (Palo Alto) &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://unit42.paloaltonetworks.com/securing-aws-agentcore-harness-credentials/>

> Analysis of how default configurations in AWS AgentCore Harness allow prompt injection to exfiltrate credentials, and key steps to secure your agents. The post A Vault with a Heap-View: The Uncomfortable Space Between AgentCore Harness and Identity appeared first on Unit 42 .

**Parallel AI Enrichment:**

- **Technical Details:** With default configuration, AgentCore Harness exposes built-in shell and file-operation tools, and the shell runs as root. Because the shell shares the process memory space in which AgentCore Identity resolves credentials into plaintext, prompt injection can cause the agent to access and exfiltrate an operator service-account credential rather than merely the end user's JWT.
- **Affected Products:** Amazon Bedrock AgentCore Harness managed harness, specifically its default built-in shell and file_operations tools; Amazon Bedrock AgentCore Identity. No specific vulnerable software version is identified; the issue concerns default configuration and tool permissions.
- **Exploit Available:** true. Unit 42 publicly demonstrates the attack path in a test scenario showing prompt injection leading to exfiltration of an AgentCore Identity JWT: https://unit42.paloaltonetworks.com/securing-aws-agentcore-harness-credentials/. No standalone exploit code or weaponized package is identified in the report.
- **Patch Available:** false for the Unit 42-described default-configuration credential exposure. Unit 42 states that AWS closed the report as informative under the shared-responsibility model and recommends configuration hardening rather than identifying a vendor patch; the separate CVE-2026-18830 InvokeHarness bulletin addresses a different input-validation issue.
- **Active Exploitation:** false. No confirmed exploitation in the wild is reported for this issue; the available reporting concerns Unit 42's controlled research demonstration and responsible disclosure to AWS.
- **Threat Actors:** None known. The Unit 42 report describes a research demonstration and disclosure to AWS, but does not identify any APT, ransomware, or other threat actor exploiting the issue.
- **Mitigation:** At InvokeHarness time, restrict allowedTools to only the capabilities required for that session; apply least privilege to every AgentCore Identity vault service account and monitor unexpected outbound traffic from harness containers. AWS's guidance also emphasizes the shared AgentCore Runtime trust boundary, input validation, prompt-injection prevention, IAM controls, and microVM isolation.

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection occurs when an AI system processes attacker-controlled content—such as a website, email, or document—and follows embedded instructions instead of the user's intent. Google observed examples targeting AI summaries, data exfiltration, and potentially destructive actions against machines used with AI assistants.
- **Affected Products:** No specific software, hardware product, or vulnerable version is identified; the article discusses AI assistants and agents that browse public websites.
- **CVSS Score:** :
- **CVSS Vector:** :
- **Exploit Available:** false. The Google article identifies observed low-sophistication prompt-injection attempts, but no public proof-of-concept or weaponized product exploit is reported: https://blog.google/security/prompt-injections-web/
- **Patch Available:** false. No product-specific vendor patch is identified because the article describes a broader attack technique rather than a CVE-linked software defect: https://blog.google/security/prompt-injections-web/
- **Active Exploitation:** true, with an important qualification: Google observed malicious indirect-prompt-injection attempts on public websites, including data-theft and destructive-instruction examples. The article says the observed activity was generally low sophistication and does not report confirmed successful compromise; advanced attacks were not observed at significant levels.
- **Threat Actors:** None known. The article names no specific threat actor group, APT, or ransomware campaign; it refers generically to attackers and website authors.
- **Mitigation:** Use layered detection: coarse pattern matching followed by LLM-based intent classification and human validation. Google also recommends hardening AI models and products, pressure-testing them through red teaming, and reporting issues through its AI Vulnerability Reward Program.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/ (official Google Security Blog research post; not a CVE bulletin).

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection occurs when malicious instructions are embedded in external data such as websites, email, or documents that an AI system processes, causing the model to treat attacker-controlled content as instructions. The Google material describes this as a general AI security vulnerability affecting Gemini and Workspace applications rather than a uniquely versioned product flaw.
- **Affected Products:** Google Workspace with Gemini, including Gemini-enabled Gmail and Docs; specific vulnerable versions are not stated.
- **CVSS Score:** :null
- **CVSS Vector:** :null
- **Exploit Available:** false for a Google Workspace-specific PoC or weaponized exploit. Public research and observed web activity demonstrate that generic indirect prompt injection attacks are possible, but no Workspace-specific exploit is identified in the cited materials.
- **Patch Available:** false for a conventional product patch. Google describes continuous policy/configuration updates, model retraining, prompt engineering, and Gemini hardening rather than a released patch for a specific vulnerable version; advisory: https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/
- **Active Exploitation:** true for generic indirect prompt injection activity: Google reports attackers experimenting with IPI on the web and observed prompt-injection attempts. The evidence does not confirm exploitation of a specific Google Workspace product vulnerability.
- **Threat Actors:** None known. Google’s materials do not identify a named APT, ransomware operator, or threat group exploiting a specific Google Workspace flaw.
- **Mitigation:** Google describes layered defenses including prompt-injection classifiers, markdown sanitization and suspicious-URL redaction, explicit user confirmation for sensitive actions, URL sanitization, tool-chaining policies, ML retraining, refined LLM system instructions, Gemini model hardening, and continuous red-team testing.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Google identifies indirect prompt injection as the primary new threat to agentic browsers: malicious instructions embedded in websites, third-party content, or user-generated content can influence the browsing agent's planning and cause unintended actions or sensitive-data exposure. Chrome's design uses alignment checks, prompt-injection detection, origin gating, and confirmation controls to limit such actions.
- **Affected Products:** Google Chrome agentic capabilities, including Gemini in Chrome; no specific vulnerable Chrome version is identified.
- **CVSS Score:** .
- **CVSS Vector:** .
- **Exploit Available:** true — Public demonstrations of indirect prompt injection against agentic browsers exist, including Brave's Perplexity Comet write-up: https://brave.com/blog/comet-prompt-injection. However, no Chrome-specific weaponized exploit is identified in the reviewed sources.
- **Patch Available:** false — No CVE-specific or versioned vendor patch is disclosed for this issue. Google's advisory describes layered product and architectural defenses rather than remediation of a version-specific software vulnerability.
- **Active Exploitation:** false for a Chrome-specific implementation. The Chrome advisory does not report confirmed in-the-wild exploitation of Chrome's agentic capabilities, although separate research has documented real-world indirect prompt-injection activity against AI agents more generally.
- **Threat Actors:** None known. Google's post does not attribute the indirect prompt-injection threat to any named APT, ransomware operator, or other threat-actor group.
- **Mitigation:** Use Chrome's built-in agentic safeguards, including alignment critics, prompt-injection detection, Agent Origin Sets/origin gating, restricted navigation, confirmation prompts for sensitive actions, and user pause/takeover/stop controls. Keep Chrome updated because Google states that Chrome auto-update is used to deliver security improvements and fixes.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2025-48530 involved a linear buffer overflow or out-of-bounds access caused by incorrect bounds checks in CrabbyAVIF's unsafe-Rust code. The flaw could theoretically enable remote code execution in combination with other bugs, but Android's Scudo hardened allocator used guard pages that converted the condition into a crash and made it non-exploitable.
- **Affected Products:** Google Android 16; CrabbyAVIF, an AVIF parser/decoder implemented in unsafe Rust. Google states that the vulnerability was fixed before release and never shipped in a public Android release.
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false. No public proof-of-concept or weaponized exploit was identified; Google states that Android's Scudo allocator rendered the flaw non-exploitable and that it never entered a public release.
- **Patch Available:** true. Google fixed the issue before public release and linked the source patch from its official security post; the Android security bulletin reference is https://source.android.com/security/bulletin/2025-08-01. This was a pre-release fix rather than a patch issued for a publicly affected Android version.
- **Active Exploitation:** false. No confirmed in-the-wild exploitation of CVE-2025-48530 has been reported; the CVE record lists exploitation as none, and Google says the vulnerability never made it into a public release.
- **Threat Actors:** None known.
- **Mitigation:** Because Google fixed the issue before it shipped publicly, no end-user workaround for an affected public Android release is identified. Keep Android devices on current security updates; Scudo guard pages and crash reporting improvements provide additional platform protection.
- **Vendor Advisory:** https://source.android.com/security/bulletin/2025-08-01

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection embeds attacker-controlled instructions in external content such as emails, documents, websites, or calendar invitations. When an AI system processes that content, the instructions may cause it to exfiltrate data, generate malicious URLs, or perform other unauthorized actions.
- **Affected Products:** Google Gemini 2.5 models, Gemini app, and Gemini in Google Workspace applications/workflows, including Gmail, Docs, and Calendar-related actions; no specific vulnerable version range was identified.
- **CVSS Score:** /
- **CVSS Vector:** /
- **Exploit Available:** true. Public research and demonstrations of indirect prompt injection exist, including a demonstration against Perplexity Comet: https://brave.com/blog/comet-prompt-injection
- **Patch Available:** false. No standalone, version-specific security patch was announced for this issue; Google's response is a defense-in-depth strategy built into Gemini and related services. Advisory: https://blog.google/security/mitigating-prompt-injection-attacks
- **Active Exploitation:** true for the broader indirect-prompt-injection technique. Google reported attackers experimenting with malicious IPI content on the public web and a 32% relative increase in malicious detections between November 2025 and February 2026, although the activity was low sophistication and not attributed to named groups: https://blog.google/security/prompt-injections-web/
- **Threat Actors:** None known. Google reported individual website authors experimenting with indirect prompt injection, but no named APT, ransomware operator, or coordinated campaign was identified.
- **Mitigation:** Google describes layered defenses including Gemini 2.5 model hardening, prompt-injection classifiers, security-oriented instruction reinforcement, markdown and suspicious-URL sanitization, external-image blocking, contextual user confirmation, and end-user security notifications. Organizations should restrict AI-agent permissions, require confirmation for high-impact actions, and treat external content as untrusted.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks

---

## 9. 🟠 Zero-Day — Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite

**CVE:** `CVE-2025-66376` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Tue, 21 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a>

> Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite Executive summary A group of Russian state-supported cyber actors has been targeting and compromising various Western government and commercial organizations using the Zimbra Collaboration Suite (ZCS) software since at least July 2025. The Russian state-supported advanced persistent threat …

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2025-66376 is a stored cross-site scripting vulnerability in Zimbra's Classic UI caused by improper sanitization of CSS @import directives in HTML email. A malicious message can execute JavaScript when viewed in Zimbra webmail, enabling theft of mailbox contents and address-book data.
- **Affected Products:** Zimbra Collaboration (ZCS) 10.0 before 10.0.18; Zimbra Collaboration (ZCS) 10.1 before 10.1.13.
- **CVSS Score:** 7.2
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:L/A:N
- **Exploit Available:** true — CISA reports that LAUNDRY BEAR used a novel weaponized exploit for CVE-2025-66376, which was a zero-day when first exploited. Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a
- **Patch Available:** true — Zimbra released fixes in ZCS 10.1.13 and 10.0.18. Vendor advisory: https://wiki.zimbra.com/wiki/Zimbra_Security_Advisories?cve=title
- **Active Exploitation:** true — CISA reports that LAUNDRY BEAR has successfully exploited CVE-2025-66376 in an ongoing phishing campaign targeting Zimbra users. Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a
- **Threat Actors:** LAUNDRY BEAR, also known as Void Blizzard, CL-STA-1114, and TA488.
- **Mitigation:** Immediately upgrade to ZCS 10.1.13 or 10.0.18. If patching is not immediately possible, have users access mail through alternative clients and avoid the Classic ZCS webmail interface; monitor internet-facing ZCS systems and connected workstations. Source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a
- **Vendor Advisory:** https://wiki.zimbra.com/wiki/Zimbra_Security_Advisories?cve=title

---

## 10. 🟡 High Severity — Critical Orkes Conductor Vulnerability Exploited in Attacks

**CVE:** `CVE-2026-58138` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://www.securityweek.com/critical-orkes-conductor-vulnerability-exploited-in-attacks/>

> CVE-2026-58138 is an unauthenticated remote code execution vulnerability that attackers can exploit via inline workflow definitions. The post Critical Orkes Conductor Vulnerability Exploited in Attacks appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** This is an unauthenticated remote-code-execution flaw in Orkes Conductor: attackers can submit inline workflow definitions containing malicious JavaScript or Python expressions to the workflow API before authentication. Unsandboxed GraalVM evaluators configured with broad host access can then be abused to execute arbitrary operating-system commands.
- **Affected Products:** Orkes Conductor / conductor-oss Conductor 3.21.21 through 3.30.1 (versions before 3.30.2).
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true — A public Exploit-DB exploit is available at https://www.exploit-db.com/exploits/52633, and public GitHub PoCs are also reported, including https://github.com/BiiTts/CVE-2026-58138-Conductor-Unauth-RCE.
- **Patch Available:** true — Version 3.30.2 is identified as the fixed release, with fixes including “Restrict graaljs further” and evaluator host-access restrictions. Official release: https://github.com/conductor-oss/conductor/releases/tag/v3.30.2
- **Active Exploitation:** true — SecurityWeek reports that CVE-2026-58138 has been exploited in attacks, and FortiGuard reports active targeting of vulnerable Orkes Conductor servers.
- **Threat Actors:** None known.
- **Mitigation:** Upgrade affected deployments to Conductor 3.30.2 or later. The listed fixes restrict GraalJS access and deny dangerous class/host access in the JavaScript and Python evaluators; until upgraded, restrict exposure of the workflow API and enforce authentication and network-level access controls.
- **Vendor Advisory:** .

---

## 11. 🟡 High Severity — Grav CMS vulnerable to remote code execution via .zip file upload

**CVE:** `CVE-2026-72819` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-r94f-hx44-8jqf>

> ### Summary

A logged-in user can run any command on the server. A settings field can fill itself by calling one of Grav&#x27;s built-in routines, and a safety check is supposed to allow only harmless ones. The check only recognises a routine when its name is written as one piece of text; named as a pair of values instead, it is not examined at all and is passed as safe. Pointing such a field at t…

---

## 12. 🟡 High Severity — Grav: Missing admin.super guard on core group blueprint access field allows admin.users operator to escalate to super-admin

**CVE:** `CVE-2026-75837` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-xhfv-7758-r9hx>

> ## Summary
The core Flex group blueprint `system/blueprints/user/group.yaml` (access field, lines 48-55) omits the `security@: admin.super` field guard that its sibling account blueprint carries (`account.yaml:131/138/150`, added by the CVE-2026-42613 fix). A delegated non-super operator holding `admin.users.update` can therefore save a group whose `access` map contains `admin.super: true`, which …

---

## 13. 🟡 High Severity — Grav: Blueprint dynamic-data bare-function branch is denylist-gated and omits error_log, giving arbitrary file write

**CVE:** `CVE-2026-75827` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-f8wv-xp27-6gq7>

> ## Affected versions and vulnerable location

- Confirmed on grav core at `78ebfc1` (tag 2.0.13).
- Sinks:
  - `system/src/Grav/Common/Data/Blueprint.php:455-458` `call_user_func_array($o, $params)` (bare-function dynamic-data provider).
  - Twin: `system/src/Grav/Framework/Flex/FlexDirectory.php:936-938` `call_user_func_array($function, $params)`.
- Validation gate: `Blueprint::isSafeDynamicCall(…

---

## 14. 🟡 High Severity — Soup Sieve: Polynomial-time ReDoS (O(n²)) in the `IDENTIFIER` / `VALUE` selector sub-patterns

**CVE:** `CVE-2026-86000` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-gjv8-xp57-g29c>

> ## Summary

soupsieve compiles CSS selector strings with a set of hand-written regular expressions. The shared `IDENTIFIER` sub-pattern (also embedded in `VALUE`, and therefore in attribute selectors) places two adjacent quantified groups over overlapping character classes: `(?:[classA]|ESC)+(?:[classB]|ESC)*`, where both classes match ordinary identifier characters such as `a`. When a selector co…

---

## 15. 🟡 High Severity — Steeltoe: Header-forwarded client cert lacks proof of private-key possession

**CVE:** `CVE-2026-81868` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-5mq7-rwhj-4fh9>

> ### Summary

When Steeltoe&#x27;s certificate-based authorization (`UseCertificateAuthorization`) is configured, the default configuration of the middleware relies on the `X-Client-Cert` HTTP header to identify the client certificate, without verifying private-key possession. This header is not stripped by common Cloud Foundry routers (like Gorouter or Envoy) on inbound requests.

### Impact

An a…

---

## 16. 🟡 High Severity — Steeltoe.Discovery.Consul: malformed 'secure' metadata aborts service instance lookup (DoS)

**CVE:** `CVE-2026-81516` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-67c9-f6v2-qv86>

> ## Summary

Steeltoe&#x27;s Consul discovery client parses the `secure` metadata field on each registered service instance using `bool.Parse`, which throws on any value other than `true` or `false`. A single service instance registered with a malformed `secure` value (for example `yes` or `1`) aborts construction of the entire instance list for that service, making the service undiscoverable. When…

---

## 17. 🟡 High Severity — Jupyter Server: 5xx request logging leaks token-bearing Referer header values

**CVE:** `CVE-2026-86049` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-c3mw-737p-c7g2>

> ### Summary

When a request returns a 500, `jupyter_server/log.py` logs a small JSON block of request headers. 

The Referer header was copied into it as-is, so a token in the Referer URL ended up in the logs in plain text.

### Impact

Anyone who can read the server logs can pick tokens out of these 500 entries. Tokens end up in the Referer during normal token-based login and launch flows.

Affec…

---

## 18. 🟡 High Severity — Grav: UserInterface offsetget/offsetexists allow-listed in Twig sandbox let editor-authored content leak hashed_password and 2FA secrets via offsetGet()

**CVE:** `CVE-2026-76839` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-3jhr-mxmx-38cx>

> ## Summary

`system/config/security.yaml`&#x27;s Twig sandbox policy allow-lists `offsetget` and
`offsetexists` for `Grav\Common\User\Interfaces\UserInterface`. The concrete
`Grav\Common\User\DataUser\User` class does not filter which fields `offsetGet()`
returns, so any sandboxed template with access to a `User` object can read
`hashed_password`, `secret` (2FA seed), and `twofa_secret` directly, …

---

## 19. 🟡 High Severity — Grav: config_denied_paths default list omits `system`, exposing real secrets (e.g. system.cache.redis.password) via the Twig sandbox when config_access is enabled

**CVE:** `CVE-2026-76846` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-xjw5-q542-3vmr>

> ## Summary

`system/config/security.yaml`&#x27;s default `twig_sandbox.config_denied_paths` list
(`plugins`, `streams`, `security`, `backups`, `scheduler`) omits the `system` prefix.
When an operator enables the documented, non-default `twig_content.config_access: true`
setting (intended to safely expose low-sensitivity values like `site.title` to
editor-authored Twig content), any real secret sto…

---

## 20. 🟡 High Severity — Grav: The system, site, and theme Twig variables bypass the content sandbox entirely and are never covered by config_denied_paths

**CVE:** `CVE-2026-72698` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-p597-crqc-m349>

> ## Summary

`Grav\Common\Twig\Twig::init()` unconditionally puts the raw `system`, `site`, and `theme` config arrays into `$this-&gt;twig_vars`. `Twig::processPage()` builds the variables for the sandboxed, editor-authored page-content render by copying that same base array (`$sandbox_vars = $twig_vars;`) and replacing only the `config` key with a filtered `SandboxConfig` facade. The `system`, `si…

---

## 21. 🟡 High Severity — Grav: Non constant time nonce comparison in Utils::verifyNonce() used for CSRF protection

**CVE:** `CVE-2026-72701` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-38p6-h87p-r4cg>

> ## Summary

`Grav\Common\Utils::verifyNonce()`, the core function Grav and its plugins use to validate CSRF nonces, compares the submitted nonce to the expected value with PHP&#x27;s `===` operator instead of `hash_equals()`. `===` on strings short circuits at the first differing byte, so the comparison time leaks how many leading bytes of a guess are correct. This is CWE-208, Observable Timing Di…

---

## 22. 🟡 High Severity — Chamilo LMS CStudio upload flow allows unauthenticated remote code execution

**CVE:** `CVE-2026-45140` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-g4c3-4g96-6g4m>

> ### Impact
Ability to run arbitrary code on the server without authentication.

---

## 23. 🟡 High Severity — Fulgur: Unbounded page slicing from attacker-controlled CSS height causes denial of service

**CVE:** `CVE-2026-68523` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-j5cx-ph8g-95v3>

> `fulgur` converts untrusted HTML/CSS into PDF, commonly on a server that
processes input supplied by many tenants. In versions prior to 0.19.0, a
body-direct child whose CSS-resolved height greatly exceeds the page height was
sliced into one fragment per page with **no upper bound**.

The height is taken directly from attacker-controlled HTML/CSS (`height`, `vh`
units), so a few bytes such as:

``…

---

## 24. 🟡 High Severity — Steeltoe.Management.Endpoint: HttpExchanges URI masking leaks query-string secrets

**CVE:** `CVE-2026-75523` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-8phw-xrj9-cpqp>

> ## Summary

Steeltoe&#x27;s `/actuator/httpexchanges` endpoint records and displays request URIs after passing them through `MaskedUri`. The masking only covers the `UserInfo` portion of the URI (inline `user:password@host` credentials) and does not inspect the query string. With `IncludeQueryString` enabled by default, any secrets carried in query strings (for example: OAuth tokens, password-rese…

---

## 25. 🟡 High Severity — Grav: Stored XSS via Markdown audio/video media <source> URL

**CVE:** `CVE-2026-75831` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-6qw9-4vv5-jr97>

> **Target:** github.com/getgrav/grav  
**Affected resource:** `Grav\Common\Media\Traits\AudioMediaTrait` / `VideoMediaTrait` `sourceParsedownElement()` — verified on 2.0.13 (latest stable) and `develop` HEAD `5a7070f`  
**Severity:** Medium (~6.9 CVSS:3.1/AV:N/AC:L/PR:H/UI:R/S:C/C:H/I:L/A:N — anchored to the sibling script-XSS advisory [CVE-2026-42841](https://github.com/getgrav/grav/security/advis…

---

## 26. 🟡 High Severity — AsyncHttpClient doesn't verify SCRAM and Digest mutual-authentication responses

**CVE:** `CVE-2026-85716` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-fj9w-c36g-h5x8>

> ### Impact
For SCRAM, and for Digest with mutual authentication, the client computes the server&#x27;s verification value (the SCRAM ServerSignature, or the Digest rspauth) but does not act on the result. If the value is present and does not verify, the client only logs it and still delivers the response to the application as a successful, authenticated result. A server that never proved knowledge…

---

## 27. 🟡 High Severity — oras-go: Blind SSRF via unvalidated Link header URL in pagination allows internal network probing

**CVE:** `CVE-2026-85732` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-h7vf-4x9w-h99v>

> ## Summary

oras-go&#x27;s pagination helper `parseLink()` in `registry/remote/utils.go` follows the `Link` response header from a registry without validating the URL&#x27;s host or scheme. When a malicious registry returns a `Link` header containing an absolute URL pointing to an arbitrary host (e.g., a cloud metadata endpoint), the client makes GET requests to that host from the victim&#x27;s ne…

---

## 28. 🟡 High Severity — Kestra: SSRF via Pebble http() function allows unauthenticated access to internal services & cloud metadata

**CVE:** `CVE-2026-73247` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-r56g-q4p6-m3p6>

> ### Summary
The Pebble template engine&#x27;s `http()` function in Kestra OSS accepts user-controlled URLs without any validation, allowing Server-Side Request Forgery (SSRF) attacks. An unauthenticated attacker can import a malicious Flow YAML and execute it to access internal services, cloud metadata endpoints (AWS 169.254.169.254), or localhost services. The vulnerability affects all Kestra OSS…

---

## 29. 🟡 High Severity — RabbitMQ amqp091-go: Protocol Desynchronization and Frame Injection via Integer Overflow in readLongstr

**CVE:** `CVE-2026-77411` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-c5pq-fr2g-9jpf>

> **Summary**

A critical stream desynchronization vulnerability has been identified in the AMQP wire-protocol parser. When parsing a long string (`readLongstr`) within a table field, providing a length that exceeds the maximum signed 32-bit integer (`2^31 - 1`, or roughly `2.1` GiB) triggers an improper error-handling condition. The parser abruptly aborts the read and returns a success status (`&qu…

---

## 30. 🟡 High Severity — RabbitMQ amqp091-go: Silent Data Truncation and State Corruption via Shortstr Integer Overflow

**CVE:** `CVE-2026-77408` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-j497-x9hr-x34x>

> ## Summary
A data integrity and protocol corruption vulnerability exists in the AMQP client&#x27;s property serialization logic. When encoding AMQP short string (`shortstr`) fields—such as identifiers, routing strings, and content metadata—the length of the string is explicitly cast to a fixed-size 8-bit unsigned integer (`uint8`). 

If an application provides a property string exceeding 255 bytes…

---

## 31. 🟡 High Severity — RabbitMQ amqp091-go: Missing Explicit TLS Minimum Version Configuration In URI Parser

**CVE:** `CVE-2026-77405` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-33mj-cw25-m34h>

> ## Summary
A structural security weakness exists in the AMQP client&#x27;s TLS configuration generator (`tlsConfigFromURI`). When constructing a `*tls.Config` object from an `amqps://` connection URI, the library initializes the structure without explicitly defining the `MinVersion` field. 

While modern versions of the Go compiler toolchain (Go 1.18+) default the implicit minimum version to TLS 1…

---

## 32. 🟡 High Severity — RabbitMQ amqp091-go: Connection Configuration Overwrite via Unsanitized TLS Path Parameter Injection

**CVE:** `CVE-2026-77404` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-465g-fh3v-9jw4>

> ## Summary
A query parameter injection vulnerability exists in the AMQP client&#x27;s connection URI formatting logic. When generating or parsing connection URIs, TLS-related filesystem paths (such as certificates or keys) are appended directly to the URI&#x27;s query string using string concatenation rather than secure URL encoding via functions like `url.QueryEscape`.

If an application handles …

---

## 33. 🟡 High Severity — Zope AccessControl vulnerable to information disclosure through Python string `format` and `format_map` functions

**CVE:** `CVE-2026-77401` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-pq59-9fq7-m886>

> ### Impact
Python&#x27;s string `format` functionality allows someone controlling the format string to &quot;read&quot; objects accessible (recursively) via attribute access and subscription from accessible objects. Those attribute accesses and subscriptions use Python&#x27;s full blown `getattr` and `getitem`, not the policy restricted `AccessControl` variants `_getattr_` and `_getitem_`. This ca…

---

## 34. 🟡 High Severity — Umbraco: Delivery API leaks protected (Public Access) content through Content Picker / Multi-Node Tree Picker expansion

**CVE:** `CVE-2026-69197` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-wr57-hqmp-fgvh>

> The Content Delivery API enforces member / Public Access protection only at the controller layer, against the node that is directly requested. When a public (unprotected) node references a protected node through a Content Picker or Multi-Node Tree Picker (including those nested inside Block List, Block Grid, or Rich Text Editor blocks), the Delivery API expands and serializes the protected node wi…

---

## 35. 🟡 High Severity — Critical Docker Sandboxes Flaw Lets Malicious Guest Code Read and Modify macOS Host Files

**CVE:** `CVE-2026-77179` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://thehackernews.com/2026/09/critical-docker-sandboxes-flaw-lets.html>

> Malicious code running inside a Docker Sandboxes virtual machine on macOS could escape the project directory shared into it and read or change files anywhere else on the host, Docker warns in a security announcement on September 15.

The escape runs with the rights of the host account that runs the virtual machine. The flaw, CVE-2026-77179, is rated Critical, affects versions

---

## 36. 🟡 High Severity — AsyncSSH: asyncio event-loop freeze via SSH maximum packet size = 0 in SSH_MSG_CHANNEL_OPEN / OPEN_CONFIRMATION

**CVE:** `CVE-2026-62949` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-rw4j-r22c-9gc3>

> ## Summary

A malicious SSH server can wedge an AsyncSSH **client**, and an authenticated
client can wedge an AsyncSSH **server**, by sending a channel `maximum packet
size` of `0` in `SSH_MSG_CHANNEL_OPEN_CONFIRMATION` (server→client) or
`SSH_MSG_CHANNEL_OPEN` (client→server). AsyncSSH stores the peer-supplied value
verbatim with no lower-bound check; the first time channel data is written,
`SSHC…

---

## 37. 🟡 High Severity — Wire: Unauthenticated decoder crash via 32-bit length integer overflow in ByteArrayProtoReader32 (incomplete fix of CVE-2026-45799)

**CVE:** `CVE-2026-63126` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-9rm7-3qhh-h2mc>

> Wire&#x27;s protobuf decoders did not consistently validate attacker-controlled length-delimited sizes against the current reader bounds before computing cursor, limit, or pointer positions.

In the Kotlin runtime, `ProtoAdapter.decode(ByteArray)` and `ProtoAdapter.decode(ByteString)` use the `ProtoReader32` fast path implemented by `ByteArrayProtoReader32`. In `ByteArrayProtoReader32.internalNext…

---

## 38. 🟡 High Severity — @cyclonedx/cyclonedx-npm: Shell Injection via Unsanitized --workspace Argument on Windows

**CVE:** `CVE-2026-71538` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-q69g-4hcv-6jg4>

> ## Summary

A **Windows-specific** command injection vulnerability exists in `@cyclonedx/cyclonedx-npm` when the CLI is invoked with the `--workspace &lt;value&gt;` option.  
User-supplied `--workspace` values can be passed to a shell command without proper neutralization on the Windows fallback execution path, enabling attackers to inject arbitrary OS commands.  

The vulnerability was fixed in v…

---

## 39. 🟡 High Severity — Nuxt OG Image has unauthenticated SSRF via `fonts[].path` URL parameter

**CVE:** `CVE-2026-61793` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-q8hw-4fvp-9rwv>

> ### Summary
`nuxt-og-image` exposes an **unauthenticated HTTP endpoint** at `/_og/d/**` that base64url-decodes and `JSON.parse`s a `fonts` URL segment, then passes each `fonts[i].path` value directly into `fetch()` server-side **without any URL validation** (no scheme allowlist, no loopback/RFC1918 block, no host allowlist, no DNS rebinding mitigation).

Under the module&#x27;s documented default …

---

## 40. 🟡 High Severity — Critical Unbound DNSSEC Validator Flaw Could Allow RCE via a Malicious DNS Zone

**CVE:** `CVE-2026-81642` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://thehackernews.com/2026/09/critical-unbound-dnssec-validator-flaw.html>

> Every release of the Unbound DNS resolver before 1.26.1 has a critical heap overflow in its DNSSEC validator, maintainer NLnet Labs said in an advisory on Wednesday.

An attacker who controls a malicious zone and queries a vulnerable resolver can trigger it, enabling remote code execution.

Unbound 1.26.1, released the same day, fixes the bug, tracked as CVE-2026-81642, along with

---

## 41. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
