# Zero Day Pulse

> **Generated:** 2026-06-17 19:57 UTC &nbsp;|&nbsp; **Total:** 49 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 20 &nbsp;|&nbsp; 🟡 High: 29 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Multiple unauthenticated path traversal vulnerabilities in SimpleHelp v5.5.7 and earlier allow attackers to read sensitive files from the server filesystem via crafted requests.
- **Affected Products:** SimpleHelp remote support / Remote Monitoring and Management software, versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public exploit or PoC documented in available sources.
- **Patch Available:** Upgrade to the vendor‑provided fixed version as described in the advisory.
- **Active Exploitation:** Confirmed active exploitation reported by CISA.
- **Threat Actors:** Ransomware actors (unspecified groups)
- **Mitigation:** Apply the vendor patch by upgrading SimpleHelp to the fixed version. If immediate patching is not possible, limit network exposure of SimpleHelp (firewall/VPN), monitor for signs of compromise, and follow CISA mitigation guidance.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — Hostile states behind three-quarters of attacks on Britain's critical infrastructure, cyber chief warns

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Record by Recorded Future &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://therecord.media/britain-nation-state-cyberattacks-richard-horne-rusi>

> NCSC CEO Richard Horne warned that “kinetic targeting in any conflict tomorrow will be based on intelligence gathered today” and that nation-state adversaries were “prepositioning” throughout British critical infrastructure.

**Parallel AI Enrichment:**

- **Technical Details:** No specific CVE or technical vulnerability disclosed; NCSC and The Record describe 'prepositioning'—state actors establishing footholds in critical infrastructure to enable rapid exploitation, but no technical exploit mechanism is detailed.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** None known.
- **Patch Available:** Patch/advisory unavailable.
- **Active Exploitation:** NCSC reported managing >200 incidents year to May 2026 with ~75% linked to hostile state actors; no public, attributed technical exploits or CVEs detailed in the cited reporting.
- **Threat Actors:** State‑linked actors (notably Russia, China, Iran); article cites Chinese‑linked Volt Typhoon as example.
- **Mitigation:** High‑level mitigations recommended: strengthen security fundamentals, understand exposure, apply patches, harden systems, improve resilience and recovery capabilities; follow NCSC guidance (e.g., Frontier AI guidance and Cyber Assessment Framework).
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — Microsoft Confirms RoguePlanet Defender Zero-Day, Says Patch is in Development

**CVE:** `CVE-2026-50656` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://thehackernews.com/2026/06/microsoft-confirms-rogueplanet-defender_02022423645.html>

> Microsoft has formally disclosed that it&#x27;s working to release a patch to address a Defender zero-day codenamed RoguePlanet.

The vulnerability has now been assigned the CVE identifier CVE-2026-50656 (CVSS score: 7.8), with the tech giant describing it as a privilege escalation flaw.

&quot;Microsoft is aware of an elevation of privilege in the Microsoft Malware Protection Engine in Microsoft …

**Parallel AI Enrichment:**

- **Technical Details:** Race condition in the Microsoft Malware Protection Engine (Microsoft Defender) that enables local privilege escalation to SYSTEM when successfully exploited.
- **Affected Products:** Microsoft Defender (Microsoft Malware Protection Engine) on Windows 10 and Windows 11 (fully patched versions reported).
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC(s) reported — e.g. MSNightmare/RoguePlanet GitHub and PoC releases by Chaotic Eclipse.
- **Patch Available:** Patch in development; Microsoft working on update (no public patch URL yet).
- **Active Exploitation:** Public reporting and prior research indicate active exploitation of Microsoft Defender vulnerabilities in the wild; Microsoft has acknowledged the issue and multiple security outlets report PoC availability and testing.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — Malicious JetBrains Plugins Steal AI API Keys as Chrome Extensions Capture Chatbot Chats

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://thehackernews.com/2026/06/malicious-jetbrains-plugins-steal-ai.html>

> Cybersecurity researchers have flagged a &quot;coordinated malware campaign&quot; on the JetBrains Marketplace that has published no less than 15 malicious plugins capable of exfiltrating artificial intelligence (AI) provider keys.

&quot;Every plugin poses as an AI coding assistant built on DeepSeek and other large language models, offering chat, commit messages, code review, bug finding, and uni…

**Parallel AI Enrichment:**

- **Technical Details:** Malicious plugins function as advertised but exfiltrate user‑entered AI provider API keys by sending them in plaintext over HTTP to attacker‑controlled server (39.107.60[.]51). Plugins share a common codebase and include a donation/payment flow that can return working API keys to paying users, enabling misuse of victims' keys.
- **Affected Products:** DeepSeek Junit Test (org.sm.yms.toolkit), DeepSeek Git Commit (com.json.simple.kit), DeepSeek FindBugs (org.bug.find.tools), DeepSeek AI Chat (org.translate.ai.simple), DeepSeek Dev AI (com.yy.test.ai.simple), DeepSeek AI Coding (com.dev.ai.toolkit), AI FindBugs (com.json.view.simple), AI Git Commitor (com.my.git.ai.kit), AI Coder Review (org.check.ai.ds), DeepSeek Coder AI (com.review.tool.code), AI Coder Assistant (org.code.assist.dev.tool), DeepSeek Code Review (com.coder.ai.dpt), CodeGPT AI Assistant (com.my.code.tools), DeepSeek AI Assist (ord.cp.code.ai.kit), Coding Simple Tool (com.dp.git.ai.tool)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC reported. No weaponized exploit URL found.
- **Patch Available:** No official vendor patch reported; JetBrains removed malicious plugins from Marketplace per reports.
- **Active Exploitation:** Reported active exfiltration of API keys by the plugins; news reports and Aikido Security analysis indicate the campaign has been ongoing since Oct 2025 with downloads (some plugins >25,000).
- **Threat Actors:** None known
- **Mitigation:** Remove/uninstall the listed plugins; revoke and rotate any exposed AI provider API keys (OpenAI, etc.); avoid pasting long‑lived secrets into unvetted plugins; enable least privilege and monitor billing/usage; use short‑lived or scoped credentials and enforce secrets scanning. Vendor removal from Marketplace reported.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when attacker‑controlled content (web pages, shared docs, emails) is retrieved by RAG or agentic systems and contains hidden or explicit instructions that the model follows. Techniques include concealment (visually‑hidden text, HTML comments, metadata), authority impersonation, conditional targeting, and exfiltration channels. GeminiJack demonstrated a zero‑click RAG/Workspace weakness that exfiltrated data via a poisoned shared artifact; Antigravity showed a prompt‑injection chain leading to sandbox escape.
- **Affected Products:** Gemini Enterprise, Vertex AI Search, agentic IDEs like Antigravity
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Public PoCs are available via Forcepoint blog and Noma disclosure; no single packaged exploit URL.
- **Patch Available:** No
- **Active Exploitation:** Yes, multiple reports of IPI payloads observed in the wild (Forcepoint, Google telemetry, Antigravity RCE).
- **Threat Actors:** None known
- **Mitigation:** Follow Google's layered defenses and hardening guidance: block/monitor IPI indicators in ingestion pipelines, perform content context checks (detect concealment like visually‑hidden elements, HTML comments, metadata abuse), restrict agent browsing and payment scopes, validate/sanitize RAG sources and long‑term memory, run red‑team IPI tests and quarterly audits.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) injects malicious instructions into data/tools consumed by LLMs (including zero‑click scenarios) to influence model behavior; attacks are discovered via red‑teaming and VRP, and defenses include deterministic sanitization and model hardening.
- **Affected Products:** Google Workspace with Gemini (Gmail, Docs, Workspace apps)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC/exploit URL provided.
- **Patch Available:** Mitigations are implemented via continuous defenses (deterministic, ML, LLM hardening); no single patch URL provided.
- **Active Exploitation:** No confirmed active exploitation detailed in this vendor blog.
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses: user confirmation, URL sanitization, tool‑chaining policies, centralized policy engine (regex takedowns), ML‑model retraining with synthetic attack data, LLM prompt engineering, Gemini model hardening.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** An indirect prompt injection attack embeds crafted content on a webpage which influences the prompt material seen by Gemini‑powered agents; when combined with the GeminiJack vulnerability in Gemini Enterprise, this enables zero‑click extraction or silent actions without user interaction.
- **Affected Products:** Chrome agentic browsing / Gemini integration, Google Gemini Enterprise (fixed in version 1.3)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No confirmed public PoC in cited sources
- **Patch Available:** Fixed in version 1.3; see Google advisory
- **Active Exploitation:** Public disclosures (Noma Labs) reported the vulnerability; no widely attributed active exploitation reports in cited sources.
- **Threat Actors:** None known
- **Mitigation:** Update to fixed version 1.3; apply Chrome’s layered defenses (origin restrictions, prompt‑injection filtering, secondary agent oversight); restrict agentic features in high‑risk environments until patched.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A no‑interaction elevation‑of‑privilege (privilege escalation) flaw in the Android Framework that allows an attacker to gain higher privileges without user interaction, enabling targeted exploits to escalate privileges on affected devices.
- **Affected Products:** Android Framework on Android 14‑16
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Active targeted exploit reported by Google (no public PoC known)
- **Patch Available:** Yes — Google released patches in the June 2026 security bulletin (patch level 2026-06-05). See Google advisory URL above.
- **Active Exploitation:** Confirmed by Google — vulnerability CVE‑2025‑48595 was reported as under active targeted attack and patched in June 2026.
- **Threat Actors:** None known
- **Mitigation:** Install the June 2026 Android security updates immediately; if patch unavailable, avoid installing untrusted apps, restrict app install sources, enable Play Protect, and limit device exposure to untrusted networks.
- **Vendor Advisory:** https://security.googleblog.com/2026/06/android-security-bulletin-june-2026.html

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection involves malicious instructions hidden in external content such as emails or documents that are fed to LLM‑based assistants. Google mitigates this by adversarial‑training Gemini 2.5 models, using markdown sanitizers to remove external image URLs, redacting suspicious URLs based on Safe Browsing, and prompting users for confirmation before risky actions.
- **Affected Products:** Gemini (app and Gemini in Google Workspace), Gemini in Gmail, AI features in Google Workspace (e.g., document summarization).
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept (PoC) or weaponized exploit was identified.
- **Patch Available:** No discrete patch is described; mitigations are delivered as built‑in product defenses.
- **Active Exploitation:** No confirmed active exploitation in the wild has been reported.
- **Threat Actors:** None known
- **Mitigation:** Layered defense: adversarial‑training of Gemini 2.5 models, ML detectors for malicious instructions, deterministic defenses such as markdown sanitization, URL redaction via Safe Browsing, and contextual user‑confirmation dialogs (Human‑In‑The‑Loop).
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors modify backbone, provider edge (PE) and customer edge (CE) routers to maintain persistent access, then leverage compromised devices and trusted connections to pivot and expand reach within target networks.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit information available.
- **Patch Available:** Patch information unavailable.
- **Active Exploitation:** Confirmed active exploitation is reported in the advisory, indicating ongoing targeting of global networks.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Implement network segmentation for backbone, PE and CE routers; monitor for unauthorized configuration changes; apply strict access controls; use simulation tools to emulate the threat behavior and validate defenses.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 12. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

---

## 13. 🟠 Zero-Day — Introducing the Red Agent POV Series

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Wiz Research &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://www.wiz.io/blog/red-agent-pov-series>

> An inside look at how the Red Agent, our AI-Powered Attacker, uncovers complex, exploitable risks in the wild

---

## 14. 🟠 Zero-Day — The Top 10 Attack Surface Exposures in 2026

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://thehackernews.com/2026/06/the-top-10-attack-surface-exposures-in.html>

> Breaches don&#x27;t always start with a zero-day. An exposed admin panel can get brute-forced, or credentials reused from a previous attack. But when a vulnerability does drop — like MongoBleed earlier this year, which let attackers pull credentials and session tokens from server memory without authentication — anything internet-facing is immediately at risk.

With time-to-exploit now down to a

---

## 15. 🟠 Zero-Day — CISA orders feds to patch max severity Joomla plugin flaw by Friday

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-max-severity-joomla-plugin-flaw-by-friday/>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has ordered federal agencies to patch a maximum-severity flaw in the Widget Factory Joomla Content Editor (JCE) plugin that is being actively exploited in the wild. [...]

---

## 16. 🟠 Zero-Day — Microsoft Working on Patch for ‘RoguePlanet’ Zero-Day

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://www.securityweek.com/microsoft-working-on-patch-for-rogueplanet-zero-day/>

> The public PoC code exploits a race condition in Microsoft Defender to spawn a command prompt with System privileges. The post Microsoft Working on Patch for ‘RoguePlanet’ Zero-Day appeared first on SecurityWeek .

---

## 17. 🟠 Zero-Day — Microsoft working on Defender patch for RoguePlanet zero-day

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://www.bleepingcomputer.com/news/microsoft/microsoft-working-on-defender-patch-for-rogueplanet-zero-day/>

> Microsoft confirmed that it&#x27;s working on a security patch for a Defender zero-day vulnerability named &quot;RoguePlanet,&quot; disclosed one week ago. [...]

---

## 18. 🟠 Zero-Day — CISA Warns of Actively Exploited Joomla JCE Flaw Allowing PHP Code Execution

**CVE:** `CVE-2026-48907` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://thehackernews.com/2026/06/cisa-warns-of-actively-exploited-joomla.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added a maximum-severity security flaw impacting Widget Factory Joomla Content Editor (JCE) to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

The vulnerability, tracked as CVE-2026-48907 (CVSS score: 10.0), is a case of improper access control that could facilitate arbitrary

---

## 19. 🟠 Zero-Day — Pi Agent: Potential XSS in HTML session exports via Markdown URL sanitization bypass

**CVE:** `CVE-2026-54326` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-7v5m-pr3q-6453>

> # Potential XSS in HTML session exports via Markdown URL handling

Pi HTML exports render session Markdown into a static HTML file. Affected versions did not consistently reject unsafe Markdown link and image URL schemes. In versions with scheme filtering, C0 control characters in the URL scheme could bypass the check because browsers normalize those characters before navigation.

## Impact

The r…

---

## 20. 🟠 Zero-Day — Malicious JetBrains Marketplace plugins steal AI API keys from developers

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://www.bleepingcomputer.com/news/security/malicious-jetbrains-marketplace-plugins-steal-ai-api-keys-from-developers/>

> At least 15 malicious plugins found on the JetBrains Marketplace were designed to steal AI API keys from developers. [...]

---

## 21. 🟡 High Severity — Avo: Missing Authorization in Avo Association Attach Endpoint Allows Unauthorized Relationship Manipulation and Privilege Escalation

**CVE:** `CVE-2026-55518` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-8fq9-273g-6mrg>

> ## Summary

A critical missing authorization flaw exists in Avo&#x27;s association attach workflow. The UI and `GET /resources/:resource/:id/:related/new` path can check `attach_&lt;association&gt;?`, but the actual write endpoint, `POST /resources/:resource/:id/:related`, does not run the same authorization check before mutating the association.

As a result, an authenticated low-privileged Avo u…

---

## 22. 🟡 High Severity — HAPI FHIR: XXE in XsltUtilities.saxonTransform via unhardened Saxon TransformerFactory

**CVE:** `CVE-2026-55471` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-2f55-g35j-5jmf>

> ### Summary

`org.hl7.fhir.utilities.XsltUtilities` exposes two parallel families of XSLT
transform helpers. The `transform(...)` overloads obtain their
`TransformerFactory` from the project&#x27;s hardened helper
`XMLUtil.newXXEProtectedTransformerFactory()` (which sets
`ACCESS_EXTERNAL_DTD=&quot;&quot;` and `ACCESS_EXTERNAL_STYLESHEET=&quot;&quot;`). The sibling
`saxonTransform(...)` overloads i…

---

## 23. 🟡 High Severity — LangChain4j: SQL injection via metadata filters in langchain4j-mariadb and langchain4j-pgvector

**CVE:** `CVE-2026-55405` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-2mfg-cc43-9pcj>

> ### Summary
The MariaDB and pgvector embedding stores build metadata-filter SQL by string-concatenating
filter **keys** (and, in MariaDB, string **values**) directly into the query without adequate
escaping. A crafted metadata key in `EmbeddingSearchRequest.filter()` can break out of its SQL
context and inject arbitrary SQL into the statements executed by the stores&#x27; search and
`removeAll(Fil…

---

## 24. 🟡 High Severity — Capsule: Incomplete fix of CVE-2026-30963: singular/plural typo leaves namespaces/finalize unprotected

**CVE:** `CVE-2026-55636` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-gwxr-7h77-7777>

> ### Summary
Capsule v0.13.2 webhook rules contain `namespace/finalize` (singular) instead of `namespaces/finalize` (plural). K8s requires plural. The finalize defense from CVE-2026-30963 fix is absent.

### Details
PUT to `/api/v1/namespaces/&lt;ns&gt;/finalize` has resource=namespaces (plural). The singular rule never matches. `matchPolicy: Equivalent` does not compensate.

### PoC
Confirmed on k…

---

## 25. 🟡 High Severity — webpack-dev-server vulnerable to HMR WebSocket interception via permissive user proxies

**CVE:** `CVE-2026-9595` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-mx8g-39q3-5c79>

> ### Impact

When a user-configured proxy on `webpack-dev-server` has a broad context (e.g. `/`) and `ws: true`, it also intercepts the dev server&#x27;s own HMR WebSocket and forwards it to the proxy target. This leaks the browser&#x27;s cookies and `Origin` header to the backend, bypasses the dev server&#x27;s Host/Origin validation, and corrupts the HMR socket (both HMR and the proxy end up writ…

---

## 26. 🟡 High Severity — Gitea: API Fork Missing CanCreateOrgRepo Check Allows Org Secret Exfiltration

**CVE:** `CVE-2026-22555` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-fhx7-m96w-mv29>

> ## Summary

The API endpoint `POST /api/v1/repos/{owner}/{repo}/forks` only checks `IsOrgMember()` when a user forks a repository into an organization, but does not check `CanCreateOrgRepo()`. The web UI fork handler correctly checks both. This allows a read-only organization member — in a team with `can_create_org_repo=false` — to create repositories in the organization namespace via the API. The…

---

## 27. 🟡 High Severity — Daytona: Cross-tenant data leak in notification WebSocket gateway via unverified organizationId join

**CVE:** `CVE-2026-54324` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-qwxf-2m7m-2m3x>

> ### Summary
A cross-tenant authorization flaw in Daytona&#x27;s notification WebSocket gateway allowed any authenticated user to subscribe to another organization&#x27;s realtime notification channel and passively receive that organization&#x27;s events.

### Impact
The notification gateway&#x27;s JWT handshake joined a client-supplied organization identifier to the corresponding notification room…

---

## 28. 🟡 High Severity — Open WebUI: SSRF Protection Bypass in Playwright Web Loader via HTTP Redirects

**CVE:** `CVE-2026-54018` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-jrfp-m64g-pcwv>

> ### Summary
The SafePlaywrightURLLoader implements a validate_url function to prevent SSRF attacks by checking the IP address of the user-provided URL. However, this validation is performed only on the initial URL.

Since Playwright automatically follows HTTP redirects (301/302) by default, an attacker can bypass the validation by providing a safe URL that redirects to a restricted internal networ…

---

## 29. 🟡 High Severity — Open WebUI: Path traversal / SSRF in terminal server proxy via encoded path traversal

**CVE:** `CVE-2026-54017` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-r2wg-2mcr-66rv>

> ### Summary

The terminal-server reverse proxy in `backend/open_webui/routers/terminals.py` does not fully confine the user-controlled `path` segment before forwarding it to an admin-configured terminal server. An authenticated user who has been granted access to a terminal server can craft `path` values containing encoded `../` traversal sequences that escape the intended path (or policy) scope o…

---

## 30. 🟡 High Severity — OpenClaw: MCP Streamable HTTP redirects could forward configured custom headers to another origin

**CVE:** `CVE-2026-53840` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-rjxq-qqhf-8hwh>

> ### Summary

OpenClaw supports remote MCP Streamable HTTP servers with operator-configured custom headers. In affected releases, those headers could be forwarded when the MCP endpoint responded with a cross-origin redirect.

This issue is limited to configured MCP Streamable HTTP servers that use custom headers. It does not expose unrelated OpenClaw credentials.

### Affected configurations

This …

---

## 31. 🟡 High Severity — Open WebUI: Redirect-Bypass SSRF in OAuth `_process_picture_url` (incomplete-fix sibling of CVE-2026-45401)

**CVE:** `CVE-2026-54008` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-226f-f24g-524w>

> ## Summary

`backend/open_webui/utils/oauth.py::_process_picture_url` (v0.9.5, lines 1435-1470) calls `validate_url(picture_url)` on the initial URL only, then invokes `aiohttp.ClientSession.get(picture_url, ...)` without `allow_redirects=False`. aiohttp&#x27;s default is `allow_redirects=True, max_redirects=10`; the function does not pass the project&#x27;s `AIOHTTP_CLIENT_ALLOW_REDIRECTS` env co…

---

## 32. 🟡 High Severity — NocoDB: Refresh Tokens Persist Through Password Recovery

**CVE:** `CVE-2026-53928` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-r989-7g3j-wjhw>

> ### Summary
A stolen refresh token survived a password-forgot flow and could be used to mint fresh
JWTs even after the user reset their password.

### Details
`passwordChange` and `passwordReset` deleted the user&#x27;s refresh tokens, but
`passwordForgot` only rotated `token_version` and revoked OAuth tokens — it did not
call `UserRefreshToken.deleteAllUserToken(user.id)`. An attacker holding a c…

---

## 33. 🟡 High Severity — vLLM: incomplete CVE-2026-22778 fix leaks PIL repr addresses via Anthropic router

**CVE:** `CVE-2026-54236` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-hgg8-fqqc-vfmw>

> # vLLM: incomplete CVE-2026-22778 fix leaks PIL repr addresses via the Anthropic API router

**Researcher:** Kai Aizen — SnailSploit (@SnailSploit), Adversarial &amp; Offensive Security Research
**Severity:** CVSS 3.1 5.3 (Medium)  `AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N`
**Target:** https://github.com/vllm-project/vllm

---

## Summary

The fix for CVE-2026-22778 / GHSA-4r2x-xpjr-7cvv (PRs #31987 an…

---

## 34. 🟡 High Severity — Traefik: Kubernetes Gateway crossProviderNamespaces bypass allows HTTPRoute outside the allowlist to expose internal Traefik services

**CVE:** `CVE-2026-54761` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-3g6v-2r68-prfc>

> ## Summary

There is a high severity vulnerability in Traefik&#x27;s Kubernetes Gateway provider affecting the `crossProviderNamespaces` allowlist. For `HTTPRoute` rules that declare multiple (WRR) backendRefs, Traefik evaluates the allowlist against the target `backendRef.namespace` instead of the route&#x27;s own namespace. As a result, an `HTTPRoute` created in a namespace that is not allow-lis…

---

## 35. 🟡 High Severity — Pi Agent: Pi loads project-local extensions without approval

**CVE:** `CVE-2026-54325` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-mqxh-6gq7-558m>

> # Pi loads project-local extensions without approval

Pi before 0.79.0 loaded project-local configuration and resources from a repository&#x27;s `.pi` directory without first asking the user to trust that repository. This included project-local extensions, which are executable TypeScript or JavaScript modules loaded into the Pi process.

An attacker who controls a repository could place Pi-specifi…

---

## 36. 🟡 High Severity — Pi Agent: Predictable temporary extension install paths allow local privilege escalation on shared Linux hosts

**CVE:** `CVE-2026-54328` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-jfgx-wxx8-mp94>

> # Predictable temporary extension install paths allow local privilege escalation on shared Linux hosts

Pi versions with temporary npm or git extension package installs used predictable paths under the operating system temporary directory. On Linux-based multi-user systems, a local attacker who can write to the shared temporary directory could prepare the expected package location before another u…

---

## 37. 🟡 High Severity — Gogs: Overwriting critical files results in a denial of service

**CVE:** `CVE-2026-52797` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-pm6v-2h4w-4rp2>

> **Vulnerability type:** Path Traversal
**Impact:** DoS
**Exploitation prerequisite:** authorized user
**Description:** As an authorized user, an intruder can dictate the value which is passed to the `git diff` command which, together with bypassing the filtering of the passed value, allows the user to bypass the target directory and write the result of the comparison to any arbitrary path.
**Resea…

---

## 38. 🟡 High Severity — n8n: SecurityScorecard Node Leaks API Token to User-Controlled Host

**CVE:** `CVE-2026-54304` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-rm2v-h48j-895m>

> ## Impact
An authenticated user with permission to create or modify workflows and access to a SecurityScorecard credential with limited allowed domains could configure the SecurityScorecard node&#x27;s report download operation to target an attacker-controlled URL. The node attached the SecurityScorecard API token to the outbound request, causing the credential to be sent to the attacker-controlle…

---

## 39. 🟡 High Severity — n8n: Cross-Tenant Credential Takeover via Dynamic Credentials EE Endpoints

**CVE:** `CVE-2026-54305` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-2j5h-858j-5mpf>

> ## Impact
Three EE endpoints used by the Dynamic Credentials feature accepted any authenticated n8n session without performing per-resource ownership or scope checks on the target workflow or credential. An authenticated user with no project membership or credential sharing relationship could enumerate credential identifiers, names, and types referenced by any private workflow in the instance, ini…

---

## 40. 🟡 High Severity — OpenStack Nova: Nova scheduler hint injection bypasses Placement resource claims and scheduling constraints

**CVE:** `CVE-2026-46448` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-mfg3-p6m3-gjgr>

> ## Affects

- Nova: &gt;=18.0.0 &lt;31.3.1, &gt;=32.0.0 &lt;32.2.1, &gt;=33.0.0 &lt;33.0.2


## Description
Erichen from the Institute of Computing Technology, Chinese Academy of 
Sciences reported that Nova&#x27;s server create API does not strip internal 
scheduler hints. An authenticated user can bypass Placement resource 
claims and scheduling constraint enforcement, including availability 
zo…

---

## 41. 🟡 High Severity — Daytona: Cross-org IDOR in organization role update/delete — any org owner can rewrite or destroy another org's roles

**CVE:** `CVE-2026-54322` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-qxvm-pcfm-qc39>

> ### Summary
Daytona&#x27;s organization role update and delete endpoints authorized the caller as an owner of the organization named in the request path, but resolved and mutated the target role by its identifier alone, without verifying the role belonged to that organization. An authenticated user who owns any organization (organizations are self-service) could therefore modify the permissions of…

---

## 42. 🟡 High Severity — Caddy: Windows `file_server` path authorization bypass via encoded backslash

**CVE:** `CVE-2026-52844` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-qrp7-cvwr-j2c6>

> ### Summary

On Windows, Caddy `path` matchers treat `/private\secret.txt` as outside `/private/*`, but `file_server` later resolves the same request path as `private\secret.txt` on disk.

An unauthenticated remote client can request `/private%5csecret.txt` and bypass Caddy path-scoped auth/deny routes protecting `/private/*`.

### Details

The mismatch is between two Caddy code paths:

- `MatchPa…

---

## 43. 🟡 High Severity — Daytona: Public sandbox previews remain accessible for up to one hour after being made private

**CVE:** `CVE-2026-54321` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-ww63-pv5x-vfc8>

> ### Summary
Sandbox previews that were switched from public to private could remain reachable without authentication for a short period after the change, due to a cached visibility state that was not invalidated when the sandbox&#x27;s visibility changed.

### Impact
When a sandbox owner changed a preview from public to private, the preview proxy could continue serving unauthenticated requests to …

---

## 44. 🟡 High Severity — Traefik: HTTP/3 mTLS bypass via exact SNI TLSOptions lookup for wildcard and mixed-case hosts

**CVE:** `CVE-2026-53622` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-9cr8-q42q-g8m7>

> ## Summary

There is a critical vulnerability in Traefik&#x27;s HTTP/3 (QUIC) TLS configuration selection that allows unauthenticated clients to bypass router-specific mTLS enforcement. When HTTP/3 is enabled on an entrypoint, the TLS handshake selects the applicable TLS configuration through an exact, case-sensitive lookup on the SNI value, which fails to match wildcard host patterns (e.g., `*.ex…

---

## 45. 🟡 High Severity — Crawl4AI: SSRF via proxy settings in the Docker server bypasses the crawl-URL SSRF check

**CVE:** `CVE-2026-53755` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-6qhc-x826-342c>

> ### Summary

The Docker API server applied its SSRF destination check to the crawl target URL only, not to the proxy address. An unauthenticated request could supply a proxy pointing at an internal IP and route the browser through it, reaching internal services and cloud-metadata endpoints, while using a perfectly valid crawl URL. The Docker API is unauthenticated by default.

### Affected paths

…

---

## 46. 🟡 High Severity — Crawl4AI: SSRF filter bypass in Docker server via IPv6 transition forms (NAT64 / 6to4 / unspecified / v4-mapped)

**CVE:** `CVE-2026-53754` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-4qqr-vv2q-cmr5>

> ### Summary

The Docker API server&#x27;s SSRF protection (`validate_webhook_url` / `validate_url_destination` in `deploy/docker/utils.py`) used an explicit IPv4/IPv6 CIDR blocklist that missed several address families. An attacker could reach internal services and cloud metadata endpoints (e.g. `169.254.169.254`) despite the filter by encoding an internal IPv4 address inside an IPv6 transition fo…

---

## 47. 🟡 High Severity — LobeHub: Unauthenticated SSRF in `/webapi/proxy`

**CVE:** `CVE-2026-54157` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-xmwj-c75x-6346>

> ## Unauthenticated SSRF in /webapi/proxy allows anyone to proxy requests and inject cookies on lobehub.com

## Summary

The `/webapi/proxy` endpoint on app.lobehub.com accepts a URL in the POST body and fetches it server-side without any authentication. This is the same proxy code that was vulnerable in CVE-2024-32964, where `/api/proxy` was fixed by adding auth middleware. The `/webapi/proxy` rou…

---

## 48. 🟡 High Severity — Crawl4AI: AST Sandbox Escape via gi_frame.f_back Chain - Pre-Auth RCE in Docker API

**CVE:** `CVE-2026-53753` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-qxjp-w3pj-48m7>

> ### Summary

The `_safe_eval_expression()` function in the computed fields feature uses an AST validator that only blocks attributes starting with underscore. Python generator and frame object attributes (`gi_frame`, `f_back`, `f_builtins`) do NOT start with underscore, enabling a complete sandbox escape to achieve arbitrary code execution.

The attack requires no authentication (JWT disabled by d…

---

## 49. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
