# Zero Day Pulse

> **Generated:** 2026-06-25 19:45 UTC &nbsp;|&nbsp; **Total:** 24 &nbsp;|&nbsp; 🔴 KEV: 2 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 8 &nbsp;|&nbsp; ✨ Enriched: 6

---

## 1. 🔴 CISA KEV — CVE-2026-20230 — Cisco Unified Communications Manager Server-Side Request Forgery (SSRF) Vulnerability

**CVE:** `CVE-2026-20230` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-20230>

> Vendor: Cisco | Product: Unified Communications Manager. Cisco Unified Communications Manager (Unified CM) and Cisco Unified Communications Manager Session Management Edition (Unified CM SME) contain a server-side request forgery (SSRF) Vulnerability that could allow an unauthenticated, remote attacker to write files to the underlying operating system that could be used later to elevate to root. R…

**Parallel AI Enrichment:**

- **Technical Details:** A server-side request forgery (SSRF) vulnerability (WebDialer/SAML component) in Cisco Unified Communications Manager that allows an unauthenticated remote attacker to perform SSRF requests which can be used to write files to the underlying operating system and lead to privilege escalation to root.
- **Affected Products:** Cisco Unified Communications Manager (Unified CM), Cisco Unified Communications Manager Session Management Edition (Unified CM SME)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof-of-concept (PoC) / exploit code has been published and discussed in multiple reports (public PoC referenced by security news outlets and researcher posts).
- **Patch Available:** Yes — Cisco has released security updates to address the issue (see Cisco advisory: http://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-ssrf-cXPnHcW).
- **Active Exploitation:** Confirmed — multiple public reports state the vulnerability is being exploited in the wild.
- **Threat Actors:** None known
- **Mitigation:** Apply Cisco security updates immediately; if WebDialer is not required, disable the WebDialer service as recommended by vendor/NVD guidance.
- **Vendor Advisory:** http://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-ssrf-cXPnHcW

---

## 2. 🔴 CISA KEV — CVE-2026-12569 — PTC Windchill and FlexPLM Improper Input Validation Vulnerability

**CVE:** `CVE-2026-12569` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-12569>

> Vendor: PTC | Product: Windchill and FlexPLM. PTC Windchill and FlexPLM contains an improper input validation vulnerability allowing an unauthenticated, remote attacker to execute arbitrary code by sending a malicious request to the network. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Ri…

---

## 3. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Directory‑traversal vulnerability allowing unauthenticated remote attackers to read arbitrary files via path manipulation.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept or weaponized exploit known.
- **Patch Available:** Vendor released patches for the vulnerabilities within two days of reporting.
- **Active Exploitation:** Confirmed active exploitation reported by CISA, with ransomware actors leveraging CVE‑2024‑57727.
- **Threat Actors:** Ransomware actors (unspecified groups)
- **Mitigation:** Apply the vendor patch, upgrade to a version newer than 5.5.7, and restrict network access to the RMM service.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 4. 🟠 Zero-Day — LangGraph Checkpoint: Unsafe JSON deserialization in checkpoint loading

**CVE:** `CVE-2026-48775` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-fjqc-hq36-qh5p>

> ## Summary

LangGraph&#x27;s `JsonPlusSerializer` can reconstruct Python objects from JSON checkpoint payloads. Under conditions where someone could modify checkpoint bytes at rest in the backing store, the deserialization path could reconstruct objects beyond what the application expects, which could in turn result in code execution at checkpoint load time.

This is a defense-in-depth issue. The …

**Parallel AI Enrichment:**

- **Technical Details:** LangGraph SQLite Checkpoint uses JsonPlusSerializer to deserialize JSON checkpoint payloads; if an attacker can modify checkpoint files, they can trigger deserialization of untrusted data, leading to remote code execution at checkpoint load time.
- **Affected Products:** LangGraph SQLite Checkpoint (LangGraph CheckpointSaver) versions <=4.1.0
- **CVSS Score:** 6.8
- **CVSS Vector:** CVSS:3.1/AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** No public proof-of-concept or weaponized exploit known
- **Patch Available:** Patch released in LangGraph version 4.1.1; see vendor advisory for details.
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Upgrade to LangGraph version 4.1.1 or later, which removes the unsafe deserialization path.
- **Vendor Advisory:** https://github.com/langchain-ai/langgraph/security/advisories/GHSA-fjqc-hq36-qh5p

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when an LLM processes external content (webpages, documents, emails, tools) that contains malicious instructions; the LLM may follow those instructions instead of the user's intent, enabling data exfiltration, behavior manipulation, or denial-of-service without direct user input.
- **Affected Products:** Google Workspace (including Gemini Enterprise)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept (PoC) available; only observed payloads in the wild.
- **Patch Available:** No official patch yet; mitigation steps are described in the advisory.
- **Active Exploitation:** Yes — multiple reports describe IPI payloads observed on public websites (e.g., "10 Indirect Prompt Injection Payloads Caught in the Wild") and a Noma Labs report identified a zero-click GeminiJack IPI issue in Google Gemini Enterprise.
- **Threat Actors:** None known
- **Mitigation:** Continuous monitoring and detection (broad web sweeps), deterministic defenses (URL sanitization, user confirmation, tool chaining policies), ML-based defenses, LLM-based defenses, synthetic data generation for retraining, and configuration-based point fixes (e.g., regex takedowns).
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection hides malicious instructions inside external data (HTML comments, hidden divs, CSS-hidden text, metadata tags, magic strings) that AI agents ingest when crawling or summarizing content; injected instructions can exfiltrate data, perform unauthorized actions, suppress or corrupt output, or trigger fraud (examples include API-key exfiltration, sudo-like command text, URL-based exfiltration, persuasion triggers).
- **Affected Products:** Google Gemini (Gemini in Google Workspace, Gemini app), Gemini 2.5
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public examples/PoC-level payloads have been documented in the wild (Forcepoint X‑Labs report) showing HTML comment, hidden div, CSS concealment, metadata, and magic-string payloads hosted on live sites; see Forcepoint report for live examples. No single weaponized exploit kit URL published by vendor.
- **Patch Available:** No single downloadable patch; Google describes integrated service mitigations (Gemini 2.5 model hardening, content classifiers, markdown sanitization, suspicious URL redaction, user confirmation framework) being rolled out via product updates (see vendor advisory).
- **Active Exploitation:** Yes — Forcepoint X‑Labs reports multiple indirect prompt injection (IPI) payloads found on active websites and deployed in live web infrastructure; Google also acknowledges indirect prompt injection as an emerging threat and describes mitigations.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: model hardening/adversarial training (Gemini 2.5), purpose-built prompt-injection content classifiers to filter malicious instructions, security thought reinforcement to steer model behavior, markdown sanitization and external-image blocking, suspicious-URL detection/redaction (Safe Browsing), user confirmation flows for potentially destructive actions, and end-user security notifications.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Exploits CVEs in network device firmware to gain persistent access via compromised backbone, provider edge (PE), and customer edge (CE) routers.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit not available.
- **Patch Available:** No official patch or remediation guidance is currently available from the vendor.
- **Active Exploitation:** Confirmed active exploitation reported by CISA and multiple security analyses.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 12. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 13. 🟠 Zero-Day — LangGraph SDK has unsafe URL path construction

**CVE:** `CVE-2026-48776` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-w39p-vh2g-g8g5>

> ## Summary

`langgraph-sdk` constructs HTTP request paths for resource operations by interpolating caller-supplied identifier values into URL templates. Without sanitization of those values, identifiers that contain characters with special meaning in URL paths could cause the resulting request to address a different resource (and potentially a different resource type) than the SDK method&#x27;s ca…

---

## 14. 🟠 Zero-Day — New macOS malware embeds fake errors to confuse AI analysis tools

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://www.bleepingcomputer.com/news/security/new-macos-malware-embeds-fake-errors-to-confuse-ai-analysis-tools/>

> A newly discovered macOS malware dubbed &quot;Gaslight&quot; is designed to confuse AI-assisted malware analysis tools by hiding prompt injection strings and fake debugging data within the executable. [...]

---

## 15. 🟠 Zero-Day — New Gaslight macOS Malware Uses Prompt Injection to Disrupt AI-Assisted Analysis

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://thehackernews.com/2026/06/new-gaslight-macos-malware-uses-prompt.html>

> A previously undocumented Rust-based macOS implant and information stealer has been found to embed a prompt injection payload designed to trick a malware analyst&#x27;s artificial intelligence (AI) tools and trick it into aborting or refusing an analysis of the artifact.

The malware has been codenamed Gaslight owing to this deceptive behavior. It&#x27;s been assessed with high confidence that the…

---

## 16. 🟠 Zero-Day — Cisco Catalyst SD-WAN Zero-Day CVE-2026-20245 Exploited to Gain Root Access

**CVE:** `CVE-2026-20245` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://thehackernews.com/2026/06/cisco-catalyst-sd-wan-zero-day-cve-2026.html>

> An unknown threat actor exploited a recently disclosed high-severity security flaw impacting Cisco Catalyst SD-WAN as a zero-day at least two months before it was publicly disclosed, according to new findings from Google-owned Mandiant.

The vulnerability, tracked as CVE-2026-20245 (CVSS score: 7.8), allows an authenticated, local attacker to execute arbitrary commands with elevated privileges

---

## 17. 🟡 High Severity — Lemur has an authorization bypass in StrictRolePermission / AuthorityCreatorPermission

**CVE:** `CVE-2026-48508` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-qcqw-jwxc-2hqg>

> ## Summary

`StrictRolePermission` and `AuthorityCreatorPermission` in `lemur/auth/permissions.py` call `flask_principal.Permission.__init__()` with zero `Need`s when their config flags are unset. Both flags defaulted to `False` in code prior to the fix, so this was the state of any Lemur install that hadn&#x27;t explicitly opted in.

Flask-Principal&#x27;s `Permission.allows()` returns `True` whe…

---

## 18. 🟡 High Severity — amazon-braket-sdk vulnerable to Insecure Deserialization via pickle.loads()

**CVE:** `CVE-2026-9291` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-g697-2xrc-gc46>

> **Summary**
Amazon Braket SDK is an open-source Python library for interacting with the Amazon Braket quantum computing service, including managing hybrid quantum jobs and retrieving job results. An issue exists where, under certain circumstances, a remote authenticated user with S3 write access to a Braket job output bucket can achieve arbitrary code execution by exploiting insecure deserializati…

---

## 19. 🟡 High Severity — i18next-fs-backend vulnerable to prototype pollution via crafted missing-key string

**CVE:** `CVE-2026-48713` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-2933-q333-qg83>

> ### Impact

`i18next-fs-backend` ≤ 2.6.5, when used to persist missing translation keys (e.g. via `i18next-http-middleware`&#x27;s `missingKeyHandler` exposed to untrusted input), is vulnerable to prototype pollution via crafted missing-key strings.

`Backend.writeFile()` splits each queued missing-key string on the configured `keySeparator` (default `.`) before calling the internal `setPath()` wa…

---

## 20. 🟡 High Severity — i18next-http-middleware: MissingKeyHandler does not reject keys whose segments contain prototype-polluting names

**CVE:** `CVE-2026-48714` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-f49m-vf83-692w>

> ### Impact

`i18next-http-middleware` ≤ 3.9.6&#x27;s `missingKeyHandler` blocked the literal request-body keys `__proto__`, `constructor`, and `prototype` (added in 3.9.3, see GHSA-5fgg-jcpf-8jjw), but did not reject dotted variants such as `&quot;__proto__.polluted&quot;`. Downstream backends that split the missing-key string on a configured `keySeparator` (notably `i18next-fs-backend` ≤ 2.6.5) h…

---

## 21. 🟡 High Severity — OpenAM: Unauthenticated Authentication Bypass via RADIUS Spoofing

**CVE:** `CVE-2026-46560` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-386j-6m86-78f9>

> ## Summary

**Description**

An Improper Verification of Cryptographic Signature (CWE-347) issue in OpenAM&#x27;s RADIUS authentication module allows an unauthenticated network attacker to spoof an Access-Accept response and obtain an OpenAM session for any RADIUS username, without knowing the configured shared secret. This affects OpenAM Community Edition through version 16.0.6 and was patched in…

---

## 22. 🟡 High Severity — @anthropic-ai/claude-code has an Insecure Temporary File in /copy Command that Enables Response Disclosure and Symlink-Based File Write

**CVE:** `CVE-2026-46406` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-4vp2-6q8c-pvq2>

> The Claude Code `/copy` command wrote responses to a hardcoded, predictable path (`/tmp/claude/response.md`) without UID isolation, randomness, or symlink protection. The file was created world-readable (0644) in a world-traversable directory (0755), allowing any local user to read a privileged user&#x27;s Claude response, which could contain secrets or credentials. Additionally, because the path …

---

## 23. 🟡 High Severity — OpenAM has Unsafe Java Deserialization via SNS

**CVE:** `CVE-2026-45794` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-25
**Reference:** <https://github.com/advisories/GHSA-pp89-732f-3g8q>

> ## Summary

**Description**

A Deserialization of Untrusted Data (CWE-502) issue exists in OpenAM&#x27;s Push Notification SNS callback resource. The REST route that handles SNS push messages is mounted with anonymous access and, when a supplied message identifier has expired from the in-memory dispatcher, falls back to a CTS-stored predicate blob whose top-level keys are treated as Java class nam…

---

## 24. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
