# Zero Day Pulse

> **Generated:** 2026-11-25 01:42 UTC &nbsp;|&nbsp; **Total:** 10 &nbsp;|&nbsp; 🔴 KEV: 3 &nbsp;|&nbsp; 📈 High EPSS: 1 &nbsp;|&nbsp; 🟠 Zero-Day: 4 &nbsp;|&nbsp; 🟡 High: 3 &nbsp;|&nbsp; 🎯 My Stack: 6 &nbsp;|&nbsp; ✨ Enriched: 0

---

## 🏁 Beat KEV

**Last 30 days**  
- All: collecting data since 2026-11-18 — Counted 0 · Earlier 0 · Same day/late 0 · Missed 0
- Edge devices: collecting data since 2026-11-18 — Counted 0 · Earlier 0 · Same day/late 0 · Missed 0
- Excluded: 13 warm-up, 0 old CVEs

**Last 90 days**  
- All: collecting data since 2026-11-18 — Counted 0 · Earlier 0 · Same day/late 0 · Missed 0
- Edge devices: collecting data since 2026-11-18 — Counted 0 · Earlier 0 · Same day/late 0 · Missed 0
- Excluded: 13 warm-up, 0 old CVEs

_Zero-days reported before a CVE ID exists can't be matched and count as missed._

---

## ⚡ Changed since last run (1)

- 🔴 CVE-2026-131914 entered KEV (due 2026-11-27)

---

## 🎯 My Stack Highlights

- 🔴 CISA KEV — Vulnerabilities in Node.js and Brotli Affecting Cisco Products: October 2026 — `CVE-2026-111497`, `CVE-2026-105482`, `CVE-2026-105483`, `CVE-2026-106069` — EPSS 100% — `node.js`
- 🟡 High Severity — CVE-2026-123633 Portfolio Status: Impact of NGINX Vulnerabilities (CVE-2026-123633, CVE-2026-123007) on Palo Alto Networks Products (Severity: CRITICAL) — `CVE-2026-123633`, `CVE-2026-123007` — EPSS 45% — `nginx`
- 🟡 High Severity — Vulnerabilities in nginx Affecting Cisco Products: November 2026 — `CVE-2026-113425`, `CVE-2026-121810`, `CVE-2026-123007`, `CVE-2026-123633`, `CVE-2026-123634` — EPSS 45% — `nginx`
- 🟠 Zero-Day — New Shirudo tool uses AI to shield unpatched Linux systems from exploits — _No CVE_ — EPSS n/a — `linux`
- 🟠 Zero-Day — OpenAI, Cisco Unveil Open Source Tool to Shield Unpatched Linux Systems — _No CVE_ — EPSS n/a — `linux`
- 🟠 Zero-Day — OpenAI and Cisco Unveil AI-Assisted Linux Security Tool to Block Exploits Before Patching — _No CVE_ — EPSS n/a — `linux`

---

## 1. 🔴 CISA KEV — Vulnerabilities in Node.js and Brotli Affecting Cisco Products: October 2026

**CVE:** `CVE-2026-111497` | `CVE-2026-105482` | `CVE-2026-105483` | `CVE-2026-106069` &nbsp;|&nbsp; **Source:** Cisco Security Advisories (PSIRT) &nbsp;|&nbsp; **Published:** 2026-11-24
**EPSS:** 100.0% (percentile 100%)
**KEV:** in catalog, due 2026-11-10
**My Stack:** `node.js`
**Reference:** <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-oct2026-node-js-Jj3SQ19u?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Vulnerabilities%20in%20Node.js%20and%20Brotli%20Affecting%20Cisco%20Products:%20October%202026%26vs_k=1>

> On October 21, 2026, Node.js announced the availability of fixes for multiple vulnerabilities across the following supported release lines: 22.x, 24.x, and 26.x. These vulnerabilities impact critical operations such as the Brotli decoder, DNS resolution, and TLS certificate validation. The vulnerabilities pose risks for remote code execution and traffic interception. For more information, see Node…

---

## 2. 🔴 CISA KEV — Rapid7 Analysis: VMware vCenter SRP Authentication Bypass to Root (CVE-2026-123890)

**CVE:** `CVE-2026-123890` &nbsp;|&nbsp; **Source:** Rapid7 Blog &nbsp;|&nbsp; **Published:** 2026-11-24
**EPSS:** 3.5% (percentile 89%)
**KEV:** in catalog, due 2026-11-23
**Reference:** <https://www.rapid7.com/blog/post/ra-rapid7-analysis-vmware-vcenter-srp-authentication-bypass-to-root-cve-2026-123890>

> Overview An unauthenticated attacker can retrieve the session key for an in-progress administrator login to VMware vCenter&#x27;s directory service. The attacker then uses that key to complete the login without knowing the account&#x27;s password. The vulnerable interface is exposed through DCE/RPC on TCP port 2012. The issue, tracked as CVE-2026-123890 , combines a Secure Remote Password (SRP) se…

---

## 3. 🔴 CISA KEV — Hackers Exploit N-able MailAssure Flaw While AI Agents Exploit MONAI Label Zero-Day

**CVE:** `CVE-2026-134624` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-11-24
**EPSS:** 0.6% (percentile 50%)
**KEV:** in catalog, due 2026-11-26
**Reference:** <https://thehackernews.com/2026/11/hackers-exploit-n-able-mailassure-flaw.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Monday added two flaws impacting N-able MailAssure and MONAI Label to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

The critical vulnerabilities are listed below -


  CVE-2026-134624 (CVSS score: 9.3) - A server-side request forgery (SSRF) vulnerability in N-able MailAssure&#x27;s LDA…

---

## 4. 🟠 Zero-Day — VMware vCenter Hit by Another Critical 9.8-Rated Auth Bypass Flaw After Zero-Day Exploitation

**CVE:** `CVE-2026-123903` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-11-24
**Reference:** <https://thehackernews.com/2026/11/vmware-vcenter-hit-by-another-critical.html>

> Broadcom has shipped patches to address 23 vulnerabilities impacting VMware ESX, vCenter, Workstation, Fusion, and Avi Load Balancer, including one critical bug that could be abused to bypass authentication.

The critical vulnerability, tracked as CVE-2026-123903, is rated 9.8 out of 10.0 on the CVSS scoring system. It resides in the VMware Directory Service (&quot;vmdir&quot;).

&quot;A malicious…

---

## 5. 🟠 Zero-Day — New Shirudo tool uses AI to shield unpatched Linux systems from exploits

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-11-24
**My Stack:** `linux`
**Reference:** <https://www.bleepingcomputer.com/news/security/new-shirudo-tool-uses-ai-to-shield-unpatched-linux-systems-from-exploits/>

> OpenAI and Cisco launched an open-source Linux security tool named Shirudo that deploys temporary runtime protections to block vulnerability exploitation while administrators prepare and roll out patches, without restarting services. [...]

---

## 6. 🟠 Zero-Day — OpenAI, Cisco Unveil Open Source Tool to Shield Unpatched Linux Systems

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** SecurityWeek &nbsp;|&nbsp; **Published:** 2026-11-24
**My Stack:** `linux`
**Reference:** <https://www.securityweek.com/openai-cisco-unveil-open-source-tool-to-shield-unpatched-linux-systems/>

> OpenAI and Cisco’s Shirudo uses AI-generated shields to block Linux exploits while patches are prepared, but it’s not yet production-ready. The post OpenAI, Cisco Unveil Open Source Tool to Shield Unpatched Linux Systems appeared first on SecurityWeek .

---

## 7. 🟠 Zero-Day — OpenAI and Cisco Unveil AI-Assisted Linux Security Tool to Block Exploits Before Patching

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-11-24
**My Stack:** `linux`
**Reference:** <https://thehackernews.com/2026/11/openai-and-cisco-unveil-ai-assisted.html>

> OpenAI and Cisco have teamed up to launch Shirudo (meaning &quot;shield&quot; in Japanese), an open-source Linux runtime that allows artificial intelligence (AI) agents to defend systems without downtime.

&quot;It lets agents write dynamic eBPF controls to shield systems from exploits, giving defenders more time to test and roll out patches,&quot; OpenAI said in a post on X.

The AI upstart calle…

---

## 8. 🟡 High Severity — CVE-2026-123633 Portfolio Status: Impact of NGINX Vulnerabilities (CVE-2026-123633, CVE-2026-123007) on Palo Alto Networks Products (Severity: CRITICAL)

**CVE:** `CVE-2026-123633` | `CVE-2026-123007` &nbsp;|&nbsp; **Source:** Palo Alto Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-24
**EPSS:** 44.7% (percentile 99%)
**My Stack:** `nginx`
**Reference:** <https://security.paloaltonetworks.com/CVE-2026-123633>

---

## 9. 🟡 High Severity — Vulnerabilities in nginx Affecting Cisco Products: November 2026

**CVE:** `CVE-2026-113425` | `CVE-2026-121810` | `CVE-2026-123007` | `CVE-2026-123633` | `CVE-2026-123634` &nbsp;|&nbsp; **Source:** Cisco Security Advisories (PSIRT) &nbsp;|&nbsp; **Published:** 2026-11-24
**EPSS:** 44.7% (percentile 99%)
**My Stack:** `nginx`
**Reference:** <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-nginx-nov-2026-e8jska2s?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Vulnerabilities%20in%20nginx%20Affecting%20Cisco%20Products:%20November%202026%26vs_k=1>

> On November 18, 2026, nginx announced the availability of a fix for multiple critical vulnerabilities in nginx that could lead to remote code execution. These vulnerabilities affect nginx releases 1.9.5 through 1.31.8 and is fixed in releases 1.31.9 (mainline) and 1.30.7 (stable). These vulnerabilities were identified by the following CVEs: CVE-2026-113425: NGINX ngx_mail_proxy_module vulnerabilit…

---

## 10. 🟡 High Severity — Vulnerability in PHP Affecting Cisco Products: November 2026

**CVE:** `CVE-2026-126714` &nbsp;|&nbsp; **Source:** Cisco Security Advisories (PSIRT) &nbsp;|&nbsp; **Published:** 2026-11-24
**EPSS:** 13.3% (percentile 96%)
**Reference:** <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-phpaftershell-nov-2026-kT9pL4Xe?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Vulnerability%20in%20PHP%20Affecting%20Cisco%20Products:%20November%202026%26vs_k=1>

> On November 19, 2026, the PHP Foundation announced the availability of security fixes that address a critical vulnerability that could lead to remote code execution. This vulnerability is identified by CVE-2026-126714. For information about this vulnerability, see the advisory GHSA-fm2m-fjf5-v3cp . This vulnerability is being referenced as phpAfterShell . For information about Splunk products and …

---
