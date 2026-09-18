# Zero Day Pulse

> **Generated:** 2026-09-18 20:11 UTC &nbsp;|&nbsp; **Total:** 41 &nbsp;|&nbsp; 🔴 KEV: 3 &nbsp;|&nbsp; 🟠 Zero-Day: 11 &nbsp;|&nbsp; 🟡 High: 27 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🔴 CISA KEV — CVE-2025-39964 — Linux Kernel Race Condition Vulnerability

**CVE:** `CVE-2025-39964` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2025-39964>

> Vendor: Linux | Product: Kernel. Linux Kernel contains a race condition vulnerability which allows concurrent writes to the same AF_ALG socket causing data to be unpredictably interleaved and creating inconsistencies in the socket&#x27;s internal state. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates…

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2025-39964 is a race condition in the Linux kernel AF_ALG cryptographic user API. Concurrent writes to the same AF_ALG socket can interleave unpredictably and leave the socket's internal state inconsistent. The flaw can be triggered by a local user and may crash the system or corrupt cryptographic operation results, causing denial of service or data-integrity issues. The upstream fix adds exclusive write ownership so only one writer can issue sendmsg() at a time.
- **Affected Products:** Linux Kernel — affected from version 2.6.38 until the corresponding fixes; fixed in 5.10.245, 5.15.194, 6.1.154, 6.6.108, 6.12.49, 6.16.9, and 6.17.
- **CVSS Score:** 7.8
- **CVSS Vector:** CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true - https://github.com/n1k0oowang/CVE-2025-39964_EXP
- **Patch Available:** true - https://git.kernel.org/stable/c/1b34cbbf4f011a121ef7b2d7d6e6920a036d5285
- **Active Exploitation:** true - CISA KEV
- **Threat Actors:** None known
- **Mitigation:** Upgrade to a kernel containing the upstream stable fix and apply the applicable distribution security update. Where patching is not immediately possible, Red Hat recommends preventing the af_alg module from loading, such as by blacklisting it; this may affect applications that require AF_ALG cryptographic interfaces. CISA also directs organizations to follow applicable BOD 26-04 prioritization and forensic-triage guidance.
- **Vendor Advisory:** https://git.kernel.org/stable/c/1b34cbbf4f011a121ef7b2d7d6e6920a036d5285

---

## 2. 🔴 CISA KEV — CVE-2026-53266 — Linux Kernel Out-of-Bounds Write Vulnerability

**CVE:** `CVE-2026-53266` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2026-53266>

> Vendor: Linux | Product: Kernel. Linux Kernel contains an out-of-bounds write vulnerability in the ebtables SNAT target which allows an ARP sender hardware address rewrite to write directly into a nonlinear socket-buffer fragment backed by a splice-imported file page. The impacted product(s) could be end-of-life (EoL) and/or end-of-service (EoS). Users are advised to discontinue use and/or transit…

**Parallel AI Enrichment:**

- **Technical Details:** The vulnerability is in the Linux kernel's netfilter bridge ebtables SNAT target. Its optional ARP sender hardware-address rewrite uses skb_store_bits() after only safely reading the ARP header; it does not ensure that the subsequent sender-hardware-address range is writable. If that range resides in a nonlinear socket-buffer fragment backed by a splice-imported file page, the kernel can write the replacement MAC address directly into the underlying page, causing memory corruption and potentially denial of service or local privilege escalation.

Exploitation requires local access and a system configured with applicable bridge netfilter/ebtables SNAT rules, particularly ARP hardware-address rewriting. The upstream fix adds a writability check covering the ARP header and Ethernet address before the rewrite.
- **Affected Products:** Linux kernel netfilter bridge ebtables SNAT: 5.4.73 through versions before 5.5; 5.8.17 through versions before 5.9; 5.9.2 through versions before 5.10; 5.10.x before 5.10.259; 5.15.x before 5.15.210; 6.1.x before 6.1.176; 6.6.x before 6.6.143; 6.12.x before 6.12.94; 6.18.x before 6.18.36; 7.0.x before 7.0.13. Linux 7.1 is listed as unaffected.
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Exploit Available:** false - No public proof-of-concept was identified; https://feedly.com/cve/CVE-2026-53266
- **Patch Available:** true - https://lore.kernel.org/linux-cve-announce/2026062517-CVE-2026-53266-6162@gregkh/T
- **Active Exploitation:** true - CISA Known Exploited Vulnerabilities Catalog; added 2026-09-18 based on evidence of active exploitation
- **Threat Actors:** None known
- **Mitigation:** Upgrade to a kernel release containing the upstream fix, preferably the latest stable kernel for the applicable branch. If an update cannot be applied immediately, disable ARP hardware-address rewriting in ebtables SNAT rules or remove ebtables SNAT rules operating on ARP traffic over bridge interfaces. CISA also requires KEV remediation in accordance with applicable BOD 26-04 guidance.
- **Vendor Advisory:** https://lore.kernel.org/linux-cve-announce/2026062517-CVE-2026-53266-6162@gregkh/T

---

## 3. 🔴 CISA KEV — CVE-2025-39682 — Linux Kernel Improper Check for Unusual or Exceptional Conditions Vulnerability

**CVE:** `CVE-2025-39682` &nbsp;|&nbsp; **Source:** CISA KEV &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://nvd.nist.gov/vuln/detail/CVE-2025-39682>

> Vendor: Linux | Product: Kernel. Linux Kernel contains an improper check for unusual or exceptional conditions vulnerability in the TLS receive path which allows a zero-length record retrieved from the rx_list to bypass the intended recvmsg() record-type handling, potentially causing subsequent TLS records to be processed using incorrect zero-copy and queuing assumptions. The impacted product(s) c…

**Parallel AI Enrichment:**

- **Technical Details:** The Linux kernel kTLS receive path mishandles a zero-length TLS record initially retrieved from rx_list. Because the record does not establish the expected content type, a subsequent record of a different type can bypass recvmsg() record-type handling and enter an invalid zero-copy path.

In zero-copy mode, the code may requeue an skb that cannot safely be queued, corrupting the receive-list fragment structure and reference counting. This can lead to a use-after-free when the socket is closed, with potential denial of service or privilege escalation when kTLS is enabled.
- **Affected Products:** Linux Kernel net/tls: 6.0–6.1.148, 6.2–6.6.102, 6.7–6.12.43, 6.13–6.16.3, 6.17-rc1, and 6.17-rc2
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true - https://github.com/khoatran107/cve-2025-39682
- **Patch Available:** true - https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/net/tls?id=62708b9452f8eb77513115b17c4f8d1a22ebf843
- **Active Exploitation:** true - CISA KEV
- **Threat Actors:** None known
- **Mitigation:** Upgrade to a kernel containing the upstream fix, including stable branches at or above 6.1.149, 6.6.103, 6.12.44, or 6.16.4; the fix is also present from Linux 6.17-rc3. Apply the corresponding distribution kernel update, such as the Debian or Amazon Linux security packages.

As an interim mitigation where patching is not immediately possible, prevent the kTLS `tls` kernel module from loading or disable kTLS use, recognizing that this may affect applications that depend on kernel TLS.
- **Vendor Advisory:** https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/net/tls?id=62708b9452f8eb77513115b17c4f8d1a22ebf843

---

## 4. 🟠 Zero-Day — Improve Router Hygiene to Protect Against Russian State-Sponsored Targeting

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Wed, 08 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a>

> Russian Government-Sponsored Activity Targets Poorly Configured and Vulnerable Devices Across Critical Sectors Executive summary Russian Federal Security Service (FSB) Center 16 cyber actors continue to exploit poorly configured and vulnerable networking devices worldwide, opportunistically compromising multiple critical infrastructure sector networks. This joint Cybersecurity Advisory (CSA) build…

**Parallel AI Enrichment:**

- **Technical Details:** The actors primarily scan Internet-facing IP ranges for poorly configured networking devices, especially routers, and exploit exposed SNMP services and weak or default community strings. They also occasionally exploit Cisco vulnerabilities, Cisco Smart Install (SMI), and web portals used to manage network devices, including CVE-2018-0171 and CVE-2008-4128.
- **Affected Products:** Networking devices, primarily routers; Cisco devices and Cisco Smart Install (SMI); cited CVEs CVE-2018-0171 and CVE-2008-4128; specific vulnerable product versions: Information unavailable.
- **CVSS Vector:** Information unavailable.
- **Exploit Available:** Information unavailable.
- **Patch Available:** Information unavailable.
- **Active Exploitation:** true - https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a
- **Threat Actors:** Russian FSB Center 16 cyber actors; commonly associated tracking names include Berserk Bear, Energetic Bear, Crouching Yeti, Dragonfly, Ghost Blizzard, and Static Tundra.
- **Mitigation:** Use strong, unique credentials for network-device accounts and store them securely. Update device software and firmware, patch known vulnerabilities, replace end-of-life devices with supported models, and restrict or disable unnecessary Internet-facing management and SNMP exposure.
- **Vendor Advisory:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a

---

## 5. 🟠 Zero-Day — September 2026 Patch Tuesday: Two Exploited Zero-Days and 113 Critical Vulnerabilities Among 972 CVEs

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Sep 08, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-september-2026/>

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2026-85880 is a heap-based buffer overflow in Windows Advanced Local Procedure Call (ALPC). An attacker with low-privilege local code execution, including code running inside an AppContainer, can exploit the flaw to escape the sandbox and elevate to SYSTEM without additional user interaction.

CVE-2026-81963 is an improper link-resolution-before-file-access flaw in the Windows Update Stack. A locally authenticated attacker with low privileges can abuse the high-privilege update components to reach SYSTEM privileges; the attack requires no user interaction.
- **Affected Products:** CVE-2026-85880: Windows 10 versions 1607, 1809, 21H2, and 22H2; Windows Server 2012, 2012 R2, 2016, 2019, and 2022, including listed Server Core editions, in the vulnerable build ranges specified by Microsoft. CVE-2026-81963: Windows 11 versions 23H2, 24H2, 25H2, and 26H1; Windows Server 2025, including Server Core, in the vulnerable build ranges specified by Microsoft.
- **CVSS Score:** 7.8 for both CVE-2026-85880 and CVE-2026-81963
- **CVSS Vector:** CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Exploit Available:** true - https://www.proofpoint.com/us/blog/threat-insight/once-bluemoon-multiple-state-aligned-threat-actors-rapidly-adopt-novel-exploit (weaponized BlueMoon chain using CVE-2026-85880); false for CVE-2026-81963 based on Microsoft's 'Publicly disclosed: No' assessment.
- **Patch Available:** true - CVE-2026-85880: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-85880; CVE-2026-81963: https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-81963
- **Active Exploitation:** true - Microsoft lists both vulnerabilities as exploited, and CISA added both to its Known Exploited Vulnerabilities catalog.
- **Threat Actors:** TA412, UNK_LateNight, and UNK_DoubleCheck are reported exploiting CVE-2026-85880 through the BlueMoon exploit chain. None known for CVE-2026-81963.
- **Mitigation:** Install Microsoft's September 8, 2026 security updates for all affected Windows builds, prioritizing internet-connected and high-value systems. Both vulnerabilities are in CISA's Known Exploited Vulnerabilities catalog, so organizations should accelerate remediation, restrict untrusted local code execution where practical, and monitor for post-compromise privilege escalation activity until patch deployment is complete.
- **Vendor Advisory:** CVE-2026-85880: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-85880; CVE-2026-81963: https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-81963

---

## 6. 🟠 Zero-Day — Convoy: Cross-Tenant Source IDOR Leaks Plaintext Message Broker Credentials

**CVE:** `CVE-2026-81505` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-p5vg-v7mj-f6q4>

> ## Summary
frain-dev/convoy (all versions up to and including v26.6.2, no patch
available) lets any authenticated caller who is authorized on at least one
project read ANY OTHER project&#x27;s &quot;Source&quot; record by ID via
GET /api/v1/projects/{projectID}/sources/{sourceID} -- regardless of whether
that Source actually belongs to the project named in the URL. The response
includes the Source…

**Parallel AI Enrichment:**

- **Technical Details:** An authenticated user or project-scoped API key holder authorized for one Convoy project can request another project's Source by supplying its source ID in GET /api/v1/projects/{projectID}/sources/{sourceID}. The handler authorizes the project from the URL, but the underlying FindSourceByID lookup and SQL query use only the source ID and do not verify that the Source belongs to the authorized project.

The endpoint can therefore return another tenant's complete Source record. Because the response is not redacted, AMQP, Kafka, SQS, and Google Pub/Sub configurations may expose plaintext broker credentials, including passwords.
- **Affected Products:** frain-dev/convoy versions before 26.6.8, including v26.6.2 and earlier
- **CVSS Score:** 6.5 (estimated)
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N (estimated; no CVSS v3.x assignment was published)
- **Exploit Available:** true - https://github.com/frain-dev/convoy/security/advisories/GHSA-p5vg-v7mj-f6q4
- **Patch Available:** true - https://github.com/frain-dev/convoy/releases/tag/v26.6.8
- **Active Exploitation:** false - no confirmed in-the-wild exploitation report or CISA KEV listing was identified
- **Threat Actors:** None known
- **Mitigation:** Upgrade Convoy to v26.6.8 or later, which adds project scoping to Source lookups and rejects cross-project IDs. Rotate any broker credentials that may have been exposed, review access and application logs for suspicious Source-ID requests, and restrict Convoy API access to trusted networks while upgrading.
- **Vendor Advisory:** https://github.com/frain-dev/convoy/security/advisories/GHSA-p5vg-v7mj-f6q4

---

## 7. 🟠 Zero-Day — ToolHive: containerized MCP servers can reach host services via host.docker.internal, enabling lateral movement

**CVE:** `CVE-2026-58197` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-qg2g-g9w3-m5h8>

> ## Summary

A containerized MCP server running with the default `network` permission profile (`insecure_allow_all: true`) can reach host-local services via `host.docker.internal`. This includes the ToolHive API itself, other ToolHive-managed MCP server proxies, and any other service listening on the host&#x27;s localhost. Combined with the unauthenticated ToolHive API and MCP proxy endpoints, this…

**Parallel AI Enrichment:**

- **Technical Details:** Prior to ToolHive CLI 0.30.1 and ToolHive Studio 0.38.0, containerized MCP servers used a default network profile that did not isolate them from host services. With host.docker.internal or the Docker gateway reachable, a malicious or compromised MCP server could access the ToolHive control plane, other MCP proxies, localhost-bound services, and potentially privileged MCP tools without escaping its container.

The issue combines unrestricted container networking with unauthenticated ToolHive API and MCP proxy endpoints. ToolHive Studio also forced network_isolation to false, overriding the backend’s secure isolation behavior.
- **Affected Products:** ToolHive CLI versions < 0.30.1, ToolHive Studio versions < 0.38.0
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS:3.1/AV:A/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H
- **Exploit Available:** true - https://github.com/stacklok/toolhive/security/advisories/GHSA-qg2g-g9w3-m5h8
- **Patch Available:** true - https://github.com/stacklok/toolhive/releases/tag/v0.30.1; https://github.com/stacklok/toolhive-studio/releases/tag/v0.38.0
- **Active Exploitation:** false - no confirmed active exploitation report identified in the cited advisory or CVE record
- **Threat Actors:** None known
- **Mitigation:** Upgrade ToolHive CLI to 0.30.1 or later and ToolHive Studio to 0.38.0 or later. Until upgraded, block host.docker.internal and 172.17.0.1 from container networking, isolate MCP server networks from the Docker bridge gateway, and require authentication or authorization tokens for MCP proxy and control-plane endpoints.

Use explicit per-container network allow-lists where possible, avoid exposing privileged native MCP tools on reachable localhost ports, and enable audit logging for MCP tool calls. Existing servers may need to be restarted before the new network-isolation defaults take effect.
- **Vendor Advisory:** https://github.com/stacklok/toolhive/security/advisories/GHSA-qg2g-g9w3-m5h8

---

## 8. 🟠 Zero-Day — A Vault with a Heap-View: The Uncomfortable Space Between AgentCore Harness and Identity

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Unit 42 (Palo Alto) &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://unit42.paloaltonetworks.com/securing-aws-agentcore-harness-credentials/>

> Analysis of how default configurations in AWS AgentCore Harness allow prompt injection to exfiltrate credentials, and key steps to secure your agents. The post A Vault with a Heap-View: The Uncomfortable Space Between AgentCore Harness and Identity appeared first on Unit 42 .

**Parallel AI Enrichment:**

- **Technical Details:** A prompt injection can steer an AgentCore Harness agent into invoking its built-in shell tool. In the default configuration, shell and file_operations are available unless restricted through allowedTools, and the shell runs with the same UID as PID 1, including root-level access.
- **Affected Products:** Amazon Bedrock AgentCore Harness in its default configuration, particularly sessions exposing the built-in shell and file_operations tools while using AgentCore Identity; no vulnerable-version range identified.
- **CVSS Score:** technical_details
- **CVSS Vector:** Information unavailable.
- **Exploit Available:** true - https://unit42.paloaltonetworks.com/securing-aws-agentcore-harness-credentials/
- **Patch Available:** false - no official vendor patch identified for this finding.
- **Active Exploitation:** false - no confirmed in-the-wild exploitation reported.
- **Threat Actors:** None known
- **Mitigation:** At InvokeHarness time, restrict allowedTools to only what each session requires; remove shell and file_operations when they are unnecessary. Apply least privilege to AgentCore Identity service accounts, filter and monitor outbound traffic from harness containers, and treat unexpected destinations as potential evidence of prompt injection.
- **Vendor Advisory:** Information unavailable.

---

## 9. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection occurs when an AI system processes untrusted content—such as a website, email, or document—that contains malicious instructions. The poisoned content can cause the AI to follow the attacker's commands instead of the user's intended request. The observed attack vector involves seeding such instructions on public websites so browsing AI agents or other systems ingest them.
- **Affected Products:** Information unavailable (the report describes a general AI-agent attack class and does not identify product names or vulnerable versions).
- **CVSS Vector:** Information unavailable.
- **Exploit Available:** true - https://greshake.github.io/
- **Patch Available:** false - no versioned vendor patch is identified; https://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html
- **Active Exploitation:** true - https://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html; http://labs.cloudsecurityalliance.org/research/csa-research-note-indirect-prompt-injection-in-the-wild-2026
- **Threat Actors:** None known
- **Mitigation:** Treat websites, emails, and documents processed by AI agents as untrusted input. Separate retrieved content from trusted system instructions, restrict agent permissions and external side effects, and require confirmation for consequential actions. Google also recommends hardening AI models and products, red-team pressure testing, and real-time monitoring to identify and neutralize malicious activity.
- **Vendor Advisory:** https://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 10. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection occurs when an AI application processes untrusted external content—such as web pages, email, or documents—that contains hidden malicious instructions. The LLM may interpret those instructions as part of the task and silently follow the attacker’s commands rather than the user’s intent.

The attack can cause unintended actions or information disclosure and may occur without direct malicious input from the user. The relevant attack surface is therefore AI applications that combine LLMs with external data sources or tools, including Workspace with Gemini.
- **Affected Products:** Google Workspace with Gemini, Gemini app, and Gemini in Workspace apps including Gmail, Docs editors, Drive, and Chat; no specific vulnerable versions identified
- **CVSS Score:** Information unavailable.
- **CVSS Vector:** Information unavailable.
- **Exploit Available:** true - http://unit42.paloaltonetworks.com/ai-agent-prompt-injection
- **Patch Available:** false - no conventional vendor patch release was identified; Google describes continuous, layered mitigation instead
- **Active Exploitation:** true - Cloud Security Alliance reports live exploitation, citing Google, Forcepoint X-Labs, and Palo Alto Networks Unit 42
- **Threat Actors:** None known
- **Mitigation:** Use Google’s layered Gemini and Workspace defenses, keep the relevant services and security controls current, and treat web pages, email, and documents supplied to an AI system as untrusted input. Review AI outputs and require human confirmation before consequential actions, especially where the AI can access sensitive data or invoke tools.

Google describes ongoing model hardening, red-team testing, attack reproduction and cataloguing, and continuous improvement rather than a one-time fix; organizations should therefore maintain defense-in-depth controls and monitor for newly disclosed indirect prompt-injection techniques.
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

## 14. 🟠 Zero-Day — Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite

**CVE:** `CVE-2025-66376` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Tue, 21 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a>

> Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite Executive summary A group of Russian state-supported cyber actors has been targeting and compromising various Western government and commercial organizations using the Zimbra Collaboration Suite (ZCS) software since at least July 2025. The Russian state-supported advanced persistent threat …

---

## 15. 🟡 High Severity — Mnemosyne has JWT signature verification bypass sync server that allows authentication bypass

**CVE:** `CVE-2026-59163` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-xcw4-53cc-hv32>

> ### Summary

The Mnemosyne sync server&#x27;s authentication check decoded JWT bearer tokens but never verified their HMAC-SHA256 signatures. Any well-formed token was accepted, allowing an unauthenticated attacker to impersonate any user and read or modify their sync data.

**Severity: Critical**

CVSS 3.1: AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N = 9.1

Assumes the sync server endpoint is network-rea…

---

## 16. 🟡 High Severity — Perses's missing authorization in datasource proxy allows cross-scope secret disclosure

**CVE:** `CVE-2026-63199` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-4227-9989-jrhx>

> ### Impact

The datasource proxy authorizes the caller on the Datasource scope, then resolves and decrypts any Secret named in the request body with no Secret-scope check.

Datasource and Secret are distinct, independently grantable role scopes, so an operator can grant datasource access without secret access. The proxy and the service to create a datasource does not verify that the operator has t…

---

## 17. 🟡 High Severity — Perses's project query parameter authorization bypass exposes cross-project resources

**CVE:** `CVE-2026-63458` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-cjgj-2fwf-4c2w>

> ### Impact
_What kind of vulnerability is it?_

An authenticated user who is only a viewer on project team-a requests GET /api/v1/projects/team-a/dashboards?project=finance-secret (or simply GET /api/v1/datasources?project=finance-secret) and receives the full list of the finance-secret project&#x27;s dashboards and datasource specifications, despite having no role on that project. This defeats Pe…

---

## 18. 🟡 High Severity — Process Compose: Browser DNS rebinding lets websites control local process-compose MCP tools

**CVE:** `CVE-2026-77339` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-5gm3-9crp-6g3v>

> ## Summary

A malicious website can use DNS rebinding to control a developer&#x27;s local process-compose MCP SSE listener when MCP SSE is enabled. The vulnerable path accepts browser-origin requests before any Host validation, Origin validation, or caller-secret check, then dispatches the requests into process-compose MCP tools.

This advisory covers `https://github.com/F1bonacc1/process-compose`…

---

## 19. 🟡 High Severity — AnyCable: Telemetry Subsystem Contains Hardcoded Authentication Token and Transmits CLI Arguments Including Secrets

**CVE:** `CVE-2026-63406` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-w72w-9qmj-c9qm>

> ### Summary
The telemetry subsystem embeds a hardcoded auth token (`&quot;secret&quot;`) in the public source and transmits raw CLI arguments—including `--secret`, `--jwt_secret`, and `--http_rpc_secret` values—to a third-party telemetry endpoint.

### Details
In `telemetry/config.go` line 12, `var authToken = &quot;secret&quot;` is committed in the public repository and used to authenticate to `h…

---

## 20. 🟡 High Severity — AnyCable: Pusher REST API Does Not Verify Request Body MD5 Enabling Signed-Request Replay with Arbitrary Body

**CVE:** `CVE-2026-63405` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-5p54-whvp-x327>

> ### Summary
The Pusher-compatible REST API includes `body_md5` in the HMAC signature string but never computes or verifies the MD5 of the received HTTP body, allowing anyone who observes a signed request to replay it with an entirely different body.

### Details
In `pusher/http.go`, the `Handler` function extracts `body_md5` from the URL query string (line 169) and includes it verbatim in `stringT…

---

## 21. 🟡 High Severity — kcp front-proxy does not strip inbound X-Remote-* identity headers, allowing any authenticated client to inject groups/warrants and impersonate system:masters in any workspace

**CVE:** `CVE-2026-61682` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-c8w2-fgvx-vhv4>

> # Summary

The kcp front-proxy fails to strip client-supplied identity headers before forwarding requests to shards. Any authenticated tenant can inject their own `X-Remote-Group` and `X-Remote-Extra-*` headers, which the shard trusts as a verified identity assertion — allowing a low-privilege user to escalate to cluster administrator (`system:masters`) and read, write, or delete resources in any …

---

## 22. 🟡 High Severity — Capsule: Tenant owner bypasses Capsule's forbidden namespace/service/node label and annotation enforcement

**CVE:** `CVE-2026-61672` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-gjw4-3v3v-rqxg>

> ## Summary

Capsule lets a cluster administrator forbid specific metadata keys that tenant owners must not place on their own resources: `Tenant.spec.namespaceOptions.forbiddenLabels` / `forbiddenAnnotations` (namespaces), `Tenant.spec.serviceOptions.forbiddenLabels` / `forbiddenAnnotations` (Services), and the cluster-wide forbidden worker-node labels/annotations. These lists are an isolation con…

---

## 23. 🟡 High Severity — LMDeploy has Remote Code Execution by Pickle Deserialization via handle_zmq_recv in lmdeploy/lmdeploy/pytorch/disagg/conn/engine_conn.py

**CVE:** `CVE-2025-66455` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-2vh9-42vm-xmv2>

> ## Summary

LMDeploy&#x27;s PyTorch DistServe/PD-disaggregation control plane used
`recv_pyobj()` to deserialize messages received through a ZeroMQ PULL
socket. PyZMQ implements `recv_pyobj()` using Python pickle
deserialization, which can execute arbitrary code while reconstructing
an object.

The peer address used by the receiver was supplied through the
`POST /distserve/p2p_connect` HTTP endpoi…

---

## 24. 🟡 High Severity — Semantic MediaWiki affected by reflected XSS in `Special:Ask` via a forged cursor pagination token

**CVE:** `CVE-2026-77616` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-cx86-7xwp-w9wf>

> ## Reflected XSS via a forged cursor pagination token

#### Failure mode

`Special:Ask` accepts a `cursor` query parameter for keyset pagination (added in 7.0.0). The token is decoded by `CursorEncoder`, which is an **unsigned** base64url-encoded JSON blob, so its contents are fully attacker-controlled. When the cursor&#x27;s sort anchor does not match the request&#x27;s `sort=` / `order=`, `Query…

---

## 25. 🟡 High Severity — org.xwiki.rendering:xwiki-rendering-xml has an Eval Injection issue

**CVE:** `CVE-2025-53837` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-26vp-8gxg-v4pg>

> ### Impact
Any user who can edit their own user profile or any other document can execute arbitrary script macros including Groovy and Python macros that allow remote code execution including unrestricted read and write access to all wiki contents. The reason is that rendering output is included as content of HTML macros without further escaping and it is thus possible to close the HTML macro and …

---

## 26. 🟡 High Severity — Opencast: Stored XSS in Paella player via WebVTT/DFXP caption cue text

**CVE:** `CVE-2026-77615` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://github.com/advisories/GHSA-m6c8-jcw2-5r25>

> ## Summary

The Opencast Paella player renders caption cue text into `innerHTML` without escaping. The captions canvas clears `_captionsContainer.innerHTML` and then appends each active cue with `_captionsContainer.innerHTML += cue`, so HTML inside a WebVTT or DFXP cue becomes live DOM and executes in the Opencast origin.

The caption track is read from any media package element with a `captions/*…

---

## 27. 🟡 High Severity — Microsoft Patches CVSS 10.0 Azure AI Foundry Flaw Enabling Unauthorized Privilege Escalation

**CVE:** `CVE-2026-85889` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://thehackernews.com/2026/09/microsoft-patches-cvss-100-azure-ai.html>

> Microsoft has released fixes for a maximum-severity security flaw in Azure AI Foundry that could be exploited to achieve privilege escalation. No customer action is required.

The vulnerability, tracked as CVE-2026-85889, carries a CVSS score of 10.0.

&quot;Missing authentication for critical function in Azure AI Foundry allows an unauthorized attacker to elevate privileges over a network,&quot;

---

## 28. 🟡 High Severity — Critical Orkes Conductor Vulnerability Exploited in Attacks

**CVE:** `CVE-2026-58138` &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-09-18
**Reference:** <https://www.securityweek.com/critical-orkes-conductor-vulnerability-exploited-in-attacks/>

> CVE-2026-58138 is an unauthenticated remote code execution vulnerability that attackers can exploit via inline workflow definitions. The post Critical Orkes Conductor Vulnerability Exploited in Attacks appeared first on SecurityWeek .

---

## 29. 🟡 High Severity — Grav CMS vulnerable to remote code execution via .zip file upload

**CVE:** `CVE-2026-72819` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-r94f-hx44-8jqf>

> ### Summary

A logged-in user can run any command on the server. A settings field can fill itself by calling one of Grav&#x27;s built-in routines, and a safety check is supposed to allow only harmless ones. The check only recognises a routine when its name is written as one piece of text; named as a pair of values instead, it is not examined at all and is passed as safe. Pointing such a field at t…

---

## 30. 🟡 High Severity — Grav: Missing admin.super guard on core group blueprint access field allows admin.users operator to escalate to super-admin

**CVE:** `CVE-2026-75837` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-xhfv-7758-r9hx>

> ## Summary
The core Flex group blueprint `system/blueprints/user/group.yaml` (access field, lines 48-55) omits the `security@: admin.super` field guard that its sibling account blueprint carries (`account.yaml:131/138/150`, added by the CVE-2026-42613 fix). A delegated non-super operator holding `admin.users.update` can therefore save a group whose `access` map contains `admin.super: true`, which …

---

## 31. 🟡 High Severity — Grav: Blueprint dynamic-data bare-function branch is denylist-gated and omits error_log, giving arbitrary file write

**CVE:** `CVE-2026-75827` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-f8wv-xp27-6gq7>

> ## Affected versions and vulnerable location

- Confirmed on grav core at `78ebfc1` (tag 2.0.13).
- Sinks:
  - `system/src/Grav/Common/Data/Blueprint.php:455-458` `call_user_func_array($o, $params)` (bare-function dynamic-data provider).
  - Twin: `system/src/Grav/Framework/Flex/FlexDirectory.php:936-938` `call_user_func_array($function, $params)`.
- Validation gate: `Blueprint::isSafeDynamicCall(…

---

## 32. 🟡 High Severity — Soup Sieve: Polynomial-time ReDoS (O(n²)) in the `IDENTIFIER` / `VALUE` selector sub-patterns

**CVE:** `CVE-2026-86000` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-gjv8-xp57-g29c>

> ## Summary

soupsieve compiles CSS selector strings with a set of hand-written regular expressions. The shared `IDENTIFIER` sub-pattern (also embedded in `VALUE`, and therefore in attribute selectors) places two adjacent quantified groups over overlapping character classes: `(?:[classA]|ESC)+(?:[classB]|ESC)*`, where both classes match ordinary identifier characters such as `a`. When a selector co…

---

## 33. 🟡 High Severity — Steeltoe: Header-forwarded client cert lacks proof of private-key possession

**CVE:** `CVE-2026-81868` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-5mq7-rwhj-4fh9>

> ### Summary

When Steeltoe&#x27;s certificate-based authorization (`UseCertificateAuthorization`) is configured, the default configuration of the middleware relies on the `X-Client-Cert` HTTP header to identify the client certificate, without verifying private-key possession. This header is not stripped by common Cloud Foundry routers (like Gorouter or Envoy) on inbound requests.

### Impact

An a…

---

## 34. 🟡 High Severity — Steeltoe.Discovery.Consul: malformed 'secure' metadata aborts service instance lookup (DoS)

**CVE:** `CVE-2026-81516` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-67c9-f6v2-qv86>

> ## Summary

Steeltoe&#x27;s Consul discovery client parses the `secure` metadata field on each registered service instance using `bool.Parse`, which throws on any value other than `true` or `false`. A single service instance registered with a malformed `secure` value (for example `yes` or `1`) aborts construction of the entire instance list for that service, making the service undiscoverable. When…

---

## 35. 🟡 High Severity — Jupyter Server: 5xx request logging leaks token-bearing Referer header values

**CVE:** `CVE-2026-86049` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-c3mw-737p-c7g2>

> ### Summary

When a request returns a 500, `jupyter_server/log.py` logs a small JSON block of request headers. 

The Referer header was copied into it as-is, so a token in the Referer URL ended up in the logs in plain text.

### Impact

Anyone who can read the server logs can pick tokens out of these 500 entries. Tokens end up in the Referer during normal token-based login and launch flows.

Affec…

---

## 36. 🟡 High Severity — Grav: UserInterface offsetget/offsetexists allow-listed in Twig sandbox let editor-authored content leak hashed_password and 2FA secrets via offsetGet()

**CVE:** `CVE-2026-76839` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-3jhr-mxmx-38cx>

> ## Summary

`system/config/security.yaml`&#x27;s Twig sandbox policy allow-lists `offsetget` and
`offsetexists` for `Grav\Common\User\Interfaces\UserInterface`. The concrete
`Grav\Common\User\DataUser\User` class does not filter which fields `offsetGet()`
returns, so any sandboxed template with access to a `User` object can read
`hashed_password`, `secret` (2FA seed), and `twofa_secret` directly, …

---

## 37. 🟡 High Severity — Grav: config_denied_paths default list omits `system`, exposing real secrets (e.g. system.cache.redis.password) via the Twig sandbox when config_access is enabled

**CVE:** `CVE-2026-76846` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-xjw5-q542-3vmr>

> ## Summary

`system/config/security.yaml`&#x27;s default `twig_sandbox.config_denied_paths` list
(`plugins`, `streams`, `security`, `backups`, `scheduler`) omits the `system` prefix.
When an operator enables the documented, non-default `twig_content.config_access: true`
setting (intended to safely expose low-sensitivity values like `site.title` to
editor-authored Twig content), any real secret sto…

---

## 38. 🟡 High Severity — Grav: The system, site, and theme Twig variables bypass the content sandbox entirely and are never covered by config_denied_paths

**CVE:** `CVE-2026-72698` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-p597-crqc-m349>

> ## Summary

`Grav\Common\Twig\Twig::init()` unconditionally puts the raw `system`, `site`, and `theme` config arrays into `$this-&gt;twig_vars`. `Twig::processPage()` builds the variables for the sandboxed, editor-authored page-content render by copying that same base array (`$sandbox_vars = $twig_vars;`) and replacing only the `config` key with a filtered `SandboxConfig` facade. The `system`, `si…

---

## 39. 🟡 High Severity — Grav: Non constant time nonce comparison in Utils::verifyNonce() used for CSRF protection

**CVE:** `CVE-2026-72701` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-38p6-h87p-r4cg>

> ## Summary

`Grav\Common\Utils::verifyNonce()`, the core function Grav and its plugins use to validate CSRF nonces, compares the submitted nonce to the expected value with PHP&#x27;s `===` operator instead of `hash_equals()`. `===` on strings short circuits at the first differing byte, so the comparison time leaks how many leading bytes of a guess are correct. This is CWE-208, Observable Timing Di…

---

## 40. 🟡 High Severity — Chamilo LMS CStudio upload flow allows unauthenticated remote code execution

**CVE:** `CVE-2026-45140` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-09-17
**Reference:** <https://github.com/advisories/GHSA-g4c3-4g96-6g4m>

> ### Impact
Ability to run arbitrary code on the server without authentication.

---

## 41. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
