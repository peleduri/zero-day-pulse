# Zero Day Pulse

> **Generated:** 2026-05-24 02:01 UTC &nbsp;|&nbsp; **Total:** 11 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 1 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path traversal vulnerability in SimpleHelp 5.5.7 and earlier that permits unauthenticated attackers to read sensitive files (logs, configs, credentials) and potentially gain elevated access to the application, enabling downstream compromise.
- **Affected Products:** SimpleHelp Remote Support (versions 5.5.7 and earlier)
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Public proof‑of‑concept and weaponized exploit activity reported; see SecurityWeek article.
- **Patch Available:** Vendor released patched versions (post‑5.5.7); see vendor advisory URL.
- **Active Exploitation:** Confirmed active exploitation in the wild reported by CISA and security media.
- **Threat Actors:** DragonForce ransomware operators and other generic ransomware actors
- **Mitigation:** Immediately update SimpleHelp to a patched version (post‑5.5.7), do not expose instances to the Internet, apply vendor‑provided mitigations, restrict network access to management interfaces, rotate any credentials exposed in logs or configuration files, and monitor for indicators of compromise per CISA guidance.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — Drupal Core SQL Injection Bug Actively Exploited, Added to CISA KEV

**CVE:** `CVE-2026-9082` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://thehackernews.com/2026/05/drupal-core-sql-injection-bug-actively.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has added a recently patched critical security flaw impacting Drupal Core to its Known Exploited Vulnerabilities (KEV) catalog, based on evidence of active exploitation.

The vulnerability in question is CVE-2026-9082 (CVSS score: 6.5), an SQL injection vulnerability affecting all supported versions of Drupal Core.

&quot;Drupal Core

**Parallel AI Enrichment:**

- **Technical Details:** An SQL injection in Drupal Core’s database abstraction/entity query handling that allows unauthenticated attackers to inject SQL against PostgreSQL‑backed sites, leading to data disclosure or modification.
- **Affected Products:** Drupal Core versions from 8.9.0 before 10.4.10, from 10.5.0 before 10.5.10, from 10.6.0 before 10.6.9, from 11.0.0 before 11.1.10, from 11.2.0 before 11.2.12, from 11.3.0 before 11.3.10
- **CVSS Score:** 6.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N
- **Exploit Available:** Public proof‑of‑concept/working exploit reported (research writeups and PoC published) – examples: https://miggo.io/post/the-death-of-patch-first-exploiting-and-mitigating-drupal-cve-2026-9082-under-60-minutes, https://thehackernews.com/2026/05/drupal-core-sql-injection-bug-actively.html
- **Patch Available:** Yes – official Drupal security advisory with patches: https://www.drupal.org/sa-core-2026-004
- **Active Exploitation:** Confirmed – CISA added CVE‑2026‑9082 to its KEV catalog based on evidence of active exploitation.
- **Threat Actors:** None known
- **Mitigation:** Apply vendor patches immediately; if unable to patch, disable or restrict access to vulnerable endpoints, implement Web Application Firewall rules to block suspicious entity‑query parameters, and restrict external access to the site until patched.
- **Vendor Advisory:** https://www.drupal.org/sa-core-2026-004

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI): attackers embed malicious instructions into web content (HTML, text, hidden code) that AI agents may consume when crawling or summarizing pages; when parsed by an AI agent, these instructions can cause data exfiltration, destructive commands, or manipulation of outputs. Detection is hampered by benign uses of similar text and false positives; attacks observed include invisible/injected prompts, SEO manipulations, infinite-stream traps, and low-sophistication exfiltration attempts.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit reported for the IPI examples identified by Google; research indicates attackers are experimenting but not widely productionized (no PoC URL).
- **Patch Available:** Vendors (e.g., Google, Microsoft, Anthropic) have issued mitigations/patches for specific prompt‑injection issues in recent months; for this Google blog entry there is no single vendor advisory URL. Microsoft assigned CVE-2026-21520 to a Copilot Studio issue and patched it (see vendor advisories).
- **Active Exploitation:** Google’s analysis found experimental/malicious IPI instances on the public web but no evidence of large‑scale, highly sophisticated, productionized exploitation; trend shows a 32% relative increase in malicious detections between Nov 2025 and Feb 2026, indicating growing interest and likely future escalation.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: input filtering and pattern matching, LLM-based intent classification, human review for high-risk cases, product hardening by vendors (model- and agent-level safeguards), AI Vulnerability Reward Programs to surface issues, and monitoring/common-crawl scanning to detect campaign activity.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when malicious instructions are embedded within data or secondary tools (documents, web content, plug‑ins, etc.) consumed by an LLM‑enabled system; the attacker’s content causes the model or agentic automation to follow unintended instructions without direct user input.
- **Affected Products:** Google Workspace (features integrating Gemini and multi‑source AI tools)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC or weaponized exploit reported
- **Patch Available:** No single patch; vendor guidance and ongoing mitigations documented at the advisory URL above
- **Active Exploitation:** No confirmed widespread active exploitation reported; Google has observed increasing malicious IPI attempts on public web content but notes sophistication remains low
- **Threat Actors:** None known
- **Mitigation:** Layered defenses including input provenance and integrity controls, model instruction filtering, content‑classification and sanitization, limiting agentic tool access, runtime checks and human review/approval workflows; continuous monitoring and threat analysis.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection—malicious site or third‑party content provides instructions that influence agentic AI behavior; mitigations include origin restrictions, prompt‑injection detection/filters, and secondary monitoring agent to prevent unsafe AI actions.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** None known
- **Patch Available:** Google announced layered defenses and mitigations in Chrome for agentic/Gemini features (advisory: https://blog.google/security/architecting-security-for-agentic/)
- **Active Exploitation:** No confirmed active exploitation of a specific CVE reported; Google and other sources have observed increasing indirect prompt‑injection attempts in the wild.
- **Threat Actors:** None known
- **Mitigation:** Use the latest Chrome updates (contains announced defenses), restrict extensions & untrusted content, follow vendor guidance in the advisory URL.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow in the Rust‑implemented CrabbyAVIF image decoder could overwrite adjacent memory, but Android’s Scudo hardened allocator places guard pages around secondary allocations, rendering the overflow non‑exploitable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept or weaponized exploit is available.
- **Patch Available:** Patch released via commit 5262cd9befecb4f8865925c23eb543f19967e050 in the Android source repository.
- **Active Exploitation:** No active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Android’s Scudo hardened allocator renders the vulnerability non‑exploitable by placing guard pages around secondary allocations.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection involves embedding hidden malicious instructions in external data sources (emails, documents, calendar invites) that the AI model processes. When the model incorporates this data into its prompt, it may execute unintended commands, leading to actions like data exfiltration or unauthorized operations.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof‑of‑concepts and exploits have been observed for indirect prompt injection attacks.
- **Patch Available:** A patch fixing the issue is available in version 1.3 (see NVD entry).
- **Active Exploitation:** Active exploitation has been reported in 2025‑2026 across several AI platforms.
- **Threat Actors:** None known
- **Mitigation:** Apply a layered defense: validate and sanitize inputs at every stage of the prompt lifecycle, enforce strict context separation between user data and prompts, and monitor AI behavior for anomalies.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors gain initial access by exploiting publicly known CVEs such as CVE-2023-20198 (Cisco IOS XE web UI authentication bypass) and CVE-2018-0171 (Cisco Smart Install RCE). They achieve persistence by modifying router configurations, enabling traffic mirroring (SPAN/RSPAN/ERSPAN), configuring GRE/IPsec tunnels, creating accounts, and executing Tcl/Python scripts on the device.
- **Affected Products:** Cisco IOS XE (CVE-2023-20198, CVE-2023-20273), Cisco Smart Install (CVE-2018-0171), Ivanti products (CVE-2024-21887)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept exploit is specifically referenced in the advisory.
- **Patch Available:** Patches for CVE-2023-20198, CVE-2023-20273, CVE-2018-0171, and CVE-2024-21887 have been released by the affected vendors. See the CISA advisory for links to the vendor advisories.
- **Active Exploitation:** Yes, active exploitation of CVE-2023-20198, CVE-2023-20273, CVE-2018-0171, and CVE-2024-21887 has been reported.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching of known exploited CVEs; disable unused ports/protocols; require public‑key authentication; change default credentials; use vendor‑recommended OS versions; monitor firmware and software integrity; review logs for signs such as creation of PCAPs, SPAN sessions, or log clearing.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** The campaign exploits Outlook NTLM (CVE-2023-23397) to harvest hashes, leverages WinRAR (CVE-2023-38831) and Roundcube Webmail vulnerabilities for code execution or credential theft, and uses tools like Impacket, PsExec, and RDP for lateral movement and data exfiltration.
- **Affected Products:** WinRAR (CVE-2023-38831), Roundcube Webmail (CVE-2020-12641, CVE-2020-35730, CVE-2021-44026), Microsoft Outlook (CVE-2023-23397) and various SOHO devices (see advisory for full list).
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploited in the wild; no public proof‑of‑concept links provided.
- **Patch Available:** Vendor-specific patches are available; see the CISA advisory for details.
- **Active Exploitation:** Confirmed active exploitation in the wild by GRU unit 26165 (APT28/Fancy Bear).
- **Threat Actors:** GRU unit 26165 (APT28 / Fancy Bear / Forest Blizzard / Blue Delta).
- **Mitigation:** Apply all vendor security patches and firmware updates, implement network segmentation/Zero Trust, enable EDR, block external NTLM/SMB traffic, harden IP cameras (disable remote access/UPnP, enable MFA), and conduct continuous monitoring and threat hunting as outlined by CISA.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — LiteSpeed cPanel Plugin CVE-2026-48172 Exploited to Run Scripts as Root

**CVE:** `CVE-2026-48172` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-23
**Reference:** <https://thehackernews.com/2026/05/litespeed-cpanel-plugin-cve-2026-48172.html>

> A maximum-severity security vulnerability impacting LiteSpeed User-End cPanel Plugin has come under active exploitation in the wild.

The flaw, tracked as CVE-2026-48172 (CVSS score: 10.0), relates to an instance of incorrect privilege assignment that an attacker could abuse to run arbitrary scripts with elevated permissions.

&quot;Any cPanel user (including an attacker or a compromised account) …

**Parallel AI Enrichment:**

- **Technical Details:** Incorrect privilege assignment in the lsws.redisAble function (related to Redis enable/disable handling) allows any cPanel user (including an attacker or compromised account) to execute arbitrary scripts with root privileges.
- **Affected Products:** LiteSpeed User-End cPanel Plugin versions 2.3 through 2.4.4 (fixed in 2.4.5; additional fixes in cPanel plugin v2.4.7 / WHM plugin v5.3.1.0)
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H
- **Exploit Available:** Active exploitation in the wild reported; no public PoC or weaponized exploit URL confirmed.
- **Patch Available:** Yes — LiteSpeed released fixes (cPanel plugin v2.4.5 and later; recommend upgrade to v2.4.7 bundled with WHM plugin v5.3.1.0).
- **Active Exploitation:** Confirmed active exploitation reported by LiteSpeed and multiple security sources (The Hacker News, NVD/INCIBE advisories).
- **Threat Actors:** None known
- **Mitigation:** Immediate upgrade to patched plugin versions; if unable to patch, remove/uninstall the user-end cPanel plugin (/usr/local/lsws/admin/misc/lscmctl cpanelplugin --uninstall). Detection IOCs: grep -rE "cpanel_jsonapi_func=redisAble" /var/cpanel/logs /usr/local/cpanel/logs/ 2>/dev/null and review/block suspicious IPs.
- **Vendor Advisory:** https://blog.litespeedtech.com/2026/05/21/security-update-for-litespeed-cpanel-plugin/

---

## 11. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
