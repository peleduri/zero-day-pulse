# Zero Day Pulse

> **Generated:** 2026-06-03 20:47 UTC &nbsp;|&nbsp; **Total:** 19 &nbsp;|&nbsp; 🔴 KEV: 1 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 4 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🔴 CISA KEV — CVE-2026-45247 — Mirasvit Full Page Cache Warmer Deserialization of Untrusted Data Vulnerability

**CVE:** `CVE-2026-45247` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-45247>

> Vendor: Mirasvit | Product: Mirasvit Full Page Cache Warmer. Mirasvit Full Page Cache Warmer contains a deserialization of untrusted data vulnerability that could allow unauthenticated attackers to achieve remote code execution by supplying a crafted serialized PHP object in the CacheWarmer cookie. Required action: Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for…

**Parallel AI Enrichment:**

- **Technical Details:** The extension unserializes attacker‑controlled data from the CacheWarmer cookie using PHP’s native unserialize(), leading to PHP Object Injection (CWE‑502). Crafted serialized objects can chain gadgets in Magento and its dependencies (e.g., Monolog handlers) to achieve unauthenticated remote code execution.
- **Affected Products:** Mirasvit Full Page Cache Warmer for Magento 2 versions before 1.11.12
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Upgrade to Mirasvit Full Page Cache Warmer version 1.11.12 or later. If an immediate upgrade is not possible, block or inspect the CacheWarmer cookie at the edge (WAF) and monitor logs for base64‑encoded serialized objects.
- **Vendor Advisory:** https://mirasvit.com/package/changelog/?package=mirasvit%2Fmodule-cache-warmer

---

## 2. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal / directory traversal in SimpleHelp (CVE‑2024‑57727) allows unauthenticated remote attackers to read sensitive files (logs, configs, credentials) via crafted requests to vulnerable endpoints.
- **Affected Products:** SimpleHelp remote support / RMM, versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (including DragonForce)
- **Mitigation:** Update SimpleHelp to 5.5.8 or later; if patching delayed, isolate/unexpose SimpleHelp from the internet, restrict access via firewall/VPN, rotate credentials, audit logs, and apply network segmentation.
- **Vendor Advisory:** https://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 3. 🟠 Zero-Day — The sorry state of skill distribution

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Trail of Bits Blog &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://blog.trailofbits.com/2026/06/03/the-sorry-state-of-skill-distribution/>

> Public skill marketplaces are being flooded with malicious skills that steal credentials, exfiltrate data, and hijack agents. In response, a segment of the security industry released skill scanners, a new family of tools designed to detect malicious skills before they’re installed. But we tested them, and they don’t work. We recently bypassed ClawHub’s malicious skill detector , Cisco’s agent skil…

**Parallel AI Enrichment:**

- **Technical Details:** Malicious skills are built to steal credentials, exfiltrate data, and hijack agents by employing straightforward bypass techniques such as simple obfuscation and innocuous‑looking entry points; the researchers created four malicious skills in under an hour that evaded ClawHub, Cisco, and skills.sh detectors.
- **Affected Products:** ClawHub (OpenClaw/ClawHub skill marketplace), Cisco agent skill scanner, skills.sh integrated scanners
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — https://blog.trailofbits.com/2026/06/03/the-sorry-state-of-skill-distribution/
- **Patch Available:** false — No official vendor patch or advisory located; Vendor advisory URL unavailable.
- **Active Exploitation:** true — https://snyk.io/articles/clawdhub-malicious-campaign-ai-agent-skills/
- **Threat Actors:** None known
- **Mitigation:** Disable automatic installation of third‑party skills; require manual code review for skill packages; run skills in strongly sandboxed environments with least privilege; enforce signing and provenance checks for skill packages; deploy runtime monitoring and data exfiltration detection.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when attackers embed malicious instructions in web content (hidden via CSS, HTML comments, accessibility attributes, meta tags, etc.). AI agents that ingest such content can execute attacker instructions (API key exfiltration, financial fraud, data destruction, unauthorized navigation, denial‑of‑service, output hijacking) because they may treat attacker‑controlled text as legitimate instructions. The attack chain is: attacker‑poisoned web content → hidden payload ingestion by AI agent → collapse of trust boundary → execution of real‑world actions with covert exfiltration channels.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Use layered defenses: restrict AI agents from treating untrusted content as executable instructions; apply concealment detection (hidden CSS/comment parsers), context‑aware filtering, provenance/metadata validation, block known IPI URLs at network layer; harden agentic capabilities (limit automated payments/navigation); monitor telemetry for IPI indicators and share intelligence.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack technique that injects adversarial instructions into data sources or tools an LLM accesses during completion (e.g., documents, web pages, tool outputs). The LLM may execute or follow these instructions without explicit user input, causing it to disclose data, bypass policies, or perform unintended actions. IPI leverages agentic automation and multi-source context to influence model behavior indirectly.
- **Affected Products:** Google Workspace (with Gemini)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Google advises a layered defense including data provenance and validation, sanitization/normalization of inputs, model grounding to trusted sources, policy‑scoring and signal‑based filtering of external content, limiting agentic tool access, monitoring and anomaly detection, and continuous updates to detection rules. (No single patch—defense is ongoing.)
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability leverages indirect prompt injection: a crafted webpage or repository can feed malicious content to an agentic LLM, causing it to execute unsafe actions such as data exfiltration or fraudulent transactions. In the Gemini CLI/CI case, untrusted workspace configuration files could be loaded in headless/CI mode, allowing an attacker to trigger remote code execution via malicious .gemini files and bypass tool allowlists in --yolo mode.
- **Affected Products:** Chrome agentic browsing / Gemini integration in Chrome, @google/gemini-cli < 0.39.1, google-github-actions/run-gemini-cli < 0.1.22
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true - https://github.com/google-github-actions/run-gemini-cli/security/advisories/GHSA-wpqr-6v78-jr5g
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor‑released updates for Chrome agentic browsing (enable User Alignment Critic, Origin Sets, and prompt‑injection detection). Upgrade @google/gemini-cli to version 0.39.1 or higher and google‑github‑actions/run‑gemini‑cli to version 0.1.22 or higher. Configure GEMINI_TRUST_WORKSPACE=false by default and only set it to true for trusted CI inputs. Restrict agent origin sets to known sites and require manual user confirmation for sensitive actions.
- **Vendor Advisory:** https://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow was identified in the CrabbyAVIF Rust implementation (unsafe Rust near‑miss). Android’s Scudo hardened allocator rendered the issue non‑exploitable by using guard pages around secondary allocations, turning silent corruption into a crash.
- **Affected Products:** CrabbyAVIF (platform/external/rust/crabbyavif) – vulnerability found pre‑release and did not ship; no public releases were affected.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use Scudo hardened allocator (make it mandatory where possible), ensure crash reporting surfaces overflows into Scudo guard pages, prioritize unsafe‑Rust review and training (new unsafe module in Comprehensive Rust training), and apply the published patch.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** An indirect prompt injection injects hidden malicious instructions into external data (emails, documents, calendar invites) that are later incorporated into AI prompts, causing the model to act on rogue commands like data exfiltration.
- **Affected Products:** Google Gemini, Google Workspace apps
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Implement Google’s layered defense strategy: validate and sanitize external data before it reaches AI models, apply context‑aware filtering, monitor for suspicious content in emails/documents/calendar invites, and enforce runtime protections in Gemini and Google Workspace apps.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors modify router configurations to move laterally between networks and run virtualized containers on network devices to evade detection; initial access is achieved by exploiting publicly known CVEs such as CVE‑2024‑21887 and CVE‑2024‑3400.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching, monitor firmware/software integrity, disable unused ports and protocols, change default credentials, require public‑key authentication, and follow vendor hardening guidance and Cisco‑specific recommendations.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Exploitation of public-facing services (VPNs, web applications) using known CVEs (CVE‑2023‑38831, CVE‑2020‑35730, CVE‑2020‑12641) and SQL injection; WinRAR before 6.23 allows arbitrary code execution via crafted archive files; Roundcube Webmail suffers XSS and command injection; attackers employ Impacket, PsExec, and RDP for lateral movement and credential dumping.
- **Affected Products:** WinRAR (versions prior to 6.23), Roundcube Webmail (versions <1.2.13, <1.3.16, <1.4.10), IP cameras (any unsupported or unpatched models)
- **CVSS Score:** CVE-2020-35730: 6.1; CVE-2020-12641: 9.8; CVE-2023-38831: unavailable
- **CVSS Vector:** CVE-2020-35730: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N; CVE-2020-12641: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Russian GRU 85th GTsSS (Unit 26165), APT28, Fancy Bear, Forest Blizzard, Blue Delta
- **Mitigation:** Apply security patches for WinRAR and Roundcube; update firmware on IP cameras; employ network segmentation and Zero Trust architecture; restrict VPN and remote access; configure host firewalls and inbound traffic filtering; disable unnecessary remote access to IP cameras.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 11. 🟠 Zero-Day — Beyond the Zero-Day: See Your Network Like an Attacker | Webinar with HD Moore

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://thehackernews.com/2026/06/beyond-zero-day-see-your-network-like.html>

> Assume the breach. Zero-days keep shipping, AI is writing exploits faster than anyone patches, and &quot;patch everything in time&quot; stopped working years ago. Stop betting the org on winning that race. You don&#x27;t control which bug lands. You control what it can reach once it does.

That is a question about the shape of your network, and most teams have the shape wrong. HD Moore, creator of…

---

## 12. 🟠 Zero-Day — Acer working to patch max severity zero-days in Wave 7 routers

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://www.bleepingcomputer.com/news/security/acer-warns-of-max-severity-zero-days-affecting-wave-7-routers/>

> Acer is working to address two maximum-severity zero-day vulnerabilities affecting its Wave 7 mesh routers. [...]

---

## 13. 🟠 Zero-Day — Unpatched Windows Search URI Vulnerability Lets Attackers Steal NTLMv2 Hashes

**CVE:** `CVE-2026-33829` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://thehackernews.com/2026/06/unpatched-windows-search-uri.html>

> Cybersecurity researchers have disclosed details of an unpatched issue that could be exploited to disclose a user&#x27;s NTLMv2 hash to the attacker.

Like in the case of CVE-2026-33829, which impacted the Windows Snipping Tool&#x27;s ms-screensketch: URI handler, the newly flagged issue resides in the search: URI handler, per Huntress.

CVE-2026-33829 refers to a spoofing vulnerability that could…

---

## 14. 🟠 Zero-Day — Microsoft Tries to Calm Legal Threat Fears After Zero-Day Disclosure Backlash

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://www.securityweek.com/microsoft-tries-to-calm-legal-threat-fears-after-zero-day-disclosure-backlash/>

> Microsoft responds to backlash over its threats of legal action against researchers who publicly disclose zero-day vulnerabilities. The post Microsoft Tries to Calm Legal Threat Fears After Zero-Day Disclosure Backlash appeared first on SecurityWeek .

---

## 15. 🟠 Zero-Day — VS Code zero-day lets hackers steal GitHub tokens in one click

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://www.bleepingcomputer.com/news/security/vs-code-zero-day-lets-hackers-steal-github-tokens-in-one-click/>

> A security researcher has released exploit code for a Visual Studio Code (VS Code) zero-day vulnerability that allows attackers to steal GitHub authentication tokens by tricking users into clicking a link. [...]

---

## 16. 🟡 High Severity — backpack/crud is vulnerable to Cross-Site Scripting (XSS)

**CVE:** `CVE-2022-31114` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-m8xx-3x29-84h8>

> ### Impact

It’s a “*moderate*” vulnerability… but being an admin panel, take this seriously. It’s difficult… but an attacker could conduct a targeted phishing campaign, in order to **trick your users or admins to click a malicious link, which under very specific circumstances could give them information... or even admin access**. It’s *unlikely*, but that’s not good enough in admin panels - It sh…

---

## 17. 🟡 High Severity — Docling: Unsafe Zip Extraction in EasyOCR Model Download

**CVE:** `CVE-2026-44017` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-cjqg-rq2h-2fvj>

> ### Impact
In versions `&lt; 2.91.0`, The EasyOCR model download functionality extracted ZIP archives without validating member paths, enabling Zip Slip attacks. If an attacker could compromise the model download source (via supply chain attack, DNS spoofing, or MITM), they could write arbitrary files to any location writable by the process, potentially achieving:
- Remote code execution by overwr…

---

## 18. 🟡 High Severity — Critical Kirki flaw exploited to hijack WordPress admin accounts

**CVE:** `CVE-2026-8206` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-02
**Reference:** <https://www.bleepingcomputer.com/news/security/critical-kirki-flaw-exploited-to-hijack-wordpress-admin-accounts/>

> Hackers are exploiting a critical privilege escalation vulnerability (CVE-2026-8206) in the Kirki plugin for WordPress to take over any user account, including those belonging to administrators. [...]

---

## 19. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
