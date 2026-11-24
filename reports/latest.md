# Zero Day Pulse

> **Generated:** 2026-11-24 03:33 UTC &nbsp;|&nbsp; **Total:** 14 &nbsp;|&nbsp; 🔴 KEV: 3 &nbsp;|&nbsp; 📈 High EPSS: 1 &nbsp;|&nbsp; 🟠 Zero-Day: 4 &nbsp;|&nbsp; 🟡 High: 7 &nbsp;|&nbsp; 🎯 My Stack: 2 &nbsp;|&nbsp; ✨ Enriched: 0

---

## 🏁 Beat KEV

**Last 30 days**  
- All: collecting data since 2026-11-18 — Counted 0 · Earlier 0 · Same day/late 0 · Missed 0
- Edge devices: collecting data since 2026-11-18 — Counted 0 · Earlier 0 · Same day/late 0 · Missed 0
- Excluded: 10 warm-up, 0 old CVEs

**Last 90 days**  
- All: collecting data since 2026-11-18 — Counted 0 · Earlier 0 · Same day/late 0 · Missed 0
- Edge devices: collecting data since 2026-11-18 — Counted 0 · Earlier 0 · Same day/late 0 · Missed 0
- Excluded: 10 warm-up, 0 old CVEs

_Zero-days reported before a CVE ID exists can't be matched and count as missed._

---

## ⚡ Changed since last run (3)

- 🔴 CVE-2026-134624 entered KEV (due 2026-11-26) — N-able Discloses Critical Mail Assure Vulnerability Found During Breach Investigation <https://thehackernews.com/2026/11/n-able-discloses-critical-mail-assure.html>
- 🎯 New My Stack hit: CVE-2026-108398 [windows] — VirtualBox Process Hardening on Windows 2026 Edition: What’s a Single Bit Between Friends? <https://projectzero.google/2026/11/virtualbox-process-hardening.html>
- 🎯 New My Stack hit: CVE-2026-87268 [windows] — VirtualBox Process Hardening on Windows 2026 Edition: What’s a Single Bit Between Friends? <https://projectzero.google/2026/11/virtualbox-process-hardening.html>

---

## 🎯 My Stack Highlights

- 🟡 High Severity — Vulnerabilities in nginx Affecting Cisco Products: November 2026 — `CVE-2026-113425`, `CVE-2026-121810`, `CVE-2026-123007`, `CVE-2026-123633`, `CVE-2026-123634` — EPSS 28% — `nginx`
- 🟡 High Severity — VirtualBox Process Hardening on Windows 2026 Edition: What’s a Single Bit Between Friends? — `CVE-2026-87268`, `CVE-2026-108398` — EPSS 1% — `windows`

---

## 1. 🔴 CISA KEV — Cisco Expressway Series Remote Code Execution Vulnerability

**CVE:** `CVE-2026-76466` &nbsp;|&nbsp; **Source:** Cisco Security Advisories (PSIRT) &nbsp;|&nbsp; **Published:** 2026-11-23
**EPSS:** 2.2% (percentile 83%)
**KEV:** in catalog, due 2026-11-23
**Reference:** <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-vcs-static-cred-hr7EWZ8t?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Cisco%20Expressway%20Series%20Remote%20Code%20Execution%20Vulnerability%26vs_k=1>

> A vulnerability in the database service feature of Cisco Expressway Series could allow an unauthenticated, remote attacker with network access to a Cisco Expressway device to execute arbitrary operating system commands as root . This vulnerability is due to the use of persistent cookies. Additionally, there is insufficient validation of client certificates when the TLS Verify Mode is set to Enable…

---

## 2. 🔴 CISA KEV — Hackers Exploit Critical ScreenConnect Flaw to Hijack MSP Technician PCs Without Warning

**CVE:** `CVE-2026-84869` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-11-23
**EPSS:** 1.2% (percentile 68%)
**KEV:** in catalog, due 2026-09-14
**Reference:** <https://thehackernews.com/2026/11/hackers-exploit-critical-screenconnect.html>

> Threat actors are exploiting a now-patched security flaw in ConnectWise ScreenConnect to target managed service provider (MSP) servers.

The activity revolves around CVE-2026-84869 (CVSS score: 9.9), a critical ScreenConnect client flaw that allows a guest to transfer and execute a malicious payload on a connecting technician&#x27;s host.

&quot;On November 12, 2026, we observed one managed servic…

---

## 3. 🔴 CISA KEV — N-able Discloses Critical Mail Assure Vulnerability Found During Breach Investigation

**CVE:** `CVE-2026-134624` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-11-23
**EPSS:** 0.4% (percentile 30%)
**KEV:** in catalog, due 2026-11-26
**Reference:** <https://thehackernews.com/2026/11/n-able-discloses-critical-mail-assure.html>

> N-able yesterday disclosed a critical flaw it found while investigating the breach of its Mail Assure and SpamExperts Hosted Cloud, an email filtering service it runs for managed service providers.

The bug, tracked as CVE-2026-134624, is a server-side request forgery (SSRF) flaw. It allowed a user with high-level API access to open connections to internal systems of the user&#x27;s choosing on th…

---

## 4. 🟠 Zero-Day — Hackers Exploit Critical ASP.NET Anti-CSRF Library Flaw Allowing Unauthenticated RCE

**CVE:** `CVE-2026-131914` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-11-23
**EPSS:** 0.6% (percentile 50%)
**Reference:** <https://thehackernews.com/2026/11/hackers-exploit-critical-aspnet-anti.html>

> Cybersecurity researchers have urged users to discontinue using a legacy ASP.NET anti-CSRF library named Idunno.AntiCsrf (&quot;Idunno.AntiCsrf.dll&quot;) following the discovery of a critical vulnerability that has been exploited in the wild.

The vulnerability, tracked as CVE-2026-131914, carries a CVSS score of 9.3 out of 10.0. The issue affects versions 0.9.1.0 and 0.9.1 Beta, and relates to a…

---

## 5. 🟠 Zero-Day — CISA flags critical Cisco RCE flaw as actively exploited in attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-11-23
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-flags-critical-cisco-expressway-rce-flaw-as-actively-exploited/>

> The US Cybersecurity and Infrastructure Security Agency (CISA) warned federal agencies that attackers are now exploiting a recently patched critical Cisco Expressway vulnerability in the wild. [...]

---

## 6. 🟠 Zero-Day — ⚡ Weekly Recap: VMware 0-Day, Java4Shell, NGINX2Root, Ruby2Shell, and a Whole Lot of Shell Trouble

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-11-23
**Reference:** <https://thehackernews.com/2026/11/weekly-recap-vmware-0-day-java4shell.html>

> A stolen key. A trusted message. A routine update. None of these looks like the start of a major security problem. That&#x27;s partly why they work. Attackers don&#x27;t always need to break down a door. Sometimes they just use one that&#x27;s already open.

This week&#x27;s stories show how quickly a small opening can turn into a much bigger mess. One breach helps attackers reach another target. …

---

## 7. 🟠 Zero-Day — Agentic Attacks: In The Wild

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Wiz Research &nbsp;|&nbsp; **Published:** 2026-11-23
**Reference:** <https://www.wiz.io/blog/agentic-attacks-artex-offensive-ai-frameworks>

> Agentic offensive frameworks like ARTEX are driving a surge in cloud intrusions. Wiz Research shares cases from the wild, including both sides of one attack via the operator&#x27;s leaked logs, an update on Black October, and the detections that catch these noisy, machine-speed attacks.

---

## 8. 🟡 High Severity — AVideo API vulnerable to OS command injection through an unescaped FFmpeg process keyword

**CVE:** `CVE-2026-63492` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-23
**Reference:** <https://github.com/advisories/GHSA-j44m-77cc-p3cc>

> ### Summary

The helper `listFFmpegProcesses($keyword)` in `plugin/API/standAlone/functions.php` builds a shell pipeline by interpolating `$keyword` inside single quotes and running it with `exec()`:

```php
$command .= &quot; | grep &#x27;$keyword&#x27;&quot;;
exec($command, $output, $status);
```

The two callers in `plugin/API/standAlone/ffmpeg.json.php` (the `list` mode and the `isKeywordRunni…

---

## 9. 🟡 High Severity — secp256k1-native has a compiler-induced timing side channel in scalar multiplication

**CVE:** `CVE-2026-63410` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-23
**EPSS:** 0.3% (percentile 21%)
**Reference:** <https://github.com/advisories/GHSA-vp2j-gqfm-r3cf>

> ## Summary

`Point#mul` — the default, constant-time scalar multiplication and the library&#x27;s headline secret-scalar operation — could leak timing information about the secret scalar (a private key or ECDSA-style nonce in a downstream consumer) **not because of a source-level bug, but because the compiler reconstructed a branch from branchless source.**

The Montgomery ladder selects between p…

---

## 10. 🟡 High Severity — Vulnerability in Oracle OpenJDK (Java4Shell) Affecting Cisco Products: November 2026

**CVE:** `CVE-2026-114938` &nbsp;|&nbsp; **Source:** Cisco Security Advisories (PSIRT) &nbsp;|&nbsp; **Published:** 2026-11-23
**EPSS:** 57.3% (percentile 99%)
**Reference:** <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-nov2026-java-rce-eCa6ss9z?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Vulnerability%20in%20Oracle%20OpenJDK%20(Java4Shell)%20Affecting%20Cisco%20Products:%20November%202026%26vs_k=1>

> On November 17, 2026, Oracle announced the availability of fixes for a vulnerability in OpenJDK that could lead to remote code execution identified by CVE-2026-114938. The vulnerability affects OpenJDK Java 17.0.6 and later on x86-64 platforms when processing Base64 encoded content. For more information, see the Oracle Critical Security Patch Update Advisory - November 2026 and the OpenJDK Vulnera…

---

## 11. 🟡 High Severity — Vulnerability in PHP Affecting Cisco Products: November 2026

**CVE:** `CVE-2026-126714` &nbsp;|&nbsp; **Source:** Cisco Security Advisories (PSIRT) &nbsp;|&nbsp; **Published:** 2026-11-23
**EPSS:** 13.3% (percentile 96%)
**Reference:** <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-phpaftershell-nov-2026-kT9pL4Xe?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Vulnerability%20in%20PHP%20Affecting%20Cisco%20Products:%20November%202026%26vs_k=1>

> On November 19, 2026, the PHP Foundation announced the availability of security fixes that address a critical vulnerability that could lead to remote code execution. This vulnerability is identified by CVE-2026-126714. For information about this vulnerability, see the advisory GHSA-fm2m-fjf5-v3cp . This vulnerability is being referenced as phpAfterShell . For information about Splunk products and …

---

## 12. 🟡 High Severity — Vulnerabilities in nginx Affecting Cisco Products: November 2026

**CVE:** `CVE-2026-113425` | `CVE-2026-121810` | `CVE-2026-123007` | `CVE-2026-123633` | `CVE-2026-123634` &nbsp;|&nbsp; **Source:** Cisco Security Advisories (PSIRT) &nbsp;|&nbsp; **Published:** 2026-11-23
**EPSS:** 27.8% (percentile 98%)
**My Stack:** `nginx`
**Reference:** <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-nginx-nov-2026-e8jska2s?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Vulnerabilities%20in%20nginx%20Affecting%20Cisco%20Products:%20November%202026%26vs_k=1>

> On November 18, 2026, nginx announced the availability of a fix for multiple critical vulnerabilities in nginx that could lead to remote code execution. These vulnerabilities affect nginx releases 1.9.5 through 1.31.8 and is fixed in releases 1.31.9 (mainline) and 1.30.7 (stable). These vulnerabilities were identified by the following CVEs: CVE-2026-113425: NGINX ngx_mail_proxy_module vulnerabilit…

---

## 13. 🟡 High Severity — Critical binary-parser Flaw Enables JavaScript Injection via Malicious Parser Definitions

**CVE:** `CVE-2026-134814` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-11-23
**EPSS:** 0.6% (percentile 50%)
**Reference:** <https://thehackernews.com/2026/11/critical-binary-parser-flaw-enables.html>

> A critical security flaw has been disclosed in the popular binary-parser library that could allow an attacker who controls parser definitions to execute arbitrary code.

The vulnerability, tracked as CVE-2026-134814 (CVSS score: 9.2 / 8.1), is a case of code injection impacting binary-parser versions prior to 2.3.1.

&quot;Binary-parser before 2.3.1 contains a code injection vulnerability that all…

---

## 14. 🟡 High Severity — VirtualBox Process Hardening on Windows 2026 Edition: What’s a Single Bit Between Friends?

**CVE:** `CVE-2026-87268` | `CVE-2026-108398` &nbsp;|&nbsp; **Source:** Google Project Zero &nbsp;|&nbsp; **Published:** 2026-11-23
**EPSS:** 0.8% (percentile 57%)
**My Stack:** `windows`
**Reference:** <https://projectzero.google/2026/11/virtualbox-process-hardening.html>

> Back in 2017 I did some research into Oracle VirtualBox on Windows. Specifically I focussed on their mechanism to protect their VM processes from the user on the host. The protection was to gate who could open the kernel driver, which might allow for privilege escalation due to the way it was designed. At the time I found 3 ways of bypassing the protection, with an additional issue in COM’s runtim…

---
