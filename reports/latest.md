# Zero Day Pulse

> **Generated:** 2026-06-04 02:33 UTC &nbsp;|&nbsp; **Total:** 26 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 12 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path traversal vulnerability in SimpleHelp v5.5.7 and earlier that lets unauthenticated remote attackers read arbitrary files (such as logs, configuration files, and credentials) by sending crafted requests that traverse directories.
- **Affected Products:** SimpleHelp Remote Support / RMM versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Proof‑of‑concept and weaponized exploit techniques have been publicly documented.
- **Patch Available:** Yes – SimpleHelp 5.5.8 contains security fixes.
- **Active Exploitation:** Yes – confirmed active exploitation reported by CISA.
- **Threat Actors:** Ransomware actors (unnamed)
- **Mitigation:** Apply the SimpleHelp 5.5.8 patch or upgrade to a later version; isolate/unexpose SimpleHelp instances from the public internet; rotate credentials stored on affected servers; review logs and implement network segmentation; if patch cannot be applied immediately, take servers offline or block access to SimpleHelp management ports from untrusted networks.
- **Vendor Advisory:** https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — The sorry state of skill distribution

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Trail of Bits Blog &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://blog.trailofbits.com/2026/06/03/the-sorry-state-of-skill-distribution/>

> Public skill marketplaces are being flooded with malicious skills that steal credentials, exfiltrate data, and hijack agents. In response, a segment of the security industry released skill scanners, a new family of tools designed to detect malicious skills before they’re installed. But we tested them, and they don’t work. We recently bypassed ClawHub’s malicious skill detector , Cisco’s agent skil…

**Parallel AI Enrichment:**

- **Technical Details:** Bypass 1: large newline truncation causes the scanner to drop malicious content. Bypass 2: .pyc bytecode poisoning embeds malicious logic that scanners miss. Bypass 3: prompt injection tricks the agent into executing attacker‑controlled commands.
- **Affected Products:** ClawHub (OpenClaw), Cisco agent skill scanner, skills.sh scanners
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC available in the Trail of Bits repository: https://github.com/trailofbits/overtly-malicious-skills
- **Patch Available:** Patch unavailable.
- **Active Exploitation:** No confirmed active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Avoid treating public skill marketplaces as trusted; curate internal skill marketplaces; pin and control skill sources; treat public skills as untrusted; implement strict format validation for skills.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is a class of prompt‑injection attacks where malicious instructions are embedded in web content or other data sources that AI agents ingest; the malicious content is designed to influence agent behavior indirectly by appearing as user content or contextual data rather than direct prompts.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC/weaponized exploit: None reported.
- **Patch Available:** Vendor patch unavailable.
- **Active Exploitation:** Yes — researchers discovered 10 IPI payloads in the wild (reported by Google Threat Intelligence, Forcepoint X-Labs, and Infosecurity).
- **Threat Actors:** None known
- **Mitigation:** Implement robust input sanitization and filtering, context-level instruction isolation, provenance validation, model output validation policies, and monitoring for known IPI payload patterns; follow vendor hardening guidance.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) – attackers inject malicious instructions into data or tools consumed by an LLM (e.g., documents, webpages, connectors, or agent tool outputs) to influence model behavior without direct user input; it especially affects complex, multi-data-source agentic workflows such as Workspace + Gemini.
- **Affected Products:** Google Workspace with Gemini
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC exploit URL known; security researchers (Forcepoint) reported captured IPI payloads but no standard weaponized exploit repository referenced.
- **Patch Available:** No single patch; Google describes continuous mitigation measures in its advisory (see vendor_advisory). If a formal patch is released it will be posted on the vendor advisory.
- **Active Exploitation:** Reports of increasing IPI attempts and payloads observed in the wild, but no widely reported confirmed mass active exploitation tied to a specific exploit disclosed in vendor advisory.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: input sanitization and filtering of external sources, strict provenance and vetting of connectors, reducing agentic automation when possible, prompt and instruction hardening, monitoring and anomaly detection, and continuous security updates as described in Google's guidance.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) is a web‑based attack where malicious or crafted web content (often not directly presented as user instructions) is surfaced to an LLM‑powered agentic browser or assistant, causing it to execute unsafe actions or disclose secrets. Google’s mitigation introduces layered defenses in Chrome for agentic browsing: origin‑restricted access, a supervisory “watcher” agent to validate actions, and runtime checks to block unsafe prompts and actions.
- **Affected Products:** Google Chrome (agentic browsing/Gemini integration)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC or weaponized exploit tied to this advisory is publicly documented (none found).
- **Patch Available:** Yes — Google announced layered defenses for agentic browsing in Chrome; advisory: http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** Reports indicate indirect prompt injection payloads have been observed in the wild (e.g., Forcepoint/OPUS reporting IPI payloads and leaked secrets from coding agents), but no public, attributable, weaponized exploit specifically against Chrome’s agentic defenses tied to this advisory has been confirmed.
- **Threat Actors:** None known
- **Mitigation:** Use latest Chrome with agentic features updated; disable agentic/browsing features where not needed; restrict web-origin access for agents; apply principle of least privilege for agent capabilities; monitor vendor advisories for updates.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Android Framework on Android 14‑16
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit not publicly available (no PoC reported).
- **Patch Available:** Yes – patches released in the June 2026 Android Security Bulletin (security patch level 2026-06-05).
- **Active Exploitation:** Confirmed active targeted exploitation reported by Google and several security outlets (Anavem, Daily Security Review, BleepingComputer).
- **Threat Actors:** None known
- **Mitigation:** Apply the June 2026 Android security patches (security patch level 2026‑06‑05) from the device OEM or Google. Until patched, follow vendor hardening guidance and avoid installing untrusted apps.
- **Vendor Advisory:** https://source.android.com/security/bulletin/2026-06-01

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) embeds malicious instructions in external data sources (emails, documents, calendar invites) so an LLM acting on that content can be coerced to exfiltrate data or perform rogue actions. Google mitigations include model hardening (Gemini 2.5), prompt‑injection content classifiers, security “thought reinforcement”, markdown sanitization, suspicious‑URL redaction, a user‑confirmation (HITL) framework, and end‑user security notifications.
- **Affected Products:** Gemini (Gemini app and Gemini in Google Workspace)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC or weaponized exploit published in the advisory; none reported.
- **Patch Available:** Google has rolled out and is rolling out mitigations integrated into Gemini (model hardening and platform defenses). Advisory URL: http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html
- **Active Exploitation:** Advisory does not report confirmed active exploitation; no known active exploitation.
- **Threat Actors:** None known
- **Mitigation:** Use Google’s layered defenses (content classifiers, security thought reinforcement, markdown sanitization, suspicious‑URL redaction, user confirmation/HITL, end‑user notifications); follow Google Help Center guidance (https://support.google.com/docs/answer/16204578) and apply secure AI agent best practices and adversarial testing.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors target large backbone, provider edge (PE) and customer edge (CE) routers, leverage compromised devices and trusted connections to pivot into other networks, and modify routers to maintain persistent, long‑term access.
- **Affected Products:** Telecommunications backbone routers, provider edge (PE) routers, customer edge (CE) routers, and other compromised network devices
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC/weaponized exploit; none publicly reported in advisory
- **Patch Available:** No single vendor patch; advisory provides mitigation guidance (https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a)
- **Active Exploitation:** Yes – advisory reports these PRC actors are compromising networks globally and maintaining persistent access across telecommunications, government, transportation, lodging, and military infrastructure networks.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Implement recommended mitigations from advisory — harden routers (restrict administrative access, rotate credentials, apply secure configurations), monitor for indicators of compromise, segment networks, limit trusted connections, validate device integrity, and perform forensics on suspected compromises.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Campaign-level TTPs include spearphishing, credential compromise, lateral movement, use of web shells and malware for espionage and disruption targeting logistics/transportation and IT companies involved with coordination/delivery of assistance to Ukraine.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** None known — no public PoC or weaponized exploit for a specific CVE is listed in the advisory.
- **Patch Available:** Not applicable — this is a threat actor campaign advisory, not a single software vulnerability; no vendor patch referenced.
- **Active Exploitation:** Yes — advisory documents ongoing targeting/active operations against Western logistics entities and technology companies since 2022. Reporting sources: CISA AA25-141A, FBI CSA, NSA advisory.
- **Threat Actors:** Russian GRU 85th Main Special Service Center (85th GTsSS), military unit 26165 (APT28)
- **Mitigation:** Apply CISA/NSA recommended mitigations: enforce MFA, patch systems, network segmentation, least‑privilege access, endpoint detection & response, logging/monitoring, block known malicious IPs/domains, investigate anomalous access, credential hygiene and rotate credentials.
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
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Not applicable
- **Patch Available:** Patch not applicable.
- **Active Exploitation:** Not applicable
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟠 Zero-Day — Acer working to patch max severity zero-days in Wave 7 routers

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://www.bleepingcomputer.com/news/security/acer-warns-of-max-severity-zero-days-affecting-wave-7-routers/>

> Acer is working to address two maximum-severity zero-day vulnerabilities affecting its Wave 7 mesh routers. [...]

---

## 12. 🟠 Zero-Day — Unpatched Windows Search URI Vulnerability Lets Attackers Steal NTLMv2 Hashes

**CVE:** `CVE-2026-33829` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://thehackernews.com/2026/06/unpatched-windows-search-uri.html>

> Cybersecurity researchers have disclosed details of an unpatched issue that could be exploited to disclose a user&#x27;s NTLMv2 hash to the attacker.

Like in the case of CVE-2026-33829, which impacted the Windows Snipping Tool&#x27;s ms-screensketch: URI handler, the newly flagged issue resides in the search: URI handler, per Huntress.

CVE-2026-33829 refers to a spoofing vulnerability that could…

---

## 13. 🟠 Zero-Day — Microsoft Tries to Calm Legal Threat Fears After Zero-Day Disclosure Backlash

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://www.securityweek.com/microsoft-tries-to-calm-legal-threat-fears-after-zero-day-disclosure-backlash/>

> Microsoft responds to backlash over its threats of legal action against researchers who publicly disclose zero-day vulnerabilities. The post Microsoft Tries to Calm Legal Threat Fears After Zero-Day Disclosure Backlash appeared first on SecurityWeek .

---

## 14. 🟠 Zero-Day — VS Code zero-day lets hackers steal GitHub tokens in one click

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-03
**Reference:** <https://www.bleepingcomputer.com/news/security/vs-code-zero-day-lets-hackers-steal-github-tokens-in-one-click/>

> A security researcher has released exploit code for a Visual Studio Code (VS Code) zero-day vulnerability that allows attackers to steal GitHub authentication tokens by tricking users into clicking a link. [...]

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
