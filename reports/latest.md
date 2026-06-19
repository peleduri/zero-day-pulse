# Zero Day Pulse

> **Generated:** 2026-06-19 19:25 UTC &nbsp;|&nbsp; **Total:** 28 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 11 &nbsp;|&nbsp; 🟡 High: 17 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is an unauthenticated path-traversal vulnerability (CWE-22) in the SimpleHelp web application (toolbox functionality). The vulnerable components fail to properly sanitize user-supplied input in HTTP requests, allowing a remote, unauthenticated attacker to inject path-traversal sequences (e.g. 'filepath=../../../../../../etc/passwd') and download arbitrary files from the SimpleHelp host. Exposed files include the server configuration (containing secrets and hashed user/technician passwords), operating-system files such as /etc/passwd, and sensitive keys including /root/.ssh/id_rsa. With the harvested credentials (and chained with CVE-2024-57728 and CVE-2024-57726) the attacker can log in with high privileges, upload and execute files, and fully compromise the SimpleHelp server and downstream customer systems.
- **Affected Products:** SimpleHelp Remote Support / Remote Monitoring and Management (RMM) software — version 5.5.7 and all earlier releases. Vendor also shipped point-fix patches on the 5.4.x branch (5.4.10) and 5.3.x branch (5.3.9).
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true — public proof-of-concept available. GitHub repository 'imjdl/CVE-2024-57727' (Python PoC / vulnerability checker): https://github.com/imjdl/CVE-2024-57727
- **Patch Available:** true — SimpleHelp released version 5.5.8 (and back-ported fixes 5.4.10 and 5.3.9) within ~2 days of being notified, before public disclosure. Patches / advisory: https://guides.simple-help.com/kb---security-vulnerabilities-01-2025 ; https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know
- **Active Exploitation:** true — confirmed. CISA added CVE-2024-57727 to the Known Exploited Vulnerabilities (KEV) Catalog on 2025-02-13 and published #StopRansomware advisory AA25-163A on 2025-06-12 documenting in-the-wild ransomware exploitation since January 2025, including the compromise of a utility billing software provider via a SimpleHelp-using MSP. Independent reporting of the DragonForce campaign: SecurityWeek (2025-05-27) and Arctic Wolf (campaign observed from 2025-01-22).
- **Threat Actors:** DragonForce ransomware actors. CISA advisory AA25-163A (2025-06-12) attributes active exploitation of CVE-2024-57727 to DragonForce, who chained it with CVE-2024-57728 and CVE-2024-57726 against a managed service provider (MSP) running SimpleHelp RMM and used the access to reach downstream customers — including a utility billing software provider — for double-extortion ransomware compromises. Independent confirmation: SecurityWeek, 'DragonForce Ransomware Hackers Exploiting SimpleHelp Vulnerabilities' (2025-05-27).
- **Mitigation:** (1) Upgrade immediately: SimpleHelp 5.5.8 or later (or 5.4.10 on the 5.4 branch, 5.3.9 on the 5.3 branch). (2) Rotate all credentials — SimpleHelp Administrator password, every Technician account password, and any API tokens in use. (3) Restrict network access — IP-allowlist Technician/Administrator logins, IP-allowlist API requests, and firewall the SimpleHelp server so only expected sources can reach it. (4) Hunt for compromise: look for newly created executables with three-letter filenames (e.g. aaa.exe, bbb.exe) dated after January 2025, unexpected SimpleHelp/Remote Access Service reconfiguration, and alerts on Administrator logins / failed logins / configuration changes. (5) For confirmed compromises — disconnect the host from the internet, reinstall from clean media, and restore only from clean offline backups.
- **Vendor Advisory:** https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — In Other News: Apple Patches Beats Eavesdropping Flaw, DOT Closes Delta CrowdStrike Probe, AWS Continuum

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://www.securityweek.com/in-other-news-apple-patches-beats-eavesdropping-flaw-dot-closes-delta-crowdstrike-probe-aws-continuum/>

> Other noteworthy stories that might have slipped under the radar: Android TV botnet Popa linked to Israeli firm, Velvet Ant maintained decade-long stealth, unpatched GCP Config Connector flaw enables takeover. The post In Other News: Apple Patches Beats Eavesdropping Flaw, DOT Closes Delta CrowdStrike Probe, AWS Continuum appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** ConfigConfusion is a confused-deputy vulnerability (CWE-441) in Google Cloud Config Connector. An attacker with access to any Kubernetes namespace managed by Config Connector submits a malicious IAMPolicyMember custom resource targeting organization-level identifiers. Config Connector invokes GCP's resourcemanager.organizations.setIamPolicy using its own privileged service account without verifying the Kubernetes user's equivalent GCP permissions. Because IAM trusts the Config Connector service identity, the attacker-controlled policy is accepted, allowing the attacker to grant themselves roles/owner on the GCP Organization and achieve full takeover of every project, folder, and resource beneath it.
- **Affected Products:** Google Cloud Config Connector for Kubernetes (GoogleCloudPlatform/k8s-config-connector), all versions (including 1.149.x release line) — every GCP organization running Config Connector is exposed.
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Exploit Available:** true. A public PoC ('org-takeover.yaml' applied via kubectl apply to create an IAMPolicyMember granting roles/owner at Organization scope) is published by Justin O'Leary at https://olearysec.com/research/config-connector-authorization-bypass/
- **Patch Available:** false. Google has not released a patch and considers the behavior 'working as intended' rather than awarding a bounty.
- **Active Exploitation:** false. No confirmed in-the-wild exploitation has been reported. The vulnerability was publicly disclosed on June 18, 2026, and as of June 19, 2026 no exploitation campaigns have been observed in cited sources.
- **Threat Actors:** None known.
- **Mitigation:** Google has not issued a patch or workaround and considers the behavior 'working as intended'. Recommended hardening: (1) Restrict who can create/update IAMPolicyMember and IAMPartialPolicy custom resources in Kubernetes clusters running Config Connector (principle of least privilege at the K8s RBAC layer); (2) Audit existing IAMPolicyMember / IAMPartialPolicy resources for unexpected organization- or folder-level targets; (3) Treat any Kubernetes namespace writable by untrusted users as a potential source of Org-level IAM changes; (4) Monitor GCP IAM audit logs (and Config Connector logs) for IAMPolicy/PolicyBindings applied at the Organization node by the Config Connector service account. Reference: https://cloud.google.com/config-connector/docs/how-to/configure-iam-permissions
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — CISA: Splunk Enterprise flaw actively exploited, patch by Sunday

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-splunk-enterprise-flaw-actively-exploited-patch-by-sunday/>

> CISA has urged U.S. federal agencies to secure their systems by Sunday against a critical Splunk Enterprise vulnerability that is being exploited in attacks. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated arbitrary file creation and truncation in a PostgreSQL sidecar service endpoint in Splunk Enterprise that can be chained to achieve remote code execution by writing/truncating files via the sidecar API.
- **Affected Products:** Splunk Enterprise <10.2.4, <10.0.7
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Threat actors unknown
- **Mitigation:** If immediate patching isn't possible, restrict network access to the PostgreSQL sidecar port (bind/firewall to localhost 127.0.0.1) and ensure the sidecar is not exposed to non-loopback interfaces; apply vendor patch immediately.
- **Vendor Advisory:** https://advisory.splunk.com/advisories/SVD-2026-0603

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when AI systems process external content (websites, documents, emails) containing malicious instructions which the AI may follow; attackers seed hidden or visible prompt payloads on the public web to manipulate agent behavior.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses: input/output validation and sanitization, suspicious URL redaction, red‑team testing, human oversight, AI Vulnerability Reward Program participation, and Google Workspace continuous mitigations.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack technique that injects malicious instructions into data sources or tools that an LLM uses while completing a user query; it can occur without direct user input (e.g., crafted emails, documents, web pages, or other integrated data) and causes the model or agentic automation to follow attacker‑supplied instructions or disclose sensitive data.
- **Affected Products:** Google Workspace (Gemini in Workspace), Gemini Enterprise
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Layered defenses including input/output validation and sanitization, provenance and source trust signals, model-level instruction filtering, capability and tool access restrictions, human review / human-in-the-loop gating for risky actions, continuous web sweeps for IPI patterns, and tight Workspace/Gemini tenant controls.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection allows malicious web content to influence agentic browser prompts and chain with other flaws (e.g., GeminiJack/CVE-2025-54131) to trigger a zero‑click compromise; the attack uses malicious pages to inject prompts or data that agentic agents act upon without user intent.
- **Affected Products:** Google Chrome (agentic/Gemini integration)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true — https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability
- **Patch Available:** true — http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Layered defenses in Chrome: deterministic rule filters, model‑level protections, origin restrictions, restricting agent actions; avoid untrusted sites and disable agentic features until patched.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is an attack class in which adversaries embed hidden malicious instructions inside external content that an LLM/agent retrieves or is given as context (email bodies, Google Docs, Drive files, Chat messages, calendar invites, web pages). When the Gemini assistant processes that content, the hidden instructions hijack the model's behavior to exfiltrate user data, invoke tools/connectors, or perform other unauthorized actions on the user's behalf. Unlike direct prompt injection (where the attacker is the user), indirect injection plants instructions in retrieved content. The blog notes Gemini does not render external images, preventing the CVE-2025-32711 'EchoLeak' zero-click image-attribute exfiltration technique from working against Gemini.
- **Affected Products:** Google Gemini (app), Gemini in Google Workspace (Gmail, Google Calendar, Google Docs, Google Drive, Google Chat), Gemini 2.5. No earlier Gemini model versions were explicitly identified as affected in the post.
- **CVSS Score:** CVSS score unavailable. No CVSS score is assigned by Google for this class of attack against Gemini in the June 13, 2025 blog post.
- **CVSS Vector:** CVSS vector unavailable. The Google Security Blog post does not assign a CVE or CVSS vector to its own indirect prompt injection defense strategy against Gemini; the only CVE cited (CVE-2025-32711) refers to a competitor product (Microsoft Copilot).
- **Exploit Available:** true. Multiple public PoCs and exploits exist. Example sources: SafeBreach Labs (https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/), Miggo (https://www.miggo.io/post/weaponizing-calendar-invites-a-semantic-attack-on-google-gemini), Noma Labs 'GeminiJack' (https://noma.security/noma-labs/geminijack/).
- **Patch Available:** true. The layered defenses described in the blog post are already shipped to Gemini and Gemini in Workspace. Advisory URL: http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html. Companion: https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini; https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/; https://deepmind.google/blog/advancing-geminis-security-safeguards/.
- **Active Exploitation:** true. The blog post acknowledges indirect prompt injection is a real-world in-the-wild threat. Independent third-party reports confirm active exploitation targeting Gemini: SafeBreach Labs (https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/), Miggo (https://www.miggo.io/post/weaponizing-calendar-invites-a-semantic-attack-on-google-gemini), Noma Labs 'GeminiJack' (https://noma.security/noma-labs/geminijack/), Forcepoint hidden-website-code research (http://hackread.com/hackers-hidden-site-instruction-attack-ai-assistants), and Gemini-in-Workspace prompt injection via GitHub Actions (https://www.reddit.com/r/programming/comments/1pe3cew/prompt_injection_within_github_actions_google/).
- **Threat Actors:** None known. The blog post references threat actors only in generic terms without naming any specific APT groups, campaigns, or ransomware operators.
- **Mitigation:** Google's layered mitigation strategy: (1) Model hardening via adversarial-data training (Gemini 2.5); (2) prompt-injection content classifiers scanning incoming emails/documents; (3) security 'thought reinforcement' system-prompt instructions; (4) markdown sanitization and suspicious-URL redaction (Google Safe Browsing, blocking external image rendering); (5) User Confirmation/Human-in-the-Loop (HITL) for sensitive or irreversible actions (e.g., deleting a calendar event); (6) end-user security notifications with contextual in-product warnings and 'Learn more' links when an attack is blocked.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC‑linked state‑sponsored actors target large backbone, provider edge (PE) and customer edge (CE) routers, leveraging compromised devices and trusted connections to pivot. They often modify router firmware or configuration to maintain persistent, long‑term access for espionage and botnet activity.
- **Affected Products:** major backbone routers, provider edge (PE) routers, customer edge (CE) routers, compromised network devices
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Follow CISA mitigations: inventory network devices, isolate management interfaces, enforce strong authentication (multifactor where possible), apply vendor firmware updates when available, restrict network management protocols, monitor for anomalous routing/configuration changes, and follow guidance in the advisory for simulation and mitigation.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Unit 26165 employed spear‑phishing (malicious attachments and credential phishing), exploitation of internet‑facing services (including VPNs and CVE‑2023‑23397 in Outlook, CVE‑2023‑38831 in WinRAR, CVE‑2020‑12641/35730 in Roundcube), credential‑guessing, and abuse of IP‑camera/SOHO device interfaces. Exploitation of Outlook's NTLM exposure allowed remote code execution, while WinRAR archive parsing and Roundcube webmail flaws enabled RCE/XSS. After compromise, actors harvested credentials, exfiltrated AD data, created scheduled tasks, and deployed malware such as HEADLACE and MASEPIE.
- **Affected Products:** Microsoft Outlook (CVE-2023-23397), WinRAR (CVE-2023-38831), Roundcube Webmail (CVE-2020-12641, CVE-2020-35730), VPN/remote‑access infrastructure, IP cameras and SOHO devices
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a
- **Active Exploitation:** true
- **Threat Actors:** GRU unit 26165 (Russian General Staff Main Intelligence Directorate), tracked as APT28, Fancy Bear, Forest Blizzard, Blue Delta
- **Mitigation:** Apply vendor patches for all referenced CVEs; harden email by disabling NTLM and SMBv1; enforce MFA and strong passwords; segment networks and apply least‑privilege controls; monitor for IOCs such as wevtutil, vssadmin, schtasks; audit and secure IP cameras (change default credentials, restrict RTSP, enable logging); deploy detection rules/YARA signatures provided in the advisory.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

---

## 12. 🟡 High Severity — py7zr: Arbitrary File Write Vulnerability

**CVE:** `CVE-2026-23879` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-q6rc-2cgv-63h7>

> ### Summary
There exists an **arbitrary file write vulnerability** in `py7zr` (1.1.0, latest), which allows symbolic links to be recreated outside the destination directory via crafted malicious symbolic link chains. When using `extractall` to extract an archive, the library restores these symbolic links, linking them to arbitrary directories on the host file system. Subsequent extraction of regul…

---

## 13. 🟡 High Severity — Weekly Metasploit Update: NTLM Relay Priv Esc, MCP Server Integration, Paperclip AI RCE Chain, and more

**CVE:** `CVE-2026-41679` | `CVE-2026-41459` | `CVE-2026-34413` | `CVE-2026-34415` | `CVE-2026-34414` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-19-06-2026>

> This week&#x27;s release includes five new modules, including a full unauthenticated RCE chain for Paperclip AI and a VS Code extension persistence technique. On the post-exploitation side, the new windows/local/ntlm_relay_2_self module coerces the local machine account to authenticate via OpenEncryptedFileRaw (WebDAV), relays that NTLM authentication to a Domain Controller&#x27;s LDAP service, th…

---

## 14. 🟡 High Severity — Nokogiri: XML::Schema on JRuby allows network requests when NONET is set, bypassing CVE-2020-26247

**CVE:** `CVE-2020-26247` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-8678-w3jw-xfc2>

> ### Summary

The `NONET` parse option, which Nokogiri turns on by default for `Nokogiri::XML::Schema` (see [CVE-2020-26247](https://github.com/sparklemotion/nokogiri/security/advisories/GHSA-vr8q-g5c7-m54m)), was not correctly enforced on the JRuby implementation. As a result, a schema parsed with default options could still cause external resources to be fetched over the network, potentially enab…

---

## 15. 🟡 High Severity — ouroboros-ai: Incomplete fix of CVE-2026-47211: untrusted project .env can still reach RCE via omitted execution-routing keys

**CVE:** `CVE-2026-47211` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-jv2h-4p9v-wf5w>

> ### Impact
The CVE-2026-47211 fix (0.39.0) added `_UNTRUSTED_ENV_DENYLIST` to stop an untrusted project-directory `.env` from redirecting execution. The denylist was incomplete — several execution-routing keys of the same RCE class were omitted, so a malicious cloned repo can still reach arbitrary command execution by shipping a `.env` (auto-loaded at import, no review step):

- **Backend config-h…

---

## 16. 🟡 High Severity — Improper neutralization of argument delimiters in AWS Bedrock AgentCore Python SDK install_packages()

**CVE:** `CVE-2026-12530` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-6rfw-mq36-jm8h>

> ### Summary
The AWS Bedrock AgentCore Python SDK (bedrock-agentcore) is an open-source SDK that enables developers to build, deploy, and manage agents on AWS Bedrock AgentCore. An issue exists in the install_packages() method of the Code Interpreter client where crafted package name arguments can bypass input validation and allow a remote authenticated user to execute arbitrary commands within the…

---

## 17. 🟡 High Severity — tract: Arbitrary file read via unsanitized ONNX external_data `location` (path traversal) on model load in tract-onnx

**CVE:** `CVE-2026-55832` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-h668-6x6g-f8r5>

> ### Summary

`tract` (the `tract-onnx` crate) resolves an ONNX tensor&#x27;s external-data `location` by joining it onto the model directory **without any sanitization**. Because `location` comes from the (untrusted) `.onnx` file, a malicious model can make `tract` open and read an **arbitrary local file** at load time, with the file&#x27;s contents flowing into the model&#x27;s tensors / inferenc…

---

## 18. 🟡 High Severity — CedarJava has type confusion vulnerability 

**CVE:** `CVE-2026-55772` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-93g4-m6xv-cmvr>

> ### Summary

CedarJava is an open source Java implementation of the Cedar policy language, used for fine-grained authorization decisions. Under certain circumstances, improper input handling could allow type confusion across the Java-Rust FFI boundary.

### Impact

**Record-to-Entity type confusion across the Java-Rust FFI boundary**

CedarJava sends authorization requests to the Rust cedar-policy…

---

## 19. 🟡 High Severity — guzzlehttp/guzzle: Dot-Only Cookie Domains Match All Hosts

**CVE:** `CVE-2026-55767` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-cwxw-98qj-8qjx>

> ### Impact

`CookieJar` incorrectly accepts cookies with a dot-only `Domain` attribute, such as `Domain=.`, `Domain=..`, `Domain=...`, and whitespace-padded variants such as `Domain= . `. In affected versions, `SetCookie::matchesDomain()` removes leading dots from the cookie domain, normalizing dot-only values to the empty string; `SetCookie::validate()` only rejected a strictly empty domain, so t…

---

## 20. 🟡 High Severity — undici vulnerable to cross-origin request routing via SOCKS5 proxy pool reuse

**CVE:** `CVE-2026-6734` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-hm92-r4w5-c3mj>

> ## Impact

When using `Socks5ProxyAgent`, undici reuses a single connection pool across different origins without verifying that the pool&#x27;s origin matches the requested origin. All requests are dispatched through the pool connected to the first origin, regardless of the intended destination.

This causes cross-origin request routing: credentials and request data intended for origin B are sent…

---

## 21. 🟡 High Severity — NL Portal Backend Libraries: Unauthenticated form resolver forwards the privileged Objecten-API token to a caller-supplied URL (SSRF)

**CVE:** `CVE-2026-55414` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-xm3x-9cfw-jhx4>

> ## Summary

The public GraphQL resolvers `getFormDefinitionByObjectenApiUrl(url)` and the deprecated `getFormDefinitionById(id)` fetch a caller-supplied URL using the **privileged Objecten-API token**. Because the `/graphql` endpoint is `permitAll()` and these resolvers do not declare a `CommonGroundAuthentication` parameter, an **unauthenticated** caller can make the backend issue an outbound req…

---

## 22. 🟡 High Severity — canto-saas-api: OAuth credentials exposed in URL query string and exception messages

**CVE:** `CVE-2026-55375` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-37pm-83g7-r22v>

> ## Summary

  In affected versions, the OAuth2 token request sends `app_id`, `app_secret`,
  `refresh_token` and `code` as URL query parameters of the POST request to
  `https://oauth.&lt;domain&gt;/oauth/api/oauth2/token`. Request URLs are commonly
  recorded in access logs, proxy logs and APM traces, so the application secret
  and refresh token can be persisted in plain text outside the applica…

---

## 23. 🟡 High Severity — Network-AI: CVE-2026-46701 fix incomplete — empty default secret still authorizes all requests

**CVE:** `CVE-2026-48814` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://github.com/advisories/GHSA-r78r-rwrf-rjwp>

> ## Advisory / Disclosure

# Network-AI — CVE-2026-46701 fix is incomplete: the &quot;Empty Default Secret&quot; unauth path survives

**Target:** Jovancoding/Network-AI (npm `network-ai`), **latest v5.7.1**
**Status:** the advisory (&quot;Unauthenticated Cross-Origin MCP Tool Invocation via Empty
Default Secret&quot;) named three flaws. The fix (5.4.5) closed the **CORS** flaw
(`Access-Control-All…

---

## 24. 🟡 High Severity — Splunk Enterprise Vulnerability Exploited in Attacks Days After Disclosure

**CVE:** `CVE-2026-20253` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-19
**Reference:** <https://www.securityweek.com/splunk-enterprise-vulnerability-exploited-in-attacks-days-after-disclosure/>

> CISA has given federal agencies only three days to patch CVE-2026-20253, which can be exploited for unauthenticated remote code execution. The post Splunk Enterprise Vulnerability Exploited in Attacks Days After Disclosure appeared first on SecurityWeek .

---

## 25. 🟡 High Severity — Signal K Server: Server-Side Request Forgery via Remote Connection Endpoints

**CVE:** `CVE-2026-55591` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-q59x-jc9f-gfqf>

> ### Summary
signalk-server versions up to and including 2.27.0 contain a Server-Side Request Forgery (SSRF) vulnerability in three administrative endpoints used for remote Signal K server connection management. The `makeRemoteRequest()` function accepts attacker-controlled `host`, `port`, `useTLS`, and `selfsignedcert` parameters without any validation, allowing an attacker to force the server to …

---

## 26. 🟡 High Severity — gemini-mcp-tool vulnerable to OS command injection and @file exfiltration via prompt quoting (CVE-2026-0755)

**CVE:** `CVE-2026-0755` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-4h5r-5jm8-jxjm>

> Untrusted prompt input could reach the Gemini CLI @file parser, allowing read/exfiltration of arbitrary local files (@/etc/passwd, @~/.ssh/id_rsa, @../../secret). On Windows, unquoted cmd.exe metacharacters could break out into OS command injection.

Fix (1.1.6): removed the broken shell:false double-quote wrapping; added assertSafeFileReferences() to contain @file refs to the working directory; h…

---

## 27. 🟡 High Severity — OpenClaw: Internal/webchat command auth could inherit ownerAllowFrom wildcard state

**CVE:** `CVE-2026-53854` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-18
**Reference:** <https://github.com/advisories/GHSA-4hpg-mp64-x7xq>

> ### Summary

Internal/webchat command auth could inherit ownerAllowFrom wildcard state. In affected versions, a sender on an affected internal or webchat path could inherit wildcard ownerAllowFrom state across channel boundaries.

This advisory is scoped to the named feature and configuration. It does not change OpenClaw&#x27;s trusted-operator model: authenticated Gateway operators, installed plu…

---

## 28. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
