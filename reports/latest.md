# Zero Day Pulse

> **Generated:** 2026-07-07 09:22 UTC &nbsp;|&nbsp; **Total:** 42 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 13 &nbsp;|&nbsp; 🟡 High: 29 &nbsp;|&nbsp; ✨ Enriched: 6

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is a path traversal flaw that allows unauthenticated remote attackers to download arbitrary files from the SimpleHelp server via crafted HTTP requests. This includes sensitive server configuration files containing hashed passwords for the SimpleHelpAdmin account or other accounts.
- **Affected Products:** SimpleHelp remote support software version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Publicly known. OffSec has published a blog post detailing how the vulnerability allows attackers to read sensitive files via path traversal (http://offsec.com/blog/cve-2024-57727).
- **Patch Available:** An official patch is available. Users are urged to upgrade immediately to the latest version of SimpleHelp. Further instructions can be found in the vendor's security vulnerability advisory: https://simple-help.com/kb---security-vulnerabilities-01-2025
- **Active Exploitation:** Confirmed active exploitation in the wild. CISA added CVE-2024-57727 to its Known Exploited Vulnerabilities (KEV) Catalog on February 13, 2025, and reported ransomware actors leveraging it to compromise customers of a utility billing software provider.
- **Threat Actors:** Ransomware actors, specifically the DragonForce group.
- **Mitigation:** Key mitigations include: 1. Upgrade immediately to the latest version of SimpleHelp. 2. Isolate the SimpleHelp server instance from the internet or stop the server process. 3. Search for suspicious or anomalous executables with three alphabetic letter filenames (e.g., aaa.exe) created after January 2025. 4. Implement hardening rules via a custom sandbox, such as the Symantec DCS Custom sandbox.
- **Vendor Advisory:** http://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — Langroid: Neo4jChatAgent executes LLM-generated Cypher without validation (prompt-to-Cypher injection; config-conditional RCE), mirroring the SQLChatAgent bug fixed in CVE-2026-25879

**CVE:** `CVE-2026-55615` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-2pq5-3q89-j7cc>

> Neo4jChatAgent passes LLM-generated Cypher queries straight to the Neo4j driver with no validation, no statement-type allowlist, and no opt-out gate. The query text is influenceable by prompt injection (direct user input or indirect content the agent reads back via RAG), so an attacker who can influence the prompt can read or destroy all graph data and, when APOC or dbms.security procedures are en…

**Parallel AI Enrichment:**

- **Technical Details:** The Neo4jChatAgent in Langroid passes LLM-generated Cypher queries directly to the Neo4j driver without any validation, statement-type allowlists, or opt-out gates. This allows an attacker to influence the executed Cypher query via prompt injection (either through direct user input or indirect content read via RAG). This vulnerability enables unauthorized reading or destruction of all graph data. Furthermore, if APOC or dbms.security procedures are enabled on the server, the attacker can achieve OS-command and filesystem access (RCE).
- **Affected Products:** langroid <= 0.65.4
- **CVSS Score:** 9.2
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** A public proof-of-concept (PoC) is available within the official advisory at https://github.com/advisories/GHSA-2pq5-3q89-j7cc
- **Patch Available:** An official patch was released in version 0.65.5.
- **Active Exploitation:** None known
- **Threat Actors:** None known
- **Mitigation:** Upgrade to langroid version 0.65.5. As a hardening measure, disable APOC or dbms.security procedures on the Neo4j server if they are not required by the application to prevent the potential for RCE.
- **Vendor Advisory:** https://github.com/advisories/GHSA-2pq5-3q89-j7cc

---

## 3. 🟠 Zero-Day — Langroid: Sandbox Escape to Remote Code Execution via Incomplete `eval()` Mitigation in TableChatAgent

**CVE:** `CVE-2026-54769` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-q9p7-wqxg-mrhc>

> ### Advisory Details
**Title**: Sandbox Escape to Remote Code Execution via Incomplete `eval()` Mitigation in TableChatAgent

**Description**:
### Summary
Langroid is vulnerable to a critical Sandbox Escape leading to Remote Code Execution (RCE) in its `TableChatAgent` and `VectorStore` capabilities. When these agents evaluate LLM-generated tool messages with `full_eval=True`, they attempt to sand…

**Parallel AI Enrichment:**

- **Technical Details:** Langroid's `TableChatAgent` and `VectorStore` components are vulnerable to a sandbox escape leading to Remote Code Execution (RCE). This occurs when these agents evaluate LLM-generated tool messages with `full_eval=True`. The vulnerability arises from an incomplete attempt to sandbox the execution by setting the `locals` parameter to an empty dictionary `{}` within Python's `eval()` function, which does not effectively prevent access to the underlying execution environment.
- **Affected Products:** langroid <= 0.65.1
- **CVSS Score:** 10.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Information on whether a public proof-of-concept (PoC) or weaponized exploit exists for the vulnerability is unavailable.
- **Patch Available:** An official patch has been released in version 0.65.2.
- **Active Exploitation:** No confirmed active exploitation in the wild has been reported.
- **Threat Actors:** None known
- **Mitigation:** Update the `langroid` package to version 0.65.2 or later.
- **Vendor Advisory:** https://github.com/advisories/GHSA-q9p7-wqxg-mrhc

---

## 4. 🟠 Zero-Day — Prompt Injection Attacks Trick AI Agents Into Making Crypto Payments

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://www.securityweek.com/prompt-injection-attacks-trick-ai-agents-into-making-crypto-payments/>

> Researchers uncovered two campaigns embedding indirect prompt injections in malicious websites to exploit autonomous AI agents browsing the web. The post Prompt Injection Attacks Trick AI Agents Into Making Crypto Payments appeared first on SecurityWeek .

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability involves indirect prompt injection, where malicious content on a website influences an AI agent's behavior. A specific manifestation, CVE-2026-0628, is an XSS vulnerability in Chrome's WebView tag that allowed for local file access and privacy invasion.
- **Affected Products:** Google Chrome (specifically Gemini agentic capabilities and the WebView tag)
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Exploit Available:** A public proof-of-concept (PoC) for the associated CVE-2026-0628 is available at https://github.com/fevar54/CVE-2026-0628-POC
- **Patch Available:** Yes, Google released a patch for the associated vulnerability CVE-2026-0628.
- **Active Exploitation:** No known exploits have been reported in the wild as of January 6, 2026.
- **Threat Actors:** None known
- **Mitigation:** Google implemented layered defenses including a 'user alignment critic' (an isolated model that vets agent actions), origin access restrictions, and prevention of unsafe AI actions.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** A linear buffer overflow vulnerability in CrabbyAVIF caused by incorrect bounds checks in multiple locations, leading to out-of-bounds (OOB) memory accesses. This vulnerability could potentially allow for remote code execution (RCE).
- **Affected Products:** CrabbyAVIF (Android ecosystem)
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** No public exploit code is currently available.
- **Patch Available:** Yes, the vulnerability was patched before shipping. Information is available in the vendor advisory (http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html).
- **Active Exploitation:** No confirmed active exploitation in the wild has been reported; the vulnerability was caught before shipping.
- **Threat Actors:** None known
- **Mitigation:** The vulnerability was identified and patched before being shipped in a production release.
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Chinese state-sponsored actors target network edge devices (backbone, provider edge, and customer edge routers) by exploiting publicly known CVEs, such as CVE-2024-21887 (Ivanti), CVE-2024-3400 (Palo Alto Networks), and CVE-2018-0171 (Cisco). Post-compromise, they maintain persistence and facilitate espionage by modifying routing tables, establishing GRE/IPsec tunnels, abusing SNMP for configuration changes, and executing Tcl scripts to siphon data.
- **Affected Products:** Cisco IOS and IOS XE, Palo Alto Networks PAN-OS GlobalProtect, Ivanti Connect Secure, Ivanti Policy, Fortinet firewalls, Juniper firewalls, Microsoft Exchange, Nokia routers and switches, Sierra Wireless devices, Sonicwall firewalls
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Publicly known exploits and proof-of-concepts exist for the individual CVEs targeted in this campaign (e.g., CVE-2024-3400 and CVE-2024-21887).
- **Patch Available:** Official patches have been released by individual vendors for the targeted CVEs; however, no single patch exists for the entire campaign.
- **Active Exploitation:** Confirmed active exploitation by PRC state-sponsored actors targeting global telecommunications, government, transportation, and military infrastructure, as reported by CISA in Alert AA25-239A.
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Implement a multi-layered defense strategy including advanced EDR, strict network segmentation, zero-trust principles, phishing-resistant MFA, and regular threat hunting. Additionally, disable the web UI feature on Cisco IOS XE devices vulnerable to CVE-2023-20198.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 11. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

---

## 12. 🟠 Zero-Day — Browser Security: Zero-Days Are Only Part of the Problem

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 30, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/browser-security-zero-days-are-only-part-of-the-problem/>

---

## 13. 🟠 Zero-Day — 94% of Organizations Report Cloud Breaches: CrowdStrike State of CDR Survey

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 22, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/crowdstrike-state-of-cdr-survey-key-takeaways/>

---

## 14. 🟡 High Severity — CERT/CC Warns of Hidden Admin Backdoor in Tenda Router Firmware

**CVE:** `CVE-2026-11405` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://thehackernews.com/2026/07/certcc-warns-of-hidden-admin-backdoor.html>

> Several versions of firmware released by Chinese network device manufacturer Tenda have been found to embed an undocumented authentication backdoor that enables administrative access to the devices&#x27; web management interfaces, the CERT Coordination Center (CERT/CC) warned Monday.

&quot;An attacker can exploit this vulnerability, tracked as CVE-2026-11405, to bypass the password verification p…

---

## 15. 🟡 High Severity — OPNsense XPATH Injection (CVE-2026-53582)

**CVE:** `CVE-2026-53582` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://seclists.org/fulldisclosure/2026/Jul/18>

> Posted by evan on Jul 06 SUMMARY: a stored XPATH injection allows any user with just ca manager/certificate manager perms to leak any secret key/any value in config.xml, thus achieving privilege escalation and potentially remote code execution. this can also likely be chained via csrf and some clever hiding. see https://github.com/opnsense/core/security/advisories/GHSA-xww7-76m6-mh2r == VULN == th…

---

## 16. 🟡 High Severity — BeyondTrust Patches Critical Auth Bypass Flaws in Remote Support and PRA

**CVE:** `CVE-2026-40138` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-07
**Reference:** <https://thehackernews.com/2026/07/beyondtrust-patches-critical-auth.html>

> BeyondTrust has released updates to address two critical security flaws affecting Remote Support (RS) and Privileged Remote Access (PRA) products that, if successfully exploited, could allow unauthenticated attackers to take control of susceptible devices.

The vulnerabilities are listed below -


  CVE-2026-40138 (CVSS score: 9.2) - A pre-authentication vulnerability exists in the

---

## 17. 🟡 High Severity — mknod: Device nodes created mislabeled on SELinux, with broken cleanup (remove_dir on a node)

**CVE:** `CVE-2026-35361` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-r9hw-mj3w-phcq>

> uutils calls `mknod` *before* setting the SELinux context (GNU uses `setfscreatecon` first, labeling atomically). If `set_selinux_security_context` fails, cleanup uses `std::fs::remove_dir`, which cannot remove device nodes or FIFOs, leaving the mislabeled node behind.

**Impact:** on SELinux-enforcing systems the node is created with the wrong context; the command reports failure but leaves a mis…

---

## 18. 🟡 High Severity — mkfifo: permissions of an existing file are changed after FIFO creation fails

**CVE:** `CVE-2026-35341` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-pmf6-rcx4-v53v>

> When `mkfifo()` fails (e.g. target already exists), the code shows an error but is missing a `continue;`, so it falls through to `fs::set_permissions` and changes the permissions of the pre-existing file to the default FIFO mode (`0o666` &amp; umask -&gt; `0644`).

```
$ touch secret; chmod 000 secret
$ coreutils mkfifo secret fifo3 fifo4
mkfifo: cannot create fifo &#x27;secret&#x27;: File exists
…

---

## 19. 🟡 High Severity — 9routers has Exposure of Sensitive Information and Unprotected Database Import/Export, Allowing Complete Credential Theft and Database Takeover

**CVE:** `CVE-2026-55500` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-qvfm-67h2-2qfx>

> ## Summary

The `/api/settings/database` endpoint allows full database export (containing all credentials, API keys, OAuth tokens, and settings) and full database import (complete overwrite) without any authentication requirement beyond the `ALWAYS_PROTECTED` middleware check, which only validates JWT or CLI token. Combined with other vulnerabilities (e.g., default password, tunnel exposure), this…

---

## 20. 🟡 High Severity — Craft CMS: Potential authenticated Remote Code Execution via referrer redirect

**CVE:** `CVE-2026-55794` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-f74w-488g-8x5r>

> ### Requirements:

* Control panel access
* Permissions to edit an entry

### Details

Control panel users with the ability to edit entries can execute unsandboxed Twig code via the HTTP Referrer header.

The issue happens when a user is saving entries. Strings for a signed redirect URL are being compiled as a Twig template via `renderObjectTemplate()`, and while a sandboxed alternative already ex…

---

## 21. 🟡 High Severity — Linuxfabrik Monitoring Plugins have local privilege escalation using embedded command

**CVE:** `CVE-2026-55426` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-798h-hpph-m24j>

> ### Summary
When a check plugin places user provided input inside a command which is passed to `shell_exec`, an attacker can abuse this to run arbitrary commands. This is mainly dangerous for plugins which are listed in the sudoers file, because this allows an attacker controlling the nagios user to get root privileges.

### Details
An example for this is the `restic-check` plugin, where the `--re…

---

## 22. 🟡 High Severity — Suspended Coder users retain access to AI Bridge LLM proxy endpoints

**CVE:** `CVE-2026-55435` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-wqxv-w64v-5wh6>

> ### Summary

AI Bridge proxy endpoints authenticate via `Server.IsAuthorized` in `coderd/aibridgedserver`, which validates key format, expiry, secret and deleted or system users but does not check whether the account is suspended. Because suspension does not revoke existing API keys, a suspended user&#x27;s unexpired token keeps working.

&gt; **Note:** Practical impact is limited to already-issue…

---

## 23. 🟡 High Severity — Coder: Devcontainer recreate endpoint missing write authorization allows read-only roles to destroy containers

**CVE:** `CVE-2026-55433` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-jqj2-x4c5-jfxm>

> ### Summary

The devcontainer recreate endpoint relied on route middleware that checked only `ActionRead` on the workspace and, unlike the sibling delete endpoint, performed no `ActionUpdate` check before triggering the destructive rebuild.

&gt; **Note:** Exploitation requires an existing low-privilege role with access to the target workspace.

### Impact

Any authenticated principal with read-on…

---

## 24. 🟡 High Severity — Coder: User-admin role can reset owner account password

**CVE:** `CVE-2026-55077` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-29xf-69gq-m9jx>

> ### Summary

The `PUT /api/v2/users/{user}/password` endpoint authorized only `ActionUpdatePersonal` and did not prevent a `user-admin` from resetting an `owner` account&#x27;s password. It also did not require the current password when an admin reset another user&#x27;s password.

&gt; **Note:** Exploitation requires the privileged `user-admin` role so practical risk is limited to deployments tha…

---

## 25. 🟡 High Severity — Coder vulnerable to OIDC account takeover via email-based user matching and email_verified bypass

**CVE:** `CVE-2026-55075` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-9r87-mvcw-x35f>

> ### Summary

Two flaws in Coder&#x27;s OIDC login chained into account takeover: email-based user matching fell back to linking by email without checking for an existing link to a different IdP subject and the `email_verified` claim was only enforced when present as a boolean `false` so an absent or non-boolean claim was treated as verified.

### Impact

An attacker who could authenticate at the c…

---

## 26. 🟡 High Severity — Coder's OIDC email_verified type coercion bypass enables account takeover via unverified email linking

**CVE:** `CVE-2026-55076` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-75vm-6w67-gwvp>

> ### Summary

Coder&#x27;s OIDC callback checked `email_verified` with a direct Go `bool` type assertion. When an IdP returned the claim as a non-boolean (for example the string `&quot;false&quot;`) or omitted it, the assertion failed open and the email was treated as verified. Combined with an unconditional email-based account fallback, this enabled account takeover.

### Impact

An attacker who r…

---

## 27. 🟡 High Severity — OpenRemote has Cross-Realm User Information Disclosure in UserResourceImpl

**CVE:** `CVE-2026-54641` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-xqr9-4wvv-gvch>

> ### Summary

A realm admin of tenant B can read the profile, client roles, and realm roles of any user in any other realm (including the master realm) by supplying the target user&#x27;s UUID in the REST API path. Three read endpoints in UserResourceImpl check whether the caller holds the read:admin role but omit a check that the target user belongs to the caller&#x27;s own realm. The vulnerabilit…

---

## 28. 🟡 High Severity — GoFiber never set HSTS header in helmet middleware due to incorrect protocol check

**CVE:** `CVE-2026-53624` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-gv83-gqw6-9j2c>

> ### Summary

The `helmet` middleware in gofiber/fiber never sets the `Strict-Transport-Security` (HSTS) response header, even when `HSTSMaxAge` is explicitly configured, because the condition check at `helmet.go:67` uses `c.Protocol()` — which returns the HTTP protocol version string (e.g., `&quot;HTTP/1.1&quot;`, `&quot;HTTP/2.0&quot;`) — instead of `c.Scheme()` — which returns the URL scheme (`&…

---

## 29. 🟡 High Severity — Langroid: handle_message() executes user-supplied tool JSON without sender verification 

**CVE:** `CVE-2026-54771` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-gjgq-w2m6-wr5q>

> ## Summary

A Langroid application exposing a chat interface to untrusted users may allow direct tool invocation via raw JSON payloads, even when tools are registered with `use=False, handle=True`.

## Details

`enable_message(..., use=False, handle=True)` only prevents the LLM from being instructed to generate the tool. The tool dispatch path in `agent_response()` → `handle_message()` → `get_tool…

---

## 30. 🟡 High Severity — Dragonfly scheduler v1 and v2 gRPC unauthenticated SSRF via attacker-controlled PeerHost in DownloadTinyFile

**CVE:** `CVE-2026-54637` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-chwm-m7g7-685g>

> ## Summary

The Dragonfly **scheduler**&#x27;s v1 gRPC service contains an unauthenticated Server-Side Request Forgery (SSRF). When a peer reports a successful download of a TINY task, the scheduler calls `Peer.DownloadTinyFile()` and issues an HTTP `GET` to a host and port taken verbatim from the attacker-controlled `PeerHost.Ip` / `PeerHost.DownPort` fields of the gRPC request body. The HTTP cli…

---

## 31. 🟡 High Severity — Decompress: Archive extraction can create files and links outside of the target directory

**CVE:** `CVE-2026-53486` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-mp2f-45pm-3cg9>

> ### Impact

When extracting an archive to a directory, a crafted archive can read or write files outside that directory. The flaw is in the code that writes the parsed entries, so it affects every format decompress handles: tar, tar.gz, tar.bz2, and zip by default, plus any others added through the plugins option.

A link (hardlink) or symlink entry is created without checking where its target poi…

---

## 32. 🟡 High Severity — mv: symlinks expanded during cross-device move (resource exhaustion / data duplication)

**CVE:** `CVE-2026-35365` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-h444-6j9x-p8vh>

> When moving directories across filesystems, uutils `mv` dereferences symlinks inside the tree, copying their targets as real files/dirs instead of preserving the symlinks. GNU preserves symlinks by default. E.g. a `etc_link -&gt; /etc` inside the source becomes a full copy of `/etc` at the destination.

**Impact:** (1) resource exhaustion — a small tree can expand into a huge copy (time/disk DoS);…

---

## 33. 🟡 High Severity — id: groups= computed from real GID instead of effective GID

**CVE:** `CVE-2026-35370` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-47c7-qrm7-mqw7>

> The id utility in uutils coreutils miscalculates the groups= section of its output. The implementation uses a user&#x27;s real GID instead of their effective GID to compute the group list, leading to potentially divergent output compared to GNU coreutils. Because many scripts and automated processes rely on the output of id to make security-critical access-control or permission decisions, this dis…

---

## 34. 🟡 High Severity — install: TOCTOU symlink race (unlink-then-create without O_EXCL) allows arbitrary file overwrite

**CVE:** `CVE-2026-35355` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-239g-2685-54x3>

> `copy_file` in `install/src/install.rs` removes the destination then recreates it by pathname via `File::create` / `fs::copy` without `O_EXCL`/`create_new`. Between the unlink and the recreate, a local attacker with write access to the destination directory can drop in a symlink and redirect the write.

**Impact:** when `install` runs privileged into an attacker-writable directory (staging/build p…

---

## 35. 🟡 High Severity — ln: rejects non-UTF-8 source filenames in target-directory mode

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

## 36. 🟡 High Severity — chmod: --preserve-root bypassed by any path that resolves to root (e.g. /../)

**CVE:** `CVE-2026-35338` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-4c7q-4928-8445>

> `Chmoder::chmod()` only compares the literal argument against `Path::new(&quot;/&quot;)`, so the `--preserve-root` guard is bypassed by any path that *resolves* to root — a symlink to `/` or simply `/../`.

```
if self.recursive &amp;&amp; self.preserve_root &amp;&amp; file == Path::new(&quot;/&quot;) {
    return Err(ChmodError::PreserveRoot(&quot;/&quot;.to_string()).into());
}
```

**PoC** — re…

---

## 37. 🟡 High Severity — 16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems

**CVE:** `CVE-2026-53359` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://thehackernews.com/2026/07/16-year-old-linux-kvm-flaw-lets-guest.html>

> A use-after-free bug in Linux&#x27;s KVM hypervisor can be triggered from a guest virtual machine to corrupt the shadow-page state of the host kernel that runs it.

Dubbed &#x27;Januscape&#x27; and tracked as CVE-2026-53359, the flaw sits in the shadow MMU code that KVM shares across both Intel and AMD. The public proof-of-concept panics the host; the researcher claims that a separate, unreleased …

---

## 38. 🟡 High Severity — flyto-core has SSRF guard bypass via IPv6 transition addresses (IPv4-mapped / 6to4 / NAT64) in validate_url_ssrf

**CVE:** `CVE-2026-55787` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-794r-5rp2-fpg8>

> ## Summary

`flyto-core`&#x27;s SSRF protection (`validate_url_ssrf` / `is_private_ip` in `src/core/utils.py`) blocks private and metadata destinations by resolving the host and testing the resulting IP for membership in a hardcoded `PRIVATE_IP_RANGES` list. That list contains only the *native* RFC 1918 / loopback / link-local / unique-local ranges. It does **not** account for IPv6 transition addr…

---

## 39. 🟡 High Severity — Cilium vulnerable to sensitive information disclosure and cluster disruption via local Envoy admin socket access

**CVE:** `CVE-2026-49445` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-3fcv-jvfp-m4q9>

> ### Impact

When Cilium L7 functionality is enabled on a cluster, the Envoy instance supporting this functionality creates a world-accessible socket on cluster nodes. A local attacker would be able to access Envoy admin endpoints. Depending on deployment configuration, this can expose sensitive information or allow disruptive administrative operations, such as:

- Exposing TLS secrets
- Disrupting…

---

## 40. 🟡 High Severity — Formie Hidden field defaults vulnerable to Server-Side Template Injection

**CVE:** `CVE-2026-52889` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://github.com/advisories/GHSA-565m-g33j-jq96>

> ## Summary
Formie Hidden fields could evaluate request-derived values as Twig during front-end form rendering.

When a Hidden field used a dynamic default value such as HTTP User Agent, Referer URL, Current URL, Query Parameter, or Cookie Value, the value was copied from the incoming request and later passed to Craft’s Twig rendering layer. This allowed an unauthenticated attacker to provide Twig …

---

## 41. 🟡 High Severity — Threat Actors Probe Gitea Docker Flaw CVE-2026-20896 13 Days After Disclosure

**CVE:** `CVE-2026-20896` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-06
**Reference:** <https://thehackernews.com/2026/07/threat-actors-probe-gitea-docker-flaw.html>

> Threat actors have been observed attempting to exploit a recently patched critical security flaw in Gitea Docker images, according to Sysdig.

The vulnerability in question is CVE-2026-20896 (CVSS score: 9.8), a vulnerability that stems from the DevOps platform trusting the &quot;X-WEBAUTH-USER&quot; header from any source IP address, effectively allowing an unauthenticated internet client to get …

---

## 42. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
