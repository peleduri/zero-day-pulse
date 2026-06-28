# Zero Day Pulse

> **Generated:** 2026-06-28 19:01 UTC &nbsp;|&nbsp; **Total:** 10 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 9 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 5

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal vulnerability that allows unauthenticated attackers to read arbitrary files via directory traversal.
- **Affected Products:** SimpleHelp remote support software v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Public PoC available on GitHub: https://github.com/imjdl/CVE-2024-57727
- **Patch Available:** Yes, SimpleHelp released patch version 5.5.8 (also 5.4.10 and 5.3.9). See https://community.simple-help.com/t/sh-5-5-8-update/1569
- **Active Exploitation:** Confirmed; ransomware actors exploited CVE-2024-57727 in the wild, as reported by CISA.
- **Threat Actors:** Ransomware actors
- **Mitigation:** Upgrade to the latest patched version (5.5.8 or newer) and apply security hardening; upgrade is the recommended mitigation.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) — attackers seed instructions inside web content (hidden text, white-text on white background, font-mapping/formatting tricks, hidden HTML or script-obfuscated instructions) that browsing AI agents may ingest; these embedded instructions attempt to override or influence the agent's behavior when the agent fetches and processes web pages.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept (PoC) or weaponized exploit URL published in the vendor post; Google and researchers report finding IPI payloads in the wild but do not publish exploit code in the advisory.
- **Patch Available:** No vendor patch released. The Google post describes detection, monitoring and mitigation work (web sweeps, pattern filtering, hardening) rather than a product software patch or versioned update.
- **Active Exploitation:** Google reports confirmed malicious indirect prompt injection attempts found on public websites and an increase in malicious IPI activity; coverage by third parties (e.g., Help Net Security) corroborates detections of IPI payloads in the wild.
- **Threat Actors:** None known
- **Mitigation:** Use input filtering and hardening for web-browsing agents (detect and ignore hidden/styled instructions), monitor and remove IPI payloads from owned sites, apply content sanitation and strict parsing for any browsed pages, and block/flag known IPI patterns. (Vendor recommends monitoring + engineering hardening.)
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow in the CrabbyAVIF Rust library could have caused out‑of‑bounds accesses; Android’s Scudo hardened allocator mitigated the issue by rendering it non‑exploitable.
- **Affected Products:** Android platform – CrabbyAVIF library (AVIF image decoding)
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** No public proof‑of‑concept or weaponized exploit is known.
- **Patch Available:** https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050
- **Active Exploitation:** No confirmed active exploitation has been reported; the vulnerability was a near‑miss and never shipped in a public release.
- **Threat Actors:** None known
- **Mitigation:** Patch applied to CrabbyAVIF in AOSP; Scudo hardened allocator provides additional protection; update Android to the patched version.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** State-sponsored APT actors exploit publicly known CVEs in internet‑facing backbone, provider-edge (PE) and customer-edge (CE) routers and abuse management features (SSH, SNMP, web GUIs, Guest Shell) to install persistent backdoors, modify ACLs/routing, create GRE/IPsec tunnels for exfiltration, enable traffic mirroring, and capture authentication traffic; they often enable services on non‑standard high ports and insert SSH keys or SNMP SETs to maintain access.
- **Affected Products:** Backbone routers, provider-edge (PE) routers, customer-edge (CE) routers, Cisco IOS / IOS XE (Guest Shell), Cisco NX‑OS (Guest Shell) — specific vendor versions not enumerated in advisory.
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit was identified in the cited advisory or industry reporting; sources do not reference a public PoC.
- **Patch Available:** No vendor patch reported in the advisory; industry reporting notes no official vendor remediation available as of the advisory (see sources).
- **Active Exploitation:** Yes — the CISA advisory and allied agencies report confirmed, ongoing exploitation in the wild targeting telecommunications and other sectors (see advisory and NSA/industry statements).
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching for known exploited CVEs on edge devices; isolate management plane (management VRF/out-of-band), block management egress except to authorized collectors, apply control-plane policing (CoPP) and management ACLs (default-deny) for SSH/HTTPS/SNMP/TACACS+/RADIUS, use SSHv2 and SNMPv3 (disable Telnet/SNMPv1/v2), enforce strong ciphers, restrict management to approved jump hosts/subnets, rate-limit management protocols, disable or harden Guest Shell on Cisco IOS XE/NX‑OS (or disable if not required), inventory and upgrade unsupported devices, and monitor/alert on unusual configuration changes (ACLs, tunnels, SNMP SETs, unexpected high ports).
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 9. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 10. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

**Parallel AI Enrichment:**

- **Technical Details:** A malicious DNS response can trigger out-of-bounds reads and writes, leading to memory safety issues and potential remote code execution in the Pixel baseband modem firmware.
- **Affected Products:** Google Pixel 10 baseband modem firmware
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** No known exploits are available.
- **Patch Available:** Patches are available. See the vendor advisory for details.
- **Active Exploitation:** No active exploitation has been reported.
- **Threat Actors:** None known
- **Mitigation:** Integrate a memory-safe Rust DNS parser into the Pixel baseband modem firmware to address memory safety vulnerabilities.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html

---
