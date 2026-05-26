# Zero Day Pulse

> **Generated:** 2026-05-26 19:54 UTC &nbsp;|&nbsp; **Total:** 20 &nbsp;|&nbsp; 🔴 KEV: 1 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 5 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🔴 CISA KEV — CVE-2026-48172 — LiteSpeed cPanel Plugin Privilege Escalation Vulnerability

**CVE:** `CVE-2026-48172` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-48172>

> Vendor: LiteSpeed | Product: cPanel Plugin. LiteSpeed cPanel Plugin contains privilege escalation vulnerability that is exposed via the user-end cPanel plugin, which can be abused by any cPanel user account to execute arbitrary scripts with root privileges. Required action: Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability arises from improper validation of the `lsws.redisAble` (or `cpanel_jsonapi_func=redisAble`) function, which can be invoked by any cPanel user to execute arbitrary shell commands as the root user, leading to full privilege escalation.
- **Affected Products:** LiteSpeed User-End cPanel Plugin versions 2.3 – 2.4.4
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (https://blog.litespeedtech.com/2026/05/21/security-update-for-litespeed-cpanel-plugin/)
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Upgrade the LiteSpeed User‑End cPanel Plugin to version 2.4.7 or later (bundled with WHM Plugin 5.3.1.0). If immediate patching is not possible, uninstall the user‑end plugin with `/usr/local/lsws/admin/misc/lscmctl cpanelplugin --uninstall`. Additionally, scan logs with `grep -rE "cpanel_jsonapi_func=redisAble" /var/cpanel/logs /usr/local/cpanel/logs/ 2>/dev/null` and block any suspicious IPs.
- **Vendor Advisory:** https://blog.litespeedtech.com/2026/05/21/security-update-for-litespeed-cpanel-plugin/

---

## 2. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Path traversal vulnerabilities in SimpleHelp 5.5.7 and earlier allow unauthenticated remote attackers to retrieve logs, configuration files, and credentials, and potentially log in with high privileges.
- **Affected Products:** SimpleHelp remote support / RMM versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** DragonForce
- **Mitigation:** Apply vendor patch/update to SimpleHelp 5.5.8 immediately; if unable to patch, isolate SimpleHelp servers from public internet, restrict access via firewall/VPN, rotate credentials stored in SimpleHelp, and audit logs for suspicious access.
- **Vendor Advisory:** https://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570

---

## 3. 🟠 Zero-Day — Hackers Exploited KnowledgeDeliver Zero-Day for Web Shell Deployment

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://www.securityweek.com/hackers-exploited-knowledgedeliver-zero-day-for-web-shell-deployment/>

> Hardcoded machineKey values in a configuration file enabled ViewState deserialization attacks leading to remote code execution. The post Hackers Exploited KnowledgeDeliver Zero-Day for Web Shell Deployment appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** Hardcoded identical ASP.NET machineKey values in KnowledgeDeliver web.config allowed attackers who obtained the key to craft malicious ViewState (__VIEWSTATE) payloads that deserialize on the server, enabling unauthenticated remote code execution and in‑memory web shell deployment.
- **Affected Products:** KnowledgeDeliver (all deployments before 2026-02-24)
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Rotate machineKey for each instance, restrict LMS access to known IP ranges, monitor IIS and application logs, hunt for indicators (Event ID 1316, suspicious w3wp.exe activity, file tampering, anomalous User-Agent strings).
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — Iranian Hackers Deploy MiniFast and MiniJunk V2 via Phishing and SEO Poisoning

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://thehackernews.com/2026/05/iranian-hackers-deploy-minifast-and.html>

> The Iranian state-sponsored threat actor known as Nimbus Manticore (aka Screening Serpens and UNC1549) has been attributed to a fresh campaign using lures impersonating organizations in the aviation and software sectors across the U.S., Europe, and the Middle East following the joint U.S.-Israeli military campaign against the country in late February 2026.

The activity, besides embracing

**Parallel AI Enrichment:**

- **Technical Details:** The campaign uses SEO‑poisoned search results to lure victims to a fake Oracle SQL Developer download page. The installer drops the MiniFast backdoor, which communicates over HTTP for tasking, file exfiltration, and additional payload download. MiniFast supports file operations, process enumeration, command execution via cmd.exe, DLL loading, ZIP creation, scheduled‑task persistence, and privilege escalation via runas. MiniJunk V2 is used for initial payload delivery through AppDomain hijacking.
- **Affected Products:** Oracle SQL Developer
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Nimbus Manticore (also known as Screening Serpens and UNC1549)
- **Mitigation:** Validate software downloads by using official vendor sites; block or monitor traffic to known malicious domains; employ endpoint detection and response solutions; disable execution of unsigned installers; regularly audit scheduled tasks and running processes for suspicious activity.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an attack where adversaries place maliciously crafted content on web pages or other data sources that AI agents consume, causing the agent to follow attacker‑controlled instructions or disclose sensitive data. The attack chain requires injecting adversarial prompts into contexts consumed by models (e.g., web text, code contexts).
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Hardening includes continuous monitoring for IPI payloads, input sanitization/validation, context filtering, content provenance and sourcing controls, model instruction‑following constraints, and vendor mitigations described by Google; refer to the vendor advisory for details.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is a class of attacks where adversaries embed malicious instructions in data or tools consumed indirectly by an LLM (e.g., content in Workspace apps or web data), causing the model or agentic workflows to follow those instructions. Attack surface includes multi-source data, tool chaining, and agent automation.
- **Affected Products:** Google Workspace with Gemini (e.g., Gmail, Docs); specific versions unavailable
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** false
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Defense-in-depth continuous approach: human and automated red‑teaming; Google AI VRP; vulnerability cataloging and synthetic data generation; deterministic defenses (user confirmation, URL sanitization, tool‑chaining policies governed by a centralized Policy Engine); ML‑based defenses retrained on synthetic variants; LLM model hardening to ignore embedded harmful instructions; monitoring of public disclosures and rapid config "point fixes" (e.g., regex takedowns).
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection occurs when untrusted web content (malicious pages, iframes, user‑generated content) crafts inputs that influence an agent/planner model to perform unwanted actions (e.g., financial transactions, data exfiltration). Chrome limits model exposure via origin gating, uses an isolated alignment critic to vet actions, runs a parallel prompt‑injection classifier, and requires user confirmations for impactful actions.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — https://blog.google/security/architecting-security-for-agentic/
- **Active Exploitation:** false
- **Threat Actors:** None known.
- **Mitigation:** Layered defenses described by Google: User Alignment Critic (isolated vetting model), Origin Sets (readable vs read‑writeable origin gating), deterministic checks on model‑generated URLs, user confirmations for sensitive actions, prompt‑injection classifier running in parallel, Safe Browsing integration, red‑teaming and VRP updates.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Race condition in the Rust implementation of the Android Binder IPC subsystem caused by an unsafe block that corrupts the prev and next pointers of a linked list, potentially leading to kernel panic or system crash (DoS).
- **Affected Products:** Linux kernel 6.18 and later with CONFIG_ANDROID_BINDER_IPC_RUST=y; some Android kernels with 6.12.x backports
- **CVSS Score:** 4.6
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the official kernel patches; restrict local access to the Binder driver; monitor system logs for rust_binder crashes; review and disable the CONFIG_ANDROID_BINDER_IPC_RUST kernel configuration if not required.
- **Vendor Advisory:** https://ubuntu.com/security/CVE-2025-68260

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection occurs when hidden malicious instructions in external data sources (emails, documents, calendar invites, or embedded URLs/images) cause a generative‑AI assistant to perform unintended actions or exfiltrate data. The attack leverages the model’s ability to follow natural‑language instructions embedded in content it processes, allowing an adversary to trigger malicious behavior without directly interacting with the model.
- **Affected Products:** Gemini 2.5, Gemini (Google Workspace)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses — model hardening/adversarial training, content classifiers, markdown sanitization (no external image rendering), suspicious URL detection/redaction (Safe Browsing), contextual user confirmation for risky actions, end‑user security notifications, and follow Google help center guidance. Monitor vendor advisories and apply recommended configuration changes.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored APTs compromise internet-exposed network-edge devices (routers, provider edge/customer edge) by exploiting publicly known CVEs and weak/default credentials, gaining administrative access to modify configurations (ACLs, routes, open ports), enable traffic mirroring or tunneling, run virtual containers or scripts on-device for persistence and lateral movement, and exfiltrate or redirect traffic.
- **Affected Products:** Cisco IOS XE, Cisco IOS, Ivanti Connect Secure, Ivanti Policy, Fortinet firewalls, Juniper firewalls, Nokia routers and switches, Sierra Wireless devices, SonicWall firewalls
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Prioritize patching known exploited CVEs; monitor router configs/logs for unexpected ACLs, GRE/IPsec tunnels, SPAN/RSPAN/ERSPAN, unexpected virtual containers; disable unused services/protocols; change default credentials; enforce PKI/public-key auth for admin access; perform firmware image/hash integrity checks and inventory; apply Cisco-specific Guest Shell hardening as recommended
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 12. 🟠 Zero-Day — XWiki Platform vulnerable to potential arbitrary file writing using path traversal from (subwiki) admin

**CVE:** `CVE-2026-48047` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-vgwr-23fq-pr7g>

> ### Impact
A potential path traversal vulnerability allow an attacker who manages to get a malicious WebJar extension installed on the wiki to write arbitrary files. While the consequences could be severe like overriding configuration files and setting the superadmin password, the attack first requires that the attacker already has admin access to at least a subwiki to be able to install a malicio…

---

## 13. 🟠 Zero-Day — CISA orders feds to patch actively exploited Drupal vulnerability

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-drupal-vulnerability/>

> CISA has given U.S. government agencies until Wednesday evening to secure their servers against an SQL injection vulnerability in the Drupal content management system (CMS) that it flagged as actively exploited. [...]

---

## 14. 🟠 Zero-Day — KnowledgeDeliver LMS Flaw Exploited to Deploy Godzilla and Cobalt Strike

**CVE:** `CVE-2026-5426` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://thehackernews.com/2026/05/knowledgedeliver-lms-flaw-exploited-to.html>

> A now-patched high-severity security flaw affecting Digital Knowledge KnowledgeDeliver, a Learning Management System (LMS) popular in Japan, was exploited as a zero-day to deliver the Godzilla web shell and ultimately facilitate the deployment of Cobalt Strike Beacon.

The vulnerability, tracked as CVE-2026-5426 (CVSS score: 7.5), stems from the use of hard-coded ASP.NET machine keys, leading to

---

## 15. 🟠 Zero-Day — [SECURITY ADVISORY] CVE-2026-34474 - ZTE H298A/H108N Unauthenticated Admin Credential Exposure

**CVE:** `CVE-2026-34474` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://seclists.org/fulldisclosure/2026/May/20>

> Posted by m.nageh on May 25 -----BEGIN SECURITY ADVISORY----- Advisory ID: MONX-2026-003 CVE ID: CVE-2026-34474 Title: ZTE ZXHN H298A / H108N - Unauthenticated Admin Password &amp; WLAN Credential Exposure Affected: ZTE ZXHN H298A 1.1, ZTE ZXHN H108N 2.6 (EOL; no patch planned) Date: 2026-05-20 Author: Mina Nageh Salalma (Monx Research) Contact: minanageh379 () gmail com Public URL:...

---

## 16. 🟡 High Severity — Typebot has Stored XSS via Rating Block Custom Icon that Bypasses isUnsafe Sandbox in Builder Preview

**CVE:** `CVE-2026-28445` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-6m7c-xfhp-p9fh>

> ## Summary
The rating block&#x27;s custom icon feature accepts arbitrary HTML/SVG via the `customIcon.svg` field and renders it using Solid&#x27;s `innerHTML` directive without any sanitization. When a malicious typebot is imported or crafted by a workspace collaborator, the payload executes in the builder&#x27;s DOM context (builder.typebot.io), bypassing the `isUnsafe` Web Worker sandbox that pr…

---

## 17. 🟡 High Severity — Reconciling the Past: Correcting Records for Unfixed Kubernetes CVEs

**CVE:** `CVE-2020-8561` | `CVE-2020-8562` | `CVE-2021-25740` | `CVE-2020-8554` &nbsp;|&nbsp; **Source:** Kubernetes Security Announcements &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://kubernetes.io/blog/2026/05/26/reconciling-unfixed-kubernetes-cves/>

> The Kubernetes project relies on transparency to empower cluster administrators and security researchers. One important way we do that is by publishing CVE records into the Common Vulnerabilities and Exposures database. As part of our ongoing effort to mature the official Kubernetes CVE Feed , we have identified some discrepancies. CVE records for a few older, unfixed issues incorrectly include a …

---

## 18. 🟡 High Severity — Weblate has a Server-Side Request Forgery issue

**CVE:** `CVE-2025-66407` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://github.com/advisories/GHSA-hfpv-mc5v-p9mm>

> ### Impact
The Create Component functionality in Weblate allows authorized users to add new translation components by specifying both a version control system and a source code repository URL to pull from. However, the repository URL field is not validated or sanitized, allowing an attacker to supply arbitrary protocols, hostnames, and IP addresses, including localhost, internal network addresses,…

---

## 19. 🟡 High Severity — Microsoft Patches SharePoint RCE Flaw CVE-2026-45659 Across Server Versions

**CVE:** `CVE-2026-45659` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-05-26
**Reference:** <https://thehackernews.com/2026/05/microsoft-patches-sharepoint-rce-flaw.html>

> Microsoft has rolled out updates to fix a remote code execution vulnerability impacting SharePoint that could be exploited by bad actors in attacks without requiring any specialized conditions to be met.

The vulnerability, tracked as CVE-2026-45659, carries a CVSS score of 8.8. It has been assigned an important severity.

&quot;Deserialization of untrusted data in Microsoft Office SharePoint allo…

---

## 20. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
