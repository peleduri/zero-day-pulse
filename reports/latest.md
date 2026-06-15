# Zero Day Pulse

> **Generated:** 2026-06-15 16:53 UTC &nbsp;|&nbsp; **Total:** 13 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 3 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** A path traversal vulnerability in SimpleHelp 5.5.7 and earlier enables unauthenticated remote attackers to read sensitive files (e.g., logs, configuration files, credentials) via crafted requests.
- **Affected Products:** SimpleHelp Remote Support/RMM 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true – https://www.tenable.com/cve/CVE-2024-57727
- **Patch Available:** true – https://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570
- **Active Exploitation:** true – https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a
- **Threat Actors:** Ransomware actors (as reported by CISA)
- **Mitigation:** Upgrade to SimpleHelp 5.5.8 or later. If immediate patching is not possible, restrict network access to the SimpleHelp server (e.g., network segmentation, firewall rules limiting inbound traffic), disable public exposure, and apply CISA‑recommended mitigations.
- **Vendor Advisory:** https://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when attacker‑controlled content in retrievable data sources (web pages, shared Docs, Calendar invites, emails) contains embedded instructions that are returned by a retrieval system (RAG) to the LLM. The model treats those embedded instructions as part of its context and executes them (e.g., assemble sensitive data and embed it in an external image URL), enabling silent exfiltration via normal network requests. GeminiJack specifically abused Gemini Enterprise/Vertex AI Search RAG access to Gmail/Docs/Calendar by planting poisoned shared content that, when retrieved, caused the model to include an attacker‑controlled external image request containing serialized sensitive data.
- **Affected Products:** Google Workspace Gemini Enterprise; Vertex AI Search (RAG integrations)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability
- **Patch Available:** true — https://blog.google/security/prompt-injections-web/, https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** - Harden retrieval/instruction separation in RAG pipelines (treat retrieved docs as data, not instructions). - Restrict and audit datasources accessible to AI (least privilege). - Sanitize or remove executable‑looking constructs (HTML/img tags, URLs) from retrieved context before sending to models. - Monitor for anomalous external resource fetches (image loads to unknown domains) and block/alert. - Apply vendor‑provided updates and follow Google Workspace continuous mitigation guidance. - Use AI‑focused DLP and agent telemetry to detect exfiltration patterns.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) embeds malicious instructions inside data sources or tool outputs that a multi‑source LLM (e.g., Gemini in Workspace) ingests while completing a user’s query. Attackers can hide instructions (e.g., steganographic/format tricks, hidden text, crafted documents) so the model executes attacker‑supplied directives or returns manipulated outputs; some IPI variants enable “zero‑click” exploitation when the model processes tainted data automatically.
- **Affected Products:** Google Gemini Enterprise, Gemini in Workspace
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — https://noma.security/noma-labs/geminijack/
- **Patch Available:** true — https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/
- **Active Exploitation:** true — https://noma.security/noma-labs/geminijack/
- **Threat Actors:** None known
- **Mitigation:** Google recommends a layered defense: input sanitation and filtering, provenance and source validation, restricting agentic automation, capability gating, model output validation and red‑team testing, least‑privilege for connectors, continuous monitoring and patching. Practical steps include blocking or sanitizing untrusted document content, disabling risky connectors, applying vendor patches/updates (e.g., fixed versions per NVD), and following Google’s published hardening guidance.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Vulnerability leverages indirect prompt injection against agentic browsing (Gemini in Chrome) allowing a malicious site to influence or chain actions; Noma Labs reported a zero‑click proof called GeminiJack and NVD lists CVE‑2025‑54131 which can be triggered when chained with indirect prompt injection.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true (source: http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability)
- **Patch Available:** true (advisory: http://security.googleblog.com/2025/12/architecting-security-for-agentic.html)
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Use Chrome's layered defenses: indirect prompt injection mitigations, origin access restrictions, AI action restrictions; follow vendor advisory for updates and feature flags.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

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
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack vector where malicious instructions are embedded within external data sources (emails, documents, calendar invites, web content) that are consumed by generative AI systems; these hidden instructions attempt to manipulate AI behavior to exfiltrate data or perform unauthorized actions.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — https://blog.google/security/mitigating-prompt-injection-attacks/
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Implement layered defenses per Google guidance — sanitize and filter untrusted inputs, enforce strict data provenance and access controls, apply policy engines and model‑guardrails, monitor and log AI interactions, and use workspace/Gemini‑specific protections where available.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors compromise backbone, provider edge, and customer edge routers, modify firmware or configurations to retain long‑term access, and leverage trusted connections and compromised devices to pivot deeper into target networks.
- **Affected Products:** Backbone routers, Provider Edge (PE) routers, Customer Edge (CE) routers
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Implement robust network segmentation, enforce strict access controls on routers, regularly validate firmware integrity, monitor configuration changes, and conduct simulated attacks to test defenses.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** This advisory describes a sustained GRU espionage campaign using phishing and spearphishing, credential theft and harvesting, use of malware and web shells, exploitation of internet‑facing services, and lateral movement to access logistics and IT enterprise environments.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Russian GRU 85th GTsSS (Unit 26165) — tracked as APT28 (and related GRU units).
- **Mitigation:** Implement multifactor authentication, endpoint detection and response (EDR), network segmentation, enforce least privilege, patch and harden internet‑facing services, enable logging and monitoring, hunt for web shells and unusual authentication, and follow indicators of compromise from the advisory.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** The disclosed flaws include an elevation‑of‑privilege issue in the Windows Collaborative Translation Framework, a security‑feature bypass in BitLocker with a PoC, stack‑based buffer overflows in the DHCP client service and Active Directory Domain Services that can be triggered via malformed DHCP packets or network traffic, an improper authentication flaw in Cryptographic Services enabling privilege escalation, and integer overflow vulnerabilities in Windows Graphics components that require local user interaction.
- **Affected Products:** Windows Collaborative Translation Framework, Windows BitLocker, DHCP Client Service, Windows Active Directory Domain Services, Microsoft Cryptographic Services, Windows Graphics Component
- **CVSS Score:** 7.8, 6.8, 9.8, 8.8, 8.4, 7.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (Proof‑of‑concept for CVE‑2026‑50507 – BitLocker)
- **Patch Available:** true (https://support.microsoft.com/en-us/topic/june-9-2026-kb5094126-os-builds-26200-8655-and-26100-8655-1a9bcba6-5f53-4075-8156-fe11ac631737)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the June 2026 cumulative update (KB5094126) immediately. For the DHCP Client Service vulnerability, audit and restrict applications that call the DhcpGetOriginalSubnetMask API. Where patches are not yet applied, limit exposure by disabling unnecessary network services and enforcing least‑privilege configurations.
- **Vendor Advisory:** https://support.microsoft.com/en-us/topic/june-9-2026-kb5094126-os-builds-26200-8655-and-26100-8655-1a9bcba6-5f53-4075-8156-fe11ac631737

---

## 10. 🟠 Zero-Day — ⚡ Weekly Recap: Chrome 0-Day, UniFi Exploits, macOS Stealers, VPN Flaw and More

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://thehackernews.com/2026/06/weekly-recap-chrome-0-day-unifi.html>

> Stuff broke again. Not in a movie way. An old tool was left exposed. An abandoned package was abused. A deprecated feature was still running in prod.

This week is the same lesson in a new form: phishing kits are easier to rent, AI names are useful bait, old login paths still fail, and forgotten software keeps becoming someone else&#x27;s entry point.

Scroll through the full Monday Cybersecurity

**Parallel AI Enrichment:**

- **Technical Details:** A path traversal vulnerability in UniFi OS allows an attacker with network access to bypass normal file‑system restrictions and retrieve arbitrary files, which can be used to harvest credentials and potentially execute unauthenticated remote code.
- **Affected Products:** UniFi OS
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Apply the security patches released in Security Advisory Bulletin 064, update UniFi OS to the latest version, and limit network exposure of UniFi devices.
- **Vendor Advisory:** http://community.ui.com/releases/Security-Advisory-Bulletin-064-064/84811c09-4cf4-42ab-bd61-cc994445963b

---

## 11. 🟡 High Severity — @angular/platform-server: URL Parser Differential leading to SSRF Allowlist Bypass

**CVE:** `CVE-2026-50168` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-xrxm-cp7j-8xf6>

> An issue in the `@angular/platform-server` package allows remote attackers to bypass host allowlist constraints and direct server-side outgoing requests to arbitrary external endpoints. This occurs due to a parser differential between the strict WHATWG URL parser used for allowlist validation and the lenient Domino URL parser used to initialize the server emulated DOM.

When a server-side request …

---

## 12. 🟡 High Severity — Angular Client Hydration DOM Clobbering & Response-Cache Poisoning

**CVE:** `CVE-2026-54267` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-15
**Reference:** <https://github.com/advisories/GHSA-rgjc-h3x7-9mwg>

> To optimize client-side bootstrap in Server-Side Rendered (SSR) environments, Angular supports **Hydration** via `provideClientHydration()`. During SSR, Angular serializes the application&#x27;s runtime state (such as cached `HttpClient` responses) and outputs it into the HTML stream as a `&lt;script&gt;` tag with a predictable identifier:

```html
&lt;script type=&quot;application/json&quot; id=&…

---

## 13. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
