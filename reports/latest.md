# Zero Day Pulse

> **Generated:** 2026-07-08 08:08 UTC &nbsp;|&nbsp; **Total:** 33 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 15 &nbsp;|&nbsp; 🟡 High: 18 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal'). SimpleHelp remote support software v5.5.7 and before contains multiple path traversal vulnerabilities that enable unauthenticated remote attackers to download arbitrary files from the SimpleHelp host via crafted HTTP requests containing traversal sequences (e.g., ../../../../../../etc/passwd). Exfiltrated files include server configuration files containing secrets (e.g., serverconfig.xml) and hashed user passwords, as well as system files such as /etc/passwd and private SSH keys (e.g., /root/.ssh/id_rsa). The vulnerability is remotely exploitable over the network without authentication or user interaction, with high confidentiality impact and no integrity/availability impact.
- **Affected Products:** SimpleHelp Remote Support / Remote Monitoring and Management (RMM) software versions 5.5.7 and all earlier releases (including v5.4.x and v5.3.x branches which received separate patch files).
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Public proof-of-concept exploit is available. A working PoC is published on GitHub at https://github.com/imjdl/CVE-2024-57727 (checks whether a target SimpleHelp server is vulnerable via path traversal). Additional exploit walkthroughs are published on Medium/TryHackMe. Exploits in the wild have been used by ransomware operators (per CISA AA25-163A).
- **Patch Available:** Yes. Patched by SimpleHelp in v5.5.8 and later releases. Patches are also provided for older branches: v5.4.10 (overwrite lib/shelp-jar-with-dependencies.jar with the provided patch file) and v5.3.9 (overwrite secure_utils.jar, secure_nlink.jar, and secure_shelp.jar in the lib directory with the provided patch ZIP). Upgrade/patching instructions are documented in the SimpleHelp Knowledge Base at https://guides.simple-help.com/kb---security-vulnerabilities-01-2025. CISA added this CVE to the Known Exploited Vulnerabilities (KEV) Catalog on 2025-02-13 with a remediation due date of 2025-03-06.
- **Active Exploitation:** Yes — confirmed active exploitation in the wild. Per CISA Advisory AA25-163A (published June 12, 2025): 'Ransomware actors likely leveraged CVE-2024-57727 to access downstream customers' unpatched SimpleHelp RMM for disruption of services in double extortion compromises.' Exploitation has been occurring since January 2025, including an incident that compromised a utility billing software provider's downstream customers. CVE-2024-57727 was added to CISA's Known Exploited Vulnerabilities (KEV) Catalog on February 13, 2025, with a remediation due date of March 6, 2025.
- **Threat Actors:** Ransomware actors (per CISA Advisory AA25-163A, June 12, 2025). CISA states ransomware actors have been targeting organizations through unpatched versions of SimpleHelp RMM since January 2025, including compromising customers of a utility billing software provider for double-extortion ransomware. Activity has been attributed by some reporting to the DragonForce ransomware group.
- **Mitigation:** If patching cannot be performed immediately: (1) Isolate the SimpleHelp server from the internet or stop the server process; (2) Change the Administrator and all Technician account passwords (used for local logins); (3) Restrict IP addresses allowed for Technician and Administrator logins; (4) Disable the built-in 'SimpleHelpAdmin' user and use a renamed Administrator Technician account; (5) Disable local Technician logins in favor of authentication services (Active Directory / LDAP); (6) Create new API tokens and restrict IP addresses for API requests and firewall connections; (7) Configure Server Event alerts for Administrator logins, failed login attempts, and configuration changes; (8) For encrypted systems, disconnect from the internet, reinstall the OS using clean media, wipe the system, and restore from clean offline backups; (9) Hunt for IOCs (suspicious/anomalous executables with three-letter alphabetic filenames such as aaa.exe, bbb.exe created after January 2025); (10) Avoid exposing remote services (e.g., RDP) to the internet and implement Software Bills of Materials (SBOM) for RMM software.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 2. 🟠 Zero-Day — CISA Adds 4 Actively Exploited Adobe, Joomla, and Langflow Flaws to KEV

**CVE:** `CVE-2026-48282` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://thehackernews.com/2026/07/cisa-adds-4-actively-exploited-adobe.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added four security flaws to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

The vulnerabilities are listed below -


  CVE-2026-48282 (CVSS score: 10.0) - A path traversal vulnerability in Adobe ColdFusion that could lead to arbitrary code execution in the context of the

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-48282 is an unauthenticated path traversal (CWE-22: Improper Limitation of a Pathname to a Restricted Directory) vulnerability in Adobe ColdFusion's Remote Development Services (RDS) FILEIO handler (FileServlet) exposed at the endpoint /CFIDE/main/ide.cfm (action=FILEIO). The handler fails to properly canonicalize or constrain resolved file paths, allowing a remote, unauthenticated attacker (via a crafted HTTP POST using a length-prefixed RPC format) to read and write arbitrary files on the server's file system, including the web root. Attackers can leverage the WRITE capability to upload a CFML webshell (using <cfexecute> tags) into an executable directory and then invoke it via a GET request to achieve unauthenticated Remote Code Execution (RCE) in the context of the current user. Scope is changed (S:C), no user interaction (UI:N) and no privileges (PR:N) are required.
- **Affected Products:** Adobe ColdFusion 2025 (Update 9 and earlier), Adobe ColdFusion 2023 (Update 20 and earlier)
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Exploit Available:** Public proof-of-concept (PoC) exploit code is available. A functional PoC is published on GitHub at https://github.com/imbas007/CVE-2026-48282 (imbas007/CVE-2026-48282) which supports vulnerability checking, arbitrary file read/write, and directory browsing against the vulnerable endpoint. The repository is also tracked in the PocOrExp_in_Github index at https://github.com/ycdxsb/PocOrExp_in_Github/blob/main/Today.md.
- **Patch Available:** Yes - Adobe released an official patch on June 30, 2026 via security bulletin APSB26-68 (https://helpx.adobe.com/security/products/coldfusion/apsb26-68.html). Fixed versions: Adobe ColdFusion 2025 Update 10 and Adobe ColdFusion 2023 Update 21. Adobe assigned the bulletin Priority Rating 1 (highest) and urged installation as soon as possible.
- **Active Exploitation:** Yes - confirmed active exploitation in the wild. CISA added CVE-2026-48282 to its Known Exploited Vulnerabilities (KEV) catalog on 2026-07-07 with a remediation due date of 2026-07-10 for Federal Civilian Executive Branch (FCEB) agencies. Vulnerability intelligence firm KEVIntel reported observing in-the-wild exploitation of its global honeypot network within two hours of public disclosure, with attacks originating from IP 103.207.14[.]220 (attacker geolocated to India). Sources: BleepingComputer, SecurityAffairs, SecurityWeek, CISA KEV catalog, The Hacker News, and HelpNet Security.
- **Threat Actors:** None known (no specific APT, ransomware group, or named campaign has been publicly attributed). In-the-wild exploitation was observed by KEVIntel originating from IP address 103.207.14[.]220 (attacker geolocated to India) within two hours of public disclosure.
- **Mitigation:** Apply Adobe's security updates immediately (CISA set the KEV remediation due date to 2026-07-10). Hardening guidance if patching cannot be performed immediately: (1) Disable RDS if it is not required, otherwise restrict it to trusted administrator hosts/internal networks; (2) Block external/HTTP access to the administrative endpoints /CFIDE/administrator, /CFIDE/main/ide.cfm, and /CFIDE/main/websocket.cfm via a WAF or network ACL; (3) Run ColdFusion under a low-privilege service account and restrict write permissions to the web root; (4) Hunt the web directories for any unauthorized .cfm, .cfc, .cfml, or .jsp files and rotate any potentially compromised credentials.
- **Vendor Advisory:** https://helpx.adobe.com/security/products/coldfusion/apsb26-68.html

---

## 3. 🟠 Zero-Day — Critical Gitea Flaw Under Active Exploitation, Researchers Warn

**CVE:** `CVE-2026-20896` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://www.securityweek.com/critical-gitea-flaw-under-active-exploitation-researchers-warn/>

> Attackers are exploiting the critical Gitea vulnerability CVE-2026-20896 to bypass authentication with a single HTTP header and access vulnerable repositories and secrets. The post Critical Gitea Flaw Under Active Exploitation, Researchers Warn appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** The official Gitea Docker image ships an app.ini template that hard-codes REVERSE_PROXY_TRUSTED_PROXIES = * (a wildcard trusting every source IP as a reverse proxy) together with reverse-proxy authentication enabled. Any remote, unauthenticated attacker who can reach the Gitea HTTP port can send a single HTTP request containing the header 'X-WEBAUTH-USER: <username>' (e.g., 'X-WEBAUTH-USER: admin') and be logged in as that user—including administrators—without supplying any password or token. The vulnerability is a default insecure configuration (not a code flaw) and only affects the official Docker image.
- **Affected Products:** Gitea Docker image versions ≤ 1.26.2; Gogs is also reportedly affected by the same REVERSE_PROXY_TRUSTED_PROXIES=* default behavior
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** Yes — public proof-of-concept and detector available. Author Ali Mustafa (@rz1027) published a PoC at https://github.com/rz1027/CVE-2026-20896 (containing poc.py, detect.py, and docker-compose.yml). Also indexed at https://sploitus.com/exploit?id=0FC89D13-9196-52D2-AF79-402D089DB0F4
- **Patch Available:** Yes — patched in v1.26.3 (initial fix) and v1.26.4 (recommended). Fix PR: https://github.com/go-gitea/gitea/pull/38151. Release tag: https://github.com/go-gitea/gitea/releases/tag/v1.26.3. Vendor blog: https://blog.gitea.com/release-of-1-26-3-and-1-26-4/. Vendor advisory: https://github.com/go-gitea/gitea/security/advisories/GHSA-f75j-4cw6-rmx4
- **Active Exploitation:** Yes — confirmed active exploitation in the wild. Sysdig reported via SecurityWeek that a VPN-exit scanner was observed probing for vulnerable instances. The Hacker News corroborated that the first in-the-wild exploitation attempt was detected 13 days after public disclosure, with scanning traced to IP 159.26.98[.]241 egressing through ProtonVPN exit nodes. The vulnerability's severity and immediate public PoC release make opportunistic mass scanning the dominant observed activity.
- **Threat Actors:** None known
- **Mitigation:** 1) Upgrade the Gitea Docker image to v1.26.4 (recommended) or at minimum v1.26.3. 2) Explicitly set REVERSE_PROXY_TRUSTED_PROXIES in app.ini to specific CIDR/IP addresses of upstream reverse proxies (never '*'). 3) Disable ENABLE_REVERSE_PROXY_AUTHENTICATION if reverse-proxy auth is not used. 4) Restrict direct internet access to the Gitea HTTP port. 5) At the edge load balancer/reverse proxy, strip any client-supplied X-WEBAUTH-USER (and X-WEBAUTH-*) headers before forwarding to Gitea. 6) Audit existing Gitea Docker instances for unauthorized access (unexpected accounts, admin actions, exposed secrets/repos).
- **Vendor Advisory:** https://github.com/go-gitea/gitea/security/advisories/GHSA-f75j-4cw6-rmx4

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an architectural vulnerability of LLM-based AI systems in which an adversary hides adversarial natural-language instructions inside content an AI later ingests - web pages, emails, calendar invites, documents, or retrieved RAG data. When the AI processes the 'poisoned' content, it silently follows the attacker's instructions instead of the user's original intent. Delivery/hiding techniques observed in the wild include HTML comments, CSS invisibility (display:none, font-size:1px, rgba(...,0.01)), accessibility attributes (aria-hidden, visually-hidden spans), meta-tag namespace spoofing, [SYSTEM OVERRIDE] / magic-string authority tags, invisible Unicode characters, multi-layer encoding, payload splitting, and semantic tricks such as multilingual or syntax-injected instructions. Demonstrated impacts include AI-based ad-review evasion, SEO/referral manipulation, data destruction via injected shell commands (e.g. 'sudo rm -rf'), unauthorized financial transactions (payment-platform exploitation), API-key and sensitive-data exfiltration, denial-of-service / system-prompt leakage, and calendar-authorization bypass that exfiltrates meeting metadata.
- **Affected Products:** Google Gemini; Google Workspace with Gemini (Gmail, Docs, Calendar); AI-powered browsers (e.g., ChatGPT Atlas); AI assistants integrated into IDEs and dev pipelines (GitHub Copilot, Cursor, Claude Code, AI-powered CI/CD reviewers); LLM-powered agents embedded in web browsers, search engines, and content-processing pipelines (developer tools, customer-support bots, security scanners, agentic crawlers, autonomous agents); secure email gateways (Mimecast SEG bypass demonstrated). Adjacent confirmed CVEs tied to the same attack class: Microsoft 365 Copilot (EchoLeak, CVE-2025-32711, CVSS 9.3) and GitHub Copilot (CVE-2025-53773).
- **CVSS Score:** 2.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes - multiple public PoCs and weaponized in-the-wild payloads are available. Public PoC sources: https://github.com/brennanbrown/atlas-prompt-injection-poc (Atlas AI browser IPI PoC), https://greshake.github.io/ (Greshake's original IPI research), and https://swisskyrepo.github.io/PayloadsAllTheThings/Prompt%20Injection/. Forcepoint X-Labs documented 10 verified, live, weaponized payloads on production websites targeting thelibrary-welcome[.]uk (API-key theft), kleintechnik[.]net (admin path-traversal), kassoon[.]com (SEO/referral hijack), faladobairro[.]com ('sudo rm -rf' data destruction), perceptivepumpkin[.]com (PayPal.me $5,000 unauthorized payment), archibase[.]co (Stripe donation scam), and others.
- **Patch Available:** No traditional CVE-style patch exists because IPI is a class of architectural vulnerability affecting how LLM products ingest untrusted content. Vendors ship continuous, layered mitigations rather than a versioned patch: Google's continuous mitigation strategy for Workspace with Gemini (advisory: https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections and https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini); Microsoft Defender Prompt Shields; Palo Alto Networks Advanced DNS Security / Advanced URL Filtering / Prisma AIRS / Prisma Browser; Forcepoint X-Labs Real Time Analytics IPI-URL blocking. Specific in-the-wild IPI findings (e.g., Miggo's Google Gemini calendar-invite authorization bypass, disclosed Jan 19, 2026) have been mitigated by Google after responsible disclosure.
- **Active Exploitation:** Yes - confirmed active exploitation in the wild by multiple independent researchers. Google's Threat Intelligence Group observed a 'relative increase of 32% in the malicious category between November 2025 and February 2026' of IPI attempts against AI systems browsing the web (source: http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html, verified 2026-04-23). Forcepoint X-Labs (Apr 22, 2026) found 10 verified, weaponized IPI payloads already live on production websites spanning financial fraud, data destruction, system-prompt leakage, and SEO manipulation (source: https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads). Palo Alto Unit 42 (Mar 3, 2026) reported web-based IPI being actively weaponized for AI-based ad-review evasion, SEO manipulation promoting phishing sites, data destruction, denial-of-service, unauthorized transactions, sensitive information leakage, and system-prompt leakage (source: https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/). Help Net Security (Apr 24, 2026) corroborated that 'indirect prompt injection is taking hold in the wild'.
- **Threat Actors:** None known
- **Mitigation:** No single patch - IPI requires layered 'defense-in-depth'. Vendor and standards guidance: (1) Google Workspace/Gemini: user confirmation prompts for risky actions, URL sanitization, tool-chaining policies, retraining Gemini with synthetic adversarial data, hardened system prompts, and Gemini model hardening to ignore embedded directives. (2) Microsoft: deploy Microsoft Defender Prompt Shields, Spotlight (data marking + metaprompting to isolate untrusted content), plan-drift detection, critic agents auditing inputs/outputs, tool-chain analysis to block risky action sequences, information-flow control with metadata/quarantined inference, principle of least privilege, short-lived agent credentials, and human-in-the-loop confirmation for risky actions. (3) Palo Alto: spotlighting, instruction hierarchy, adversarial training, design-level defenses, plus network-layer controls via Advanced DNS Security, Advanced URL Filtering, Prisma AIRS and Prisma Browser. (4) Forcepoint: enforce a strict data-instruction boundary and block known IPI URLs via Real Time Analytics. (5) OWASP (LLM01:2025): treat all retrieved/external content as untrusted input, apply structural delimiters and input sanitization, inspect the full assembled prompt, and implement output validation.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) influences an LLM's behavior by embedding malicious instructions inside external content (web pages, emails, documents, slides, calendar entries) or third-party tools the model consumes while completing a user's query — without requiring any direct input from the user. Documented attack vectors include: (1) hidden or manipulated instructions in web pages that AI agents later summarize or act on (Unit 42 web-based IPI); (2) dormant payloads placed in the description field of a Google Calendar invite that activate when a user asks Gemini about their schedule, abusing the Calendar.create tool to exfiltrate summaries of private meetings (Miggo); (3) malicious instructions inside emails, documents, and slide speaker notes that cause Gemini to render phishing URLs (e.g., fake password-reset pages) or otherwise manipulate chatbot output (HiddenLayer). Google's own telemetry scanning 2–3 billion pages/month showed a 32% relative rise in malicious IPI between November 2025 and February 2026.
- **Affected Products:** Google Workspace with Gemini (Gmail, Google Docs, Drive, Chat, Calendar) and the standalone Gemini app. No specific version numbers were published.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — multiple public PoCs and weaponized payloads exist: Miggo 'Weaponizing Calendar Invites' (https://www.miggo.io/post/weaponizing-calendar-invites-a-semantic-attack-on-google-gemini); HiddenLayer 'New Gemini for Workspace Vulnerability' (https://www.hiddenlayer.com/research/new-gemini-for-workspace-vulnerability-enabling-phishing-content-manipulation); HiddenLayer 'Hidden Prompt Injections Can Hijack AI Code Assistants' (https://www.hiddenlayer.com/research/how-hidden-prompt-injections-can-hijack-ai-code-assistants-like-cursor); Trail of Bits 'Prompt injection engineering for attackers' (https://blog.trailofbits.com/2025/08/06/prompt-injection-engineering-for-attackers-exploiting-github-copilot/); Palo Alto Unit 42 web-based IPI (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/); Forcepoint X-Labs 10 IPI payloads (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads); OWASP reference (https://github.com/OWASP/www-community/blob/master/pages/attacks/prompt-injection.md); Google bug-bounty write-up paid $15,000 (https://www.reddit.com/r/bugbounty/comments/1row41z/google_paid_me_15000_for_this_prompt_injection_bug/).
- **Patch Available:** No single discrete vendor patch. Google has deployed multiple point-fix mitigations continuously through 2025–2026 (e.g., the Calendar-invite attack reported by Miggo was confirmed and mitigated; HiddenLayer's reported issues were triaged through Google's VRP). The 'patch' is the rolling set of layered defenses described in the advisory itself: http://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections and the supporting admin help at https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini.
- **Active Exploitation:** Yes — confirmed active exploitation in the wild. (1) Google's own scan of 2–3 billion pages/month observed a 32% relative increase in malicious IPI between November 2025 and February 2026 (https://blog.google/security/prompt-injections-web/, April 23 2026). (2) Forcepoint X-Labs documented 10 distinct indirect-prompt-injection payloads caught in the wild on April 22, 2026 (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads), with observed impacts including financial fraud (PayPal/Stripe donation-link redirection), API-key and sensitive-data exfiltration, destructive commands, denial-of-service/content-suppression, SEO manipulation, and output hijacking. (3) Palo Alto Unit 42 reported web-based indirect prompt injection observed in the wild (March 3 2026, https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/). (4) Help Net Security summarized the in-the-wild findings on April 24 2026 (https://www.helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild/). (5) Specific weaponized examples include the Miggo Gemini Calendar-invite data-exfiltration attack (disclosed January 19 2026) and HiddenLayer's Gemini-for-Workspace phishing-content manipulation (published September 25 2024, with public PoC payloads).
- **Threat Actors:** None known. Indirect prompt injection is a technique, not a campaign tied to a specific APT or ransomware group. Published in-the-wild reports (Google, Forcepoint X-Labs, Palo Alto Unit 42, Miggo, HiddenLayer) describe opportunistic abuse (financial fraud, data exfiltration, phishing content manipulation, SEO/output hijacking) by unnamed actors rather than attributed threat actor groups.
- **Mitigation:** Google describes a continuous, layered defense rather than a single patch: (a) Discovery & Cataloging — human + automated red-teaming, the Google AI Vulnerability Rewards Program, and public-disclosure monitoring feeding a centralized vulnerability catalog; (b) Synthetic Data Generation — attack variants used to train/test defenses; (c) Deterministic Defenses — user confirmation prompts for risky actions (e.g., deleting calendar events), URL sanitization (Google Safe Browsing), tool-chaining policies, and rapid point fixes enforced via a centralized Policy Engine; (d) ML-Based Defenses — retrained classifiers on synthetic variants; (e) LLM-Based Defenses — refined system instructions ('security thought reinforcement'); (f) Gemini Model Hardening — improved internal capability to recognize and ignore harmful instructions; (g) End-to-end evaluation against Workspace features, plus end-user security-mitigation notifications. Workspace administrators should review and enforce Gemini/Workspace security controls at https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini. General hardening for downstream systems: apply 'spotlighting' / instruction-hierarchy techniques, adversarial training, intent-analysis detection, and behavioral correlation (per Unit 42 recommendations).
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html (also at http://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections). Companion admin documentation: https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The blog describes indirect prompt injection as the primary new threat class facing all agentic browsers. In this attack, an adversary embeds hidden or obfuscated natural-language instructions inside web content (HTML, user-generated text, metadata, images) that an AI agent subsequently reads while performing an action on the user's behalf. The injected instructions can hijack the agent into performing attacker-chosen actions. Two concrete instances: (1) 'GeminiJack' (Noma Labs, Dec 8, 2025) — a zero-click indirect prompt injection against Gemini Enterprise where poisoned Workspace data sources (emails, calendar invites, documents) caused Gemini to silently exfiltrate sensitive corporate data (Gmail, Calendar, Docs); (2) CVE-2026-0628 (Chrome) — insufficient policy enforcement in the WebView tag that allowed a malicious Chrome extension (using declarativeNetRequest rules against gemini.google.com/app) to inject scripts/HTML into the privileged Gemini panel, enabling camera, microphone, local-file access and screenshots.
- **Affected Products:** Google Chrome prior to 143.0.7499.192, Gemini in Chrome agentic capabilities, Google Gemini Enterprise, Vertex AI Search
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Exploit Available:** Yes — proof-of-concept exploits are publicly available. Noma Labs disclosed a step-by-step PoC and demonstration video for the 'GeminiJack' zero-click indirect prompt injection vulnerability against Google Gemini Enterprise on December 8, 2025 (https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability/). A general benign PoC for indirect prompt injection in AI browsers is available at https://github.com/brennanbrown/atlas-prompt-injection-poc. No public weaponized exploit code has been published for the Chrome-side CVE-2026-0628 WebView tag policy-enforcement flaw.
- **Patch Available:** Yes. Google Chrome 143.0.7499.192 (Stable channel update for Desktop, released January 6, 2026 — https://chromereleases.googleblog.com/2026/01/stable-channel-update-for-desktop.html) fixes CVE-2026-0628. For the Gemini Enterprise 'GeminiJack' flaw, Google deployed mitigations to retrieval and indexing system interactions and fully separated Vertex AI Search from Gemini Enterprise, with comprehensive mitigations rolled out before December 10, 2025.
- **Active Exploitation:** No confirmed in-the-wild exploitation has been publicly reported for CVE-2026-0628. However, Palo Alto Networks Unit 42 documented in March 2026 the first large-scale indirect prompt injection campaigns observed in the wild, including AI ad-review evasion (reviewerpress[.]com) and SEO-manipulation phishing campaigns impersonating betting platforms. These targeted AI agents integrated into browsers, search engines, developer tools, and support bots rather than this specific Chrome vulnerability, and no specific APT group, ransomware operator, or named cybercrime campaign has been publicly attributed.
- **Threat Actors:** None known
- **Mitigation:** Google's layered defense architecture for agentic Chrome includes: (1) the 'User Alignment Critic' — an isolated secondary Gemini model that vets every proposed primary-agent action; (2) 'Agent Origin Sets' — restricting the agent's read and write access to a specific allow-list of origins/iframes; (3) explicit user confirmations before any critical or sensitive action; (4) a real-time prompt-injection classifier that scans page content alongside Safe Browsing and on-device scam detection; (5) 'Spotlighting' — preferring user/system instructions over page content via deterministic structural transforms; (6) deterministic safety checks for public URLs; and (7) ongoing red-teaming. For users of Gemini Enterprise / Vertex AI Search, Google separated Vertex AI Search from Gemini Enterprise to break the trust boundary that GeminiJack exploited.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2025-48530 is a linear buffer overflow (CWE-125, Out-of-bounds Read) in CrabbyAVIF, an AVIF image parser/decoder written in 'unsafe Rust' that ships with the Android platform. In multiple locations in the code, incorrect bounds checks allowed out-of-bounds memory accesses. When chained with other bugs it could lead to remote code execution over the network without user interaction or additional execution privileges (high attack complexity). It is notable as the very first Rust-based memory safety vulnerability discovered in Android, discovered internally by Google before being shipped.
- **Affected Products:** Google Android 16.0
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** No public exploit code is available. Per the Google Security Blog, the vulnerability never made it into a public Android release and was rendered non-exploitable in the development build by Android's Scudo hardened allocator (guard pages surrounding secondary allocations converted silent memory corruption into a noisy crash).
- **Patch Available:** Yes. Google addressed CVE-2025-48530 in the Android Security Bulletin August 2025 (https://source.android.com/security/bulletin/2025-08-01). Devices running the 2025-08-05 security patch level (or later) include the fix.
- **Active Exploitation:** No active exploitation in the wild has been reported. Per the Google Security Blog post 'Rust in Android: move fast and fix things' (Nov 13, 2025), the bug was caught internally before reaching a public Android release, and in internal builds the Scudo hardened allocator turned silent corruption into a noisy crash that prevented exploitation. CVE records, NVD, SentinelOne, and Tenable all list the vulnerability as not in the Known Exploited Vulnerabilities (KEV) catalog.
- **Threat Actors:** None known
- **Mitigation:** Apply the Android Security Bulletin August 2025 security patch (2025-08-05 patch level or later) to all Android 16.0 devices. Until patches are deployed, limit network exposure of affected Android devices, implement network segmentation and strict firewall rules to restrict inbound network access, use mobile device management (MDM) solutions, and monitor for system service crashes or restarts that could indicate exploitation attempts.
- **Vendor Advisory:** https://source.android.com/security/bulletin/2025-08-01

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection embeds hidden malicious instructions inside external content (emails, documents, calendar invites, web pages, chat messages) that an LLM ingests during a legitimate task. Because the LLM cannot reliably distinguish trusted user/system instructions from attacker-controlled data, the injected instructions can steer the model to exfiltrate sensitive data or take other rogue actions. The canonical example cited by Google is EchoLeak (CVE-2025-32711), a 0-click attack on Microsoft 365 Copilot in which a crafted email uses a markdown image reference to an attacker-controlled URL to silently exfiltrate sensitive context to an external server. Google also documented related techniques where hidden HTML/CSS (white-on-white text, display:none, 1px fonts, HTML comments) hides prompt instructions inside documents the user asks Gemini to summarize, and where notifications/messages to Gemini's connected tools can be weaponized to invoke unauthorized actions.
- **Affected Products:** Google Gemini (including Gemini 2.5 models), Gemini in Google Workspace, Gemini app, Gmail, Google Calendar, Google Docs, Microsoft 365 Copilot (referenced via CVE-2025-32711 / EchoLeak as an analogous example).
- **CVSS Score:** 6.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes. Multiple public proof-of-concept exploits exist: (1) Aim Security's EchoLeak (CVE-2025-32711) 0-click prompt-injection exfiltration against M365 Copilot - https://arxiv.org/html/2509.10540v1; (2) SafeBreach Labs' Gemini Voice Assistant / Android Utilities indirect prompt injection PoC - https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/; (3) Forcepoint X-Labs' 10 verified indirect prompt injection payloads found on live websites - https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads; (4) 0-Day Labs / invisible malicious-prompt PoC against Gemini in Workspace - https://www.darkreading.com/remote-workforce/google-gemini-ai-bug-invisible-malicious-prompts.
- **Patch Available:** No traditional software patch is applicable - this is a defense-strategy announcement rather than a CVE advisory. The layered mitigations (content classifiers, Safe Browsing URL redaction, markdown sanitization, system-prompt reinforcement, HITL confirmation) are being progressively deployed across Google Workspace Gemini features. Google GenAI Security PM Adam Gavish confirmed these defenses are launched across all Workspace AI features. Reference: http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html and supporting material at https://research.google/pubs/an-introduction-to-googles-approach-for-secure-ai-agents/.
- **Active Exploitation:** Yes - active exploitation has been observed. Forcepoint X-Labs confirmed 10 verified indirect-prompt-injection payloads operating on live, public websites across financial-fraud, data-destruction, traffic-hijacking, and payment-redirection scenarios (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads). Google states that its layered Gemini protections 'have consistently mitigated indirect prompt injection attempts' since the initial deployment of its enhanced defenses, indicating ongoing real-world attack attempts are being blocked (http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html). The referenced EchoLeak (CVE-2025-32711) 0-click vulnerability in M365 Copilot was similarly weaponized prior to Microsoft mitigation.
- **Threat Actors:** The Google Security Blog post does not name specific threat actors exploiting indirect prompt injection. Google Threat Intelligence Group (GTIG) has separately documented that APT-42 (Iranian government), UNC2970 (linked to North Korea's Lazarus Group), APT31 (Zirconium / Violet Typhoon), UNC795, and APT41 have abused Gemini for espionage, social-engineering persona creation, and malicious tooling development. Forcepoint X-Labs observed 10 indirect-prompt-injection payloads on live web infrastructure in the wild but did not attribute them to named APT groups.
- **Mitigation:** Google's layered defense strategy consists of six reinforcing controls: (1) Model hardening - training models with adversarial data so they are inherently more resilient to malicious instructions; (2) Prompt-injection content classifiers - proprietary ML models that detect and filter malicious instructions in inbound emails and files; (3) Security thought reinforcement - targeted system instructions that remind the model to ignore adversarial prompts and stay on the user-directed task; (4) Markdown sanitization and suspicious URL redaction - blocking external image rendering (specifically to prevent EchoLeak-style exfiltration) and using Google Safe Browsing to redact suspicious links; (5) Human-in-the-loop user confirmation - requiring explicit user approval for sensitive actions such as deleting calendar events; (6) End-user security mitigation notifications - surfacing contextual warnings with 'Learn more' links whenever an attack is mitigated so users remain informed.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 9. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors exploit known (n-day) CVEs in network edge devices — primarily large backbone routers of major telecommunications providers and provider edge (PE) / customer edge (CE) routers. The exploited vulnerabilities target Ivanti Connect Secure / Policy Secure, Palo Alto Networks PAN-OS GlobalProtect, Cisco IOS XE Web UI, and Cisco IOS/IOS XE Smart Install. After gaining initial access, the actors modify router configurations to maintain persistent, long-term access: they enable GRE/IPsec tunnels and static routes for covert connectivity, configure SPAN/RSPAN/ERSPAN traffic mirroring to collect data, modify Access Control Lists (often naming them 'access-list 20'), and abuse virtualized container features — notably Cisco IOS XE GuestShell — to deploy a custom utility dubbed 'JumbledPath' that runs Linux commands and obfuscates the source/destination of requests. They then pivot from compromised devices and trusted interconnections into other networks across telecommunications, government, transportation, lodging, and military infrastructure globally. CISA notes that exploitation of zero-day vulnerabilities has not been observed to date — all observed exploitation is against known, previously disclosed CVEs.
- **Affected Products:** Ivanti Connect Secure and Ivanti Policy Secure (CVE-2024-21887); Palo Alto Networks PAN-OS GlobalProtect (CVE-2024-3400); Cisco IOS XE Software Web UI (CVE-2023-20198, CVE-2023-20273); Cisco IOS and IOS XE Software Smart Install (CVE-2018-0171). Additional products observed being targeted in the same campaign include Fortinet firewalls, Juniper firewalls, Microsoft Exchange, Nokia routers/switches, Sierra Wireless devices, and SonicWall firewalls.
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Exploit Available:** Yes. Public PoC and weaponized exploit code is available for the listed CVEs. Notable references: Cisco CVE-2023-20198 / CVE-2023-20273 advisory at https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxe-webui-privesc-j22SaA4z and Cisco CVE-2018-0171 Smart Install advisory at https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180328-smi2.html. The threat actors deploy a custom utility dubbed 'JumbledPath' that abuses Cisco IOS XE GuestShell to evade detection.
- **Patch Available:** Yes — vendor patches are available for every CVE listed in Appendix B. Patch the five CVEs as a high priority: Ivanti CVE-2024-21887 (https://forums.ivanti.com/s/article/CVE-2024-21887), Palo Alto Networks CVE-2024-3400 (https://security.paloaltonetworks.com/CVE-2024-3400), Cisco CVE-2023-20198 / CVE-2023-20273 (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxe-webui-privesc-j22SaA4z), and Cisco CVE-2018-0171 (https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180328-smi2.html).
- **Active Exploitation:** Confirmed active in-the-wild exploitation. CISA, NSA, FBI, and international partners (AA25-239A, co-authored with the Canadian Centre for Cyber Security and other Five Eyes members) document a long-running, ongoing PRC state-sponsored espionage campaign — active since at least 2021 — in which Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, and GhostEmperor have systematically compromised telecommunications, government, transportation, lodging, and military infrastructure networks worldwide by exploiting the listed known CVEs against backbone, PE, and CE routers. CISA notes that exploitation of zero-day vulnerabilities has not been observed to date; the threat is exploitation of previously disclosed (n-day) vulnerabilities combined with configuration tampering for long-term persistence.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor (PRC state-sponsored). Associated entities: Sichuan Juxinhe Network Technology Co. Ltd., Beijing Huanyu Tianqiong Information Technology Co. Ltd., Sichuan Zhixin Ruijie Network Technology Co. Ltd. (linked to PRC Ministry of State Security / People's Liberation Army).
- **Mitigation:** Per CISA AA25-239A and Appendix C: (1) Immediately patch the five CVEs listed in Appendix B (CVE-2024-21887, CVE-2024-3400, CVE-2023-20198, CVE-2023-20273, CVE-2018-0171); (2) Upgrade unsupported network devices to vendor-supported models; (3) Regularly review network device logs and configurations for unexpected activity (GRE/IPsec tunnels, AAA/TACACS+/RADIUS changes, ACL modifications, packet captures, virtualized containers); (4) Disable Cisco Smart Install (SMI) and Cisco GuestShell where not operationally required; (5) Disable unused ports and protocols and outbound connections from management interfaces; (6) Change all default credentials and enforce strong cryptographic algorithms; (7) Validate firmware/image hashes against vendor values and enable signed-image enforcement; (8) Audit containerized services (GuestShell via syslog/AAA) and disable if not required; (9) Monitor for unauthorized ACL modifications, services on non-standard ports, and suspicious authentication behavior.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 10. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2023-23397 is a Microsoft Outlook (Windows) Elevation of Privilege vulnerability (CWE-20/CWE-294). An attacker sends a specially crafted email containing an extended MAPI property 'PidLidReminderFileParameter' whose value is set to a Universal Naming Convention (UNC) path pointing to an attacker-controlled SMB server (TCP 445). When Outlook processes the message — for example when a calendar reminder fires or the user interacts with the message — Outlook automatically connects to that UNC path and authenticates using the victim's Windows credentials, leaking the victim's Net-NTLMv2 hash to the attacker. No user interaction (beyond receiving the email) is required for the leak to occur. The captured hash can be cracked offline or used in an NTLM relay attack.
- **Affected Products:** Microsoft 365 Apps for Enterprise, Microsoft Office 2019 (32/64-bit), Microsoft Office LTSC 2021, Microsoft Outlook 2013 SP1 (32/64-bit, including RT), Microsoft Outlook 2016 (32/64-bit). Only Outlook for Windows is affected — Outlook for Mac, iOS, Android, and Outlook on the web are not vulnerable.
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** Yes. Public PoC exploits are available on GitHub: https://github.com/Trackflaw/CVE-2023-23397 and https://github.com/vlad-a-man/CVE-2023-23397. The vulnerability has also been weaponized by Russian GRU Unit 26165 (APT28) as documented in CISA AA25-141A.
- **Patch Available:** Yes — Microsoft released an out-of-band security update for CVE-2023-23397 on March 14, 2023. Patch and guidance: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23397
- **Active Exploitation:** Yes — confirmed active exploitation in the wild. CISA added CVE-2023-23397 to the Known Exploited Vulnerabilities (KEV) catalog on 2023-03-14. CISA joint advisory AA25-141A confirms Russian GRU Unit 26165 has weaponized CVE-2023-23397 since at least 2022 against Western logistics entities and technology companies supporting aid delivery to Ukraine.
- **Threat Actors:** Russian GRU 85th Main Special Service Center (85th GTsSS), military unit 26165 — tracked by industry as APT28, Fancy Bear, Forest Blizzard, and BlueDelta
- **Mitigation:** 1) Apply the Microsoft March 14, 2023 security update to all affected Outlook/Office installs. 2) Block outbound SMB/TCP 445 at the perimeter and on VPN clients. 3) Add privileged users to the 'Protected Users' security group to prevent NTLM authentication. 4) Where feasible, disable NTLM entirely and require Kerberos. 5) Enforce multi-factor authentication to mitigate NTLM relay. 6) Use Microsoft's official script to find and remove the malicious PidLidReminderFileParameter from messages already delivered. 7) Reset credentials for any user observed sending outbound SMB to external IPs and audit NTLM authentications. 8) Per AA25-141A hardening: enforce MFA with strong factors, use hardware MFA tokens for admin accounts, block logins from public VPN services, block egress to hosting/API-mocking services.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a; https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23397

---

## 11. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

---

## 12. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 13. 🟠 Zero-Day — CrowdStrike Uncovers New Prompt Injection Techniques

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jul 07, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-uncovers-new-prompt-injection-techniques/>

---

## 14. 🟠 Zero-Day — CISA orders feds to patch max severity ColdFusion flaw by Friday

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-max-severity-coldfusion-flaw-by-friday/>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has ordered government agencies to patch an actively exploited maximum-severity flaw in the Adobe ColdFusion commercial web app development platform by Friday. [...]

---

## 15. 🟠 Zero-Day — Chinese hackers develop LONGLEASH malware to expand ORB network

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://www.bleepingcomputer.com/news/security/chinese-hackers-develop-longleash-malware-to-expand-orb-network/>

> Chinese hackers tracked as &#x27;UAT-7810&#x27; are actively evolving their malware to expand their Operational Relay Box (ORB) network by compromising internet-facing networking devices, primarily unpatched Ruckus routers. [...]

---

## 16. 🟡 High Severity — 15-Year-Old GhostLock Flaw Enables Root and Container Escape on Most Linux Distros

**CVE:** `CVE-2026-43499` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-08
**Reference:** <https://thehackernews.com/2026/07/15-year-old-ghostlock-flaw-enables-root.html>

> Researchers at Nebula Security have disclosed GhostLock (CVE-2026-43499), a 15-year-old Linux kernel flaw that lets any logged-in user take full root control of a machine that has not been patched.

The vulnerable code has shipped by default in essentially every mainstream distribution since 2011. The flaw needs no special permission, no unusual settings, and no network

---

## 17. 🟡 High Severity — Weblate SSRF: outbound URL guard misses some private ranges

**CVE:** `CVE-2026-50127` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-vmfc-9982-2m45>

> ### Impact

Weblate&#x27;s `VCS_RESTRICT_PRIVATE` did not properly account for some transitional IPv6 ranges, multicast addresses, or some semi-private IPv4 ranges, which allowed some addresses to bypass private range restrictions.

### Patches

* https://github.com/WeblateOrg/weblate/pull/19768

### Resources

The issue was reported by @tonghuaroot via GitHub, and the same user also provided the …

---

## 18. 🟡 High Severity — oasdiff does not enforce --allow-external-refs=false on the git-revision load path (SSRF / local file read)

**CVE:** `CVE-2026-53508` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-2jcc-mxv7-p3f9>

> ## Summary

From **v1.13.2** through **v1.18.0**, oasdiff did not enforce `--allow-external-refs=false` (library: `openapi3.Loader.IsExternalRefsAllowed = false`) when loading a spec from a **git revision** (the `rev:path` form, e.g. `main:openapi.yaml`). External `$ref`s were resolved on that load path even when external refs were explicitly disabled, so the mitigation silently did not apply ther…

---

## 19. 🟡 High Severity — Goploy: Cross-namespace IDOR and RCE via body-supplied row id in project and project_file handlers

**CVE:** `CVE-2026-53552` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-26rh-24rg-j3vv>

> ### Summary

`Project.AddFile`, `Project.EditFile`, `Project.RemoveFile`, and `Project.Edit` in `cmd/server/api/project/handler.go` accept a project or project-file row id from the JSON body and act on it without checking that the project belongs to the caller&#x27;s namespace. The corresponding `model.ProjectFile.GetData` and `model.Project.GetData` queries filter only by row id. A user holding t…

---

## 20. 🟡 High Severity — Kite has an authenticated cluster RBAC bypass in /api/v1/overview

**CVE:** `CVE-2026-53487` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-gvhc-wv3v-7pf8>

> ## Summary

Authenticated Kite users with any role can request `/api/v1/overview` for a cluster that their roles do not permit by selecting that cluster with `x-cluster-name`. The overview route is registered before `middleware.RBACMiddleware()` and `GetOverview` only checks `len(user.Roles) &gt; 0`, so it returns aggregate Kubernetes inventory and capacity data from unauthorized clusters.

The is…

---

## 21. 🟡 High Severity — ratex-parser has unbounded parser recursion that leads to stack overflow (process abort)

**CVE:** `CVE-2026-53531` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-4w5h-hx6r-28q7>

> ### Summary


RaTeX’s recursive-descent parser recurses one (or more) native stack frame per nesting level at `{`, `\left`, `\sqrt{`, `^{`, etc, with **no maximum depth limit**. A short, ~10 KB input of nested groups overflows the 8 MB main-thread stack and aborts the process. With `panic = &quot;abort&quot;` (`Cargo.toml:48`), and because a Rust stack overflow is always a fatal `SIGABRT` regardle…

---

## 22. 🟡 High Severity — @better-auth/oauth-provider's OAuth authorization-code grant allows concurrent redemption when two token requests race the find-then-delete primitive

**CVE:** `CVE-2026-53518` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-7w99-5wm4-3g79>

> ### Am I affected?

Users are affected if all of the following are true:

- Their project depends on `@better-auth/oauth-provider` at a version `&gt;= 1.6.0, &lt; 1.6.11`, or uses the embedded plugin in `better-auth &gt;= 1.4.8-beta.7, &lt; 1.6.0`, or enables the legacy `oidc-provider` or `mcp` plugins from `better-auth/plugins`.
- Their application exposes `/api/auth/oauth2/token` (or the legacy …

---

## 23. 🟡 High Severity — @better-auth/sso provider registration has server-side request forgery via unvalidated OIDC endpoints

**CVE:** `CVE-2026-53513` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-5rr4-8452-hf4v>

> ### Am I affected?

Users are affected if all of the following are true:

- Their application uses `@better-auth/sso` at a version `&gt;= 0.1.0, &lt; 1.6.11` on the stable line, or any `1.7.0-beta.x` on the pre-release line.
- The `sso()` plugin is added to their application&#x27;s `betterAuth({ plugins: [...] })` array.
- Any user with a valid Better Auth session can reach `POST /sso/register` (t…

---

## 24. 🟡 High Severity — Better Auth: OAuth refresh-token rotation forks the token family on concurrent redemption

**CVE:** `CVE-2026-53517` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-392p-2q2v-4372>

> ### Am I affected?

Users are affected if all of the following are true:

- Their project depends on `@better-auth/oauth-provider` at a version `&gt;= 1.6.0, &lt; 1.6.11`, or uses the embedded plugin in `better-auth &gt;= 1.4.8-beta.7, &lt; 1.6.0`.
- At least one OAuth client served by their application&#x27;s authorization server requests the `offline_access` scope, so refresh tokens are minted.
…

---

## 25. 🟡 High Severity — Better Auth: OAuth refresh-token replay via missing client authentication on oidc-provider and mcp plugins

**CVE:** `CVE-2026-53512` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-pw9m-5jxm-xr6h>

> ### Am I affected?

Users are affected if all of the following are true:

- Their application uses `better-auth` and has enabled at least one of: `oidcProvider()` (imported from `better-auth/plugins/oidc-provider`), or `mcp()` (imported from `better-auth/plugins/mcp`).
- Their application has at least one confidential OAuth client registered (any client with `type: &quot;web&quot; | &quot;native&q…

---

## 26. 🟡 High Severity — @aborruso/ckan-mcp-server: SSRF via base_url allows access to internal networks (Potential fix bypass of CVE-2026-33060)

**CVE:** `CVE-2026-53509` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-g84h-j7jj-x32p>

> ### Summary
A known vulnerability CVE-2026-33060 indicated tools including ckan_package_search and sparql_query that accept a base_url parameter had the risk of making HTTP requests to arbitrary endpoints without restriction. A fix was applied to filter out ip addresses. However, a method to bypass exists.

### Details
CKAN MCP Server validates caller-supplied CKAN server URLs by inspecting only t…

---

## 27. 🟡 High Severity — Open WebUI has Blind Server Side Request Forgery in its Image Edit Functionality

**CVE:** `CVE-2026-34225` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-jgx9-jr5x-mvpv>

> ### Summary
There is a blind server side request forgery in the functionality that allows editing an image via a prompt. The affected function will perform a GET request on the URL provided by the user. There is no restriction on the domain of the provided URL allowing the local address space to be interacted with. Since the SSRF is blind (the response cannot be read) impact is port scanning of th…

---

## 28. 🟡 High Severity — Open WebUI vulnerable to stored XSS via unescaped markdown token in MarkdownTokens.svelte leading to full account takeover and RCE via functions

**CVE:** `CVE-2025-46719` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-9f4f-jv96-8766>

> ### Summary

A vulnerability in the way certain html tags in chat messages are rendered allows attackers to inject JavaScript code into a chat transcript. The JavaScript code will be executed in the user&#x27;s browser every time that chat transcript is opened, allowing attackers to retrieve the user&#x27;s access token and gain full control over their account. Chat transcripts can be shared with …

---

## 29. 🟡 High Severity — EGroupware has Authenticated RCE via Malicious eTemplate Upload

**CVE:** `CVE-2026-40187` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-8737-2x9g-xjj7>

> ## Summary

An authenticated administrator can achieve OS-level Remote Code Execution (RCE) by uploading a malicious eTemplate XML file (`.xet`) to the VFS `/etemplates` mount.

The `Widget::expand_name()` method passes template widget attribute values directly into a PHP `eval()` call with only double-quote escaping applied - **backtick characters are not escaped**.

In PHP, backticks inside a do…

---

## 30. 🟡 High Severity — New API: SSRF Protection Bypass via Unresolved Hostname in Notification URLs

**CVE:** `CVE-2026-33655` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-6qcr-qxgr-m7fv>

> ## Summary

The default SSRF protection configuration did not apply IP filtering to hostnames. With `ApplyIPFilterForDomain` disabled by default, URL validation checked domain allow/block rules but did not resolve a hostname and validate the resolved IP address. Authenticated users could configure notification URLs for Webhook, Bark, or Gotify notifications and point a hostname at an internal or m…

---

## 31. 🟡 High Severity — EGroupware has a Remote Code Execution Vulnerability

**CVE:** `CVE-2026-27823` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-h9qx-v5xp-ph8p>

> ## Summary
A critical vulnerability has been identified in EGroupware that may lead to Remote Code Execution (RCE).
The issue allows an authenticated attacker to execute arbitrary commands on the server. If user self-registration is enabled, the vulnerability may be exploitable without prior authentication.

The vulnerability stems from improper authorization checks combined with a file write prim…

---

## 32. 🟡 High Severity — Suspected China-Aligned Hackers Exploit Roundcube Flaws Against Universities

**CVE:** `CVE-2024-42009` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://thehackernews.com/2026/07/suspected-china-aligned-hackers-exploit.html>

> A suspected China-aligned threat activity cluster has been observed exploiting Roundcube webmail software belonging to physics and engineering departments of U.S. and Canadian universities as part of a new campaign.

The activity involves the exploitation of now-patched, critical security flaws in the open-source email solution, such as CVE-2024-42009 (CVSS score: 9.3), to siphon credentials,

---

## 33. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
