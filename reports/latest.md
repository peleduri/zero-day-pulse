# Zero Day Pulse

> **Generated:** 2026-10-03 02:38 UTC &nbsp;|&nbsp; **Total:** 16 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 9 &nbsp;|&nbsp; 🟡 High: 7 &nbsp;|&nbsp; ✨ Enriched: 0

---

## 1. 🟠 Zero-Day — Improve Router Hygiene to Protect Against Russian State-Sponsored Targeting

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Wed, 08 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a>

> Russian Government-Sponsored Activity Targets Poorly Configured and Vulnerable Devices Across Critical Sectors Executive summary Russian Federal Security Service (FSB) Center 16 cyber actors continue to exploit poorly configured and vulnerable networking devices worldwide, opportunistically compromising multiple critical infrastructure sector networks. This joint Cybersecurity Advisory (CSA) build…

---

## 2. 🟠 Zero-Day — September 2026 Patch Tuesday: Two Exploited Zero-Days and 113 Critical Vulnerabilities Among 972 CVEs

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CrowdStrike Blog &nbsp;|&nbsp; **Published:** Sep 08, 20
**Reference:** <https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-september-2026/>

---

## 3. 🟠 Zero-Day — Critical FortiMail Zero-Day Flaw Exploited in Attacks Allows Unauthenticated Arbitrary File Writes

**CVE:** `CVE-2026-104286` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-10-02
**Reference:** <https://thehackernews.com/2026/10/critical-fortimail-zero-day-flaw.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA), on Thursday, added a critical security flaw impacting Fortinet FortiMail to its Known Exploited Vulnerabilities (KEV) catalog, following reports of active exploitation.

The vulnerability, tracked as CVE-2026-104286 (CVSS score: 9.8), allows unauthenticated attackers to write arbitrary files on the underlying system.

&quot;An impro…

---

## 4. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

---

## 5. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

---

## 6. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

---

## 7. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

---

## 8. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 9. 🟠 Zero-Day — Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite

**CVE:** `CVE-2025-66376` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Tue, 21 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a>

> Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite Executive summary A group of Russian state-supported cyber actors has been targeting and compromising various Western government and commercial organizations using the Zimbra Collaboration Suite (ZCS) software since at least July 2025. The Russian state-supported advanced persistent threat …

---

## 10. 🟡 High Severity — gitea-runner: workflow container.options passes host namespaces and capability flags to job container when privileged mode is disabled

**CVE:** `CVE-2026-73802` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-02
**Reference:** <https://github.com/advisories/GHSA-x4q3-gcj3-m6cf>

> ### Summary
act_runner appends workflow-controlled `jobs.&lt;job&gt;.container.options` directly 
to the Docker HostConfig for the job container. When runner privileged mode is 
disabled, only `Privileged` is forced false. Host namespace flags, capability 
expansion, and security profile overrides from workflow YAML are preserved in 
the final HostConfig. A workflow author can enter host PID/IPC n…

---

## 11. 🟡 High Severity — SiYuan MCP asset.upload Reads Arbitrary Absolute File Paths (Workspace Boundary Bypass)

**CVE:** `CVE-2026-66012` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-02
**Reference:** <https://github.com/advisories/GHSA-p23f-cm6q-2qp8>

> # Security Advisory — SiYuan MCP `asset.upload` Reads Arbitrary Absolute File Paths (Workspace Boundary Bypass)

| Field | Value |
|---|---|
| **Disclosed by** | joysinleung (`joysinleung@gmail.com`) |
| **Report date** | 2026-08-13 |
| **Product** | SiYuan (思源笔记) — `siyuan-note/siyuan` |
| **Go module** | `github.com/siyuan-note/siyuan/kernel` |
| **Affected versions** | `&lt;= 3.8.0` (latest rel…

---

## 12. 🟡 High Severity — aws-smithy-json: Uncontrolled recursion in the aws-smithy-json unknown-key skip path allows unauthenticated remote denial of service in smithy-rs generated servers

**CVE:** `CVE-2026-18140` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-02
**Reference:** <https://github.com/advisories/GHSA-8ffr-xgwf-xj56>

> ### Summary
Smithy-RS is a Rust code generation and runtime framework that generates HTTP clients and servers from Smithy interface definitions, powering the AWS SDK for Rust and custom service implementations. An issue exists which allows uncontrolled recursion in the unknown-key skip path of the Amazon aws-smithy-json runtime crate in versions 0.62.6 and earlier.

### Impact
Uncontrolled recursi…

---

## 13. 🟡 High Severity — Composer: GHSA-gjfg-22fp-rrxx fix bypass via symlinked package bin path

**CVE:** `CVE-2026-59944` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-02
**Reference:** <https://github.com/advisories/GHSA-96h3-5x6v-m776>

> ## Summary

A malicious or compromised Composer package could, when installed as a dependency, cause Composer to change the permissions of a file outside that package&#x27;s own directory and to register a runnable `vendor/bin` command that points at that outside file. This is a path traversal and link following issue. It is not remote code execution, the attacker gains no ability to read or recei…

---

## 14. 🟡 High Severity — Copernik XML Factory (stock JDK provider) has Improper restriction of XInclude resource resolution

**CVE:** `CVE-2026-61586` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-02
**Reference:** <https://github.com/advisories/GHSA-xm28-xvqc-gxxg>

> Copernik XML Factory through `0.1.1`, when running on its stock JDK provider, does not block XInclude resource resolution after an application enables XInclude on a factory returned by `XmlFactories.newDocumentBuilderFactory()` or `XmlFactories.newSAXParserFactory()`, or on an `XMLReader` passed through `XmlFactories.harden()`. The library&#x27;s documented guarantee that XInclude resolution stays…

---

## 15. 🟡 High Severity — Dell CSM Flaws Enable Unauthenticated Admin Access and Root on Kubernetes Nodes

**CVE:** `CVE-2026-63688` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-10-02
**Reference:** <https://thehackernews.com/2026/10/dell-csm-flaws-enable-unauthenticated.html>

> Dell has released security updates to address multiple critical security flaws in Dell Container Storage Modules (CSM) that could be exploited by bad actors to take over susceptible systems.

The vulnerabilities are listed below -


  CVE-2026-63688 (CVSS score: 10.0) - A missing authentication for critical function vulnerability in the csm-authorization-storage gRPC server that an

---

## 16. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
