# Zero Day Pulse

> **Generated:** 2026-11-05 03:58 UTC &nbsp;|&nbsp; **Total:** 14 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 9 &nbsp;|&nbsp; 🟡 High: 5 &nbsp;|&nbsp; ✨ Enriched: 0

---

## 1. 🟠 Zero-Day — SonicWall warns of unpatched flaws in end-of-life GMS software

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-11-04
**Reference:** <https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-unpatched-flaws-in-end-of-life-gms-software/>

> SonicWall warned customers of two security flaws affecting end-of-life Global Management System (GMS) systems that will not be patched. [...]

---

## 2. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

---

## 3. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

---

## 4. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

---

## 5. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

---

## 6. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

---

## 7. 🟠 Zero-Day — Zyxel fixes zero-day exploited to hack nearly 1,000 network switches

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-11-04
**Reference:** <https://www.bleepingcomputer.com/news/security/zyxel-fixes-zero-day-exploited-to-hack-nearly-1-000-network-switches/>

> Zyxel has patched a zero-day vulnerability in its GS1900 series network switches that hackers exploited to compromise nearly 1,000 devices worldwide and steal configuration files and credentials. [...]

---

## 8. 🟠 Zero-Day — Researchers Uncover Prompt Adware Hidden in OpenAI Codex Jailbreak Toolkit

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-11-04
**Reference:** <https://thehackernews.com/2026/11/researchers-uncover-prompt-adware.html>

> Cybersecurity researchers have disclosed details of an OpenAI Codex jailbreak bundle that&#x27;s designed to modify an artificial intelligence (AI) agent&#x27;s trusted instructions to insert advertisements for a third-party AI gateway.

The phenomenon has been codenamed prompt adware by Check Point Research.

Called Haiou (meaning Seagull in Chinese), the jailbreak modifies OpenAI Codex&#x27;s co…

---

## 9. 🟠 Zero-Day — CISA flags WordPress RCE flaw as actively exploited in attacks

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-11-04
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-flags-wordpress-rce-flaw-as-actively-exploited-in-attacks/>

> The US Cybersecurity and Infrastructure Security Agency (CISA) warned federal agencies that attackers have started exploiting a recently patched high-severity WordPress vulnerability in the wild. [...]

---

## 10. 🟡 High Severity — Arc: DuckDB I/O aliases bypass database RBAC after CVE-2026-47735

**CVE:** `CVE-2026-55098` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-04
**Reference:** <https://github.com/advisories/GHSA-93cm-2v4m-c56c>

> ### Summary

The fix for CVE-2026-47735 (released 2026.06.1) is incomplete. It added a DuckDB sandbox (`SET GLOBAL allowed_directories=[&lt;storage root&gt;]; SET GLOBAL enable_external_access=false`) and an Arc SQL-layer denylist of the **literal** functions `read_parquet(` and `arc_partition_agg(`. The sandbox correctly blocks reads **outside** the storage root (OS files, `http://` SSRF), but it…

---

## 11. 🟡 High Severity — SonicWall Won't Patch EoL GMS Flaws That Could Expose Files, Alter Database Records

**CVE:** `CVE-2026-109593` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-11-04
**Reference:** <https://thehackernews.com/2026/11/sonicwall-wont-patch-eol-gms-flaws-that.html>

> SonicWall has warned of two vulnerabilities impacting end-of-life Global Management System (GMS) systems that it said will not be patched.

Details of the security flaws, which affect SonicWall GMS 9.5.2 and earlier versions, are below -


  CVE-2026-109593 (CVSS score: 9.1) - An unauthenticated file read vulnerability that could allow an attacker with network access to read internal GMS files,

---

## 12. 🟡 High Severity — odf-kit: HTML injection leading to XSS in odtToHtml() and odsToHtml() via unescaped style attribute values

**CVE:** `CVE-2026-113787` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-11-04
**Reference:** <https://github.com/advisories/GHSA-3cgg-c5pp-57h6>

> ### Summary

ODF style attribute values are interpolated into `style=&quot;...&quot;` attributes without HTML-escaping in **both** of odf-kit&#x27;s to-HTML renderers (`odtToHtml` and `odsToHtml`). A double-quote character inside an attacker-controlled style value breaks out of the attribute, allowing arbitrary HTML/attribute injection — and therefore script execution (XSS) — from a crafted `.odt`…

---

## 13. 🟡 High Severity — Google Issues Patches for Critical Android Flaw That Could Allow RCE Without User Interaction

**CVE:** `CVE-2026-58868` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-11-04
**Reference:** <https://thehackernews.com/2026/11/google-patches-critical-android-flaw.html>

> A critical Android flaw could allow an attacker to run code on a phone without any user action remotely, Google said in its November security bulletin.

The flaw, CVE-2026-58868, affects Android 14 through 17. Phones get the fix with security patch level 2026-11-01 or later, which phone makers and carriers send on their own schedules.

As of November 4, Google&#x27;s bulletin did not report

---

## 14. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
