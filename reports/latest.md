# Zero Day Pulse

> **Generated:** 2026-06-17 02:33 UTC &nbsp;|&nbsp; **Total:** 41 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 15 &nbsp;|&nbsp; 🟡 High: 26 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Unauthenticated path traversal vulnerability in SimpleHelp RMM permits remote attackers to retrieve sensitive files (e.g., logs, configuration, credentials) by manipulating file‑path inputs to access directories outside the intended scope.
- **Affected Products:** SimpleHelp remote support / RMM, versions 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Ransomware actors (e.g., DragonForce and other unspecified ransomware operators)
- **Mitigation:** Apply SimpleHelp 5.5.8 or later; if immediate patching is not possible, isolate internet‑facing SimpleHelp instances, restrict access with firewalls or VPNs, rotate any exposed credentials, and monitor for indicators of compromise.
- **Vendor Advisory:** https://broadcom.com/support/security-center/protection-bulletin/cve-2024-57727-simplehelp-directory-traversal-vulnerability

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** GeminiJack leverages an indirect prompt injection inside Google Gemini Enterprise, exploiting the trust boundary between user‑controlled data sources and the AI model's instruction parsing, allowing attackers to inject malicious prompts without direct interaction.
- **Affected Products:** Google Gemini Enterprise
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Exploit availability unknown.
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** None known
- **Mitigation:** Apply the Google‑released patch for Gemini Enterprise immediately. In the meantime, restrict the ingestion of untrusted data sources, employ content sanitisation, and monitor for anomalous AI behaviour.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) occurs when attackers embed malicious instructions into data sources or tools consumed by an LLM (e.g., documents, web content, tool outputs). The LLM may then follow those instructions during query processing, potentially without any direct user input, leading to unintended behavior.
- **Affected Products:** Google Workspace with Gemini
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply deterministic defenses such as user confirmation prompts, URL sanitization, and tool‑chaining policies; employ ML‑based retraining with synthetic attack variants; use LLM‑based prompt engineering and model hardening; conduct red‑team testing and participate in the Google AI Vulnerability Rewards Program.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection allows malicious or third‑party web content to influence an agentic AI by injecting prompts or instructions. Chrome mitigates this with layered defenses: restricting origin access, sandboxing agent contexts, runtime monitors, and a supervising agent that watches agent actions.
- **Affected Products:** Chrome (agentic/Gemini browsing features)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Use the latest Chrome build with agentic protections enabled, block untrusted content, restrict origin access, and rely on Chrome’s layered defenses (prompt‑injection filters, sandboxing, runtime monitors, supervising agent).
- **Vendor Advisory:** https://blog.google/security/architecting-security-for-agentic

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Follow Android Security Bulletin updates, apply vendor/OS updates when available; general hardening (least privilege, sandboxing).
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2026/2026-06-01

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) – hidden malicious instructions embedded within external data sources (emails, documents, calendar invites) that cause AI agents (e.g., Gemini) to execute rogue actions such as data exfiltration; chaining IPI with other vulnerabilities can trigger exploits.
- **Affected Products:** Google Gemini (Google Workspace), Google Gemini app (version 1.3 fixed)
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Layered defense strategy: input sanitization/validation, retrieval filtering, strict access controls, model‑side defenses, minimization of sensitive context exposure, telemetry/monitoring, and rapid patching; upgrade to fixed vendor versions (>=1.3).
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 7. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable
- **CVSS Vector:** CVSS vector unavailable
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** true
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Update software/firmware to patched versions, apply vendor advisories, audit router configurations and firmware integrity, segment networks and limit trusted connections, rotate credentials and keys, monitor for indicators of compromise and unusual routing/telemetry, and follow CISA/NSA mitigation guidance.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

---

## 8. 🟠 Zero-Day — Russian GRU Targeting Western Logistics Entities and Technology Companies

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 12 Ma
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a>

> Executive Summary This joint cybersecurity advisory (CSA) highlights a Russian state-sponsored cyber campaign targeting Western logistics entities and technology companies. This includes those involved in the coordination, transport, and delivery of foreign assistance to Ukraine. Since 2022, Western logistics entities and IT companies have faced an elevated risk of targeting by the Russian General…

**Parallel AI Enrichment:**

- **Technical Details:** This is a threat campaign advisory (TTP‑focused) describing Russian GRU 85th GTsSS (military unit 26165) espionage operations against Western logistics and technology organizations since 2022; it details tactics, techniques, and procedures (phishing, credential access, network intrusion, living‑off‑the‑land) rather than a single software vulnerability.
- **Affected Products:** Affected products unavailable.
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true
- **Threat Actors:** Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (85th GTsSS), military unit 26165 (also tracked as APT28).
- **Mitigation:** Follow CSA hardening and operational security recommendations—implement MFA, network segmentation, patching of known vulnerable services, endpoint detection and response, threat hunting using provided IOCs, and supply‑chain/logistics operational risk controls.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 9. 🟠 Zero-Day — June 2026 Patch Tuesday: Microsoft Patches 206 Vulnerabilities Including Three Publicly Disclosed Zero-Days

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Jun 09, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** Technical details unavailable.
- **Affected Products:** Windows Collaborative Translation Framework, Windows BitLocker, DHCP Client Service, Windows Active Directory Domain Services
- **CVSS Score:** 7.8, 6.8, 9.8, 8.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true (https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/)
- **Patch Available:** true (https://msrc.microsoft.com/update-guide/releaseNote/2026-Jun)
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Apply the Microsoft June 2026 security updates to all affected components. No additional vendor‑provided work‑around is mentioned.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/releaseNote/2026-Jun

---

## 10. 🟠 Zero-Day — Pi Agent: Potential XSS in HTML session exports via Markdown URL sanitization bypass

**CVE:** `CVE-2026-54326` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-7v5m-pr3q-6453>

> # Potential XSS in HTML session exports via Markdown URL handling

Pi HTML exports render session Markdown into a static HTML file. Affected versions did not consistently reject unsafe Markdown link and image URL schemes. In versions with scheme filtering, C0 control characters in the URL scheme could bypass the check because browsers normalize those characters before navigation.

## Impact

The r…

**Parallel AI Enrichment:**

- **Technical Details:** HTML session export renders markdown into static HTML using marked v15 without URL scheme sanitization; unsafe schemes (javascript:, vbscript:, data:) in link or image hrefs can execute JavaScript. In implementations that attempted scheme filtering, C0 control characters in the scheme bypass the check because browsers normalize them before navigation.
- **Affected Products:** pi-mono (Pi Agent) version 0.68.1 and earlier versions
- **CVSS Score:** CVSS score unavailable.
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** true
- **Patch Available:** true
- **Active Exploitation:** false
- **Threat Actors:** None known.
- **Mitigation:** Upgrade to the patched release (apply the upstream PR/commit), or implement server‑side/client‑side sanitization: override marked link/image renderers to strip dangerous schemes, normalize and remove C0 control characters before scheme checks, or render links as plain text/no‑op. Disable automatic HTML export sharing until patched.
- **Vendor Advisory:** https://github.com/advisories/GHSA-7v5m-pr3q-6453

---

## 11. 🟠 Zero-Day — Malicious JetBrains Marketplace plugins steal AI API keys from developers

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://www.bleepingcomputer.com/news/security/malicious-jetbrains-marketplace-plugins-steal-ai-api-keys-from-developers/>

> At least 15 malicious plugins found on the JetBrains Marketplace were designed to steal AI API keys from developers. [...]

---

## 12. 🟠 Zero-Day — Google Vertex AI SDK Flaw Let Attackers Hijack Model Uploads via Bucket Squatting

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://thehackernews.com/2026/06/google-vertex-ai-sdk-flaw-let-attackers.html>

> A flaw in the Google Cloud Vertex AI SDK for Python let an attacker with no access to a victim&#x27;s project hijack the victim&#x27;s machine learning model upload and run code inside Google&#x27;s serving infrastructure.

Palo Alto Networks Unit 42, which found and reported the bug through Google&#x27;s bug bounty program, calls the technique &quot;Pickle in the Middle&quot; and said it saw no e…

---

## 13. 🟠 Zero-Day — LangChain: Path traversal and sandbox escape in LangChain file-search middleware and loaders

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-gr75-jv2w-4656>

> ## Summary

Several LangChain components that resolve filesystem paths or expand search patterns do not consistently confine the *resolved* path to the intended root directory. Affected behaviors include: a file-search agent middleware that validates a starting directory but not the search pattern or the resolved target of matched files, so glob patterns and symlinks can reach files outside the co…

---

## 14. 🟠 Zero-Day — Fake Microsoft Alerts Used to Deploy North Korean NarwhalRAT Malware

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://thehackernews.com/2026/06/fake-microsoft-alerts-used-to-deploy.html>

> The North Korean state-sponsored hacking group known as ScarCruft (aka APT37) has been observed using spear-phishing messages impersonating Microsoft Account security notifications to deliver malware called NarwhalRAT.

&quot;The attack email contained a message impersonating an MS account security alert,&quot; the Genians Security Center (GSC) said. &quot;It was designed to create concern over po…

---

## 15. 🟠 Zero-Day — Cisco Releases Security Updates for Actively Exploited SD-WAN Manager Flaw

**CVE:** `CVE-2026-20262` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://thehackernews.com/2026/06/cisco-releases-security-updates-for.html>

> Cisco has released security updates for a medium-severity security flaw in Catalyst SD-WAN Manager that has come under active exploitation in the wild.

The vulnerability, tracked as CVE-2026-20262, carries a CVSS score of 6.5 out of 10.0.

&quot;A vulnerability in the web UI of Cisco Catalyst SD-WAN Manager, formerly SD-WAN vManage, could allow an authenticated, remote attacker to create a file o…

---

## 16. 🟡 High Severity — Gogs: Overwriting critical files results in a denial of service

**CVE:** `CVE-2026-52797` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-pm6v-2h4w-4rp2>

> **Vulnerability type:** Path Traversal
**Impact:** DoS
**Exploitation prerequisite:** authorized user
**Description:** As an authorized user, an intruder can dictate the value which is passed to the `git diff` command which, together with bypassing the filtering of the passed value, allows the user to bypass the target directory and write the result of the comparison to any arbitrary path.
**Resea…

---

## 17. 🟡 High Severity — n8n: SecurityScorecard Node Leaks API Token to User-Controlled Host

**CVE:** `CVE-2026-54304` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-rm2v-h48j-895m>

> ## Impact
An authenticated user with permission to create or modify workflows and access to a SecurityScorecard credential with limited allowed domains could configure the SecurityScorecard node&#x27;s report download operation to target an attacker-controlled URL. The node attached the SecurityScorecard API token to the outbound request, causing the credential to be sent to the attacker-controlle…

---

## 18. 🟡 High Severity — n8n: Cross-Tenant Credential Takeover via Dynamic Credentials EE Endpoints

**CVE:** `CVE-2026-54305` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-2j5h-858j-5mpf>

> ## Impact
Three EE endpoints used by the Dynamic Credentials feature accepted any authenticated n8n session without performing per-resource ownership or scope checks on the target workflow or credential. An authenticated user with no project membership or credential sharing relationship could enumerate credential identifiers, names, and types referenced by any private workflow in the instance, ini…

---

## 19. 🟡 High Severity — Daytona: Cross-org IDOR in organization role update/delete — any org owner can rewrite or destroy another org's roles

**CVE:** `CVE-2026-54322` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-qxvm-pcfm-qc39>

> ### Summary
Daytona&#x27;s organization role update and delete endpoints authorized the caller as an owner of the organization named in the request path, but resolved and mutated the target role by its identifier alone, without verifying the role belonged to that organization. An authenticated user who owns any organization (organizations are self-service) could therefore modify the permissions of…

---

## 20. 🟡 High Severity — Caddy: Windows `file_server` path authorization bypass via encoded backslash

**CVE:** `CVE-2026-52844` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-qrp7-cvwr-j2c6>

> ### Summary

On Windows, Caddy `path` matchers treat `/private\secret.txt` as outside `/private/*`, but `file_server` later resolves the same request path as `private\secret.txt` on disk.

An unauthenticated remote client can request `/private%5csecret.txt` and bypass Caddy path-scoped auth/deny routes protecting `/private/*`.

### Details

The mismatch is between two Caddy code paths:

- `MatchPa…

---

## 21. 🟡 High Severity — Daytona: Public sandbox previews remain accessible for up to one hour after being made private

**CVE:** `CVE-2026-54321` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-ww63-pv5x-vfc8>

> ### Summary
Sandbox previews that were switched from public to private could remain reachable without authentication for a short period after the change, due to a cached visibility state that was not invalidated when the sandbox&#x27;s visibility changed.

### Impact
When a sandbox owner changed a preview from public to private, the preview proxy could continue serving unauthenticated requests to …

---

## 22. 🟡 High Severity — Traefik: HTTP/3 mTLS bypass via exact SNI TLSOptions lookup for wildcard and mixed-case hosts

**CVE:** `CVE-2026-53622` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-9cr8-q42q-g8m7>

> ## Summary

There is a critical vulnerability in Traefik&#x27;s HTTP/3 (QUIC) TLS configuration selection that allows unauthenticated clients to bypass router-specific mTLS enforcement. When HTTP/3 is enabled on an entrypoint, the TLS handshake selects the applicable TLS configuration through an exact, case-sensitive lookup on the SNI value, which fails to match wildcard host patterns (e.g., `*.ex…

---

## 23. 🟡 High Severity — Crawl4AI: SSRF via proxy settings in the Docker server bypasses the crawl-URL SSRF check

**CVE:** `CVE-2026-53755` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-6qhc-x826-342c>

> ### Summary

The Docker API server applied its SSRF destination check to the crawl target URL only, not to the proxy address. An unauthenticated request could supply a proxy pointing at an internal IP and route the browser through it, reaching internal services and cloud-metadata endpoints, while using a perfectly valid crawl URL. The Docker API is unauthenticated by default.

### Affected paths

…

---

## 24. 🟡 High Severity — Crawl4AI: SSRF filter bypass in Docker server via IPv6 transition forms (NAT64 / 6to4 / unspecified / v4-mapped)

**CVE:** `CVE-2026-53754` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-4qqr-vv2q-cmr5>

> ### Summary

The Docker API server&#x27;s SSRF protection (`validate_webhook_url` / `validate_url_destination` in `deploy/docker/utils.py`) used an explicit IPv4/IPv6 CIDR blocklist that missed several address families. An attacker could reach internal services and cloud metadata endpoints (e.g. `169.254.169.254`) despite the filter by encoding an internal IPv4 address inside an IPv6 transition fo…

---

## 25. 🟡 High Severity — LobeHub: Unauthenticated SSRF in `/webapi/proxy`

**CVE:** `CVE-2026-54157` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-xmwj-c75x-6346>

> ## Unauthenticated SSRF in /webapi/proxy allows anyone to proxy requests and inject cookies on lobehub.com

## Summary

The `/webapi/proxy` endpoint on app.lobehub.com accepts a URL in the POST body and fetches it server-side without any authentication. This is the same proxy code that was vulnerable in CVE-2024-32964, where `/api/proxy` was fixed by adding auth middleware. The `/webapi/proxy` rou…

---

## 26. 🟡 High Severity — Crawl4AI: AST Sandbox Escape via gi_frame.f_back Chain - Pre-Auth RCE in Docker API

**CVE:** `CVE-2026-53753` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-qxjp-w3pj-48m7>

> ### Summary

The `_safe_eval_expression()` function in the computed fields feature uses an AST validator that only blocks attributes starting with underscore. Python generator and frame object attributes (`gi_frame`, `f_back`, `f_builtins`) do NOT start with underscore, enabling a complete sandbox escape to achieve arbitrary code execution.

The attack requires no authentication (JWT disabled by d…

---

## 27. 🟡 High Severity — Deno: Permission Bypass via Unicode Normalization Mismatch on macOS (APFS)

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

## 28. 🟡 High Severity — Deno: BYONM module resolution allows `package.json` main path traversal to bypass `--allow-read` restrictions

**CVE:** `CVE-2026-49406` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-968w-xfqw-vp9q>

> ## Summary

When Deno was run in BYONM mode (`nodeModulesDir: &quot;manual&quot;`), the module resolver did not validate that a package&#x27;s resolved entrypoint stayed within its `node_modules/&lt;pkg&gt;/` directory. A malicious `package.json` whose `main` field contained `..` segments was able to resolve to an arbitrary path on disk, and the resolver then read that file without consulting the …

---

## 29. 🟡 High Severity — n8n: Merge Node SQL Mode Prototype Pollution

**CVE:** `CVE-2026-54311` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-9c38-2mcm-q7f7>

> ## Impact
An authenticated user with permission to create or modify workflows could pollute the sandbox used by the Merge node&#x27;s SQL Query mode. Because the sandbox context was cached and reused across all workflow executions on the instance, prototype mutations introduced by one user&#x27;s workflow persist into subsequent Merge SQL executions belonging to other users or projects. This allow…

---

## 30. 🟡 High Severity — Langflow: Unauthenticated RCE in Shareable Playgrounds

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

## 31. 🟡 High Severity — Astro: XSS via Unescaped Attribute Names in Spread Props

**CVE:** `CVE-2026-54298` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-jrpj-wcv7-9fh9>

> ## Summary

The `spreadAttributes` function in Astro&#x27;s server-side rendering pipeline iterates over object keys and passes them directly to `addAttribute`, which interpolates the key into the HTML output without escaping. When a developer uses the spread syntax `{...props}` on an HTML element and the object keys come from an untrusted source (API, CMS, URL parameters), an attacker can inject …

---

## 32. 🟡 High Severity — Astro: Host header SSRF in prerendered error page fetch

**CVE:** `CVE-2026-54299` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-2pvr-wf23-7pc7>

> ## Summary

Astro SSR apps with prerendered error pages (`/404` or `/500` using `export const prerender = true`) fetch those pages over HTTP at runtime when an error occurs. The URL for this fetch is derived from `request.url`, which in turn gets its origin from the incoming `Host` header. When the `Host` header is not validated against `allowedDomains`, an attacker can point the fetch at an arbit…

---

## 33. 🟡 High Severity — hono: Body Limit Middleware can be bypassed on AWS Lambda by understating `Content-Length`

**CVE:** `CVE-2026-54288` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-rv63-4mwf-qqc2>

> ### Summary

The Body Limit Middleware trusts the request&#x27;s `Content-Length` header to decide whether a body is within the limit. On AWS Lambda (API Gateway v1/v2, ALB, VPC Lattice, and Lambda@Edge) the body is delivered fully buffered and the adapter builds the request with the client-declared `Content-Length`, which need not match the actual payload. A client can declare a tiny `Content-Len…

---

## 34. 🟡 High Severity — hono: Lambda@Edge adapter keeps only the last value of a repeated request header, dropping the rest

**CVE:** `CVE-2026-54289` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-wgpf-jwqj-8h8p>

> ### Summary

On AWS Lambda@Edge, CloudFront delivers a request header that appears more than once as several separate entries. The adapter writes each value with `Headers.set` instead of `Headers.append`, so every value overwrites the previous one and only the last reaches the application. Repeated request headers such as `X-Forwarded-For`, `Forwarded`, and `Via` are silently truncated to a single…

---

## 35. 🟡 High Severity — hono: Path traversal in `serve-static` on Windows via encoded backslash (`%5C`)

**CVE:** `CVE-2026-54286` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-wwfh-h76j-fc44>

> ### Summary

On Windows hosts, an encoded backslash (`%5C`) in the request path decodes to `\`, which the Windows path resolver treats as a separator. `serve-static` then resolves a single URL segment such as `admin\secret.txt` into a nested file under the root and serves it, letting an attacker read static files meant to be protected behind prefix-mounted middleware. Directory escape (`..`) remai…

---

## 36. 🟡 High Severity — hono: AWS Lambda adapter merges multiple `Set-Cookie` headers into one value, dropping cookies on ALB single-header and Lattice

**CVE:** `CVE-2026-54287` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://github.com/advisories/GHSA-j6c9-x7qj-28xf>

> ### Summary

On AWS Lambda, the ALB single-header response and the VPC Lattice v2 response join multiple `Set-Cookie` headers into one comma-separated value. Because commas also appear inside cookie attributes (for example `Expires` dates), clients cannot split the value back into individual cookies and silently drop or misparse them.

### Details

Per RFC 6265, each cookie must be its own `Set-Co…

---

## 37. 🟡 High Severity — Attackers Exploit Three Fortinet FortiSandbox Flaws, One Patched Last Week

**CVE:** `CVE-2026-39813` | `CVE-2026-39808` | `CVE-2026-25089` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://thehackernews.com/2026/06/attackers-exploit-three-fortinet.html>

> Bad actors are exploiting multiple security vulnerabilities in Fortinet FortiSandbox, according to threat intelligence firm Defused Cyber.

In a post shared on X, the company said it has observed exploitation of CVE-2026-39813, CVE-2026-39808, and CVE-2026-25089 over the past 24 hours.

CVE-2026-39813 (CVSS score: 9.1) refers to a path traversal vulnerability in FortiSandbox JRPC API that could

---

## 38. 🟡 High Severity — SEC Consult SA-20260610-0 :: Local Privilege Escalation in Slate Digital Connect (macOS)

**CVE:** `CVE-2026-24066` | `CVE-2026-24067` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://seclists.org/fulldisclosure/2026/Jun/7>

> Posted by SEC Consult Vulnerability Lab via Fulldisclosure on Jun 15 SEC Consult Vulnerability Lab Security Advisory &lt; 20260610-0 &gt; ======================================================================= title: Local Privilege Escalation product: Slate Digital Connect (macOS) vulnerable version: 1.37.0 fixed version: - CVE number: CVE-2026-24066, CVE-2026-24067 impact: high homepage:...

---

## 39. 🟡 High Severity — SEC Consult SA-20260609-0 :: Multiple Local Privilege Escalation Vulnerabilities in Waves Audio - Waves Central

**CVE:** `CVE-2026-24064` | `CVE-2026-24065` &nbsp;|&nbsp; **Source:** Full Disclosure &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://seclists.org/fulldisclosure/2026/Jun/6>

> Posted by SEC Consult Vulnerability Lab via Fulldisclosure on Jun 15 SEC Consult Vulnerability Lab Security Advisory &lt; 20260609-0 &gt; ======================================================================= title: Multiple Local Privilege Escalation Vulnerabilities product: Waves Audio - Waves Central vulnerable version: v13.0.8 - v16.6.0 fixed version: v16.6.2 CVE number: CVE-2026-24064, CVE-2…

---

## 40. 🟡 High Severity — CISA Flags LiteSpeed cPanel Plugin Flaw Exploited for Root Privilege Escalation

**CVE:** `CVE-2026-54420` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-06-16
**Reference:** <https://thehackernews.com/2026/06/cisa-flags-litespeed-cpanel-plugin-flaw.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has added a security flaw impacting LiteSpeed cPanel Plugin to its Known Exploited Vulnerabilities (KEV) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the fixes by June 18, 2026.

The vulnerability in question is CVE-2026-54420 (CVSS score: 8.5), which has been described as a case of privilege

---

## 41. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
