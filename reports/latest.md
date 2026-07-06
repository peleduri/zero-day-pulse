# Zero Day Pulse

> **Generated:** 2026-07-06 19:32 UTC &nbsp;|&nbsp; **Total:** 18 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 11 &nbsp;|&nbsp; 🟡 High: 7 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path‑traversal vulnerability in SimpleHelp (v5.5.7 and earlier) that allows unauthenticated remote attackers to craft HTTP requests to read/download arbitrary files from the host (server configuration, secrets, hashed passwords).
- **Affected Products:** SimpleHelp Remote Support / Remote Monitoring and Management (RMM) — versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — public proof‑of‑concept code has been published (GitHub repository: https://github.com/imjdl/CVE-2024-57727) and third‑party writeups describe exploitation steps.
- **Patch Available:** Yes — SimpleHelp published fixes for the vulnerabilities (vendor KB/release notes). See vendor advisory: https://simple-help.com/kb---security-vulnerabilities-01-2025
- **Active Exploitation:** Confirmed — CISA reported ransomware actors exploited unpatched SimpleHelp instances (including a compromise of a utility billing software provider) and included the CVE in its Known Exploited Vulnerabilities catalog.
- **Threat Actors:** Ransomware actors (unnamed in the public advisories)
- **Mitigation:** Apply vendor patches or follow vendor mitigations immediately; if you cannot patch, apply the mitigations from the CISA advisory (or discontinue use). See vendor guidance and CISA advisory for step-by-step mitigations.
- **Vendor Advisory:** https://simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — Prompt Injection Attacks Trick AI Agents Into Making Crypto Payments

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://www.securityweek.com/prompt-injection-attacks-trick-ai-agents-into-making-crypto-payments/>

> Researchers uncovered two campaigns embedding indirect prompt injections in malicious websites to exploit autonomous AI agents browsing the web. The post Prompt Injection Attacks Trick AI Agents Into Making Crypto Payments appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is an Indirect Prompt Injection (IPI) where threat actors embed malicious instructions in web content retrieved by autonomous AI agents. Attackers use SEO poisoning to attract agents, and then use techniques like JSON-LD structured metadata (e.g., misrepresenting a site as a SoftwareApplication with an 'offers' object) and CSS hiding (positioning content off-screen) to deliver prompts that are invisible to humans but readable by the agent. These prompts instruct the agent to ignore previous directions and execute specific actions, such as making cryptocurrency payments or misclassifying fraudulent sites as authoritative sources.
- **Affected Products:** Llama 3.3 70B Instruct, Llama 3.2 90B Vision Instruct, Gemini 3 Flash, Gemini 2.5 Pro, GPT-5.4, Claude Sonnet 4.5
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes, the exploit consists of specific Indirect Prompt Injection (IPI) patterns embedded in malicious websites, as detailed and demonstrated by Zscaler.
- **Patch Available:** No official patch is available as this vulnerability is a behavioral characteristic of Large Language Models (LLMs) susceptible to indirect prompt injection rather than a software bug.
- **Active Exploitation:** Confirmed. Zscaler ThreatLabz identified two active campaigns: one involving a payment scam utilizing SEO poisoning for a fake Python library (requests-secure-v2), and another using typosquatting to impersonate the DeBank cryptocurrency platform.
- **Threat Actors:** None known
- **Mitigation:** Mitigation involves treating all retrieved web content as an untrusted attack surface. Recommendations include improving the agent's ability to identify and filter out hidden instructions and implementing stricter validation for payment-executing tools to prevent context contamination and Retrieval-Augmented Generation (RAG) poisoning.
- **Vendor Advisory:** https://www.zscaler.com/blogs/security-research/indirect-prompt-injection-web-content-targets-ai-agents

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an AI system ingests external content (web pages, email, documents) that contains embedded instructions; the model may follow those hidden instructions instead of the user's intent. Observed patterns include deterrence instructions, infinite-stream pages to waste/timeout resources, data-exfiltration prompts, and destructive command text — detected via pattern matching, LLM-based classification, and human validation.
- **Affected Products:** AI agents and systems that process external content (e.g., AI assistants that browse or summarize web pages — Google Gemini and GenAI-enabled Google Workspace are cited examples)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof-of-concept prompts and academic PoCs exist in research (2025 research is referenced), but Google did not observe widespread, productionized weaponized exploits in their Common Crawl web scan (they observed only a small number of data-exfiltration attempts and largely low-sophistication experiments).
- **Patch Available:** No single vendor 'patch' exists for IPI (it is a class of behavioural/agent attack). Google has published mitigation guidance and hardening posts instead (examples: https://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html and https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html).
- **Active Exploitation:** Google observed active experimentation on the public web (small numbers of malicious pages and experiments) and a measured uptick — a 32% relative increase in pages classified as malicious between November 2025 and February 2026 in their Common Crawl analysis — but the study did not find evidence of large-scale, productionized exploitation in that dataset and it excluded social media.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: detect likely injection signatures (pattern matching), use model/LLM-based intent classification and human validation for suspicious content, red-team and hardening testing, restrict agent actions (avoid translating LLM output directly into OS-level commands), sandbox and rate-limit content processing, and follow vendor mitigation guidance (see Google Workspace mitigation and layered-defense posts).
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) allows an attacker to influence an LLM's behavior by injecting malicious instructions into external data or tools used by the LLM during a query, which can occur without direct user input. In the case of GeminiJack, attackers used hidden instructions in shared Workspace files, emails, or invites to steer the AI and leak corporate data.
- **Affected Products:** Google Workspace with Gemini, Google Gemini Enterprise
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** A public proof-of-concept for indirect prompt injection in AI-powered browsers is available on GitHub (https://github.com/brennanbrown/atlas-prompt-injection-poc). Additionally, Noma Labs reported the GeminiJack vulnerability.
- **Patch Available:** For general indirect prompt injection (IPI), Google states it is an evolving threat that is continuously mitigated rather than solved with a single patch. However, a specific zero-click flaw known as 'GeminiJack' was reported as fixed by Google on December 11, 2025.
- **Active Exploitation:** Active exploitation of indirect prompt injection has been reported 'in the wild' by multiple sources, including Forcepoint and Palo Alto Networks. Specifically, GeminiJack was identified as a zero-click vulnerability that could lead to data exfiltration.
- **Threat Actors:** None known
- **Mitigation:** Google employs a layered defense strategy including: (1) Deterministic Defenses such as user confirmation, URL sanitization, tool chaining policies, and regex takedowns; (2) ML-Based Defenses through continuous retraining of models using synthetic data; (3) LLM-Based Defenses via refined system instructions and prompt engineering; and (4) Gemini Model Hardening to improve the model's internal ability to ignore harmful instructions.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** An indirect prompt-injection (zero-click) vulnerability in Gemini Enterprise / Vertex AI search where attacker-controlled content (e.g., hidden instructions inside shared Workspace files, emails, calendar invites or other data sources) can cross the trust boundary into the model’s instruction context, steering the model and enabling data leakage from corporate data sources.
- **Affected Products:** Google Gemini Enterprise (Vertex AI / Gemini Enterprise integrations with Google Workspace — shared files, emails, calendar invites)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept for 'GeminiJack' was found in the corpus. Related benign PoCs for indirect prompt-injection style issues exist (demonstrations of indirect prompt injection in AI-powered browsers).
- **Patch Available:** Yes — Google released a fix for the issue (reported in media Dec 10–11, 2025). See vendor blog (architecting security for agentic capabilities) and independent coverage noting Google fixed GeminiJack.
- **Active Exploitation:** No confirmed reports of active exploitation in the wild in the provided sources; press coverage describes how the flaw could have been exploited but does not report confirmed in-the-wild use.
- **Threat Actors:** None known
- **Mitigation:** Apply vendor updates/patches (Google reported fixes), and adopt the vendor guidance and layered defenses for agentic browsing (update Chrome/agentic components, restrict origin access and agent capabilities, limit/avoid placing sensitive instructions/data in shared documents or untrusted content).
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow was identified in CrabbyAVIF (a Rust-based AVIF image parser/decoder). The issue was described as a "near-miss" and was caught before shipping.
- **Affected Products:** CrabbyAVIF
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** None known
- **Patch Available:** Fixed before shipping (no public patch/advisory URL provided in the sources).
- **Active Exploitation:** None known
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injections involve hidden malicious instructions within external data sources, such as emails, documents, or calendar invites, which can trick the AI into exfiltrating user data or executing rogue actions.
- **Affected Products:** Gemini, Gemini in Google Workspace, Gemini app
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Indirect prompt injection is a known attack vector with public proof-of-concepts; however, no specific weaponized exploit URL for Gemini is provided in the advisory. The advisory mentions the 'EchoLeak' (CVE-2025-32711) vulnerability as a known attack that Gemini is protected against.
- **Patch Available:** Google has deployed Gemini 2.5 model hardening and system-level safeguards as the primary means of mitigation.
- **Active Exploitation:** Confirmed; Google reports that its built-in defenses have successfully mitigated indirect prompt injection attacks in the wild, providing users with notifications when such attacks are blocked.
- **Threat Actors:** None known
- **Mitigation:** A layered defense strategy including Gemini 2.5 model hardening (adversarial training), prompt injection content classifiers, security thought reinforcement, markdown sanitization and suspicious URL redaction (via Google Safe Browsing), a Human-In-The-Loop (HITL) user confirmation framework, and end-user security mitigation notifications.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors target and exploit vulnerabilities in network-edge devices (backbone routers, provider-edge and customer-edge routers) and chain authentication bypasses and command-injection flaws to modify routers for persistent, long-term access; they also pivot using compromised devices and trusted connections into other networks.
- **Affected Products:** Ivanti Connect Secure (CVE-2024-21887), Ivanti Policy Secure (related CVEs), Palo Alto GlobalProtect (CVE-2024-3400), Cisco IOS XE (CVE-2023-20198, CVE-2023-20273), Cisco (CVE-2018-0171), Fortinet (vendors named, CVEs not specified in advisory), Juniper (vendors named, CVEs not specified), Microsoft Exchange (vendors named, CVEs not specified)
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit has been reported for the specific activity described in AA25-239A; CISA and multiple reporting sources state there are no known exploits in the wild for the new activity described.
- **Patch Available:** No — multiple sources in the corpus state that no official vendor patch or remediation guidance is currently available for the activity described.
- **Active Exploitation:** CISA reports targeting and compromises of network-edge devices but states 'Exploitation of zero-day vulnerabilities has not been observed to date.' Other reporting lists exploited CVEs in Cisco/Ivanti/Palo Alto devices (reports of active exploitation of known CVEs), but no broadly published zero-day PoC tied to AA25-239A is documented in the cited corpus.
- **Threat Actors:** People's Republic of China (PRC) state-sponsored cyber threat actors — named groups include Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Create alarms/alerts for unusual router activity; deploy vendor guidance where available; monitor for the advisory's IOCs/STIX feeds and detection tips; harden and segment network-edge devices and restrict/monitor management access.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** GRU unit 26165 used credential guessing/brute force and spearphishing (including malicious attachments/links) for initial access, weaponized an Outlook NTLM vulnerability (CVE-2023-23397) to collect NTLM hashes via crafted calendar invites, exploited Roundcube CVEs to execute shell commands and access email, and leveraged a WinRAR flaw (CVE-2023-38831) to achieve code execution from archives; post-compromise activity included mailbox permission manipulation and sustained email collection, DLL search-order hijacking, lateral movement using tools like Impacket/PsExec, and exfiltration.
- **Affected Products:** Microsoft Outlook (CVE-2023-23397), Roundcube Webmail (vulnerable: before 1.2.13; 1.3.x before 1.3.16; 1.4.x before 1.4.10 — CVE-2020-12641/CVE-2020-35730/CVE-2021-44026), RARLAB WinRAR (CVE-2023-38831)
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — multiple CVEs referenced in the advisory were weaponized/observed in active campaigns (e.g., CVE-2023-23397 was weaponized to collect NTLM hashes; CVE-2023-38831 was reported exploited in the wild). The corpus does not provide a public PoC URL.
- **Patch Available:** Partial — the advisory lists fixed Roundcube versions (implying vendor patches/updates for Roundcube CVEs). The corpus shows vendor/NVD entries for the other CVEs but does not include direct vendor patch URLs for all CVEs in the advisory.
- **Active Exploitation:** Yes — CISA documents that actors weaponized CVE-2023-23397 and used it in campaign activity; NVD notes CVE-2023-38831 was exploited in the wild (April–October 2023).
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th GTsSS, unit 26165 (tracked in industry as APT28 / GRU unit 26165)
- **Mitigation:** Follow CISA guidance: network segmentation and access restrictions; apply Zero Trust principles; configure host firewalls to limit legitimate flows; collect and monitor Windows logs and alert on suspicious events; enable Windows security features and Attack Surface Reduction rules to block execution from email and globally writable directories; change default credentials and disable weak authentication; enable and enforce MFA where possible.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

**Parallel AI Enrichment:**

- **Technical Details:** Pre-authentication OS command injection (CWE-78) in Ivanti Sentry management API allowing a remote unauthenticated attacker to execute arbitrary commands as root (root-level RCE).
- **Affected Products:** Ivanti Sentry 10.5.1, 10.6.1, 10.7.0 and prior (fixed in 10.5.2, 10.6.2, 10.7.1)
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Exploit Available:** Yes — a public proof-of-concept was released around June 10, 2026 and has been used for scanning/exploitation attempts.
- **Patch Available:** Yes — Ivanti published fixes and provides updated Sentry images (10.5.2, 10.6.2, 10.7.1) in its advisory: https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523?language=en_US
- **Active Exploitation:** Exploitation attempts and scanning using a public PoC have been observed (reports from Shadowserver, CrowdSec and multiple security vendors). Ivanti states it was not aware of customer compromises at time of disclosure, but CISA added the CVE to its Known Exploited Vulnerabilities catalog due to observed attempts.
- **Threat Actors:** None known
- **Mitigation:** Update Sentry to the fixed versions (10.5.2, 10.6.2, 10.7.1). Do NOT expose the management interface (port 8443) to the Internet; restrict management-plane access and enable mTLS where applicable (EPMM-managed appliances).
- **Vendor Advisory:** https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523?language=en_US

---

## 11. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 12. 🟡 High Severity — chmod: --preserve-root bypassed by any path that resolves to root (e.g. /../)

**CVE:** `CVE-2026-35338` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-4c7q-4928-8445>

> `Chmoder::chmod()` only compares the literal argument against `Path::new(&quot;/&quot;)`, so the `--preserve-root` guard is bypassed by any path that *resolves* to root — a symlink to `/` or simply `/../`.

```
if self.recursive &amp;&amp; self.preserve_root &amp;&amp; file == Path::new(&quot;/&quot;) {
    return Err(ChmodError::PreserveRoot(&quot;/&quot;.to_string()).into());
}
```

**PoC** — re…

---

## 13. 🟡 High Severity — 16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems

**CVE:** `CVE-2026-53359` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://thehackernews.com/2026/07/16-year-old-linux-kvm-flaw-lets-guest.html>

> A use-after-free bug in Linux&#x27;s KVM hypervisor can be triggered from a guest virtual machine to corrupt the shadow-page state of the host kernel that runs it.

Dubbed &#x27;Januscape&#x27; and tracked as CVE-2026-53359, the flaw sits in the shadow MMU code that KVM shares across both Intel and AMD. The public proof-of-concept panics the host; the researcher claims that a separate, unreleased …

---

## 14. 🟡 High Severity — flyto-core has SSRF guard bypass via IPv6 transition addresses (IPv4-mapped / 6to4 / NAT64) in validate_url_ssrf

**CVE:** `CVE-2026-55787` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-794r-5rp2-fpg8>

> ## Summary

`flyto-core`&#x27;s SSRF protection (`validate_url_ssrf` / `is_private_ip` in `src/core/utils.py`) blocks private and metadata destinations by resolving the host and testing the resulting IP for membership in a hardcoded `PRIVATE_IP_RANGES` list. That list contains only the *native* RFC 1918 / loopback / link-local / unique-local ranges. It does **not** account for IPv6 transition addr…

---

## 15. 🟡 High Severity — Cilium vulnerable to sensitive information disclosure and cluster disruption via local Envoy admin socket access

**CVE:** `CVE-2026-49445` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-3fcv-jvfp-m4q9>

> ### Impact

When Cilium L7 functionality is enabled on a cluster, the Envoy instance supporting this functionality creates a world-accessible socket on cluster nodes. A local attacker would be able to access Envoy admin endpoints. Depending on deployment configuration, this can expose sensitive information or allow disruptive administrative operations, such as:

- Exposing TLS secrets
- Disrupting…

---

## 16. 🟡 High Severity — Formie Hidden field defaults vulnerable to Server-Side Template Injection

**CVE:** `CVE-2026-52889` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-565m-g33j-jq96>

> ## Summary
Formie Hidden fields could evaluate request-derived values as Twig during front-end form rendering.

When a Hidden field used a dynamic default value such as HTTP User Agent, Referer URL, Current URL, Query Parameter, or Cookie Value, the value was copied from the incoming request and later passed to Craft’s Twig rendering layer. This allowed an unauthenticated attacker to provide Twig …

---

## 17. 🟡 High Severity — Threat Actors Probe Gitea Docker Flaw CVE-2026-20896 13 Days After Disclosure

**CVE:** `CVE-2026-20896` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://thehackernews.com/2026/07/threat-actors-probe-gitea-docker-flaw.html>

> Threat actors have been observed attempting to exploit a recently patched critical security flaw in Gitea Docker images, according to Sysdig.

The vulnerability in question is CVE-2026-20896 (CVSS score: 9.8), a vulnerability that stems from the DevOps platform trusting the &quot;X-WEBAUTH-USER&quot; header from any source IP address, effectively allowing an unauthenticated internet client to get …

---

## 18. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
