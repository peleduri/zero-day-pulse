# Zero Day Pulse

> **Generated:** 2026-06-29 10:20 UTC &nbsp;|&nbsp; **Total:** 12 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 2 &nbsp;|&nbsp; ✨ Enriched: 3

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE‑2024‑57727 is a directory‑traversal flaw that lets unauthenticated remote attackers read arbitrary files on the SimpleHelp server via crafted HTTP requests.
- **Affected Products:** SimpleHelp remote support software (SimpleHelp Remote Monitoring and Management) version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** A public proof‑of‑concept is hosted on GitHub at https://github.com/imjdl/CVE-2024-57727
- **Patch Available:** The vendor released a patch for SimpleHelp 5.5.7 and earlier within two days of reporting; the patch is available from the vendor advisory URL.
- **Active Exploitation:** CISA advisory and security reports confirm that ransomware actors have actively exploited CVE-2024-57727 in the wild.
- **Threat Actors:** Ransomware actors (unspecified groups) have been reported exploiting this vulnerability.
- **Mitigation:** Apply the vendor patch from the advisory, upgrade to a version newer than 5.5.7, and restrict remote access to the RMM service.
- **Vendor Advisory:** http://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) injects malicious instructions into the data or tools an LLM consumes while completing a user query (potentially without direct user input); agentic automation and multiple data sources increase the attack surface.
- **Affected Products:** Google Workspace, Gemini (specific versions not provided)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit reported in the advisory or cited Workspace guidance.
- **Patch Available:** No single vendor 'patch' published; Google describes continuous engineering and layered defenses in the advisory (no discrete patch URL provided).
- **Active Exploitation:** No confirmed reports of active exploitation provided in the advisory; the advisory describes IPI as an evolving threat vector and a top priority but does not report confirmed in-the-wild exploitation.
- **Threat Actors:** None known
- **Mitigation:** Google recommends a layered defense strategy and continuous improvements to LLM resistance (engineering mitigations, layered defenses and monitoring) rather than a single-step workaround.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

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

- **Technical Details:** Chinese state-sponsored actors exploit CVEs in network devices such as backbone routers, provider edge (PE) routers, and customer edge (CE) routers to gain persistent access, leveraging compromised devices and trusted connections to pivot across networks.
- **Affected Products:** Backbone routers, Provider Edge (PE) routers, Customer Edge (CE) routers, Network edge devices
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit known.
- **Patch Available:** No official patch or remediation guidance is currently available from the vendor.
- **Active Exploitation:** Yes, active exploitation has been reported in the wild, targeting government, telecom, transportation, lodging, and military infrastructure networks.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Mitigation steps unavailable.
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

## 10. 🟠 Zero-Day — Microsoft Removes 119 Edge Extensions That Hid Malware in Images and Fonts

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-29
**Reference:** <https://thehackernews.com/2026/06/microsoft-removes-119-edge-extensions.html>

> Microsoft has shut down a long-running malicious extension operation on the Edge Add-ons store that hid its payloads inside ordinary image and font files, then woke up days after install to steal credentials and run ad fraud.

The company calls it StegoAd, a mash-up of steganography and adware, and ties 119 extensions to a single threat actor it says has been active since at least 2021.

---

## 11. 🟡 High Severity — Public PoC Released for Critical libssh2 CVE-2026-55200 Client-Side SSH Flaw

**CVE:** `CVE-2026-55200` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-29
**Reference:** <https://thehackernews.com/2026/06/public-poc-released-for-critical.html>

> A public proof-of-concept is now out for CVE-2026-55200, a critical flaw in libssh2 that lets a malicious or compromised SSH server trigger memory corruption on a connecting client, with possible code execution. No credentials, no user interaction. The bug affects every release up to and including 1.11.1 and carries a CVSS 4.0 score of 9.2.

libssh2 is a client-side SSH library, not a server.

---

## 12. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
