# Zero Day Pulse

> **Generated:** 2026-10-10 20:48 UTC &nbsp;|&nbsp; **Total:** 16 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 7 &nbsp;|&nbsp; 🟡 High: 9 &nbsp;|&nbsp; ✨ Enriched: 0

---

## 1. 🟠 Zero-Day — Improve Router Hygiene to Protect Against Russian State-Sponsored Targeting

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Wed, 08 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a>

> Russian Government-Sponsored Activity Targets Poorly Configured and Vulnerable Devices Across Critical Sectors Executive summary Russian Federal Security Service (FSB) Center 16 cyber actors continue to exploit poorly configured and vulnerable networking devices worldwide, opportunistically compromising multiple critical infrastructure sector networks. This joint Cybersecurity Advisory (CSA) build…

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

## 7. 🟠 Zero-Day — Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite

**CVE:** `CVE-2025-66376` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Tue, 21 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a>

> Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra Collaboration Suite Executive summary A group of Russian state-supported cyber actors has been targeting and compromising various Western government and commercial organizations using the Zimbra Collaboration Suite (ZCS) software since at least July 2025. The Russian state-supported advanced persistent threat …

---

## 8. 🟡 High Severity — Chinese Government-linked Cyber Threat Actors Combine Automated and Hands-on Hacking Tools to Steal Sensitive Data

**CVE:** `CVE-2014-6278` | `CVE-2015-3306` | `CVE-2015-5477` | `CVE-2016-3081` | `CVE-2019-11510` | `CVE-2021-22205` | `CVE-2021-3199` | `CVE-2023-22894` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Tue, 06 Oc
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-281a>

> Advisory at a Glance Title Chinese Government-linked Cyber Threat Actors Combine Automated and Hands-on Hacking Tools to Steal Sensitive Data Original Publication October 8, 2026 Executive Summary Chinese government-linked cyber threat actors, enabled by the Integrity Technology Group, are combining automated scanning tools, large-scale botnets, and hands-on exploitation techniques to target and s…

---

## 9. 🟡 High Severity — Vikunja: Planka migration retains an unbounded aggregate of attacker-served attachments and can OOM the API

**CVE:** `CVE-2026-91970` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-09
**Reference:** <https://github.com/advisories/GHSA-wq92-8x3r-fm38>

> # Planka migration retains an unbounded aggregate of attacker-served attachments and can OOM the API

## Summary

The always-registered Planka migration lets any ordinary user select a Planka server. Although Vikunja caps each JSON response, pagination loop, and attachment independently, it has no aggregate job budget. The conversion stage downloads every advertised non-link attachment and keeps e…

---

## 10. 🟡 High Severity — Vikunja: Any user can enumerate every team and its members by attaching arbitrary teams to a throwaway project

**CVE:** `CVE-2026-91980` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-09
**Reference:** <https://github.com/advisories/GHSA-39p5-2wrr-xh29>

> ### Summary
When you share a project with a team, the API lets you attach any team on the instance, including teams you have nothing to do with, as long as you&#x27;re an admin of the project. Listing a project&#x27;s teams then returns each team&#x27;s full member roster. So any logged-in user can spin up a throwaway project, attach team IDs one by one, and read back the name, description, and co…

---

## 11. 🟡 High Severity — Vikunja: CalDAV and feeds BasicAuth endpoints have no rate limit, bypassing the anti-brute-force floor on account passwords

**CVE:** `CVE-2026-91973` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-09
**Reference:** <https://github.com/advisories/GHSA-m469-88xx-8rx2>

> ### Summary
The `/dav`, `/.well-known`, and `/feeds` groups are registered on the root Echo instance with only BasicAuth and no rate limiter. CalDAV BasicAuth accepts the plain account password, so password guessing over `/dav` is unbounded and never returns 429, while `/api/v1/login` is throttled from the tenth attempt. The only anti-brute-force control on the instance is therefore bypassable.

#…

---

## 12. 🟡 High Severity — Vikunja: Cross-tenant task-position rows can be injected into arbitrary project views via the unvalidated project_view_id in the task position endpoint (v1 and v2)

**CVE:** `CVE-2026-91984` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-09
**Reference:** <https://github.com/advisories/GHSA-w39f-h553-h2mx>

> ## Summary

The task-position endpoint authorizes only the task side of the write: `TaskPosition.CanUpdate` delegates to `Task.CanUpdate` (write access to the task&#x27;s own project) and the request body&#x27;s `project_view_id` is never validated to belong to the task&#x27;s project, nor is any access to that view required. Any authenticated user with a single writable task of their own can pers…

---

## 13. 🟡 High Severity — Vikunja: Read-only project members can obtain any link share's access hash via the single-share read endpoint (v1 and v2) and escalate to the share's permission level

**CVE:** `CVE-2026-91985` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-09
**Reference:** <https://github.com/advisories/GHSA-qfwc-vx6f-3g6g>

> ## Summary

A user who has only read permission on a project can call the single link-share read endpoint and receive the share&#x27;s `hash` field — the secret credential that the anonymous `POST /shares/{share}/auth` endpoint exchanges for a link-share JWT carrying the share&#x27;s permission (read / read-write / admin). A read-only member can therefore mint a write- or admin-level token for the…

---

## 14. 🟡 High Severity — Vikunja: TOTP secret is readable after enrollment, no step-up auth

**CVE:** `CVE-2026-91982` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-09
**Reference:** <https://github.com/advisories/GHSA-88f6-4rjv-x774>

> ### Summary
Once a user has TOTP enabled, the API still hands back the raw shared secret to anyone holding that account&#x27;s access token. Reading it doesn&#x27;t ask for the password, even though disabling TOTP does. So a stolen token, an XSS, or a browser left open is enough to copy the second factor into your own authenticator and keep generating valid codes indefinitely.

### Details
`GET /a…

---

## 15. 🟡 High Severity — Vikunja: Every /api/v2 pre-auth endpoint is unthrottled on a stock install while its /api/v1 twin is rate limited

**CVE:** `CVE-2026-91972` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-10-09
**Reference:** <https://github.com/advisories/GHSA-6rvj-qwjf-3m4q>

> ### Summary
`registerAPIRoutesV2` never applies the unconditional pre-auth rate-limit floor (`unauthRateLimit()`) to the v2 public routes — it passes that limiter only to `/api/v2/ws` — and otherwise relies on `setupRateLimit`, which registers nothing when `ratelimit.enabled` is false (the default). So on a stock install every v2 pre-auth endpoint (login, register, password-reset token, oauth toke…

---

## 16. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
