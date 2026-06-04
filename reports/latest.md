# Zero Day Pulse

> **Generated:** 2026-06-04 14:33 UTC &nbsp;|&nbsp; **Total:** 24 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 14 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a directory/path traversal vulnerability in SimpleHelp's web component that lets unauthenticated attackers read arbitrary files (e.g., logs, configuration, credentials) by crafting requests that traverse the filesystem.
- **Affected Products:** SimpleHelp remote support/RMM v5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true - https://www.offsec.com/blog/cve-2024-57727/
- **Patch Available:** true - https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know
- **Active Exploitation:** true - https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a
- **Threat Actors:** Ransomware actors (likely DragonForce/other ransomware operators)
- **Mitigation:** Upgrade to SimpleHelp 5.5.8 or later. If immediate patching is not possible, restrict access to the SimpleHelp web interface using network controls (IP allowlists, VPN, firewall rules), isolate RMM servers, rotate stored credentials, and monitor for suspicious activity.
- **Vendor Advisory:** https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — CISA Adds Exploited Magento RCE Flaw CVE-2026-45247 to KEV Catalog

**CVE:** `CVE-2026-45247` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://thehackernews.com/2026/06/cisa-adds-exploited-magento-rce-flaw.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Wednesday added a critical flaw impacting Mirasvit Cache Warmer, a popular Magento full-page cache extension, to its Known Exploited Vulnerabilities (KEV) catalog, following reports of active exploitation in the wild.

The vulnerability, tracked as CVE-2026-45247 (CVSS score: 9.8), is a case of deserialization of untrusted

**Parallel AI Enrichment:**

- **Technical Details:** A PHP object injection vulnerability allows unauthenticated attackers to achieve remote code execution by sending a crafted serialized PHP object in the CacheWarmer cookie, exploiting deserialization of untrusted data.
- **Affected Products:** Mirasvit Full Page Cache Warmer for Magento 2, versions prior to 1.11.12
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Update the Mirasvit Full Page Cache Warmer extension to version 1.11.12 or later.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Attackers hide malicious prompts in web pages using techniques like CSS display:none, 1‑pixel fonts, HTML comments, meta namespaces, Base64 encoding, or canvas OCR. When an LLM‑enabled agent parses the page, it treats the hidden text as a valid instruction, leading to actions such as credential theft, financial fraud, data destruction, or DoS.
- **Affected Products:** LLM‑based browser agents, code assistants (e.g., GitHub Copilot, Claude Code), AI‑powered ad review systems, AI agents with payment or navigation capabilities
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Enforce a data‑instruction boundary (treat web content as untrusted), sanitize inputs, use heuristics to detect concealed payloads, restrict agent privileges (no payment/exec/navigation without explicit human confirmation), deploy web‑scale filtering (WAF, URL blocklists), and follow OWASP LLM prompt injection mitigation recommendations.
- **Vendor Advisory:** https://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is an attack where adversaries inject malicious instructions into data sources (documents, web pages, emails, metadata) that LLMs ingest; attacks exploit AI agents’ ingestion of external content to cause unauthorized actions or data exfiltration. Google’s whitepaper describes attack techniques (hidden HTML comments, metadata spoofing, authority impersonation, system‑override tags) and an IPI kill chain involving poisoned content → agent ingestion → execution → covert exfiltration.
- **Affected Products:** Google Workspace (Gemini app; Gemini in Gmail, Docs editors, Drive, Chat)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Google’s layered defenses include prompt‑injection content classifiers, security thought reinforcement, markdown sanitization and suspicious‑URL redaction (Google Safe Browsing), user confirmation framework, end‑user security mitigation notifications, deterministic defenses (URL sanitization, tool‑chaining policies, policy engine), ML‑based and LLM‑based defenses, Gemini model hardening, plus human & automated red‑team testing, vulnerability cataloging, and automated mitigations (regex takedowns, config updates).
- **Vendor Advisory:** http://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is a class of attacks where malicious or untrusted web content (including pages, iframes, or user‑generated content) influences an agent planning model to take unwanted actions such as financial transactions or data exfiltration. In Chrome, the planner can be exposed to page content which may cause goal‑hijacking or leaking of sensitive data across origins.
- **Affected Products:** Google Chrome (agentic/Gemini agent capabilities)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Exploit availability unknown
- **Patch Available:** true — http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** Active exploitation status unknown
- **Threat Actors:** None known
- **Mitigation:** Chrome’s mitigations include a User Alignment Critic (a separate high‑trust model that vets actions), Agent Origin Sets with read‑only and read‑writable origins, deterministic user confirmations for sensitive actions, a parallel prompt‑injection classifier, real‑time Safe Browsing/on‑device AI scanning, continuous red‑team testing, and updated VRP guidance. Users should keep Chrome updated to benefit from these built‑in controls.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** The blog post discusses Google's strategy of using Rust in Android to improve memory safety, reporting that memory‑safety vulnerabilities fell below 20% of total vulnerabilities in 2025.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** Patch availability unknown
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when an AI system processes external content—such as emails, documents, calendar invites, or web pages—that contains malicious instructions. These instructions can cause the model to exfiltrate data or perform rogue actions. Google mitigates IPI using model hardening (adversarial training), dedicated content classifiers, markdown sanitization, suspicious‑URL redaction, user‑confirmation frameworks, and end‑user mitigation notifications.
- **Affected Products:** Gemini (Gemini app and Gemini in Google Workspace); other affected products unavailable
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known
- **Mitigation:** Apply Google’s layered defenses where available (use updated Gemini versions and Workspace integrations with built‑in classifiers and URL redaction), enable user confirmation/HITL for risky operations, sanitize or strip external content before feeding to AI agents, employ content filters and suspicious‑URL detection, and follow Google Help Center guidance (https://support.google.com/docs/answer/16204578).
- **Vendor Advisory:** https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** State‑sponsored actors infiltrate backbone, provider edge (PE) and customer edge (CE) routers, modify firmware or configuration to embed persistent backdoors, and leverage trusted network connections to pivot laterally across the infrastructure.
- **Affected Products:** backbone routers, provider edge (PE) routers, customer edge (CE) routers
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Implement strict network segmentation between backbone, provider edge, and customer edge segments; enforce strong, multi‑factor authentication on router management interfaces; regularly audit router configurations for unauthorized changes; apply vendor security patches promptly; monitor logs for abnormal traffic or configuration changes; disable unused services and enforce principle of least privilege.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

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
- **Active Exploitation:** true
- **Threat Actors:** GRU 85th Main Special Service Center (85th GTsSS), unit 26165 (aka APT28) and associated Russian state-sponsored actors.
- **Mitigation:** Follow CISA/US‑CERT recommended mitigations in the advisory (network segmentation, multifactor authentication, logging and monitoring, incident response readiness, apply vendor updates where available). Specific vendor mitigation steps unavailable.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — Beyond the Zero-Day: See Your Network Like an Attacker | Webinar with HD Moore

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://thehackernews.com/2026/06/beyond-zero-day-see-your-network-like.html>

> Assume the breach. Zero-days keep shipping, AI is writing exploits faster than anyone patches, and &quot;patch everything in time&quot; stopped working years ago. Stop betting the org on winning that race. You don&#x27;t control which bug lands. You control what it can reach once it does.

That is a question about the shape of your network, and most teams have the shape wrong. HD Moore, creator of…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟡 High Severity — Axios: Proxy-Authorization Credential Leak to Origin Server Across HTTP-to-HTTPS Redirect in Axios Node.js HTTP Adapter

**CVE:** `CVE-2026-44487` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-p92q-9vqr-4j8v>

> ## Summary

Axios’s Node.js HTTP adapter may forward a `Proxy-Authorization` header to a redirected origin during specific proxy-to-direct redirect flows.

This affects Node.js usage, where an initial HTTP request is sent through an authenticated HTTP proxy, redirects are followed, and the redirected URL is no longer proxied. Under affected redirect shapes, the final origin can receive the proxy c…

---

## 12. 🟡 High Severity — Axios: Proxy-Authorization header leaks to redirect target when proxy is re-evaluated to direct connection

**CVE:** `CVE-2026-44486` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-04
**Reference:** <https://github.com/advisories/GHSA-j5f8-grm9-p9fc>

> ### Summary

Axios’ Node.js HTTP adapter can leak proxy credentials to a redirect target in affected versions. When a request is sent through an authenticated proxy, Axios may add a `Proxy-Authorization` header. If Axios then follows a redirect and the redirected request is no longer sent through that proxy, the stale `Proxy-Authorization` header can remain on the redirected request and be sent to…

---

## 13. 🟡 High Severity — browserstack-runner vulnerable to Remote Code Execution via vm sandbox escape in _log HTTP handler

**CVE:** `CVE-2026-49143` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-6vr3-7wcx-v5g5>

> ### Summary

The HTTP handler `/_log` in `lib/server.js` (lines 491–515) of browserstack-runner passes unauthenticated user-supplied data to `vm.runInNewContext()` combined with `eval()`, enabling a sandbox escape and arbitrary code execution on the host system.

### Details

When `browserstack-runner` starts, it creates an HTTP server on port 8888 (configurable) that listens on all network interf…

---

## 14. 🟡 High Severity — Jupyter Enterprise Gateway: Kubernetes Manifest Injection in Jinja2 Template Rendering

**CVE:** `CVE-2026-44182` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-cfw7-6c5v-2wjq>

> ### Summary

The environment variables used during the rendering of the Kubernetes manifest allow YAML injection, enabling attackers to overwrite existing keys like `securityContext` and inject multi-document YAML to create additional unintended Kubernetes resources.

### Details

The server interpolates untrusted environment variables (e.g., `KERNEL_XXX`) into Kubernetes manifests without YAML-aw…

---

## 15. 🟡 High Severity — Jupyter Enterprise Gateway: Jinja2 Template Server Side Template Injection resulting in Remote Code Execution

**CVE:** `CVE-2026-44181` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-f49j-v924-fx9w>

> ### Summary

The environment variables (`KERNEL_XXX`) used during the rendering of the Kubernetes manifest are vulnerable to Server Side Template Injection (SSTI).
By including Jinja2 template expressions it is possible to execution Python code and OS Commands in the Enterprise Gateway service.
The code can use or steal the Kubernetes service account token, which can steal Kubernetes secrets and b…

---

## 16. 🟡 High Severity — Jupyter Enterprise Gateway: ContainerProcessProxy._enforce_prohibited_ids Bypass

**CVE:** `CVE-2026-44180` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-chq7-94j8-cj28>

> ### Summary

Jupyter Enterprise Gateway has a prohibited UID and GID feature that by default prevents launching kernels with UID or GID 0 (root).
This can be bypassed. It is possible to launch kernels with a prohibited UID and/or GID by using a specially crafted `KERNEL_UID` or `KERNEL_GID` value.

The feature is described in the documentation: 

https://github.com/jupyter-server/enterprise_gatewa…

---

## 17. 🟡 High Severity — Docling Core: Unsafe remote filename resolution

**CVE:** `CVE-2026-44023` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-jmmv-h3mp-59v8>

> ### Impact
In versions `&gt;= 1.5.0, &lt; 2.74.1`, `docling-core` did not sufficiently restrict remote request destinations and could resolve a server-provided `Content-Disposition` to a local path in an unsafe manner.

In applications that accept untrusted URLs, this could allow SSRF attacks targeting local files outside the user-defined cache directory.

### Patches
Patched in `docling-core` `2.…

---

## 18. 🟡 High Severity — Docling: Unsafe URI and Path Handling in HTML Backend

**CVE:** `CVE-2026-47214` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-q29v-xc37-wh5m>

> ### Impact
The HTML backend did not perform sufficient validation during resource handling:
- Accepted `file://` URIs enabling local file system access when `enable_local_fetch=True`
- Path resolution allowed traversal outside intended directories via `../` sequences and absolute paths
- Did not block internal network resources under `enable_remote_fetch=True`
- HTTP redirects were not validated, …

---

## 19. 🟡 High Severity — Docling: Unsafe XML Entity Expansion in USPTO Patent Backend

**CVE:** `CVE-2026-44020` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-m88r-rg27-5xfg>

> ### Impact
The USPTO patent XML parser used the standard `xml.sax.parseString()` without protection against XML External Entity (XXE) attacks. An attacker could craft malicious USPTO patent XML files with external entity references that could:
- Read arbitrary files from the server filesystem
- Perform Server-Side Request Forgery (SSRF) attacks
- Cause denial of service through entity expansion (B…

---

## 20. 🟡 High Severity — Docling: Unsafe Archive Extraction and XML Parsing in METS-GBS Backend

**CVE:** `CVE-2026-44018` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-r3xg-rg9j-67fv>

> ### Impact
The METS-GBS backend&#x27;s XML parsing and the input document format detection lacked security controls, enabling:
- XML External Entity (XXE) attacks to read local files or cause denial of service
- Decompression bombs (zip bombs) to exhaust memory and disk space
- Unbounded archive extraction consuming system resources

An attacker could craft malicious METS-GBS archives that, when p…

---

## 21. 🟡 High Severity — Docling: Unsafe Playwright-based HTML Rendering

**CVE:** `CVE-2026-44016` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-pj2v-ggqh-cmq2>

> ### Impact
In versions `&gt;= 2.82.0, &lt; 2.91.0`, if the HTML backend was explicitly configured for rendering (rendering option by default deactivated), then the Playwright-based rendering feature could allow JavaScript execution and unrestricted network access when processing untrusted HTML documents. An attacker could craft malicious HTML that executes arbitrary JavaScript in the rendering con…

---

## 22. 🟡 High Severity — backpack/crud is vulnerable to Cross-Site Scripting (XSS)

**CVE:** `CVE-2022-31114` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-m8xx-3x29-84h8>

> ### Impact

It’s a “*moderate*” vulnerability… but being an admin panel, take this seriously. It’s difficult… but an attacker could conduct a targeted phishing campaign, in order to **trick your users or admins to click a malicious link, which under very specific circumstances could give them information... or even admin access**. It’s *unlikely*, but that’s not good enough in admin panels - It sh…

---

## 23. 🟡 High Severity — Docling: Unsafe Zip Extraction in EasyOCR Model Download

**CVE:** `CVE-2026-44017` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://github.com/advisories/GHSA-cjqg-rq2h-2fvj>

> ### Impact
In versions `&lt; 2.91.0`, The EasyOCR model download functionality extracted ZIP archives without validating member paths, enabling Zip Slip attacks. If an attacker could compromise the model download source (via supply chain attack, DNS spoofing, or MITM), they could write arbitrary files to any location writable by the process, potentially achieving:
- Remote code execution by overwr…

---

## 24. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
