# Zero Day Pulse

> **Generated:** 2026-06-17 14:48 UTC &nbsp;|&nbsp; **Total:** 42 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 19 &nbsp;|&nbsp; 🟡 High: 23 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** A path traversal vulnerability in SimpleHelp remote support software (versions ≤5.5.7) permits unauthenticated attackers to craft file paths that traverse directories, potentially leading to arbitrary file read or code execution.
- **Affected Products:** SimpleHelp Remote Support software versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true (patch released; see vendor advisory and SimpleHelp blog)
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors
- **Mitigation:** Update SimpleHelp to a version newer than 5.5.7 (or apply the vendor’s patch). Until patched, restrict remote access to trusted networks and monitor for suspicious activity.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — Malicious JetBrains Plugins Steal AI API Keys as Chrome Extensions Capture Chatbot Chats

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://thehackernews.com/2026/06/malicious-jetbrains-plugins-steal-ai.html>

> Cybersecurity researchers have flagged a &quot;coordinated malware campaign&quot; on the JetBrains Marketplace that has published no less than 15 malicious plugins capable of exfiltrating artificial intelligence (AI) provider keys.

&quot;Every plugin poses as an AI coding assistant built on DeepSeek and other large language models, offering chat, commit messages, code review, bug finding, and uni…

**Parallel AI Enrichment:**

- **Technical Details:** The plugins (shared codebase) capture API keys entered in plugin settings and immediately POST them in plaintext to an attacker‑controlled server (hardcoded IP 39.107.60[.]51) using an HTTP request authenticated with a static token; plugins may also return a server‑supplied API key to paying users so the operator can resell stolen credentials.
- **Affected Products:** JetBrains Marketplace IDE plugins: DeepSeek Junit Test (org.sm.yms.toolkit), DeepSeek Git Commit (com.json.simple.kit), DeepSeek FindBugs (org.bug.find.tools), DeepSeek AI Chat (org.translate.ai.simple), DeepSeek Dev AI (com.yy.test.ai.simple), DeepSeek AI Coding (com.dev.ai.toolkit), AI FindBugs (com.json.view.simple), AI Git Commitor (com.my.git.ai.kit), AI Coder Review (org.check.ai.ds), DeepSeek Coder AI (com.review.tool.code), AI Coder Assistant (org.code.assist.dev.tool), DeepSeek Code Review (com.coder.ai.dpt), CodeGPT AI Assistant (com.my.code.tools), DeepSeek AI Assist (ord.cp.code.ai.kit), Coding Simple Tool (com.dp.git.ai.tool)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Uninstall affected plugins immediately; revoke and rotate any AI provider keys entered into these plugins; search for plugin indicators (plugin IDs and C2 IP 39.107.60[.]51) and remove from developer machines; avoid pasting long‑lived secrets into unvetted plugins; use short‑lived or scoped keys and enforce billing alerts; monitor for unauthorized API usage and block traffic to the listed C2 IP.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when adversarial content on the web (or other sources) is ingested by AI agents (e.g., RAG systems, browser‑enabled models) and contains hidden or overt instructions that override or manipulate the agent’s intended prompt, enabling data exfiltration or undesired actions. Notable instances include in‑the‑wild IPI payloads disclosed by Forcepoint and a zero‑click IPI (GeminiJack) against Google Gemini reported by Noma Labs.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true — https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads, https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability
- **Patch Available:** false — https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections
- **Active Exploitation:** true — https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads, https://blog.google/security/prompt-injections-web/, https://securityweek.com/malicious-ai-prompt-injection-attacks-increasing-but-sophistication-still-low-google
- **Threat Actors:** None known
- **Mitigation:** Harden prompts, validate and filter web‑browsed content, use allowlists/denylists, model‑level safeguards and continuous monitoring; follow Google’s mitigation guidance.
- **Vendor Advisory:** https://blog.google/security/prompt-injections-web/

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) injects malicious instructions into data or tools consumed by an LLM (e.g., documents, web content, connectors). The LLM then follows those instructions while completing user queries, potentially enabling zero‑click attacks and agentic automation abuse.
- **Affected Products:** Google Workspace (including Workspace apps integrating Gemini), Gemini Enterprise (versions not specified)
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true — http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability
- **Patch Available:** true — http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html
- **Active Exploitation:** true — http://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability
- **Threat Actors:** None known
- **Mitigation:** Apply vendor guidance and layered defenses: restrict untrusted data sources, apply content filtering and sanitization, implement contextual grounding and instruction isolation, enable vendor‑provided Workspace/Gemini mitigations per advisory; monitor indicators of compromise and apply least privilege.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is where untrusted web content (including iframes or user‑generated content) influences an agent to perform unwanted actions (financial transactions, data exfiltration). Chrome defends via a separate high‑trust “User Alignment Critic” that vets planner actions without seeing untrusted content, origin gating restricting readable/writable origins per task, deterministic checks on model‑generated URLs, real‑time prompt‑injection classifiers, and logging/confirmations to place the user in the loop.
- **Affected Products:** Chrome (agentic browsing / Gemini integration)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true — http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses described by vendor: User Alignment Critic (veto actions), Agent Origin Sets (read‑only and read‑writable origin gating), user confirmations for sensitive actions, real‑time prompt‑injection detection, and keep Chrome updated (auto‑update). Follow VRP rules to report issues.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Google reports that Rust adoption in Android (first‑party and third‑party open‑source code across C, C++, Java, Kotlin, and Rust) has led to a sharp drop in memory‑safety vulnerabilities; 2025 data shows memory‑safety vulnerabilities fell below 20% of total vulnerabilities for the first time. The post attributes gains to replacing unsafe C/C++ with Rust, plus improved review/fuzzing and reduced rollback/review time for Rust changes.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** None known.
- **Mitigation:** Continue adopting memory-safe languages (Rust), increase fuzzing and code review, sandboxing components, and prefer Rust for new code to reduce memory-safety vulnerability density.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) embeds malicious instructions within external data sources (emails, documents, calendar invites, web content). AI agents retrieve or incorporate that external content into prompts or context, causing the model to follow adversarial instructions (e.g., exfiltrate data or perform unauthorized actions) via the retrieval/ingestion pathway rather than direct user prompt manipulation.
- **Affected Products:** Gemini, Gemini in Workspace apps
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply layered defenses — restrict retrieval scope, sanitize and provenance‑check external content, model‑level instruction filtering, context and prompt hardening, rate‑limiting and monitoring for anomalous retrievals, and deploy vendor guidance from Google’s layered defense strategy.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Actors target large backbone, provider edge (PE), and customer edge (CE) routers and modify routers to maintain persistent, long-term access; they leverage compromised devices and trusted connections to pivot into other networks.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** Patch availability unknown.
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon; OPERATOR PANDA; RedMike; UNC5807; GhostEmperor
- **Mitigation:** Harden and monitor edge and backbone routers, apply vendor advisories and mitigations from CISA; segment networks, restrict management plane access, enforce least privilege, rotate credentials, monitor for indicators of compromise.
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
- **Threat Actors:** GRU 85th GTsSS (Unit 26165) — APT28 (Russian GRU)
- **Mitigation:** Increase monitoring and threat hunting for known TTPs, implement recommended hardening and detection guidance from CISA advisory (see vendor advisory URL).
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Windows 10 (OS Build 26200.8655), Windows 11 (OS Build 26100.8655)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (https://thehackernews.com/2026/06/microsoft-defender-rogueplanet-zero-day.html)
- **Patch Available:** true (https://support.microsoft.com/en-us/topic/june-9-2026-kb5094126-os-builds-26200-8655-and-26100-8655-1a9bcba6-5f53-4075-8156-fe11ac631737)
- **Active Exploitation:** Active exploitation status unknown.
- **Threat Actors:** Threat actors unknown.
- **Mitigation:** Apply the Microsoft June 9, 2026 update (KB5094126) to affected Windows builds.
- **Vendor Advisory:** https://support.microsoft.com/en-us/topic/june-9-2026-kb5094126-os-builds-26200-8655-and-26100-8655-1a9bcba6-5f53-4075-8156-fe11ac631737

---

## 11. 🟠 Zero-Day — The Top 10 Attack Surface Exposures in 2026

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://thehackernews.com/2026/06/the-top-10-attack-surface-exposures-in.html>

> Breaches don&#x27;t always start with a zero-day. An exposed admin panel can get brute-forced, or credentials reused from a previous attack. But when a vulnerability does drop — like MongoBleed earlier this year, which let attackers pull credentials and session tokens from server memory without authentication — anything internet-facing is immediately at risk.

With time-to-exploit now down to a

---

## 12. 🟠 Zero-Day — CISA orders feds to patch max severity Joomla plugin flaw by Friday

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-max-severity-joomla-plugin-flaw-by-friday/>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has ordered federal agencies to patch a maximum-severity flaw in the Widget Factory Joomla Content Editor (JCE) plugin that is being actively exploited in the wild. [...]

---

## 13. 🟠 Zero-Day — Microsoft Working on Patch for ‘RoguePlanet’ Zero-Day

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://www.securityweek.com/microsoft-working-on-patch-for-rogueplanet-zero-day/>

> The public PoC code exploits a race condition in Microsoft Defender to spawn a command prompt with System privileges. The post Microsoft Working on Patch for ‘RoguePlanet’ Zero-Day appeared first on SecurityWeek .

---

## 14. 🟠 Zero-Day — Microsoft working on Defender patch for RoguePlanet zero-day

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://www.bleepingcomputer.com/news/microsoft/microsoft-working-on-defender-patch-for-rogueplanet-zero-day/>

> Microsoft confirmed that it&#x27;s working on a security patch for a Defender zero-day vulnerability named &quot;RoguePlanet,&quot; disclosed one week ago. [...]

---

## 15. 🟠 Zero-Day — CISA Warns of Actively Exploited Joomla JCE Flaw Allowing PHP Code Execution

**CVE:** `CVE-2026-48907` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://thehackernews.com/2026/06/cisa-warns-of-actively-exploited-joomla.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added a maximum-severity security flaw impacting Widget Factory Joomla Content Editor (JCE) to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

The vulnerability, tracked as CVE-2026-48907 (CVSS score: 10.0), is a case of improper access control that could facilitate arbitrary

---

## 16. 🟠 Zero-Day — Pi Agent: Potential XSS in HTML session exports via Markdown URL sanitization bypass

**CVE:** `CVE-2026-54326` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-7v5m-pr3q-6453>

> # Potential XSS in HTML session exports via Markdown URL handling

Pi HTML exports render session Markdown into a static HTML file. Affected versions did not consistently reject unsafe Markdown link and image URL schemes. In versions with scheme filtering, C0 control characters in the URL scheme could bypass the check because browsers normalize those characters before navigation.

## Impact

The r…

---

## 17. 🟠 Zero-Day — Malicious JetBrains Marketplace plugins steal AI API keys from developers

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://www.bleepingcomputer.com/news/security/malicious-jetbrains-marketplace-plugins-steal-ai-api-keys-from-developers/>

> At least 15 malicious plugins found on the JetBrains Marketplace were designed to steal AI API keys from developers. [...]

---

## 18. 🟠 Zero-Day — Google Vertex AI SDK Flaw Let Attackers Hijack Model Uploads via Bucket Squatting

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://thehackernews.com/2026/06/google-vertex-ai-sdk-flaw-let-attackers.html>

> A flaw in the Google Cloud Vertex AI SDK for Python let an attacker with no access to a victim&#x27;s project hijack the victim&#x27;s machine learning model upload and run code inside Google&#x27;s serving infrastructure.

Palo Alto Networks Unit 42, which found and reported the bug through Google&#x27;s bug bounty program, calls the technique &quot;Pickle in the Middle&quot; and said it saw no e…

---

## 19. 🟠 Zero-Day — LangChain: Path traversal and sandbox escape in LangChain file-search middleware and loaders

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-gr75-jv2w-4656>

> ## Summary

Several LangChain components that resolve filesystem paths or expand search patterns do not consistently confine the *resolved* path to the intended root directory. Affected behaviors include: a file-search agent middleware that validates a starting directory but not the search pattern or the resolved target of matched files, so glob patterns and symlinks can reach files outside the co…

---

## 20. 🟡 High Severity — Open WebUI: Redirect-Bypass SSRF in OAuth `_process_picture_url` (incomplete-fix sibling of CVE-2026-45401)

**CVE:** `CVE-2026-54008` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-226f-f24g-524w>

> ## Summary

`backend/open_webui/utils/oauth.py::_process_picture_url` (v0.9.5, lines 1435-1470) calls `validate_url(picture_url)` on the initial URL only, then invokes `aiohttp.ClientSession.get(picture_url, ...)` without `allow_redirects=False`. aiohttp&#x27;s default is `allow_redirects=True, max_redirects=10`; the function does not pass the project&#x27;s `AIOHTTP_CLIENT_ALLOW_REDIRECTS` env co…

---

## 21. 🟡 High Severity — NocoDB: Refresh Tokens Persist Through Password Recovery

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

## 22. 🟡 High Severity — vLLM: incomplete CVE-2026-22778 fix leaks PIL repr addresses via Anthropic router

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

## 23. 🟡 High Severity — Traefik: Kubernetes Gateway crossProviderNamespaces bypass allows HTTPRoute outside the allowlist to expose internal Traefik services

**CVE:** `CVE-2026-54761` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-3g6v-2r68-prfc>

> ## Summary

There is a high severity vulnerability in Traefik&#x27;s Kubernetes Gateway provider affecting the `crossProviderNamespaces` allowlist. For `HTTPRoute` rules that declare multiple (WRR) backendRefs, Traefik evaluates the allowlist against the target `backendRef.namespace` instead of the route&#x27;s own namespace. As a result, an `HTTPRoute` created in a namespace that is not allow-lis…

---

## 24. 🟡 High Severity — Pi Agent: Pi loads project-local extensions without approval

**CVE:** `CVE-2026-54325` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-mqxh-6gq7-558m>

> # Pi loads project-local extensions without approval

Pi before 0.79.0 loaded project-local configuration and resources from a repository&#x27;s `.pi` directory without first asking the user to trust that repository. This included project-local extensions, which are executable TypeScript or JavaScript modules loaded into the Pi process.

An attacker who controls a repository could place Pi-specifi…

---

## 25. 🟡 High Severity — Pi Agent: Predictable temporary extension install paths allow local privilege escalation on shared Linux hosts

**CVE:** `CVE-2026-54328` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://github.com/advisories/GHSA-jfgx-wxx8-mp94>

> # Predictable temporary extension install paths allow local privilege escalation on shared Linux hosts

Pi versions with temporary npm or git extension package installs used predictable paths under the operating system temporary directory. On Linux-based multi-user systems, a local attacker who can write to the shared temporary directory could prepare the expected package location before another u…

---

## 26. 🟡 High Severity — Gogs: Overwriting critical files results in a denial of service

**CVE:** `CVE-2026-52797` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-pm6v-2h4w-4rp2>

> **Vulnerability type:** Path Traversal
**Impact:** DoS
**Exploitation prerequisite:** authorized user
**Description:** As an authorized user, an intruder can dictate the value which is passed to the `git diff` command which, together with bypassing the filtering of the passed value, allows the user to bypass the target directory and write the result of the comparison to any arbitrary path.
**Resea…

---

## 27. 🟡 High Severity — n8n: SecurityScorecard Node Leaks API Token to User-Controlled Host

**CVE:** `CVE-2026-54304` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-rm2v-h48j-895m>

> ## Impact
An authenticated user with permission to create or modify workflows and access to a SecurityScorecard credential with limited allowed domains could configure the SecurityScorecard node&#x27;s report download operation to target an attacker-controlled URL. The node attached the SecurityScorecard API token to the outbound request, causing the credential to be sent to the attacker-controlle…

---

## 28. 🟡 High Severity — n8n: Cross-Tenant Credential Takeover via Dynamic Credentials EE Endpoints

**CVE:** `CVE-2026-54305` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-2j5h-858j-5mpf>

> ## Impact
Three EE endpoints used by the Dynamic Credentials feature accepted any authenticated n8n session without performing per-resource ownership or scope checks on the target workflow or credential. An authenticated user with no project membership or credential sharing relationship could enumerate credential identifiers, names, and types referenced by any private workflow in the instance, ini…

---

## 29. 🟡 High Severity — Daytona: Cross-org IDOR in organization role update/delete — any org owner can rewrite or destroy another org's roles

**CVE:** `CVE-2026-54322` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-qxvm-pcfm-qc39>

> ### Summary
Daytona&#x27;s organization role update and delete endpoints authorized the caller as an owner of the organization named in the request path, but resolved and mutated the target role by its identifier alone, without verifying the role belonged to that organization. An authenticated user who owns any organization (organizations are self-service) could therefore modify the permissions of…

---

## 30. 🟡 High Severity — Caddy: Windows `file_server` path authorization bypass via encoded backslash

**CVE:** `CVE-2026-52844` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-qrp7-cvwr-j2c6>

> ### Summary

On Windows, Caddy `path` matchers treat `/private\secret.txt` as outside `/private/*`, but `file_server` later resolves the same request path as `private\secret.txt` on disk.

An unauthenticated remote client can request `/private%5csecret.txt` and bypass Caddy path-scoped auth/deny routes protecting `/private/*`.

### Details

The mismatch is between two Caddy code paths:

- `MatchPa…

---

## 31. 🟡 High Severity — Daytona: Public sandbox previews remain accessible for up to one hour after being made private

**CVE:** `CVE-2026-54321` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-ww63-pv5x-vfc8>

> ### Summary
Sandbox previews that were switched from public to private could remain reachable without authentication for a short period after the change, due to a cached visibility state that was not invalidated when the sandbox&#x27;s visibility changed.

### Impact
When a sandbox owner changed a preview from public to private, the preview proxy could continue serving unauthenticated requests to …

---

## 32. 🟡 High Severity — Traefik: HTTP/3 mTLS bypass via exact SNI TLSOptions lookup for wildcard and mixed-case hosts

**CVE:** `CVE-2026-53622` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-9cr8-q42q-g8m7>

> ## Summary

There is a critical vulnerability in Traefik&#x27;s HTTP/3 (QUIC) TLS configuration selection that allows unauthenticated clients to bypass router-specific mTLS enforcement. When HTTP/3 is enabled on an entrypoint, the TLS handshake selects the applicable TLS configuration through an exact, case-sensitive lookup on the SNI value, which fails to match wildcard host patterns (e.g., `*.ex…

---

## 33. 🟡 High Severity — Crawl4AI: SSRF via proxy settings in the Docker server bypasses the crawl-URL SSRF check

**CVE:** `CVE-2026-53755` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-6qhc-x826-342c>

> ### Summary

The Docker API server applied its SSRF destination check to the crawl target URL only, not to the proxy address. An unauthenticated request could supply a proxy pointing at an internal IP and route the browser through it, reaching internal services and cloud-metadata endpoints, while using a perfectly valid crawl URL. The Docker API is unauthenticated by default.

### Affected paths

…

---

## 34. 🟡 High Severity — Crawl4AI: SSRF filter bypass in Docker server via IPv6 transition forms (NAT64 / 6to4 / unspecified / v4-mapped)

**CVE:** `CVE-2026-53754` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-4qqr-vv2q-cmr5>

> ### Summary

The Docker API server&#x27;s SSRF protection (`validate_webhook_url` / `validate_url_destination` in `deploy/docker/utils.py`) used an explicit IPv4/IPv6 CIDR blocklist that missed several address families. An attacker could reach internal services and cloud metadata endpoints (e.g. `169.254.169.254`) despite the filter by encoding an internal IPv4 address inside an IPv6 transition fo…

---

## 35. 🟡 High Severity — LobeHub: Unauthenticated SSRF in `/webapi/proxy`

**CVE:** `CVE-2026-54157` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-xmwj-c75x-6346>

> ## Unauthenticated SSRF in /webapi/proxy allows anyone to proxy requests and inject cookies on lobehub.com

## Summary

The `/webapi/proxy` endpoint on app.lobehub.com accepts a URL in the POST body and fetches it server-side without any authentication. This is the same proxy code that was vulnerable in CVE-2024-32964, where `/api/proxy` was fixed by adding auth middleware. The `/webapi/proxy` rou…

---

## 36. 🟡 High Severity — Crawl4AI: AST Sandbox Escape via gi_frame.f_back Chain - Pre-Auth RCE in Docker API

**CVE:** `CVE-2026-53753` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-qxjp-w3pj-48m7>

> ### Summary

The `_safe_eval_expression()` function in the computed fields feature uses an AST validator that only blocks attributes starting with underscore. Python generator and frame object attributes (`gi_frame`, `f_back`, `f_builtins`) do NOT start with underscore, enabling a complete sandbox escape to achieve arbitrary code execution.

The attack requires no authentication (JWT disabled by d…

---

## 37. 🟡 High Severity — Deno: Permission Bypass via Unicode Normalization Mismatch on macOS (APFS)

**CVE:** `CVE-2026-49401` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-8xpq-cjcf-3wh9>

> ## Summary

Deno&#x27;s permission system enforces filesystem and execution restrictions by
comparing the requested path against the path supplied to `--deny-read`,
`--deny-write`, `--deny-run`, or `--deny-ffi`. On macOS, that comparison was
done at the raw-byte level while the APFS filesystem treats different Unicode
spellings of the same name as the same file.

That means a program could reach a…

---

## 38. 🟡 High Severity — Deno: BYONM module resolution allows `package.json` main path traversal to bypass `--allow-read` restrictions

**CVE:** `CVE-2026-49406` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-968w-xfqw-vp9q>

> ## Summary

When Deno was run in BYONM mode (`nodeModulesDir: &quot;manual&quot;`), the module resolver did not validate that a package&#x27;s resolved entrypoint stayed within its `node_modules/&lt;pkg&gt;/` directory. A malicious `package.json` whose `main` field contained `..` segments was able to resolve to an arbitrary path on disk, and the resolver then read that file without consulting the …

---

## 39. 🟡 High Severity — n8n: Merge Node SQL Mode Prototype Pollution

**CVE:** `CVE-2026-54311` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-9c38-2mcm-q7f7>

> ## Impact
An authenticated user with permission to create or modify workflows could pollute the sandbox used by the Merge node&#x27;s SQL Query mode. Because the sandbox context was cached and reused across all workflow executions on the instance, prototype mutations introduced by one user&#x27;s workflow persist into subsequent Merge SQL executions belonging to other users or projects. This allow…

---

## 40. 🟡 High Severity — Langflow: Unauthenticated RCE in Shareable Playgrounds

**CVE:** `CVE-2026-48519` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-v5ff-9q35-q26f>

> ### Summary
The &quot;Shareable Playground&quot; (or &quot;Public Flows&quot; in code) contains a critical RCE vulnerability.
Simply sharing a flow exposes the deployment to RCE risk by authenticated users.

Tested on commit 2d67402b1dbaefcbce85a244d4a6cd5e4bda1cfe

### Details
Shareable Playground feature works by enabling the execution of workflows by unauthenticated users, by accessing a link.
…

---

## 41. 🟡 High Severity — Astro: XSS via Unescaped Attribute Names in Spread Props

**CVE:** `CVE-2026-54298` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-jrpj-wcv7-9fh9>

> ## Summary

The `spreadAttributes` function in Astro&#x27;s server-side rendering pipeline iterates over object keys and passes them directly to `addAttribute`, which interpolates the key into the HTML output without escaping. When a developer uses the spread syntax `{...props}` on an HTML element and the object keys come from an untrusted source (API, CMS, URL parameters), an attacker can inject …

---

## 42. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
