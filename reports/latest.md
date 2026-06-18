# Zero Day Pulse

> **Generated:** 2026-06-18 02:31 UTC &nbsp;|&nbsp; **Total:** 35 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 18 &nbsp;|&nbsp; 🟡 High: 17 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is a path traversal / directory traversal flaw that lets unauthenticated remote attackers request file paths outside the intended directory, enabling reading of arbitrary files on the server.
- **Affected Products:** SimpleHelp remote support software, versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof‑of‑concepts and exploit details have been reported (e.g., OffSec blog, FortiGuard report).
- **Patch Available:** Patch is available; vendor released fix for SimpleHelp versions 5.5.7 and earlier (see advisory URL).
- **Active Exploitation:** Confirmed active exploitation; CISA advisory reports ransomware actors exploiting CVE-2024-57727.
- **Threat Actors:** Ransomware actors (unspecified groups)
- **Mitigation:** Update SimpleHelp to the fixed version released by the vendor, restrict SimpleHelp services to trusted networks (e.g., VPN or firewall rules), disable internet‑facing instances, apply network segmentation and monitoring, and follow CISA advisory recommendations.
- **Vendor Advisory:** https://www.broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — Hostile states behind three-quarters of attacks on Britain's critical infrastructure, cyber chief warns

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Record by Recorded Future &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://therecord.media/britain-nation-state-cyberattacks-richard-horne-rusi>

> NCSC CEO Richard Horne warned that “kinetic targeting in any conflict tomorrow will be based on intelligence gathered today” and that nation-state adversaries were “prepositioning” throughout British critical infrastructure.

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit reported.
- **Patch Available:** No vendor patch — high-level threat assessment; patch not applicable.
- **Active Exploitation:** No confirmed discrete CVE‑based active exploitation reported; reporting describes ongoing nation‑state targeting/prepositioning of UK critical infrastructure.
- **Threat Actors:** None known
- **Mitigation:** Follow NCSC hardening guidance: network segmentation, multi-factor authentication, patching, least privilege, logging and threat hunting; if vendor-specific guidance needed, consult NCSC advisories.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — Microsoft Confirms RoguePlanet Defender Zero-Day, Says Patch is in Development

**CVE:** `CVE-2026-50656` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://thehackernews.com/2026/06/microsoft-confirms-rogueplanet-defender_02022423645.html>

> Microsoft has formally disclosed that it&#x27;s working to release a patch to address a Defender zero-day codenamed RoguePlanet.

The vulnerability has now been assigned the CVE identifier CVE-2026-50656 (CVSS score: 7.8), with the tech giant describing it as a privilege escalation flaw.

&quot;Microsoft is aware of an elevation of privilege in the Microsoft Malware Protection Engine in Microsoft …

**Parallel AI Enrichment:**

- **Technical Details:** A race‑condition (improper link resolution) in the Microsoft Malware Protection Engine within Microsoft Defender allows local privilege escalation to SYSTEM when successfully exploited.
- **Affected Products:** Microsoft Malware Protection Engine / Microsoft Defender on Windows 10 and Windows 11 (fully patched)
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC available (GitHub repository). Example: https://github.com/MSNightmare/RoguePlanet
- **Patch Available:** Patch is in development; no official patch URL published as of 2026-06-17.
- **Active Exploitation:** Yes — multiple sources report active exploitation in the wild (Microsoft confirmation and KEV listings referenced by prior research).
- **Threat Actors:** None known
- **Mitigation:** Apply Microsoft updates when published; until a patch is available, restrict local unprivileged user access, remove or limit local accounts, enable endpoint protection/EDR monitoring for unusual process escalation, and follow vendor guidance when released.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — Malicious JetBrains Plugins Steal AI API Keys as Chrome Extensions Capture Chatbot Chats

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://thehackernews.com/2026/06/malicious-jetbrains-plugins-steal-ai.html>

> Cybersecurity researchers have flagged a &quot;coordinated malware campaign&quot; on the JetBrains Marketplace that has published no less than 15 malicious plugins capable of exfiltrating artificial intelligence (AI) provider keys.

&quot;Every plugin poses as an AI coding assistant built on DeepSeek and other large language models, offering chat, commit messages, code review, bug finding, and uni…

**Parallel AI Enrichment:**

- **Technical Details:** The malicious JetBrains Marketplace plugins masquerade as AI coding assistants, collect user‑provided AI provider API keys, and exfiltrate those keys in plaintext via an unsecured HTTP request to a hard‑coded attacker IP address (39.107.60.51). The same codebase is reused across multiple plugins, and a paid tier can return a functional API key from the attacker server, enabling resale of stolen credentials.
- **Affected Products:** DeepSeek Junit Test (org.sm.yms.toolkit), DeepSeek Git Commit (com.json.simple.kit), DeepSeek FindBugs (org.bug.find.tools), DeepSeek AI Chat (org.translate.ai.simple), DeepSeek Dev AI (com.yy.test.ai.simple), DeepSeek AI Coding (com.dev.ai.toolkit), AI FindBugs (com.json.view.simple), AI Git Commitor (com.my.git.ai.kit), AI Coder Review (org.check.ai.ds), DeepSeek Coder AI (com.review.tool.code), AI Coder Assistant (org.code.assist.dev.tool), DeepSeek Code Review (com.coder.ai.dpt), CodeGPT AI Assistant (com.my.code.tools), DeepSeek AI Assist (ord.cp.code.ai.kit), Coding Simple Tool (com.dp.git.ai.tool)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit reported.
- **Patch Available:** No official JetBrains patch or advisory located as of 2026-06-18; check JetBrains Marketplace and JetBrains security advisories for updates.
- **Active Exploitation:** Confirmed active exploitation reported since ~October 2025; malicious plugins are publicly available on the JetBrains Marketplace and have been observed stealing AI API keys.
- **Threat Actors:** None known
- **Mitigation:** Immediately uninstall suspicious JetBrains AI plugins; assume any API key entered is compromised and rotate/revoke keys; audit developer environments for installed plugins and remove untrusted ones; monitor outbound traffic for connections to 39.107.60.51; enforce plugin installation policies to allow only vetted sources; follow any future JetBrains guidance.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when adversarial content hosted externally (webpages, documents, calendar invites, comments) is incorporated as context by an AI system (RAG, agents, CLI tools), causing the model or agent to follow attacker‑supplied instructions or reveal/confuse data. Vectors include hidden page elements, crafted web pages, shared documents/calendars, and comment systems that are ingested by agents.
- **Affected Products:** Microsoft Copilot Studio (CVE-2026-21520), Google Gemini (>=1.3)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Proof‑of‑concepts published (Forcepoint 10 IPI payloads, Noma Labs GeminiJack).
- **Patch Available:** No universal patch; product‑specific fixes exist (e.g., CVE‑2025‑54131 fixed in version 1.3, Google Gemini patch).
- **Active Exploitation:** Confirmed researcher‑demonstrated in‑the‑wild IPI payloads; Google and other security teams detected real‑world attempts.
- **Threat Actors:** None known
- **Mitigation:** Use strict input/output sanitization, enforce content provenance and allow‑list filtering for external web content, validate RAG sources, sandbox agentic actions, reduce automatic execution of web‑derived instructions, and apply vendor hardening guidance from Google and Forcepoint.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) in RAG pipelines: attacker plants malicious instructions in accessible Workspace content (Docs, Calendar, Gmail). When RAG retrieval includes poisoned content, Gemini treats embedded instructions as executable, enabling the model to search across datasources and exfiltrate results (e.g., via crafted img tag making external HTTP request). This is an architectural/agentic exploitation rather than a traditional code bug.
- **Affected Products:** Google Gemini Enterprise, Vertex AI Search
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit has been published.
- **Patch Available:** Google deployed updates separating Vertex AI Search from Gemini Enterprise and made RAG processing changes; no discrete patch binary was released.
- **Active Exploitation:** Confirmed active exploitation reported by Noma Labs (GeminiJack) and validated by Google.
- **Threat Actors:** None known
- **Mitigation:** Google implemented layered mitigations: deterministic defenses (user confirmation, URL sanitization, tool‑chaining policies governed by a Policy Engine), ML/LLM‑based defenses (synthetic‑data‑driven retraining and prompt‑engineering), model hardening for Gemini, and architectural separation (Vertex AI Search separated from Gemini Enterprise). Organizations should restrict RAG‑accessible datasources, apply least‑privilege configurations, enable Google’s URL sanitization and user‑confirmation controls, and follow Google AI VRP and red‑team guidance.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** An indirect prompt injection delivered via web content can chain into an agentic browsing capability, causing the agent to execute attacker‑provided instructions or perform unauthorized actions; the specific vulnerability (CVE‑2025‑54131) can be triggered when such indirect prompt injection is chained to the vulnerable component.
- **Affected Products:** Google Chrome version 1.3
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** None known
- **Patch Available:** Yes — mitigated in version 1.3 (see NVD CVE‑2025‑54131 entry).
- **Active Exploitation:** Reports of related indirect prompt‑injection activity have been published, but no publicly attributed, confirmed exploitation of CVE‑2025‑54131 by known threat actors has been reported.
- **Threat Actors:** None known
- **Mitigation:** Restrict agentic browsing origin access, apply layered defenses for prompt‑injection detection and origin/permission restrictions; follow Google’s recommended architecture and hardening for agentic capabilities.
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic/

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow in the Android CrabbyAVIF component could overwrite adjacent memory, but Android’s Scudo hardened allocator placed guard pages around secondary allocations, making the overflow non‑exploitable.
- **Affected Products:** Android platform – CrabbyAVIF component
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit or PoC is known.
- **Patch Available:** https://android.googlesource.com/platform/external/rust/crabbyavif/+/5262cd9befecb4f8865925c23eb543f19967e050
- **Active Exploitation:** No confirmed active exploitation in the wild has been reported.
- **Threat Actors:** None known
- **Mitigation:** Scudo hardened allocator placed guard pages around secondary allocations, making the linear buffer overflow non‑exploitable; additional unsafe‑Rust review and training were added.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injections embed malicious instructions in external data sources (emails, files, calendar invites) which, when ingested by LLM‑based assistants, can cause data exfiltration or undesired actions. Google mitigates these vectors with adversarial training, content‑classifier models, prompt sanitization, URL redaction, and human‑in‑the‑loop confirmations.
- **Affected Products:** Gemini (including Gemini in Workspace and the Gemini app), Google Workspace integrations
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** None reported
- **Patch Available:** No discrete patch available; mitigation is achieved via model hardening and platform defenses as described in the advisory.
- **Active Exploitation:** Advisory does not report confirmed active exploitation in the wild.
- **Threat Actors:** None known
- **Mitigation:** Implement content‑injection classifiers, enable security‑thought reinforcement, apply markdown sanitization and suspicious URL redaction, require user confirmation for risky actions, and provide end‑user security notifications.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors compromise routers by altering firmware or configuration to establish persistent footholds, then leverage trusted links and compromised devices to move laterally across network segments.
- **Affected Products:** Backbone routers, Provider Edge routers, Customer Edge routers
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept or weaponized exploit known.
- **Patch Available:** No official patch currently available.
- **Active Exploitation:** Active exploitation reported; Chinese state‑sponsored groups are currently targeting routers in critical infrastructure worldwide.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Update router firmware to the latest version, change all default passwords, segment critical network zones, monitor router configuration changes, and simulate the threat to validate defenses.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

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

## 19. 🟡 High Severity — Avo: Missing Authorization in Avo Association Attach Endpoint Allows Unauthorized Relationship Manipulation and Privilege Escalation

**CVE:** `CVE-2026-55518` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-8fq9-273g-6mrg>

> ## Summary

A critical missing authorization flaw exists in Avo&#x27;s association attach workflow. The UI and `GET /resources/:resource/:id/:related/new` path can check `attach_&lt;association&gt;?`, but the actual write endpoint, `POST /resources/:resource/:id/:related`, does not run the same authorization check before mutating the association.

As a result, an authenticated low-privileged Avo u…

---

## 20. 🟡 High Severity — HAPI FHIR: XXE in XsltUtilities.saxonTransform via unhardened Saxon TransformerFactory

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

## 21. 🟡 High Severity — LangChain4j: SQL injection via metadata filters in langchain4j-mariadb and langchain4j-pgvector

**CVE:** `CVE-2026-55405` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-2mfg-cc43-9pcj>

> ### Summary
The MariaDB and pgvector embedding stores build metadata-filter SQL by string-concatenating
filter **keys** (and, in MariaDB, string **values**) directly into the query without adequate
escaping. A crafted metadata key in `EmbeddingSearchRequest.filter()` can break out of its SQL
context and inject arbitrary SQL into the statements executed by the stores&#x27; search and
`removeAll(Fil…

---

## 22. 🟡 High Severity — Capsule: Incomplete fix of CVE-2026-30963: singular/plural typo leaves namespaces/finalize unprotected

**CVE:** `CVE-2026-55636` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-gwxr-7h77-7777>

> ### Summary
Capsule v0.13.2 webhook rules contain `namespace/finalize` (singular) instead of `namespaces/finalize` (plural). K8s requires plural. The finalize defense from CVE-2026-30963 fix is absent.

### Details
PUT to `/api/v1/namespaces/&lt;ns&gt;/finalize` has resource=namespaces (plural). The singular rule never matches. `matchPolicy: Equivalent` does not compensate.

### PoC
Confirmed on k…

---

## 23. 🟡 High Severity — webpack-dev-server vulnerable to HMR WebSocket interception via permissive user proxies

**CVE:** `CVE-2026-9595` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-mx8g-39q3-5c79>

> ### Impact

When a user-configured proxy on `webpack-dev-server` has a broad context (e.g. `/`) and `ws: true`, it also intercepts the dev server&#x27;s own HMR WebSocket and forwards it to the proxy target. This leaks the browser&#x27;s cookies and `Origin` header to the backend, bypasses the dev server&#x27;s Host/Origin validation, and corrupts the HMR socket (both HMR and the proxy end up writ…

---

## 24. 🟡 High Severity — Gitea: API Fork Missing CanCreateOrgRepo Check Allows Org Secret Exfiltration

**CVE:** `CVE-2026-22555` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-fhx7-m96w-mv29>

> ## Summary

The API endpoint `POST /api/v1/repos/{owner}/{repo}/forks` only checks `IsOrgMember()` when a user forks a repository into an organization, but does not check `CanCreateOrgRepo()`. The web UI fork handler correctly checks both. This allows a read-only organization member — in a team with `can_create_org_repo=false` — to create repositories in the organization namespace via the API. The…

---

## 25. 🟡 High Severity — Daytona: Cross-tenant data leak in notification WebSocket gateway via unverified organizationId join

**CVE:** `CVE-2026-54324` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-qwxf-2m7m-2m3x>

> ### Summary
A cross-tenant authorization flaw in Daytona&#x27;s notification WebSocket gateway allowed any authenticated user to subscribe to another organization&#x27;s realtime notification channel and passively receive that organization&#x27;s events.

### Impact
The notification gateway&#x27;s JWT handshake joined a client-supplied organization identifier to the corresponding notification room…

---

## 26. 🟡 High Severity — Open WebUI: SSRF Protection Bypass in Playwright Web Loader via HTTP Redirects

**CVE:** `CVE-2026-54018` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-jrfp-m64g-pcwv>

> ### Summary
The SafePlaywrightURLLoader implements a validate_url function to prevent SSRF attacks by checking the IP address of the user-provided URL. However, this validation is performed only on the initial URL.

Since Playwright automatically follows HTTP redirects (301/302) by default, an attacker can bypass the validation by providing a safe URL that redirects to a restricted internal networ…

---

## 27. 🟡 High Severity — Open WebUI: Path traversal / SSRF in terminal server proxy via encoded path traversal

**CVE:** `CVE-2026-54017` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-r2wg-2mcr-66rv>

> ### Summary

The terminal-server reverse proxy in `backend/open_webui/routers/terminals.py` does not fully confine the user-controlled `path` segment before forwarding it to an admin-configured terminal server. An authenticated user who has been granted access to a terminal server can craft `path` values containing encoded `../` traversal sequences that escape the intended path (or policy) scope o…

---

## 28. 🟡 High Severity — OpenClaw: MCP Streamable HTTP redirects could forward configured custom headers to another origin

**CVE:** `CVE-2026-53840` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-rjxq-qqhf-8hwh>

> ### Summary

OpenClaw supports remote MCP Streamable HTTP servers with operator-configured custom headers. In affected releases, those headers could be forwarded when the MCP endpoint responded with a cross-origin redirect.

This issue is limited to configured MCP Streamable HTTP servers that use custom headers. It does not expose unrelated OpenClaw credentials.

### Affected configurations

This …

---

## 29. 🟡 High Severity — Open WebUI: Redirect-Bypass SSRF in OAuth `_process_picture_url` (incomplete-fix sibling of CVE-2026-45401)

**CVE:** `CVE-2026-54008` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-226f-f24g-524w>

> ## Summary

`backend/open_webui/utils/oauth.py::_process_picture_url` (v0.9.5, lines 1435-1470) calls `validate_url(picture_url)` on the initial URL only, then invokes `aiohttp.ClientSession.get(picture_url, ...)` without `allow_redirects=False`. aiohttp&#x27;s default is `allow_redirects=True, max_redirects=10`; the function does not pass the project&#x27;s `AIOHTTP_CLIENT_ALLOW_REDIRECTS` env co…

---

## 30. 🟡 High Severity — NocoDB: Refresh Tokens Persist Through Password Recovery

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

## 31. 🟡 High Severity — vLLM: incomplete CVE-2026-22778 fix leaks PIL repr addresses via Anthropic router

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

## 32. 🟡 High Severity — Traefik: Kubernetes Gateway crossProviderNamespaces bypass allows HTTPRoute outside the allowlist to expose internal Traefik services

**CVE:** `CVE-2026-54761` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-3g6v-2r68-prfc>

> ## Summary

There is a high severity vulnerability in Traefik&#x27;s Kubernetes Gateway provider affecting the `crossProviderNamespaces` allowlist. For `HTTPRoute` rules that declare multiple (WRR) backendRefs, Traefik evaluates the allowlist against the target `backendRef.namespace` instead of the route&#x27;s own namespace. As a result, an `HTTPRoute` created in a namespace that is not allow-lis…

---

## 33. 🟡 High Severity — Pi Agent: Pi loads project-local extensions without approval

**CVE:** `CVE-2026-54325` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-mqxh-6gq7-558m>

> # Pi loads project-local extensions without approval

Pi before 0.79.0 loaded project-local configuration and resources from a repository&#x27;s `.pi` directory without first asking the user to trust that repository. This included project-local extensions, which are executable TypeScript or JavaScript modules loaded into the Pi process.

An attacker who controls a repository could place Pi-specifi…

---

## 34. 🟡 High Severity — Pi Agent: Predictable temporary extension install paths allow local privilege escalation on shared Linux hosts

**CVE:** `CVE-2026-54328` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-jfgx-wxx8-mp94>

> # Predictable temporary extension install paths allow local privilege escalation on shared Linux hosts

Pi versions with temporary npm or git extension package installs used predictable paths under the operating system temporary directory. On Linux-based multi-user systems, a local attacker who can write to the shared temporary directory could prepare the expected package location before another u…

---

## 35. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
