# Zero Day Pulse

> **Generated:** 2026-06-17 10:25 UTC &nbsp;|&nbsp; **Total:** 42 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 19 &nbsp;|&nbsp; 🟡 High: 23 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2024-57727 is a path traversal vulnerability in SimpleHelp RMM that lets unauthenticated attackers craft requests to traverse directories and read sensitive files.
- **Affected Products:** SimpleHelp Remote Monitoring and Management (RMM) version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept or exploit is known at this time.
- **Patch Available:** No official vendor patch has been released yet.
- **Active Exploitation:** Yes, active exploitation by ransomware actors has been reported.
- **Threat Actors:** Ransomware actors (unspecified)
- **Mitigation:** Apply any future patches when released and follow CISA’s recommended mitigation guidance, such as restricting access to the SimpleHelp service and monitoring for suspicious activity.
- **Vendor Advisory:** https://www.broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — Malicious JetBrains Plugins Steal AI API Keys as Chrome Extensions Capture Chatbot Chats

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://thehackernews.com/2026/06/malicious-jetbrains-plugins-steal-ai.html>

> Cybersecurity researchers have flagged a &quot;coordinated malware campaign&quot; on the JetBrains Marketplace that has published no less than 15 malicious plugins capable of exfiltrating artificial intelligence (AI) provider keys.

&quot;Every plugin poses as an AI coding assistant built on DeepSeek and other large language models, offering chat, commit messages, code review, bug finding, and uni…

**Parallel AI Enrichment:**

- **Technical Details:** Malicious JetBrains Marketplace plugins (~15) pose as AI assistants. When a user enters an API key and clicks Apply, the plugin's settings handler calls a save() routine that sends the key in plaintext over HTTP to attacker‑controlled C2 (hardcoded IP 39.107.60.51) authenticated by a static token; plugins may also return attacker‑supplied working API keys to paying users.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit found; tooling observed in plugins exfiltrating keys (malicious plugin code is the exploit).
- **Patch Available:** Patch not reported; no vendor patch/advisory found as of 2026-06-17.
- **Active Exploitation:** Confirmed active exploitation: plugins harvested API keys in the wild since Oct 2025; reported by Aikido Security and The Hacker News.
- **Threat Actors:** None known
- **Mitigation:** Uninstall identified plugins; revoke/rotate any API keys entered into these plugins; do not paste long‑lived secrets into unvetted plugins; block egress to 39.107.60.51; review JetBrains Marketplace accounts listed by Aikido and remove/uninstall listed plugin IDs; monitor billing/usage for stolen API key abuse; use short‑lived keys or organization‑scoped credentials and enforce least privilege.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) happens when AI systems retrieve externally supplied content (web pages, documents, emails) that embeds hidden instructions. When the retrieved content is fed into a retrieval‑augmented generation or agentic workflow, the embedded instructions are treated as legitimate prompts, enabling actions such as data exfiltration, instruction overriding, or command execution. The GeminiJack example demonstrated a zero‑click attack where malicious markup in a shared Google Doc caused Gemini Enterprise to exfiltrate corporate data.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof‑of‑concept exploits described in academic paper and security research write‑ups (see citations).
- **Patch Available:** Updates deployed by Google for Gemini Enterprise and Vertex AI Search; no single patch URL available.
- **Active Exploitation:** Confirmed active exploitation reported in Forcepoint X‑Labs, Infosecurity Magazine, HackRead, and Google Security Blog.
- **Threat Actors:** None known
- **Mitigation:** Mitigations include content filtering, coarse‑to‑fine scanning to reduce false positives, RAG pipeline hardening, separation of services (e.g., Vertex AI Search from Gemini Enterprise), and vendor‑issued updates for affected Google products.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection injects malicious instructions into data, tools, or document content accessed by the LLM, corrupting its reasoning and causing it to perform unauthorized actions such as bypassing calendar permissions or exfiltrating data across documents.
- **Affected Products:** Google Workspace with Gemini, Gemini Advanced, Gemini in Workspace, Google Gemini CLI Action, Docker Ask Gordon AI (beta), Docker CLI, Docker Desktop
- **CVSS Score:** -9999.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes – public PoC descriptions exist, including a calendar authorization bypass, cross‑document data exfiltration, a paid bug bounty disclosure, and GitHub comment injection.
- **Patch Available:** No traditional patch for the IPI issue; mitigation is performed via continuous defense enhancements. For the related Docker “Dockerdash” issue, upgrade to Docker Desktop 4.50.0 or later.
- **Active Exploitation:** No confirmed widespread active exploitation; only observations of experimentation and increased detections.
- **Threat Actors:** None known
- **Mitigation:** Implement Google’s layered defense approach (deterministic filters, ML‑based detection, LLM‑based hardening) and continuously update AI applications. For Docker’s related vulnerability, upgrade to Docker Desktop 4.50.0 or later.
- **Vendor Advisory:** http://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The primary new threat is "indirect prompt injection," where malicious page content injects or influences prompts supplied to agentic AI in the browser, causing unsafe actions or data exfiltration. Google describes layered defenses to limit origin access, detect and block prompt injections, and place supervisory/guardrail agents between web content and the agentic model.
- **Affected Products:** Affected products unavailable
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** No public PoC or weaponized exploit reported (Exploit unavailable)
- **Patch Available:** Yes — Google announced new layered defenses and architectural changes (vendor advisory URL above).
- **Active Exploitation:** No confirmed active exploitation in the wild reported in the advisory or referenced coverage
- **Threat Actors:** None known
- **Mitigation:** Use Google’s mitigations (layered defenses, origin restrictions, supervisory agent), keep Chrome updated to receive the security changes, avoid visiting untrusted sites while using agentic features, and disable agentic/automatic browsing features until patched. If vendor guidance unavailable, treat agentic browsing as high‑risk and restrict it.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Memory-safety vulnerability in CrabbyAVIF (AVIF image handling) leading to out-of-bounds/memory-corruption in native image decoding components.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit reported.
- **Patch Available:** See vendor advisory for Google-released fixes and mitigation guidance: http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html
- **Active Exploitation:** None known
- **Threat Actors:** None known
- **Mitigation:** Apply vendor patches/Android security updates as published in the vendor advisory; disable or sandbox AVIF decoding where possible until patched.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection is an attack where hidden malicious instructions are embedded in external data sources (emails, documents, calendar invites, web pages) and are ingested by an AI system, causing it to exfiltrate data or perform unauthorized actions; Google describes mitigations implemented in Gemini and Workspace to detect and block such payloads and limit model capabilities when processing untrusted content.
- **Affected Products:** Google Gemini, Gemini in Workspace apps
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC referenced in vendor advisory.
- **Patch Available:** Patch unavailable; mitigations described in vendor advisory: https://blog.google/security/mitigating-prompt-injection-attacks/
- **Active Exploitation:** No confirmed active exploitation reported in the vendor advisory.
- **Threat Actors:** None known
- **Mitigation:** Layered defense strategy described by Google: content provenance signals, origin restrictions, input/output filtering and sanitization, principle‑of‑least‑privilege for model actions, restricting access to sensitive connectors, and developer guidance for treating external content as untrusted.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Adversaries target large backbone routers and provider edge (PE) and customer edge (CE) routers, leveraging compromised devices and trusted connections to pivot; they modify routers to maintain persistent, long‑term access to networks.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public PoC or weaponized exploit: None known.
- **Patch Available:** No official vendor patch specified in the advisory; no single vendor patch applies because this advisory describes state‑sponsored compromises of network infrastructure rather than a single CVE. (No patch URL available.)
- **Active Exploitation:** Confirmed active exploitation reported — CISA advisory AA25-239A and supporting reporting describe persistent, long‑term compromises of telecommunications, government, transportation, lodging, and military infrastructure networks.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Practical mitigations from the advisory: segment and isolate critical infrastructure networks; restrict access to network management interfaces; enforce strong credentials and MFA for administrative access; apply vendor‑recommended updates and hardening for network devices where available; monitor for abnormal router configuration changes and unusual routing/traffic; implement comprehensive logging, network device integrity checks, and incident response plans; apply least‑privilege access and multi‑factor authentication for trusted connections.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Actors exploit internet‑facing infrastructure (corporate VPNs, public‑facing apps) via public vulnerabilities and SQL injection, and leverage the WinRAR CVE‑2023‑38831 vulnerability to achieve arbitrary code execution when viewing archive files. Post‑compromise activity includes use of living‑off‑the‑land tools such as Impacket, PsExec, RDP, and NTDS.dit dumping.
- **Affected Products:** WinRAR (CVE-2023-38831), Roundcube Webmail (CVE-2020-35730, CVE-2020-12641); also mentions IP cameras and various internet‑facing infrastructure.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit URL unavailable.
- **Patch Available:** Vendor patches not referenced as fixes for a single vulnerability; advisory recommends applying vendor/firmware updates where available.
- **Active Exploitation:** Confirmed. The advisory documents exploitation of public‑facing infrastructure and specific CVEs by GRU unit 26165.
- **Threat Actors:** GRU unit 26165 (tracked as APT28 / Fancy Bear / Forest Blizzard / Blue Delta).
- **Mitigation:** Employ appropriate network segmentation and Zero Trust principles; restrict lateral access; enable EDR and monitor Windows logs; apply security patches and firmware updates to all IP cameras; disable unnecessary remote access; use VPN with MFA for management; enable Windows attack‑surface reduction rules and application allowlisting.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Windows 10 (OS Build 26200.8655), Windows 11 (OS Build 26100.8655), other Microsoft products
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof‑of‑concept reported; no definitive public exploit repository URL available.
- **Patch Available:** Yes — Microsoft June 2026 Patch Tuesday updates (KB5094126).
- **Active Exploitation:** Confirmed active exploitation reported for the RoguePlanet zero‑day on Windows 10/11 with June 2026 updates; sources include CrowdStrike, The Hacker News, BleepingComputer, SecurityWeek.
- **Threat Actors:** None known
- **Mitigation:** Apply June 2026 Patch Tuesday updates (KB5094126); enable automatic updates, enable tamper protection, enable endpoint protection monitoring.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟠 Zero-Day — CISA orders feds to patch max severity Joomla plugin flaw by Friday

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-max-severity-joomla-plugin-flaw-by-friday/>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has ordered federal agencies to patch a maximum-severity flaw in the Widget Factory Joomla Content Editor (JCE) plugin that is being actively exploited in the wild. [...]

---

## 12. 🟠 Zero-Day — Microsoft Working on Patch for ‘RoguePlanet’ Zero-Day

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://www.securityweek.com/microsoft-working-on-patch-for-rogueplanet-zero-day/>

> The public PoC code exploits a race condition in Microsoft Defender to spawn a command prompt with System privileges. The post Microsoft Working on Patch for ‘RoguePlanet’ Zero-Day appeared first on SecurityWeek .

---

## 13. 🟠 Zero-Day — Microsoft working on Defender patch for RoguePlanet zero-day

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://www.bleepingcomputer.com/news/microsoft/microsoft-working-on-defender-patch-for-rogueplanet-zero-day/>

> Microsoft confirmed that it&#x27;s working on a security patch for a Defender zero-day vulnerability named &quot;RoguePlanet,&quot; disclosed one week ago. [...]

---

## 14. 🟠 Zero-Day — CISA Warns of Actively Exploited Joomla JCE Flaw Allowing PHP Code Execution

**CVE:** `CVE-2026-48907` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-17
**Reference:** <https://thehackernews.com/2026/06/cisa-warns-of-actively-exploited-joomla.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added a maximum-severity security flaw impacting Widget Factory Joomla Content Editor (JCE) to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

The vulnerability, tracked as CVE-2026-48907 (CVSS score: 10.0), is a case of improper access control that could facilitate arbitrary

---

## 15. 🟠 Zero-Day — Pi Agent: Potential XSS in HTML session exports via Markdown URL sanitization bypass

**CVE:** `CVE-2026-54326` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-7v5m-pr3q-6453>

> # Potential XSS in HTML session exports via Markdown URL handling

Pi HTML exports render session Markdown into a static HTML file. Affected versions did not consistently reject unsafe Markdown link and image URL schemes. In versions with scheme filtering, C0 control characters in the URL scheme could bypass the check because browsers normalize those characters before navigation.

## Impact

The r…

---

## 16. 🟠 Zero-Day — Malicious JetBrains Marketplace plugins steal AI API keys from developers

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://www.bleepingcomputer.com/news/security/malicious-jetbrains-marketplace-plugins-steal-ai-api-keys-from-developers/>

> At least 15 malicious plugins found on the JetBrains Marketplace were designed to steal AI API keys from developers. [...]

---

## 17. 🟠 Zero-Day — Google Vertex AI SDK Flaw Let Attackers Hijack Model Uploads via Bucket Squatting

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://thehackernews.com/2026/06/google-vertex-ai-sdk-flaw-let-attackers.html>

> A flaw in the Google Cloud Vertex AI SDK for Python let an attacker with no access to a victim&#x27;s project hijack the victim&#x27;s machine learning model upload and run code inside Google&#x27;s serving infrastructure.

Palo Alto Networks Unit 42, which found and reported the bug through Google&#x27;s bug bounty program, calls the technique &quot;Pickle in the Middle&quot; and said it saw no e…

---

## 18. 🟠 Zero-Day — LangChain: Path traversal and sandbox escape in LangChain file-search middleware and loaders

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-gr75-jv2w-4656>

> ## Summary

Several LangChain components that resolve filesystem paths or expand search patterns do not consistently confine the *resolved* path to the intended root directory. Affected behaviors include: a file-search agent middleware that validates a starting directory but not the search pattern or the resolved target of matched files, so glob patterns and symlinks can reach files outside the co…

---

## 19. 🟠 Zero-Day — CISA warns of another cPanel plugin flaw exploited in attacks

**CVE:** `CVE-2026-54420` &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-warns-of-another-actively-exploited-cpanel-plugin-flaw/>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has given U.S. government agencies three days to secure their servers against an actively exploited vulnerability (CVE-2026-54420) in the LiteSpeed cPanel user-end plugin. [...]

---

## 20. 🟡 High Severity — Gogs: Overwriting critical files results in a denial of service

**CVE:** `CVE-2026-52797` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-pm6v-2h4w-4rp2>

> **Vulnerability type:** Path Traversal
**Impact:** DoS
**Exploitation prerequisite:** authorized user
**Description:** As an authorized user, an intruder can dictate the value which is passed to the `git diff` command which, together with bypassing the filtering of the passed value, allows the user to bypass the target directory and write the result of the comparison to any arbitrary path.
**Resea…

---

## 21. 🟡 High Severity — n8n: SecurityScorecard Node Leaks API Token to User-Controlled Host

**CVE:** `CVE-2026-54304` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-rm2v-h48j-895m>

> ## Impact
An authenticated user with permission to create or modify workflows and access to a SecurityScorecard credential with limited allowed domains could configure the SecurityScorecard node&#x27;s report download operation to target an attacker-controlled URL. The node attached the SecurityScorecard API token to the outbound request, causing the credential to be sent to the attacker-controlle…

---

## 22. 🟡 High Severity — n8n: Cross-Tenant Credential Takeover via Dynamic Credentials EE Endpoints

**CVE:** `CVE-2026-54305` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-2j5h-858j-5mpf>

> ## Impact
Three EE endpoints used by the Dynamic Credentials feature accepted any authenticated n8n session without performing per-resource ownership or scope checks on the target workflow or credential. An authenticated user with no project membership or credential sharing relationship could enumerate credential identifiers, names, and types referenced by any private workflow in the instance, ini…

---

## 23. 🟡 High Severity — Daytona: Cross-org IDOR in organization role update/delete — any org owner can rewrite or destroy another org's roles

**CVE:** `CVE-2026-54322` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-qxvm-pcfm-qc39>

> ### Summary
Daytona&#x27;s organization role update and delete endpoints authorized the caller as an owner of the organization named in the request path, but resolved and mutated the target role by its identifier alone, without verifying the role belonged to that organization. An authenticated user who owns any organization (organizations are self-service) could therefore modify the permissions of…

---

## 24. 🟡 High Severity — Caddy: Windows `file_server` path authorization bypass via encoded backslash

**CVE:** `CVE-2026-52844` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-qrp7-cvwr-j2c6>

> ### Summary

On Windows, Caddy `path` matchers treat `/private\secret.txt` as outside `/private/*`, but `file_server` later resolves the same request path as `private\secret.txt` on disk.

An unauthenticated remote client can request `/private%5csecret.txt` and bypass Caddy path-scoped auth/deny routes protecting `/private/*`.

### Details

The mismatch is between two Caddy code paths:

- `MatchPa…

---

## 25. 🟡 High Severity — Daytona: Public sandbox previews remain accessible for up to one hour after being made private

**CVE:** `CVE-2026-54321` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-ww63-pv5x-vfc8>

> ### Summary
Sandbox previews that were switched from public to private could remain reachable without authentication for a short period after the change, due to a cached visibility state that was not invalidated when the sandbox&#x27;s visibility changed.

### Impact
When a sandbox owner changed a preview from public to private, the preview proxy could continue serving unauthenticated requests to …

---

## 26. 🟡 High Severity — Traefik: HTTP/3 mTLS bypass via exact SNI TLSOptions lookup for wildcard and mixed-case hosts

**CVE:** `CVE-2026-53622` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-9cr8-q42q-g8m7>

> ## Summary

There is a critical vulnerability in Traefik&#x27;s HTTP/3 (QUIC) TLS configuration selection that allows unauthenticated clients to bypass router-specific mTLS enforcement. When HTTP/3 is enabled on an entrypoint, the TLS handshake selects the applicable TLS configuration through an exact, case-sensitive lookup on the SNI value, which fails to match wildcard host patterns (e.g., `*.ex…

---

## 27. 🟡 High Severity — Crawl4AI: SSRF via proxy settings in the Docker server bypasses the crawl-URL SSRF check

**CVE:** `CVE-2026-53755` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-6qhc-x826-342c>

> ### Summary

The Docker API server applied its SSRF destination check to the crawl target URL only, not to the proxy address. An unauthenticated request could supply a proxy pointing at an internal IP and route the browser through it, reaching internal services and cloud-metadata endpoints, while using a perfectly valid crawl URL. The Docker API is unauthenticated by default.

### Affected paths

…

---

## 28. 🟡 High Severity — Crawl4AI: SSRF filter bypass in Docker server via IPv6 transition forms (NAT64 / 6to4 / unspecified / v4-mapped)

**CVE:** `CVE-2026-53754` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-4qqr-vv2q-cmr5>

> ### Summary

The Docker API server&#x27;s SSRF protection (`validate_webhook_url` / `validate_url_destination` in `deploy/docker/utils.py`) used an explicit IPv4/IPv6 CIDR blocklist that missed several address families. An attacker could reach internal services and cloud metadata endpoints (e.g. `169.254.169.254`) despite the filter by encoding an internal IPv4 address inside an IPv6 transition fo…

---

## 29. 🟡 High Severity — LobeHub: Unauthenticated SSRF in `/webapi/proxy`

**CVE:** `CVE-2026-54157` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-xmwj-c75x-6346>

> ## Unauthenticated SSRF in /webapi/proxy allows anyone to proxy requests and inject cookies on lobehub.com

## Summary

The `/webapi/proxy` endpoint on app.lobehub.com accepts a URL in the POST body and fetches it server-side without any authentication. This is the same proxy code that was vulnerable in CVE-2024-32964, where `/api/proxy` was fixed by adding auth middleware. The `/webapi/proxy` rou…

---

## 30. 🟡 High Severity — Crawl4AI: AST Sandbox Escape via gi_frame.f_back Chain - Pre-Auth RCE in Docker API

**CVE:** `CVE-2026-53753` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-qxjp-w3pj-48m7>

> ### Summary

The `_safe_eval_expression()` function in the computed fields feature uses an AST validator that only blocks attributes starting with underscore. Python generator and frame object attributes (`gi_frame`, `f_back`, `f_builtins`) do NOT start with underscore, enabling a complete sandbox escape to achieve arbitrary code execution.

The attack requires no authentication (JWT disabled by d…

---

## 31. 🟡 High Severity — Deno: Permission Bypass via Unicode Normalization Mismatch on macOS (APFS)

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

## 32. 🟡 High Severity — Deno: BYONM module resolution allows `package.json` main path traversal to bypass `--allow-read` restrictions

**CVE:** `CVE-2026-49406` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-968w-xfqw-vp9q>

> ## Summary

When Deno was run in BYONM mode (`nodeModulesDir: &quot;manual&quot;`), the module resolver did not validate that a package&#x27;s resolved entrypoint stayed within its `node_modules/&lt;pkg&gt;/` directory. A malicious `package.json` whose `main` field contained `..` segments was able to resolve to an arbitrary path on disk, and the resolver then read that file without consulting the …

---

## 33. 🟡 High Severity — n8n: Merge Node SQL Mode Prototype Pollution

**CVE:** `CVE-2026-54311` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-9c38-2mcm-q7f7>

> ## Impact
An authenticated user with permission to create or modify workflows could pollute the sandbox used by the Merge node&#x27;s SQL Query mode. Because the sandbox context was cached and reused across all workflow executions on the instance, prototype mutations introduced by one user&#x27;s workflow persist into subsequent Merge SQL executions belonging to other users or projects. This allow…

---

## 34. 🟡 High Severity — Langflow: Unauthenticated RCE in Shareable Playgrounds

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

## 35. 🟡 High Severity — Astro: XSS via Unescaped Attribute Names in Spread Props

**CVE:** `CVE-2026-54298` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-jrpj-wcv7-9fh9>

> ## Summary

The `spreadAttributes` function in Astro&#x27;s server-side rendering pipeline iterates over object keys and passes them directly to `addAttribute`, which interpolates the key into the HTML output without escaping. When a developer uses the spread syntax `{...props}` on an HTML element and the object keys come from an untrusted source (API, CMS, URL parameters), an attacker can inject …

---

## 36. 🟡 High Severity — Astro: Host header SSRF in prerendered error page fetch

**CVE:** `CVE-2026-54299` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-2pvr-wf23-7pc7>

> ## Summary

Astro SSR apps with prerendered error pages (`/404` or `/500` using `export const prerender = true`) fetch those pages over HTTP at runtime when an error occurs. The URL for this fetch is derived from `request.url`, which in turn gets its origin from the incoming `Host` header. When the `Host` header is not validated against `allowedDomains`, an attacker can point the fetch at an arbit…

---

## 37. 🟡 High Severity — hono: Body Limit Middleware can be bypassed on AWS Lambda by understating `Content-Length`

**CVE:** `CVE-2026-54288` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-rv63-4mwf-qqc2>

> ### Summary

The Body Limit Middleware trusts the request&#x27;s `Content-Length` header to decide whether a body is within the limit. On AWS Lambda (API Gateway v1/v2, ALB, VPC Lattice, and Lambda@Edge) the body is delivered fully buffered and the adapter builds the request with the client-declared `Content-Length`, which need not match the actual payload. A client can declare a tiny `Content-Len…

---

## 38. 🟡 High Severity — hono: Lambda@Edge adapter keeps only the last value of a repeated request header, dropping the rest

**CVE:** `CVE-2026-54289` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-wgpf-jwqj-8h8p>

> ### Summary

On AWS Lambda@Edge, CloudFront delivers a request header that appears more than once as several separate entries. The adapter writes each value with `Headers.set` instead of `Headers.append`, so every value overwrites the previous one and only the last reaches the application. Repeated request headers such as `X-Forwarded-For`, `Forwarded`, and `Via` are silently truncated to a single…

---

## 39. 🟡 High Severity — hono: Path traversal in `serve-static` on Windows via encoded backslash (`%5C`)

**CVE:** `CVE-2026-54286` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-wwfh-h76j-fc44>

> ### Summary

On Windows hosts, an encoded backslash (`%5C`) in the request path decodes to `\`, which the Windows path resolver treats as a separator. `serve-static` then resolves a single URL segment such as `admin\secret.txt` into a nested file under the root and serves it, letting an attacker read static files meant to be protected behind prefix-mounted middleware. Directory escape (`..`) remai…

---

## 40. 🟡 High Severity — hono: AWS Lambda adapter merges multiple `Set-Cookie` headers into one value, dropping cookies on ALB single-header and Lattice

**CVE:** `CVE-2026-54287` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-j6c9-x7qj-28xf>

> ### Summary

On AWS Lambda, the ALB single-header response and the VPC Lattice v2 response join multiple `Set-Cookie` headers into one comma-separated value. Because commas also appear inside cookie attributes (for example `Expires` dates), clients cannot split the value back into individual cookies and silently drop or misparse them.

### Details

Per RFC 6265, each cookie must be its own `Set-Co…

---

## 41. 🟡 High Severity — Attackers Exploit Three Fortinet FortiSandbox Flaws, One Patched Last Week

**CVE:** `CVE-2026-39813` | `CVE-2026-39808` | `CVE-2026-25089` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://thehackernews.com/2026/06/attackers-exploit-three-fortinet.html>

> Bad actors are exploiting multiple security vulnerabilities in Fortinet FortiSandbox, according to threat intelligence firm Defused Cyber.

In a post shared on X, the company said it has observed exploitation of CVE-2026-39813, CVE-2026-39808, and CVE-2026-25089 over the past 24 hours.

CVE-2026-39813 (CVSS score: 9.1) refers to a path traversal vulnerability in FortiSandbox JRPC API that could

---

## 42. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
