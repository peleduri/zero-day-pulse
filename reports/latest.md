# Zero Day Pulse

> **Generated:** 2026-06-04 09:43 UTC &nbsp;|&nbsp; **Total:** 26 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 12 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE‑2024‑57727 is a directory traversal vulnerability in SimpleHelp RMM (≤ 5.5.7) that allows unauthenticated attackers to read arbitrary files on the target system, enabling retrieval of logs, configuration data, and credentials.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (https://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570)
- **Active Exploitation:** true
- **Threat Actors:** DragonForce ransomware
- **Mitigation:** Upgrade SimpleHelp to version 5.5.8 or later. Apply network segmentation or firewall rules to restrict external access to the RMM service until the patch is applied.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — CISA Adds Exploited Magento RCE Flaw CVE-2026-45247 to KEV Catalog

**CVE:** `CVE-2026-45247` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://thehackernews.com/2026/06/cisa-adds-exploited-magento-rce-flaw.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Wednesday added a critical flaw impacting Mirasvit Cache Warmer, a popular Magento full-page cache extension, to its Known Exploited Vulnerabilities (KEV) catalog, following reports of active exploitation in the wild.

The vulnerability, tracked as CVE-2026-45247 (CVSS score: 9.8), is a case of deserialization of untrusted

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated PHP object injection (CWE-502) via the CacheWarmer cookie. The extension unserializes attacker‑controlled cookie data, and crafted serialized objects combined with Magento gadget chains lead to remote code execution.
- **Affected Products:** Mirasvit Full Page Cache Warmer for Magento 2 versions before 1.11.12
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Update to version 1.11.12 or later. Additionally, block or monitor HTTP requests with CacheWarmer cookies containing base64‑encoded serialized objects (patterns Tz|Qz|YT) and apply WAF rules to drop such requests.
- **Vendor Advisory:** https://mirasvit.com/package/changelog/?package=mirasvit/module-cache-warmer

---

## 3. 🟠 Zero-Day — The sorry state of skill distribution

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Trail of Bits Blog &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://blog.trailofbits.com/2026/06/03/the-sorry-state-of-skill-distribution/>

> Public skill marketplaces are being flooded with malicious skills that steal credentials, exfiltrate data, and hijack agents. In response, a segment of the security industry released skill scanners, a new family of tools designed to detect malicious skills before they’re installed. But we tested them, and they don’t work. We recently bypassed ClawHub’s malicious skill detector , Cisco’s agent skil…

**Parallel AI Enrichment:**

- **Technical Details:** Trail of Bits demonstrated four bypasses against public skill scanners: (1) large newline padding to bypass OpenClaw/ClawHub truncation and VirusTotal/Code Insight confusion; (2) use of .docx (ZIP) containing embedded script to hide malicious instructions referenced by SKILL.md; (3) Python bytecode (.pyc) poisoning where precompiled bytecode contains malicious behavior not visible in source; (4) prompt‑injection framed as benign configuration (e.g., changing npm/yarn registries). Scanners missed these due to truncated context, ignoring opaque file types, limited file‑scope analysis, and susceptibility of LLM‑based analyzers to crafted natural‑language explanations.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Do not trust public skill marketplaces for sensitive agents; curate internal skill repositories, whitelist sources, restrict allowable file types, perform exhaustive repository traversal and inspect binaries/compiled artifacts, use strict format validation (agentskills.io spec), pin and vet dependencies, require human review for skills that include binaries, archives, or external registry configuration. Cisco submitted PRs to harden skill‑scanner (strict format validation and expanded language support) but these are partial mitigations.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Prompt injection manipulates Large Language Models by embedding crafted instructions within user input or external content, causing the model to follow attacker‑supplied commands. Indirect prompt injection seeds malicious prompts on websites or other data sources that AI systems process, allowing the attacker to corrupt the model's behavior. The “Comment and Control” variant weaponizes comments in code or documentation to achieve the same effect.
- **Affected Products:** Microsoft Copilot Studio (CVE-2026-21520), MS‑Agent (CVE-2026-2256), EmailGPT (CVE-2024-5184), Claude Code, Gemini CLI, GitHub Copilot
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Treat the LLM as untrusted; implement robust input and output validation and sanitization; add human oversight and controls in LLM workflows; harden system prompts; limit exposure of sensitive data to the model; monitor and block known malicious prompt patterns.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when attacker‑controlled content embedded in data sources or tools used by an LLM contains malicious instructions that the model ingests and follows while fulfilling a user query (no explicit user prompt needed). Attack surface includes integrated connectors, web content, files, and third‑party tools; mitigations focus on provenance, policy‑based instruction sanitization, and reducing agentic automation surface area.
- **Affected Products:** Google Workspace (including Gemini integrations)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true - https://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads
- **Patch Available:** false - http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html
- **Active Exploitation:** true - https://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads, http://infosecurity-magazine.com/news/researchers-10-wild-indirect
- **Threat Actors:** None known
- **Mitigation:** Google recommends layered defenses including input provenance and filtering, strict tool/data vetting, runtime instruction filtering, safe defaults and least‑privilege for agentic actions, continuous red‑team testing and telemetry/monitoring.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection: malicious web content can influence agentic browser prompts/actions by injecting or manipulating prompts delivered to the agent; mitigations include layered defenses restricting origin access, blocking indirect prompt injections, and limiting unsafe AI actions.
- **Affected Products:** Chrome (agentic/Gemini features)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use Chrome’s layered defenses: restrict origin access, block indirect prompt injections, limit agent actions to trusted UI flows, and apply vendor updates.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Rust’s ownership/borrow‑checker model eliminates many memory‑safety bugs (e.g., use‑after‑free, buffer overflows) by enforcing compile‑time safety guarantees, which the blog cites as the reason for a 1000× reduction in memory‑safety vulnerability density in Android.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use Rust and memory‑safety practices in Android; continue migrating risky components to memory‑safe languages.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injections hide malicious instructions in external data sources such as emails, documents, or calendar invites that LLM‑based assistants may read and act upon. Google counters this by adding model‑level resilience, content classifiers that detect malicious instructions, sanitization/redaction of suspicious URLs and external content, and requiring user confirmation before performing risky actions.
- **Affected Products:** Gemini
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Model hardening (Gemini 2.5), prompt injection content classifiers, security thought reinforcement, markdown sanitization and suspicious URL redaction, user confirmation framework, end‑user security mitigation notifications, adversarial training, red‑team testing, and collaborations with industry partners.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Chinese state‑sponsored actors compromise backbone, provider edge (PE), and customer edge (CE) routers and leverage compromised devices and trusted connections to pivot. Actors modify routers to maintain persistent, long‑term access and use these access points for global espionage operations.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Implement CISA and NSA hardening guidance: detect and disrupt persistent router compromises, apply network segmentation, audit trusted connections, monitor for unusual configurations and persistence mechanisms, rotate credentials, restrict administrative access, and deploy vendor-provided updates where available.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Russian GRU (85th Main Special Service Center, Military Unit 26165)
- **Mitigation:** Mitigation steps unavailable.
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

## 15. 🟡 High Severity — browserstack-runner vulnerable to Remote Code Execution via vm sandbox escape in _log HTTP handler

**CVE:** `CVE-2026-49143` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-6vr3-7wcx-v5g5>

> ### Summary

The HTTP handler `/_log` in `lib/server.js` (lines 491–515) of browserstack-runner passes unauthenticated user-supplied data to `vm.runInNewContext()` combined with `eval()`, enabling a sandbox escape and arbitrary code execution on the host system.

### Details

When `browserstack-runner` starts, it creates an HTTP server on port 8888 (configurable) that listens on all network interf…

---

## 16. 🟡 High Severity — Jupyter Enterprise Gateway: Kubernetes Manifest Injection in Jinja2 Template Rendering

**CVE:** `CVE-2026-44182` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-cfw7-6c5v-2wjq>

> ### Summary

The environment variables used during the rendering of the Kubernetes manifest allow YAML injection, enabling attackers to overwrite existing keys like `securityContext` and inject multi-document YAML to create additional unintended Kubernetes resources.

### Details

The server interpolates untrusted environment variables (e.g., `KERNEL_XXX`) into Kubernetes manifests without YAML-aw…

---

## 17. 🟡 High Severity — Jupyter Enterprise Gateway: Jinja2 Template Server Side Template Injection resulting in Remote Code Execution

**CVE:** `CVE-2026-44181` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-f49j-v924-fx9w>

> ### Summary

The environment variables (`KERNEL_XXX`) used during the rendering of the Kubernetes manifest are vulnerable to Server Side Template Injection (SSTI).
By including Jinja2 template expressions it is possible to execution Python code and OS Commands in the Enterprise Gateway service.
The code can use or steal the Kubernetes service account token, which can steal Kubernetes secrets and b…

---

## 18. 🟡 High Severity — Jupyter Enterprise Gateway: ContainerProcessProxy._enforce_prohibited_ids Bypass

**CVE:** `CVE-2026-44180` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-chq7-94j8-cj28>

> ### Summary

Jupyter Enterprise Gateway has a prohibited UID and GID feature that by default prevents launching kernels with UID or GID 0 (root).
This can be bypassed. It is possible to launch kernels with a prohibited UID and/or GID by using a specially crafted `KERNEL_UID` or `KERNEL_GID` value.

The feature is described in the documentation: 

https://github.com/jupyter-server/enterprise_gatewa…

---

## 19. 🟡 High Severity — Docling Core: Unsafe remote filename resolution

**CVE:** `CVE-2026-44023` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-jmmv-h3mp-59v8>

> ### Impact
In versions `&gt;= 1.5.0, &lt; 2.74.1`, `docling-core` did not sufficiently restrict remote request destinations and could resolve a server-provided `Content-Disposition` to a local path in an unsafe manner.

In applications that accept untrusted URLs, this could allow SSRF attacks targeting local files outside the user-defined cache directory.

### Patches
Patched in `docling-core` `2.…

---

## 20. 🟡 High Severity — Docling: Unsafe URI and Path Handling in HTML Backend

**CVE:** `CVE-2026-47214` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-q29v-xc37-wh5m>

> ### Impact
The HTML backend did not perform sufficient validation during resource handling:
- Accepted `file://` URIs enabling local file system access when `enable_local_fetch=True`
- Path resolution allowed traversal outside intended directories via `../` sequences and absolute paths
- Did not block internal network resources under `enable_remote_fetch=True`
- HTTP redirects were not validated, …

---

## 21. 🟡 High Severity — Docling: Unsafe XML Entity Expansion in USPTO Patent Backend

**CVE:** `CVE-2026-44020` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-m88r-rg27-5xfg>

> ### Impact
The USPTO patent XML parser used the standard `xml.sax.parseString()` without protection against XML External Entity (XXE) attacks. An attacker could craft malicious USPTO patent XML files with external entity references that could:
- Read arbitrary files from the server filesystem
- Perform Server-Side Request Forgery (SSRF) attacks
- Cause denial of service through entity expansion (B…

---

## 22. 🟡 High Severity — Docling: Unsafe Archive Extraction and XML Parsing in METS-GBS Backend

**CVE:** `CVE-2026-44018` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-r3xg-rg9j-67fv>

> ### Impact
The METS-GBS backend&#x27;s XML parsing and the input document format detection lacked security controls, enabling:
- XML External Entity (XXE) attacks to read local files or cause denial of service
- Decompression bombs (zip bombs) to exhaust memory and disk space
- Unbounded archive extraction consuming system resources

An attacker could craft malicious METS-GBS archives that, when p…

---

## 23. 🟡 High Severity — Docling: Unsafe Playwright-based HTML Rendering

**CVE:** `CVE-2026-44016` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-pj2v-ggqh-cmq2>

> ### Impact
In versions `&gt;= 2.82.0, &lt; 2.91.0`, if the HTML backend was explicitly configured for rendering (rendering option by default deactivated), then the Playwright-based rendering feature could allow JavaScript execution and unrestricted network access when processing untrusted HTML documents. An attacker could craft malicious HTML that executes arbitrary JavaScript in the rendering con…

---

## 24. 🟡 High Severity — backpack/crud is vulnerable to Cross-Site Scripting (XSS)

**CVE:** `CVE-2022-31114` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-m8xx-3x29-84h8>

> ### Impact

It’s a “*moderate*” vulnerability… but being an admin panel, take this seriously. It’s difficult… but an attacker could conduct a targeted phishing campaign, in order to **trick your users or admins to click a malicious link, which under very specific circumstances could give them information... or even admin access**. It’s *unlikely*, but that’s not good enough in admin panels - It sh…

---

## 25. 🟡 High Severity — Docling: Unsafe Zip Extraction in EasyOCR Model Download

**CVE:** `CVE-2026-44017` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-cjqg-rq2h-2fvj>

> ### Impact
In versions `&lt; 2.91.0`, The EasyOCR model download functionality extracted ZIP archives without validating member paths, enabling Zip Slip attacks. If an attacker could compromise the model download source (via supply chain attack, DNS spoofing, or MITM), they could write arbitrary files to any location writable by the process, potentially achieving:
- Remote code execution by overwr…

---

## 26. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
