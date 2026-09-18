# Zero Day Pulse

> **Generated:** 2026-09-18 15:24 UTC &nbsp;|&nbsp; **Total:** 41 &nbsp;|&nbsp; 🔴 KEV: 2 &nbsp;|&nbsp; 🟠 Zero-Day: 9 &nbsp;|&nbsp; 🟡 High: 30 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🔴 CISA KEV — CVE-2025-39964 — Linux Kernel Race Condition Vulnerability

**CVE:** `CVE-2025-39964` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2025-39964>

> Vendor: Linux | Product: Kernel. Linux Kernel contains a race condition vulnerability which allows concurrent writes to the same AF_ALG socket causing data to be unpredictably interleaved and creating inconsistencies in the socket&#x27;s internal state. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is a race in the Linux kernel's crypto AF_ALG af_alg_sendmsg path: concurrent writes to the same AF_ALG socket can interleave unpredictably and corrupt the socket's internal state. The fix adds ctx->write ownership tracking so concurrent writers are rejected, including with an -EBUSY response.
- **Affected Products:** Linux kernel with AF_ALG support: affected from 2.6.38 until fixes in 5.10.245, 5.15.194, 6.1.154, 6.6.108, 6.12.49, 6.16.9, and 6.17; Debian bullseye linux 5.10.223-1 was vulnerable, with fixes including 5.10.259-1/5.10.247-1, bookworm 6.1.176-1, and trixie 6.12.95-1
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true - https://cve.imfht.com/detail/CVE-2025-39964?lang=en
- **Patch Available:** true - https://git.kernel.org/stable/c/1b34cbbf4f011a121ef7b2d7d6e6920a036d5285
- **Active Exploitation:** true - https://www.cisa.gov/news-events/alerts/2025/09/04/cisa-adds-three-known-exploited-vulnerabilities-catalog
- **Threat Actors:** None known
- **Mitigation:** Upgrade to a kernel release containing the AF_ALG fix, such as the listed fixed stable-branch versions. If immediate patching is not possible, prevent the af_alg kernel module from loading by blacklisting it, subject to application compatibility requirements.
- **Vendor Advisory:** https://git.kernel.org/stable/c/1b34cbbf4f011a121ef7b2d7d6e6920a036d5285

---

## 2. 🔴 CISA KEV — CVE-2026-53266 — Linux Kernel Out-of-Bounds Write Vulnerability

**CVE:** `CVE-2026-53266` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-53266>

> Vendor: Linux | Product: Kernel. Linux Kernel contains an out-of-bounds write vulnerability in the ebtables SNAT target which allows an ARP sender hardware address rewrite to write directly into a nonlinear socket-buffer fragment backed by a splice-imported file page. The impacted product(s) could be end-of-life (EoL) and/or end-of-service (EoS). Users are advised to discontinue use and/or transit…

**Parallel AI Enrichment:**

- **Technical Details:** The ebtables SNAT target's optional ARP sender-hardware-address rewrite uses skb_store_bits() after only safely reading the ARP header, without first making the target range writable. When that range resides in a nonlinear socket-buffer fragment backed by a splice-imported file page, the operation can write the replacement MAC address directly into the file-backed page, causing an out-of-bounds write and memory corruption. Exploitation requires local access and a system configured with relevant bridge netfilter rules.
- **Affected Products:** Linux kernel, including net/bridge/netfilter/ebt_snat.c: 5.4.73 through <5.5; 5.8.17 through <5.9; 5.9.2 through <5.10.259; 5.11 through <5.15.210; 5.16 through <6.1.176; 6.2 through <6.6.143; 6.7 through <6.12.94; 6.13 through <6.18.36; 6.19 through <7.0.13; and Linux 7.1-rc1 through 7.1-rc6.
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Exploit Available:** true - https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-53266
- **Patch Available:** true - https://git.kernel.org/stable/c/153ea96c806aea395daba907a4f88480b6ad5093
- **Active Exploitation:** true - https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-53266
- **Threat Actors:** None known
- **Mitigation:** Apply the upstream Linux stable-kernel patches or the corresponding distribution kernel updates. If patching is unavailable, disable ARP hardware-address rewriting in ebtables SNAT rules or remove ebtables SNAT rules operating on ARP traffic over bridge interfaces.
- **Vendor Advisory:** https://git.kernel.org/stable/c/153ea96c806aea395daba907a4f88480b6ad5093

---

## 3. 🟠 Zero-Day — Improve Router Hygiene to Protect Against Russian State-Sponsored Targeting

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Wed, 08 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a>

> Russian Government-Sponsored Activity Targets Poorly Configured and Vulnerable Devices Across Critical Sectors Executive summary Russian Federal Security Service (FSB) Center 16 cyber actors continue to exploit poorly configured and vulnerable networking devices worldwide, opportunistically compromising multiple critical infrastructure sector networks. This joint Cybersecurity Advisory (CSA) build…

**Parallel AI Enrichment:**

- **Technical Details:** FSB Center 16 primarily uses scanning to identify poorly configured networking devices, especially routers. The actors also exploit common vulnerabilities in Cisco devices, Cisco Smart Install (SMI), and web portals used to manage network devices.
- **Affected Products:** Poorly configured networking devices, primarily routers; Cisco devices; Cisco Smart Install (SMI); web portals used to manage network devices; specific versions not identified
- **Exploit Available:** false
- **Patch Available:** false
- **Active Exploitation:** true - https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a
- **Threat Actors:** Russian FSB Center 16; Berserk Bear; Energetic Bear; Crouching Yeti; Dragonfly; Ghost Blizzard; Static Tundra
- **Mitigation:** Correct insecure router configurations, restrict and secure management interfaces, disable unnecessary services such as SMI where applicable, and apply available vendor updates for known Cisco vulnerabilities. CISA urges device owners and network defenders to take mitigation and remediation actions against this activity.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a

---

## 4. 🟠 Zero-Day — September 2026 Patch Tuesday: Two Exploited Zero-Days and 113 Critical Vulnerabilities Among 972 CVEs

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Sep 08, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-september-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-81963 is a local elevation-of-privilege flaw caused by improper link resolution before file access in the Windows Update Stack, allowing an authorized attacker to reach SYSTEM privileges. CVE-2026-85880 is a heap-based buffer overflow in Windows ALPC that can let an attacker with code execution, including inside an AppContainer sandbox, escape the sandbox and obtain SYSTEM privileges. Both attacks require local code execution but no user interaction.
- **Affected Products:** Windows 10; Windows Server 2012, 2016, 2019, and 2022 (CVE-2026-85880); supported Windows client and server editions running the Windows Update Stack (CVE-2026-81963)
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false
- **Patch Available:** true - https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-81963; https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-85880
- **Active Exploitation:** true - https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-september-2026/
- **Threat Actors:** None known
- **Mitigation:** Install Microsoft's September 8, 2026 security updates addressing both CVEs and prioritize remediation across Windows clients and servers. Review potentially affected systems for signs of post-compromise privilege escalation.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-81963, https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-85880

---

## 5. 🟠 Zero-Day — A Vault with a Heap-View: The Uncomfortable Space Between AgentCore Harness and Identity

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Unit 42 (Palo Alto) &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://unit42.paloaltonetworks.com/securing-aws-agentcore-harness-credentials/>

> Analysis of how default configurations in AWS AgentCore Harness allow prompt injection to exfiltrate credentials, and key steps to secure your agents. The post A Vault with a Heap-View: The Uncomfortable Space Between AgentCore Harness and Identity appeared first on Unit 42 .

**Parallel AI Enrichment:**

- **Technical Details:** In the default configuration, AgentCore Harness provides shell and file_operations tools to sessions unless restricted with allowedTools. The shell tool runs in the same memory space and UID context as the harness process, allowing prompt injection to cause commands that read plaintext credentials after AgentCore Identity resolves them at runtime. The credentials can then be exfiltrated through an attacker-controlled destination.
- **Affected Products:** Amazon Bedrock AgentCore Harness; affected default configurations with built-in shell and file_operations tools enabled. Specific version range not stated.
- **CVSS Score:** :null
- **CVSS Vector:** :null
- **Exploit Available:** true - https://unit42.paloaltonetworks.com/securing-aws-agentcore-harness-credentials/
- **Patch Available:** false
- **Active Exploitation:** false
- **Threat Actors:** None known
- **Mitigation:** Restrict allowedTools at InvokeHarness time to only the tools required for each session, disabling the default shell and file_operations tools when unnecessary. Apply least privilege to Identity vault service accounts and monitor or filter outbound traffic from harness containers.
- **Vendor Advisory:** :null

---

## 6. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection occurs when an AI system processes external content—such as a website, email, or document—that contains malicious instructions. The AI may then silently follow those instructions instead of the user's intended request, potentially manipulating outputs or causing unintended actions.
- **Exploit Available:** true - https://greshake.github.io/
- **Patch Available:** false
- **Active Exploitation:** true - https://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html
- **Threat Actors:** None known
- **Mitigation:** Treat external web pages, emails, and documents as untrusted input; separate data from executable instructions and restrict agent permissions. Apply layered defenses, confirmation requirements for consequential actions, monitoring, and ongoing adversarial testing of AI systems.
- **Vendor Advisory:** https://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 7. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection occurs when an LLM processes external data such as websites, email, documents, or connected tools containing hidden malicious instructions. The LLM may follow those instructions while completing the user's request, potentially without any direct attacker input. This can cause unintended actions or information disclosure.
- **Affected Products:** Google Gemini app, Gemini in Google Workspace apps including Gmail, Docs editors, Drive, and Chat; specific versions not stated
- **CVSS Score:** .
- **CVSS Vector:** .
- **Exploit Available:** true - http://unit42.paloaltonetworks.com/ai-agent-prompt-injection
- **Patch Available:** false
- **Active Exploitation:** true - http://labs.cloudsecurityalliance.org/research/csa-research-note-indirect-prompt-injection-in-the-wild-2026
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses including user confirmation, URL sanitization, tool-chaining policies, and centralized policy controls. Google also recommends model hardening so Gemini can identify and ignore harmful instructions embedded in data.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html

---

## 8. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection occurs when an AI agent processes untrusted external content—such as webpages, iframes, email, or documents—that contains hidden malicious instructions. The agent may treat those instructions as task guidance, causing unwanted actions, information disclosure, data exfiltration, or financial transactions. In agentic browsing, the attack targets the planning model through content encountered during navigation.
- **Affected Products:** Google Chrome agentic browsing / Gemini in Chrome (specific versions not stated), other agentic browsers (versions not specified)
- **Exploit Available:** true - http://immersivelabs.com/resources/c7-blog/weaponizing-llms-bypassing-email-security-products-via-indirect-prompt-injection
- **Patch Available:** false
- **Active Exploitation:** true - http://labs.cloudsecurityalliance.org/research/csa-research-note-indirect-prompt-injection-in-the-wild-2026
- **Threat Actors:** None known
- **Mitigation:** Use layered defenses such as a user-alignment critic isolated from untrusted content, origin isolation, user confirmations for critical actions, real-time threat detection, and red-team response processes. Treat webpage and document content as untrusted and require explicit confirmation before sensitive actions.
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 9. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2025-48530 is an incorrect bounds-check condition in multiple locations of CrabbyAVIF, producing out-of-bounds accesses in Android 16's AVIF parsing/decoding path. The flaw could contribute to remote code execution when combined with other bugs, without additional privileges or user interaction. Google's analysis describes it as a linear buffer overflow in unsafe Rust; Android's Scudo allocator deterministically prevented exploitation on configurations using its guard pages.
- **Affected Products:** Google Android 16, including the CrabbyAVIF AVIF parser/decoder component
- **CVSS Score:** 8.1
- **CVSS Vector:** CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** false - https://app.opencve.io/cve/CVE-2025-48530
- **Patch Available:** true - https://source.android.com/docs/security/bulletin/2025-08-01
- **Active Exploitation:** false - https://app.opencve.io/cve/CVE-2025-48530
- **Threat Actors:** None known
- **Mitigation:** Apply Android security patch level 2025-08-05 or later. Keep Google Play Protect enabled; Scudo allocator hardening also mitigates this overflow on devices using it.
- **Vendor Advisory:** https://source.android.com/docs/security/bulletin/2025-08-01

---

## 10. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection occurs when an AI system processes attacker-controlled external content—such as a website, email, document, or calendar invite—containing hidden instructions. The model may follow those instructions instead of the user's request, potentially exfiltrating data, executing rogue actions, or causing destructive effects.
- **Affected Products:** Generative AI systems, AI assistants, AI agents, and LLM-integrated applications processing untrusted external content; no specific products or versions identified
- **CVSS Score:** .
- **CVSS Vector:** .
- **Exploit Available:** true - https://greshake.github.io/
- **Patch Available:** false
- **Active Exploitation:** true - https://blog.google/security/prompt-injections-web
- **Threat Actors:** None known
- **Mitigation:** Treat external content as untrusted input; isolate model access to sensitive data and tools, require confirmation for consequential actions, and apply layered monitoring, guardrails, and red-team testing. Limit agent privileges and prevent arbitrary execution or unrestricted data access.
- **Vendor Advisory:** http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html

---

## 11. 🟠 Zero-Day — Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite

**CVE:** `CVE-2025-66376` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Tue, 21 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a>

> Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite Executive summary A group of Russian state-supported cyber actors has been targeting and compromising various Western government and commercial organizations using the Zimbra Collaboration Suite (ZCS) software since at least July 2025. The Russian state-supported advanced persistent threat …

---

## 12. 🟡 High Severity — org.xwiki.rendering:xwiki-rendering-xml has an Eval Injection issue

**CVE:** `CVE-2025-53837` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-26vp-8gxg-v4pg>

> ### Impact
Any user who can edit their own user profile or any other document can execute arbitrary script macros including Groovy and Python macros that allow remote code execution including unrestricted read and write access to all wiki contents. The reason is that rendering output is included as content of HTML macros without further escaping and it is thus possible to close the HTML macro and …

---

## 13. 🟡 High Severity — Opencast: Stored XSS in Paella player via WebVTT/DFXP caption cue text

**CVE:** `CVE-2026-77615` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-m6c8-jcw2-5r25>

> ## Summary

The Opencast Paella player renders caption cue text into `innerHTML` without escaping. The captions canvas clears `_captionsContainer.innerHTML` and then appends each active cue with `_captionsContainer.innerHTML += cue`, so HTML inside a WebVTT or DFXP cue becomes live DOM and executes in the Opencast origin.

The caption track is read from any media package element with a `captions/*…

---

## 14. 🟡 High Severity — Microsoft Patches CVSS 10.0 Azure AI Foundry Flaw Enabling Unauthorized Privilege Escalation

**CVE:** `CVE-2026-85889` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://thehackernews.com/2026/09/microsoft-patches-cvss-100-azure-ai.html>

> Microsoft has released fixes for a maximum-severity security flaw in Azure AI Foundry that could be exploited to achieve privilege escalation. No customer action is required.

The vulnerability, tracked as CVE-2026-85889, carries a CVSS score of 10.0.

&quot;Missing authentication for critical function in Azure AI Foundry allows an unauthorized attacker to elevate privileges over a network,&quot;

---

## 15. 🟡 High Severity — Critical Orkes Conductor Vulnerability Exploited in Attacks

**CVE:** `CVE-2026-58138` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://www.securityweek.com/critical-orkes-conductor-vulnerability-exploited-in-attacks/>

> CVE-2026-58138 is an unauthenticated remote code execution vulnerability that attackers can exploit via inline workflow definitions. The post Critical Orkes Conductor Vulnerability Exploited in Attacks appeared first on SecurityWeek .

---

## 16. 🟡 High Severity — Grav CMS vulnerable to remote code execution via .zip file upload

**CVE:** `CVE-2026-72819` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-r94f-hx44-8jqf>

> ### Summary

A logged-in user can run any command on the server. A settings field can fill itself by calling one of Grav&#x27;s built-in routines, and a safety check is supposed to allow only harmless ones. The check only recognises a routine when its name is written as one piece of text; named as a pair of values instead, it is not examined at all and is passed as safe. Pointing such a field at t…

---

## 17. 🟡 High Severity — Grav: Missing admin.super guard on core group blueprint access field allows admin.users operator to escalate to super-admin

**CVE:** `CVE-2026-75837` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-xhfv-7758-r9hx>

> ## Summary
The core Flex group blueprint `system/blueprints/user/group.yaml` (access field, lines 48-55) omits the `security@: admin.super` field guard that its sibling account blueprint carries (`account.yaml:131/138/150`, added by the CVE-2026-42613 fix). A delegated non-super operator holding `admin.users.update` can therefore save a group whose `access` map contains `admin.super: true`, which …

---

## 18. 🟡 High Severity — Grav: Blueprint dynamic-data bare-function branch is denylist-gated and omits error_log, giving arbitrary file write

**CVE:** `CVE-2026-75827` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-f8wv-xp27-6gq7>

> ## Affected versions and vulnerable location

- Confirmed on grav core at `78ebfc1` (tag 2.0.13).
- Sinks:
  - `system/src/Grav/Common/Data/Blueprint.php:455-458` `call_user_func_array($o, $params)` (bare-function dynamic-data provider).
  - Twin: `system/src/Grav/Framework/Flex/FlexDirectory.php:936-938` `call_user_func_array($function, $params)`.
- Validation gate: `Blueprint::isSafeDynamicCall(…

---

## 19. 🟡 High Severity — Soup Sieve: Polynomial-time ReDoS (O(n²)) in the `IDENTIFIER` / `VALUE` selector sub-patterns

**CVE:** `CVE-2026-86000` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-gjv8-xp57-g29c>

> ## Summary

soupsieve compiles CSS selector strings with a set of hand-written regular expressions. The shared `IDENTIFIER` sub-pattern (also embedded in `VALUE`, and therefore in attribute selectors) places two adjacent quantified groups over overlapping character classes: `(?:[classA]|ESC)+(?:[classB]|ESC)*`, where both classes match ordinary identifier characters such as `a`. When a selector co…

---

## 20. 🟡 High Severity — Steeltoe: Header-forwarded client cert lacks proof of private-key possession

**CVE:** `CVE-2026-81868` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-5mq7-rwhj-4fh9>

> ### Summary

When Steeltoe&#x27;s certificate-based authorization (`UseCertificateAuthorization`) is configured, the default configuration of the middleware relies on the `X-Client-Cert` HTTP header to identify the client certificate, without verifying private-key possession. This header is not stripped by common Cloud Foundry routers (like Gorouter or Envoy) on inbound requests.

### Impact

An a…

---

## 21. 🟡 High Severity — Steeltoe.Discovery.Consul: malformed 'secure' metadata aborts service instance lookup (DoS)

**CVE:** `CVE-2026-81516` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-67c9-f6v2-qv86>

> ## Summary

Steeltoe&#x27;s Consul discovery client parses the `secure` metadata field on each registered service instance using `bool.Parse`, which throws on any value other than `true` or `false`. A single service instance registered with a malformed `secure` value (for example `yes` or `1`) aborts construction of the entire instance list for that service, making the service undiscoverable. When…

---

## 22. 🟡 High Severity — Jupyter Server: 5xx request logging leaks token-bearing Referer header values

**CVE:** `CVE-2026-86049` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-c3mw-737p-c7g2>

> ### Summary

When a request returns a 500, `jupyter_server/log.py` logs a small JSON block of request headers. 

The Referer header was copied into it as-is, so a token in the Referer URL ended up in the logs in plain text.

### Impact

Anyone who can read the server logs can pick tokens out of these 500 entries. Tokens end up in the Referer during normal token-based login and launch flows.

Affec…

---

## 23. 🟡 High Severity — Grav: UserInterface offsetget/offsetexists allow-listed in Twig sandbox let editor-authored content leak hashed_password and 2FA secrets via offsetGet()

**CVE:** `CVE-2026-76839` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-3jhr-mxmx-38cx>

> ## Summary

`system/config/security.yaml`&#x27;s Twig sandbox policy allow-lists `offsetget` and
`offsetexists` for `Grav\Common\User\Interfaces\UserInterface`. The concrete
`Grav\Common\User\DataUser\User` class does not filter which fields `offsetGet()`
returns, so any sandboxed template with access to a `User` object can read
`hashed_password`, `secret` (2FA seed), and `twofa_secret` directly, …

---

## 24. 🟡 High Severity — Grav: config_denied_paths default list omits `system`, exposing real secrets (e.g. system.cache.redis.password) via the Twig sandbox when config_access is enabled

**CVE:** `CVE-2026-76846` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-xjw5-q542-3vmr>

> ## Summary

`system/config/security.yaml`&#x27;s default `twig_sandbox.config_denied_paths` list
(`plugins`, `streams`, `security`, `backups`, `scheduler`) omits the `system` prefix.
When an operator enables the documented, non-default `twig_content.config_access: true`
setting (intended to safely expose low-sensitivity values like `site.title` to
editor-authored Twig content), any real secret sto…

---

## 25. 🟡 High Severity — Grav: The system, site, and theme Twig variables bypass the content sandbox entirely and are never covered by config_denied_paths

**CVE:** `CVE-2026-72698` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-p597-crqc-m349>

> ## Summary

`Grav\Common\Twig\Twig::init()` unconditionally puts the raw `system`, `site`, and `theme` config arrays into `$this-&gt;twig_vars`. `Twig::processPage()` builds the variables for the sandboxed, editor-authored page-content render by copying that same base array (`$sandbox_vars = $twig_vars;`) and replacing only the `config` key with a filtered `SandboxConfig` facade. The `system`, `si…

---

## 26. 🟡 High Severity — Grav: Non constant time nonce comparison in Utils::verifyNonce() used for CSRF protection

**CVE:** `CVE-2026-72701` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-38p6-h87p-r4cg>

> ## Summary

`Grav\Common\Utils::verifyNonce()`, the core function Grav and its plugins use to validate CSRF nonces, compares the submitted nonce to the expected value with PHP&#x27;s `===` operator instead of `hash_equals()`. `===` on strings short circuits at the first differing byte, so the comparison time leaks how many leading bytes of a guess are correct. This is CWE-208, Observable Timing Di…

---

## 27. 🟡 High Severity — Chamilo LMS CStudio upload flow allows unauthenticated remote code execution

**CVE:** `CVE-2026-45140` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-g4c3-4g96-6g4m>

> ### Impact
Ability to run arbitrary code on the server without authentication.

---

## 28. 🟡 High Severity — Fulgur: Unbounded page slicing from attacker-controlled CSS height causes denial of service

**CVE:** `CVE-2026-68523` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-j5cx-ph8g-95v3>

> `fulgur` converts untrusted HTML/CSS into PDF, commonly on a server that
processes input supplied by many tenants. In versions prior to 0.19.0, a
body-direct child whose CSS-resolved height greatly exceeds the page height was
sliced into one fragment per page with **no upper bound**.

The height is taken directly from attacker-controlled HTML/CSS (`height`, `vh`
units), so a few bytes such as:

``…

---

## 29. 🟡 High Severity — Steeltoe.Management.Endpoint: HttpExchanges URI masking leaks query-string secrets

**CVE:** `CVE-2026-75523` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-8phw-xrj9-cpqp>

> ## Summary

Steeltoe&#x27;s `/actuator/httpexchanges` endpoint records and displays request URIs after passing them through `MaskedUri`. The masking only covers the `UserInfo` portion of the URI (inline `user:password@host` credentials) and does not inspect the query string. With `IncludeQueryString` enabled by default, any secrets carried in query strings (for example: OAuth tokens, password-rese…

---

## 30. 🟡 High Severity — Grav: Stored XSS via Markdown audio/video media <source> URL

**CVE:** `CVE-2026-75831` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-6qw9-4vv5-jr97>

> **Target:** github.com/getgrav/grav  
**Affected resource:** `Grav\Common\Media\Traits\AudioMediaTrait` / `VideoMediaTrait` `sourceParsedownElement()` — verified on 2.0.13 (latest stable) and `develop` HEAD `5a7070f`  
**Severity:** Medium (~6.9 CVSS:3.1/AV:N/AC:L/PR:H/UI:R/S:C/C:H/I:L/A:N — anchored to the sibling script-XSS advisory [CVE-2026-42841](https://github.com/getgrav/grav/security/advis…

---

## 31. 🟡 High Severity — AsyncHttpClient doesn't verify SCRAM and Digest mutual-authentication responses

**CVE:** `CVE-2026-85716` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-fj9w-c36g-h5x8>

> ### Impact
For SCRAM, and for Digest with mutual authentication, the client computes the server&#x27;s verification value (the SCRAM ServerSignature, or the Digest rspauth) but does not act on the result. If the value is present and does not verify, the client only logs it and still delivers the response to the application as a successful, authenticated result. A server that never proved knowledge…

---

## 32. 🟡 High Severity — oras-go: Blind SSRF via unvalidated Link header URL in pagination allows internal network probing

**CVE:** `CVE-2026-85732` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-h7vf-4x9w-h99v>

> ## Summary

oras-go&#x27;s pagination helper `parseLink()` in `registry/remote/utils.go` follows the `Link` response header from a registry without validating the URL&#x27;s host or scheme. When a malicious registry returns a `Link` header containing an absolute URL pointing to an arbitrary host (e.g., a cloud metadata endpoint), the client makes GET requests to that host from the victim&#x27;s ne…

---

## 33. 🟡 High Severity — Kestra: SSRF via Pebble http() function allows unauthenticated access to internal services & cloud metadata

**CVE:** `CVE-2026-73247` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-r56g-q4p6-m3p6>

> ### Summary
The Pebble template engine&#x27;s `http()` function in Kestra OSS accepts user-controlled URLs without any validation, allowing Server-Side Request Forgery (SSRF) attacks. An unauthenticated attacker can import a malicious Flow YAML and execute it to access internal services, cloud metadata endpoints (AWS 169.254.169.254), or localhost services. The vulnerability affects all Kestra OSS…

---

## 34. 🟡 High Severity — RabbitMQ amqp091-go: Protocol Desynchronization and Frame Injection via Integer Overflow in readLongstr

**CVE:** `CVE-2026-77411` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-c5pq-fr2g-9jpf>

> **Summary**

A critical stream desynchronization vulnerability has been identified in the AMQP wire-protocol parser. When parsing a long string (`readLongstr`) within a table field, providing a length that exceeds the maximum signed 32-bit integer (`2^31 - 1`, or roughly `2.1` GiB) triggers an improper error-handling condition. The parser abruptly aborts the read and returns a success status (`&qu…

---

## 35. 🟡 High Severity — RabbitMQ amqp091-go: Silent Data Truncation and State Corruption via Shortstr Integer Overflow

**CVE:** `CVE-2026-77408` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-j497-x9hr-x34x>

> ## Summary
A data integrity and protocol corruption vulnerability exists in the AMQP client&#x27;s property serialization logic. When encoding AMQP short string (`shortstr`) fields—such as identifiers, routing strings, and content metadata—the length of the string is explicitly cast to a fixed-size 8-bit unsigned integer (`uint8`). 

If an application provides a property string exceeding 255 bytes…

---

## 36. 🟡 High Severity — RabbitMQ amqp091-go: Missing Explicit TLS Minimum Version Configuration In URI Parser

**CVE:** `CVE-2026-77405` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-33mj-cw25-m34h>

> ## Summary
A structural security weakness exists in the AMQP client&#x27;s TLS configuration generator (`tlsConfigFromURI`). When constructing a `*tls.Config` object from an `amqps://` connection URI, the library initializes the structure without explicitly defining the `MinVersion` field. 

While modern versions of the Go compiler toolchain (Go 1.18+) default the implicit minimum version to TLS 1…

---

## 37. 🟡 High Severity — RabbitMQ amqp091-go: Connection Configuration Overwrite via Unsanitized TLS Path Parameter Injection

**CVE:** `CVE-2026-77404` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-465g-fh3v-9jw4>

> ## Summary
A query parameter injection vulnerability exists in the AMQP client&#x27;s connection URI formatting logic. When generating or parsing connection URIs, TLS-related filesystem paths (such as certificates or keys) are appended directly to the URI&#x27;s query string using string concatenation rather than secure URL encoding via functions like `url.QueryEscape`.

If an application handles …

---

## 38. 🟡 High Severity — Zope AccessControl vulnerable to information disclosure through Python string `format` and `format_map` functions

**CVE:** `CVE-2026-77401` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-pq59-9fq7-m886>

> ### Impact
Python&#x27;s string `format` functionality allows someone controlling the format string to &quot;read&quot; objects accessible (recursively) via attribute access and subscription from accessible objects. Those attribute accesses and subscriptions use Python&#x27;s full blown `getattr` and `getitem`, not the policy restricted `AccessControl` variants `_getattr_` and `_getitem_`. This ca…

---

## 39. 🟡 High Severity — Umbraco: Delivery API leaks protected (Public Access) content through Content Picker / Multi-Node Tree Picker expansion

**CVE:** `CVE-2026-69197` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-wr57-hqmp-fgvh>

> The Content Delivery API enforces member / Public Access protection only at the controller layer, against the node that is directly requested. When a public (unprotected) node references a protected node through a Content Picker or Multi-Node Tree Picker (including those nested inside Block List, Block Grid, or Rich Text Editor blocks), the Delivery API expands and serializes the protected node wi…

---

## 40. 🟡 High Severity — Critical Docker Sandboxes Flaw Lets Malicious Guest Code Read and Modify macOS Host Files

**CVE:** `CVE-2026-77179` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://thehackernews.com/2026/09/critical-docker-sandboxes-flaw-lets.html>

> Malicious code running inside a Docker Sandboxes virtual machine on macOS could escape the project directory shared into it and read or change files anywhere else on the host, Docker warns in a security announcement on September 15.

The escape runs with the rights of the host account that runs the virtual machine. The flaw, CVE-2026-77179, is rated Critical, affects versions

---

## 41. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
