# Zero Day Pulse

> **Generated:** 2026-07-12 18:48 UTC &nbsp;|&nbsp; **Total:** 12 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 11 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** A path/directory traversal vulnerability in SimpleHelp RMM (CVE-2024-57727) that allows unauthenticated remote attackers to read sensitive files on the server.
- **Affected Products:** SimpleHelp remote support / remote monitoring and management software, versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true, https://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570
- **Active Exploitation:** true
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Apply vendor update (SimpleHelp 5.5.8) immediately; restrict network exposure to the SimpleHelp service (firewall/ACLs), segment RMM systems, and rotate credentials/keys after remediation.
- **Vendor Advisory:** http://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) embeds adversarial instructions inside external content (web pages, HTTP responses, documents) that an LLM or agent will fetch or consume. Hidden instructions (in page text, comments, scripts or other embedded content) can override or influence model instructions, cause data leakage (API keys, private data), enable unauthorized actions by agentic workflows, or facilitate fraud.
- **Affected Products:** LLM-based agents and agentic workflows (e.g., GitHub Agentic Workflows), AI coding assistants, web‑connected LLM agents and browsers, Google Gemini in Workspace (Gmail, Docs, Drive, Chat)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — public PoCs / weaponized payloads reported (examples: Forcepoint X‑Labs: https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads, Mozilla PoC writeups: https://devops.com/mozilla-shows-the-danger-of-indirect-prompt-injections-in-ai-coding-agents/, Noma Labs GitLost: https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/)
- **Patch Available:** false
- **Active Exploitation:** true — multiple vendors/research teams report IPI payloads observed on live sites and empirical evidence of prevalence (examples: Forcepoint X‑Labs, Unit42, arXiv empirical study)
- **Threat Actors:** None known
- **Mitigation:** Apply layered defenses: content filtering and detection of IPI payloads, context isolation (avoid blindly concatenating external content into prompts), instruction hygiene (explicit system prompts and prompt separation), allowlisting/high-risk action gating, human review for sensitive actions, and vendor-provided protections (see Google Workspace layered defenses).
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI): an attacker injects malicious instructions into the data or tools an LLM uses while completing a user’s query (possibly without direct user input), causing the model/agent to follow attacker-supplied instructions or behave incorrectly.
- **Affected Products:** Google Workspace with Gemini (Gemini app; Gemini in Gmail, Docs editors, Drive, Chat)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (see http://unit42.paloaltonetworks.com/ai-agent-prompt-injection)
- **Patch Available:** false
- **Active Exploitation:** true (see http://unit42.paloaltonetworks.com/ai-agent-prompt-injection, http://helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild)
- **Threat Actors:** None known
- **Mitigation:** Vendor-recommended layered defenses and hardening: follow Google’s Workspace/Gemini guidance (apply platform hardening, limit or audit agentic automation, restrict/sanitize external content sources, and follow admin guidance for Gmail/Docs/Drive/Chat). No single patch is described; Google describes continuous improvements and a layered defense strategy.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: adversarial or hidden web content (or injected scripts) can influence an agentic LLM integrated into the browser (Gemini/agentic browsing) to perform privileged actions or disclose data. Researchers demonstrated zero-click/indirect injection (GeminiJack) and PoC HTML/script pages that trigger privileged behavior.
- **Affected Products:** Google Chrome (agentic browsing with Gemini), Google Gemini Enterprise
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — public PoC(s) available: https://github.com/fevar54/CVE-2026-0628-POC, https://github.com/brennanbrown/atlas-prompt-injection-poc
- **Patch Available:** true — Google announced layered defenses / mitigations (see vendor advisory URL above)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Update to Chrome builds that include Google’s layered defenses; restrict agentic capabilities, restrict origin access and origin privileges for AI agents, block or sanitize untrusted content that may carry prompt-instructions, and apply least-privilege and sandboxing for agentic actions.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Incorrect bounds checks in the Android System component leading to out-of-bounds accesses that enable remote code execution.
- **Affected Products:** Android System (core System component), Android 16.0 devices (see Android Security Bulletin August 2025 for security-patch-level mappings)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true; https://source.android.com/docs/security/bulletin/2025-08-01
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the Android Security Bulletin (August 2025) security patches immediately; update Android 16.0 devices to the latest security patch level; limit network exposure / implement network segmentation; configure alerts for system service crashes or restarts.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: hidden or adversarial instructions embedded in external data sources (emails, files, calendar invites, web content) that AI models or agents fetch and incorporate into prompts, causing data exfiltration or undesired actions. Google’s described attack surface includes Workspace-integrated Gemini; Google’s mitigations include model hardening (Gemini 2.5 with adversarial training), prompt-injection content classifiers, security-thought reinforcement (additional reasoning/context to ignore adversarial instructions), markdown sanitization and suspicious-URL redaction, user confirmation flows for destructive actions, and end-user mitigation notifications.
- **Affected Products:** Gemini (including Gemini 2.5 model), Gemini app, Google Workspace (Gmail, Google Docs, Google Drive, Google Chat)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — public PoC/benign demonstrations exist (example: http://github.com/brennanbrown/atlas-prompt-injection-poc)
- **Patch Available:** true — Google has published and begun deploying layered mitigations / model hardening (see vendor advisory URL above: http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html)
- **Active Exploitation:** true — public reporting describes real-world exploitation (see cited sources)
- **Threat Actors:** None known
- **Mitigation:** Apply vendor mitigations and controls: use updated Gemini/Workspace releases with model hardening; enable and rely on content classifiers and markdown/suspicious-URL redaction; require explicit user confirmation for potentially destructive actions; monitor end-user security notifications and follow vendor Help Center guidance; adopt least-privilege data access and avoid sending highly sensitive data into agents that fetch external content.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors target backbone and edge network devices (backbone, provider-edge (PE) and customer-edge (CE) routers) and leverage compromised devices and trusted connections to pivot; they exploit known vulnerabilities in network device OSes (examples cited: Ivanti Connect Secure, Cisco IOS XE, Palo Alto PAN-OS), modify router configuration to maintain persistence (industry reports note artifacts such as ACLs named "access-list 20"), and focus on unpatched, internet-facing devices rather than widespread novel zero-day exploitation.
- **Affected Products:** Ivanti Connect Secure, Cisco IOS XE, Palo Alto PAN-OS, Fortinet devices, Juniper devices, Microsoft Exchange
- **CVSS Score:** 4.3 (reported by some industry trackers); 6.4 (alternative tracker report) — conflicting reports
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Upgrade unsupported network devices to vendor-supported versions; apply strict hardening to management interfaces and features (disable/limit GuestShell or similar management shells if not needed); restrict and log administrative access, segment networks, prioritize remediation of internet-facing unpatched devices, and monitor for known indicators of compromise.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** GRU unit 26165 weaponized an Outlook NTLM vulnerability (CVE-2023-23397) to collect NTLM hashes; campaign targeted Western logistics and technology companies since 2022.
- **Affected Products:** Microsoft Outlook (CVE-2023-23397; versions unspecified)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Russian GRU unit 26165 (85th GTsSS / 85th Main Special Service Center)
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

**Parallel AI Enrichment:**

- **Technical Details:** An OS command injection vulnerability in Ivanti Sentry (pre-fixed versions) that allows a remote unauthenticated attacker to execute commands as root (root-level RCE). Exploitation requires access to the Sentry management interface (management port 8443) in typical deployments.
- **Affected Products:** Ivanti Sentry — affected: 10.5.1, 10.6.1, 10.7.0 and prior; resolved in 10.5.2, 10.6.2, 10.7.1
- **CVSS Score:** 10
- **CVSS Vector:** CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Exploit Available:** true — public PoC available (public PoC reported/released; e.g., June 10, 2026 PoC reports and third‑party PoC references).
- **Patch Available:** true — Ivanti released updates that fix the issue; see Ivanti advisory: https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523
- **Active Exploitation:** true — multiple independent sources reported attempted/active exploitation (reports include Shadowserver/CISA/third‑party researchers), though Ivanti initially stated no known customer exploitation at time of disclosure.
- **Threat Actors:** None known
- **Mitigation:** Update Ivanti Sentry appliances to the fixed versions (10.5.2, 10.6.2, 10.7.1). Do not expose the management interface (port 8443) to the Internet; for managed deployments ensure mTLS and follow Ivanti's guidance for management/MDM configurations.
- **Vendor Advisory:** https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523

---

## 10. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated OS command-injection / remote code execution in Ivanti Sentry appliances that allows full control of the device (configuration changes, credential theft, data access and lateral movement). Exploitation is remote and facilitated by a published PoC.
- **Affected Products:** Ivanti Sentry appliances (specific versions unavailable)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (public PoC reported; e.g. Horizon3 PoC reported 2026-06-10)
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true (confirmed active exploitation reported)
- **Threat Actors:** None known
- **Mitigation:** Update affected Ivanti Sentry appliances urgently (outside normal patching cycles) as recommended by Rapid7; apply vendor patch when available.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟠 Zero-Day — CrowdStrike Uncovers New Prompt Injection Techniques

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jul 07, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-uncovers-new-prompt-injection-techniques/>

---

## 12. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
