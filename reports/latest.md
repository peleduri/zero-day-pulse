# Zero Day Pulse

> **Generated:** 2026-06-08 20:00 UTC &nbsp;|&nbsp; **Total:** 21 &nbsp;|&nbsp; 🔴 KEV: 2 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 5 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🔴 CISA KEV — CVE-2026-42271 — BerriAI LiteLLM Command Injection Vulnerability

**CVE:** `CVE-2026-42271` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-42271>

> Vendor: BerriAI | Product: LiteLLM. BerriAI LiteLLM contains a command injection vulnerability that could allow any authenticated user, including holders of low-privilege internal-user keys, to run arbitrary commands on the host. Required action: Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are …

**Parallel AI Enrichment:**

- **Technical Details:** Two preview endpoints (/mcp-rest/test/connection and /mcp-rest/test/tools/list) accepted full server configurations including command, args, and env fields. When a stdio configuration was supplied, the server spawned the supplied command as a subprocess with proxy process privileges, enabling arbitrary command execution (CWE‑77/CWE‑78).
- **Affected Products:** BerriAI LiteLLM versions >=1.74.2 and <1.83.7
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** No public PoC or weaponized exploit reported in major sources; the claim on LinkedIn is uncorroborated.
- **Patch Available:** Yes — fixed in LiteLLM v1.83.7; advisory: https://github.com/BerriAI/litellm/security/advisories/GHSA-v4p8-mg3p-g94g; release: https://github.com/BerriAI/litellm/releases/tag/v1.83.7-stable
- **Active Exploitation:** No confirmed widespread exploitation reported by primary sources; the LinkedIn claim of exploitation is uncorroborated.
- **Threat Actors:** None known
- **Mitigation:** Upgrade to LiteLLM v1.83.7 or later. If upgrade is not possible, disable or block the /mcp-rest/test/connection and /mcp-rest/test/tools/list endpoints via firewall/reverse‑proxy, revoke or restrict unnecessary API keys, disable stdio transport, and set disable_error_logs: true as a temporary workaround.
- **Vendor Advisory:** https://github.com/BerriAI/litellm/security/advisories/GHSA-v4p8-mg3p-g94g

---

## 2. 🔴 CISA KEV — CVE-2026-50751 — Check Point Security Gateway Improper Authentication Vulnerability

**CVE:** `CVE-2026-50751` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-50751>

> Vendor: Check Point | Product: Security Gateway. Check Point Security Gateway contains an improper authentication vulnerability in IKEv1 key exchange that could allow an unauthenticated remote attacker to bypass user authentication and establish a remote access VPN connection without a valid user password. Required action: Apply mitigations per vendor instructions, follow applicable BOD 22-01 guid…

**Parallel AI Enrichment:**

- **Technical Details:** Authentication bypass in deprecated IKEv1 key‑exchange due to a logic flow weakness in Remote Access and Mobile Access certificate validation, enabling a VPN session to be established without a valid user password.
- **Affected Products:** Mobile Access / SSL VPN, Remote Access VPN, Spark Firewall (versions: R80.20.X (EOS), R80.40 (EOS), R81 (EOS), R81.10 (EOS), R81.10.X, R81.20, R82, R82.00.X, R82.10)
- **CVSS Score:** 9.3
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Public proof-of-concept not identified.
- **Patch Available:** Yes – Check Point has released hotfixes (see SK185033).
- **Active Exploitation:** Yes – active exploitation in the wild has been observed.
- **Threat Actors:** Qilin ransomware; other financially motivated ransomware affiliates (medium confidence)
- **Mitigation:** Apply the Check Point hotfixes immediately; alternatively, disable/deprecate IKEv1, require machine certificates for connections, audit logs and configurations, and follow the guidance in SK185033.
- **Vendor Advisory:** https://support.checkpoint.com/results/sk/sk185033

---

## 3. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is a directory/path traversal that lets unauthenticated remote attackers read arbitrary files, potentially exposing logs, configuration files, and credentials.
- **Affected Products:** SimpleHelp remote support software version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public exploit reported; no public PoC link provided.
- **Patch Available:** Patch released by vendor; see vendor advisory.
- **Active Exploitation:** Active exploitation reported by ransomware actors as described in the CISA advisory.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 4. 🟠 Zero-Day — Critical Check Point VPN Zero-Day Exploited in the Wild (CVE-2026-50751)

**CVE:** `CVE-2026-50751` | `CVE-2026-50752` | `CVE-2024-24919` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://www.rapid7.com/blog/post/etr-critical-check-point-vpn-zero-day-exploited-in-the-wild-cve-2026-50751>

> Overview On June 8, 2026, Check Point published a security advisory for CVE-2026-50751 , a critical authentication bypass vulnerability affecting Check Point Remote Access VPN, Mobile Access, and Spark Firewall products. The vulnerability affects deployments configured to use the deprecated IKEv1 key exchange protocol where gateways accept legacy Remote Access clients and do not require a machine …

**Parallel AI Enrichment:**

- **Technical Details:** Authentication bypass in deprecated IKEv1 key‑exchange due to a logic flow weakness in Remote Access and Mobile Access certificate validation, enabling a VPN session to be established without a valid user password.
- **Affected Products:** Mobile Access / SSL VPN, Remote Access VPN, Spark Firewall (versions: R80.20.X (EOS), R80.40 (EOS), R81 (EOS), R81.10 (EOS), R81.10.X, R81.20, R82, R82.00.X, R82.10)
- **CVSS Score:** 9.3
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Public proof-of-concept not identified.
- **Patch Available:** Yes – Check Point has released hotfixes (see SK185033).
- **Active Exploitation:** Yes – active exploitation in the wild has been observed.
- **Threat Actors:** Qilin ransomware; other financially motivated ransomware affiliates (medium confidence)
- **Mitigation:** Apply the Check Point hotfixes immediately; alternatively, disable/deprecate IKEv1, require machine certificates for connections, audit logs and configurations, and follow the guidance in SK185033.
- **Vendor Advisory:** https://support.checkpoint.com/results/sk/sk185033

---

## 5. 🟠 Zero-Day — Gogs patches critical zero-day enabling remote code execution

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://www.bleepingcomputer.com/news/security/gogs-patches-critical-zero-day-enabling-remote-code-execution/>

> Gogs has patched a critical security zero-day flaw that can allow attackers to compromise Internet-facing instances and access any repositories (including private ones). [...]

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal / symlink handling flaw in Gogs repository file‑editing functionality allows attackers to overwrite files outside the repository (including application files), enabling remote code execution when web‑accessible files or service processes are replaced.
- **Affected Products:** Gogs (self‑hosted Git service)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC exists — https://github.com/zAbuQasem/gogs-CVE-2025-8110
- **Patch Available:** Yes — vendor has released a patch (see CISA directive).
- **Active Exploitation:** Confirmed active exploitation in the wild; over 700 compromised instances reported.
- **Threat Actors:** None known.
- **Mitigation:** Apply vendor patch immediately; if patch unavailable, restrict Internet exposure of Gogs instances, disable repository file‑editing web functionality, remove/deny untrusted users, and enforce network controls (firewall, IP allowlists).
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 6. 🟠 Zero-Day — Check Point links VPN zero-day attacks to Qilin ransomware gang

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://www.bleepingcomputer.com/news/security/check-point-links-vpn-zero-day-attacks-to-qilin-ransomware-gang/>

> Israeli cybersecurity company Check Point has released security updates to patch a critical flaw affecting Remote Access VPN and Mobile Access deployments, which was exploited in zero-day attacks. [...]

**Parallel AI Enrichment:**

- **Technical Details:** An authentication bypass vulnerability in Check Point Remote Access VPN/Mobile Access when configured to use deprecated IKEv1 key exchange, allowing unauthenticated remote attackers to bypass authentication and establish a remote access VPN connection (CVE‑2026‑50751).
- **Affected Products:** Check Point Remote Access VPN, Mobile Access deployments and Spark firewalls configured to use deprecated IKEv1 key exchange and accepting legacy Remote Access clients without mandatory machine certificate.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC/weaponized exploit reported in sources reviewed.
- **Patch Available:** Yes — Check Point released security updates/hotfixes for the issue.
- **Active Exploitation:** Yes — Check Point observed active exploitation starting May 7, with a surge in early June; a few dozen organizations were affected and at least one confirmed incident was linked to Qilin ransomware.
- **Threat Actors:** Qilin ransomware gang
- **Mitigation:** Remove support for legacy remote access client; configure Remote Access VPN Authentication to IKEv2 only; require Machine Certificate Authentication; enable IPS and download signatures.
- **Vendor Advisory:** https://support.checkpoint.com/results/sk/sk185033

---

## 7. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) – attackers place adversarial instructions inside external content retrieved by LLM‑based systems (e.g., web pages or knowledge corpora) so the model executes those instructions when processing user queries; impacts RAG and agentic systems where retrieval or tool‑use bridges attacker‑controlled content into the model context.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Proof‑of‑concept and end‑to‑end IPI exploits have been demonstrated (see arXiv 2601.07072).
- **Patch Available:** Google addressed the GeminiJack issue per vendor post; patch/advisory URL unavailable.
- **Active Exploitation:** Confirmed active exploitation: security reports and research demonstrate real‑world IPI examples and a zero‑click GeminiJack vulnerability indicating active abuse.
- **Threat Actors:** None known
- **Mitigation:** Harden retrieval and validation controls: sanitize/trust‑boundary retrieval results, apply provenance and content filtering, enforce instruction‑safety layers, minimize automatic execution of retrieved instructions, use model fine‑tuning or instruction guards, and monitor for anomalous agent behavior.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) enables attackers to inject malicious instructions into data sources (emails, documents, calendar invites) consumed by LLMs or agents; GeminiJack used specially crafted content to trigger Gemini Enterprise to follow attacker‑supplied instructions without user interaction.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC/weaponized exploit: Reports indicate a zero‑click exploit named "GeminiJack" was discovered; PoC details reported by Noma Labs and security media—no official public exploit URL confirmed.
- **Patch Available:** Google released mitigations for Workspace/Gemini Enterprise per Google Security Blog; patch/advisory URL: http://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections
- **Active Exploitation:** Reports of vulnerability discovery; no public widespread exploitation confirmed.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: input sanitization, provenance/metadata checks, content classification, sandboxing agentic actions, restricting automated actions on untrusted sources, user prompts/confirmation for high-risk actions, continuous monitoring and model hardening as described in Google’s advisory.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection allows a malicious site to inject or modify prompts that the browser‑integrated AI model processes, potentially causing the model to perform unsafe actions on behalf of the user.
- **Affected Products:** Google Chrome (latest version as of December 2025)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit known.
- **Patch Available:** Patch incorporated in Chrome updates; no separate patch advisory URL.
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Chrome’s built‑in layered defenses block indirect prompt injections, limit cross‑origin access for AI prompts, and enforce safe‑action policies. Users should keep Chrome updated to receive these protections.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 10. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** The post reports Android’s shift to using Rust for new components reduces memory‑safety vulnerabilities by preventing classes of memory‑corruption bugs common in C/C++; Rust’s ownership/borrowing model, strong type system, and safe standard library eliminate many use‑after‑free, buffer overflow, and related errors, while unsafe blocks are minimized and audited.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** None known
- **Patch Available:** Patch information not applicable — the source is an informational Google Security Blog post about Rust adoption rather than a single vulnerability; no vendor patch URL provided.
- **Active Exploitation:** None known
- **Threat Actors:** None known
- **Mitigation:** Continue migrating new code to memory‑safe languages (Rust), apply code auditing and fuzzing, sandboxing, and backport security fixes to C/C++ components where Rust conversion is not yet possible.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 11. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 12. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

---

## 13. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 14. 🟠 Zero-Day — ⚡ Weekly Recap: Instagram Account Hacks, Android Zero-Day, GitHub Worm and More

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://thehackernews.com/2026/06/weekly-recap-instagram-account-hacks.html>

> Monday again. The weekend was meant to be quiet. It wasn&#x27;t. Last week had poisoned packages, a broken AI helper, and a worm tearing through repos. The ugly part: basic tricks still worked.

A chatbot got fooled. A bot token got leaked inside the malware. The same old mistakes showed up again. And while everyone chased the loud stuff, quieter attackers sat in inboxes for months, reading mail a…

---

## 15. 🟠 Zero-Day — Everest Forms Vulnerability Exploited to Hack WordPress Sites

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://www.securityweek.com/everest-forms-vulnerability-exploited-to-hack-wordpress-sites/>

> The flaw allows attackers to execute arbitrary code remotely and has been exploited in the wild for two months. The post Everest Forms Vulnerability Exploited to Hack WordPress Sites appeared first on SecurityWeek .

---

## 16. 🟠 Zero-Day — SolarWinds Serv-U Vulnerability Exploited in the Wild

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://www.securityweek.com/solarwinds-patches-exploited-serv-u-vulnerability/>

> Unauthenticated attackers can exploit the flaw via specially crafted POST requests that crash the Serv-U service. The post SolarWinds Serv-U Vulnerability Exploited in the Wild appeared first on SecurityWeek .

---

## 17. 🟡 High Severity — Netty: HAProxy SSL TLV parsing leaks retained slice on invalid TLV length

**CVE:** `CVE-2026-44893` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-cc37-9q2j-3hfv>

> When decoding a PP2_TYPE_SSL TLV, HAProxyMessage.readNextTLV() first calls `header.retainedSlice(header.readerIndex(), length)` and only then reads the 1-byte client field and 4-byte verify field. If the attacker sets the TLV length below 5, the subsequent readByte/readInt throws IndexOutOfBoundsException. HAProxyMessageDecoder only catches HAProxyProtocolException around this call, so the IOOBE p…

---

## 18. 🟡 High Severity — Netty has Unbounded Direct Memory Consumption in its RedisDecoder

**CVE:** `CVE-2026-44890` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-6ghj-frrj-jjj3>

> ### Summary
An attacker can cause DoS by sending crafted Redis payloads across multiple connections without `\r\n`. This exhausts the server&#x27;s direct memory pool (OutOfDirectMemoryError), preventing legitimate connections from being processed.

### Details
io.netty.handler.codec.redis.RedisDecoder decodes the length of bulk strings and array headers using the `decodeLength` method. This metho…

---

## 19. 🟡 High Severity — Critical Check Point VPN Flaw Exploited to Bypass Passwords in IKEv1 Setups

**CVE:** `CVE-2026-50751` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://thehackernews.com/2026/06/critical-check-point-vpn-flaw-exploited.html>

> Check Point has warned of active exploitation of a critical vulnerability impacting Remote Access VPN and Mobile Access deployments that are configured to use the deprecated IKEv1 key exchange protocol.

The vulnerability, tracked as CVE-2026-50751 (CVSS score: 9.3), is a case of a logic flow weakness in certificate validation that allows an unauthenticated remote attacker to bypass user

---

## 20. 🟡 High Severity — GeoNode contains a server-side request forgery vulnerability in the service registration endpoint

**CVE:** `CVE-2026-39922` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-08
**Reference:** <https://github.com/advisories/GHSA-hw9r-6m78-w6h3>

> GeoNode versions 4.4.5 and 5.0.2 (and prior within their respective releases) contain a server-side request forgery vulnerability in the service registration endpoint that allows authenticated attackers to trigger outbound network requests to arbitrary URLs by submitting a crafted service URL during form validation. Attackers can probe internal network targets including loopback addresses, RFC1918…

---

## 21. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
