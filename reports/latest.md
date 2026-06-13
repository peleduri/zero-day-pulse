# Zero Day Pulse

> **Generated:** 2026-06-13 19:06 UTC &nbsp;|&nbsp; **Total:** 21 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 10 &nbsp;|&nbsp; 🟡 High: 11 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated path traversal enabling download of arbitrary files (e.g., serverconfig.xml) from the SimpleHelp server; can be chained with authenticated arbitrary file upload (CVE‑2024‑57728) to achieve remote code execution.
- **Affected Products:** SimpleHelp remote support/RMM versions 5.5.7 and earlier (also 5.4.x prior to 5.4.10; 5.3.x prior to 5.3.9)
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Public PoC Nuclei template available at https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2024/CVE-2024-57727.yaml
- **Patch Available:** SimpleHelp released patches (5.5.8, 5.4.10, 5.3.9). Patch download page: https://simple-help.com/downloads and advisory: https://simple-help.com/kb---security-vulnerabilities-01-2025
- **Active Exploitation:** Confirmed – CISA added CVE‑2024‑57727 to its KEV catalog on Feb 13 2025 and reports indicate ransomware actors have exploited unpatched SimpleHelp instances in the wild.
- **Threat Actors:** Ransomware actors (e.g., DragonForce) as reported by CISA and Sophos.
- **Mitigation:** Upgrade immediately to patched SimpleHelp versions (5.5.8, 5.4.10, 5.3.9). If patching is not possible, isolate SimpleHelp servers from the internet, stop the server process, apply vendor‑provided mitigations, and conduct threat‑hunting per CISA guidance. Use detection queries (e.g., /allversions) and network monitoring.
- **Vendor Advisory:** https://simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an AI agent ingests poisoned content (web pages, docs, emails, form submissions) containing attacker‑supplied instructions that the model treats as legitimate commands; attacks exploit retrieval/RAG pipelines and trust boundaries between content and system instructions to cause exfiltration, destructive commands, or unauthorized actions.
- **Affected Products:** Google Gemini Enterprise, Google Workspace
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public weaponized PoC disclosed by Google; research teams (Forcepoint, Noma Labs, others) published in‑the‑wild examples but no centralized public exploit repository.
- **Patch Available:** Vendor advisory and mitigation guidance available at https://blog.google/security/prompt-injections-web/; additional mitigations referenced at https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/
- **Active Exploitation:** Google observed a small number of malicious IPI instances on the public web and reported a ~32% increase in detections between Nov 2025 and Feb 2026; researchers (Forcepoint, Noma Labs) reported additional in‑the‑wild examples.
- **Threat Actors:** None known
- **Mitigation:** Layered defense — enforce strict instruction/data separation, coarse‑to‑fine filtering when scanning web content, deny or sanitize untrusted content before ingestion, minimize RAG data scope and permissions, continuous telemetry/monitoring and model hardening.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) in Retrieval‑Augmented Generation (RAG): an attacker embeds malicious instructions in shared Workspace artifacts (Docs, Calendar invites, Gmail). The Gemini model retrieves this content, treats the embedded instructions as genuine prompts, and may execute actions such as data exfiltration by embedding results in an external image request.
- **Affected Products:** Google Workspace (Gemini Enterprise / Gemini-powered Workspace features: Gmail, Calendar, Docs)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Proof-of-concept described by Noma Labs (GeminiJack) in disclosure; no publicly weaponized exploit URL listed.
- **Patch Available:** Patch/advisory implemented via continuous defenses; no discrete patch URL available.
- **Active Exploitation:** Noma Labs disclosed an active zero‑click vulnerability (GeminiJack) and confirmed that Google applied mitigations. No widespread active exploitation groups have been reported.
- **Threat Actors:** None known
- **Mitigation:** Defense‑in‑depth per Google: human and automated red‑team testing, synthetic attack data generation, deterministic defenses (user confirmation, URL sanitization, tool‑chaining policies governed by a centralized Policy Engine), ML/LLM‑based retraining and prompt engineering, and Gemini model hardening. Additionally, apply least‑privilege datasource access and monitor for anomalous outbound requests.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection in agentic browsing can cause an AI agent (Gemini) to be manipulated via malicious webpage content, enabling zero‑click exploit chains (e.g., GeminiJack) when combined with other flaws.
- **Affected Products:** Chrome (Gemini for Chrome / agentic browsing feature)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Noma Labs disclosed GeminiJack zero‑click vulnerability; no public PoC URL provided.
- **Patch Available:** Google announced layered defenses and architectural changes to mitigate indirect prompt injection; see vendor blog for details (no separate patch URL provided).
- **Active Exploitation:** No confirmed in-the-wild exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Use Chrome’s layered defenses for agentic browsing (restrict origin access, block prompt injections, monitor agent actions); follow vendor blog guidance.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Privilege‑escalation in Android Framework allowing apps to bypass permission checks and gain elevated privileges without user interaction.
- **Affected Products:** Android 11, Android 12, Android 13, Android 14
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Proof‑of‑concept/exploit details not published publicly; no public PoC URL available.
- **Patch Available:** June 2026 security patches are available; AOSP source patches to be released (see bulletin).
- **Active Exploitation:** Yes — Google bulletin notes "indications" of limited, targeted exploitation; secondary reporting confirms active targeted attacks.
- **Threat Actors:** None known
- **Mitigation:** Disable unknown‑source installs, restrict app permissions, enable Google Play Protect, push updates via MDM, block sideloading/allowlisting until patched.
- **Vendor Advisory:** http://source.android.com/docs/security/bulletin/2026/2026-06-01

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection injects hidden malicious instructions into external data (emails, documents, calendar invites) that cause AI models to exfiltrate data or execute actions. Google mitigates this with layered defenses (content classifiers, markdown sanitization, URL redaction, user‑confirmation, security notifications). The Cursor vulnerability (CVE‑2025‑54131) allows bypass of the allowlist in auto‑run mode via backtick (`) or $(cmd), leading to arbitrary command execution when combined with indirect prompt injection; fixed in version 1.3.
- **Affected Products:** Gemini (models and app), Gemini CLI, Cursor <1.3
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept linked in the vendor advisory; third‑party write‑ups exist (The Register) but no widely circulated exploit.
- **Patch Available:** Gemini CLI versions 0.39.1 and 0.40.0-preview.3 are patched; Cursor is patched in version 1.3. References: the Google blog, the NVD entry and The Register article.
- **Active Exploitation:** No confirmed active exploitation reported in the vendor blog; third‑party sources only warn of potential abuse.
- **Threat Actors:** None known
- **Mitigation:** Apply Google’s layered defenses (prompt‑injection content classifiers, markdown sanitization, suspicious URL redaction, user‑confirmation framework, security‑notification system) and update Gemini CLI to versions 0.39.1 or 0.40.0‑preview.3 and Cursor to ≥1.3. Avoid running the CLI in headless or untrusted environments, pin GitHub Action versions, require explicit workspace trust, enable user confirmations, and sanitize all inputs.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors target large backbone routers and PE/CE routers, leverage compromised devices and trusted connections to pivot, and modify routers to maintain persistent long‑term access; they exploit weak credentials, unpatched vulnerabilities, misconfigurations, and supply‑chain/access via managed service providers to establish persistence and global espionage capabilities.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unavailable (no public PoC/weaponized exploit linked in CISA advisory).
- **Patch Available:** Patch availability varies by vendor; no single vendor patch covers all affected routers/devices. Refer to vendor advisories for specific router vendors. No unified CISA‑hosted vendor patch URL available.
- **Active Exploitation:** Confirmed active exploitation in the wild reported by CISA; actors maintain persistent access to telecommunications, government, transportation, lodging, and military networks (see CISA advisory AA25-239A).
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Key mitigations—restrict administrative access (apply least privilege, multifactor authentication), inventory and segment router management networks, deploy strong patch management per vendor advisories, rotate credentials and keys, monitor for configuration changes and unauthorized tunnels, apply logging/alerting on anomalous routing/configuration activity, isolate compromised devices and rebuild from known‑good images, and follow vendor‑specific mitigation guidance. If vendor advisories are unavailable, apply compensating controls and hardening per CISA guidance.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC/weaponized exploit reported in cited advisories
- **Patch Available:** Patch not applicable
- **Active Exploitation:** Confirmed ongoing targeting since 2022 per joint CSA
- **Threat Actors:** GRU 85th GTsSS (Unit 26165, APT28)
- **Mitigation:** Follow joint CSA mitigation and detection recommendations (network monitoring, multifactor authentication, timely patching, principle of least privilege, segmentation, incident response planning).
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 9. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** Race-condition in Microsoft Defender/Malware Protection Engine enables a SYSTEM-level shell (RoguePlanet).
- **Affected Products:** Windows 10, Windows 11, Microsoft Defender, Visual Studio
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC exploit named RoguePlanet reported; source: The Hacker News article.
- **Patch Available:** June 2026 Patch Tuesday update KB5094126 released by Microsoft.
- **Active Exploitation:** Confirmed active exploitation of Microsoft Defender and Malware Protection Engine vulnerabilities reported by RedLegg.
- **Threat Actors:** None known
- **Mitigation:** Apply the June 2026 Patch Tuesday update (KB5094126). If the patch cannot be applied, disable or harden Microsoft Defender components and monitor with standard EDR/IDS tools.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 10. 🟠 Zero-Day — US Gov asks Anthropic to ban 'foreign national' access to Fable, Mythos

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-13
**Reference:** <https://www.bleepingcomputer.com/news/security/us-gov-asks-anthropic-to-ban-foreign-national-access-to-fable-mythos/>

> The US government has ordered Anthropic to block all foreign nationals from accessing Fable 5 and Mythos 5, forcing the company to suspend both models worldwide. Anthropic is complying but disputes the basis, calling the cited jailbreak narrow and the capability widely available elsewhere. [...]

**Parallel AI Enrichment:**

- **Technical Details:** Anthropic disabled access to Fable 5 and Mythos 5 after receiving a U.S. government export‑control directive ordering a block on foreign‑national access; the company argues the cited jailbreak is narrow and the capability exists elsewhere.
- **Affected Products:** Claude Fable 5; Claude Mythos 5 (discontinued/unavailable as of 2026-06-12/13)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** None known.
- **Patch Available:** Not applicable — models were suspended by vendor in response to a government directive; Vendor advisory URL unavailable.
- **Active Exploitation:** No confirmed active exploitation reported; action appears to be regulatory/export‑control driven rather than evidence of exploitation in the wild.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟡 High Severity — Critical Splunk Enterprise Flaw Lets Attackers Run Code Without Authentication

**CVE:** `CVE-2026-20253` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-13
**Reference:** <https://thehackernews.com/2026/06/critical-splunk-enterprise-flaw-lets.html>

> Splunk has released security updates to address a critical security flaw in Splunk Enterprise that could be exploited to conduct unauthenticated file operations and even remote code execution.

The vulnerability, tracked as CVE-2026-20253, is rated 9.8 on the CVSS scoring system.

&quot;In Splunk Enterprise versions below 10.2.4 and 10.0.7, an unauthenticated user could create or truncate arbitrar…

---

## 12. 🟡 High Severity — File Browser has incorrect access control for public directory shares via rule path rebasing

**CVE:** `CVE-2026-54091` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-j9jx-hp4c-ghhh>

> ### Summary
File Browser&#x27;s public share handlers rebase the share owner&#x27;s filesystem root to the shared directory and then evaluate descendant paths against the owner&#x27;s global and per-user rules using the rebased relative path instead of the original path relative to the owner&#x27;s scope.

As a result, an attacker who knows a public directory share URL can access files and subdire…

---

## 13. 🟡 High Severity — File Browser has a DoS Vulnerability via Public Login API

**CVE:** `CVE-2026-54092` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-w5fm-68j4-fpc4>

> ### Summary
Unchecked passwords maximums allow for an arbitrarily large password to be passed into the login API. This spikes CPU and memory, and after testing, crashes, heavily lags any container created, and has even made my docker daemon start to send errors with status code 500 even after the container was destroyed.

### Details
When sending JSON in the body of the request to the route `api/l…

---

## 14. 🟡 High Severity — Fleet: Observer-level enrollment secret extraction via ORDER BY oracle on Apple MDM commands endpoint

**CVE:** `CVE-2026-46371` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-x4qr-qw6h-wvxq>

> ### Summary

A vulnerability in Fleet&#x27;s Apple MDM commands listing endpoint allowed authenticated users with the lowest-privilege Observer role to extract sensitive values from joined database tables — including host enrollment secrets and Apple Push Notification Service (APNS) tokens — through a cursor-based binary search oracle. The endpoint accepted a user-supplied `order_key` parameter th…

---

## 15. 🟡 High Severity — Fleet has observer-level enrollment secret extraction via ORDER BY oracle on labels host-listing endpoint

**CVE:** `CVE-2026-46370` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-vxm7-9x8v-8gm4>

> ### Summary

A vulnerability in Fleet&#x27;s labels host-listing endpoint allowed authenticated users with the lowest-privilege Observer role to extract host enrollment secrets (`node_key`, `orbit_node_key`) through a cursor-based binary search oracle. The endpoint accepted a user-supplied `order_key` parameter that was not validated against a column allowlist, permitting sort order to be driven b…

---

## 16. 🟡 High Severity — Fabric.js improper escaping in fabric.Gradient colorStops leads to XSS in SVG serialization

**CVE:** `CVE-2026-44311` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-w22m-hvvm-xmwx>

> ### Summary

A potential Cross-Site Scripting (XSS) vulnerability exists in Fabric.js due to improper escaping of user-controlled input during SVG serialization via the `toSVG()` method.

Specifically, the `color` field within the `colorStops` array of a `fabric.Gradient` object is not properly escaped when converted into SVG `&lt;stop&gt;` elements. If an application renders the generated SVG str…

---

## 17. 🟡 High Severity — Radius Controller May Delete a Container Resource via an Injected Deployment Annotation (Multi-Tenant Installs)

**CVE:** `CVE-2026-53999` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-fp5j-4fj2-4jvq>

> # Radius Controller May Delete a Container Resource via an Injected Deployment Annotation (Multi-Tenant Installs)

## Summary

A configuration-validation issue in the Radius Kubernetes controller can cause it to issue a `DELETE` for the container resource referenced by a tampered `radapp.io/status` annotation on a Deployment. It follows the &quot;Confused Deputy&quot; pattern. Real-world impact is…

---

## 18. 🟡 High Severity — TYPO3 CMS has Privilege Escalation & SQL Injection in its Form Framework

**CVE:** `CVE-2026-49741` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-jh32-v29g-68pq>

> ### Problem
Backend users with write access to the `form_definition` database table were able to directly create, update, or delete form definition records via `DataHandler`, bypassing the Form Framework&#x27;s persistence validation and permission checks. This allowed injecting arbitrary form configurations, re-enabling attack vectors originally addressed in [TYPO3-CORE-SA-2018-003](https://typo3…

---

## 19. 🟡 High Severity — TYPO3 CMS has Insecure Deserialization via Core API

**CVE:** `CVE-2026-49740` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-c78m-c52x-jgwp>

> ### Problem
TYPO3&#x27;s cache frontend (`VariableFrontend`) and persistent key-value store (`Registry`) deserialized PHP payloads without integrity validation or class restrictions. An attacker with write access to the underlying storage backend (cache store or sys_registry database table) could inject a crafted serialized payload to trigger PHP Object Injection, potentially exploiting a gadget c…

---

## 20. 🟡 High Severity — TYPO3 CMS has Broken Access Control in its File Abstraction Layer

**CVE:** `CVE-2026-49738` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://github.com/advisories/GHSA-jf56-v8jc-jcc5>

> ### Problem
The path allowance check in `GeneralUtility::isAllowedAbsPath()` performed a plain string prefix comparison without requiring a directory separator boundary, causing a path like `/var/www/html-other/secret.yaml` to be incorrectly accepted as valid when the project root was `/var/www/html`. Administrator users with access to the File Abstraction Layer were able to create new file storag…

---

## 21. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
