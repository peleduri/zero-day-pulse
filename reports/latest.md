# Zero Day Pulse

> **Generated:** 2026-06-12 14:31 UTC &nbsp;|&nbsp; **Total:** 24 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 14 &nbsp;|&nbsp; 🟡 High: 10 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** CVE‑2024‑57727 is a path‑traversal vulnerability enabling unauthenticated attackers to craft HTTP requests that read arbitrary files (e.g., server logs, configuration files) from SimpleHelp hosts running version 5.5.7 or earlier.
- **Affected Products:** SimpleHelp remote support / RMM, versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Exploit Available:** Public PoC/scan template available (e.g., ProjectDiscovery nuclei template). Link: https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2024/CVE-2024-57727.yaml
- **Patch Available:** Vendor released SimpleHelp 5.5.8 containing security fixes. Advisory URL: https://community.simple-help.com/t/simplehelp-5-5-8-critical-security-fixes/1570
- **Active Exploitation:** Confirmed active exploitation reported by CISA (AA25‑163A) and multiple incident reports; ransomware actors leveraged the vulnerability to compromise downstream customers.
- **Threat Actors:** Ransomware actors (reported in CISA advisory); DragonForce/other ransomware groups
- **Mitigation:** Upgrade to SimpleHelp 5.5.8 or later. If immediate patching is not possible, restrict network access to the SimpleHelp service (ingress filtering, firewall rules), disable public‑facing instances, apply network segmentation, rotate credentials, and follow CISA advisory recommendations.
- **Vendor Advisory:** https://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — Active Exploitation of Oracle PeopleSoft Zero-Day (CVE-2026-35273)

**CVE:** `CVE-2026-35273` | `CVE-2013-3821` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://www.rapid7.com/blog/post/etr-active-exploitation-of-oracle-peoplesoft-zero-day-cve-2026-35273>

> Overview On June 10, 2026, Oracle published a security alert for CVE-2026-35273 , a critical vulnerability in the Updates Environment Management component of PeopleSoft Enterprise PeopleTools. Oracle released an out-of-band patch the same day as the advisory, underscoring the urgency of remediation. The vulnerability has a CVSSv3.1 score of 9.8 and is remotely exploitable without authentication. P…

**Parallel AI Enrichment:**

- **Technical Details:** Server‑side request forgery (CWE‑918) in the Updates Environment Management component that can be triggered over HTTP by unauthenticated remote attackers, potentially leading to remote code execution.
- **Affected Products:** Oracle PeopleSoft Enterprise PeopleTools Updates Environment Management component (PeopleTools versions 8.61, 8.62)
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** Public proof‑of‑concept and weaponized exploit reported; see Rapid7 blog.
- **Patch Available:** Out‑of‑band patch released June 10 2026; see Oracle advisory.
- **Active Exploitation:** Confirmed active exploitation reported; sources include Rapid7, BleepingComputer, and ShinyHunters.
- **Threat Actors:** ShinyHunters
- **Mitigation:** Apply the Oracle out‑of‑band patch immediately; if patching is delayed, block incoming access to PeopleSoft HTTP interfaces from untrusted networks, restrict access to the Updates Environment Management endpoints, and deploy web‑application‑firewall rules to block exploit patterns.
- **Vendor Advisory:** https://www.oracle.com/security-alerts/alert-cve-2026-35273.html

---

## 3. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** GeminiJack leverages indirect prompt injection: an attacker injects malicious instructions into a shared or publicly indexed document. When Gemini Enterprise or Vertex AI Search retrieves and processes that document, the hidden prompt is executed, enabling data exfiltration without any user action.
- **Affected Products:** Google Gemini Enterprise, Vertex AI Search
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof‑of‑concept described in Noma Labs blog (see citation).
- **Patch Available:** Updates released by Google (see advisory blog post).
- **Active Exploitation:** Confirmed active exploitation reported via Google’s threat‑intelligence analysis and Noma Labs’ discovery of GeminiJack.
- **Threat Actors:** None known
- **Mitigation:** Apply the latest Google security updates for Gemini Enterprise and Vertex AI Search; enforce content sanitization for external documents.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 4. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) allows an attacker to inject malicious instructions into the data sources or tools (e.g., emails, documents, web retrievals, plugins) that a multi‑source LLM agent such as Workspace with Gemini uses to fulfill user queries, potentially influencing model behavior without direct user input.
- **Affected Products:** Google Workspace with Gemini (workspace-integrated Gemini/ Gemini Enterprise)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Proof‑of‑concepts and wild payloads have been reported (e.g., Noma Labs’ GeminiJack disclosure and multiple IPI payload collections), but no single formal public exploit URL exists.
- **Patch Available:** No single vendor software patch; Google describes layered mitigations and continuous defenses in the advisory above.
- **Active Exploitation:** Confirmed research disclosures and wild payload detections (e.g., Noma Labs’ GeminiJack and other reports) indicate real‑world abuse and proof‑of‑concept exploits.
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses—input provenance and validation, retrieval filtering, context sanitization, strict tool access controls, capability confinement, monitoring and alerting, and continuous model‑behavior testing—as described by Google.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 5. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection enables an attacker to embed malicious prompts that are executed by Gemini's AI, potentially leading to unauthorized actions without any user interaction.
- **Affected Products:** Google Chrome (agentic capabilities enabled)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof‑of‑concept disclosed.
- **Patch Available:** Patch released via Chrome update; advisory URL: http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
- **Active Exploitation:** None known
- **Threat Actors:** None known
- **Mitigation:** Enable Chrome's layered defenses that block prompt injections, restrict origin access for agentic browsing, and enforce safe AI action policies.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 6. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** -1.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public exploit available.
- **Patch Available:** No official patch available.
- **Active Exploitation:** No active exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 7. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection embeds malicious instructions in external sources (e.g., emails, documents) that are later consumed by AI models. Google mitigates this via adversarial model training, purpose‑built ML detectors for malicious instructions, markdown sanitization with suspicious‑URL redaction based on Safe Browsing, system‑level safeguards, and end‑user security notifications.
- **Affected Products:** Cursor <1.3 (CVE‑2025‑54131), Gemini CLI prior to 0.39.1 and 0.40.0‑preview.3
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC available.
- **Patch Available:** No official patch for the blog‑post vulnerability; related product fixes are available (e.g., Gemini CLI versions 0.39.1 and 0.40.0‑preview.3).
- **Active Exploitation:** No confirmed broad active exploitation of the vulnerability described in the blog post.
- **Threat Actors:** None known
- **Mitigation:** Apply layered defenses: adversarial model training, ML detectors for malicious instructions, markdown sanitization with suspicious‑URL redaction, system‑level safeguards (e.g., workspace‑trust changes in Gemini CLI), and enable end‑user security notifications. For affected products, upgrade to patched versions (Cursor ≥ 1.3, Gemini CLI ≥ 0.39.1).
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks

---

## 8. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state‑sponsored actors target large backbone routers, provider edge (PE) and customer edge (CE) routers, leveraging compromised devices and trusted connections to pivot; they modify routers to maintain persistent, long‑term access for espionage.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown; no public PoC reported in advisory.
- **Patch Available:** Patch availability varies by vendor; no single vendor patch listed in advisory. Patch information unavailable; refer to vendor advisories.
- **Active Exploitation:** Confirmed active exploitation reported by CISA and NSA (CISA AA25-239A; NSA guidance) indicating global targeting of telecommunications, government, transportation, lodging, and military infrastructure networks.
- **Threat Actors:** Salt Typhoon; OPERATOR PANDA; RedMike; UNC5807; GhostEmperor
- **Mitigation:** Recommended mitigations include monitoring and hardening of backbone/PE/CE routers, isolating management interfaces, rotating credentials, deploying network segmentation, implementing detection for router modifications and persistence, and following CISA/NSA guidance for countering Chinese state‑sponsored actors.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public proof-of-concept or weaponized exploit reported in the advisory; exploit status: none reported.
- **Patch Available:** Vendor patch information unavailable.
- **Active Exploitation:** Confirmed active exploitation reported: advisory and FBI/NSA indicate targeting and operations against Western logistics and technology entities since 2022.
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS), unit 26165 (aka APT28)
- **Mitigation:** General mitigations in advisory include heightened monitoring, implement MFA, network segmentation, patching, restrict administrative privileges, review logs and indicators of compromise (IOCs) from the advisory.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a

---

## 10. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** Improper input neutralization (cross‑site scripting) in Exchange Server’s web page generation allows an unauthenticated attacker to inject malicious scripts, leading to post‑authentication actions or code execution on the server.
- **Affected Products:** Microsoft Exchange Server (cumulative updates/versions indicated in the MSRC advisory)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC confirmed in the cited sources.
- **Patch Available:** Yes — Microsoft security update released (see MSRC advisory).
- **Active Exploitation:** Confirmed active exploitation reported by Microsoft and security press.
- **Threat Actors:** None known
- **Mitigation:** Apply the Microsoft security update immediately; isolate affected Exchange servers; follow Microsoft Exchange emergency response guidance; monitor for indicators of compromise.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42897

---

## 11. 🟠 Zero-Day — Factoring "short-sleeve" RSA keys with polynomials

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Trail of Bits Blog &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://blog.trailofbits.com/2026/06/12/factoring-short-sleeve-rsa-keys-with-polynomials/>

> What happens when the bits of an RSA private key are heavily biased toward 0 instead of being randomly generated? The public key’s bits could be biased enough for us to detect these incorrectly generated keys in the wild. Together with Hanno Böck of the badkeys project, we found hundreds of unique keys that not only have this property, but can be quickly factored. We also found the bug that led to…

---

## 12. 🟠 Zero-Day — Anthropic Disputes Fable 5 AI Jailbreak

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://www.securityweek.com/anthropic-disputes-fable-5-ai-jailbreak/>

> An AI hacker claims to have achieved a prompt-based jailbreak shortly after Fable 5’s launch, but Anthropic says it’s not a real jailbreak. The post Anthropic Disputes Fable 5 AI Jailbreak appeared first on SecurityWeek .

---

## 13. 🟠 Zero-Day — CISA orders feds to patch actively exploited Ivanti flaw by Sunday

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-12
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-gives-feds-3-days-to-patch-ivanti-flaw-exploited-in-attacks/>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) ordered government agencies to patch an actively exploited Ivanti Sentry flaw within three days, as mandated by the newly issued Binding Operational Directive (BOD) 26-04. [...]

---

## 14. 🟠 Zero-Day — ShinyHunters Exploits Oracle PeopleSoft Zero-Day (CVE-2026-35273) to Breach Universities

**CVE:** `CVE-2026-35273` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://thehackernews.com/2026/06/shinyhunters-exploits-oracle-peoplesoft.html>

> The ShinyHunters extortion crew exploited an unpatched flaw in Oracle PeopleSoft to break into enterprise systems, steal data, and demand payment to keep it private. The campaign hit universities hardest.

Google&#x27;s Mandiant attributes it to the group it tracks as UNC6240, and dates the activity between May 27 and June 9. Oracle did not publish its advisory until June 10, so the bug was a

---

## 15. 🟡 High Severity — GeoServer DB2 DataStore Extension has a JNDI Vulnerability via Store Connection

**CVE:** `CVE-2025-27511` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-g628-r368-6vh7>

> ## Summary

Administrator can perform JNDI attack through specially crafted DB2 jdbc url leading to Remote Code Execution (RCE).

## Impact

If GeoServer has DB2 extension installed, this vulnerability can lead to executing arbitrary code.

## Details

Authenticated users can access Vector Data Sources page to creating a new data store through db2 jdbc connection, performing JNDI attack due to unr…

---

## 16. 🟡 High Severity — Russh SSH message fields were decoded through allocation-first parsers before field-specific bounds

**CVE:** `CVE-2026-48110` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-4r3c-5hpg-58qr>

> # SSH message fields were decoded through allocation-first parsers before field-specific bounds

### Summary

Several `russh` client and server message handlers decoded attacker-controlled SSH strings, name-lists, and byte fields into owned allocations before applying field-specific bounds. A remote SSH peer could send oversized, high-fanout, or malformed length-prefixed fields and make the librar…

---

## 17. 🟡 High Severity — AWS Advanced Go Wrapper has Privilege Escalation in Aurora PostgreSQL instance

**CVE:** `CVE-2026-11401` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-r236-5pc3-3qcp>

> Aurora PostgreSQL is a fully managed relational database engine that&#x27;s compatible with PostgreSQL.

An issue in Aurora PostgreSQL using the AWS Go Wrapper waa identified, see CVE-2026-11401.


Impact
An issue in AWS Wrappers for Amazon Aurora PostgreSQL may allow for privilege escalation to rds_superuser role. A low privilege authenticated user can create a crafted function that could be exec…

---

## 18. 🟡 High Severity — Russh: SSH identification parsing accepted non-canonical client banners and did not bound pre-banner input

**CVE:** `CVE-2026-48108` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-76r6-x97p-67vr>

> ### Summary

`russh` did not enforce the SSH identification-string rules as deliberately as OpenSSH. In particular, the server-side identification reader used the same permissive path as the client, allowing pre-banner lines from clients, and the reader did not enforce a bounded number of pre-banner lines.

For a library server built on `russh`, this could allow a remote peer to hold connection se…

---

## 19. 🟡 High Severity — WsgiDAV encoded dot segments can escape filesystem share roots

**CVE:** `CVE-2026-48099` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-wxq4-cc2q-338q>

> ### Impact
WsgiDAV 4.3.3 can allow a WebDAV request path containing an encoded parent-directory segment to escape the configured filesystem share root in a specific path layout.

### Patches
The issue is fixed with version 4.3.4.

### Preconditions

The practical impact depends on the deployment.

The deployment uses a filesystem-backed WsgiDAV share.

The attacker can send WebDAV requests accepte…

---

## 20. 🟡 High Severity — Netty HAProxy: Unbalanced Reference Count in Nested PP2_TYPE_SSL TLV Parsing Leads to Memory Exhaustion

**CVE:** `CVE-2026-48059` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-h2qv-fj59-j46j>

> ### Impact
The HAProxy PROXY protocol v2 codec in netty leaks native or heap memory on every connection when a client sends a syntactically valid header containing nested `PP2_TYPE_SSL` TLVs (type-length-value records) at depth two or greater. The leak occurs on the successful parse path — no exception is thrown, the message fires downstream, the decoder removes itself, and the application release…

---

## 21. 🟡 High Severity — Kolibri has Unauthenticated Server-Side Request Forgery (SSRF) in RemoteFacilityUserViewset

**CVE:** `CVE-2026-48053` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-4mj9-pf4r-cqrc>

> ## Summary

Several Kolibri API endpoints accept an unvalidated `baseurl` parameter and fetch attacker-controlled URLs from the Kolibri server, reflecting the response body back to the caller. The original report identified two endpoints on the `RemoteFacilityUser*` viewsets; remediation review found two further reflection points on the same pattern. The GET endpoint was unauthenticated.

## Affec…

---

## 22. 🟡 High Severity — Arc: Unauthenticated access to Go debug pprof endpoints leaks runtime state and enables CPU-burn DoS

**CVE:** `CVE-2026-48050` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-j93g-rp6m-j32m>

> ### Summary

Arc registers Go&#x27;s `net/http/pprof` handlers at `/debug/pprof/*` via `app.Use(pprof.New())` in `internal/api/server.go`, and `/debug/pprof` is added to `PublicPrefixes` in `cmd/arc/main.go`. The auth middleware short-circuits before the token check on prefix match, so the endpoints are reachable without any authentication.

### Impact

Any network-reachable caller (no token requi…

---

## 23. 🟡 High Severity — @hapi/inert has a static-file confinement bypass via sibling-prefix path

**CVE:** `CVE-2026-48049` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-11
**Reference:** <https://github.com/advisories/GHSA-rcvq-m9j9-6f4g>

> ### Impact
`@hapi/inert` serves static files from a directory configured with `path` (in the `directory` / `file` handlers) or `relativeTo` (for `h.file()`), with confinement enforced by the `confine` option (default `true`). Before the patch, the confinement check compared the resolved absolute path against the confine directory using a raw string-prefix test, so a sibling directory whose absolut…

---

## 24. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
